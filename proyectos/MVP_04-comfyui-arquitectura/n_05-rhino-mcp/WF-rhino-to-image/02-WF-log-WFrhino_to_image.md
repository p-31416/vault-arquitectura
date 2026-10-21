---
tipo: log
mvp: 04
nivel: n_05
wf: WF-rhino-to-image
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_04, comfyui, workflow, log, flux2, klein, lora]
---

# WF-rhino-to-image — log de corridas

Más nuevo → más arriba

## 2026-10-20 — Preparación del flujo (sin corrida todavía)

- **Análisis del LoRA**: `rhino-to-image-lora.basic.safetensors` identificado como LoRA rank 16 sobre FLUX.2 [klein] 9B (176 tensores, 31,66 M params, F32, 120,8 MB). Matrices B no nulas (σ ≈ 1e-3): delta entrenado y sano. Detalle en [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]].
- **Investigación**: [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|research 2026-10-20]] (54 fuentes verificadas).
- **Construcción del grafo** contra el código de ComfyUI local (`b08e6cf3`): `UNETLoader` (input `weight_dtype`, no `weight_name`), `CLIPLoader(type=flux2)`, `LoraLoaderModelOnly`, doble `ReferenceLatent`, `FluxKontextMultiReferenceLatentMethod(index)`, `CFGGuider`, `Flux2Scheduler`, `KSamplerSelect(euler)`, `RandomNoise` y `SamplerCustomAdvanced` con el esquema nuevo (`noise`/`guider`/`sampler`/`sigmas`/`latent_image`).
- **Pendiente**: stack de modelos en RunPod, copia del LoRA, exportación de referencias desde Rhino, trigger word del instructor, y la primera corrida comparativa A/B/C/D.

### Tabla de corridas

| Corrida | Fecha | Seed | LoRA strength | steps/cfg | Referencia material | Archivo | Nota |
|---------|-------|------|---------------|-----------|--------------------|--------|------|
| — | — | — | — | — | — | — | Flow preparado, sin corrida registrada |
