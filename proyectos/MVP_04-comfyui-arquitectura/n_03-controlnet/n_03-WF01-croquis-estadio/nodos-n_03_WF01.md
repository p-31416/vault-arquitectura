---
tipo: indice-nodos
nivel: n_03-controlnet
fecha_creacion: 2026-07-19
ultima_actualizacion: 2026-07-19 21:00
tags: [indice, nodos, comfyui, controlnet, canny, scribble, depth]
---

# Registro de Nodos — por Workflow

## Nomenclatura de versiones

| Componente | Significado |
|------------|-------------|
| `v1.0.x` | Versiones del flujo canny baseline (deprecado). `x` = cambios de parámetros/prompt dentro de los mismos nodos |
| `v1.1a` | Primera bifurcación estructural: Scribble ControlNet. Nuevos nodos (cambia el pipeline) |
| `v1.1b` | Segunda bifurcación estructural: Dual Canny+Depth. Nuevos nodos (DA3) |
| `.x` (patch) | Parche dentro de un flujo. Ej: `v1.1a.0` → `v1.1a.1` (cambio de prompt, threshold, etc.) |
| `BAK_` | Última versión funcional de una línea. Congelada cuando se abre una nueva bifurcación |

## Workflows activos

| Workflow | Carpeta | Pipeline |
|----------|---------|----------|
| v1.1a — Scribble | `WF/WF_v1.1a_scribble/` | LoadImage → ImageScale → ControlNetApply → KSampler |
| v1.1b — Dual Canny+Depth | `WF/WF_v1.1b_dual/` | LoadImage → ImageScale → [Canny + Depth] → 2×ControlNetApply → KSampler |

## Workflows deprecados

| Workflow | Carpeta | Última versión funcional |
|----------|---------|--------------------------|
| v1.0.x — Canny baseline | `WF/BAK_WF_v1.0.x_canny/` | `BAK_v1.0.2__stadium-prompt-tuned.json` |

La documentación canónica de cada nodo vive en [[wiki/glosario/software/comfyui]].

→ [[index-n_03_WF01]] · [[prompts_log-n_03_WF01]] · [[workflow_log-n_03_WF01]] · [[backlog-n_03_WF01]]
