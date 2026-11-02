---
tipo: guia
mvp: 04
version: 1.4.0
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-11-01
tags: [mvp_04, modelos, comfyui, hardware, arquitectura]
---

# Modelos Recomendados para Render Arquitectónico en ComfyUI

## Escenarios de Hardware

### Escenario A: Tu hardware actual — AMD RX 570 8GB VRAM (DirectML)

Tarjeta AMD RX 570 con 8GB VRAM, corriendo ComfyUI vía DirectML. Modelos recomendados:

| #   | Modelo                               | Tipo             | VRAM                     | Calidad  | Velocidad | Descarga                                                                                  | Licencia   |
| --- | ------------------------------------ | ---------------- | ------------------------ | -------- | --------- | ----------------------------------------------------------------------------------------- | ---------- |
| 1   | **ArchitectureRealmix v1.1**         | Checkpoint SD1.5 | ✅ ya instalado           | ⭐⭐⭐      | ⚡⚡⚡       | [CivitAI](https://civitai.com/models/84958/architecturerealmix)                           | OpenRAIL-M |
| 2   | **Juggernaut XL v9**                 | Checkpoint SDXL  | ✅ instalado (6.62 GiB)   | ⭐⭐⭐⭐⭐    | ⭐⚡⚡       | [HF: RunDiffusion/Juggernaut-XL-v9](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9) | OpenRAIL++ |
| 2b  | **RealVisXL V5.0 fp16 BakedVAE**     | Checkpoint SDXL  | ✅ instalado (6.46 GiB) 2026-11-01 | ⭐⭐⭐⭐⭐    | ⭐⭐⚡⚡      | [CivitAI v789646 fp16](https://civitai.com/models/139562?modelVersionId=789646) · [doc parámetros](https://civitai.com/models/139562) | merge OpenRAIL, **licencia a confirmar en ficha antes de uso comercial** |
| 2c  | **RealVisXL V5.0 Lightning fp16 BakedVAE** | Checkpoint SDXL destilado | ✅ instalado (6.46 GiB) 2026-11-01 | ⭐⭐⭐⭐     | ⚡⚡⚡⚡      | [CivitAI v798204 fp16](https://civitai.com/models/139562?modelVersionId=798204) · [doc parámetros](https://civitai.com/models/139562) | merge OpenRAIL, **licencia a confirmar en ficha antes de uso comercial** |
| 3   | **Z-Image Turbo GGUF Q4_K_S**        | Checkpoint (DiT) | ~4GB                     | ⭐⭐⭐⭐     | ⚡⚡⚡⚡      | [HF: city96/Z-Image-Turbo-GGUF](https://huggingface.co/city96/Z-Image-Turbo-GGUF)         | Apache 2.0 |
| 4   | **Z-Image Base GGUF Q4_K_S**         | Checkpoint (DiT) | ~6GB                     | ⭐⭐⭐⭐⭐    | ⚡⚡        | [HF: city96/Z-Image-Base-GGUF](https://huggingface.co/city96/Z-Image-Base-GGUF)           | Apache 2.0 |
| 5   | **Flux schnell GGUF Q4_K_S**         | Checkpoint (DiT) | ~8GB                     | ⭐⭐⭐⭐⭐    | ⚡⚡⚡       | [HF: city96/FLUX.1-schnell-GGUF](https://huggingface.co/city96/FLUX.1-schnell-GGUF)       | Apache 2.0 |
| 6   | **ERNIE-Image Turbo GGUF**           | Checkpoint (DiT) | ~4GB                     | ⭐⭐⭐⭐     | ⚡⚡⚡⚡      | [HF: city96/ERNIE-Image-Turbo-GGUF](https://huggingface.co/city96/ERNIE-Image-Turbo-GGUF) | Apache 2.0 |
| 7   | **4x_foolhardy_Remacri**             | Upscaler         | ~100MB                   | ⭐⭐⭐⭐     | ⚡⚡⚡       | [HF: locon/4x_foolhardy_Remacri](https://huggingface.co/locon/4x_foolhardy_Remacri)       | CC BY-NC   |
| 8   | **4x-ClearRealityV1**                | Upscaler         | ~100MB                   | ⭐⭐⭐⭐⭐    | ⚡⚡        | [HF: philz1337/4x-ClearRealityV1](https://huggingface.co/philz1337/4x-ClearRealityV1)     | CC BY-NC   |
| 9   | **LoRAs de arquitectura en CivitAI** | LoRA             | ~10MB                    | Variable | N/A       | [CivitAI: architecture LoRAs](https://civitai.com/tag/architecture)                       | Varía      |
|     |                                      |                  |                          |          |           |                                                                                           |            |
|     |                                      |                  |                          |          |           |                                                                                           |            |

#### Modelos instalados actualmente

> Leyenda comercial: ✅ = uso comercial permitido · ⚠️ = limitado/condicional (leer condiciones) · ⛔ = NO comercial.
> `Image/Rent/Sell` = valores de `allowCommercialUse` en Civitai (`Image` vender imágenes, `Rent` ofrecer generación como servicio, `Sell` vender el modelo/merges; `RentCivit` = solo dentro de Civitai). Open RAIL-M/++ = licencias StabilityAI/RunDiffusion: los outputs son tuyos, con restricciones por escrito.

**CHECKPOINTS instalados**

| Archivo | Base / peso | Para qué sirve | Comercial | Licencia / condiciones |
|---------|-------------|----------------|-----------|------------------------|
| `architecturerealmix_v11.safetensors` | SD 1.5 · 2.1 GB | Arquitectura/urbano/interior fotorreal liviano | ⛔ **NO** | El autor lo prohíbe explícitamente ([Civitai 84958](https://civitai.com/models/84958)): solo estudio personal; ni enseñanza sin su permiso + atribución. **Solo tests internos, nunca láminas de cliente** |
| `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | SDXL · 6.62 GiB | Fotorrealismo general, probado en agencias | ✅ con límite | [Open RAIL-M](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9) + cláusula RunDiffusion: **prohibido desplegarlo detrás de APIs pagas** sin licencia (`juggernaut@rundiffusion.com`). Renders para clientes OK |
| `realvisxlV50_v50Bakedvae.safetensors` | SDXL fp16 · 6.46 GiB | Calidad final (30-35 steps) | ✅ | Open RAIL++-M ([realvisxl.com](https://realvisxl.com/)). SHA256 verificado 2026-11-01 |
| `realvisxlV50_v50LightningBakedvae.safetensors` | SDXL fp16 destilado · 6.46 GiB | Iteración rápida (4-6 steps, CFG 1-2) | ✅ | Idem anterior. SHA256 verificado 2026-11-01 |
| `sd-v1-5-inpainting-fp16.safetensors` | SD 1.5 · 2.1 GB | Inpaint/outpaint | ✅ | Open RAIL-M (base `runwayml/stable-diffusion-inpainting`) |

**LORAS instaladas**

| Archivo | Base | Para qué sirve | Comercial | Licencia / condiciones |
|---------|------|----------------|-----------|------------------------|
| `ArcvizXL_V01.safetensors` | SDXL 870 MB | Interior + exterior archviz | ✅ | `Image/Rent/Sell` ([Civitai 549260](https://civitai.com/models/549260)) |
| `Architecture_Building.safetensors` | SD 1.5 218 MB | Edificios públicos, vistas aéreas | ✅ | `Image/Rent/Sell` ([Civitai 100737](https://civitai.com/models/100737)) |
| `markerhandsketch-V1.safetensors` | SD 1.5 9 MB | Croquis estilo marker | ✅ | `Image/Rent/Sell` ([Civitai 34384](https://civitai.com/models/34384)) |
| `Architectural_Massing.safetensors` | SDXL 218 MB | Massing/conceptos volumétricos | ⚠️ solo RentCivit | Sin `Image`: NO vender imágenes fuera de Civitai ([Civitai 724833](https://civitai.com/models/724833)) |
| `JJ_Archvizcg_v2.safetensors` | SDXL? 144 MB | Hoteles/edificios (jjhuang) | ⚠️ solo RentCivit | Idem anterior |
| `sandiese.safetensors` | SD 1.5 36 MB | Conceptos arquitectura | ⛔ | `allowCommercialUse` vacío |
| `xsarchitectural-10superhighrise… .safetensors` | SDXL? 36 MB | Supertorres (familia XSarchitectural) | ⛔ probable | La familia XSarchitectural declara `[]` (verificado en 5 variantes) |
| `archisketch-v1.safetensors` | ? 18 MB | Boceto arquitectónico | ⚠️ origen sin confirmar | No matchea CWG (ese prohíbe comercial explícito). Verificar hash vs ficha antes de usar |
| `SLskyscraperrenderingXL_V1.0.safetensors` | SDXL 870 MB | Rascacielos render | ⚠️ origen sin confirmar | Sin match en Civitai. Verificar antes de uso comercial |
| `landscape_architecture_sketch.safetensors` · `isometric-v1.safetensors` · `BrutalistTech-20.safetensors` · `room.safetensors` · `bookstore-xl.safetensors` · `baroque_architecture-….safetensors` · `Le Corbusier … .safetensors` | varios | varios | ⚠️ ver ficha | Buscar cada nombre en Civitai y leer `allowCommercialUse` |
| `rhino-to-image-lora.basic.safetensors` | FLUX.2 121 MB | LoRA del curso Gaudí (interno) | ✅ propio | Entrenado por el estudio |

**CONTROLNET + UPSCALER**

| Archivo | Para qué sirve | Comercial | Licencia / condiciones |
|---------|----------------|-----------|------------------------|
| `control_v11p_sd15_canny/depth_fp16/scribble.safetensors` | Control geométrico SD 1.5 | ✅ | `openrail` (lllyasviel). Derivados fp16 comunitarios |
| `RealESRGAN_x4plus.pth` | Upscale final | ⚠️ confirmar | Código BSD-3-Clause; pesos sin restricción adicional declarada — confirmar antes de producción masiva |

**Regla operativa del estudio**: para láminas/entregables de cliente usar SOLO filas ✅ (Juggernaut con su cláusula, RealVisXL, ArcvizXL, Architecture_Building, markerhandsketch, inpainting, ControlNets lllyasviel). Todo lo ⛔/⚠️ queda para exploración interna salvo verificación escrita en esta tabla.

#### Sugeridos para descargar (próximos)

| Modelo | Tipo | Tamaño aprox. | Por qué | Link | Estado |
|--------|------|---------------|---------|------|--------|
| **RealArchvis XL v5.0** | Checkpoint SDXL | 6.46 GiB | Específico arquitectura | [CivitAI 533040](https://civitai.com/models/533040) | ⛔ **Generation-Only por decisión del creador** (verificado en ficha 2026-11-01): NO descargable por diseño — ni login ni token lo destraban. Uso: solo onsite con Buzz (subasta ~10-20 k/semana). Vigilar mirror en [CivArchive](https://civarchive.com/models/533040) |
| **RealArchmix XL v3.5** (jjhuang) | Checkpoint SDXL fp16 | 6.46 GiB | Espacios+arquitectura/interior/paisaje, compatible con sus LoRAs | [CivitAI 1323614](https://civitai.com/models/1323614?modelVersionId=2066579) | ⛔ Bloqueado 2026-11-01: `requires login` (SHA256 B6C880D8FC8884AD…). **Se destraba con cuenta+token Civitai** |
| **Natty Realistic SDXL v2.0** | Checkpoint SDXL fp16 | 6.46 GiB | Fotorreal general, 78 reviews muy positivas (ago-2025) | [CivitAI 1884205](https://civitai.com/models/1884205/natty-realistic-sdxl) | ✅ Descarga abierta + espejos TensorArt/SeaArt — candidato D-modelo |
| **Juggernaut XL v13 Ragnarok** | Checkpoint SDXL | 6.6 GiB | Mejora anatomía/manos vs v9-v11 (feb-2026, según InsiderLLM) | Buscar "Juggernaut Ragnarok" en Civitai | Candidato a probar (verificar descarga anónima antes) |
| **RealArchMix XL v2.0** | Checkpoint SDXL | 6.94 GB | Específico arquitectura, interiores + exteriores | [HF: John6666/realarchmix-xl-v20-sdxl](https://huggingface.co/John6666/realarchmix-xl-v20-sdxl) | ⚠️ Formato diffusers/ (carpeta, no .safetensors único) — no prioritario |
| **Z-Image Turbo GGUF Q4_K_S** | Checkpoint DiT | ~4 GB | Turbo 8 pasos, ideal para iteración rápida | [HF: city96/Z-Image-Turbo-GGUF](https://huggingface.co/city96/Z-Image-Turbo-GGUF) |
| **Flux schnell GGUF Q4_K_S** | Checkpoint DiT | ~8 GB | 4 pasos, máxima velocidad | [HF: city96/FLUX.1-schnell-GGUF](https://huggingface.co/city96/FLUX.1-schnell-GGUF) |
| **4x_foolhardy_Remacri** | Upscaler | ~100 MB | Upscale renders finales | [HF: locon/4x_foolhardy_Remacri](https://huggingface.co/locon/4x_foolhardy_Remacri) |
| **ControlNet Union SDXL** | ControlNet SDXL | ~1.5 GB | Control geométrico unificado para SDXL | [HF: xinsir/controlnet-union-sdxl-1.0](https://huggingface.co/xinsir/controlnet-union-sdxl-1.0) |

#### Recomendación prioritaria (AMD 8GB)

**Orden de instalación sugerido:**

1. ✅ **ArchitectureRealmix v1.1** — Ya instalado. SOLO tests internos: su licencia **prohíbe uso comercial** (ver cuadro). Para láminas de cliente usar RealVisXL/Juggernaut.
2. ✅ **Juggernaut XL v9** — Instalado. Fotorrealismo SDXL para arquitectura, interiores, exteriores.
3. ✅ **RealVisXL V5.0 + Lightning (2026-11-01)** — Instalados. Lightning para iteración rápida (4-8 pasos), estándar para calidad final.
4. ⬇️ **Z-Image Turbo GGUF Q4_K_S** — Alternativa ligera turbo (~4GB) para iteración rápida.
5. ⬇️ **4x_foolhardy_Remacri** — Upscale de renders finales sin perder calidad.

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

**Configuración RealVisXL V5.0 en tu hardware (verificado 2026-11-01):**

```bash
# Lightning (fase R rápida — doc oficial del creador)
Sampler: DPM++ SDE Karras (o DPM++ SDE)
Steps: 4-6
CFG: 1-2.5
Resolution fase R: 768x512 / 1024x640
Negative: (worst quality, low quality, illustration, 3d, 2d, painting, cartoons, sketch), open mouth
ENSD: 31337 (opcional, semilla de ruido del creador)

# Estándar V5.0 (fase Q calidad)
Sampler: DPM++ SDE Karras (30+ steps) o DPM++ 2M Karras (50+ steps)
Steps: 30-35
CFG: 3-4
Resolution: 1216x832 (landscape) / 832x1216 (portrait)
Negative: blurry, low quality, distorted, watermark, text, signature, cartoon, illustration,
          warped perspective, melting geometry, bent windows (+ people si vacía)

# Hires Fix (ambos, doc oficial)
Upscaler: 4x-UltraSharp o 4x-NMKD-Superscale
Denoise: 0.1-0.3 (Lightning: 3 steps, denoise 0.5)
Upscale: 1.1-1.5x
```

**Por qué estos dos archivos rinden en la RX 570:**
- **fp16**: 6.46 GiB vs 12.92 GiB del fp32 — la mitad de VRAM en pesos
- **BakedVAE**: el servidor tiene `models/vae/` VACÍO — sin VAE horneado estos checkpoints no decodificarían
- **Lightning destilado**: 4-6 pasos en vez de 30-50 → cada test de la fase R tarda minutos, no 651 s
- **Flags ya activos en tu línea de arranque** (verificados en el proceso vivo PID 5176): `--directml 0 --force-fp16 --disable-cuda-malloc --lowvram --cpu-vae --disable-dynamic-vram

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

| #   | Modelo                      | Tipo               | VRAM       | Calidad | Velocidad | Ideal para                                        | Descarga                                                                                                        |
| --- | --------------------------- | ------------------ | ---------- | ------- | --------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 1   | **Flux.1 Dev**              | Checkpoint DiT 12B | ~24GB fp16 | ⭐⭐⭐⭐⭐   | ⚡⚡        | Renders finales fotorrealistas                    | [HF: black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)                         |
| 2   | **Flux.1 Schnell**          | Checkpoint DiT 12B | ~24GB fp16 | ⭐⭐⭐⭐⭐   | ⚡⚡⚡       | Renders rápidos, 4 pasos                          | [HF: black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell)                 |
| 3   | **SDXL 1.0**                | Checkpoint         | ~12GB      | ⭐⭐⭐⭐    | ⚡⚡⚡       | Render general, ecosistema enorme                 | [HF: stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) |
| 4   | **SDXL LoRAs arquitectura** | LoRA               | ~100MB     | ⭐⭐⭐⭐    | N/A       | Estilos específicos (brutalista, high-tech, etc.) | [CivitAI: SDXL architecture](https://civitai.com/models/354774/sdxl-architecture-interior-design)               |
| 5   | **Z-Image Base (fp8)**      | Checkpoint DiT 6B  | ~8GB       | ⭐⭐⭐⭐⭐   | ⚡⚡⚡       | Ideal para iteración, gran calidad                | [HF: Comfy-Org/Z-Image-Base](https://huggingface.co/Comfy-Org/Z-Image-Base)                                     |
| 6   | **Qwen-Image GGUF Q8_0**    | Checkpoint DiT 20B | ~24GB      | ⭐⭐⭐⭐⭐   | ⚡         | Combinación con WAN video                         | [HF: city96/Qwen-Image-GGUF](https://huggingface.co/city96/Qwen-Image-GGUF)                                     |
| 7   | **WAN 2.2 T2V A14B**        | Video DiT          | ~24GB fp8  | ⭐⭐⭐⭐    | ⚡         | Texto → video arquitectónico                      | [HF: Wan-AI/Wan2.2-T2V-14B](https://huggingface.co/Wan-AI/Wan2.2-T2V-14B)                                       |
| 8   | **WAN 2.2 I2V A14B**        | Video DiT          | ~24GB fp8  | ⭐⭐⭐⭐    | ⚡         | Imagen → walkthrough animado                      | [HF: Wan-AI/Wan2.2-I2V-14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-14B)                                       |
| 9   | **LTX-2.3 GGUF Q8_0**       | Video DiT 22B      | ~24GB      | ⭐⭐⭐⭐    | ⚡⚡        | Video + audio sincronizado                        | [HF: city96/LTX-2.3-GGUF](https://huggingface.co/city96/LTX-2.3-GGUF)                                           |
| 10  | **KREA 2 Turbo**            | Checkpoint         | ~12GB      | ⭐⭐⭐⭐⭐   | ⚡⚡⚡⚡      | Turbo ultra-rápido, 8 pasos                       | [HF: Comfy-Org/KREA2](https://huggingface.co/Comfy-Org/KREA2)                                                   |
| 11  | **ControlNet Union (SDXL)** | ControlNet         | ~1.5GB     | ⭐⭐⭐⭐⭐   | N/A       | Control geométrico unificado                      | [HF: xinsir/controlnet-union-sdxl-1.0](https://huggingface.co/xinsir/controlnet-union-sdxl-1.0)                 |
| 12  | **4x-ClearRealityV1**       | Upscaler           | ~100MB     | ⭐⭐⭐⭐⭐   | ⚡⚡        | Upscale renders finales                           | [HF: philz1337/4x-ClearRealityV1](https://huggingface.co/philz1337/4x-ClearRealityV1)                           |

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

**Tiers gratuitos (sin RunPod ni cloud pago) — verificado 2026-11-01:**

| Vía | Cuota | Uso para el estudio |
|-----|-------|---------------------|
| **Kaggle** | ~30 h GPU/semana (T4x2), sesiones 12 h. Requiere teléfono + Internet ON | ComfyUI entero en notebook para tandas pesadas (video LTX, FLUX). Apagar al terminar |
| **HF ZeroGPU** | 5 min GPU/día (2 min anónimo) | Probar un checkpoint en un Space antes de descargarlo (51 Spaces RealVisXL V5) |
| **Lightning AI** | 15 créditos/mes | Desarrollo puntual |
| **Comfy Cloud free** | 400 créditos | 1-2 corridas de referencia |
| Google Colab free | T4 variable, límites no publicados | ⚠️ Riesgo de ToS con SD — no plan A |

Detalle completo: [[wiki/glosario/software/proveedores-modelos-ia|proveedores-modelos-ia]] § GPU gratis.

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
