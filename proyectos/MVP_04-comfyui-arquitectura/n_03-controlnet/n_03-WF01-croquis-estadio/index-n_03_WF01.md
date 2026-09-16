---
tipo: index
nivel: n_03-WF01-croquis-estadio
wf: n_03-controlnet
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-07-19 22:00
tags: [index, controlnet, canny, scribble, depth, da3, mvp04, estadio, croquis]
---

# n_03 — ControlNet: Croquis de Estadio

Render desde croquis arquitectónico guiado por ControlNet.

## Nomenclatura de versiones

| Formato | Significado | Ejemplo |
|---------|-------------|---------|
| `v1.0.x` | Ajustes de parámetros/prompt (mismos nodos) | `v1.0.0` → `v1.0.1` (cambio de prompt) |
| `v1.1` + letra | Bifurcación estructural (nuevos nodos) | `v1.1a` (scribble), `v1.1b` (dual) |
| `.x` (patch) | Parche dentro de un flujo | `v1.1a.0` → `v1.1a.1` |

## Índice

- [[prompts_log-n_03_WF01]] — Log detallado de corridas (parámetros, prompts, evaluación)
- [[output_log-n_03_WF01]] — Output log: todos los outputs organizados por versión (1.0, 1.1a, 1.1b)
- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1a_scribble/bug_log-WF_v1.1a_scribble|bug_log-WF_v1.1a_scribble]] — Bug log de Scribble (v1.1a)
- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/bug_log-WF_v1.1b_dual|bug_log-WF_v1.1b_dual]] — Bug log de Dual Canny+Depth (v1.1b) — DA3 mode, kornia + DirectML
- [[workflow_log-n_03_WF01]] — Changelog del grafo del workflow
- [[backlog-n_03_WF01]] — Próximas pruebas pendientes
- [[nodos-n_03_WF01]] — Índice de nodos por workflow
- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/adr/00-index|ADRs]] — Decisiones arquitectónicas

## Workflows activos

| Carpeta | Workflow | Pipeline |
|---------|----------|----------|
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1a_scribble/00-index|WF_v1.1a_scribble]] | Scribble (v1.1a) | Scribble ControlNet sin preprocesador |
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/00-index|WF_v1.1b_dual]] | Dual Canny+Depth (v1.1b) | Canny + Depth Anything 3 |

## Workflows deprecados

| Carpeta | Workflow | Última versión |
|---------|----------|----------------|
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/00-index|BAK_WF_v1.0.x_canny]] | Canny baseline (v1.0.x) | `BAK_v1.0.2__stadium-prompt-tuned.json` |

## Variantes ejecutadas

| Versión | Fecha | Cambio | Config | Imagen |
|---------|-------|--------|--------|--------|
| `v1.1a_02` | 2026-07-19 22:00 | Scribble — prompt exterior vs croquis interior → fix v1.1a.1 | steps=30, cfg=7, euler, normal, 512×512, strength=0.7 | ![v1.1a_02](outputs-salidas/n_03-v1.1a_02.png) |
| `v1.1a_01` | 2026-07-19 17:30 | Primer test Scribble — croquis directo al CN | steps=30, cfg=7, euler, normal, 512×512, seed=42, strength=0.7 | ![v1.1a_01](outputs-salidas/n_03-v1.1a_01.png) |
| `v1.0.0_01` | 2026-07-19 10:00 | Baseline — Canny preprocesado externamente | steps=30, cfg=7, euler, normal, 512×512, seed=42 | ![v1.0.0_01](outputs-salidas/n_03-v1.0.0_01.png) |
| `v1.0.0_02` | 2026-07-19 11:00 | Fix Canny nativo — kornia en CPU por bug DirectML `F.pad` | steps=30, cfg=7, euler, normal, 512×512, seed=42 | ![v1.0.0_02](outputs-salidas/n_03-v1.0.0_02.png) |
| `v1.0.0_03` | 2026-07-19 12:30 | Re-queue manual desde UI — seed random, verifica estabilidad del fix | steps=30, cfg=7, euler, normal, 512×512, seed=random | ![v1.0.0_03](outputs-salidas/n_03-v1.0.0_03.png) |
| `v1.0.1_01` | 2026-07-19 14:00 | Prompt de estadio + Canny más sensible + CN strength 0.85 / end 1.0 | steps=30, cfg=7, euler, normal, 512×512, seed=42, canny=0.20/0.45, strength=0.85 | ![v1.0.1_01](outputs-salidas/n_03-v1.0.1_01.png) |
| `v1.0.2_01` | 2026-07-19 15:00 | Stadium prompt + ControlNet revertido (strength 0.7, end 0.7, canny 0.31/0.59) | steps=30, cfg=7, euler, normal, 512×512, seed=42 | ![v1.0.2_01](outputs-salidas/n_03-v1.0.2_01.png) |

### Nomenclatura

`n_03-v{version}_{corrida}.png` donde `version` es la versión del workflow (v1.0.0, v1.1a, v1.1b) y `corrida` es el número secuencial dentro de esa versión.

---

## Flujo de trabajo

### v1.0.x — Canny (deprecado)

```
CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────┤
    └──vae──────────────────┐   │
                            │   │
LoadImage ──► ImageScale ──► Canny ──┐
                │           │       │
ControlNetLoader ──cn───────┤       │
                │           │       │
CLIPTextEncode (pos) ───────┤       │
CLIPTextEncode (neg) ───────┤       │
                            ▼       ▼
ControlNetApplyAdvanced ──► KSampler ──► VAEDecode ──► SaveImage
```

### v1.1a — Scribble

```
LoadImage → ImageScale ──→ ControlNetApply (Scribble) ──→ KSampler ──→ VAEDecode ──→ SaveImage
```

- **ControlNet:** `control_v11p_sd15_scribble.safetensors`
- **Sin preprocesador** — el croquis se alimenta directo al modelo Scribble

### v1.1b — Dual Canny+Depth

```
LoadImage → ImageScale ──┬──→ Canny ──→ ControlNetApply (Canny) ──┐
                          │                                        │
                          └──→ DA3Inference → DA3Render ──→ ControlNetApply (Depth) ──→ KSampler
```

- **ControlNet 1:** `control_v11p_sd15_canny.safetensors`
- **ControlNet 2:** `control_v11f1p_sd15_depth_fp16.safetensors`
- **Depth estimator:** Depth Anything 3 Small (`depth_anything_3_small.safetensors`, 131 MB)

## Recursos

- **Modelo:** `architecturerealmix_v11.safetensors`
- **ControlNet Canny:** `control_v11p_sd15_canny.safetensors`
- **ControlNet Scribble:** `control_v11p_sd15_scribble.safetensors`
- **ControlNet Depth:** `control_v11f1p_sd15_depth_fp16.safetensors`
- **Depth model:** `depth_anything_3_small.safetensors` (131 MB, `models/geometry_estimation/`)
- **Hardware:** AMD RX 570 8GB (DirectML), ~88–111s
- **Input:** `inputs-croquis/croquis001.jpg`
