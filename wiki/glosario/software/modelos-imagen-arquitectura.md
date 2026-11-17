---
tipo: software
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-16
tags: [glosario, software, imagen-ia, arquitectura, flux, qwen, nano-banana, seedream, flujos-nativos]
idioma: es
---

# Modelos imagen arquitectura

Guía viva para elegir motor de imagen en el estudio, desde exploración veloz hacia entrega cuidada. **SDXL deja de ser base**: queda como ecosistema (ControlNet + LoRAs legacy). Base abierta nueva: FLUX 3 Image Klein / klein 4B.

- [[#Resumen]]
- [[#Mejor cerrado]]
- [[#Mejor abierto]]
- [[#Mejor para arquitectura]]
- [[#Flux y Flux 2 y Flux 3]]
- [[#LoRA para arquitectura]]
- [[#Decisiones para el estudio]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Resumen

Panorama 2026-11-03: liderazgo cerrado en `GPT Image 2.5 Sunburst` + `Nano Banana 2.1`, liderazgo abierto en calidad en `Qwen-Image-2.1`, liderazgo abierto permisivo en `Z-Image-Turbo`, `Qwen-Image-2512` y `FLUX.2 klein 4B`. Para arquitectura, `Nano Banana Pro` lidera exteriores y `FLUX.2 Pro` lidera interiores con valor destacado. LoRA queda como capa opcional de estilo propio; ControlNet + fotos de referencia resuelven identidad de lugar.

## Mejor cerrado

Arena texto-imagen octubre 2026:

| Puesto | Modelo | Elo | Punto fuerte |
|---|---|---|---|
| 1 | `GPT Image 2.5 Sunburst` | 1424.6 / 1466 texto | instrucción + edición + texto |
| 2 | `GPT Image 2.5 Flare` | 1397.6 / 1435 texto | velocidad diaria |
| 3 | `GPT Image 2 medium` | 1383.0 / 1423 texto | equilibrio |
| 4 | `MAI-Image-2.6` | 1332.1 / 1365 texto | fotorrealismo |
| 5 | `Nano Banana 2.1` | 1327.8 / 1361 texto | grounding + 14 refs |

`Nano Banana 2.1` integra conocimiento amplio, 1K/2K/4K, 14 imágenes de referencia, búsqueda web + imagen, marca SynthID. Ideal para iteración rápida con base real. `GPT Image 2.5` destaca en póster con texto exacto y edición por máscara multi-turno. `Seedream 5.0 Pro` ganó 6 de 8 pruebas Rangy por juicio contextual. Todos operan vía API, con licencia comercial incluida en planes pagos.

## Mejor abierto

| Modelo | Calidad | Licencia | VRAM | Uso sugerido |
|---|---|---|---|---|
| `Qwen-Image-2.1` 7B | top open Arena 1222.9 | Qwen Research, uso investigación, comercial vía acuerdo | 16 GB INT8 | máxima calidad abierta, edición 10 refs, RGBA |
| `FLUX 3 Image Klein` 5.6B | +91 Elo T2I vs Klein 9B en eval interna | Kommunity, comercial libre hasta $5M revenue | 8 GB INT8, 11.2 GB BF16 | 8 GB GPU, 4K nativo, 10 refs, 4 s RTX 5090 / 9 s RTX 4070 |
| `Z-Image-Turbo` | veloz, nítido | Apache 2.0 | liviano | throughput + comercial pleno |
| `Qwen-Image-2512` | tipografía sólida | Apache 2.0 | 24 GB | texto + infografía comercial |
| `FLUX.2 klein 4B` | interactivo | Apache 2.0 | bajo | tiempo real + comercial pleno |
| `SDXL 1.0` | ecosistema | OpenRAIL permisiva | 8-12 GB | ControlNet + miles de LoRAs |

`Qwen-Image-2.1 Turbo` genera y edita en 8 pasos. `ComfyUI` ofrece soporte día cero vía `Comfy-Org/Qwen-Image-2.1`, `Diffusers` vía `QwenImage21Pipeline`, `vLLM-Omni` y `SGLang` para serving. `FLUX 3 Klein` incluye base para fine-tuning + destilado para latencia, FP8/INT8/NVFP4, entrenamiento LoRA con AI-Toolkit desde día uno.

## Mejor para arquitectura

| Ranking | Modelo | Score | Costo | Lectura |
|---|---|---|---|---|
| LLM Stats arquitectura #1 | `Gemini 2.5 Flash Image` | 2418 en 514 ciegas | medio | punto de partida sólido para concepto |
| VibeDex archviz #1 | `Nano Banana Pro` | 4.62 | $0.138 | cutaways + interiores época |
| VibeDex archviz #2 | `FLUX.2 Pro` | 4.53 | $0.035 | cantilever + detalle ingenieril + exterior |
| VibeDex interior #1 | `FLUX.2 Pro` | 4.59 | $0.035 | física material + espacialidad |
| VibeDex valor | `Qwen 2512` | 94% del top | $0.003 | 46 renders por 1 NBP |

Patrón de uso: `Midjourney V8.2` para mood, `Nano Banana` para sketch-to-render económico, `GPT 2.5` para edit con máscara, `FLUX + ControlNet` para control total en `[[wiki/glosario/software/comfyui|ComfyUI]]`. Para geometría fiel, `SDXL + ControlNet M-LSD` sostiene líneas de planta y massing.

## Flux y Flux 2 y Flux 3

Linaje Black Forest Labs:

- `FLUX.1 schnell / dev` 12B: base 2024, `schnell` Apache 2.0 veloz, `dev` referencia calidad con uso comunitario.
- `FLUX.1.1 pro`: adherencia fina, dimensiones precisas, múltiplos de 32 (usar 1280x704).
- `FLUX.1 kontext pro/max`: edición por instrucción, preserva identidad.
- `FLUX.2 klein 4B/9B`, `dev 32B`, `pro/flex/max`: salto en fotorrealismo y edición 4MP + 10 refs. `klein 4B` único Apache 2.0 puro de la familia.
- `FLUX 3 Image Klein` 5.6B + `FLUX 3 Image`: 4K nativo, pixel-perfect edit, bounding boxes, encoder Qwen3-VL-4B. En Pollinations: `flux` = `flux.1-schnell` 0.002 Pollen para explorar, `flux.1.1-pro` 0.03 para lámina, `kontext` 0.03 para editar con foto, `klein` 0.005 para interactivo.

Competencia abierta: `Qwen-Image`, `Z-Image`, `Krea 2`, `MOSS-Image`, `HunyuanImage 3.0 80B MoE`, `HiDream`, `Wan`. Competencia cerrada: `GPT Image`, `Nano Banana`, `Seedream`, `MAI-Image`, `Muse`, `Reve`, `Grok Imagine`, `Ideogram`, `Recraft` vectores, `Midjourney` arte.

## Flujos nativos por modelo — qué ya sabe hacer de base (verificado 2026-11-16)

Sin ControlNet ni nodos: lo que el modelo trae de fábrica. Fuentes: [BFL FLUX 3 Klein](https://docs.bfl.ai/flux_3/flux3_image_klein) (edit+10 refs+bbox+LoRA, verificado hoy) + [OpenRouter Seedream 5.0 Pro](https://openrouter.ai/bytedance-seed/seedream-5-0-pro) (14 refs+seed+aspecto, verificado hoy) + catálogos vivos Pollinations/OpenRouter.

| Modelo | txt2img | Edit instrucción | Multi-ref | Máscara inpaint | Outpaint | Layout bbox | Texto exacto | 4K / upscale | Cámara | LoRA propio | Licencia |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **FLUX 3 Image Klein** 5.6B | ✅ +upsampler | ✅ | 10 refs | vía Kontext/Fill | vía Expand | ✅ | ✅ | ✅ 4K nativo | por instrucción+ref | ✅ Base rank 32, ~4.5 h 1 GPU | Kommunity (<$5M) |
| **klein 4B** | ✅ | ✅ | hasta 10 refs | vía Kontext | — | — | ✅ | 1 MP | por instrucción+ref | ✅ ai-toolkit | **Apache 2.0** |
| Kontext pro/max | ✅ | ✅ identidad | ✅ | ✅ Fill + erase | ✅ Expand | — | ✅ | — | conserva toma | ❌ | API comercial |
| **Seedream 5.0 Pro** | ✅ | ✅ 14 refs (OR) | 14 | — | — | — | ✅ | 1K/2K | por instrucción+ref | ❌ | API comercial |
| **NanoBanana 2/2.1** | ✅ | ✅ 14 refs | 14 | — | — | — | ✅ | 1K/2K/4K + SynthID | por instrucción+ref | ❌ | API comercial |
| **GPT-image 2.5/2.6** sunburst | ✅ | ✅ multi-turno | ✅ | ✅ máscara | — | — | ✅ top | — | por instrucción+ref | ❌ | API comercial |
| Ideogram v4 | ✅ esquemas | ✅ | — | — | — | — | ✅ | — | — | ❌ | API comercial |
| Qwen-Image-2.1 7B | ✅ Turbo 8 pasos | ✅ 10 refs | 10 + RGBA | — | — | — | ✅ | — | — | ✅ | research (comercial vía acuerdo) |
| Z-Image-Turbo | ✅ veloz | — | — | — | — | — | — | — | — | ✅ | **Apache 2.0** |
| SDXL 1.0 | ✅ | vía img2img | vía IPAdapter | vía nodos | vía nodos | vía CN | débil | vía upscaler | vía ControlNet | ✅ miles | OpenRAIL (ecosistema) |

Lectura: **cámara y layout paramétricos no existen en ningún modelo** (solo bbox en FLUX 3 + instrucción con referencia). Inpaint/outpaint con máscara dibujada = Kontext/Fill/Expand o Comfy. Todo lo demás (estación, hora, material, vano, textura) ya es edición por instrucción: no justifica flujo propio.

## Base mejor que XL — pesos abiertos (orden del estudio)

1. **FLUX 3 Image Klein** 5.6B: mejor calidad abierta usable (Kommunity, 4K, bbox, LoRA). Pide 24 GB en BF16, INT8 en 8 GB, pod para entrenar.
2. **klein 4B**: Apache 2.0 pleno, interactivo, LoRA barato. El que escala al hardware del estudio.
3. **Qwen-Image-2.1**: top calidad cruda, edición 10 refs + RGBA; licencia research (mirar, no cliente).
4. **Z-Image-Turbo**: throughput Apache 2.0, volumen barato.
5. SDXL: relegado a ecosistema (sus ControlNet/LoRAs se reutilizan, no se entrena nada nuevo encima).

Novedad: `seedream-5-5` en catálogo (sucesor del 5.0) y `FLUX.2` como familia de transición — evaluar antes de fijar defaults.

## LoRA para arquitectura

LoRA aporta estilo propio y consistencia de serie; identidad de lugar avanza también con referencias + ControlNet.

- Cerrados (`GPT`, `Nano Banana`, `Seedream`, `FLUX Pro API`): trabajan con refs (hasta 14-16) + grounding, LoRA queda fuera del flujo.
- Abiertos (`SDXL`, `FLUX.1`, `FLUX.2`, `Qwen`): LoRA útil para lenguaje propio del estudio y para Sagrada Família, donde repositorio público ofrece material genérico y queda oportunidad de dataset propio 15-40 fotos + trigger + rank 16.
- `SDXL` incluye biblioteca amplia de LoRAs interior/exterior + ControlNet profundo; `FLUX.1` en crecimiento; `FLUX.2/Qwen` con catálogo joven.
- Prioridad para concurso: `ControlNet M-LSD` para líneas, `Depth` para masa, `IC-Light` para reiluminar, luego LoRA propio según backlog `[[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/30-backlog-futuras-pruebas|30-backlog-futuras-pruebas]]`.

Flujo estudio con RX 570 8 GB: `[[wiki/glosario/software/pollinations|Pollinations]]` `flux` para abrir abanico, `flux.1.1-pro` para cerrar lámina, `kontext` con foto real para anclar sitio, `[[wiki/glosario/software/comfyui|ComfyUI]]` `SDXL` local para control geométrico.

## Decisiones para el estudio

- Base abierta (ya no XL): **FLUX 3 Image Klein** (calidad, 4K, bbox, LoRA Base) + **klein 4B** (Apache 2.0, interactivo, LoRA barato). SDXL queda solo como ecosistema legacy.
- Exploración diaria: `flux.1-schnell` vía `[[wiki/glosario/software/pollinations|Pollinations]]` + `[[wiki/glosario/software/n8n|n8n]]` + `[[wiki/glosario/software/telegram|Telegram]]`.
- Lámina cuidada: `flux.1.1-pro` 1280x704 seed fijo.
- Identidad Sagrada: foto real + `kontext`, 3-8 refs.
- Entrega con grounding: `Nano Banana Pro` 2K, final 4K.
- Edición quirúrgica texto/máscara: `GPT Image 2.5 Sunburst`.
- Valor masivo: `Qwen 2512` / `z-image-turbo`.
- Salto local futuro: `FLUX 3 Klein INT8` en 8 GB, `Qwen-2512` Apache 2.0 para tipografía.

## Documentación oficial por modelo (verificada 2026-11-12)

Regla del estudio: cada modelo enlaza su documentación canónica (BFL docs + tutorial Comfy + pesos HF). Índice maestro: índice oficial BFL.

| Modelo | Doc principal | API / ComfyUI / Pesos | Guías |
|---|---|---|---|
| **FLUX 3 Image Klein** | [BFL docs](https://docs.bfl.ai/flux_3/flux3_image_klein) (200: specs, upsampler obligatorio, LoRA rank 32) | [API ref](https://docs.bfl.ai/api-reference/utility/generate-an-image-with-flux-3-klein) · [LoRA guide](https://docs.bfl.ai/flux_3/flux3_image_klein_lora_guide) · [Comfy tutorial](https://docs.comfy.org/tutorials/flux/flux-3-klein) (200: workflows JSON, int8, `<ref_image_N>`) · [Pesos Comfy HF](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) | [Prompting summary](https://docs.bfl.ai/guides/prompting_summary) · [Multi-ref editing](https://docs.bfl.ai/guides/prompting_editing_multi_reference) |
| **FLUX.2 klein 4B/9B** | [API 4B](https://docs.bfl.ai/api-reference/models/generate-or-edit-an-image-with-flux2-klein-4b) · [API 9B](https://docs.bfl.ai/api-reference/models/generate-or-edit-an-image-with-flux2-klein-9b) | [Training](https://docs.bfl.ai/flux_2/flux2_klein_training) · [Style training](https://docs.bfl.ai/flux_2/flux2_klein_training_example) · [Comfy tutorial](https://docs.comfy.org/tutorials/flux/flux-2-klein) (verificado 2026-10-20) | [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview) · [Image editing](https://docs.bfl.ai/flux_2/flux2_image_editing) |
| **Kontext pro/max** | [Overview](https://docs.bfl.ai/kontext/kontext_overview) (BFL recomienda FLUX.2 para proyectos nuevos) | [API pro](https://docs.bfl.ai/api-reference/models/edit-or-create-an-image-with-flux1-kontext-pro) | [Text-to-image](https://docs.bfl.ai/kontext/kontext_text_to_image) · [Editing](https://docs.bfl.ai/kontext/kontext_image_editing) |
| **FLUX1.1 pro** | [API ref](https://docs.bfl.ai/flux_models/flux_1_1_pro) | [Ultra mode](https://docs.bfl.ai/flux_models/flux_1_1_pro_ultra_raw) | — |
| **FLUX.1 dev / Fill** | [API dev](https://docs.bfl.ai/api-reference/models/generate-an-image-with-flux1-dev) | [Fill inpainting](https://docs.bfl.ai/api-reference/models/inpaint-an-image-with-flux1-fill-pro-using-an-input-image-and-mask) | — |
| Croquis→render, interior | — | — | [Drawing rendering](https://docs.bfl.ai/guides/usecases_editing_drawing_rendering) · [Interior design](https://docs.bfl.ai/guides/usecases_editing_interior_design) · [Character consistency](https://docs.bfl.ai/guides/usecases_editing_character_consistency) |

## Conceptos relacionados

- [[wiki/glosario/software/pollinations|Pollinations]]
- [[wiki/glosario/software/comfyui|ComfyUI]]
- [[wiki/glosario/software/n8n|n8n]]
- [[wiki/glosario/software/proveedores-modelos-ia|Proveedores modelos IA]]

## Referencias

- [Qwen-Image-2.1 — GitHub oficial](https://github.com/QwenLM/Qwen-Image-2.1) (verificado 2026-11-03 — 200, 7B, Turbo 8 pasos, 10 refs, ComfyUI día cero)
- [FLUX 3 Image Klein — Black Forest Labs](https://bfl.ai/blog/flux-3-image-klein) (verificado 2026-11-03 — 200, 5.6B, 4K, 10 refs, INT8 8 GB, Kommunity <$5M)
- [Nano Banana 2.1 — Model Card Google DeepMind](https://deepmind.google/models/model-cards/nano-banana-2-1/) (verificado 2026-11-03 — 200, Thinking 1050 Elo, multi-ref 1066)
- [Best Image Generation Models — Arena](https://bestllmmodels.com/best-llm-for-image-generation) (Arena 07-10-26, Sunburst 1424.6 top, open top Qwen-2.1 1222.9)
- [Text Rendering Leaderboard — Arena](https://arena.ai/leaderboard/text-to-image/text-rendering) (26-10-26, Sunburst 1466 top)
- [Best AI for Architects — LLM Stats](https://llm-stats.com/best-ai-for-architects) (Nano Banana lidera cluster arquitectura)
- [Archviz benchmark — VibeDex](https://vibedex.ai/blog/best-ai-architectural-visualization-2026) (NBP 4.62, FLUX.2 Pro 4.53)
