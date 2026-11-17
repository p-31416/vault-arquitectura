---
tipo: spec
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [spec, agente, pi-imagenes, pollinations, flux, n8n, telegram, hermes]
estado: activo
---

# Agente pi imágenes — spec único

> Todo lo del agente de primera clase `pi imágenes` (`FWGtRuylIqexTigj`): https://n8n.pitau.tech/projects/pWOSkiVhnAWt5tSi/agents/FWGtRuylIqexTigj. Asistente genérico de generación de imágenes para arquitectura. Estado: draft validado, sin publicar (publicar + Telegram con tu `s`).

- [[#Objetivo]]
- [[#Estado actual]]
- [[#Cerebro y routing de motores]]
- [[#Prompting por motor]]
- [[#Edición e imagen de entrada]]
- [[#Capabilities: 3 tools HTTP + qué más sirve]]
- [[#Memoria y sessions]]
- [[#Knowledge y vector stores]]
- [[#Budget, sesiones y loops]]
- [[#Subagentes y custom model routing]]
- [[#MCP]]
- [[#Telegram]]
- [[#Skills y referencias]]
- [[#Build log]]
- [[#Fase Hermes]]
- [[#Gates]]
- [[#Costos]]
- [[#Riesgos]]

## Objetivo

Un agente que interpreta pedidos en lenguaje natural y genera o edita imágenes solo, sin prefijos ni copy-paste. Genérico para arquitectura (no atado al concurso), con el contrato listo para que Hermes lo tome después.

## Estado actual

Agente de primera clase, proyecto PI, draft validado sin errores, probado con `call_agent` (exploración Gaudí + cabaña genérica, ambas con URL válida). Sin publicar. Sin integración Telegram (pendiente tu ID para `allowedUsers`).

| Punto | Estado |
|---|---|
| Nombre | `pi imágenes` |
| Cerebro | `openrouter/z-ai/glm-5.3-flash` (con imagen, sin tilde que rompe el runtime) |
| Credencial LLM | `OpenRouter account` activa |
| Credencial imagen | `ppi-Pollinations(sk-)` en los 3 tools |
| Memoria | Activada (`storage: n8n`) |
| Budget | USD 1 mensual, alerta al 50% |
| Skills | `prompting-arquitectura` (genérica) + `prompt-cascara-gaudi` (solo concurso) |

## Cerebro y routing de motores

GLM 5.3 Flash: barato ($0.0399/$0.0784 por 1M tokens), con imagen, tool-calling verificado. El agente elige tool según pedido: explorar flux schnell (0.002), lámina flux 1.1-pro (0.03, 1280x704), nítido z-image (0.004), texto mai-flash (1280x768 mínimo), edición kontext (0.03).

## Prompting por motor (Pollinations solo entiende prompt)

- schnell: corto, 30-50 palabras, un sujeto, una luz.
- 1.1-pro: 50-80 palabras con atmósfera; dimensiones múltiplos de 32.
- z-image: directo y nítido.
- mai-flash: único fiable con texto; alto mínimo 768px.
- kontext: NUNCA redescribe; conserva (misma cámara, geometría, contexto) + cambia UNA variable; máximo 3 edits, después regenera.
- Siempre: prosa en positivo, sin negaciones, sin 8k/masterpiece, sin JSON en FLUX, sin comillas dobles.

## Edición e imagen de entrada

Tool `editar_imagen` (`POST /v1/images/edits`, kontext): prompt conserva+cambia + `image_url` pública. La foto de Telegram llega como binario al workflow, no como URL — el loop con foto vive en el workflow Eval hasta que haya upload a URL; en el agente funciona cuando el usuario pega URL. Anotar sobre la foto (círculos/flechas) lo interpreta el modelo si el usuario lo describe.

## Capabilities: 3 tools HTTP + qué más sirve

| Tool | Qué hace | Cuándo |
|---|---|---|
| generar_explorar | POST generations flux schnell, dims fijos 1280x720 seed 7 | Todo pedido nuevo |
| generar_lamina | POST generations flux 1.1-pro 1280x704 | Versión final |
| editar_imagen | POST edits kontext con image_url | Cambios sobre imagen existente |

NanoBanana analizada y NO agregada: todos los Gemini/NB son `paid_only` (grants no los cubren). NB2.1 ~0.034 Pollen/img (~29 imgs con USD 1), Pro ~0.134 (~7 imgs). Gate: comprar Paid Pollen o x402 antes de agregar tool `generar_nanobanana`.

## Memoria y sessions

Memoria activada (`storage: n8n`): cada conversación es una session y recuerda el hilo (última imagen, supuestos). Cross-session knowledge (memoria episódica/observacional entre sesiones) apagado: cuesta tokens y hoy no hace falta; se enciende si pedís continuidad entre días.

## Knowledge y vector stores

Vacío. Sirve para darle documentos propios (brief del concurso, paletas, normativa): se suben a un vector store (Pinecone/Qdrant/Supabase/Postgres) y el agente los consulta con `search_<nombre>`. Requiere credential + índice; se agrega cuando haya corpus.

## Budget, sesiones y loops

Guardrail activo: USD 1 mensual, alerta al 50%. No hay cap por sesión: el freno a loops es `maxIterations: 10` por corrida + máximo 3 edits por la regla del prompt. Cada imagen gasta centavos de Pollen, no USD del budget (el budget mide el LLM).

## Subagentes y custom model routing

Sin subagentes configurados. Cuando exista Hermes, vive como subagente (`useWhen: ...`) o este agente pasa a ser su tool. Routing por dificultad apagado; el cerebro único GLM cubre todo el rango actual.

## MCP

`mcpServers` vacío a propósito: yo opero al agente directo por MCP (ya lo testeo con `call_agent`). Se llena si el agente debe exponer herramientas a otros sistemas.

## Telegram

Integración pendiente de tu ID: `accessMode: private` + `allowedUsers: [tu_id]`. Al publicar, el canal conecta en vivo — confirmar antes.

## Skills y referencias

- `prompting-arquitectura` (genérica): úsala siempre antes de armar un prompt, salvo pedido del concurso.
- `prompt-cascara-gaudi` (concurso): SOLO si el pedido menciona Gaudí Nexus, Sagrada Familia o la cáscara.
- Referencias de skill: archivos adjuntos a la skill (hoy ninguna; servirían para brief PDF o paleta). El `when to use` vive en la descripción de cada skill.

## Build log

- ProjectId correcto: `pWOSkiVhnAWt5tSi` (un tipeo sin la `t` rompía el link con credenciales).
- Modelo `openrouter/z-ai/glm-5.3-flash` (el alias `~z-ai/glm-flash-latest` con tilde lo rechaza el runtime).
- Tools con dims numéricos fijos (strings dan 400), credencial Header enlazada, validados sin warnings.
- Tests `call_agent` 2026-11-03: exploración Gaudí (flux, URL válida) y cabaña genérica en bosque (genérico confirmado). Segunda imagen guardada en `activos/proyectos/concurso-gaudi-nexus/pollinations-tests/agente-firstclass-2026-11-03.jpg`.
- Tools migrados de node a workflow (`IMG Generar` publicado, `voMAYlv6d280QjSW`): el runtime rechaza `$fromAi` en la URL; inputs `fixed` para modelo/dims/seed, prompt queda AI.
- Grants agotados 2026-11-03 tras ~20 imágenes del día: POST y GET con key devuelven 402, anónimo 401 por throttling. Test casa BA (hormigón visto + madera + hierro, entre medianeras) quedó con prompt armado por el agente, en espera de recarga (grant diario o x402 desde $0.01). El agente diagnosticó solo el problema de billing y propuso los pasos.

## Fase Hermes

El plan Hermes sigue por delinear; este agente deja el contrato para que Hermes conecte directo después:

```json
{"tool": "pollinations.generate", "input": {"prompt": "texto", "model": "flux.1-schnell", "width": 1280, "height": 720, "seed": 7}}
{"tool": "pollinations.edit", "input": {"image": "binary", "instruction": "conserva torres, agrega cáscara + vidrio", "model": "flux.1-kontext-pro"}}
{"tool": "pollinations.async_poll", "input": {"job_id": "id", "hasta": "succeeded"}}
```

Preguntas abiertas: dónde vive Hermes (mismo bot u otro), memoria compartida, quién elige modelo cuando difieren, y si Hermes reutiliza este draft o sus propios tools.

## Gates

- G0: draft validado + `call_agent` OK (hecho).
- G1: tu ID de Telegram registrado como `allowedUsers`.
- G2: publicado + canal Telegram conectado (con tu `s`), primera imagen real por chat.
- G3: plan Hermes delineado y contrato adoptado.

## Costos

LLM GLM por turno: centavos de dólar (0.0399/1M in). Imágenes: flux 0.002, z-image 0.004, klein 0.005, 1.1-pro y kontext 0.03, sana 0.0001, mai-flash 0.00001425 + tokens (todo Pollen de grants). NanoBanana: solo con Paid Pollen.

## Riesgos

- Integración Telegram conecta en vivo tras publicar: confirmar antes.
- Sin tu ID no hay canal privado: el agente queda solo testeable por Preview.
- Grants agotados: error 402; fallback a modelos 0 Pollen o recarga x402.
