---
tipo: documentacion
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha: 2026-10-16
version: 2.0
tags: [n8n, automatizacion, fathom, telegram, drive, studio-os, referencia-tecnica]
---

# Arquitectura n8n — OS-Emilia · referencia nodo por nodo

> v2.1 — Actualizado el **2026-10-21**: cada persona tiene su propio flujo de agente de voz y su propio subagente de agendamiento, con un `Voz Dispatcher` que reparte por `chat_id` (§0 y §5.b).
>
> v2.0 — Estado verificado el 2026-10-16 por API (MCP `n8n-mcp`, `get_workflow_details` full de los 6 workflows). Reemplaza v1.3: los Cores Agenda/Cancel/Modif por comandos (`UTkII2kd3RHDlizo`, `B7gGFGcD89vKfc5k`, `c08s62Lo9EmAEJJf`) culminaron su ciclo y ya no existen en la instancia; el camino principal es el agente de voz/texto en lenguaje natural. El Router solo conserva `/sync` + `/help`. Para el manual de uso ver `playbook-os-emilia-n8n.md` v2. Fuente de diseño original: `specs/260924-plan-os-emilia-n8n.md`.

## 0 · Mapa en 1 tabla (vigente 21/10)

> **v2.1 (21/10):** cada persona tiene **su propio flujo** de agente de voz y **su propio subagente de agendamiento**. Un `Voz Dispatcher` reparte por `chat_id`. Los workflows "nuevos" de la v2.0 son copias de los de Sol con identidad propia (Redis, memoria, credencial de Cal.com y prompt distintos).

| Workflow | ID n8n | Trigger | Nodos | Estado 21/10 | Función en 1 línea |
|---|---|---|---|---|---|
| Fathom Core | `UeDkqVZSeLnae5cF` | Schedule 07:00 AR + ExecuteWorkflowTrigger | 13 | activo | Lee Fathom (26h) → `.md` a Drive → Google Doc formateado |
| Telegram Router | `YWpuV5p0vCDTbIHz` | Telegram Trigger (message + callback_query) | 17 (13+4 stickies) | activo | Identidad → Voz Dispatcher / Inbox Fuentes (grupo) / `/sync` + `/help` |
| **Voz Dispatcher** | `Msh31moofBKBwZId` | ExecuteWorkflowTrigger (lo invoca el Router) | 5 | activo | Saca el `chat_id` → `8459099332` va al flujo de Sol, el resto al de Emilia |
| Agent Voz TEST | `Gpd6NHB4HQdU7ary` | ExecuteWorkflowTrigger (`Voz Agent Trigger`) | 26 | activo (perfil **Sol**) | Voz/texto → STT → lote Redis `studio_os_test_8459099332` → Agent + memoria Postgres + tools |
| **Agent Voz Emilia** | `Fa2AlIDqUntSWMrw` | ExecuteWorkflowTrigger (`Voz Emilia Trigger`) | 23 | activo (perfil **Emilia**) | Igual, con Redis `studio_os_emilia_<chat_id>`, memoria `studio_os_emilia` y su propio prompt |
| Agenda Sub TEST | `ygdjqRfXpxKMFWEN` | ExecuteWorkflowTrigger (lo invoca el Agent Voz de Sol) | 12 | activo (Sol) | Agente ejecutor + 6 tools Cal.com (ET `7467793`) + Google Calendar |
| **Agenda Sub Emilia** | `2JogeOoT3Wjq2ncH` | ExecuteWorkflowTrigger (lo invoca el Agent Voz de Emilia) | 11 | activo (Emilia) | 7 tools Cal.com sobre **su** cuenta (ET `7563141` presencial / `7563142` online / `7563143` libre) + su Calendar |
| SET_01 Cuadro carpinterías | `VIQmMEZ9tkDBfKjd` | Webhook `POST /set01-carpinterias` | 12 | activo | Cuadro CAD → planilla `SET_01-REP-carpinterias` en Drive |
| Limpiar Memoria TEST | `uOonS1LWzowvwyns` | Manual | 6 | inactivo | Borra sesión Postgres + Redis del agente |

Antecedentes que ya no existen (referencia histórica, no borrar de git): Agenda Core `UTkII2kd3RHDlizo`, Cancel Core `B7gGFGcD89vKfc5k`, Modif Core `c08s62Lo9EmAEJJf`, Fathom Cron `2gUlVXu7xk1Jd12s` (trigger absorbido por el Core), Format Google Doc `LysH41yu1s5wXkPz` (cadena inline en el Core), Agenda Dispatcher `CVvxZgn0AipO6dV0` (intermedio del 20/10, archivado el 21/10).

```
Recibo Mensaje (único trigger del token)
└─ Route Identidad (chat.id)
   ├─ Sol 8459099332 → Run Voz Agent → Voz Dispatcher
   └─ resto → Route Fuentes Group (chat.id == -5417177870)
      ├─ link (contains http) → Prepara Fila → Extrae Jina → Parsea Info → Append Sheet → Ack "Anotado ✓"
      └─ resto → Route Telegram Command
         ├─ /sync → Fathom Core
         ├─ /help → Send Help
         └─ chat de Emilia (regla 2) → Run Voz Agent → Voz Dispatcher
Voz Dispatcher (chat.id)
├─ 8459099332 → Agent Voz TEST (Sol)   → Tool Agenda → Agenda Sub TEST  → Cal.com de Sol
└─ resto      → Agent Voz Emilia        → Tool Agenda → Agenda Sub Emilia → Cal.com de Emilia
Schedule 07:00 AR ──► Fathom Core ──► Fetch (26h) → Split → BuildDoc → BuildReq → Classify ──► Save .md ──► Create Doc → Move → Apply formato
Webhook CAD ──► SET_01 ──► Busca/Crea planilla → matriz → escribe rango → mueve a W03-CAD
Drive (.md) ──► vault (import_drive_reuniones.py)
```

> **Pendiente de cargar (21/10):** el `chat_id` real de Emilia, con el placeholder `999999999` en 2 lugares (Router → regla 2 `rightValue`; `Detectar Entrada Emilia` → `PERMITIDO`). Después, **publicar** las 2 versiones.

Data Table `OS-Emilia — Bot State` (`2YgepkPbLD3s4Nu9`) creada, conexión fase 2 para dedup total (ver §6).

## 1 · Fathom Core — `UeDkqVZSeLnae5cF` (13 nodos, sin cambios desde 09/10)

Dos triggers alimentan `Fetch Fathom Meetings`: `Daily Fathom Sync 07:00` (cron diario, timezone workflow `America/Argentina/Buenos_Aires`, servidor en UTC) y `Fathom Core Trigger` (llamadas de `/sync` y del Agent Voz, con `source` informativo). Después del Classify, ambas ramas confluyen en una cadena compartida de Docs (pairing nativo `$('Classify Meeting').item`).

| # | Nodo | Tipo / credential | Qué hace |
|---|---|---|---|
| 0a | Daily Fathom Sync 07:00 | `scheduleTrigger` | Disparo diario 07:00 AR |
| 0b | Fathom Core Trigger | `executeWorkflowTrigger` (`source` opcional) | Entrada para `/sync` (Router) y Tool Fathom (Voz) |
| 1 | Fetch Fathom Meetings | `httpRequest` · `ppi-EmiliaOS_Fathom` (`mAaHtYoCUcSj0via`) | `GET https://api.fathom.ai/external/v1/meetings` con `include_transcript/summary/action_items=true` + `created_after = {{ $now.minus({ hours: 26 }).toISO() }}`. Solo lo del último día (ventana 26h, 2h de solape). Backfills con corrida manual y ventana ampliada |
| 2 | Split Meetings | `splitOut` (`fieldToSplitOut: items`) | 1 item por reunión |
| 3 | Build Meeting Document | `code` | Arma `fileName`, `document` (`.md` completo), `summaryDocument` (sin transcript), `folder`, `folderId`, `needsReview`. Detalle en §2 |
| 4 | Build Google Docs Requests | `code` | markdown → `plainText` + array `requests` (insertText, títulos, bullets, negritas, links); devuelve `batchUpdate: { requests }`, `docTitle` |
| 5 | Classify Meeting | `if` (`$json.folder` equals `clientes`) | Rama clientes (true) vs internas (false) |
| 6a | Save Client Meeting | `googleDrive` · `ppi-EmiliaOS_Google Drive` (`F5AzgwsgpCsEth7M`) | `createFromText` en `Reuniones-Clientes` (`1l7EHaiKJQfKcatPkDCnYkkrCjHiqbNN5`), `=$json.fileName`, `=$json.document` |
| 6b | Save Internal Meeting | `googleDrive` · misma Drive | Idem en `Reuniones-Internas` (`1n5mkPNdHhgFEsYfLmx3LYD4sIUiHDtcQ`) |
| 7 | Create Google Doc | `googleDocs` · `Google Docs account` (`kdQydeePwlZbNbkY`) | `title = $('Classify Meeting').item.json.docTitle`, `folderId = $('Classify Meeting').item.json.folderId` |
| 8 | Move Google Doc to Folder | `googleDrive` · `ppi-EmiliaOS_Google Drive` | Mueve el Doc (`$json.id` de Create) al `folderId` del Classify |
| 9 | Apply Google Docs Formatting | `httpRequest` · Docs OAuth | `POST .../documents/{{ $json.id }}:batchUpdate`, `jsonBody = {{ JSON.stringify($('Classify Meeting').item.json.batchUpdate) }}` |

Versión activa `ffd071f6` (09/10). Cron con success diario incl. 16/10 (execs 3564→3772, 26 totales).

## 2 · Lógica del builder (`Build Meeting Document`)

```js
// Fuentes: calendar_invitees[] + transcript[].speaker + recorded_by
sideOf(nombre, email) → 'emilia' | 'proyectopi' | 'externo'
// emilia: mail interno o nombre con emilia/pimenta/lombardi
// proyectopi: mail/nombre con proyectopi, proyecto-pi, maria-sol, azcona
sides = unión deduplicada por lado (nombres + mails)
hasExternal = existe lado 'externo'
needsReview = sin invitados Y sin hablantes
folder      = hasExternal ? 'clientes' : 'internas'   // cero señal → internas + [revisar]-
folderId    = internas ? '1n5mkPNdHhgFEsYfLmx3LYD4sIUiHDtcQ'
                       : '1l7EHaiKJQfKcatPkDCnYkkrCjHiqbNN5'
slug        = sin externos ? lados internos ('emilia-proyectopi')
            : lados internos + hasta 2 externos
            // ej internas: 2026-09-24_emilia-proyectopi_186596516.md
            // ej clientes: 2026-10-03_emilia-vanessa-ferreira-leticia-gentilini_189333562.md
fileName    = ([revisar]-) + YYYY-MM-DD + _ + slug + _ + recording_id + .md
```

El `.md` lleva: título, Fecha, Recording ID, URL, Participantes, Invitados calendario (con mails), Hablantes (con conteo), Grabado por, Clasificación, Resumen, Action items, Transcripción. `summaryDocument` es lo mismo sin transcript (para el Google Doc).

> Nota: `calendar_invitees_domains_type` de Fathom no es confiable (devuelve `one_or_more_external` aun con un solo invitado interno) — no se usa.

## 3 · Telegram Router — `YWpuV5p0vCDTbIHz` (17 nodos, verificado 16/10)

Trigger `Recibo Mensaje` (`telegramTrigger`, cred `emiliaospi_bot` `PqGQSTIshKSriHOm`, `message` + `callback_query`, sin filtro: todo entra por acá) → `Route Identidad` (`String(chat.id) == 8459099332`, Sol) → `Run Voz Agent` (invoca `Gpd6NHB4HQdU7ary` con `update` completo); resto → `Route Fuentes Group` (`String(chat.id) == -5417177870`, grupo Fuentes) → `Has Link` (`text contains "http"`) → `Prepara Fila` (Set: fecha AR, de Sol/nombre, link por `entities[0]`, tipo YT/IG/SHARE/LIBRO/WEB, nota) → `Extrae Jina` (`GET https://r.jina.ai/<link>`, 30s timeout, retry + continue-on-error) → `Parsea Info` (Code: título hasta 140 chars, tags hasta 8) → `Append Fuentes Sheet2` (Sheets `18iDrvNUOApNFsEDDQ4rMMo40cw4t0hn3CApLK9iLpvI`, hoja `Fuentes-Inbox`, columnas Fecha/De/Link/Tipo/Título/Estado/Destino/Nota/Tags, Estado `pendiente`) → `Ack Fuente Guardada` ("Anotado ✓ <tipo> (<nota>)"). Texto sin link en el grupo: salida muda (no guarda). Resto fuera del grupo → `Route Telegram Command` (Switch, case-insensitive): `equals /sync` → `Run Fathom Sync` (`source: telegram`); `equals /help` → `Send Help`; fallback extra → `Send Help`.

Texto de ayuda vigente: *"Hablame en privado con voz o texto para agendar. Links al grupo Fuentes. Comandos: /sync (sincroniza reuniones), /help (esta ayuda)."*

4 stickies: Entrada (único trigger del token) · Identidad · Inbox Fuentes · Comandos legacy (antecedente: no borrar).

**Regla de oro verificada 13-14/10:** 1 trigger por token — un segundo trigger le roba el webhook. El Agent Voz TEST vive detrás del Router (ExecuteWorkflowTrigger), así conviven sin robarse el webhook.

## 4 · Agent Voz TEST — `Gpd6NHB4HQdU7ary` (26 nodos, camino principal)

`Voz Agent Trigger` (recibe `update` del Router) → `Detectar Entrada` (Code: clasifica `audio`/`texto`/`callback`/`otro`, allowlist `8459099332` Sol, resto → `rechazado`) → `Tipos Entrada` (Switch) → rama audio: `Descargar Voz` (Telegram file:get) → `Transcribir Voz` (Gemini `gemini-2.5-flash-lite`, cred `Google Gemini(PaLM) Api`); rama texto: `Fijar Texto Escrito`; rama callback: `Sintetizar Callback` (`/cancel <uid>` desde `cancel:<uid>`) → `Normalizar W02` (`{texto, nombre, ID}`) → `Fijar Contexto` (`TXT_Mensaje/ID_Chat/Nickname`) → `Guardar Mensaje` (Redis push `studio_os_test_8459099332`) → `Esperar Lote` (Wait 12s, absorbe ráfagas) → `Recuperar Lote` (Redis get) → `Es Ultimo Mensaje` (solo el último sigue, resto obsoleto) → `Armar Lote` (join `\n`) → `Limpiar Lote` (Redis delete) → `Agente Voz TEST` (Agent + `Modelo Free TEST` OpenRouter `openai/gpt-5.6-luna` + `Memoria Postgres TEST` tabla `studio_os_test` por `chat.id`, ventana 10) → `Responder Telegram` (mismo `chat_id`, `appendAttribution false`).

Tools del agente: `Tool Agenda` (→ Agenda Sub TEST, query en lenguaje natural) · `Tool Sincronizar Fathom` (→ Fathom Core, `source: telegram-voz-test`) · `buscar_contacto` (SheetsTool read `clientes-contactos` `1t9-j_7gJypLOicaJNpwYWLsBy0VDtSmdBJZumW8jtVA`, match insensible a mayúsculas/acentos/parcial) · `agregar_contacto` (SheetsTool append, alta `nombre+email+activo Sí` tras verificar duplicado).

System prompt vigente: fecha HOY AR, rioplatense 2-3 líneas, 1 pregunta por vez; ante agendar PRIMERO `buscar_contacto`; nunca propone horario sin validar slots con Tool Agenda; email siempre obligatorio; antes de escribir muestra resumen y pide Confirmar; de voz cita lo entendido.

> Convivencia: el TEST está `activo` detrás del Router; NO crear un Telegram Trigger propio en este workflow (le robaría el webhook al Router). Stickies del canvas lo marcan como borrador en revisión: perfil Sol hasta validar, perfil Emilia en M4.

## 5 · Agenda Sub TEST — `ygdjqRfXpxKMFWEN` (12 nodos, ejecutor)

`Agenda TEST Trigger` (recibe `query` en lenguaje natural) → `Agente Agenda TEST` (Agent + `Modelo Agenda TEST` OpenRouter `openai/gpt-5.6-luna` + `Memoria Agenda TEST` BufferWindow por `$execution.id`, sin estado entre llamadas) con 7 tools: `consultar_disponibilidad` (GET `/v2/slots`, SIEMPRE antes de agendar) · `obtener_reuniones` (GET `/v2/bookings`, `eventTypeId 7467793`, para Ref y listados) · `agendar_online` (POST booking, videollamada del evento) · `agendar_presencial` (POST booking con `location` en texto plano) · `actualizar_reunion` (POST `/bookings/<uid>/reschedule`, solo horario; cambio de duración = cancelar + reagendar) · `cancelar_reunion` (POST `/bookings/<uid>/cancel`) · `leer_calendario` (Google Calendar `proyectopi.31416@gmail.com`, incluye eventos manuales).

Cred Cal.com: `ppi_calcom-Bearer Auth` (`60SFxvMa6AaqmWWi`), header `cal-api-version: 2024-08-13` (slots `2024-09-04`). Evento `7467793` (`Reunión Semanal`, duraciones 30/60/180, Meet por defecto, Working hours Lun-Vie 9-17). Horario AR `America/Argentina/Buenos_Aires`; los horarios Google con `-03:00` se copian tal cual, solo los `Z` se convierten. Revisión de agenda: consulta ambas fuentes (bookings + calendario), une por fecha, deduce duplicados fecha+título, solo `accepted` cuenta.

> **Perfil Emilia: ya no es un perfil de este workflow.** Desde el 21/10 tiene flujo propio (§5.b). Este quedó solo para Sol: su `Tool Agenda` volvió a apuntar directo acá (sin el dispatcher intermedio) y su clave Redis volvió a `studio_os_test_8459099332` (así `Limpiar Memoria TEST` sigue funcionando).

## 5.b · Flujos de Emilia — `Fa2AlIDqUntSWMrw` (23) + `2JogeOoT3Wjq2ncH` (11) + `Msh31moofBKBwZId` (5)

**Por qué un flujo por persona.** El bot es uno solo, pero cada persona necesita **sus** datos: claves Redis, memoria, credencial de Cal.com y prompt. Con un único agente de voz, la credencial de Cal.com era de una sola persona → el otro agendaba en la cuenta ajena. La solución: **dos copias del agente de voz** (misma estructura, parámetros distintos) y un **despachador** que decide por `chat_id` *antes* de entrar al flujo. El aislamiento real queda porque **la credencial de Cal.com vive dentro de cada subagente de agenda**, no en el agente.

**`Voz Dispatcher` (`Msh31moofBKBwZId`, 5 nodos):** `Voz Dispatcher Trigger` (recibe `update`) → `Parsea Chat` (Code: saca `chat.id` y **conserva el `update` original** en el item — si no, el flujo destino recibe `undefined`) → `Elige Voz` (Switch: `== 8459099332` → `Run Voz Sol`; `!=` → `Run Voz Emilia`) → 2 `executeWorkflow` con `waitForSubWorkflow`.

**`Agent Voz Emilia` (`Fa2AlIDqUntSWMrw`, 23 nodos):** misma cadena que el de Sol (`Detectar Entrada` → `Tipos Entrada` → ramas audio/texto/callback → `Normalizar W02` → `Fijar Contexto` → Redis push → Wait 12 s → Redis get → `Es Ultimo Mensaje` → `Armar Lote` → Redis delete → `Agente Voz Emilia` → `Responder Telegram Emilia`), con:
- allowlist: **solo su chat** (`const PERMITIDO = 999999999` → *pendiente: su `chat_id` real*), comparado con `String()` para no depender del tipo del id
- Redis: `studio_os_emilia_{{ $('Fijar Contexto Emilia').item.json.ID }}` (dinámica → no hace falta conocer el id)
- memoria Postgres: tabla `studio_os_emilia`, sesión por `chat.id`
- `Tool Agenda Emilia` → `2JogeOoT3Wjq2ncH` (directo)
- `Tool Fathom Emilia` → Fathom Core con `source: telegram-voz-emilia`
- credenciales: bot `emiliaospi_bot`, Sheets `ppi-EmiliaOS_Google Sheets` (la planilla `clientes-contactos` es compartida con Sol)

**`Agenda Sub Emilia` (`2JogeOoT3Wjq2ncH`, 11 nodos):** `Agenda Emilia Trigger` → `Agente Agenda Emilia` (OpenRouter `openai/gpt-5.6-luna` + BufferWindow) con las 7 tools. Cambios frente al de Sol:
- cred Cal.com `ppi-EmiliaOS_Cal.com` (`3MvZXPNH8LrDYPZS`)
- `eventTypeId` **fijo por tool** → `7563142` online · `7563141` presencial · `7563143` libre (el LLM no puede inventar IDs)
- `agendar_presencial` **sin `location`**: la dirección la hereda del event type → se actualiza en un solo lugar
- `leer_calendario` sobre `arq.emiliapimentalombardi@gmail.com` (funciona cuando ella comparte su calendario con `proyectopi.31416@gmail.com`)
- las descripciones de las tools enumeran los 3 IDs válidos

**Eventos de Emilia en Cal.com:** `7563141` presencial (`address`, 60 min, aviso 120) · `7563142` online Meet (60 min, aviso 120) · `7563143` libre (Meet, oculto, aviso 0) · schedule `2527411` "Disponibilidad 24/7" (creado, **sin asignar**). Su Google Calendar **ya estaba conectado** en Cal.com (`credentialId 2605522`) → las reservas caen en su calendario y Cal.com le resta sus ocupados.

**Pruebas (21/10):** el Dispatcher enrutó el chat de Emilia a su flujo → el agente llamó `Tool Agenda Emilia` y respondió con **su** Cal.com; con el chat de Sol enrutó a su flujo y **el bot le envió un Telegram real** (`message_id 277`).

> Nota de API: la versión que expone `/v2/event-types` es `cal-api-version: 2024-06-11` (con `2024-08-13` da **404**) y su body usa `length` (no `lengthInMinutes`); además **ignora** `metadata.multipleDuration` y `scheduleId` → las duraciones 120/180 y el schedule 24/7 se cargan en la **UI de Cal.com**.

## 6 · SET_01 Cuadro carpinterías — `VIQmMEZ9tkDBfKjd` (12 nodos, activo)

`Recibe cuadro` (Webhook `POST /set01-carpinterias`) → `Busca planilla` (Drive search `SET_01-REP-carpinterias`) → `Existe planilla` (IF): existe → `Limpia hoja` → `Arma matriz` → `Escribe rango` (`PUT sheets.googleapis.com/.../cuadro!A1:H100`); no existe → `Crea planilla` (locale `es_AR`, hoja `cuadro`) → `Busca carpeta` (`W03-CAD`) → `Mueve a carpeta` → `Limpia hoja nueva` → `Arma matriz nueva` → `Escribe rango nueva`. Matriz de 8 columnas: `categoria,bloque,tipo_id,ancho_m,altura_m,alfeizar,descripcion,cantidad`. Re-posteable sin duplicados (limpia antes de escribir). Producción: `https://n8n.pitau.tech/webhook/set01-carpinterias`.

## 7 · Caveats y pendientes (16/10)

1. **Sin dedup por `recording_id` (mitigado):** el filtro `created_after` 26h corta duplicados de raíz en el cron diario; queda solape de 2h (1 reunión como máximo). Fix fase 2: Data Table `Bot State`. El import al vault es inmune (idempotente por `call_id`). Dedup dual Emilia+PPI: por fecha/hora+título+participantes, nunca por ID (dual 17/09 genera 2 `recording_id`).
2. **Voz TEST en perfil Sol:** allowlist `8459099332`, cred Cal.com Sol, sheet `clientes-contactos` real compartida, carpetas Drive Emilia (no probar sync en vivo hasta perfil Sol en Drive). Pendientes stickies: `eventTypeId` propio (resuelto: `7467793`), carpeta `OS-Sol`, Data Table `OS-Bot-Profiles`, cred Telegram `emiliaospi_bot` en los 3 nodos Telegram.
3. **Agente Emilia (Mes 2):** API key Cal.com de SU cuenta + evento 60 min con Meet · su `chat_id` (manda `/start`) · agregarla al grupo Fuentes (grupo `-5417177870`) + compartir Sheet `Fuentes-Inbox` · Fathom PPI (cred Header `ppi-PPI_Fathom`, cron dual de 1 cron con 2 ramas Fetch, §9 v1.3 archivado como diseño).
4. **Router sin filtro global a propósito:** el filtro vive en `Route Identidad` (Sol→Voz) y `Route Fuentes Group` (grupo→inbox); cerrar el resto cuando Emilia mande `/start`.
5. **Modelo del Voz:** hoy `openai/gpt-5.6-luna` (pago mínimo, auditable por `usage`); swap free documentado en el spec del MVP_06 como alternativa.

## 8 · Cómo probar

- **Fathom manual:** MCP `execute_workflow` (`UeDkqVZSeLnae5cF`, `executionMode: production`) → `search_workflow_executions` → `get_workflow_execution` con `includeData`. Ver `.md` nuevo en `G:\Mi unidad\OS-Emilia\Reuniones-*/`.
- **Telegram (seguro):** `/help` (no toca Fathom/Drive) → `/sync` (corre el Core real) → 1 link al grupo Fuentes (fila nueva en `Fuentes-Inbox` + "Anotado ✓").
- **Voz (perfil Sol):** mensaje de voz o texto en privado ("agendame mañana 10h con X") → confirma con Ref → verificar booking en Cal.com → cancelar desde el bot.
- **Import vault:** `python scripts/import_drive_reuniones.py` (`--dry-run` para simular) → `raw/reuniones/YYYY-MM-DD-<call_id>.md`.

## 9 · Referencias

- Guías por flujo: `resumen-flujo-fathom.md` · `resumen-flujo-router.md` · `resumen-flujo-voz.md` · `resumen-flujo-agenda-sub.md` · `resumen-flujo-set01.md`.
- Manual Emilia: `playbook-os-emilia-n8n.md` v2.
- Canónico Voz: `proyectos/MVP_06-agente-voz/01-spec-mvp_06.md`.
- Foto 16/10: `specs/archived/261016-inventario-automatizaciones-mes1.md` · plan vigente: `specs/261016-plan-unificado-studio-os-quickwins.md` · inbox: `specs/261013-plan-fuentes-emilia-inbox.md`.
- Import: `scripts/import_drive_reuniones.py` + `scripts/import_drive_reuniones_notas.md`.
- Credenciales (nombres, nunca secretos): §1, §3-§5 del presente doc y `list_credentials` por MCP.
