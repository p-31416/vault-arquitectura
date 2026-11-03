---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, wf-02, txt2img, interior, boveda]
idioma: es
---

# WF-02 — Interior de bóveda catenaria 1216×832

> JSON: `workflow_WF-02_sdxl.json` · 7 nodos · 1216×832 · seed 43 · 35 steps · cfg 4
> Estado: sin validar contra servidor (R4 pendiente).

## 1. Qué tipo de flujo es

**Txt2img horizontal de interior.** Es la vista que sostiene la lámina principal del pabellón: el espacio bajo la bóveda, con la luz entrando por el lucernario. Hereda el esqueleto de WF-01 y cambia prompt, encuadre, seed y steps.

## 2. Modelo

`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` — SDXL, VAE horneado, Open RAIL-M.

En este WF conviene además probar **RealVisXL v5.0**, que rinde mejor en interiores y materiales, y **RealArchmix XL v3.5** si se destraba la descarga. Ver [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]].

## 3. Cadena de nodos

| # | Nodo | Doc | Función |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Modelo, CLIP y VAE |
| 2 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: "catenary vault interior, trencadis mosaic light accents, warm concrete, volumetric light through skylight, fractal column forest, photorealistic, 8k uhd, masterpiece, architectural photography" |
| 3 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo compartido del set |
| 4 | `EmptyLatentImage` | [doc](https://docs.comfy.org/built-in-nodes/EmptyLatentImage) | 1216×832, batch 1 |
| 5 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` / `karras`, 35 steps, cfg 4, denoise 1,0, seed 43 |
| 6 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles |
| 7 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-WF02` |

## 4. Parámetros y por qué

| Parámetro | Valor | Razón |
|---|---|---|
| Resolución | 1216×832 | Relación 3:2 horizontal, la recomendada por el autor para paisaje |
| Steps | 35 | Un punto por encima del baseline: el interior tiene más detalle que resolver |
| CFG | 4 | Obediencia moderada, piel fotográfica |
| Seed | 43 | La semilla de la matriz: permite comparar contra las corridas ya hechas |

## 5. Cambios factibles

| Quiero | Cómo | Efecto |
|---|---|---|
| Ver el techo completo | 1216×832 → 1344×768 | Más aire arriba, menos suelo |
| Retrato | 832×1216 | Vista vertical para lámina de detalle |
| Luz más dramática | Añadir "god rays, hard shadows" al positivo y subir cfg a 5 | Contraste alto |
| Trencadís más presente | Reforzar "trencadis mosaic, broken tile" al inicio del prompt | El color entra como material |
| Un LoRA de interior | `LoraLoader` con `ArcvizXL_V01` (0,6–0,8) | Lenguaje de archviz |
| Más resolución | `UpscaleModelLoader` tras `VAEDecode` | Lámina A2 |

En SDXL conviene mantener la seed 43 mientras se cambia el modelo: así la diferencia que se ve es del modelo y no de la composición.

## 6. Qué mirar en el resultado

Continuidad de la bóveda (sin quiebres), columnas que llegan al suelo, luz volumétrica coherente con el lucernario, trencadís como material y no como textura pegada, escala del recinto creíble.

## 7. Pendientes

- R4 contra `/object_info`.
- Fila en la matriz con modelo, segundos y veredicto.
