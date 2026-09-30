---
tipo: metodologia
fecha_creacion: 2026-09-24
ultima_actualizacion: 2026-09-24
tags: [emilia, studio-os, n8n, telegram, cal-com, fathom, drive]
idioma: es
estado: plan
---

# Plan de reanudación — OS-Emilia en n8n

> **Estado al 2026-09-29: AVANZADO, SIN ACTIVAR — Drive IDs confirmados (raíz + 2 carpetas), Cal.com evento `7109200`, Fathom lectura ok (`recording 184073789`), doble salida md+Doc lista. Pendiente §16.4-16.5: reemplazar credenciales autoasignadas por `* Emilia`, configurar Telegram/Cal/Fathom finales, activar Router → `/help` → `/sync` → `/agendar` → Cron.**

> Objetivo: retomar sin perder decisiones después del reinicio. Implementar un único bot privado de Telegram para Emilia que agenda reuniones en Cal.com y sincroniza reuniones de Fathom a una carpeta compartida de Google Drive, sin depender de una computadora encendida y sin usar un agente de IA.

## 1. Alcance

El sistema tendrá dos funciones:

1. Emilia envía un mensaje con formato estricto para crear una reunión en el Cal.com de su cuenta.
2. Emilia usa `/sync`, o el sistema usa un cron diario, para traer las reuniones nuevas de Fathom y guardarlas automáticamente en la carpeta correcta de Drive.

La primera versión funciona sin IA. La interpretación queda determinada por comandos, patrones de texto y campos estructurados de las APIs.

## 2. Decisiones tomadas

- La automatización vive en el n8n actual del VPS: `https://n8n.pitau.tech`.
- Los flujos se organizan dentro de la carpeta `OS-Emilia`, ya creada.
- Se utiliza el mismo VPS que Lidia, con credenciales separadas para Emilia.
- Se utiliza un único bot de Telegram en chat privado con Emilia.
- Se utiliza Cal.com para agendar, en lugar de Google Calendar.
- Se utiliza Google Drive compartido para guardar los documentos de Fathom.
- El mantenimiento del VPS queda incorporada al ciclo de mantenimiento de Lidia.
- El monitoreo del VPS queda como backlog posterior al MVP.
- El MVP no utiliza agentes de IA ni nodos de LLM.

## 3. Carpeta compartida de trabajo

El Drive local sincronizado es:

```text
G:\Mi unidad\OS-Emilia\
```

Dentro se utilizarán estas carpetas:

```text
Reuniones-Internas\
Reuniones-Clientes\
```

Las carpetas ya fueron creadas. Antes de configurar los nodos de Drive se deben obtener sus Folder IDs desde la URL de cada carpeta:

```text
https://drive.google.com/drive/folders/<FOLDER_ID>
```

La cuenta o servicio que conecte n8n con Drive debe tener permiso de edición sobre la carpeta raíz `OS-Emilia`.

## 4. Arquitectura propuesta

### 4.1 `WF-Router-Telegram`

Workflow público. Contiene un único nodo `Telegram Trigger` asociado al bot de Emilia.

Luego usa un nodo `Switch` o `IF` para separar los comandos:

- `/agendar ...` ejecuta `WF-Agenda-Core`.
- `/sync` ejecuta `WF-Fathom-Core`.
- Otros comandos devuelven ayuda breve.

Se usa un solo Telegram Trigger porque Telegram admite un webhook activo por token de bot. Dos workflows con el mismo token pueden competir por el mismo webhook.

### 4.2 `WF-Agenda-Core`

Subworkflow de agendamiento. Componentes:

1. `Execute Workflow Trigger`.
2. `Edit Fields` o `Set` para extraer fecha, hora y nombre desde el mensaje.
3. `Google Sheets: Lookup` en la hoja de clientes.
4. Filtro para abandonar el flujo si no encuentra un email único.
5. `Cal.com: Create Booking` usando la credencial `cal.com-emilia`.
6. `Google Drive` o `Google Sheets` para registrar el resultado.
7. Nodo `Telegram: Send Message` para confirmar a Emilia.

Formato inicial recomendado:

```text
/agendar 25/09 10:00 Juan Perez
```

Expresión de referencia:

```regex
^/agendar (\d{2}/\d{2}) (\d{2}:\d{2}) (.+)$
```

La confirmación inicial devuelve fecha, hora, contacto y enlace de la reunión creada.

### 4.3 `WF-Fathom-Core`

Subworkflow de sincronización. Recibe opcionalmente el origen del disparo y un mensaje de estado.

Componentes:

1. `Execute Workflow Trigger`.
2. `HTTP Request` autenticado contra la API de Fathom.
3. `Split In Batches` o `Loop Over Items` para procesar reuniones individualmente.
4. Filtro de reuniones nuevas según el estado guardado.
5. `IF` para clasificar la reunión.
6. Construcción de un documento `.md` o `.txt` con los datos disponibles.
7. `Google Drive: Upload` en la carpeta elegida.
8. Registro del `recording_id` procesado.
9. `Telegram: Send Message` con el resumen del resultado.

La primera versión puede guardar metadatos, resumen, action items y transcripción si la respuesta de la API los incluye. El resumen y la transcripción pueden venir generados por Fathom; n8n solamente los organiza y transporta.

### 4.4 `WF-Fathom-Cron`

Workflow público. Contiene:

1. `Schedule Trigger` a las `07:00`, hora de `America/Argentina/Buenos_Aires`.
2. `Execute Workflow` llamando a `WF-Fathom-Core`.

El comando `/sync` llama al mismo subworkflow. De esta forma existe una única lógica de sincronización.

## 5. Clasificación automática de reuniones

La API de Fathom expone información de calendarios e invitados. Se usará `calendar_invitees` y, cuando esté disponible, `calendar_invitees_domains_type`.

Regla inicial:

```text
Si todos los participantes pertenecen a los correos internos conocidos
  → G:\Mi unidad\OS-Emilia\Reuniones-Internas\

Si existe al menos un participante externo
  → G:\Mi unidad\OS-Emilia\Reuniones-Clientes\
```

Correos internos que faltan confirmar antes de implementar:

- Correo de Emilia.
- Correo asociado a Proyecto Pi.
- Otros correos internos del estudio, si corresponde.

Caso límite:

```text
Si la reunión no contiene invitados de calendario
  → Guardar en Reuniones-Internas
  → Anteponer "[revisar]" al nombre del archivo
  → Notificar el caso por Telegram
```

La clasificación no depende de la cantidad bruta de participantes. Una reunión con diez personas externas sigue siendo una reunión de clientes; una reunión únicamente interna se archiva como interna.

## 6. Estructura de clientes para agendar

La hoja `clientes` debe contener, como mínimo:

| nombre | email | empresa | activo |
|---|---|---|---|
| Juan Perez | ejemplo@dominio.com | Empresa SA | Sí |

Reglas:

1. La búsqueda normaliza mayúsculas, minúsculas y espacios.
2. El flujo exige un único email activo.
3. Si hay coincidencias múltiples, devuelve la lista para que Emilia elija.
4. Si el nombre no existe, solicita el email en el chat y no crea la reserva.
5. El mensaje de confirmación incluye el email utilizado.

## 7. Credenciales a crear

### 7.1 Telegram Emilia

Nombre sugerido:

```text
telegram-emilia
```

Pasos:

1. En `@BotFather`, ejecutar `/newbot`.
2. Crear el bot con un nombre claramente diferenciable, por ejemplo `@EmiliaOS_bot` si el nombre está libre.
3. Guardar el token entregado. El token es secreto.
4. En n8n, crear una credencial `Telegram` con el token.
5. Activar el workflow de prueba y pedir a Emilia que envíe `/start`.
6. Obtener el `chat_id` de Emilia.
7. Configurar el trigger o un filtro de autorización para aceptar únicamente ese `chat_id`.
8. Registrar en BotFather los comandos visibles `/agendar` y `/sync`.

La credencial de Telegram se separa de la credencial usada por Lidia.

### 7.2 Cal.com Emilia

Nombre sugerido:

```text
cal.com-emilia
```

Pasos:

1. Emilia abre la configuración de API de su cuenta Cal.com.
2. Crea una API Key con los permisos mínimos necesarios para consultar event types y crear bookings.
3. En n8n, crea una credencial `Cal.com`.
4. Ingresa la API Key.
5. Ejecuta una lectura de Event Types mediante un nodo Cal.com.
6. Confirma que la cuenta y el evento predeterminado pertenecen a Emilia.
7. Anota el `eventTypeId` y la duración predeterminada.
8. Ejecuta una reserva de prueba y verifica que aparezca en `cal.com/bookings`.

La credencial de Cal.com Emilia se separa de la cuenta utilizada por Lidia.

### 7.3 Fathom Emilia

Nombre sugerido:

```text
fathom-emilia
```

Pasos:

1. En la cuenta de Fathom correspondiente, crear o recuperar una API Key.
2. En n8n, crear una credencial de encabezado HTTP.
3. Configurar el encabezado de autenticación según la documentación vigente de Fathom.
4. Probar un endpoint de listado de reuniones con límite `1`.
5. Confirmar respuesta HTTP 200 y presencia de un `recording_id`.
6. Probar una segunda llamada incluyendo resumen, action items y transcripción.
7. Verificar que la cuenta devuelve solamente reuniones accesibles para Emilia o el equipo compartido.

Referencia oficial: [Fathom — List meetings](https://developers.fathom.ai/api-reference/meetings/list-meetings).

### 7.4 Google Drive y Google Sheets Emilia

Nombre sugerido:

```text
google-drive-emilia
google-sheets-emilia
```

Pasos:

1. Elegir el mecanismo de autenticación compatible con la cuenta que administra el Drive compartido.
2. Conectar n8n a la carpeta raíz `OS-Emilia`.
3. Comprobar lectura, escritura y creación de archivos mediante un archivo de prueba.
4. Obtener los IDs de `Reuniones-Internas` y `Reuniones-Clientes`.
5. Conectar la hoja `clientes`.
6. No almacenar tokens, API Keys ni JSON de servicio dentro de workflows o repositorios.

## 8. Estado para evitar duplicados

Cada reunión se marcará como procesada por su `recording_id`.

El estado puede guardarse en una hoja `fathom-state` con una fila por reunión:

| recording_id | procesado_en | carpeta | archivo_id |
|---|---|---|---|

Antes de escribir, el flujo comprobará si el `recording_id` ya fue procesado.

La primera versión continúa desde la última ejecución exitosa. El diseño definitivo de paginación y fechas se ajusta con una respuesta real de la API.

## 9. Formato de archivo de reunión

Nombre propuesto:

```text
YYYY-MM-DD_cliente-reunion_grabacion-123456.md
```

Ejemplo:

```text
2026-09-24_emilia-studio-os_grabacion-123456.md
```

Contenido inicial:

```markdown
# Título de la reunión

## Datos

- Fecha:
- Inicio:
- Fin:
- URL de Fathom:
- Recording ID:
- Participantes:
- Tipo: Internas | Clientes

## Resumen

<resumen de Fathom, si está disponible>

## Action items

<action items, si están disponibles>

## Transcripción

<transcripción, si está disponible>
```

El documento se arma mediante nodos nativos de n8n, sin un agente de IA.

## 10. Playbook de creación y pruebas

### Fase 1 — Credenciales

- [ ] Crear el bot de Telegram para Emilia.
- [ ] Guardar el token como credencial de n8n.
- [ ] Obtener y validar el `chat_id` de Emilia.
- [ ] Crear la API Key de Cal.com Emilia.
- [ ] Guardar y probar la credencial Cal.com.
- [ ] Crear o recuperar la API Key de Fathom Emilia.
- [ ] Guardar y probar la credencial HTTP de Fathom.
- [ ] Conectar Drive y Sheets a `OS-Emilia`.
- [ ] Obtener los Folder IDs de las dos subcarpetas.

### Fase 2 — Agendamiento

- [ ] Crear `WF-Agenda-Core` tomando como referencia el agendamiento existente de Lidia.
- [ ] Implementar el formato `/agendar DD/MM HH:MM Nombre`.
- [ ] Implementar la búsqueda de email en la hoja `clientes`.
- [ ] Implementar la creación del booking en Cal.com.
- [ ] Implementar la confirmación por Telegram.
- [ ] Registrar el resultado en la hoja o archivo de auditoría.

### Fase 3 — Fathom

- [ ] Consultar una página de reuniones desde la API.
- [ ] Inspeccionar una respuesta real completa.
- [ ] Implementar la lectura de resumen, action items y transcripción.
- [ ] Implementar el control de duplicados por `recording_id`.
- [ ] Implementar la clasificación internas/clientes.
- [ ] Implementar la carga en la carpeta correcta.
- [ ] Notificar el resultado a Emilia.

### Fase 4 — Router y disparadores

- [ ] Crear `WF-Router-Telegram` con un único Telegram Trigger.
- [ ] Enrutar `/agendar` hacia `WF-Agenda-Core`.
- [ ] Enrutar `/sync` hacia `WF-Fathom-Core`.
- [ ] Crear `WF-Fathom-Cron` con horario diario.
- [ ] Publicar los tres workflows.
- [ ] Confirmar que solo existe un webhook activo para el token del bot.

### Fase 5 — Pruebas de aceptación

- [ ] Emilia agenda una reunión de prueba.
- [ ] La reunión aparece en Cal.com.
- [ ] Emilia recibe la confirmación en Telegram.
- [ ] `/sync` trae una reunión real de Fathom.
- [ ] Una reunión interna llega a `Reuniones-Internas`.
- [ ] Una reunión con participante externo llega a `Reuniones-Clientes`.
- [ ] Repetir `/sync` no duplica el archivo.
- [ ] Una reunión sin invitados de calendario queda marcada `[revisar]`.
- [ ] Un usuario no autorizado no puede operar el bot.
- [ ] El cron ejecuta correctamente y conserva el horario de Buenos Aires.

## 11. Documentación para Emilia

El playbook entregable se ubicará en:

```text
proyectos/STUDIO_OS-Emilia/documentacion/playbook-os-emilia-n8n.md
```

Debe explicar solamente la operación diaria:

1. Cómo abrir Telegram.
2. Cómo escribir `/agendar DD/MM HH:MM Nombre`.
3. Cómo interpretar la confirmación.
4. Cómo escribir `/sync`.
5. Cómo encontrar los documentos en la carpeta compartida de Drive.
6. Qué hacer si un contacto no aparece.
7. A quién escribir si el bot deja de responder.

La documentación-evidencia de implementación queda en `specs/`; el manual de uso para Emilia queda en el proyecto.

## 12. Backlog posterior

- [ ] Monitoreo del VPS con Uptime Kuma o servicio equivalente.
- [ ] Alerta por Telegram si n8n o el VPS no responden.
- [ ] Respaldo periódico de las credenciales mediante el mecanismo seguro de n8n.
- [ ] Respaldo de la base de clientes y del estado de Fathom.
- [ ] Auditoría de duplicados y Meetings processed.
- [ ] Opcional: interpretación de lenguaje natural con un modelo local o un nodo de IA económico.
- [ ] Opcional: agenda de clientes mediante enlace directo de Cal.com, evitando escribir la fecha manualmente.

## 13. Información pendiente para retomar

- [ ] Correo de Emilia.
- [ ] Correo interno de Proyecto Pi.
- [ ] Confirmar si existen otros dominios internos.
- [ ] Confirmar el `eventTypeId` de Emilia.
- [ ] Confirmar la duración predeterminada de la reunión.
- [ ] Confirmar si la agenda incluye videollamada, teléfono o ubicación.
- [ ] Confirmar si la hoja de clientes ya existe o hay que crearla.
- [ ] Confirmar formato final `.md` o `.txt`.
- [ ] Confirmar cuenta y mecanismo de autenticación de Google Drive.
- [ ] Confirmar el usuario o equipo de Fathom desde el que se sincronizará.

## 14. Criterio de cierre del MVP

El MVP queda terminado cuando Emilia puede, desde su teléfono:

1. Crear una reunión real en su Cal.com mediante un mensaje de Telegram.
2. Pedir una sincronización inmediata de Fathom.
3. Encontrar cada reunión en la carpeta Drive correcta.
4. Recibir una confirmación después de cada acción.

Todo debe funcionar con la computadora de Emilia apagada y sin consumir créditos de IA.

## 15. Telegram: comandos, acciones y recolección estructurada de datos

### 15.1 Qué puede hacer el bot

El bot se utiliza como una interfaz de operaciones, no como un agente autónomo. Las acciones iniciales son deterministas, auditables y gratuitas:

| Comando | Acción | Resultado esperado |
|---|---|---|
| `/start` | Iniciar o recuperar la conversación | Mensaje de bienvenida y autorización |
| `/help` | Mostrar ayuda | Lista de comandos disponibles |
| `/agendar` | Iniciar una solicitud de reunión | El bot pide los datos faltantes |
| `/agendar DD/MM HH:MM Nombre` | Solicitud completa | El bot busca el email, muestra confirmación y crea el booking al confirmar |
| `/sync` | Sincronizar Fathom ahora | Procesa reuniones nuevas y las clasifica en Drive |
| `/reuniones` | Ver el estado de la última sincronización | Fecha, cantidad procesada y cantidad omitida |
| `/cancelar` | Cancelar la solicitud en curso | Borra el estado pendiente y confirma la cancelación |
| `/estado` | Mostrar el estado de la solicitud actual | Indica qué datos faltan |

La primera versión reserva `/settings` para una etapa posterior. El bot solo necesita una usuaria autorizada y sus preferencias actualmente están definidas en la credencial y en la hoja de configuración.

### 15.2 Acciones internas de n8n

Cada comando se convierte en una acción interna estable:

```text
start
help
agendar
sync
reuniones
cancelar
estado
```

El router identifica la acción y ejecuta el subworkflow correspondiente:

```text
/agendar → WF-Agenda-Core
/sync → WF-Fathom-Core
/reuniones → WF-Fathom-Status
/start, /help, /cancelar, /estado → respuesta directa o estado
```

El nombre de la acción no depende del mensaje completo. Esto permite registrar métricas y detectar errores sin depender de un modelo de lenguaje.

### 15.3 Recolección estructurada de una reunión

El bot puede aceptar el pedido completo en un mensaje o puede recomendarlo paso a paso. La segunda opción es más cómoda para una usuaria no técnica y se implementa sin IA.

#### Opción A — Pedido completo

```text
/agendar 25/09 10:00 Juan Perez
```

El flujo extrae:

```text
fecha: 25/09
hora: 10:00
nombre_contacto: Juan Perez
```

#### Opción B — Pedido guiado

1. Emilia envía `/agendar`.
2. El bot responde: `Indicame fecha y hora: DD/MM HH:MM`.
3. Emilia envía `25/09 10:00`.
4. El bot responde: `¿Con quién es la reunión?`.
5. Emilia envía `Juan Perez`.
6. El flujo busca el contacto en la hoja de clientes.
7. El bot muestra una tarjeta de confirmación:

```text
Reunión: Juan Perez
Fecha: 25/09/2026
Hora: 10:00
Email: juan@example.com
Evento: duración predeterminada de Cal.com
```

8. El bot agrega botones `Confirmar`, `Cambiar` y `Cancelar`.
9. Emilia toca `Confirmar`.
10. Se crea el booking en Cal.com y se responde con el enlace.

La estructura mínima que se conserva entre mensajes es:

| Campo | Tipo | Ejemplo |
|---|---|---|
| `chat_id` | Entero | `123456789` |
| `action` | Texto | `agendar` |
| `date` | Texto o ISO | `2026-09-25` |
| `time` | Texto | `10:00` |
| `contact_name` | Texto | `Juan Perez` |
| `email` | Texto | `juan@example.com` |
| `event_type_id` | Texto o entero | `123456` |
| `status` | Texto | `esperando_datos`, `esperando_confirmacion`, `confirmado`, `cancelado` |
| `updated_at` | ISO datetime | `2026-09-24T14:00:00-03:00` |

El estado puede guardarse en una Data Table de n8n o en una hoja `bot-state`. Para el MVP se recomienda una hoja de Drive porque resulta más fácil de auditar y recuperar desde el VPS.

Cada estado tiene una antigüedad máxima, por ejemplo 30 minutos. Si expira, el bot informa que la solicitud quedó cancelada y ofrece comenzar nuevamente con `/agendar`.

### 15.4 Botones de Telegram

Telegram ofrece dos tipos de teclado que resultan útiles:

- Teclado de respuesta: muestra opciones que envían texto.
- Teclado inline: los botones aparecen debajo del mensaje y envían un `callback_query` sin agregar texto al chat.

Para este bot se recomienda teclado inline para:

- `Confirmar` → callback `agenda:confirm`.
- `Cambiar` → callback `agenda:edit`.
- `Cancelar` → callback `agenda:cancel`.
- `Procesar ahora` → callback `sync:run`.
- `Ver resumen` → callback `fathom:status`.

El `callback_data` debe ser corto porque Telegram limita esta cadena a 64 bytes. El dato completo de la solicitud permanece guardado en el estado del flujo, no dentro del botón.

El nodo `Telegram Trigger` debe recibir el evento `Callback Query` además de `Message`. El nodo Telegram de n8n se utiliza para enviar y editar los mensajes con los botones.

### 15.5 Confirmación antes de escribir

La agenda sigue este principio:

```text
Texto recibido
  → parseo determinista
  → búsqueda del contacto
  → mostrar resumen
  → Confirmar
  → crear booking en Cal.com
```

Si falta la fecha, la hora o el contacto, el bot pregunta solo el dato que falta. Si el contacto tiene varias coincidencias, devuelve botones o una lista numerada. La creación en Cal.com ocurre una única vez, después de la confirmación.

La respuesta de Cal.com se conserva en el registro de auditoría junto con:

- `chat_id`.
- Fecha y hora solicitadas.
- Email del contacto.
- `eventTypeId`.
- Resultado de la API.
- Enlace de la reunión.
- Fecha de creación.

### 15.6 Creación del bot en BotFather

1. Abrir `@BotFather` desde Telegram.
2. Enviar `/newbot`.
3. Elegir un nombre visible para Emilia, por ejemplo `Asistente OS Emilia`.
4. Elegir un username único terminado en `bot`, por ejemplo `@emilia_os_bot`, siempre que esté disponible.
5. Guardar el token en el gestor de secretos de n8n, nunca en el repositorio.
6. Crear la credencial `telegram-emilia` en n8n.
7. Configurar los comandos visibles con BotFather o mediante `setMyCommands`:
   - `/start`
   - `/help`
   - `/agendar`
   - `/sync`
   - `/reuniones`
   - `/cancelar`
   - `/estado`
8. Activar el workflow del router.
9. Pedir a Emilia que abra el bot y envíe `/start`.
10. Guardar el `chat_id` de Emilia como usuario autorizado.

El token de Telegram funciona como una contraseña. Cualquier persona que lo obtenga puede controlar el bot. Se mantiene únicamente en la credencial cifrada de n8n y no aparece en mensajes, logs, capturas ni documentos compartidos.

### 15.7 Seguridad y autorización

- El `Telegram Trigger` se configura para restringir el `chat_id` de Emilia.
- Se agrega un filtro de `from.id` para validar que el mensaje proviene de la cuenta autorizada.
- El bot no acepta bookings desde grupos en el MVP.
- El grupo se deja como etapa posterior; cada grupo necesita un `chat_id` negativo y reglas de privacidad propias.
- El bot no expone tokens, Folder IDs privados ni contenido de otros chats.
- Los mensajes de Fathom se procesan en la cuenta autorizada y se guardan únicamente en las carpetas acordadas.
- La API Key de Cal.com se limita a las operaciones necesarias para leer event types y crear bookings.

### 15.8 Comandos de Fathom dentro del mismo bot

No hace falta crear un segundo bot. El comando `/sync` reutiliza el mismo Telegram Trigger y ejecuta `WF-Fathom-Core`.

Mensajes que puede recibir Emilia:

```text
/sync
```

Respuesta inicial:

```text
Sincronizando reuniones nuevas de Fathom…
```

Respuesta final:

```text
Procesé 2 reuniones:
- 1 en Reuniones-Internas
- 1 en Reuniones-Clientes
No encontré reuniones nuevas en la sincronización anterior.
```

Si una reunión tiene participantes externos, el bot informa el destino sin enviar datos personales de los participantes. El archivo completo queda en la carpeta compartida de Drive.

### 15.9 Referencias oficiales verificadas

- [Telegram Bot API](https://core.telegram.org/bots/api) — comandos, mensajes, keyboards, `callback_query`, webhooks y authorization.
- [Telegram Bot Features — Commands](https://core.telegram.org/bots/features#commands) — comandos, alcance y registro mediante BotFather.
- [Telegram Bot Features — Inline Keyboards](https://core.telegram.org/bots/features#inline-keyboards) — botones debajo del mensaje y `callback_data`.
- [Telegram BotFather](https://core.telegram.org/bots/features#botfather) — creación y configuración del bot.
- [n8n Telegram Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger.md) — eventos `Message`, `Callback Query`, restricción por Chat ID y User ID.
- [n8n Telegram node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram.md) — envío, edición y botones desde n8n.

### 15.10 Criterio de aceptación de Telegram

El bot se considera listo para Emilia cuando puede:

1. Mostrar `/help` con instrucciones claras.
2. Aceptar `/agendar DD/MM HH:MM Nombre`.
3. Pedir los datos faltantes uno por uno.
4. Mostrar la propuesta antes de escribir en Cal.com.
5. Crear el booking después de `Confirmar`.
6. Cancelar una solicitud desde el chat.
7. Ejecutar `/sync` manualmente.
8. Informar cuántas reuniones fueron guardadas y en qué carpetas.
9. Rechazar cualquier `chat_id` diferente al de Emilia.
10. Mantener el mismo token en un único Telegram Trigger activo.

## 16. Implementación inicial en n8n VPS

### 16.1 Flujos creados

Los siguientes workflows fueron creados dentro de la carpeta `OS-Emilia` del proyecto `Proyecto PI`:

| Workflow | ID n8n | Función |
|---|---|---|
| `OS-Emilia — Telegram Router (sin credenciales)` | `YWpuV5p0vCDTbIHz` | Router único de Telegram |
| `OS-Emilia — Agenda Core (sin credenciales)` | `UTkII2kd3RHDlizo` | Parseo de `/agendar`, lookup Sheets y Cal.com |
| `OS-Emilia — Fathom Core (sin credenciales)` | `UeDkqVZSeLnae5cF` | Consulta Fathom, clasifica y crea Markdown en Drive |
| `OS-Emilia — Fathom Cron` | `2gUlVXu7xk1Jd12s` | Ejecuta Fathom Core todos los días a las 07:00 |

También se creó la Data Table `OS-Emilia — Bot State` con ID `2YgepkPbLD3s4Nu9` para el siguiente ciclo de estado conversacional y control de duplicados.

### 16.2 Estado funcional de esta primera versión

- Todos los workflows están desactivados.
- El router utiliza un único `Telegram Trigger`.
- `/agendar` acepta el formato `/agendar DD/MM HH:MM Nombre`.
- La agenda consulta una hoja de clientes y llama a Cal.com.
- `/sync` llama al mismo Fathom Core que usa el cron.
- Las reuniones se clasifican por la lista de emails internos que se complete en `Build Meeting Document`.
- Las reuniones sin invitados se guardan provisionalmente como internas y reciben el prefijo `[revisar]-`.
- La confirmación con botones, la conversación guiada y el control persistente de duplicados quedan para el siguiente ciclo.
- La Data Table de estado está creada, pero todavía no está conectada a los workflows.

### 16.3 Credenciales que hay que crear en n8n

#### Telegram Emilia

1. En `@BotFather`, crear un bot nuevo para Emilia con `/newbot`.
2. Guardar el token en una credencial Telegram llamada `Telegram Emilia Bot`.
3. En el nodo `Telegram OS-Emilia`, reemplazar la credencial asignada por `Telegram Emilia Bot`.
4. En el nodo `Send Help` del router y `Send Agenda Confirmation` del Agenda Core, seleccionar la misma credencial.
5. Abrir el chat con Emilia y enviar `/start`.
6. Obtener el `chat_id` de Emilia.
7. Configurar el trigger con ese `chat_id` como restricción.
8. Crear y activar únicamente este workflow como Telegram Trigger activo para el nuevo bot.

#### Cal.com Emilia

1. Crear una API Key dentro de la cuenta de Cal.com de Emilia.
2. En n8n, crear una credencial `HTTP Bearer Auth` o la credencial templada compatible con Cal.com, llamada `Cal.com Emilia API`.
3. En `Create Cal.com Booking`, seleccionar `Cal.com Emilia API`.
4. Reemplazar el `eventTypeId` `123456` por el identificador real del evento de Emilia.
5. Probar la creación con un contacto de prueba antes de publicar.

#### Fathom Emilia

1. Generar una API Key desde la cuenta Fathom de Emilia.
2. En n8n, crear una credencial de encabezado o credencial templada con esta cabecera:

```text
X-Api-Key: <API_KEY_DE_EMILIA>
```

3. Nombrarla `Fathom Emilia API`.
4. En `Fetch Fathom Meetings`, seleccionar `Fathom Emilia API`.
5. Verificar que el endpoint `https://api.fathom.ai/external/v1/meetings` devuelva reuniones de la cuenta correcta.
6. No usar una API Key de otra cuenta aunque tenga acceso a reuniones compartidas sin revisar el alcance.

#### Google Drive Emilia

Ya existe en n8n la credencial OAuth `pitau.tech-Google Drive account` (ID `zJXVWJDxVV77ErdC`) asociada al proyecto PI. La prueba de listado confirmó que la cuenta accede a `My Drive`, pero `OS-Emilia` todavía no aparece en esa cuenta.

1. Definir quién es propietario de la carpeta compartida: Google de Emilia o Google de Proyecto PI.
2. Si es de Emilia, compartir `OS-Emilia` con el correo de Google de Emilia y autorizar ese mismo usuario en n8n.
3. Si es de Proyecto PI, crear o sincronizar `OS-Emilia` dentro del `My Drive` de la credencial existente.
4. En n8n, usar `pitau.tech-Google Drive account` como `Google Drive Emilia` provisional o crear una copia de la credencial con ese nombre.
5. En `Save Internal Meeting`, seleccionar la credencial y elegir `Reuniones-Internas`.
6. En `Save Client Meeting`, seleccionar la misma credencial y elegir `Reuniones-Clientes`.
7. Comprobar permisos de lectura y escritura con un archivo de prueba.

#### Google Sheets Emilia

Ya existen dos credenciales OAuth de Google Sheets en el proyecto PI: `pitau.tech-Google Sheets` (ID `TT9NeaFF1ayv59t0`) y `p.pi-Google Sheets account` (ID `c5ExvoJWAdpGVDzA`). La primera muestra un documento llamado `clientes`; la segunda fue la que n8n asignó automáticamente al Agenda Core, pero su pestaña no pudo verificarse por permisos.

1. Usar `pitau.tech-Google Sheets` como candidata inicial para `Google Sheets Emilia`.
2. En `Lookup Client Email`, seleccionar esa credencial.
3. Elegir el documento `clientes` y la pestaña `clientes`.
4. Confirmar que la pestaña tenga las columnas `name`, `email` y `activo`.
5. Usar una fila por contacto y emails únicos.
6. Si la hoja pertenece a otro estudio, crear una credencial nueva para Emilia en lugar de reutilizarla.

### 16.4 Componentes que deben reemplazarse antes de activar

- Credenciales Telegram existentes asignadas automáticamente por n8n.
- Credenciales Google Sheets existentes asignadas automáticamente.
- Credenciales Google Drive existentes asignadas automáticamente.
- Los dos valores `REEMPLAZAR_EMILIA` y `REEMPLAZAR_PROYECTOPI` del nodo Code.
- El `eventTypeId` `123456`.
- Los selectores de documentos y carpetas vacíos.
- El `chat_id` autorizado de Emilia.

La API de creación de workflows de n8n autoasignó credenciales existentes cuando ya había una credencial del mismo tipo. Por seguridad, hay que reemplazarlas manualmente por las credenciales `* Emilia` antes de activar cualquier workflow. Ningún workflow queda activo durante esta etapa.

### 16.5 Orden de activación

1. Activar solamente `OS-Emilia — Telegram Router` después de configurar Telegram.
2. Ejecutar una prueba de `/help`.
3. Probar `/sync` con el Fathom Core configurado.
4. Probar `/agendar` con un contacto de prueba.
5. Activar `OS-Emilia — Fathom Cron` al final.
6. Revisar las ejecuciones y los archivos creados en Drive.
7. Agregar estado conversacional, botones de confirmación y deduplicación desde la Data Table antes de usarlo con clientes reales.

### 16.7 Cal.com — consulta de Event Type

La API de Cal.com de Emilia se consultó mediante un workflow temporal de solo lectura. El endpoint requirió `cal-api-version: 2024-06-14` y devolvió:

- `7109198` — Reunión de 15 min.
- `7109200` — Reunión de 30 min.
- `7109199` — Reunión Secreta, oculto.

Se seleccionó `7109200` como evento predeterminado del flujo de agenda. El workflow temporal se desactivó y archivó después de la consulta. La credencial `ppi-EmiliaOS_Cal.com.Bearer Auth account` quedó asociada a `Create Cal.com Booking`.

### 16.8 Fathom — prueba de lectura y doble salida

La credencial `ppi-EmiliaOS_Fathom.-Header Auth account` fue corregida y validada. La prueba de lectura con filtro `recorded_by[]=proyectopi.31416@gmail.com` devolvió la reunión `Impromptu Google Meet Meeting`, `recording_id: 184073789`, del 17/09/2026. Su resumen menciona a Proyecto Pi y Emilia.

El Fathom Core quedó preparado para crear por cada reunión:

1. Un archivo Markdown de texto plano con extensión `.md`.
2. Un Google Doc con el mismo contenido, sin extensión `.md`, en la misma carpeta.

Las dos salidas usan `ppi-EmiliaOS_Google Drive account`; la credencial Google Docs queda disponible para una futura etapa de edición enriching. La clasificación usa como emails internos `arq.emiliapimentalombardi@gmail.com` y `proyectopi.31416@gmail.com`.

### 16.6 IDs de Drive confirmados

- Carpeta raíz `OS-Emilia`: `1sJqdw8_cqsaBiVjLQWnSccmTw6Ey52ad`.
- `Reuniones-Clientes`: `1l7EHaiKJQfKcatPkDCnYkkrCjHiqbNN5`.
- `Reuniones-Internas`: `1n5mkPNdHhgFEsYfLmx3LYD4sIUiHDtcQ`.

Estos IDs quedaron asignados a los nodos `Save Client Meeting` y `Save Internal Meeting` del Fathom Core. La credencial utilizada es `ppi-EmiliaOS_Google Drive account` (`F5AzgwsgpCsEth7M`).

