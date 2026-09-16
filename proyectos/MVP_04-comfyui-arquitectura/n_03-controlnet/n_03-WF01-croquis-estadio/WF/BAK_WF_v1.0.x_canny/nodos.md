---
tipo: registro-nodos
workflow: BAK_WF_v1.0.x_canny
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-07-19 21:00
tags: [registro, nodos, comfyui, controlnet, canny, bak]
---

# Registro de Nodos — Canny Baseline (v1.0.x, deprecado)

Reemplazado por [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1a_scribble/DET-WF_v1.1a_scribble|v1.1a scribble]] y [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/DET-WF_v1.1b_dual|v1.1b dual]].

## Pipeline

```
CheckpointLoaderSimple ──model──â”
    ├──clip─────────────────────┤
    └──vae──────────────────â”   │
                            │   │
LoadImage ──► ImageScale ──► Canny ──â”
                │           │       │
ControlNetLoader ──cn───────┤       │
                │           │       │
CLIPTextEncode (pos) ───────┤       │
CLIPTextEncode (neg) ───────┤       │
                            ▼       ▼
ControlNetApplyAdvanced ──► KSampler ──► VAEDecode ──► SaveImage
```

## Nodos específicos del workflow

| ID | Nodo | Configuración | Documentación wiki |
|----|------|--------------|-------------------|
| 1 | CheckpointLoaderSimple | `architecturerealmix_v11.safetensors` | [[wiki/glosario/software/comfyui|Nodos comunes]] |
| 2 | LoadImage | `croquis001.jpg` | [ComfyUI Docs](https://docs.comfy.org/built-in-nodes/LoadImage) |
| 12 | ImageScale | `lanczos`, 512×512, `crop=center` | [[wiki/glosario/software/comfyui#nodo--imagescale|ImageScale]] |
| 3 | Canny | `low=0.31`, `high=0.59` | [[wiki/glosario/software/comfyui#nodo--canny|Canny]] |
| 4 | ControlNetLoader | `control_v11p_sd15_canny.safetensors` | [[wiki/glosario/software/comfyui#nodo--controlnetloader|ControlNetLoader]] |
| 5 | CLIPTextEncode (pos) | Prompt estadio (ver prompts-log) | — |
| 6 | CLIPTextEncode (neg) | Prompts negativos | — |
| 7 | EmptyLatentImage | 512×512, batch=1 | — |
| 8 | ControlNetApplyAdvanced | `strength=0.7`, `start=0`, `end=0.7` | [[wiki/glosario/software/comfyui#nodo--controlnetapplyadvanced|ControlNetApplyAdvanced]] |
| 9 | KSampler | `steps=30`, `cfg=7`, `euler`, `normal`, `seed=42` | — |
| 10 | VAEDecode | — | — |
| 11 | SaveImage | prefix=`n_03` | — |

## Parámetros clave

| Parámetro | Valor | Notas |
|-----------|-------|-------|
| Canny low/high | 0.31 / 0.59 | Revertido en v1.0.2 |
| strength | 0.7 | Balance fidelidad/libertad |
| end_percent | 0.7 | Último 30% libre para texturas |
| resolución | 512×512 | Necesaria para evitar OOM en 8GB VRAM |
