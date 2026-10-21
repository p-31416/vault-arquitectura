---
tipo: proyecto
mvp: 04
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [mvp_04, comfyui, agente, mcp, hermes, openclaw, gradio, dashboard, metodo, ia]
---

# De "coach de prompting" a asistente que ejecuta — la evolución del estudio

> Por qué la diferencia entre el curso y lo que podemos hacer no está en el prompt: está en **quién ejecuta**. Hoy el curso propone un prompt coach (copiar y pegar un JSON en el canvas); la evolución es que el JSON sea un **contrato** y un agente lo ejecute solo, con lo que el resultado caiga **con su metadata en un índice vivo**. Y que todo eso lleve nuestra impronta, como un LoRA.

- [[#El diagnóstico]]
- [[#Las 5 capas]]
- [[#El paralelo con el tablero del curso]]
- [[#La impronta: tres artefactos, como un LoRA]]
- [[#Hermes, OpenClaw o quedarnos donde estamos]]
- [[#Hoja de ruta]]
- [[#Riesgos]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## El diagnóstico

| | Hoy (el curso) | Evolución (nosotros) |
|---|---|---|
| Quién redacta el prompt | El prompt coach, en el chat | El agente, con nuestro schema de prompts |
| Quién ejecuta el render | La persona, en el canvas | El agente, vía MCP contra el ComfyUI local |
| Cómo se documenta | Carpeta de PNG | **Índice con metadata leída de la imagen** |
| Cómo se pide | Copiar y pegar el JSON | Un mensaje: "4 variantes, LoRA al 50 %, misma seed" |
| Qué estilo | El del curso (o ninguno) | **El nuestro**: schema + LoRA propio + índice |

La diferencia sustantiva no es "más IA": es que **el trabajo del estudio deja de depender de que alguien recuerde el procedimiento**. Hoy el método está en la cabeza de la persona y en los `.md`; con un agente, el método queda **escrito, ejecutable y versionado** — que es exactamente lo que le vamos a pedir a un cliente cuando cobramos la arquitectura.

## Las 5 capas

```
┌─ Capa 4 · EL AGENTE ────────────────────────────────────────────────┐
│  Hermes u OpenClaw: chat (Telegram/WhatsApp), skills propias,       │
│  memoria, cron. Conecta el MCP de ComfyUI local.                    │
│  "renderizá 4 variantes con el LoRA al 50 % y guardá el comparativo"│
└───────────────────────────────┬──────────────────────────────────────┘
                                │ MCP (tools: encolar, cola, output, metadata)
┌─ Capa 3 · LA INTERFAZ ──────────▼──────────────────────────────────┐
│  Gradio local (o comfy-headless / comfy-webui): campos simples,       │
│  cola visible, historial con metadata. Un mismo botón para persona   │
│  y agente (API + MCP + gradio_client).                              │
└───────────────────────────────┬──────────────────────────────────────┘
                                │ workflow API (JSON)
┌─ Capa 2 · EL ÍNDICE ────────────▼──────────────────────────────────┐
│  El recolector lee la metadata de cada PNG y regenera el índice y el │
│  dashboard. Cada render cae con modelo, LoRA, seed, sampler, steps, │
│  cfg, resolución y prompt. Sin base de datos: la trazabilidad está   │
│  DENTRO de la imagen.                                              │
└───────────────────────────────┬──────────────────────────────────────┘
                                │ prompt
┌─ Capa 1 · EL CONTRATO ──────────▼──────────────────────────────────┐
│  El prompt como JSON con schema propio (el del curso adaptado):      │
│  scene, subjects, style, color_palette, lighting, mood, background,  │
│  composition, camera + campos propios (material, entrega, licencia). │
└───────────────────────────────┬──────────────────────────────────────┘
                                │ referencias (volumetría + material)
┌─ Capa 0 · LA EJECUCIÓN ─────────▼──────────────────────────────────┐
│  ComfyUI local (P:\00-repos\ComfyUI, :8188) + MCP. Sin GPU no hay   │
│  agente: la ejecución tiene que ser local o en un pod propio.       │
└──────────────────────────────────────────────────────────────────────┘
```

### Qué hay y qué falta en cada capa

| Capa | Estado | Falta |
|------|--------|-------|
| 0 · Ejecución | ✅ ComfyUI local + MCP funcionando (es lo que vengo usando en esta sesión: encolar, consultar la cola, leer el output, extraer la metadata de un PNG) | El pod para 9B (producción) |
| 1 · Contrato | ✅ el schema JSON del curso está extraído al vault (3 prompts) | Adaptarlo a **nuestro** schema (material, licencia, criterio de entrega) y validarlo |
| 2 · Índice | ✅ `scripts/indice-renders-comfy.py` → 80 renders, 100% con metadata, `INDICE-RENDERS.md/.json` | Que se regenere solo (watcher o cron) y que alimente el dashboard |
| 3 · Interfaz | ⬜ | Gradio local mínimo (o `comfy-headless` / `comfy-webui` como base) |
| 4 · Agente | ⬜ | Hermes u OpenClaw + skills propias + MCP de ComfyUI local |

## El paralelo con el tablero del curso

El curso resolvió el problema de "dónde está cada cosa" con un **tablero de Miro**: un índice compartido de recursos, workflows y prompts, con la contraseña `Gaudi2026`. Es un buen patrón, con dos límites:

1. **Es manual**: si el curso agrega un workflow, alguien lo agrega al board.
2. **No tiene metadata**: no dice qué seed, qué modelo, qué LoRA ni qué prompt produjo cada imagen.

Nuestro índice es **el mismo tablero, con metadata y que se regenera solo**:

| | Tablero del curso | Nuestro índice |
|---|---|---|
| Índice compartido | ✅ | ✅ |
| Se actualiza solo | ❌ | ✅ (el recolector lee las imágenes) |
| Metadata de cada pieza | ❌ | ✅ (modelo, LoRA+strength, seed, sampler, steps, cfg, resolución, prompt) |
| Reejecutable | ❌ | ✅ (el prompt y el workflow se leen de la imagen) |
| Vive en el vault | ❌ | ✅ |

La diferencia de fondo: el tablero **muestra** recursos; nuestro índice **reconstruye** decisiones. Por eso un render archivable vale más que una carpeta de PNG: la imagen lleva su propia historia y esa historia se puede volver a ejecutar.

## La impronta: tres artefactos, como un LoRA

Un LoRA no es "un filtro de estilo": es **un artefacto entrenado, versionado y con licencia**, que hereda material y gramática. La impronta del estudio tiene la misma forma, en tres capas:

| Artefacto | Qué es | Dónde vive | Estado |
|---|---|---|---|
| **El schema de prompts** | El contrato JSON: qué se pregunta (material, tipología, ubicación, lente, luz) y con qué palabras | `proyectos/.../WF-rhino-to-image/prompt-*.md` → a consolidar como `prompt.schema.json` | extracting el del curso |
| **El LoRA propio** | Entrenado con fotos y croquis del estudio sobre klein 4B (Apache 2.0) → estilo propio y comercializable | `models/loras/` en el pod | pendiente (P3) |
| **El índice + dashboard** | La trazabilidad: cada render con su metadata, su WF y su log | `INDICE-RENDERS.md` + `dashboard-comfy.html` | ✅ collector funcionando |

**El argumento para el cliente** es el mismo que el del curso, pero con la tinta del estudio: no "esto lo hizo una IA", sino **"esto es el método de la casa, y acá está la cadena que lo produjo"** (imagen → workflow → seed → dataset). El dashboard es la prueba, y por eso tiene que regenerarse solo.

## Hermes, OpenClaw o quedarnos donde estamos

Los dos son agentes ejecutores open source con cliente MCP nativo. La diferencia está en el shell y en el Learning loop.

| | **Hermes** (Nous Research, MIT) | **OpenClaw** (Fundación, MIT) | **opencode + MCP** (lo que ya hay) |
|---|---|---|---|
| Forma | CLI + TUI + app de escritorio + web + gateway | Gateway local + apps (Windows/macOS/Linux) | opencode en la terminal + MCP |
| MCP | Cliente nativo: `mcp_servers` en `config.yaml`, descubrimiento al arranque, tools `mcp_<servidor>_<tool>` | Cliente nativo: `mcp.servers` (stdio / streamable-http / SSE) + filtros por tool + `openclaw mcp doctor --probe` + `openclaw mcp serve` | Cliente MCP (este server) |
| Canales | Telegram, Discord, WhatsApp, Signal, Email, Home Assistant, CLI | 29 canales (Telegram, WhatsApp, Discord, iMessage, Signal, Teams…) | Telegram vía n8n, no el agente |
| Skills | **Se auto-crean y se auto-mejoran**; Skills Hub | Skills + Skill Workshop; puede escribir las suyas | AGENTS.md + agentes `.opencode/agents/` |
| Memoria | Persistente, aprende del uso, busca conversaciones previas | Persistente, en tu hardware | La memoria es el vault |
| Automatización | Cron en lenguaje natural + webhooks + delegación | Cron + eventos | n8n en el VPS |
| Aislamiento | 7 backends (local, Docker, SSH, Modal, Daytona…) | Sandbox por código | local |
| Migración | `hermes import-agent claude-code` (trae MCP + skills) | config declarativa | — |
| Veredicto para el estudio | **el que más se parece a lo que ya somos** (n8n + Telegram + vault + agentes) | más simple y con más canales, pero Node | **ya resuelve el 90% técnico** |

**Lo importante**: los dos hacen **lo mismo que ya hacemos hoy con el MCP** — la diferencia es el *shell* (¿desde dónde se habla?) y la *memoria*. La capacidad no está en el agente: está en el MCP + el contrato + el índice. Por eso el orden correcto es **índice → interfaz → agente**, y no al revés.

### Por qué el agente tiene que ser local (y no el de Comfy Cloud)

El propio Comfy documenta dos conexiones MCP: **Cloud** (pide suscripción activa, corre en GPUs de Comfy) y **Local** (conduce tu ComfyUI, el agente ve *tus* modelos, LoRAs y nodos, y corre en *tu* GPU). La local es la que sirve: el Agente de Comfy Cloud guarda la conversación en la nube, no alcanza tus archivos y cobra por GPU. Un asistente del estudio que no puede tocar el disco del estudio no es un asistente: es un chat.

## Hoja de ruta

| Etapa | Qué | Esfuerzo | Cierre | Cuándo |
|-------|-----|----------|--------|--------|
| **A · El índice** (arranca ya) | El recolector lee la metadata de los PNG y regenera `INDICE-RENDERS` + el dashboard | Hecho ✅ (falta el watcher y que alimente el dashboard) | Los renders entran solos al índice con su metadata | esta semana |
| **B · El contrato** | Consolidar nuestro schema de prompts (el del curso + material, licencia, entrega) y un validador | 1 mañana | Un JSON de prompt validado que se puede pedir por Telegram | antes del 7/11 |
| **C · La interfaz** | Gradio local: campos (volumetría, foto de material, prompt JSON, strength, seed) + botón "renderizar" + historial con metadata | 1-2 días | Emilia pide una batería de 4 renders **sin abrir el canvas ni copiar-pegar** | 10-14/11 |
| **D · El agente** | Hermes (u OpenClaw) + MCP de ComfyUI local + 3 skills propias ("render con LoRA propio", "comparar strengths", "armar comparativo para la lámina") + cron | 2-3 días | Desde Telegram: "4 variantes, LoRA 50 %, misma seed" → vuelve con el comparativo en el vault | después del 16/12 |
| **E · El loop 3D** | El vault ya tiene el MCP de Rhino (`scripts/rhino-mcp-server-rhino.py`): el agente exporta la captura de la volumetría, renderiza y devuelve el resultado al modelo | 3-5 días | Un ciclo Rhino → render → Rhino sin intervención manual | diciembre |

**Secuencia y por qué:** A y B no dependen de nada externo y ya tienen el 80% del valor. C es lo que le cambia el día a día a Emilia. D y E son el salto de "asistente" y llegan **después** de la entrega, cuandoSepamos si el flujo aguanta en la práctica.

## Riesgos

| Riesgo | Mitigación |
|--------|------------|
| **El agente ejecuta solo y se equivoca** (cobra GPU, llena el disco, genera basura) | Todo pasa por el ComfyUI local y el índice: cada corrida queda registrada y se puede auditar. El Agent corre con aprobación para acciones destructivas |
| **Costo** | El pod se prende para la tarea y se apaga; el índice muestra el costo por render |
| **Privacidad** | El material del concurso no pasa por el Agent de Comfy Cloud ni por nodos Partner Nodes. En el pod: disco de contenedor, y terminar el pod al terminar |
| **Dependencia de un framework** | La capa 1-2 (contrato + índice) es independiente del agente: si mañana no nos gusta Hermes, el índice y el schema siguen sirviendo |
| **Mantenimiento** | El schema JSON y las skills son texto en el vault: se versionan con el resto y los lee cualquiera |

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|comfyui]] · [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]]
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]] · [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]]
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — playbook operativo
- [[wiki/glosario/conceptos/vault-visual|vault-visual]] — el pipeline de render del estudio
- [[wiki/glosario/conceptos/ia-lab-partnership|ia-lab-partnership]] — el encuadre de la IA como laboratorio del oficio
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image|WF-rhino-to-image]] — el flujo del concurso
- [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|research 2026-10-20]] — el informe base

## Referencias

- [OpenClaw — repo (MIT, gateway local, canales, skills)](https://github.com/openclaw/openclaw) (verificado 2026-10-21 — 200)
- [OpenClaw — Conectar servidores MCP (`mcp.servers`, `openclaw mcp doctor --probe`)](https://docs.openclaw.ai/tools/mcp) (verificado 2026-10-21 — 200)
- [Hermes Agent — Nous Research (MIT, gateway multi-plataforma, memoria, skills, cron)](https://github.com/NousResearch/hermes-agent) (verificado 2026-10-21 — 200)
- [Hermes Agent — MCP nativo (`mcp_servers`, prefijo `mcp_<servidor>_<tool>`)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) (verificado 2026-10-21 — 200)
- [ComfyUI — MCP: conexión local vs Cloud (documentación oficial)](https://docs.comfy.org/llms-full.txt) (verificado 2026-10-21 — 200)
- [Comfy — Comfy Agent: datos y privacidad (local y cloud)](https://docs.comfy.org/agent-tools/in-app-agent-data-privacy) (verificado 2026-10-21 — 200)
- [comfy-webui — Gradio + Workflow-as-a-Service con API semántica y MCP (MIT)](https://github.com/RioShiina47/comfy-webui) (verificado 2026-10-21 — 200)
- [comfy-headless — Gradio sobre las 7 rutas de ComfyUI, con Queue & History](https://github.com/mcp-tool-shop-org/comfy-headless) (verificado 2026-10-21 — 200)
- [ComfyUI_to_webui — frontend Gradio generado desde un workflow](https://github.com/kungful/ComfyUI_to_webui) (verificado 2026-10-21 — 200)
- [HF Blog — Gradio `gradio.Server`: frontend propio con la cola y el API de Gradio (2026-04-01)](https://huggingface.co/blog/introducing-gradio-server) (verificado 2026-10-21 — 200)
- [HF Blog — De un workflow de ComfyUI a una app Gradio (comfy-to-gradio)](https://github.com/huggingface/blog/blob/main/run-comfyui-workflows-on-spaces.md) (verificado 2026-10-21 — 200)
