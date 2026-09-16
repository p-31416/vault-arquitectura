---
tipo: software
software: comfyui
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-07
tags: [glosario, software, comfyui]
---

# ComfyUI

> Wiki técnica de ComfyUI — nodos, modelos y flujos para el estudio. Migrado de `comfyui/` (legacy: 00-index, architecture-realmix, modelos/*, nodos/*) a archivo único. Hardware objetivo: AMD RX 570 8GB VRAM (DirectML), SD 1.5 principalmente.

- [Hardware objetivo](#hardware-objetivo)
- [Catálogo de modelos — índice](#catalogo-de-modelos--indice)
- [Checkpoint — ArchitectureRealmix v1.1](#checkpoint--architecturerealmix-v11)
- [Checkpoint — Juggernaut XL v9](#checkpoint--juggernaut-xl-v9)
- [Checkpoint — Z-Image Turbo GGUF Q4](#checkpoint--z-image-turbo-gguf-q4)
- [Checkpoint — Flux Schnell GGUF Q4](#checkpoint--flux-schnell-gguf-q4)
- [ControlNet — Canny SD15](#controlnet--canny-sd15)
- [ControlNet — Depth SD15 FP16](#controlnet--depth-sd15-fp16)
- [ControlNet — Union SDXL](#controlnet--union-sdxl)
- [Upscaler — 4x_foolhardy_Remacri](#upscaler--4x_foolhardy_remacri)
- [Upscaler — 4x-ClearRealityV1](#upscaler--4x-clearrealityv1)
- [Catálogo de nodos — índice](#catalogo-de-nodos--indice)
- [Nodo — ImageScale](#nodo--imagescale)
- [Nodo — Canny](#nodo--canny)
- [Nodo — ControlNetLoader](#nodo--controlnetloader)
- [Nodo — ControlNetApplyAdvanced](#nodo--controlnetapplyadvanced)
- [Nodos nativos pendientes](#nodos-nativos-pendientes)
- [Flujos y playbooks](#flujos-y-playbooks)
- [Convención de nombrado y frontmatter](#convencion-de-nombrado-y-frontmatter)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Hardware objetivo

AMD RX 570 8GB VRAM (DirectML), SD 1.5 principalmente. 2 ControlNets a la vez con checkpoint SD 1.5 sin problema. Ver `AGENTS.md: ComfyUI — Generación de Imágenes`.

> Fuente: `comfyui/00-index.md` — `tipo: indice, seccion: comfyui` (2026-07-19).

---

## Catálogo de modelos — índice

> Fuente: `comfyui/modelos/00-index.md` — `tipo: indice, seccion: comfyui-modelos` (2026-07-24). Referencia centralizada de todos los modelos instalados, descargando y recomendados.

### Checkpoints instalados

| Modelo | Tipo | Base | Tamaño | Estado | Uso principal |
|--------|------|------|--------|--------|---------------|
| ArchitectureRealmix v1.1 | Checkpoint | SD 1.5 | 2.1 GB | ✅ Instalado | Renders arquitectura base, iteración rápida |
| Juggernaut XL v9 | Checkpoint | SDXL | 7.11 GB | ⬇️ Descargando | Fotorrealismo arquitectura (int/ext), calidad máxima 8GB |

### Checkpoints pendientes / recomendados

| Modelo | Tipo | Base | Tamaño | Estado | Uso principal |
|--------|------|------|--------|--------|---------------|
| Z-Image Turbo GGUF Q4_K_S | Checkpoint (DiT) | Z-Image | ~4 GB | ⬜ Pendiente | Iteración ultra-rápida (8 pasos) |
| Flux Schnell GGUF Q4_K_S | Checkpoint (DiT) | Flux | ~8 GB | ⬜ Pendiente | Máxima velocidad (4 pasos) |

### ControlNet instalados

| Modelo | Tipo | Base | Tamaño | Estado | Uso |
|--------|------|------|--------|--------|-----|
| ControlNet Canny v11p | ControlNet | SD 1.5 | 689 MB | ✅ Instalado | Control geométrico por bordes/líneas |
| ControlNet Depth v11f1p | ControlNet | SD 1.5 | 689 MB | ✅ Instalado | Control espacial 3D / profundidad |

### ControlNet pendientes

| Modelo | Tipo | Base | Tamaño | Estado | Uso |
|--------|------|------|--------|--------|-----|
| ControlNet Union SDXL | ControlNet | SDXL | ~1.5 GB | ⬜ Pendiente | Control unificado (canny+depth+openpose+etc) |

### Upscalers

| Modelo | Tipo | Tamaño | Estado | Uso |
|--------|------|--------|--------|-----|
| 4x_foolhardy_Remacri | ESRGAN | ~100 MB | ⬜ Pendiente | Upscale renders finales, detalle alto |
| 4x-ClearRealityV1 | ESRGAN | ~100 MB | ⬜ Pendiente | Upscale fotorrealista general |

### LoRAs arquitectura (en investigación)

| LoRA | Base | Tamaño | Estado | Descripción | Fuente |
|------|------|--------|--------|-------------|--------|
| Architecture Interior SDXL | SDXL | ~100 MB | ⬜ Pendiente | Estilos interiores, muebles, materiales | CivitAI |
| Architectural Visualization | SD 1.5 | ~100 MB | ⬜ Pendiente | Renders visualización arquitectónica | CivitAI |
| Modern Architecture | SDXL | ~100 MB | ⬜ Pendiente | Arquitectura moderna minimalista | CivitAI |

---

## Checkpoint — ArchitectureRealmix v1.1

> Fuente: `comfyui/architecture-realmix.md` + `comfyui/modelos/checkpoint-architecturerealmix-v11.md` — `tipo: modelo, categoria: checkpoint, familia: sd1.5, archivo: architecturerealmix_v11.safetensors, tamaño_gb: 2.1, licencia: OpenRAIL-M, fuente: https://civitai.com/models/84958/architecturerealmix, estado: instalado` (2026-07-17/24).

### Descripción

Checkpoint SD 1.5 fine-tuneado para render arquitectónico. Produce renders fotorrealistas de exteriores e interiores en 512x512 a 768x768. Modelo primario actual para iteración rápida y ControlNet en RX 570 8GB.

### Ficha técnica

| Campo | Valor |
|-------|-------|
| **Archivo** | `architecturerealmix_v11.safetensors` |
| **Tipo** | Checkpoint SD 1.5 (merged) |
| **Tamaño** | 2.1 GB |
| **VRAM mínima** | ~3 GB (fp16) |
| **Licencia** | CreativeML OpenRAIL-M |
| **Fuente** | [CivitAI #84958](https://civitai.com/models/84958/architecturerealmix) |
| **Estado** | ✅ Instalado en `models/checkpoints/` |
| **Resolución nativa** | 512x512 (puede estirarse a 768) |

### Uso recomendado

| Parámetro | Valor |
|-----------|-------|
| steps | 25-35 (óptimo 30) |
| cfg | 6-8 (óptimo 7) |
| sampler | euler_ancestral, euler, dpmpp_2m |
| scheduler | karras, normal |
| Resolution | 512x512, 768x512, 768x768 |

```json
{
  "checkpoint": "architecturerealmix_v11.safetensors",
  "sampler": "euler_ancestral",
  "scheduler": "karras",
  "steps": 30, "cfg": 7, "width": 768, "height": 512, "denoise": 1.0
}
```

Variantes: concepto rápido 512x512/20/euler_a/7/~55s; estándar 768x512/30/euler_a/7/~90s; detalle alto 768x768/40/dpmpp_2m/6/~130s; ControlNet img2img 512x512/25/euler_a/7/denoise 0.6-0.8.

### Prompts efectivos

```
Exterior: "architecturerealmix style, modern architecture, concrete and glass facade,
minimalist design, photorealistic, architectural photography, natural lighting, 8K"

Interior: "architecturerealmix style, modern living room, floor-to-ceiling windows,
warm wood accents, minimalist furniture, natural light, photorealistic"
```

Negative: `blurry, low quality, distorted, deformed, ugly, bad anatomy, extra limbs, watermark, text, signature, grain, noise, overexposed, cartoon, illustration`.

### ControlNet probados (SD 1.5)

| ControlNet | Archivo | Strength | End % | Caso |
|------------|---------|----------|-------|------|
| Canny | `control_v11p_sd15_canny.safetensors` | 0.8-1.0 | 0.8 | Bordes duros, plantas, secciones |
| Depth | `control_v11f1p_sd15_depth_fp16.safetensors` | 0.7-0.9 | 0.8 | Espacialidad, volúmenes |
| Scribble | `control_v11p_sd15_scribble.safetensors` | 0.8-1.0 | 0.85 | Bocetos a mano |
| OpenPose | `control_v11p_sd15_openpose.safetensors` | 0.6-0.8 | 0.7 | Figuras humanas |
| Seg | `control_v11p_sd15_seg.safetensors` | 0.7-0.9 | 0.8 | Layout programático |

### LoRAs recomendadas (SD 1.5)

| LoRA | Descripción | CivitAI |
|------|-------------|---------|
| Architectural Visualization | Estilo render clásica | [#119936](https://civitai.com/models/119936) |
| Modern Architecture | Minimalista, high-tech | Buscar "modern architecture" |
| Brutalist Architecture | Hormigón visto, rough | Buscar "brutalist" |
| Interior Design | Mobiliario, materiales | Buscar "interior design" |

Strength 0.6-0.8 en `LoraLoader` antes de `KSampler`.

### Workflows de referencia

- `proyectos/MVP_04-comfyui-arquitectura/n_01-txt2img/` — txt2img baseline
- `proyectos/MVP_04-comfyui-arquitectura/n_02-img2img/` — img2img + ControlNet
- `proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/` — ControlNet Canny/Depth/Scribble

### Limitaciones

| Limitación | Impacto | Workaround |
|------------|---------|------------|
| SD 1.5 nativo | Res max 768 sin Hires Fix | `ImageScale` + `UltimateSDUpscale` |
| Texturas a distancia | Pierde detalle >10m | Hires Fix 2x + 4x_foolhardy_Remacri |
| Figuras humanas | Genéricas | ControlNet OpenPose + LoRA "people" |
| Texto en renders | No genera texto legible | Post-prod Photoshop/InDesign |
| Licencia OpenRAIL-M | Atribución requerida | Ver ADR-001 |

### Historial

| Fecha | Evento |
|-------|--------|
| 2026-07-17 | Descargado e instalado (primer modelo MVP_04) |
| 2026-07-17 | Primer render: Estadio fútbol 768x512 seed=42 ~114s |
| 2026-07-18 | Baseline A-02 seed=43 + img2img Canny validado (n_02) |
| 2026-07-19 | Scribble + Depth validado (n_03) |

---

## Checkpoint — Juggernaut XL v9

> Fuente: `comfyui/modelos/checkpoint-juggernaut-xl-v9.md` — `categoria: checkpoint, base_model: sdxl, archivo: Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors, tamaño_gb: 7.11, licencia: OpenRAIL++, fuente: https://huggingface.co/RunDiffusion/Juggernaut-XL-v9, estado: descargando` (2026-07-24).

Checkpoint SDXL fotorrealista generalista de RunDiffusion — mejor SDXL todo terreno para arquitectura. Límite superior de calidad en 8GB VRAM.

### Tecnología

- Arquitectura: SDXL (UNet 2.6B + 2 text encoders), FP16, merge iterativo (v8 + RunDiffusion Photo), VAE incluido, resolución nativa 1024x1024, triggers `photorealistic, raw photo, 8k uhd, highly detailed, masterpiece`.

### Configuración óptima RX 570 8GB

```json
{
  "sampler": "dpmpp_2m", "scheduler": "karras",
  "steps": 30, "cfg": 3,
  "resolution": "832x1216 / 1216x832 / 896x896",
  "vae": "incluido", "batch_size": 1
}
```

Flags: `python main.py --directml 0 --force-fp16 --disable-cuda-malloc --lowvram`. Pipeline: txt2img → Hires Fix 1.5x (15 steps, denoise 0.3, 4x_foolhardy_Remacri) → opcional ControlNet Union SDXL.

### Casos de uso

| Uso | Config | Notas |
|-----|--------|-------|
| Render final exterior día | 1216x832, 35 steps, cfg 4 | + Hires Fix 1.5x |
| Render final interior | 832x1216, 30 steps, cfg 3.5 | Iluminación natural crítica |
| Vista aérea / masterplan | 1024x1024, 40 steps, cfg 4 | Detalle urbano |
| Detalle constructivo | 896x896, 30 steps, cfg 4 | Junta, encuentro, materialidad |
| Nocturno | 1216x832, 35 steps, cfg 5 | `night, illuminated windows, floodlights` |

Prompts SDXL: `photorealistic, raw photo, 8k uhd, architecture, modern building, curtain wall, glass facade, concrete structure, sunlight, blue sky, sharp focus, highly detailed, masterpiece, canon r5, 24mm tilt-shift` + variantes interior/nocturno.

### Limitaciones 8GB

| Limitación | Impacto | Mitigación |
|------------|---------|------------|
| Res max ~1216x832 | No 4K nativo | Hires Fix + upscaler |
| 1 solo ControlNet | Canny o Depth, no ambos | ControlNet Union SDXL (requiere 12GB+) |
| Batch size = 1 | No paralelismo | Secuencial ~40-60s/imagen |
| DirectML inestable | Algunos nodos fallan a CPU | Testear; fallback RunPod |

Comparativa vs ArchitectureRealmix: VRAM 2.1 vs 7.11 GB; velocidad 90s vs 45-60s (+Hires); calidad materiales/composición notablemente superior en Juggernaut; uso ideal iteración vs entrega final.

---

## Checkpoint — Z-Image Turbo GGUF Q4

> Fuente: `comfyui/modelos/checkpoint-z-image-turbo-gguf-q4.md` — `categoria: checkpoint, familia: dit, archivo: z-image-turbo-q4_k_s.gguf, tamaño_gb: 4, vram_gb: 5, licencia: Apache-2.0, fuente: https://huggingface.co/city96/Z-Image-Turbo-GGUF, estado: pendiente` (2026-07-24).

Modelo ultra-rápido 8 pasos, arquitectura DiT (Diffusion Transformer), cuantizado GGUF Q4_K_S para 8GB VRAM.

### Ficha técnica

| Campo | Valor |
|-------|-------|
| **Archivo** | `z-image-turbo-q4_k_s.gguf` |
| **Tipo** | Checkpoint DiT (no UNet) |
| **Base** | Z-Image (Z.ai) tipo SD3/Flux |
| **Cuantización** | GGUF Q4_K_S (4-bit K-quant small) |
| **Tamaño** | ~4 GB |
| **VRAM mínima** | ~5 GB |
| **Licencia** | Apache 2.0 |
| **Fuente** | [Hugging Face: city96/Z-Image-Turbo-GGUF](https://huggingface.co/city96/Z-Image-Turbo-GGUF) |
| **Estado** | ⬜ Pendiente |

Tecnología DiT: bloques de atención vs UNet conv, mejor escalabilidad y coherencia global, GGUF carga unificada, Q4_K_S mejor ratio calidad/tamaño, requiere `ComfyUI-GGUF` + `UnetLoaderGGUF`.

### Configuración óptima

```json
{
  "loader": "UnetLoaderGGUF",
  "unet_name": "z-image-turbo-q4_k_s.gguf",
  "clip": "t5xxl_fp16.safetensors (o clip_l + clip_g SDXL)",
  "vae": "ae.safetensors (Z-Image VAE)",
  "sampler": "euler", "scheduler": "simple",
  "steps": 8, "cfg": 1.0, "width": 1024, "height": 1024
}
```

Crítico: `cfg=1.0` (turbo distilado), `steps=8`, scheduler `simple`. Prompts estilo DiT/Flux: descriptivos completos con sujeto+entorno+iluminación+estilo, negative vacío/mínimo. Descarga: `city96/Z-Image-Turbo-GGUF` + auxiliares `t5xxl_fp16.safetensors`, `ae.safetensors`. Comparativa: 8 steps ~18s en RX 570 vs 30 steps ~130s ArchitectureRealmix.

---

## Checkpoint — Flux Schnell GGUF Q4

> Fuente: `comfyui/modelos/checkpoint-flux-schnell-gguf-q4.md` — `categoria: checkpoint, familia: flux, archivo: flux-schnell-q4_k_s.gguf, tamaño_gb: 8, vram_gb: 8, licencia: Apache-2.0, fuente: https://huggingface.co/city96/FLUX.1-schnell-GGUF, estado: pendiente` (2026-07-24).

Modelo más rápido de Flux (Black Forest Labs), cuantizado GGUF Q4_K_S, 4 pasos, 12B params.

### Ficha técnica

| Campo | Valor |
|-------|-------|
| **Archivo** | `flux-schnell-q4_k_s.gguf` |
| **Tipo** | Checkpoint DiT Flux.1 Schnell |
| **Base** | Flux.1 [dev] 12B destilado 4 pasos |
| **Cuantización** | GGUF Q4_K_S |
| **Tamaño** | ~8 GB |
| **VRAM mínima** | 8 GB exacto (límite RX 570) |
| **Licencia** | Apache 2.0 — comercial |
| **Fuente** | [Hugging Face: city96/FLUX.1-schnell-GGUF](https://huggingface.co/city96/FLUX.1-schnell-GGUF) |
| **Estado** | ⬜ Pendiente |

Requisitos: `ComfyUI-GGUF` + `ComfyUI-Flux`, auxiliares `t5xxl_fp16.safetensors` (~9 GB), `clip_l.safetensors` (~230 MB), `ae.safetensors` (~300 MB). VRAM 8GB = límite absoluto, necesita `--lowvram --cpu-vae`, offload T5 a CPU. Config: `UnetLoaderGGUF` + `DualCLIPLoader` + `VAELoader`, `sampler: euler, scheduler: simple, steps: 4, cfg: 1.0, guidance: 3.5`. Uso: iteración máxima velocidad 4 pasos ~8-12s/imagen, concepto volumétrico, prompt adherence superior. No usar para entregas finales ni ControlNet. Comparativa: 4 steps ~10s vs Z-Image 8 steps ~18s.

---

## ControlNet — Canny SD15

> Fuente: `comfyui/modelos/controlnet-canny-sd15.md` — `categoria: controlnet, familia: sd1.5, archivo: control_v11p_sd15_canny.safetensors, tamaño_mb: 689, vram_gb: 1.5, licencia: Apache-2.0, fuente: https://huggingface.co/lllyasviel/ControlNet-v1-1, estado: instalado` (2026-07-24).

Control geométrico principal para arquitectura: líneas duras, plantas, secciones, fachada, estructura. ControlNet v1.1 (Canny), SD 1.5, preprocesador `CannyEdgeDetector` (kornia/OpenCV), 689 MB, ~1.5 GB VRAM adicional.

### Tecnología

ControlNet (copy + zero-conv) congela SD, entrena copia editable. Condicionamiento mapa de bordes Canny threshold low/high inyectado en bloques UNet. Resolución nativa 512x512, strength 0.0-2.0.

### Configuración óptima

Preprocesador `CannyEdgeDetector`: low 50-100 (detalle fino), high 150-200 (muros). Presets: planta/sección limpia low 30/high 100; fachada low 80/high 180; croquis mano low 20/high 80. `ControlNetApplyAdvanced`: strength 0.8-1.0, start 0.0, end 0.7-0.85.

### Casos de uso

| Tipología | Input | Strength | End % | Preprocessor |
|-----------|-------|----------|-------|--------------|
| Planta arquitectónica | DWG export PNG | 1.0 | 0.8 | low=30, high=100 |
| Sección constructiva | Línea técnica | 1.0 | 0.85 | low=20, high=80 |
| Fachada paramétrica | Rhino/GH make2d | 0.9 | 0.8 | low=50, high=150 |
| Croquis mano | Foto móvil / scan | 0.8 | 0.75 | low=20, high=80 |
| Modelo 3D vista oculta | SketchUp/Revit hidden line | 0.9 | 0.8 | low=40, high=120 |
| Referencia fotografía | Foto edificio | 0.7 | 0.7 | low=80, high=180 |

Workflow validado n_03: `LoadImage → CannyEdgeDetector (50/150) → ControlNetLoader → ControlNetApplyAdvanced (0.85/0.8) → KSampler (ArchitectureRealmix) → VAEDecode → SaveImage`. Dual Canny+Depth no cabe en 8GB (2.4GB+), default producción: Canny solo.

---

## ControlNet — Depth SD15 FP16

> Fuente: `comfyui/modelos/controlnet-depth-sd15.md` — `categoria: controlnet, familia: sd1.5, archivo: control_v11f1p_sd15_depth_fp16.safetensors, tamaño_mb: 689, vram_gb: 1.2, licencia: OpenRAIL-M, fuente: https://huggingface.co/lllyasviel/ControlNet-v1-1, estado: instalado` (2026-07-24).

Control espacial/volumétrico: perspectivas, profundidad espacial, relación interior-exterior, topografía. ControlNet v1.1 Depth FP16 (half), 689 MB, ~1.2 GB VRAM.

### Preprocesador

`DepthMapPreprocessor` (MiDaS v2.1 / DPT-Hybrid): `dpt_hybrid` recomendado general (alta calidad), `midas_v21_small` iteración rápida, `DepthAnything V2` mejor detalle (requiere node pack extra).

### Configuración óptima

```json
{
  "controlnet_name": "control_v11f1p_sd15_depth_fp16.safetensors",
  "strength": 0.7, "start_percent": 0.0, "end_percent": 0.85,
  "preprocessor": "DepthMapPreprocessor", "model_type": "dpt_hybrid", "resolution": 512
}
```

Por caso: perspectiva exterior 0.6-0.8/0.8-0.9/dpt_hybrid; interior profunda 0.7-0.85/0.85; sección 0.5-0.7/0.7-0.8; topografía 0.4-0.6/0.7/midas_small; foto→render 0.75-0.9/0.85. Validada dual: Canny 0.75/0.0-0.75 (Canny 50/200) + Depth 0.65/0.0-0.85 (dpt_hybrid).

---

## ControlNet — Union SDXL

> Fuente: `comfyui/modelos/controlnet-union-sdxl.md` — `categoria: controlnet, familia: sdxl, archivo: controlnet-union-sdxl-1.0.safetensors, tamaño_gb: 1.5, vram_gb: 2.5, licencia: Apache-2.0, fuente: https://huggingface.co/xinsir/controlnet-union-sdxl-1.0, estado: pendiente` (2026-07-24).

Un solo ControlNet para todo: Canny + Depth + OpenPose + Scribble + LineArt + Tile + Normal + Seg simultáneamente en SDXL. 1.5 GB, ~2.5 GB VRAM (80% ahorro vs 8 modelos separados). Task embedding vector 8 dims selecciona condición(es). Joint training, SDXL nativo 1024x1024, compatible Juggernaut/RealVis.

### Task embeddings

| Índice | Tarea | Preprocesador típico |
|--------|-------|---------------------|
| 0 | Canny | `CannyEdgePreprocessor` |
| 1 | Depth | `DepthMapPreprocessor` |
| 2 | OpenPose | `OpenPosePreprocessor` (DWpose) |
| 3 | Scribble | `ScribblePreprocessor` (HED/PidiNet) |
| 4 | LineArt | `LineArtPreprocessor` |
| 5 | Tile | `TilePreprocessor` (upscale) |
| 6 | Normal Map | `NormalMapPreprocessor` (BAE) |
| 7 | Segmentation | `SemSegPreprocessor` (SegFormer) |

Ejemplo Canny+Depth: `task_embedding: [1.0, 1.0, 0,0,0,0,0,0], strength 0.8, start 0.0, end 0.8`. VRAM: Juggernaut XL + Union ~9.6 GB (OOM en RX 570 8GB), necesita NVIDIA 12GB+ mínimo. En RX 570 solo SD1.5 + Canny/Depth separados.

---

## Upscaler — 4x_foolhardy_Remacri

> Fuente: `comfyui/modelos/upscaler-4x-foolhardy-remacri.md` — `categoria: upscaler, familia: esrgan, archivo: 4x_foolhardy_Remacri.pth, tamaño_mb: 100, vram_gb: 0.5, licencia: CC-BY-NC, fuente: https://huggingface.co/locon/4x_foolhardy_Remacri, estado: pendiente` (2026-07-24).

ESRGAN 4x (RRDB 23 bloques), dataset mixto fotos+renders+artwork, ~100 MB, ~0.5 GB VRAM. Referencia para renders arquitectónicos: texturas materiales fieles, bordes limpios sin halos, sin alucinaciones geométricas, conservación línea para plantas/secciones.

### Uso ComfyUI

```json
{ "upscale_model_name": "4x_foolhardy_Remacri.pth", "node": "ImageUpscaleWithModel" }
```

Pipeline Hires Fix: `KSampler → VAEDecode → ImageUpscaleWithModel → ImageBlend (denoise 0.1-0.2) → SaveImage`, Hires `upscale_by: 1.5-2.0, denoise: 0.15-0.25`. Workflow entrega: txt2img 768x512/30/cfg7 → Hires Fix 1.5x → post 2x → ~2304x1536 (~3.5 MP) para A3/A2 300dpi. Comparativa upscalers arquitectura: Remacri ★★★★★ (CC-BY-NC, solo interno), ClearReality ★★★★★, UltraSharp ★★★★☆ (MIT, alternativa comercial), RealESRGAN ★★★☆☆ (BSD-3). Licencia CC-BY-NC: no usar en entregas clientes/concursos/portfolio comercial — solo interno/investigación.

---

## Upscaler — 4x-ClearRealityV1

> Fuente: `comfyui/modelos/upscaler-4x-clearreality-v1.md` — `categoria: upscaler, archivo: 4x-ClearRealityV1.pth, tamaño_mb: 100, vram_gb: 0.5, licencia: CC-BY-NC, fuente: https://huggingface.co/philz1337/4x-ClearRealityV1, estado: pendiente` (2026-07-24).

ESRGAN 4x (RRDB 23), dataset fotográfico diverso, 4x, ~100 MB, CC-BY-NC solo no comercial. Upscaler fotorrealista equilibrado: buena alternativa a Remacri para renders con gente, vegetación, contexto urbano.

Comparativa: Arquitectura pura Remacri ★★★★★ vs ClearReality ★★★★☆; Humanos ClearReality ★★★★★ vs Remacri ★★☆☆☆; Vegetación/paisaje ClearReality ★★★★★★; equilibrado no agresivo. Hires Fix `upscale 1.5, denoise 0.35, steps 15-20` o standalone post. Pipeline mixto: txt2img → Hires Fix 1.5x ClearReality (denoise 0.35) → opcional 2º pass Remacri en áreas clave (mask blend). Misma restricción CC-BY-NC que Remacri; para comercial usar `RealESRGAN_x4plus` (BSD-3) o `SwinIR_4x`.

---

## Catálogo de nodos — índice

> Fuente: `comfyui/nodos/00-index.md` — `tipo: indice, seccion: comfyui-nodos` (2026-07-19).

| Nodo | Categoría | Usado en |
|------|-----------|----------|
| ImageScale | image/upscaling | n_03-controlnet |
| Canny (Detect Edges) | image/filters | n_03-controlnet (canny, dual) |
| ControlNetLoader | model/loaders | n_03-controlnet (canny, scribble, dual) |
| ControlNetApplyAdvanced | model/conditioning/controlnet | n_03-controlnet (canny, scribble, dual) |

---

## Nodo — ImageScale

> Fuente: `comfyui/nodos/image-scale.md` — `tipo: nodo, nodo: ImageScale, categoria: image/upscaling` (2026-07-19).

Redimensiona imagen a dimensiones exactas. Nativo ComfyUI.

### Inputs / Output

| Input | Tipo | Rango | Descripción |
|-------|------|-------|-------------|
| `image` | IMAGE | — | Tensor imagen RGB |
| `upscale_method` | COMBO | — | Método interpolación |
| `width` | INT | 0-16384 (def 512) | Ancho destino |
| `height` | INT | 0-16384 (def 512) | Alto destino |
| `crop` | COMBO | disabled/center | disabled deforma, center recorta y escala |

Output: `IMAGE` redimensionada.

### Métodos

| Método | Calidad | Velocidad | Alias PIL | Uso |
|--------|---------|-----------|-----------|-----|
| `nearest-exact` | Mínima | Máxima | NEAREST | Pixel art, debugging |
| `bilinear` | Baja | Alta | BILINEAR | Genérico |
| `area` | Media | Alta | BOX/AREA | Downscaling anti-aliasing |
| `bicubic` | Alta | Media | BICUBIC | Upscale general |
| `lanczos` | Máxima | Baja | LANCZOS | Líneas arquitectónicas |

Recomendación arquitectura: downscale a 512x512 usar `lanczos` (preserva bordes para Canny); upscale usar `bicubic` o `lanczos`. Usos estudio: n_03-controlnet reducir croquis 1600x1315 → 512x512 antes de Canny/Scribble/Dual.

---

## Nodo — Canny

> Fuente: `comfyui/nodos/canny.md` — `tipo: nodo, nodo: Canny, categoria: image/filters` (2026-07-19). Detecta bordes con kornia 0.8.1.

### Inputs / Output

| Input | Tipo | Rango | Descripción |
|-------|------|-------|-------------|
| `image` | IMAGE | — | Imagen RGB |
| `low_threshold` | FLOAT | 0.01-0.99 | Threshold inferior histéresis |
| `high_threshold` | FLOAT | 0.01-0.99 | Threshold superior |

Output: `IMAGE` mapa de bordes blanco/negro. Thresholds normalizados 0-0.99 (convertir: `threshold/255`), usa `kornia.filters.canny` con `rgb_to_grayscale` interno. Bug v0.28.0: falla con ciertos tamaños si no pasa por `rgb_to_grayscale` — parche en `comfy_extras/nodes_canny.py`.

### Thresholds para arquitectura

| Rango | Low | High | Captura |
|-------|-----|------|---------|
| Detalle fino | 0.10-0.30 | 0.30-0.60 | Texturas, vegetación |
| **Estructura** | **0.30-0.50** | **0.60-0.80** | **Líneas arquitectónicas** |
| Solo siluetas | 0.50-0.80 | 0.80-0.99 | Alto contraste |

Pipeline: `LoadImage → ImageScale → Canny → ControlNetApplyAdvanced`. Usos: n_03-controlnet low=0.31/high=0.59.

---

## Nodo — ControlNetLoader

> Fuente: `comfyui/nodos/controlnet-loader.md` — `tipo: nodo, nodo: ControlNetLoader, categoria: model/loaders` (2026-07-19).

Carga modelo ControlNet desde `models/controlnet/`.

### Inputs / Output

| Input | Tipo | Descripción |
|-------|------|-------------|
| `control_net_name` | COMBO | Archivo .safetensors en `models/controlnet/` |

Output: `CONTROL_NET`.

### Modelos disponibles

| Modelo | Tipo | Tamaño | VRAM extra | Uso |
|--------|------|--------|------------|-----|
| `control_v11p_sd15_canny` | Bordes (Canny) | 689 MB | ~1-2 GB | Líneas exactas |
| `control_v11f1p_sd15_depth` | Profundidad (MiDaS) | 689 MB | ~1-2 GB | Profundidad espacial |
| `control_v11p_sd15_mlsd` | Líneas rectas (MLSD) | 689 MB | ~1-2 GB | Fachadas rectas |
| `control_v11p_sd15_lineart` | Arte lineal | 689 MB | ~1-2 GB | Croquis → render |
| `control_v11p_sd15_normal` | Mapa normales | 689 MB | ~1-2 GB | Orientación superficies |
| `control_v11p_sd15_scribble` | Garabatos | 689 MB | ~1-2 GB | Bocetos → render |

Usos: n_03-controlnet canny/scribble/dual (depth fp16).

---

## Nodo — ControlNetApplyAdvanced

> Fuente: `comfyui/nodos/controlnet-apply.md` — `tipo: nodo, nodo: ControlNetApplyAdvanced, categoria: model/conditioning/controlnet` (2026-07-19).

Aplica ControlNet al conditioning con control fino de fuerza y rango de pasos.

### Inputs / Outputs

| Input | Tipo | Descripción |
|-------|------|-------------|
| `positive` | CONDITIONING | Conditioning positivo (CLIPTextEncode) |
| `negative` | CONDITIONING | Conditioning negativo |
| `control_net` | CONTROL_NET | Modelo cargado |
| `image` | IMAGE | Mapa de control (edge/depth) |
| `strength` | FLOAT | Intensidad 0.0-10.0 |
| `start_percent` | FLOAT | Cuándo empieza (0.0-1.0) |
| `end_percent` | FLOAT | Cuándo deja de actuar (0.0-1.0) |

Outputs: `positive`, `negative` con ControlNet.

### Parámetros clave arquitectura

| Parámetro | Recomendación | Explicación |
|-----------|---------------|-------------|
| **strength** | 0.5-0.85 (1.0 = trazado) | Fidelidad al mapa |
| **start_percent** | 0.0 (desde inicio) | Composición guiada |
| **end_percent** | 0.7-0.8 (70% guiado, 30% libre) | Suelta para texturas |

Pipeline: `CLIPTextEncode → ControlNetApplyAdvanced → KSampler` (ControlNetLoader + Canny como inputs). Usos: canny A-01 strength 0.7/start 0.0/end 0.7; dual-canny 0.3/0.0/1.0; dual-depth 1.0/0.0/1.0.

---

## Nodos nativos pendientes

Nodos built-in con ficha completa pendiente — se documentan paso a paso. Referencia general: https://docs.comfy.org. Migrado de stubs `comfyui/*.md`.

| Nodo | Uso |
|---|---|
| CheckpointLoaderSimple | Carga checkpoints desde `models/checkpoints/` |
| CLIPTextEncode | Conditioning positivo/negativo |
| EmptyLatentImage | Latent vacío para txt2img |
| KSampler | Muestreo (steps/cfg/sampler/scheduler) |
| VAEDecode | Latent a píxeles |
| SaveImage | Guarda en `output/` |

---

## Flujos y playbooks

- [[wiki/glosario/interno/pbooks/pbk-comfyui]] — Control Geométrico (bordes, profundidad, líneas)
- [[wiki/glosario/interno/pbooks/00-index|pbooks/]] — `pbk-comfyui`, `pbk-troubleshooting-reconexion`
- Proyecto vinculado: [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04|MVP 04 — ComfyUI Arquitectura]]

## Convención de nombrado y frontmatter

```
<tipo>-<nombre-modelo>-<version>.md  # legacy: checkpoint-architecturerealmix-v11.md etc.
```

Frontmatter obligatorio por modelo (legacy):

```yaml
tipo: modelo
categoria: checkpoint|controlnet|upscaler|lora|vae|clip|text_encoder|unet
base_model: sd15|sdxl|flux|zimage|dit|otro
archivo: nombre-exacto.safetensors|.gguf|.pth
tamaño_gb: 2.1
licencia: OpenRAIL-M|Apache-2.0|CC-BY-NC|etc
fuente: huggingface|civitai|github|etc
url: https://...
estado: instalado|descargando|pendiente|archivado
hardware_min_vram_gb: 4
tags: [arquitectura, interiores, fotorrealismo, rapido, etc]
fecha_instalacion: YYYY-MM-DD
ultima_actualizacion: YYYY-MM-DD
```

---

## Conceptos relacionados

- [[wiki/glosario/conceptos/bim-metodologia]]
- [[wiki/glosario/conceptos/cerebro-digital-karpathy]]

## Referencias

- [ComfyUI Docs — ImageScale](https://docs.comfy.org/built-in-nodes/ImageScale) (verificado 2026-07-19 — migrado de `image-scale.md`)
- [ComfyUI Docs — ControlNetLoader](https://docs.comfy.org/built-in-nodes/ControlNetLoader) (migrado de `controlnet-loader.md`)
- [ComfyUI Docs — ControlNetApplyAdvanced](https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced) (migrado de `controlnet-apply.md`)
- [OpenCV — Canny Edge Detection](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html) (migrado de `canny.md`)
- [kornia — Canny](https://kornia.readthedocs.io/en/latest/filters.html#kornia.filters.canny)
- [ControlNet Paper](https://arxiv.org/abs/2302.05543)
- [MiDaS Paper](https://arxiv.org/abs/1907.01341) — Depth
- [DPT Paper](https://arxiv.org/abs/2103.13413) — Depth
- [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2)
- [Hugging Face Architecture Models](https://huggingface.co/models?search=architecture) (migrado de `modelos/00-index.md`)
- [CivitAI Architecture Tag](https://civitai.com/tag/architecture)
- [CivitAI — ArchitectureRealmix](https://civitai.com/models/35080/architecturerealmix) / [#84958](https://civitai.com/models/84958/architecturerealmix)
- [Hugging Face: RunDiffusion/Juggernaut-XL-v9](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9)
- [Hugging Face: city96/Z-Image-Turbo-GGUF](https://huggingface.co/city96/Z-Image-Turbo-GGUF) / [city96/FLUX.1-schnell-GGUF](https://huggingface.co/city96/FLUX.1-schnell-GGUF)
- [Hugging Face: xinsir/controlnet-union-sdxl-1.0](https://huggingface.co/xinsir/controlnet-union-sdxl-1.0)
- [Hugging Face: locon/4x_foolhardy_Remacri](https://huggingface.co/locon/4x_foolhardy_Remacri) / [philz1337/4x-ClearRealityV1](https://huggingface.co/philz1337/4x-ClearRealityV1)
- [ESRGAN Paper](https://arxiv.org/abs/1809.00219)
- [city96 ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)
- Verificar con webfetch antes de publicar — patrón docs.comfy.org es `/built-in-nodes/<PascalCase>` (no `/node-reference/<kebab-case>`).
