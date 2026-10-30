---
tipo: plan
proyecto: concurso-gaudi-nexus
slug: earth2rhino-plan-rhino
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [earth2rhino, rhino, plan, sagrada-familia, concurso, fotorrealismo]
idioma: es
---

# Plan de implementación Rhino — massing Sagrada + fondo fotorrealista sin foto propia

> Sin foto propia del sitio. El entorno se cuenta con foto libre (Commons CC) + massing open extruido. Nada Google en la entrega. La malla Google queda solo como referencia interna de calibración, apagada antes de la lámina.

## 0. Decisiones tomadas

- Archivo nuevo: `SF-sitio-massing-v01.3dm`, metros, origen en Plaza Sagrada Família (41.3879, 2.1715), CPlane documentado + nota ETRS89/UTM31N EPSG:25831.
- Capas: `SF-MASSING-OSM` (entrega, sólidos cerrados) · `SF-TERRENO-ICGC` · `TESTIGO-SF` (caja 60×100 m, 172,5 m altura, modelado propio) · `SF-CONTEXTO-GOOGLE` (solo calibración, apagada en lámina) · `REF-FOTO-CC` (plano con foto libre) · `PROPUESTA` (tu volumetría).
- Atribución en rótulo: `Massing: © OpenStreetMap contributors (ODbL) + © ICGC (CC-BY 4.0). Foto fondo: [autor] vía Wikimedia Commons [licencia]. Sin datos Google.`

## 1. Carril concurso (sin pagar)

### Paso 1 — Fotos libres Sagrada (15 min, en navegador)
- Buscar en Wikimedia Commons `Sagrada Família Plaça` con filtro libre comercial (CC-BY / CC-BY-SA). Descargar 2-3 (fachada Pasión + vista Eixample + plaza).
- Guardar en `activos/proyectos/concurso-gaudi-nexus/earth2rhino3d/ref/` + anotar autor + URL + licencia en esta ficha (tabla abajo). La foto vive fuera de git por diseño.

| Foto | Archivo | Autor | Licencia | URL |
|---|---|---|---|---|
| Fachada Pasión NNE | `ref/sf-plaza-pasio-nne.jpg` (26 MB, 4032×6048) | Txllxt TxllxT | CC BY-SA 4.0 | `https://commons.wikimedia.org/wiki/File:Barcelona_-_Plaça_de_la_Sagrada_Família_-_View_NNE_on_La_Sagrada_Família_-_Passion_façade_I.jpg` |
| Fachada Pasión NE | `ref/sf-plaza-pasio-ne.jpg` (24 MB, 4032×6048) | Txllxt TxllxT | CC BY-SA 4.0 | `https://commons.wikimedia.org/wiki/File:Barcelona_-_Plaça_de_la_Sagrada_Família_-_View_NE_on_La_Sagrada_Família_-_Passion_façade_I.jpg` |
| Plaza general | `ref/sf-plaza-general.jpg` (8 MB, 3472×4624) | Renamed user 00b713b85f958b9550f25104393fadb8 | CC BY-SA 4.0 | `https://commons.wikimedia.org/wiki/File:Place_de_la_Sagrada_Família_2.jpg` |

> Nota: las fotos de la basílica muestran la obra en construcción (grúas, andamios): sirven como fondo de contexto y referencia de escala humana, no como estado final.

### Paso 1b — Fotos de la PLAZA como espacio urbano (2026-10-29)

| Foto | Archivo | Autor | Licencia | URL |
|---|---|---|---|---|
| Plaça de Gaudí vista NW | `ref/sf-plaza-gaudi-nw.jpg` (28 MB, 6048×4032) | Txllxt TxllxT | CC BY-SA 4.0 | `https://commons.wikimedia.org/wiki/File:Barcelona_-_Plaça_de_Gaudí_-_View_NW.jpg` |
| Carrer de Provença oeste | `ref/sf-plaza-gaudi-provenza.jpg` (19 MB, 4032×6048) | Txllxt TxllxT | CC BY-SA 4.0 | `https://commons.wikimedia.org/wiki/File:Barcelona_-_Plaça_de_Gaudí_-_View_West_on_Carrer_de_Provença.jpg` |
| Panorámica plaza + Eixample (B/N) | `ref/sf-plaza-gaudi-panorama.jpg` (2,3 MB, 4527×1262) | Flickr upload bot | CC BY-SA 2.0 | `https://commons.wikimedia.org/wiki/File:Placa_de_Gaudi_panorama.jpg` |

### Paso 1c — Segunda tanda plaza (2026-10-29)

| Foto | Archivo | Autor | Licencia | URL |
|---|---|---|---|---|
| Plaça de Gaudí SW (obra, detalle torres) | `ref/sf-plaza-gaudi-sw-pond.jpg` (22 MB, 6048×4032) | Txllxt TxllxT | CC BY-SA 4.0 | `https://commons.wikimedia.org/wiki/File:Barcelona_-_Plaça_de_Gaudí_-_View_SW_on_La_Sagrada_Família_II.jpg` |
| Cola de acceso SE (vida en plaza) | `ref/sf-plaza-queue-se.jpg` (0,2 MB, 1600×1067) | Txllxt TxllxT | CC BY-SA 4.0 | `https://commons.wikimedia.org/wiki/File:Barcelona_-_Plaça_de_la_Sagrada_Família_-_View_SE,_Waiting_in_Queue.jpg` |
| La plaza como square | `ref/sf-plaza-square.jpg` (9 MB, 3472×4624) | Renamed user 00b713b85f958b9550f25104393fadb8 | CC BY-SA 4.0 | `https://commons.wikimedia.org/wiki/File:Place_de_la_Sagrada_Família.jpg` |
| Aérea parque + Eixample | `ref/sf-plaza-aerea.jpg` (13 MB, 4608×3456) | MB-one | CC BY-SA 4.0 | `https://commons.wikimedia.org/wiki/File:Sagrada_Familia,_Barcelona_(P1170690).jpg` |

> La aérea es la pieza clave: parque de la Plaça de Gaudí en primer plano + fachadas Eixample de 7–8 plantas (~24 m, coincide con levels×3,1). Sirve de testigo visual para calibrar las alturas del massing (§2 bitácora). La SW-pond es detalle de obra (material, no plaza).

### Paso 2 — Base open en QGIS (15 min)
- Proyecto QGIS EPSG:25831 → QuickOSM `building=*` en bbox 41.383–41.393, 2.165–2.178 → `sagrada_buildings.gpkg`.
- Sumar WMS ICGC ortofoto 25 cm + WFS Catastro parcelas como control visual.
- Exportar `sagrada_buildings.osm` + `sagrada_met2.tif` (ICGC MET2 2×2 m recortado a 1×1 km) a `activos/.../earth2rhino3d/base/`.

### Paso 3 — Massing en Grasshopper (20 min, puente MCP Rhino)
Precondición puente: en Rhino `_RunPythonScript "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\rhino-mcp-server-rhino.py"` (puerto 9876).
- GH: `HeronSRS EPSG:25831 + SetEAP (41.3879, 2.1715)` → `ImportOSM` → extruir por `height`, sino `levels×3,1 m`, sino `21 m` default manzana Eixample → `ImportTopo (sagrada_met2.tif)` → `MoveToTopo`.
- `Bake` a `SF-MASSING-OSM` (blanco mate) + `SF-TERRENO-ICGC` + `TESTIGO-SF` aparte.
- Validación MCP: `get_scene_summary` + `BoundingBox` contra manzana 133,3 m y altura 172,5 m. Gate humano con captura antes de densificar.

### Paso 4 — Composición fotorrealista sin foto propia (WF-03)
- En Rhino: ubicar `PROPUESTA` al frente, plano `REF-FOTO-CC` con foto CC al fondo (sin trazar geometría sobre foto Google — no hay foto Google en escena de entrega).
- Captura viewport Shaded → WF-03 `rhino-to-image` (SDXL + ControlNet Canny/Depth + LoRA curso): 3 corridas A + 1 B, seed fijo, log en `02-WF-log`.
- La foto CC aporta arquitectura real de la Sagrada; la IA pone luz/material del entorno. Salidas `gx-{LETRA}-{NN}.png` según R3.

### Paso 5 — Cierre
- Apagar `SF-CONTEXTO-GOOGLE` (si se usó para calibrar) antes del render final.
- Checklist jurado: lógica constructiva, trazabilidad de fuentes, atribuciones en rótulo, sin logos Google en imagen.

## 2. Anexo comercial (para después del concurso / encargo real)

| Opción | Qué incluye | Costo | Cuándo |
|---|---|---|---|
| Google Maps Tiles Enterprise | Visualización con billing + key + atribución en pantalla y lámina, sin bakear mesh a entrega | 1K root free/mes, luego por SKU (precio exacto en pricing list) | Solo si se levanta el bloqueo EEA o billing fuera EEA + permiso escrito para impreso |
| Imagery comercial | Nearmap / Airbus Pléiades / vuelo ICGC a pedido + MDT propio → mesh tuyo entregable | A cotizar por km² | Encargo con presupuesto |
| Drone + fotogrametría propia | Ortomosaico + mesh tuyos, 100% entregables | Vuelo + procesado | Sitio accesible + permiso |

## 3. Lo que NO se hace

- No bakear Google Tiles al `.3dm` de entrega ni subirlo a RunPod/pod.
- No trazar footprints sobre screenshot Google (derivado prohibido).
- No guardar API keys en el vault (solo referencia, secret en `.env` gitignored).

## 4. Riesgos y validación

- OSM Eixample puede traer `%` sin `height`: cae al default 21 m — validar a ojo contra ortofoto.
- ICGC `icgc.cat` devolvió 403 a bots: descargar en navegador, no con script.
- Licencias Catastro/Cadmapper-terms todavía gap: no van a lámina final sin verificar `/terms` en navegador.
