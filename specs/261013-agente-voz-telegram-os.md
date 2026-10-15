---
tipo: plan
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [specs, telegram, agente-voz, openrouter, stt, n8n, studio-os, emilia, sol]
idioma: es
estado: superado por [[proyectos/MVP_06-agente-voz/01-spec-mvp_06|01-spec-mvp_06]]
---

# PLAN — Agente voz + lenguaje natural Telegram (flujo ejemplo TEST en cuenta Sol)

> **Estado al 2026-10-13: SUPERADO — el plan canónico vive ahora como proyecto propio en [[proyectos/MVP_06-agente-voz/01-spec-mvp_06|MVP_06 01-spec-mvp_06]] (SPEC + flujo + nodos + ADRs en un solo documento). Este archivo queda como antecedente; no se edita más.**

> Un mismo bot `@emiliaospi_bot` responde a Emilia (producción) y Sol (testing). Entrada texto + voz en lenguaje natural para agendar, cancelar, modificar y sincronizar Fathom a pedido más cron automático. Fase ejemplo 100% free para validar, con swap a pago mínimo en 2 nodos. Reutiliza Cores existentes sin multiplicar flujos. Modelo de entrada: `LidIA_V5.0-PROD-Ycloud_Wsp` (`pw5OHhXNjeXSnD3u`).

## SPEC (qué se decide)

* Bot único Telegram `@emiliaospi_bot` (cred `emiliaospi_bot-Telegram account`). Un solo `Telegram Trigger` activo por token.
* Modalidades: texto + voz + audio + `callback_query` (botones Confirmar/Cambiar/Cancelar y `cancel:<uid>`).
* Capacidades v1 ejemplo: agendar, cancelar, modificar, listar próximas, `sync_fathom` a pedido, ayuda. Fathom automático por Cron 07:00 AR intacto.
* Cuentas ejemplo: todo a Sol (`proyectopi.31416@gmail.com`) — su Cal (`Cal.com API Key`), su hoja copia `clientes-sol-test`, su carpeta `OS-Sol` (a crear). Emilia queda en producción sin tocarse.
* STT fase free: nodo Gemini `audio.transcribe` nativo (cred `Google Gemini(PaLM) Api account`, modelo `gemini-2.5-flash-lite`). Destino pago: HTTP OpenRouter `POST /audio/transcriptions` modelo `openai/whisper-large-v3-turbo`, `language: es`.
* Chat fase free: `openrouter/free` fijo con tool-calling (`deepseek/deepseek-v4-distill:free` o `meta-llama/llama-4-scout:free`). Destino pago: `google/gemini-2.5-flash-lite:floor` con `provider.sort=price` + `max_price`, fallback `deepseek/deepseek-v4-flash`.
* Patrón ejecución: 1 Agent único con sub-flujos como `toolWorkflow` (Agenda + Fathom Sync). Switch solo técnico antes del Agent (auth + audio/txt). Sin clasificador humano, sin sub-agente separado.
* Debounce Redis copiado de LidIA (key `studio_os_{{chat_id}}`): junta mensajes en ráfaga en 1 `mensajes` para el Agent.
* Memoria `Postgres Chat Memory` (`Postgres account`, `sessionKey=chat.id`), compartida texto + voz.

## PLAN (cómo)

### Grupos canvas (8, workflow nuevo `OS-Studio — Agent Voz TEST`)

```text
0 Auth allowlist (IF chat_id en [Sol TEST, Emilia prod], resto → mensaje privado + fin)
1 Tipos_Msj Switch v3.4 (audio: voice.file_id existe / txt: text existe / UK → ayuda)
2a Rama audio free: Telegram file:get download=true → Gemini audio.transcribe binary → Set texto
2b Rama audio destino pago (apagada en free): Code base64 → HTTP OpenRouter transcriptions → Set texto
3 Rama txt: Set texto=message.text
4 Normalizar W01+W02: {texto, nombre=from.first_name, ID=chat.id}
5 Redis batch: Edit Fields2 → GuardoMensaje push → EsperoRedis Wait 12s → RecuperoMensaje get → If2 last==current → redis_mensaje join \n → EliminoMensajes
6 OS Agent + memory Postgres + tools (Agenda TEST, Fathom Sync TEST)
7 Responder Telegram sendMessage mismo chat_id, appendAttribution false + sendChatAction typing previo
```

### Detalle STT destino pago (2 nodos, apagados en free)

1. `Code base64`:
```js
const buf = await this.helpers.getBinaryDataBuffer(0, 'data');
return [{ json: { base64: buf.toString('base64'), format: 'ogg' } }];
```
2. `HTTP Request POST https://openrouter.ai/api/v1/audio/transcriptions`, auth `httpBearerAuth` con key OpenRouter (`OpenRouter account`), body JSON:
```json
{"model":"openai/whisper-large-v3-turbo","input_audio":{"data":"={{ $json.base64 }}","format":"ogg"},"language":"es","response_format":"json"}
```
3. `Set texto={{ $json.text }}` + guarda `usage.cost` + `usage.seconds` en auditoría.

### Tools del Agent

* `toolWorkflow Agenda TEST`: envuelve `OS-Emilia — Agenda Core`, `Cancel Core`, `Modif Core` con perfil Sol inyectado (`query` en lenguaje natural + `chat_id`). Expone agendar/modificar/cancelar/listar.
* `toolWorkflow Fathom Sync TEST`: envuelve `OS-Emilia — Fathom Core` con `source: telegram-voz-test` + filtro Sol. Cron 07:00 existente sigue para Emilia; se agrega 2° Cron TEST para Sol con su filtro y carpetas.
* System prompt: fecha HOY `America/Argentina/Buenos_Aires`, perfil activo, reglas fecha (mañana=+1, pasado=+2, el jueves=próximo), obligación de pedir email si falta, propuesta juntos vs separado, confirmación con Ref antes de escribir en Cal.com, cita de lo entendido en voz.

### Tabla perfiles (escala sin nuevos flujos)

| perfil | chat_id | cal_cred | eventType | fathom | drive | sheet |
|---|---|---|---|---|---|---|
| emilia prod | de su `/start` | `ppi-EmiliaOS_Cal.com` | `7109200` (+60min+Meet tras reunión) | `ppi-EmiliaOS_Fathom` | `OS-Emilia 1sJq...` + `1l7E...` + `1n5m...` | `clientes-contactos` |
| sol test | `8459099332` (confirmar) | `Cal.com API Key` | eventType Sol (pendiente) | key Sol o team con `recorded_by` Sol | `OS-Sol` (crear raíz + 2 subcarpetas) | `clientes-sol-test` (copia) |

## TASKS (construcción + prueba free)

* [ ] Crear `OS-Sol` en Drive (raíz + `Reuniones-Internas` + `Reuniones-Clientes`) y hoja `clientes-sol-test` (columnas `nombre,email,activo`)
* [ ] Crear Data Table `OS-Bot-Profiles` con filas emilia/sol (campos §PLAN)
* [ ] Crear workflow `OS-Studio — Agent Voz TEST`: Trigger + Auth + Switch tipos + rama audio Gemini + normalizadores + Redis (clonar de `pw5OHhXNjeXSnD3u`) + Agent free + memory Postgres + 2 tools + responder
* [ ] Dejar rama HTTP OpenRouter turbo + modelo pago chat cableadas pero desactivadas (swap en 2 nodos)
* [ ] Fijar allowlist a tu `chat_id`, probar desde Telegram: 5 texto + 5 voz 10–20s en español con nombres reales
* [ ] Medir: tasa éxito, latencia, WER en nombres, `usage` por mensaje; umbral pase 8/10
* [ ] Con pase: activar swap pago (turbo + flash-lite `:floor`), crear 2° Cron TEST Sol, documentar costos reales 7 días
* [ ] Recién después: replicar perfil Emilia prod al Agent (sin tocar Cores)

## MILESTONES y OKRs

* **M1 — Ejemplo TEST free operativo:** voz y texto llegan al Agent con tu cuenta, 0 credenciales nuevas salvo las ya existentes.
* **M2 — Validación 8/10:** 10 mensajes prueba con métricas en log.
* **M3 — Swap pago mínimo:** costo mensual ~$1–2 total, `usage.cost` auditable por mensaje.
* **M4 — Emilia prod al Agent:** comandos legacy conviven con lenguaje natural, sin duplicar workflows.

**OKR:** 100% mensajes TEST con respuesta en <20s, 0 bookings sin confirmación, 0 `chat_id` fuera de allowlist atendidos, 0 workflows nuevos al agregar 3er usuario.

## ADRs (decisión justificada, gasto mínimo)

### ADR-2026-10-13-stt-free-then-turbo

**Fecha**: 2026-10-13
**Estado**: propuesta
**Deciden**: SOL
**Proyecto**: estudio (Studio OS)

#### Contexto

Voz Telegram (`oga/ogg/opus`, notas 10–20s, español rioplatense con nombres propios) necesita pasar a texto con gasto mínimo y trazabilidad única OpenRouter. El endpoint OpenRouter STT no ofrece tier free.

#### Decisión

Arrancamos STT free con Gemini nativo y dejamos listo el swap a `openai/whisper-large-v3-turbo` vía HTTP base64.

#### Alternativas

##### Alternativa 1: whisper-large-v3-turbo pago directo ($0.000003/s)

* Pros: 33× más barato que `whisper-1`, WER 12%, 216x realtime, failover DeepInfra↔Groq, `usage.cost` por request
* Contras: gasta desde el día 1 (~$0.04/mes igual)
* Por qué no ahora: se quiere validar flujo con costo cero antes

##### Alternativa 2: whisper-1 / large-v3 / gpt-4o-mini-transcribe

* Pros: misma API
* Contras: `whisper-1` 33× costo sin ganancia; `large-v3` 2.6× costo por +1.7% WER; `mini-transcribe` token-based caro en notas cortas y rechaza `verbose_json` en endpoints
* Por qué no: costo/beneficio peor para notas cortas

##### Alternativa 3: openrouter/free para STT

* Pros: costo cero teórico
* Contras: no existe — el router free solo acepta texto+imagen, el endpoint STT es pago por doc oficial
* Por qué no: inviable técnica

#### Consecuencias

Positivas: costo cero en prueba, swap en 1 nodo. Negativas: 2 implementaciones STT conviven temporalmente. Riesgos + mitigación: WER en nombres → confirmación citada ("Entendí: ... ¿confirmo?") + `language: es`.

### ADR-2026-10-13-chat-free-then-floor

**Fecha**: 2026-10-13
**Estado**: propuesta
**Deciden**: SOL

#### Contexto

Agent con tools (Agenda + Fathom) necesita tool-calling estable en español con gasto mínimo. Free falla más y cada retry sale caro.

#### Decisión

Agent ejemplo con free fijo (`deepseek-v4-distill:free` o `llama-4-scout:free`), destino `gemini-2.5-flash-lite:floor` ($0.10/M) con `provider.sort=price` + `max_price {prompt:1, completion:2}`, fallback `deepseek-v4-flash`.

#### Alternativas

##### Alternativa 1: gpt-5.6-luna-pro (LidIA)

* Pros: probado en LidIA
* Contras: sobrecosto sin valor para agenda simple
* Por qué no: gasto mayor sin ganancia en esta tarea

##### Alternativa 2: openrouter/free rotativo

* Pros: cero costo
* Contras: salta de modelo por turno, rompe coherencia de tools y memoria
* Por qué no: se fija 1 free para la prueba

#### Consecuencias

Positivas: prueba gratis, techo anti-sorpresa en pago. Negativas: free con topes 20/min, 50–1000/día, sin ZDR. Mitigación: sesión abierta (prompt caching auto en DeepSeek/Gemini), retry 1 vez + 2° free + mensaje de ocupado, nunca inventar slots.

### ADR-2026-10-13-transporte-http-base64

**Fecha**: 2026-10-13
**Estado**: propuesta
**Deciden**: SOL

#### Contexto

Binario de voz Telegram necesita llegar a OpenRouter. n8n ofrece nodo OpenAI nativo, multipart y JSON base64.

#### Decisión

Usamos `HTTP Request JSON base64` (Code buffer → base64 raw + `format: ogg`).

#### Alternativas

##### Alternativa 1: nodo OpenAI audio.transcribe

* Pros: nativo
* Contras: exige cred `openAiApi` nueva, misma red, más setup
* Por qué no: 0 credenciales nuevas con HTTP + Bearer existente

##### Alternativa 2: multipart file

* Pros: estilo OpenAI clásico
* Contras: cap 25 MB, fricción binarios n8n; doc OpenRouter recomienda base64 JSON para archivos grandes
* Por qué no: más frágil en n8n para este caso

#### Consecuencias

Positivas: 0 credenciales nuevas, `usage.cost` auditable. Negativas: payload +33% por base64 (irrelevante en notas <2 min). Riesgo timeout 60s → partir audios largos y pedir reenvío.

## Fuentes

* OpenRouter STT crear transcripción: https://openrouter.ai/docs/api/api-reference/stt/create-transcription (verificado 2026-10-13 — 200)
* OpenRouter guía STT + modelos `?output_modalities=transcription`: https://openrouter.ai/docs/guides/overview/multimodal/stt (verificado 2026-10-13 — 200)
* OpenRouter tutorial transcripción + costos por segundo/token: https://openrouter.ai/blog/tutorials/transcription-on-openrouter/ (verificado 2026-10-13 — 200)
* OpenRouter colección STT (turbo $0.000003/s, large-v3 $0.000008/s, whisper-1 $0.0001/s): https://openrouter.ai/collections/speech-to-text-models (verificado 2026-10-13 — 200)
* n8n Telegram node: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/ (verificado 2026-10-13 — 200)
* n8n Telegram file:get: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations.md (verificado 2026-10-13 — 200)
* n8n Telegram Trigger: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger.md (verificado 2026-10-13 — 200)
* Vault: [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura-n8n-os-emilia]] · [[specs/260924-plan-os-emilia-n8n|plan-os-emilia-n8n]] · [[wiki/glosario/software/telegram|telegram]] · [[wiki/glosario/software/n8n|n8n]]
* n8n: Router `YWpuV5p0vCDTbIHz`, Agenda `UTkII2kd3RHDlizo`, Cancel `B7gGFGcD89vKfc5k`, Modif `c08s62Lo9EmAEJJf`, Fathom `UeDkqVZSeLnae5cF`, entrada modelo `pw5OHhXNjeXSnD3u`, agenda modelo `w8iMJ01WGCSxvSMg`
