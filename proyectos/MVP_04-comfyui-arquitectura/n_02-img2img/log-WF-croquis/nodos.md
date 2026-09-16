---
tipo: registro-nodos
workflow: workflow_img2img_croquis.json
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-18
tags: [registro, nodos, comfyui, documentacion, img2img]
---

# Registro de Nodos — Workflow Croquis img2img

Lista completa de nodos utilizados en [[workflow_img2img_croquis.json]].

## Nodo 1: CheckpointLoaderSimple

| Propiedad | Valor |
|-----------|-------|
| **Clase** | CheckpointLoaderSimple |
| **Categoría** | model/loaders |
| **Función** | Carga un checkpoint de modelo de difusión (modelo base + CLIP + VAE) |
| **Input** | `ckpt_name` — nombre del archivo .safetensors en `models/checkpoints/` |
| **Outputs** | `MODEL`, `CLIP`, `VAE` |
| **Valor actual** | `architecturerealmix_v11.safetensors` |

**Documentación oficial:**
- [ComfyUI Docs — CheckpointLoaderSimple](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple)

---

## Nodo 2: CLIPTextEncode (Prompt Positivo)

| Propiedad | Valor |
|-----------|-------|
| **Clase** | CLIPTextEncode |
| **Categoría** | conditioning |
| **Función** | Codifica el prompt positivo en embeddings de conditioning |
| **Inputs** | `text`, `clip` |
| **Output** | `CONDITIONING` |
| **Valor actual** | prompt base (sketch a render) |

**Documentación oficial:**
- [ComfyUI Docs — CLIPTextEncode](https://docs.comfy.org/built-in-nodes/CLIPTextEncode)
- [CLIP Paper](https://arxiv.org/abs/2103.00020)

---

## Nodo 3: CLIPTextEncode (Prompt Negativo)

| Propiedad | Valor |
|-----------|-------|
| **Clase** | CLIPTextEncode |
| **Categoría** | conditioning |
| **Función** | Codifica el prompt negativo |
| **Inputs** | `text`, `clip` |
| **Output** | `CONDITIONING` |

---

## Nodo 4: LoadImage

| Propiedad | Valor |
|-----------|-------|
| **Clase** | LoadImage |
| **Categoría** | image |
| **Función** | Carga una imagen desde el directorio `input/` de ComfyUI |
| **Inputs** | `image` (nombre de archivo en input/), `RGBA` (bool) |
| **Output** | `IMAGE` — tensor de píxeles |
| **Valor actual** | `croquis/mi_sketch.png` (subcarpeta en ComfyUI `input/`) |

**Nota:** La imagen de entrada se busca en `ComfyUI/input/croquis/`. Antes de ejecutar, copiá tu sketch del vault (`inputs-croquis/`) a `ComfyUI/input/croquis/` con el mismo nombre que uses en el workflow.

**Documentación oficial:**
- [ComfyUI Docs — LoadImage](https://docs.comfy.org/built-in-nodes/LoadImage)

---

## Nodo 5: ImageScale

| Propiedad | Valor |
|-----------|-------|
| **Clase** | ImageScale |
| **Categoría** | image/transform |
| **Función** | Redimensiona la imagen de entrada a una resolución fija antes de codificarla, evitando OOM (out of memory) con imágenes grandes |
| **Inputs** | `image` (IMAGE), `upscale_method`, `width`, `height`, `crop` |
| **Output** | `IMAGE` — imagen redimensionada |
| **Valor actual** | `lanczos, 512×512, crop=center` |

**Nota:** Crítico en img2img para evitar OOM. Redimensiona cualquier imagen de entrada a 512×512 (resolución nativa SD 1.5, mínima VRAM). El `crop=center` preserva el centro del croquis, que suele ser el foco compositivo. Con crop se evita distorsión por stretching (`disabled`).

**Documentación oficial:**
- [ComfyUI Docs — ImageScale](https://docs.comfy.org/built-in-nodes/ImageScale)

---

## Nodo 6: VAEEncode

| Propiedad | Valor |
|-----------|-------|
| **Clase** | VAEEncode |
| **Categoría** | latent |
| **Función** | Codifica la imagen de píxeles al espacio latente (compresión 8x) para que el sampler la procese |
| **Inputs** | `pixels` (IMAGE), `vae` (VAE) |
| **Output** | `LATENT` — representación latente de la imagen de entrada |

**Nota:** Este nodo reemplaza a EmptyLatentImage en el pipeline img2img. En lugar de arrancar de ruido puro, arranca de la imagen codificada. El sampler luego aplica denoise parcial.

**Documentación oficial:**
- [ComfyUI Docs — VAEEncode](https://docs.comfy.org/built-in-nodes/VAEEncode)

---

## Nodo 6: KSampler

| Propiedad | Valor |
|-----------|-------|
| **Clase** | KSampler |
| **Categoría** | sampling |
| **Función** | Ejecuta el denoising sobre latentes. En img2img, el `denoise < 1` preserva estructura de la imagen original mientras aplica el prompt |
| **Inputs** | `model`, `positive`, `negative`, `latent_image`, `seed`, `steps`, `cfg`, `sampler_name`, `scheduler`, `denoise` |
| **Output** | `LATENT` |
| **Valores actuales** | `seed=42, steps=30, cfg=7, sampler=euler, scheduler=normal, denoise=0.7` |

### Parámetros clave para img2img

| Parámetro | Qué controla |
|-----------|-------------|
| **denoise** | **El más importante en img2img.** 0.3 = cambios sutiles, 0.7 = transformación fuerte, 0.9 = casi txt2img |
| **seed** | Define el ruido añadido. Misma seed + mismo denoise = misma textura aplicada |
| **steps** | Pasos de denoising. A menos denoise, menos steps necesarios |

**Documentación oficial:**
- [ComfyUI Docs — KSampler](https://docs.comfy.org/built-in-nodes/KSampler)
- [Karras Scheduler Paper](https://arxiv.org/abs/2206.00364)

---

## Nodo 7: VAEDecode

| Propiedad | Valor |
|-----------|-------|
| **Clase** | VAEDecode |
| **Categoría** | latent |
| **Función** | Decodifica los latentes denoised a imagen RGB visible |
| **Inputs** | `samples` (LATENT), `vae` (VAE) |
| **Output** | `IMAGE` |

**Documentación oficial:**
- [ComfyUI Docs — VAEDecode](https://docs.comfy.org/built-in-nodes/VAEDecode)

---

## Nodo 8: SaveImage

| Propiedad | Valor |
|-----------|-------|
| **Clase** | SaveImage |
| **Categoría** | image |
| **Función** | Guarda la imagen generada en `ComfyUI/output/` |
| **Inputs** | `images` (IMAGE), `filename_prefix` |
| **Output** | — |
| **Valor actual** | `filename_prefix=croquis_render` |

**Documentación oficial:**
- [ComfyUI Docs — SaveImage](https://docs.comfy.org/built-in-nodes/SaveImage)
