---
tipo: nodos
workflow: WF-vivienda
nivel: n_01-txt2img
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [nodos, config, sdxl, juggernaut, vivienda]
---

# 03-nodos-WFvivienda — Configuración Específica por Nodo

**Workflow:** `workflow_txt2img_vivienda_sdxl.json`  
**Modelo:** Juggernaut XL v9 (SDXL) — VAE incluido en checkpoint  
**Referencia genérica:** [[wiki/glosario/software/comfyui]] — *solo lo NO genérico va aquí*

---

## Nodo 1 — CheckpointLoaderSimple

| Campo | Valor | Justificación |
|-------|-------|---------------|
| **class_type** | `CheckpointLoaderSimple` | Carga checkpoint + VAE + CLIP en uno |
| **ckpt_name** | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | Modelo SDXL fotorrealista, VAE embebido |
| **Outputs** | `MODEL` (0), `CLIP` (1), `VAE` (2) | VAE en output 2 evita VAELoader separado |

> ⚠ï¸ **No usar VAELoader aparte** — Juggernaut XL trae VAE optimizado. Cargar VAE externo rompe color/negros.

---

## Nodo 2 — CLIPTextEncode (Positive)

| Campo | Valor | Justificación |
|-------|-------|---------------|
| **class_type** | `CLIPTextEncode` | Codifica prompt en conditioning SDXL |
| **text** | `photorealistic, raw photo, 8k uhd, architectural photography, modern single-family house, clean geometric volumes, white stucco facade, floor-to-ceiling windows, flat roof, minimal landscaping, morning sunlight, sharp shadows, highly detailed, masterpiece, canon r5, 24mm tilt-shift lens` | **Estilo SDXL**: lenguaje natural fotográfico, NO trigger words. Incluye: estilo, sujeto, materiales, iluminación, cámara, calidad |
| **clip** | `["1", 1]` | Input CLIP del CheckpointLoader (output 1) |

**Diferencia clave SD 1.5 → SDXL:**
- SD 1.5: `architecturerealmix style, modern house...` (trigger word + tags)
- SDXL: `photorealistic, raw photo, 8k uhd, architectural photography, modern house...` (descripción natural)

---

## Nodo 3 — CLIPTextEncode (Negative)

| Campo | Valor | Justificación |
|-------|-------|---------------|
| **class_type** | `CLIPTextEncode` | Negative conditioning |
| **text** | `blurry, low quality, distorted, ugly, bad architecture, cartoon, sketch, deformed, watermark, text, signature, grain, noise, overexposed, underexposed, illustration, painting, drawing, people, cars, clutter, messy` | **Amplio**: SDXL más sensible a negative. Incluye: calidad, estilo no deseado, elementos distractores (gente, autos), artefactos |
| **clip** | `["1", 1]` | Mismo CLIP que positive |

---

## Nodo 4 — EmptyLatentImage

| Campo | Valor | Justificación |
|-------|-------|---------------|
| **class_type** | `EmptyLatentImage` | Latente vacío para KSampler |
| **width** | `1216` | **Bucket SDXL landscape 16:9** — nativo 1024² entrenado en aspect ratios |
| **height** | `832` | 1216×832 = 1.01 MP ≈ 1024² área equivalente |
| **batch_size** | `1` | **VRAM 8GB límite** — batch >1 OOM en SDXL |

**Buckets SDXL recomendados (Juggernaut XL):**
| Aspect Ratio | Resolution | Uso |
|--------------|------------|-----|
| Landscape 16:9 | **1216×832** | Fachadas, vistas aéreas, sitio |
| Portrait 9:16 | **832×1216** | Interiores verticales, detalles |
| Square 1:1 | **1024×1024** | Composiciones centradas, plantas |
| 4:3 | **1152×896** | Render general equilibrado |
| 3:2 | **1216×832** | Fotografía arquitectónica estándar |

---

## Nodo 5 — KSampler (CRÃTICO: configs SDXL ≠ SD 1.5)

| Campo | Valor | Justificación SDXL |
|-------|-------|-------------------|
| **class_type** | `KSampler` | Sampler principal |
| **model** | `["1", 0]` | MODEL del checkpoint |
| **positive** | `["2", 0]` | Conditioning positive |
| **negative** | `["3", 0]` | Conditioning negative |
| **latent_image** | `["4", 0]` | Latent del EmptyLatentImage |
| **seed** | `42` | Baseline fijo (cambiar por versión) |
| **steps** | `35` | SDXL necesita ligeramente más steps que SD 1.5 (30) |
| **cfg** | `4` | **SDXL: CFG 3-5** — CFG 7+ quema, pierde realismo |
| **sampler_name** | `dpmpp_2m` | **Óptimo SDXL** — euler/euler_a dan peores resultados |
| **scheduler** | `karras` | **Obligatorio SDXL** — normal/constant peores |
| **denoise** | `1.0` | txt2img = 1.0 (img2img usar 0.3-0.8) |

### Tabla: SD 1.5 vs SDXL — KSampler

| Parámetro | SD 1.5 (ArchitectureRealmix) | SDXL (Juggernaut XL) | Por qué cambia |
|-----------|------------------------------|----------------------|----------------|
| **Sampler** | `euler` / `euler_ancestral` | `dpmpp_2m` / `dpmpp_2m_sde` | SDXL entrenado con DPM++ |
| **Scheduler** | `normal` / `karras` | **`karras` obligatorio** | Ruido schedule distinto |
| **CFG** | 6-8 | **3-5** | SDXL más sensible, CFG alto = burn |
| **Steps** | 25-30 | **30-40** | Más steps para converger |
| **Resolution** | 512² / 768×512 | **1024² buckets** | Nativo 1024² |

---

## Nodo 6 — VAEDecode

| Campo | Valor | Justificación |
|-------|-------|---------------|
| **class_type** | `VAEDecode` | Decodifica latent a píxeles |
| **samples** | `["5", 0]` | Output del KSampler |
| **vae** | `["1", 2]` | **VAE del checkpoint (output 2)** — no VAE externo |

> Juggernaut XL VAE está en el checkpoint (output index 2 de CheckpointLoaderSimple).

---

## Nodo 7 — SaveImage

| Campo | Valor | Justificación |
|-------|-------|---------------|
| **class_type** | `SaveImage` | Guarda PNG en output/ |
| **images** | `["6", 0]` | Output VAEDecode |
| **filename_prefix** | `vivienda_sdxl_juggernaut` | Prefijo identificable: `{tema}_{modelo}_{checkpoint}` |

**Output esperado:** `output/vivienda_sdxl_juggernaut_XXXXX_.png`

---

## Flags ComfyUI obligatorios (AMD RX 570 8GB)

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

| Flag | Función | Por qué en 8GB |
|------|---------|----------------|
| `--directml 0` | Usa GPU AMD via DirectML | RX 570 no tiene CUDA |
| `--force-fp16` | Fuerza half precision | Ahorra ~50% VRAM weights |
| `--disable-cuda-malloc` | Evita allocador CUDA | DirectML no usa CUDA malloc |
| `--lowvram` | **Offload weights a CPU entre steps** | **CRÃTICO** — sin esto OOM en SDXL |
| `--cpu-vae` | VAE decode en CPU | Ahorra ~1GB VRAM peak |

---

## Referencias

- Glosario genérico: [[wiki/glosario/software/comfyui]]
- Ficha modelo: [[wiki/glosario/software/comfyui#checkpoint--juggernaut-xl-v9|Ficha Juggernaut XL v9]]
- Index flujo: [[01-index.md]]
- Log corridas: [[02-WF-log-WFvivienda.md]]
- Playbook AMD: [[wiki/glosario/interno/pbooks/pbk-troubleshooting-reconexion#vram-llena-oom--liberar-y-prevenir]]