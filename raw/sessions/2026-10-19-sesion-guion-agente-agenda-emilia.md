---
tipo: log
fecha: 2026-10-19
tags: [sesion, n8n, agente-voz, agenda, cal-com, google-calendar, miercoles, studio-os]
---

# Sesión 2026-10-19 — guion del miércoles: agente de agenda de Emilia

## Qué se hizo

- Decisiones de Sol tomadas esta sesión: **concurso ya inscripto** (Sol + Emilia) con **entrega 16/12/2026** ·
  carril del concurso en **proyecto Leantime propio** `Proyecto Pi — Gaudí Nexus` (fuera del contrato
  Studio OS × Emilia) · foco operativo en **configurar el agente de Cal.com + Calendar de Emilia**.
- Levantamiento del estado real de n8n por MCP (`N8N_MCP_TOKEN` del `.env`, JSON-RPC sobre
  `https://n8n.pitau.tech/mcp-server/http`): lista de 26 workflows, 28 credenciales y los parámetros
  completos de los 3 workflows del camino de agenda.
- Escrito `proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia.md`: documento operativo
  de la cita presencial del miércoles 21/10 13:00.
- **Carga a Leantime ejecutada** (ver sección propia más abajo): 33 cards + 85 subtasks + 10 milestones +
  2 sprints + 1 proyecto nuevo.

## Estado real verificado (19/10)

| Workflow | ID | Estado | Rol |
|---|---|---|---|
| OS-Studio — Agent Voz TEST (revision) | `Gpd6NHB4HQdU7ary` | activo (perfil Sol) | agente principal, 26 nodos |
| OS-Studio — Agenda Sub TEST | `ygdjqRfXpxKMFWEN` | activo (perfil Sol) | subagente ejecutor de Cal.com, 12 nodos |
| OS-Emilia — Telegram Router | `YWpuV5p0vCDTbIHz` | activo | trigger único del token + ruteo |
| OS-Emilia — Fathom Core | `UeDkqVZSeLnae5cF` | activo | sync diario 07:00 AR |

**Credenciales clave:** `ppi-EmiliaOS_Cal.com.Bearer Auth account` (`3MvZXPNH8LrDYPZS`, **ya existe**),
`ppi_calcom-Bearer Auth account` (`60SFxvMa6AaqmWWi`, la que usa hoy el Agenda Sub TEST),
`Cal.com API Key` (`zdNucNjAM21guAuR`, Sol), `Google Calendar account` (`3wo33TixNfgYPeJY`, hoy apunta a
`proyectopi.31416@gmail.com`), `emiliaospi_bot-Telegram account` (`PqGQSTIshKSriHOm`),
`ppi-EmiliaOS_Google Sheets account` (`yb1G3uAHS2QqK1wu`), `Postgres account` (`mmwdgjWdYmF7aBUe`),
`Redis account` (`dySiFumFmvckOGdn`), `OpenRouter account` (`F3k0GtQqqEJqBGjl`),
`Google Gemini(PaLM) Api account` (`ST3rNoKVMZGOSppJ`).

**Constantes a cambiar en el clon (hoy hardcodeadas para Sol):** allowlist `8459099332` en `Detectar Entrada` ·
key Redis `studio_os_test_8459099332` (3 nodos) · tabla Postgres `studio_os_test` · `chatId` fijo `8459099332`
en `Responder Telegram` · `eventTypeId 7467793` en `obtener_reuniones` · `calendar = proyectopi.31416@gmail.com`
en `leer_calendario` · `metadata.origen = OS-Studio-TEST` · `cal-api-version` 2024-08-13 (bookings) y
2024-09-04 (slots).

## Las 3 claves a pedirle a Emilia (miércoles)

1. **API key de Cal.com v2** de su cuenta → a la credencial `ppi-EmiliaOS_Cal.com` (que ya existe).
2. **Autorización OAuth de Google Calendar** desde la UI de n8n con su cuenta → credencial nueva
   `emilia-Google Calendar` (la actual pertenece a la cuenta de Sol y queda intacta).
3. **Definición de sus calendarios** + **evento de 60 min con Meet** en Cal.com → define el campo *Calendar*
   de `leer_calendario` y el `eventTypeId` de `obtener_reuniones`.

El `chat_id` de Emilia no se pide: se lee de la ejecución del Router cuando ella escriba al bot.

## Hallazgos

- **La credencial de Cal.com de Emilia ya existe** en n8n desde el 24/09 (`3MvZXPNH8LrDYPZS`, ligada al
  `Create Cal.com Booking` del Core archivado). El trabajo del miércoles es verificar que apunte a su cuenta
  y, si hace falta, reemplazar el token.
- **Clonar en vez de un agente con perfiles:** la credencial n8n no admite expresiones, así que un agente
  con dos perfiles obligaría a duplicar las 7 tools de agenda detrás de un Switch — el mismo costo de
  mantenimiento que clonar, con más riesgo de cruce. Se mantiene 1 agente + 1 subflujo por persona.
- **`Responder Telegram` tiene el `chatId` fijo** en el `chatId` de Sol: sin cambiarlo, la respuesta le
  llega al chat equivocado aunque todo lo demás funcione.
- **Trigger duplicado = incidente conocido (13-14/10):** el clon conserva solo `executeWorkflowTrigger`;
  el trigger Telegram sigue siendo único en el Router.
- **La API de Cal.com responde 403 (Cloudflare 1010) desde esta PC**, así que la verificación de la key
  queda para la sesión, corriendo desde la instancia n8n.
- **Tool set para "manejar todos los datos":** el set de 7 cubre agendar/mover/cancelar/listar; se suman
  `listar_bookings` (todas las reuniones de la cuenta, sin filtrar por `eventTypeId`) y el cruce de
  disponibilidad de Cal.com con los eventos del Google Calendar, con deduplicación por fecha+título.

## Carga a Leantime (hecha)

**Hallazgo de fondo:** el MCP de Leantime (`/mcp`) responde `initialize` pero **`tools/list` devuelve
`tools: []`** — el plugin MCP Server no publica ninguna tool, aunque `opencode mcp list` lo muestre
conectado. La vía que sí funciona es la **API JSON-RPC** `POST /api/jsonrpc` con el mismo header
`x-api-key` y métodos `leantime.rpc.<Servicio>.<Clase>.<metodo>` — la misma que el vault ya usó para los
milestones 443-457 del 13/10.

Cliente nuevo: `scripts/leantime_rpc.py` (+ `_notas.md`) y `scripts/carga_leantime_planes_261019.py`
(+ `_notas.md`).

**Resultado:**

| | Proyecto 4 `O.S_ARQ-Emi` | Proyecto 6 `Proyecto Pi - Concurso Gaudi Nexus` (nuevo) |
|---|---|---|
| Sprint | 27 · `S1 Agentes + agenda Emilia (19/10-23/10)` | 28 · `S1 Bases + primer flujo (19/10-23/10)` |
| Milestones | 461-464 (M-A1 a M-A4) | 537-542 (M-B1 a M-B6, M-B6 = entrega 16/12) |
| Cards | 20 (ids 465-533) | 13 (ids 543-585) |
| Subtasks | 52 | 33 |
| `planHours` | 45,52 h | 29,59 h |
| Miembros | Emilia + Pitau Tech | Emilia + Pitau Tech |

Total: **10 milestones, 33 cards, 85 subtasks, 75,11 h planificadas**, 0 cards sin subtasks, 0 subtasks
huérfanos. Estado final en `raw/reuniones/leantime-carga-261019-estado.json`.

**Aprendizajes de la API (documentados en `wiki/glosario/software/leantime`):**

- El id creado viene como **array de 1 elemento** (`[458]`), no como entero.
- `updateTicket` exige **`values.id`** (no `params.id`) → si falta, `Undefined array key "id"`.
- `updateTicket` **siempre con `type` + `projectId`**: sin `type` degrada el milestone a task (lección del 13/10).
- Los subtasks se crean con `addTicket` + `type: 'subtask'` + `dependingTicketId`; **`upsertSubtask` no
  funciona por RPC** (`parentTicket` llega como array → `Attempt to read property "projectId" on array`).
- `quickAddMilestone` crea el milestone con `sprint = 0` → linkear después con `updateTicket`.
- `addProject` con `assignedUsers` **no** crea la relación de membresía: la vía es
  `Projects.editUserProjectRelations` con `id` + lista **completa** de proyectos (reemplaza, no suma).
- `Projects.addUserToProject` y `Tickets.delMilestone` **no** están expuestos por RPC; `Tickets.delete` sí.
- La API tira **429 por minuto** → 1,6 s entre llamadas y 20 s de espera al reintentar.
- Los **Goals no están expuestos** por la API: siguen siendo carga manual en la UI.

## Archivos

- **Nuevo:** `proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia.md` ·
  `scripts/leantime_rpc.py` + `scripts/leantime_rpc_notas.md` ·
  `scripts/carga_leantime_planes_261019.py` + `scripts/carga_leantime_planes_261019_notas.md` ·
  `raw/reuniones/leantime-carga-261019-estado.json`.
- **Editado:** `specs/261019-plan-concurso-gaudi-nexus-ia.md` (M-B1 cerrado, M-B6 = 16/12, tablero propio,
  preguntas 1/2/3/5 resueltas) · `specs/261019-plan-agentes-telegram-agenda-emilia.md` (task C1b nueva,
  D2 a 3 pom, 20 cards, M-A2 y preguntas 3/7 con enlace al guion) · `wiki/glosario/software/leantime`
  (sección "El MCP /mcp expone 0 tools — la vía real es la API JSON-RPC") · `log.md`.
- **Fuera de git:** el JSON de workflows con parámetros se leyó por MCP y quedó en temp; el vault solo
  guarda nombres e IDs públicos de credenciales, nunca secretos.

## Queda

- **Goals en Leantime**: crear a mano en la UI y linkear los milestones nuevos (M-A2, M-A3 en el proyecto 4;
  M-B1 a M-B6 en el 6) — la API no expone Goals.
- Ejecutar la sesión del miércoles y volcar los IDs de los 2 workflows clonados en §9 del documento.
- Guardar el comprobante de la inscripción del concurso y volcar los plazos a la agenda (E1.3, F1.2).
