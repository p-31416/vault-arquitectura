---
tipo: documentacion
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha_creacion: 2026-10-19
ultima_actualizacion: 2026-10-19
tags: [n8n, agente-voz, agenda, cal-com, google-calendar, credenciales, sesion-presencial, miercoles, studio-os]
idioma: es
---

# Configurar el agente de agenda de Emilia — sesión presencial del miércoles 21/10

> Documento operativo de la cita presencial del **miércoles 21/10 a las 13:00**. Objetivo: dejar **el agente de Emilia con sus propios datos de Cal.com y de Google Calendar**, con la misma arquitectura que hoy usa Sol en n8n — **un agente (Voz) + un subagente-subflujo (Agenda)** — pero con el perfil de Emilia cableado y probado.
>
> Contexto: la reunión del 16/10 20:33 ([[raw/reuniones/2026-10-16_emilia-proyectopi_193660891|transcript 193660891]]) dejó el compromiso de "conectar la cuenta de cal.com de Emilia" y "conectar su calendario de Google" en esa cita. Arquitectura de referencia: [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura n8n OS-Emilia v2.0]] · [[proyectos/STUDIO_OS-Emilia/documentacion/resumen-flujo-agenda-sub|resumen flujo Agenda Sub]] · [[proyectos/STUDIO_OS-Emilia/documentacion/resumen-flujo-voz|resumen flujo Voz]] · [[proyectos/MVP_06-agente-voz/documentacion/onboarding-emilia-perfiles|onboarding por perfiles]] · [[proyectos/MVP_06-agente-voz/documentacion/credenciales-conexiones|credenciales y conexiones]].
>
> Tareas ejecutoras: [[specs/261019-plan-agentes-telegram-agenda-emilia|plan agentes + agenda]] (M-A2) · Sprint en el proyecto Leantime `O.S_ARQ-Emi` (id 4).

---

## 1 · Objetivo y criterio de aceptación

**Objetivo:** que el bot que Emilia usa desde el celu agende, mueva y cancele reuniones **en la cuenta de Cal.com de Emilia**, consultando **el Google Calendar de Emilia**, con su `chat_id` identificado y con respuestas en su propio calendario — sin que Sol tenga que intervenir.

**Criterio de aceptación (checklist verificable el mismo día):**

- [ ] Emilia recibe en su chat privado un mensaje del bot `emiliaospi_bot` que la reconoce por nombre (no la caída a comandos).
- [ ] `consultar_disponibilidad` devuelve slots **de la cuenta de Cal.com de Emilia** (event type de 60 min con Meet).
- [ ] `leer_calendario` devuelve eventos **del calendario de Emilia** (no los de `proyectopi.31416@gmail.com`).
- [ ] 1 reserva real creada desde el chat de Emilia, con link de Meet y mail al invitado.
- [ ] Esa misma reserva mueve (`reschedule`) y cancela desde el bot, con el `bookingUid` correcto.
- [ ] La memoria de la conversación queda aislada por `chat_id` (la de Sol no se mezclan).
- [ ] 0 secretos escritos en el vault, en el repo o en mensajes: viven solo en credenciales n8n cifradas.

## 2 · Arquitectura objetivo

Hoy el sistema es de **Sol** (perfil TEST). Para Emilia se clonan los 2 workflows de voz y se los cablea con sus datos. El Fathom Core y el Telegram Router quedan compartidos (no se tocan salvo el Router, que suma una rama).

```
┌─ Telegram (bot emiliaospi_bot) ───────────────────────────────────────────┐
│  Recibo Mensaje  (Router YWpuV5p0vCDTbIHz · trigger ÚNICO del token)     │
│  ├─ Route Identidad                                                      │
│  │   ├─ chat_id Sol      8459099332 → Run Voz Agent (Sol)      Gpd6NHB4HQdU7ary
│  │   └─ chat_id Emilia   <NUEVO>   → Run Voz Agent Emilia     <CLON>      ← rama nueva
│  └─ Route Fuentes Group (-5417177870) → Inbox de enlaces (Sheet)          │
└───────────────────────────────────────────────────────────────────────────┘
                                    │
      ┌─────────────────────────────▼──────────────────────────────┐
      │ OS-Studio — Agent Voz Emilia  (clon de Gpd6NHB4HQdU7ary)    │
      │ ExecuteWorkflowTrigger → STT Gemini → lote Redis → Agente   │
      │ (OpenRouter gpt-5.6-luna + memoria Postgres) → Responder    │
      │ Tools: Tool Agenda (→ subflujo) · buscar_contacto ·         │
      │         agregar_contacto · Tool Sincronizar Fathom          │
      └─────────────────────────────┬──────────────────────────────┘
                                    │ ExecuteWorkflow (query en lenguaje natural)
      ┌─────────────────────────────▼──────────────────────────────┐
      │ OS-Studio — Agenda Sub Emilia (clon de ygdjqRfXpxKMFWEN)    │
      │ Agente (OpenRouter) + 7 tools:                              │
      │   consultar_disponibilidad · obtener_reuniones ·            │
      │   agendar_online · agendar_presencial · actualizar_reunion · │
      │   cancelar_reunion · leer_calendario                        │
      │ Credenciales: Cal.com de Emilia + Google Calendar de Emilia  │
      └────────────────────────────────────────────────────────────┘
```

**Por qué clonar y no un único agente con dos perfiles.** La credencial en n8n no admite expresiones: cada llamada externa necesita una credencial fija. Un agente con perfiles obligaría a duplicar cada una de las 7 tools de agenda detrás de un Switch por perfil (mismo costo de mantenimiento que clonar, con más riesgo de cruce entre perfiles). El mecanismo de perfiles documentado en [[proyectos/MVP_06-agente-voz/documentacion/onboarding-emilia-perfiles|onboarding por perfiles]] sirve cuando los perfiles comparten credenciales; acá cada uno tiene la suya. Se mantiene **1 agente + 1 subflujo por persona**, misma forma que el patrón `LidIA_V5.0-SWF_Agenda` (`w8iMJ01WGCSxvSMg`).

**Regla de oro que se mantiene:** mover o cancelar **siempre desde el bot o desde Cal.com**, nunca desde Google Calendar — desde Google el `bookingUid` queda huérfano y la cancelación rebota (verificado 15/10).

## 3 · Credenciales y claves a pedir (bloque para la sesión)

> Los secretos viajan en la UI de n8n, de una persona a otra, cara a cara. En el vault solo quedan **nombres y IDs públicos**.

### 3.1 Lo que hay que pedirle a Emilia (3 cosas)

| # | Qué pedir | Dónde lo obtiene Emilia | Dónde se carga | Credencial n8n |
|---|---|---|---|---|
| **P1** | **API key de Cal.com (v2)** de su cuenta | cal.com → *Settings → Integrations → API Keys → Add API key* → Cal.com API v2 (lectura + escritura) | n8n → Credentials → Editar `ppi-EmiliaOS_Cal.com.Bearer Auth account` → campo *Bearer Token* | `ppi-EmiliaOS_Cal.com.Bearer Auth account` (`3MvZXPNH8LrDYPZS`) — **ya existe**, se reutiliza; si la key vigente está vencida o es de otra cuenta, se regenera y se reemplaza el token |
| **P2** | **Autorizar Google Calendar** de su cuenta | Nada que traer: en n8n → Credentials → New → *Google Calendar* → OAuth2 → *Connect* → Emilia inicia sesión con su Google y acepta el permiso de calendario | n8n → credencial nueva | `emilia-Google Calendar` (nueva, a crear el mismo día) — la existente `Google Calendar account` (`3wo33TixNfgYPeJY`) pertenece a `proyectopi.31416@gmail.com` y se deja intacta |
| **P3** | **Definir sus calendarios** (profesional / personal) y **qué evento de Cal.com** se agenda | Cal.com → *Event Types*: verificar `7109200` (30 min) y crear/ajustar **"Reunión de 60 min"** con Google Meet por defecto, Horarios Lun-Vie | n8n → nodo `leer_calendario` (campo *Calendar*) + nodo `obtener_reuniones` (*eventTypeId*) | — |

**Datos que se leen solos, sin pedirlos:**
- **`chat_id` de Emilia**: lo entrega el bot en su primera ejecución. Se lee en n8n → *Executions* → el trigger `Recibo Mensaje` de la sesión del miércoles (campo `message.chat.id`) y se pega en la rama del Router. Es el mismo número que aparece en la URL del chat (`t.me/<bot>` → el ID numérico) o en el mensaje de `/start`.
- **Su mail de Google** (para el campo *Calendar* de la tool): `arq.emiliapimentalombardi@gmail.com`.

### 3.2 Credenciales que reusan las que ya están (no se piden nada)

| Credencial n8n | ID | Rol en el perfil Emilia |
|---|---|---|
| `emiliaospi_bot-Telegram account` | `PqGQSTIshKSriHOm` | Trigger, envío de respuestas, descarga de audio |
| `Google Gemini(PaLM) Api account` | `ST3rNoKVMZGOSppJ` | STT de notas de voz (`gemini-2.5-flash-lite`) |
| `OpenRouter account` | `F3k0GtQqqEJqBGjl` | Modelo del agente y del subagente (`openai/gpt-5.6-luna`) |
| `Redis account` | `dySiFumFmvckOGdn` | Lote de mensajes (key nueva por perfil) |
| `Postgres account` | `mmwdgjWdYmF7aBUe` | Memoria de la conversación (tabla nueva por perfil) |
| `ppi-EmiliaOS_Google Sheets account` | `yb1G3uAHS2QqK1wu` | `buscar_contacto` / `agregar_contacto` sobre la hoja `clientes-contactos` (`1t9-j_7gJypLOicaJNpwYWLsBy0VDtSmdBJZumW8jtVA`) — **reconectar** si figura caída |
| `ppi-EmiliaOS_Fathom` | `mAaHtYoCUcSj0via` | Tool *Sincronizar Fathom* (no es foco del miércoles) |

### 3.3 Recursos a crear antes de la cita (10 min, Sol)

- [ ] Tabla Postgres `studio_os_emilia` (misma estructura que `studio_os_test`) — la crea quien administra el Postgres del VPS.
- [ ] Confirmar que la credencial de Sheets `ppi-EmiliaOS_Google Sheets` está conectada (n8n → Credentials → muestra *Reconnect* si expiró el OAuth).
- [ ] Confirmar saldo de OpenRouter (el agente del subflujo corre en cada consulta de slots).
- [ ] Verificar que el bot `emiliaospi_bot` responde (n8n → Executions del Router: `Recibo Mensaje` con ok).

## 4 · Cambios nodo a nodo

### 4.1 Subflujo `OS-Studio — Agenda Sub Emilia` (clon de `ygdjqRfXpxKMFWEN`, 12 nodos)

| Nodo | Cambio | Valor |
|---|---|---|
| `Agenda TEST Trigger` | Renombrar | `Agenda Emilia Trigger` — input `query` (string) |
| `Agende Agenda TEST` → `Agente Agenda Emilia` | System prompt | Cambiar "operador de agenda" por "operador de agenda de Emilia" + su `eventTypeId` por defecto en el prompt |
| `Modelo Agenda TEST` | Sin cambio | OpenRouter `openai/gpt-5.6-luna` |
| `Memoria Agenda TEST` | Opcional | Dejar `sessionKey = {{ $execution.id }}` (memoria de una sola ejecución, sin estado entre llamadas) |
| `consultar_disponibilidad` | **Credencial** | `ppi-EmiliaOS_Cal.com.Bearer Auth account` (en vez de `ppi_calcom-Bearer Auth account`). `eventTypeId` llega por `$fromAI` → el subagente debe pasarlo (ver §4.3) |
| `obtener_reuniones` | **Credencial** + **`eventTypeId`** | `ppi-EmiliaOS_Cal.com…` + `eventTypeId` = `<ID del evento de Emilia>` (en vez del `7467793` de Sol). `take` 100 |
| `agendar_online` | **Credencial** | `ppi-EmiliaOS_Cal.com…` · body: `attendee.timeZone = America/Argentina/Buenos_Aires` · `metadata.origen` = `OS-Emilia` |
| `agendar_presencial` | **Credencial** | ídem + `location` en texto plano (el evento debe tener `attendeeDefined` habilitado) |
| `actualizar_reunion` | **Credencial** | ídem · POST `/v2/bookings/<uid>/reschedule` (solo horario; cambio de duración = cancelar + reagendar) |
| `cancelar_reunion` | **Credencial** | ídem · POST `/v2/bookings/<uid>/cancel` |
| `leer_calendario` | **Credencial** + **Calendar** | `emilia-Google Calendar` (nueva) + `arq.emiliapimentalombardi@gmail.com` (o el calendario profesional que defina Emilia) |
| Sticky notes | Conservar los 3 | Sirven de mapa del clon (patrón, credenciales, reglas) |

Headers que ya funcionan y se respetan: `cal-api-version: 2024-08-13` en bookings y `2024-09-04` en `/v2/slots` (el endpoint de slots exige la versión nueva). Body de booking: `eventTypeId`, `start` ISO, `lengthInMinutes` (30/60/180 según el evento), `attendee {name, email, timeZone}`, `metadata {cliente, resumen, origen}`.

### 4.2 Agente `OS-Studio — Agent Voz Emilia` (clon de `Gpd6NHB4HQdU7ary`, 26 nodos)

| Nodo | Cambio | Detalle |
|---|---|---|
| `Voz Agent Trigger` | Sin cambio | Sigue siendo `executeWorkflowTrigger`; lo invoca el Router (nada de trigger de Telegram propio: se le robaría el webhook al Router) |
| `Detectar Entrada` (Code) | **Allowlist** | Cambiar la constante `8459099332` por el `chat_id` de Emilia. Se acepta una lista de dos IDs si se quiere que ambos Operen desde el mismo workflow |
| `Tipos Entrada` (Switch) | Sin cambio | 4 ramas: audio / texto / callback / rechazada |
| `Descargar Voz`, `Transcribir Voz`, `Fijar Texto*`, `Normalizar W02`, `Fijar Contexto` | Sin cambio | Misma cadena STT |
| `Guardar Mensaje` (Redis) | **Key** | `studio_os_emilia_<chat_id>` (hoy `studio_os_test_8459099332`) |
| `Esperar Lote` / `Recuperar Lote` / `Es Ultimo Mensaje` / `Armar Lote` / `Limpiar Lote` | **Key** | Misma key en los 3 nodos Redis |
| `Agente Voz TEST` → `Agente Voz Emilia` | **System prompt** | "Sos el asistente de agenda de **Emilia**" + su `eventTypeId` + su calendario. Mantener: responder en 2-3 líneas rioplatenses, 1 pregunta por vez, `buscar_contacto` primero, validar slots antes de proponer horario, email siempre obligatorio, resumen + confirmación antes de escribir |
| `Memoria Postgres TEST` | **Tabla** | `tableName = studio_os_emilia` (la sesión ya se separa sola por `chat.id`) |
| `Tool Agenda` | **Apunta al clon** | `workflowId` = ID del nuevo `OS-Studio — Agenda Sub Emilia` |
| `Tool Sincronizar Fathom` | Opcional | Apunta al Fathom Core `UeDkqVZSeLnae5cF` (sin cambios) |
| `buscar_contacto` / `agregar_contacto` | **Hoja** | `clientes-contactos` `1t9-j_7gJypLOicaJNpwYWLsBy0VDtSmdBJZumW8jtVA`, credencial `ppi-EmiliaOS_Google Sheets` |
| `Responder Telegram` | **chatId** | Hoy está fijo en `8459099332` → pasar a `={{ $('Fijar Contexto').item.json.ID_Chat }}` (o `$json.ID_Chat`), para que la respuesta caiga en el chat de quien escribió |
| `Modelo Free TEST` | Sin cambio | `openai/gpt-5.6-luna` |

### 4.3 Router `OS-Emilia — Telegram Router` (`YWpuV5p0vCDTbIHz`)

- **Agregar** una segunda regla en `Route Identidad`: `chat_id == <chat_id de Emilia>` → salida nueva `Emilia`.
- **Agregar** el nodo `Run Voz Agent Emilia` (`executeWorkflow`, input `update` = `{{ $json }}`, `waitForSubWorkflow: true`) apuntando al clon del agente.
- **No tocar** el trigger `Recibo Mensaje`: sigue siendo el único del token `emiliaospi_bot`.
- **No tocar** la rama del grupo Fuentes ni `/sync` y `/help`.
- **Ojo:** mientras la rama de Emilia no exista, sus mensajes caen en *Resto* → *Route Telegram Command* → `/help`. Ese mensaje de error es el que sirve para detectar el `chat_id`.

### 4.4 Tool set para "manejar todos los datos de calendario y Cal.com"

El set de 7 tools cubre agendar, modificar, cancelar y listar. Para que el agente "maneje todos los datos", se suman dos capacidades al clon (son el mismo patrón `httpRequestTool` con `genericAuthType: httpBearerAuth`):

| Tool nueva | Endpoint | Para qué |
|---|---|---|
| `listar_bookings` | `GET /v2/bookings` **sin** `eventTypeId` + `take` + `status=accepted` | Traer **todas** las reuniones de la cuenta de Emilia (no solo las de un evento), para la revisión semanal de agenda |
| `buscar_disponibilidad_calendario` | `GET /v2/slots` con `start`/`end`/`timeZone` + `GET` de eventos ocupados del Google Calendar de Emilia | Cruzar la disponibilidad de Cal.com con lo que ya está en su calendario manual (el `leer_calendario` ya lee el Google; el subagente cruza ambos) |

Y un tercer movimiento, de orden interno: **agenda unificada** — el subagente lee Cal.com **y** Google Calendar y deduplica por fecha+título antes de listar (mismo criterio que usa hoy el Core de Fathom para evitar duplicados entre cuentas).

## 5 · Guion de la sesión del miércoles (13:00, presencial, ~2 h)

| # | Bloque | Quién | Min | Resultado |
|---|---|---|---|---|
| 1 | Apertura: qué hace el bot y qué se va a dejar andando | Sol | 10 | Emilia sabe qué va a poder hacer desde el celu |
| 2 | **P2**: Emilia autoriza Google Calendar desde la UI de n8n | Emilia + Sol | 20 | Credencial `emilia-Google Calendar` conectada |
| 3 | **P1**: Emilia genera la API key de Cal.com y la pega en la credencial | Emilia + Sol | 15 | `ppi-EmiliaOS_Cal.com` con el token de su cuenta |
| 4 | **P3**: Emilia revisa sus eventos en Cal.com y su calendario en Google; se define cuál se agenda | Emilia | 15 | `eventTypeId` + calendario definidos y anotados |
| 5 | Sol clona los 2 workflows y cablea los 20+ parámetros del §4 | Sol | 45 | Los 2 workflows activos con perfil Emilia |
| 6 | Sol agrega la rama de Emilia en el Router con el `chat_id` leído de la ejecución | Sol | 15 | Emilia entra al camino del agente |
| 7 | Prueba en vivo: voz "agendame mañana a las 10 con X" → slots → confirmación → reserva → mover → cancelar | Emilia + Sol | 25 | Los 7 criterios de aceptación del §1 |
| 8 | Cierre: qué queda funcionando, qué pendiente, quién lo toma | Ambos | 10 | Lista escrita con dueño y fecha |

**Orden de ejecución dentro del bloque 5** (cada cambio se publica antes del siguiente; n8n no ejecuta borradores): clonar → renombrar → credenciales → parámetros → `Publish` → probar nodo a nodo.

## 6 · Pruebas de aceptación (checklist de la sesión)

| # | Prueba | Cómo se verifica | Resultado esperado |
|---|---|---|---|
| T1 | El bot la reconoce | Emilia escribe "hola" en su chat privado | Respuesta conversacional en 2-3 líneas, no el `/help` |
| T2 | Identidad | Se mira la ejecución del Router | `Route Identidad` cae en la salida **Emilia** |
| T3 | Slots de su cuenta | El agente pide un horario | La tool devuelve slots del `eventTypeId` de Emilia (no el de Sol `7467793`) |
| T4 | Calendario | El agente lista la agenda de la semana | Trae eventos de **calendario de Emilia** (no de `proyectopi.31416@gmail.com`) |
| T5 | Reserva real | "Agendame mañana 10:00 con [nombre] [email]" | Reserva creada, mail al invitado, link de Meet, `bookingUid` en la respuesta |
| T6 | Reprogramar | "Cambiala a las 15" | `reschedule` OK sobre el mismo `bookingUid` |
| T7 | Cancelar | "Cancelala" | `cancel` OK; la reserva desaparece de Cal.com |
| T8 | Memoria aislada | Se relee el historial | El agente de Emilia no ve ni menciona reuniones de Sol |
| T9 | Contactos | "Agendame con [cliente del Sheet]" | `buscar_contacto` devuelve el contacto y el mail se completa solo |
| T10 | Higiene | Revisión del vault y del repo | 0 tokens, 0 claves, 0 `bookingUid` escritos en el vault |

## 7 · Riesgos y plan de rollback

| Riesgo | Mitigación |
|---|---|
| **Trigger duplicado**: crear un trigger de Telegram en el clon rompe el webhook del Router | El clon conserva solo `executeWorkflowTrigger`; verificación: en el Router, *Executions* sigue recibiendo mensajes |
| **Credencial vencida de Sheets** | Reconectar en la UI antes de la cita (bloque 0 del §3.3) |
| **403 de Cal.com** (CDN bloquea por IP/origen) | Si la API responde 403 desde el VPS, se reintenta desde la instancia n8n (que es quien llama) y se deja registro en la ejecución |
| **`eventTypeId` equivocado** | El `eventTypeId` se lee de la respuesta del propio Cal.com en la sesión, no de memoria; el subagente lo recibe por `$fromAI` |
| **Perfil mezclado** | Redis, Postgres y credenciales con sufijo `emilia`; T8 lo detecta |
| **Regresión en Sol** | Los workflows de Sol no se editan: se clonan. Rollback = desactivar la rama Emilia del Router (1 nodo) y, si hace falta, el clon |

**Rollback en 1 minuto:** en el Router, `Route Identidad` → dejar la regla de Emilia sin salida (o desactivar el nodo `Run Voz Agent Emilia`) → publicar. El sistema vuelve al estado previo sin tocar los workflows de Sol.

## 8 · Preguntas que se resuelven en la sesión

1. **¿Qué calendarios** entra Emilia al agente: solo el profesional, o también el personal? (define el campo *Calendar* de `leer_calendario`).
2. **¿Una duración única o varias?** Si el evento de 60 min con Meet alcanza, el agente propone siempre 60; si quiere variety, se deja que `$fromAI` elija entre las duraciones habilitadas del evento.
3. **¿Dónde vive la agenda de los clientes** — la misma hoja `clientes-contactos` que usa Sol, o una copia propia del estudio? Afecta a `buscar_contacto`.
4. **¿El bot le escribe al invitado o solo lo agenda?** El comportamiento por defecto agenda y Cal.com avisa por mail; una fila en la agenda puede ser un evento interno que ella prefiera confirmar a mano.
5. **¿Quién ve la memoria de la conversación?** Hoy queda en Postgres del VPS, sin panel; si Emilia quiere leerla, se abre una vista o un export.

## 9 · Trazabilidad

- **Workflows clonados:** `OS-Studio — Agenda Sub Emilia` (de `ygdjqRfXpxKMFWEN`) y `OS-Studio — Agent Voz Emilia` (de `Gpd6NHB4HQdU7ary`). Sus IDs se anotan acá apenas se creen.
- **Workflow compartido con cambios mínimos:** `OS-Emilia — Telegram Router` (`YWpuV5p0vCDTbIHz`) — 1 rama nueva.
- **Sin tocar:** Fathom Core (`UeDkqVZSeLnae5cF`), SET_01 (`VIQmMEZ9tkDBfKjd`), workflows `LidIA_*`.
- **Tareas del plan:** [[specs/261019-plan-agentes-telegram-agenda-emilia|plan agentes + agenda]] — B2 (credencial de Calendar), C1 (cal.com), C2 (`chat_id`), C3 (calendario + evento), D2 (cita del miércoles). Este documento es el guion que las ejecuta.
