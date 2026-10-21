# Plan — Google Calendar de Emilia + 3 event types + arquitectura de 1 trigger

> 2026-10-19 · Sol · `proyecto-pi/vault-arquitectura`
> Dejar el agente de agenda de Emilia con **sus** datos (Cal.com, Google Calendar, hoja de clientes),
> con los event types definidos, y con la arquitectura de n8n que no se desarma con más personas.

---

## 1 · Hallazgo de fondo: no existe "el Google de Emilia"

Verificado en `raw/sessions/2026-09-24-sesion-plan-os-emilia-n8n.md` L79-97 y
`raw/sessions/2026-10-08-sesion-n8n-fathom-agenda.md` L19.

| Credencial n8n | De quién es realmente | Estado |
|---|---|---|
| `ppi-EmiliaOS_Google Drive account` (`F5AzgwsgpCsEth7M`) | **`proyectopi.31416@gmail.com`** (usuario de prueba del OAuth Client `n8n OS Emilia`, proyecto Cloud `academia-pi-31416`) | Reconectada por Sol el 08/10 |
| `Google Docs account` (`kdQydeePwlZbNbkY`) | ídem (mismo OAuth Client) | Reconectada por Sol el 08/10 |
| `ppi-EmiliaOS_Google Sheets account` (`yb1G3uAHS2QqK1wu`) | ídem | Reconectada por Sol el 08/10 |
| `Google Calendar account` (`3wo33TixNfgYPeJY`) | `proyectopi.31416@gmail.com` | Activa (lee `proyectopi.31416@gmail.com`) |
| `ppi-EmiliaOS_Cal.com.Bearer Auth account` (`3MvZXPNH8LrDYPZS`) | **API key de la cuenta Cal.com de Emilia** | Activa (usada el 24/09 con `eventTypeId 7109200`) |

**Consecuencia:** Drive, Docs y Sheets ya los maneja Sol desde su PC, sin loguearse con la cuenta de
Emilia. **Lo único que falta de Google es Calendar.**

**Mantenimiento real (no semanal):** los access tokens de Google expiran a la hora y n8n los refresca
solo; el refresh token vive hasta que alguien lo revoca. Lo que hay que mirar es el flag *needs to be
reconnected* de n8n (el del 08/10 en Drive/Docs). Chequeo **mensual de 15 min** (ya está en
`credenciales-conexiones.md`); el trigger real es "un exec falló con 401/403".

---

## 2 · Arquitectura de n8n: 1 trigger, switch por `chat_id`, 2 clones

### Preguntas de Sol y respuestas con fuente

> "¿no pueden estar en el mismo workflow? ¿puede hacer dos telegram webhook de entrada? ¿o un switch
> por número desde el que le llega el mensaje? ¿o es más fácil tener el flujo separado? es que crecen
> exponencialmente los flujos"

**Dos triggers de Telegram con el mismo token: imposible.** Telegram admite **un webhook por bot**;
n8n lo bloquea con *"Due to Telegram API limitations, you can use just one Telegram trigger for each
bot at a time"* (docs oficiales `telegramtrigger/common-issues`). Es el incidente del 13-14/10:
*"1 trigger por token — un segundo trigger le roba el webhook"*.

**Dos triggers con tokens distintos: frágil.** La comunidad reporta que aun con credenciales
diferentes *"only the last activated workflow executes"* (n8n #14610, foro "Only the last activated
workflow runs").

**Switch por `chat_id`: sí, y ya está la mitad.** El `Route Identidad` del Router (`YWpuV5p0vCDTbIHz`)
ya es un Switch con la regla `chat_id == 8459099332 → Run Voz Agent`. Falta **una regla más** para
Emilia y **un `executeWorkflow`** al clon.

### Decisión: clones, no un agente multi-perfil

`onboarding-emilia-perfiles.md` propone hoy *"UNO con perfiles"*; **se reconcilia en §7.5** porque su
propio análisis admite el problema: *"el único punto donde n8n obliga a ramificar es la credencial
(no admite expresiones)"*.

| | 1 agente, 2 perfiles | **2 clones (elegido)** |
|---|---|---|
| Workflows | 3 | **4** (Router + 2×(Voz + Agenda)) |
| Tools del agente | 20 (10 por perfil, duplicadas con credencial distinta) | 10 por agente |
| Error posible | El LLM llama la tool del perfil equivocado → **agenda en la cuenta Cal.com ajena** y mail al cliente desde la cuenta que no es | Ninguno: cada workflow tiene una sola credencial |
| Crecimiento con N personas | 6 tools × N en un agente | Lineal: N workflows de 38 nodos |

**El riesgo que decide:** con credenciales fijas por nodo y tools duplicadas, un error del LLM
selecciona la cuenta equivocada. No es un bug de software: es un mail que sale al cliente desde la
cuenta que no es, con un booking real. El aislamiento por workflow lo hace imposible.

**El crecimiento no es exponencial, es lineal:** persona N = 38 nodos + 1 regla en el Router. El
Router sigue siendo **el único** trigger, el Fathom Core **uno**, la hoja de clientes **una**.

### Topología final

```
Telegram (bot emiliaospi_bot) — UN solo trigger: Recibo Mensaje (Router YWpuV5p0vCDTbIHz)
└─ Route Identidad (Switch por chat_id)
   ├─ 8459099332 (Sol)    → Run Voz Agent        → OS-Studio — Agent Voz TEST   (Gpd6NHB4HQdU7ary)
   │                                            → OS-Studio — Agenda Sub TEST (ygdjqRfXpxKMFWEN)
   └─ <chat_id Emilia>     → Run Voz Agent Emilia → OS-Studio — Agent Voz Emilia  (CLON)
                                                    → OS-Studio — Agenda Sub Emilia (CLON)
└─ Route Fuentes Group (-5417177870) → Inbox de enlaces (Sheet)   [sin cambios]
└─ Route Telegram Command → /sync · /help                        [sin cambios]
```

El clon de Emilia **no lleva trigger de Telegram**: entra por `executeWorkflow` desde el Router
(igual que el de Sol). Es la regla que evita que se le robe el webhook.

**Sobre `OS.emi-pi`:** en n8n no existe ninguna credencial de Telegram con ese nombre (las 4 son
`emiliaospi_bot`, `Telegram account`, `Lidia_mdgbot`, `lidia_testbot`). Se asume que `OS.emi-pi` **es
`emiliaospi_bot`** y que el "mensaje de activación" que la reunión menciona es simplemente el primer
mensaje de Emilia al bot → de ahí sale su `chat_id`. **A verificar en la sesión** (mandar `/start` y
leer el `chat_id` de la ejecución). Si fuera un token nuevo, hay que revisar la arquitectura (2º bot,
2º trigger → frágil, ver arriba).

---

## 3 · Google Calendar de Emilia

### Decisiones de Sol

- El calendario **personal está en otra cuenta** (gmail personal).
- El bot lee **profesional (detalles) + personal (solo free/busy)**.
- Las reservas caen en el **calendario profesional**.
- En Cal.com **solo el profesional bloquea** la disponibilidad.
- Orden del miércoles: **1) crear event types, 2) conectar la app.**

### Cómo se resuelve, paso a paso

**A) Ver la agenda (lo que lee el bot).** Emilia comparte sus 2 calendarios con
`proyectopi.31416@gmail.com` (*Google Calendar → Configuración → Compartir calendarios*), cada uno
con su nivel:

| Calendario | Permiso en Google | Cómo lo lee n8n | Bloquea en Cal.com |
|---|---|---|---|
| Profesional (`arq.emiliapimentalombardi@gmail.com`) | *Ver todos los detalles de los eventos* | `leer_calendario` (Get Many) — ve título, hora, lugar | **Sí** |
| Personal (gmail personal) | *Ver solo disponibilidad libre/ocupado* | `consultar_disponibilidad_google` (operación **Availability**/freebusy) — ve ocupado, no el contenido | **No** |

Reutiliza la credencial `Google Calendar account` (`3wo33TixNfgYPeJY`) → **sin OAuth nuevo, sin
mantenimiento**. Si Emilia revoca el acceso, el bot pierde la lectura de agenda y **sigue agendando**
(solo pierde el listing).

**B) Evitar el doble booking (vive en Cal.com, no en n8n).** La app *Google Calendar* debe estar
conectada dentro de la cuenta de Cal.com de Emilia: Cal.com consulta los calendarios conectados y
**excluye los ocupados de los slots** (`getBusyTimes.ts` → `getBusyCalendarTimes(credentials, …)`,
`source: "busy_time.calendar"`), además de los bookings propios. Sin esa app, Cal.com solo conoce
sus propios bookings.

**Hallazgo que simplifica el paso:** `GET /v2/calendars/google/connect` **acepta API key** y devuelve
el `authUrl`. Se puede generar el link desde n8n (workflow temporal con la API key que ya está en la
credencial) y Emilia **solo abre el link y autoriza** — 1 clic, sin tocar la UI de Cal.com. El
callback `/v2/calendars/google/save` guarda las credenciales.

**C) Qué calendarios bloquean.** Dentro de Cal.com, *Checking for Conflicts* → nivel usuario o por
link → destrancar el personal. Como el personal está en **otra cuenta** y la app se conecta con la
cuenta profesional, en principio Cal.com ni lo ve → no bloquea. Si se suscribiera al profesional, se
desmarca explícitamente.

### Qué NO hay que pedirle a Emilia

~~Contraseña de Google~~ · ~~API key de Google~~ · ~~Acceso a Drive/Docs/Sheets~~ (ya lo tenés) ·
~~Que separe una agenda interna~~ (el ET-C es el mecanismo).

**Lo único puntual:** su primer mensaje al bot (para el `chat_id`) y el 1 clic del link de授权 de
Google Calendar dentro de Cal.com.

---

## 4 · Event types de Emilia (3) y cómo decide el agente

### Restricciones técnicas verificadas

- `POST /v2/event-types` con `cal-api-version: 2024-08-13`. La **API key de su cuenta** alcanza: no
  hace falta su contraseña.
- **Desde esta PC la API da 403 (Cloudflare 1010)** → las llamadas se hacen desde n8n (VPS).
- `POST /v2/schedules` exige **`cal-api-version: 2024-06-11`** (distinta a event-types).
- `google-meet` **sí** se puede fijar por API (*"Via API, only Google Meet, Teams and Zoom can be
  installed"*), **pero** solo si la app ya está instalada o conectada en la cuenta → **se conecta la
  app primero** (paso B) y recién después se crean los event types. El 08/10 se concluyó que "no se
  puede por API"; era por versión de API y por app no conectada.
- El endpoint de slots acepta `duration` cuando el event type tiene varias duraciones.

### Los 3 event types

| | ET-A | ET-B | ET-C |
|---|---|---|---|
| Título | `Reunión presencial · Estudio` | `Reunión online` | `Disponibilidad libre` |
| `lengthInMinutes` | 60 | 60 | 60 |
| `lengthInMinutesOptions` | `[60,120,180]` | `[60,120,180]` | `[60,120,180]` |
| `locations` | `[{type:"address", address:"<DIRECCIÓN DEL ESTUDIO>"}]` | `[{type:"integration", integration:"google-meet"}]` | `[{type:"integration", integration:"google-meet"}]` |
| `minimumBookingNotice` | 120 | 120 | **0** |
| `bookingLimitsDuration` / `bookingWindow` | default | default | **deshabilitados** |
| `scheduleId` | default de la cuenta | default de la cuenta | **schedule 24/7 propio** |
| `hidden` | no | no | **sí** (solo el bot lo usa) |
| Cuándo lo elige el bot | "presencial" / "al estudio" / "voy a la oficina" / da una dirección | "videollamada" / "meet" / "online" / "zoom" | **solo** si dice "urgente" / "sin límite" / "ya" / "en un rato" / "cuanto antes" |
| Reserva cae en | calendario profesional | calendario profesional | calendario profesional |

**El schedule 24/7** (`POST /v2/schedules`, `cal-api-version: 2024-06-11`):
`availability: [{days:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], startTime:"00:00", endTime:"12:00"}, {…, startTime:"12:00", endTime:"23:59"}]`
→ se parte en dos franjas porque `"24:00"` no es una hora válida. Después
`PATCH /v2/event-types/{id}` con `scheduleId`.

**Falta un `schedule` default de la cuenta** (Lun-Vie 9-17) para ET-A y ET-B: si la cuenta de
Emilia no lo tiene, se crea primero (`isDefault: true`).

**El `eventTypeId` va FIJO en el body de cada tool, nunca por `$fromAI`.** Hoy
`consultar_disponibilidad` lo pide por `$fromAI('EventTypeId')` → el LLM podría inventar un ID. Con
un event type por tool, el LLM elige la *tool* y el ID es un hecho.

**7109200 (30 min) queda intacto** como backup.

### Tools del clon de Emilia (11, con el ID fijo)

| Tool | Qué hace | Cambio vs. el de Sol |
|---|---|---|
| `consultar_disponibilidad_presencial` | `GET /v2/slots` | `eventTypeId` fijo ET-A |
| `consultar_disponibilidad_online` | `GET /v2/slots` | `eventTypeId` fijo ET-B |
| `consultar_disponibilidad_libre` | `GET /v2/slots` | `eventTypeId` fijo ET-C |
| `agendar_presencial` | `POST /v2/bookings` | ET-A + `location` |
| `agendar_online` | `POST /v2/bookings` | ET-B + Meet |
| `agendar_libre` | `POST /v2/bookings` | ET-C |
| `obtener_reuniones` | `GET /v2/bookings` | sin `eventTypeId` → todas (verificar si la v2 lo acepta omitido) |
| `actualizar_reunion` | `POST /v2/bookings/{uid}/reschedule` | igual que Sol |
| `cancelar_reunion` | `POST /v2/bookings/{uid}/cancel` | igual que Sol |
| `leer_calendario` | Google Calendar **Get Many** | calendario **profesional** compartido (detalles) |
| `consultar_disponibilidad_google` | Google Calendar **Availability** (freebusy) | calendario **personal** (free/busy, sin títulos) |

### Cómo decide el agente (reglas al system prompt)

1. Si el pedido **no dice** presencial ni online → preguntar cuál (1 pregunta, rioplatense, 2-3 líneas).
2. **Presencial** si dice "presencial", "al estudio", "voy a la oficina", o da una dirección → ET-A.
3. **Online** si dice "videollamada", "meet", "zoom", "online" → ET-B.
4. **Libre** **solo** si dice "urgente", "sin límite", "ya", "en un rato", "cuanto antes" → ET-C.
   Si no lo pide, **no se ofrece**.
5. **Duración**: 60 por defecto; 120 o 180 solo si ella las pide o el tipo de reunión lo pide
   (revisión de proyecto, entrega). Nunca inventar duración: son las 3 opciones del event type.
6. **Siempre** `buscar_contacto` primero; el email es obligatorio.
7. **Siempre** validar slots con la tool del event type correspondiente **antes** de proponer horario;
   para el personal, cruzar `consultar_disponibilidad_google`.
8. Antes de escribir: resumen + "Confirmá" (escritura, no se perdona).
9. Mover o cancelar **siempre desde el bot o Cal.com**, nunca desde Google (el `bookingUid` queda
   huérfano y el cancel rebota — verificado 15/10).
10. El bot **solo agenda**: el aviso al invitado lo manda Cal.com por mail.

---

## 5 · Aislamiento de datos entre los dos agentes

| Recurso | Sol | Emilia | Cómo se separan |
|---|---|---|---|
| Postgres (memoria) | `studio_os_test`, `sessionKey = chat.id` | **misma tabla**, `sessionKey` distinto | La `sessionKey` ya usa el `chat.id` → se separa sola. No hace falta tabla nueva |
| Redis (lote) | `studio_os_test_8459099332` | `studio_os_emilia_<chat_id>` | **única línea a cambiar** en el clon (3 nodos Redis) |
| Cal.com | `ppi_calcom-Bearer Auth account` (`60SFxvMa6AaqmWWi`), evento `7467793` | `ppi-EmiliaOS_Cal.com` (`3MvZXPNH8LrDYPZS`), ET-A/B/C | Credencial fija por workflow |
| Google Calendar | `Google Calendar account` → `proyectopi.31416@gmail.com` | misma credencial → profesional (detalles) + personal (free/busy) | Campos *Calendar* de los 2 nodos |
| Sheet de clientes | `clientes-contactos` (`1t9-j_7gJypLOicaJNpwYWLsBy0VDtSmdBJZumW8jtVA`), hoja `clientes` | **la misma** (decisión de Sol) | Una sola hoja y credencial → no hay cruce que aislar |
| Telegram | bot `emiliaospi_bot` | **el mismo bot** | El `chat_id` define el perfil |
| Memoria de conversación | Visible para Sol (Postgres del VPS) | Visible para **Sol** (decisión de Sol); Emilia no accede | Sin panel: se lee por SQL |

---

## 6 · Guion del miércoles 21/10 (2 h, presencial)

| # | Bloque | Quién | Min | Resultado |
|---|---|---|---|---|
| 1 | Apertura: qué va a poder hacer el bot con sus datos | Sol | 10 | Emilia sabe qué esperar |
| 2 | **Conectar la app Google Calendar en Cal.com**: Sol genera el `authUrl` con la API key (workflow temporal) → Emilia abre y autoriza (1 clic) | Sol + Emilia | 20 | Cal.com ya ve los ocupados |
| 3 | **Crear los 3 event types + schedule 24/7** por API (workflow temporal en n8n con la API key de la credencial) | Sol | 30 | ET-A/B/C con sus IDs |
| 4 | **Compartir los 2 calendarios** con `proyectopi.31416@gmail.com` (profesional con detalles, personal free/busy) | Emilia | 10 | El bot puede leer la agenda |
| 5 | Sol clona los 2 workflows y cablea el perfil (allowlist, Redis, prompt, tools con ID fijo, `leer_calendario` ×2, `chatId` dinámico) + rama en el Router | Sol | 40 | Clones con perfil Emilia |
| 6 | Probar en vivo: "agendame mañana 10 con X" → slots → confirmación → reserva → mover → cancelar | Emilia + Sol | 25 | Los 7 criterios de aceptación |
| 7 | Cierre: qué queda, quién lo toma | Ambos | 10 | Lista con dueño y fecha |

**El paso 5 es el que se puede dejar a medias** si algo falla: los clones no se publican hasta que
las pruebas dan bien (el workflow clonado queda desactivado mientras tanto).

**Rollback en 1 minuto:** en el Router, `Route Identidad` → desactivar el nodo `Run Voz Agent Emilia`
→ publicar. El sistema vuelve al estado previo sin tocar los workflows de Sol.

---

## 7 · Archivos a tocar

### 7.1 NUEVO `proyectos/STUDIO_OS-Emilia/documentacion/playbook-google-oauth-emilia.md`

Playbook de autorización de Google, escrito para que lo ejecute **Sol desde su PC**:

1. **Mapa de "qué es de quién"** (tabla de §1) — para no volver a confiar credenciales por el nombre.
2. **Qué NO hay que pedirle a Emilia** (contraseña, API key, acceso a Drive/Docs/Sheets).
3. **Ruta de lectura de la agenda** (compartir 2 calendarios, con el nivel de permiso por calendario y
   por qué el personal es free/busy).
4. **Conectar la app Google Calendar en Cal.com** — el flujo por API: `GET /v2/calendars/google/connect`
   → `authUrl` → Emilia autoriza → `GET /v2/calendars/google/save`. Con el ejemplo de nodo HTTP
   Request para n8n y qué mirar en la respuesta.
5. **Mantenimiento real**: qué pasa cada mes, qué es *needs to be reconnected*, qué hacer si se cae,
   por qué **no** es semanal, y qué pasa si Emilia revoca el acceso (el bot sigue agendando).
6. **Tabla de permisos de Calendar** (compartido / free-busy / escritura) y qué se elige en cada caso.
7. **Los 2 roles de calendario**: el que *lee* el bot y el que *bloquea* en Cal.com — no son el mismo.
8. Checklist de la sesión.

### 7.2 `proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia.md` (reescritura)

- **§0 Índice con wikilinks** a las 9 secciones + referencias a
  [[proyectos/STUDIO_OS-Emilia/documentacion/playbook-google-oauth-emilia|playbook Google OAuth Emilia]] ·
  [[proyectos/MVP_06-agente-voz/documentacion/workflow-voz-test-referencia|referencia workflow Voz]] ·
  [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura n8n v2.0]] ·
  [[specs/261019-plan-agentes-telegram-agenda-emilia|plan agentes]] ·
  [[raw/sessions/2026-10-19-sesion-guion-agente-agenda-emilia|sesión 19/10]].
- Cada sección del guion (§6) con wikilink a la parte del doc que la ejecuta, y viceversa.
- **§2 Arquitectura** → topología de §2 + tabla comparativa + fuentes de la restricción de Telegram.
- **§3 Claves a pedir** → **3 pedidos** (API key de Cal.com ya cargada; compartir 2 calendarios;
  1 clic de autorización de Google Calendar en Cal.com) + la dirección del estudio como dato que
  carga Sol en la sesión. Con el bloque "qué NO se pide".
- **§4 Cambios nodo a nodo** → los 26 nodos del clon (allowlist, Redis ×3, Postgres, prompt, Tool
  Agenda, `Responder Telegram` con `chatId` dinámico) + los 12 del subflujo (11 tools con
  `eventTypeId` fijo, `cal-api-version`, 2 nodos Calendar) + la rama del Router.
- **§4bis Event types** → tabla ET-A/B/C con los **JSON literales** de creación (los que se ejecutan
  en la sesión) + el schedule 24/7 + el schedule default + las 10 reglas de decisión.
- **§5 Aislamiento de datos** → tabla de §5.
- **§6 Guion** → los 7 bloques de §6 con wikilinks a §4bis (qué se crea) y §7 (cómo se prueba).
- **§7 Pruebas** → las 10, con las 3 nuevas: "no agendo fuera del horario del schedule del event type
  elegido", "el evento cae en el calendario profesional y no en otro", "el personal aparece como
  ocupado sin exponer el título".
- **§8 Riesgos y rollback** → rollback en 1 minuto.
- **§9 Preguntas** → **respondidas** (hoja única, el bot solo agenda y avisa por mail, la memoria la ve
  solo Sol, credenciales resueltas, calendarios definidos).
- **§10 Trazabilidad** → tabla de lo hecho en la sesión (IDs de workflows, event types, schedule,
  credenciales tocadas, `chat_id` leídos).

### 7.3 `specs/261019-plan-agentes-telegram-agenda-emilia.md`

- §2 PLAN: la carga de la semana cambia (C1.2 y C3.2 pasan a "crear 3 event types + schedule por API"
  y "compartir calendarios + 1 clic de autorización").
- §3 TASKS: reescribir **B2** (credencial de Calendar → *compartir + 1 clic de autorización*),
  **C1.2** (*crear 3 event types + schedule 24/7 por API*), **C3** (*definir los 2 calendarios que lee
  el bot*), **C1b** (agregar los 3 event types y el `chatId` dinámico al clon) y **D2** (el guion nuevo).
- §4 MILESTONES: M-A2 reescrito con los 3 event types + el `chat_id` + 1 reserva real como criterio.
- §5 Leantime: actualizar el `planHours` de las cards tocadas.
- §6 Preguntas: las 7 respondidas.
- §7 Fuentes: sumar el playbook y la sesión.

### 7.4 `proyectos/MVP_06-agente-voz/documentacion/credenciales-conexiones.md`

- Fila nueva: *Calendar de Emilia (compartido con `proyectopi`)* → credencial `Google Calendar account`
  → **sin mantenimiento** (se comparte, no se renueva) → condición de salida: si Emilia revoca, el bot
  pierde la lectura de agenda y sigue agendando.
- Fila `Google Calendar account`: aclarar que es de `proyectopi.31416@gmail.com` y que además lee los
  calendarios compartidos por Emilia.
- Corregir la fila `ppi-EmiliaOS_*` → "cuenta real: `proyectopi.31416@gmail.com`".
- Cadencia: **mensual** (15 min) + el trigger real (exec con 401/403).

### 7.5 `proyectos/MVP_06-agente-voz/documentacion/onboarding-emilia-perfiles.md`

Reconciliar con la decisión de clones: título → *"Onboarding Emilia al agente de voz — 2 clones,
1 trigger"*; explicar por qué se descarta el "1 agente N perfiles" (el riesgo de la tool equivocada);
apuntar al playbook y al doc de configuración.

### 7.6 Sesión y log

- NUEVO `raw/sessions/2026-10-19-sesion-playbook-google-event-types.md` — análisis cerebro-digital.
- `log.md` — 2 entradas nuevas arriba (19/10): playbook Google + event types/arquitectura.

---

## 8 · Orden de ejecución

1. `playbook-google-oauth-emilia.md` (nuevo) — desbloquea todo lo demás.
2. `config-agente-agenda-emilia.md` (reescritura) — el guion del miércoles.
3. `specs/261019-plan-agentes-telegram-agenda-emilia.md` — tareas y cards.
4. `credenciales-conexiones.md` + `onboarding-emilia-perfiles.md` — coherencia del vault.
5. Sesión + `log.md`.

**HITL:** los pasos 1-5 tocan el vault → requieren `s` de Sol. La creación de event types y del
schedule **no se ejecuta desde acá** (403 de Cloudflare): se hace en la sesión del 21/10 desde n8n,
con la API key que ya está en la credencial.

---

## 9 · Decisiones de Sol (21/10 → registro en los docs)

| Decisión | Dónde |
|---|---|
| Calendar personal en **otra cuenta** (gmail personal) | §3 |
| El bot lee **profesional (detalles) + personal (free/busy)** | §3 |
| Las reservas caen en el **calendario profesional** | §3 |
| En Cal.com **solo el profesional bloquea** | §3 |
| **ET-C oculto**, solo el bot lo usa | §4 |
| **ET-C 24/7 real** con schedule propio, notice 0, sin límites | §4 |
| ET-C duraciones **60/120/180** (hasta 3 horas) | §4 |
| Los 3 event types con **1, 2 y 3 horas** | §4 |
| ET-C se ofrece **solo cuando ella lo pide** | §4 |
| **ET-A con dirección fija** del estudio (la carga Sol en la sesión) | §4 |
| **7109200 queda como backup** | §4 |
| Los event types se crean con **workflow temporal en n8n** | §6 |
| La app de Cal.com se intenta **por API desde n8n** | §6 |
| Orden del miércoles: **1 event types, 2 conectar app** | §6 |
| **Hoja única** `clientes-contactos` | §5 |
| El bot **solo agenda**; el aviso al invitado lo manda Cal.com | §4 regla 10 |
| La **memoria la abre solo Sol** (Postgres del VPS) | §5 |
| **2 clones, 1 trigger** (no 1 agente multi-perfil) | §2 |

**Abierta para la sesión del 21/10:** confirmar que `OS.emi-pi` **es** `emiliaospi_bot` (§2) y leer su
`chat_id`; y la dirección del estudio para ET-A.

---

## 10 · Verificación antes de dar por cerrado

- [ ] Los 6 archivos escritos, UTF-8 sin caracteres de reemplazo, wikilinks absolutos sin extensión.
- [ ] Los JSON de event type del doc son copiables y ejecutables (validar contra la API en la sesión).
- [ ] `log.md` y `raw/sessions/` con la entrada del 19/10.
- [ ] `git status` sin archivos ajenos tocado.
