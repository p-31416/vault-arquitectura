# 2026-10-28 — LoRAs de ComfyUI que corren en la infra local: catálogo verificado, 17 instaladas y WF de calibración

## Qué se hizo

- **Investigación de los LoRAs que pueden generarse en esta máquina** (RX 570 8 GB · DirectML · ComfyUI 0.28.0): inventario real del stack (checkpoints, ControlNets, text encoders, custom nodes, parches locales, flags del launch), búsqueda dirigida en la API de CivitAI por base model y descarga verificada de **16 LoRAs de arquitectura** (9 SD 1.5 + 7 SDXL), más 3 sustitutos para los que exigían login. Con los 2 que ya estaban, quedan **17 LoRAs instalados y validados (17/17)**.
- **Validación de integridad real**: cada `.safetensors` se abrió con `safetensors.safe_open` (el lector que usa ComfyUI) y se leyó su metadata embebida (`ss_output_name`, `ss_base_model_version`, `ss_network_dim`, `modelspec.architecture`) para confirmar base y rank. Se detectaron y repusieron 2 descargas truncadas.
- **Ficha nueva** [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]]: criterio de elegibilidad local (SD1.5 / SDXL / FLUX), catálogo completo con base-rank-tamaño-trigger-CivitAI, los 5 que piden login con sus sustitutos, los candidatos de aceleración, **qué hace cada flag del launch** y los tres parches locales.
- **Correcciones al vault**: (a) el link a CivitAI #119936 como "Architectural Visualization" era errónero (es "Action - Eating Watermelon"); (b) `dpt_hybrid`/`midas_v21_small` no están disponibles (falta `comfyui_controlnet_aux`) pero el core 0.28 trae Depth Anything V3 y SD Pose nativos; (c) los SDXL de 870 MB–1,3 GB quedan para RunPod.
- **Workflow de calibración nuevo** `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/` (00-README · 01-index · 02-WF-log · 03-nodos · 04-backlog + 2 grafos API) y **script nuevo** `scripts/calibrar-loras-comfyui.py` + notas didácticas.
- **Leyenda de salidas ampliada**: la letra **G = LoRA** se añadió a `reglas-workflows-comfy.md` y al índice del WF.
- **Informe de investigación** en `raw/research/2026-10-28-loras-comfyui-locales.md` (fuentes, método, hallazgos).

## Hallazgos

- **El límite no es el LoRA: es la base.** `models/text_encoders/` está vacío → aunque se baje un LoRA de FLUX, no hay base FLUX local ni text encoder (T5/CLIP-L). FLUX/SD3/Qwen → RunPod 24 GB.
- **El rank pesa más que el tamaño del archivo**: un LoRA rank 128 (144 MB en SD1.5, 870 MB en SDXL) genera tensores mucho más grandes al fusionarse; ese delta define el pico de VRAM. Rank 8–16 es prácticamente gratis.
- **5 LoRAs de CivitAI devuelven la página de login en vez del binario** (≈0,01 MB, `content-type: text/html`). Se detectan con un HEAD: exigir `200` + tipo no-HTML.
- **CivitAI no soporta `Range`**: una descarga cortada no se puede reanudar (`curl: (33)`); hay que borrarla y bajarla de nuevo.
- **El tamaño NO prueba la integridad**: `ArcvizXL_V01` llegó con 64,87 MB de 870,3 MB y solo `safe_open` lo delató (`incomplete metadata, file not fully covered`). Comparar contra `sizeKB` de la API deja pasar un archivo roto.
- **El mirror de HF del brutalista de JJ es la variante FLUX** (`modelspec.architecture: flux-1-dev/lora`, 292 MB): no sirve para local aunque parezca el mismo modelo.
- **La SDXL de 900 MB es una hipótesis, no un dato**: con `--lowvram` el modelo se pagina contra la RAM, así que el delta real de VRAM es el del parche LoRA (rank), no el del archivo. Falta medirlo con los renders de rank 128.
- **ComfyUI 0.28 trae Depth Anything V3 y SD Pose nativos** (`comfy_extras/nodes_depth_anything_3.py`, `nodes_sdpose.py`): el `pbk` atribúa el preprocesado de profundidad a `comfyui_controlnet_aux`, pack que no está instalado.
- **DirectML rompe `F.pad` de kornia** (invierte los ejes) → el Canny corre en CPU (parche local ya aplicado).
- **El trigger va en el prompt, nunca el nombre del `.safetensors`** — error cometido en el primer grafo encolado y corregido.
- **El sampler `lcm` es nativo** (`comfy/samplers.py:972`): la aceleración no necesita nodos extra, solo `LoraLoader` + `KSampler(lcm, sgm_uniform, 4-6 steps, cfg 1-2)`.
- **HF responde 401** a `sdxl-lightning`, `control-lora`, `TCD-SDXL-LoRA` y `sdxl-detail-tweaker` desde esta red; `lcm-lora-sdv1-5`, `lcm-lora-sdxl` y `ByteDance/Hyper-SD` sí se verifican.

## Archivos

**Nuevos**

- `wiki/glosario/software/lora-locales-comfyui.md`
- `raw/research/2026-10-28-loras-comfyui-locales.md`
- `scripts/calibrar-loras-comfyui.py` · `scripts/calibrar-loras-comfyui_notas.md`
- `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/00-README.md`
- `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/01-index.md`
- `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/02-WF-log-WFloraslocales.md`
- `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/03-nodos-WFloraslocales.md`
- `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/04-backlog.md`
- `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/workflow_loras-locales.json`
- `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/workflow_loras-locales_sdxl.json`
- `raw/sessions/2026-10-28-sesion-loras-comfyui-locales.md`

**Modificados**

- `wiki/glosario/software/comfyui.md` (tabla de LoRAs reales · corrección del link #119936 · enlace a la ficha nueva)
- `wiki/glosario/software/00-index.md` (entrada de la ficha nueva)
- `wiki/glosario/interno/pbooks/pbk-comfyui.md` (nota de preprocesadores de profundidad · sección «LoRAs locales» · triggers reales)
- `proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy.md` (letra **G = LoRA** en la leyenda)
- `scripts/00-index.md` (entrada del script nuevo)
- `log.md` (entrada del 28/10 noche arriba)

**Fuera del vault (instalación local, gitignored por diseño)**

- `P:\00-repos\ComfyUI\models\loras\` → 16 LoRAs nuevos (≈4,0 GB) + los 2 preexistentes
- ComfyUI quedó **corriendo** en background (`corre_comfyui_background.bat`, pid 1780, `http://127.0.0.1:8188`) — se puede detener con:
  `Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like '*ComfyUI*main.py*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }`

## Estado y qué sigue

- **Renders de calibración: pendientes.** La tanda de 32 se abortó a pedido del estudio (job `99eeabec` cancelado; 0 imágenes generadas). El script quedó escrito y verificado en `--dry-run`.
- **Próximo paso sugerido**: `P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py --solo SD1.5 --fuerzas 0.8` (9 renders, ~20 min) para tener lectura rápida antes de la tanda larga.
- **Decisiones abiertas**: token de CivitAI para los 5 LoRAs con login · instalación de `comfyui_controlnet_aux` (MiDaS/DPT) · instalación de LCM-LoRA / Hyper-SD · medir el techo real de SDXL con LoRAs rank 128.

## Análisis cerebro-digital

**Topics:** comfyui-loras · calibracion-lora · sd15 · sdxl · rx570 · directml · civitai-api · huggingface-lora · lcm-lora · hyper-sd · depth-anything-3 · controlnet-aux · safetensors · directml-vram-patch · workflow-g-lora

**Entidades:** `P:\00-repos\ComfyUI` (instalación local, v0.28.0, 3 parches) · `wiki/glosario/software/lora-locales-comfyui` (ficha nueva) · `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales` (WF nuevo) · `scripts/calibrar-loras-comfyui.py` (script nuevo) · `raw/research/2026-10-28-loras-comfyui-locales` (informe) · ComfyUI API `POST /prompt` + `GET /history/{id}` (transporte del script) · CivitAI API `models`/`model-versions` (metadatos) · `safetensors.safe_open` (validación de integridad) · job cancelado `99eeabec-4590-49b2-a9c6-c55cdbdbb386`

**Hechos:**
- Con `text_encoders/` vacío no se puede cargar ningún LoRA de FLUX/SD3/Qwen en local.
- La base del LoRA se deduce de su metadata: `ss_base_model_version` (`sd_v1`, `sdxl_base_v1-0`) y `modelspec.architecture` (`stable-diffusion-v1/lora`, `stable-diffusion-xl-v1-base/lora`).
- Los LoRAs de SD 1.5 traen 792 tensores y los de SDXL 2958: el recuento sirve como huella de familia.
- CivitAI exige login (no solo token) para 5 modelos del catálogo; el mirror de HF del brutalista de JJ es la variante FLUX.
- Un LoRA rank 128 en SDXL ocupa 870,3 MB en disco y es el caso que define el techo de VRAM local.
- El script de calibración deja 32 salidas previstas (`n_01-G-01`…`G-32`) y un JSON de resultados con segundos y error por intento.
