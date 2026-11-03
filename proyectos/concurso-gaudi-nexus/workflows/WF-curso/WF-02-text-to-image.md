---
tipo: guia
proyecto: concurso-gaudi-nexus
modulo: 2
slug: text-to-image
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, wf-curso, wf-02, curso-ai-gaudi, sdxl, txt2img, interior]
idioma: es
---

# WF-02 — Text-to-Image + interior bóveda 1216×832

> Unifica [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/flujo-02-text-to-image\|flujo-02]] + [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/WF-02_sdxl\|WF-02_sdxl]].

## 1. Ver en Miro + video

| Fuente | Link |
|--------|------|
| Miro frame módulo 2 | pendiente link Sol |
| Video módulo 2 (47 min 09 s) | pendiente link Sol |
| Transcripción ES/EN | [[raw/yt/transcripts/2026-10-21_mux-text-to-image\|transcripción]] |

## 2. Flujo del curso (resumen)

Comparativa mismo prompt + misma seed sobre SD1.5 (DreamShaper) → SDXL → FLUX.1 (1024²) → FLUX.2 klein 9B + LoRA rhino-to-image al 50 % y 100 %.

Prompt constante: `concrete house in desert rocky landscape` · negativo SD1.5: `cat, dog, waterpark`.
Coach: `start` → modelo `FLUX.2 klein` → refs Tadao Ando / Rick Joy / Kogan → JSON por bloques (escena·descripción·estilo·iluminación·ambiente·fondo·composición) → simplificar a 50 palabras sin JSON en fase inicial.
LoRA: `Load LoRA` al MODEL, repo HF privado + token `read` + secret Comfy Cloud + Model Library → strength 1.0 vs 0.5 vs sin LoRA.

Veredicto video: FLUX.2 klein 9B de lejos la mejor opción, en Comfy Cloud.

## 3. WF SDXL vista

JSON: `workflow_WF-02_sdxl.json` (misma carpeta WF-curso/, original en `workflows/sdxl-vista/`) · 1216×832 · seed 43 · 35 steps · cfg 4 · prefijo `gx-WF02`. R4 pendiente.

+ `catenary vault interior, trencadis mosaic light accents, warm concrete, volumetric light through skylight, fractal column forest, photorealistic, 8k uhd, masterpiece, architectural photography` · − de la casa. Probar RealVisXL v5.0 (mejor interior) y RealArchmix XL v3.5.

## 4. Cómo lo adaptamos

Rama SD1.5/SDXL local con checkpoints en disco · rama FLUX.2 klein 9B en RunPod · LoRA `rhino-to-image.basic` (120,8 MB) por `scp` al pod · prompt coach como proyecto Claude.

## 5. Checks jurado

Una variable por vez con prompt/seed fijos · tabla sin LoRA / 50 % / 100 % con `strength` anotado · referencia de autor (Ando/Rick Joy/Kogan) declarada como decisión de proyecto.
