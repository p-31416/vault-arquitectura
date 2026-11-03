---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, wf-06, txt2img, detalle, constructivo, jurado]
idioma: es
---

# WF-06 — Detalle constructivo 1024² (criterio de jurado)

> JSON: `workflow_WF-06_sdxl.json` · 7 nodos · 1024×1024 · seed 6 · 30 steps · cfg 4
> Estado: sin validar contra servidor (R4 pendiente).

## 1. Qué tipo de flujo es

**Txt2img de detalle.** Primer plano de la unión entre columna ramificada y estructura: encuentro de piedra y acero, con la lógica tectónica por delante de la apariencia. Es la imagen que responde a la pregunta que hace un jurado técnico: *¿cómo se construye?*

El encuadre se cierra sobre la junta, la junta se lee como material y la pieza de unión aparece como elemento diseñado.

## 2. Modelo

`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` — SDXL, VAE horneado, Open RAIL-M.

Alternativa: **RealVisXL v5.0**, más nítido en superficies de piedra y hormigón. Para forzar la geometría del detalle, **ControlNet Union SDXL** sobre el mismo WF. Comparativa en [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]].

## 3. Cadena de nodos

| # | Nodo | Doc | Función |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Modelo, CLIP y VAE |
| 2 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: "close-up constructive detail, branching fractal column joint, stone and steel connection, tectonic logic over appearance, raking light, architectural photography, 8k uhd, masterpiece" |
| 3 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo del set **+ "decorative only"** |
| 4 | `EmptyLatentImage` | [doc](https://docs.comfy.org/built-in-nodes/EmptyLatentImage) | 1024×1024, batch 1 |
| 5 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` / `karras`, 30 steps, cfg 4, denoise 1,0, seed 6 |
| 6 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles |
| 7 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-WF06` |

## 4. Parámetros y por qué

| Parámetro | Valor | Razón |
|---|---|---|
| Resolución | 1024×1024 | Cuadrado del plano de detalle |
| Steps | 30 | Base del set: la junta se resuelve con detalle del modelo, no con pasos extra |
| CFG | 4 | El prompt ya nombra "tectonic logic over appearance"; subir cfg rigidiza el material |
| Seed | 6 | Fija las juntas y la dirección de la luz rasante |
| Negativo extra | `decorative only` | Empuja el resultado hacia la lógica constructiva y lo aleja del ornamento |

## 5. Cambios factibles

| Quiero | Cómo | Efecto |
|---|---|---|
| Detalle más extremo | Añadir "extreme macro, 1:1 scale" | Primer plano de la veta del material |
| Segundo detalle | Cambiar "branching fractal column joint" por "arch keystone and roof beam" | Otra junta |
| Tercer detalle | "trencadis mosaic panel fixing system" | Detalle de revestimiento |
| Geometría forzada | `ControlNetLoader` + `ControlNetApplyAdvanced` con Union SDXL sobre un croquis de la junta | La junta sigue el dibujo |
| Luz de taller | "raking light" → "diffuse overcast light" | Menos contraste, más lectura de material |
| Lámina A3 | `UpscaleModelLoader` tras `VAEDecode` | Detalle imprimible |

Una junta por corrida. El detalle constructivo se lee mejor cuando muestra una sola condición.

## 6. Qué mirar en el resultado

Continuidad de la junta, espesor de material creíble, presencia de la pieza metálica sin inventar tornillos, textura que se lee al tacto, sombra rasante que describe la forma. Señal de falla: la junta "se derrite" y el material pierde el borde.

## 7. Pendientes

- R4 contra `/object_info`.
- Dibujar una junta de referencia si se activa ControlNet Union.
