---
tipo: plan
mvp: 04.02
fecha_creacion: 2026-10-14
ultima_actualizacion: 2026-10-14
tags: [mvp_04.02, plan, lora, inpainting, outpainting, sd15, demo]
---

# PLAN F1-F8 — 8 flujos nuevos (txt2img → LoRA, inpainting, outpainting)

> Vive en MVP 04.02 (versión activa). MVP_04 queda cerrado como lección aprendida — su resumen vive en [[proyectos/MVP_04-comfyui-arquitectura/RESUMEN-flujos-probados|RESUMEN-flujos-probados]]. Leer este plan antes de construir los JSON. Todo corre en RX 570 8GB DirectML con modelos ya presentes en `P:\00-repos\ComfyUI\models\`.

## Mapeo a los WF 04.02 (sin duplicar)

| Flujos | Dónde viven | Estado que aprovechan |
|---|---|---|
| F1–F4 (txt2img + LoRAs) | Base nueva `WF-03/inputs/base-01.png` + serie F-E | F-E pedía LoRAs A+B (791004+1911622, 54 MB): **desbloqueado con los descargados hoy** (markers 9 MB + archisketch 18 MB, rol estilo cubierto; B detail-enhancer queda descarga opcional) |
| F5 (img2img + LoRA) | Extensión de WF-03 F-A (denoise 0.4/0.6/0.8 ya probados) | T2 (0.4) aún pendiente — correr junto |
| F6 (inpainting) | Fase 2 de WF-02 (F-01 ventanas OK, 141s) | Casos nuevos: cielo→atardecer, paño→madera; más test denoise 0.8 del backlog |
| F7 (outpainting) | Nuevo: propone `WF-04-outpainting` (nadie lo cubre) | `ImagePadForOutpaint` verificado en servidor |
| F8 (Canny + LoRA) | Cruce WF-03 F-C (pendiente JSON) + F-E | Params Canny 0.25/0.55 + CN 0.9 ya validados en WF-01 |
| — | WF-01 planta ilustrada | En pausa, no se toca |

## Base común (todos los flujos)

- Checkpoint: `architecturerealmix_v11.safetensors` (SD1.5) salvo F6/F7 que usan `sd-v1-5-inpainting-fp16.safetensors`.
- LoRAs: `markerhandsketch-V1.safetensors` (triggers `marker painting, handsketch`) · `archisketch-v1.safetensors` (trigger `linear`).
- Regla R1: todo input de imagen pasa por `ImageScale` 512×512 lanczos crop center.
- 1 rama por corrida (lección WF_v5 OOM). Batch 1. Salidas `salidas/n_07-{L}-{NN}.png`.

## F1 — txt2img base (baseline de la serie)

- Nodos: `CheckpointLoaderSimple → CLIPTextEncode± → EmptyLatentImage 768×512 → KSampler → VAEDecode → SaveImage (demoF1_txt2img)`.
- Params: euler/normal, 30 steps, cfg 7, seed 42, denoise 1.0. Prompt casa hormigón minimalista (mismo que demo-01).
- Salida: `n_07-A-01.png`. Tiempo estimado ~60-90s. Es el input de F5.

## F2 — txt2img + LoRA markers

- F1 + nodo `LoraLoader` (markers, 0.6/0.6) entre checkpoint y sampler/CLIP. Prompt suma `marker painting, handsketch`.
- Mismo seed 42 que F1 → par comparativo foto vs croquis. Salida `n_07-B-01.png`.

## F3 — txt2img + LoRA sketch

- F1 + `LoraLoader` (archisketch, 0.5/0.5). Prompt suma `linear, grey, white background, simple background`.
- Salida `n_07-B-02.png`. Si el trazo sale débil: sweep 0.5 → 0.8 (corrida B-03).

## F4 — txt2img + stack 2 LoRAs

- markers 0.6 → archisketch 0.5 en serie (dos `LoraLoader` encadenados). Ambos triggers en prompt.
- Salida `n_07-B-04.png`. Demuestra stacking (eco imagen Civitai 29073569).

## F5 — img2img + LoRA (foto → croquis)

- Input `n_07-A-01.png` vía `LoadImage → ImageScale 512 → VAEEncode`, KSampler denoise 0.65 + LoRAs F4.
- Corridas: denoise 0.45 (`n_07-F-01`), 0.65 (`n_07-F-02`), 0.75 (`n_07-F-03`). Misma seed para comparar.

## F6 — inpainting (cambiar zona sin tocar el resto)

- Checkpoint `sd-v1-5-inpainting-fp16` + `InpaintModelConditioning` (positive/negative + VAE + pixels + mask, noise_mask true) + `KSampler` denoise 1.0.
- Casos demo: a) cielo de F1 → atardecer (máscara rectángulo superior, se pinta en editor del LoadImage); b) paño fachada → madera oscura. `grow_mask_by 6`.
- Salidas `n_07-F-04.png` (cielo), `n_07-F-05.png` (material). Si el borde se nota: subir feather/grow a 12.

## F7 — outpainting (agrandar encuadre)

- F1 + `ImagePadForOutpaint` (extender derecha 256px, feather 32) → máscara auto → mismo condicionamiento inpaint F6.
- Salida `n_07-F-06.png` (768×512 → 1024×512). Si la extensión deriva: bajar denoise a 0.8 en la zona de pad.

## F8 — Canny + LoRA (croquis con geometría exacta y estilo)

- `croquis001.jpg → ImageScale 512 → Canny 0.31/0.59 → ControlNetLoader canny → ControlNetApplyAdvanced 0.9/0.0-0.85` + markers 0.6, KSampler denoise 0.4 (lección WF_v5), seed 42.
- Salida `n_07-F-07.png`. Puente entre n_03 (fidelidad) y n_07 (estilo).

## Orden de construcción y prueba

1. F1 → correr → `n_07-A-01.png` (input de F5/F6/F7).
2. F2, F3, F4 en serie (mismo seed, comparativa directa).
3. F5 (3 denoise), F6 (2 máscaras), F7, F8.
4. Cada corrida: entrada en su `02-WF-log` + imagen en `salidas/`.

## Fuera del plan (próximo ciclo)

- SDXL/Juggernaut (9 min/imagen, solo entrega), upscale Remacri (modelo ausente), video LTX (RunPod).
