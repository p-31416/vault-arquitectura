---
tipo: indice
mvp: 04.02
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [mvp_04.02, comfyui, indice]
---

# MVP 04.02 — ComfyUI Arquitectura (versión organizada)

> Evolución organizada de [[proyectos/MVP_04-comfyui-arquitectura/00-index|MVP_04]]. Un archivo único por WF. Solo PC local (RX 570 8GB DirectML), sin RunPod en esta fase.

- [[#Puerta de entrada]]
- [[#Workflows]]
- [[#Convención de archivo único por WF]]
- [[#Hardware de esta fase]]

## Puerta de entrada

- [[proyectos/MVP_04.02-comfyui-arquitectura/README|README]] — orden de lectura y paso a paso para correr un WF
- [[proyectos/MVP_04.02-comfyui-arquitectura/pbook-comfy_setup|pbook-comfy_setup]] — opciones de instalación (movido desde MVP_04)
- [[proyectos/MVP_04.02-comfyui-arquitectura/comfy-tratamiento-datos|comfy-tratamiento-datos]] — privacidad y PI, regla del estudio (movido desde MVP_04)
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] — reglas obligatorias de WF, vive en MVP_04 y se referencia (no se duplica)
- [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|modelos-recomendados]] — guía de modelos por hardware, vive en MVP_04 y se referencia
- [[proyectos/MVP_04-comfyui-arquitectura/PLANS/2026-10-08-plan-tests-24h|plan-tests-24h]] — plan de testeo 24 h, vive en MVP_04 y se referencia
- [[proyectos/MVP_04.02-comfyui-arquitectura/PLANS/PLAN-F1-F8-lora-inpaint-outpaint|PLAN F1-F8]] — 8 flujos nuevos (txt2img→LoRA, inpainting, outpainting), mapeados a WF-02/WF-03 + WF-04 propuesto
- MVP_04 cerrado como lección: [[proyectos/MVP_04-comfyui-arquitectura/RESUMEN-flujos-probados|RESUMEN-flujos-probados]] (23 imágenes, por flujo y corrida)

## Workflows

| WF | Objetivo | Modelo | Estado |
|---|---|---|---|
| [[proyectos/MVP_04.02-comfyui-arquitectura/WF-01-planta-ilustrada/WF-01-planta-ilustrada\|WF-01-planta-ilustrada]] | Planta técnica → planta ilustrada estilo inmobiliaria | ArchitectureRealmix + Canny | en pausa — techo SD1.5 no convence (ver §6) |
| [[proyectos/MVP_04.02-comfyui-arquitectura/WF-02-inpainting-ventanas/WF-02-inpainting-ventanas\|WF-02-inpainting-ventanas]] | Inpainting: dibujar ventanas con máscara | sd-v1-5-inpainting (instalado) | F-01 OK (ventanas dibujadas) |
| [[proyectos/MVP_04.02-comfyui-arquitectura/WF-03-serie-controles/WF-03-serie-controles\|WF-03-serie-controles]] | Serie 5 controles sobre 1 imagen (base→Scribble→Canny→Depth→LoRA) — spec en [[proyectos/MVP_04.02-comfyui-arquitectura/WF-03-serie-controles/SPECS/serie-controles-spec\|serie-controles-spec]] | ArchitectureRealmix + CNs + LoRA A+B | F-A listo para correr (T1/T2/T3) |
| [[proyectos/MVP_04.02-comfyui-arquitectura/WF-04-serie-txt2img/WF-04-serie-txt2img\|WF-04-serie-txt2img]] | Serie txt2img 1.0.0→1.1.2 (+LoRAs) + 2.0.0 SDXL, 6 JSON validados | Realmix + 2 LoRAs + Juggernaut | JSON listos, sin correr |
| [[proyectos/MVP_04.02-comfyui-arquitectura/WF-05-img2img-croquis/WF-05-img2img-croquis\|WF-05-img2img-croquis]] | img2img matriz denoise 0.4/0.6/0.8 sobre base WF-04 | Realmix | JSON listo, espera base-05.png |
| [[proyectos/MVP_04.02-comfyui-arquitectura/WF-06-inpaint-outpaint/WF-06-inpaint-outpaint\|WF-06-inpaint-outpaint]] | inpaint 3.x + outpaint 4.x con modelo inpainting | sd-v1-5-inpainting | JSON listos, esperan base-06.png |

## Convención de archivo único por WF

Cada WF vive en UN solo `WF-<nombre>.md` con 7 secciones: 1. Ficha · 2. Modelo sugerido · 3. Grafo · 4. Prompts · 5. Corridas (más nuevo arriba) · 6. Evaluación · 7. Backlog. El `.json` y los PNG (`inputs/`, `salidas/`) quedan como archivos aparte. Se parte solo si supera ~500 líneas.

## Hardware de esta fase

RX 570 8GB VRAM vía DirectML (conda env `P:\Anaconda\envs\comfyenv`). ComfyUI 0.28.0 en `http://127.0.0.1:8188`. Sin RunPod: todas las pruebas corren en esta PC.
