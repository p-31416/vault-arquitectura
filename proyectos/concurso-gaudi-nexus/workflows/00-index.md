---
tipo: indice
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, workflows, comfyui, runpod]
idioma: es
---

# Workflows del concurso — siete flujos, uno por módulo

> Cada workflow se construye y se revisa **uno por uno**: grafo → validación estática → tres corridas A y una B → revisión de Sol → cierre en v1.0. El plan completo está en [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro]].
>
> **Matriz de pruebas (organizada por flujos)**: [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|00-matriz-pruebas-concurso]] · **Cuadro ampliable** en `00-matriz-pruebas-concurso.excalidraw.md` (zoom/pan en Obsidian) + PNG en `activos/diagramas/matriz-pruebas-concurso.png`.
>
> **Set SDXL solo-vista**: [[proyectos/concurso-gaudi-nexus/workflows/sdxl-vista/01-index|sdxl-vista]] — un flujo por WF (01–07) para abrir en ComfyUI con drag-and-drop, sin ejecutar ni validar (R4 pendiente).

## Mapa

| WF | Módulo | Grafos | Corre en | Precondiciones | Estado |
|----|--------|--------|----------|----------------|--------|
| **WF-01** base | 1 | `workflow_base_lectura.json` | local | ninguna | pendiente |
| **WF-02** texto a imagen | 2 | `workflow_comparativa_modelos.json` · `workflow_lora_strength.json` | local + pod | stack FLUX.2 en el pod | pendiente |
| **WF-03** rhino a imagen | 3 | `workflow_rhino_to_imagen.json` (existe) · `workflow_upscale_local.json` · `workflow_edicion_inpaint.json` | pod + local | capturas de Rhino + stack FLUX.2 | grafo (a) ya existe |
| **WF-04** imagen a video | 4 | `workflow_video_ltxi2v.json` · `workflow_timelapse.json` · `workflow_interpolacion.json` | pod (+ prueba en Comfy Cloud Free) | modelos LTX | pendiente |
| **WF-05** imagen a 3D | 5 | `workflow_prep_3d.json` · `workflow_img2_3d.json` | local + pod | ComfyUI-3D-Pack y sus modelos | pendiente |
| **WF-06** criterio del jurado | 6 | sin grafo | local (faster-whisper) | bajar el audio del módulo | script listo |
| **WF-07** flujo Gaudí | 7 | `workflow_gaudi_paso1_arcilla.json` + WF-03 como paso 2 | pod | INSTRUCTION.md var. B (listo) + LoRA | pendiente |

## Ciclo de construcción y revisión

| # | Paso | Herramienta | Gate |
|---|------|-------------|------|
| 1 | Ficha de flujo | `flujos/flujo-0X-*.md` | — |
| 2 | Grafo + documentación de nodos | `workflow_<nombre>.json` · `03-nodos-<nombre>.md` | — |
| 3 | Validación estática | `/object_info` del servidor destino + inventario de modelos | — |
| 4 | Corridas | 3× A + 1× B, con `02-WF-log` | — |
| 5 | Revisión de Sol | salidas + `03-nodos` | **HITL** |
| 6 | Cierre | `01-index` · `04-backlog` · checklist del jurado | — |

## Convenciones

- **Estructura de carpeta**: `00-README.md` · `01-index.md` · `02-WF-log-WF<nn>.md` · `03-nodos-WF<nn>.md` · `04-backlog.md` · `salidas/` · `PLANS/` · `SPECS/` · `workflow_<nombre>.json`.
- **JSON en API format**, ids numéricos correlativos como strings, links por `["id", índice_de_salida]`, `_meta.title` en los nodos con rol editorial.
- **Salidas**: `gx-{LETRA}-{NN}.png` (A baseline · B prompt · C parámetros · D modelo · E resolución · F ControlNet/img2img).
- **Binarios fuera de git**: las corridas viven en `salidas/` y los materiales en `activos/`.
- **Reglas vigentes**: [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|R1 (escala en SD1.5) · R2 (escala a megapíxeles en FLUX.2) · R3 (nomenclatura `gx-`) · R4 (validación estática antes de la corrida)]].

## Antes de la primera corrida

| Recurso | Ubicación | Estado |
|---------|-----------|--------|
| Checkpoint SD1.5 | `models/checkpoints/architecturerealmix_v11.safetensors` | en disco |
| Checkpoint SDXL | `models/checkpoints/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | en disco |
| Checkpoint inpainting | `models/checkpoints/sd-v1-5-inpainting-fp16.safetensors` | en disco |
| LoRA del curso | `models/loras/rhino-to-image-lora.basic.safetensors` | en disco |
| ControlNet canny / depth / scribble | `models/controlnet/` | en disco |
| IPAdapter + CLIP vision | `models/ipadapter/` · `models/clip_vision/` | en disco |
| Depth Anything 3 | `models/geometry_estimation/depth_anything_3_small.safetensors` | en disco |
| Upscaler | `models/upscale_models/RealESRGAN_x4plus.pth` | en disco |
| Stack FLUX.2 klein 9B | transformer fp8 + Qwen3-8B + VAE Flux2 (18,3 GB) | **falta** → pod |
| LTX (video) | modelos de video | **falta** → pod |
| ComfyUI-3D-Pack | custom node + modelos | **falta** → pod |

## Conceptos relacionados

- [[proyectos/concurso-gaudi-nexus/index|Índice del proyecto]] · [[proyectos/concurso-gaudi-nexus/flujos/00-index|Fichas de flujo]] · [[proyectos/concurso-gaudi-nexus/criterio/criterio-jurado|Criterio del jurado]] · [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image|WF-rhino-to-image (existente)]] · [[proyectos/MVP_04-comfyui-arquitectura/n_04-video|n_04-video]] · [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] · [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]]
