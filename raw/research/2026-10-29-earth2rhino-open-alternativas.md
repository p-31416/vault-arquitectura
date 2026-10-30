---
tipo: research
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [research, sherlock, earth2rhino, google-3d-tiles, rhino8, heron, os-data, sagrada-familia, concurso]
idioma: es
---

# Earth2Rhino open — dónde dice Google que 3D es privado + alternativas abiertas a Rhino 8 (Sagrada Família / Eixample)

> Fecha: 2026-10-29 | Fuentes N: 24 (9 webfetch 200 + 15 search-snippets citadas) | Confianza: Alta (ToS oficial Google + Policies + Heron releases) / Media (licencias ICC/Copernicus por snippet, Catastro gap) / Baja (precios exactos USD por SKU — no dichos en páginas fetchadas)

## Resumen

- **Google sí lo dice, en 4 lugares:** (1) `Google Maps Platform ToS §3.2.3 (a) No Scraping / (b) No Caching / (c) No Creating Content`, (2) `Map Tiles API Policies §Pre-fetching, caching, or storage` (prohíbe image analysis, geodata extraction, offline uses), (3) `Google Earth Additional Terms §2 Prohibited Conduct` (no copiar, no mass download, no crear dataset sustituto), (4) `Geo Guidelines §Google Earth Web and apps — don't do this: You may not use output, or use third party tools to capture output, from Google Earth, Google Earth Pro, or Earth Studio to reconstruct 3D models`.
- **El bake Heron `G3DTilesAoi / G3DTilesPoi` NO transfiere propiedad:** requiere Cloud project + billing + API key propia habilitada en `Map Tiles API`; cada root tileset = evento facturable (Enterprise SKU); el mesh importado sigue siendo `Google Maps Content` bajo licencia no-exclusiva, no-transferible, no-sublicenciable. Llevarlo a lámina de concurso pública, a PDF impreso, o a RunPod/cloud = redistribución / creación de contenido derivado → prohibido sin autorización escrita. Heron lo mitiga regenerando filenames por sesión y con cache local purgable, pero no lo legaliza.
- **Bloqueo EEA crítico para Barcelona:** desde 2025-07-08 rige `Google Maps Platform EEA ToS`; `Photorealistic 3D Tiles` + `2D Satellite` bloqueados para billing accounts EEA (reportado por usuaria Jess en Discourse McNeel 2026-01-13, y nota oficial `Before you begin — EEA developers`). Con facturación española, el trial no habilita 3D Tiles. No dicho el detalle de qué tiles alternativos sí devuelven.
- **Trial 90 días / $300:** Google Cloud $300 trial sí aplica a Maps (FAQ oficial), pero Map Tiles exige billing habilitado + API key/OAuth en cada request. Desde 2025-03-01: Essentials 10K free / Pro 5K / Enterprise 1K free calls por SKU/mes (3D Tiles = Enterprise → 1K). Cuotas: 10.000 root tileset/día, renderer tiles ilimitados por 3h por sesión, 12.000 q/min. Precio USD exacto por root request = no dicho en páginas fetchadas (remite a pricing list).
- **Ruta open recomendada Sagrada (sin API key Google):** `QGIS + QuickOSM (footprints Eixample) + ICGC MDT2/MDS + Catastro Inspire GML + Heron ImportOSM / Elk OSMData → extrusión por height/levels → Rhino 8 metros en ETRS89/UTM31N EPSG:25831`. Templo 172,5 m como testigo aparte (modelado propio, no extruido de OSM). Todo CC-BY / ODbL apto concurso con atribución en lámina.

## Ejes

### 1. Dónde dice Google que es privado/restringido — cláusulas exactas

**1a. Google Maps Platform ToS — §3.2.3 Restrictions Against Misusing the Services (verificado 200 https://cloud.google.com/maps-platform/terms):**

> "3.2.3 (a) No Scraping. Customer will not export, extract, or otherwise scrape Google Maps Content for use outside the Services. For example, Customer will not: (i) pre-fetch, index, store, reshare, or rehost Google Maps Content outside the services; (ii) bulk download Google Maps tiles, Street View images, geocodes, directions, distance matrix results, roads information, places information, elevation values, and time zone details;" [trad. propia — no oficial: el Cliente no exportará, extraerá ni raspará Contenido de Google Maps para uso fuera de los Servicios]

> "(b) No Caching. Customer will not cache Google Maps Content except as expressly permitted under the Maps Service Specific Terms." [trad. propia: no almacenará en caché salvo lo expresamente permitido]

> "(c) No Creating Content From Google Maps Content. Customer will not create content based on Google Maps Content. For example, Customer will not: (i) trace or digitize roadways, building outlines [...] (ii) create 3D building models from 45° Imagery [...] (iii) build terrain models based on elevation values [...] (vii) use Google Maps Content to improve machine learning models..." [trad. propia]

§3.1 License Grant: `non-exclusive, non-transferable, non-sublicensable license` + §3.2.1(b) `will not sell, resell, sublicense, transfer, or distribute the Services` + §10.6(c) `Customer will delete Software and any content from the Services by termination`.

**1b. Map Tiles API Policies — §Pre-fetching, caching, or storage (verificado 200 https://developers.google.com/maps/documentation/tile/policies):**

> "you must not pre-fetch, index, store, or cache any Content except under the limited conditions stated in the terms. Specifically, applications should use Map Tiles API for map visualizations. You may not use Map Tiles API for any non-visualization use cases, such as: Image analysis / Machine interpretation / Object detection or identification / Geodata extraction or resale / Offline uses" [trad. propia]

> "#### Geodata overlays with Photorealistic 3D Tiles — You may overlay your own 3D objects on Photorealistic 3D Tiles as long as the 3D objects aren't extracted, traced, or otherwise derived by hand or machine from Photorealistic 3D Tiles." [trad. propia: podés superponer objetos propios siempre que no sean extraídos/trazados/derivados de los 3D Tiles]

Atribución obligatoria: logo `Google Maps` + `asset.copyright` por tile glTF agregado en línea al pie del render; con Cesium `showCreditsOnScreen: true`. Prohíbe superponer/oscurecer logos.

**1c. Google Earth End User Additional Terms — §2 Prohibited Conduct (verificado 200 https://www.google.com/help/terms_maps-earth/, Last Modified 2025-06-04):**

> "2.1 redistribute or sell any part of Google Earth or create a new product or service based on Google Earth; 2.2 copy the content (unless permitted by Geo Guidelines permissions page or fair use); 2.3 mass download or create bulk feeds; 2.4 use Google Earth to create or augment any other mapping-related dataset [...] for use in a service that is a substitute for [...] Google Earth" [trad. propia]

§1 License: solo `view and annotate / create KML / publicly display with proper attribution online, in video, and in print` — no menciona export mesh.

**1d. Geo Guidelines — Brand Resource Center (verificado 200 https://about.google/brand-resource-center/products-and-services/geo-guidelines):**

> "You may not use output, or use third party tools to capture output, from Google Earth, Google Earth Pro, or Earth Studio to reconstruct 3D models or create similar content, or to create other content, products, or services that may violate our Terms of Service." [trad. propia: no podés usar salida ni herramientas de terceros para capturar salida de Earth/Pro/Studio para reconstruir modelos 3D]

> "Google Earth may not be embedded online or in apps. [...] export and use a handful of static images, with proper attribution, for non-commercial purposes" + "Google Earth content may not be used for any commercial or promotional purposes." [trad. propia]

> "Google Earth content can never be used without attribution." Lámina de concurso = uso comercial/promocional + distribución impresa → fuera de `Go for it` (solo libros ≤5k, reports, presentaciones con fair use).

**Diferencia Earth Pro desktop vs Maps Tiles API vs Earth Studio:**

- Earth Pro desktop: licencia end-user gratuita, solo visualización/anotación/KML, prohíbe scraping/reconstrucción 3D (1c+1d). No hay API key, no hay bake a mesh.
- Maps Tiles API (incl. Photorealistic 3D Tiles): licencia developer con billing, permite visualización inmersiva vía renderer compatible (CesiumJS ≥1.91), pero cada uso sigue atado a 1a+1b. Es la única vía que Heron usa.
- Earth Studio: herramienta de animación/video, exige atribución + registro; su salida tampoco puede reconstruir 3D (cita 1d). Video promo ≤30s solo para Maps API, Street View excluido.

**Trial y facturación (verificado 200 https://developers.google.com/maps/documentation/tile/usage-and-billing + https://mapsplatform.google.com/pricing/ + https://developers.google.com/maps/documentation/tile/3d-tiles):**

- Trial: `Yes, you can [use $300 trial] (see Billing Account Credits)` + `New customers get $300 trial credit`. Debe habilitar billing por proyecto + API key/OAuth.
- Desde 2025-03-01: Essentials 10K free / Pro 5K / Enterprise 1K free calls por SKU/mes. 3D Tiles = Enterprise → 1K root requests/mes free. Antes: $200 monthly credit hasta 2025-02-28 (página usage-and-billing aún lo cita — desactualizada).
- Cuotas: 10.000 root tileset/día, sesión 3h de renderer tiles, ilimitados renderer tiles/día, 12.000 q/min.
- Precio USD/root request exacto: **no dicho** en páginas fetchadas (remite a `Global pricing list`). Gap.
- EEA: `If your billing address is in EEA, effective 8 July 2025 EEA ToS will apply [...] certain content will no longer be returned` + Discourse Jess 2026-01-13: `Photorealistic 3D Tiles - Blocked for EEA billing accounts / 2D Satellite Tiles - Also blocked`. Para estudio con billing ES, ruta Google inviable. Verificar con cuenta propia.

### 2. Caso Heron Google 3D Tiles IOI — de dónde saca data, de quién es el bake, ¿a lámina/cloud?

- **Fuente data (verificado 200 https://github.com/blueherongis/Heron/releases v0.5.0 2026-01-10 + v0.5.1):** `G3DTilesAoi` (boundary + LOD/zoom 0-20) y `G3DTilesPoi` (boundary + POI + Max SSE + K). `You must provide your own Google Maps Platform API key (HERONGOOGLEAPIKEY env var)` + habilitar `Map Tiles API` en Cloud Console + archivo geoide `egm08_25.gtx (145 MB)` para elevaciones. Requiere Rhino 8+ (import GLB) solo PC. Descarga tiles vía `GoogleTilesApi.GetRootTileset()`, cache local con manifest hash, `Clear Cache Before Download` en menú, `Max Size (GB)`.
- **Hilos McNeel Discourse Brian Washburn (search-snippet, no fetch 200 — citar como snippet):** `discourse.mcneel.com/t/google-street-view-to-grasshopper/199389` — Brian 2026-01-10 anuncia componentes por contribución Nico Azel @Nicolas_Azel (PR #57 `Dev google 3d tiles`); 2026-02-13 explica `each downloaded tile counts as an event`, `Google will generate new filename for same tile per session, making reuse difficult — helps comply with terms`; recomienda `start with low LOD`. Error 403 = key sin habilitar Maps 3D Tiles o billing EEA.
- **¿De quién es el bake?** Del Cliente solo la escena Rhino; el contenido sigue siendo `Google Maps Content` (ToS §6 Google retains IP in Core Services). Licencia no transfiere propiedad. Bake = copia/derivado almacenado fuera de Services → cae en `No Scraping (i) store/reshare/rehost` + `No Creating Content`. Heron cachea GLB con SHA1 de URL (evita leak de key) pero el `.glb` + mesh bakeado en `.3dm` sigue siendo contenido Google.
- **¿Puede ir a lámina de concurso o RunPod?** No. Lámina pública impresa/PDF/web = `distribute / rehost / include in electronic or printed documents` (Cesium Appx B-2 §3.a.vi `will not include any Google Maps Content in any electronic or printed documents`, citado vía search-snippet https://cesium.com/legal/terms-for-google/). Subir `.3dm`/GLB a RunPod = `store outside services + rehost + third-party access` + viola mandato vault `planos legales nunca en cloud` (ver informe RunPod 2026-10-28). Uso permitido: visualización interna efímera con atribución, sin extraer medidas (`programmatically reading measurements is considered derivative and prohibited` — blog Photorealistic FAQ Lisa Bos/Danbi Lee 2023-08-09, snippet). Para concurso: usar solo como referencia de massing interno, no entregar.
- **Videos base vault:** `olUmAJBoMJU` (How to Rhino, 1 MINUTE, Heron 0.5.0, LOD 13, trial 90 días, bake Custom Preview) y `uIhX4IYBobc` (Earth Free 2026, 1 cue) — describen flujo técnico, no mencionan ToS/EEA/límites. No dicen licencia.

### 3. Alternativas abiertas a Rhino 8 — fuente, cobertura Sagrada, LOD, entrada Rhino, costo, licencia concurso, límites

**3a. OSM vía Heron ImportOSM / Elk OSMData (recomendado base):**
- Fuente: OpenStreetMap.org export `.osm` XML (openstreetmap.org/export, Overpass API, BBBike/Geofabrik para distritos). Heron `RESTOSM/ImportOSM` + Elk `Location → OSMData (Create 3D Buildings)` (verificado snippet https://www.food4rhino.com/en/app/elk + tutorial Columbia GSAPP).
- Cobertura Eixample/Sagrada: total (footprints + calles + `building:levels`, `height`, `building:part`). Calidad Barcelona alta (import IGN/CC-BY + comunidad).
- LOD real: 2.5D — footprint extruido por `height` > `levels × heightPerLevel_` > random range. Sin cubiertas ni textura fotoreal. Sagrada misma: footprint existe pero altura 172,5 m NO usar OSM — modelar testigo aparte.
- Entrada Rhino 8: Heron set `EarthAnchorPoint + HeronSRS EPSG:25831 + ImportOSM → breps → Mesh`; Elk `Bldg output → Deconstruct Brep`. Nativo GH, sin key.
- Costo: 0.
- Licencia concurso: **ODbL 1.0** (verificado 200 https://www.openstreetmap.org/copyright): `free to copy, distribute, transmit and adapt, as long as you credit OSM and contributors. If you alter/build upon, distribute result only under same license`. Atribución en lámina: `© OpenStreetMap contributors / Map data © OpenStreetMap, disponible bajo ODbL https://www.openstreetmap.org/copyright`. Produced Work (imagen/lámina) solo requiere atribución visible próxima, no share-alike del diseño; Derived Database (GDB con alturas mejoradas) sí compartir si se distribuye. Apto concurso público con atribución. OSM tiles `tile.openstreetmap.org` NO para uso comercial pesado — bajar data, no tiles.
- Límites/peso: export OSM web ~50k nodos; para Eixample 500×500 m usar Overpass/QuickOSM. Mesh liviano (<50 MB) apto PC 8 GB.

**3b. Cadmapper (atajo DXF/SKP sin GH):**
- Fuente: OSM + NASA + USGS procesados (verificado 200 https://cadmapper.com/).
- Cobertura: lista `barcelona` en Whole City Files (2D roads+water DXF gratis sin cuenta). 3D con alturas `available in many locations` — Barcelona 3D = no garantizado, verificar en app.
- LOD: massing extruido + topografía donde hay dato; sin textura.
- Entrada Rhino: web `Create File → DWG/DXF/SKP → Import Rhino 5+`. Sin plugin.
- Costo: Whole Cities free + `Up to 1 km2 free (signup)` + `Up to 100 km2 premium small fee (academic discount)`. Sagrada cabe en 1 km2 free (manzana 133 m → 7×7 manzanas ≈ 1 km).
- Licencia concurso: **no dicha** en página fetchada (remite a https://cadmapper.com/terms — no fetchada). Marcar gap: asumir ODbL heredado de OSM + atribución OSM, pero verificar terms antes de entregar. Apto borrador, no entrega sin leer terms.
- Límites: 1 km2 free, simplificado 2D en whole-city.

**3c. ICGC / Institut Cartogràfic i Geològic de Catalunya (terreno + ortofoto + base):**
- Fuente: VISSIR + `appdownloads` + `betaportal`. Productos: `MET2 2×2 m LiDAR (RMSE 0,15 m, ortométricas)`, `MET5 5×5 m`, `MDS/MDS correlació 1 m`, `MDT Litoral 50 cm/1 m`, `Ortofoto Territorial 25 cm`, `Topo 1:1000`, `Base Map Service WMS/WMTS` (search-snippets).
- Cobertura Sagrada: total (Catalunya). Ideal para terreno plano Eixample (cota ~30-50 m) + MDT con edificios litoral.
- LOD: terreno (no edificios extruidos salvo MDS). Edificios = footprints topo, no 3D.
- Entrada Rhino: descargar ZIP ASCII/GeoTIFF por hojas → QGIS → `ImportTopo/Heron RESTTopo custom URL` o Elk `Topography (GeoTIFF/HGT)`; ortofoto como textura vía `SlippyRaster/Heron`. Reproyectar a EPSG:25831.
- Costo: 0.
- Licencia: **CC-BY 4.0 Internacional** (`This geoinformation is under CC-BY 4.0` + `Vector: Catalunya ©ICGC CC-BY / resto ©OpenMapTiles/OSM ODbL` — snippets http://www.icgc.cat/en/... + Base Map Service). Atribución `© ICGC` en lámina + link. Apto concurso público. Descarga directa permitida (a diferencia de Google).
- Límites: selector área min/max (rojo si muy grande/pequeña); hojas 2 m pesadas — recortar a 1×1 km para 8 GB. `http://www.icgc.cat/...` devolvió 403 en fetch (bloqueo bot) — verificado solo por snippet, reintentar en navegador.

**3d. Sede Catastro España + Inspire Buildings GML:**
- Fuente: `https://www.sedecatastro.gob.es/` (SEC) + servicios Inspire `Buildings 3D / Cadastral Parcels WFS + GML` (búsqueda pagó 429/errores parciales).
- Cobertura: Eixample total (referencia catastral por parcela, `SUPERFICIE`, `USO`, alturas por `plantas` en GML en zonas Inspire).
- LOD: footprint + nº plantas (no mesh texturado). Suficiente para extruir manzanas a altura real Eixample (20-27 m).
- Entrada Rhino: QGIS `Capa WFS Catastro → filtrar Eixample → Export SHP/DXF → Import Rhino` o Heron `ImportVector (GML)` con SRS EPSG:25831.
- Costo: 0 (consulta no protegida free; certificaciones literales 4,50 € solo si se piden — no necesario para massing).
- Licencia: **no dicha / gap** — snippets no traen licencia de reuso; presunción `datos abiertos con atribución Dirección General del Catastro` + normativa Inspire UE, pero NO citar sin verificar `sedecatastro.gob.es` + `datos.gob.es` en navegador. No entregar a concurso sin verificar. Candidato Nivel 2.
- Límites: WFS por bbox pequeño; GML pesado — pedir por manzana.

**3e. OpenTopography / Copernicus DEM GLO-30 (terreno regional, no urbano fino):**
- Fuente: `portal.opentopography.org` dataset `OTSDEM.032021.4326.3` GLO-30 DSM 30 m (TanDEM-X WorldDEM editado) (search-snippet).
- Cobertura: global incl. Barcelona, pero 30 m/píxel = 4 píxeles por manzana — inútil para massing Eixample, útil para contexto Collserola-mar.
- LOD: DSM (incl. edificios/vegetación) — no separa edificios.
- Entrada Rhino: API `API/globaldem?demtype=COP30&...&outputFormat=GTiff` + key free OpenTopography → GeoTIFF → Elk/Heron Topo. O bulk COG.
- Costo: 0.
- Licencia: **Copernicus free & open licence** (`reproduction/distribution/communication/adaptation free of charge, worldwide, unlimited` — snippet PDF License-COPDEM-30). Requiere cita DOI `https://doi.org/10.5270/ESA-c5d3d65` + `© DLR/Airbus/Copernicus EU/ESA`. Apto concurso.
- Límites: 30 m insuficiente urbano; usar solo fondo regional.

**3f. QGIS + QuickOSM + export (pegamento open):**
- Flujo: QGIS (EPSG:25831) + plugins QuickOSM (query `building=*` en bbox Sagrada) + `MDT ICGC` + `WFS Catastro` → `Export DXF/SHP/OBJ` → Rhino `Import` / Heron `ImportVector`.
- Costo 0, licencia = suma de fuentes (ODbL + CC-BY + Catastro gap). Apto concurso si se atribuye cada capa.
- Peso 8 GB: trabajar 600×600 m, simplificar meshes (`ReduceMesh`, `QuadRemesh`), drape ortofoto 25 cm solo en vista, no en modelo.

**3g. Gismo / BlenderGIS → OBJ/FBX → Rhino (mencionados vault):**
- Gismo (GH, snippet Discourse): `location+radius → buildings/streets/trees/terrain` automático desde OSM, extrusión por height/levels/randomHeightRange. Sin descarga manual. ODbL igual que 3a. Bueno si Elk falla.
- BlenderGIS + Blender → `OBJ/FBX` → Rhino Import: útil para draping ortofoto + MDT + OSM en Blender y pasar mesh limpio. Licencia = fuentes + Blender GPL no contamina modelo. Flujo más pesado para 8 GB — solo si QGIS no alcanza.
- No fetch 200 (snippets) — candidatos Nivel 2 para ficha propia.

### 4. Tabla comparativa Sagrada (Eixample)

| Herramienta | Cobertura Sagrada | 3D real sí/no | Licencia concurso | Costo | Peso PC 8 GB |
|---|---|---|---|---|---|
| Google 3D Tiles vía Heron IOI | total fotoreal | sí (mesh+textura) | NO — ToS prohíbe derivado/redistribución/impreso | Enterprise (1K free/mes) + billing, bloqueado EEA | pesado (cientos MB, LOD13+) |
| Heron ImportOSM / Elk OSMData | total footprints | 2.5D extruido (height/levels) | SÍ — ODbL + atribución OSM | 0 | liviano (<50 MB) ✅ |
| Cadmapper 1 km2 | barcelona 2D sí, 3D verificar | 2.5D si hay dato | GAP — verificar /terms, presumible ODbL | 0 hasta 1 km2 | liviano ✅ |
| ICGC MDT2/MDS/orto 25 cm | total Catalunya | terreno sí, edificios no | SÍ — CC-BY 4.0 + ©ICGC | 0 | medio (recortar 1 km) ✅ |
| Catastro Inspire GML | total parcelas | footprint+plantas | GAP — no dicho, verificar SEC | 0 | medio |
| Copernicus GLO-30 | global 30 m | DSM regional, no urbano | SÍ — Copernicus free + DOI | 0 (+key free) | liviano pero inútil urbano |
| QGIS+QuickOSM export | total (combina todo) | 2.5D compuesto | SÍ si se atribuye cada capa | 0 | liviano ✅ |
| Gismo / BlenderGIS→OBJ | total OSM | 2.5D / mesh draped | SÍ (ODbL+CC-BY) | 0 | medio-pesado |

### 5. Recomendación operativa massing Sagrada — paso a paso open, en metros, sin key Google

- **CRS:** todo en `ETRS89 / UTM zone 31N EPSG:25831` (oficial Catalunya). En Rhino: `EarthAnchorPoint` lat 41.3879 lon 2.1715 (Plaza Sagrada Família, frente Pasión), elevación ~33 m (tomar de ICGC MET2, no de Google Earth). Unidades metros, origen en plaza para acotar manzanas 133,3 m.
- **Paso 1 — QGIS base (15 min):** nuevo proyecto EPSG:25831 → `QuickOSM → Key=building en bbox 41.383-41.393, 2.165-2.178` → guardar `sagrada_buildings.gpkg` → añadir `WMS ICGC ortofoto 25 cm` + `WFS Catastro parcels` como control.
- **Paso 2 — Terreno ICGC (10 min):** `visors.icgc.cat/appdownloads → MET2 2×2 m → bbox 1×1 km Sagrada → ZIP ASC/GeoTIFF` → en QGIS recortar + export `sagrada_met2.tif`.
- **Paso 3 — GH Heron/Elk (20 min):** GH con `HeronSRS EPSG:25831 + SetEAP (41.3879,2.1715)` → `ImportOSM (sagrada_buildings.osm) → filtrar height/levels` → extruir: `height si existe, sino levels×3.1 m Eixample, sino 21 m default manzana` → `ImportTopo (sagrada_met2.tif) → mesh terreno` → `MoveToTopo` edificios.
- **Paso 4 — Testigo Sagrada 172,5 m:** NO extruir de OSM. Caja testigo `60×100 m base, 172,5 m altura` en parcela templo + cruces Eixample (chamfer 45° característico) como sólidos separados en capa `TESTIGO`.
- **Paso 5 — A Rhino:** `Bake` capas `EIXAMPLE_MASS (blanco mate) / TERRENO_ICGC / TESTIGO_SF` → `ReduceMesh` → guardar `activos/.../sagrada_massing_open.3dm` (no en git). Atribución en layout: `Massing: © OpenStreetMap contributors (ODbL) + © ICGC (CC-BY 4.0) + DG Catastro. Sin datos Google.`
- **Qué NO hacer:** no bakear Google Tiles a `.3dm` de entrega, no subir meshes Google a RunPod, no trazar footprints sobre screenshot Google (derivado prohibido).

## Fuentes APA idioma original + [trad. propia]

- Google. (s.f.). *Google Maps Platform Terms of Service* (en). https://cloud.google.com/maps-platform/terms [§3.2.3 No Scraping/Caching/Creating Content; verificado 200 2026-10-29]
- Google. (s.f.). *Map Tiles API Policies* (en). https://developers.google.com/maps/documentation/tile/policies [Pre-fetching/caching + Geodata overlays; verificado 200]
- Google. (2025-06-04). *Google Earth End User Additional Terms of Service* (en). https://www.google.com/help/terms_maps-earth/ [§2 Prohibited Conduct; verificado 200]
- Google. (s.f.). *Google Maps, Google Earth, and Street View — Geo Guidelines* (en). https://about.google/brand-resource-center/products-and-services/geo-guidelines [No reconstruct 3D models; verificado 200]
- Google. (s.f.). *Map Tiles API Usage and Billing* (en). https://developers.google.com/maps/documentation/tile/usage-and-billing [cuotas 10K root/día; verificado 200]
- Google. (s.f.). *Photorealistic 3D Tiles* (en). https://developers.google.com/maps/documentation/tile/3d-tiles [setup + nota EEA 2025-07-08; verificado 200]
- Google. (s.f.). *Pricing* (en). https://mapsplatform.google.com/pricing/ [Essentials 10K/Pro 5K/Enterprise 1K + $300 trial; snippet]
- Blueherongis. (2026-01-10 / 2026-09). *Heron Releases v0.5.0/v0.5.1* (en). https://github.com/blueherongis/Heron/releases [G3DTilesAoi/Poi + API key + egm08_25.gtx; verificado 200]
- Washburn, B. et al. (2025-2026). *Google street view to grasshopper* (en). https://discourse.mcneel.com/t/google-street-view-to-grasshopper/199389 [posts Brian 2026-01-10/12, 2026-02-13; Jess EEA blocked 2026-01-13; snippet]
- Azel, N. (s.f.). *Dev google 3d tiles — PR #57 Heron* (en). https://github.com/blueherongis/Heron/pull/57 [snippet]
- OpenStreetMap Foundation. (s.f.). *Copyright and License* (en). https://www.openstreetmap.org/copyright [ODbL; verificado 200]
- OpenStreetMap Foundation. (s.f.). *Licence and Legal FAQ* (en). https://osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ [ODbL commercial ok + attribution; snippet]
- ICGC. (s.f.). *2x2 m Terrain elevation model* (en). http://www.icgc.cat/en/Data-and-products/Bessons-digitals-Elevacions/2x2-m-Terrain-elevation-model [CC-BY 4.0, RMSE 0,15 m; snippet, fetch 403]
- ICGC. (s.f.). *Descarregar la cartografia — appdownloads* (ca). https://visors.icgc.cat/appdownloads/ [MET/MDS/orto lista; snippet]
- ICGC. (s.f.). *Base Map Service* (en). https://www.icgc.cat/en/Geoinformation-and-Maps/Base-Map-Service [CC-BY Catalunya / ODbL resto; snippet]
- CADMAPPER. (s.f.). *Worldwide map files* (en). https://cadmapper.com/ [1 km2 free, Whole City Barcelona; verificado 200]
- European Space Agency / OpenTopography. (2021-2024). *Copernicus GLO-30 DEM* (en). https://portal.opentopography.org/raster?opentopoID=OTSDEM.032021.4326.3 [DSM 30 m + Copernicus free licence; snippet]
- Food4Rhino. (2011). *Elk* (en). https://www.food4rhino.com/en/app/elk [OSM+USGS to Rhino; snippet]
- Center for Spatial Research. (s.f.). *Downloading Spatial Data in Grasshopper Using Elk* (en). https://github.com/CenterForSpatialResearch/gis_tutorials/blob/master/15_Downloading_Spatial_Data_In_Grasshopper_Using_Elk.md [snippet]
- Cesium. (s.f.). *Appendix B-2 Google Maps Content Third Party Terms* (en). https://cesium.com/legal/terms-for-google/ [no include in printed docs; snippet]
- Google Maps Platform Blog. Bos, L. & Lee, D. (2023-08-09). *FAQ Photorealistic 3D Tiles* (en). https://mapsplatform.google.com/resources/blog/commonly-asked-questions-about-our-recently-launched-photorealistic-3d-tiles/ [measurements = derivative prohibited; snippet]
- How to Rhino. (s.f.). *Google Maps to Rhino in 1 MINUTE* (en). https://www.youtube.com/watch?v=olUmAJBoMJU [Heron 0.5.0 LOD13 trial 90d; ref vault, no fetch transcript]
- Sede Electrónica Catastro. https://www.sedecatastro.gob.es/ [licencia reuso: no dicho — gap]

## Metodología queries por idioma + URLs + status + gaps

- ES: `Google Earth ToS copia derivado scraping`, `ICGC descarrega MDT licencia`, `Sede Catastro Inspire buildings GML licencia`, `Elk Grasshopper OSM heights` → 429 parcial en Exa (rate limit), fallback a snippets + fetch directo.
- EN: `Google Maps Platform Terms photorealistic 3D Tiles scraping prohibition caching` → 8 hits (terms, policies, service-terms, Cesium terms, blog FAQ) ; `Heron Grasshopper Google 3D Tiles IOI API key Brian Washburn discourse` → 8 hits (discourse, releases, PR57, 3D-Tile-Server, YouTube) ; `OpenStreetMap ODbL commercial use attribution competition` → 6 hits ; `Copernicus DEM GLO-30 open license OpenTopography` → 6 hits ; `Cadmapper free limits 1km2`, `Elk food4rhino`, `ICGC MET2 CC-BY` → verificados.
- IT: no aplicado (normativa ES local + docs EN).
- URLs verificadas 200 (2026-10-29, fetch): cloud.google.com/maps-platform/terms, developers.google.com/maps/documentation/tile/policies, google.com/help/terms_maps-earth, about.google/.../geo-guidelines, github.com/blueherongis/Heron/releases, openstreetmap.org/copyright, developers.google.com/.../usage-and-billing, .../3d-tiles, cadmapper.com. Status 403: icgc.cat http (bot-block). 429: búsquedas Exa seguidas.
- Gaps explícitos: precio USD exacto SKU 3D Tiles (no dicho), licencia reuso Cadmapper /terms (no fetchada), licencia Catastro Inspire para concurso (datos insuficientes), LOD alturas OSM Eixample % con height (requiere query Overpass en QGIS), EEA qué contenido sí devuelve (no dicho).

## Propuestas wiki (esqueleto, no escribir)

- `heron` (actualizar § Google 3D Tiles IOI: key+billing+EEA block+ToS §§ + no a lámina/cloud)
- `google-maps-3d-tiles-licencia` (nueva: cláusulas + policies + Earth terms + geo guidelines)
- `sagrada-massing-open` (nueva: ruta QGIS+OSM+ICGC paso a paso EPSG:25831)
- `icgc-vissir` (nueva: MET2/MDS/orto + CC-BY + appdownloads)
- `catastro-inspire` (nueva cuando se verifique licencia)
- `osm-odbl-concurso` (nueva: ODbL + atribución en lámina)

## Candidatos (Nivel 2 — esperar s de SOL)

1. Cadmapper Terms https://cadmapper.com/terms — por qué: define reuso comercial concurso. Acceso abierto.
2. Sede Catastro Inspire WFS Buildings https://www.sedecatastro.gob.es/ + datos.gob.es ficha VISSIR — por qué: alturas oficiales Eixample. Acceso abierto.
3. Gismo docs + Elk Food4Rhino versions — por qué: comparativa extrusión OSM en GH. Acceso abierto.
4. Google EEA FAQ https://developers.google.com/maps/comms/eea/faq + EEA ToS https://cloud.google.com/terms/maps-platform/eea — por qué: confirma bloqueo 3D Tiles ES. Acceso abierto.

---
*Informe @sherlock solo exterior, sin tocar wiki/ ni contenidos. ¿Avanzo a curaduría? (s/N)*
