---
tipo: log
fecha: 2026-11-03
tags: [sesion, concurso, gaudi-nexus, wf-comfy-yt, inpainting, crop-stitch]
---

# 2026-11-03 — Sesión YT-01 mask + YT-03 crop-stitch + ALT local

## Qué se hizo

- YT-01: aclarada la duda de máscara (el video pinta en MaskEditor, entra por `LoadImage[MASK]`). Detectada divergencia doc vs JSON (`VAEEncode+SetLatentNoiseMask` vs `VAEEncodeForInpaint grow 6` del video). Propuesto v2 con `ImageScaleToMaxDimension` 1024 + cadena `MaskToImage>Scale>ImageToMask`, validado (`Workflow is valid`, 12 nodos) y encolado como T1 árbol (prompt_id `a1b95d7c`); quedaba en pending tras otro trabajo en curso.
- El usuario observó que la corrida salió sin máscara útil (máscara vacía encolada por API). Canceló la pendiente del lado del usuario. Acordado: T1 real pide pintar en canvas o usar archivo de máscara.
- Entregado JSON YT-01 v2 inline + paso a paso MaskEditor; el usuario lo prueba del lado propio. Ubicación del v1 explicada (`WF-Comfy-YT/workflow_YT-01-sdxl-inpainting.json`).
- Nuevo video documentado como YT-03: pixaroma Ep19 SDXL/Flux Inpainting (`YT-03-sdxl-flux-inpaint-crop-stitch-pixaroma.md`): pack `ComfyUI-Inpaint-CropAndStitch`, checkpoint Juggernaut XL inpainting (Civitai 403361), KSampler `dpmpp_2m`/karras/30/cfg 3.5/denoise 0.8–0.9, grafo Crop>sample>Stitch, cuadro T1–T4. Enlaces verificados.
- Variante ALT local creada (`YT-03-alt-local-sd15.md` + `workflow_YT-03-alt-local-sd15.json` validado): `sd-v1-5-inpainting-fp16` ya instalado, 512, `grow 12`, euler/cfg 7/denoise 1.0, sin descargas ni pack.
- Instalado pack `ComfyUI-Inpaint-CropAndStitch` por clonado manual en `P:\00-repos\ComfyUI\custom_nodes\` (commit `6005efc`), porque la API de ComfyUI-Manager no responde en el servidor. Documentado §7 + §8 (cómo continuar) en el md YT-03.
- Borrador principal `workflow_YT-03-inpaint-crop-stitch.json` (formato UI arrastrable, adaptado del ejemplo oficial `inpaint_sd15.json` del repo: checkpoint Juggernaut inpainting, `fachada-01.png`, crop 1024, contexto x1.2, blend 32, T1 árbol, denoise 0.9, SaveImage `gx-YT03-crop-stitch`). Preparado SIN correr, a pedido del usuario. No validable aún: pack sin cargar (falta reinicio) y checkpoint sin descargar.
- `00-index.md` actualizado con filas YT-03 e YT-03 ALT.

## Archivos modificados

- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-03-sdxl-flux-inpaint-crop-stitch-pixaroma.md` (nuevo, +§7 custom nodes y §8 continuar pruebas)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/workflow_YT-03-inpaint-crop-stitch.json` (nuevo, borrador UI sin correr)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-03-alt-local-sd15.md` (nuevo)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/workflow_YT-03-alt-local-sd15.json` (nuevo, validado)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-index.md` (filas YT-03 / YT-03 ALT)
- `P:\00-repos\ComfyUI\custom_nodes\ComfyUI-Inpaint-CropAndStitch\` (clonado, fuera del vault)

## Cerebro-digital

- topics: [comfyui, concurso-gaudi-nexus, inpainting, crop-stitch, sdxl, sd15, maskeditor]
- entidades: [YT-01-inpainting, YT-03-crop-stitch, YT-03-ALT-local, fachada-01.png, juggernautXL-inpainting, sd-v1-5-inpainting-fp16, ComfyUI-Inpaint-CropAndStitch-6005efc, prompt-a1b95d7c-cancelado]
- hechos: [máscara API vacía si no se pinta en canvas, el inpaint real pide MaskEditor o LoadImageMask; Manager-API caída, instalación manual por git clone verificada; colisión de numeración YT-03 con `YT-03-vista-nueva-desde-render-propio.md` de la sesión anterior, pendiente renumerar; próxima acción es reinicio ComfyUI + descarga checkpoint 6,46 GB + T1 crop-stitch]
