---
tipo: proyecto
mvp: 04.02
wf: WF-06-inpaint-outpaint
cliente:
proyecto:
ciudad:
pais:
fase: concepto
fecha_creacion: 2026-10-14
ultima_actualizacion: 2026-10-14
tags: [mvp_04.02, comfyui, inpainting, outpainting, mascara, serie]
estado: activo
---

# WF-06 — inpainting (3.x) + outpainting (4.x): editar y extender

> Cambiar una zona sin tocar el resto (inpaint) y agrandar el encuadre (outpaint), ambos con el modelo inpainting dedicado. Continúa WF-02 (ventanas OK) con casos nuevos.

- [[#1. Ficha]]
- [[#2. Modelo]]
- [[#3. Grafos]]
- [[#4. Prompts]]
- [[#5. Corridas]]
- [[#6. Evaluación]]
- [[#7. Backlog del WF]]
- [[#8. Referencias]]

## 1. Ficha

| Campo | Valor |
|---|---|
| Objetivo | Probar edición localizada y extensión de encuadre sobre base propia |
| Input | `inputs/base-06.png` (copiar `n_04-1.0.0.png`) + máscara (MaskEditor: click derecho en LoadImage → Open in MaskEditor) |
| Output esperado | `salidas/n_06-3.0.x.png` (inpaint) + `salidas/n_06-4.0.0.png` (outpaint 768→1024) |
| Versiones | `3.0.x` = inpaint (3.0.0 ventanas, 3.0.1 cielo→atardecer) · `4.0.0` = outpaint derecha 256px |
| Hardware | RX 570 8GB, `sd-v1-5-inpainting-fp16` entra sin cambiar flags |

### Variantes de un vistazo

| Versión | Diferencia | Config | Imagen |
|---|---|---|---|
| `3.0.0` | Inpaint ventanas (máscara MaskEditor, grow 6) | inpainting, denoise 1.0, seed 42 | _(pendiente)_ |
| `3.0.1` | Inpaint cielo→atardecer (grow 12 si hay borde) | inpainting, denoise 1.0, seed 42 | _(pendiente)_ |
| `4.0.0` | Outpaint: extiende derecha 256px, feathering 32 (máscara automática) | inpainting, denoise 1.0, seed 42 | _(pendiente)_ |

Leyenda: `3.x` edita una zona (máscara a mano) · `4.x` agranda el encuadre (máscara automática del pad). Detalle en §5.

## 2. Modelo

`sd-v1-5-inpainting-fp16.safetensors` (inpainting SD1.5 oficial). KSampler euler/normal, 30 steps, cfg 7, seed 42, denoise 1.0.

## 3. Grafos

**3.0.0** `workflow_3.0.0_inpaint.json`: `LoadImage(base-06.png, máscara pintada) → VAEEncodeForInpaint(grow_mask_by 6) → KSampler → VAEDecode → SaveImage(WF06-3.0.0)`. La máscara define DÓNDE, el denoise CUÁNTO.
**4.0.0** `workflow_4.0.0_outpaint.json`: mismo + `ImagePadForOutpaint(right 256, feathering 32)` entre LoadImage y VAEEncode (el pad genera imagen extendida + máscara automática). Mantener prompts coherentes con la base para integrar la zona nueva.

## 4. Prompts

**3.0.0 (+):** `modern floor-to-ceiling glass windows, black aluminum frames, photorealistic architectural detail`
**4.0.0 (+):** `modern concrete house exterior, neighboring brick facades, street trees, sidewalk, photorealistic, architectural photography, coherent daylight`
**− (ambos):** `blurry, low quality, distorted, watermark, text`

## 5. Corridas

> Más nuevo → más arriba.

| Fecha | Versión | Caso | Archivo | Vista | Tiempo | Calidad | Nota |
|---|---|---|---|---|---|---|---|
| _(pendiente)_ | 3.0.0 | ventanas | `salidas/n_06-3.0.0.png` | — | ~140s est. | | Réplica de WF-02 F-01 sobre base propia |
| _(pendiente)_ | 3.0.1 | cielo→atardecer | `salidas/n_06-3.0.1.png` | — | | | Si borde visible → grow 12 |
| 2026-10-15 | 4.0.0 | extender derecha 256px, feathering 32 | `salidas/n_06-4.0.0.png` (origen `WF06-4.0.0_00001_.png`, prompt_id `b62dffe4`) | ![4.0.0](salidas/n_06-4.0.0.png) | 273s | ✅ casa vecina coherente a la derecha, sin corte visible, misma luz | Primer outpaint OK; probar arriba (4.0.1) |

## 6. Evaluación

DoD: inpaint cambia solo la máscara (verificar píxeles fuera intactos) · outpaint integra vegetación/fachadas vecinas sin corte visible · sin textos ni caras fantasma en zonas nuevas.

## 7. Backlog del WF

- [ ] Copiar base a `inputs/base-06.png` + pintar máscaras + correr 3.0.x
- [ ] Correr 4.0.0 + probar extender arriba (cielo) como variante 4.0.1
- [ ] Comparar `SetLatentNoiseMask` (template) vs `VAEEncodeForInpaint` (este WF) en mismo caso

## 8. Referencias

- Oficial inpaint (MaskEditor, VAEEncodeForInpaint, grow_mask_by): https://docs.comfy.org/tutorials/basic/inpaint (verificado 200)
- Oficial outpaint (Pad Image for Outpainting, feathering, mismos prompts): https://docs.comfy.org/tutorials/basic/outpaint (verificado 200)
- Wiki inpaint (alternativa SetLatentNoiseMask, denoise desde 0.1): https://comfyui-wiki.com/en/tutorial/basic/how-to-inpaint-an-image-in-comfyui
- Wiki outpaint (2 etapas: SD común + modelo inpainting): https://comfyui-wiki.com/en/tutorial/basic/how-to-outpaint-an-image-in-comfyui
- Video 2026 inpaint/outpaint/upscale: https://comfy.org/learning/basics/inpainting-outpainting-upscaling
- Ejemplos inpaint + outpaint con v2: https://comfyui-wiki.com/en/workflows/inpaint
