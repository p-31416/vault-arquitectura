---
tipo: software
fecha_creacion: 2026-10-05
ultima_actualizacion: 2026-10-05
tags: [leantime, pm, agile, kanban, sprints, okrs, mcp, vps, easypanel, estudio, emilia]
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
