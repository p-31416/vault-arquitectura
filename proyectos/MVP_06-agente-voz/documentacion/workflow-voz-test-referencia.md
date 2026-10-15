---
tipo: referencia
mvp: 06
fecha_creacion: 2026-10-14
ultima_actualizacion: 2026-10-14
tags: [referencia, mvp_06, telegram, n8n, nodos, credenciales, edicion]
---

# Referencia — Workflow Telegram Voz TEST

> Documento único: qué hace cada nodo, cómo está configurado, qué credenciales usa, cómo editar el flujo y cómo ordenarlo con post-its por bloque. Workflow: `OS-Studio — Agent Voz TEST (revision)` · ID `Gpd6NHB4HQdU7ary` · [abrir en n8n](https://n8n.pitau.tech/workflow/Gpd6NHB4HQdU7ary)

## 0. El flujo en 30 segundos

```
Telegram ─► Detectar ─► Tipos ─┬─► Voz: Descargar ► Transcribir ► Fijar
(chat 8459099332)   (código)   │   Texto: Fijar ─► Normalizar ► Contexto
                               └─► Callback: Sintetizar ──────────┘
        ─► Guardar (Redis) ─► Esperar 12s ─► Recuperar ─► ¿Último? ─► Armar lote ─► Limpiar
        ─► Agente Voz (+ modelo, memoria, 4 tools) ─► Responder Telegram
```

Voz o texto llegan al mismo agente. Los mensajes se agrupan 12 segundos (por si hablás en partes), el agente resuelve el contacto en la planilla y opera Cal.com/Fathom vía subflujos, y responde en rioplatense. Antes de escribir en tu agenda siempre pide confirmación.

## 1. Bloques y nodos (en orden de ejecución)

### Bloque A — Entrada (filtra que seas vos)

| Nodo | Tipo | Qué hace | Config clave |
|---|---|---|---|
| Telegram TEST Trigger | Trigger Telegram | Escucha todo lo que llega al bot | `updates: message + callback_query`, allowlist `chatIds: 8459099332` — nadie más lo activa |
| Detectar Entrada | Code | Clasifica cada update y rechaza chats ajenos | Si `chatId !== 8459099332` → `kind: rechazado`. Voz → `audio`, texto → `texto`, botón → `callback` |
| Tipos Entrada | Switch | Deriva a la rama que corresponde | 3 salidas: `audio`, `texto`, `callback` (+ `Otro` de respaldo) |

### Bloque B — Normalización (las 3 ramas vuelven a un solo texto)

| Nodo | Tipo | Qué hace | Config clave |
|---|---|---|---|
| Descargar Voz | Telegram (file) | Baja el archivo de voz | Credencial Telegram; `fileId` del mensaje |
| Transcribir Voz | Google Gemini | Pasa el audio a texto | Modelo `models/gemini-2.5-flash-lite`; credencial Google Gemini(PaLM) |
| Fijar Texto Voz | Set | Guarda texto transcripto + nombre + chat | Lee `text` del resultado Gemini |
| Fijar Texto Escrito | Set | Guarda texto escrito + nombre + chat | Directo del mensaje |
| Sintetizar Callback | Set | Convierte el botón tocado en texto | Botón de cancelar → `/cancel <Ref>` para que el agente lo entienda |
| Normalizar W02 | Set | Unifica las 3 ramas en `texto / nombre / ID` | A partir de acá el flujo ya no distingue voz de texto |
| Fijar Contexto | Set | Renombra a `TXT_Mensaje / ID_Chat / Nickname` | Formato que espera el loteo |

### Bloque C — Loteo anti-fragmento (memoria temporal Redis)

Si mandás 3 mensajes seguidos, no querés 3 respuestas: se juntan 12 segundos y responde una sola vez.

| Nodo | Tipo | Qué hace | Config clave |
|---|---|---|---|
| Guardar Mensaje | Redis push | Agrega tu mensaje a la cola | Lista `studio_os_test_8459099332` (una por chat), al final |
| Esperar Lote | Wait 12s | Pausa para dejar llegar el resto | `amount: 12` segundos |
| Recuperar Lote | Redis get | Lee toda la cola acumulada | Misma lista; trae `mensajes` |
| Es Ultimo Mensaje | Switch | Solo el último mensaje procesa el lote | Compara el último de la cola con el actual; los anteriores salen por `Obsoleto` y mueren ahí |
| Armar Lote | Code | Une los textos con saltos de línea + nickname | `mensajes` (unidos) y `Nickname` para el agente |
| Limpiar Lote | Redis delete | Borra la cola para no reprocesarla | Misma key; si no se borrara, repetiría respuestas |

### Bloque D — Agente y respuesta

| Nodo | Tipo | Qué hace | Config clave |
|---|---|---|---|
| Agente Voz TEST | AI Agent v3.1 | El cerebro: entiende y llama tools | REGLA 1 (siempre `buscar_contacto` primero), REGLA OFRECER (solo propone horario validado con el subflujo), confirmación antes de escribir; `maxIterations: 6`; cita lo entendido si vino de voz. Reglas completas del sistema en punto 1bis |
| Modelo Free TEST | OpenRouter chat | El modelo que razona | `openai/gpt-5.6-luna`, `temperature: 0.3` |
| Memoria Postgres TEST | Memoria chat | Recuerda las últimas 10 interacciones | Tabla `studio_os_test`, clave = tu chat ID; es lo que le da continuidad ("cambiala a las 5" sabe de qué hablás) |
| Tool Agenda | Subflujo | Toda la operatoria Cal.com | Invoca `OS-Studio — Agenda Sub TEST`; recibe el pedido con ficha completa |
| Tool Sincronizar Fathom | Subflujo | Trae reuniones nuevas de Fathom | Invoca `OS-Emilia — Fathom Core` con `source: telegram-voz-test` |
| buscar_contacto | Google Sheets tool | Devuelve TODA la planilla para matchear | Doc `clientes-contactos`, hoja `clientes` (gid `207767283`); match insensible a mayúsculas/acentos/parcial |
| agregar_contacto | Google Sheets tool | Da de alta nombre+email+activo=Sí | Misma planilla; solo cuando no hay match real |
| Responder Telegram | Telegram | Manda la respuesta al chat | Fijo a `chatId: 8459099332`; texto = `output` del agente (o disculpa de respaldo) |

## 1bis. Reglas vigentes del sistema (padre + subflujo agenda)

Las del padre viven en `Agente Voz TEST`; las del subflujo en `Agente Agenda TEST` del workflow `OS-Studio — Agenda Sub TEST`. Resumen a hoy:

* **REGLA 1**: ante pedido de agendar, primero `buscar_contacto`, sin excepción.
* **REGLA OFRECER**: jamás proponer día/hora sin validarlo antes con el subflujo.
* **REGLA FICHA**: nombre/email del invitado salen siempre de la ficha, nunca de otros bookings ni del dueño de la cuenta.
* **REGLA MODIFICAR**: reprogramar va directo a `actualizar_reunion`, sin chequeo previo; solo ante conflicto real se consultan slots ignorando el bloque propio.
* **REGLA DURACION**: cambiar duración = cancelar + reagendar (la API no lo permite en un paso); se avisa la Ref nueva.
* **REGLA HORAS**: lo que trae `-03:00` se copia tal cual; solo se convierte lo que termina en `Z`. Nunca restar dos veces.
* **Agenda**: solo cuentan bookings `accepted`; los `cancelled` se ignoran. Alternativas siempre con día, hora y duración.
* **HORARIO CAL.COM**: schedule Working hours Lun–Vie 9–17 (id `2495785`); sábados apagados a nivel cuenta. Evento `7467793` sin schedule propio (usa el default). Google primario conectado y seleccionado: eventos manuales sí bloquean slots.
* **RECURRENCIA**: la API no crea recurrentes; se agenda la primera ocurrencia y se avisa.

## 2. Credenciales (todas reutilizables, ninguna se toca al editar prompts)

| Credencial | Tipo | Dónde se usa | Nota |
|---|---|---|---|
| `emiliaospi_bot-Telegram account` | Telegram API | Trigger + Descargar Voz + Responder | Mismo token que el Router de producción: **el último workflow activado se queda con el webhook** |
| `Redis account` | Redis | Guardar / Recuperar / Limpiar lote | Solo la cola temporal de 12s |
| `Postgres account` | Postgres | Memoria del agente | Tabla `studio_os_test`, 10 mensajes de ventana |
| `OpenRouter account` | OpenRouter | Modelo del agente | Facturación por uso; hoy ~cero |
| `Google Gemini(PaLM) Api account` | Google Gemini | Transcripción de voz | Gratis en este volumen |
| `ppi-EmiliaOS_Google Sheets account` | Google Sheets OAuth | buscar/agregar contacto | Lee tu planilla `clientes` |

## 3. Cómo editar el flujo (sin romper nada)

1. **Abrí el link** de arriba. Lo que ves es el borrador; lo que corre es la versión **publicada**. Cambiar nodos no afecta lo que corre hasta que publicás.
2. **Prompts** (lo más común): doble clic en `Agente Voz TEST` → campo system message → editar → **Save** → arriba a la derecha **Publish**. Sin Publish, Telegram sigue con lo viejo.
3. **Probar sin Telegram**: botón `Test workflow` (abajo) ejecuta el borrador con datos simulados; los nodos con credencial se saltean. Para pruebas reales de agenda usá el chat (el TEST responde ahí).
4. **Desactivar un nodo sin borrarlo**: clic derecho → Disable. Útil para aislar un problema.
5. **Historial**: menú `⋯` → Version history → ves cada Publish con su nombre y podés restaurar. Todo cambio importante se publica con nombre descriptivo.
6. **Regla de oro del webhook**: si el bot de producción (Emilia) deja de responder, es porque este TEST le robó el webhook. Revert: este workflow **Off** → Router **Off y On** → mandar `/help` para verificar.

## 4. Post-its por bloque (cómo ordenar el canvas)

Los post-its son solo visuales (no afectan la ejecución) y sirven para marcar los bloques del punto 1:

1. Botón `+` del canvas → **Sticky note** → escribí el nombre del bloque (ej. `## A — Entrada`, `## B — Normalización`, `## C — Loteo Redis`, `## D — Agente`).
2. Arrastralo detrás de sus nodos y estiralo hasta enmarcarlos.
3. Color sugerido fijo para no marearse: Entrada = azul, Normalización = verde, Loteo = amarillo, Agente = rosa, Notas de peligro (webhook) = rojo.
4. Un post-it rojo permanente arriba del Trigger que diga *"Mismo token que el Router — ver punto 3.6"* evita el 90% de los accidentes.
5. Si un bloque crece (ej. nueva tool), agrandá su post-it en vez de crear otro: un bloque = un post-it.

## 5. Múltiples eventos Cal.com (tu pregunta de la reunión semanal)

Hoy el subflujo tiene **un solo event ID** (`7467793`, `Reunión Semanal`) escrito en 6 tools + prompt. Cambiarlo por otro es fácil (buscar/reemplazar, 10 min), pero **no hace falta cambiarlo para agendar con gente de afuera**: el evento es solo la plantilla (duraciones, Meet, horario); el invitado puede ser cualquiera con email. Lo de "Emilia OS" que viste es la identidad de la cuenta organizadora en el email de Cal.com, no una restricción.

Si querés tipos distintos (ej. `Reunión semanal` para interno + `Llamada cliente` para afuera): se crea el segundo evento en Cal.com y se agrega una regla al prompt ("interno → ID A, cliente → ID B") con el ID como parámetro de las tools. Complejidad baja; se hace cuando lo pidas.

## 6. Probado

- **Memoria temporal Redis (loteo)**: probado 2026-10-14 con 6 fragmentos seguidos → 5 ejecuciones `Obsoleto` + 1 respuesta combinada. OK.
