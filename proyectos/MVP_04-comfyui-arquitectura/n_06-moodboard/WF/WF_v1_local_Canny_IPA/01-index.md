---
tipo: proyecto
fase: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [mvp_04, n_06, indice]
---

# 01-index — WF_v1_local_Canny_IPA

## Versiones

| Ver | Archivo | Cambio | Estado |
|---|---|---|---|
| v1 | `workflow_moodboard_local.json` | L1 Canny local desde txt2img Realmimix | Armado, enqueue pendiente (Comfy caído) |

## Config mínima L1

Checkpoint `architecturerealmix_v11.safetensors` + `control_v11p_sd15_canny.safetensors` + ImageScale lanczos 512 + Canny 0.31/0.59 + CN 0.85/0.0-0.80 + euler_ancestral/karras/30/cfg 7/seed 42 + prefijo `n_06-B-01`.

## Nomenclatura salidas

`salidas/n_06-B-01.png` (B = variación prompt). Letra B según `reglas-workflows-comfy.md:93-102`.
