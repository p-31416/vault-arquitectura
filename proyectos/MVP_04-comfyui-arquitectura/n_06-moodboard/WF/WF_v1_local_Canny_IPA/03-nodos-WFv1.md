---
tipo: proyecto
fase: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [mvp_04, n_06, nodos]
---

# 03-nodos — configs propias del flujo

## Incluidos en v1 (12 nodos)

LoadImage `mood-product-ref.png` → ImageScale lanczos 512x512 center (R1) → Canny 0.31/0.59 → ControlNetLoader `control_v11p_sd15_canny.safetensors` → ControlNetApplyAdvanced 0.85/0.0-0.80 → KSampler (Realmimix, euler_ancestral/karras/30/cfg 7/seed 42) → VAEDecode → SaveImage `n_06-B-01`.

Docs: ImageScale, CheckpointLoaderSimple, ControlNetLoader, ControlNetApplyAdvanced, CLIPTextEncode, KSampler, VAEDecode, VAEEncode, LoadImage, SaveImage en `https://docs.comfy.org/built-in-nodes/<PascalCase>`; Canny/IPA vía `comfyui_controlnet_aux` + `ComfyUI_IPAdapter_plus`, guía https://docs.comfy.org/controlnet-guide

## L2 Alteration (activa cuando IPAdapter instalado)

Batch mood refs → CLIPVision → IPAdapterUnifiedLoader weight 0.8 (product) + Canny producto 0.12/0.39 + KSampler denoise 0.75 → `n_06-B-02`. L1 + IPA style 0.65 opcional sobre este v1.

## Fallback cuando IPAdapter ausente

VAEEncode del producto escalado 512 → KSampler denoise 0.65, misma seed. Mantiene composición con re-estilo leve.
