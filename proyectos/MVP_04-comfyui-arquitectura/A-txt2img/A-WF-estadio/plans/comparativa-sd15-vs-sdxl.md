---
tipo: comparativa
mvp: 04
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [mvp_04, sdxl, sd15, comparativa, workflow, juggernaut, architecture-realmix]
---

# Comparativa SD 1.5 vs SDXL — Mismo Prompt, Mismo Seed

**Objetivo**: Evaluar Juggernaut XL v9 vs ArchitectureRealmix v1.1 con **prompt idéntico**, **seed idéntico (42)**, **workflow equivalente** para decisión de migración a SDXL en entregas finales.

---

## Workflows

| | SD 1.5 (Baseline) | SDXL (Nuevo) |
|---|---|---|
| **Archivo** | `workflow_txt2img_estadio.json` | `workflow_txt2img_estadio_sdxl.json` |
| **Checkpoint** | `architecturerealmix_v11.safetensors` | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` |
| **Resolución** | 768×512 | 1216×832 (landscape SDXL nativo) |
| **Sampler** | euler | dpmpp_2m |
| **Scheduler** | normal | karras |
| **Steps** | 30 | 35 |
| **CFG** | 7 | 4 |
| **VAE** | Incluido en checkpoint | Incluido en checkpoint (Juggernaut XL) |

---

## Diferencias clave SD 1.5 → SDXL

| Aspecto | SD 1.5 | SDXL | Impacto |
|---------|--------|------|---------|
| **Resolución nativa** | 512² | 1024² | SDXL compone mejor en 1024+ |
| **Text encoders** | 1 (CLIP-L) | 2 (CLIP-L + CLIP-G) | SDXL entiende prompts más complejos |
| **CFG óptimo** | 6-8 | 3-5 | SDXL más sensible, CFG alto quema |
| **Sampler recomendado** | euler/euler_a | dpmpp_2m/dpmpp_2m_sde | Karras scheduler crítico en SDXL |
| **Aspect ratio** | Cuadrado preferido | Cualquier (entrenado en bucket) | 1216×832 = 16:9 landscape |
| **VAE** | SD 1.5 VAE | SDXL VAE (mejor color/negros) | Juggernaut XL lo trae integrado |

---

## Prompts usados (idénticos semánticamente)

### Positive (adaptado a estilo SDXL)
```
SD 1.5: architecturerealmix style, modern football stadium, aerial view, curved steel roof, floodlights, green pitch, photorealistic, architectural photography, 8K, highly detailed, dramatic lighting, sunset golden hour

SDXL: photorealistic, raw photo, 8k uhd, architectural photography, modern football stadium, aerial view, curved steel roof, floodlights, green pitch, sunlight, blue sky, sharp focus, highly detailed, masterpiece, canon r5, 24mm tilt-shift lens
```
> **Nota**: SDXL no necesita "trigger word" del modelo. Usa lenguaje natural fotográfico.

### Negative (ampliado para SDXL)
```
SD 1.5: low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, deformed

SDXL: low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, deformed, watermark, text, signature, grain, noise, overexposed, underexposed, painting, illustration, drawing
```

---

## Plan de test (5 seeds por modelo)

| Seed | SD 1.5 Output | SDXL Output | Notas |
|------|---------------|-------------|-------|
| 42 | `n_01-A-01.png` (baseline) | `n_01-D-01.png` ✅ **COMPLETADO** | **Comparación principal** |
| 43 | `n_01-A-02.png` | `n_01-D-02.png` ⬜ Pendiente | Variación 1 |
| 44 | — | `n_01-D-03.png` ⬜ Pendiente | Variación 2 |
| 45 | — | `n_01-D-04.png` ⬜ Pendiente | Variación 3 |
| 46 | — | `n_01-D-05.png` ⬜ Pendiente | Variación 4 |

---

## Criterios de evaluación

### 1. Calidad arquitectónica (1-5)
- [ ] Geometría estadio (elipse, gradas, techo)
- [ ] Materialidad (hormigón, acero, vidrio, césped)
- [ ] Iluminación (sol, sombras, floodlights)
- [ ] Composición aérea (perspectiva, escala)

### 2. Calidad técnica (1-5)
- [ ] Nitidez / enfoque
- [ ] Ausencia de artefactos (halos, bordes, ruido)
- [ ] Color (balance, saturación, realismo)
- [ ] Detalle fino (texturas, pequeños elementos)

### 3. Fidelidad al prompt (1-5)
- [ ] "Aerial view" visible
- [ ] "Curved steel roof" legible
- [ ] "Floodlights" presentes
- [ ] "Green pitch" correcto
- [ ] "Photorealistic / architectural photography" estilo

### 4. VRAM / Performance (RX 570 8GB)
| Métrica | SD 1.5 | SDXL |
|---------|--------|------|
| VRAM peak | ~4 GB | ~7.5 GB |
| Tiempo (30/35 steps) | ~90s | ~55-65s |
| OOM risk | Bajo | Medio (requiere --lowvram) |

---

## Ejecución

### 1. Verificar Juggernaut XL descargado
```bash
# En ComfyUI: models/checkpoints/ debe tener
Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors  (7.11 GB)
```

### 2. Lanzar ComfyUI con flags AMD 8GB
```bat
@echo off
set PYTORCH_DIRECTML_DEVICE=0
P:\Anaconda\envs\comfyenv\python.exe -m comfyui ^
  --directml 0 ^
  --force-fp16 ^
  --disable-cuda-malloc ^
  --lowvram ^
  --listen 127.0.0.1 ^
  --port 8188
```
> **Crítico**: `--lowvram` obligatorio para SDXL en 8GB

### 3. Cargar workflow SDXL
- Arrastrar `workflow_txt2img_estadio_sdxl.json` a ComfyUI
- Verificar: CheckpointLoaderSimple → `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors`
- Queue Prompt

### 4. Cambiar seed y re-queue (5 veces)
- En KSampler (nodo 5): cambiar `seed: 42` → `43` → `44` → `45` → `46`
- Queue Prompt cada vez

### 5. Documentar resultados
- Outputs en `output/` con prefix `estadio_futbol_sdxl_`
- Copiar a `n_01-txt2img/WF-estadio/salidas/` con nomenclatura:
  - `n_01-D-01.png` (seed 42 SDXL)
  - `n_01-D-02.png` (seed 43 SDXL)
  - etc.

---

## Análisis post-test (plantilla)

### Tabla comparativa seeds 42

| Criterio | SD 1.5 (ArchitectureRealmix) | SDXL (Juggernaut XL) | Ganador |
|----------|------------------------------|----------------------|---------|
| Geometría estadio | | | |
| Materialidad | | | |
| Iluminación | | | |
| Nitidez | | | |
| Artefactos | | | |
| Color | | | |
| Fidelidad prompt | | | |
| **TOTAL /35** | | | |

### Decisión

- [ ] **Migrar a SDXL para entregas finales** (Juggernaut XL calidad superior)
- [ ] **Mantener SD 1.5 para iteración/ControlNet** (VRAM, velocidad, CN compatible)
- [ ] **Híbrido**: SD 1.5 concepto → SDXL Hires Fix / img2img refinado
- [ ] **Esperar hardware NVIDIA 12GB+** para SDXL + ControlNet completo

---

## Referencias

- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/workflow_txt2img_estadio.json|Workflow SD 1.5 original]]
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/workflow_txt2img_estadio_sdxl.json|Workflow SDXL nuevo]]
- [[modelos-recomendados|Modelos recomendados (sección Juggernaut XL)]]
- [[wiki/glosario/software/comfyui#checkpoint--juggernaut-xl-v9|Ficha técnica Juggernaut XL v9]]
- [[wiki/estudio/adr-001-comfyui-mcp|ADR-001 licencias]]