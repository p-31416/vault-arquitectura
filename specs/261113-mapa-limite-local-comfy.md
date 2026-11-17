---
tipo: spec
fecha_creacion: 2026-11-13
ultima_actualizacion: 2026-11-13
estado: borrador
tags: [spec, comfyui, limite-local, rx570, modelos, nodos, pod, mapa]
---

# Mapa límite local ComfyUI — qué se prueba con lo instalado y qué pide cada flujo

> Base: spec [[specs/261112-spec-10-flujos-yt|10 flujos YT]]. Relevamiento 2026-11-13 sobre `P:\00-repos\ComfyUI\`.
> Doctrina vigente: local prueba mínimo, pod ráfagas, Cloud solo irremplazable (ver [[specs/261112-matriz-local-pod-cloud|matriz]] §5).

## Inventario real instalado

- **Checkpoints:** `realvisxlV50_v50Bakedvae` + `realvisxlV50_v50LightningBakedvae` (6.46GB c/u) · `Juggernaut-XL_v9_RunDiffusionPhoto_v2` + `juggernautXL_ragnarok` (6.62GB c/u) · `sd-v1-5-inpainting-fp16` (1.99GB, SD1.5, licencia Open RAIL-M apta estudio — NO es el mix retirado).
- **ControlNet:** `control_sdxl_canny_fp16` (2.33GB) · `XL_controlnet-union-sdxl_promax` (2.34GB) · `control_v11f1p_sd15_depth_fp16` + `control_v11p_sd15_canny` + `control_v11p_sd15_scribble` (SD1.5, livianos).
- **Custom nodes:** `ComfyUI-IC-Light` · `ComfyUI-Inpaint-CropAndStitch` · `ComfyUI_IPAdapter_plus` (+ `CLIP-ViT-H-14` en clip_vision → IPAdapter usable).
- **Upscale:** `RealESRGAN_x4plus.pth`.
- **LoRAs arq:** archisketch, markerhandsketch, Architectural_Massing, Architecture_Building, ArcvizXL, JJ_Archvizcg, isometric, room, landscape_sketch, BrutalistTech, bookstore.
- **Ausente:** todo video (sin AnimateDiff/SVD/LTX ni VideoHelperSuite) · todo 3D (sin Tripo/TRELLIS/Fast3D/Zero123++, sin ComfyUI-3D-Pack) · sin Qwen-Image-Edit · sin Flux.

## Flujo por flujo (orden barato → caro)

| Flujo | Local con lo instalado | Si pide más, qué pide exactamente |
|---|---|---|
| F1 txt2img base | ✅ RealVis v5.0 keeper F0b verificada | Nada. Alternativa rápida: Lightning (archivada, blanda). |
| F3 cámara ±15° (F1-camara, denoise 0.6) | ✅ RealVis img2img, ~6-12min | Giro >30° real: pod + `CameraAngleSelector` + LoRA multi-ángulo Qwen (96 poses) o F8 malla. |
| F4 inpaint (F3, denoise 0.8) | ✅ RealVis v5.0 SDXL + `SetLatentNoiseMask`/nodo CropAndStitch instalado (inpaint SDXL puro, máxima calidad) | Nada local. `sd-v1-5-inpainting-fp16` solo fallback si SDXL no entra en VRAM — nunca píxel final. |
| F5 relight denoise (F2b, 0.4) | ✅ Lightning/RealVis img2img | Serie física fiel: IC-Light (abajo). |
| F5 relight IC-Light (F2a) | ⚠️ PROBAR: IC-Light + `sd-v1-5-inpainting-fp16` como base SD1.5 (licencia apta, 2GB) | Si el nodo rechaza la base inpainting: bajar base SD1.5 txt2img apta (~2-4GB, ej. Realistic Vision / DreamShaper, Open RAIL-M) o pod. La retirada `architecturerealmix` sigue vetada (⛔ comercial). |
| F6 ControlNet canny (F6) | ✅ `control_sdxl_canny_fp16` + RealVis v5.0; si 9.4GB excede → tiling/half precision | Dual SDXL+Union 9.4GB > 8GB: pod 24GB. Vía SD1.5 solo diagnóstico geométrico, nunca imagen final. |
| F2 sketch→render LoRA | ✅ LoRAs archisketch/markerhandsketch/ArcvizXL + RealVis/Juggernaut | Nada; es el flujo más barato para croquis P-03. |
| F8 style/IPAdapter | ✅ `IPAdapter_plus` + CLIP Vision presentes | Nada; probar con foto referente Gaudí como style ref. |
| F7 upscale (F5) | ✅ RealESRGAN por mitades (full 4K OOM en 8GB) | Full-res o 2º denoise 0.2-0.35 pesado: pod o cierre Topaz/Magnific trial. |
| F2 3D→render (vuelta) | ✅ captura viewport (ya existe `capture_rhino_viewport`) + img2img | Nada para la vuelta; la ida (abajo) es lo caro. |
| F8 imagen→3D (ida) | ❌ sin nodos ni modelos 3D | Opción A pod: `ComfyUI-3D-Pack` + TRELLIS (~8GB modelo, 24GB VRAM). Opción B Cloud: Tripo API (pago/mes). Opción C liviana: Zero123++ (6 vistas, ~3GB) en pod CPU/gamma. Local RX 570: no. |
| F9 imagen→video | ❌ sin modelos ni nodos video; 8GB DirectML inviable | Opción A pod: LTX-Video/LTX-2.3 + VideoHelperSuite. Opción B Cloud: Seedance/Veo por API (dueño paga). Clip 15s plaza = fase pod, no iteración. |
| F10 Telegram/n8n loop | ✅ caption=prompt, LAN, Pollinations free | Pod auto-encendido: webhook RunPod (fase tardía). |
| Qwen-Image-Edit / Kontext | ❌ modelo ~14-24GB | Pod 24GB directo. |

## Regla de calidad (2026-11-13, Sol)

Modelo final siempre RealVisXL v5.0 estándar (retador: Juggernaut Ragnarok). SD1.5 (`sd-v1-5-inpainting-fp16`) solo como plomería donde la arquitectura del nodo lo exija (IC-Light fc) — nunca genera el píxel final.

## Orden de pruebas propuesto (esta semana, todo $0)

1. F1 cámara sobre keeper T1 (4 variantes) → 2. F4 inpaint muebles → 3. F5 denoise noche → 4. F5 IC-Light con base inpainting (desbloqueo) → 5. F6 canny SDXL y SD1.5 → 6. LoRA sketch → 7. IPAdapter style → 8. F7 upscale mitades → 9. F10 loop → 10. F8/F9 solo spec pod (no correr).
