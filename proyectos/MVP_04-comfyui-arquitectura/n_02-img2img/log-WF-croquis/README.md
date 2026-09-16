---
tipo: registro-workflow
workflow: workflow_img2img_croquis.json
nivel: n_02-img2img
modelo: architecturerealmix_v11.safetensors
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-18
tags: [registro, workflow, croquis, img2img]
---

# Registro: Workflow img2img — Croquis a Render

**Archivo ejecutable:** [[workflow_img2img_croquis.json]]

Pipeline img2img: croquis/foto → render arquitectónico. Similar al txt2img pero recibe una imagen de entrada (sketch) que el denoising transforma en render.

### Grafo de nodos

```
[1] CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────────┤
    └──vae──────────────────────┐   │
                                │   │
[2] CLIPTextEncode (pos) ──────┤   │
[3] CLIPTextEncode (neg) ──────┤   │
                                ▼   ▼
[4] LoadImage ──► [5] ImageScale ──► [6] VAEEncode ──► [7] KSampler ──► [8] VAEDecode ──► [9] SaveImage
                  (512², crop)                      denoise < 1
```

**Diferencia clave con txt2img:** En lugar de `EmptyLatentImage` (ruido puro), usa `VAEEncode` para codificar la imagen de entrada al espacio latente, y el `KSampler` aplica denoise < 1 para transformar el croquis manteniendo su estructura base.

## Parámetros base recomendados

| Parámetro | Valor | Rango de iteración |
|-----------|-------|-------------------|
| steps | 30 | 20-40 |
| cfg | 7 | 5-10 |
| sampler | euler | euler, dpmpp_2m, dpmpp_sde |
| scheduler | normal | normal, karras, exponential |
| seed | variable | 0 - 2^32 |
| denoise | 0.7 | 0.3-0.9 |
| resolución | según croquis | — |

## Input / Output

| Carpeta | Contenido |
|---------|-----------|
| `inputs-croquis/` | **Sketch original** (PNG/JPG) — repositorio local en el vault |
| `salidas/` | **Render generado** — enlace desde `prompts-log.md` |
| ComfyUI `input/croquis/` | Carpeta destino: copiar sketch acá antes de ejecutar el workflow |

## Enlaces útiles

- [[prompts-log]] — Log versionado de corridas (imágenes en `salidas/`)
- [[nodos]] — Documentación de nodos
- [[modelos-recomendados]] — Guía de modelos del estudio
