---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, wf-07, img2img, materialidad, gaudi]
idioma: es
---

# WF-07 — Geometría → piedra (img2img, denoise 0,55)

> JSON: `workflow_WF-07_sdxl.json` · 10 nodos · 1024×1024 · seed 77 · 30 steps · denoise 0,55
> Estado: sin validar contra servidor (R4 pendiente). `LoadImage` trae ruta `PONER-RUTA-boceto_geometria.png`.

## 1. Qué tipo de flujo es

**Img2img de baja libertad.** Toma una imagen de geometría limpia (viewport, axonometría, dibujo de líneas) y la viste de material gaudiano: piedra, ladrillo, trencadís. Con `denoise 0,55` la silueta manda y el modelo solo resuelve la piel.

Es el flujo del "puente": el mismo dibujo que sirve de base pasa a ser imagen de concurso sin redibujar. Hermano de WF-03, con el dial bajado para conservar la geometría.

## 2. Modelo

`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` — SDXL, VAE horneado, Open RAIL-M.

Alternativas: **RealVisXL v5.0** para materialidad de piedra, **Flux.2 klein 9B** con el LoRA `rhino-to-image` como camino paralelo en RunPod, y **ControlNet Union SDXL** cuando la geometría tiene que quedar clavada al dibujo. Comparativa en [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]].

## 3. Cadena de nodos

| # | Nodo | Doc | Función |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Modelo, CLIP y VAE |
| 8 | `LoadImage` | [doc](https://docs.comfy.org/built-in-nodes/LoadImage) | Geometría base desde `input/` |
| 9 | `ImageScale` | [doc](https://docs.comfy.org/built-in-nodes/ImageScale) | 1024×1024, `bilinear`, recorte centrado |
| 10 | `VAEEncode` | [doc](https://docs.comfy.org/built-in-nodes/VAEEncode) | Píxeles → latente |
| 2 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Positivo: "gaudi workflow pass, catenary geometry emerging from sketch lines, charcoal construction lines with photorealistic stone fill, medium intensity, branching columns taking shape, architectural render" |
| 3 | `CLIPTextEncode` | [doc](https://docs.comfy.org/built-in-nodes/CLIPTextEncode) | Negativo compartido del set |
| 5 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | `dpmpp_2m` / `karras`, 30 steps, cfg 4, **denoise 0,55**, seed 77 |
| 6 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Latente → píxeles |
| 7 | `SaveImage` | [doc](https://docs.comfy.org/built-in-nodes/SaveImage) | Prefijo `gx-WF07` |

## 4. El dial: denoise 0,55

| Denoise | Qué conserva | Cuándo usarlo |
|---|---|---|
| 0,40 | Geometría al pixel, piel muy fina | Cambiar solo el color del material |
| **0,55** | Silueta y proporciones, material nuevo | **Este WF**: la vista general del set |
| 0,65 | Material y luz nuevos, composición conservada | WF-03 (vista general con contexto) |
| 0,75 | Re-imagina y afloja la geometría | Exploración libre |

Por debajo de 0,45 la imagen se queda en el dibujo de origen con una capa de color. Por encima de 0,70 las catenarias empiezan a torcerse.

## 5. Cambios factibles

| Quiero | Cómo | Efecto |
|---|---|---|
| Material más fiel | `denoise` 0,55 → 0,45 | Geometría intacta, material sutil |
| Piedra más expresiva | `denoise` 0,55 → 0,62 | Juntas y patina más ricas |
| Trencadís dominante | Reforzar "trencadis mosaic" y bajar cfg a 3,5 | El color sube a primer plano |
| Ladrillo en vez de piedra | Cambiar el material del positivo | Otra familia de acabado |
| Geometría clavada | Sumar `ControlNetLoader` + `ControlNetApplyAdvanced` con Union SDXL | El dibujo manda sobre el denoise |
| Serie de materiales | Misma seed, tres positivos distintos | Tres pieles del mismo dibujo |

Combinar `denoise 0,55` con ControlNet es la vía más segura cuando la geometría tiene que quedar exacta y el material puede inventar.

## 6. Qué mirar en el resultado

Sombra propia del material, juntas con espesor real, patina distribuida sin manchas repetidas, catenarias idénticas al dibujo de entrada. Señal de falla: el material aparece como textura plana pegada sobre la silueta.

## 7. Pendientes

- R4 contra `/object_info`.
- Exportar la geometría base en alta resolución desde `mcp-plaza.3dm`.
- Cruce con el camino Flux 9B + LoRA en RunPod para la misma geometría.
