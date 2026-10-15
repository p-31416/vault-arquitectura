---
tipo: documentacion
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha: 2026-10-08
version: 1.3
tags: [n8n, automatizacion, fathom, telegram, drive, studio-os, referencia-tecnica]
---

# Arquitectura n8n — OS-Emilia · referencia nodo por nodo

> Documento técnico de las automatizaciones. Estado verificado el 2026-10-08 por API (MCP `n8n-mcp`): **canvas único** — Fathom Core absorbió Cron + Format (v1.1). Quedan 3 workflows: Core unificado, Telegram Router, Agenda mock. Cal.com no se toca (mock temporal). Para el manual de uso de Emilia ver `playbook-os-emilia-n8n.md` (spec §11, pendiente de redacción). Fuente de diseño: `specs/260924-plan-os-emilia-n8n.md`.

## 0 · Mapa en 1 tabla

| Workflow | ID n8n | Trigger | Estado 09/10 | Función en 1 línea |
|---|---|---|---|---|
| Fathom Core (canvas único) | `UeDkqVZSeLnae5cF` | Schedule 07:00 + ExecuteWorkflowTrigger | activo | Lee Fathom → `.md` a Drive → Google Doc formateado, todo en un canvas |
| Telegram Router | `YWpuV5p0vCDTbIHz` | Telegram Trigger (message + callback_query) | activo (sin filtro `chat_id`) | `/agendar` → Agenda · `/sync` → Fathom · `/cancel`+callback → Cancel · `/modif` → Modif · `/help` |
| Agenda Core (real) | `UTkII2kd3RHDlizo` | ExecuteWorkflowTrigger | activo | Reserva real Cal.com (parseo + hoja clientes + confirmación) |
| Cancel Core | `B7gGFGcD89vKfc5k` | ExecuteWorkflowTrigger | activo | `/cancel` lista con botones · `/cancel Ref` directo · cancela en Cal.com |
| Modif Core | `c08s62Lo9EmAEJJf` | ExecuteWorkflowTrigger | activo | `/modif` lista numerada · `/modif N [DD/MM] HH:MM` · `/modif Ref DD/MM HH:MM` · reprograma en Cal.com |
| ~~Fathom Cron~~ | `2gUlVXu7xk1Jd12s` | — | **archivado** (trigger vive en el Core) | — |
| ~~Format Google Doc~~ | `LysH41yu1s5wXkPz` | — | **archivado** (cadena inline en el Core) | — |

```
Schedule 07:00 ──┐
                 ├─► Fetch → Split → BuildDoc → BuildReq → Classify ─┬─► Save .md ─┐
Telegram (/sync) ─┘                                                  └─► (clientes | internas) ─┘
                                                                                          ▼
                                                              Create Doc → Move → Apply formato
Telegram (/agendar) ──► Agenda mock ──► Cal.com (reserva prueba) + confirmación
Drive (.md) ──► vault (import_drive_reuniones.py)
```

Data Table `OS-Emilia — Bot State` (`2YgepkPbLD3s4Nu9`) existe pero **sin conectar** (spec §16.2): no hay control de duplicados (ver §6).

## 1 · Canvas único — `UeDkqVZSeLnae5cF` (13 nodos, ex Fathom Core + Cron + Format)

Dos triggers alimentan `Fetch Fathom Meetings`: `Daily Fathom Sync 07:00` (cron diario) y `Fathom Core Trigger` (llamadas de `/sync`, con `source` informativo). Después del Classify, ambas ramas confluyen en **una cadena compartida** de Docs (los datos viajan en el item + pairing nativo `$('Classify Meeting').item`).

| # | Nodo | Tipo / credential | Qué hace |
|---|---|---|---|
| 0a | Daily Fathom Sync 07:00 | `scheduleTrigger` | Disparo diario 07:00 (ex workflow Cron, absorbido). Timezone del workflow: `America/Argentina/Buenos_Aires` (el servidor corre en UTC) |
| 0b | Fathom Core Trigger | `executeWorkflowTrigger` | Entrada para `/sync` (Router). Recibe `source` opcional |
| 1 | Fetch Fathom Meetings | `httpRequest` · `ppi-EmiliaOS_Fathom` (`mAaHtYoCUcSj0via`) | `GET https://api.fathom.ai/external/v1/meetings` con `include_transcript/summary/action_items=true` + `created_after = {{ $now.minus({ hours: 26 }).toISO() }}`. Solo trae lo del último día (ventana 26h: cubre el cron diario con 2h de solape). Backfills requieren corrida manual con ventana ampliada |
| 2 | Split Meetings | `splitOut` (`fieldToSplitOut: items`) | Separa el lote en 1 item por reunión |
| 3 | Build Meeting Document | `code` | Arma `fileName`, `document` (`.md` completo), `summaryDocument` (sin transcript), `folder`, `folderId`, `needsReview`. Detalle en §2 |
| 4 | Build Google Docs Requests | `code` | Convierte el markdown a `plainText` + array `requests` (insertText, estilos de títulos, bullets, negritas, links) y devuelve `batchUpdate: { requests }`, `docTitle` |
| 5 | Classify Meeting | `if` (`$json.folder` equals `clientes`) | Rama clientes (true) vs internas (false) |
| 6a | Save Client Meeting | `googleDrive` · `ppi-EmiliaOS_Google Drive` (`F5AzgwsgpCsEth7M`) | `createFromText` en `Reuniones-Clientes` (`1l7EHaiKJQfKcatPkDCnYkkrCjHiqbNN5`), nombre `=$json.fileName`, contenido `=$json.document` |
| 6b | Save Internal Meeting | `googleDrive` · misma Drive | Idem en `Reuniones-Internas` (`1n5mkPNdHhgFEsYfLmx3LYD4sIUiHDtcQ`) |
| 7 | Create Google Doc | `googleDocs` · `Google Docs account` (`kdQydeePwlZbNbkY`) | Crea el Doc con `title = $('Classify Meeting').item.json.docTitle` en `folderId = $('Classify Meeting').item.json.folderId` (pairing nativo, porque Save reemplaza el item) |
| 8 | Move Google Doc to Folder | `googleDrive` · `ppi-EmiliaOS_Google Drive` | Mueve el Doc (`$json.id` local, salida de Create) a `folderId = $('Classify Meeting').item.json.folderId` |
| 9 | Apply Google Docs Formatting | `httpRequest` · Docs OAuth | `POST .../documents/{{ $json.id }}:batchUpdate` con `jsonBody = {{ JSON.stringify($('Classify Meeting').item.json.batchUpdate) }}` |

> Por qué pairing en expresiones y no MergeBack con Code: los nodos Save/Create **reemplazan** el item (solo devuelven metadata del archivo), y en Code el pairing (`$input.item`, `.first()`) resultó inconsistente entre modos; en parámetros, `$('Nodo').item.json` es el mecanismo estándar y verificado en producción (exec 3500 `success`).

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
slug        = sin lados externos ? lados internos ('emilia-proyectopi')
            : lados internos + hasta 2 externos
            // ej internas: 2026-09-24_emilia-proyectopi_186596516.md
            // ej clientes: 2026-10-03_emilia-vanessa-ferreira-leticia-gentilini_189333562.md
fileName    = ([revisar]-) + YYYY-MM-DD + _ + slug + _ + recording_id + .md
```

El `.md` (`document`) lleva: título, Fecha, Recording ID, URL, Participantes (unión por lados), **Invitados calendario (con mails)**, **Hablantes en transcript (con conteo)**, **Grabado por**, Clasificación, Resumen, Action items, Transcripción. `summaryDocument` es lo mismo sin transcript (para el Google Doc).

> Nota: `calendar_invitees_domains_type` de Fathom no es confiable (devuelve `one_or_more_external` aun con un solo invitado interno) — no se usa. `shared_with` viene como string (`no_teams`), sin mails.

## 3 · WF Telegram Router — `YWpuV5p0vCDTbIHz`

Trigger `Telegram OS-Emilia` (`telegramTrigger`, cred `emiliaospi_bot` `PqGQSTIshKSriHOm`, escucha `message` + `callback_query`) → `Route Telegram Command` (`switch`, case-insensitive):

| Rama | Condición sobre `$json.message.text` | Destino |
|---|---|---|
| 1 | startsWith `/agendar` | `Run Agenda Core` (pasa `text` + `chat_id`) |
| 2 | equals `/sync` | `Run Fathom Sync` (pasa `source: telegram`) |
| 3 | equals `/help` | `Send Help` (responde la lista de comandos al mismo `chat_id`) |
| fallback | resto | salida `Help` (renombrada) |

**Sin filtro de `chat_id`** (`additionalFields` vacío): cualquiera con el username del bot lo dispara. Cerrar al `chat_id` de Emilia cuando mande su primer `/start` (pendiente).

## 4 · WF Agenda Core (real, sin mock) — `UTkII2kd3RHDlizo`

`Agenda Core Trigger` (recibe `text`, `chat_id` del Router) → `Parse Agenda Command` (regex `/agendar DD/MM[/AA] HH:MM Nombre [emails...]`; año implícito con rollover; valida calendario/fecha pasada/máx 1 año; convierte AR→UTC; separa emails del nombre) → `IF/SW Valid` → `IF/SW Has Email` → rama directa a `Build Booking Payload`, o rama Sheets: `Lookup Client Email` (lee toda `clientes-contactos`/`clientes` con cred `ppi-EmiliaOS_Google Sheets` `yb1G3uAHS2QqK1wu`) → `Find Client Email` (match normalizado sin tildes, solo filas activas) → `IF/SW Found` → `Build Booking Payload` (unifica `{chat_id, humanDate, humanTime, contactName, email, startISO, guests, source}`) → `Create Cal.com Booking` (`POST https://api.cal.com/v2/bookings`, header `cal-api-version: 2024-08-13`, cred `ppi-EmiliaOS_Cal.com` `3MvZXPNH8LrDYPZS`, `eventTypeId: 7109200` 30 min, `attendee{name,email,timeZone America/Argentina/Buenos_Aires,language es}` + `guests[]`) → `IF/SW Booking OK` (`status` equals `success`) → `Send Agenda Confirmation` (fecha/hora AR + attendee + Ref `uid`). Errores: `Send Format Error` (sintaxis), `Send No Email Found` (sin match en hoja), `Send Booking Error` (rechazo API).

> Lección 08/10: los nodos **IF creados por API no evalúan** en esta instancia (todo sale por rama 0, probado hasta con condición deliberadamente falsa; el IF viejo del Fathom Core sí funciona). Se migraron los 4 a **Switch v3.4** con la estructura exacta del Router (probado en producción). Ver fix 9.

## 5 · Historial de fixes (08/10, verificados por API)

| # | Síntoma | Causa | Fix | Versión |
|---|---|---|---|---|
| 1 | Core moría en `Save Internal Meeting` | OAuth Drive/Docs expirado (último success 24/09) | Reconnect en n8n UI (Sol) | — |
| 2 | `Apply`: "JSON Body is not valid JSON" | `jsonBody` interpolaba el objeto (`[object Object]`) | Serializar en Code node (`batchUpdateJson`) | Format `46e197f9` |
| 3 | Mismo error tras fix 2 | Cableado `Restore → Move → Apply`: el `$json` del Apply no trae `batchUpdateJson` | Apply referencia `$('Restore Format Requests')` por nombre en `url` y `jsonBody` | Format `8ac83b6f` |
| 4 | `.gdoc` en raíz de Mi unidad | Builder no enviaba `folderId` | Builder mapea `folder` → Folder ID | Core `4babe389` |
| 5 | Nombres `impromptu-...` | Slug salía del título Fathom | Opción A: `fecha_participantes_recid` | Core `a3a73dad` |

Ejecuciones de prueba: 3473/3475 (fallo Drive) → 3477/3480 (fallo JSON) → 3483/3486 (fallo wiring) → **3489 `success`** → 3492 (nombres A) → **3495 `success`** (gdocs en carpeta) → 3497/3498/3499 (MergeBack: match por nombre imposible —Save devuelve solo `id`— y `$input.first/item` inconsistente en Code) → **3500 `success`** (canvas único con pairing en expresiones).

| 6 | 3 canvas separados (desfasajes de versión entre Core/Format) | Merge a 1 canvas de 13 nodos | Schedule + cadena compartida con pairing `$('Classify Meeting').item`; MergeBack descartados (Code no resuelve pairing de forma estable); Cron y Format archivados | Core `28524385` |
| 7 | Clasificación solo por invitados (externos del transcript invisibles; cero invitados caía en clientes) | Filtro por lados: invitados + hablantes + recorded_by | `sideOf` mapea a emilia/proyectopi/externo; externo presente → clientes; cero señal → internas + `[revisar]-`; nombre y `.md` con evidencia | Core `52cc8643` |
| 8 | Fetch traía todo el historial (cada corrida re-escribía las 8, copias `(1)(2)(3)` en Drive) | Filtro `created_after` a nivel API | Query param `created_after = $now − 26h`; verificado exec 3505: lote vacío, success sin escribir | Core `ffd071f6` |
| 9 | IFs nuevos no discriminan (todo sale por rama 0, en test Y producción; el IF viejo sí funciona) | Migración a Switch v3.4 | Estructura idéntica al Router probado; verificado exec 3525: rama Sheets → reserva real `gnCrXcR1j3mz8Hd9THXhyh` + confirmación Telegram | Agenda `453e84ce` |
| 10 | `/cancel` exigía el Ref (nadie lo sabe) | Modo lista con botones inline | `GET /v2/bookings?status=upcoming` → un mensaje por reunión con botón (`cancel:<uid>`, 64B) → callback ruteado en Router → Cancel Core sin cambios (texto sintetizado) | Cancel `5f7761b2`, Router `79b42584` |
| 11 | `/modif` exigía Ref + fecha completa | Modos lista/número/Ref + misma-hora | `/modif` lista numerada; `/modif N DD/MM HH:MM`; `/modif N HH:MM` (mismo día de esa reunión); `/modif Ref DD/MM HH:MM`. Pick por índice + Compute Start | Modif `4bf64ff0` |
| 12 | Switch nuevos sin evaluar (comparaban literal) | Prefijo `=` en leftValues | Sin `=` n8n compara el texto crudo `{{ ... }}` → siempre fallback. Estandarizado al patrón del Cancel/Router que funciona | Cancel + Modif |

## 6 · Caveats y pendientes

1. **Sin dedup por `recording_id` (mitigado):** el filtro `created_after` (fix 8) corta los duplicados de raíz en el cron diario; queda un solape de 2h que puede re-escribir 1 reunión como máximo. Fix completo pendiente: conectar la Data Table `OS-Emilia — Bot State`. El import al vault es inmune (idempotente por `call_id`).
2. **Router sin `chat_id`:** cerrar cuando Emilia mande `/start`.
3. **Agenda mock:** pasar a Sheets real (`clientes`: `name`, `email`, `activo`) + parseo de `/agendar DD/MM HH:MM Nombre` + botones Confirmar/Cambiar/Cancelar (spec §15).
4. **Quirk `needsReview` resuelto:** cero señal → internas + `[revisar]-` (spec §5).
5. ~~**Mejora por lados:** pendiente~~ — implementada (ver §2 y fix 7).

## 7 · Cómo probar

- **Corrida manual:** MCP `execute_workflow` (`UeDkqVZSeLnae5cF`, `executionMode: production`; el trigger Schedule lo hace ejecutable directo) → `search_workflow_executions` → `get_workflow_execution` con `includeData`. Ver `.md` nuevo en `G:\Mi unidad\OS-Emilia\Reuniones-*/`.
- **Telegram:** `/help` (seguro, no toca Fathom/Drive) → `/sync` (corre el Core real).
- **Import vault:** `python scripts/import_drive_reuniones.py` (`--dry-run` para simular) → `raw/reuniones/YYYY-MM-DD-<call_id>.md`.

## 8 · Referencias

- Diseño: `specs/260924-plan-os-emilia-n8n.md` (especialmente §16.4-16.5, IDs de Drive, credenciales).
- Import: `scripts/import_drive_reuniones.py` + `scripts/import_drive_reuniones_notas.md`.
- Análisis de reuniones: agente `.opencode/agents/fathom-pm.md`.
- Credenciales (nombres, nunca secretos): §1 del presente doc y `list_credentials` por MCP.
