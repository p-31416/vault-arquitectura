---
tipo: plan
proyecto: concurso-gaudi-nexus
titulo: Diagnostico ControlNet inpaint outpaint upscale XL cuantizados LoRA
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
estado: borrador-activo
tags: [comfyui, controlnet, inpaint, outpaint, upscale, sdxl, rx570, diagnostico]
idioma: es
---

# Diagnostico tecnico — por que nunca funciono ControlNet / inpaint / upscale

> Servidor vivo `127.0.0.1:8188`, 856 nodos en `/object_info` (verificado 2026-11-12). Todos los nodos existen. El problema son archivos y VRAM, no nodos.

## 1. Hallazgo madre

12 workflows piden `architecturerealmix_v11.safetensors` (SD1.5 2GB) que **no esta en disco**. Solo queda un `BIT5A90.tmp` = descarga interrumpida. Todo Canny/scribble SD1.5 + WF_v1/IPA/demo-manana falla con `checkpoint not found` al encolar. No es bug de ControlNet.

## 2. Por herramienta

| Herramienta | Estado real | Causa |
|---|---|---|
| Canny SD1.5 | nodos SI (`Canny`, `ControlNetLoader`, `ControlNetApplyAdvanced`), controlnets SD1.5 en disco SI | base SD1.5 ausente → re-descargar 2GB |
| Canny SDXL | nodos SI, `control_sdxl_canny_fp16` + Union ProMax en disco SI | VRAM: 6.9GB base + 2.5GB control = 9.4GB > 8GB → OOM en RX 570 |
| Inpaint SDXL | YT-01 (`SetLatentNoiseMask`) + WF-curso loggia OK nodos, Juggernaut en disco SI | deberia correr; si fallo fue por 1216x832 demasiado grande → bajar a 1024x640 |
| Inpaint SD1.5 | YT-03-alt + YT-04-rhino-vivo OK nodos, `sd-v1-5-inpainting-fp16` SI | deberia correr a 512 |
| Inpaint crop/stitch | UI JSON usa `InpaintCropImproved/StitchImproved` = nombres correctos actuales | OK, era falso positivo del auditor |
| Outpaint | nodo `ImagePadForOutpaint` SI | ningun workflow lo cablea → crear uno |
| Upscale | `UpscaleModelLoader` + `ImageUpscaleWithModel` SI, `RealESRGAN_x4plus.pth` SI | ningun workflow los usa; los hires usan `LatentUpscale` = causa del look blando |
| UltimateSDUpscale | NO instalado | instalar o evitar (tiles a mano con ESRGAN) |
| IPAdapter | 30+ nodos SI (`IPAdapterAdvanced`, `IPAdapterModelLoader`...) | ningun workflow MVP_04 los usa; el JSON calco-estilo del concurso SI los usa |
| Depth/scribble aux | solo `Canny` core + DA3 small | sin `comfyui_control_aux`: no hay hed/lineart/mlsd |
| GGUF cuantizados | NO instalado | Flux/Z-Image cuantizados imposibles hasta instalar pack |
| LTX video | nodos SI | modelos ausentes (`diffusion_models` vacio) |
| Flux2 rhino | nodos SI | stack 18.3GB ausente (transformer + Qwen3-8B + VAE) |

## 3. Limitacion XL en RX 570

- `--lowvram` esta MUERTO en DirectML (`model_management.py:121` fuerza `lowvram_available=False`). Solo salva `--cpu-vae`.
- `--disable-dynamic-vram` en tus `.bat` impide offload fino; para SDXL + ControlNet conviene quitarlo y sumar `--reserve-vram 1.0`.
- SDXL solo a 512-768px + Lightning 4-6 pasos para iterar; 1216x832 solo final y con VAE en CPU.

## 4. Upscale: version correcta

`LatentUpscale x1.5 + denoise 0.35` = blando por diseno (ruido gaussiano ampliado). Version correcta en tu disco:
`LoadImage → UpscaleModelLoader (RealESRGAN_x4plus) → ImageUpscaleWithModel → (opcional) 2º KSampler denoise 0.2-0.25 por tiles` = nitido sin cambiar composicion.

## 5. Cuantizados y LoRA

- LoRAs: todos los usados existen (ArcvizXL, Architecture_Building, archisketch, markerhandsketch, JJ_Archvizcg_v2). Solo `rhino-to-image` pide Flux2 ausente.
- Cuantizados: instalar `ComfyUI-GGUF` + bajar `Z-Image-Turbo Q4` (~4GB) o `Flux schnell Q4` (~8GB limite) para iterar rapido. Requiere `s` (instala codigo).

## 6. Plan de arreglo ($0, sin pod)

1. Re-descargar `architecturerealmix_v11` 2GB (CivitAI 84958, SOLO tests, licencia NO comercial) → desbloquea 12 workflows. (requiere `s`)
2. Crear `workflow_upscale_esrgan.json` (LoadImage + UpscaleModelLoader + ImageUpscaleWithModel) + `workflow_outpaint_sdxl.json` (PadForOutpaint + SetLatentNoiseMask). (requiere `s`)
3. Probar 1 flujo minimo: YT-03-alt SD1.5 512 inpaint o WF-01 SDXL Lightning 512 5 steps (~80s). (requiere `s` por GPU)
4. Flags `.bat`: quitar `--disable-dynamic-vram`, sumar `--reserve-vram 1.0` para SDXL+ControlNet. (requiere `s`)
5. Luego: ComfyUI-GGUF + Z-Image Q4 para iteracion rapida. (requiere `s`)

## 7. Verificacion hecha (sin GPU)

- `/object_info` 856 nodos: ControlNet/inpaint/upscale/IPAdapter/ICLight SI; UltimateSDUpscale y GGUF NO.
- 37 workflows validados estaticamente: 0 nodos faltantes, 12 con checkpoint ausente, LTX/Flux2 con modelos ausentes.
- Servidor responde `system_stats` OK.
