---
tipo: research
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [research, massing, caba, buenos-aires, earth2rhino, open-data, osm, cadmapper, tejido-urbano, overpass]
idioma: es
---

# Massing 3D en CABA — fuentes abiertas verificadas y opciones (reutilización del flujo Sagrada)

> Fecha: 2026-11-01 | Base: [[proyectos/concurso-gaudi-nexus/earth2rhino3d/doc-massing-03d-sagrada|doc-massing-03d-sagrada]] (flujo Barcelona) + verificación propia de hoy. Cada dato dice si está **verificado** (fetch 200 / API CKAN) o es **gap** (a confirmar en navegador).

## Resumen

- El flujo Barcelona es **location-agnóstico**: Overpass es global y la conversión lat/lon→metros es equirectangular local (los scripts de `scripts/` aceptan cualquier lat/lon). Lo que cambia por ciudad: el CRS de referencia, la regla de alturas cuando falta dato y, sobre todo, la fuente de alturas.
- **Hallazgo clave**: el GCBA publica el dataset **Tejido Urbano** con **altura real en metros por volumen edificado** (restitución 2013, actualización 2017) + pisos sobre/bajo rasante, licencia **CC-BY-2.5-AR**, descarga directa en SHP, CSV, GeoJSON y XLSX. En Barcelona el 45 % de las alturas salía de OSM (`levels`); en CABA existe una fuente oficial municipal que las reemplaza de base.
- Densidad OSM en CABA: quedó sin medir hoy (los endpoints Overpass rechazaron o demoraron los GET desde el entorno). Link de Overpass Turbo abajo para verificarlo en el navegador.

## Opciones evaluadas (todas aptas massing 600×600, en metros)

| # | Fuente | Qué entrega | Altura | Costo | Licencia | Estado de verificación |
|---|---|---|---|---|---|---|
| 1 | **Tejido Urbano GCBA** ([dataset](https://data.buenosaires.gob.ar/dataset/tejido-urbano)) | Volúmenes edificados de la CIUDAD ENTERA, por barrio | **Sí — `alt_2013`/`alt_2017` en metros reales** (restitución aérea) + `altos` = pisos + `bajos` = subsuelo | 0 | CC-BY-2.5-AR (algunos recursos CC-BY-4.0) | ✅ VERIFICADO: API CKAN 200, campos y URLs de recursos listados; descarga pendiente de abrir |
| 2 | **OpenStreetMap** vía Overpass (mismo flujo Barcelona) | Footprints + `building:levels` | Parcial: `levels × 3,1 m` (en Barcelona 580/1054 quedaron en default 21 m) | 0 | ODbL 1.0 | ✅ Servible — densidad CABA pendiente de medir |
| 3 | **CADMapper** | `buenos-aires` listado en Whole City Files (DXF 2D: viales + agua) | 3D con alturas: `available in many locations` — por ciudad se confirma en la app | 0 (whole city) · 1 km² free con signup | ODbL heredado; /terms sigue siendo gap (informe 2026-10-29) | ✅ ciudad listada · ⚠ 3D CABA sin verificar |
| 4 | **CAD ATLAS** ([buenos-aires](https://cad-atlas.com/city/buenos-aires/)) | DWG/SKP/IFC con footprints + calles de ancho real + sombras vectoriales + DEM (centro 1 km²: >5400 edificios) | "Alturas reales" + estimación con algoritmo entrenado (OSM + Overture + catastro) | Pagado (prueba free + acceso gratis estudiantes .edu/.ac) | No declarada en la página visitada | ✅ página verificada hoy · ⚠ licencia gap |
| 5 | **Anyscape** ([buenos-aires](https://anyscape.io/3d-city-models/buenos-aires/)) | Modelo 3D entero: edificios (LoD1) + calles + terreno, entregado en CRS nacional (EPSG:5343/5344/5345) | Overture Maps Buildings LoD1 (ODbL) + terreno IGN Argentina MDE-Ar DTM 5 m | Pagado | ODbL según declarado | ✅ página verificada hoy · ⚠ licencia de producto sin leer |
| 6 | **LiDAR "Edificios Públicos 3D"** GCBA | Nubes LAS de 9 edificios públicos icónicos (Cabildo, Casa Rosada, Catedral, CCK, Congreso, Dique 3, Legislatura, Teatro Colón, TSJ) | Detalle real de esos monumentos | 0 | CC-BY-2.5-AR | ✅ VERIFICADO vía API CKAN (9 recursos LAS/ZIP listados) |

## Cómo se maneja BA Data (portal de datos abiertos del GCBA)

- Es un portal **CKAN** estándar: cada dataset tiene metadatos + lista de **resources** (archivos descargables).
- Dos formas de consumo:
  1. **Navegador**: `data.buenosaires.gob.ar/dataset/<nombre>` → botones por formato (SHP/CSV/GeoJSON/XLSX) → descarga directa desde el CDN `cdn.buenosaires.gob.ar`.
  2. **API** (verificada hoy 200): `data.buenosaires.gob.ar/api/3/action/package_show?id=tejido-urbano` → JSON con campos exactos, licencias y URL de cada archivo. También funciona `package_search?q=...` para descubrir datasets.
- Licencias observadas: la mayoría de los datasets destacados son **CC-BY-2.5-AR** (apto lámina con atribución `© Gobierno de la Ciudad de Buenos Aires`); algunos recursos individuales declaran CC-BY-4.0.
- Antigüedad: el Tejido Urbano declará "datos hasta el 2021" (restitución 2013 + actualización 2017). Para barrios con tormenta de obras recientes (Puerto Madero, Catalinas, Palermo Soho) conviene contrastar con OSM, que sí ve lo nuevo.
- Geometría: poligonos 2D + atributos (alturas) — llega como mismo patrón del flujo: footprint + altura → extrusión. El SHP trae ~35 campos del catastro (sección-manzana-parcela, áreas, pisos); el GeoJSON trae una versión reducida de 8 campos (id, smp, altura, altos, origen, tipo, fuente).

### Links verificados hoy

- Tejido Urbano: `https://data.buenosaires.gob.ar/dataset/tejido-urbano`
- API metadatos: `https://data.buenosaires.gob.ar/api/3/action/package_show?id=tejido-urbano`
- Descargas directas (patrón CDN): `.../secretaria-de-desarrollo-urbano/tejido-urbano/tejido.zip` · `tejido.geojson` · `tejido.csv` · `tejido.xlsx`
- Edificios Públicos en 3D (LiDAR): `https://data.buenosaires.gob.ar/dataset/edificios-publicos-3d`
- Visor de referencia de la capa Tejido: [cambalache.coop.ar — GEO 3D](https://cambalache.coop.ar/mapas/maplibre/3d.html)

## Médición OSM CABA — verificación en el navegador (sin código)

- Query lista con mapa centrado en el Obelisco (~600 m): [Overpass Turbo — bbox CABA](https://overpass-turbo.eu/?Q=%5Bout%3Ajson%5D%5Btimeout%3A90%5D%3B%28way%5B%22building%22%5D%28-34.6065%2C-58.3846%2C-34.6015%2C-58.3786%29%3Brelation%5B%22building%22%5D%28-34.6065%2C-58.3846%2C-34.6015%2C-58.3786%29%3B%29%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B&C=-34.604%3B-58.3816%3B15)
- Mapa navegable del mismo recorte: [openstreetmap.org — CABA centro](https://www.openstreetmap.org/#map=16/-34.6037/-58.3816)

## Pendientes / gaps

1. **Descargar Tejido.zip y abrir el .prj** → definir CRS real (BA Data suele entregar 2D en algún Gauss-Krüger/POSGAR o 4326; se confirma al abrir). El flujo equirectangular local < 1 m error en 600 m red indiependiente del CRS de origen.
2. **Densidad OSM CABA** (equivalente del "1054 · 474 con levels" Barcelona) → Overpass Turbo arriba o script `scripts/test-overpass-caba.py` (la vía shell/HTTP falló hoy por TLS y timeouts).
3. **Licencia CADMapper /terms** para entrega comercial (gap abierto desde el informe 2026-10-29 de @sherlock).
4. **IGN Argentina MDE-Ar 5 m** (terreno): citado como fuente por Anyscape; verificar disponibilidad y licencia directa en ign.gob.ar.
5. Default 21 m del Eixample **NO aplica en CABA** → con Tejido Urbano la regla de default casi no se usa; si queda algún nil, usar `piso_2017 × 3,1 m`.

## Recomendación operativa (equivalente Barcelona, paso a paso)

1. **Alturas de base**: nuevo `descargar-tejido-caba.py` (calco de `descargar-osm-sagrada.py`: GET CDN → descomprimir → filtrar por bbox → extraer `alt_2017` sobre `alt_2013` sobre `piso × 3,1`) → massing `GCBA-MASS` con alturas reales oficiales.
2. **Contexto y control cruzado**: capa OSM para calles/verde + CADMapper DXF whole city 2D como contraste de geometría (igual que el overlay OSM↔CADMapper de Sagrada).
3. **Monumentos con detalle**: solo si el proyecto toca Puerto Madero/Plaza de Mayo → nubes LAS del dataset Edificios Públicos 3D.
4. **Atribución en lámina**: `Tejido Urbano © Gobierno de la Ciudad de Buenos Aires (CC-BY 2.5 AR) + Massing © OpenStreetMap contributors (ODbL). Sin datos Google.`

## Fuentes

- GCBA. Subsecretaría de Planeamiento. (2020–2021). *Tejido Urbano* (es). https://data.buenosaires.gob.ar/dataset/tejido-urbano — [CC-BY-2.5-AR; campos y recursos verificados vía API CKAN 2026-11-01]
- GCBA. (2019–2021). *Edificios Públicos en 3D (LiDAR LAS)* (es). https://data.buenosaires.gob.ar/dataset/edificios-publicos-3d — [CC-BY-2.5-AR; verificado vía API 2026-11-01]
- CADMAPPER. (s.f.). *Worldwide map files* (en). https://cadmapper.com/ — [buenos-aires en Whole City Files Sudamérica; verificado 2026-11-01]
- Anyscape. (s.f.). *Buenos Aires 3D City Model* (en). https://anyscape.io/3d-city-models/buenos-aires/ — [Overture ODbL + IGN MDE-Ar; verificado hoy, producto pagado]
- CAD ATLAS. (s.f.). *Buenos Aires Site plan* (en). https://cad-atlas.com/city/buenos-aires/ — [OSM/Overture/catastro + DEM NASA/ESA; verificado hoy, pagado]
- Cambalache Coop. (s.f.). *GEO 3D — visor capa Tejido* (es). https://cambalache.coop.ar/mapas/maplibre/3d.html — [verificado hoy]
- Previo @sherlock: [[raw/research/2026-10-29-earth2rhino-open-alternativas|2026-10-29-earth2rhino-open-alternativas]] (ToS Google, ICGC, Copernicus, comparativa completa).

## Candidatos Nivel 2 (esperan `s`)

1. Descargar Tejido.zip → chequear .prj (CRS) y volumen de datos — da cierre al pendiente 1.
2. `scripts/test-overpass-caba.py` con `P:\Anaconda\envs\comfyenv\python.exe` — medición real de densidad OSM (la vía shell falló por TLS).
3. leer licencia CAD AtLAS y Anyscape antes de considerarlas para entrega.
