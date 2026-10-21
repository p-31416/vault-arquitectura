---
tipo: especificaciones
mvp: 06
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [especificaciones, mvp_06, agente-voz, telegram, n8n, cal-com, fathom, openrouter, vivo]
---

# 01-spec-mvp_06 — Agente de voz Telegram + n8n (documento canónico único)

Documento VIVO. Contiene SPEC, propuesta de valor, arquitectura, flujo nodo por nodo, ADRs, costos, documentación operativa y plan. La implementación nunca se aleja de este spec; si hay desvío, se actualiza acá primero.

> Proyecto propio de n8n, separado de [[proyectos/STUDIO_OS-Emilia/00-index|STUDIO_OS-Emilia]]. Reutiliza sus Cores como ejecutores y los deja intactos. Camino principal 100% lenguaje natural hablado y escrito, **sin comandos con slash**. Pruebas con la cuenta Proyecto Pi.

## 1. SPEC (qué se logra)

* Un mismo bot `@emiliaospi_bot` atiende por perfil: Sol en testing (cuenta `proyectopi.31416@gmail.com`), Emilia en producción cuando valide.
* El usuario habla o escribe normal ("agendame mañana 10h con Juan", "cancelá la del jueves", "cambiala a las 17", "qué tengo esta semana", "sincronizá mis reuniones") y el bot resuelve.
* Capacidades v1: agendar, cancelar, modificar, **revisar agenda** (próximas, semana, por cliente, "cuándo veo a X"), sincronizar Fathom a pedido, ayuda conversacional. Fathom automático por Cron 07:00 AR continúa por fuera.
* La operatoria real en Cal.com vive en el subflujo `OS-Studio — Agenda Sub TEST` (`ygdjqRfXpxKMFWEN`, patrón `LidIA_V5.0-SWF_Agenda` `w8iMJ01WGCSxvSMg`): un agente ejecutor con 5 tools Cal.com (slots, listar, agendar, reprogramar, cancelar) que hace todo con tu cred `Cal.com API Key`. Los contactos viven en el Agent Voz: `buscar_contacto` (lookup) + `agregar_contacto` (alta con nombre+email tras verificar duplicado) sobre `clientes-contactos`. El Agent Voz resuelve la ficha completa y la pasa en `query`; el subflujo exige ficha completa y falla cerrado sin email. Email siempre obligatorio (todo invitado recibe mail). Videollamada por defecto del evento Cal.com (se configura manual en Cal.com; el payload no envía ubicación; presenciales con dirección después).
* Fathom a pedido invoca `OS-Emilia — Fathom Core` (`UeDkqVZSeLnae5cF`) con el perfil activo.
* Cuentas de prueba: Cal `Cal.com API Key` (Proyecto Pi), hoja copia `clientes-sol-test`, carpeta Drive `OS-Sol` (raíz + `Reuniones-Internas` + `Reuniones-Clientes`). Producción Emilia (`ppi-EmiliaOS_*`, evento `7109200`, `OS-Emilia`) se conecta recién en M4.
* Entrada modelo: `LidIA_V5.0-PROD-Ycloud_Wsp` (`pw5OHhXNjeXSnD3u`) para audio/texto + normalizadores + debounce Redis. Agenda modelo: `LidIA_V5.0-SWF_Agenda` (`w8iMJ01WGCSxvSMg`) para Agent + `toolWorkflow` + memoria.
* Comandos slash quedan solo como fallback apagado; el camino principal no los expone ni los documenta al usuario.
* Criterio de éxito: 10 mensajes de prueba (5 texto + 5 voz) con 8/10 resueltos en <20s, 0 bookings sin confirmación, 0 `chat_id` fuera de allowlist atendidos.

## 2. Por qué vale este bot (y por qué escalar de comandos a IA)

### Lo que Siri ya hace y lo que este bot agrega

Siri revisa la agenda del teléfono. Este bot **opera** la agenda de trabajo: crea, mueve y cancela reuniones reales en Cal.com con invitación por email, responde qué hay esta semana con Refs accionables, y archiva Fathom en Drive — con los datos quedando en el ecosistema propio.

### Ventajas (listadas para validar)

1. **Contactos catalogados, no mezclados.** Busca solo en la planilla `clientes` que el usuario cura (`nombre,email,activo`); nunca entre todos los contactos del teléfono. Alta/baja de un cliente = 1 fila, sin alterar nada fuera del ecosistema.
2. **Lenguaje normal hablado y escrito.** Voz y texto entran al mismo Agent; el bot cita lo entendido y confirma antes de escribir en Cal.com.
3. **Datos propios.** Cada app de asistente con IA guarda el historial en su nube de pago y la información queda atrapada ahí; acá reuniones, contactos y decisiones quedan en Drive/vault/Leantime del estudio y mejoran con el uso.
4. **Revisión de agenda conversacional.** "Qué tengo esta semana", "cuándo veo a Juan", "listame las próximas" — lee Cal.com real y devuelve Refs para cancelar/modificar en el mismo hilo.
5. **Trazabilidad total.** Cada acción deja `Ref uid`, `usage.cost` y auditoría (quién, cuándo, qué perfil).
6. **Escala sin nuevos flujos.** Un perfil más = 1 fila en tabla.

### Por qué IA y no solo comandos

Los comandos ya resuelven la reserva; la IA existe para todo lo que excede la sintaxis fija:

* Desambiguación ("Juan" → propone candidatos de la planilla en vez de fallar por formato).
* Multi-paso en 1 mensaje ("agendame con Juan mañana a las 10 y pasame el link").
* Combinaciones ("sincronizá y decime qué tengo mañana").
* Seguimiento con memoria ("cambiala a las 17" entiende cuál reunión).
* Revisión de agenda en lenguaje libre con filtros (semana, cliente, internas vs clientes).
* Regla: lo que se resuelve igual de fácil con comando mantiene el comando como fallback; la IA se justifica por todo lo anterior, no por repetir comandos con otras palabras.

## 3. Arquitectura (1 bot, 0 multiplicación de flujos)

```text
Telegram @emiliaospi_bot (único webhook del token)
 → Auth allowlist (IF chat_id ∈ [Sol TEST, Emilia prod])
 → Tipos_Msj Switch v3.4 (audio: voice.file_id existe / txt: text existe / resto → ayuda)
   audio → Telegram file:get download=true → STT free: Gemini audio.transcribe
           (destino pago apagado: Code base64 → HTTP OpenRouter transcriptions) → Set texto
   txt   → Set texto = message.text
 → Normalizar W01+W02 {texto, nombre=from.first_name, ID=chat.id}
 → sendChatAction typing
 → Redis batch (GuardoMensaje push studio_os_ID → Wait 12s → RecuperoMensaje get
                 → If2 last==current → redis_mensaje join \n → EliminoMensajes)
 → OS Agent (`google/gemini-3.7-flash`, el mismo que usa LidIA en producción — el nodo allá se llama "luna-pro" pero el parámetro es Gemini)
     ├─ Tool Agenda → OS-Studio — Agenda Sub TEST (subflujo ejecutor + 5 tools Cal, tu cred Cal.com API Key, eventTypeId 0 fail-closed)
     ├─ buscar_contacto + agregar_contacto (planilla `clientes-contactos`: lookup y alta con verificación de duplicado)
     └─ Tool Sincronizar Fathom → Fathom Core (source telegram-voz-test)
 → Telegram sendMessage mismo chat_id (appendAttribution false)
Cron 07:00 existente (Emilia) intacto + 2° Cron TEST (Sol) al mismo Fathom Core
```

Agregar un tercer usuario = 1 fila en `OS-Bot-Profiles`, 0 workflows nuevos.

| perfil | chat_id | cal_cred | eventType | fathom | drive | sheet |
|---|---|---|---|---|---|---|
| sol test | `8459099332` (confirmado 2026-10-13 vía execs del Router; allowlist TEST) | `ppi_calcom-Bearer Auth account` (key propia cuenta proyectopi-31416; la anterior del paraguas escribe pero no lee) | `7467793` (`Reunión Semanal`, slug `30min`, duraciones 30/60/180, Meet default, `scheduleId: null` → usa Working hours default; lectura+escritura verificadas 2026-10-13) | key Sol o team con `recorded_by` Sol | `OS-Sol` (crear) | `clientes-contactos` (decisión 2026-10-13: hoja real compartida) |
| emilia prod (M4) | de su `/start` | `ppi-EmiliaOS_Cal.com` | `7109200` (+60min+Meet tras reunión) | `ppi-EmiliaOS_Fathom` | `OS-Emilia 1sJq...` | `clientes-contactos` |

### Normas de construcción n8n (obligatorias en este proyecto)

* **Norma normalizadores.** Todo flujo del proyecto normaliza la entrada a `{texto, nombre, ID}` en `W01+W02` antes de cualquier lógica — habilita escalar a nuevos canales sin reescribir el core.
* Norma Redis.** Toda entrada conversacional pasa por batch Redis (`studio_os_ID`, Wait 12s) para absorber ráfagas de mensajes cortos.
* **Norma memoria.** La conversación vive en el Agent Voz (Postgres por `chat.id`); el sub-agente usa Simple Memory por ejecución (`$execution.id`, sin estado entre llamadas).
* **Norma Switch.** Nodos `IF` nuevos creados por API no discriminan en esta instancia; usar `Switch` v3.4 con el patrón del Router.

## 4. Flujo nodo por nodo (workflow nuevo `OS-Studio — Agent Voz TEST`)

> Documento: esta misma sección es la referencia nodo por nodo del workflow https://n8n.pitau.tech/workflow/Gpd6NHB4HQdU7ary (el subflujo vive en https://n8n.pitau.tech/workflow/ygdjqRfXpxKMFWEN).

### Por qué `Detectar Entrada` es un nodo de código

El Trigger de Telegram emite formas distintas según lo que llegue: `message.text` (texto), `message.voice.file_id` (voz), `callback_query.data` (botones), y otras (`edited_message`, etc.). Un Switch no distingue "qué campo existe" sin expresiones frágiles, y los `IF` nuevos no evalúan en esta instancia. El Code clasifica una sola vez en `kind` (`audio|texto|callback|otro`), aplica la allowlist (`8459099332`, resto → `rechazado` que cae al fallback y se descarta) y extrae `fileId/chatId/nombre` — todo lo que sigue trabaja sobre ese contrato (norma normalizadores §3) y el Switch queda en igualdades de string triviales.

| # | Nodo | Tipo / cred | Qué hace |
|---|---|---|---|
| 0 | Telegram Trigger TEST | `telegramTrigger`, cred `emiliaospi_bot-Telegram account`, escucha `message + voice + audio + callback_query` | Único trigger del token en TEST (Router comandos queda apagado o convive solo como fallback) |
| 1 | Auth allowlist | `switch` sobre `message.chat.id` | TEST admite solo `8459099332` (Sol, confirmado 2026-10-13); resto recibe "bot privado" y fin. El filtro de Emilia se agrega en M4 |
| 2 | Tipos_Msj | `switch` v3.4 (patrón `Tipos_Msj` de `pw5OHhXNjeXSnD3u`) | `voice.file_id` existe → audio; `message.text` existe → txt; resto → ayuda conversacional |
| 3a | Telegram file:get | `telegram` resource `file` operation `get`, `download=true` | Descarga `oga` a binario `data`. Doc: [[wiki/glosario/software/n8n|n8n]] refs oficiales §8 |
| 4a | STT free | `googleGemini` resource `audio` operation `transcribe`, modelo `gemini-2.5-flash-lite`, cred `Google Gemini(PaLM) Api account`, `inputType binary` | Transcribe sin costo OpenRouter para la prueba |
| 4b | STT pago (apagado en free) | `code` base64 + `httpRequest` | `Code`: buffer binario → base64 raw. `HTTP POST https://openrouter.ai/api/v1/audio/transcriptions`, Bearer OpenRouter, body `{model: openai/whisper-large-v3-turbo, input_audio:{data, format: ogg}, language: es}` → `Set texto=$json.text` + auditoría `usage.cost` |
| 3b | Set texto txt | `set` | `texto=message.text` |
| 5 | Normalizar W01+W02 | 2× `set` (clon `normalizadorW01/W02`, norma §3) | Unifica `{texto, nombre, ID}` venga de voz o texto |
| 6 | Redis batch | `redis` push/get/delete + `wait` 12s + `if` + `set` (clon `GuardoMensaje→EsperoRedis→RecuperoMensaje→If2→redis_mensaje→EliminoMensajes`, key `studio_os_{{ID}}`, cred `Redis account`, norma §3) | Junta ráfagas ("agendame mañana... con Juan... a las 10") en 1 `mensajes` |
| 7 | OS Agent | `agent` + `lmChatOpenRouter` free fijo + `memoryPostgresChat` (`Postgres account`, `sessionKey=chat.id`) | System prompt con HOY AR, perfil Sol, reglas fecha, obligación de pedir email, propuesta juntos vs separado, confirmación con Ref antes de escribir, cita de lo entendido en voz |
| 8a | Tool Agenda | `toolWorkflow` → `OS-Studio — Agenda Sub TEST` (`ygdjqRfXpxKMFWEN`) | Recibe `query` en lenguaje natural; el subflujo (agente + 5 tools Cal) agenda, modifica, cancela y lista con tu cred |
| 8b | Tool Sincronizar Fathom | `toolWorkflow` → Fathom Core | Recibe pedido de sync; clasifica y guarda (hoy en `OS-Sol` cuando exista el perfil; mientras tanto no probar en vivo) |
| 8c | buscar_contacto | `googleSheetsTool` read `clientes-contactos` | Lookup `nombre` → email; el principal lo usa antes de agendar |
| 8d | agregar_contacto | `googleSheetsTool` append `clientes-contactos` | Alta `nombre+email` (activo Sí) tras verificar duplicado; el principal lo ofrece si no hay match |
| 9 | Responder | `telegram` `sendMessage` mismo `chat_id` | Confirmación con fecha AR + Ref + botones inline (`cancel:<uid>`, Confirmar/Cambiar). Callbacks los atiende el mismo Trigger |

System prompt (resumen): fecha HOY `America/Argentina/Buenos_Aires`; nadie inventa slots (primero consultar disponibilidad/listar, después crear); sin email no se agenda (se pide); direcciones solo calle+barrio al invitado; respuesta 2–3 líneas en rioplatense con 1 pregunta y CTA de confirmación.

## 5. ADRs

### ADR-2026-10-13-stt-free-then-turbo

**Fecha**: 2026-10-13 · **Estado**: propuesta · **Deciden**: SOL

**Contexto.** Voz Telegram (`oga/ogg/opus`, 10–20s, español rioplatense con nombres) necesita pasar a texto con gasto mínimo y trazabilidad única OpenRouter. El endpoint OpenRouter STT no ofrece tier free.

**Decisión.** Arrancamos STT free con Gemini nativo y dejamos listo el swap a `openai/whisper-large-v3-turbo` vía HTTP base64.

**Alternativas.** `turbo` pago directo ($0.000003/s, ~$0.04/mes, WER 12%, failover DeepInfra↔Groq): se adopta como destino, no de inicio para validar a costo cero. `whisper-1` (33× costo sin ganancia), `large-v3` (2.6× costo por +1.7% WER), `gpt-4o-mini-transcribe` (token-based caro en corto): costo/beneficio peor. `openrouter/free` para STT: inviable (router free solo texto+imagen).

**Consecuencias.** Prueba a costo cero, swap en 1 nodo; conviven 2 STT temporalmente. Riesgo WER en nombres → confirmación citada + `language: es`.

### ADR-2026-10-13-chat-free-then-floor

**Fecha**: 2026-10-13 · **Estado**: propuesta · **Deciden**: SOL

**Contexto.** Agent con tools necesita tool-calling estable en español con gasto mínimo; cada retry fallido sale más caro que el modelo barato que acierta.

**Decisión.** Agent ejemplo con free fijo (`deepseek-v4-distill:free` o `llama-4-scout:free`); destino `gemini-2.5-flash-lite:floor` ($0.10/M) con `provider.sort=price` + `max_price {prompt:1, completion:2}`, fallback `deepseek-v4-flash`.

**Alternativas.** `gpt-5.6-luna-pro` (LidIA): sobrecosto sin valor en agenda simple. `openrouter/free` rotativo: rompe coherencia de tools; se fija 1 free para la prueba.

**Consecuencias.** Topes free 20/min, 50–1000/día, sin ZDR. Mitigación: sesión abierta (prompt caching auto), retry 1 vez + mensaje de ocupado, jamás inventar slots.

### ADR-2026-10-13-transporte-http-base64

**Fecha**: 2026-10-13 · **Estado**: propuesta · **Deciden**: SOL

**Contexto.** El binario de voz necesita llegar a OpenRouter; n8n ofrece nodo OpenAI nativo, multipart y JSON base64.

**Decisión.** `HTTP Request JSON base64` (Code buffer → base64 raw + `format: ogg`).

**Alternativas.** Nodo OpenAI `audio.transcribe`: exige cred nueva, mismo resultado. Multipart: cap 25 MB y fricción con binarios n8n; doc OpenRouter recomienda base64 JSON.

**Consecuencias.** 0 credenciales nuevas, `usage.cost` auditable. Payload +33% irrelevante en notas <2 min. Timeout 60s → partir audios largos.

### ADR-2026-10-13-proyecto-propio-mvp_06

**Fecha**: 2026-10-13 · **Estado**: aceptada · **Deciden**: SOL

**Contexto.** El flujo se trataba como parte de Studio OS Emilia, lo que mezcla pruebas con producción y dificulta planes, ADRs y bitácora propios.

**Decisión.** El agente vive como proyecto propio `MVP_06-agente-voz`, con spec canónica única acá. `specs/261013-agente-voz-telegram-os.md` queda como antecedente superado que apunta acá. Studio OS Emilia solo aporta los Cores reutilizados.

**Consecuencias.** Trazabilidad limpia (spec+ft+log por proyecto), producción Emilia protegida, escala a más usuarios sin tocar su documentación.

### ADR-2026-10-13-revisar-agenda

**Fecha**: 2026-10-13 · **Estado**: propuesta · **Deciden**: SOL

**Contexto.** Siri lee la agenda del teléfono pero no opera Cal.com ni distingue contactos de trabajo; la revisión de agenda ("qué tengo esta semana") es el uso diario que sostiene el hábito del bot.

**Decisión.** El Agent expone `tool Agenda-leer` (lectura `GET /v2/bookings?status=upcoming` por perfil) con respuestas en lenguaje natural y Refs accionables para cancelar/modificar en el mismo hilo.

**Alternativas.** Solo comandos de escritura sin lectura: el bot agenda pero no informa; se descarta porque la lectura es el valor diferencial diario. Delegar lectura a Siri/otra app: fragmenta el ecosistema y pierde trazabilidad.

**Consecuencias.** Un tool más sobre el mismo endpoint ya probado; 0 credenciales nuevas. Riesgo de exponer invitados: se responde con nombres + fecha + Ref, sin mails ajenos.

## 6. Costos (OpenRouter, octubre 2026)

| Capa | Free prueba | Destino pago |
|---|---|---|
| STT | Gemini nativo $0 | `whisper-large-v3-turbo` $0.000003/s (~$0.04/mes por 30 notas/día) |
| Chat | free fijo $0 (topes arriba) | `gemini-2.5-flash-lite:floor` $0.10/M + fallback `deepseek-v4-flash` (~$1/mes uso normal) |

## 7. Documentación operativa

* Manual de uso (lenguaje normal, sin tecnicismos): [[proyectos/MVP_06-agente-voz/documentacion/manual-uso-agente-voz|manual-uso-agente-voz]] — qué decirle por voz y texto, revisión de agenda, Fathom, botones, FAQ.
* Credenciales y conexiones (mantenimiento): [[proyectos/MVP_06-agente-voz/documentacion/credenciales-conexiones|credenciales-conexiones]] — matriz credencial → uso → cadencia de revisión. Secrets solo en credenciales n8n, nunca en repos ni workflows.
* Cadencia: revisión mensual de 15 min (OAuth Drive/Docs/Sheets expiran —caso 08/10—, saldo OpenRouter, Redis, Postgres, Data Table perfiles).

## 8. TASKS (detalladas, vía `@fathom-pm` → Leantime)

> Proceso: estas tasks se trabajan con el subagente `@fathom-pm` (PM del vault: SPEC/PLAN/TASKS/MILESTONES-OKRs + regla pomodoro) y se cargan a Leantime (manual lunes 15 min hasta MCP; estados `borrador → aprobado → en-leantime`). Regla dura: subtask ≤25 min, tope 16/día por persona, WIP máx 2. Cada TASK cita su milestone.

* [ ] **M1 infra Sol** — crear `OS-Sol` (raíz + 2 subcarpetas) [10 min] · planilla: se usa `clientes-contactos` real (decisión 2026-10-13, sin copia) [0 min] · leer tu `eventTypeId` Cal.com y registrar fila sol en `OS-Bot-Profiles` [15 min] · confirmar tu `chat_id` con `/start` [5 min] ✓ (`8459099332`)
* [ ] **M1 build entrada** — clonar Auth + Tipos + STT Gemini + Normalizar + Redis de `pw5OHhXNjeXSnD3u` al workflow TEST [25 min] · cablear rama HTTP turbo apagada [15 min]
* [ ] **M1 build agent** — cablear Agent free + Postgres memory + Tool Agenda (subflujo `ygdjqRfXpxKMFWEN`) [25 min] · cablear Tool Fathom + responder Telegram [25 min]
* [ ] **M2 validación escritura** — probar 5 mensajes (agendar texto, agendar voz, cancelar, modificar, listar) [25 min] · registrar resultados en `03-log` [10 min]
* [ ] **M2 validación lectura+sync** — probar "qué tengo esta semana" + "cuándo veo a X" + "sincronizá" por voz y texto [25 min] · medir latencia, WER en nombres, `usage` [20 min]
* [ ] **Docs** — publicar manual de uso [25 min] · publicar matriz credenciales [25 min]
* [ ] **M3 swap pago** — activar turbo + `flash-lite:floor` + fallback [15 min] · crear 2° Cron TEST [10 min] · medir costos 7 días [10 min]
* [ ] **M4 Emilia prod** — conectar perfil Emilia sin tocar Cores [25 min] · archivar slash como fallback [10 min]

## 9. MILESTONES y OKRs

* **M1 — TEST free operativo.** Voz y texto llegan al Agent con tu cuenta.
* **M2 — Validación 8/10.** Métricas en bitácora (incluye revisión de agenda por voz).
* **M3 — Swap pago mínimo.** ~$1–2/mes, auditable.
* **M4 — Emilia prod.** Lenguaje natural convive con slash como fallback, sin nuevos flujos por usuario.

**OKR:** 100% mensajes TEST respondidos en <20s, 0 bookings sin confirmación, 0 fuera de allowlist atendidos, 0 workflows nuevos al sumar usuario.

## Fuentes

* OpenRouter STT crear transcripción: https://openrouter.ai/docs/api/api-reference/stt/create-transcription (verificado 2026-10-13 — 200)
* OpenRouter guía STT: https://openrouter.ai/docs/guides/overview/multimodal/stt (verificado 2026-10-13 — 200)
* OpenRouter tutorial transcripción: https://openrouter.ai/blog/tutorials/transcription-on-openrouter/ (verificado 2026-10-13 — 200)
* OpenRouter colección STT: https://openrouter.ai/collections/speech-to-text-models (verificado 2026-10-13 — 200)
* n8n Telegram node: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/ (verificado 2026-10-13 — 200)
* n8n Telegram file:get: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations.md (verificado 2026-10-13 — 200)
* n8n Telegram Trigger: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger.md (verificado 2026-10-13 — 200)
* Vault: [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura-n8n-os-emilia]] · [[260924-plan-os-emilia-n8n|plan-os-emilia-n8n]] · [[wiki/glosario/software/telegram|telegram]] · [[wiki/glosario/software/n8n|n8n]] · agente `.opencode/agents/fathom-pm.md` → Leantime
* n8n: Router `YWpuV5p0vCDTbIHz`, Agenda `UTkII2kd3RHDlizo`, Cancel `B7gGFGcD89vKfc5k`, Modif `c08s62Lo9EmAEJJf`, Fathom `UeDkqVZSeLnae5cF`, entrada modelo `pw5OHhXNjeXSnD3u`, agenda modelo `w8iMJ01WGCSxvSMg`
