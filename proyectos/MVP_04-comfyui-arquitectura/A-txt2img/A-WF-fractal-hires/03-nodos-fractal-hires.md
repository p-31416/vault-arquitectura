---
tipo: regla
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, fractal, hires, nodos]
---

# 03-nodos — configs propias de WF fractal hires

## Cadena (igual en las 3 variantes locales)

`CheckpointLoaderSimple → CLIPTextEncode ×2 → EmptyLatentImage 1344×768 → KSampler (denoise 1.0) → LatentUpscale ×1.5 → KSampler (denoise 0.35-0.4) → VAEDecode → SaveImage`

- **Por qué hires en latente y no en píxel**: la segunda pasada a 2016×1152 en píxel + VAEEncode no entra en 8 GB DirectML; en latente sí.
- **1344×768**: 16:9 del prompt original (`--ar 16:9`), múltiplos de 64.
- **Segunda seed 43** (fija): el ruido de detalle es reproducible; misma 43 en las 3 variantes.
- **Mismo sampler en las 3** (`dpmpp_2m/karras`): la variable bajo test es el checkpoint, no el sampler. Desvío documentado: el creador recomienda SDE para RealVisXL estándar — si el resultado sale lavado, T-H2b con `dpmpp_sde`.

## Por variante

| Variante | Base | Hires | Nota |
|---|---|---|---|
| Juggernaut | 30 steps, cfg 4 | 20 steps, denoise 0.35, cfg 4 | receta casa |
| RealVisXL V5 | 30 steps, cfg 4 | 20 steps, denoise 0.35, cfg 4 | dentro del rango del creador (30+) |
| Lightning | 6 steps, cfg 1.5 | 4 steps, denoise 0.4, cfg 1.5 | doc oficial: 4-6 steps, CFG 1-2 |
| Nano Banana | API `gemini-2.5-flash-image`, 16:9, seed 42 | — | bloqueado: login Comfy org |
