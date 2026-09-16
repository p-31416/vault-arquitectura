---
tipo: guia
mvp: 04
version: 1.1.0
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-19
tags: [mvp_04, modelos, comfyui, hardware, arquitectura]
---

# Modelos Recomendados para Render Arquitectónico en ComfyUI

## Escenarios de Hardware

### Escenario A: Tu hardware actual — AMD RX 570 8GB VRAM (DirectML)

Tarjeta AMD RX 570 con 8GB VRAM, corriendo ComfyUI vía DirectML. Modelos recomendados:

| # | Modelo | Tipo | VRAM | Calidad | Velocidad | Descarga | Licencia |
|---|--------|------|------|---------|-----------|----------|----------|
| 1 | **ArchitectureRealmix v1.1** | Checkpoint SD1.5 | ✅ ya instalado | ⭐⭐⭐ | ⚡⚡⚡ | [CivitAI](https://civitai.com/models/84958/architecturerealmix) | OpenRAIL-M |
| 2 | **Juggernaut XL v9** | Checkpoint SDXL | ⬇️ descargando (7.11 GB) | ⭐⭐⭐⭐⭐ | ⭐⚡⚡ | [HF: RunDiffusion/Juggernaut-XL-v9](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9) | OpenRAIL++ |
| 3 | **Z-Image Turbo GGUF Q4_K_S** | Checkpoint (DiT) | ~4GB | ⭐⭐⭐⭐ | ⚡⚡⚡⚡ | [HF: city96/Z-Image-Turbo-GGUF](https://huggingface.co/city96/Z-Image-Turbo-GGUF) | Apache 2.0 |
| 4 | **Z-Image Base GGUF Q4_K_S** | Checkpoint (DiT) | ~6GB | ⭐⭐⭐⭐⭐ | ⚡⚡ | [HF: city96/Z-Image-Base-GGUF](https://huggingface.co/city96/Z-Image-Base-GGUF) | Apache 2.0 |
| 5 | **Flux schnell GGUF Q4_K_S** | Checkpoint (DiT) | ~8GB | ⭐⭐⭐⭐⭐ | ⚡⚡⚡ | [HF: city96/FLUX.1-schnell-GGUF](https://huggingface.co/city96/FLUX.1-schnell-GGUF) | Apache 2.0 |
| 6 | **ERNIE-Image Turbo GGUF** | Checkpoint (DiT) | ~4GB | ⭐⭐⭐⭐ | ⚡⚡⚡⚡ | [HF: city96/ERNIE-Image-Turbo-GGUF](https://huggingface.co/city96/ERNIE-Image-Turbo-GGUF) | Apache 2.0 |
| 7 | **4x_foolhardy_Remacri** | Upscaler | ~100MB | ⭐⭐⭐⭐ | ⚡⚡⚡ | [HF: locon/4x_foolhardy_Remacri](https://huggingface.co/locon/4x_foolhardy_Remacri) | CC BY-NC |
| 8 | **4x-ClearRealityV1** | Upscaler | ~100MB | ⭐⭐⭐⭐⭐ | ⚡⚡ | [HF: philz1337/4x-ClearRealityV1](https://huggingface.co/philz1337/4x-ClearRealityV1) | CC BY-NC |
| 9 | **LoRAs de arquitectura en CivitAI** | LoRA | ~10MB | Variable | N/A | [CivitAI: architecture LoRAs](https://civitai.com/tag/architecture) | Varía |

#### Modelos instalados actualmente

| Archivo | Tipo | Tamaño | Estado |
|---------|------|--------|--------|
| `architecturerealmix_v11.safetensors` | Checkpoint SD1.5 | 2.1 GB | ✅ Instalado |
| `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | Checkpoint SDXL | 7.11 GB | ⬇️ Descargando |
| `control_v11p_sd15_canny.safetensors` | ControlNet SD1.5 FP16 | 689 MB | ✅ Instalado |
| `control_v11f1p_sd15_depth_fp16.safetensors` | ControlNet SD1.5 FP16 | 689 MB | ✅ Instalado |

#### Sugeridos para descargar (próximos)

| Modelo | Tipo | Tamaño aprox. | Por qué | Link |
|--------|------|----------------|---------|------|
| **RealArchMix XL v2.0** | Checkpoint SDXL | 6.94 GB | Específico arquitectura, interiores + exteriores | [HF: John6666/realarchmix-xl-v20-sdxl](https://huggingface.co/John6666/realarchmix-xl-v20-sdxl) |
| **Z-Image Turbo GGUF Q4_K_S** | Checkpoint DiT | ~4 GB | Turbo 8 pasos, ideal para iteración rápida | [HF: city96/Z-Image-Turbo-GGUF](https://huggingface.co/city96/Z-Image-Turbo-GGUF) |
| **Flux schnell GGUF Q4_K_S** | Checkpoint DiT | ~8 GB | 4 pasos, máxima velocidad | [HF: city96/FLUX.1-schnell-GGUF](https://huggingface.co/city96/FLUX.1-schnell-GGUF) |
| **4x_foolhardy_Remacri** | Upscaler | ~100 MB | Upscale renders finales | [HF: locon/4x_foolhardy_Remacri](https://huggingface.co/locon/4x_foolhardy_Remacri) |
| **ControlNet Union SDXL** | ControlNet SDXL | ~1.5 GB | Control geométrico unificado para SDXL | [HF: xinsir/controlnet-union-sdxl-1.0](https://huggingface.co/xinsir/controlnet-union-sdxl-1.0) |

#### Recomendación prioritaria (AMD 8GB)

**Orden de instalación sugerido:**

1. ✅ **ArchitectureRealmix v1.1** — Ya instalado. Arrancá acá para tests inmediatos (SD 1.5, liviano).
2. ⬇️ **Juggernaut XL v9** — El mejor fotorrealismo SDXL. Funciona para arquitectura, interiores, exteriores, y todo tipo de renders. **Cabe en 8GB** pero justo — usar resolución 832x1216 o 1216x832.
3. ⬇️ **Z-Image Turbo GGUF Q4_K_S** — Alternativa ligera turbo (~4GB) para iteración rápida.
4. ⬇️ **4x_foolhardy_Remacri** — Upscale de renders finales sin perder calidad.

**Configuración Juggernaut XL v9 en tu hardware:**

```bash
# Settings óptimos para AMD 8GB VRAM
Sampler: DPM++ 2M Karras
Steps: 30-40
CFG: 3-7 (menos = más realista)
Resolution: 832x1216 (portrait) / 1216x832 (landscape)
VAE: Ya incluido en el checkpoint
Upscale: 4xNMKD-Siax_200k, 15 steps, 0.3 denoise, 1.5x
```

**Configuración AMD DirectML:**

```bash
# Lanzar ComfyUI con soporte AMD
python main.py --directml

# Si hay OOM (out of memory):
python main.py --directml --lowvram --gpu-only

# Con comfy-cli:
comfy launch -- --directml --lowvram
```

**Atención AMD:** Algunos nodos (especialmente ciertos ControlNets) pueden no ser compatibles con DirectML. En ese caso, caen a CPU automáticamente pero son más lentos. Para producción, considerar NVIDIA o RunPod.

---

### Escenario B: Hardware ideal recomendado (producción)

Para el estudio cuando se invierta en hardware dedicado:

#### Opción recomendada: NVIDIA RTX 4090 24GB

| Componente | Especificación | Precio aprox (USD) |
|------------|---------------|-------------------|
| GPU | NVIDIA RTX 4090 24GB GDDR6X | $1,800-2,000 |
| RAM | 64GB DDR5 | $200-300 |
| CPU | Intel i7-14700K / AMD 7950X | $400-500 |
| SSD | NVMe 2TB | $150-200 |
| **Total** | | **~$2,600-3,000** |

#### Opción profesional: NVIDIA RTX 6000 Ada 48GB

Para oficina compartida o servidor de renders — $6,800+ (ideal si 3+ personas usan el mismo equipo vía red).

#### Modelos para hardware ideal

| # | Modelo | Tipo | VRAM | Calidad | Velocidad | Ideal para | Descarga |
|---|--------|------|------|---------|-----------|------------|----------|
| 1 | **Flux.1 Dev** | Checkpoint DiT 12B | ~24GB fp16 | ⭐⭐⭐⭐⭐ | ⚡⚡ | Renders finales fotorrealistas | [HF: black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) |
| 2 | **Flux.1 Schnell** | Checkpoint DiT 12B | ~24GB fp16 | ⭐⭐⭐⭐⭐ | ⚡⚡⚡ | Renders rápidos, 4 pasos | [HF: black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) |
| 3 | **SDXL 1.0** | Checkpoint | ~12GB | ⭐⭐⭐⭐ | ⚡⚡⚡ | Render general, ecosistema enorme | [HF: stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) |
| 4 | **SDXL LoRAs arquitectura** | LoRA | ~100MB | ⭐⭐⭐⭐ | N/A | Estilos específicos (brutalista, high-tech, etc.) | [CivitAI: SDXL architecture](https://civitai.com/models/354774/sdxl-architecture-interior-design) |
| 5 | **Z-Image Base (fp8)** | Checkpoint DiT 6B | ~8GB | ⭐⭐⭐⭐⭐ | ⚡⚡⚡ | Ideal para iteración, gran calidad | [HF: Comfy-Org/Z-Image-Base](https://huggingface.co/Comfy-Org/Z-Image-Base) |
| 6 | **Qwen-Image GGUF Q8_0** | Checkpoint DiT 20B | ~24GB | ⭐⭐⭐⭐⭐ | ⚡ | Combinación con WAN video | [HF: city96/Qwen-Image-GGUF](https://huggingface.co/city96/Qwen-Image-GGUF) |
| 7 | **WAN 2.2 T2V A14B** | Video DiT | ~24GB fp8 | ⭐⭐⭐⭐ | ⚡ | Texto → video arquitectónico | [HF: Wan-AI/Wan2.2-T2V-14B](https://huggingface.co/Wan-AI/Wan2.2-T2V-14B) |
| 8 | **WAN 2.2 I2V A14B** | Video DiT | ~24GB fp8 | ⭐⭐⭐⭐ | ⚡ | Imagen → walkthrough animado | [HF: Wan-AI/Wan2.2-I2V-14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-14B) |
| 9 | **LTX-2.3 GGUF Q8_0** | Video DiT 22B | ~24GB | ⭐⭐⭐⭐ | ⚡⚡ | Video + audio sincronizado | [HF: city96/LTX-2.3-GGUF](https://huggingface.co/city96/LTX-2.3-GGUF) |
| 10 | **KREA 2 Turbo** | Checkpoint | ~12GB | ⭐⭐⭐⭐⭐ | ⚡⚡⚡⚡ | Turbo ultra-rápido, 8 pasos | [HF: Comfy-Org/KREA2](https://huggingface.co/Comfy-Org/KREA2) |
| 11 | **ControlNet Union (SDXL)** | ControlNet | ~1.5GB | ⭐⭐⭐⭐⭐ | N/A | Control geométrico unificado | [HF: xinsir/controlnet-union-sdxl-1.0](https://huggingface.co/xinsir/controlnet-union-sdxl-1.0) |
| 12 | **4x-ClearRealityV1** | Upscaler | ~100MB | ⭐⭐⭐⭐⭐ | ⚡⚡ | Upscale renders finales | [HF: philz1337/4x-ClearRealityV1](https://huggingface.co/philz1337/4x-ClearRealityV1) |

---

### Escenario C: Cloud (RunPod / Vast.ai)

Para cuando se necesite potencia sin inversión inicial:

**RunPod:**
- GPU: RTX 4090 24GB ~$0.39/hora
- GPU: RTX 6000 Ada 48GB ~$0.79/hora
- Storage: $0.0007/GB/hora
- Template recomendado: "ComfyUI (with comfy-cli)"

**Costo estimado:**
- Sesión de render intensiva (4h): ~$1.60-$3.20
- Iteración diaria (1h): ~$0.40/día → ~$8/mes
- vs. Comfy Cloud: $20/mes base + créditos

## Guía de instalación de modelos

### Desde Opencode (recomendado, usa MCP)

```bash
# Z-Image Turbo GGUF Q4_K_S
comfyui_download_model(
  url="https://huggingface.co/city96/Z-Image-Turbo-GGUF/resolve/main/z-image-turbo-Q4_K_S.gguf",
  target_subfolder="checkpoints"
)

# 4x_foolhardy_Remacri (upscaler)
comfyui_download_model(
  url="https://huggingface.co/locon/4x_foolhardy_Remacri/resolve/main/4x_foolhardy_Remacri.pth",
  target_subfolder="upscale_models"
)
```

### Desde CivitAI

```bash
# Buscar modelos de arquitectura
comfyui_search_civitai_models(query="architecture", types=["Checkpoint","LORA"])

# Descargar
comfyui_download_civitai_model(model_id=35080, target_subfolder="checkpoints")
```

### Manual (descargar y copiar)

Descargar a `P:\00-repos\ComfyUI\models\<tipo>\`:

| Tipo de modelo | Carpeta destino |
|----------------|-----------------|
| Checkpoints | `models/checkpoints/` |
| LoRAs | `models/loras/` |
| VAEs | `models/vae/` |
| Upscalers | `models/upscale_models/` |
| ControlNet | `models/controlnet/` |
| Text Encoders | `models/text_encoders/` |
| Clip | `models/clip/` |

## LoRAs de arquitectura recomendados

| LoRA | Base Model | Descripción | Link |
|------|-----------|-------------|------|
| Architecture Interior SDXL | SDXL | Estilos de interiores, muebles, materiales | [CivitAI](https://civitai.com/models/354774) |
| Architectural Visualization | SD 1.5 | Renders de visualización arquitectónica | [CivitAI](https://civitai.com/models/119936) |
| Modern Architecture | SDXL | Arquitectura moderna minimalista | [CivitAI](https://civitai.com/tag/architecture) |
| Texture Pack | SDXL | Texturas de materiales (hormigón, madera, metal) | Buscar en CivitAI |

## Comparativa rápida por uso arquitectónico

| Uso | AMD 8GB | NVIDIA 24GB+ | Cloud (RunPod) |
|-----|---------|--------------|----------------|
| Concepto rápido (txt2img) | Juggernaut XL v9, ArchitectureRealmix, Z-Image Turbo | Flux Schnell, KREA 2 | Flux Dev |
| Croquis → Render (img2img) | Juggernaut XL v9 + denoise, Z-Image Turbo | SDXL + ControlNet Sketch | SDXL + Union |
| Render fotorrealista | Juggernaut XL v9 + upscale | Flux Dev + upscale 4x | Flux Dev + 4x |
| Cambiar material (inpaint) | Z-Image Inpainting | SDXL Inpaint + ControlNet | Qwen-Image-Edit |
| Video walkthrough | ❌ No recomendado | WAN / LTX-2.3 | WAN / LTX-2.3 |
| Batch de variantes | ArchitectureRealmix (rápido), Z-Image Turbo (8 pasos) | KREA 2 (8 pasos) | Flux Schnell (4 pasos) |

## Referencias

- [Hugging Face — Architecture Models](https://huggingface.co/models?search=architecture)
- [CivitAI — Architecture Tag](https://civitai.com/tag/architecture)
- [ComfyUI Models Directory](https://comfyui.art/models)
- [[wiki/estudio/adr-001-comfyui-mcp]] — Licencias y propiedad intelectual
- [Stability AI Community License](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium/blob/main/LICENSE.md)
- [Black Forest Labs — Flux License](https://blackforestlabs.ai)
