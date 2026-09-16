---
tipo: playbook
codigo: pbk-comfyui
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-09-09
tags: [pbook, comfyui, txt2img, img2img, controlnet, canny, depth, video, runpod, arquitectura]
---

# pbk-comfyui — ComfyUI para el estudio

> Documento canónico de generación con IA: qué flujo usar para cada necesidad arquitectónica, con qué modelo y parámetros en RX 570 8GB (DirectML) vs RunPod, y cómo archivar resultados en el vault. Fusiona `pbk-comfyui-arquitectura` + `pbk-comfyui-controlnet` + `pbk-comfyui-flujos-index` (2026-09-09, UNICO pbk ComfyUI). Fichas de modelos en [[wiki/glosario/software/comfyui|comfyui]].

- [Catálogo de flujos](#catálogo-de-flujos)
- [Mapa de decisión: qué flujo uso](#mapa-de-decisión-qué-flujo-uso)
- [Base local: RX 570 8GB DirectML](#base-local-rx-570-8gb-directml)
- [txt2img (concepto)](#txt2img-concepto)
- [img2img (variaciones sobre base)](#img2img-variaciones-sobre-base)
- [Pipeline ControlNet (diagrama)](#pipeline-controlnet-diagrama)
- [ControlNet: Canny](#controlnet-canny)
- [ControlNet: Depth](#controlnet-depth)
- [Otros ControlNets útiles](#otros-controlnets-útiles)
- [Doble ControlNet (Canny+Depth)](#doble-controlnet-cannydepth)
- [Validación n_03](#validación-n_03)
- [Upscale / Hires Fix (entrega)](#upscale--hires-fix-entrega)
- [Video: imagen→video y recorridos](#video-imagenvideo-y-recorridos)
- [RunPod: cuándo y cómo](#runpod-cuándo-y-cómo)
- [Prompt-packs de arquitectura](#prompt-packs-de-arquitectura)
- [DoD y archivo en el vault](#dod-y-archivo-en-el-vault)
- [Proyectos vinculados](#proyectos-vinculados)
- [Troubleshooting exprés](#troubleshooting-exprés)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Catálogo de flujos

| Flujo | Sección | Pipeline base |
|---|---|---|
| txt2img (concepto) | [§ txt2img](#txt2img-concepto) | CheckpointLoader → CLIPTextEncode → KSampler → VAEDecode |
| img2img (variaciones) | [§ img2img](#img2img-variaciones-sobre-base) | LoadImage → VAEEncode → KSampler (denoise<1) → VAEDecode |
| ControlNet (Canny/Depth/otros) | [§ diagrama](#pipeline-controlnet-diagrama) | LoadImage → preprocesador → ControlNetApply → KSampler |
| Upscale / Hires Fix | [§ upscale](#upscale--hires-fix-entrega) | 2º KSampler denoise bajo → ImageUpscaleWithModel |
| Video img2video | [§ video](#video-imagenvideo-y-recorridos) | Render → stage → LTX i2v (RunPod) |

## Mapa de decisión: qué flujo uso

| Necesidad | Flujo | Modelo local | Si no cabe → |
|---|---|---|---|
| Concepto rápido / mood | txt2img 512 | ArchitectureRealmix v1.1 | — (siempre cabe) |
| Variante de foto/croquis | img2img denoise 0.6–0.8 | ArchitectureRealmix | — |
| Planta/corte/fachada → render fiel | ControlNet **Canny** | Realmimix + canny SD15 | RunPod SDXL + Union |
| Perspectiva/volumetría con espacio real | ControlNet **Depth** | Realmimix + depth fp16 | RunPod SDXL + Union |
| Croquis a mano → render | Scribble/Lineart | Realmimix + scribble | — |
| Fachada ortogonal exacta | MLSD | Realmimix + mlsd | — |
| Render final entrega A3/A2 | txt2img/CN + Hires + upscaler 4x | Juggernaut XL (justo) | **RunPod** (recomendado) |
| Recorrido / video masa | img2video (LTX/AnimateDiff) | no local | **RunPod** |
| Iteración ultra-rápida | GGUF turbo (Z-Image/Flux schnell) | pendiente instalar | RunPod Flux |

## Base local: RX 570 8GB DirectML

- **Launch:** `corre_comfyui.bat` → `python main.py --directml 0 --force-fp16 --disable-cuda-malloc` (nunca flags CUDA/Nvidia; torch `2.4.1+cpu`, GPU vía torch_directml).
- **Patch VRAM:** `comfy/model_management.py:324` parcheado (WMI) — DirectML reporta 1GB fantasma. Si se actualiza ComfyUI, re-aplicar.
- **Capacidad real:** SD 1.5 + hasta **2 ControlNet** sin problema · SDXL cabe justo (batch 1, res ≤ ~1216×832, `--lowvram`/`--cpu-vae` si OOM).
- **Preferencia FP16** (FP32 cabe pero más lento). Ver `AGENTS.md` § ComfyUI.

## txt2img (concepto)

Pipeline: `CheckpointLoader → CLIPTextEncode(±) → KSampler → VAEDecode → SaveImage`.

| Parámetro | ArchitectureRealmix (SD1.5) | Juggernaut XL (SDXL, entrega) |
|---|---|---|
| steps / cfg | 30 / 7 | 30–35 / 3–4 |
| sampler/scheduler | euler_ancestral + karras | dpmpp_2m + karras |
| resolución | 512² concepto · 768×512 estándar | 1216×832 ext · 832×1216 int · 1024² aérea |
| tiempo RX570 | ~55 s / ~90 s / ~130 s | ~45–60 s + Hires |
| batch | 1 (3 corridas baseline letra **A**) | 1 |

Negativo base: `blurry, low quality, distorted, watermark, text, signature, cartoon, illustration`.

## img2img (variaciones sobre base)

Pipeline: `LoadImage → VAEEncode → KSampler (denoise < 1) → VAEDecode`. El **denoise** es el mando: `0.3` = retoque leve · `0.6–0.8` = re-estilo manteniendo composición · `1.0` = txt2img (ignora input). Caso estudio: foto de maqueta / render viejo denoise 0.6 + prompt de materialidad nueva.

## Pipeline ControlNet (diagrama)

```
CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────┤
    └──vae──────────────────┐   │
                            │   │
LoadImage ──► ImageScale ──► Canny ──┐
                │           │       │
ControlNetLoader ──cn───────┤       │
                │           │       │
CLIPTextEncode (pos) ───────┤       │
CLIPTextEncode (neg) ───────┤       │
                            ▼       ▼
ControlNetApplyAdvanced ──► KSampler ──► VAEDecode ──► SaveImage
```

## ControlNet: Canny

**Qué es:** ControlNet v1.1 copia la UNet congelada y le inyecta un mapa de **bordes Canny** (zero-conv). Preserva líneas exactas; el modelo rellena materiales/luz. Archivo: `control_v11p_sd15_canny.safetensors` (689 MB, +~1.5 GB VRAM).

Pipeline: `LoadImage → ImageScale(512, lanczos) → CannyEdgeDetector → ControlNetLoader → ControlNetApplyAdvanced → KSampler`.

| Input | low/high preprocessor | strength | end% |
|---|---|---|---|
| Planta / sección limpia (DWG→PNG) | 30 / 100 | 1.0 | 0.80 |
| Fachada (Rhino make2d) | 80 / 180 | 0.9 | 0.80 |
| Croquis mano (foto celular) | 20 / 80 | 0.8 | 0.75 |
| Vista hidden-line (Revit/SketchUp) | 40 / 120 | 0.9 | 0.80 |

Nodo Canny usa thresholds normalizados 0–0.99 (dividir por 255). Default producción local: **Canny solo** (dual no cabe holgado en 8 GB con SDXL; con SD1.5 sí — ver abajo).

## ControlNet: Depth

**Qué es:** preserva **estructura espacial** (masas, profundidad, interior-exterior) vía mapa de profundidad MiDaS/DPT. Archivo: `control_v11f1p_sd15_depth_fp16.safetensors` (689 MB FP16, +~1.2 GB VRAM).

Preprocesadores: `dpt_hybrid` (calidad general) · `midas_v21_small` (rápido) · DepthAnything V2 (mejor detalle, requiere pack `comfyui_controlnet_aux`).

| Caso | strength | end% | preprocessor |
|---|---|---|---|
| Perspectiva exterior | 0.6–0.8 | 0.8–0.9 | dpt_hybrid |
| Interior profundo | 0.7–0.85 | 0.85 | dpt_hybrid |
| Sección / topografía | 0.4–0.7 | 0.7–0.8 | midas_small |
| Foto → render fotorreal | 0.75–0.9 | 0.85 | dpt_hybrid |

## Otros ControlNets útiles

| CN | Input ideal | strength | Nota |
|---|---|---|---|
| Scribble | boceto suelto | 0.5–0.7 | Sin preprocesador (trazo directo) |
| Lineart | DWG exportado, CAD | 0.5–0.7 | Estética "plano delineado" |
| MLSD | fachadas/elevaciones rectas | 0.7–0.9 | Solo rectas (M-LSD) |
| Normal Map | export Rhino (normales) | 0.7–0.9 | Orientación superficies |
| Seg | zonificación/programa | 0.7–0.9 | Layout por colores |
| OpenPose | figura humana escala | 0.6–0.8 | Gente en renders |
| Union SDXL | todo-en-uno (SDXL) | 0.8 | 1.5 GB; task-embeddings 0–7; **solo RunPod** con Juggernaut (9.6 GB combinados) |

Preprocesadores via `comfyui_controlnet_aux` (Fannovel16): canny/hed/lineart/mlsd/scribble + MiDaS/LeReS/Zoe/DepthAnything + normales.

## Doble ControlNet (Canny+Depth)

Validado local SD1.5 (n_03 dual): Canny `0.75 / 0.0–0.75` (50/200) + Depth `0.65 / 0.0–0.85` (dpt_hybrid) sobre ArchitectureRealmix. Dos `ControlNetApplyAdvanced` en serie antes del KSampler. Con SDXL en RX 570 **no intentar** (OOM) — usar Union en RunPod.

## Validación n_03

Variantes del flujo validadas en `n_03-controlnet`:

| Variante | ControlNet | Preprocesador | Pipeline |
|----------|-----------|---------------|----------|
| Canny (v1.0.2) | `sd15_canny` | Canny edges | LoadImage → ImageScale → Canny → CN |
| Scribble (opt2) | `sd15_scribble` | Ninguno | LoadImage → ImageScale → CN |
| Dual (opt3) | Canny + Depth | Canny + DA3 | LoadImage → ImageScale → [Canny, DA3] → 2×CN |

Nodos (fichas en [[wiki/glosario/software/comfyui|comfyui]]): [ImageScale]([[wiki/glosario/software/comfyui#nodo--imagescale]]) · [Canny]([[wiki/glosario/software/comfyui#nodo--canny]]) · [ControlNetLoader]([[wiki/glosario/software/comfyui#nodo--controlnetloader]]) · [ControlNetApplyAdvanced]([[wiki/glosario/software/comfyui#nodo--controlnetapplyadvanced]]).

## Upscale / Hires Fix (entrega)

- **Hires Fix:** 2º KSampler 15–20 steps denoise 0.15–0.35 con upscale latente 1.5x.
- **Upscaler modelo:** `ImageUpscaleWithModel` — Remacri (arquitectura pura ★★★★★) o ClearReality (gente/vegetación ★★★★★). Ambos CC-BY-NC: **solo interno**, para comercial usar RealESRGAN_x4plus/SwinIR.
- Cadena entrega: txt2img 768×512 → Hires 1.5x → post 2x ≈ 2304×1536 (~3.5 MP, A3/A2 300 dpi).

## Video: imagen→video y recorridos

Local RX 570 **no viable** para video serio. Dos rutas:

1. **RunPod (recomendado):** workflow LTX-2 ControlNet (texto→video, imagen→video, video→video) con guías Depth/Canny/Pose + audio sincronizado, 2 etapas (base + upscale latente x2), `VHS_VideoCombine` a MP4. Control LoRAs: `ltx-2-19b-IC-LoRA-{Depth,Canny,Pose}-Control` + `ltx-2-19b-distilled-lora-384`. Regla i2v: `strength ~0.6` (1.0 congela).
2. **Local experimental:** AnimateDiff (SD1.5, 16 frames 512²) solo para tests de masa/movimiento, nunca entrega.

Caso estudio: render final (este pbook) → `stage` como input → LTX i2v 4 s → recorrido de 10 s para comitente.

## RunPod: cuándo y cómo

**Cuándo:** SDXL + Union · video · batch de concurso (>20 renders) · Emilia sin GPU dedicada.

**Cómo (resumen):** cuenta RunPod → Pod GPU ≥24 GB (RTX 3090 ≈ 0.22 USD/h community) → template `ComfyUI + Flux.1-dev` (valyriantech/comfyui-with-flux) → abrir ComfyUI en browser → subir workflow + modelos/LoRA vía JupyterLab → Queue → descargar MP4/PNG. Detener el pod al terminar (**billa por hora**). Guía paso a paso: RunPod ComfyUI+Flux (ver Referencias). ComfyUI es agnóstico: el mismo pod corre SD1.5/SDXL/ControlNets/LoRAs.

## Prompt-packs de arquitectura

Exterior: `architecturerealmix style, modern architecture, concrete and glass facade, minimalist design, photorealistic, architectural photography, natural lighting, 8K` · Interior: `modern living room, floor-to-ceiling windows, warm wood accents, minimalist furniture, natural light, photorealistic` · SDXL: prefijar `photorealistic, raw photo, 8k uhd, highly detailed, masterpiece, canon r5, 24mm tilt-shift` + tipología. Nocturno: `night, illuminated windows, floodlights`. LoRA SD1.5 (Architectural Visualization / Brutalist / Interior) a strength 0.6–0.8 **antes** del KSampler.

## DoD y archivo en el vault

Toda salida que entre al proyecto: nombre `n_XX-{A–F}-{NN}.png` (A baseline · B prompt · C parámetros · D modelo · E resolución · F ControlNet/img2img) en `.../salidas/` del WF + entrada en `02-WF-log` (seed, cfg, steps, modelo, strength) + render final a `activos/proyectos/<proyecto>/renders/`. Renders de entrega comercial: verificar licencia del checkpoint/upscaler (OpenRAIL ok con atribución; CC-BY-NC nunca a cliente).

## Proyectos vinculados

- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/00-index|n_03 — ControlNet]]
- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/index-n_03_WF01|n_03-WF01-croquis-estadio]]
- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/adr/00-index|ADRs]]

## Troubleshooting exprés

| Síntoma | Causa probable | Fix |
|---|---|---|
| OOM en SDXL | res/batch/CN de más | `--lowvram --cpu-vae`, res ≤1216×832, 1 CN, batch 1 |
| Negro / artefactos | scheduler/cfg de DiT mal | GGUF: cfg 1.0, steps 4–8, scheduler simple |
| Canny no guía | strength/end bajos o res ≠512 | strength ≥0.8, end 0.8, ImageScale lanczos 512 |
| Modelo no aparece | carpeta equivocada | `models/checkpoints|controlnet|upscale_models`, Refresh, reiniciar |
| Cola atascada / VRAM full | modelo anterior en memoria | `Free VRAM` / reiniciar; detalle en [[wiki/glosario/interno/pbooks/pbk-troubleshooting-reconexion|pbk-troubleshooting-reconexion]] |

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|comfyui]]
- [[wiki/glosario/interno/pbooks/pbk-troubleshooting-reconexion|pbk-troubleshooting-reconexion]]
- [[wiki/glosario/conceptos/lean|lean]]

## Referencias

- ComfyUI Docs — ControlNet guide: https://docs.comfy.org/controlnet-guide (verificado 2026-09-09 — 200)
- ComfyUI Docs — Flux.1 ControlNet (Canny/Depth): https://docs.comfy.org/tutorials/flux/flux-1-controlnet (verificado 2026-09-09 — 200)
- ComfyUI ControlNet integration (tipos Union 0–7): https://deepwiki.com/comfyanonymous/ComfyUI/7.1-controlnet-integration (verificado 2026-09-09 — 200)
- comfyui_controlnet_aux (preprocesadores): https://github.com/Fannovel16/comfyui_controlnet_aux (verificado 2026-09-09 — 200)
- RunPod — ComfyUI + Flux guide (template, costos, txt2img/img2img/video): https://www.runpod.io/articles/guides/comfy-ui-flux (verificado 2026-09-09 — 200)
- LTX-2 ControlNet depth video workflow: https://www.runcomfy.com/comfyui-workflows/ltx-2-controlnet-in-comfyui-depth-controlled-video-workflow (verificado 2026-09-09 — 200)
- Zhang et al. — ControlNet paper: https://arxiv.org/abs/2302.05543 (verificado 2026-09-09 — 200)
- MiDaS paper: https://arxiv.org/abs/1907.01341 (verificado 2026-09-09 — 200)
- ComfyUI repo: https://github.com/comfyanonymous/ComfyUI (verificado 2026-09-09 — 200)
