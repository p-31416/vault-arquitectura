---
tipo: software
software: lora-locales-comfyui
categoria: lora
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [glosario, software, comfyui, lora, sd15, sdxl, rx570, directml, arquitectura, calibracion]
---

# LoRAs locales de ComfyUI — catálogo operativo

> Inventario verificado de los LoRAs que **corren en la infraestructura local** (AMD RX 570 8 GB · DirectML), con base, rank, tamaño, trigger, fuente CivitAI y estado real. Verificado contra disco, API de CivitAI y el lector de safetensors de ComfyUI el **2026-10-28**. Los 17 LoRAs instalados abren sin error y su base se confirmó leyendo la metadata embebida (`ss_base_model_version`, `modelspec.architecture`).

- [[#Criterio de elegibilidad local]]
- [[#Catálogo instalado — SD 1.5]]
- [[#Catálogo instalado — SDXL]]
- [[#LoRA FLUX (no local)]]
- [[#Bloqueados por login de CivitAI]]
- [[#Aceleración: candidatos para instalar]]
- [[#Launch local: qué hace cada flag]]
- [[#Método de verificación y trampas]]
- [[#Calibración: estado y cómo seguir]]
- [[#Conceptos relacionados]]

---

## Criterio de elegibilidad local

Un LoRA corre en el RX 570 cuando **el modelo base está instalado** y **el peso cabe en 8 GB junto al checkpoint**.

| Base del LoRA | ¿Corre local? | Condición | Salida |
|---|---|---|---|
| **SD 1.5** | ✅ | ≤250 MB de LoRA, con 2 ControlNet simultáneo | ArchitectureRealmix v1.1 |
| **SDXL** | ⚠️ | hasta **900 MB** con `--lowvram --cpu-vae`; **sin ControlNet** (Union SDXL no entra) | Juggernaut XL v9 |
| **FLUX.1 / FLUX.2 / Qwen** | ❌ | falta text encoder (T5/CLIP-L), falta base model y falta VRAM | RunPod 24 GB |

> **Por qué 900 MB y no 450:** el techo original salió de una estimación conservadora. Con `--lowvram` el modelo se paginea contra la RAM (32 GB disponibles), así que un LoRA de 870 MB entra a costa de velocidad: el delta de VRAM es el del parche LoRA, no el del archivo. **El techo de 900 MB es una hipótesis a medir** — la calibración del 2026-10-29 lo confirma o lo ajusta.

> **Rank importa más que el tamaño del archivo.** Un LoRA rank 128 (144 MB SD1.5 / 870 MB SDXL) genera tensores más grandes al fusionarse: es el que define el pico de VRAM. Los LoRAs rank 8–16 son prácticamente gratis.

---

## Catálogo instalado — SD 1.5

Con **ArchitectureRealmix v1.1** (`architecturerealmix_v11.safetensors`, 2,1 GB) · 768×512 · 30 steps · cfg 7 · euler_ancestral + karras.

| Archivo | Rank | Tamaño | Trigger | CivitAI | Para qué sirve |
|---|---|---|---|---|---|
| `JJ_Archvizcg_v2.safetensors` | 128 | 144,1 MB | `archviz` | [191596](https://civitai.com/models/191596) v2.0 | Render clásico de visualización arquitectónica |
| `sandiese.safetensors` | 32 | 36,1 MB | `architecture, building, grey_background` | [134165](https://civitai.com/models/134165) | Conceptos de arquitectura sobre fondo gris |
| `xsarchitectural-10superhighrisebuilding.safetensors` | 32 | 36,1 MB | `architectural renderings, bird's-eye view` | [25509](https://civitai.com/models/25509) | Torres en vista aérea |
| `room.safetensors` | 64 | 72,1 MB | `room` | [37483](https://civitai.com/models/37483) | Interiores (trigger genérico) |
| `landscape_architecture_sketch.safetensors` | 32 | 36,1 MB | `sketch, architecture, building` | [45218](https://civitai.com/models/45218) | Croquis de paisaje |
| `Le Corbusier 2.2.7.2_sd1.5-000016.safetensors` | 32 | 36,1 MB | `zhuai_pb, brutalism` | [67585](https://civitai.com/models/67585) | Brutalismo público (Villa Savoye, La Tourette) |
| `BrutalistTech-20.safetensors` | 128 | 144,1 MB | `brutaltech, cement` | [85252](https://civitai.com/models/85252) | Sustituye al brutalista de JJ (pide login) |
| `archisketch-v1.safetensors` | 16 | 18,1 MB | `linear` | [32757](https://civitai.com/models/32757) | Foto de arquitectura → croquis (preinstalado) |
| `markerhandsketch-V1.safetensors` | 8 | 9,1 MB | `marker painting, handsketch` | [34384](https://civitai.com/models/34384) | Croquis a marcador (preinstalado) |

## Catálogo instalado — SDXL

Con **Juggernaut XL v9** (`Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors`, 6,8 GB) · 1216×832 · 30 steps · cfg 4 · dpmpp_2m + karras.

| Archivo | Rank | Tamaño | Trigger | CivitAI | Para qué sirve |
|---|---|---|---|---|---|
| `isometric-v1.safetensors` | 16 | 109,1 MB | `isometric style` | [151008](https://civitai.com/models/151008) | Axonometría — el más liviano del set |
| `Architectural_Massing.safetensors` | 32 | 217,9 MB | — | [724833](https://civitai.com/models/724833) | Masa y volumetría |
| `Architecture_Building.safetensors` | 32 | 217,9 MB | — | [731161](https://civitai.com/models/731161) | Edificio como sujeto; sustituye al ArchViz de ArteFactoryLab |
| `baroque_architecture-000006.safetensors` | 64 | 435,3 MB | — | [336095](https://civitai.com/models/336095) | Barroco; sustituye al brutalista XL de JJ |
| `ArcvizXL_V01.safetensors` | 128 | 870,3 MB | `archviz 1` | [549260](https://civitai.com/models/549260) | Archviz interior/exterior — el más pesado |
| `bookstore-xl.safetensors` | 128 | 870,3 MB | `mrares, bookstore` | [139539](https://civitai.com/models/139539) | Interior de librería |
| `SLskyscraperrenderingXL_V1.0.safetensors` | 128 | 870,3 MB | — | [198528](https://civitai.com/models/198528) | Render de rascacielos |

## LoRA FLUX (no local)

| Archivo | Base | Rank | Tamaño | Dónde corre |
|---|---|---|---|---|
| `rhino-to-image-lora.basic.safetensors` | FLUX.2 [klein] 9B | 16 | 120,8 MB | RunPod 24 GB — ver [[wiki/glosario/software/lora-rhino-to-image-gaudi\|lora-rhino-to-image-gaudi]] |

## Bloqueados por login de CivitAI

Cinco LoRAs del catálogo elegido **exigen cuenta de CivitAI** (la API devuelve la página de login en lugar del binario). Con `CIVITAI_API_TOKEN` exportado en el entorno se bajan sin problema.

| LoRA | Base | Tamaño | Trigger | Sustituto ya instalado |
|---|---|---|---|---|
| JJ's Brutalist Architecture | SD 1.5 | 126,1 MB | `Brutalist Architecture` | `BrutalistTech-20` |
| JJ's Brutalist Architecture XL | SDXL | 435,3 MB | `Brutalist Architecture` | `baroque_architecture-000006` |
| Building Info Concepts Sheets | SD 1.5 | 144,1 MB | `info reference sheet` | — (sin equivalente; chessboard de información) |
| ArchViz Workflow (ArteFactoryLab) | SDXL | 36,1 MB | `archviz` | `Architecture_Building` + `ArcvizXL_V01` |
| JJ's Skyscraper | SDXL | 435,4 MB | `Skyscraper` | `SLskyscraperrenderingXL_V1.0` |

## Aceleración: candidatos para instalar

Los LoRAs de aceleración son los únicos que cambian el **tiempo** y no solo el estilo. Quedan documentados para su implementación (decisión 2026-10-28: aún no se instalan).

| LoRA | Fuente | Tamaño | Config | Estado |
|---|---|---|---|---|
| LCM-LoRA SD 1.5 | [latent-consistency/lcm-lora-sdv1-5](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5) (`pytorch_lora_weights.safetensors`) | ~135 MB | sampler `lcm` + `sgm_uniform`, 4–6 steps, cfg 1–2, strength 0,5–1,0 | URL verificada |
| LCM-LoRA SDXL | [latent-consistency/lcm-lora-sdxl](https://huggingface.co/latent-consistency/lcm-lora-sdxl) | ~197 MB | ídem | URL verificada |
| Hyper-SD (SD1.5 + SDXL) | [ByteDance/Hyper-SD](https://huggingface.co/ByteDance/Hyper-SD) | 135 MB–1,5 GB | 1/2/4/8 steps; trae workflows ComfyUI listos en `comfyui/` | URL verificada |
| SDXL Lightning | `stabilityai/sdxl-lightning` | — | 2/4/8 steps | HF responde 401 desde esta red |
| Control-LoRA SDXL | `johannah/control-lora` | — | ControlNet destilado → menos VRAM que Union | HF responde 401 desde esta red |
| TCD-SDXL | `jaznewton/TCD-SDXL-LoRA` | — | destilación por tensor | HF responde 401 desde esta red |
| DetailTweaker | `ostris/sdxl-detail-tweaker` | — | micro-detalle | HF responde 401 desde esta red |

> El sampler `lcm` ya es nativo en ComfyUI 0.28 (`comfy/samplers.py:972`), así que la aceleración no requiere nodos extra: alcanza con `LoraLoader` + `KSampler(sampler_name="lcm", scheduler="sgm_uniform", steps=4..6, cfg=1..2)`.

## Launch local: qué hace cada flag

El launch es `P:\00-repos\ComfyUI\corre_comfyui.bat` (o `corre_comfyui_background.bat`, que lo deja detached y loguea en `user/comfyui_8188.log`). Ambos arman el mismo `PARAMS`:

```
python main.py --listen 127.0.0.1 --port 8188 --force-fp16 --preview-method auto
                --disable-auto-launch --cache-ram 2 8 --lowvram --cpu-vae
                --directml 0 --disable-cuda-malloc --disable-dynamic-vram
```

| Flag | Qué resuelve en esta máquina |
|---|---|
| `--directml 0` | GPU AMD vía `torch-directml`; el `0` es el índice de adaptador. Sin esto ComfyUI busca CUDA y no hay NVIDIA. |
| `--force-fp16` | Fuerza fp16 donde el modelo no es fp32 nativo. En Polaris (RX 570, sin bf16 nativo) es la diferencia entre que quepa o no. |
| `--lowvram` | Divide el modelo en partes y las pagina GPU↔RAM. Imprescindible con SDXL + LoRA rank 128 en 8 GB; cuesta velocidad. |
| `--cpu-vae` | El VAE decodifica en CPU → libera ~1 GB de VRAM. Es el flag que evitó el OOM en `VAEDecode` a 768×512 (2026-10-09). |
| `--cache-ram 2 8` | 2 GB de RAM como caché inicial de modelos, crecer hasta 8 GB → al cambiar de LoRA no se relee del disco. |
| `--preview-method auto` | Vista previa barata durante el sampling → menos RAM y menos cortes en la UI. |
| `--listen 127.0.0.1` | Solo escucha en local: la interfaz no queda expuesta a la red. |
| `--port 8188` | Puerto de la API/UI (el que usa el MCP de comfyui). |
| `--disable-auto-launch` | No abre el navegador al arrancar. |
| `--disable-cuda-malloc` | Sin CUDA el allocator no aplica; queda explícito para que una actualización no lo active. Inofensivo. |
| `--disable-dynamic-vram` | Evita que ComfyUI recalcule el presupuesto de VRAM: con el parche de DirectML, recalcular devuelve el default de 1 GB y rompe. |

### Los tres parches locales (ComfyUI 0.28.0, `git b08e6cf3`)

| Archivo | Qué hace |
|---|---|
| `comfy/model_management.py:321` | DirectML reporta **1 GB de VRAM** (placeholder de ComfyUI). El parche lo lee de WMI (`AdapterRAM`) y, como ese campo es uint32, fuerza **8 GB** para la clase RX 570/580. Sin este parche ComfyUI cree que tiene 1 GB y no carga ningún modelo. **Reaplicar si se actualiza ComfyUI.** |
| `comfy_extras/nodes_canny.py` | DirectML rompe `F.pad` de kornia (invierte los ejes) → el preprocesado **Canny corre en CPU**. |
| `app/logger.py` | Ajuste de logging del launcher. |

## Método de verificación y trampas

Tres cosas que costaron tiempo el 2026-10-28 y conviene no repetir:

1. **Una descarga de CivitAI puede devolver HTML, no el binario.** Si el modelo pide login, la respuesta es la página "Civitai Login" (~0,01 MB) con `content-type: text/html`. Chequeo: `curl -sIL -o NUL -w "%{http_code}|%{content_type}"` y exigir `200` + tipo no-HTML.
2. **CivitAI no soporta `Range`** → una descarga cortada **no se puede reanudar**: hay que borrarla y bajarla de nuevo (con `curl --retry 3`, que es más robusto que `Invoke-WebRequest`).
3. **El tamaño del archivo no basta para saber si un safetensors está sano.** La verificación autoritativa es abrirlo con el mismo lector que usa ComfyUI:
   ```
   P:\Anaconda\envs\comfyenv\python.exe scripts\analizar-lora-safetensors.py <archivo>
   ```
   o `safetensors.safe_open(path, "pt")` → si el archivo está truncado, revienta con `incomplete metadata, file not fully covered`.

> `models/text_encoders/` está **vacío** → ningún LoRA de FLUX/SD3/Qwen puede cargarse local, ni aunque se baje el base model.

## Calibración: estado y cómo seguir

| Estado | Detalle |
|---|---|
| Script | `scripts/calibrar-loras-comfyui.py` (didáctico, con notas en `scripts/calibrar-loras-comfyui_notas.md`) |
| Workflow | `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/` |
| Renders | **Pendientes** — 32 renders planeados (16 LoRAs × strength 0,6 y 0,8), seed 42 |
| Nomenclatura | `n_01-G-NN.png` en `salidas/` — letra **G = LoRA** (extensión de la leyenda A–F) |

```powershell
# Tanda completa (32 renders, ~2 h en RX 570)
P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py
# Solo una familia o una strength
P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py --solo SD1.5 --fuerzas 0.8
```

El script deja `PLANS/calibracion-loras.json` con LoRA, base, strength, seed, trigger, segundos de render y error (si hubo) por cada intento.

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|comfyui]] — página madre del stack
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]] — el LoRA FLUX del curso AI×Gaudí
- [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]] — base FLUX local
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — playbook: qué flujo usar para cada necesidad
- [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] — local vs nube: límites y costos
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/00-README|WF-loras-locales]] — workflow de calibración
