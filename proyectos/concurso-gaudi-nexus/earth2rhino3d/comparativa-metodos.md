---
tipo: comparativa
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [earth2rhino, comparativa, heron, google-3d-tiles, open-data, sagrada-familia]
idioma: es
---

# Comparativa — video 01 vs video 02 + vía limpia open-data

> Decide qué se replica en Rhino para la Sagrada Família. Fuentes: [[proyectos/concurso-gaudi-nexus/earth2rhino3d/ficha-video-01-earth-free-2026\|ficha-video-01]] · [[proyectos/concurso-gaudi-nexus/earth2rhino3d/ficha-video-02-maps-1min-heron\|ficha-video-02]].

## Tabla

| Eje | Video 01 Earth free 2026 | Video 02 Maps 1 min Heron | Vía limpia open-data (propuesta estudio) |
|---|---|---|---|
| Herramienta | Plugin no identificado, exige Chrome cerrado (ver en pantalla) | Heron 0.5.0 + `Google 3D Tiles IOI` en GH | Heron OSM / Elk + ICC / Catastro (sin Google) |
| Entrada | Área en Google Earth (ver en pantalla) | lat,lon de Google Maps → Anchor + boundary | lat,lon + boundary + catastro ICC |
| Salida | Malla Earth (ver en pantalla) | Malla Google texturada, bake a Rhino | Sólidos cerrados por manzana, alturas OSM/catastro |
| Costo | Gratis (según título) | Gratis 90 días, luego Cloud facturado | Gratis, sin API key de Google |
| LOD / control | No dicho (ver en pantalla) | LOD 0–20, arrancar en 13 | LOD propio: extrusion por altura |
| Georreferencia | No dicha | No dicha (origen del bake sin documentar) | Origen declarado en plaza + nota ETRS89/UTM31N |
| Licencia entrega | ToS Google Earth (no apto como base final) | ToS Google Maps Tiles (no apto como base final) | Open-data (apto para pod, render y lámina) |
| Peso en RX 570 8 GB | No dicho | Riesgo LOD alto → paginado a RAM | Liviano: primero massing, luego detalle |
| Estado en vault | Transcript 1 cue válido, falta ver pantalla | Transcript 80 líneas completo, replicable | A validar en Fase C |

## Decisión del estudio (propuesta)

1. Replicar el **video 02** como capa de calibración `SF-CONTEXTO-GOOGLE` (rápida, texturada, LOD 13).
2. Reconstruir el massing de entrega en `SF-MASSING-OSM` con open-data (sin ToS Google).
3. El **video 01** queda en espera hasta identificar el plugin viendo 2 min de pantalla; si es scrape Earth, cae en la misma restricción que el 02.
4. Ninguna malla Google sale a cloud/pod ni a la lámina final (regla auditada PI terceros).

## Riesgos abiertos

- El bake Heron puede llegar en grados o en origen desplazado: validar con `BoundingBox` contra manzana Eixample y altura 172,5 m.
- La API key Google vive en `.env`, nunca en el vault ni en git.
- Video 01 sin audio: la identificación del plugin exige revisión manual.
