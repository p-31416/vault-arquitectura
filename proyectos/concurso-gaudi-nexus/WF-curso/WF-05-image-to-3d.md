---
tipo: guia
proyecto: concurso-gaudi-nexus
modulo: 5
slug: image-to-3d
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, wf-curso, wf-05, curso-ai-gaudi, sdxl, maqueta, 3d]
idioma: es
---

# WF-05 — Image-to-3D + maqueta aislada 1024²

> Unifica [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-05-image-to-3d\|flujo-05]] + [[proyectos/concurso-gaudi-nexus/WF-curso/WF-05_sdxl\|WF-05_sdxl]].

## 1. Ver en Miro + video

| Fuente | Link |
|--------|------|
| Miro frame MODULE 5 - IMG-2-3D (9 tarjetas) | pendiente link Sol |
| Video módulo 5 (19 min 33 s) | pendiente link Sol |
| Transcripción ES/EN | [[raw/yt/transcripts/2026-10-21_mux-image-to-3d\|transcripción]] |

## 2. Flujo del curso (resumen)

Imagen 2D → preparación Nano Banana Pro (9 variantes, favorita AO map opción 7) → Hunyuan3D 3.0 (face 500k, low poly 126 / normal 105 / geometry barato) o Tripo 3.1 image-to-model / multiview (2+ imgs, v1 frontal+izq+atrás+der) → Export OBJ/FBX → Rhino importar + `zoom` + escala a cota real (ej. diámetro 150 cm → 1,5) + Arctic + captura a Miro.

Fórmula preparación: qué debe ser la salida + qué eliminar + anclaje (`Keep the character…`, `Maintain consistent proportions…`). Forma simple = modelar a mano; compleja = image-to-3D.

## 3. WF SDXL vista

JSON: `workflow_WF-05_sdxl.json` (misma carpeta WF-curso/, original en `workflows/sdxl-vista/`) · txt2img 1024² · seed 5 · prefijo `gx-WF05-prep3d`. Objeto aislado sin contexto, entrada del flujo 3D (Tripo/Hunyuan3D/Meshy).

+ `isolated catenary module maquette, branching fractal column study, neutral grey studio background, soft shadows, product photography, three-quarter view, sharp geometry edges` · − casa + `cluttered background, people`.

## 4. Cómo lo adaptamos

Preparación local SDXL + ControlNet depth/scribble + Depth Anything 3 (cubre AO) · 3D con ComfyUI-3D-Pack (Tripo3D/Hunyuan3D-2) en pod · multiview con 4 prompts de encuadre · OBJ/FBX + Rhino tal cual.

## 5. Checks jurado

AO/geometría pura antes que estética · multiview como economía de información (no inventa la parte de atrás) · escala contra cota de ficha · par imagen+prompt+3D como evidencia del método.
