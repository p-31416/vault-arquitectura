---
tipo: proyecto
mvp: 04.02
wf: WF-05-img2img-croquis
cliente:
proyecto:
ciudad:
pais:
fase: concepto
fecha_creacion: 2026-10-14
ultima_actualizacion: 2026-10-14
tags: [mvp_04.02, comfyui, img2img, croquis, denoise, serie]
estado: activo
---

# WF-05 — img2img: croquis → render (matriz de denoise)

> De un croquis o de la salida de WF-04 a render: el mando es el denoise. Método científico: misma imagen, misma seed, solo cambia denoise.

- [[#1. Ficha]]
- [[#2. Modelo]]
- [[#3. Grafo 2.0.0]]
- [[#4. Prompts]]
- [[#5. Corridas]]
- [[#6. Evaluación]]
- [[#7. Backlog del WF]]
- [[#8. Referencias]]

## 1. Ficha

| Campo | Valor |
|---|---|
| Objetivo | Medir cuánto cambia el render según denoise sobre la misma base |
| Input | `inputs/base-05.png` (copiar salida `n_04-1.0.0.png` de WF-04; o `croquis001.jpg`) |
| Output esperado | 3 imágenes `salidas/n_05-2.0.x.png` comparables (denoise 0.4/0.6/0.8) |
| Versiones | `2.0.x` = familia img2img (2.0.0 denoise 0.6 · 2.0.1 denoise 0.4 · 2.0.2 denoise 0.8, mismo JSON editando 1 campo) · `2.1.0` = img2img + LoRA markers 0.8 (`workflow_2.1.0_img2img_lora.json`, convierte una imagen existente a sketch) |
| Hardware | RX 570 8GB, R1 ImageScale 512 siempre |

### Variantes de un vistazo

| Versión | Diferencia | Config | Imagen |
|---|---|---|---|
| `2.0.0/2.0.1/2.0.2` | Solo cambia denoise: 0.6 / 0.4 / 0.8 | Realmix, euler 30, cfg 7, seed 42 | _(pendiente)_ |
| `2.1.0` | +LoRA markers 0.8, denoise 0.65 | markers, seed 42 | ![2.1.0](salidas/n_05-2.1.0.png) |
| `2.1.1` | +LoRA markers 1.0, denoise 0.8 | markers, seed 42 | ![2.1.1](salidas/n_05-2.1.1.png) |

Leyenda: `2.0.x` mide el denoise · `2.1.x` suma estilo sobre la foto. Detalle en §5.

## 2. Modelo

`architecturerealmix_v11.safetensors` (SD1.5). KSampler euler/normal, 30 steps, cfg 7, seed 42.

## 3. Grafo 2.0.0

`workflow_2.0.0_img2img.json`: `LoadImage(base-05.png) → ImageScale(lanczos 512) → VAEEncode → KSampler(denoise 0.6) → VAEDecode → SaveImage(WF05-2.0.0)`.

## 4. Prompts

**+:** `architecturerealmix style, same modern concrete house at golden hour, warm wood accents, long shadows, photorealistic, architectural photography`
**−:** `blurry, low quality, distorted, watermark, text, cartoon, deformed`

## 5. Corridas

> Más nuevo → más arriba.

| Fecha         | Versión | Denoise                    | Archivo                                                                         | Vista                            | Tiempo    | Calidad                                                                                                  | Nota                                    |
| ------------- | ------- | -------------------------- | ------------------------------------------------------------------------------- | -------------------------------- | --------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| 2026-10-15 | 2.0.0 | 0.6 | `salidas/n_05-2.0.0.png` (origen `WF05-2.0.0_00001_.png`, prompt_id `a39f2041`) | ![2.0.0](salidas/n_05-2.0.0.png) | 143s | ✅ misma casa, calidez golden hour | Punto medio ideal demo |
| 2026-10-15 | 2.0.1 | 0.4 | `salidas/n_05-2.0.1.png` (origen `WF05-2.0.1_00001_.png`, prompt_id `0c6f64ee`) | ![2.0.1](salidas/n_05-2.0.1.png) | 120s | ✅ casi calco con micro-refinamiento | Base de la matriz |
| 2026-10-14 | 2.1.1 | 0.8 +markers 1.0, seed 42 | `salidas/n_05-2.1.1.png` (origen `WF05-2.1.1_00001_.png`, prompt_id `7f8eaadd`) | ![2.1.1](salidas/n_05-2.1.1.png) | 126s | ⚠️ estilo parcial (trazo en cielo/vegetación) pero la casa se reinventa: pierde identidad de la base | Tradeoff img2img+LoRA: 0.65 conserva sin estilo, 0.8 estila sin identidad. Hipótesis: 0.7 + LoRA 1.0, o ControlNet para fijar geometría (F8) |
| 2026-10-14 | 2.1.0 | 0.65 +markers 0.8, seed 42 | `salidas/n_05-2.1.0.png` (origen `WF05-2.1.0_00001_.png`, prompt_id `d83313fc`) | ![2.1.0](salidas/n_05-2.1.0.png) | 138s | ⚠️ composición idéntica pero estilo NO transfiere | Motivó 2.1.1 |
| 2026-10-15 | 2.0.2 | 0.8 | `salidas/n_05-2.0.2.png` (origen `WF05-2.0.2_00001_.png`, prompt_id `e68f64ed`) | ![2.0.2](salidas/n_05-2.0.2.png) | 143s | ✅ reinvención contenida: lamas de madera, luz cálida, misma masa | Cierra matriz: 0.4 calco → 0.6 dorado → 0.8 nuevo |

## 6. Evaluación

DoD: 2.0.1 casi calco con mejor material · 2.0.0 cambio de luz visible sin mover volúmenes · 2.0.2 aún reconocible como la misma casa. Si 0.6 ya reinventa: bajar a 0.5.

## 7. Backlog del WF

- [ ] Copiar `n_04-1.0.0.png` a `inputs/base-05.png` + correr matriz 2.0.x
- [ ] Repetir matriz sobre `croquis001.jpg` (croquis real vs render base)
- [ ] Tabla comparativa denoise para el índice

## 8. Referencias

- Oficial img2img (denoise 0.87 ejemplo, matemática steps/denoise): https://docs.comfy.org/tutorials/basic/image-to-image (verificado 200)
- Ejemplos oficiales (repo): https://github.com/comfyanonymous/ComfyUI_examples/blob/master/img2img/README.md
- Guía img2img con VAE + denoise: https://comfyui-wiki.com/en/workflows/img2img
- Sketch→imagen con ControlNet 2026: https://www.runflow.io/blog/comfyui-sketch-to-image
- ControlNet oficial (sketch como condición): https://docs.comfy.org/tutorials/controlnet/controlnet (verificado 200)
