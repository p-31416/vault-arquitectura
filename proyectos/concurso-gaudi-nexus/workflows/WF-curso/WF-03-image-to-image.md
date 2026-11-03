---
tipo: guia
proyecto: concurso-gaudi-nexus
modulo: 3
slug: image-to-image
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, wf-curso, wf-03, curso-ai-gaudi, sdxl, img2img, rhino]
idioma: es
---

# WF-03 — Rhino-to-Image + Rhino → render denoise 0,65

> Unifica [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/flujo-03-image-to-image\|flujo-03]] + [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/WF-03_sdxl\|WF-03_sdxl]].

## 1. Ver en Miro + video

| Fuente | Link |
|--------|------|
| Miro frame módulo 3 | pendiente link Sol |
| Video módulo 3 (1 h 22 min 14 s) | pendiente link Sol |
| Transcripción ES/EN | [[raw/yt/transcripts/2026-10-21_mux-image-to-image\|transcripción]] |

## 2. Flujo del curso (resumen)

Upscaling (×3/×4, Topaz creativity 1-9, 2K diario / 4K final) → **Rhino-to-Image** (INSTRUCTION.md en proyecto LLM → `start` + captura Rhino + foto referencia → prompt JSON → workflow FLUX.2 klein 9B + Load LoRA, strength 1, megapíxeles fijos, compare images) → image-edit (Nano Banana, 1 ref borrar / 2 refs material) → collage Photoshop + inpainting máscara ~75 %.

Claves: `STRICT CAMERA LOCK` + `MATCH CAMERA OF IMAGE 1 EXACTLY` · negro = ventana/loggia · seed vía `edit subgraph widgets` / `random noise` · prompt coach por bloques.

## 3. WF SDXL vista

JSON: `workflow_WF-03_sdxl.json` (misma carpeta WF-curso/, original en `workflows/sdxl-vista/`) · 10 nodos · img2img · seed 11 · 30 steps · **denoise 0,65** · prefijo `gx-WF03`. `LoadImage PONER-RUTA-rhino_vista.png` → `ImageScale` 1024² bilinear center → `VAEEncode` → `KSampler` → `VAEDecode` → `SaveImage`. R4 pendiente.

Dial: 0,35 repinta · 0,55 WF-07 · **0,65 este WF** · 0,80 explora. Segundo camino Flux 9B + LoRA en RunPod (decisión día 2).

## 4. Cómo lo adaptamos

Grafo 23 nodos API con doble `ReferenceLatent` ya armado · render Flux en pod (transformer fp8 + Qwen3-8B + VAE Flux2) · upscale `RealESRGAN_x4plus` + hires denoise 0,15-0,35 · edición `sd-v1-5-inpainting-fp16` + Depth Anything 3 · collage Photoshop/Photopea.

## 5. Checks jurado

Geometría del equipo intacta (`compare images` A render / B volumetría) · encuadre fijado por texto · negro declarado como ventana/loggia · escala desde cota real · prompt del agente leído antes de pegar.
