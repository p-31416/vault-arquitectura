# Flujos por modelo — cadena de nodos y parámetros

> La receta que acompaña al prompt. Cada cadena está verificada contra la estructura de `reglas-workflows-comfy.md` (R1–R4) y contra lo que el stack del estudio tiene en disco.

## Comparativa rápida

| | SD 1.5 | SDXL | FLUX.1 | FLUX.2 klein 9B |
|---|---|---|---|---|
| Cargador | `CheckpointLoaderSimple` | `CheckpointLoaderSimple` | `UNETLoader` + `DualCLIPLoader` + `VAELoader` | `UNETLoader` + `CLIPLoader` + `VAELoader` |
| Text encoder | CLIP integrado | CLIP integrado | clip_l + t5xxl | qwen3-8b |
| Sampler | `KSampler` | `KSampler` | `KSampler` (cfg 1) | `SamplerCustomAdvanced` |
| Guía | `cfg` en KSampler | `cfg` en KSampler | `FluxGuidance` | `CFGGuider` |
| Sigmas | scheduler del KSampler | scheduler del KSampler | `BasicScheduler` | `Flux2Scheduler` |
| Negativo | texto | texto | `ConditioningZeroOut` | no aplica |
| Resolución | 512² | 1024² | 1024² | 1024² / 1,0 MP |
| Control | ControlNet | Union (RunPod) | Tools (Kontext/Canny/Depth) | `ReferenceLatent` |
| Corre en | local RX 570 | local justo / RunPod | RunPod | RunPod 24 GB |

## SD 1.5 — txt2img

```
CheckpointLoaderSimple
  ├─ MODEL ───────────────────────────────┐
  ├─ CLIP ─ CLIPTextEncode (+) ───────────┤
  └─ CLIP ─ CLIPTextEncode (−) ───────────┤
EmptyLatentImage (512×512) ───────────────┴→ KSampler → VAEDecode → SaveImage
```

| Widget | Valor |
|---|---|
| steps | 20–30 |
| cfg | 7–8 |
| sampler_name | `euler_ancestral` |
| scheduler | `karras` |
| denoise | 1,0 |
| batch_size | 1 |

## SD 1.5 — img2img / ControlNet

```
LoadImage → ImageScale (512×512, lanczos) → [CannyEdgeDetector] ─┐
                                                                  │
ControlNetLoader → ControlNetApplyAdvanced ← CLIPTextEncode (+) ──┤
                                                                  ┴→ KSampler (denoise 0,6–0,9) → VAEDecode → SaveImage
```

R1 del vault: el `ImageScale` a 512×512 va **siempre** antes del sampler cuando entra una imagen. Con dos ControlNet, dos `ControlNetApplyAdvanced` en serie.

## SDXL — txt2img

Misma cadena que SD 1.5. Cambian tres cosas: checkpoint, resolución y `cfg`.

| Widget | Valor |
|---|---|
| steps | 30–35 |
| cfg | 3–4 |
| sampler_name | `dpmpp_2m` |
| scheduler | `karras` |
| EmptyLatentImage | 1216×832 exterior · 832×1216 interior · 1024² aérea |

## FLUX.1 — txt2img

```
UNETLoader (flux1-dev)
DualCLIPLoader (clip_l, t5xxl)
VAELoader (ae.safetensors)
CLIPTextEncode (+) → FluxGuidance → ┐
ConditioningZeroOut ────────────────┤
EmptyLatentImage (1024×1024) ───────┴→ KSampler (cfg 1) → VAEDecode → SaveImage
```

| Widget | Valor |
|---|---|
| steps | 20–28 (dev) · 4 (schnell) |
| cfg | 1,0 |
| FluxGuidance | 2,5–3,5 |
| sampler_name | `euler` |
| scheduler | `simple` |

## FLUX.2 klein 9B — Rhino-to-Image

```
UNETLoader (flux2-klein-9b)
CLIPLoader (qwen3-8b)
VAELoader (flux2-vae)
LoadImage (geo_shaded.png)     → ImageScaleToTotalPixels (1.0 MP, lanczos) → VAEEncode ─┐
LoadImage (material.jpg)       → ImageScaleToTotalPixels (0.5 MP, lanczos) → VAEEncode ─┤
                                                                  ReferenceLatent ×2 ────┤
CLIPTextEncode (+) ─────────────────────────────────────────────────────────────────────┤
Flux2Scheduler ─────────────────────────────────────────────────────────────────────────┤
CFGGuider ──────────────────────────────────────────────────────────────────────────────┴→ SamplerCustomAdvanced → VAEDecode → ImageUpscaleWithModel → SaveImage
```

| Widget | Valor |
|---|---|
| steps | 4 (destilado) · 20 (base) |
| cfg | 1 (destilado) · 5 (base) |
| sampler | `euler` dentro de `SamplerCustomAdvanced` |
| LoRA strength | 0,0 / 0,6 / 0,8 / 1,0 (calibración de 4 corridas) |
| megapixels | 1,0 geometría · 0,5 material |

## LoRA — cómo se inserta

```
CheckpointLoaderSimple ─ MODEL ─→ LoraLoader ─ MODEL ─→ KSampler
                        └ CLIP ─→           ─ CLIP  ─→ CLIPTextEncode
```

El `CLIPTextEncode` cuelga de la salida **CLIP del LoRA**, no del checkpoint: así el texto también recibe el LoRA. El trigger va en el prompt, nunca el nombre del archivo.

| Base | Techo local | Nota |
|---|---|---|
| SD 1.5 | ≤250 MB | hasta 2 ControlNet |
| SDXL | ≤900 MB | Union no entra en 8 GB |
| FLUX.1 / FLUX.2 | — | RunPod |

## Video — LTX-2.3 imagen→video

```
LoadImage (render final) → LTX-2 base i2v → upscale latente ×2 → VHS_VideoCombine (MP4)
```

| Widget | Valor |
|---|---|
| strength | ~0,6 (1,0 congela) |
| duración | 4 s base, extensible a 10 s por etapas |
| control LoRAs | `ltx-2-19b-IC-LoRA-{Depth,Canny,Pose}-Control` |
| acelerador | `ltx-2-19b-distilled-lora-384` |

## Validación obligatoria (R4)

Antes de entregar o encolar:

```
comfyui_get_system_stats      → el servidor responde
comfyui_list_local_models     → checkpoint, VAE, text encoder y LoRA existen
comfyui_validate_workflow     → class_type y widgets contra /object_info
```

Lo que no esté instalado se reporta con su nombre exacto. Nunca se asume una ruta.

## Dónde corre cada cosa

| Escenario | Plataforma | Motivo |
|---|---|---|
| SD 1.5 concepto, ControlNet | local RX 570 | entra holgado |
| SDXL entrega | RunPod | Union + 1024² no caben con margen |
| FLUX.1 | RunPod | el T5 rompe la VRAM local |
| FLUX.2 klein 9B | RunPod 24 GB | ~24 GB de modelo |
| Video | RunPod | local no viable |

## Nomenclatura de salidas

`n_XX-{A–G}-{NN}.png` — A baseline · B prompt · C parámetros · D modelo · E resolución · F ControlNet/img2img · G LoRA. La corrida se registra en `02-WF-log-WF<nombre>.md` con seed, steps, cfg, sampler, scheduler, modelo, resolución, strength y tiempo.
