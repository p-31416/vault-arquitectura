---
tipo: indice
fase: concepto
fecha_creacion: 2026-09-30
ultima_actualizacion: 2026-09-30
tags: [mvp_04, n_06, indice]
---

# 01-index — WF_v5_fachada_hormigon_madera

Catálogo de versiones y configs mínimas. Detalle corridas en `02-WF-log-WFv5_fachada_hormigon_madera.md`. Configs propias en `03-nodos-WFv5.md`.

| Versión | Estado | Workflow | Prompts | Canny/CN/Denoise | Salidas |
|---|---|---|---|---|---|
| v5.0 | armado 30/09 | `workflow_fachada_hormigon_madera.json` (27 nodos) | Hamad hormigón visto + madera oscura x3 | `0.31/0.59`, `0.90`, `0.40` | `n_06-C-01/02/03.png` (pendiente) |

Configs mínimas: `architecturerealmix_v11`, `control_v11p_sd15_canny`, `euler_ancestral/karras 30 cfg7`, seeds 42/77/123, `ImageScale` orientado (768x512 / 512x768).
