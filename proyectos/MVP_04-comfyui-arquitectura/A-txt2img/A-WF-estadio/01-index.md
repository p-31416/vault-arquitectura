---
tipo: index
workflow: WF-estadio
nivel: n_01-txt2img
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-24
tags: [index, txt2img, estadio, sdxl, sd15, architecture-realmix, juggernaut]
estado: activo
---

# 01-index — WF-estadio (txt2img SD 1.5 + SDXL)

**Workflow SD 1.5:** `workflow_txt2img_estadio.json`  
**Workflow SDXL:** `workflow_txt2img_estadio_sdxl.json`  
**Modelo SD 1.5:** ArchitectureRealmix v1.1 (`architecturerealmix_v11.safetensors`, 2.1 GB)  
**Modelo SDXL:** Juggernaut XL v9 (`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors`, 7.11 GB)  
**Hardware:** AMD RX 570 8GB VRAM (DirectML) — SDXL requiere `--lowvram --cpu-vae`

---

## Configuración base (Baseline A — SD 1.5)

| Parámetro | Valor | Nota |
|-----------|-------|------|
| **Checkpoint** | `architecturerealmix_v11.safetensors` | SD 1.5, VAE incluido |
| **Resolución** | 768×512 | Landscape 3:2 |
| **Sampler** | euler | Estándar SD 1.5 |
| **Scheduler** | normal | Estándar SD 1.5 |
| **Steps** | 30 | |
| **CFG** | 7 | SD 1.5 rango 6-8 |
| **Batch size** | 1 | VRAM 8GB |

---

## Configuración base (Baseline D — SDXL)

| Parámetro | Valor | Nota |
|-----------|-------|------|
| **Checkpoint** | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | SDXL, VAE embebido |
| **Resolución** | 1216×832 | Landscape SDXL nativo 16:9 |
| **Sampler** | dpmpp_2m | **Óptimo SDXL** |
| **Scheduler** | karras | **Obligatorio SDXL** |
| **Steps** | 35 | Ligeramente > SD 1.5 |
| **CFG** | 4 | **SDXL rango 3-5** |
| **Batch size** | 1 | VRAM 8GB límite |
| **Flags AMD** | `--lowvram --cpu-vae` | **Obligatorio** |

---

## Prompts base

### SD 1.5 (ArchitectureRealmix — trigger words)
```
# Positive
architecturerealmix style, modern football stadium, aerial view, curved steel roof, floodlights, green pitch, photorealistic, architectural photography, 8K, highly detailed, dramatic lighting, sunset golden hour

# Negative
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, deformed
```

### SDXL (Juggernaut XL — lenguaje natural fotográfico)
```
# Positive
photorealistic, raw photo, 8k uhd, architectural photography, modern football stadium, aerial view, curved steel roof, floodlights, green pitch, sunlight, blue sky, sharp focus, highly detailed, masterpiece, canon r5, 24mm tilt-shift lens

# Negative
blurry, low quality, distorted, ugly, bad architecture, cartoon, sketch, deformed, watermark, text, signature, grain, noise, overexposed, underexposed, illustration, painting, drawing
```

---

## Versiones ejecutadas

| Versión | Fecha | Tipo | Modelo | Seed | Config clave | Archivo salida | Log |
|---------|-------|------|--------|------|--------------|----------------|-----|
| `D-01` | 2026-07-24 | **SDXL Migración** | Juggernaut XL v9 | 42 | steps=35, cfg=4, dpmpp_2m, karras, 1216×832 | `n_01-D-01.png` | [WF-log](#) |
| `C-01` | 2026-07-24 | Parámetros (seed) | ArchitectureRealmix | 43 | steps=30, cfg=7, euler, normal, 768×512 | `n_01-C-01.png` | [WF-log](#) |
| `B-01` | 2026-07-18 | Prompt (nocturno) | ArchitectureRealmix | 42 | steps=30, cfg=7, euler, normal, 768×512 | `n_01-B-01.png` | [WF-log](#) |
| `A-02` | 2026-07-18 | Baseline 2 | ArchitectureRealmix | 42 | steps=30, cfg=7, euler, normal, 768×512 | `n_01-A-02.png` | [WF-log](#) |
| `A-01` | 2026-07-17 | Baseline 1 | ArchitectureRealmix | 42 | steps=30, cfg=7, euler, normal, 768×512 | `n_01-A-01.png` | [WF-log](#) |

> **Convención:** `n_01-{LETRA}-{NN}.png` en `salidas/` — ver `00-README.md`

### Leyenda de versiones

`n_01-{LETRA}-{NN}`:
- **A** = Baseline absoluto (3 corridas idénticas, sin cambios)
- **B** = Variación de **prompt** (atmósfera, estilo, materiales)
- **C** = Exploración de **parámetros** (cfg, sampler, scheduler, steps)
- **D** = **Migración de modelo** (ej. SD 1.5 → SDXL)
- **E** = Variación de **resolución / aspect ratio**
- **F** = Test de **ControlNet / img2img**

---

## Referencias cruzadas

- **Log detallado:** `02-WF-log-WFestadio.md`
- **Nodos (configs propias):** `03-nodos-WFestadio.md`
- **Backlog:** `04-backlog.md`
- **Salidas:** `salidas/n_01-{L}-{NN}.png`
- **Plan comparativa:** `PLANS/comparativa-sd15-vs-sdxl.md`
- **Specs:** `SPECS/`

---

## Flujo de trabajo (nodos)

### SD 1.5 (ArchitectureRealmix)
```
CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────┤
    └──vae──────────────────┐   │
[CLIPTextEncode (pos)] ─────┤   │
[CLIPTextEncode (neg)] ─────┤   │
                            ▼   ▼
EmptyLatentImage ──► KSampler ──► VAEDecode ──► SaveImage
```

### SDXL (Juggernaut XL v9)
```
CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────┤
    └──vae (embebido)────────┐   │
[CLIPTextEncode (pos)] ─────┤   │
[CLIPTextEncode (neg)] ─────┤   │
                            ▼   ▼
EmptyLatentImage ──► KSampler ──► VAEDecode ──► SaveImage
```

**Workflow SD 1.5:** [[workflow_txt2img_estadio.json]]  
**Workflow SDXL:** [[workflow_txt2img_estadio_sdxl.json]]