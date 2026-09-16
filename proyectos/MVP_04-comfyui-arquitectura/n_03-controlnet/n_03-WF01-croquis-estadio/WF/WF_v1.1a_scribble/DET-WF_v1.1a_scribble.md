---
tipo: registro-nodos
workflow: WF_v1.1a.0__scribble.json
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-07-19 22:30
tags: [registro, nodos, comfyui, controlnet, scribble]
---

# Registro de Nodos — Scribble (v1.1a)

Workflow: `WF_v1.1a.0__scribble.json`

## Objetivo del flujo

Renderizar un croquis arquitectónico a imagen fotorrealista usando **ControlNet Scribble**, alimentando el dibujo a mano alzada directamente como entrada — sin preprocesador de bordes. El modelo interpreta el trazo del arquitecto como "intención" y completa texturas, materiales, luces y contexto.

**Caso de uso:** Bocetos conceptuales tempranos donde se quiere explorar materialidad y atmósfera sin dibujar planos exactos.

## Pipeline

```
CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────┤
    └──vae──────────────────┐   │
                            │   │
LoadImage ──► ImageScale ───┤   │
               │            │   │
ControlNetLoader ──cn───────┤   │
               │            │   │
CLIPTextEncode (pos) ───────┤   │
CLIPTextEncode (neg) ───────┤   │
                            ▼   ▼
ControlNetApplyAdvanced ──► KSampler ──► VAEDecode ──► SaveImage
```

**Sin preprocesador** — El croquis se alimenta directo al ControlNet Scribble. No hay Canny, Depth ni ningún otro filtro intermedio.

## Detalle de nodos

### Carga del modelo base

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 1 | **CheckpointLoaderSimple** | `CheckpointLoaderSimple` | `architecturerealmix_v11.safetensors` | Carga el checkpoint SD 1.5 y lo descompone en 3 salidas: **MODEL** (difusión), **CLIP** (encoder de texto) y **VAE** (codificador/decodificador de imágenes ↔ latentes). El checkpoint define el estilo base, la calidad y el conocimiento visual del modelo. |

**Referencia:** [ComfyUI Docs — CheckpointLoaderSimple](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple)

---

### Entrada de imagen

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 2 | **LoadImage** | `LoadImage` | `croquis001.jpg` | Carga la imagen desde el directorio `input/` de ComfyUI. Convierte la imagen a tensor (formato `IMAGE` — batch de RGB) y extrae la máscara si existe (alpha channel). La imagen queda lista para ser procesada o redimensionada. |

**Referencia:** [ComfyUI Docs — LoadImage](https://docs.comfy.org/built-in-nodes/LoadImage)

---

### Preprocesamiento

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 3 | **ImageScale** | `ImageScale` | `upscale_method=lanczos`, `width=512`, `height=512`, `crop=center` | Redimensiona la imagen de entrada a 512×512 píxeles usando interpolación Lanczos (alta calidad). Si la imagen no es cuadrada, `crop=center` recorta el excedente desde el centro. La resolución debe coincidir con `EmptyLatentImage`. |

**Referencia:** [ComfyUI Docs — ImageScale](https://docs.comfy.org/built-in-nodes/ImageScale)

---

### ControlNet

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 4 | **ControlNetLoader** | `ControlNetLoader` | `control_v11p_sd15_scribble.safetensors` | Carga el modelo ControlNet Scribble desde `models/controlnet/`. Este modelo fue entrenado específicamente con garabatos y bocetos a mano alzada. A diferencia de Canny (bordes exactos), Scribble entiende trazos incompletos, líneas temblorosas y sombreados aproximados. |

**Referencia:** [ComfyUI Docs — ControlNetLoader](https://docs.comfy.org/built-in-nodes/ControlNetLoader)

---

### Texto (prompts)

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 5 | **CLIPTextEncode (pos)** | `CLIPTextEncode` | Prompt positivo: descripción del render deseado (ej: estadio, arquitectura, materiales) | Convierte el prompt textual en un embedding de condicionamiento usando el CLIP encoder del checkpoint. Este embedding guía al KSampler hacia el contenido descrito. El prompt positivo dice *qué queremos ver*. |
| 6 | **CLIPTextEncode (neg)** | `CLIPTextEncode` | Prompt negativo: artefactos a evitar (ej: texto, firmas, baja calidad, deformaciones) | Genera un embedding negativo: guía al KSampler para *alejarse* de lo descrito. Esencial para evitar distorsiones, duplicación de elementos, texto ilegible o calidad baja. |

**Referencia:** [ComfyUI Docs — CLIPTextEncode](https://docs.comfy.org/built-in-nodes/CLIPTextEncode)

---

### Latente inicial

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 7 | **EmptyLatentImage** | `EmptyLatentImage` | `width=512`, `height=512`, `batch_size=1` | Genera un tensor latente vacío (ruido puro) de 512×512 del cual el KSampler partirá para generar la imagen. Las dimensiones están en píxeles de imagen final, ComfyUI las convierte internamente a dimensiones de latente (64×64 para SD 1.5, factor de compresión 8). `batch_size=1` genera una sola imagen por corrida. |

**Referencia:** [ComfyUI Docs — EmptyLatentImage](https://docs.comfy.org/built-in-nodes/EmptyLatentImage)

---

### ControlNet Apply + Sampling

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 8 | **ControlNetApplyAdvanced** | `ControlNetApplyAdvanced` | `strength=1.0`, `start_percent=0`, `end_percent=1.0` | Aplica el ControlNet Scribble al condicionamiento positivo. **Strength=1.0** — el scribble domina completamente la composición. **end=1.0** — guía todo el denoising sin zona libre. Ajustado en v1.1a.2 tras v1.1a_02 donde strength 0.85 no logró que la composición del croquis (vista interior) se respetara frente al sesgo exterior del prompt en SD 1.5. |
| 9 | **KSampler** | `KSampler` | `steps=30`, `cfg=7`, `sampler_name=euler`, `scheduler=normal`, `seed=42` (o random) | Ejecuta el proceso de denoising: parte del latente vacío, aplica el condicionamiento (positivo + negativo + ControlNet) y genera el latente final. **steps=30**: iteraciones de refinamiento. **cfg=7**: balance creatividad-adherencia al prompt. **euler + normal**: sampler estable y versátil, buena calidad general. |

**Referencia KSampler:** [ComfyUI Docs — KSampler](https://docs.comfy.org/built-in-nodes/KSampler)
**Referencia ControlNetApplyAdvanced:** [ComfyUI Docs — ControlNetApplyAdvanced](https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced)

---

### Decodificación + salida

| ID | Nodo | Clase | Configuración | Qué hace |
|----|------|-------|--------------|----------|
| 10 | **VAEDecode** | `VAEDecode` | — | Decodifica el latente generado por el KSampler de vuelta a una imagen RGB mediante el VAE del checkpoint. El VAE "descomprime" el espacio latente (64×64×4) a píxeles (512×512×3). Es el paso inverso a la codificación que ocurriría en un img2img. |
| 11 | **SaveImage** | `SaveImage` | `prefix=n_03-v1.1a.2-scribble-` | Guarda la imagen decodificada en el directorio `output/` de ComfyUI con el prefijo de versión. Produce archivos como `n_03-v1.1a.2-scribble_00001_.png`, etc. PNG con metadatos incrustados (workflow, prompt, seed) para trazabilidad. |

**Referencia VAEDecode:** [ComfyUI Docs — VAEDecode](https://docs.comfy.org/built-in-nodes/VAEDecode)
**Referencia SaveImage:** [ComfyUI Docs — SaveImage](https://docs.comfy.org/built-in-nodes/SaveImage)

---

## Modelos utilizados

| Modelo | Tipo | Ruta en ComfyUI | Tamaño | Propósito |
|--------|------|----------------|--------|-----------|
| `architecturerealmix_v11.safetensors` | Checkpoint SD 1.5 | `models/checkpoints/` | 2.1 GB | Modelo base de difusión, especializado en arquitectura. Define el estilo, la calidad y el conocimiento visual general. |
| `control_v11p_sd15_scribble.safetensors` | ControlNet | `models/controlnet/` | ~689 MB | ControlNet entrenado con garabatos para guiar la forma desde bocetos a mano alzada. |

## Referencias externas

| Recurso | Enlace |
|---------|--------|
| ComfyUI Docs — CheckpointLoaderSimple | https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple |
| ComfyUI Docs — LoadImage | https://docs.comfy.org/built-in-nodes/LoadImage |
| ComfyUI Docs — ImageScale | https://docs.comfy.org/built-in-nodes/ImageScale |
| ComfyUI Docs — ControlNetLoader | https://docs.comfy.org/built-in-nodes/ControlNetLoader |
| ComfyUI Docs — CLIPTextEncode | https://docs.comfy.org/built-in-nodes/CLIPTextEncode |
| ComfyUI Docs — EmptyLatentImage | https://docs.comfy.org/built-in-nodes/EmptyLatentImage |
| ComfyUI Docs — ControlNetApplyAdvanced | https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced |
| ComfyUI Docs — KSampler | https://docs.comfy.org/built-in-nodes/KSampler |
| ComfyUI Docs — VAEDecode | https://docs.comfy.org/built-in-nodes/VAEDecode |
| ComfyUI Docs — SaveImage | https://docs.comfy.org/built-in-nodes/SaveImage |
| ComfyUI Docs — ControlNet Guide | https://docs.comfy.org/controlnet-guide |
| ControlNet Scribble Paper | https://arxiv.org/abs/2302.05543 |

→ [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1a_scribble/00-index|WF_v1.1a_scribble]] · [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1a_scribble/WF_v1.1a.0__scribble.json]] · [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1a_scribble/bug_log-WF_v1.1a_scribble]] · [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/index-n_03_WF01|n_03]]
