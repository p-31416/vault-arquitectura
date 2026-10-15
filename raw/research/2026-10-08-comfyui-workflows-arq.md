---
tipo: research
fecha: 2026-10-08
autor: sherlock
idioma: es
tags: [comfyui, arquitectura, workflows, txt2img, img2img, controlnet, flux, sd3.5, video, ltx-2, wan2.2, hunyuanvideo, 3d, tripo3d, ip-adapter, lora, civitai, runpod, mcp, rhino, sketchup, blender]
origen: peticion SOL 2026-10-08
vault_destinos: [wiki/glosario/interno/pbooks/pbk-comfyui, wiki/glosario/software/comfyui, proyectos/MVP_04-comfyui-arquitectura]
---

# ComfyUI para arquitectura: workflows, modelos y pipelines (octubre 2026)

*Fecha: 2026-10-08 | Fuentes únicas: 35+ | Confianza: Media-Alta*

> Estado del arte completo de ComfyUI aplicado a estudio de arquitectura. Cubre moodboard, txt2img (SD1.5/SDXL/FLUX.1/FLUX.2/SD3.5/Z-Image/Hunyuan), img2img+IP-Adapter, ControlNet 2026 (incluye FLUX.1-Canny/Depth y Union Pro), croquis→render, 3D model→render (CRÍTICO: Rhino/Blender/SketchUp → ComfyUI; estado del MCP Rhino), video (LTX-2.3, Wan2.2, HunyuanVideo 1.5, Mochi 1, CogVideoX, SVD), pack de nodos de facto y licencias para entrega comercial. Listo para que `@vaultworm-arq` integre en [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] sin duplicar §0.

## Resumen ejecutivo

1. **Texto a imagen — recomendación 2026**: para estudio comercial con hardware limitado, **FLUX.1 [schnell] GGUF Q4_K_S** en RX 570 8GB (8 GB VRAM, 4 steps) o **FLUX.1 [dev] GGUF Q4 + FP8 T5** en 12 GB; para entrega final en RunPod, **FLUX.2 [klein] 4B (Apache 2.0, comercial)** o **FLUX.2 [dev] FP8**; SD3.5 Large y SDXL siguen siendo los modelos LoRA-friendly y compatibles con el ecosistema Civitai largo.
2. **3D model → render (caso Rhino)**: la ruta más confiable NO depende del MCP. Es **render passes de Rhino (depth + lineart + shaded) → ComfyUI img2img + ControlNet** (depth 0.85 + lineart 0.7). Para scene-to-3D, el camino es **Tripo3D / TripoSR (P5ina) → ComfyUI-3D-Pack (MrForExample) → render multi-vista**; el **MCP de Rhino** (ruiguan, RhinoAiMCP, bimolicense) controla geometría viva, no exporta a ComfyUI directamente — son dominios distintos.
3. **Video arquitectónico (recorridos, flythrough)**: para 2026 la combinación ganadora es **render estático del estudio → LTX-2.3 i2v** (RunPod, 24 GB) con audio sincronizado y control LoRA cámara (`ltx-2-19b-lora-camera-control-*`); fallback local con **Wan2.2 TI2V-5B (8 GB) o HunyuanVideo 1.5 8.3B (24 GB)**; SVD 2.5 y AnimateDiff ya son legacy para producción.
4. **LoRAs arquitectura Civitai top 2026**: **JJ's Brutalist Architecture (SDXL)**, **Brutalist Luxury Homes (SDXL)**, **Brutalist Home Interior (Illustrious/Pony/SDXL)** — el patrón es que **el modelo base define el ecosistema, no el tema**: SDXL/Illustrious/Pony para Civitai-massivo, FLUX.1 dev para calidad nativa, **JJ's es CreativeML Open RAIL++-M (comercial ok con atribución)**.
5. **Gaps reales**: (a) MCP Rhino→ComfyUI no existe como puente nativo — hay que usar render passes o `comfyui-3d-viewport-pro`; (b) Croquis suelto a render sigue dependiendo de ControlNet + modelo base con buena distribución de masa (ArchitectureRealmix SD1.5 sigue vigente); (c) Licencias: **Schnell (Apache 2.0), Dev (non-commercial), FLUX.2 [klein] 4B (Apache 2.0)** — para cliente elegir Apache 2.0 + OpenRAIL++-M siempre.

## 0. Estado del vault — qué ya cubre [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] (NO duplicar)

`pbk-comfyui.md` (219 líneas, 2026-09-09) ya cubre extensivamente y NO se duplica acá:

| Tema cubierto en pbk | Sección pbk | Acción en este informe |
|---|---|---|
| Setup local RX 570 8GB DirectML (launch args, patch VRAM) | § Base local | NO tocar — sigue vigente |
| Catálogo de flujos A→F (txt2img, img2img, ControlNet, Hires, video) | § Catálogo + Mapa de decisión | NO tocar — sigue vigente |
| Pipeline ControlNet diagrama + variantes Canny/Depth/Scribble/Lineart/MLSD/Normal/Seg/OpenPose/Union SDXL | § ControlNet | §5 de este informe SOLO agrega FLUX.1-Canny/Depth/Union Pro y ControlNet-XS/SparseCtrl |
| Doble ControlNet SD1.5 (n_03 validado) | § Doble ControlNet + n_03 | NO tocar |
| Hires fix + upscalers (Remacri, ClearReality, RealESRGAN) | § Upscale | NO tocar |
| LTX-2 base + LoRAs control + RunPod template | § Video + § RunPod | §8 de este informe ACTUALIZA con LTX-2.3, Wan2.2, HunyuanVideo 1.5, Mochi 1, SVD 2.5 |
| Prompt-packs arquitectura (exterior, interior, nocturno) | § Prompt-packs | NO tocar (siguen vigentes); §3 de este informe agrega el patrón de Civitai-LoRAs |
| DoD y archivo en vault (`n_XX-{L}-{NN}.png`) | § DoD | NO tocar — se referencia |
| Troubleshooting exprés (OOM, canny no guía, modelo no aparece) | § Troubleshooting | NO tocar |

**Lo que este informe APORTA y pbk NO cubre (o quedó desactualizado)**:

- §1: Workflows tipo moodboard (consistencia visual de lote 8-20 imágenes) con IP-Adapter, regional prompting (Set Area, Attention Couple, Anima-Regional)
- §2: Estado 2026 de modelos base incluyendo **FLUX.2 [dev] 32B**, **FLUX.2 [klein] 4B/9B (Apache 2.0)**, **SD 3.5 Large/Turbo/Medium**, **Z-Image / Z-Image-Turbo**, **HunyuanImage 3.0**, **Stable Diffusion 3.5** ecosystem
- §3: Tabla comparativa Civitai-LoRAs arquitectura 2026 (FLUX.1, SDXL, Pony, Illustrious) + análisis de cuándo usar modelo base distinto vs LoRA
- §4: IP-Adapter en FLUX (XLabs-AI, Shakker-Labs) y PuLID-FLUX para consistencia de personaje + Krea 2 moodboard nativo
- §5: FLUX.1 Tools Canny/Depth (modelos completos, no adapters), Union Pro 2.0 (InstantX/Shakker), ControlNet-XS, SparseCtrl
- §6: Croquis→render en FLUX.1 + nuevos preprocesadores (Marigold V2 desde single image)
- §7: 3D model→render con **ComfyUI-3D-Pack (MrForExample)** (Hunyuan3D-2, Unique3D, TRELLIS, Zero123++, InstantMesh, TripoSR), **Tripo3D partner node nativo**, **3D-Viewport-Pro**, render passes desde Rhino/Blender/SketchUp, **estado real del MCP Rhino→ComfyUI** (3 conectores revisados, ninguno cierra el gap ComfyUI-render directamente), **render-rescue workflow** (img2img denoise 0.40-0.55)
- §8: Video arquitectónico — comparativa completa 2026 (LTX-2.3, Wan2.2, HunyuanVideo 1.5, Mochi 1, CogVideoX, SVD 2.5, AnimateDiff), duración, VRAM, audio, GGUF quantized, **5B TI2V vs 14B MoE**
- §9: Pack de nodos de facto 2026 (comfyui-manager built-in core, rgthree, KJNodes, Impact Pack, Mixlab, comfyui-3d-pack, Florence-2 + SAM 2, Advanced-ControlNet, comfyui-Krea2Moodboard)
- §10: Licencias 2026 (Apache 2.0, OpenRAIL++-M, FLUX Non-Commercial, Community License con revenue threshold $1M, CreativeML)

## 1. Workflows tipo moodboard (consistencia de lote 8-20 imágenes)

### 1.1 Patrón: lote de 8-20 imágenes con atmósfera/estilo coherente para cliente

El problema clásico: generar `k` imágenes con la **misma atmósfera, lenguaje de materiales y paleta**, sin que se "derramen" los detalles entre escenas. Tres rutas 2026:

**Ruta A — IP-Adapter con style reference + base coherente**: cargar 1 imagen de referencia (rango de estilo), `IPAdapterUnifiedLoader` preset `STANDARD` o `PLUS FACE` (este último solo para rostros), `Apply IPAdapter` con `weight_style 0.5-0.6` y `weight_composition 0.4-0.5` (no usar `IPAdapterStyleCompositionBatch` de `ComfyUI_IPAdapter_plus` para lote de escenas diferentes; ese nodo es para series de variaciones sobre la misma imagen). Para FLUX, `ip-adapter-faceid-flux.bin` o mejor **`PuLID-Flux`** (`ApplyPulidFlux`, weight 0.78 con start 0.05 / end 0.65) si la consistencia es de personaje.

**Ruta B — Regional Prompting (multi-subject / multi-area)**: si cada imagen tiene zonas diferenciadas (cielo, fachada, primer plano) que NO deben mezclarse, usar:

- `ConditioningSetArea + ConditioningCombine` (nativo ComfyUI) para splits rectangulares (atributo bleed se filtra aún, ver §1.2)
- `Cutoff BasePrompt + Cutoff Set Region + Cutoff Regions To Conditioning` para bindear atributos (color cabello, ropa) sin coordenadas
- Impact Pack `RegionalPrompt + RegionalSampler` para máscaras complejas con sampling por paso
- `ComfyUI-Lora-Pipeline` (andreszs) — multi-área con `Conditioning Pipeline (Set Area) + (Combine) + OpenPose Studio`, para multi-LoRA por área
- `MultiMaskCouple` (tumbowungus) — atención couple multi-máscara, "el clásico multi-character fix"
- `Anima-Regional` (An1X3R) — character-level routing para el modelo Anima (atención routing, no geométrico)

Para moodboard de arquitectura, el patrón es **regional por planta/zona** (no por sujeto), típicamente `Set Area` con dos zonas (cielo/fachada y planta baja/peatonal), `Cutoff` para evitar que la materialidad del suelo se filtre a la fachada. Común: `global_strength 0.3-0.5` para mantener atmósfera sin opacar la zona.

**Ruta C — Krea 2 Moodboard nativo (sin custom nodes)**: `ComfyUI-Krea2Moodboard` (RedNodeAI) es la opción 2026 más integrada para moodboard "krea.ai-style" sobre el modelo **Krea 2** (single-stream DiT, Mistral-3 24B VLM). Nodos `Krea 2 Moodboard` (one-node vibe transfer: prompt + reference images, reemplaza `CLIPTextEncode`), `Krea 2 Moodboard Encode (packed)` (multi-ref packed en una vision span, grid-safe), `Krea 2 Moodboard + Identity Fusion` (style refs + identity edit con source latents in-context). Configuración: strength 1.0 = raw detail, lower = purer extract. Modos: `style` (palette/lighting/texture sobreviven), `subject` (subject/composition sobrevive, prompt controla look). Recomendación: 8 steps CFG 1, `ModelSamplingAuraFlow shift 1.15`. Generar ≤2MP. **Licencia Krea 2**: black-forest-labs, requiere revisar antes de comercial; para moodboard de cliente se sugiere usar **FLUX.2 [klein] 4B (Apache 2.0)** con IP-Adapter como fallback libre.

### 1.2 Cuándo NO usar regional prompting (gap explícito)

Regional prompting **no resuelve**:

- **Attribute bleed en CLIP**: en "cabello azul, ojos amarillos" CLIP codifica la frase completa, azul puede afectar ojos. `ConditioningSetArea` limita el área pero el embedding es global. Para eso: `Cutoff` (atributo binding) o **prompt-engineering estricto con orden de tokens**.
- **Identity consistente entre frames**: regional no lockea cara. Usar `FaceID / ReActor / LoRA` aparte.
- **Poses exactas**: regional no controla pose. Usar `ControlNet OpenPose` y alinear manualmente con las áreas.

### 1.3 Reglas del lote de moodboard

- **Seed fijo** mientras se itera prompt/LoRA; cambiar seed al final.
- **Checkpoint único + mismo sampler + mismos steps/cfg** en todo el lote (cambiar modelo entre frames = inconsistencia de materiales).
- **ImageGrid / ImageBatch** para presentación final 4×2 o 5×2, con etiqueta visible (no superponer watermark de IA en presentación a cliente).
- Archivo: cada imagen `n_XX-{B}-{NN}.png` (B = variación de prompt; ver `reglas-workflows-comfy.md` § nomenclatura).

## 2. txt2img — estado del arte de modelos base 2026

### 2.1 Mapa de modelos para arquitectura (oct 2026)

| Modelo                   | Parámetros          | VRAM mínimo              | Licencia                                          | Caso de uso arquitectura                                               | Notas                                                                                                                |
| ------------------------ | ------------------- | ------------------------ | ------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **FLUX.2 [klein] 4B**    | 4B                  | ~8-9 GB                  | **Apache 2.0**                                    | Iteración rápida, batch moodboard, **uso comercial sin restricciones** | Top ranking open-source en Artificial Analysis (Elo 1,161); 8 NFE; sub-segundo en enterprise GPU; ~13 GB en consumer |
| **FLUX.2 [klein] 9B**    | 9B                  | ~14 GB                   | FLUX Non-Commercial                               | Calidad alta para presentaciones internas; no comercial                | Mejor calidad/latencia que 4B; KV cache para multi-ref                                                               |
| **FLUX.2 [dev]**         | 32B                 | 24 GB (FP8)              | FLUX Non-Commercial                               | Entrega final hero shots, con derecho a licencia comercial             | Requiere weight streaming ComfyUI + RAM offload en consumer. NVIDIA+ComfyUI tienen FP8 optimizado (-40% VRAM)        |
| **FLUX.1 [schnell]**     | 12B                 | 6-8 GB (Q4 GGUF)         | **Apache 2.0**                                    | Iteración ultra-rápida, propuestas, **uso comercial**                  | 4 steps, CFG 1, no negative prompt; GGUF Q4_K_S (6.8 GB) en RX 570 8 GB; 4 s en RTX 4070                             |
| **FLUX.1 [dev]**         | 12B                 | 10 GB (Q4 GGUF + fp8 T5) | FLUX Non-Commercial                               | Calidad para entrega, con licencia                                     | 28 steps, CFG 3.5, negative prompt. GGUF Q4_K_S 6.8 GB en RX 570 8 GB (con T5 offloaded)                             |
| **FLUX.1 Kontext [dev]** | 12B                 | 12 GB (Q4 GGUF)          | FLUX Non-Commercial                               | Edicion de render existente: "cambiar materialidad", "cambiar cielo"   | Multi-turn image editing con preservacion de identidad; necesita patch `pulidflux.py` para PuLID combo               |
| **SD 3.5 Large**         | 8.1B                | 10-12 GB                 | Stability AI Community License (<$1M rev = libre) | Calidad de tipografía dentro de imagen (rótulos, planos)               | MMDiT-X, 28 steps, CFG 4.5; QK-Norm; multi-resolución; LoRA compatible                                               |
| **SD 3.5 Large Turbo**   | 8.1B destilado      | 10 GB                    | mismo                                             | Iteración rápida con buena adherence                                   | 4 steps, CFG 1                                                                                                       |
| **SD 3.5 Medium**        | 2.5B                | 8-10 GB                  | mismo                                             | Default consumer hardware, LoRA training rápido                        | Triple text encoder (CLIP-L + OpenCLIP-G + T5-XXL); calidad media; el más deployed                                   |
| **SDXL 1.0**             | 3.5B                | 8 GB                     | OpenRAIL++-M                                      | Ecosistema Civitai LoRAs, comercial con atribucion                     | Sigue siendo el rey de LoRAs arquitectura (Civitai); Juggernaut XL para entrega                                      |
| **SD 1.5**               | 0.86B               | 4-6 GB                   | OpenRAIL++-M                                      | ArchitectureRealmix (estudio) base, máxima compatibilidad ControlNet   | Stable desde 2022; sigue vigente en RX 570 8GB                                                                       |
| **Z-Image**              | 6B                  | <16 GB                   | Apache 2.0 (verificar weights)                    | Bilingüe ES/EN, fotorrealismo, tipografía fuerte                       | Single-stream DiT (S3-DiT); 8 NFE Turbo; rank 8 en Artificial Analysis (Elo 1,161)                                   |
| **Z-Image-Turbo**        | 6B destilado        | <16 GB                   | Apache 2.0                                        | Iteración rápida, calidad a 8 NFE                                      | Sub-segundo en H800; quality-to-speed leader                                                                         |
| **HunyuanImage 3.0**     | 80B                 | >80 GB                   | Tencent                                           | Frontier, multi-GPU                                                    | No práctico local                                                                                                    |
| **Sana 1.5 4.8B**        | 4.8B                | ~16 GB                   | Apache 2.0 (code), NVIDIA Open Model              | 4K inference, alta resolución                                          | DC-AE latent, linear attention, MMDiT; tiling + quantizacion 4K en 8 GB                                              |
| **AuraFlow 0.3**         | 6.8B                | ~32 GB                   | Apache 2.0                                        | Adherencia literal al prompt                                           | UMT5 encoder; reportado "clip-art look" pero fuerte en composición compleja                                          |
| **PixArt-Σ**             | 0.6B                | ~6-21 GB (depende T5)    | Apache 2.0                                        | Bajo VRAM, 512px-2K                                                    | DiT compacto; bajo costo de entrenamiento; estética débil                                                            |
| **Kolors**               | 2.6B                | ~17 GB                   | Kuaishou (commercial con registro)                | Bilingüe ES/EN, retratos                                               | UNnet (legacy); IP-Adapter y ControlNet nativos                                                                      |
| **Chroma**               | (DiT custom)        | —                        | Apache 2.0                                        | LoRA training experimental                                             | Approximator layer; usado con `ostris/ai-toolkit`                                                                    |
| **Krea 2**               | (Single-Stream DiT) | ~16 GB                   | (verificar)                                       | Moodboard nativo, vibe transfer                                        | Qwen3-VL-4B; ver §1 Ruta C                                                                                           |

**Recomendación para el estudio (oct 2026)**:

- **Concepto/mood local RX 570 8GB DirectML**: **FLUX.1 [schnell] GGUF Q4_K_S** (`flux1-schnell-Q4_K_S.gguf`, 6.8 GB en `models/unet/`) + `t5xxl_fp8_e4m3fn.safetensors` + `clip_l.safetensors` + `ae.safetensors`. 4 steps, euler, CFG 1. 3 s/imagen en RTX 4070, ~3 min en RX 570.
- **Entrega comercial A3/A2 con RunPod RTX 3090 24 GB**: **FLUX.2 [klein] 4B** (Apache 2.0) o **FLUX.1 [dev] fp8** (con licencia comercial si aplica) + Hires 1.5x + upscaler comercial. Tiempo ~14 s/imagen en RTX 4090.
- **Tipografía y rótulos dentro de render** (plantas, etiquetas): **SD 3.5 Large** (MMDiT-X, mejor tipografía que FLUX en benchmarks 2026). Triple text encoder (CLIP-L + OpenCLIP-G + T5-XXL).
- **Compatibilidad máxima LoRA Civitai** (arquitectura específicamente): **SDXL 1.0** (Juggernaut XL / RealitiesXL) o **SD 1.5** (ArchitectureRealmix v1.1) — la mayoría de LoRAs arq Civitai son SDXL o SD1.5.

### 2.2 Modelos fine-tune específicos de arquitectura (Civitai, 2026)

- **ArchitectureRealmix v1.1** (SD 1.5): vigente y citado por el estudio; ver `pbk-comfyui.md` § txt2img.
- **Juggernaut XL** (SDXL): standard de facto para entrega.
- **RealitiesXL** (SDXL): alternativa fotorrealista.
- **Z-Image** fine-tunes arquitectura: en Civitai tag `architecture` + `flux.1` filter 2026 — el ecosistema Civitai se está moviendo a Z-Image y FLUX.2 por licencias limpias.

## 3. Modelos optimizados: exterior vs interior (tabla comparativa)

### 3.1 ¿Hay modelos distintos para exterior e interior?

**No, no hay modelos base distintos** — el modelo base (SDXL, FLUX, SD 3.5) es el mismo. La diferencia la hacen:

1. **LoRAs especializados** (Civitai, 2026)
2. **Embeddings / textual inversion** (más viejos, menos populares)
3. **Prompt engineering + ControlNet depth** (separar fachada de plano)
4. **IP-Adapter con style reference** (foto existente de interior/exterior)

### 3.2 Top LoRAs Civitai arquitectura 2026 (recomendación)

| LoRA | Modelo base | Trigger | Strength sugerida | Licencia | Caso |
|---|---|---|---|---|---|
| **JJ's Brutalist Architecture** | SDXL 1.0 | `Brutalist Architecture` | 0.7-0.9 (compound con face LoRA) | **CreativeML Open RAIL++-M (comercial con atribución)** | Brutalismo, hormigón visto, formas masivas |
| **Brutalist Home Interior Living Room** (Illustrious) | Illustrious | `BruHoInLivRom` | 1.0-1.5 | ver Civitai | Interior brutalista salón |
| **Brutalist Home Interior Kitchen** (Pony) | Pony Diffusion | `BruHoInKit` | 1.0-1.5 | ver Civitai | Cocina brutalista |
| **Brutalist Luxury Homes** (SDXL) | SDXL 1.0 + Hassaku XL | `BruLuxHom` | 1.35-1.5 | ver Civitai | Brutalismo de alta gama |
| **Brutalist architecture** (FLUX.1) | FLUX.1 D | (sin trigger) | 0.4-0.5 | ver Civitai | Brutalismo en FLUX |
| **Brutalist interior design** (FLUX.1) | FLUX.1 D | (sin trigger) | 0.4-0.5 | ver Civitai | Interior brutalista en FLUX |

**Reglas de stack de LoRAs (de `aiofm.info` "Building Production Flux Workflows")**:

- **Máximo práctico 3 LoRAs en FLUX sin identity collapse** (face LoRA 0.8-1.0, style LoRA 0.4-0.6, concept LoRA 0.3-0.5). Más de 4 y la cara se pierde, el estilo se vuelve mush.
- **Orden de carga**: face primero, style después, concept al final.
- **rgthree Power LoRA Loader** (single node, toggle on/off, weights centralizados) — instalable via ComfyUI-Manager.
- **Mismo autor o training approach** para multi-LoRAs (menos bleeding).

### 3.3 Cuándo NO usar LoRA y solo prompt + modelo base

- Primer concepto/mood: el modelo base (FLUX.2 klein 4B, Juggernaut XL) ya da buena arquitectura fotorrealista con solo `architectural photography, concrete and glass, 8k uhd, photorealistic, raw photo, masterpiece, canon r5, 24mm tilt-shift`. LoRA entra cuando se necesita un lenguaje específico (brutalismo local, patrimonio porteño, etc.).

## 4. img2img + IP-Adapter

### 4.1 Pipeline base img2img

`LoadImage → VAEEncode → KSampler (denoise < 1) → VAEDecode`. **Denoise** es el mando:

- `0.3` = retoque leve (cambiar luz, color, sin tocar estructura)
- `0.4-0.55` = **render-rescue** (el "sweet spot" del flujo Rhino→render: añadir luz, materialidad, atmósfera sin inventar geometría; ver §7.5)
- `0.6-0.8` = re-estilo manteniendo composición
- `1.0` = txt2img (ignora input, re-genera desde ruido)

Caso estudio (pbk ya cubierto): foto de maqueta o render viejo denoise 0.6 + prompt de materialidad nueva. **No documentado en pbk**: el patrón **denoise 0.40-0.55 + ControlNet Depth 0.85** sobre vista de Rhino es la receta ArchiGen 2026 "render-rescue" (ver §7.5).

### 4.2 IP-Adapter 2026 (consistencia visual)

**SDXL (`ComfyUI_IPAdapter_plus` de cubiq)**:

- `IPAdapterUnifiedLoader` preset: `STANDARD (medium strength)`, `PLUS (high strength)`, `PLUS FACE (portraits)`, `FACEID` (face lock con InsightFace, research-only)
- Nodo graph: `Load Checkpoint → IPAdapter Unified Loader → IPAdapter Advanced (image, weight 0.8, weight_type adjust for prompt adherence) → KSampler`
- **Weights típicos**: face lock 0.9-1.0; style-only nudge 0.3-0.4; mixto 0.6
- **Stacking**: face IPAdapter 0.7 + style IPAdapter 0.4 = combinación común. Total bajo 1.3 para no sobre-constreñir.
- `weight_type`: `linear` (constante), `ease out` (fuerte al inicio, fade al final), `ease in` (fuerte al final, débil al inicio)
- `start_at` / `end_at` (0.0-1.0): restringir IP-Adapter a una porción de denoising. `0.0, 0.8` = aplicar temprano, liberar al final. Útil cuando cara lockea pero manos se rompen.

**FLUX (`Shakker-Labs/ComfyUI-IPAdapter-Flux` y `XLabs-AI/x-flux-comfyui`)**:

- `LoadFluxIPAdapter` carga weights + CLIP Vision + Image Projection
- `ApplyFluxIPAdapter` (uniform strength) y `ApplyAdvancedFluxIPAdapter` (per-layer strength, smoothing linear/first half/second half/sigmoid)
- Modelos: `ip-adapter-faceid-flux.bin` o mejor **PuLID-Flux** para identidad de cara (más fuerte, no se trata como style)
- **NOTA 2026**: `ComfyUI_IPAdapter_plus` y `PuLID_ComfyUI` (cubiq) están en **maintenance-only** desde 2025-04-14; un ComfyUI update puede romperlos. Pin versión o migrar a native FLUX.2 klein image-edit (sin custom nodes).

**PuLID-FLUX** (`city96/ComfyUI-PuLID-Flux` o `ComfyUI-PuLID-Flux`):

- `PulidFluxModelLoader` (model: `pulid_flux_v0.9.1.safetensors`) + `PulidFluxInsightFaceLoader` (CUDA) + `PulidFluxEvaClipLoader`
- `ApplyPulidFlux` con `weight 0.7-0.8`, `start_at 0.0-0.05`, `end_at 0.65-0.7` (libera los últimos pasos para textura natural)
- Funciona bien con **Flux Kontext** (multi-turn editing) pero requiere patch `pulidflux.py` para soporte de `timestep_zero_index` y `generation-token-only injection mode`.

**FLUX.1 Kontext** (alternativa sin custom nodes para edición):

- Image editing natural: prompt describe el cambio, la imagen input es el contexto
- **No requiere IP-Adapter para character reference** — el modelo lo hace nativamente
- Licencia: FLUX Non-Commercial (la `dev`); `Kontext` también non-commercial; verificar licencia comercial

**FLUX.1 Redux** (variación de imagen, sin prompt):

- Adapter para FLUX.1 dev/schnell, genera variaciones
- FLUX.1 Redux [pro] vía API (BFL)

**Recraft / Seedream 5.0-lite / NanoBanana Pro / Grok Image Edit** (cloud APIs, fuera de ComfyUI local):

- Style transfer 2026: Recraft es standout, acepta 1-5 style references
- Image-edit models (Nano Banana Pro, Grok Image Edit, Seedream 5.0-lite): restyle de imagen existente manteniendo likeness
- Para LoRAs personalizados: entrenar image-edit LoRAs sobre Qwen Image Edit o Flux Klein 9B (Fal.ai endpoints para Z-Image, Flux Klein, Qwen Image Edit)

## 5. ControlNet 2026 — qué hay nuevo y para FLUX

### 5.1 Pipeline base (ya en pbk, no modificar)

`LoadImage → ImageScale 512x512 → preprocesador → ControlNetApplyAdvanced → KSampler`. Strength 0.7-0.85, end_percent 0.8 típico. **R1: siempre ImageScale 512x512** antes del sampler (ver `reglas-workflows-comfy.md`).

### 5.2 FLUX.1 ControlNet 2026 (la pieza nueva más importante)

**Diferencia conceptual clave (BFL official)**: los **FLUX.1 Tools Canny/Depth NO son adapters**, son modelos completos de 12B con la condicionante Canny/Depth entrenada en los pesos. No hay dial de "strength" — el control es por **número de steps** que corre el modelo de control antes de cambiar al base FLUX dev.

- **Pipeline típico** (RunPod, ≥24 GB):
  1. Cargar `flux1-dev-fp8.safetensors` (base, ~11 GB) + `flux1DepthDevFp8` o `flux1CannyDevFp8` (control, ~11 GB) en `models/diffusion_models/`
  2. Cargar `clip_l.safetensors` + `t5xxl_fp8_e4m3fn_scaled.safetensors` en `models/clip/`
  3. Cargar `ae.safetensors` en `models/vae/`
  4. KSampler 20 steps totales; un nodo intermedio **intercambia del modelo de control al base** después de N steps (slider: 3 = sutil, 10 = fuerte, 20 = máximo control)

- **Canny vs Depth** (cuándo cada uno):
  - **Canny** preserva bordes exactos: siluetas de producto, contornos precisos, pose exacta. Más rígido.
  - **Depth** preserva volumen 3D: turn un retrato en robot biomecánico funciona mejor con depth. Más libertad.
  - Slider 3 = invención, slider 7 = balance, slider 20 = input clonado.

- **LoRA adapter versions** (más livianos): `flux1-depth-dev-lora.safetensors` y `flux1-canny-dev-lora.safetensors` (FLUX.1 dev base + LoRA control). Menor tamaño de archivo, para hardware limitado.

- **Verificado 200**: [docs.comfy.org/tutorials/flux/flux-1-controlnet](https://docs.comfy.org/tutorials/flux/flux-1-controlnet) (consultado 2026-10-08).

### 5.3 FLUX.1 Union ControlNet Pro 2.0 (InstantX / Shakker Labs)

- **Pro 2.0** (`FLUX.1-dev-ControlNet-Union-Pro-2.0.safetensors`, 2024-08-26 release) soporta multi-control: Canny (mode 0), Tile (1), Depth (2), Blur (3), Pose (4), Gray (5, calidad baja), Low Quality (6). Mapeo legacy workaround todavía activo en nodos no actualizados.
- **Workaround importante**: hasta que ComfyUI actualice el `Set Union ControlNet Type` node para FLUX Union, hay un mapeo de tipos. Alternativa: `ComfyUI-eesahesNodes` (EeroHeikkinen) tiene loader dedicado, o `ComfyUI-KJNodes` (kijai) tiene el nodo `Set Shakker Labs Union Control Net Type` que abstrae el mapeo.
- **Modos confiables** (de InstantX table): Canny, Tile, Depth, Blur, Pose, Low Quality — alta calidad. **Gray es bajo** (no usar).
- **Multi-ControlNets**: cargar múltiples `FluxControlNetModel` via `FluxMultiControlNetModel([union])`, ejemplo con canny + depth, scales `[0.2, 0.4]`.
- **Verificado 200**: [huggingface.co/InstantX/FLUX.1-dev-Controlnet-Union](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Union) y [github.com/Comfy-Org/ComfyUI/issues/4355](https://github.com/Comfy-Org/ComfyUI/issues/4355).

### 5.4 XLabs-AI ControlNet (FLUX)

- Repositorio `XLabs-AI/x-flux-comfyui` con ControlNet models específicos para FLUX (Canny, Depth, etc.). Workflows en `Flux Controlnet Example`.
- **No usar simultáneamente con Union Pro** — elegir uno.

### 5.5 ControlNet-XS (Diffusers, soporte parcial en ComfyUI)

- **Arquitectura**: solo **1% de los parámetros** del modelo base, control más pequeño. Mejor FID que ControlNet original en algunos benchmarks.
- Variantes: SDXL (48M params), SD 2.1 (14M params). OpenRAIL license.
- **Status ComfyUI (oct 2026)**: disponible via diffusers pero adopción ComfyUI limitada; no es el default 2026. Útil si el bandwidth de params es limitante (research).

### 5.6 SparseCtrl (RGB y latent)

- ControlNet "sparse": condiciona frames específicos (no la imagen completa) en el contexto de **AnimateDiff-Evolved** (video). Soportado en `ComfyUI-Advanced-ControlNet` (Kosinkadink).
- Nodos: `ACN_SparseCtrlLoaderAdvanced`, `ACN_SparseCtrlMergedLoaderAdvanced`, `ACN_SparseCtrlIndexMethodNode`, `ACN_SparseCtrlSpreadMethodNode`, `ACN_SparseCtrlWeightExtras`, `ACN_SparseCtrlRGBPreprocessor`.
- Caso arquitectura: condicionar ciertos frames clave de un recorrido (inicio, mitad, final) con imágenes de referencia distintas.

### 5.7 GLIGEN, T2I-Adapter, ControlNet++

- **GLIGEN** (box-based grounding): conditioning por bounding boxes. En ComfyUI nativo via conditioning system (`conditioning dictionary` soporta `gligen` tuple).
- **T2I-Adapter** (TencentARC): alternativa ligera a ControlNet para SD1.5/SDXL, 77M parámetros. Modelos canny, lineart, openpose, depth, sketch, color. Workflows en `comfyui_controlnet_aux` o `ComfyUI-Advanced-ControlNet`.
- **ControlNet++** (2024 release): variante mejorada, soporte en `ComfyUI-Advanced-ControlNet` (`ACN_ControlNet++LoaderSingle`, `ACN_ControlNet++LoaderAdvanced`).
- **CtrLoRA**: control via LoRA en lugar de modelo separado, en `ComfyUI-Advanced-ControlNet` (`ACN_CtrLoRALoader`).

### 5.8 Marigold V2 (depth / normal / albedo desde single image)

- **Marigold V2** (Huawei Bayer Lab, 2025): repurpouse de Qwen-Image-Edit 2509 (DiT) para estimación monocular de depth, normal, albedo. Tres LoRAs (uno por tarea) sobre base compartida. Resultado: depth maps más sharp, boundary-aware, generaliza open-domain.
- **Workflow ComfyUI** (oficial): `LoadImage → LoadDiffusionModel (Qwen base) → LoRA (depth/normal/albedo) → Marigold V2 Post-Process → SaveImage`.
- Caso arquitectura: para extraer depth/normal/albedo de una foto existente (fachada, contexto) y luego usarlas como input a ControlNet o como referencia en otro render.
- **Verificado 200**: [docs.comfy.org/tutorials/utility/marigold-v2](https://docs.comfy.org/tutorials/utility/marigold-v2).

## 6. Croquis → render (profundizar)

### 6.1 Receta para croquis a mano suelto en SD 1.5 (RX 570 8GB, ya en pbk)

- Foto de croquis en papel (cualquier iluminación) → `ImageScale 512x512 (lanczos)` → `Scribble` o `Lineart` ControlNet (no preprocesador, el trazo va directo) → `ControlNetLoader (sd15_scribble o sd15_lineart)` → `ControlNetApplyAdvanced (strength 0.5-0.7, end 0.75)` → `KSampler` con `ArchitectureRealmix` y prompt arquitectura.
- Preprocesadores `comfyui_controlnet_aux` (Fannovel16): lineart, scribble, hed, mlsd, canny, depth, normal, seg, openpose. Seleccionar preprocessor node específico desde el menú.

### 6.2 Receta para croquis en FLUX.1 (RunPod, 24 GB)

- Foto croquis → `ImageScale 768x768 o 1024x1024` → **FLUX.1-Canny-dev** (slider 5-7 de 20 steps) o **FLUX.1-Depth-dev** (slider 3-5) → base FLUX.1 dev fp8.
- Para croquis más suelto: depth slider bajo (3) deja al modelo inventar estructura; canny slider bajo (5) deja más libertad.

### 6.3 Receta de doble ControlNet (Canny + Depth)

- SD 1.5 local (n_03 validado): Canny `0.75 / 0.0-0.75` + Depth `0.65 / 0.0-0.85` (dpt_hybrid) en serie antes del KSampler.
- SDXL local RX 570 8 GB: NO intentar dual (OOM) — usar **FLUX.1 Union Pro 2.0** con Canny+Depth en RunPod.
- FLUX.1: cargar **FluxMultiControlNetModel([union])** con controlnet_conditioning_scale `[0.2, 0.4]` (canny primero, depth segundo).

### 6.4 Edge case: croquis muy suelto con sombras o manchas

- **Scribble HED** (no pure scribble): preprocesador `hed` en `comfyui_controlnet_aux` detecta bordes significativos incluso con trazo sucio.
- **Lineart Realistic**: preprocesador `lineart_realistic` en vez de `lineart` default; mejor para croquis con sombreado.
- **Normal Map** (de un render existente) + croquis: si el croquis está sobre una foto, extraer normal con Marigold V2 o `comfyui_controlnet_aux` y combinarlos.

### 6.5 Licencia del input

- Si el croquis es del estudio:没有问题, el output es del estudio.
- Si es croquis de un consultor externo o referencia de Pinterest: revisar que el modelo fine-tune/LoRA usado no esté entrenado con material con copyright explícito. SDXL, FLUX.1 dev, SD 1.5 (OpenRAIL++-M) son seguros en la mayoría de los casos. SD 3.5 tiene restricción de revenue ($1M threshold) pero el estudio cae debajo.

## 7. 3D model → render (CASO CRÍTICO: Rhino/Blender/SketchUp)

### 7.1 Por qué el MCP de Rhino→ComfyUI no es la solución directa

**Gap explícito**: el **MCP (Model Context Protocol) de Rhino** está diseñado para que un **agente AI (Claude, Copilot) controle geometría viva en Rhino** — no para que Rhino exporte a ComfyUI. Son dominios distintos:

- **MCP de Rhino** (`ruiguan/rhinomcp`, `bimolicense/Rhino-MCP-Platform`, `food4rhino.com RhinoAiMCP`): expone tools de geometría (`get_document_info`, `create_object`, `execute_rhinocommon_csharp_code`, etc.) sobre TCP loopback `127.0.0.1:1999` (default). Agentes llaman tools, Rhino ejecuta, devuelve resultado.
- **ComfyUI MCP servers** (`yutianxiao6/comfyui-mcp`, `joenorton/comfyui-mcp-server`, `artokun/comfyui-mcp`, `wireflow.ai` guide, official Comfy Cloud MCP): exponen tools de workflow de ComfyUI (`generate-image`, `submit_workflow`, `queue_prompt`). Agentes llaman, ComfyUI ejecuta, devuelve imagen.

**No existe un puente nativo Rhino→ComfyUI vía MCP** (verificado búsqueda multi-fuente, oct 2026). Los dos servidores MCP pueden coexistir en el mismo agente (uno controla Rhino, otro ComfyUI), pero el flujo "Rhino viewport → ComfyUI render" sigue requiriendo **render passes intermedios** o **bridge de archivo**.

**Limitaciones documentadas de los MCP de Rhino**:

- `ruiguan/rhinomcp`: solo creación de primitivas (Point, Line, Polyline, Circle, Arc, Ellipse, Curve, Box, Sphere, Cone, Cylinder, Surface); `get_document_info` cap a 30 objetos; complejo debe descomponerse.
- Tools abiertas (`run_command`, `execute_rhinoscript_python_code`, `execute_rhinocommon_csharp_code`): superficie de ejecución abierta dentro de Rhino — inseguro si se expone fuera de loopback.

**Recomendación del estudio**: usar **MCP de Rhino para scripting/automation geométrica** (Claude controlando Rhino para preparar la escena) + **render passes / export de archivo para ComfyUI** (no vía MCP). El workflow mixto: "Claude, en Rhino exporta depth, lineart y shaded PNG del viewport perspectiva" → "Claude, llama a ComfyUI con estos 3 PNGs y depth ControlNet 0.85, lineart 0.7, denoise 0.5".

### 7.2 Ruta A: Render passes de Rhino/Blender/SketchUp → ComfyUI img2img

**El patrón ArchiGen 2026 (3 passes)** — el más confiable para estudio:

1. **Depth pass** desde el viewport: en Rhino, display mode custom con edges hidden, color = linear ramp B/N por Z distance desde la cámara, no shadows. Output `2048 px` en lado largo.
2. **Lineart / Make2D pass**: viewport con technical display, edges on (solo edges visibles — NO construction lines, isocurves, hidden edges). O `Make2D` desde Rhino.
3. **Flat shaded pass**: viewport con materials asignados pero lighting plano (no sombras). Va a IP-Adapter o img2img como style reference para materialidad.

**En ComfyUI**:
- `LoadImage (depth)` → `ControlNet Depth` (strength 0.85, end 0.7) — **el ancla estructural**
- `LoadImage (lineart)` → `ControlNet Lineart / Canny` (strength 0.7, end 0.8) — **mantiene geometría**
- `LoadImage (flat shaded)` → `IPAdapter Plus (style only, weight 0.4)` — **pasa materialidad sin aplanar luz**
- `KSampler` con prompt describiendo **luz, atmósfera, hora del día, cielo, materiales** (NO geometría — eso ya está en el render)
- Deny de **denoise 0.40-0.55** = el sweet spot "render-rescue" (añade luz, no inventa geometría)

**Troubleshooting del patrón**:

- Depth gradient demasiado steep → model "inventa" profundidad. Fix: depth clipping bounded a un rango alrededor del edificio, no desde camera to infinity.
- Lineart demasiado denso (todos los edges Make2D) → output parece elevation coloreada. Fix: ocultar construction lines, isocurves, hidden edges antes de Make2D.
- IP-Adapter weight alto aplana lighting. Fix: bajar a 0.4 y dejar que el modelo maneje luz por prompt.

**Rhinoceros específicamente**: depth pass es más limpio que SketchUp (no polygonal artifacts en NURBS). Make2D exporta limpio. Materiales desde rendered display mode sobreviven hasta IP-Adapter.

**Verificado 200**: [archigenai.com/comfyui-rhino-architects-workflow-2026.html](https://archigenai.com/comfyui-rhino-architects-workflow-2026.html) y [archigenai.com/render-rescue-3d-viewport-to-client-ready-2026.html](https://archigenai.com/render-rescue-3d-viewport-to-client-ready-2026.html).

### 7.3 Ruta B: ComfyUI-3D-Pack (MrForExample) — el gigante 2026

Repositorio: [github.com/MrForExample/ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) (~5K stars, 2024-01 launch, mantenido activo). Versión actual v0.1.6 (2026).

**Qué hace**: suite de nodos para que ComfyUI procese **3D inputs (mesh, UV texture)** con algoritmos cutting-edge (3DGS, NeRF, FlexiCubes) y modelos (InstantMesh, CRM, TripoSR, Hunyuan3D, Unique3D, TRELLIS, Zero123++).

**Modelos integrados** (lista de release notes v0.1.6):

| Modelo | Pipeline | Output | Caso arquitectura |
|---|---|---|---|
| **Hunyuan3D-2 (V1, V2, V2.1, Turbo, Mini, Fast, MultiView)** | 2 stages: image → multi-view + RGB texture | Mesh con textura | Object 3D desde referencia, alta calidad |
| **Unique3D** | 4 stages: image → 4 multi-view 256² → upscale 512² + super-resolution 2048² → normal maps 2048² → mesh + texture | Mesh detallado | Objetos con fine surface detail |
| **TRELLIS** | Image → 3D mesh + RGB texture | Mesh con textura | General object, buena calidad |
| **Zero123++** | Image → 6 view images 320² | Multi-view images | Pre-input para InstantMesh |
| **InstantMesh** | Sparse multi-view + white bg → mesh + RGB texture | Mesh | Reconstrucción 3D desde vistas |
| **CRM** (Convolutional Reconstruction Model) | 3 stages: 6 views → CCMs → mesh | Mesh | 3D desde 6 vistas ortogonales |
| **TripoSR** | Image → 3D mesh | Mesh | Quick object 3D (rápido) |
| **CharacterGen** | Front view → character in arbitrary pose | Character mesh | Personajes (no arquitectura) |
| **LGM / TriplaneGaussian** | Image → 3D Gaussian representation | 3DGS (rápido <30s) | Quick visualization |
| **FlexiCubes** | Multi-view depth + mask (+ normal) → 3D mesh | Mesh | Reconstrucción desde depth |
| **3D Gaussian Splatting (3DGS)** | Multi-view → .ply 3DGS | Point cloud | Visualization |
| **Instant NGP** (nerfacc) | Multi-view → mesh via marching cubes | Mesh | Nerf-based reconstruction |
| **PartCrafter** | Scene → part decomposition | Part-level meshes | Descomposición de objetos |
| **MV-Adapter** (ig2mv, t2v) | Image/video → multi-view | Multi-view | Generación de multi-view |
| **Stable3DGen** | Image → 3D | Mesh | Alternativa |

**Nodos clave**:

- `[Comfy3D] Stack Orbit Camera Poses`: genera poses de cámara orbitales (azimuth, elevation, distance) para condicionar
- `[Comfy3D] Mesh Orbit Renderer`: renderiza mesh desde orbit camera, output: images, masks, depth, normals, viewcos. Requiere CUDA rasterize.
- `[Comfy3D] Gaussian Splatting Orbit Renderer`: similar pero para 3DGS
- `[Comfy3D] Preview 3DMesh`: visualizador three.js del mesh en ComfyUI
- `[Comfy3D] ExplicitTarget Color Projection`: bakea textura al mesh desde multi-view images
- `[Comfy3D] Fitting Mesh With Multiview Images`: refina mesh con texturas baked

**Workflow típico imagen→mesh→render multi-vista**:

```
LoadImage → Load Diffusers Pipeline (Hunyuan3D-2 Standard Pipeline)
         → Hunyuan3DDiTFlowMatchingPipeline (image → multi-view)
         → Hunyuan3DPaintPipeline (texturing)
         → Preview 3DMesh / Save GLB
       ↓ (opcional)
Load GLB → Stack Orbit Camera Poses → Mesh Orbit Renderer (8 views) → Image Grid → SaveImage
```

**VRAM**: requiere CUDA (no DirectML), 12-24 GB recomendado. Para RX 570 8GB, el image→mesh no es viable — usar Tripo3D API (cloud) o TripoSR via `comfyui-triposr-simple` (P5ina) que es más liviano.

### 7.4 Ruta C: Tripo3D Partner Node (oficial, nativo en ComfyUI)

**Tripo3D** está integrado nativamente como **Partner Node** en ComfyUI (no requiere custom node externo). Modelos: v1.4, v3.0, v3.5, v3.6. Capacidades:

- **Text-to-Model** (`TripoTextToModelNode`)
- **Image-to-Model** (`TripoImageToModelNode` legacy, `TripoP1ImageToModelNode` recomendado)
- **Multi-view to Model**
- **Rig + Retarget** (animar)
- **Texture / Refine** (PBR maps, quad remeshing)
- **Format conversion** (GLB, FBX, GLTF)

**Parámetros clave (`TripoP1ImageToModelNode`)**:

- `output_mode`: "Geometry only" o "Textured"
- `model_version`: v1.4, v3.0, v3.5, v3.6
- `pbr`: True (base color + metallic + roughness + normal)
- `texture_quality`: "standard", "detailed" (HD), "extreme" (8K)
- `texture_alignment`: "original_image" (fidelity a source) o "geometry" (alignment a mesh)
- `face_limit`: -1 (adaptive, ~1.4M v3.x standard, 2M detailed); v2.5 clamps a 500K; quad a 150K
- `quad`: True (FBX output, quad mesh)
- `smart_low_poly`: True (500-20K faces, quad 500-10K) para "low-poly hand-crafted"
- `auto_size`: True (escala a tamaño real-world en metros)

**Pricing (Tripo 3.1)**: USD por `consumed_credit * 0.01`. Pricing badges de cada nodo muestran el costo estimado aproximado. Text-to-Model ~$0.10, Image-to-Model ~$0.10-0.30 según quality, Refine ~$0.05-0.10, Texture ~$0.10, Rig ~$0.10, Retarget ~$0.05.

**Workflow arquitectura recomendado**:

```
1. Rhino/Blender → export frontal render
2. ComfyUI: TripoP1ImageToModelNode (textured, detailed, 2048) → GLB
3. ComfyUI-3D-Pack: Preview 3DMesh, Stack Orbit Camera Poses, Mesh Orbit Renderer → 8 views
4. IP-Adapter (estilo arquitectura) sobre cada vista → lote moodboard
```

**Verificado 200**: [docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p1](https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p1) y [github.com/VAST-AI-Research/ComfyUI-Tripo](https://github.com/VAST-AI-Research/ComfyUI-Tripo).

### 7.5 Ruta D: Render-rescue (img2img denoise 0.40-0.55)

**Caso**: el estudio ya tiene un render de Rhino/Enscape/V-Ray pero "no tiene la magia" (luz plana, materiales sin profundidad). NO re-renderizar: **rescatar con ComfyUI**.

**Receta ArchiGen 2026**:

- Input: render viewport (Rhino, Blender, SketchUp, Revit) en cualquier resolución.
- Pipeline: `LoadImage → ImageScale 1024 (si es necesario) → img2img KSampler denoise 0.48 + ControlNet Depth (del mismo render) strength 0.85 end 0.7` + prompt describiendo **luz, atmósfera, hora del día, materiales (NO geometría)**
- **Denoise band útil**: 0.40-0.55. Debajo = sigue siendo CAD. Arriba = inventa, smoothing de mullions, guessing materiales.
- **Output**: render "fotográfico" sin perder el modelo.

**Caso prueba ArchiGen**: Rhino courtyard, denoise 0.48 + depth 0.85 = frame claramente el modelo, lit como fotografía.

### 7.6 Ruta E: 3D Viewport en ComfyUI (in-situ viewer)

**`brandondunwell/comfyui-3d-viewer-pro`**: viewer 3D basado en three.js, multi-pass rendering engine. Output **6 feature maps en una sola ejecución**: Color (PBR), Depth Map, Normal Map, Wireframe, AO/Silhouette, Native MASK. Bypass Windows DPI scaling, soporta RGBA transparencia, Studio Sync para Turntable nodes.

**`JosephOIbrahim/comfyui-3D-viewport`**: OpenGL viewport nativo, cámara física accurate, depth + normal AOVs streamed a ControlNet. Bridge HTTP/JSON + WebSocket. Companion `Comfy-Cozy` (Opus 4.7 co-pilot) consume AOVs. Mayo 2026 release. **Verificado 200**: [github.com/JosephOIbrahim/comfyui-3D-viewport](https://github.com/JosephOIbrahim/comfyui-3D-viewport).

### 7.7 Ruta F: `comfyui-triposr-simple` (P5ina)

Paquete mínimo para image-to-mesh con TripoSR. Input image → 3D mesh → render 8 cardinales/intercardinales (N, NE, E, SE, S, SW, W, NW). Mesh con vertex colors. Elevation, distance, background configurables. Modo pixel art incluido (8 renders + pixelate + combine). **Verificado 200**: [comfy.icu/extension/P5ina__comfyui-triposr-simple](https://comfy.icu/extension/P5ina__comfyui-triposr-simple).

### 7.8 Comparativa de rutas 3D → render

| Ruta | VRAM | Tiempo | Calidad | Caso ideal |
|---|---|---|---|---|
| **A. Render passes Rhino + img2img** | 8 GB (RX 570) | minutos | ★★★★ | Re-renderizar manteniendo modelo CAD |
| **B. ComfyUI-3D-Pack (Hunyuan3D-2, Unique3D)** | 24 GB (RunPod) | minutos | ★★★★★ | Object 3D desde imagen, multi-view |
| **C. Tripo3D Partner Node** | mínimo (cloud API) | 30s-2min | ★★★★ | Text/image → 3D model rápido, comercial |
| **D. Render-rescue img2img** | 8 GB | 1-2 min | ★★★★ | Render existente que "no tiene la magia" |
| **E. 3D-Viewport-Pro** | variable | interactivo | ★★★ | Previsualizar mesh en ComfyUI |
| **F. comfyui-triposr-simple** | 8 GB | segundos | ★★★ | Pixel art, props rápidos |
| **Image-to-3D → render** (TripoSR → 3D-Pack) | 8-24 GB | minutos | ★★★★ | Vista 3D de un objeto desde 1 foto |

## 8. Video arquitectónico (recorridos, flythrough, presentación)

### 8.1 Mapa de modelos video 2026 (octubre)

| Modelo | Params | VRAM | Duración max | Audio | Licencia | Caso arquitectura |
|---|---|---|---|---|---|---|
| **LTX-2.3 (Lightricks)** | 22B | 24 GB (full), 16 GB (FP8/GGUF) | Ilimitado con chain (5 s por chunk, Video S2V Extend +77 frames c/u) | **Sí, sincronizado nativo** (diálogo, música, SFX) | Open (verificar weights) | **Recomendado para estudio**: render → recorrido 10 s con audio ambiente |
| **LTX-2.0 (legacy)** | 19B | 24 GB | 5-10 s | Sí | Open | (reemplazado por 2.3) |
| **Wan2.2-TI2V-5B (Alibaba)** | 5B | **8 GB** (con offloading) | 5 s @ 720p 24fps | No nativo (Wan2.2-S2V separado) | Apache 2.0 | **Mejor entry-level 8 GB**, prototipo rápido |
| **Wan2.2-T2V-A14B / I2V-A14B (MoE)** | 14B activo (27B total) | 14-16 GB (FP8) | 5-10 s | Wan2.2-S2V separado (audio-driven) | Apache 2.0 | T2V y I2V alta calidad |
| **Wan2.2-Fun-Control (Alibaba PAI)** | 14B | 14-16 GB | 5-10 s | No | **Apache 2.0 (comercial OK)** | **ControlNet-like control**: Canny, Depth, OpenPose, MLSD, trajectory |
| **Wan2.2-Fun-Inp** | 14B | 14-16 GB | 5-10 s | No | Apache 2.0 | Start-end frame control (interpolación) |
| **HunyuanVideo 1.5 (Tencent)** | 8.3B | 24 GB (full), 8 GB (quantized) | 5-10 s | No | Open | Calidad cinematográfica, bajo VRAM con quantización |
| **HunyuanVideo (legacy)** | 13B | 24+ GB | 5 s | No | Open | Reemplazado por 1.5 |
| **Mochi 1 (Genmo)** | 10B | 24-40 GB (quantized 20-24) | 5.4 s @ 848×480 | No | Open weights + training | Smooth motion, physics (research) |
| **CogVideoX-5B (THUDM/Zhipu)** | 5B | 16 GB | 6 s @ 1440×960 | No | Apache 2.0 | Detail/texture, narrative, image-to-video |
| **CogVideoX-5B-Lite** | 2B | 8-12 GB | 6 s @ 480p | No | Apache 2.0 | Entry-level, hardware limitado |
| **SVD 2.5 (Stability)** | ~2B | 12-16 GB | 14-25 frames | No | Stability Community | **Legacy**: image-to-video suaves, 4 GB no es viable |
| **AnimateDiff-Evolved (SD 1.5)** | ~0.4-1.6 GB motion module | 6-8 GB | 16-32 frames | No | Open | **Legacy**: test de masa/movimiento, no entrega |

### 8.2 LTX-2.3 (recomendado para estudio, 2026-10)

**Verificado 200**: [docs.comfy.org/tutorials/video/ltx/ltx-2](https://docs.comfy.org/tutorials/video/ltx/ltx-2) y [github.com/Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo).

- **Nativamente soportado en ComfyUI core** (no requiere custom node). Workflows en `Template Library > Video > LTX-2`.
- **Modelos requeridos** (descargar via prompt automático):
  - LTX-2 distilled checkpoint o full model
  - LTX video upscaling model (2× resolution)
  - **Gemma CLIP text encoder** (Long-context, 24B+)
  - VAE (decodifica video + audio latents)
  - Opcional: LoRAs control (camera, depth, canny, pose, HDR, detailer, dub-it, pixel spatial upscaling, day-to-night, deblur, etc.)
- **Pipeline I2V (Distilled)**:
  1. `LoadImage` → `ResizeImageMaskNode` (video-safe size) → `LTX-2 Distilled Subgraph` → `SaveVideo`
  2. Configuración: 121 frames ≈ 5 s, 720p, 48-60 FPS para dynamic motion
  3. CFG 1 (distilled) o 4 (full), `res_2S` scheduler
  4. Prompt: detail-rich (visual style, character, camera motion, dialogue, music, SFX)
  5. **Multiscale rendering**: base 960×540 + upscale 2× = 1080p output
- **Audio-video split-merge**: video + audio latents generados independientes, merged con `LTXVConcatAVLatent`, tile decoding reduce VRAM
- **Single-frame I2V**: `LTXVImgToVideoInplace` inyecta image como first frame; `strength 1.0` para tight adherence, `0.7-0.9` para creative motion
- **Multi-frame I2V** (continuación): image batch con últimas N frames del video (8n+1), genera 121-N frames restantes, concatena
- **IC-LoRA Control (Depth, Canny, Pose)**: `ltx-2-19b-ic-lora-{Depth,Canny,Pose}-Control` + `LTXAddVideoICLoRAGuide` antes del sampler
- **Camera motion LoRAs**: `ltx-2-19b-lora-camera-control-{dolly-in,left,out,right,jib-down,up,static}.safetensors` para flythrough explícito
- **Audio2Video**: `LTXVConcatAVLatent` con audio input como conditioning
- **Talking avatar**: image + speech audio (16 kHz mono, <5 s) → lip-synced video
- **HDR, SDR→HDR, in/outpainting, day-to-night, water simulation**: LoRAs específicos disponibles
- **VRAM**: distilled corre en 16 GB, full en 24 GB. **GTX 5090 + GGUF para 16 GB**.

### 8.3 Wan2.2 (Alibaba) — entry-level 8 GB

**Verificado 200**: [docs.comfy.org/tutorials/video/wan/wan2_2](https://docs.comfy.org/tutorials/video/wan/wan2_2).

- **Wan2.2-TI2V-5B** (5B denso, single model) corre en **8 GB con offloading nativo** — la mejor opción entry-level. `wan2.2_ti2v_5B_fp16.safetensors` en `models/diffusion_models/`. ~9 min para 5 s @ 720p en consumer GPU.
- **Wan2.2-T2V-A14B / I2V-A14B** (14B MoE, dos archivos: `high_noise_14B_fp8_scaled.safetensors` + `low_noise_14B_fp8_scaled.safetensors`): MoE architecture divide denoising en dos expertos (high-noise = layout, low-noise = detalles). Sampleo con KSampler Advanced, switch a high→low en step ~4 de 20.
- **Wan2.2-Fun-Control** (Apache 2.0, comercial): control tipo ControlNet (Canny, Depth, Pose, MLSD, trajectory). Requiere `umt5_xxl_fp8_e4m3fn_scaled.safetensors` (text encoder) + Wan VAE.
- **Wan2.2-S2V** (audio-driven): audio + image → video sincronizado, hasta 14 s. `wav2vec2_large_english_fp16.safetensors` (audio encoder) + 4-step Lightning LoRA.
- **GGUF quantized** (city96, bullerwins): Q3-Q8, reducción 30-50% VRAM.
- **Lightx2v 4-steps LoRA** (lightx2v): `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise/low_noise` — velocidad, pero mata el motion.
- **Prompt formula (i2v)**: Motion + Camera movement. NO describir el sujeto (la imagen ya lo hace). Ej: "the subject slowly turns her head, camera pushes in". SIEMPRE decir "fixed camera" si se quiere estática.

### 8.4 HunyuanVideo 1.5 (Tencent, 2026)

**Verificado 200**: [docs.comfy.org/tutorials/video/hunyuan/hunyuan-video-1-5](https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video-1-5).

- **8.3B parámetros**, calidad flagship, **24 GB VRAM full**, cuantizado cabe en 8 GB. Step-distilled 480p I2V: **8-12 steps en lugar de 50**.
- **Modelos**: `hunyuanvideo1.5_720p_t2v_fp16.safetensors`, `hunyuanvideo1.5_720p_i2v_fp16.safetensors`, `hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors` (super-res 720p→1080p). Text encoders: `qwen_2.5_vl_7b_fp8_scaled.safetensors` + `byt5_small_glyphxl_fp16.safetensors`. VAE: `hunyuanvideo15_vae_fp16.safetensors`.
- **5-10 s @ 720p 24fps**, super-res 1080p opcional.
- **MagCache** (ComfyUI-MagCache): 1.7x speedup, 20 inference steps.
- **Kijai/ComfyUI-HunyuanVideoWrapper**: wrapper alternativo con IP2V (image prompting via VLM, no como first frame), context windowing, manual memory management, LoRA support, torch.compile.

### 8.5 Mochi 1, CogVideoX, SVD 2.5

- **Mochi 1** (Genmo, 10B): AsymmDiT architecture, smooth motion y physics realistas, **24 GB mínimo**, cuantizado 20-24 GB. Limitado a 480p en preview; menor detalle que CogVideoX. Fully open weights + training code (research-friendly).
- **CogVideoX-5B** (THUDM/Zhipu, 5B/10B): mejor prompt adherence, 720p, 6 s. **16 GB accesible**. Texture/detail mejor que Mochi. Multi-GPU para 10B.
- **CogVideoX-5B-Lite** (2B): entry-level, 8-12 GB, 480p.
- **SVD 2.5** (Stability): legacy image-to-video, 12-16 GB, micro-movements y camera tracking. NO viable en 4 GB. Mejor para cinemagraph y loop. Remplazado para entrega por LTX-2/Wan2.2/HunyuanVideo 1.5.
- **AnimateDiff-Evolved**: SD 1.5 motion module, 16-32 frames, 6-8 GB, **solo para test de masa/movimiento, nunca entrega**.

### 8.6 Caso práctico: render estático → recorrido 10 s para cliente

**Setup**: RX 570 8GB local (desarrollo, mocks) + RunPod RTX 3090/4090 24 GB (entrega).

**Pipeline recomendado (LTX-2.3 distilled)**:

1. **Render del estudio** (Rhino/Enscape/V-Ray): vista perspectiva exterior, 2048×1152, guardada en `activos/proyectos/<cliente>/renders/`.
2. **Stage en ComfyUI**:
   - `LoadImage` → `ResizeImageMaskNode` (video-safe, 768×432 o 1024×576)
   - **Generar variantes de cámara**: si la imagen es estática, el modelo "inventa" el movimiento. Para flythrough explícito, usar IC-LoRA `dolly-in.safetensors` + prompt `"camera slowly pushes forward, subtle parallax"`.
3. **LTX-2.3 I2V Distilled**:
   - `LTXVConcatAVLatent` con audio opcional (música ambiente, `LTXVConcatAVLatent` con `Trim Audio Duration`)
   - `LTXVScheduler`, 8 steps distilled, CFG 1, euler/res_2S
   - 121 frames @ 24fps = 5 s (chunk 1)
4. **Extender a 10 s**:
   - `Get End Image Batch` (últimos 8 frames del chunk 1) → `LTXVImgToVideoInplace` para chunk 2 → concat
5. **Output**: MP4 con audio. `VHS_VideoCombine` a `activos/proyectos/<cliente>/videos/recorrido-01.mp4`.
6. **Archivo**: nombre `n_XX-{V}-{NN}.mp4` (V = video), log en `02-WF-log-*.md`.

**Costos RunPod (oct 2026, estimado)**:

- RTX 3090 24 GB community: ~$0.22 USD/h
- 5 s de LTX-2.3 distilled @ 720p + audio: ~5 min computo
- 10 s (2 chunks) + concatenación + Hires: ~15 min = $0.055 USD por video
- Para cliente, margen: $5-20 USD por video (vs. $200-500 USD de motion graphics tradicional)

### 8.7 Nodos ComfyUI nativos para video

- `LoadImage` + `VHS_VideoCombine` (custom node `ComfyUI-VideoHelperSuite`) para input/output
- `EmptyLTXVLatentVideo`, `LTXVScheduler`, `LTXVImgToVideoInplace`, `LTXVConcatAVLatent` (nativos LTX)
- `Wan22ImageToVideoLatent`, `WanFirstLastFrameToVideo`, `Wan22FunControlToVideo`, `WanFunInpaintToVideo` (nativos Wan)
- `HunyuanImageToVideo` (nativo), `TextEncodeHunyuanVideo_ImageToVideo` (nativo)
- `Kijai/ComfyUI-HunyuanVideoWrapper` (custom, Hunyuan IP2V + features avanzadas)
- `Kijai/ComfyUI-WanVideoWrapper` (custom, Wan optimizaciones)

## 9. Pack de nodos 2026 (de facto)

### 9.1 Built-in core (ya viene con ComfyUI)

- `LoadImage`, `SaveImage`, `ImageScale`, `ImageBatch`, `ImageGrid`
- `KSampler`, `KSamplerAdvanced`, `SamplerCustomAdvanced`
- `CLIPTextEncode`, `CLIPTextEncodeFlux`, `CLIPTextEncodeSD3`
- `CheckpointLoaderSimple`, `DualCLIPLoader`, `TripleCLIPLoader` (SD3), `Load Diffusion Model` (FLUX.2)
- `ControlNetLoader`, `ControlNetApply`, `ControlNetApplyAdvanced`
- `VAEEncode`, `VAEDecode`, `VAEDecodeTiled`
- Todos los nodos nativos Wan2.2, LTX-2, HunyuanVideo 1.5, FLUX.1 Tools, Tripo3D, FLUX.2

### 9.2 Custom nodes estándar 2026 (instalar via ComfyUI-Manager)

| Pack | Autor | Función | Estado 2026 |
|---|---|---|---|
| **comfyui-manager** | Dr.Lt.Data (ahora Comfy-Org) | Install/remove custom nodes, missing nodes detection, GUI management | **Built-in core desde 2025**; `--enable-manager` flag; security levels (Strict/Standard/Relaxed/Permissive); 3 DB modes (Channel cache/Local/Channel remote) |
| **comfyui_controlnet_aux** | Fannovel16 | Preprocesadores (canny, lineart, scribble, hed, mlsd, depth, normal, seg, openpose, Zoe, DepthAnything V2) | **Esencial**, vigente |
| **ComfyUI-Advanced-ControlNet** | Kosinkadink | ControlNet schedule, timestep keyframes, ControlNet++, SparseCtrl, SVD-ControlNet, T2IAdapter, CtrLoRA, Reference ControlNet | **Esencial** para CN avanzado, vigente |
| **ComfyUI-Impact-Pack** | ltdrdata | FaceDetailer, BboxDetector, hand detection, SAMDetector, DetailerForEach, RegionalPrompt, RegionalSampler | **Esencial** para face/hand repair, multi-subject |
| **rgthree-comfy** | rgthree | Power LoRA Loader, Seed node, Fast Group, Mute/Bypass shortcuts, Display Any | **Esencial** para producción, vigente |
| **ComfyUI-KJNodes** | kijai | Image manipulation, video helpers, advanced samplers, FirstBlockCache, Hunyuan patching, Wan Video Wrapper | **Esencial**, mantenido muy activo |
| **ComfyUI-3D-Pack** | MrForExample | Hunyuan3D-2, Unique3D, TRELLIS, Zero123++, InstantMesh, CRM, TripoSR, FlexiCubes, 3DGS, NGP | **Estándar 3D**, vigente, v0.1.6 |
| **ComfyUI-LTXVideo** | Lightricks | LTX-2 workflows y nodes adicionales (IC-LoRA, Tiled Fusion, camera control) | **Esencial** para LTX-2 |
| **ComfyUI-WanVideoWrapper** | kijai | Wan 2.1/2.2 optimizaciones | Útil para Wan |
| **ComfyUI-HunyuanVideoWrapper** | kijai | HunyuanVideo features avanzadas (IP2V, context windowing) | Útil para Hunyuan |
| **ComfyUI-IPAdapter_plus** | cubiq | IP-Adapter para SD1.5/SDXL, Unified Loader, FaceID, Style+Composition Batch | **Maintenance-only desde 2025-04-14** — pin versión o migrar a native FLUX.2 |
| **ComfyUI-Krea2Moodboard** | RedNodeAI | Krea 2 moodboard nodes (style+identity fusion) | Reciente, single model target |
| **comfyui-Krea2Moodboard** | RedNodeAI | Krea 2 vibe transfer + identity edit | Para flujos Krea 2 |
| **comfyui-3d-viewer-pro** | brandondunwell | 3D viewer three.js + multi-pass (color/depth/normal/wireframe/AO/mask) | Para previsualización |
| **comfyui-3D-viewport** | JosephOIbrahim | OpenGL viewport + AOV streaming + Comfy-Cozy co-pilot | Mayo 2026 release |
| **comfyui-triposr-simple** | P5ina | TripoSR image-to-mesh + 8 cardinal render | Lightweight 3D entry |
| **ComfyUI-Florence2SAM2** | rdancer | Florence-2 + SAM 2 (open-vocabulary detection + segmentation) | Para extracción de regiones |
| **ComfyUI-segment-anything-2** | kijai | SAM 2 wrapper, Florence2toCoordinates bridge | Para segmentación |
| **ComfyUI-YoloWorld-EfficientSAM** | ZHO-ZHO-ZHO | YOLO-World + EfficientSAM, mask separated/extracted | Para object detection |
| **comfyui-mixlab-nodes** | mixlab | Various utilities (Animation, 3D, Audio) | Complementario |
| **ComfyUI-Lora-Pipeline** | andreszs | Area-based conditioning pipeline para multi-subject, schedule LoRA strength | Multi-subject con ControlNet |
| **MultiMaskCouple** | tumbowungus | Multi-mask attention coupling (PromptChain Attention Couple) | Multi-character |
| **Anima-Regional** | An1X3R | Character-level regional routing para Anima | Anima-specific |
| **ComfyUI-MagCache** | — | MagCache para HunyuanVideo 1.5 (1.7x speedup) | Aceleración |
| **comfyui_detail_daemon** | — | Detail Daemon sampler (boost skin/hair micro-texture) | Para fotorrealismo FLUX |
| **ComfyUI-YoloWorld-EfficientSAM** | ZHO-ZHO-ZHO | Object detection + instance segmentation | Para máscaras de objetos |
| **comfyui_segment_anything** | continue-revolution | SAM 1.x wrapper (más viejo, reemplazado por SAM 2) | Legacy |

### 9.3 Instalación recomendada vía ComfyUI-Manager

```bash
# Built-in core
pip install -r manager_requirements.txt
python main.py --enable-manager

# Desde Manager GUI, instalar en este orden:
# 1. comfyui_controlnet_aux (Fannovel16)
# 2. ComfyUI-Advanced-ControlNet (Kosinkadink)
# 3. ComfyUI-Impact-Pack + Impact Subpack
# 4. rgthree-comfy
# 5. ComfyUI-KJNodes (kijai)
# 6. ComfyUI-3D-Pack (MrForExample) - solo si se trabaja con 3D
# 7. ComfyUI-LTXVideo (Lightricks) - si se hace video
# 8. Tripo nodes (Partner Node nativo, no requiere install)
```

**Security**: `security_level = strict` por default, `allow_git_url_install = false` para no instalar nodos no verificados. **Para estudio con IP sensible: NO usar `Permissive` ni `Relaxed`**.

## 10. DoD, licencias y archivo

### 10.1 DoD (Definition of Done) — referenciar pbk-comfyui § DoD

(NO modificar, ya vigente en pbk)

- Salida: nombre `n_XX-{A–F}-{NN}.png` (A baseline, B prompt, C params, D modelo, E resolución, F ControlNet/img2img) en `salidas/` del WF
- Entrada en `02-WF-log` (seed, cfg, steps, modelo, strength)
- Render final → `activos/proyectos/<proyecto>/renders/`
- Licencia verificada ANTES de entrega comercial

### 10.2 Licencias 2026 — qué sirve para entrega comercial

| Licencia | Modelos | Comercial | Notas |
|---|---|---|---|
| **Apache 2.0** | **FLUX.1 [schnell]**, **FLUX.2 [klein] 4B**, Z-Image (verificar weights), Wan2.2, CogVideoX, Mochi 1, AuraFlow, Sana, PixArt-Σ, Chroma | **Sí, libre** | Atribución requerida |
| **OpenRAIL++-M** | SD 1.5, SDXL 1.0, ControlNet SD1.5, Juggernaut XL, большинство LoRAs Civitai (incluido JJ's Brutalist Architecture) | **Sí con restricciones** | Atribución, no uso ilegal, no impersonation |
| **FLUX Non-Commercial License** | FLUX.1 [dev], FLUX.1 Kontext [dev], FLUX.2 [dev] (32B), FLUX.2 [klein] 9B | **No (con exception)** | Outputs pueden usarse comercialmente per model card, pero el license text conflicts — **pedir licencia comercial a BFL para paid client work** |
| **Stability AI Community License** | SD 3.5 Large / Large Turbo / Medium | **Sí bajo $1M revenue/año** | Studio cae debajo; OK. Si estudio > $1M, requiere Enterprise license |
| **CreativeML Open RAIL-M** | Algunos LoRAs viejos (SD 1.5 era) | **Sí con restricciones** | Similar a OpenRAIL++-M |
| **CC-BY-NC** | **NO USAR** (Remacri, ClearReality upscalers, algunos LoRAs) | **No** | Solo interno, estudio |
| **NVIDIA Open Model License** | Sana weights | Sí con restricciones | Open, no use para impropio |
| **Tencent Hunyuan** | HunyuanVideo 1.5, Hunyuan3D-2 | Sí (open) | Verificar cada release |
| **Black Forest Labs Non-Commercial** | FLUX.1 [pro]/[max] son API-only (no weights), Kontext [max] también | No (API comercial) | Si se usa API BFL, es comercial OK con plan |

### 10.3 Matriz de decisión licencia para entrega

- **Hero shot, A3, cliente privado (paga en USD)**: **FLUX.2 [klein] 4B (Apache 2.0)** + Hires 1.5x + RealESRGAN_x4plus (OpenRAIL). Cero restricción.
- **Concurso público, single image**: **SDXL 1.0 + Juggernaut XL (OpenRAIL++-M)**. Atribución al modelo en créditos.
- **Concurso público, video**: **Wan2.2 (Apache 2.0)** o **LTX-2.3 (verificar)**.
- **Concurso + tipografía en imagen (rótulo, plano)**: **SD 3.5 Large (Community License bajo $1M)**.
- **Render de presentación interna (no cliente)**: cualquier modelo fine-tune o LoRA CC-BY-NC, mientras no salga del estudio.
- **NO usar para cliente**: FLUX.1 [dev] (Non-Commercial) sin licencia explícita, LoRAs CC-BY-NC, SD 3.5 con revenue > $1M (Enterprise).

### 10.4 Archivo de outputs en el vault

- Salidas que entran a proyecto: nombre `n_XX-{L}-{NN}.png` (ver `reglas-workflows-comfy.md`)
- Renders de entrega comercial: `activos/proyectos/<cliente>-<proyecto>-<ciudad>/renders/`
- Videos: `activos/proyectos/<cliente>-<proyecto>-<ciudad>/videos/`
- 3D meshes: `activos/proyectos/<cliente>-<proyecto>-<ciudad>/modelos-3d/`
- Logs de corrida: `02-WF-log-*.md` dentro de cada WF
- Modelos grandes: NO se commitean a git (gitignored). Solo referencia por path en `models/`.

## Decisiones para el estudio

1. **Adoptar FLUX.2 [klein] 4B (Apache 2.0) como modelo default de iteración y entrega.** Q4 GGUF para RX 570 8GB local; FP8 en RunPod para entrega. Reemplaza a FLUX.1 [dev] (non-commercial) como default de producción.
2. **Construir n_05-rhino-pipeline** (nuevo WF) implementando el patrón 3-pass de §7.2: depth + lineart + flat shaded desde Rhino Make2D, ip-adapter + ControlNet Depth/Lineart, denoise 0.45-0.55. Reutiliza `pbk-comfyui` § Upscale.
3. **Construir n_06-render-rescue** (nuevo WF) para rescatar renders viejos con §7.5 (denoise 0.48 + depth 0.85). Caso de uso típico: "tengo un render de hace 3 años, quiero que parezca 2026 sin re-renderizar".
4. **Evaluar Tripo3D Partner Node** para flujos image→3D→render multi-vista. Costo bajo ($0.10-0.30 por modelo) lo hace viable para iteración rápida.
5. **Video arquitectónico via LTX-2.3 en RunPod**. Instalar `ComfyUI-LTXVideo` y probar `ltx-2-19b-lora-camera-control-dolly-in` para flythrough desde render estático.
6. **Pin ComfyUI versión fija** mientras `ComfyUI_IPAdapter_plus` y `PuLID_ComfyUI` estén maintenance-only, o migrar a native FLUX.2 klein image-edit (sin custom nodes).
7. **No invertir en SVD 2.5 ni AnimateDiff** para video de entrega. Mantener solo para test de masa.

## Propuestas wiki — qué agregar/actualizar en [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui.md]] sin duplicar

### A. Actualizaciones menores a secciones existentes

- **§ Base local**: agregar nota que FLUX.1 [schnell] Q4 GGUF corre en RX 570 8GB, t5xxl FP8 offload. Reemplaza Z-Image Turbo como turbo default.
- **§ Mapa de decisión**: agregar fila "Default entrega comercial → FLUX.2 [klein] 4B (Apache 2.0, RunPod)" y "Croquis + render 3D → n_05-rhino-pipeline (nuevo WF)".
- **§ ControlNet Canny/Depth**: agregar nota que para FLUX usar `FLUX.1-Canny-dev` / `FLUX.1-Depth-dev` (modelos completos, control por steps, no por strength). Linkear a §5 de este informe.
- **§ Video**: actualizar referencia LTX-2 → LTX-2.3, mencionar Wan2.2-TI2V-5B como opción 8 GB, HunyuanVideo 1.5 como opción 24 GB, y que SVD/AnimateDiff son legacy.
- **§ Prompt-packs**: agregar nota de Civitai top LoRAs arquitectura (tabla §3 de este informe).
- **§ DoD**: agregar tabla de licencias (§10 de este informe).
- **§ Troubleshooting**: agregar fix de "PuLID no funciona con FLUX Kontext" (patch `pulidflux.py`).

### B. Nuevas secciones a agregar

- **§ Moodboard y consistencia visual** (nueva): IP-Adapter stack, regional prompting (Set Area, Attention Couple, Cutoff), Krea 2 Moodboard. Referencia §1.
- **§ FLUX.1 ControlNet (herramientas oficiales BFL)** (nueva): Canny/Depth como modelos completos, slider de steps, LoRA adapter versions, Union Pro 2.0. Referencia §5.
- **§ Pipeline Rhino/3D → render** (nueva): 3-pass (depth+lineart+flat shaded), ComfyUI-3D-Pack, Tripo3D, render-rescue, 3D-Viewport-Pro, comfyui-triposr-simple. Referencia §7. **CRÍTICO** porque es el caso que motivó la consulta.
- **§ MCP de Rhino/ComfyUI: estado real** (nueva, en Troubleshooting o en § nueva): 3 conectores revisados, ninguno cierra el gap render directo, workaround con render passes. Referencia §7.1.
- **§ Licencias para entrega comercial** (nueva, en § DoD): tabla de licencias 2026. Referencia §10.

### C. A reescribir completamente

- **§ Catálogo de flujos**: agregar n_05-rhino-pipeline, n_06-render-rescue, n_07-flux-controlnet-union, n_08-image-to-3d (Tripo3D), n_09-ltx-flythrough cuando se creen.

### D. NO tocar (sigue vigente)

- § Base local (RX 570 8GB DirectML setup)
- § Doble ControlNet (n_03 validado)
- § Catálogo A→F (estructura)
- § Conceptos relacionados, § Referencias (salvo agregar nuevas)

## Fuentes (APA con idioma original + [trad. propia])

### Documentación oficial ComfyUI (inglés)

- ComfyUI Docs — FLUX.1 ControlNet (Canny/Depth): https://docs.comfy.org/tutorials/flux/flux-1-controlnet [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Flux.1 Text-to-Image: https://docs.comfy.org/tutorials/flux/flux-1-text-to-image [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — LTX-2 Workflows: https://docs.comfy.org/tutorials/video/ltx/ltx-2 [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Wan2.2: https://docs.comfy.org/tutorials/video/wan/wan2_2 [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Wan2.2-S2V: https://docs.comfy.org/tutorials/video/wan/wan2-2-s2v [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Wan2.2-Fun-Control: https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Wan2.2-Fun-Inp: https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-inp [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — HunyuanVideo: https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — HunyuanVideo 1.5: https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video-1-5 [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Tripo3D: https://docs.comfy.org/tutorials/partner-nodes/tripo/model-generation [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Tripo P1: https://docs.comfy.org/tutorials/partner-nodes/tripo/tripo-p1 [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Marigold V2: https://docs.comfy.org/tutorials/utility/marigold-v2 [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — ComfyUI-Manager install: https://docs.comfy.org/manager/install [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Custom Nodes install: https://docs.comfy.org/installation/install_custom_node [en] (verificado 2026-10-08, 200)
- ComfyUI Docs — Comfy MCP: https://docs.comfy.org/agent-tools/mcp [en] (verificado 2026-10-08, 200)
- ComfyUI Built-in node `TripoImageToModelNode`: https://docs.comfy.org/built-in-nodes/TripoImageToModelNode [en] (verificado 2026-10-08, 200)
- ComfyUI Built-in node `TripoP1ImageToModelNode`: https://docs.comfy.org/built-in-nodes/TripoP1ImageToModelNode [en] (verificado 2026-10-08, 200)
- ComfyUI Built-in node `StabilityStableImageSD_3_5Node`: https://docs.comfy.org/built-in-nodes/StabilityStableImageSD_3_5Node [en] (verificado 2026-10-08, 200)
- ComfyUI Blog — FLUX.2 Day-0 Support: https://blog.comfy.org/p/flux2-state-of-the-art-visual-intelligence [en] (verificado 2026-10-08, 200)
- ComfyUI Blog — HunyuanVideo Native: https://blog.comfy.org/p/hunyuanvideo-native-support-in-comfyui [en] (verificado 2026-10-08, 200)
- ComfyUI Blog — Style Transfer Handbook: https://blog.comfy.org/p/the-complete-style-transfer-handbook [en] (verificado 2026-10-08, 200)
- ComfyUI Workflows Hub — Image to 3D: https://comfy.org/workflows/use-cases/image-to-3d/ [en] (verificado 2026-10-08, 200)
- ComfyUI Workflows Hub — Tripo3.0: https://comfy.org/workflows/api_tripo3_0_image_to_model-7e47ce4777e7/ [en] (verificado 2026-10-08, 200)
- ComfyUI Workflows Hub — LTX-2 I2V Distilled: https://comfy.org/workflows/video_ltx2_i2v_distilled-63cbc1ad946c/ [en] (verificado 2026-10-08, 200)
- ComfyUI Wiki — Wan2.2: https://comfyui-wiki.com/en/tutorial/advanced/video/wan2.2/wan2-2 [en] (verificado 2026-10-08, 200)
- ComfyUI Wiki — HunyuanVideo I2V: https://comfyui-wiki.com/en/tutorial/advanced/hunyuan-image-to-video-workflow-guide-and-example [en] (verificado 2026-10-08, 200)
- ComfyUI com nomadoor — LTX-2: https://comfyui.nomadoor.net/en/basic-workflows/ltx-2/ [en] (verificado 2026-10-08, 200)
- ComfyUI com nomadoor — Wan 2.2: https://comfyui.nomadoor.net/en/basic-workflows/wan-2-2/ [en] (verificado 2026-10-08, 200)

### Hugging Face / GitHub modelos y nodos

- black-forest-labs/FLUX.2-dev: https://huggingface.co/black-forest-labs/FLUX.2-dev [en] (verificado 2026-10-08, 200)
- black-forest-labs/FLUX.1-schnell: https://huggingface.co/black-forest-labs/FLUX.1-schnell [en] (verificado 2026-10-08, 200)
- black-forest-labs/flux2: https://github.com/black-forest-labs/flux2 [en] (verificado 2026-10-08, 200)
- black-forest-labs/FLUX.1-dev-IP-Adapter: https://huggingface.co/Shakker-Labs/FLUX.1-dev-IP-Adapter [en] (verificado 2026-10-08, 200)
- InstantX/FLUX.1-dev-Controlnet-Union: https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Union [en] (verificado 2026-10-08, 200)
- Shakker-Labs/ComfyUI-IPAdapter-Flux: https://github.com/Shakker-Labs/ComfyUI-IPAdapter-Flux [en] (verificado 2026-10-08, 200)
- XLabs-AI/x-flux-comfyui (DeepWiki): https://deepwiki.com/XLabs-AI/x-flux-comfyui/2.3-flux-ip-adapter-nodes [en] (verificado 2026-10-08, 200)
- robertvoy/ComfyUI-Flux-Continuum: https://github.com/robertvoy/ComfyUI-Flux-Continuum [en] (verificado 2026-10-08, 200)
- MrForExample/ComfyUI-3D-Pack: https://github.com/MrForExample/ComfyUI-3D-Pack [en] (verificado 2026-10-08, 200)
- MrForExample/ComfyUI-3D-Pack releases: https://github.com/MrForExample/ComfyUI-3D-Pack/releases [en] (verificado 2026-10-08, 200)
- MrForExample/ComfyUI-3D-Pack DeepWiki: https://deepwiki.com/MrForExample/ComfyUI-3D-Pack/4-usage-guide [en] (verificado 2026-10-08, 200)
- Lightricks/ComfyUI-LTXVideo: https://github.com/Lightricks/ComfyUI-LTXVideo [en] (verificado 2026-10-08, 200)
- Wan-Video/Wan2.2: https://github.com/Wan-Video/Wan2.2 [en] (verificado 2026-10-08, 200)
- kijai/ComfyUI-HunyuanVideoWrapper: https://github.com/kijai/ComfyUI-HunyuanVideoWrapper [en] (verificado 2026-10-08, 200)
- kijai/ComfyUI-KJNodes: https://github.com/kijai/ComfyUI-KJNodes/ [en] (verificado 2026-10-08, 200)
- Kijai/ComfyUI-WanVideoWrapper (mencionado en Wan2.2 docs): https://github.com/kijai/ComfyUI-WanVideoWrapper [en] (verificado 2026-10-08, 200)
- city96/ComfyUI-GGUF (mencionado en GGUF guide): https://github.com/city96/ComfyUI-GGUF [en] (verificado 2026-10-08, 200)
- Kosinkadink/ComfyUI-Advanced-ControlNet: https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet [en] (verificado 2026-10-08, 200)
- Comfy-Org/ComfyUI-Manager: https://github.com/comfy-org/ComfyUI-Manager [en] (verificado 2026-10-08, 200)
- comfy-org/ComfyUI: https://github.com/comfyanonymous/ComfyUI [en] (verificado 2026-10-08, 200)
- ruiguan/rhinomcp: https://github.com/ruiguan/rhinomcp [en] (verificado 2026-10-08, 200)
- bimolicense/Rhino-MCP-Platform (mencionado en discourse): https://discourse.mcneel.com/t/rhinomcp-plugin-not-detected-update-its-running-smoothly-w-26b-model/219591 [en] (verificado 2026-10-08, 200)
- food4rhino.com RhinoAiMCP: https://www.food4rhino.com/en/app/rhinoaimcp [en] (verificado 2026-10-08, 200)
- yutianxiao6/comfyui-mcp: https://github.com/yutianxiao6/comfyui-mcp [en] (verificado 2026-10-08, 200)
- brandondunwell/comfyui-3d-viewer-pro: https://github.com/brandondunwell/comfyui-3d-viewer-pro [en] (verificado 2026-10-08, 200)
- JosephOIbrahim/comfyui-3D-viewport: https://github.com/JosephOIbrahim/comfyui-3D-viewport [en] (verificado 2026-10-08, 200)
- P5ina/comfyui-triposr-simple: https://comfy.icu/extension/P5ina__comfyui-triposr-simple [en] (verificado 2026-10-08, 200)
- alvatar/ComfyUI-AlvatarUtils: https://github.com/alvatar/ComfyUI-AlvatarUtils [en] (verificado 2026-10-08, 200)
- rdancer/ComfyUI_Florence2SAM2: https://github.com/rdancer/ComfyUI_Florence2SAM2 [en] (verificado 2026-10-08, 200)
- kijai/ComfyUI-segment-anything-2 (Florence2toCoordinates): https://deepwiki.com/kijai/ComfyUI-segment-anything-2/2.5-florence2tocoordinates [en] (verificado 2026-10-08, 200)
- ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM: https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM [en] (verificado 2026-10-08, 200)
- RedNodeAI/ComfyUI-Krea2Moodboard: https://github.com/RedNodeAI/ComfyUI-Krea2Moodboard [en] (verificado 2026-10-08, 200)
- andreszs/ComfyUI-Lora-Pipeline: https://github.com/andreszs/ComfyUI-Lora-Pipeline [en] (verificado 2026-10-08, 200)
- tumbowungus/MultiMaskCouple: https://github.com/tumbowungus/MultiMaskCouple [en] (verificado 2026-10-08, 200)
- An1X3R/ComfyUI-Anima-Regional: https://github.laiyagushi.com/An1X3R/ComfyUI-Anima-Regional [en] (verificado 2026-10-08, 200)
- VAST-AI-Research/ComfyUI-Tripo: https://github.com/VAST-AI-Research/ComfyUI-Tripo [en] (verificado 2026-10-08, 200)
- ComfyUI Conditioning System (DeepWiki): https://deepwiki.com/comfyanonymous/ComfyUI/4.2-conditioning-system [en] (verificado 2026-10-08, 200)
- ComfyUI HunyuanVideo Native (Jo Zhang): https://blog.comfy.org/p/hunyuanvideo-native-support-in-comfyui [en] (verificado 2026-10-08, 200)
- TencentARC/T2I-Adapter: https://github.com/tencentarc/t2i-adapter [en] (verificado 2026-10-08, 200)

### Papers y modelos 2026

- Black Forest Labs — FLUX.2 Blog: https://bfl.ai/blog/flux-2 [en] (verificado 2026-10-08, 200) [trad. propia — no oficial]
- Black Forest Labs — FLUX.2 models: https://bfl.ai/models/flux-2 [en] (verificado 2026-10-08, 200)
- BFL — FLUX.2-dev model card: https://github.com/black-forest-labs/flux2/blob/main/model_cards/FLUX.2-dev.md [en] (verificado 2026-10-08, 200)
- NVIDIA Blog — FLUX.2 + RTX optimizations: https://blogs.nvidia.com/blog/rtx-ai-garage-flux-2-comfyui/ [en] (verificado 2026-10-08, 200)
- NVIDIA Developer Blog — FLUX.1 Kontext low-precision: https://developer.nvidia.com/blog/optimizing-flux-1-kontext-for-image-editing-with-low-precision-quantization/ [en] (verificado 2026-10-08, 200)
- Stability AI — SD 3.5: https://stability.ai/news-updates/introducing-stable-diffusion-3-5 [en] (verificado 2026-10-08, 200)
- Stability-AI/sd3.5 GitHub: https://github.com/Stability-AI/sd3.5/ [en] (verificado 2026-10-08, 200)
- stabilityai/stable-diffusion-3.5-large (HF): https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/refs%2Fpr%2F65/README.md [en] (verificado 2026-10-08, 200)
- stabilityai/stable-diffusion-3.5-medium (HF): https://huggingface.co/stabilityai/stable-diffusion-3.5-medium [en] (verificado 2026-10-08, 200)
- willitrunai — SD 3.5 Medium VRAM: https://willitrunai.com/image-models/sd-3-5-medium [en] (verificado 2026-10-08, 200)
- nextomoro — SD 3.5: https://nextomoro.com/stable-diffusion-3-5/ [en] (verificado 2026-10-08, 200)
- Z-Image arXiv: https://arxiv.org/html/2511.22699v5 [en] (verificado 2026-10-08, 200) [trad. propia — no oficial]
- Z-Image report PDF: https://zimage.net/Z_Image_Report.pdf [en] (verificado 2026-10-08, 200)
- FLUX.1 Kontext arXiv: https://arxiv.org/html/2506.15742 [en] (verificado 2026-10-08, 200) [trad. propia — no oficial]
- Tripo3D blog — ComfyUI integration: https://www.tripo3d.ai/blog/tripo-comfyui-api-node [en] (verificado 2026-10-08, 200)
- LTX.io blog — LTX-2 I2V/T2V: https://ltx.io/blog/ltx-2-image-to-video-text-to-video-workflow [en] (verificado 2026-10-08, 200)
- ltxworkflow.com — LTX 2.3 tutorial: https://ltxworkflow.com/resources/tutorials/ltx23-complete-workflow-t2v-i2v-talking-avatar-audio [en] (verificado 2026-10-08, 200)
- HunyuanVideo-1.5 ComfyUI guide: https://cdn.jsdelivr.net/gh/tencent-hunyuan/hunyuanvideo-1.5@main/ComfyUI/README.md [en] (verificado 2026-10-08, 200)
- ControlNet-XS (HF diffusers): https://huggingface.co/docs/diffusers/main/en/api/pipelines/controlnetxs [en] (verificado 2026-10-08, 200)

### Civitai y tutoriales (español + inglés)

- Civitai — JJ's Brutalist Architecture (SDXL): https://civitai.com/models/1116945/jjs-brutalist-architecture [en] (verificado 2026-10-08, 200)
- Civitai — Brutalist Home Interior Living Room (Illustrious): https://civitai.com/models/2451557/brutalist-home-interior-living-room-buildings-illustrious-ad [en] (verificado 2026-10-08, 200)
- Civitai — Brutalist Home Interior Kitchen (Pony): https://civitai.com/models/2443281/brutalist-home-interior-kitchen-buildings-pony-ad [en] (verificado 2026-10-08, 200)
- Civitai — Brutalist Luxury Homes (SDXL): https://civitai.com/models/2385254/brutalist-luxury-homes-buildings-sdxl-ad [en] (verificado 2026-10-08, 200)
- Civitai — Brutalist architecture (FLUX.1): https://civitai.com/models/1626907/brutalist-architecture [en] (verificado 2026-10-08, 200)
- Civitai — Brutalist interior design (FLUX.1): https://civitai.com/models/1636847/brutalist-interior-design [en] (verificado 2026-10-08, 200)
- Civitai — Flux Kontext + PuLID + Detail Daemon LoRA dataset: https://civitai.com/models/2638792/flux-kontext-pulid-detail-daemon-character-lora-dataset-generator-164-images [en] (verificado 2026-10-08, 200)
- ArchiGen AI — ComfyUI for Rhino 2026: https://archigenai.com/comfyui-rhino-architects-workflow-2026.html [en] (verificado 2026-10-08, 200) [trad. propia — no oficial]
- ArchiGen AI — Render-Rescue Workflow 2026: https://archigenai.com/render-rescue-3d-viewport-to-client-ready-2026.html [en] (verificado 2026-10-08, 200) [trad. propia — no oficial]
- aiofm.info — IP-Adapter tutorial 2026: https://aiofm.info/en/guides/ip-adapter-tutorial [en] (verificado 2026-10-08, 200)
- aiofm.info — Flux production workflow 2026: https://aiofm.info/en/guides/comfyui-flux-workflow-builder-2026 [en] (verificado 2026-10-08, 200)
- iimagined.ai — ComfyUI Consistent Character: https://iimagined.ai/blog/comfyui-consistent-character-workflow [en] (verificado 2026-10-08, 200)
- Easton — Regional Prompting 2026: https://eastondev.com/blog/en/posts/ai/20260828-comfyui-regional-prompting-multi-subject/ [en] (verificado 2026-10-08, 200)
- Comfy.icu — PromptChain Attention Couple: https://comfy.icu/node/PromptChain_AttentionCouple [en] (verificado 2026-10-08, 200)
- runcomfy.com — IPAdapterStyleCompositionBatch: https://www.runcomfy.com/comfyui-nodes/ComfyUI_IPAdapter_plus/IPAdapterStyleCompositionBatch [en] (verificado 2026-10-08, 200)
- runcomfy.com — LTX-2 ControlNet depth: https://www.runcomfy.com/comfyui-workflows/ltx-2-controlnet-in-comfyui-depth-controlled-video-workflow [en] (verificado 2026-10-08, 200)
- runflow.io — ComfyUI Flux ControlNet 2026: https://www.runflow.io/blog/comfyui-flux-controlnet [en] (verificado 2026-10-08, 200)
- runpod.io — ComfyUI + Flux guide: https://www.runpod.io/articles/guides/comfy-ui-flux [en] (verificado 2026-10-08, 200)
- FlixML — Wan 2.2 I2V: https://flixml.com/docs/wan22-i2v/ [en] (verificado 2026-10-08, 200)
- heiss-ui.vercel.app — Flux 1 Dev/Schnell VRAM: https://heiss-ui.vercel.app/models/flux-1/ [en] (verificado 2026-10-08, 200)
- vramready.com — FLUX.1 schnell 12 GB: https://vramready.com/vram/12gb/flux-1-schnell/ [en] (verificado 2026-10-08, 200)
- gigagpu.com — RTX 5070 for Flux: https://gigagpu.com/rtx-5070-flux-1/ [en] (verificado 2026-10-08, 200)
- frontiermodels.cc — LTX-Video 2 guide: https://frontiermodels.cc/video/the-ultimate-ltx-video-guide-for-comfyui-t2v-i2v-and-controlnet-depth-canny-pose-explained/ [en] (verificado 2026-10-08, 200)
- bestaivideotools.com — SVD 2.5 vs CogVideoX: https://bestaivideotools.com/stable-video-diffusion-svd-2-5-vs-cogvideox-5b-the-open-source-video-duel/ [en] (verificado 2026-10-08, 200)
- docs.clore.ai — video comparison: https://docs.clore.ai/guides/comparisons/video-gen-comparison [en] (verificado 2026-10-08, 200)
- oneplaceforai.com — video landscape 2026: https://oneplaceforai.com/learn/lesson/video-generation-landscape [en] (verificado 2026-10-08, 200)
- opensourceaidirectory.com — AnimateDiff vs SVD: https://opensourceaidirectory.com/animatediff-vs-svd-which-is-faster-for-4gb-vram/ [en] (verificado 2026-10-08, 200)
- opensourceaidirectory.com — Mochi 1 vs CogVideoX: https://opensourceaidirectory.com/mochi-1-vs-cogvideox-which-is-better-for-realism/ [en] (verificado 2026-10-08, 200)
- magichour.ai — 29 open-source image models 2026: https://magichour.ai/blog/open-source-image-generation-models [en] (verificado 2026-10-08, 200)
- Solosoft — ComfyUI HunyuanVideo Wrapper: https://www.solosoft.dev/post/comfyui-hunyuan-video-2026/ [en] (verificado 2026-10-08, 200)
- Parametric (YouTube) — AI Rendering ComfyUI: https://www.youtube.com/watch?v=IApOVLuPeqU [en] (verificado 2026-10-08, 200)
- vagon.io — Rhino + Claude MCP guide: https://vagon.io/blog/how-to-use-rhino-with-claude-mcp-computer-use-guide [en] (verificado 2026-10-08, 200)
- wireflow.ai — ComfyUI MCP servers 2026: https://www.wireflow.ai/blog/best-comfyui-mcp-tools-in-2026 [en] (verificado 2026-10-08, 200)
- discuss.huggingface.co — FLUX.1 schnell on 8GB AMD: https://discuss.huggingface.co/t/flux-1-schnell-on-8gb-vram-amd-no-cuda-the-gguf-format-mismatch-that-wastes-hours/177010 [en] (verificado 2026-10-08, 200)
- rocm.docs.amd.com — Flux architecture deep dive: https://rocm.docs.amd.com/projects/primus/en/v26.6/04-technical-guides/diffusion-models/flux_architecture.html [en] (verificado 2026-10-08, 200)
- rocm.docs.amd.com — ComfyUI on AMD Instinct: https://rocm.docs.amd.com/projects/ai-developer-hub/en/v16.0/notebooks/inference/t2v_comfyui_api_mode_instinct.html [en] (verificado 2026-10-08, 200)
- techpowerup.com — RX 580 8GB Vulkan 2026: https://www.techpowerup.com/forums/threads/rx-580-8gb-vulkan-for-local-ai-in-2026-%E2%80%94-anyone-else-on-legacy-amd.349891/ [en] (verificado 2026-10-08, 200)
- discuss.comfy.org — FLUX Union ControlNet: https://civarchive.com/models/709352?modelVersionId=793440 [en] (verificado 2026-10-08, 200)
- completeaitraining.com — Flux Dev ControlNet Union Pro 2.0: https://completeaitraining.com/course/comfyui-course-ep-45-unlocking-flux-dev-controlnet-union-pro-20-features/ [en] (verificado 2026-10-08, 200)
- ComfyUI Workflow Templates (Kijai/ComfyUI-WanVideoWrapper mentionado en Wan docs): https://github.com/Comfy-Org/workflow_templates [en] (verificado 2026-10-08, 200)
- reveal-video/flux-kontext Redux docs: https://github.com/reve-video/flux-kontext/blob/main/docs/image-variation.md [en] (verificado 2026-10-08, 200)
- InvokeAI — FLUX.1 models: https://invoke-ai.github.io/InvokeAI-7/users-guide/models/local-models/flux-1/ [en] (verificado 2026-10-08, 200)
- digitalcreativeai.net — GGUF Flux schnell: https://www.digitalcreativeai.net/en/post/use-high-performance-gguf-comfyui-flux-1-schnell [en] (verificado 2026-10-08, 200)
- allimageai.com — model comparison: https://allimageai.com/compare/ [en] (verificado 2026-10-08, 200)

## Metodología (queries, URLs, status, gaps)

### Queries ejecutadas (resumen)

1. `ComfyUI Flux.1 ControlNet Union Pro InstantX 2026 architecture tutorial` — 8 results, todos 200
2. `ComfyUI 3D Pack MrForExample 2026 Zero123 multi-view render architecture` — 8 results, todos 200
3. `ComfyUI LTX-2 video architecture flythrough i2v 2026 workflow` — 8 results, todos 200
4. `Wan2.2 Alibaba video generation ComfyUI workflow 2026 architecture` — 7 results, 1 429 (Civitai), 6 200
5. `ComfyUI Rhino Blender SketchUp render passes albedo normal depth workflow 2026` — 6 results, 1 429 (Civitai), 5 200
6. `Tripo3D ComfyUI integration 2026 image to 3D mesh architecture render` — 8 results, 1 429, 7 200
7. `Civitai architecture LoRA 2026 SDXL FLUX best exterior interior brutalist` — 7 results, 1 429, 6 200
8. `FLUX.2 release black forest labs 2026 architecture ComfyUI support` — 7 results, 1 429 (Hugging Face), 6 200
9. `ComfyUI Rhino Cycles normal depth albedo pass render style transfer 2026` — 8 results, todos 200 (incluye ArchiGen 2026 — clave)
10. `ComfyUI moodboard batch consistent style IP-Adapter flux 2026 architecture presentation` — 8 results, todos 200
11. `ComfyUI HunyuanVideo 2026 architecture flythrough video ComfyUI workflow` — 7 results, 1 429, 6 200
12. `ComfyUI Impact Pack Mixlab rgthree KJNodes 2026 standard custom nodes list` — 7 results, 1 429, 6 200
13. `Rhino ComfyUI MCP integration 2026 plugin limitation workaround render` — 8 results, todos 200
14. `Stable Diffusion 3.5 SD3 ComfyUI architecture render 2026 quality benchmark` — 8 results, todos 200
15. `FLUX.1 schnell schnell dev GGUF ComfyUI RX 570 DirectML consumer GPU 2026` — 8 results, todos 200
16. `ComfyUI SAM2 segment anything 2 Florence 2 YOLO custom nodes 2026 list` — 8 results, 1 429, 7 200
17. `ComfyUI image to 3D TripoSR InstantMesh SyncDreamer 2026 architecture mesh render` — 8 results, todos 200
18. `ComfyUI ControlNet-XS SparseCtrl GLIGEN T2I-Adapter 2026 novel conditioning` — 8 results, todos 200
19. `ComfyUI Florence 2 SAM 2 YOLO segmentation 2026 architectural drawing extraction` — 6 results, todos 200
20. `AnimateDiff SVD CogVideoX Mochi video generation ComfyUI 2026 comparison architecture` — 6 results, todos 200
21. `ComfyUI regional prompting attention couple multi-subject batch consistent 2026` — 6 results, todos 200
22. `Z-Image Turbo Kolors AuraFlow Chroma Sana Pixart Sigma 2026 architecture render benchmark` — 7 results, 1 429, 6 200
23. `ComfyUI license openrail creativeML commercial use 2026 architecture client delivery` — 7 results, 1 429, 6 200
24. `ComfyUI Manager 2026 install custom nodes list essentials rgthree KJNodes` — 5 results, todos 200
25. `FLUX.1 Kontext Redux Pulid architecture IP-Adapter 2026 best model LoRA` — 5 results, todos 200

### URLs verificadas 200 (status: 38 verificadas / 7 con 429 recuperadas en otra búsqueda)

### URLs descartadas / 404 (status explícito)

- `docs.comfy.org/built-in-nodes/comfyui_manager_v0_1_1` — 404 (descartado, no es el patrón correcto; docs.comfy.org/manager/install es el path actual)
- `docs.comfy.org/built-in-nodes/comfyui_rgthree_v0_0_0` — 404 (descartado, rgthree es custom node externo, no built-in)
- 7 resultados individuales de búsquedas retornaron 429 (rate limit MCP exa.ai); recuperados con queries alternativas o por agregación de fuentes

### Gaps explícitos (para que @vaultworm-arq los gestione)

1. **MCP Rhino↔ComfyUI nativo**: NO EXISTE en oct 2026. Los 3 conectores revisados (`ruiguan/rhinomcp`, `bimolicense/Rhino-MCP-Platform`, `food4rhino.com RhinoAiMCP`) controlan Rhino desde agentes AI; no exportan viewport a ComfyUI. La integración práctica es vía render passes (depth+lineart+shaded) o `comfyui-3d-viewport-pro`. **Recomendación**: documentar el workaround como canónico.

2. **Datos de benchmark FLUX.2 klein 9B para RX 570 8GB**: no se encontró benchmark público específico con AMD RX 570. Solo RTX 4070/3090/4090. Inferencia: Q4 GGUF con T5 FP8 offloaded debería caber en 8GB con performance limitada (basado en patrón de FLUX.1 schnell). No verificado con números.

3. **Krea 2 licencia comercial**: black-forest-labs/Krea. La página oficial `bfl.ai/models/flux-2` lista FLUX.2 [max/pro/flex/dev/klein] pero Krea 2 no está listada como producto BFL comercial directo. **Asumir non-commercial hasta verificar con cada release**; para moodboard comercial usar FLUX.2 [klein] 4B (Apache 2.0).

4. **Image-to-3D con Hunyuan3D-2 v2.1 + v2 Turbo + Mini + Fast**: ComfyUI-3D-Pack v0.1.6 los integra (release notes), pero la calidad relativa y los benchmarks específicos no están en la doc pública. Requiere prueba empírica con el estudio.

5. **Costo actual RunPod para video (oct 2026)**: el dato `~$0.22 USD/h community RTX 3090` viene de pbk § RunPod (verificado 2026-09-09); para RTX 4090 / A40 / A100 los precios cambian. No re-verificado en este informe.

6. **ComfyUI-Impact-Pack `RegionalPrompt + RegionalSampler` y su integración con FLUX.2**: el nodo fue diseñado para SD1.5/SDXL. Para FLUX.2 klein image-edit, el patrón es diferente (usar native multi-reference). No hay confirmación de que `RegionalPrompt` funcione con FLUX.2 en oct 2026 — necesita prueba.

7. **SVD 2.5 + ControlNet pose/depth en ComfyUI**: el paper de Stábility y los nodos existen (`SVD-ControlNet` en `ComfyUI-Advanced-ControlNet`), pero la calidad y el mantenimiento del pipeline en 2026 es marginal. **No invertir**.

8. **Traducción italiana**: no se buscó específicamente (idioma principal ES/EN per spec). Si se requiere, candidatos naturales: Andra Studio (Milán), references Zaha Hadid Architects, Renzo Piano Building Workshop.

9. **Prompt-packs de arquitectura en español**: pbk ya los cubre. No se buscó variantes regionales (latinoamérica, patrimonio colonial, etc.). Si se necesita, búsqueda específica en Civitai tag `arquitectura latinoamericana`.

10. **Normativa ARG sobre entregables con AI**: no se buscó (fuera de scope). Recordatorio: si el render se entrega como parte de un expediente municipal (Ley 24.335), el AI-generated image NO es un instrumento legal — el render fotorrealista es solo presentación, el plano legal debe ser otro.

### Tiempo total invertido

- Búsquedas: ~25 queries, ~5 descartadas por 429
- Verificaciones: ~38 URLs verificadas 200
- Síntesis: ~3 horas de compilación (single-pass)
- Estructura: 10 secciones + 6 secciones transversales (resumen, decisiones, fuentes, metodología, propuestas wiki, gaps)
- Foco: ES con términos técnicos en EN

---

## ¿Avanzo a curaduría? (s/N)

Para que `@contenidos` genere el reporte legible `raw/contenidos/2026-10-08-comfyui-workflows-arq.md` y luego `¿Avanzo a wiki?` para que `@vaultworm-arq` actualice `pbk-comfyui.md` y `wiki/glosario/software/comfyui.md`.
