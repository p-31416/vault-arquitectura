---
tipo: documento
proyecto: concurso-gaudi-nexus
slug: doc-massing-03d-sagrada
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-30
tags: [earth2rhino, massing, rhino, sagrada-familia, documentacion, fuentes, osm, cadmapper]
idioma: es
---

# Cómo se hizo el massing 3D del entorno Sagrada Família — proceso, datos y fuentes

> **Documento único** del massing: qué se construyó, con qué pasos y comandos, de dónde sale cada dato, en qué página web oficial se verifica, qué bugs aparecieron y qué falta. Todos los links fueron abiertos y verificados el 2026-10-30 (los videos y transcripts, el 2026-10-29).

## 1. Qué es

Massing 2.5D de ~600 × 600 m del Eixample alrededor del templo (origen local 0,0 = 41.4036, 2.1744), en Rhino 8, dos capas comparadas templo-con-templo y apoyadas en cota 0: `SF-MASSING-OSM` (1045 sólidos, z 0→37,2) + `SF-MASSING-CADMAPPER` (5599 objetos, z 0→203 con el templo) + `TESTIGO-SF` (caja propia 60×100×172,5 m, NO extruida de OSM). Escena guardada fuera del vault: `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\mcp-plaza.3dm` (43 MB). Capturas: `activos/.../earth2rhino3d/salidas/` (top, iso, overlay, cota cero, cota cero v02).

## 2. Cómo se hizo, paso a paso

```
# 1. Base OSM (terminal, vault como workdir)
P:\Anaconda\envs\comfyenv\python.exe scripts\descargar-osm-sagrada.py
# → activos/.../earth2rhino3d/base/sagrada_overpass.json (1054 footprints + 9236
#   nodos, bbox 41.4005–41.4065 / 2.1705–2.1785; 3 endpoints Overpass con fallback;
#   1er intento con bbox 1200 m dio timeout, 2do con bbox 600 m OK)

# 2. Puente Rhino (línea de comandos de Rhino 8)
_RunPythonScript "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\rhino-mcp-server-rhino.py"
# → "RhinoMCP script loaded. Server started automatically." (puerto 9876)

# 3. Massing (terminal, vía scripts\rhino-mcp-cli.py → puente → Rhino)
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\rhino-mcp-cli.py exec scripts\construir-massing-sagrada-rhino.py
# → convierte lat/lon a metros (equirectangular local), extruye cada footprint
#   a su altura, crea capas SF-MASSING-OSM + TESTIGO-SF + SF-ORIGEN

# 4. Overlay CADMapper (terminal, vía CLI → puente)
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\rhino-mcp-cli.py exec scripts\importar-cadmapper-comparar-rhino.py
# → importa el .3dm de CADMapper (5599 objetos) en SF-MASSING-CADMAPPER (+1000 X),
#   informa bbox y alturas de ambas capas

# 5. Alineación + comparación (terminal, vía CLI → puente)
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\rhino-mcp-cli.py exec scripts\alinear-comparar-cadmapper-rhino.py
# → mueve CADMapper templo-con-templo (-1490,4, -623,3), compara alturas
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\rhino-mcp-cli.py exec scripts\comparar-altos-osm-cm-rhino.py
# → compara los 47 edificios OSM ≥ 30 m con su vecino CADMapper más cercano

# 6. Cota cero (terminal, vía CLI → puente)
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\rhino-mcp-cli.py exec scripts\apoyar-cota-cero-rhino.py
# → baja cada capa a z=0 (el CADMapper venía con datum propio, base a -15,26)
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\rhino-mcp-cli.py exec scripts\apoyar-objetos-cota-cero-rhino.py
# → baja CADA objeto a z=0 (cada edificio CADMapper conservaba su cota de terreno)

# 7. Verificación (terminal, vía CLI)
# layers / conteos por capa / BoundingBox / distribución de alturas / shot top + iso
```

Correcciones de bbox en el camino: el primer bbox apuntaba 1,7 km al sur (41.383–41.393); se corrigió al templo real 41.4036/2.1744, bbox 600 m.

## 2b. Cómo lo ejecutó el agente (cadena Antigravity → Rhino) y reporte de corridas

El agente corre dentro del IDE (Antigravity, motor opencode) y **no toca Rhino directamente**: ejecuta comandos en la terminal del vault; para Rhino usa el puente MCP en dos saltos: `scripts\rhino-mcp-cli.py` habla JSON-RPC por stdio con el servidor `reer-rhino-mcp`, que reenvía al script-puente `scripts\rhino-mcp-server-rhino.py` (vive dentro del proceso Rhino, escucha en `localhost:9876`) y devuelve el resultado a la terminal. Todo lo que corre dentro de Rhino es IronPython (sin `def` visibles, sin f-strings) y nada se guarda solo: el arquitecto guarda con `Ctrl+S`.

Pasos humanos en Rhino (línea de comandos, no terminal): abrir el `.3dm` y `_RunPythonScript "...\rhino-mcp-server-rhino.py"` hasta ver `Server started automatically`. Ver comandos copiables en `comandos-rhino-copiar.md`.

**Reporte de corridas (2026-10-29/30, en orden):**

| # | Qué corrió el agente | Resultado |
|---|---|---|
| 1 | `transcribir_youtube.py` ×2 videos | Video 01: 1 cue (demo visual; whisper local confirmó 0 voz) · Video 02: 80 líneas Heron completo |
| 2 | `descargar-osm-sagrada.py` (bbox 1200 m) | Timeout 502 → se achicó a bbox 600 m |
| 3 | `descargar-osm-sagrada.py` (bbox 600 m) | OK: 1054 ways + 9236 nodos (474 con `levels`, 0 con `height`) |
| 4 | `construir-massing-sagrada-rhino.py` (3 corridas) | Fallaron: `Rhino.Geometry.Guid` no existe → se cambió a `System.Guid.Empty` |
| 5 | `construir-massing-sagrada-rhino.py` (4ª) | OK: **1045 extruidos**, 9 salteados; testigo 172,5 m + cruz origen |
| 6 | Limpieza | Borradas 3135 polilíneas residuales; duplicados de testigo/origen a 1 + 2 |
| 7 | Verificación + capturas | Bbox x −457…443, y −369…437, z 0→37,2 · `sf-massing-v01-top.png` + `sf-massing-v01-iso.png` |
| 8 | `auditar-alturas-osm.py` | min 3,1 / mediana 21,0 / max 37,2 m; 34,1 = levels 11, 37,2 = levels 12 |
| 9 | `importar-cadmapper-comparar-rhino.py` | OK: 5599 objetos en `SF-MASSING-CADMAPPER` (+1000 X) |
| 10 | `auditar/alinear/comparar-cadmapper` | Templo CM a 170 m en (490,4/623,3) → mover `(-1490,4, -623,3)` templo-con-templo; ~35/47 altos coinciden a 1 m |
| 11 | `apoyar-cota-cero-rhino.py` | OSM ya en 0; CADMapper bajado de −15,26 a 0 |
| 12 | `apoyar-objetos-cota-cero-rhino.py` | 5599 objetos bajados uno por uno (offsets 0→196 m); malla de terreno quedó plana en 0 |
| 13 | `cortes-plaza-rhino.py` (varias corridas) | Fallaron: lista vacía en `AddClippingPlane`, `.Remove`/`.Name`/`.Details` inexistentes, clip en `Attributes` en vez del objeto → todo corregido (ver §5) |
| 14 | `cortes-plaza-rhino.py` (final) | OK: CORTE-A-A (Back) + CORTE-B-B (Right), láminas A1 `SF-CORTE-AA`/`SF-CORTE-BB`, detalles 1:2000 en Shaded, bloqueados, cada plano solo en su detalle |
| 15 | `detalles-shaded.py` + `activa-aa/bb.py` + capturas | `sf-corte-aa-lamina.png` + `sf-corte-bb-lamina.png` (templo ~85 mm en hoja = 170 m a 1:2000 ✓) |
| 16 | `commons-*.py` + `descargar-*.py` + `generar-thumbs-ref.py` | 10 fotos CC BY-SA en `ref/` + thumbs + `fotos-plaza-commons.md` |

## 3. De dónde sale cada dato

| Dato | Fuente | Cómo se obtuvo | Licencia |
|---|---|---|---|
| Footprints + `building:levels` (474 con niveles, 0 con `height`) | OpenStreetMap vía Overpass API | Query `way["building"](bbox)` + `out skel` — ver §6 link 1 para repetirla en el navegador | [ODbL](https://opendatacommons.org/licenses/odbl/1-0/) — © OpenStreetMap contributors (España incluye IGN CC BY 4.0) |
| Altura por edificio | Regla: `height` directo → `levels × 3,1 m` → default 21 m manzana Eixample | `scripts/auditar-alturas-osm.py` (min 3,1 / mediana 21,0 / max 37,2) | Derivado OSM → ODbL |
| Contraste de alturas (170 m templo, 3256 extrusiones) | CADMapper (procesa OSM + NASA + USGS) | Archivo `cadmapper-barcelona-catalonia-es.3dm` (signup gratuito 1 km²) + `LICENSE.txt` | [ODbL](https://opendatacommons.org/licenses/odbl/1-0/) + USGS/NASA dominio público |
| Fondo fotorrealista (10 fotos plaza + basílica) | Wikimedia Commons | Búsqueda + API (autor, licencia, URL) → `activos/.../ref/` | CC BY-SA 2.0/4.0 + autor en rótulo |
| Atribución obligatoria en lámina | `Massing © OpenStreetMap contributors (ODbL). Sin datos Google.` + créditos Commons | — | Ver §6 links 4 y 5 |

Nota sobre 3,1 m/planta: el wiki oficial de OSM fija **3 metros por planta** como dimensión por defecto para render 3D cuando no hay `height` (ver §6 link 3); el estudio usa 3,1 m por la altura libre típica del Eixample.

### De dónde salen las alturas (auditoría real)

| Medida | Valor |
|---|---|
| min / mediana / max | 3,1 / 21,0 / 37,2 m |
| levels 7–8 (típico Eixample) | 148 edificios → 21,7–24,8 m |
| levels 10 | 35 edificios → 31,0 m |
| levels 11 | 9 edificios → **34,1 m** (medición de manzana del estudio) |
| levels 12 | 3 edificios → **37,2 m** (uno es `Edifici Califòrnia`) |
| sin levels | 580 edificios → 21,0 m default |

Lectura: los 34/37 m **salen de OSM** (`levels=11/12` × 3,1), no de un error de escala. El Eixample histórico ronda PB+5/7 (~20–25 m), pero junto a la Sagrada hay bloques modernos de 10–12 plantas. El default 21 m es hipótesis del estudio, no dato: 580 edificios quedaron en 21 m parejo. Ejemplo auditable: [way 775772567](https://www.openstreetmap.org/way/775772567) (`building=apartments` + `building:levels=12` → 37,2 m).

### Comparación OSM vs CADMapper (misma escena, por MCP)

- CADMapper trae ciudad completa (882×1110 m, 3256 extrusiones + 2342 curvas + 1 malla), con el templo (170 m) en coords de archivo (490,4 / 623,3). Alineación: mover capa `(-1490,4, -623,3)` → templo con templo. Verificación visual: `salidas/sf-overlay-osm-cm-top.png` (footprints coinciden, misma fuente OSM).
- Nuestros altos (47 edificios ≥ 30 m) vs vecino CADMapper más cercano:
  - **Mayoría (~35): coinciden a 1 m** — OSM 31,0 ↔ CM 30,0 · 34,1 ↔ 33,0 · 37,2 ↔ 36,0. Offset sistemático −1 m (3,1 vs 3,0 m/planta o parapeto). **Los 34/37 m son reales.**
  - **Minoría (~12): discrepan** — OSM 31–37 ↔ CM 3–6: el centroide cae en una sub-pieza CADMapper (patio/kiosco/porche) mientras el way OSM cubre la manzana entera, o viceversa. Revisar caso por caso en el mapa (§6 link 2).
  - Donde OSM no tenía `levels` (default 21), CADMapper trae 21/24/27/30/33: **el overlay sirve para refinar** los 580 defaults.
- **Cota cero por capa**: el CADMapper venía con datum propio (base a −15,26 m) → bajado a z=0; OSM ya en cero (0→37,2), testigo 0→172,5. Captura: `salidas/sf-overlay-cota-cero-iso.png`.
- **Cota cero por objeto** (a pedido del estudio): el promedio estaba en cero pero cada edificio CADMapper conservaba su cota de terreno (hasta ~10 m de diferencia visible) → 5599 objetos bajados uno por uno a z=0. Efecto colateral: la malla de terreno CADMapper también quedó plana en 0 — si se quiere relieve real, está en el `.3dm` original. Captura: `salidas/sf-overlay-cota-cero-v02-iso.png`.

## 4. Decisiones del estudio

- Origen local 0,0 = templo (41.4036, 2.1744); nota CRS ETRS89/UTM31N EPSG:25831. Conversión equirectangular local (error < 1 m en 600 m).
- Capas: `SF-MASSING-OSM` (1045 sólidos) · `SF-MASSING-CADMAPPER` (5599, templo-con-templo, cota 0) · `TESTIGO-SF` (caja propia 60×100×172,5 m, NO extruida de OSM) · `SF-ORIGEN` (cruz 0,0).
- El script NO guarda: el arquitecto guarda como `SF-sitio-massing-v01.3dm` (ya guardado como `mcp-plaza.3dm`).
- Nada Google en la entrega (ToS + bloqueo EEA): la malla Google queda fuera del flujo.
- Atribución de lámina: `Massing © OpenStreetMap contributors (ODbL). Sin datos Google.`

## 5. Bugs del puente encontrados y corregidos

1. `Rhino.Geometry.Guid` no existe → `System.Guid.Empty` (todas las extrusiones caían en excepción).
2. Offset por cara depende de la normal → mitad del massing bajo cota (z −37) → extrusión recta +Z (`ExtrudeCurveStraight` + `CapPlanarHoles`, 14 sin tapa, sirven igual).
3. El puente ejecuta sin `def` visibles (globals separados) → script 100 % plano, sin funciones ni constantes de módulo.
4. 3135 polilíneas residuales de las 3 corridas fallidas → borradas; duplicados de testigo/origen → 1 + 2.

## 6. Páginas web de los recursos (verificadas 2026-10-30)

1. **Repetir la descarga en el navegador** — Overpass Turbo con la query lista (`Run`): [overpass-turbo.eu — bbox Sagrada](https://overpass-turbo.eu/?Q=%5Bout%3Ajson%5D%5Btimeout%3A90%5D%3B%28way%5B%22building%22%5D%2841.4005%2C2.1705%2C41.4065%2C2.1785%29%3Brelation%5B%22building%22%5D%2841.4005%2C2.1705%2C41.4065%2C2.1785%29%3B%29%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B&C=41.4035%3B2.1745%3B15)
2. **Mapa navegable del mismo recorte** (clic en un edificio → `Query features` → ver sus tags): [openstreetmap.org — Sagrada Família](https://www.openstreetmap.org/#map=16/41.4036/2.1744)
3. **Qué significan los tags**: [Key:building:levels](https://wiki.openstreetmap.org/wiki/Key:building:levels) (nº de plantas sobre rasante; 3 m/planta por defecto) · [Key:height](https://wiki.openstreetmap.org/wiki/Key:height) (altura en metros) · [Key:building](https://wiki.openstreetmap.org/wiki/Key:building)
4. **Licencia de los datos** (qué se puede hacer + cómo atribuir): [ODbL — openstreetmap.org/copyright](https://www.openstreetmap.org/copyright)
    - Texto legal completo de la licencia: [Open Database License (ODbL) v1.0](https://opendatacommons.org/licenses/odbl/1-0/) — permite copiar, distribuir, transmitir y adaptar (incluso uso comercial) con atribución; lo derivado se distribuye bajo la misma licencia.
    - Resumen en lenguaje claro: [ODbL Summary](https://opendatacommons.org/licenses/odbl/summary/) · página de licencias de la OSMF: [osmfoundation.org/Licence](https://osmfoundation.org/Licence) · guía de atribución: [Attribution Guidelines](https://osmfoundation.org/wiki/Licence/Attribution_Guidelines)
5. **Motor de la query**: [Overpass API](https://overpass-api.de/) · [Overpass Turbo](https://overpass-turbo.eu/)
6. **CADMapper** (1 km² gratis con signup; whole-city Barcelona gratis sin cuenta): [cadmapper.com](https://cadmapper.com/) · [signup](https://cadmapper.com/pro/signup)
7. **Videos que originaron el flujo** (transcripts verbatim en `raw/yt/transcripts/`): [Google Earth to Rhino — Free Workflow 2026](https://www.youtube.com/watch?v=uIhX4IYBobc) (demo visual, 1 cue) · [Google Maps to Rhino in 1 MINUTE](https://www.youtube.com/watch?v=olUmAJBoMJU) (Heron + Google 3D Tiles, 80 líneas) — fichas: `ficha-video-01-earth-free-2026.md` · `ficha-video-02-maps-1min-heron.md` · informe de licencias @sherlock: `raw/research/2026-10-29-earth2rhino-open-alternativas.md`
8. **Fotos**: [Category:Plaça de Gaudí](https://commons.wikimedia.org/wiki/Category:Pla%C3%A7a_de_Gaud%C3%AD) · [Category:Plaça de la Sagrada Família](https://commons.wikimedia.org/wiki/Category:Pla%C3%A7a_de_la_Sagrada_Fam%C3%ADlia) — documento visual con las 10 usadas: [[proyectos/concurso-gaudi-nexus/earth2rhino3d/fotos-plaza-commons|fotos-plaza-commons]]

## 7. Archivos (dónde está cada cosa)

- **Escena**: `G:\Mi unidad\OS-Emilia\AIxGaudi\Materials\mcp-plaza.3dm` (43 MB, referencia externa, no se duplica en el vault).
- **Base OSM**: `activos/proyectos/concurso-gaudi-nexus/earth2rhino3d/base/sagrada_overpass.json` · **CADMapper**: `.../base/cadmapper/cadmapper-barcelona-catalonia-es.3dm` + `LICENSE-cadmapper.txt` · **Fotos**: `.../ref/` + `.../ref/thumbs/` · **Capturas**: `.../salidas/` (top, iso, overlay, cota cero, cota cero v02).
- **Scripts** (`scripts/`): `descargar-osm-sagrada.py` · `construir-massing-sagrada-rhino.py` (+`_notas.md`) · `auditar-alturas-osm.py` · `importar-cadmapper-comparar-rhino.py` · `auditar-cadmapper-rhino.py` · `alinear-comparar-cadmapper-rhino.py` · `comparar-altos-osm-cm-rhino.py` · `apoyar-cota-cero-rhino.py` · `apoyar-objetos-cota-cero-rhino.py` · `commons-*.py` · `descargar-*.py` · `generar-thumbs-ref.py` · `rhino-mcp-cli.py` · `rhino-mcp-server-rhino.py`. Índice: `scripts/00-index.md`.

## 8. Cortes por la plaza (2026-10-30)

- Script `scripts/cortes-plaza-rhino.py` (+ `_notas.md`): CORTE A-A (plano XZ en y=0, vista Back) + CORTE B-B (plano YZ en x=0, vista Right), cada uno con su lámina A1 (`SF-CORTE-AA`, `SF-CORTE-BB`) y su detalle a 1:2000, bloqueado, en Shaded. Cada plano recorta solo su detalle.
- Capturas: `salidas/sf-corte-aa-lamina.png` + `salidas/sf-corte-bb-lamina.png`.
- Para imprimir sin widgets: `Print` → *Visibility* → desmarcar **Clipping planes**. Sin rótulos todavía.

## 9. Pendiente

1. Refino de alturas con Catastro (plantas oficiales) donde OSM y CADMapper discrepen > 3 m.
2. Función Hermes `earth2rhino-massing` location-agnóstica (`--lat --lon --radio` + `meta.json`, ficha formato SKILL).
3. **Composite plaza**: foto Commons CC-BY-SA como fondo + captura iso del massing + propuesta → WF-03 `rhino-to-image` para el fotorrealismo del conjunto.
