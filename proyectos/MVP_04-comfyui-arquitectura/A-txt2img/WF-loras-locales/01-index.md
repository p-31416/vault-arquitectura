---
tipo: index
workflow: WF-loras-locales
nivel: n_01-txt2img
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [index, txt2img, lora, calibracion, rx570]
estado: activo
---

# 01-index — WF-loras-locales

**Workflow SD 1.5:** `workflow_loras-locales.json`
**Workflow SDXL:** `workflow_loras-locales_sdxl.json`
**Script de corrida:** `scripts/calibrar-loras-comfyui.py` (notas en `scripts/calibrar-loras-comfyui_notas.md`)
**Catálogo completo:** [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]]

---

## Configuración por familia de base

| Parámetro | SD 1.5 | SDXL |
|-----------|---------|------|
| **Checkpoint** | `architecturerealmix_v11.safetensors` | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` |
| **Resolución** | 768×512 | 1216×832 |
| **Sampler** | `euler_ancestral` | `dpmpp_2m` |
| **Scheduler** | `karras` | `karras` |
| **Steps** | 30 | 30 |
| **CFG** | 7 | 4 |
| **Batch** | 1 | 1 |
| **Denoise** | 1.0 | 1.0 |
| **Seed** | 42 (fija en todas las corridas) | 42 |
| **Flags** | `--lowvram --cpu-vae --force-fp16` | ídem |

### Prompts base

**SD 1.5 (positive):** `architecturerealmix style, modern architecture, concrete and glass facade, minimalist design, photorealistic, architectural photography, natural lighting, 8K`
**SD 1.5 (negative):** `low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, deformed, watermark, text, signature, illustration, painting`

**SDXL (positive):** `photorealistic, raw photo, 8k uhd, architectural photography, modern building, concrete and glass facade, minimalist design, natural sunlight, sharp focus, highly detailed, masterpiece, canon r5, 24mm tilt-shift lens`
**SDXL (negative):** `blurry, low quality, distorted, ugly, bad architecture, cartoon, sketch, deformed, watermark, text, signature, grain, noise, overexposed, illustration, painting`

> El prompt final antepone el **trigger** del LoRA: `{trigger}, {prompt_base}`.

---

## Plan de corridas

16 LoRAs × 2 strengths (0,6 y 0,8) = **32 renders**. Numeración global: `G-01`…`G-18` son SD 1.5, `G-19`…`G-32` son SDXL.

### SD 1.5 (ArchitectureRealmix) — G-01 a G-18

| # | LoRA | Trigger | Strength | Estado |
|---|------|---------|----------|--------|
| G-01 / G-02 | `JJ_Archvizcg_v2.safetensors` | `archviz` | 0,6 / 0,8 | ⬜ Pendiente |
| G-03 / G-04 | `sandiese.safetensors` | `architecture, building, grey_background` | 0,6 / 0,8 | ⬜ Pendiente |
| G-05 / G-06 | `xsarchitectural-10superhighrisebuilding.safetensors` | `architectural renderings, bird's-eye view` | 0,6 / 0,8 | ⬜ Pendiente |
| G-07 / G-08 | `room.safetensors` | `room` | 0,6 / 0,8 | ⬜ Pendiente |
| G-09 / G-10 | `landscape_architecture_sketch.safetensors` | `sketch, architecture, building` | 0,6 / 0,8 | ⬜ Pendiente |
| G-11 / G-12 | `Le Corbusier 2.2.7.2_sd1.5-000016.safetensors` | `zhuai_pb, brutalism` | 0,6 / 0,8 | ⬜ Pendiente |
| G-13 / G-14 | `BrutalistTech-20.safetensors` | `brutaltech, cement` | 0,6 / 0,8 | ⬜ Pendiente |
| G-15 / G-16 | `archisketch-v1.safetensors` | `linear` | 0,6 / 0,8 | ⬜ Pendiente |
| G-17 / G-18 | `markerhandsketch-V1.safetensors` | `marker painting, handsketch` | 0,6 / 0,8 | ⬜ Pendiente |

### SDXL (Juggernaut XL) — G-19 a G-32

| # | LoRA | Trigger | Strength | Estado |
|---|------|---------|----------|--------|
| G-19 / G-20 | `Architectural_Massing.safetensors` | — | 0,6 / 0,8 | ⬜ Pendiente |
| G-21 / G-22 | `Architecture_Building.safetensors` | — | 0,6 / 0,8 | ⬜ Pendiente |
| G-23 / G-24 | `ArcvizXL_V01.safetensors` (rank 128) | `archviz 1` | 0,6 / 0,8 | ⬜ Pendiente |
| G-25 / G-26 | `bookstore-xl.safetensors` (rank 128) | `mrares, bookstore` | 0,6 / 0,8 | ⬜ Pendiente |
| G-27 / G-28 | `isometric-v1.safetensors` (rank 16) | `isometric style` | 0,6 / 0,8 | ⬜ Pendiente |
| G-29 / G-30 | `SLskyscraperrenderingXL_V1.0.safetensors` (rank 128) | — | 0,6 / 0,8 | ⬜ Pendiente |
| G-31 / G-32 | `baroque_architecture-000006.safetensors` (rank 64) | — | 0,6 / 0,8 | ⬜ Pendiente |

---

## Leyenda de versiones

`n_01-{LETRA}-{NN}.png` — la letra **G** se suma a la leyenda de `reglas-workflows-comfy.md`:

- **A** = Baseline absoluto (3 corridas idénticas, sin cambios)
- **B** = Variación de **prompt** (atmósfera, estilo, materiales)
- **C** = Exploración de **parámetros** (cfg, sampler, scheduler, steps)
- **D** = Migración de **modelo** (SD 1.5 → SDXL)
- **E** = Variación de **resolución / aspect ratio**
- **F** = Test de **ControlNet / img2img**
- **G** = **Test de LoRA** (fuerza, trigger, base) — añadido 2026-10-28

---

## Referencias cruzadas

- **Log detallado:** `02-WF-log-WFloraslocales.md`
- **Nodos y triggers:** `03-nodos-WFloraslocales.md`
- **Backlog:** `04-backlog.md`
- **Salidas:** `salidas/n_01-G-{NN}.png`
- **Datos de corrida:** `PLANS/calibracion-loras.json`
