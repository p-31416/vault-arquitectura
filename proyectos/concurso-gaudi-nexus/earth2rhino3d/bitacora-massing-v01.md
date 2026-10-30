---
tipo: bitacora
proyecto: concurso-gaudi-nexus
slug: earth2rhino-bitacora-v01
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [earth2rhino, bitacora, massing, osm, rhino, sagrada-familia, odbl]
idioma: es
---

# Bitácora massing v01 — del video al 3D del entorno Sagrada, principio a fin

> Documento vivo del proceso completo: qué se hizo, en qué orden, con qué comando, de dónde salió cada dato y qué falta. El 3D ingresó perfecto a Rhino el 2026-10-29.

## 1. De dónde sale la volumetría (fuentes)

| Fuente                                                                                 | Qué aporta                                                                                                | Fecha/corte                       | Licencia                                | Archivo en vault                                                                                  |
| :------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Video 01 `https://www.youtube.com/watch?v=uIhX4IYBobc` (Earth free 2026)               | Idea del flujo, demo visual sin narración (1 cue)                                                         | transcript 2026-10-29             | — (referencia, no base)                 | `raw/yt/transcripts/2026-10-29_uIhX4IYBobc.en.md` (generado por `scripts/transcribir_youtube.py`) |
| Video 02 `https://www.youtube.com/watch?v=olUmAJBoMJU` (Maps→Rhino 1 min, Heron 0.5.0) | Flujo Heron + Google 3D Tiles IOI, LOD 13, API key                                                        | transcript 2026-10-29 (80 líneas) | Google Maps Content (no va a entrega)   | `raw/yt/transcripts/2026-10-29_olUmAJBoMJU.en.md` (generado por `scripts/transcribir_youtube.py`) |
| Overpass API (`overpass-api.de`, fallback kumi/private.coffee)                         | 1054 footprints `building=*` + 9236 nodos, bbox 41.4005–41.4065 / 2.1705–2.1785 (600 m, templo al centro) | descarga 2026-10-29               | **ODbL** (© OpenStreetMap contributors) | `activos/.../earth2rhino3d/base/sagrada_overpass.json`                                            |
| Fotos Commons | 10 fotos CC BY-SA (7 plaza + 3 basílica) verificadas 2026-10-29 | descarga 2026-10-29 | CC BY-SA 2.0/4.0 + autor en rótulo | `activos/.../earth2rhino3d/ref/` + doc `fotos-plaza-commons.md` |
| CADMapper 1 km² (versión Rhino) | `cadmapper-barcelona-catalonia-es.3dm` (4 MB) + `LICENSE-cadmapper.txt`, descargado por el estudio 2026-10-29 | descarga 2026-10-29 | **ODbL** (Map data © OSM contributors) + USGS NED / NASA SRTM **dominio público** (ver `LICENSE-cadmapper.txt`) — gap de licencia **cerrado** | `activos/.../earth2rhino3d/base/cadmapper/` y original en `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\cadmapper-barcelona-catalonia-es\` |
| Massing MCP guardado | `mcp-plaza.3dm` (43 MB), escena verificada 2026-10-29 | 2026-10-29 | ODbL | `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\mcp-plaza.3dm` (referencia externa, no se duplica en el vault) |

Fichas de análisis: `ficha-video-01-earth-free-2026.md` · `ficha-video-02-maps-1min-heron.md` · `comparativa-metodos.md` · informe @sherlock `raw/research/2026-10-29-earth2rhino-open-alternativas.md`.

## 1b. Revisión manual en la web (links OSM)

- **Ver el bbox tal como lo baja el script** (Overpass Turbo, query lista para `Run`): [overpass-turbo.eu — bbox Sagrada](https://overpass-turbo.eu/?Q=%5Bout%3Ajson%5D%5Btimeout%3A90%5D%3B%28way%5B%22building%22%5D%2841.4005%2C2.1705%2C41.4065%2C2.1785%29%3Brelation%5B%22building%22%5D%2841.4005%2C2.1705%2C41.4065%2C2.1785%29%3B%29%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B&C=41.4035%3B2.1745%3B15) — muestra footprints + tags (`height`, `building:levels`) edificio por edificio.
- **Mapa navegable del mismo recorte**: [openstreetmap.org — Sagrada Família](https://www.openstreetmap.org/#map=16/41.4036/2.1744) (zoom 16, templo al centro; clic en un edificio → `Query features` → ver sus tags).
- **Qué significan los tags**: [Key:building:levels](https://wiki.openstreetmap.org/wiki/Key:building:levels) (nº de plantas sobre rasante) · [Key:height](https://wiki.openstreetmap.org/wiki/Key:height) (altura en metros) · [Key:building](https://wiki.openstreetmap.org/wiki/Key:building) (tipos de edificio).
- **Licencia de los datos**: [ODbL — openstreetmap.org/copyright](https://www.openstreetmap.org/copyright) (atribución `© OpenStreetMap contributors` obligatoria en la lámina).
- **Caso testigo**: el `Edifici Califòrnia` (`levels=12` → 37,2 m) se verifica clicando sus torres junto a la Sagrada en el mapa de arriba.

## 2. De dónde salen las alturas (pregunta del estudio)

Regla aplicada en `scripts/construir-massing-sagrada-rhino.py`:

1. Tag `height` → valor directo (0 casos en este bbox).
2. Tag `building:levels` × **3,1 m** → 474 edificios.
3. Sin dato → **default 21 m** (manzana Eixample PB+6) → 580 edificios.

Auditoría real (`scripts/auditar-alturas-osm.py`):

| Medida | Valor |
|---|---|
| min / mediana / max | 3,1 / 21,0 / 37,2 m |
| levels 7–8 (típico Eixample) | 148 edificios → 21,7–24,8 m |
| levels 10 | 35 edificios → 31,0 m |
| levels 11 | 9 edificios → **34,1 m** ← tu medición de manzana |
| levels 12 | 3 edificios → **37,2 m** (uno es `Edifici Califòrnia`) ← tu medición baja |
| sin levels | 580 edificios → 21,0 m default |

Lectura: los 34/39 m **salen de OSM** (`levels=11/12` × 3,1), no de un error de escala. El Eixample histórico ronda PB+5/7 (~20–25 m), pero junto a la Sagrada hay bloques modernos de 10–12 plantas que OSM registra así. El default 21 m es hipótesis del estudio, no dato: 580 edificios quedaron en 21 m parejo. Para afinar: overlay CADMapper (§5) + Catastro (nº plantas oficial) + chequeo visual contra ortofoto ICGC.

## 3. Paso a paso con comandos

```
# 1. Base OSM (terminal, vault como workdir)
P:\Anaconda\envs\comfyenv\python.exe scripts\descargar-osm-sagrada.py
# → activos/.../earth2rhino3d/base/sagrada_overpass.json (3 endpoints con fallback; 1er intento 502/1200 m timeout, 2do bbox 600 m OK)

# 2. Puente Rhino (línea de comandos de Rhino 8)
_RunPythonScript "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\rhino-mcp-server-rhino.py"
# → "RhinoMCP script loaded. Server started automatically." (puerto 9876)

# 3. Massing (terminal, vía scripts\rhino-mcp-cli.py → puente → Rhino)
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\rhino-mcp-cli.py exec scripts\construir-massing-sagrada-rhino.py

# 4. Verificación (terminal, vía CLI)
# layers / conteos por capa / BoundingBox / shot top + iso
```

Correcciones de bbox en el camino: el primer bbox apuntaba 1,7 km al sur (41.383–41.393); se corrigió al templo real 41.4036/2.1744, bbox 600 m.

## 4. Decisiones del estudio

- Origen local 0,0 = templo (41.4036, 2.1744); nota CRS ETRS89/UTM31N EPSG:25831. Conversión equirectangular local (error < 1 m en 600 m).
- Capas: `SF-MASSING-OSM` (1045 sólidos) · `TESTIGO-SF` (caja propia 60×100×172,5 m, NO extruida de OSM) · `SF-ORIGEN` (cruz 0,0).
- El script NO guarda: el arquitecto guarda como `SF-sitio-massing-v01.3dm`.
- Nada Google en la entrega (ToS + bloqueo EEA): la malla Google queda fuera del flujo.
- Atribución de lámina: `Massing © OpenStreetMap contributors (ODbL). Sin datos Google.`

## 5. Bugs del puente encontrados y corregidos

1. `Rhino.Geometry.Guid` no existe → `System.Guid.Empty` (todas las extrusiones caían en excepción).
2. Offset por cara depende de la normal → mitad del massing bajo cota (z −37) → extrusión recta +Z (`ExtrudeCurveStraight` + `CapPlanarHoles`, 14 sin tapa, sirven igual).
3. El puente ejecuta sin `def` visibles (globals separados) → script 100 % plano.
4. 3135 polilíneas residuales de las 3 corridas fallidas → borradas; duplicados de testigo/origen → 1 + 2.

## 6. Resultado verificado (2026-10-29, por MCP)

- `SF-MASSING-OSM`: 1045 sólidos, z 0→37,2, x −457…443,6, y −369,7…437,2 (ancho extra por ways que cruzan el borde del bbox).
- Capturas: `activos/.../earth2rhino3d/salidas/sf-massing-v01-top.png` (planta, retícula Eixample + chamfers legibles) + `sf-massing-v01-iso.png` (isométrica SE, testigo naranja al centro).

## 6b. Comparación OSM vs CADMapper (2026-10-30, por MCP, misma escena)

- Import: `scripts/importar-cadmapper-comparar-rhino.py` (lee el `.3dm` CADMapper, 5599 objetos, capa `SF-MASSING-CADMAPPER`). Scripts de auditoría: `scripts/auditar-cadmapper-rhino.py` · `scripts/alinear-comparar-cadmapper-rhino.py` · `scripts/comparar-altos-osm-cm-rhino.py`.
- CADMapper trae ciudad completa (882×1110 m, 3256 extrusiones + 2342 curvas + 1 malla), con el templo (170 m) en coords de archivo (490,4 / 623,3). Alineación: mover capa `(-1490,4, -623,3)` → templo con templo. Verificación visual: `salidas/sf-overlay-osm-cm-top.png` (footprints coinciden, misma fuente OSM).
- Nuestros altos (47 edificios ≥ 30 m) vs vecino CADMapper más cercano:
  - **Mayoría (~35): coinciden a 1 m** — OSM 31,0 ↔ CM 30,0 · 34,1 ↔ 33,0 · 37,2 ↔ 36,0. Offset sistemático −1 m (3,1 vs 3,0 m/planta o parapeto). **Los 34/37 m son reales.**
  - **Minoría (~12): discrepan** — OSM 31–37 ↔ CM 3–6 m: el centroide cae en una sub-pieza CADMapper (patio/kiosco/porche) mientras el way OSM cubre la manzana entera, o viceversa. Revisar caso por caso en el mapa (§1b).
  - Donde OSM no tenía `levels` (default 21), CADMapper trae 21/24/27/30/33: **el overlay sirve para refinar** los 580 defaults.
- Conclusión: usar OSM como base + tomar alturas CADMapper donde discrepen > 3 m, verificando en el mapa. Nada Google en ningún paso.
- **Cota cero común (2026-10-30)**: el CADMapper venía con su propio datum (base a −15,26 m). Script `scripts/apoyar-cota-cero-rhino.py` baja cada capa a z=0 → OSM ya en cero (0→37,2), CADMapper ahora 0→203, testigo 0→172,5. Ambas apoyan en el mismo plano xyz. Captura: `salidas/sf-overlay-cota-cero-iso.png`.
- **Cota cero por objeto (2026-10-30, a pedido)**: el promedio estaba en cero pero cada edificio CADMapper conservaba su cota de terreno (hasta ~10 m de diferencia visible). Script `scripts/apoyar-objetos-cota-cero-rhino.py` bajó los 5599 objetos uno por uno a z=0 (offsets 0→196 m; el de 196 m es una pieza alta suelta). Efecto colateral: la malla de terreno CADMapper también quedó plana en 0 — si se quiere relieve real, está en el `.3dm` original. Captura: `salidas/sf-overlay-cota-cero-v02-iso.png`.

## 7. Pendiente (en orden)

1. **Guardar** `SF-sitio-massing-v01.3dm` en Rhino ✅ (hecho por el estudio 2026-10-29/30).
2. **CADMapper**: importar `base/cadmapper/cadmapper-barcelona-catalonia-es.3dm` en capa `SF-MASSING-CADMAPPER` desplazada +X para comparar alturas lado a lado (misma ubicación = misma base, no superpuesta, para ver si coinciden). Licencia verificada 2026-10-30: ODbL + dominio público (gap cerrado).
3. Refino de alturas con Catastro (plantas oficiales) donde OSM y CADMapper discrepen.
4. **Composite plaza**: foto Commons CC-BY-SA de la Sagrada como fondo + captura iso del massing + propuesta → WF-03 `rhino-to-image` para el fotorrealismo del conjunto.
