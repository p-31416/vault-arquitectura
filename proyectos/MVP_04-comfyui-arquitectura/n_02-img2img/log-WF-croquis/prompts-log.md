---
tipo: registro-prompts-log
workflow: workflow_img2img_croquis.json
nivel: n_02-img2img
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-18
tags: [registro, prompts, log, versiones, croquis]
---

# Prompts Log — n_02-img2img (Croquis)

Cada corrida se registra como `n_02-{L}-{nn}`. Las imágenes están en `salidas`.

- **A** = Baseline — denoise fijo, prompt base, mismo croquis de entrada
- **B** = Variación de prompt (atmósfera, estilo, materiales)
- **C** = Exploración de denoise (0.3 → 0.9)

Más nuevo → más arriba. [[index]] para vista general de variantes.

## Prompts base

Salvo que se indique otra cosa.

**Positivo:**
```
architecturerealmix style, architectural sketch to render, photorealistic,
high quality, detailed, professional architectural visualization
```

**Negativo:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch lines, deformed, poor design
```

---

## Log

### `n_02-A-01` | 2026-07-18 | ~?

**Cambio:** Baseline img2img — primer render desde croquis (croquis001.jpg). denoise=0.7, prompt base.

**Prompt positivo usado:**
```
architecturerealmix style, architectural sketch to render, photorealistic,
high quality, detailed, professional architectural visualization
```

| Parámetro | Valor |
|-----------|-------|
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 (ImageScale center crop) |
| seed | 42 |
| denoise | 0.7 |
| input | `croquis001.jpg` (186KB, ~1600×1350→512×512) |
| tiempo | ~74s (AMD DirectML) |

![n_02-A-01](salidas/n_02-A-01.png)

**Evaluación:** _(no pude inspeccionar visualmente)_ Primer img2img exitoso. Sin error de VRAM gracias a ImageScale. Croquis original se redimensionó de ~1600×1350 a 512×512 center crop.

**Sugerencias → [[backlog]]:**
- Probar distintos valores de denoise (0.3, 0.5, 0.9)
- Probar con prompt más descriptivo del sketch
- Probar scheduler karras para + contraste

**Referencias:** [[nodos]], [[index]], [[modelos-recomendados]]
