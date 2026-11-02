---
tipo: playbook
codigo: pbk-comfy-agent
fecha_creacion: 2026-10-30
ultima_actualizacion: 2026-10-30
tags: [pbook, tim, comfyui, prompts, flujos, recetario, bitacora, fotoarquitectura]
idioma: es
---

# pbk-comfy-agent — Playbook del director creativo @tim

> Qué hace Tim, cómo está configurado, cómo invocarlo y el recetario por tipología. Definición viva en `.opencode/agents/tim.md`; este pbook es el índice razonado + manual de uso.

- [[Qué hace]])
- [[Dónde vive el código]])
- [[Cómo está conformado (código)]])
- [[Manual de invocación]])
- [[Checklist antes del s]])
- [[Recetario por tipología]])
- [[Constantes de fotografía]])
- [[Ciclo con la bitácora de corridas]])
- [[Delegación]])
- [[Conceptos relacionados]])
- [[Referencias]])

## Qué hace

**@tim** es el director creativo de ComfyUI del estudio. Convierte una idea, un croquis de Rhino o una foto de referencia en **dos artefactos que viajan juntos**: el prompt en el dialecto exacto del modelo y el flujo (cadena de nodos con parámetros, y `workflow_*.json` en API format si se pide). Un prompt sin flujo es una intención; un flujo sin prompt es una máquina vacía.

Modelos que maneja: SD 1.5 · SDXL · FLUX.1 · FLUX.2 klein 9B · LTX-2.3 · Kling 3.0 · Seedance 2.0. La decisión relevante es una: **¿imagen fija, edición (inpaint) o video?** — y de ahí el dialecto (keywords+negativo / prosa / JSON) y la plataforma (local / RunPod / Cloud).

## Dónde vive el código

| Capa | Ruta | Qué hay |
|---|---|---|
| **Agente** | `.opencode/agents/tim.md` | Frontmatter (permisos por ruta + MCP) + Frontera + Delegación + Misión 7 pasos + Tabla de decisión + Plancha local + Léxico + Reglas duras + Checklist + Invocación |
| **Skill** | `.opencode/skills/comfy-prompting/SKILL.md` | Router de dialectos + 6 references (sd15-sdxl, flux1, flux2, video, léxico-cine-foto, workflows-por-modelo) |
| **Recetario + constantes** | Este pbook, [[#Recetario por tipología]] y [[#Constantes de fotografía]] | Fórmulas por tipología para copiar y adaptar |
| **Reglas de WF** | [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] | R1–R4, nomenclatura `n_XX-{A–G}-{NN}.png`, estructura de carpetas |
| **Bitácora** | [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/04-bitacora-corridas|04-bitacora-corridas]] | Índice central de corridas repetibles; log completo en cada WF |
| **Prompts del curso (fuente)** | [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/00-README|prompt-coach/00-README]] | Los 3 prompts del curso AI x Gaudi archivados verbatim |
| **Escritura de salida** | `.opencode/`, `proyectos/<MVP>/…`, `raw/prompts/` | `wiki/` queda para `@vaultworm-arq` |

## Cómo está conformado (código)

Frontmatter: `mode: subagent` + `temperature: 0.4` (balance: respeta receta, propone variantes) + permisos:

- `edit: allow` global con **deny por ruta**: `wiki/**`, `activos/**`, `.git/**` — límite en la config, no solo en el prompt.
- `bash: deny` — propone el comando y SOL lo corre. Todo lo demás (`read/grep/glob/list/task/skill/websearch/webfetch`) allow.
- **MCP**: `comfyui_*` + `rhino_*` allow; `leantime_*`, `n8n_*`, `fathom_*`, `autocad_*`, `autodesk_*` deny.
- Ejecución: con `s` explícito corre `comfyui_execute_workflow` y lee `comfyui_get_history` para registrar la corrida; **nada se encola sin `s`**.

Los permisos cargan al iniciar opencode: cualquier cambio de frontmatter requiere reiniciar.

## Manual de invocación

| Lo que pedís | Lo que recibís |
|---|---|
| `@tim prompt pabellón de hormigón en Barcelona` | Prompt + flujo del modelo que Tim elija y declare |
| `@tim flujo sdxl fachada nocturna` | Cadena de nodos y parámetros, sin prompt de proyecto |
| `@tim flux2 rhino` | Prompt FLUX.2 con vistas de Rhino + foto de material como referencias |
| `@tim video recorrido fachada` | Prompt de movimiento (LTX-2.3 / Seedance según duración y plataforma) |
| `@tim json` | Variante JSON estructurada (solo FLUX.2) |

En la respuesta esperás siempre: **modelo elegido y declarado**, el prompt en su dialecto, el flujo con nombre exacto de `class_type` + valores + justificación de una línea, el checklist pre-corrida y el siguiente paso en una línea. Si el modelo ideal corre en otra plataforma (FLUX.2, video), el prompt sale igual con el tag `requiere RunPod/Cloud`: no hay encargo de corrida local.

## Checklist antes del s

Antes de que des el `s`, Tim muestra exactamente cuatro líneas:

1. **Archivos en disco** — modelo, VAE y LoRA confirmados con `comfyui_list_local_models`.
2. **Resolución nativa** — 512² SD 1.5 · 1024² SDXL · 1,0 MP FLUX.2.
3. **Dialecto correcto** — keywords+negativo / prosa / JSON, el del modelo elegido.
4. **Una sola variable** respecto de la última corrida: steps, o cfg, o modelo, o strength.

Cualquier línea fallida cancela el pedido de `s`: corrige primero o declara lo que falta.

## Recetario por tipología

Fórmulas base: copiás, cambiás el sujeto/material/luz y corregís. "Léxico" refiere a `.opencode/skills/comfy-prompting/references/lexico-cine-foto.md`. El vocabulario es el mismo; lo que cambia es el empaquetado por dialecto.

### 1 · Fachada / exterior (entrega)

- **Modelo**: SDXL `Juggernaut-XL_v9` (local justo) · FLUX.1/2 en RunPod.
- **Estructura keyword**: sujeto (con material tectónico) → detalles (3m structural bays, reveal) → estilo → encuadre (`three-quarter view, eye level`) → lente (`35mm tilt-shift`) → luz (`golden hour / overcast`) → color → quality tags.
- **Negativos**: warped perspective, melting geometry, bent windows, blurry, low quality.
- **Concepto rápido**: SD 1.5 `architecturerealmix` a 512², cfg 7–8, 20 variantes del mismo prompt con seeds.

### 2 · Interior

- **Modelo**: SDXL · FLUX.1 en RunPod.
- **Encuadre**: `WS/FS, one-point perspective`; lente `16–24mm` (ojo con distorsión de rectas — ControlNet Canny si importa).
- **Luz**: `soft overcast daylight from north windows` o `warm tungsten interior, CineStill 800T register` para entrega de noche.
- **Materialidad**: piso, pared, carpintería nombradas por material real; sin adjetivos genéricos.

### 3 · Masterplan / vista aérea

- **Modelo**: SD 1.5 concepto · SDXL entrega.
- **Encuadre**: `bird's-eye / high angle`; lente `24–35mm`.
- **Luz**: `overcast, flat even light` (sin sombras que distorsionen la escala); paleta `6 hex` derivada del suelo y el césped.
- **Para corte/axonométrica de producción**: mejor FLUX.2 JSON desde Rhino (siguiente).

### 4 · Detalle / materialidad

- **Modelo**: SDXL · FLUX.2 (referencia de material a 0,5 MP, lanczos).
- **Encuadre**: `macro / ECU`; lente `100mm macro`; ángulo `low` o frontal.
- **Luz**: `raking hard light` para textura (board-formed concrete, bush-hammered, corten), `bounce` para bronce anodizado.
- **El high de la casa**: 40–70 palabras de prosa FLUX.2 = la fórmula de las constantes (abajo).

### 5 · Contexto urbano

- **Modelo**: SDXL · FLUX.1 en RunPod.
- **Encuadre**: `35mm, street context, neighbors included, pedestrians at scale`.
- **Regla**: el edificio entra con su lógica urbana (retiro, vereda, alineación); Baan para el registro de vida cotidiana.

### 6 · Video / recorrido

- **Modelo**: LTX-2.3 (movimiento claro y acotado) · Kling 3.0 (multi-shot con audio, timestamps) · Seedance 2.0 (desglose EN+ZH). Todo `requiere RunPod/Cloud`.
- **Seedance 2.0 tiene skill propia**: `.opencode/skills/seedance-director/` (del curso AI x Gaudi) — JSON array EN+ZH, arquetipos action/general/dialogue, hard cap 15 s, double contrast por corte. `@tim video seedance <escena>` o `@tim seedance <escena>`.
- **Orden**: escena/sujeto → acción/movimiento → cámara (`dolly in / tracking / orbit`) → luz/estilo → pacing.
- **Registro del estudio**: recorrido lento a 1,4 m de altura (ojo del visitante), one take, 3–5 s por beat, `MATCH CAMERA` del esqueleto JSON si hay stills previos.

## Constantes de fotografía

Heredadas del FLUX.2 Architectural Prompt Refiner del curso ([[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/03-flux2-prompt-refiner|fuente]]) — obligatorias en la variante JSON de FLUX.2:

| Constante | Valor | Por qué |
|---|---|---|
| Fotógrafo principal | **Iwan Baan** + uno contextual (Hélène Binet · Julien Lanoo · Rory Gardiner) | registro de arquitectura en uso |
| Cuerpo | **Phase One IQ4** | medio formato, detalle y rango dinámico |
| Paleta | **exactamente 6 hex** — 3–4 de la materialidad, 1–2 de luz/cielo | el color queda firmado, no improvisado |
| Film stock | uno de los siete (Portra 400 · Ektar 100 · Velvia 50 · Pro 400H · Tri-X 400 · HP5 · CineStill 800T) | el grano ata el mood a una época |
| Referente de autor | oficina real, **distinta en cada option card**, con proyecto built citado | la lógica material, sin name-drop |

Quality guards que Tim aplica siempre: geometria declarada o implied (sin wings/floors inventados), cada adjetivo comprobable ("board-formed concrete tower with 3m structural bays" sí; "sleek modern building" no), y lenguaje de lo que **ve la cámara** (luz, sombra, superficie, depth), no de intención.

Para el JSON completo (10 claves, `STRICT CAMERA LOCK`, `MATCH CAMERA OF IMAGE 1 EXACTLY`): [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-instruction-md|INSTRUCTION.md Rhino-to-Image]] y [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-esqueleto-json|esqueleto JSON]].

## Ciclo con la bitácora de corridas

```
receta (este pbook) → @tim genera prompt + flujo → checklist → s
  → corrida comfyui_execute_workflow → log completo en 02-WF-log-WF<nombre>.md
  → si es repetible: fila en [[proyectos/MVP_04-comfyui-arquitectura/prompt-coach/04-bitacora-corridas|04-bitacora-corridas]] (más nuevo arriba)
  → la próxima receta se ajusta con lo que funcionó (seed, cfg, stock, luz)
```

La bitácora es la memoria del recetario: qué receta dio qué foto, con qué parámetros, y la primera variable a cambiar si se repite. Tim agrega la fila; vos decidís si la corrida vale.

## Delegación

Tim delega para **traer**, no para decidir:

| Situación | Delega a | Qué le pide |
|---|---|---|
| Falta referencia visual, video, ficha de modelo o guía oficial | `@sherlock` | búsqueda acotada con lo que necesita el prompt (encuadre, material, luz, plataforma) |
| No sabe si el WF ya existe o dónde quedó un parámetro | `explore` | rastreo en `proyectos/` y `.opencode/` por nombre de nodo o WF |
| Falta un dato del estudio (norma, cliente, tipología) | no delega | lo pide a SOL en una línea |

El resultado vuelve citado con su ruta o URL; la decisión de modelo, prompt y flujo sigue siendo de Tim.

## Conceptos relacionados

- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — flujos, parámetros y base local RX 570 (canónico UNICO de ComfyUI)
- [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]] — registro de agentes del vault
- [[wiki/glosario/software/comfyui|ComfyUI]] — ficha de glosario
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] — R1–R4 y nomenclatura de salidas

## Referencias

- `.opencode/agents/tim.md` — definición viva del agente
- `.opencode/skills/comfy-prompting/SKILL.md` — router de dialectos y references por modelo
- FLUX.2 prompting guide (BFL, oficial) — https://docs.bfl.ai/guides/prompting_guide_flux2 (verificado 2026-10-30)
- FLUX.2 overview (BFL, oficial) — https://docs.bfl.ai/flux_2/flux2_overview (verificado 2026-10-30)
- Stable Diffusion prompt guide (SD 1.5/SDXL) — https://stable-diffusion-art.com/prompt-guide/ (verificado 2026-10-30)
- Opencode docs — agentes y permisos: https://opencode.ai/docs/agents/ (verificado 2026-09-08 — 200)
