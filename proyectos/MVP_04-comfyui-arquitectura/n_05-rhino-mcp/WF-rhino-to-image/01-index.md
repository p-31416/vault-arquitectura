---
tipo: indice
mvp: 04
nivel: n_05
wf: WF-rhino-to-image
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_04, comfyui, workflow, flux2, klein, lora, gaudi]
---

# WF-rhino-to-image — índice de versiones

## Versiones

| Versión | Fecha | Cambio | Archivo |
|---------|-------|--------|---------|
| v1.0.0 | 2026-10-20 | Grafo inicial: FLUX.2 klein 9B + LoRA rhino-to-image + doble referencia (geometría + material) | `workflow_rhino_to_image.json` |

## Config mínima

| Nodo | Valor |
|------|-------|
| `UNETLoader.unet_name` | `flux-2-klein-9b-fp8.safetensors` (o GGUF Q4 con `UnetLoaderGGUF`) |
| `UNETLoader.weight_dtype` | `default` |
| `CLIPLoader.clip_name` | `qwen_3_8b_fp8mixed.safetensors` |
| `CLIPLoader.type` | `flux2` (obligatorio) |
| `VAELoader.vae_name` | `full_encoder_small_decoder.safetensors` |
| `LoraLoaderModelOnly.lora_name` | `rhino-to-image-lora.basic.safetensors` |
| `LoraLoaderModelOnly.strength_model` | 0,6 → 0,8 → 1,0 |
| `ImageScaleToTotalPixels` (geometría) | `lanczos`, 1,0 MP |
| `ImageScaleToTotalPixels` (material) | `lanczos`, 0,5 MP |
| `ReferenceLatent` ×2 | geometría → material |
| `FluxKontextMultiReferenceLatentMethod.reference_latents_method` | `index` |
| `Flux2Scheduler.steps` | 4 (destilado) · 20 (base) |
| `Flux2Scheduler.width / height` | 1024 / 1024 (idéntico a `EmptyFlux2LatentImage`) |
| `CFGGuider.cfg` | 1,0 (destilado) · 5,0 (base) |
| `KSamplerSelect.sampler_name` | `euler` |
| `RandomNoise.noise_seed` | 42 (fijo para las corridas comparables) |

## Precondiciones

| Recurso | Ubicación | Estado |
|---------|-----------|--------|
| Transformer | `models/diffusion_models/flux-2-klein-9b-fp8.safetensors` | ⬜ |
| Text encoder | `models/text_encoders/qwen_3_8b_fp8mixed.safetensors` | ⬜ |
| VAE | `models/vae/full_encoder_small_decoder.safetensors` | ⬜ |
| LoRA | `models/loras/rhino-to-image-lora.basic.safetensors` | ⬜ (origen: `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\`) |
| Referencia geometría | `input/geo_shaded.png` | ⬜ |
| Referencia material | `input/material.jpg` | ⬜ |

## Entradas y salidas

- **Entradas**: 2 imágenes (`geo_shaded.png`, `material.jpg`), 1 prompt JSON, 1 seed.
- **Salida**: 1 imagen PNG 1024×1024 en `output/` + copia en `salidas/`.

## Relación con otros flujos

- Predecesor conceptual: [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio|n_03-WF01-croquis-estadio]] (control geométrico por bordes, SD1.5).
- Sucesor natural: moodboard y láminas del concurso (nivel n_06).
