---
tipo: software
fecha_creacion: 2026-10-05
ultima_actualizacion: 2026-10-20
tags: [leantime, pm, agile, kanban, sprints, okrs, mcp, jsonrpc, api, vps, easypanel, estudio, emilia]
idioma: es
---

# Leantime

Gestor de proyectos open-source (PHP + MySQL) para equipos ágiles: Kanban, sprints, gantt, milestones, OKRs y wiki. Self-hosted, con/edición gratuita para siempre y versión Cloud. Es el **tablero de tareas del estudio**: ahí vive el flujo `Fathom → specs/ → Leantime` (ver [[wiki/glosario/internal/pbooks/pbk-pm_vault|pbk-pm_vault]]).

Instancia del estudio: `https://pitautech-leantime.3nq4ow.easypanel.host` — EasyPanel en el VPS `pitau.tech`. El panel de EasyPanel vive aparte, en `https://panel.pitau.tech` (cert autofirmado `CN=Easypanel`).

## Índice

- [[#Instalación y arquitectura]]
- [[#MCP Server — conexión desde OpenCode]]
- [[#Credenciales]]
- [[#Diagnóstico 2026-10-05 — MCP leantime caído y reparado]]
- [[#Horas — time tracking]]
- [[#Conceptos relacionados]]
- [[#Referencias]]
## Instalación y arquitectura

- **Servidor**: Leantime 3.10.3+ self-hosted en EasyPanel (VPS), plugin **MCP Server** habilitado, ruta `/mcp` expuesta.
- **URL pública**: subdominio propio de EasyPanel con certificado Let's Encrypt válido (`*.3nq4ow.easypanel.host`) → permite `type: remote` desde cualquier cliente.
- **Puerta de entrada por dominio**: EasyPanel sirve cada app en `https://<servicio>.<id>.easypanel.host`; un dominio propio o certificado autofirmado exige bridge local o `--insecure`.

## MCP Server — conexión desde OpenCode

Leantime 3.10.3+ habla **Streamable HTTP** en `/mcp`: cualquier cliente MCP moderno se conecta directo por HTTP, sin proxy local.

Config canónica en `opencode.json` del vault:

```json
"leantime": {
  "type": "remote",
  "url": "https://pitautech-leantime.3nq4ow.easypanel.host/mcp",
  "headers": { "x-api-key": "{env:LEANTIME_TOKEN}" },
  "enabled": true,
  "timeout": 30000
}
```

Notas operativas:

- La credencial viaja en **header**, nunca en la línea de comando → deja de quedar expuesta en `opencode mcp list` y en la lista de procesos.
- El token en `.env` local; en la config solo `{env:LEANTIME_TOKEN}`.

### El MCP `/mcp` expone 0 tools — la vía real es la API JSON-RPC

Verificado el 2026-10-19: `POST /mcp` responde `initialize` (200, `serverInfo: "Laravel MCP" 1.0.0`) pero `tools/list` devuelve `{"tools":[]}` — **el plugin MCP Server no publica ninguna tool**, aunque el endpoint "funcione" y `opencode mcp list` lo muestre como conectado. Por eso el MCP no sirve para cargar tasks.

La API que sí funciona es **`POST /api/jsonrpc`** con el mismo header `x-api-key`, y los métodos son `leantime.rpc.<Servicio>.<Clase>.<metodo>` (los del *service*, no los del repositorio):

| Necesidad | Método | Notas |
|---|---|---|
| Leer | `Tickets.getAll`, `Tickets.getAllMilestones` (`searchCriteria.currentProject`), `Tickets.getStatusLabels`, `Tickets.getAllSubtasks` (`ticketId`) | `getAll` devuelve `type` real (`task`/`subtask`/`milestone`) |
| Crear card | `Tickets.addTicket` con `values.headline/type/projectId/milestoneid/sprint/status/priority/planHours/dateToFinish/editorId/collaborators/acceptanceCriteria` | `type: 'task'` = card, `type: 'subtask'` + `dependingTicketId` = subtask. `upsertSubtask` **no** funciona por RPC (`parentTicket` llega como array) |
| Crear milestone | `Tickets.quickAddMilestone` con `params.{headline,projectId,dateToFinish,description}` | Se crea con `sprint = 0`; linkear después con `updateTicket` |
| Editar | `Tickets.updateTicket` con **`values.id`** (no `params.id`) | Si falta `id` → `Undefined array key "id"`. `type` y `projectId` **siempre** (sin `type` degrada el milestone a task) |
| Borrar | `Tickets.delete` con `id` | Sí funciona (limpia probes) |
| Proyecto | `Projects.addProject` con `values.{name,details,clientId,type,assignedUsers[{id,projectRole}]}` | `projectRole: ''` no crea relación: usar `Projects.editUserProjectRelations` con `id` + lista completa de `projects` (**reemplaza**, no suma) |
| Sprint | `Sprints.addSprint` con `params.{name,projectId,startDate,endDate}` · `Sprints.editSprint` con `params.id` | No hay método de borrado expuesto: un sprint de prueba se repara con `editSprint` |
| Miembros | `Projects.getUsersAssignedToProject` (`projectId`) · `Projects.getProjectsAssignedToUser` (`userId`) · `Projects.isUserMemberOfProject` | `Projects.addUserToProject` **no** está expuesto por RPC |
| **Horas (timesheets)** | `Timesheets.logTime(ticketId, params)` con `params.{dateString,hours,kind,description}` · `Timesheets.getAll(dateFrom,dateTo)` · `Timesheets.deleteTime(id)` · `Timesheets.upsertTime(ticketId,params)` · `Timesheets.getBookedHourTypes()` | `ticketId` = la tarjeta contra la que se imputa. `kind` **obligatorio** (`GENERAL`, `GENERAL_BILLABLE`, `GENERAL_NOT_BILLABLE`, `PROJECTMANAGEMENT`, `DEVELOPMENT`, `BUGFIXING_NOT_BILLABLE`, `TESTING`). Ver "Horas —.time tracking." abajo |

Límites prácticos: la API tira **429 "Too many requests per minute"** → esperar 20 s y reintentar (el script `scripts/leantime_rpc.py` ya lo hace, con 1,6 s entre llamadas). Los **Goals no están expuestos** por la API: se crean a mano en la UI.

Cliente en el vault: `scripts/leantime_rpc.py` (+ `_notas.md`) y `scripts/carga_leantime_planes_261019.py` (carga de los 2 planes del 19/10).

## Horas — time tracking

Las horas trabajadas se imputan **contra una tarjeta** (o milestone), con fecha, cantidad, tipo y descripción. El método es `Timesheets.logTime(ticketId, params)`, del servicio `Timesheets` (`app/Domain/Timesheets/Services/Timesheets.php`).

Dos trampas medidas el 2026-10-20:

1. **La fecha se desplaza 7 h por RPC.** La instancia corre en UTC+7 y la UI manda hora local; el RPC no. Para que una entrada se lea a las `19:00:00` (la convención del estudio, fin de jornada) hay que mandar `dateString` con `12:00:00`. Mandar `19:00:00` deja la entrada **un día después**.
2. **`logTime` suma, no crea.** Si ya hay una entrada para ese mismo ticket+fecha+tipo, **incrementa las horas** de la fila existente y concatena las descripciones (separador `--`). 2 entradas de 1 h del mismo ticket el mismo día quedan como 1 fila de 2 h.

Cliente en el vault: `scripts/leantime_registrar_horas.py` (+ `_notas.md`) — trae `--dry`, `--verificar` y `--borrar` para el rollback.

## Credenciales

| Tipo | Dónde se genera | Header |
|---|---|---|
| API key (`lt_…`) | Leantime → My Profile → API keys | `x-api-key: lt_…` |
| Personal Access Token | Leantime → My Profile → Personal Access Tokens | `Authorization: Bearer …` |

El vault usa API key (`LEANTIME_TOKEN`). Con `Authorization: Bearer` sobre una API key, Leantime responde `{"error":"Invalid API Key"}` — el prefijo `lt_` delata el tipo y evita esa trampa.

## Diagnóstico 2026-10-05 — MCP leantime caído y reparado

Síntoma: `✗ leantime failed (MCP error -32000: Connection closed)` con 6/7 MCP conectados.

Dos causas encadenadas:

1. **Puente local inexistente** — la config apuntaba a `node …/node_modules/leantime-mcp/bin/leantime-mcp.js`, y ese paquete ya no estaba instalado (lo arrastró una reinstalación de opencode). El proceso moría al instante. El paquete `leantime-mcp` quedó **deprecado oficialmente** ("no longer needed and no longer maintained").
2. **URL equivocada + certificado** — la config usaba `https://pitau.tech/mcp`, que es el **panel de EasyPanel** (cert autofirmado `CN=Easypanel`, sin SAN) y no el MCP de Leantime. Node rechazaba el certificado: `self-signed certificate`.

Diagnóstico (réplica):

```bash
# ¿la URL responde?
node -e "fetch('https://pitautech-leantime.3nq4ow.easypanel.host/mcp').then(r=>console.log(r.status))"   # 401 = existe, pide credencial

# ¿el certificado es válido?
node -e "const t=require('tls'),h='pitautech-leantime.3nq4ow.easypanel.host';const s=t.connect({host:h,port:443,servername:h,rejectUnauthorized:false},()=>{console.log(s.getPeerCertificate().issuer);s.end()})"

# ¿la credencial sirve? (probe JSON-RPC, no imprime el token)
node -e "fetch('https://…/mcp',{method:'POST',headers:{'content-type':'application/json',accept:'application/json, text/event-stream','x-api-key':process.env.LEANTIME_TOKEN},body:JSON.stringify({jsonrpc:'2.0',id:1,method:'initialize',params:{protocolVersion:'2024-11-05',capabilities:{},clientInfo:{name:'probe',version:'0.0.1'}}})}).then(async r=>console.log(r.status,await r.text()))"   # 200 = MCP responde
```

Resultado: `type: local` + puente → `type: remote` + header `x-api-key`. `opencode mcp list` → 7 servers, `✓ leantime connected`.

**Lección para el vault**: `pitau.tech` = panel EasyPanel (cert autofirmado); cada app vive en su propio subdominio `*.easypanel.host` con Let's Encrypt. Para cualquier MCP remoto del VPS, apuntar al subdominio de la app, nunca al dominio raíz del panel.

## Conceptos relacionados

- [[wiki/glosario/software/opencode|opencode]] — donde vive la config MCP del vault
- [[wiki/glosario/conceptos/agile-arquitectura|agile-arquitectura]] — sprints y Ceremonias, y su implementación en Leantime
- [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]] — Leantime como implementación operativa del meta arquitecto
- [[wiki/glosario/internal/pbooks/pbk-pm_vault|pbk-pm_vault]] — playbook PM: tasks/subtasks/sprints/milestones/OKRs, Kanban + LPS
- [[wiki/glosario/internal/pbooks/pbk-config_ctas_git_github_opencode|pbk-config_ctas_git_github_opencode]] — capa OpenCode y secretos vía `{env:}`
- [[wiki/estudio/adrs/ADR-INFRA-001-leantime-selfhosted|ADR-INFRA-001 Leantime self-hosted]]
- [[specs/260929-alta-emilia-leantime|spec 260929 — alta Emilia en Leantime]]
- [[specs/260909-agente-reuniones-fathom-specs|spec 260909 — agente reuniones Fathom → specs → Leantime]]

## Referencias

- Docs oficiales MCP Server: https://docs.leantime.io/#/installation/leantime-mcp (200, 2026-10-05)
- Plugin MCP Server (marketplace): https://marketplace.leantime.io/product/mcp-server/ (200, 2026-10-05)
- `leantime-mcp` (bridge deprecado): https://github.com/leantime/leantime-mcp (200, 2026-10-05)
- Producto y planes: https://leantime.io/pricing (200, 2026-10-05)
