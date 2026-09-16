---
tipo: workflow-log
nivel: n_03-controlnet
workflow: workflow_v1.0.1__stadium-prompt.json
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-07-19 22:30
tags: [workflow-log, changelog, n_03, controlnet, canny, scribble, depth]
---

# Workflow Changelog — n_03 ControlNet (Canny / Scribble / Dual)

Tracks structural changes to the workflow graph. Each entry documents nodes added/removed/modified and links to functional backups (`BAK_*`).

Más nuevo → más arriba.

---

## v1.1 — Bifurcación: Scribble (v1.1a) ± Dual Canny+Depth (v1.1b)  |  2026-07-19 21:00

Per ADR-001, two parallel branches from v1.0.2 baseline. Numeración actualizada de `opt2`/`opt3` a `v1.1a`/`v1.1b`.

| Rama | Branch | ControlNet | Preprocessor | Status | Workflow |
|------|--------|-----------|-------------|--------|----------|
| **v1.1a** | Scribble | Scribble | Ninguno (croquis raw → CN directa) | ✅ Listo para test | [`WF_v1.1a.0__scribble.json`](WF/WF_v1.1a_scribble/WF_v1.1a.0__scribble.json) |
| **v1.1b** | Dual Canny+Depth | Canny + Depth | Canny (nativo) + DA3 Small | ⚠️ Listo, requiere probar DA3 | [`WF_v1.1b.0__dual-canny-depth.json`](WF/WF_v1.1b_dual/WF_v1.1b.0__dual-canny-depth.json) |

### v1.1a — Scribble ControlNet

**Tesis:** El croquis arquitectónico ES un scribble. Alimentarlo directo a un ControlNet Scribble debería guiar la forma sin forzar bordes lineales rígidos.

**Cambios vs v1.0.2:**

| Node | v1.0.2 | v1.1a | Why |
|------|--------|-------|-----|
| ControlNetLoader | `control_v11p_sd15_canny` | **`control_v11p_sd15_scribble`** | Scribble model trained on rough sketches |
| Canny | present | **removed** | Scribble model takes raw image, no preprocessing needed |
| ImageScale → ControlNetApply | via Canny | **direct** | ImageScale output feeds directly into ControlNetApplyAdvanced |

### v1.1b — Dual Canny + Depth

**Tesis:** Combinar Canny (bordes + forma) con Depth (volumen + profundidad) para guiar tanto la silueta como el espacio tridimensional del estadio.

**Nuevos nodos vs v1.0.2:**

| ID | Type | Role | Config |
|----|------|------|--------|
| 6 | ControlNetLoader | Depth CN model | `control_v11f1p_sd15_depth_fp16.safetensors` |
| 9 | LoadDA3Model | DA3 Small depth estimator | `depth_anything_3_small.safetensors`, fp16 |
| 10 | DA3Inference | Run depth estimation | res=504, mono mode |
| 11 | DA3Render | Render depth map → IMAGE | depth, v2_style normalization |
| 13 | ControlNetApplyAdvanced | Apply depth conditioning | strength=1.0, start=0, end=1.0 |

**Pipeline:**
```
LoadImage → ImageScale ──┬──→ Canny ──→ ControlNetApply (Canny) ──┐
                          │                                        │
                          └──→ DA3Inference → DA3Render ──→ ControlNetApply (Depth) ──→ KSampler
```

**Modelo descargado:** `depth_anything_3_small.safetensors` (131 MB, 81M params, Apache 2.0) → `models/geometry_estimation/`

### Backups

- [`BAK_v1.0.2__stadium-prompt-tuned.json`](WF/BAK_WF_v1.0.x_canny/BAK_v1.0.2__stadium-prompt-tuned.json) — v1.0.2 frozen before bifurcation

### Active workflows

- [`WF_v1.1a.0__scribble.json`](WF/WF_v1.1a_scribble/WF_v1.1a.0__scribble.json)
- [`WF_v1.1b.0__dual-canny-depth.json`](WF/WF_v1.1b_dual/WF_v1.1b.0__dual-canny-depth.json)

---

## v1.1a.1 — Interior Prompt + Scribble Reforzado  |  2026-07-19 22:00

Prompt reorientado a vista interior del estadio. v1.1a_02 reveló que el prompt exterior (`grandstands, stadium bowl, pitch`) ignoraba la composición del croquis, que es una vista desde el interior.

### Changes (v1.1a.0 → v1.1a.1)

| Node | Parameter | v1.1a.0 | v1.1a.1 | Why |
|------|-----------|---------|---------|-----|
| 3 CLIPTextEncode (pos) | prompt | `soccer stadium, football stadium architecture, grandstands, stadium bowl, pitch` | **`stadium interior view, looking up from the pitch, rows of empty seats rising on all sides, concrete grandstands, steel roof structure overhead, open sky above`** | Croquis es vista interior — prompt debe alinearse con la composición |
| 4 CLIPTextEncode (neg) | prompt | `...empty interior` | **`...exterior view, aerial view, bird eye view, facade, street level`** | Refuerzo explícito anti-vistas exteriores |
| 7 ControlNetApplyAdvanced | strength | 0.7 | **0.85** | Scribble más fuerte para que la composición del croquis domine sobre el prompt |
| 7 ControlNetApplyAdvanced | end_percent | 0.7 | **0.85** | Mantener influencia del Scribble hasta el 85% del denoising |
| 11 SaveImage | prefix | `n_03-v1.1a-scribble-` | **`n_03-v1.1a.1-scribble-`** | Prefijo actualizado para nueva versión |

### Backup

[`BAK_v1.1a.0__scribble.json`](WF/WF_v1.1a_scribble/BAK_v1.1a.0__scribble.json) — frozen before interior prompt change.

### Active workflow

[`WF_v1.1a.0__scribble.json`](WF/WF_v1.1a_scribble/WF_v1.1a.0__scribble.json) — actualizado in-place a v1.1a.1 parameters.

---

## v1.1a.2 — Scribble Max + Prompt Simplificado  |  2026-07-19 22:30

v1.1a.1 siguió generando vista exterior a pesar del prompt interior y strength 0.85. Diagnóstico: SD 1.5 asocia "stadium" fuertemente con vistas exteriores (sesgo del training data). Fix: quitar "stadium" del prompt, simplificar a descriptores visuales puros, y llevar strength/end a 1.0.

### Changes (v1.1a.1 → v1.1a.2)

| Node | Parameter | v1.1a.1 | v1.1a.2 | Why |
|------|-----------|---------|---------|-----|
| 3 CLIPTextEncode (pos) | prompt | `...stadium interior view, looking up from the pitch...stadium bowl interior...` | **`interior of a large sports venue, tiered seating rising on multiple levels, concrete grandstands, steel roof trusses overhead, open sky visible above, rows of empty seats`** | Eliminar "stadium" — SD 1.5 lo asocia a exterior. Descriptor visuales puros sin ambigüedad semántica. |
| 4 CLIPTextEncode (neg) | prompt | `...exterior view, aerial view...` | **`...exterior, outside, aerial, bird eye, facade, street, outdoor, building exterior, roof from above, cityscape`** | Negativo más agresivo contra conceptos exteriores |
| 7 ControlNetApplyAdvanced | strength | 0.85 | **1.0** | Scribble al máximo — la composición del croquis debe dominar completamente |
| 7 ControlNetApplyAdvanced | end_percent | 0.85 | **1.0** | Guía todo el denoising, sin zona libre |
| 11 SaveImage | prefix | `n_03-v1.1a.1-scribble-` | **`n_03-v1.1a.2-scribble-`** | Prefijo actualizado |

### Backup

[`BAK_v1.1a.1__interior-prompt.json`](WF/WF_v1.1a_scribble/BAK_v1.1a.1__interior-prompt.json) — frozen before v1.1a.2 changes.

### Active workflow

[`WF_v1.1a.0__scribble.json`](WF/WF_v1.1a_scribble/WF_v1.1a.0__scribble.json) — actualizado in-place a v1.1a.2 parameters.

---

## v1.0.2 — Stadium Prompt, ControlNet Tuned  |  2026-07-19 14:00

Kept stadium prompts, reverted ControlNet to previous stable values. v1.0.1_01 (v1.0.1) showed that strength 0.85 + end 1.0 forces Canny edge artifacts (broken lines), too rigidly attached to the linear croquis.

### Changes (v1.0.1 → v1.0.2)

| Node | Parameter | v1.0.1 | v1.0.2 | Why |
|------|-----------|--------|--------|-----|
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Parámetros clave\|3 Canny]] | low/high | 0.20 / 0.45 | **0.31 / 0.59** | Revert — thresholds from v1.0.0_02 avoided edge noise |
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Parámetros clave\|8 ControlNetApplyAdvanced]] | strength | 0.85 | **0.7** | Revert — 0.85 forced broken lines |
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Parámetros clave\|8 ControlNetApplyAdvanced]] | end_percent | 1.0 | **0.7** | Revert — last 30% free to fill line gaps |

### What stayed from v1.0.1

- Stadium prompts (positive + negative) — theme is correct per v1.0.1_01 evaluation

### Backups

- [`BAK_v1.0.1__stadium-prompt.json`](WF/BAK_WF_v1.0.x_canny/BAK_v1.0.1__stadium-prompt.json) — frozen before revert
- [`BAK_v1.0.0__baseline-canny.json`](WF/BAK_WF_v1.0.x_canny/BAK_v1.0.0__baseline-canny.json) — original baseline

### Active workflow (deprecated)

[`WF_v1.0.2__stadium-prompt-tuned.json`](WF/BAK_WF_v1.0.x_canny/WF_v1.0.2__stadium-prompt-tuned.json) — última versión funcional de la rama Canny (congelada). Todas las variantes v1.0.x ahora son `BAK_`.

---

## v1.0.1 — Stadium Prompt + Stronger ControlNet  |  2026-07-19 11:30

Added soccer stadium context to prompts and tightened ControlNet adherence for more precise output.

### Changes

| Node | Parameter | v1.0.0 | v1.0.1 | Why |
|------|-----------|--------|--------|-----|
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Parámetros clave\|3 Canny]] | low_threshold | 0.31 | **0.20** | Capture finer croquis lines |
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Parámetros clave\|3 Canny]] | high_threshold | 0.59 | **0.45** | More edge sensitivity |
| 5 CLIPTextEncode (pos) | prompt | `modern building, architectural photography` | `+soccer stadium, stadium architecture, grandstands, pitch` | Add stadium semantic context |
| 6 CLIPTextEncode (neg) | prompt | — | `+office building, residential, empty interior` | Reject non-stadium typologies |
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Parámetros clave\|8 ControlNetApplyAdvanced]] | strength | 0.7 | **0.85** | Stronger croquis adherence |
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Parámetros clave\|8 ControlNetApplyAdvanced]] | end_percent | 0.7 | **1.0** | Guide full denoising |

### Backup

[`BAK_v1.0.0__baseline-canny.json`](WF/BAK_WF_v1.0.x_canny/BAK_v1.0.0__baseline-canny.json) — frozen before this change.

### Active workflow (deprecated)

[`BAK_v1.0.1__stadium-prompt.json`](WF/BAK_WF_v1.0.x_canny/BAK_v1.0.1__stadium-prompt.json) — frozen, original v1.0.1. Toda la rama v1.0.x está deprecada.

---

## v1.0.0 — Baseline Canny  |  2026-07-19 10:00

Initial functional workflow: single ControlNet Canny pipeline. Croquis → edge map → guided render.

### Nodes

| ID | Type | Role | Config |
|----|------|------|--------|
| 1 | CheckpointLoaderSimple | Model loader | `architecturerealmix_v11.safetensors` |
| 2 | LoadImage | Image input | `croquis001.jpg` |
| 12 | [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Pipeline\|ImageScale]] | Resize to 512×512 | `lanczos`, `center` |
| 3 | [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Parámetros clave\|Canny]] | Edge detection | low=0.31, high=0.59 |
| 4 | [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Nodos específicos del workflow\|ControlNetLoader]] | CN model | `control_v11p_sd15_canny.safetensors` |
| 5 | CLIPTextEncode | Positive prompt | — |
| 6 | CLIPTextEncode | Negative prompt | — |
| 7 | EmptyLatentImage | Latent init | 512×512, batch=1 |
| 8 | [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/nodos#Parámetros clave\|ControlNetApplyAdvanced]] | CN applied | strength=0.7, start=0, end=0.7 |
| 9 | KSampler | Sampler | steps=30, cfg=7, euler, normal, seed=42, denoise=1 |
| 10 | VAEDecode | Decode | — |
| 11 | SaveImage | Output | prefix=`n_03` |

### Pipeline

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

### Fixes applied this version

- [[prompts_log-n_03_WF01#v1.0.0_02 2026-07-19 ✅\|v1.0.0_02]]: `nodes_canny.py` workaround for DirectML `F.pad` axis bug → kornia runs on CPU

### Backup

[`BAK_v1.0.0__baseline-canny.json`](WF/BAK_WF_v1.0.x_canny/BAK_v1.0.0__baseline-canny.json) — 39-line UI-format ComfyUI workflow

---

## Legend

| Nomenclatura | Significado | Ejemplo |
|-------------|-------------|---------|
| `v1.0.x` | Versiones del flujo canny baseline (deprecado). `x` = cambios de parámetros/prompt | `v1.0.0` → `v1.0.1` (prompt) |
| `v1.1a` / `v1.1b`... | Bifurcación estructural. Letra = variante de pipeline diferente | `v1.1a` (scribble), `v1.1b` (dual) |
| `.x` (patch) | Parche dentro de un flujo (cambia prompts, thresholds, etc.) | `v1.1a.0` → `v1.1a.1` |
| `BAK_` + versión | Último flujo funcional de una línea antes de bifurcar | `BAK_v1.0.2__stadium-prompt-tuned.json` |

Los backups dentro de una carpeta llevan prefijo `BAK_v{version}__{desc}.json`.
El nuevo desarrollo sigue como `WF_v{version}__{desc}.json`.

→ [[index-n_03_WF01]] — [[prompts_log-n_03_WF01]] — [[nodos-n_03_WF01]] — [[backlog-n_03_WF01]] — [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/adr/00-index|ADRs]]
