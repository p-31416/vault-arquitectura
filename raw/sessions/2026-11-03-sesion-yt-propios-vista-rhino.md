---
tipo: log
fecha: 2026-11-03
tags: [sesion, concurso, gaudi-nexus, wf-comfy-yt, propio]
---

# 2026-11-03 — Sesión YT propios vista nueva + rhino vivo

## Qué se hizo

- Creados 2 flujos propios en `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/`:
  - YT-03 vista nueva desde render (`YT-03-vista-nueva-desde-render-propio.md` + `workflow_YT-03-vista-nueva.json`): img2img SDXL Juggernaut v9, 1024 lanczos, denoise 0,65, salida `gx-YT03-vista`.
  - YT-04 rhino vivo por captura manual (`YT-04-rhino-vivo-propio.md` + `workflow_YT-04-rhino-vivo.json`): SD1.5 inpainting + ControlNet canny SD1.5 strength 0,85, `ImageScale` 512 R1, salida `gx-YT04-rhino-vivo`.
- Actualizado `WF-Comfy-YT/00-index.md` con filas YT-03/YT-04 marcadas propio.
- Validación R4: ambos JSON validados contra `/object_info` y `models/` del ComfyUI local. Único error esperado: nombre de LoadImage pendiente de la imagen real del usuario.
- YT-03 topeado a SDXL 512 (nodo 3, validación R4 limpia con `r-01-baseline.png`); ficha con dato de entrenamiento SDXL-1024 en §3. T1-1024 de la casa en curso como referencia, T1-512 a cargo del usuario.
- Upgrade §8 en YT-03: `ComfyUI_CameraAngleSelector` (https://github.com/NickPittas/ComfyUI_CameraAngleSelector) + LoRA `fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA` (https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA), ambos links verificados 2026-11-03. Sin instalar: corre en pod, en local queda documentado.
- Entrada `WF-Comfy-YT/30-backlog-futuras-pruebas.md`: unifica pendientes YT-01–04 + reporte P-01/P-03 + líneas A–D de Sherlock + matriz WF-01–07 y backlogs hermanos referenciados; sección agregada en `WF-Comfy-YT/00-index.md`.
- Cierre: T1-1024 (`b947a95a`, casa blanca, seed 7) terminó como **interrupted** en nodo 8 VAEDecode tras ~13 min — cancelación, no crash; grafo validado limpio. T1-512 queda a cargo de Sol.

## Archivos modificados

- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/workflow_YT-03-vista-nueva.json` (nuevo)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-03-vista-nueva-desde-render-propio.md` (nuevo)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/workflow_YT-04-rhino-vivo.json` (nuevo)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/YT-04-rhino-vivo-propio.md` (nuevo)
- `proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-index.md` (filas YT-03/YT-04)

## Cerebro-digital

- topics: [comfyui, concurso-gaudi-nexus, img2img-sdxl, controlnet-sd15, rhino-vivo, vista-nueva]
- entidades: [YT-03-vista-nueva, YT-04-rhino-vivo, Juggernaut-XL-v9, sd-v1-5-inpainting-fp16, control_v11p_sd15_canny]
- hechos: [YT-03 usa SDXL sin ControlNet en JSON para validar en local; YT-04 usa pareja SD1.5 coherente checkpoint+ControlNet; giro grande +30° queda para vía RunPod 3D; próxima acción es T1 de YT-03 con render propio del usuario]
