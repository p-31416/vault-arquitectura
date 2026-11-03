---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, sdxl, inpainting, local, sd15]
idioma: es
---

# YT-03 ALT — Inpaint local SD1.5 sin descargas ni pack extra

> Variante del [YT-03 principal](YT-03-sdxl-flux-inpaint-crop-stitch-pixaroma) para correr hoy en la RX 570 con lo ya instalado. Misma idea de máscara, sin CropAndStitch y sin bajar los 6,46 GB de Juggernaut inpainting.

## 1. Cuándo usar cada uno

| Camino | Usa | Ideal para |
|---|---|---|
| YT-03 principal | Juggernaut XL inpainting + pack CropAndStitch, 1024, denoise 0,8–0,9 | Calidad final SDXL, costura mínima, zonas chicas en fotos grandes |
| Esta ALT | `sd-v1-5-inpainting-fp16` (ya instalado) + nodos core, 512, denoise 1.0 | Validar máscara, prompt y composición rápido (~140 s) antes de la corrida pesada |

Receta tomada de [[proyectos/MVP_04.02-comfyui-arquitectura/WF-06-inpaint-outpaint/WF-06-inpaint-outpaint|WF-06]] 3.0.0 y lecciones de [[proyectos/MVP_04.02-comfyui-arquitectura/WF-02-inpainting-ventanas/WF-02-inpainting-ventanas|WF-02]].

## 2. JSON

- `workflow_YT-03-alt-local-sd15.json` (misma carpeta): validado contra el servidor (`Workflow is valid`, 12 nodos, 0 errores).
- Carga el checkpoint inpainting SD1.5 oficial en fp16, entra en RX 570 sin flags extra.

## 3. Grafo

```
LoadImage(fachada-01.png + máscara MaskEditor)
 ├─ IMAGE ─→ ImageScale 512 ─→ VAEEncodeForInpaint(pixels) ─→ KSampler ─→ VAEDecode ─→ SaveImage(gx-YT03-alt-inpaint)
 └─ MASK ─→ MaskToImage ─→ ImageScale 512 ─→ ImageToMask(red) ─→ VAEEncodeForInpaint(mask, grow 12)
CheckpointLoaderSimple(sd-v1-5-inpainting-fp16) ─→ MODEL a KSampler, CLIP a prompts, VAE a encode/decode
```

Diferencias con el principal: escala a 512 (nativo SD1.5, regla R1) en vez de 1024; `grow_mask_by 12` en vez de 6 para paños de muro; `euler / cfg 7 / denoise 1.0 / seed 42` (receta WF-06 probada); sin nodos del pack.

## 4. Paso a paso

1. En ComfyUI `Load` este JSON.
2. En `LoadImage` elegí `fachada-01.png` → `Open in MaskEditor` → pintá con `Mask Pen` la zona del paño → `Save to Node`.
3. Verificá el preview de la máscara: blanco = repintar. Si sale invertido, agregá `InvertMask`.
4. Encolá. Salida `gx-YT03-alt-inpaint`.
5. Si el borde canta, subí `grow_mask_by` a 16–32 (regla WF-02 para muros) y repetí con la misma seed.

## 5. Pruebas sugeridas

| # | Caso | Prompt (+) | Denoise | Qué mirar |
|---|---|---|---|---|
| A1 | Ventanas en paño | "modern floor-to-ceiling glass windows, black aluminum frames, photorealistic architectural detail" | 1.0 | marcos a plomo, resto intacto |
| A2 | Muro pleno | "smooth concrete parapet wall, subtle formwork texture" + negar glass/railing | 1.0 | paño continuo, sin fantasma de ventana |
| A3 | Cielo atardecer | describir atardecer coherente con la luz de la foto | 1.0 | transición sin corte en el borde |

## 6. Límite conocido

SD1.5 a 512 valida composición y máscara, pero el detalle fino queda para la corrida SDXL principal. Flujo de trabajo sugerido: ALT para 3–4 iteraciones rápidas, principal CropAndStitch para la imagen keeper.

## Referencias

- Principal: [YT-03](YT-03-sdxl-flux-inpaint-crop-stitch-pixaroma) · video https://www.youtube.com/watch?v=EJ7LhNS67KM
- Base probada: WF-06 3.0.0 (`sd-v1-5-inpainting-fp16`, euler, cfg 7, denoise 1.0)
- Lecciones de máscara: WF-02 (Mask Pen vs Paint Pen, Save, polaridad, grow)
- Inpainting oficial: https://docs.comfy.org/tutorials/basic/inpaint
