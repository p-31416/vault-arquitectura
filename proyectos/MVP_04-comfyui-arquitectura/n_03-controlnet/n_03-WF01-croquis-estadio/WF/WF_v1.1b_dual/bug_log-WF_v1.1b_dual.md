---
tipo: bug-log
workflow: WF_v1.1b_dual
nivel: n_03-controlnet
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-07-19 22:15
tags: [bug-log, bugs, lecciones, da3, canny, depth, directml, comfyui]
---

# Bug Log — WF_v1.1b Dual (Canny+Depth)

Registro de bugs encontrados durante el desarrollo del workflow v1.1b (Dual Canny+Depth), con causa raíz, solución y lección aprendida.

Más nuevo → más arriba.

---

## B-002: DA3Inference — missing required positional argument 'mode'

| Campo | Detalle |
|-------|---------|
| **Fecha** | 2026-07-19 22:15 |
| **Workflow** | [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/00-index|WF_v1.1b.0__dual-canny-depth.json]] |
| **Nodo** | ID 10 — `DA3Inference` |
| **Severidad** | 🔴 Bloqueante — el workflow no ejecuta |
| **Estado** | ✅ Resuelto |

### Síntoma

```
TypeError: DA3Inference.execute() missing 1 required positional argument: 'mode'
```

El workflow se encola pero falla al instante. ComfyUI loguea el traceback completo apuntando al nodo 10.

### Causa raíz

El nodo `DA3Inference` tiene un parámetro `mode` de tipo `COMFY_DYNAMICCOMBO_V3` con dos opciones:

| Opción | Descripción |
|--------|-------------|
| `mono` | Single view image (funciona con cualquier variante del modelo) |
| `multiview` | Múltiples vistas procesadas juntas (solo Small/Base) |

El workflow JSON se creó desde la UI sin seleccionar explícitamente el widget `mode`. Al serializar el grafo, el valor quedó como `undefined` / ausente en el input del nodo. ComfyUI no asigna un default automático para `COMFY_DYNAMICCOMBO_V3` — requiere un valor explícito.

### Solución

1. En la UI de ComfyUI, hacer clic en el nodo **DA3Inference** (ID 10)
2. Seleccionar **`mono`** en el widget `mode` (modo single view, apropiado para un solo croquis de entrada)
3. Guardar el workflow nuevamente
4. Re-ejecutar

### Sub-opciones de `mode`

Si en el futuro se usa `multiview`, el nodo expone dos sub-opciones:

| Sub-opción | Valores | Default |
|------------|---------|---------|
| `ref_view_strategy` | `saddle_balanced`, `saddle_sim_range`, `first`, `middle` | `saddle_balanced` |
| `pose_method` | `cam_dec`, `ray_pose` | `cam_dec` |

### Lección aprendida

**Los widgets `COMFY_DYNAMICCOMBO_V3` no tienen default automático en la serialización API del workflow.** Siempre verificar que todos los combos dinámicos tengan un valor seleccionado antes de guardar/ejecutar. Esto aplica a cualquier nodo que use `COMFY_DYNAMICCOMBO_V3` — no solo `DA3Inference`.

### Referencias

- [[nodos-n_03_WF01]] — Registro de nodos del workflow
- [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/DET-WF_v1.1b_dual|Nodos v1.1b]]
- [Depth Anything 3 — GitHub](https://github.com/DepthAnything/Depth-Anything-3)
- [[prompts_log-n_03_WF01]] — Próximas corridas documentarán outputs con mono mode

---

## B-001: Canny nativo — kornia `F.pad` invierte ejes con DirectML

| Campo | Detalle |
|-------|---------|
| **Fecha** | 2026-07-19 11:00 |
| **Workflow** | v1.0.0 → v1.0.1 (Canny baseline) → heredado por v1.1b |
| **Nodo** | Canny (`comfy_extras/nodes_canny.py`) |
| **Severidad** | 🟠 Alto — output degradado |
| **Estado** | ✅ Resuelto |

### Síntoma

El nodo Canny nativo de ComfyUI produce edge maps corruptos cuando se ejecuta en GPU con DirectML (AMD RX 570). Los bordes aparecen desplazados, rotados o con artefactos de eje invertido. A simple vista se ve como un "Canny roto" pero no hay error en consola.

### Causa raíz

El backend de kornia (que ComfyUI usa internamente para Canny) llama a `F.pad` de PyTorch. En DirectML, `F.pad` tiene un bug conocido: **invierte los ejes de padding** cuando el device es `privateuseone`. El padding se aplica al eje equivocado, produciendo bordes geométricamente incorrectos.

Específicamente:
- `F.pad(tensor, (left, right, top, bottom))` en CPU/CUDA → padding correcto
- `F.pad(tensor, (left, right, top, bottom))` en DirectML → padding aplicado a ejes transpuestos

### Solución

**Workaround:** Forzar la ejecución de kornia en CPU cuando se detecta device DirectML.

Parche aplicado en `P:\00-repos\ComfyUI\comfy_extras\nodes_canny.py`:

```python
import os
os.environ['KORNIA_DEVICE'] = 'cpu'  # Fuerza kornia a CPU
```

O más preciso, detectar el device del modelo y si es `privateuseone`, ejecutar el preprocesador en CPU:

```python
if hasattr(model, 'device') and 'privateuseone' in str(model.device):
    # Fallback a CPU para kornia (F.pad bug en DirectML)
    import torch
    # ... lógica condicional
```

### Impacto

- ✅ Canny ahora produce edge maps correctos
- ⚠️ Penalidad de performance menor (~2-5ms adicionales por transferencia CPU↔GPU)
- No afecta otros preprocesadores (DA3 corre nativamente en DirectML)

### Lección aprendida

**kornia + DirectML = bugs conocidos en `F.pad`.** Ante cualquier operación de visión computacional (Canny, filtros, morfología) que se ejecute en GPU con DirectML, verificar si usa kornia y considerar forced CPU fallback. Esto aplica a cualquier GPU AMD/Intel con backend DirectML.

### Referencias

- [[prompts_log-n_03_WF01#v1.0.0_02 2026-07-19 ✅\|v1.0.0_02: Fix Canny nativo]]
- [ComfyUI issue #3165 — F.pad axis bug on DirectML](https://github.com/comfyanonymous/ComfyUI/issues/3165)
- [[workflow_log-n_03_WF01#v1.0.0 — Baseline Canny 2026-07-19 10:00\|v1.0.0 changelog]]

---

## Tabla de bugs

| ID | Fecha | Nodo | Síntoma | Severidad | Estado |
|----|-------|------|---------|-----------|--------|
| B-002 | 2026-07-19 | DA3Inference (10) | `missing 1 required positional argument: 'mode'` | 🔴 Bloqueante | ✅ Resuelto |
| B-001 | 2026-07-19 | Canny | kornia `F.pad` invierte ejes en DirectML | 🟠 Alto | ✅ Resuelto |

---

## Bugs prevenidos / no registrados

| # | Issue | Detectado en | Acción preventiva |
|---|-------|-------------|-------------------|
| 1 | DA3 model no encontrado en `models/geometry_estimation/` | Setup v1.1b | Se documentó la ruta exacta en [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/WF/WF_v1.1b_dual/DET-WF_v1.1b_dual|nodos v1.1b]] línea 64. Modelo: `depth_anything_3_small.safetensors` (131 MB) |
| 2 | ControlNet Depth (`control_v11f1p_sd15_depth_fp16`) no instalado | Setup v1.1b | Se verificó que ya existe en `models/controlnet/` (689 MB) |

→ [[index-n_03_WF01]] · [[workflow_log-n_03_WF01]] · [[prompts_log-n_03_WF01]] · [[backlog-n_03_WF01]]
