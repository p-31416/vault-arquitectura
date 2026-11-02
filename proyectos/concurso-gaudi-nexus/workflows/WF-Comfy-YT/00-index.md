---
tipo: indice
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, indice]
idioma: es
---

# WF-Comfy-YT — Flujos de YouTube analizados

> Carpeta de trabajo sobre videos de ComfyUI: cada video que manda Sol se analiza con la misma plantilla y su JSON queda guardado junto al análisis. Vive junto al set [[proyectos/concurso-gaudi-nexus/WF-curso/01-index-sdxl-vista|sdxl-vista]] porque los flujos que sirven se prueban con los mismos checkpoints (Juggernaut v9, RealVisXL v5.0).

## Plantilla de análisis (la que pide cada video)

1. **Video**: título, canal, URL, duración, de qué trata.
2. **JSON**: archivo del autor si es abierto; si está tras paywall, reconstrucción local marcada como tal.
3. **Modelo**: nombre, base (SD/SDXL/Flux…), link de descarga, licencia y si corre en la RX 570.
4. **Nodos**: tabla con función en el flujo y link a la doc oficial.
5. **Cuadro de pruebas**: matriz de pruebas (agregar/quitar/cambiar elementos) con máscara, prompt, denoise y qué mirar.
6. **Referencias**: video, archivos, docs.

## Base (00, prerrequisito)

| Doc | Qué cubre |
|---|---|
| [00 — ComfyUI en un pod](00-pod-runpod-comfyui) | guía de pod en Runpod siguiendo el video de DorianAI + notas de mejora 2026 (precios, templates oficiales, storage, atajo con la herramienta propia) |
| [00 — Pod Flux económico](00-pod-flux-economico) | pod mínimo viable para Flux (klein 9B + LoRA) al menor costo, con n8n en el VPS como mayordomo start→run→stop |
| [00 — Comfy $20 vs RunPod](00-comfy-vs-runpod) | guía paso a paso, costo final por escenario y recomendación (custom nodes y LoRA propio como criterio) |
| [00 — Instalar ComfyUI en Runpod](00-pod-instalar-comfy-paso-a-paso) | instalación paso a paso: de cuenta nueva a URL usable desde cualquier PC, con la PC local libre |
| [00 — n8n como mayordomo del pod](00-n8n-ciclo-pod) | ciclo start→run→stop desde el VPS: endpoints v2, nodos n8n, fail-safe de apagado |

## Videos analizados

| # | Video | Técnica | Modelo | JSON | Estado |
|---|---|---|---|---|---|
| YT-01 | [SDXL Inpainting para arquitectura](YT-01-sdxl-inpainting-diffuseda) (Diffused.A Studio, 2:56) | inpainting + ControlNet opcional | Juggernaut XL + LoRA archviz (sin identificar) | reconstrucción local (`workflow_YT-01-sdxl-inpainting.json`; original tras paywall USD 7,99) | listo para probar |

## Cómo pedir el siguiente

Pasar la URL del video. El análisis devuelve: JSON reconstruido o del autor, modelo con link de descarga, nodos con docs y cuadro de pruebas, todo en un `YT-NN-*.md` nuevo en esta carpeta.
