---
tipo: registro-nodos
workflow: WF_v1.1b.0__dual-canny-depth.json
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-07-19
tags: [registro, nodos, comfyui, controlnet, canny, depth, da3]
---

# Registro de Nodos — Dual Canny+Depth (v1.1b)

Workflow: `WF_v1.1b.0__dual-canny-depth.json`

## Objetivo del flujo

Renderizar un croquis arquitectónico a imagen fotorrealista combinando **dos ControlNet en paralelo**: Canny para los bordes/forma 2D y Depth (Depth Anything 3) para la estructura espacial 3D. Ambos condicionamientos se fusionan antes del KSampler para guiar simultáneamente composición y profundidad.

**Caso de uso:** Croquis donde importa tanto la silueta exacta del edificio como la relación espacial entre masas (volumetría, fondos, planos de profundidad).

## Pipeline

```
CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────┤
    └──vae──────────────────┐   │
                            │   │
LoadImage ──► ImageScale ──┬──► Canny ──► ControlNetApply (Canny) ──┐
               │           │                                        │
               │           └──► DA3Inference → DA3Render ──► ControlNetApply (Depth) ──┤
               │                                                                     ▼
CLIPTextEncode (pos) ──────────────────────────────────────────────────────────────────┤
CLIPTextEncode (neg) ──────────────────────────────────────────────────────────────────┤
                                                                                        ▼
                                                                                 KSampler ──► VAEDecode ──► SaveImage
```

Dos ControlNet en paralelo: Canny (bordes/forma) + Depth (volumen/profundidad). Ambos caben en 8GB VRAM con SD 1.5.

## Detalle de nodos

### Carga del modelo base

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 1 | **CheckpointLoaderSimple** | `CheckpointLoaderSimple` | `architecturerealmix_v11.safetensors` | Carga el checkpoint SD 1.5 y lo descompone en **MODEL** (difusión), **CLIP** (encoder de texto) y **VAE** (codificador/decodificador). El checkpoint arquitectura-realmix define el estilo base especializado en edificios y espacios. |

**Referencia:** [ComfyUI Docs — CheckpointLoaderSimple](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple)

---

### Entrada de imagen

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 2 | **LoadImage** | `LoadImage` | `croquis001.jpg` | Carga la imagen desde `input/` de ComfyUI y la convierte a tensor IMAGE (RGB batch + alpha mask). La imagen original se bifurca: una copia va a Canny (bordes) y otra a DA3 (profundidad). |

**Referencia:** [ComfyUI Docs — LoadImage](https://docs.comfy.org/built-in-nodes/LoadImage)

---

### Preprocesamiento

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 3 | **ImageScale** | `ImageScale` | `upscale_method=lanczos`, `width=512`, `height=512`, `crop=center` | Redimensiona el croquis de entrada a 512×512 (Lanczos, alta calidad). `crop=center` recorta el excedente si la imagen no es cuadrada. Esta imagen redimensionada alimenta tanto al Canny como al DA3. |

**Referencia:** [ComfyUI Docs — ImageScale](https://docs.comfy.org/built-in-nodes/ImageScale)

---

### Rama 1: Canny (bordes 2D)

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 4 | **Canny** | `Canny` | `low_threshold=0.31`, `high_threshold=0.59` | Aplica el detector de bordes Canny a la imagen. Los thresholds controlan la sensibilidad: `low=0.31` / `high=0.59` es un nivel medio-alto que captura líneas principales sin ruido fino. ⚠️ **Bug conocido:** Con DirectML el nodo Canny nativo produce bordes corruptos (kornia `F.pad` invierte ejes). Solucionado con workaround CPU (ver B-001 en bug_log). |
| 5 | **ControlNetLoader (Canny)** | `ControlNetLoader` | `control_v11p_sd15_canny.safetensors` | Carga el ControlNet Canny, entrenado para guiar la generación desde mapas de bordes. Este modelo responde bien a líneas nítidas y contornos definidos. |

**Referencia Canny:** [ComfyUI Docs — Canny](https://docs.comfy.org/built-in-nodes/Canny)
**Referencia ControlNetLoader:** [ComfyUI Docs — ControlNetLoader](https://docs.comfy.org/built-in-nodes/ControlNetLoader)

---

### Rama 2: Depth (profundidad 3D)

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 9 | **LoadDA3Model** | `LoadDA3Model` | `model_name=depth_anything_3_small.safetensors`, `dtype=fp16` | Carga el modelo Depth Anything 3 Small en precisión fp16 (ahorra VRAM). Este modelo de estimación de profundidad monocular infiere un mapa de profundidad desde una sola imagen 2D. |
| 10 | **DA3Inference** | `DA3Inference` | `res=504`, `mode=mono` | Ejecuta la inferencia de profundidad. **res=504**: resolución interna del análisis (cercano a 512×512 pero divisible por 12 como requiere DA3). **mode=mono**: vista única (no multiview). ⚠️ **Bug conocido:** Este nodo requiere seleccionar `mode` explícitamente en la UI, no tiene default (ver B-002 en bug_log). |
| 11 | **DA3Render** | `DA3Render` | `render_type=depth`, `normalization=v2_style` | Convierte el tensor de profundidad crudo del modelo en un mapa de profundidad visual usable por ControlNet Depth. `normalization=v2_style` normaliza usando el estilo v2 (mejor contraste de profundidad para arquitectura). |
| 6 | **ControlNetLoader (Depth)** | `ControlNetLoader` | `control_v11f1p_sd15_depth_fp16.safetensors` | Carga el ControlNet Depth, entrenado para guiar la generación desde mapas de profundidad. Responde a la estructura espacial: masas cercanas, lejanas, vacíos. |

**Referencia DA3:** https://github.com/DepthAnything/Depth-Anything-3

---

### Texto (prompts)

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 7 | **CLIPTextEncode (pos)** | `CLIPTextEncode` | Prompt positivo: estadio, arquitectura, materiales, atmósfera | Codifica el prompt positivo a embedding CLIP para guiar el estilo y contenido semántico del render. |
| 8 | **CLIPTextEncode (neg)** | `CLIPTextEncode` | Prompt negativo: texto, firmas, baja calidad, deformaciones | Codifica el prompt negativo para alejar la generación de artefactos no deseados. |

**Referencia:** [ComfyUI Docs — CLIPTextEncode](https://docs.comfy.org/built-in-nodes/CLIPTextEncode)

---

### Latente inicial

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 14 | **EmptyLatentImage** | `EmptyLatentImage` | `width=512`, `height=512`, `batch_size=1` | Crea el latente vacío (ruido puro) de 512×512 desde el cual el KSampler comienza a generar. |

**Referencia:** [ComfyUI Docs — EmptyLatentImage](https://docs.comfy.org/built-in-nodes/EmptyLatentImage)

---

### ControlNet Apply + Sampling

| ID  | Nodo                        | Clase                     | Configuración                                                                       | Qué hace                                                                                                                                                                                                                                                                       |
| --- | --------------------------- | ------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 12  | **ControlNetApply (Canny)** | `ControlNetApplyAdvanced` | `strength=0.3`, `start_percent=0`, `end_percent=1.0`                                | Aplica el ControlNet Canny al condicionamiento. **Strength bajo (0.3):** los bordes Canny actúan como guía suave de composición — suficiente para mantener la forma sin cortar líneas (problema detectado en v1.0.x con strength alto). Actúa durante todo el proceso (0–1.0). |
| 13  | **ControlNetApply (Depth)** | `ControlNetApplyAdvanced` | `strength=1.0`, `start_percent=0`, `end_percent=1.0`                                | Aplica el ControlNet Depth al condicionamiento. **Strength alto (1.0):** la profundidad es crítica para la estructura espacial, se aplica con máxima intensidad durante todo el proceso.                                                                                       |
| 15  | **KSampler**                | `KSampler`                | `steps=30`, `cfg=7`, `sampler_name=euler`, `scheduler=normal`, `seed=42` (o random) | Ejecuta el denoising fusionando ambos condicionamientos (Canny + Depth + texto). steps=30, cfg=7, euler+normal son valores estables probados en v1.0.x.                                                                                                                        |

**Referencia KSampler:** [ComfyUI Docs — KSampler](https://docs.comfy.org/built-in-nodes/KSampler)
**Referencia ControlNetApplyAdvanced:** [ComfyUI Docs — ControlNetApplyAdvanced](https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced)

---

### Decodificación + salida

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 16 | **VAEDecode** | `VAEDecode` | — | Decodifica el latente final a imagen RGB mediante el VAE del checkpoint. |
| 17 | **SaveImage** | `SaveImage` | `prefix=n_03-v1.1b-dual-` | Guarda la imagen en `output/` con el prefijo de versión. Produce archivos como `n_03-v1.1b-dual_00001_.png`, `n_03-v1.1b-dual_00002_.png`, etc. Metadatos de workflow incrustados. |

**Referencia VAEDecode:** [ComfyUI Docs — VAEDecode](https://docs.comfy.org/built-in-nodes/VAEDecode)
**Referencia SaveImage:** [ComfyUI Docs — SaveImage](https://docs.comfy.org/built-in-nodes/SaveImage)

---

## Modelos utilizados

| Modelo | Tipo | Ruta en ComfyUI | Tamaño | Propósito |
|--------|------|----------------|--------|-----------|
| `architecturerealmix_v11.safetensors` | Checkpoint SD 1.5 | `models/checkpoints/` | 2.1 GB | Modelo base de difusión especializado en arquitectura. |
| `control_v11p_sd15_canny.safetensors` | ControlNet | `models/controlnet/` | ~689 MB | ControlNet Canny para guía por bordes 2D (líneas, contornos, siluetas). |
| `control_v11f1p_sd15_depth_fp16.safetensors` | ControlNet | `models/controlnet/` | 689 MB | ControlNet Depth para guía por profundidad 3D (planos espaciales, masas). |
| `depth_anything_3_small.safetensors` | Depth estimator | `models/geometry_estimation/` | 131 MB | Modelo de estimación de profundidad monocular (Depth Anything 3 Small). |

## Parámetros clave

| ControlNet | Strength | start | end | Rol |
|-----------|----------|-------|-----|-----|
| Canny | 0.3 | 0.0 | 1.0 | Bordes suaves como guía de composición (bajo para evitar líneas cortadas) |
| Depth | 1.0 | 0.0 | 1.0 | Estructura espacial 3D, masas, profundidad |

## Referencias externas

| Recurso | Enlace |
|---------|--------|
| ComfyUI Docs — CheckpointLoaderSimple | https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple |
| ComfyUI Docs — LoadImage | https://docs.comfy.org/built-in-nodes/LoadImage |
| ComfyUI Docs — ImageScale | https://docs.comfy.org/built-in-nodes/ImageScale |
| ComfyUI Docs — Canny | https://docs.comfy.org/built-in-nodes/Canny |
| ComfyUI Docs — ControlNetLoader | https://docs.comfy.org/built-in-nodes/ControlNetLoader |
| ComfyUI Docs — CLIPTextEncode | https://docs.comfy.org/built-in-nodes/CLIPTextEncode |
| ComfyUI Docs — EmptyLatentImage | https://docs.comfy.org/built-in-nodes/EmptyLatentImage |
| ComfyUI Docs — ControlNetApplyAdvanced | https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced |
| ComfyUI Docs — KSampler | https://docs.comfy.org/built-in-nodes/KSampler |
| ComfyUI Docs — VAEDecode | https://docs.comfy.org/built-in-nodes/VAEDecode |
| ComfyUI Docs — SaveImage | https://docs.comfy.org/built-in-nodes/SaveImage |
| ComfyUI Docs — ControlNet Guide | https://docs.comfy.org/controlnet-guide |
| Depth Anything 3 — GitHub | https://github.com/DepthAnything/Depth-Anything-3 |
| ControlNet Paper | https://arxiv.org/abs/2302.05543 |

→ [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/00-index|WF_v1.1b_dual]] · [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/WF_v1.1b.0__dual-canny-depth.json]] · [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/bug_log-WF_v1.1b_dual]] · [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/index-n_03_WF01|n_03]]
