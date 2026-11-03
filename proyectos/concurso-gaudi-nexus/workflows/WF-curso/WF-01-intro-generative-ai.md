---
tipo: guia
proyecto: concurso-gaudi-nexus
modulo: 1
slug: intro-generative-ai
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, wf-curso, wf-01, curso-ai-gaudi, sdxl, txt2img, baseline]
idioma: es
---

# WF-01 — Intro Generative AI + baseline txt2img 1024²

> Unifica [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/flujo-01-intro-generative-ai\|flujo-01]] + [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/WF-01_sdxl\|WF-01_sdxl]]. Detalle verbatim en las fichas origen.

## 1. Ver en Miro + video

| Fuente | Link |
|--------|------|
| Miro frame módulo 1 | pendiente link Sol |
| Video módulo 1 (1 h 30 min 49 s) | pendiente link Sol |
| Transcripción ES/EN | [[raw/yt/transcripts/2026-10-21_mux-intro-generative-ai\|transcripción]] |

## 2. Flujo del curso (resumen)

Teoría mínima (tokens, seed, dataset, difusión, VAE) + lectura nodo a nodo del workflow base + Comfy Cloud + Comfy Expert + Prompt Coach. Profesor: Thomas Nelissen.

| Clave | Valor del video |
|-------|-----------------|
| Grafo base | Checkpoint → Prompt ± → EmptyLatentImage (ej. 512², prueba 1024 ancho) → KSampler (motor) → SaveImage |
| Seed | fixed = misma imagen · randomize = nueva por corrida |
| Steps / CFG (SD1.5) | 20 plantilla · 4 roto / 10 ok / 20 = 10 · CFG 8 (1 hace lo que quiere, 20 rompe) |
| Batch | batch count 1 (no 15) |
| Prompt | keyword (viejo) · lenguaje natural (actual) · JSON (solo FLUX.2, lo escribe IA). Lo importante va primero |
| Comfy Expert | proyecto LLM con 2 URLs (docs Comfy Cloud + ComfyWiki) + captura |
| Prompt Coach | proyecto LLM con instrucciones del tablero, se arranca con `start` |
| LoRA | ~100 MB, 20-30 imgs, conoce una cosa, va con su modelo base |
| Modelos curso | SD1.5 · SDXL · FLUX.1 · FLUX.2 klein 9B (principal). Cloud 96 GB VRAM ~5 s vs local ~2 min |

Prompt de prueba: `beautiful scenery nature glass bottle landscape, purple galaxy bottle`.
Prompt plantilla edición: `to add a beanie on her head`.

Vacíos: sampler/scheduler, seeds concretas, CFG/steps FLUX, nombres `.safetensors`, trigger LoRA → **no dicho en el video**.

## 3. WF SDXL vista

JSON: `workflow_WF-01_sdxl.json` (misma carpeta WF-curso/, original en `workflows/sdxl-vista/`) · 7 nodos · 1024×1024 · seed 7 · 30 steps · cfg 4 · `dpmpp_2m`/`karras` · prefijo `gx-WF01`. Sin validar contra servidor (R4 pendiente).

| # | Nodo | Función |
|---|------|---------|
| 1 | `CheckpointLoaderSimple` | Juggernaut-XL_v9 (MODEL/CLIP/VAE) |
| 2 | `CLIPTextEncode` | + `architectural concept render, catenary arches pavilion inspired by Gaudi, stone and brick, fractal branching columns, park background, soft daylight, photorealistic, 8k uhd, masterpiece` |
| 3 | `CLIPTextEncode` | − `blurry, low quality, distorted, watermark, text, cartoon, illustration, oversaturated` |
| 4 | `EmptyLatentImage` | 1024² batch 1 |
| 5 | `KSampler` | 30 steps, cfg 4, denoise 1.0, seed 7 |
| 6 | `VAEDecode` | latente → píxeles |
| 7 | `SaveImage` | `gx-WF01` |

Corridas R1-R3: Juggernaut v9 control · RealVisXL v5.0 comparación · Lightning descartado 2026-11-02. Variante prompt v2 plaza + mosaico Escher pendiente R4.

## 4. Cómo lo adaptamos

Local con `architecturerealmix_v11` (SD1.5) y Juggernaut v9 (SDXL) ya en disco, una variable por corrida, seed registrada, validación `/object_info` antes de encolar.

## 5. Checks jurado

Reproducibilidad (misma seed = misma imagen), prompt en metadatos PNG, grafo + `03-nodos` + `02-WF-log` por corrida. Checklist definitivo cierra con transcripción módulo 6.
