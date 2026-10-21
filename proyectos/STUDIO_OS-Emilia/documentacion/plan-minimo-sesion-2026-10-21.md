---
tipo: log
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [n8n, cal-com, emilia, os-studio, sesion-2026-10-21, agenda]
---

# Plan mínimo — sesión con Emilia (miércoles 21/10, 13:00)

Objetivo: que Emilia use **mañana mismo** el bot de agenda, con **sus** datos y **su** cuenta Cal.com. Todo lo que sigue ya está armado y probado; mañana quedan **3 clics y 2 textos**.

Complementa [[proyectos/STUDIO_OS-Emilia/documentacion/config-agente-agenda-emilia]] (guion de la sesión) y [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia]] (mapa técnico del stack).

---

## 0. Estado del VPS: volvió y quedó verificado

El **20/10 a la tarde el VPS `pitau.tech` (89.117.73.109) se cayó entero** (n8n, Leantime y el panel de EasyPanel viven en la misma IP; GitHub seguía respondiendo, así que no era la conexión del estudio). **Volvió durante la noche** y el 21/10 se verificó todo:

| Workflow | ID | Carpeta | Estado verificado |
|---|---|---|---|
| OS-Studio — Agenda Sub Emilia | `2JogeOoT3Wjq2ncH` | OS-Emilia / MVP06-Agente_Voz_telegram | activo · movimiento de carpeta **completado** |
| OS-Studio — Agenda Dispatcher | `CVvxZgn0AipO6dV0` | OS-Emilia / MVP06-Agente_Voz_telegram | activo · movimiento de carpeta **completado** |
| OS-Studio — Agent Voz TEST (revision) | `Gpd6NHB4HQdU7ary` | OS-Emilia / MVP06-Agente_Voz_telegram | activo, versión `fae63d66` = activa |
| OS-Emilia — Telegram Router | `YWpuV5p0vCDTbIHz` | OS-Emilia | activo, versión `1c745d12` = activa |

Pruebas hechas después de que volviera:

- **Cadena de Emilia** (mensaje simulado con su chat) → detector → agente → Dispatcher → **Agenda Sub Emilia** → respuesta correcta ✓ (el único error es Telegram "chat not found", porque el id de prueba no existe).
- **Cadena de Sol** → responde con su agenda, y `leer_calendario` **sigue trayendo su Google Calendar** (la credencial de Google sobrevivió al reinicio) ✓.
- **Leantime** volvió con las **15 h** ya cargadas ✓ (no se perdió nada).
- Los 3 event types de Emilia viven en Cal.com (servicio externo) → intactos ✓.

Los pendientes quedaron **anotados en la descripción de cada workflow** (se ven en la lista de n8n):

- Router → *"PENDIENTE 21/10: la regla 2 usa el placeholder 999999999 → reemplazar por el chat_id real de Emilia"*
- Agent Voz → *"PENDIENTE 21/10: allowlist de Detectar Entrada con placeholder 999999999 → chat_id real de Emilia"*
- Agenda Sub Emilia → *"PENDIENTE: dirección del estudio y compartir su calendario con proyectopi.31416@gmail.com"*

> Si el bot no respondiera después del reinicio, el arreglo es: desactivar y **volver a publicar** el Router (re-registra el webhook de Telegram). La credencial de Google y la de Cal.com no se ven afectadas.

---

## 1. Estado real al 20/10 (ya hecho y verificado)

### 1.1 Cal.com de Emilia — cuenta lista

Credencial usada: `ppi-EmiliaOS_Cal.com.Bearer Auth account` (cuenta "Emilia Pimenta Lombardi", `userId 3251516`, perfil `emilia-pimenta-lombardi-ctcojl`).

| ID | Event type | Modo | Duración | Anticipación | Schedule | Estado |
|---|---|---|---|---|---|---|
| **7563141** | Reunion presencial - Estudio | `address` (dirección del estudio) | 60 min | 120 min | default (L-V 9-17) | slots OK · falta dirección |
| **7563142** | Reunion online - Estudio | `google-meet` | 60 min | 120 min | default (L-V 9-17) | **slots OK** (8/día, 09-16) |
| **7563143** | Disponibilidad libre | `google-meet`, oculto | 60 min | 0 | default (L-V 9-17) | falta asignarle el 24/7 |
| 2527411 | *schedule* "Disponibilidad 24/7" (Lun-Dom 00:00-23:59) | — | — | — | — | creado, **sin asignar** |
| 7109200 | Reunión de 60 min (el que ya usaba) | google-meet | 60 min | 120 | default | intacto, queda de backup |
| 7109198 / 7109199 | 15 min / Secreta | daily | 15 | 120 | default | intactos |

**Hallazgo que simplifica la sesión:** el Google Calendar de Emilia **ya está conectado** en Cal.com (`arq.emiliapimentalombardi@gmail.com`, `credentialId 2605522`) y es el *destination calendar*. Por lo tanto:

- las reservas **ya caen en su calendario de Google** (no hay que autorizar nada),
- Cal.com **ya le resta sus ocupados** al calcular slots (no hace falta el free/busy del calendario personal).

→ **Mañana no hay ningún click de OAuth.** Ese paso, que era el más frágil del plan original, quedó descartado por los hechos.

### 1.2 n8n — un flujo por persona

| Workflow | ID | Rol |
|---|---|---|
| OS-Emilia — Telegram Router | `YWpuV5p0vCDTbIHz` | **único trigger de Telegram** (1 webhook por bot) → reparte: tu chat, el grupo Fuentes, /sync, /help, y el chat de Emilia |
| OS-Studio — Voz Dispatcher | `Msh31moofBKBwZId` | **nuevo**: decide a qué flujo de voz va el mensaje según el `chat_id` (`8459099332` → Sol; el resto → Emilia) |
| OS-Studio — Agent Voz TEST (revision) | `Gpd6NHB4HQdU7ary` | **el tuyo**: Telegram (voz+texto), Redis `studio_os_test_8459099332`, memoria `studio_os_test`, Tool Agenda → tu Agenda Sub |
| OS-Studio — Agent Voz Emilia | `Fa2AlIDqUntSWMrw` | **el de ella** (nuevo): Telegram (voz+texto), Redis `studio_os_emilia_<chat_id>`, memoria `studio_os_emilia`, Tool Agenda → su Agenda Sub, tool de Fathom con source propio |
| OS-Studio — Agenda Sub TEST | `ygdjqRfXpxKMFWEN` | **el tuyo**: agente Cal.com contra tu cuenta (ET 7467793) |
| OS-Studio — Agenda Sub Emilia | `2JogeOoT3Wjq2ncH` | **el de ella**: agente Cal.com con las 7 tools contra su cuenta (ET 7563141/42/43) |

> **Cambio de arquitectura (21/10):** se pasó de "1 flujo de voz compartido + dispatcher de Cal.com" a **1 flujo completo por persona** (agente de voz y subagente de agendamiento propios), con un **despachador de flujos** que decide por `chat_id`. Motivo: cada persona queda con sus datos (Redis, memoria, credencial de Cal.com, prompt) sin compartir nada, y el `chat_id` deja de viajar "disfrazado" dentro del pedido en lenguaje natural. El `OS-Studio — Agenda Dispatcher` (intermedio) quedó **archivado**.

**Aislamiento real:** la credencial de Cal.com vive **dentro** de cada subagente de agenda, no en el agente de voz. Aunque los dos agentes compartieran el mismo modelo, ninguno puede agendar en la cuenta del otro.

### 1.3 Pruebas ya ejecutadas (20-21/10)

| Prueba | Resultado |
|---|---|
| Agenda Sub Emilia: "listame las reuniones de esta semana" | el agente llamó `obtener_reuniones` con los **3 ET IDs correctos** (7563142, 7563141, 7563143) y respondió ✅ |
| Agent Voz Emilia: mensaje simulado de su chat | detector → agente → **Tool Agenda Emilia** → su Cal.com → respuesta correcta ✅ |
| Voz Dispatcher con chat `999999999` | enrutó a **Run Voz Emilia** y la cadena completa respondió ✅ |
| Voz Dispatcher con tu chat `8459099332` | enrutó a **Run Voz Sol** y el bot **te envió un Telegram real** (`message_id 277`) con tu agenda ✅ |
| Regresión de Sol | su agenda sigue salir de su Cal.com + su Google Calendar (`leer_calendario` OK) ✅ |
| Restauración de tu flujo | Tool Agenda vuelve a apuntar directo a tu Agenda Sub (sin dispatcher ni marcador `[chat:ID]`), y tu clave Redis vuelve a `studio_os_test_8459099332` (para que `Limpiar Memoria TEST` siga funcionando) ✅ |

### 1.3 Pruebas end-to-end ya ejecutadas (20/10)

| Prueba | Resultado |
|---|---|
| Agenda Sub Emilia: "listame las reuniones de esta semana" | el agente llamó `obtener_reuniones` con los **3 ET IDs correctos** (7563142, 7563141, 7563143) y respondió ✅ |
| Dispatcher con `[chat:999999999]` | enrutó a **Run Agenda Emilia** (sub-ejecución `2JogeOoT3Wjq2ncH`) ✅ |
| Flujo de voz completo con chat de Emilia | detector → agente → Dispatcher → Agenda Sub Emilia → respuesta correcta ✅ (el único error fue Telegram "chat not found" porque el id de test no existe) |
| Flujo de voz completo con chat de Sol (8459099332) | **regresión OK**: enrutó a la cuenta de Sol y respondió con su agenda real (Lun 19: 10:00 Emilia Pimenta + 14:00 Delfi CAD · Mar 20: 18:00 Clase Mora) ✅ |

---

## 2. Lo único que falta mañana (≈ 12 minutos)

| # | Qué | Dónde | Tiempo |
|---|---|---|---|
| **1** | Cargar el `chat_id` real de Emilia | 2 lugares (abajo) | 2 min |
| **2** | Cargar la dirección del estudio | Event type 7563141 → location | 2 min |
| **3** | Compartir el calendario profesional de Emilia con la cuenta del estudio | Google Calendar → `arq.emiliapimentalombardi@gmail.com` → compartir con `proyectopi.31416@gmail.com` | 1 min |
| 4 | *opcional*: duraciones 120/180 en los 3 event types | Cal.com → cada ET → duración | 3 min |
| 5 | *opcional*: asignar el schedule 24/7 al ET libre (7563143) | Cal.com → ET 7563143 → disponibilidad | 1 min |
| 6 | *opcional*: `leer_calendario` del calendario personal (free/busy) | n8n → nuevo nodo + credencial | 15 min |

### 2.1 Dónde va el `chat_id` de Emilia (2 reemplazos, mismo número)

`999999999` es un **placeholder**. Aparece en:

1. **Router** `YWpuV5p0vCDTbIHz` → nodo `Route Telegram Command` → regla 2 → `rightValue` → poner el id real (define si su chat entra al flujo o cae en el inbox de Fuentes).
2. **Agent Voz Emilia** `Fa2AlIDqUntSWMrw` → nodo `Detectar Entrada Emilia` (Code) → `const PERMITIDO = 999999999;` → poner el id real (allowlist de su propio flujo).

> El id se consigue solo: Emilia manda `/start` (o cualquier mensaje) al bot y el `chat_id` aparece en la ejecución del Router (`Recibo Mensaje` → mensaje recibido).

---

## 3. Las 7 tools del subflujo de Emilia

| Tool | Qué hace | Event type |
|---|---|---|
| `consultar_disponibilidad` | slots libres en un rango | el que le pida el LLM (7563141/2/3) |
| `obtener_reuniones` | bookings con `bookingUid` | se llama 1 vez por cada ET para la agenda completa |
| `agendar_online` | crea reunión con Meet | **7563142** (fijo en el body) |
| `agendar_presencial` | crea reunión en el estudio | **7563141** (fijo en el body) |
| `actualizar_reunion` | reprograma (misma duración) | por `bookingUid` |
| `cancelar_reunion` | cancela | por `bookingUid` |
| `leer_calendario` | eventos de Google Calendar | `arq.emiliapimentalombardi@gmail.com` (funciona al compartirlo) |

Reglas duras: el `eventTypeId` va **fijo** en el body de cada tool (el LLM no puede inventarlo) y la dirección **se hereda** del event type (no la inventa el agente).

---

## 4. Guion de la sesión (13:00 → 14:00)

**Bloque 1 — 5 min · el bot**
Emilia manda un mensaje al bot desde su Telegram. Entramos al Router y vemos su `chat_id` → lo cargamos en los 2 lugares → **Publicar** ambas versiones. Le pedimos que mande otro mensaje: ahora le responde.

**Bloque 2 — 10 min · la cuenta de Emilia**
Le mostramos su cuenta Cal.com: los 3 event types, el horario L-V 9-17, el calendario destino. Con un contacto de prueba hacemos el circuito completo:
1. "agendame una reunión online con Juan Pérez (juan@test.com) el jueves 22 a las 11" → confirmar → **queda agendada**;
2. la vemos en su Google Calendar (mismo día);
3. "movéla a las 15" → `actualizar_reunion`;
4. "cancelala" → `cancelar_reunion`.

**Bloque 3 — 5 min · el calendario**
Cargamos la dirección del estudio en el ET presencial y la probamos: "agendame una presencial con Juan el viernes 23 a las 10" → la ubicación dice la dirección real.

**Bloque 4 — 5 min · compartir**
Emilia comparte su calendario profesional con `proyectopi.31416@gmail.com` → `leer_calendario` deja de dar error y el agente puede responder "¿qué tengo el martes?" incluyendo lo que se agendó a mano.

**Bloque 5 — 5 min · decisión de alcance**
Si el tiempo alcanza: 120/180 min de duración y el schedule 24/7 del ET libre.

---

## 5. Checklist de pruebas (marcá cada una)

- [ ] Emilia recibe respuesta del bot (texto)
- [ ] Emilia puede mandar **audio** y el bot transcribe y responde
- [ ] "qué reuniones tengo esta semana" → responde con su agenda
- [ ] agenda online → queda en su Cal.com **y** en su Google Calendar
- [ ] agenda presencial → aparece la dirección del estudio
- [ ] reprogramar y cancelar funcionan
- [ ] el contacto de prueba queda con nombre+email en la planilla `clientes-contactos` / hoja `clientes`
- [ ] Sol sigue funcionando (su cuenta, su agenda, su bot)

---

## 6. Rollback (si algo falla en la sesión)

| Symptoma | Acción |
|---|---|
| El bot no responde a nadie | en el Router, `Route Telegram Command` → regla 2 → `rightValue` = `__sin_emilia__` (nadie matchea) → **Publicar** |
| El bot de Sol rompió | Router → volver a la versión `839a972c-8a7e-4dae-aa45-4ce0cdc225ad` (16/10, la que estaba activa) → **Publicar** |
| El flujo de voz rompió | Agent Voz → volver a la versión `21f718be-9cc9-4a44-8f52-76660389086d` (14/10) → **Publicar** |
| Agendar falla en la cuenta equivocada | dejar de usar el bot; el Dispatcher decide por `chat_id`, no hay migración de datos |

---

## 7. Deuda para la fase 2 (no bloquea mañana)

1. **Duraciones 120/180** — la API de Cal.com ignora `metadata.multipleDuration` y `scheduleId` en la versión `2024-06-11` (responde `success` sin aplicar). Se cargan en la UI de Cal.com.
2. **ET-C sin schedule 24/7** — mismo motivo; el schedule 2527411 está creado y listo para asignar.
3. **Voz del calendario personal** — `leer_calendario` hoy lee el calendario profesional; para el free/busy del personal hace falta un segundo nodo `Calendar → Availability` y decidir si Cal.com debe bloquearlo.
4. **Memoria compartida** — la tabla Postgres `studio_os_test` la usan las dos personas; las sesiones se separan por `chat_id` (ya lo hace el `sessionKey`), pero las tablas distintas llegan cuando se quiera aislar de verdad.
5. **Cuentas y credenciales** — las credenciales `ppi-EmiliaOS_*` de Google (Drive/Docs/Sheets) siguen apuntando a `proyectopi.31416@gmail.com`; Emilia usa la del estudio para todo.
6. **Wiki** — las lecciones técnicas de hoy (versiones de API de Cal.com, el MCP de n8n degradando parámetros, publicación de versiones) van al glosario cuando se apruebe la escritura en `wiki/`.

---

## 8. Lecciones técnicas de hoy (20/10)

1. **La API de Cal.com solo expone los event types en `cal-api-version: 2024-06-13`… `2024-06-11`.** Con `2024-08-13` el `GET /v2/event-types` da 404 y el `POST` también. Y en esa versión el schema del body usa `length` (no `lengthInMinutes`).
2. **La API no aplica `metadata.multipleDuration` ni `scheduleId`**: responde `success` y no cambia nada. Por eso las duraciones y los schedules se cargan en la UI.
3. **El MCP de n8n degrada los parámetros**: `addNode` y `updateNodeParameters` convierte booleanos a string y aplana las colecciones (`headerParameters.parameters` → `{item: …}`); con `sendBody: "true"` el body **no viaja**. Con `sendBody` string, n8n oculta el campo por `displayOptions` y el POST sale vacío.
4. **La vía fiable es `create_workflow_from_code` (SDK)**: preserva tipos, y además completa los campos que faltaban (`contentType: "json"`, `specifyHeaders: "keypair"`). Los `subnodes` van **dentro de `config`**, no al nivel del nodo.
5. **Editar un workflow no cambia lo que se ejecuta**: hay que **publicar**. Los subflujos llamados por `Execute Workflow` requieren estar publicados (el error lo dice: *"references workflow X which is not published"*).
6. **`setNodeParameter` con puntero JSON sobre hojas de string** es la única edición in-place segura vía MCP (permite tocar reglas de un switch, un `jsCode`, un `chatId`, una `workflowId`) sin pasar por el SDK.
7. **El `pinData` del MCP stringifica los valores**: un `chat.id` numérico llega como texto → las allowlists hay que compararlas con `String(...)`.
