---
tipo: wf-log
workflow: WF-estadio
nivel: n_01-txt2img
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-24
tags: [wf-log, txt2img, estadio, sd15, architecture-realmix]
---

# 02-WF-log — WF-estadio (txt2img SD 1.5 / SDXL)

**Log detallado de TODAS las corridas** — Extensión de `01-index.md`  
Cada versión ejecutada → una entrada aquí + archivo en `salidas/n_01-{L}-{NN}.png`

**Formato:** Una entrada por versión. Más nuevo → más arriba.  
**Referencia cruzada:** Cada versión link a su imagen en `salidas/` y a su fila en `01-index.md`.

---

## Plantilla de entrada (copiar para cada corrida)

```markdown
## n_01-{LETRA}-{NN} — {YYYY-MM-DD} — {HH:MM}

**Versión:** `n_01-{LETRA}-{NN}`
**Archivo output:** `salidas/n_01-{LETRA}-{NN}.png`
**ComfyUI output:** `estadio_futbol_XXXXX_.png` / `estadio_futbol_sdxl_XXXXX_.png`

### Configuración
| Parámetro | Valor |
|-----------|-------|
| Seed | 42 |
| Steps | 30 / 35 |
| CFG | 7 / 4 |
| Sampler | euler / dpmpp_2m |
| Scheduler | normal / karras |
| Resolution | 768×512 / 1216×832 |
| Batch | 1 |
| Denoise | 1.0 |
| Checkpoint | architecturerealmix_v11.safetensors / Juggernaut-XL_v9... |
| VAE | Incluido / Incluido |
| Flags ComfyUI | --directml 0 --force-fp16 / --lowvram --cpu-vae |

### Prompts
**Positive:**
```
[pegar prompt exacto usado]
```

**Negative:**
```
[pegar negative exacto usado]
```

### Métricas
| Métrica | Valor |
|---------|-------|
| Tiempo generación | ~XXs |
| VRAM peak | ~X.X GB |
| VRAM free post | ~X.X GB |
| Tamaño archivo | XXX KB |

### Observaciones
- [Qué funcionó bien]
- [Qué mejorar / artefactos / fidelidad prompt]
- [Decisión: mantener / iterar / descartar]

### Evaluación (1-5)
| Criterio | Score | Nota |
|----------|-------|------|
| Geometría estadio (elipse, gradas, techo) | /5 | |
| Materialidad (hormigón, acero, vidrio, césped) | /5 | |
| Iluminación (sol, sombras, floodlights) | /5 | |
| Nitidez / Detalle | /5 | |
| Ausencia artefactos | /5 | |
| Color / Realismo | /5 | |
| Fidelidad prompt | /5 | |
| **TOTAL** | **/35** | |

---

---

---

## n_01-D-01 — 2026-07-24 — 22:52 (SDXL)

**Versión:** `n_01-D-01`
**Archivo output:** `salidas/n_01-D-01.png`
**ComfyUI output:** `estadio_sdxl_juggernaut_00001_.png`

### Configuración
| Parámetro | Valor |
|-----------|-------|
| Seed | 42 |
| Steps | 35 |
| CFG | 4 |
| Sampler | dpmpp_2m |
| Scheduler | karras |
| Resolution | 1216×832 |
| Batch | 1 |
| Denoise | 1.0 |
| Checkpoint | Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors |
| VAE | Incluido en checkpoint |
| Flags ComfyUI | --directml 0 --force-fp16 --disable-cuda-malloc --lowvram --cpu-vae |

### Prompts
**Positive:**
```
photorealistic, raw photo, 8k uhd, architectural photography, modern football stadium, aerial view, curved steel roof, floodlights, green pitch, sunlight, blue sky, sharp focus, highly detailed, masterpiece, canon r5, 24mm tilt-shift lens
```

**Negative:**
```
blurry, low quality, distorted, ugly, bad architecture, cartoon, sketch, deformed, watermark, text, signature, grain, noise, overexposed, underexposed, illustration, painting, drawing
```

### Métricas
| Métrica | Valor |
|---------|-------|
| Tiempo generación | 561.86s (~9.3 min) |
| VRAM peak | ~7.5 GB (LOW_VRAM mode) |
| Tamaño archivo | 1.87 MB (1871599 bytes) |

### Observaciones
- Primera corrida SDXL (Juggernaut XL v9) en hardware AMD RX 570 8GB
- LOW_VRAM + CPU-VAE obligatorio — 561s total (vs ~90s SD 1.5)
- Mismo seed (42) y prompt semántico equivalente al baseline SD 1.5 A-01
- Output guardado como `n_01-D-01.png` para comparativa directa

### Evaluación (1-5) — Pendiente inspección visual
| Criterio | Score | Nota |
|----------|-------|------|
| Geometría estadio (elipse, gradas, techo) | /5 | |
| Materialidad (hormigón, acero, vidrio, césped) | /5 | |
| Iluminación (sol, sombras, floodlights) | /5 | |
| Nitidez / Detalle | /5 | |
| Ausencia artefactos | /5 | |
| Color / Realismo | /5 | |
| Fidelidad prompt | /5 | |
| **TOTAL** | **/35** | |

---

## n_01-C-01 — 2026-07-24 — ~12:57 (SD 1.5)

**Versión:** `n_01-C-01`
**Archivo output:** `salidas/n_01-C-01.png`
**ComfyUI output:** `estadio_futbol_00009_.png`

### Configuración
| Parámetro | Valor |
|-----------|-------|
| Seed | 43 |
| Steps | 30 |
| CFG | 7 |
| Sampler | euler |
| Scheduler | normal |
| Resolution | 768×512 |
| Batch | 1 |
| Denoise | 1.0 |
| Checkpoint | architecturerealmix_v11.safetensors |
| VAE | Incluido en checkpoint |
| Flags ComfyUI | --directml 0 --force-fp16 --disable-cuda-malloc |

### Prompts
**Positive:**
```
architecturerealmix style, modern football stadium, aerial view, curved steel roof, floodlights, green pitch, photorealistic, architectural photography, 8K, highly detailed, dramatic lighting, sunset golden hour
```

**Negative:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, deformed
```

### Métricas
| Métrica | Valor |
|---------|-------|
| Tiempo generación | ~88s (caché 2 nodos) |
| VRAM peak | ~4 GB |
| Tamaño archivo | ~741 KB |

### Observaciones
- Primera variación de seed (43 vs 42 baseline)
- Misma config que A-01/A-02 → evalúa variabilidad estocástica
- Archivo distinto a A-02 (741KB vs 731KB) → variación real, no duplicado

### Evaluación (1-5)
| Criterio | Score | Nota |
|----------|-------|------|
| Geometría estadio | /5 | Pendiente inspección visual |
| Materialidad | /5 | |
| Iluminación | /5 | |
| Nitidez / Detalle | /5 | |
| Ausencia artefactos | /5 | |
| Color / Realismo | /5 | |
| Fidelidad prompt | /5 | |
| **TOTAL** | **/35** | |

---

## n_01-B-01 — 2026-07-18 (SD 1.5)

**Versión:** `n_01-B-01` — Variación prompt: nocturno
**Archivo output:** `salidas/n_01-B-01.png`
**ComfyUI output:** `estadio_futbol_XXXXX_.png`

### Configuración
| Parámetro | Valor |
|-----------|-------|
| Seed | (no registrado) |
| Steps | 30 |
| CFG | 7 |
| Sampler | euler |
| Scheduler | normal |
| Resolution | 768×512 |
| Checkpoint | architecturerealmix_v11.safetensors |

### Prompts
**Positive:**
```
architecturerealmix style, modern football stadium, aerial view, curved steel roof,
floodlights illuminated, green pitch under lights, night match atmosphere,
photorealistic, architectural photography, 8K, highly detailed,
dramatic artificial lighting, stadium lights
```

**Negative:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, deformed
```

### Métricas
| Métrica | Valor |
|---------|-------|
| Tiempo generación | ~88s |

### Observaciones
- Primera variación de prompt del proyecto (sunset → night match)
- Evalúa respuesta ArchitectureRealmix a cambio de atmósfera
- Seed no registrada — no replicable exactamente

### Evaluación (1-5)
| Criterio | Score | Nota |
|----------|-------|------|
| Geometría estadio | /5 | Pendiente inspección visual |
| Materialidad | /5 | |
| Iluminación nocturna | /5 | |
| Nitidez / Detalle | /5 | |
| Ausencia artefactos | /5 | |
| Color / Realismo | /5 | |
| Fidelidad prompt | /5 | |
| **TOTAL** | **/35** | |

---

## n_01-A-02 — 2026-07-18 (SD 1.5)

**Versión:** `n_01-A-02` — Baseline run 2 (repetibilidad)
**Archivo output:** `salidas/n_01-A-02.png`

### Configuración
| Parámetro | Valor |
|-----------|-------|
| Seed | 42 (igual A-01) |
| Steps | 30 |
| CFG | 7 |
| Sampler | euler |
| Scheduler | normal |
| Resolution | 768×512 |
| Checkpoint | architecturerealmix_v11.safetensors |

### Métricas
| Métrica | Valor |
|---------|-------|
| Tiempo generación | ~88s (2 nodos cacheados) |
| Tamaño archivo | ~731 KB (vs 741 KB A-01) |

### Observaciones
- Segunda corrida baseline idéntica a A-01 (seed=42)
- Archivo distinto (731 vs 741 KB) → variación estocástica normal
- Tiempo menor por caché: CheckpointLoader, CLIPTextEncode, EmptyLatentImage
- Verifica determinismo relativo del flujo

### Evaluación (1-5)
| Criterio | Score | Nota |
|----------|-------|------|
| Geometría estadio | /5 | |
| Materialidad | /5 | |
| Iluminación | /5 | |
| Nitidez / Detalle | /5 | |
| Ausencia artefactos | /5 | |
| Color / Realismo | /5 | |
| Fidelidad prompt | /5 | |
| **TOTAL** | **/35** | |

---

## n_01-A-01 — 2026-07-17 (SD 1.5)

**Versión:** `n_01-A-01` — Baseline inicial (primera corrida workflow)
**Archivo output:** `salidas/n_01-A-01.png`

### Configuración
| Parámetro | Valor |
|-----------|-------|
| Seed | 42 |
| Steps | 30 |
| CFG | 7 |
| Sampler | euler |
| Scheduler | normal |
| Resolution | 768×512 |
| Checkpoint | architecturerealmix_v11.safetensors |

### Prompts
**Positive:**
```
architecturerealmix style, modern football stadium, aerial view, curved steel roof, floodlights, green pitch, photorealistic, architectural photography, 8K, highly detailed, dramatic lighting, sunset golden hour
```

**Negative:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, deformed
```

### Métricas
| Métrica | Valor |
|---------|-------|
| Tiempo generación | ~114s (primera corrida, sin caché) |
| Tamaño archivo | ~731 KB |

### Observaciones
- Primer render exitoso del MVP_04
- Cielo sunset correcto, césped texturado, techo curvo presente
- Iluminación general plana — falta contraste arquitectónico
- Bordes del estadio sin definición nítida

### Evaluación (1-5)
| Criterio | Score | Nota |
|----------|-------|------|
| Geometría estadio | 3/5 | Forma general OK, bordes blandos |
| Materialidad | 3/5 | Césped OK, hormigón/vidrio genérico |
| Iluminación | 2/5 | Plana, poca direccionalidad |
| Nitidez / Detalle | 3/5 | |
| Ausencia artefactos | 4/5 | Sin artefactos graves |
| Color / Realismo | 3/5 | Sunset OK, pero plano |
| Fidelidad prompt | 3/5 | Techo curvo presente, floodlights débiles |
| **TOTAL** | **21/35** | |

---

## Próximas versiones planificadas (ver `04-backlog.md`)

| Letra | Foco | Descripción |
|-------|------|-------------|
| **D** | Migración SDXL | Juggernaut XL v9, mismo prompt semántico, seed=42 |
| **B** | Prompt | Variaciones: amanecer, interior, brutalista, high-tech |
| **C** | Params | CFG 10-12, scheduler karras, sampler dpmpp_2m |
| **E** | Resolución | 512×512, 768×768, 1024×1024 (con Hires Fix) |
| **F** | ControlNet | img2img + Canny/Depth desde croquis |

---

## n_01-D-01 — 2026-07-24 — 22:53 (SDXL Juggernaut XL v9)

**Versión:** `n_01-D-01` — **Migración SDXL** — mismo prompt semántico, seed=42
**Archivo output:** `salidas/n_01-D-01.png`
**ComfyUI output:** `estadio_sdxl_juggernaut_00001_.png`

### Configuración
| Parámetro | Valor |
|-----------|-------|
| Seed | 42 |
| Steps | 35 |
| CFG | 4 |
| Sampler | dpmpp_2m |
| Scheduler | karras |
| Resolution | 1216×832 |
| Batch | 1 |
| Denoise | 1.0 |
| Checkpoint | Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors |
| VAE | Incluido en checkpoint |
| Flags ComfyUI | --directml 0 --force-fp16 --disable-cuda-malloc --lowvram --cpu-vae |

### Prompts
**Positive:**
```
photorealistic, raw photo, 8k uhd, architectural photography, modern football stadium, aerial view, curved steel roof, floodlights, green pitch, sunlight, blue sky, sharp focus, highly detailed, masterpiece, canon r5, 24mm tilt-shift lens
```

**Negative:**
```
blurry, low quality, distorted, ugly, bad architecture, cartoon, sketch, deformed, watermark, text, signature, grain, noise, overexposed, underexposed, illustration, painting, drawing
```

### Métricas
| Métrica | Valor |
|---------|-------|
| Tiempo generación | 561.86s (~9.3 min) |
| VRAM peak | ~7.5 GB (LOW_VRAM mode) |
| VRAM mode | LOW_VRAM + CPU VAE |
| Tamaño archivo | TBD KB |

### Observaciones
- **Primera corrida SDXL exitosa** en AMD RX 570 8GB con LOW_VRAM + CPU VAE
- Mismo prompt semántico que baseline SD 1.5 (seed=42), adaptado a estilo SDXL (lenguaje natural fotográfico)
- Resolución nativa SDXL 1216×832 (landscape 16:9 bucket)
- Sampler dpmpp_2m + karras (óptimo SDXL) vs euler + normal (SD 1.5)
- CFG 4 (rango SDXL 3-5) vs CFG 7 (SD 1.5)

### Evaluación (1-5)
| Criterio | Score | Nota |
|----------|-------|------|
| Geometría estadio (elipse, gradas, techo) | /5 | Pendiente inspección visual |
| Materialidad (hormigón, acero, vidrio, césped) | /5 | |
| Iluminación (sol, sombras, floodlights) | /5 | |
| Nitidez / Detalle | /5 | |
| Ausencia artefactos | /5 | |
| Color / Realismo | /5 | |
| Fidelidad prompt | /5 | |
| **TOTAL** | **/35** | |