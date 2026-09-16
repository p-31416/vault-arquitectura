---
tipo: backlog
workflow: WF-vivienda
nivel: n_01-txt2img
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [backlog, pendientes, vivienda, sdxl, juggernaut]
---

# 04-backlog — Pruebas y Iteraciones Pendientes WF-vivienda

---

## Prioridad Alta — Baseline y Validación

| ID | Título | Descripción | Origen | Estado |
|----|--------|-------------|--------|--------|
| B-01 | **Baseline A — 3 corridas seed 42/43/44 (SDXL)** | Validar consistencia Juggernaut XL v9, misma config, 3 seeds | Plan | ⬜ Pendiente |
| B-02 | **Hires Fix 1.5× + Remacri (SDXL)** | Agregar Hires Fix en KSampler (denoise 0.35, 15 steps, Remacri) | Plan SDXL | ⬜ Pendiente (req. modelo) |
| B-03 | **Comparativa tipología** | Mismo config: estadio (WF-estadio) vs vivienda unifamiliar (WF-vivienda) | Cross-WF | ⬜ Pendiente |

---

## Prioridad Media — Exploración Parámetros (Letra C)

| ID | Título | Descripción | Origen | Estado |
|----|--------|-------------|--------|--------|
| C-01 | **CFG sweep SDXL** | CFG 3, 4, 5, 6 — Juggernaut XL sweet spot vivienda | Plan | ⬜ Pendiente |
| C-02 | **Sampler comparison** | dpmpp_2m vs dpmpp_2m_sde vs euler_a — mismo seed | Plan | ⬜ Pendiente |
| C-03 | **Steps sweep** | 25, 30, 35, 40, 50 — costo/beneficio | Plan | ⬜ Pendiente |
| C-04 | **Scheduler SDXL** | karras vs exponential vs simple — coherencia volumétrica | Plan | ⬜ Pendiente |
| C-05 | **Resolución SDXL nativa** | 1024×1024 vs 1216×832 vs 832×1216 — mismo seed | Plan | ⬜ Pendiente |

---

## Prioridad Media — Variaciones Prompt (Letra B)

| ID | Título | Descripción | Origen | Estado |
|----|--------|-------------|--------|--------|
| B-01 | **Atmósfera golden hour** | `golden hour, warm directional light, long shadows` | Plan | ⬜ Pendiente |
| B-02 | **Atmósfera nublado/difusa** | `overcast, soft diffuse light, no harsh shadows` | Plan | ⬜ Pendiente |
| B-03 | **Atmósfera noche** | `twilight, exterior lights on, warm interior glow spilling out` | Plan | ⬜ Pendiente |
| B-04 | **Estilo brutalista** | `brutalist house, exposed concrete, raw texture, massive forms` | Plan | ⬜ Pendiente |
| B-05 | **Estilo high-tech** | `high-tech architecture, steel glass curtain wall, exposed structure` | Plan | ⬜ Pendiente |
| B-06 | **Contexto urbano denso** | `urban infill, narrow lot, party walls, rooftop terrace, city context` | Plan | ⬜ Pendiente |

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
- [ ] **Variantes tipología vivienda** — unifamiliar vs colectiva vs torre vs rural

---

## Dependencias externas

| Dependencia | Estado | Bloquea |
|-------------|--------|---------|
| `4x_foolhardy_Remacri.pth` descargado | ⬜ Pendiente | Hires Fix, Upscale 4×, Pipeline entrega |
| `4x-ClearRealityV1.pth` descargado | ⬜ Pendiente | Upscale alternativo fotorrealista |

---

## Referencias cruzadas

- **Index:** `01-index.md` (tabla versiones + configs)
- **Log:** `02-WF-log-WFvivienda.md` (detalle corridas + evaluaciones)
- **Nodos:** `03-nodos-WFvivienda.md` (configs propias del flujo)
- **Planes:** `PLANS/` (planes de test formales)
- **Specs:** `SPECS/` (especificaciones técnicas si aplica)
- **Salidas:** `salidas/n_01-{L}-{NN}.png`