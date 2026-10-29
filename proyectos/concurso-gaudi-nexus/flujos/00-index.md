---
tipo: indice
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [concurso, gaudi-nexus, curso-ai-gaudi, flujos, workflows]
idioma: es
---

# Flujos del curso AI×Gaudí — fichas

> Una ficha por módulo del curso. Cada ficha es la transcripción del video **hecha flujo**: pasos con el nodo exacto y su valor, los prompts literales, las reglas que el instructor explica y la lista de lo que el video deja vacío. Todo lo técnico lleva su `[HH:MM:SS]`.

## Mapa

| Módulo | Ficha | Duración | Qué deja | La consume |
|--------|-------|----------|----------|-------------|
| 1 · Introduction to Generative AI | [[proyectos/concurso-gaudi-nexus/flujos/flujo-01-intro-generative-ai\|flujo-01]] | 1 h 30 min 49 s | La lectura de nodos del grafo base, el protocolo de comparación y la elección de plataforma | WF-01 |
| 2 · Text-to-Image | [[proyectos/concurso-gaudi-nexus/flujos/flujo-02-text-to-image\|flujo-02]] | 47 min 09 s | La comparativa SD1.5 / SDXL / FLUX.1 / FLUX.2 klein 9B y el LoRA al 50 % y al 100 % | WF-02 |
| 3 · Image-to-Image (Rhino-to-Image) | [[proyectos/concurso-gaudi-nexus/flujos/flujo-03-image-to-image\|flujo-03]] | 1 h 22 min 14 s | El grafo Rhino-to-Image, el upscale, la edición con referencias y el inpainting | WF-03 |
| 4 · Image-to-Video | [[proyectos/concurso-gaudi-nexus/flujos/flujo-04-image-to-video\|flujo-04]] | 26 min 22 s | Seedance 2.0, el escalonado en segundos, el time-lapse de trípode fijo y la interpolación de fotogramas | WF-04 |
| 5 · Image-to-3D | [[proyectos/concurso-gaudi-nexus/flujos/flujo-05-image-to-3d\|flujo-05]] | 19 min 33 s | Las nueve preparaciones de imagen, Hunyuan3D y Tripo, y el retorno a Rhino a cota real | WF-05 |
| 6 · Round Table | [[proyectos/concurso-gaudi-nexus/flujos/flujo-06-round-table\|flujo-06]] | sin medir | El criterio del jurado (Cas Esbach): lógica constructiva sobre apariencia | el checklist de cierre de los 7 WF |
| 7 · The Gaudí Workflow | [[proyectos/concurso-gaudi-nexus/flujos/flujo-07-gaudi-workflow\|flujo-07]] | 35 min 42 s | El flujo de dos pasos, el dial de intensidad 0-10 y el INSTRUCTION.md variante B | WF-07 |

## De dónde salen

Las seis fichas transcritas vienen de los subtítulos que el CDN del curso expone sin token (EN y ES, 4.010 cues en total). La transcripción vive cruda en [[raw/yt/transcripts/00-index|raw/yt/transcripts]] y el procedimiento quedó en [[scripts/mux_lecciones_curso_notas|mux_lecciones_curso_notas]].

El módulo 6 no expone subtítulos (404 en sus dos pistas) y se transcribe en local: ver [[proyectos/concurso-gaudi-nexus/flujos/flujo-06-round-table|flujo-06]].

## Cómo se leen

Cada ficha termina con dos secciones añadidas por el estudio:

- **Cómo lo adaptamos** — tabla de tres columnas (`Lo que hace el curso · Lo que hacemos nosotros · Por qué`) con la decisión de infraestructura que convierte el flujo del curso en un workflow ejecutable en nuestra pila.
- **Checks contra el criterio del jurado** — los puntos que cada módulo tiene que cumplir para cerrar el workflow con el criterio del concurso. Se completan cuando la transcripción del módulo 6 esté lista.

## Regla de honestidad

Cuando el video no dice un valor, la ficha lo marca como **"no dicho en el video"**. Los valores que el curso muestra en pantalla sin leer (el prompt JSON, las instrucciones del prompt coach) remiten al tablero del curso, cuyo inventario está en [[raw/research/2026-10-20-miro-curso/miro-inventario|miro-inventario]].
