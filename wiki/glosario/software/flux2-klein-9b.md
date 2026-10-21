---
tipo: software
software: flux2-klein-9b
categoria: diffusion_model
familia: flux2
base_model: flux2-klein-9b
archivo: flux-2-klein-9b-fp8.safetensors
licencia: FLUX Non-Commercial (9B) | Apache 2.0 (4B)
estado: pendiente de descarga (runpod / PC segun VRAM)
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [glosario, software, comfyui, flux2, klein, qwen3, vae, fotorrealismo, arquitectura, cloud]
---

# FLUX.2 [klein] 9B

> Modelo de imagen de Black Forest Labs: un DiT de 9B params, unificado para generación y edición multi-referencia, destilado a 4 pasos de inferencia. Es la base del LoRA «Rhino-to-Image» del curso AI×Gaudí y el motor de render del concurso. No corre en la RX 570 de 8 GB: la ruta es **RunPod 24 GB** (~$0,22/h).

- [[#Qué es]]
- [[#Arquitectura]]
- [[#Stack de instalación]]
- [[#Grafo de referencia]]
- [[#Parámetros de inferencia]]
- [[#Rendimiento y coste]]
- [[#Licencia]]
- [[#Variantes]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Qué es

| Campo | Valor |
|-------|-------|
| **Familia** | FLUX.2 (sucesor de FLUX.1) |
| **Variante** | klein 9B — flagship chico, destilado a 4 pasos |
| **Parámetros** | 9.078.581.248 (GGUF `total`) |
| **Licencia** | FLUX Non-Commercial License (la 4B es Apache 2.0) |
| **Texto** | Qwen3-8B embebido (`joint_attention_dim` 12288 = 3 × 4096) |
| **Latente** | 128 canales (VAE de 32 ch con unpatchify 2×), patch 1, down factor 16 |
| **Resolución de trabajo** | 1024×1024 / 1024×768 / 768×1024 |
| **Pasos de inferencia** | 4 (destilado) · 20 (variante base) |
| **VRAM** | ~29 GB (bf16) · ~9,4 GB (fp8) · ~5,7 GB (GGUF Q4) + text encoder |
| **Estado en el vault** | ⬜ Pendiente (no instalado) |

Es el modelo que el curso AI×Gaudí usa para el módulo «Rhino-to-Image» y para los entregables del concurso «The Gaudí Nexus».

---

## Arquitectura

Verificada contra `Klein9BParams` en `black-forest-labs/flux2` (`src/flux2/model.py`) y contra la configuración `image_model: "flux2"` de `comfy/model_detection.py:238`:

| Parámetro | klein 9B | klein 4B | FLUX.2 [dev] |
|-----------|----------|----------|--------------|
| `hidden_size` | 4096 | 3072 | 6144 |
| `num_heads` | 32 | 24 | 48 |
| Bloques duales (`double_blocks`) | 8 | 5 | 8 |
| Bloques simples (`single_blocks`) | 24 | 20 | 48 |
| `mlp_ratio` | 3,0 | 3,0 | 3,0 |
| `axes_dim` (RoPE) | [32,32,32,32] | [32,32,32,32] | [32,32,32,32] |
| `theta` | 2000 | 2000 | 2000 |
| `in_channels` / `out_channels` | 128 | 128 | 128 |
| `context_in_dim` | 12288 | 7680 | 15360 |
| `guidance_embed` | no | no | sí |

Puntos que explican el comportamiento en la práctica:

- **`global_modulation`**: la modulación es global y compartida (`double_stream_modulation_img/txt.lin`, `single_stream_modulation.lin`), no por bloque.
- **`mlp_silu_act`**: el MLP de los bloques simples concatena dos mitades (gate/up), por eso `linear1` = 3·hidden + 2·mlp_hidden.
- **Sin `guidance_in`**: klein no usa embedding de guidance; la escala se controla con `CFGGuider`.
- **Patch 1**: el latent de 128 canales entra directo, sin patchify, y el VAE trabaja a down factor 16.

### Mecanismo de referencia (el "bloqueo" de geometría)

FLUX.2 no usa ControlNet oficial: la imagen de referencia entra como **latent de referencia** al conditioning:

```
ReferenceLatent(conditioning, latent)  →  conditioning con "reference_latents"
FluxKontextMultiReferenceLatentMethod(reference_latents_method = "index" | "offset" | "uxo/uno" | "index_timestep_zero")
```

El método `index` reparte los tokens de referencia en su propia banda posicional (`ref_index_scale = 10.0` en `comfy/model_detection.py:248`), de modo que la geometría y el material se conservan en su sitio mientras el modelo genera el resto.

---

## Stack de instalación

Tres archivos, tres carpetas. El text encoder es la pieza forgotten: sin él el grafo no corre.

| Componente | Archivo | Carpeta en ComfyUI | Tamaño |
|------------|---------|---------------------|--------|
| Transformer (DiT) | `flux-2-klein-9b-fp8.safetensors` (`black-forest-labs/FLUX.2-klein-9b-fp8`) | `models/diffusion_models/` | ~9,4 GB |
| Text encoder | `qwen_3_8b_fp8mixed.safetensors` (`Comfy-Org/vae-text-encorder-for-flux-klein-9B`, carpeta `split_files/text_encoders/`) | `models/text_encoders/` | 8,66 GB |
| VAE | `full_encoder_small_decoder.safetensors` (`black-forest-labs/FLUX.2-small-decoder`) | `models/vae/` | 238 MB |
| LoRA del curso | `rhino-to-image-lora.basic.safetensors` | `models/loras/` | 120,8 MB |

### Comandos (RunPod, imagen con ComfyUI)

```bash
hf auth login
hf download black-forest-labs/FLUX.2-klein-9b-fp8 flux-2-klein-9b-fp8.safetensors --local-dir /workspace/ComfyUI/models/diffusion_models
hf download Comfy-Org/vae-text-encorder-for-flux-klein-9B split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors --local-dir /workspace/ComfyUI/models/text_encoders
hf download black-forest-labs/FLUX.2-small-decoder full_encoder_small_decoder.safetensors --local-dir /workspace/ComfyUI/models/vae
```

Los repos de BFL son *gated*: hay que aceptar la licencia en la página del modelo antes de la descarga.

### GGUF para VRAM chica

`unsloth/FLUX.2-klein-9B-GGUF` ofrece Q4_K (~5,7 GB), Q5_K, Q6_K y Q8_0 con upcast selectivo. Requiere el pack `ComfyUI-GGUF` y el nodo `UnetLoaderGGUF`; el LoRA rank 16 se aplica igual sobre el modelo cuantizado.

> En la PC de Emilia (8 GB) el cuello de botella es el **text encoder de 8,7 GB**, que va a RAM con offload. El flujo completo local es viable en calidad y muy lento; la ruta de producción es cloud.

### Arranque en la PC local (DirectML)

```cmd
P:\Anaconda\envs\comfyenv\python.exe -s ComfyUI\main.py --directml --disable-dynamic-vram --reserve-vram 1.0
```

`--lowvram` no aporta nada con DirectML: `comfy/model_management.py:121` fuerza `lowvram_available = False` cuando la pantalla es DirectML.

---

## Grafo de referencia

```
UNETLoader (flux-2-klein-9b-fp8)
   └─► LoraLoaderModelOnly (rhino-to-image, 0.8) ──► CFGGuider ──► SamplerCustomAdvanced
CLIPLoader (type=flux2, qwen_3_8b_fp8mixed)
   ├─► CLIPTextEncode (positivo) ──► ReferenceLatent (geo) ──► ReferenceLatent (material) ──► CFGGuider.positive
   └─► CLIPTextEncode (negativo) ──────────────────────────────────────────────────────────────► CFGGuider.negative
VAELoader (full_encoder_small_decoder)
   ├─► VAEEncode (geo) ──► ReferenceLatent
   ├─► VAEEncode (material) ──► ReferenceLatent
   └─► VAEDecode ──► SaveImage
EmptyFlux2LatentImage (1024×1024) ──► SamplerCustomAdvanced.latent_image
Flux2Scheduler (steps=4, width=1024, height=1024) ──► SamplerCustomAdvanced.scheduler
KSamplerSelect (euler) ──► SamplerCustomAdvanced.sampler_name
```

Detalles que importan:

- `CLIPLoader` con `type: "flux2"` es obligatorio: es lo que selecciona el tokenizador Qwen3 y la clave de embedding `qwen3_8b`.
- El sampler es **`SamplerCustomAdvanced`** (no `KSampler`): FLUX.2 usa sigmas calculadas por `Flux2Scheduler`, que necesita el `width`/`height` final para el largo de secuencia.
- `Flux2Scheduler` y `EmptyFlux2LatentImage` deben compartir resolución: el scheduler calcula `seq_len` a partir de ella.
- `FluxKVCache` es experimental y optimiza el uso de referencias repetidas en pasos múltiples; se deja fuera del flujo base por stability.

Workflow listo para importar: [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/workflow_rhino_to_image.json|workflow_rhino_to_image.json]].

---

## Parámetros de inferencia

| Parámetro | klein 9B (destilado) | klein base 9B | 4B (destilado) |
|-----------|----------------------|---------------|----------------|
| steps | 4 | 20 | 4 |
| cfg (`CFGGuider`) | 1,0 | 5,0 | 1,0 |
| sampler | euler | euler | euler |
| scheduler | `Flux2Scheduler` | `Flux2Scheduler` | `Flux2Scheduler` |
| resolución | 1024×1024 | 1024×1024 | 1024×1024 |
| LoRA strength | 0,6-1,0 | 0,6-1,0 | 0,6-1,0 |

Prompt: FLUX.2 responde mejor a frases completas y estructuradas (el curso recomienda **JSON**). Ejemplo de caption de trabajo:

```json
{"subject": "volumetric study of a brick hyperbolic paraboloid pavilion",
 "material": "handmade brick, rough mortar joints",
 "lighting": "late afternoon sun, hard shadows, warm bounce",
 "view": "three quarter exterior, eye level, 24mm",
 "style": "architectural photography, raw photo, high detail"}
```

Negative: cadena vacía o mínima (Flux.2 no penaliza con negative largo).

---

## Rendimiento y coste

| Entorno | Throughput orientativo | Coste |
|----------|------------------------|-------|
| RunPod RTX 3090 24 GB | ~8-12 s/imagen (4 pasos, 1024²) | $0,22/h |
| RunPod RTX 4090 24 GB | ~5-8 s/imagen | $0,34/h |
| Local RX 570 8 GB + DirectML | minutos por imagen (offload del text encoder a RAM) | $0 (energía) |
| BFL API | segundos | por imagen, créditos de API |

Coste del concurso completo (20-40 imágenes finales + iteraciones): **$2-5**.

---

## Licencia

| Variante | Licencia | Uso comercial |
|----------|----------|----------------|
| FLUX.2 [klein] 4B | Apache 2.0 | Sí, con atribución |
| FLUX.2 [klein] 9B | FLUX Non-Commercial License | A confirmar con BFL |
| FLUX.2 [dev] 32B | FLUX Non-Commercial License | A confirmar con BFL |

La diferencia no es menor: **el LoRA del curso está afinado sobre la 9B**, de modo que para trabajo de cliente el camino es 4B + LoRA reentrenado (o licencia comercial de BFL). El portado de LoRA entre 9B y 4B no es viable por arquitectura.

Uso personal, investigación y desarrollo están contemplados en la FLUX Non-Commercial License; los outputs tienen un régimen distinto del de los pesos, que hay que leer en el texto de licencia vigente.

---

## Variantes

| Variante | Parámetros | VRAM (fp8) | Licencia | Nota |
|----------|-----------|------------|----------|------|
| `FLUX.2-klein-9B` | 9 B | 9,4 GB | Non-Commercial | Destilado 4 pasos. La del curso |
| `FLUX.2-klein-base-9B` | 9 B | 9,4 GB | Non-Commercial | Sin destilar: 20 pasos, mejor control |
| `FLUX.2-klein-4B` | 4 B | ~5 GB | Apache 2.0 | La opción comercial |
| `FLUX.2-klein-base-4B` | 4 B | ~5 GB | Apache 2.0 | Base de entrenamiento |
| `FLUX.2 [dev]` | 32 B | 24 GB (fp8) | Non-Commercial | Calidad máxima, 32 GB+ de VRAM |

---

## Conceptos relacionados

- [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]] — LoRA afinado sobre este modelo
- [[wiki/glosario/software/comfyui|comfyui]] — nodos y catálogo de modelos del estudio
- [[wiki/glosario/software/rhino|rhino]] — origen de las volumetrías de referencia
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — playbook operativo
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/00-README|WF-rhino-to-image]] — workflow «Rhino-to-Image»
- [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|research 2026-10-20]] — informe con 54 fuentes

## Referencias

- [black-forest-labs/FLUX.2-klein-9B (HF)](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B) (verificado 2026-10-20)
- [black-forest-labs/FLUX.2-klein-4B (HF)](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) (verificado 2026-10-20 — Apache 2.0)
- [black-forest-labs/FLUX.2-dev (HF)](https://huggingface.co/black-forest-labs/FLUX.2-dev) (verificado 2026-10-20 — gated)
- [black-forest-labs/flux2 (GitHub — implementación de referencia)](https://github.com/black-forest-labs/flux2) (verificado 2026-10-20 — `src/flux2/model.py`)
- [Comfy-Org/vae-text-encorder-for-flux-klein-9B (HF)](https://huggingface.co/Comfy-Org/vae-text-encorder-for-flux-klein-9B) (verificado 2026-10-20 — text encoder + VAE)
- [black-forest-labs/FLUX.2-small-decoder (HF)](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder) (verificado 2026-10-20)
- [unsloth/FLUX.2-klein-9B-GGUF (HF)](https://huggingface.co/unsloth/FLUX.2-klein-9B-GGUF) (verificado 2026-10-20)
- [ComfyUI Docs — FLUX.2 Klein](https://docs.comfy.org/tutorials/flux/flux-2-klein) (verificado 2026-10-20)
- [ComfyUI Blog — FLUX.2 Day-0 Support](https://blog.comfy.org/p/flux2-state-of-the-art-visual-intelligence) (verificado 2026-10-20)
- [city96/ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) (verificado 2026-10-20)
- [FLUX Non-Commercial License (texto)](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B/blob/main/LICENSE.txt) (verificado 2026-10-20)
