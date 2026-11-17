---
tipo: flujo
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp_04, upscale, esrgan, armado-sin-correr]
---

# n_09 upscale ESRGAN — armado, SIN correr en este disco

> Workflow: `workflow_upscale_esrgan.json` (API format, 4 nodos).
> Estado: validado contra `/object_info` (UpscaleModelLoader + ImageUpscaleWithModel existen, `RealESRGAN_x4plus.pth` en disco). No encolar full-res en RX 570: partir la imagen por mitades o reservar para pod.
> Uso: reemplazar `PONER-RENDER-PROPIO.png` por el keeper en `ComfyUI/input/`, arrastrar el JSON a ComfyUI, encolar.
