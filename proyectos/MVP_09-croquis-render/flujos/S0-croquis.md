---
tipo: flujo
mvp: 09
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp_09, S0, croquis, prompt, sketch, lora]
idioma: es
---

# S0 — prompt croquis (línea suelta, misma casa)

> JSON: `workflow_S0-croquis.json` (LoRA `markerhandsketch-V1` 0.7 + RealVis, 32 steps cfg 4 seed 42).
> El seed 42 es el mismo sorteo que la keeper F0: la volumetría sale de la misma familia.

## Positivo (croquis)

```text
architectural hand sketch, marker drawing, loose black ink lines on white paper,
modern single-family house, two concrete volumes, dark timber slat screen,
large glass openings, flat roof, small front patio with plants,
eye-level street view, sketchy construction drawing style, visible stroke texture
```

## Negativo (fijo)

```text
photo, photorealistic, render, 3d, color fill, blurry, watermark, text, cartoon, people, cars
```

## Pruebas S0 (una variable por prueba, seed 42 salvo T2)

| # | Cambio | Esperado | Salida |
|---|---|---|---|
| T1 | base + markerhandsketch 0.7 | croquis legible, vanos claros | `casa-S0cro-v01_00001_.png` |
| T2 | archisketch-v1 0.7 (cambiar `lora_name`) | otra mano, misma casa | comparar trazo |
| T3 | strength 0.5 | más RealVis, menos dibujo | si pierde línea, volver a 0.7 |

El croquis ganador alimenta S1/S2/S3 (copiar a `ComfyUI/input/`).
