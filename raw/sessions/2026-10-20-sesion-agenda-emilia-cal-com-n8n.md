---
tipo: log
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [n8n, cal-com, emilia, os-studio, agenda, agente-voz]
---

# Sesión 2026-10-20 — Cuenta Cal.com de Emilia + bot de agenda armado (2 clones, 2 parches)

## Qué se hizo

Objetivo pedido por Sol: **dejar mañana una versión funcional** del bot de agenda para Emilia, con el flujo ya armado y que solo haya que cambiar credenciales. Se priorizó "que funcione" por sobre "que esté completo".

### 1. Cal.com de Emilia (desde n8n, la API bloquea a la PC)

Se creó un workflow temporal por el que se pudo operar la API de Cal.com desde el VPS (desde la PC responde **403 Cloudflare 1010**).

- La credencial `ppi-EmiliaOS_Cal.com.Bearer Auth account` es **la cuenta de Emilia** (perfil "Emilia Pimenta Lombardi", `userId 3251516`).
- **Creados** los 3 event types: `7563141` presencial (address), `7563142` online (google-meet), `7563143` libre (google-meet, oculto, notice 0).
- **Creado** el schedule "Disponibilidad 24/7" `2527411` (Lun-Dom 00:00-23:59), todavía sin asignar.
- **Verificado**: `GET /v2/slots` para ET-A y ET-B devuelve 8 slots/día (09:00-16:00) → los dos son bookables.
- **Hallazgo**: el Google Calendar de Emilia **ya está conectado** en Cal.com (`arq.emiliapimentalombardi@gmail.com`, `credentialId 2605522`) y es el destination calendar → las reservas ya caen en su calendario y Cal.com ya le resta los ocupados. **El paso de OAuth de la sesión se cae solo.**
- Los 3 event types que ya tenía (7109200, 7109198, 7109199) quedaron intactos.
- **Deuda**: duraciones 120/180 y el schedule 24/7 no se pueden setear por API (ver lección 2 abajo) → se cargan en la UI de Cal.com.

### 2. n8n — 2 workflows nuevos + 2 parcheados (sin clones, sin swap de webhook)

- **Nuevo** `OS-Studio — Agenda Sub Emilia` (`2JogeOoT3Wjq2ncH`): agente con las **7 tools** sobre los 3 event types de Emilia, credencial Cal.com de Emilia y `leer_calendario` apuntando a su calendario.
- **Nuevo** `OS-Studio — Agenda Dispatcher` (`CVvxZgn0AipO6dV0`): lee el marcador `[chat:ID]` del pedido y lo enruta al subflujo de Sol (`ygdjqRfXpxKMFWEN`) o al de Emilia, según el `chat_id`.
- **Parcheado** `OS-Studio — Agent Voz TEST (revision)` (`Gpd6NHB4HQdU7ary`): allowlist de chats (`String()`-segura), claves Redis por chat, respuesta al chat de origen, `Tool Agenda` → Dispatcher, prompt "del estudio (Sol o Emilia)".
- **Parcheado** `OS-Emilia — Telegram Router` (`YWpuV5p0vCDTbIHz`): la regla 2 del switch `Route Telegram Command` pasó de `/help` a **identidad de Emilia** (su salida va a `Run Voz Agent`); `/help` sigue funcionando por el fallback.
- **Publicado** todo (los subflujos de `Execute Workflow` exigen estar publicados).

**Cambio de arquitectura respecto de lo planificado:** en vez de 2 clones del flujo de voz + 2 clones del subflujo de agenda + un Router con 3 ramas, se resolvió con **1 flujo de voz compartido + 1 Dispatcher**. Motivo: la API de n8n por MCP degrada los parámetros complejos, y el único camino fiel (SDK) exige pegar el código de 26 nodos; además el flujo compartido evita el swap del webhook de Telegram (un webhook por bot) y el riesgo de cortar el bot de Sol. **El aislamiento real se mantiene**: la credencial de Cal.com vive dentro de cada subflujo de agenda.

### 3. Pruebas

- Agenda Sub Emilia: el agente llamó `obtener_reuniones` con los 3 ET IDs correctos y respondió.
- Dispatcher con `[chat:999999999]` → `Run Agenda Emilia` (sub-ejecución `2JogeOoT3Wjq2ncH`).
- Flujo de voz completo con chat de Emilia → detector → agente → Dispatcher → Agenda Sub Emilia → respuesta correcta (el único error fue Telegram "chat not found", porque `999999999` es un id inventado).
- **Regresión de Sol**: el flujo de voz con su chat enrutó a su cuenta y respondió con su agenda real (Lun 19: 10:00 Emilia Pimenta + 14:00 Delfi CAD · Mar 20: 18:00 Clase Mora).

## Archivos del vault

- `proyectos/STUDIO_OS-Emilia/documentacion/plan-minimo-sesion-2026-10-21.md` (nuevo) — el plan de mañana.
- `raw/sessions/2026-10-20-sesion-agenda-emilia-cal-com-n8n.md` (este archivo).
- `log.md` (entrada del 20/10).

## Análisis cerebro-digital

**Topics:** Cal.com API v2 (versiones y schemas por endpoint), n8n SDK vs MCP (degradación de params), arquitectura de routing multi-persona en un bot de Telegram, OAuth de Google Calendar ya resuelto en Cal.com, publicación de versiones en n8n.

**Entidades:** Emilia Pimenta Lombardi (cuenta Cal.com `userId 3251516`, perfil `emilia-pimenta-lombardi-ctcojl`, calendario `arq.emiliapimentalombardi@gmail.com`); cuenta Cal.com de Sol (event type 7467793); chat de Sol `8459099332`; grupo Fuentes `-5417177870`; workflows `2JogeOoT3Wjq2ncH`, `CVvxZgn0AipO6dV0`, `Gpd6NHB4HQdU7ary`, `YWpuV5p0vCDTbIHz`, `ygdjqRfXpxKMFWEN`; credenciales `ppi-EmiliaOS_Cal.com` `3MvZXPNH8LrDYPZS`, `Google Calendar account` `3wo33TixNfgYPeJY`, `ppi-EmiliaOS_Google Sheets` `yb1G3uAHS2QqK1wu`.

**Hechos verificados:**
1. `POST/GET /v2/event-types` de Cal.com solo existen con `cal-api-version: 2024-06-11`; con `2024-08-13` → 404. En esa versión el body usa `length`, no `lengthInMinutes`.
2. La API de Cal.com **responde `success` pero no aplica** `metadata.multipleDuration` ni `scheduleId` → esas cosas van por la UI.
3. `POST /v2/schedules` (2024-06-11) acepta `availability` con días por **nombre** ("Monday") y `isDefault`.
4. El MCP de n8n (`addNode`, `updateNodeParameters`) **stringifica** los valores de parámetro: booleanos → `"true"`, objetos → `""`, colecciones → `{item: […]}`. Con `sendBody: "true"` n8n oculta el body (displayOptions) y el POST sale vacío (zod reporta campos requeridos como no válidos).
5. `create_workflow_from_code` (SDK) preserva tipos y completa `contentType`/`specifyHeaders`. Los `subnodes` van dentro de `config`.
6. `setNodeParameter` con puntero JSON **sobre hojas de string** sí edita in-place de forma fiel (reglas de switch, `jsCode`, `chatId`, `workflowId`).
7. Editar un workflow no cambia lo que se ejecuta: hay que **publicar**. Los subflujos de `Execute Workflow` deben estar publicados.
8. El `pinData` del MCP stringifica: un `chat.id` numérico llega como texto → allowlists con `String(...)`.
9. El `authUrl` de `GET /v2/calendars/google/connect` lleva la API key en el `state` → no va a ningún archivo del vault.

**Pendiente para el 21/10:** `chat_id` real de Emilia (2 reemplazos), dirección del estudio (ET 7563141), compartir su calendario con `proyectopi.31416@gmail.com`, y opcionalmente duraciones 120/180 + schedule 24/7 en la UI de Cal.com.
