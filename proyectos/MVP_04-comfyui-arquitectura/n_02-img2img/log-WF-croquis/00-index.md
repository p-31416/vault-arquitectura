---
tipo: index
nivel: n_02-img2img
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-18
tags: [index, img2img, mvp04, croquis]
---

# n_02 — img2img: Croquis → Render

Transformación de croquis arquitectónicos en renders fotorrealistas. Pipeline SD 1.5 con ArchitectureRealmix v1.1 + imagen de entrada.

- [[prompts-log]] — Log detallado de corridas
- [[nodos]] — Documentación de cada nodo
- [[backlog]] — Próximas pruebas pendientes

## Variantes ejecutadas

| Versión | Fecha | Hora | Cambio | Config | Imagen |
|---------|-------|------|--------|--------|--------|
| `A-01` | 2026-07-18 | — | Primer render img2img desde croquis001.jpg | steps=30, cfg=7, euler, normal, 512×512, seed=42, denoise=0.7 | ![A-01](salidas/n_02-A-01.png) |

### Leyenda de versiones

`n_02-{L}-{nn}`:
- **A** = Baseline (denoise fijo, prompt base, sin cambiar nada)
- **B** = Variación de prompt (atmósfera, estilo, materiales)
- **C** = Exploración de denoise (0.3, 0.5, 0.7, 0.9)

---

## Flujo de trabajo

```
CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────┤
    └──vae──────────────────┐   │
[CLIPTextEncode (pos)] ─────┤   │
[CLIPTextEncode (neg)] ─────┤   │
                            ▼   ▼
LoadImage ──► ImageScale ──► VAEEncode ──► KSampler ──► VAEDecode ──► SaveImage
              (512², crop)                 denoise < 1
```

- **Modelo:** `architecturerealmix_v11.safetensors` (~2 GB, SD 1.5)
- **Hardware actual:** AMD 8GB VRAM (DirectML)
- **Workflow:** [[workflow_img2img_croquis.json]]
- **Input sketches:** `inputs-croquis` — subí acá los croquis originales (luego copiar a `ComfyUI/input/croquis/`)
