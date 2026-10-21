---
tipo: proyecto
mvp: 04.02
wf: WF-02-inpainting-ventanas
cliente:
proyecto:
ciudad:
pais:
fase: concepto
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [mvp_04.02, comfyui, inpainting, ventanas, mascara]
estado: activo
---

# WF-02 — Inpainting: dibujar ventanas

> Pintás una máscara sobre una zona de la imagen (ej. dónde van ventanas en una fachada) y el modelo dibuja solo esa parte. Estilo video "ComfyUI For Architecture - Simple SDXL Inpainting Workflow" (https://www.youtube.com/watch?v=px8POauudLY). Docs oficiales: https://docs.comfy.org/tutorials/basic/inpaint

- [[#1. Ficha]]
- [[#2. Modelo sugerido]]
- [[#3. Grafo]]
- [[#4. Prompts]]
- [[#5. Corridas]]
- [[#6. Evaluación]]
- [[#7. Backlog del WF]]

## 1. Ficha

| Campo | Valor |
|---|---|
| Objetivo | Editar zonas puntuales de un render/foto (dibujar ventanas, cambiar puertas, sacar objetos) |
| Input | `inputs/fachada-01.png` (render o foto) + máscara pintada en MaskEditor (click derecho en LoadImage → Open in MaskEditor) |
| Output esperado | Misma imagen con solo la zona enmascarada regenerada según prompt |
| Output NO esperado | Cambios fuera de la máscara (si pasa, ver grow_mask) |
| Workflow base | `workflow_inpaint_v1_ui.json` (arrastrable a la UI, validado) + `workflow_inpaint_v1.json` (formato API, mismo grafo) + `workflow_fachada_txt2img_v1.json` (generó la fachada base) |
| Hardware | Esta PC: RX 570 8GB DirectML. Sin RunPod |

## 2. Modelo sugerido

| Rol | Sugerido | Por qué |
|---|---|---|
| Checkpoint fase 1 | `sd-v1-5-inpainting` fp16 (~2.1 GB, descargando) | Inpainting SD1.5 oficial (`runwayml/stable-diffusion-inpainting`), entra en RX 570 sin cambiar flags |
| Checkpoint fase 2 | SDXL inpainting (video de referencia) | Solo si fase 1 funciona: ~7 GB + requiere `--lowvram --cpu-vae` + reinicio. Decisión tras fase 1 |
| KSampler | denoise 0.8-1.0 (1.0 = reemplazo total, 0.8 = conserva parte), steps 30, cfg 7 | La máscara define DÓNDE, el denoise define CUÁNTO cambia |
| Nodo clave | `VAEEncodeForInpaint` (pixels + vae + mask) o `SetLatentNoiseMask` | Ver https://docs.comfy.org/tutorials/basic/inpaint |

## 3. Grafo

```
LoadImage ──image──┬──► VAEEncodeForInpaint ──► KSampler ──► VAEDecode ──► SaveImage
(máscara pintada)  │         │                       │
en MaskEditor ──mask─────────┘                       │
                                                     │
CheckpointLoader ──model─────────────────────────────┤
(inpainting)  ├──clip──► CLIPTextEncode (pos) ───────┤
              └──clip──► CLIPTextEncode (neg) ───────┘
```

| Nodo | Clase | Parámetros propios de este WF |
|---|---|---|
| CheckpointLoader | `CheckpointLoaderSimple` | `sd-v1-5-inpainting-fp16.safetensors` (fase 1) |
| LoadImage | `LoadImage` | `inputs/fachada-01.png` + máscara vía MaskEditor |
| VAEEncode | `VAEEncodeForInpaint` | grow_mask_by 6 (expande la máscara unos px para borde limpio) |
| KSampler | `KSampler` | denoise 1.0 primera prueba, seed variable |

## 4. Prompts

_(Pendiente — se definen con la primera imagen: ej. positivo `modern floor-to-ceiling glass windows, black aluminum frames, photorealistic` sobre fachada.)_

## 5. Corridas

> Más nuevo → más arriba.

| Fecha | Seed | Cambio | Archivo | Tiempo | Calidad | Nota |
|---|---|---|---|---|---|---|
| 2026-10-15 | 42 (fixed) | prompt corregido a MURO (concrete parapet, niega glass/railing), misma máscara+seed | `salidas/n_02-F-03.png` (origen `WF02-inpaint-muro_00001_.png`, prompt_id `fded66a8`) | 132 s | ❓ a vista de miniatura casi idéntica a F-02: verificar a pleno si el paño es muro | Misma seed → fuera de máscara idéntico; comparar F-02 vs F-03 píxel a píxel en la zona del trazo |
| 2026-10-15 | 42 (fixed) | SOL en canvas: MaskEditor sobre clipspace + MaskToImage verificador, prompt ventanas noche, denoise 1.0, grow 5 | `salidas/n_02-F-02.png` (origen `WF02-inpaint_00002_.png`, prompt_id `68a56475`) | 214 s | ⚠️ sale render completo nuevo en vez de edición local → máscara blanca demasiado grande: con denoise 1.0 todo lo blanco se repinta entero | Cableado verificado OK en metadata (mask→VAEEncodeForInpaint + MaskToImage). Regla: máscara chica y precisa; verificar preview de MaskToImage antes de Queue |
| 2026-10-08 | 42 | baseline: máscara programática en muro hormigón + prompt ventanas vidrio/marcos negros, denoise 1.0 | `salidas/n_02-F-01.png` | 141 s | _pendiente evaluación SOL_ | prompt_id `342b01b8` — ventanas dibujadas OK, resto intacto. Input: `fachada-01.png` (generada con `workflow_fachada_txt2img_v1.json`, seed 42) |
| _(pendiente)_ | | | | | | ~~Esperando modelo inpainting + `inputs/fachada-01.png`~~ ← modelo listo, fachada generada |

## 6. Evaluación

Diagnóstico 2026-10-15 (F-02 vs F-03 casi idénticas, prompts opuestos) — ranking @sherlock:
1. **Máscara efectiva vacía** (más probable): en el MaskEditor nuevo es fácil pintar en capa `Paint Pen (RGB)` en vez de `Mask Pen`, o salir sin `Save` → mask sale negro y el sampler conserva todo. Verificar con `MaskToImage` antes de Queue.
2. **Polaridad**: blanco = repintar en todo ComfyUI; si el preview muestra lo contrario, probar `InvertMask` (una de las dos muerde).
3. **Grow chico**: para un paño de muro usar 16-32 + feather, no 5-6.
4. **Vía alternativa**: `InpaintModelConditioning` (noise_mask true) en vez de `VAEEncodeForInpaint`; o checkpoint normal + `SetLatentNoiseMask` + denoise 0.6-0.8 como contraste.
5. Denoise 1.0 es correcto con modelo inpainting; DirectML sin reportes de fallo silencioso.
Refs: https://docs.comfy.org/tutorials/basic/inpaint · https://comfyui.nomadoor.net/en/basic-workflows/sd15-inpainting · https://github.com/Comfy-Org/ComfyUI/issues/1186 · https://docs.comfy.org/built-in-nodes/InpaintModelConditioning

## 7. Backlog del WF

- [ ] Descargar `sd-v1-5-inpainting` + convertir fp16 + verificar carga
- [ ] Armar `workflow_inpaint_v1.json` (LoadImage → MaskEditor → VAEEncodeForInpaint → KSampler)
- [ ] Test 1: dibujar ventanas sobre fachada (denoise 1.0)
- [ ] Test 2: denoise 0.8 vs 1.0
- [ ] Decidir fase 2 SDXL (video referencia) según resultado + VRAM
