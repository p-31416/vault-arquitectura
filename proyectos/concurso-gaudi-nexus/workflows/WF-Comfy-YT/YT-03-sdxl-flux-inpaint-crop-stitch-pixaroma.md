---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, sdxl, flux, inpainting, crop-stitch, juggernaut]
idioma: es
---

# YT-03 — SDXL y Flux Inpainting con CropAndStitch (pixaroma Ep19)

> Video: "ComfyUI Tutorial Series: Ep19 - SDXL & Flux Inpainting Tips with ComfyUI" · canal pixaroma · 2024-11-03 · https://www.youtube.com/watch?v=EJ7LhNS67KM · Serie tutorial de ComfyUI, episodio 19. Transcripción vía subtítulos y espejo bilibili con lista de materiales.
> Lo útil para el estudio: recorta solo la zona enmascarada antes de samplear y la vuelve a pegar sin tocar el resto. Acelera y fija resolución de trabajo.

## 1. Qué aporta el video

Inpainting SDXL y Flux para retocar fotos e ilustraciones: corregir detalles, borrar intrusos y agregar elementos con prompt. Nodos `Inpaint Crop` + `Inpaint Stitch` (pack `ComfyUI-Inpaint-CropAndStitch`): el crop recorta alrededor de la máscara con contexto configurable y resolución forzada, el stitch lo devuelve al original con blend automático. El resto intacto sale sin pasar por VAE.

Flujos dedicados del vault que ya aplican la base: [[proyectos/MVP_04.02-comfyui-arquitectura/WF-02-inpainting-ventanas/WF-02-inpainting-ventanas|WF-02]] (ventanas, lecciones de máscara) y [[proyectos/MVP_04.02-comfyui-arquitectura/WF-06-inpaint-outpaint/WF-06-inpaint-outpaint|WF-06]] (inpaint 3.x + outpaint 4.x con modelo inpainting dedicado). Este YT-03 suma el recorte previo para alta resolución y bajo VRAM.

## 2. JSON

- Sin archivo del autor en el video: se trabaja con el workflow ejemplo del repo del pack y reconstrucción local.
- Ejemplo oficial del pack (arrastrable a ComfyUI): `inpaint-cropandstitch_example_workflow.json` en https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch
- Borrador Nexus listo SIN correr: `workflow_YT-03-inpaint-crop-stitch.json` (misma carpeta, formato UI arrastrable). Adaptado del ejemplo oficial: checkpoint Juggernaut XL inpainting, foto `fachada-01.png`, crop forzado a 1024 con contexto x1.2 y blend 32, prompts T1 árbol, KSampler `dpmpp_2m` + `karras`, 30 pasos, cfg 3.5, denoise 0.9, `InpaintModelConditioning` con `noise_mask true`, salida `gx-YT03-crop-stitch`. Requisitos previos: pack instalado + checkpoint en `models/checkpoints`.

## 3. Modelo y nodos extra

| Pieza | Dato del video / espejo | Link / estado |
|---|---|---|
| Checkpoint SDXL inpainting | `juggernautXL_juggernautX_inpainting.safetensors`, fp16, 6,46 GB, base SDXL 1.0 Inpainting, hash AutoV2 `B1689257E6`, Clip Skip 2 | https://civitai.com/models/403361?modelVersionId=456538 (versión X Inpaint, verificado) |
| Custom nodes | `ComfyUI-Inpaint-CropAndStitch` (`Inpaint Crop Improved` + `Inpaint Stitch Improved`), instalación vía ComfyUI-Manager, reinicio + refresco de navegador | https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch (1202 stars, licencia GPL-3.0) · registro https://registry.comfy.org/nodes/comfyui-inpaint-cropandstitch |
| KSampler video | `DPM++ 2M` + `Karras`, 30+ pasos (hasta 80 a gusto), CFG 2–6, denoise 0,8 de arranque (0,9 si sale tímido) | contrasta con WF-06 (`euler`, cfg 7, denoise 1.0) y WF-02 (denoise 0,8–1,0) |
| Licencia checkpoint | Derivado de Juggernaut XL, verificar ficha Civitai antes de uso comercial | ver ficha del link Civitai |

Instalación: Manager → buscar `ComfyUI-Inpaint-CropAndStitch` → Install → Restart + refresh. Alternativa manual: `git clone https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch.git` en `custom_nodes/`.

## 4. Nodos y docs oficiales

| # | Nodo | Doc | Función en este flujo |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | [doc](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple) | Carga Juggernaut XL inpainting |
| 2 | `LoadImage` | [doc](https://docs.comfy.org/built-in-nodes/LoadImage) | Foto base; máscara vía *Open in MaskEditor* |
| 3 | `Inpaint Crop Improved` | [repo](https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch) | Recorta alrededor de la máscara con contexto, fuerza resolución (1024x1024 SDXL), blend y relleno de huecos |
| 4 | `VAEEncodeForInpaint` o `InpaintModelConditioning` | [inpaint](https://docs.comfy.org/tutorials/basic/inpaint) | El repo recomienda `InpaintModelConditioning` con `noise_mask` para denoise menor a 1; WF-02/WF-06 usan `VAEEncodeForInpaint` con `grow_mask_by` |
| 5 | `KSampler` | [doc](https://docs.comfy.org/built-in-nodes/KSampler) | Denoise 0,8–0,9, el resto según ficha §3 |
| 6 | `VAEDecode` | [doc](https://docs.comfy.org/built-in-nodes/VAEDecode) | Crop ya sampleado a píxeles |
| 7 | `Inpaint Stitch Improved` | [repo](https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch) | Pega el crop en el original con blend, resto intacto |

```
2 ─ IMAGE ─→ 3 ─ crop ─→ 4 ─ latent ─→ 5 ─→ 6 ─→ 7 ─→ Save
2 ─ MASK ───→ 3 ─┘              3 ─ stitcher ─→ 7
```

Parámetros que rinden en el repo: `mask_fill_holes true`, `mask_blend_pixels 32`, `context_from_mask_extend_factor 1,2`, `output_resize_to_target_size true` a la resolución del modelo, `mask_hipass_filter 0,1`.

## 5. Cómo se usa (3 pasos)

1. Pintar la máscara en `LoadImage > Open in MaskEditor` con `Mask Pen` y `Save to Node` (lección WF-02: capa RGB o salir sin Save deja máscara vacía).
2. Pasar imagen + máscara por `Inpaint Crop` con salida forzada a 1024 (SDXL) y blend 32.
3. Samplear solo el crop y cerrar con `Inpaint Stitch`. Salida `gx-YT03-crop-stitch`.

## 6. Cuadro de pruebas

| # | Prueba | Máscara | Prompt + (extracto) | Denoise | Qué mirar |
|---|---|---|---|---|---|
| T1 | Borrar intruso chico | ajustada al objeto + blend 32 | vacío o descripción del fondo | 0,8 | borde sin costura, fondo continuo |
| T2 | Ventana nueva en paño | rectángulo preciso (WF-02 F-01) | "floor-to-ceiling glazing, slim dark mullions" | 0,9 | a plomo, reflejo creíble |
| T3 | Extensión outpaint | extend derecha con el propio crop | coherente con base WF-06 4.0.0 | 1,0 | sin corte, misma luz |
| T4 | Detalle material | chica + upscale previo del crop | "travertine cladding" vs "board-formed concrete" | 0,8 | escala y junta |

Escalera si el relleno transparenta: verificar máscara 100% opaca (`#FFFFFF`), luego subir denoise 0,8 → 0,9 → 1,0. Para paños grandes usar `InpaintModelConditioning` con `noise_mask true`.

## 7. Custom nodes usados (instalado en este equipo)

| Pack | Nodos | Instalación | Estado |
|---|---|---|---|
| `ComfyUI-Inpaint-CropAndStitch` (lquesada, GPL-3.0) | `Inpaint Crop Improved` + `Inpaint Stitch Improved` | clonado manual en `P:\00-repos\ComfyUI\custom_nodes\ComfyUI-Inpaint-CropAndStitch` (commit `6005efc`, 2026-10-21), porque la API de ComfyUI-Manager no responde en este servidor | instalado, pendiente reiniciar ComfyUI para cargarlos |

Reinicio requerido: los nodos nuevos cargan solo al reiniciar ComfyUI. Tras el reinicio, verificar en canvas que aparecen `Inpaint Crop Improved` y `Inpaint Stitch Improved` antes de encolar.

## 8. Cómo continuar las pruebas

1. Reiniciar ComfyUI y confirmar que los dos nodos del pack aparecen.
2. Bajar `juggernautXL_juggernautX_inpainting.safetensors` (Civitai 403361, 6,46 GB) a `models/checkpoints`.
3. Arrastrar `workflow_YT-03-inpaint-crop-stitch.json` al canvas, elegir `fachada-01.png`, pintar la máscara con Mask Pen → Save to Node, Queue. Primera corrida T1 árbol (denoise 0,9, seed 7).
4. Comparar contra la variante liviana [YT-03 ALT](YT-03-alt-local-sd15): misma máscara y foto, medir tiempo y costura del borde en RX 570.
5. Si el relleno transparenta, verificar máscara 100% opaca (`#FFFFFF`) y subir denoise 0,9 → 1,0; si el borde canta, subir `mask_blend_pixels`.
6. Registrar cada corrida en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|20-reporte-corridas-YT]] (probamos / sucedió / veredicto).

## 9. Pendientes

- Reiniciar ComfyUI para cargar el pack.
- Bajar Juggernaut XL inpainting (6,46 GB).
- Primera corrida T1 y comparativa con/sin crop.
- Registrar corridas en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|20-reporte-corridas-YT]].

## Referencias

- Video: https://www.youtube.com/watch?v=EJ7LhNS67KM
- Espejo bilibili con materiales: https://www.bilibili.com/video/BV1owbTzKEXc/
- Juggernaut XL inpainting (video): https://civitai.com/models/403361?modelVersionId=456538
- Pack CropAndStitch: https://github.com/lquesada/ComfyUI-Inpaint-CropAndStitch · https://registry.comfy.org/nodes/comfyui-inpaint-cropandstitch
- Inpainting oficial ComfyUI: https://docs.comfy.org/tutorials/basic/inpaint
- Outpainting oficial ComfyUI: https://docs.comfy.org/tutorials/basic/outpaint
- Flujos dedicados del vault: WF-02 ventanas y WF-06 inpaint 3.x + outpaint 4.x
