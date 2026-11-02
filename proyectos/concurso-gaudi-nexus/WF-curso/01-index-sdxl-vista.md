---
tipo: indice
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, sdxl, vista]
idioma: es
---

# SDXL vista — un flujo por WF del concurso (solo ver, no ejecutar)

> Set para abrir en ComfyUI con drag-and-drop. **Nada encolado ni ejecutado.** Sin validar contra servidor (R4 pendiente): antes de cualquier corrida, verificar `ckpt_name` en `models/checkpoints/` y los `class_type` en `/object_info`.

## Cómo abrirlos

Arrastrar cada `.json` sobre la ventana de ComfyUI. Los `LoadImage` traen ruta `PONER-RUTA-*.png`: reemplazar por la imagen real al momento de usar.

## Los 7

| WF | Archivo | Ficha | Tipo | Qué es |
|----|---------|-------|------|--------|
| WF-01 protocolo | `workflow_WF-01_sdxl.json` | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-01_sdxl|WF-01]] | txt2img 1024² | Baseline comparativa, seed 7 |
| WF-02 texto-imagen | `workflow_WF-02_sdxl.json` | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-02_sdxl|WF-02]] | txt2img 1216×832 | Interior bóveda catenaria, seed 43 |
| WF-03 rhino-imagen | `workflow_WF-03_sdxl.json` | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-03_sdxl|WF-03]] | img2img denoise 0,65 | Vista Rhino → render, ImageScale bilinear 1024² |
| WF-04 imagen-video | `workflow_WF-04_sdxl.json` | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-04_sdxl|WF-04]] | txt2img 1280×768 | Keyframe plano fijo al atardecer (etapa imagen previa al video) |
| WF-05 imagen-3D | `workflow_WF-05_sdxl.json` | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-05_sdxl|WF-05]] | txt2img 1024² | Maqueta aislada fondo neutro (etapa imagen previa al 3D) |
| WF-06 criterio jurado | `workflow_WF-06_sdxl.json` | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-06_sdxl|WF-06]] | txt2img 1024² | Detalle constructivo, lógica tectónica (el módulo 6 no genera imagen; este flujo la interpreta) |
| WF-07 gaudí workflow | `workflow_WF-07_sdxl.json` | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-07_sdxl|WF-07]] | img2img denoise 0,55 | Pass geometría→piedra, intensidad media (el dial 0-10 se ajusta en `denoise`) |

Base común: `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` · `dpmpp_2m`/`karras` · cfg 4 · 30-35 steps (plantilla: `WF-04-serie-txt2img/workflow_2.0.0_txt2img_sdxl.json`).

## Fichas y modelos

- [[proyectos/concurso-gaudi-nexus/WF-curso/00-base-modelo|00-base-modelo]] — el checkpoint, sus links verificados, los 9 nodos con documentación oficial y los cambios globales.
- [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]] — qué otros SDXL probar en cada WF, licencias, LoRA del curso y protocolo de comparación.
- Cada ficha `WF-0x_sdxl.md` trae: tipo de flujo, modelo, cadena de nodos con doc, parámetros razonados, tabla de cambios factibles y qué mirar en el resultado.

Cada corrida suma una fila en [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|la matriz del concurso]]; el plan de campaña vive en [[specs/261030-plan-continuacion-pruebas|plan de continuación de pruebas]].
