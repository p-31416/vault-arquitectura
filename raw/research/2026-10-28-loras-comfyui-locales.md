---
tipo: research
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [research, comfyui, lora, rx570, directml, sd15, sdxl, arquitectura]
---

# 2026-10-28 — LoRAs de ComfyUI que corran en la infraestructura local

Informe de investigación: qué LoRAs de arquitectura pueden generarse **en esta máquina** (AMD RX 570 8 GB · DirectML · ComfyUI 0.28.0) y cuáles son de RunPod. Todo verificado contra disco, la API de CivitAI, la API de Hugging Face y el propio lector de safetensors de ComfyUI.

**Resultado integrado en el vault:** [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]] · workflow [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/00-README|WF-loras-locales]].

---

## 1. Punto de partida: la infraestructura real

Medido sobre la máquina el 2026-10-28, no sobre la documentación:

| Dato | Valor | Cómo se verificó |
|---|---|---|
| ComfyUI | 0.28.0 · `P:\00-repos\ComfyUI` · git `b08e6cf3` (2026-07-17) | `comfyui_version.py` + `git log` |
| Parches locales | 3 no commiteados: `comfy/model_management.py`, `comfy_extras/nodes_canny.py`, `app/logger.py` | `git status` + `git diff` |
| GPU / backend | RX 570 8 GB vía DirectML (`torch 2.4.1+cpu`, Python 3.11.13) | `GET /system_stats` |
| VRAM que ve ComfyUI | 8 GB gracias al parche; sin él, DirectML reporta 1 GB (placeholder del core) | `comfy/model_management.py:321` |
| Checkpoints | ArchitectureRealmix v1.1 (SD 1.5, 2,03 GB) · Juggernaut-XL v9 (SDXL, 6,78 GB) · sd-v1-5-inpainting | `models/checkpoints/` |
| ControlNets | canny · depth fp16 · scribble (los tres SD 1.5) | `models/controlnet/` |
| `models/text_encoders/` | **vacío** | listado de disco + `/models` |
| `custom_nodes/` | solo `ComfyUI_IPAdapter_plus` y `ComfyUI-IC-Light` | listado de disco |
| Upscaler | `RealESRGAN_x4plus.pth` | `models/upscale_models/` |
| LoRAs previos | `archisketch-v1` (SD 1.5) · `markerhandsketch-V1` (SD 1.5) · `rhino-to-image` (FLUX.2 klein 9B) | `models/loras/` |
| Último render | 30 steps en 132 s | `user/comfyui_8188.log.err` |
| Espacio libre | 626 GB en P: | `Get-PSDrive P` |
| Sampler `lcm` | nativo (`comfy/samplers.py:972`) | grep del core |

**Consecuencia directa:** con `text_encoders/` vacío y sin base FLUX instalada, **ningún LoRA de FLUX/SD3/Qwen puede cargarse local**, aunque se baje el modelo base. El límite real no es el LoRA: es la base.

## 2. Criterio derivado

| Base | Local | Condición |
|---|---|---|
| SD 1.5 | ✅ | LoRA ≤250 MB; conviven 2 ControlNet |
| SDXL | ⚠️ | LoRA ≤900 MB (a medir) **sin** ControlNet |
| FLUX.1 / FLUX.2 / Qwen | ❌ | RunPod 24 GB |

El factor dominante no es el tamaño del archivo del LoRA sino su **rank**: un rank 128 genera tensores mucho más grandes al fusionarse, y ese delta es el que define el pico de VRAM. Un rank 8–16 es prácticamente gratis.

## 3. Método de selección

1. Búsqueda en la API de CivitAI filtrando por `types=LORA` y `baseModels=SD 1.5` / `SDXL 1.0`, ordenadas por descargas, con las consultas *architecture, interior, brutalist, archviz, isometric, sketch architecture, architectural visualization, skyscraper, diorama*.
2. Resolución de `modelVersion` y de `fileId` por modelo; extracción de `baseModel`, `trainedWords`, `sizeKB` y `downloadUrl`.
3. Descarga con `curl --retry 3` (más robusto que `Invoke-WebRequest`) con `User-Agent` y `Referer` a CivitAI.
4. Validación de integridad abriendo cada archivo con `safetensors.safe_open` —el mismo lector que usa ComfyUI— y leyendo la metadata embebida para confirmar la base real.

## 4. Catálogo verificado (instalado)

### SD 1.5 — con ArchitectureRealmix v1.1 (768×512, 30 steps, cfg 7, euler_ancestral+karras)

| Archivo | Rank | MB | Trigger | CivitAI (modelo/version) |
|---|---|---|---|---|
| `JJ_Archvizcg_v2.safetensors` | 128 | 144,1 | `archviz` | 191596 / 235659 |
| `sandiese.safetensors` | 32 | 36,1 | `architecture, building, grey_background` | 134165 / 147752 |
| `xsarchitectural-10superhighrisebuilding.safetensors` | 32 | 36,1 | `architectural renderings, bird's-eye view` | 25509 / 30541 |
| `room.safetensors` | 64 | 72,1 | `room` | 37483 / 43473 |
| `landscape_architecture_sketch.safetensors` | 32 | 36,1 | `sketch, architecture, building` | 45218 / 49832 |
| `Le Corbusier 2.2.7.2_sd1.5-000016.safetensors` | 32 | 36,1 | `zhuai_pb, brutalism` | 67585 / 90878 |
| `BrutalistTech-20.safetensors` | 128 | 144,1 | `brutaltech, cement` | 85252 |
| `archisketch-v1.safetensors` | 16 | 18,1 | `linear` | 32757 / 39140 (previo) |
| `markerhandsketch-V1.safetensors` | 8 | 9,1 | `marker painting, handsketch` | 34384 / 40665 (previo) |

### SDXL — con Juggernaut XL v9 (1216×832, 30 steps, cfg 4, dpmpp_2m+karras)

| Archivo | Rank | MB | Trigger | CivitAI |
|---|---|---|---|---|
| `isometric-v1.safetensors` | 16 | 109,1 | `isometric style` | 151008 / 168807 |
| `Architectural_Massing.safetensors` | 32 | 217,9 | — | 724833 / 810516 |
| `Architecture_Building.safetensors` | 32 | 217,9 | — | 731161 |
| `baroque_architecture-000006.safetensors` | 64 | 435,3 | — | 336095 |
| `ArcvizXL_V01.safetensors` | 128 | 870,3 | `archviz 1` | 549260 / 611104 |
| `bookstore-xl.safetensors` | 128 | 870,3 | `mrares, bookstore` | 139539 / 154559 |
| `SLskyscraperrenderingXL_V1.0.safetensors` | 128 | 870,3 | — | 198528 / 223346 |

### FLUX (RunPod)

| Archivo | Base | Rank | MB |
|---|---|---|---|
| `rhino-to-image-lora.basic.safetensors` | FLUX.2 [klein] 9B | 16 | 120,8 |

## 5. LoRAs que exigen login de CivitAI

La API entrega el `downloadUrl` pero el binario llega con `content-type: text/html` (la página "Civitai Login", ~0,01 MB) cuando el uploader exige cuenta. **Cinco** del catálogo elegido caen en ese caso:

| LoRA | Base | MB | Trigger | Sustituto local |
|---|---|---|---|---|
| JJ's Brutalist Architecture | SD 1.5 | 126,1 | `Brutalist Architecture` | `BrutalistTech-20` |
| JJ's Brutalist Architecture XL | SDXL | 435,3 | `Brutalist Architecture` | `baroque_architecture-000006` |
| Building Info Concepts Sheets | SD 1.5 | 144,1 | `info reference sheet` | — |
| ArchViz Workflow (ArteFactoryLab) | SDXL | 36,1 | `archviz` | `Architecture_Building` + `ArcvizXL_V01` |
| JJ's Skyscraper | SDXL | 435,4 | `Skyscraper` | `SLskyscraperrenderingXL_V1.0` |

Con `CIVITAI_API_TOKEN` exportado en el entorno, la cabecera `Authorization: Bearer <token>` resuelve los cinco.

**Mirror en HF:** existe `Muapi/jj-s-brutalist-architecture`, pero el archivo es la **variante FLUX** (`ss_output_name: JJsBrutalistArchitecture_Flux`, `modelspec.architecture: flux-1-dev/lora`, 292 MB) → no sirve para local.

## 6. Aceleración (documentada, pendiente de instalar)

| Recurso | Fuente | Estado |
|---|---|---|
| LCM-LoRA SD 1.5 | `latent-consistency/lcm-lora-sdv1-5` → `pytorch_lora_weights.safetensors` | URL verificada por API |
| LCM-LoRA SDXL | `latent-consistency/lcm-lora-sdxl` | URL verificada por API |
| Hyper-SD (1/2/4/8 steps + workflows ComfyUI) | `ByteDance/Hyper-SD` | URL verificada por API |
| SDXL Lightning | `stabilityai/sdxl-lightning` | HTTP 401 desde esta red |
| Control-LoRA SDXL | `johannah/control-lora` | HTTP 401 desde esta red |
| TCD-SDXL | `jaznewton/TCD-SDXL-LoRA` | HTTP 401 desde esta red |
| DetailTweaker | `ostris/sdxl-detail-tweaker` | HTTP 401 desde esta red |

Configuración de referencia (CivitAI Education, "Quickstart Guide to LCM LoRA"): sampler `lcm` o `euler a`, scheduler `sgm_uniform`, **steps 3–8**, **CFG 1–2,5**, strength del LoRA 0,5–1,0. El sampler `lcm` ya viene en el core 0.28 → no hacen falta nodos extra.

## 7. Findings técnicos reutilizables

1. **Una descarga de CivitAI puede devolver HTML.** Detección: `curl -sIL -o NUL -w "%{http_code}|%{content_type}"` → exigir `200` y tipo no-HTML.
2. **CivitAI no soporta `Range`**: una descarga cortada no se puede reanudar (`curl: (33) HTTP server does not seem to support byte ranges`). Hay que borrar y bajar de nuevo.
3. **El tamaño no prueba la integridad.** `ArcvizXL_V01` llegó con 64,87 MB de 870,3 MB y solo el `safe_open` lo delató (`incomplete metadata, file not fully covered`). Un validador que solo compara `sizeKB` de la API se deja engañar.
4. **DirectML rompe `F.pad` de kornia** (invierte los ejes) → el preprocesado Canny corre en CPU (parche local en `comfy_extras/nodes_canny.py`).
5. **ComfyUI 0.28 trae Depth Anything V3 y SD Pose nativos** (`comfy_extras/nodes_depth_anything_3.py`, `comfy_extras/nodes_sdpose.py`): MiDaS/DPT requieren instalar `comfyui_controlnet_aux`, que hoy no está.
6. **El `LoraLoader` debe ir entre el checkpoint y el sampler**, y los `CLIPTextEncode` deben colgar de su salida 1 (CLIP) para que el prompt también reciba el LoRA.
7. **El trigger va en el prompt**, nunca el nombre del archivo `.safetensors` (error cometido y corregido el 2026-10-28).

## 8. Fuentes

- CivitAI API: `https://civitai.com/api/v1/models/{id}`, `.../model-versions/{id}`, búsqueda con `types=LORA&baseModels=`
- Modelos citados: [191596](https://civitai.com/models/191596) · [134165](https://civitai.com/models/134165) · [25509](https://civitai.com/models/25509) · [37483](https://civitai.com/models/37483) · [45218](https://civitai.com/models/45218) · [67585](https://civitai.com/models/67585) · [85252](https://civitai.com/models/85252) · [1112495](https://civitai.com/models/1112495) · [181034](https://civitai.com/models/181034) · [151008](https://civitai.com/models/151008) · [724833](https://civitai.com/models/724833) · [731161](https://civitai.com/models/731161) · [538977](https://civitai.com/models/538977) · [336095](https://civitai.com/models/336095) · [2870219](https://civitai.com/models/2870219) · [549260](https://civitai.com/models/549260) · [139539](https://civitai.com/models/139539) · [198528](https://civitai.com/models/198528) · [1116945](https://civitai.com/models/1116945) · [315139](https://civitai.com/models/315139) · [2280607](https://civitai.com/models/2280607) · [307178](https://civitai.com/models/307178) · [709956](https://civitai.com/models/709956)
- Hugging Face: [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) · [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) · [ByteDance/Hyper-SD](https://huggingface.co/ByteDance/Hyper-SD) · [Muapi/jj-s-brutalist-architecture](https://huggingface.co/Muapi/jj-s-brutalist-architecture)
- Docs: [CivitAI Education — Quickstart Guide to LCM LoRA](https://education.civitai.com/quickstart-guide-to-lcm-lora-acceleration-modules/) · [ComfyUI Docs — KSampler](https://docs.comfy.org/built-in-nodes/sampling/ksampler) · [ComfyUI Docs — LoRA](https://docs.comfy.org/built-in-nodes/lora) · [Comfy-Org/ComfyUI — VRAM / DirectML](https://github.com/Comfy-Org/ComfyUI) · [kornia — Canny](https://kornia.readthedocs.io/en/latest/filters.html#kornia.filters.canny) · [CivitAI — Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2)
- Contexto de la máquina: `P:\00-repos\ComfyUI` (core 0.28.0 + parches), `user/comfyui_8188.log.err` (tiempos reales), `wiki/glosario/software/comfyui`, `wiki/glosario/interno/pbooks/pbk-comfyui`
