---
tipo: log
fecha_creacion: 2026-09-24
ultima_actualizacion: 2026-09-24
tags: [sesion, os-emilia, n8n, telegram, cal-com, fathom, drive]
---

# Sesión 2026-09-24 — Plan OS-Emilia n8n

## Qué se hizo

- Analizadas las alternativas para que Emilia agende reuniones desde Telegram.
- Decidido usar el n8n actual del VPS `n8n.pitau.tech`, dentro de la carpeta `OS-Emilia`, con credenciales separadas de Lidia.
- Decidido usar un único bot de Telegram en chat privado, con un router y subworkflows, debido a la limitación de un webhook activo por token.
- Decidido usar Cal.com para crear reuniones y Google Drive para guardar las reuniones de Fathom.
- Decidido que el MVP funciona sin IA: comandos estrictos, búsqueda en Sheets y clasificación por datos estructurados de Fathom.
- Definida la clasificación automática: invitados completamente internos hacia `Reuniones-Internas`; cualquier invitado externo hacia `Reuniones-Clientes`; reuniones sin invitados hacia Internas con marca `[revisar]`.
- Definidos cron diario a las 07:00 `America/Argentina/Buenos_Aires` y comando manual `/sync`.
- Creado el documento de reanudación en `specs/260924-plan-os-emilia-n8n.md`.

## Archivos modificados

- `specs/260924-plan-os-emilia-n8n.md` — creado como plan ejecutable, playbook técnico, criterios de prueba e información pendiente.
- `raw/sessions/2026-09-24-sesion-plan-os-emilia-n8n.md` — creado como registro de continuidad.

## Análisis cerebro-digital

### Topics

- Automatización de agenda con Telegram, Cal.com y n8n.
- Sincronización programada y bajo demanda de Fathom hacia Drive.
- Clasificación automática de reuniones por participantes internos y externos.
- Arquitectura de workflows públicos y subworkflows n8n.
- Uso de un único Telegram Trigger por token de bot.
- Playbook técnico y onboarding sencillo para usuaria no técnica.

### Entidades

- Emilia Pimenta, Studio OS, Proyecto Pi.
- n8n VPS `n8n.pitau.tech`, carpeta `OS-Emilia`.
- Telegram BotFather, bot privado de Emilia.
- Cal.com de Emilia, Google Drive compartido, Google Sheets de clientes.
- Fathom API, `recording_id`, `calendar_invitees`.
- Workflow de referencia Lidia `w8iMJ01WGCSxvSMg`.

### Hechos

- La carpeta compartida local es `G:\Mi unidad\OS-Emilia`.
- Las carpetas `Reuniones-Internas` y `Reuniones-Clientes` ya están creadas.
- La carpeta `OS-Emilia` dentro de n8n ya está creada.
- El mantenimiento del VPS se integra al ciclo de mantenimiento de Lidia.
- El monitoreo del VPS queda como backlog posterior al MVP.
- El MVP no consume créditos de IA.

## Próximo

- Confirmar los correos internos de Emilia y Proyecto Pi.
- Obtener el `eventTypeId` y la duración predeterminada de Cal.com.
- Crear las credenciales separadas de Telegram, Cal.com, Fathom, Drive y Sheets.
- Construir y probar `WF-Router-Telegram`, `WF-Agenda-Core`, `WF-Fathom-Core` y `WF-Fathom-Cron`.

## Continuación de implementación — 2026-09-24

- Conectado el n8n del VPS mediante MCP.
- Resuelto el proyecto `Proyecto PI` y la carpeta `OS-Emilia`.
- Creados y validados los workflows:
  - `YWpuV5p0vCDTbIHz` — Telegram Router.
  - `UTkII2kd3RHDlizo` — Agenda Core.
  - `UeDkqVZSeLnae5cF` — Fathom Core sin credenciales.
  - `2gUlVXu7xk1Jd12s` — Fathom Cron diario 07:00 Buenos Aires.
- Creada la Data Table `OS-Emilia — Bot State` con ID `2YgepkPbLD3s4Nu9`.
- Todos los workflows quedaron desactivados.
- Se detectó que la creación automática de workflows asignó credenciales existentes por tipo: Drive, Sheets y Telegram. Se documentó que deben reemplazarse manualmente por credenciales de Emilia antes de activar.
- Fathom Core usa el endpoint oficial `https://api.fathom.ai/external/v1/meetings` con `X-Api-Key` y solicita resumen, action items y transcripción.
- El siguiente ciclo debe implementar botones de confirmación, estado conversacional conectado a la Data Table y deduplicación por `recording_id`.

## Continuación OAuth — 2026-09-24

- El usuario creó un OAuth Client nuevo en Google Cloud para `n8n OS Emilia` bajo el proyecto `academia-pi-31416`.
- Se habilitaron Google Drive API y Google Sheets API, y se agregó `proyectopi.31416@gmail.com` como usuario de prueba.
- El usuario completó el Sign in with Google en las credenciales nuevas de n8n.
- Credenciales nuevas detectadas:
  - `ppi-EmiliaOS_Google Drive account` — `F5AzgwsgpCsEth7M`.
  - `ppi-EmiliaOS_Google Sheets account` — `yb1G3uAHS2QqK1wu`.
- Se asociaron esas credenciales a los nodos Drive de Fathom Core y Sheets de Agenda Core.
- El usuario entregó el Folder ID raíz de Google Drive `OS-Emilia`: `1sJqdw8_cqsaBiVjLQWnSccmTw6Ey52ad`.
- Se configuró ese Folder ID como carpeta raíz temporal de los dos nodos Drive; faltan los IDs de `Reuniones-Internas` y `Reuniones-Clientes` para separar la clasificación.
- La búsqueda de una hoja `clientes` con la credencial nueva de Sheets no devolvió resultados; queda por verificar la pestaña y el documento real.
- Todos los workflows continúan desactivados.

## Continuación doble salida Fathom — 2026-09-24

- Se agregó a Fathom Core una salida Google Doc para cada rama:
  - `Save Client Google Doc` en `Reuniones-Clientes`.
  - `Save Internal Google Doc` en `Reuniones-Internas`.
- Cada reunión conserva el `.md` de texto plano y crea un Google Doc con el mismo contenido.
- Ambos nodos usan `ppi-EmiliaOS_Google Drive account`; `Google Docs account` queda para edición posterior.
- Se reemplazaron los placeholders del clasificador por `arq.emiliapimentalombardi@gmail.com` y `proyectopi.31416@gmail.com`.
- El workflow sigue desactivado hasta completar la prueba de escritura y deduplicación.


## Prueba Fathom — 2026-09-24

- Se creó y ejecutó un workflow temporal de solo lectura con filtro `recorded_by[]=proyectopi.31416@gmail.com`.
- Fathom respondió `401 Authorization failed` antes de devolver reuniones.
- La URL, el filtro y el endpoint fueron aceptados; la credencial `ppi-EmiliaOS_Fathom.-Header Auth account` necesita revisión.
- El workflow temporal fue desactivado y archivado.
- Próximo control: confirmar que la credencial use header exacto `X-Api-Key` y una API Key activa de la cuenta Fathom de Emilia, sin `Bearer`.


## Continuación Cal.com y credenciales — 2026-09-24

- Se detectó y conectó `ppi-EmiliaOS_Cal.com.Bearer Auth account` (`3MvZXPNH8LrDYPZS`) al nodo `Create Cal.com Booking`.
- Se detectó y conectó `ppi-EmiliaOS_Fathom.-Header Auth account` (`mAaHtYoCUcSj0via`) al nodo `Fetch Fathom Meetings`.
- Se detectó y conectó `emiliaospi_bot-Telegram account` (`PqGQSTIshKSriHOm`) al router y a los nodos Telegram.
- Se consultó Cal.com mediante un workflow temporal de solo lectura con `cal-api-version: 2024-06-14`.
- Event Types encontrados: `7109198` (15 min), `7109200` (30 min), `7109199` (Secreto, oculto).
- Se configuró `eventTypeId: 7109200` como evento predeterminado de Emilia.
- Los workflows temporales de consulta de Event Types se desactivaron y archivaron.
- Sigue pendiente obtener/verificar el link de la planilla `clientes` para publicar Agenda Core y Router.


## Continuación carpetas Drive — 2026-09-24

- El usuario confirmó los IDs de las subcarpetas compartidas:
  - `Reuniones-Clientes`: `1l7EHaiKJQfKcatPkDCnYkkrCjHiqbNN5`.
  - `Reuniones-Internas`: `1n5mkPNdHhgFEsYfLmx3LYD4sIUiHDtcQ`.
- Se actualizaron los nodos `Save Client Meeting` y `Save Internal Meeting` del Fathom Core con esos IDs.
- La credencial `ppi-EmiliaOS_Google Drive account` queda asociada a ambos nodos.
- El workflow Fathom Core sigue desactivado hasta configurar Fathom, probar la clasificación y resolver la planilla de clientes.

## Prueba de escritura Fathom — 2026-09-24

- Se ejecutó Fathom Core con una reunión real: `Impromptu Google Meet Meeting`, `recording_id: 184073789`, del 17/09/2026.
- La clasificación la envió a `Reuniones-Internas` porque el único invitado devuelto fue Emilia.
- La salida Markdown fue creada en Drive.
- La salida Google Doc alcanzó Google Drive, pero Google respondió `403 SERVICE_DISABLED`: Google Docs API no está habilitada en el proyecto OAuth `14757827498`.
- Se localizó un Google Doc parcial en `Reuniones-Internas` con nombre `2026-09-17_imprompt-google-meet-meeting_184073789`.
- El wrapper temporal de escritura y Fathom Core fueron desactivados.
- Próximo paso: habilitar `Google Docs API` en el proyecto de Google Cloud usado por el OAuth Client, esperar propagación y repetir la prueba.

## Formato Google Docs estructurado — 2026-09-24

- Se reemplazó la conversión de texto plano por un subworkflow reusable: `OS-Emilia — Format Google Doc` (`LysH41yu1s5wXkPz`).
- El subworkflow crea el Google Doc en la carpeta indicada y ejecuta `documents.batchUpdate` con Google Docs API.
- Fathom Core ahora separa:
  - `.md`: resumen, action items y transcripción.
  - Google Doc: resumen de Fathom con títulos, negritas, enlaces y estructura de viñetas.
- Se corrigió el preset de viñetas a `BULLET_DISC_CIRCLE_SQUARE`, valor aceptado por la API.
- Prueba exitosa con `recording_id: 184073789`:
  - Markdown: `1SQb65z_w1Oit2DeTbxFKrikU_bW40ugr`.
  - Google Doc formateado: `1loupJj2L_KRlZHWZxyMu8mRy-IiU6ESctUjuBcIWxXw`.
  - Verificación: 74 párrafos; `HEADING_1` ×1, `HEADING_2` ×7, `HEADING_3` ×3.
- El Fathom Core quedó desactivado; el subworkflow de formateo permanece disponible para la ejecución de producción.
- Permanecen documentos parciales de las pruebas fallidas; su eliminación requiere confirmación.

## Pruebas Telegram — 2026-09-24

- Telegram Router recibió `/agendar prueba` correctamente.
- Primer mock de Cal.com: se corrigió `chat_id` numérico y luego se detectó anticipación mínima; el mock quedó en `25/09/2026 15:00` Buenos Aires.
- El booking mock se creó correctamente; un segundo intento al mismo horario devolvió `409` por conflicto, confirmando que el evento ya existía.
- La respuesta de Telegram se mejoró a nombre, email, fecha, hora y zona horaria.
- `/sync` recibió y ejecutó Fathom Core exitosamente: una reunión, un Markdown interno y un Google Doc interno, sin errores.
- IDs de la última prueba Fathom:
  - Markdown: `1w_TU6ZW0iJ-HNI6x-L9zvySDeKZfvacr`.
  - Google Doc: `1-GphPquJUy6T62HiKxA6jvVkIjNkP6oOJk0FoDi1x68`.
- Agenda mock, Telegram Router, Fathom Core, Cron y formateador quedaron desactivados al finalizar para evitar bookings o duplicados automáticos.
- Pendiente producción: configurar planilla real, deduplicación por `recording_id` y decidir si se reactiva el Cron.

## Corrección de ubicación Drive — 2026-09-24

- La auditoría de hijos directos confirmó que `Reuniones-Internas` contenía solo el `.md` y la subcarpeta `docs`.
- Los Google Docs se estaban creando en la raíz del Drive (`parent: 0ALObjCSzgLB-Uk9PVA`) porque el nodo Google Docs no aplicaba el `folderId` compartido.
- Se actualizó `OS-Emilia — Format Google Doc` para mover cada documento creado a la carpeta de destino antes de aplicar el formato.
- Se movió el Google Doc válido de la última prueba a `Reuniones-Internas`.
- Verificación final: la carpeta contiene el `.md`, el Google Doc válido y la subcarpeta `docs`.
- Workflows temporales de auditoría y movimiento fueron archivados.







