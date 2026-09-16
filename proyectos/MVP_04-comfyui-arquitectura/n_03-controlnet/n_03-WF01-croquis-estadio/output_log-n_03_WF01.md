---
tipo: output-log
workflow: n_03-WF01-croquis-estadio
nivel: n_03-controlnet
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-07-19
tags: [output-log, controlnet, canny, scribble, depth, da3, estadio, croquis]
---

# Output Log — n_03-WF01: Croquis → Render de Estadio

Pipeline: croquis arquitectónico → render fotorrealista de estadio guiado por ControlNet.

Más nuevo → más arriba.

## Nomenclatura de outputs

```
n_03-v{version}_{corrida}.png
```

| Componente | Descripción | Ejemplo |
|------------|-------------|---------|
| `n_03` | Prefijo del proyecto (n_03-controlnet) | `n_03` |
| `v{version}` | Versión exacta del workflow | `v1.0.0`, `v1.1a`, `v1.1b` |
| `{corrida}` | Número secuencial de corrida para esa versión | `01`, `02` |

Ejemplos: `n_03-v1.1a_01.png`, `n_03-v1.0.0_02.png`.

---

## 1.1b — Dual Canny+Depth

### 1.1b-index

| Rama | ControlNet 1 | ControlNet 2 | Preprocesador | Pipeline |
|------|-------------|-------------|---------------|----------|
| v1.1b | Canny (strength=0.3) | Depth (strength=1.0) | Canny nativo + DA3 Small | LoadImage → ImageScale → [Canny + DA3Inference → DA3Render] → 2×ControlNetApply → KSampler |

| Parámetros base | Valor |
|----------------|-------|
| checkpoint | architecturerealmix_v11.safetensors |
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |
| prompt | stadium (arquitectura + estadio + grandstands) |

**Input:** croquis001.jpg ([inputs-croquis/croquis001.jpg](inputs-croquis/croquis001.jpg))

**Modelo Depth:** Depth Anything 3 Small (`depth_anything_3_small.safetensors`, 131 MB, `models/geometry_estimation/`)
**Modo DA3:** `mono` (single view, res=504)

**Bug conocido resuelto:** [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/bug_log-WF_v1.1b_dual#B-002 DA3Inference missing required positional argument mode\|B-002: DA3Inference mode faltante]]

### 1.1b-outputs

| Variante | Fecha | Prompt | Seed | Tiempo | Output | Evaluación |
|----------|-------|--------|------|--------|--------|------------|
| — | — | Pendiente | — | — | — | Pendiente de ejecución tras fix B-002 |

> Próxima corrida: `n_03-v1.1b_01`. Una vez ejecutado, agregar entrada abajo con imagen y evaluación.

---

## 1.1a — Scribble ControlNet

### 1.1a-index

| Rama | ControlNet | Preprocesador | Pipeline |
|------|-----------|-------------|----------|
| v1.1a | Scribble (strength=1.0) | Ninguno (croquis raw → CN directa) | LoadImage → ImageScale → ControlNetApply → KSampler |

| Parámetros base | Valor |
|----------------|-------|
| checkpoint | architecturerealmix_v11.safetensors |
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |

**Input:** croquis001.jpg

**Tesis:** El croquis arquitectónico ES un scribble. Alimentarlo directo a un ControlNet Scribble guía la forma sin forzar bordes lineales rígidos.

### 1.1a-outputs

| Versión | Fecha | Seed | Strength | guidance_end | Prompt | Tiempo | Output | Evaluación |
|---------|-------|------|----------|-------------|--------|--------|--------|------------|
| `v1.1a_02` | 2026-07-19 22:00 | — | 0.7 | 0.7 | 🏟️ stadium (exterior) | — | ![v1.1a_02](outputs-salidas/n_03-v1.1a_02.png) | ❌ No sigue el croquis — prompt exterior vs croquis interior → fix en v1.1a.1 |
| `v1.1a_01` | 2026-07-19 17:30 | 42 | 0.7 | 0.7 | 🏟️ stadium | ~90s | ![v1.1a_01](outputs-salidas/n_03-v1.1a_01.png) | Pendiente — revisar si el scribble guía la forma sin forzar bordes lineales rotos |

**Referencia detallada:** [[prompts_log-n_03_WF01#n_03-v1.1a-scribble-01 2026-07-19 17:30 ✅]]

---

## 1.0.x — Canny Baseline (deprecado)

### 1.0-index

| Rama | ControlNet | Preprocesador | Pipeline |
|------|-----------|-------------|----------|
| v1.0.x | Canny (strength=0.7) | Canny nativo (kornia CPU workaround) | LoadImage → ImageScale → Canny → ControlNetApply → KSampler |

| Parámetros base | Valor |
|----------------|-------|
| checkpoint | architecturerealmix_v11.safetensors |
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |

**Input:** croquis001.jpg

**Estados del workflow:**
| Versión | Cambio | Archivo |
|---------|--------|---------|
| v1.0.0 | Baseline — Canny preprocesado externamente | [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/BAK_v1.0.0__baseline-canny.json]] |
| v1.0.1 | Stadium prompt + Canny más sensible (0.20/0.45) + strength 0.85 | [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/BAK_v1.0.1__stadium-prompt.json]] |
| v1.0.2 | Stadium prompt + ControlNet revertido (strength 0.7, end 0.7) | [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/BAK_WF_v1.0.x_canny/BAK_v1.0.2__stadium-prompt-tuned.json]] |

### 1.0-outputs

| Versión | Fecha | Seed | Canny low/high | CN strength | CN end | Prompt | Tiempo | Output | Evaluación |
|---------|-------|------|---------------|-------------|--------|--------|--------|--------|------------|
| `v1.0.2_01` | 2026-07-19 15:00 | 42 | 0.31 / 0.59 | 0.7 | 0.7 | 🏟️ stadium | ~88s | ![v1.0.2_01](outputs-salidas/n_03-v1.0.2_01.png) | Pendiente — verificar que las líneas cortadas desaparecieron |
| `v1.0.1_01` | 2026-07-19 14:00 | 42 | 0.20 / 0.45 | 0.85 | 1.0 | 🏟️ stadium | ~97s | ![v1.0.1_01](outputs-salidas/n_03-v1.0.1_01.png) | ⚠️ Líneas cortadas del Canny por strength alto |
| `v1.0.0_03` | 2026-07-19 12:30 | random | 0.31 / 0.59 | 0.7 | 0.7 | modern building | ~92s | ![v1.0.0_03](outputs-salidas/n_03-v1.0.0_03.png) | Verificación de estabilidad del fix Canny |
| `v1.0.0_02` | 2026-07-19 11:00 | 42 | 0.31 / 0.59 | 0.7 | 0.7 | modern building | ~97s | ![v1.0.0_02](outputs-salidas/n_03-v1.0.0_02.png) | Fix Canny nativo — kornia en CPU por bug DirectML |
| `v1.0.0_01` | 2026-07-19 10:00 | 42 | 0.31 / 0.59 (externo) | 0.7 | 0.7 | modern building | ~111s | ![v1.0.0_01](outputs-salidas/n_03-v1.0.0_01.png) | Baseline — Canny preprocesado externamente |

**Referencia detallada:** [[prompts_log-n_03_WF01]]

---

## Referencias cruzadas

| Archivo | Contenido |
|---------|-----------|
| [[prompts_log-n_03_WF01]] | Log detallado de cada corrida (parámetros, prompts, evaluación) |
| [[workflow_log-n_03_WF01]] | Changelog del grafo del workflow |
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1a_scribble/bug_log-WF_v1.1a_scribble|bug_log-WF_v1.1a_scribble]] | Bug log de Scribble (v1.1a) |
| [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/bug_log-WF_v1.1b_dual|bug_log-WF_v1.1b_dual]] | Bug log de Dual Canny+Depth (v1.1b) |
| [[backlog-n_03_WF01]] | Próximas pruebas pendientes |
| [[index-n_03_WF01]] | Índice general del proyecto |
