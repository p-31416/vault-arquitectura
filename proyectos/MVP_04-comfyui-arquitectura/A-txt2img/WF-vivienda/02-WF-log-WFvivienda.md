---
tipo: log
workflow: WF-vivienda
nivel: n_01-txt2img
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [log, txt2img, vivienda, sdxl, juggernaut]
---

# 02-WF-log — WF-vivienda (txt2img SDXL)

Log detallado de cada corrida del workflow `workflow_txt2img_vivienda_sdxl.json`.

**Formato:** Una entrada por versión ejecutada.  
**Referencia cruzada:** Cada versión link a su imagen en `salidas/` y a su fila en `01-index.md`.

---

## Plantilla de entrada (copiar para cada corrida)

```markdown
## n_01-{LETRA}-{NN} — {YYYY-MM-DD} — {HH:MM}

**Versión:** `n_01-{LETRA}-{NN}`
**Archivo output:** `salidas/n_01-{LETRA}-{NN}.png`
**ComfyUI output:** `vivienda_sdxl_juggernaut_XXXXX_.png`

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
| Flags ComfyUI | --lowvram --cpu-vae --directml 0 --force-fp16 |

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
| Geometría / Volumetría | /5 | |
| Materialidad (estuco, vidrio, sombra) | /5 | |
| Iluminación / Sombras | /5 | |
| Nitidez / Detalle | /5 | |
| Ausencia artefactos | /5 | |
| Color / Realismo | /5 | |
| Fidelidad prompt | /5 | |
| **TOTAL** | **/35** | |

---

---

## n_01-A-01 — 2026-07-XX — XX:XX (PENDIENTE)

**Versión:** `n_01-A-01`
**Archivo output:** `salidas/n_01-A-01.png`
**ComfyUI output:** `vivienda_sdxl_juggernaut_XXXXX_.png`

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

### Prompts
**Positive:**
```
photorealistic, raw photo, 8k uhd, architectural photography, modern single-family house, clean geometric volumes, white stucco facade, floor-to-ceiling windows, flat roof, minimal landscaping, morning sunlight, sharp shadows, highly detailed, masterpiece, canon r5, 24mm tilt-shift lens
```

**Negative:**
```
blurry, low quality, distorted, ugly, bad architecture, cartoon, sketch, deformed, watermark, text, signature, grain, noise, overexposed, underexposed, illustration, painting, drawing, people, cars, clutter, messy
```

### Métricas
| Métrica | Valor |
|---------|-------|
| Tiempo generación | ~XXs |
| VRAM peak | ~X.X GB |
| Tamaño archivo | XXX KB |

### Observaciones
- [Pendiente de ejecución]

### Evaluación (1-5)
| Criterio | Score | Nota |
|----------|-------|------|
| Geometría / Volumetría | /5 | |
| Materialidad | /5 | |
| Iluminación / Sombras | /5 | |
| Nitidez / Detalle | /5 | |
| Ausencia artefactos | /5 | |
| Color / Realismo | /5 | |
| Fidelidad prompt | /5 | |
| **TOTAL** | **/35** | |

---

## n_01-A-02 — 2026-07-XX — XX:XX (PENDIENTE)

**Versión:** `n_01-A-02` — Baseline 2 (repetibilidad)
**Archivo output:** `salidas/n_01-A-02.png`

> Misma config que A-01, seed=42. Verificar que output es idéntico (determinismo).

### Observaciones
- [Pendiente]

---

## n_01-A-03 — 2026-07-XX — XX:XX (PENDIENTE)

**Versión:** `n_01-A-03` — Baseline 3
**Archivo output:** `salidas/n_01-A-03.png`

> Tercera corrida baseline para confirmar estabilidad.

### Observaciones
- [Pendiente]

---

## Próximas versiones planificadas (ver 04-backlog.md)

| Letra | Foco | Descripción |
|-------|------|-------------|
| **B** | Prompt | Variaciones atmósfera: atardecer, noche, nublado, golden hour |
| **C** | Params | CFG 3 vs 5, Steps 30 vs 40, Sampler euler_a vs dpmpp_2m |
| **D** | Resolution | 1024×1024 (square), 832×1216 (portrait) |
| **E** | Hires Fix | 1.5× denoise 0.35 + 4x_foolhardy_Remacri |
| **F** | Comparativa | Mismo prompt/seed vs WF-estadio SDXL (tipología distinta) |