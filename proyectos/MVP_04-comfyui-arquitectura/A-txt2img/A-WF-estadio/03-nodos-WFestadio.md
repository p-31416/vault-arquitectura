---
tipo: nodos
workflow: WF-estadio
nivel: n_01-txt2img
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-24
tags: [nodos, sdxl, sd15, estadio, juggernaut, architecture-realmix]
---

# 03-nodos — Configuración Propia WF-estadio

**Solo configs específicas de este flujo.**  
Lo genérico (qué hace cada nodo, inputs estándar) → [[wiki/glosario/software/comfyui]].

---

## Flujo SD 1.5 — ArchitectureRealmix v1.1

### 1. CheckpointLoaderSimple (nodo 1)

| Input | Valor | Nota |
|-------|-------|------|
| `ckpt_name` | `architecturerealmix_v11.safetensors` | SD 1.5, 2.1 GB, VAE incluido |

> **Outputs:** `MODEL` (0), `CLIP` (1), `VAE` (2)

---

### 2. CLIPTextEncode Positive (nodo 2)

| Input | Valor |
|-------|-------|
| `text` | *ver `01-index.md` Prompts base SD 1.5* |
| `clip` | `["1", 1]` |

> **Trigger words ArchitectureRealmix:** `architecturerealmix style`, `architectural photography`, `8K`, `photorealistic`

---

### 3. CLIPTextEncode Negative (nodo 3)

| Input | Valor |
|-------|-------|
| `text` | *ver `01-index.md` Prompts base SD 1.5* |
| `clip` | `["1", 1]` |

---

### 4. EmptyLatentImage (nodo 4)

| Input | Valor | Nota |
|-------|-------|------|
| `width` | 768 | 3:2 landscape |
| `height` | 512 | |
| `batch_size` | 1 | VRAM 8GB |

> Latentes: 768×512 px → 96×64 latentes (compresión 8× SD 1.5)

---

### 5. KSampler (nodo 5) — **Config SD 1.5**

| Input | Valor | Justificación |
|-------|-------|---------------|
| `model` | `["1", 0]` | Del checkpoint |
| `positive` | `["2", 0]` | CLIP encode pos |
| `negative` | `["3", 0]` | CLIP encode neg |
| `latent_image` | `["4", 0]` | Empty latent |
| `seed` | 42 | Baseline fijo |
| `steps` | 30 | Estándar SD 1.5 |
| `cfg` | 7 | SD 1.5 rango 6-8 |
| `sampler_name` | `euler` | Simple, rápido |
| `scheduler` | `normal` | Estándar |
| `denoise` | 1.0 | txt2img puro |

---

### 6. VAEDecode (nodo 6)

| Input | Valor |
|-------|-------|
| `samples` | `["5", 0]` |
| `vae` | `["1", 2]` | VAE del checkpoint |

---

### 7. SaveImage (nodo 7)

| Input | Valor |
|-------|-------|
| `filename_prefix` | `estadio_futbol` |
| `images` | `["6", 0]` |

> Output: `estadio_futbol_XXXXX_.png`

---

## Flujo SDXL — Juggernaut XL v9

### 1. CheckpointLoaderSimple (nodo 1)

| Input | Valor | Nota |
|-------|-------|------|
| `ckpt_name` | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | SDXL, 7.11 GB, **VAE embebido** |

---

### 2. CLIPTextEncode Positive (nodo 2)

| Input | Valor |
|-------|-------|
| `text` | *ver `01-index.md` Prompts base SDXL* |
| `clip` | `["1", 1]` | CLIP-L + CLIP-G dual |

> **SDXL style:** Lenguaje natural fotográfico — `photorealistic`, `raw photo`, `8k uhd`, `canon r5`, `tilt-shift lens`  
> **NO requiere trigger words** del modelo.

---

### 3. CLIPTextEncode Negative (nodo 3)

| Input | Valor |
|-------|-------|
| `text` | *ver `01-index.md` Prompts base SDXL* |
| `clip` | `["1", 1]` |

> **Ampliado vs SD 1.5:** Incluye `illustration, painting, drawing, oversaturated, cartoonish` — artefactos típicos SDXL

---

### 4. EmptyLatentImage (nodo 4)

| Input | Valor | Nota |
|-------|-------|------|
| `width` | 1216 | Landscape SDXL nativo 16:9 |
| `height` | 832 | Bucket válido SDXL |
| `batch_size` | 1 | VRAM 8GB límite |

> **Resoluciones SDXL bucket válidas:** 1024×1024, 1152×896, **1216×832**, 1344×768, 1536×640, 832×1216, 896×1152, 768×1344, 640×1536

---

### 5. KSampler (nodo 5) — **Config SDXL CRÃTICA**

| Input | Valor | Justificación |
|-------|-------|---------------|
| `model` | `["1", 0]` | Del checkpoint |
| `positive` | `["2", 0]` | CLIP encode pos |
| `negative` | `["3", 0]` | CLIP encode neg |
| `latent_image` | `["4", 0]` | Empty latent |
| `seed` | 42 | Baseline fijo |
| `steps` | 35 | SDXL beneficia steps extra |
| `cfg` | 4 | **SDXL rango 3-5** (CFG 7 quema) |
| `sampler_name` | `dpmpp_2m` | **Óptimo SDXL** (no euler) |
| `scheduler` | `karras` | **Obligatorio SDXL** (no normal) |
| `denoise` | 1.0 | txt2img puro |

> **Diferencias clave vs SD 1.5:**
> - Sampler: `dpmpp_2m` (no euler)
> - Scheduler: `karras` (no normal)
> - CFG: 4 (no 7)
> - Steps: 35 (no 30)
> - Resolution: 1216×832 (no 768×512)

---

### 6. VAEDecode (nodo 6)

| Input | Valor |
|-------|-------|
| `samples` | `["5", 0]` |
| `vae` | `["1", 2]` | **VAE del checkpoint** (Juggernaut XL lo trae) |

> No cargar VAE externo — el embebido está afinado para el modelo.

---

### 7. SaveImage (nodo 7)

| Input | Valor |
|-------|-------|
| `filename_prefix` | `estadio_futbol_sdxl` |
| `images` | `["6", 0]` |

> Output: `estadio_futbol_sdxl_XXXXX_.png`

---

## Flags ComfyUI Obligatorios (AMD RX 570 8GB)

```bat
@echo off
set PYTORCH_DIRECTML_DEVICE=0
P:\Anaconda\envs\comfyenv\python.exe -m comfyui ^
  --directml 0 ^
  --force-fp16 ^
  --disable-cuda-malloc ^
  --lowvram ^
  --cpu-vae ^
  --listen 127.0.0.1 ^
  --port 8188
```

| Flag | Por qué (SDXL en 8GB) |
|------|----------------------|
| `--lowvram` | Offload weights a CPU entre steps (SDXL 7GB no cabe sin esto) |
| `--cpu-vae` | VAE decode en CPU (ahorra ~1GB VRAM peak) |
| `--force-fp16` | Half precision obligatorio |
| `--disable-cuda-malloc` | Evita fragmentación VRAM DirectML |

---

## Pipeline Post-Generación Recomendado (no en workflow)

```
Output base (1216×832)
  │
  ├─→ Hires Fix (en KSampler o aparte):
  │     upscale_by: 1.5
  │     upscale_model: 4x_foolhardy_Remacri
  │     denoise: 0.35
  │     steps: 15-20
  │     → ~1824×1248
  │
  └─→ Upscale standalone 2× (ImageUpscaleWithModel):
        model: 4x_foolhardy_Remacri
        → 2432×1664 (~4 MP, entrega A3 300dpi)
```

> **Requiere:** `4x_foolhardy_Remacri.pth` en `models/upscale_models/` (pendiente descarga)

---

## Referencias

- Ficha ArchitectureRealmix: [[wiki/glosario/software/comfyui#checkpoint--architecturerealmix-v11|checkpoint-architecturerealmix-v11]]
- Ficha Juggernaut XL v9: [[wiki/glosario/software/comfyui#checkpoint--juggernaut-xl-v9|checkpoint-juggernaut-xl-v9]]
- Glosario KSampler: [[wiki/glosario/software/comfyui|k-sampler]]
- Glosario CheckpointLoader: [[wiki/glosario/software/comfyui|checkpoint-loader]]
- Troubleshooting VRAM: [[wiki/glosario/interno/pbooks/pbk-troubleshooting-reconexion#vram-llena-oom--liberar-y-prevenir]]