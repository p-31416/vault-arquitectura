---
tipo: proyecto
cliente: Concurso AI×Gaudí (Fundació Antoni Gaudí + Archademy.ai)
proyecto: "The Gaudí Nexus — Mercado de Proximidad y Centro de Cultura Digital"
ciudad: Barcelona
pais: España
fase: concepto
area_m2:
fecha_inicio: 2026-10-19
fecha_estimada_entrega: 2026-12-16
equipo: [Sol, Emilia]
estado: activo
tags: [concurso, gaudi-nexus, barcelona, comfyui, workflows, rhino, fundacio-gaudi]
---

# The Gaudí Nexus — proyecto de concurso

> Carpeta de trabajo del concurso AI×Gaudí: los siete workflows adaptados del curso, las fichas de flujo que los originan y el criterio con el que se revisan. **Todo el material binario vive en `activos/`** (fuera de git); acá solo texto y referencias.

## Qué hay acá

| Carpeta | Contenido | Puerta de entrada |
|---------|-----------|------------------|
| `flujos/` | Una ficha por módulo del curso: la transcripción del video hecha flujo, con valor de tiempo, prompts literales y la lista de vacíos | [[proyectos/concurso-gaudi-nexus/flujos/00-index\|flujos/00-index]] |
| `workflows/` | Siete workflows ejecutables, uno por módulo, en orden de curso | [[proyectos/concurso-gaudi-nexus/workflows/00-index\|workflows/00-index]] |
| `criterio/` | El checklist del jurado que cierra cada workflow | [[proyectos/concurso-gaudi-nexus/criterio/criterio-jurado\|criterio-jurado]] |

## El plan

[[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|specs/261028-plan-workflows-adaptados-curso-ai-gaudi]] — plan maestro: los siete workflows, la matriz de adaptación del curso a nuestra infraestructura, el método de construcción y revisión uno por uno, los milestones M-C1 a M-C7 y el sprint 1.

## Cómo se trabaja

1. **Ficha de flujo** (`flujos/`): qué dice el video, con timestamp.
2. **Grafo** (`workflows/WF-<nn>/workflow_<nombre>.json`, API format).
3. **Validación estática** contra `/object_info` del servidor destino y contra el disco.
4. **Corridas**: tres A (idénticas) más una B (variante), con el `02-WF-log` completo.
5. **Revisión de Sol** — el gate: el workflow pasa a v1.0 con su `s`.
6. **Cierre**: `01-index` con la configuración mínima, `04-backlog` con lo pendiente y el checklist del jurado satisfied.

## Reglas que aplican

- Los binarios (imágenes, videos, `.dwg`, audio) viven en `activos/`, que está fuera de git. En las carpetas de workflow, las corridas van a `salidas/` (también fuera de git) y se referencian desde el `.md`.
- Cada workflow sigue [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|las reglas de workflows del estudio]]: `00-README` · `01-index` · `02-WF-log` · `03-nodos` · `04-backlog` · `salidas/` · `PLANS/` · `SPECS/` · JSON en API format.
- Las reglas nuevas **R2** (escala según el modelo), **R3** (nomenclatura `gx-{LETRA}-{NN}.png`) y **R4** (validación estática antes de la corrida) viven en ese mismo documento.
- Wikilinks con ruta absoluta desde la raíz y sin extensión.

## El concurso, en tres líneas

**Tema**: coexistence entre turismo de masa y población local en el entorno de la Sagrada Família — un Mercado de Proximidad y un Centro de Cultura Digital, con la reconfiguración de la plaza. **Entrega**: 16/12/2026 23:59 GMT-7, una lámina A1 online de máx. 15 MB en JPEG (+ A4 opcional para el Premio de Diseño). **Criterio de la Fundació**: lógica constructiva, no imitación de estilo.

## Fuentes del proyecto

- [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|Extracción del material del curso AI×Gaudí]] — el tablero Miro, los prompts oficiales y los LoRA
- [[proyectos/STUDIO_OS-Emilia/presentacion/08-propuesta-mes2-cad-urbano|Propuesta CAD → Rhino → ComfyUI → A1]] — la cadena de cartografía urbana
- [[specs/261019-plan-concurso-gaudi-nexus-ia|Plan del concurso]] — inscripción, propiedad intelectual y honorarios
- [[raw/yt/transcripts/indice-curso-ai-gaudi|Índice del curso]] — transcripciones, playback IDs y tablero
- [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] — dónde renderizar y qué cuesta
