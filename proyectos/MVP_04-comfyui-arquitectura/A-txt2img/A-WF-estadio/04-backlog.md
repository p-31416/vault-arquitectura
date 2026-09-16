---
tipo: backlog
workflow: WF-estadio
nivel: n_01-txt2img
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-24
tags: [backlog, pendientes, estadio, sd15, sdxl, migracion]
---

# 04-backlog — Pruebas y Iteraciones Pendientes WF-estadio

---

## Prioridad Alta — Baseline y Migración SDXL

| ID | Título | Descripción | Origen | Estado |
|----|--------|-------------|--------|--------|
| B-01 | **Baseline A — 3 corridas seed 42/43/44 (SD 1.5)** | Validar consistencia ArchitectureRealmix, misma config, 3 seeds | A-01/A-02 | ⬜ Pendiente |
| B-02 | **Baseline D — 3 corridas seed 42/43/44 (SDXL)** | Validar Juggernaut XL v9 estable, misma config SDXL | D-01 (plan) | ⬜ Pendiente |
| B-03 | **Hires Fix 1.5× + Remacri (SDXL)** | Agregar Hires Fix en KSampler (denoise 0.35, 15 steps, Remacri) | Plan SDXL | ⬜ Pendiente (req. modelo) |
| B-04 | **Comparativa SD 1.5 vs SDXL — seed 42** | Mismo prompt semántico, ambos modelos, evaluar /35 | `PLANS/comparativa-sd15-vs-sdxl.md` | ⬜ Pendiente |

---

## Prioridad Media — Exploración Parámetros (Letra C)

| ID | Título | Descripción | Origen | Estado |
|----|--------|-------------|--------|--------|
| C-01 | **CFG sweep SD 1.5** | CFG 5, 7, 9, 11, 13 — identificar sweet spot ArchitectureRealmix | A-01 | ⬜ Pendiente |
| C-02 | **CFG sweep SDXL** | CFG 3, 4, 5, 6 — Juggernaut XL sweet spot | Plan SDXL | ⬜ Pendiente |
| C-03 | **Sampler comparison SDXL** | dpmpp_2m vs dpmpp_2m_sde vs euler_a — mismo seed | Plan SDXL | ⬜ Pendiente |
| C-04 | **Steps sweep SDXL** | 25, 30, 35, 40, 50 — costo/beneficio | Plan SDXL | ⬜ Pendiente |
| C-05 | **Scheduler SDXL** | karras vs exponential vs simple — coherencia | Plan SDXL | ⬜ Pendiente |
| C-06 | **Resolución SDXL nativa** | 1024×1024 vs 1216×832 vs 832×1216 — mismo seed | Plan SDXL | ⬜ Pendiente |

---

## Prioridad Media — Variaciones Prompt (Letra B)

| ID | Título | Descripción | Origen | Estado |
|----|--------|-------------|--------|--------|
| B-01 | **Atmósfera golden hour** | `golden hour, warm directional light, long shadows` | B-01 | ⬜ Pendiente |
| B-02 | **Atmósfera nublado/difusa** | `overcast, soft diffuse light, no harsh shadows` | B-01 | ⬜ Pendiente |
| B-03 | **Atmósfera noche** | `twilight, exterior lights on, warm interior glow spilling out` | B-01 | ⬜ Pendiente |
| B-04 | **Estilo brutalista** | `brutalist architecture, exposed concrete, raw concrete texture, massive forms` | B-01 | ⬜ Pendiente |
| B-05 | **Estilo high-tech** | `high-tech architecture, steel glass curtain wall, exposed structure, technical aesthetic` | B-01 | ⬜ Pendiente |
| B-06 | **Contexto urbano denso** | `urban infill, narrow lot, party walls, rooftop terrace, city context` | B-01 | ⬜ Pendiente |

---

## Prioridad Baja — Pipeline Entrega (Letra E)

| ID | Título | Descripción | Origen | Estado |
|----|--------|-------------|--------|--------|
| E-01 | **Upscale 4× standalone** | ImageUpscaleWithModel Remacri 4× post Hires Fix | Plan entrega | ⬜ Pendiente (req. modelo) |
| E-02 | **Color correction LUT** | Aplicar LUT cine/archviz post-generación | Plan entrega | ⬜ Pendiente |
| E-03 | **Batch 4 seeds automático** | Script/loop para 4 seeds consecutivas | Calidad de vida | ⬜ Pendiente |

---

## Ideas / Sugerencias (no planificadas)

- [ ] **ControlNet Union SDXL** — cuando baje VRAM o migre a NVIDIA 12GB+
- [ ] **img2img refinado** — render base → img2img denoise 0.3-0.5 para detalle
- [ ] **LoRA arquitectura SDXL** — testear LoRAs CivitAI (Interior Design, Modern Arch, etc.)
- [ ] **Prompt engineering sistemático** — matriz tipología × material × luz × cámara
- [ ] **Comparativa tipología** — misma config: estadio vs vivienda unifamiliar vs torre

---

## Dependencias externas

| Dependencia | Estado | Bloquea |
|-------------|--------|---------|
| `4x_foolhardy_Remacri.pth` descargado | ⬜ Pendiente | Hires Fix, Upscale 4×, Pipeline entrega |
| `4x-ClearRealityV1.pth` descargado | ⬜ Pendiente | Upscale alternativo fotorrealista |
| Juggernaut XL v9 validado estable | ⬜ Pendiente | Migración SDXL completa |

---

## Referencias cruzadas

- **Index:** `01-index.md` (tabla versiones + configs)
- **Log:** `02-WF-log-WFestadio.md` (detalle corridas + evaluaciones)
- **Nodos:** `03-nodos-WFestadio.md` (configs propias del flujo)
- **Planes:** `PLANS/comparativa-sd15-vs-sdxl.md` (plan comparativo formal)
- **Specs:** `SPECS/` (especificaciones técnicas si aplica)
- **Salidas:** `salidas/n_01-{L}-{NN}.png`