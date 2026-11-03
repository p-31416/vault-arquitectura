---
tipo: indice
proyecto: MVP_04-comfyui-arquitectura
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [mvp_04, comfyui, marca-de-agua, indice, n_08]
idioma: es
---

# WF-marca-agua — índice

> Flujo v1.0 en construcción. R4 (validación contra `/object_info`) pendiente antes de la primera corrida.

## Versiones

| v | Fecha | JSON | Cambios | Estado |
|---|-------|------|---------|--------|
| 1.0 | 2026-11-02 | `workflow_marca_agua.json` | overlay marca+mask, posición fija, opacidad por blend | R4 pendiente |

## Config mínima

Foto en `input/` + marca PNG con alfa en `input/` · `scale_by` 0.25 · posición (40, 40) · `blend_factor` 0.3 · prefijo `n_08-marca-agua`.
