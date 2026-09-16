---
tipo: flujo
workflow: WF-vivienda
nivel: n_01-txt2img
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [vivienda, txt2img, arquitectura, sdxl, juggernaut]
estado: pendiente
---

# 01-index — Catálogo de Versiones WF-vivienda

**Workflow:** `workflow_txt2img_vivienda_sdxl.json`  
**Modelo:** Juggernaut XL v9 (`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors`)  
**Resolución base:** 1216×832 (landscape SDXL nativo 16:9)  
**Hardware:** AMD RX 570 8GB VRAM — `--lowvram --cpu-vae` obligatorio

---

## Tabla de versiones ejecutadas

| Versión | Fecha | Tipo | Seed | Config clave | Archivo salida | Log |
|---------|-------|------|------|--------------|----------------|-----|
| *Pendiente* | — | — | — | — | — | — |

> **Formato:** `n_01-{LETRA}-{NN}.png` → ver `00-README.md` para convención de letras.

---

## Configuración base (Baseline A — 3 corridas idénticas)

| Parámetro | Valor | Nota |
|-----------|-------|------|
| **Checkpoint** | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | SDXL, VAE embebido |
| **Resolución** | 1216×832 | Landscape 16:9 nativo |
| **Sampler** | `dpmpp_2m` | Óptimo SDXL |
| **Scheduler** | `karras` | Obligatorio SDXL |
| **Steps** | 35 | Ligeramente > SD 1.5 |
| **CFG** | 4 | SDXL rango 3-5 |
| **Denoise** | 1.0 | txt2img puro |
| **Batch size** | 1 | VRAM 8GB límite |
| **VAE** | Embebido en checkpoint | Juggernaut XL lo incluye |

---

## Prompts base (SDXL style — lenguaje natural fotográfico)

### Positive
```
photorealistic, raw photo, 8k uhd, architectural photography, modern single-family house, clean geometric volumes, white stucco facade, floor-to-ceiling windows, flat roof, minimal landscaping, morning sunlight, sharp shadows, sharp focus, highly detailed, masterpiece, canon r5, 24mm tilt-shift lens
```

### Negative
```
blurry, low quality, distorted, ugly, bad architecture, cartoon, sketch, deformed, watermark, text, signature, grain, noise, overexposed, underexposed, illustration, painting, drawing, oversaturated, cartoonish
```

---

## Nodos del flujo (ver `03-nodos-WFvivienda.md` para detalle)

1. **CheckpointLoaderSimple** → Carga Juggernaut XL v9
2. **CLIPTextEncode (pos)** → Prompt positivo SDXL style
3. **CLIPTextEncode (neg)** → Prompt negativo extendido
4. **EmptyLatentImage** → 1216×832, batch=1
5. **KSampler** → dpmpp_2m, karras, 35 steps, cfg 4
6. **VAEDecode** → VAE del checkpoint
7. **SaveImage** → Prefix: `vivienda_sdxl_juggernaut`

---

## Referencias cruzadas

- **Log corridas:** `02-WF-log-WFvivienda.md`
- **Detalle nodos:** `03-nodos-WFvivienda.md`
- **Backlog:** `04-backlog.md`
- **Salidas:** `salidas/n_01-{L}-{NN}.png`
- **Plans/Comparativas:** `PLANS/`
- **Specs:** `SPECS/`
- **Glosario nodos genérico:** [[wiki/glosario/software/comfyui|nodos ComfyUI]]