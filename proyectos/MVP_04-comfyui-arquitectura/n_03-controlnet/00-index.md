---
tipo: index
nivel: n_03-controlnet
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-19
tags: [index, controlnet, canny, mvp04, estadio]
---

# n_03 — ControlNet

Generación de renders arquitectónicos con guía espacial. ControlNet permite que el modelo respete la geometría de una imagen de entrada (foto, plano, croquis).

## Modelos ControlNet instalados

| Modelo | Tipo | Tamaño | VRAM extra |
|--------|------|--------|------------|
| `control_v11p_sd15_canny.safetensors` | Detección de bordes | 689 MB (fp16) | ~1-2 GB |
| `control_v11f1p_sd15_depth_fp16.safetensors` | Profundidad | 689 MB (fp16) | ~1-2 GB |

## Workflow logs

- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/index-n_03_WF01]] — Croquis de estadio → ControlNet Canny

## Flujo de trabajo base

```
CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────┤
    └──vae──────────────────┐   │
                            │   │
LoadImage ──► Canny ────────┤   │
                │           │   │
ControlNetLoader ──cn───────┤   │
                │           │   │
CLIPTextEncode (pos) ───────┤   │
CLIPTextEncode (neg) ───────┤   │
                            ▼   ▼
ControlNetApplyAdvanced ──► KSampler ──► VAEDecode ──► SaveImage
```

- **Modelo:** `architecturerealmix_v11.safetensors` (~2 GB, SD 1.5)
- **Hardware actual:** AMD RX 570 8GB (DirectML), ~5-8s por render 512×512
