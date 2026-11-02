---
tipo: indice
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, wf-curso, curso-ai-gaudi, flujos, sdxl]
idioma: es
---

# WF-curso — flujos del curso + WF SDXL en un solo documento por flujo

> Unifica [[proyectos/concurso-gaudi-nexus/WF-curso/00-index-flujos-origen|flujos/]] (transcripción del video hecha flujo) con [[proyectos/concurso-gaudi-nexus/WF-curso/01-index-sdxl-vista|sdxl-vista]] (WF SDXL solo-vista). Un documento por flujo. Esta carpeta es la que mira el canvas de Miro y los videos del concurso.

## Mapa

| WF | Módulo curso | Ficha unificada | Origen curso | Origen SDXL | Miro frame | Video |
|----|--------------|-----------------|--------------|-------------|------------|-------|
| WF-01 | 1 · Introduction to Generative AI | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-01-intro-generative-ai\|WF-01]] | [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-01-intro-generative-ai\|flujo-01]] | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-01_sdxl\|WF-01_sdxl]] | pendiente link Sol | pendiente link Sol |
| WF-02 | 2 · Text-to-Image | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-02-text-to-image\|WF-02]] | [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-02-text-to-image\|flujo-02]] | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-02_sdxl\|WF-02_sdxl]] | pendiente link Sol | pendiente link Sol |
| WF-03 | 3 · Image-to-Image (Rhino-to-Image) | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-03-image-to-image\|WF-03]] | [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-03-image-to-image\|flujo-03]] | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-03_sdxl\|WF-03_sdxl]] | pendiente link Sol | pendiente link Sol |
| WF-04 | 4 · Image-to-Video | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-04-image-to-video\|WF-04]] | [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-04-image-to-video\|flujo-04]] | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-04_sdxl\|WF-04_sdxl]] | pendiente link Sol | pendiente link Sol |
| WF-05 | 5 · Image-to-3D | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-05-image-to-3d\|WF-05]] | [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-05-image-to-3d\|flujo-05]] | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-05_sdxl\|WF-05_sdxl]] | pendiente link Sol | pendiente link Sol |
| WF-06 | 6 · Round Table (jurado) | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-06-round-table\|WF-06]] | [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-06-round-table\|flujo-06]] | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-06_sdxl\|WF-06_sdxl]] | pendiente link Sol | pendiente link Sol |
| WF-07 | 7 · The Gaudí Workflow | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-07-gaudi-workflow\|WF-07]] | [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-07-gaudi-workflow\|flujo-07]] | [[proyectos/concurso-gaudi-nexus/WF-curso/WF-07_sdxl\|WF-07_sdxl]] | pendiente link Sol | pendiente link Sol |

## JSON en esta misma carpeta

Cada ficha + su `.json` conviven acá para abrir con drag-and-drop. Copias de `workflows/sdxl-vista/` al 2026-11-02 (originales intactos):

- `workflow_WF-01_sdxl.json` · `workflow_WF-02_sdxl.json` · `workflow_WF-03_sdxl.json` · `workflow_WF-04_sdxl.json`
- `workflow_WF-05_sdxl.json` · `workflow_WF-06_sdxl.json` · `workflow_WF-07_sdxl.json`
- `workflow_inpaint-loggia-local_sdxl.json` (inpaint loggia, queda para WF-03)

## Cómo se lee cada ficha

1. **Ver en Miro + video** — frame del canvas y link del video (los completa Sol).
2. **Flujo del curso** — resumen del video con timestamps, prompts literales y vacíos.
3. **WF SDXL vista** — nodos, parámetros y JSON para abrir con drag-and-drop.
4. **Cómo lo adaptamos + checks jurado** — decisión local vs nube.

Base común SDXL: [[proyectos/concurso-gaudi-nexus/WF-curso/00-base-modelo|00-base-modelo]] · modelos a probar: [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]] · matriz: [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz]].

## Regla

El detalle verbatim queda en la ficha origen. Acá solo el resumen operativo + el WF. Si el video no dice un valor, se marca **no dicho en el video**.
