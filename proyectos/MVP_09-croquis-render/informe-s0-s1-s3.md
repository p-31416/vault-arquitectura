---
tipo: proyecto
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp_09, informe, croquis-render, pruebas, realvis]
idioma: es
---

# Informe S0–S1–S3 — croquis → render directo (2026-11-12)

> Flujos: [[proyectos/MVP_09-croquis-render/flujos/00-README|00-README]] · Batería: [[specs/261112-plan-pruebas-rumbo-miercoles|rumbo miércoles]] pruebas 2 y 5.
> Base única: RealVisXL v5.0 estándar, 1216×832, seed 42. Todo local $0, RX 570.

## La cadena (qué hace cada flujo)

- **S0** — `Checkpoint → LoRA sketch → prompt CROQUIS → KSampler txt2img (32 steps, cfg 4)` → croquis.
- **S1** — `LoadImage croquis → VAEEncode → prompt RENDER F0 → KSampler img2img (20 steps, cfg 4, denoise 0.55)` → intento de foto.
- **S3** — igual que S1 + `LoRA ArcvizXL 0.6` antes del sampler → intento de foto con estilo.
- **S2** — `croquis → mapa canny → ControlNet SDXL` → lock geométrico. ⛔ Gated: falta `ComfyUI-ControlNet-Aux` en el servidor.

## Pruebas y miniaturas

### S0-T1 — croquis marker ✅ (8 min)

`workflow_S0-croquis.json` · markerhandsketch 0.7 · seed 42. Misma familia que la keeper F0: dos volúmenes, pantallas de listones, vanos y patio legibles.

![[proyectos/MVP_09-croquis-render/flujos/salidas/casa-S0cro-v01-T1-marker.png]]

### S1-T1 — render directo ⚠️ quedó dibujo (6 min)

`workflow_S1-croquis-render.json` · denoise 0.55. La línea del croquis domina: sale foto-dibujo, no foto. Geometría respetada al 100% (vano por vano), pero no cruza a fotorrealismo.

![[proyectos/MVP_09-croquis-render/flujos/salidas/casa-S1ren-v01-T1-d055-quedo-dibujo.png]]

### S3-T1 — render + LoRA ⚠️ casi igual a S1 (6 min)

`workflow_S3-lora.json` · ArcvizXL 0.6, denoise 0.55. El LoRA a 0.6 casi no mueve la aguja frente a S1: confirma que el freno es el denoise, no el estilo.

![[proyectos/MVP_09-croquis-render/flujos/salidas/casa-S3lora-v01-T1-d055-quedo-dibujo.png]]

## Veredicto y próximo paso

Denoise 0.55 conserva geometría pero no alcanza la foto. Camino: **S1b con denoise 0.75** (a riesgo de inventar) o **S2 con ControlNet canny** (geometría exacta + foto real) — S2 requiere instalar el Aux (`s` de Sol).
