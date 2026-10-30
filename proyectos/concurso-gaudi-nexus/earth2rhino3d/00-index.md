---
tipo: indice
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [concurso, gaudi-nexus, earth2rhino, sitio, sagrada-familia, rhino]
idioma: es
---

# earth2rhino3d — importar la locación Sagrada Família a Rhino

> Carpeta de trabajo Fase B: transcripción hecha análisis de los 2 videos referentes + comparativa + plan de implementación. El crudo verbatim vive en `raw/yt/transcripts/`. Los binarios (`.3dm`, mallas, capturas) viven en `activos/` (fuera de git).

## Mapa

| Pieza | Archivo | Estado |
|---|---|---|
| Video 01 — Google Earth to Rhino Free Workflow 2026 | [[proyectos/concurso-gaudi-nexus/earth2rhino3d/ficha-video-01-earth-free-2026\|ficha-video-01]] | transcript 1 cue — demo visual, ver video a mano |
| Video 02 — Google Maps to Rhino in 1 MINUTE (Heron) | [[proyectos/concurso-gaudi-nexus/earth2rhino3d/ficha-video-02-maps-1min-heron\|ficha-video-02]] | transcript 80 líneas completo |
| Comparativa de métodos | [[proyectos/concurso-gaudi-nexus/earth2rhino3d/comparativa-metodos\|comparativa-metodos]] | pendiente validación en Rhino |
| Plan de implementación Rhino | [[proyectos/concurso-gaudi-nexus/earth2rhino3d/plan-implementacion-rhino\|plan-implementacion-rhino]] | Fase C ejecutada 2026-10-29: massing en escena (ver salidas) |
| Comandos copiar | `comandos-rhino-copiar.md` | puente + massing + verificación |

## Massing v01 en escena (2026-10-29, verificado por MCP)

- Base: `activos/.../earth2rhino3d/base/sagrada_overpass.json` (1054 ways, 474 con levels, bbox 600 m templo 41.4036/2.1744).
- Escena: `SF-MASSING-OSM` 1045 sólidos (z 0→37,2) + `TESTIGO-SF` 172,5 m + `SF-ORIGEN`. Bbox x −457…443,6, y −369,7…437,2.
- Salidas: `activos/.../earth2rhino3d/salidas/sf-massing-v01-top.png` (planta Eixample) + `sf-massing-v01-iso.png` (isométrica SE).
- Script: `scripts/construir-massing-sagrada-rhino.py` (plano, sin `def`, extrusión +Z + `CapPlanarHoles`; corrección `System.Guid.Empty`).
- Bitácora: [[proyectos/concurso-gaudi-nexus/earth2rhino3d/bitacora-massing-v01\|bitacora-massing-v01]] (fuentes, alturas, comandos, bugs, pendientes).
- Fotos Commons con thumbnails: [[proyectos/concurso-gaudi-nexus/earth2rhino3d/fotos-plaza-commons\|fotos-plaza-commons]] (10 fotos CC BY-SA verificadas + atribución para el rótulo).
- Pendiente del arquitecto: guardar como `SF-sitio-massing-v01.3dm` + pasar links Commons para el fondo.

## Fuentes crudas

- `raw/yt/transcripts/2026-10-29_uIhX4IYBobc.en.md` (generado por `scripts/transcribir_youtube.py`, fuente `manual-sub`, 1 cue)
- `raw/yt/transcripts/2026-10-29_olUmAJBoMJU.en.md` (generado por `scripts/transcribir_youtube.py`, fuente `auto-sub`, 80 líneas)
- Videos: `https://www.youtube.com/watch?v=uIhX4IYBobc` · `https://www.youtube.com/watch?v=olUmAJBoMJU`

## Regla de honestidad

Cuando el video no dice un valor, la ficha lo marca como **no dicho en el video**. El video 01 es demo visual sin narración: lo no audible se marca como **ver en pantalla** y queda para revisión manual del arquitecto.
