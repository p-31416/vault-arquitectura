---
tipo: indice
mvp: 04
n: 07
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, comfyui, img2video, ltx, video, indice]
---

# n_07-img2video — Spariador→render en movimiento

Objetivo: un **render (o croquis renderizado) se convierte en clip de video** (walkthrough/cámara fija breve) como etapa siguiente a txt2img/img2img.

- Flujo activo: [[#WF_v1.0 — LTX 2.3 img-to-video]]
- Reglas: [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]]
- Prueba en nube: pendiente según orden aprobado (RunPod pod sin configurar a esta fecha)

## WF_v1.0 — LTX 2.3 img-to-video

- JSON fuente: `WF/WF_v1.0_ltx_i2v/workflow_ltx_i2v.json`
- Log: [[proyectos/MVP_04-comfyui-arquitectura/n_07-img2video/WF/WF_v1.0_ltx_i2v/02-WF-log-ltx_i2v|02-WF-log]]
- Nodos/configs propias: [[proyectos/MVP_04-comfyui-arquitectura/n_07-img2video/WF/WF_v1.0_ltx_i2v/03-nodos-ltx_i2v|03-nodos]]
- Backlog: [[proyectos/MVP_04-comfyui-arquitectura/n_07-img2video/WF/WF_v1.0_ltx_i2v/04-backlog|04-backlog]]
- Salidas: `WF/WF_v1.0_ltx_i2v/salidas/` (vacía a la fecha — se llena con `n_07-A-01.mp4`...)

Config mínima declarada (a verificar en `/object_info` antes de la primera corrida, R4):
- checkpoint `ltx-2.3-22b-dev.safetensors` + text encoder gemma fp8 + 2 LoRAs distill — **sin localizar en la instalación P:\00-repos\ComfyUI** (paquete ~24-46GB; instalación vía `apply_manifest` pendiente de `s`)
- primero en probarse en la NUBE (RunPod pod o Comfy Cloud/API)
