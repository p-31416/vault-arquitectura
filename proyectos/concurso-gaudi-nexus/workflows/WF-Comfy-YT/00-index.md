---
tipo: indice
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-03
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, indice]
idioma: es
---

# WF-Comfy-YT — Flujos de YouTube analizados

> Carpeta de trabajo sobre videos de ComfyUI: cada video que manda Sol se analiza con la misma plantilla y su JSON queda guardado junto al análisis. Vive junto al set [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/01-index-sdxl-vista|sdxl-vista]] porque los flujos que sirven se prueban con los mismos checkpoints (Juggernaut v9, RealVisXL v5.0).

## Plantilla de análisis (la que pide cada video)

1. **Video**: título, canal, URL, duración, de qué trata.
2. **JSON**: archivo del autor si es abierto; si está tras paywall, reconstrucción local marcada como tal.
3. **Modelo**: nombre, base (SD/SDXL/Flux…), link de descarga, licencia y si corre en la RX 570.
4. **Nodos**: tabla con función en el flujo y link a la doc oficial.
5. **Cuadro de pruebas**: matriz de pruebas (agregar/quitar/cambiar elementos) con máscara, prompt, denoise y qué mirar.
6. **Referencias**: video, archivos, docs.

## Base (unificada 2026-11-02)

Único vigente: [[proyectos/concurso-gaudi-nexus/workflows/00-pod-comfyui-unificado|00 — Pod ComfyUI unificado]] (montar + pagar + instalar + Comfy-vs-pod + n8n start→run→stop con video DorianAI ítem 19). Los 5 `pod-`/`comfy-vs`/`n8n-ciclo` viejos fueron borrados tras verificar que el unificado conserva precios, endpoints, checklists y troubleshooting.

## Videos analizados

| # | Video | Técnica | Modelo | JSON | Estado |
|---|---|---|---|---|---|
| YT-01 | [SDXL Inpainting para arquitectura](YT-01-sdxl-inpainting-diffuseda) (Diffused.A Studio, 2:56) | inpainting + ControlNet opcional | Juggernaut XL + LoRA archviz (sin identificar) | reconstrucción local (`workflow_YT-01-sdxl-inpainting.json`; original tras paywall USD 7,99) | listo para probar |
| YT-02 | [LoRA SDXL con pocas imágenes](YT-02-lora-sdxl-pocas-imagenes) (ítem 15 playlist) | LoRA estilo SDXL dataset chico + regularización | SDXL 1.0 (OpenRAIL) | pendiente extraer al ver | pendiente ver video |
| YT-03 | [SDXL y Flux Inpainting con CropAndStitch](YT-03-sdxl-flux-inpaint-crop-stitch-pixaroma) (pixaroma Ep19) | inpaint crop + stitch, fuerza 1024, blend 32 | Juggernaut XL inpainting (Civitai 403361) | `workflow_YT-03-inpaint-crop-stitch.json` borrador listo, sin correr | instalar pack + checkpoint y probar |
| YT-03 ALT | [Inpaint local SD1.5 sin descargas](YT-03-alt-local-sd15) (variante taller) | VAEEncodeForInpaint core, 512, grow 12, euler cfg 7 | sd-v1-5-inpainting-fp16 (instalado) | `workflow_YT-03-alt-local-sd15.json` validado | listo para pintar máscara y encolar |
| YT-03 | [Cambiar punto de vista desde render propio](YT-03-vista-nueva-desde-render-propio) (propio, 2026-11-03) | img2img SDXL denoise medio, cámara nueva | Juggernaut XL v9 | `workflow_YT-03-vista-nueva.json` (propio, validado R4) | listo para probar con tu render |
| YT-04 | [Rhino vivo por captura manual](YT-04-rhino-vivo-propio) (propio, 2026-11-03) | ControlNet canny SD1.5 + img2img sobre captura Rhino | sd-v1-5-inpainting-fp16 | `workflow_YT-04-rhino-vivo.json` (propio, validado R4) | listo para probar con tu captura |

## Set Nexus (pedido Sol 2026-11-02)

| Doc | Qué cubre |
|---|---|
| [10 prompts prueba Nexus](10-prompts-prueba-nexus) | P-01 a P-10 con visión / estructura / requisitos / modelo (SDXL local vs Flux pod vs cuantizado GGUF) + qué probamos |
| [10 formas Sagrada sin invento](11-diez-formas-sagrada-familia) | F-01 a F-10 fondo fiel → libre, decisión rápida |
| [Reporte corridas YT](20-reporte-corridas-YT) | hoja viva: probamos / sucedió / funcionó, miniatura, config, solución |

## Flujo propio (croquis de Sol)

| Doc | Qué cubre |
|---|---|
| [[proyectos/concurso-gaudi-nexus/workflows/ipadapter-calco-estilo/01-index-ipadapter-calco-estilo\|IPAdapter calco→estilo]] | calco de líneas + editado Photoshop con `style transfer`, previo al LoRA; JSON en la misma carpeta |

## Backlog unificado de futuras pruebas

| Doc | Qué cubre |
|---|---|
| [30-backlog-futuras-pruebas](30-backlog-futuras-pruebas) | lista única: líneas nuevas de Sherlock (iluminación, vistas, LoRA croquis, nodos) + pendientes YT-01–04 y reporte P-01/P-03 + matriz WF-01–07 y backlogs hermanos sin duplicar |

## Cómo pedir el siguiente

Pasar la URL del video. El análisis devuelve: JSON reconstruido o del autor, modelo con link de descarga, nodos con docs y cuadro de pruebas, todo en un `YT-NN-*.md` nuevo en esta carpeta.
