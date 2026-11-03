# Sesión 2026-11-02 — WF-01 ×3 modelos, inpainting local, WF-Comfy-YT, pod, token Civitai

## Qué se hizo

1. **WF-01, 3 corridas (una por modelo)**: R1 Juggernaut v9 control, R2 RealVisXL v5.0 con receta de la casa (bajo spec del autor → salió mal: necesita `dpmpp_sde`/30 o `dpmpp_2m`/50+), R3 Lightning descartado (resultado pésimo). Prompt v2 plaza + mosaico Escher documentado como variante. Advertencia registrada: 512² no es representativo en SDXL.
2. **Inpainting loggia local**: del PNG con metadata se extrajo el flujo Nano Banana (partner) y se reconstruyó 100 % local (`workflow_inpaint-loggia-local_sdxl.json`, Juggernaut + SetLatentNoiseMask + denoise 0,7).
3. **Carpeta `workflows/WF-Comfy-YT/`** con plantilla de análisis + `YT-01` (Diffused.A Studio, SDXL inpainting). Forensia de 35 frames: checkpoint exacto `juggernautXL_ragnarokBy.safetensors` (= Ragnarok oficial, SHA256 idéntico), LoRA exacto `XL_sdxlaang_Aerial-Render` (0,85/1,00, solo en pack del autor), receta exacta (VAE for Inpainting grow 6, `uni_pc_bh2`/30/3,5/denoise 1,0, Union promax + DepthAnything strength 0,15). JSON del autor tras paywall USD 7,99 → reconstrucción propia.
4. **Docs 00**: pod general, pod Flux económico (A5000 $0,16/h), Comfy $20 vs RunPod ($20 = 5,7 h vs 125 h; LoRA local obliga pod), instalación paso a paso, ciclo n8n start→run→stop (API v2).
5. **Civitai token**: `CIVITAI_API_TOKEN` en `.env` (Read Only alcanza; Buzz OFF irrelevante; sin límites salvo 429). Descargado y verificado: LoRA 36 MB, Ragnarok 6,62 GB (SHA256 OK), Union promax 2,34 GB. Pendiente: `download_model` del agente no ancla `models/` (main.py relativo) → fix con ruta absoluta en el `.bat` + reinicio + reconnect.
6. **Rename detectado**: `sdxl-vista/` → `WF-curso/` (ediciones propias sobrevivieron; links corregidos).

## Archivos

- Creados: `WF-Comfy-YT/{00-index,00-pod-runpod-comfyui,00-pod-flux-economico,00-comfy-vs-runpod,00-pod-instalar-comfy-paso-a-paso,00-n8n-ciclo-pod,YT-01-sdxl-inpainting-diffuseda,workflow_YT-01-sdxl-inpainting}.md|json`, `WF-curso/workflow_inpaint-loggia-local_sdxl.json`, `.env:CIVITAI_API_TOKEN`.
- Modificados: `WF-curso/{WF-01_sdxl,00-modelos-sdxl-a-probar}.md`, `WF-Comfy-YT/{00-index,YT-01}*.md`, workspace default → `P:\00-repos\ComfyUI`.
- Modelos en disco: `loras/ArteFactoryLab_LORA-10`, `checkpoints/juggernautXL_ragnarok` (hash OK), `controlnet/XL_controlnet-union-sdxl_promax`.

## Cerebro digital

- **Topics**: comparativa SDXL por modelo, inpainting local vs API, forensia de video, RunPod económico, Comfy Cloud pricing, token Civitai.
- **Entidades**: Juggernaut Ragnarok (133005/1759168), RealVisXL v5.0, Union promax (xinsir), LoRA `XL_sdxlaang_Aerial-Render` (autor), A5000 $0,16/h, Comfy Standard $20 = 5,7 h.
- **Hechos**: Lightning fuera del set; R2 falló por steps insuficientes para 2M; LoRA exacto no es público; token Read Only + Buzz OFF; descargas OK por curl; resolver MCP pendiente de fix.
