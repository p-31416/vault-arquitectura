---
tipo: log
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [sesion, massing-caba, tejido-urbano, pyshp, rhino, pip-install, overpass, licencias]
idioma: es
---

# 2026-11-01 — Sesión massing CABA (fuentes abiertas + primer 3D)

Más nuevo → más arriba.

## Qué se hizo

1. **Revisión de doc del flujo Barcelona** (`proyectos/concurso-gaudi-nexus/earth2rhino3d/doc-massing-03d-sagrada.md` + informe sherlock `raw/research/2026-10-29-earth2rhino-open-alternativas.md`): el flujo es location-agnóstico (Overpass global + conversión equirectangular); lo localizable: CRS, alturas y fuente.
2. **Verificación contra CABA**:
   - CADMapper: `buenos-aires` en Whole City Files (2D). 3D sin verificar en app (gap heredado).
   - Overpass: los GET del día fallaron (schannel TLS en PS 5.1 y curl; espejos kumi/private.coffee 406/timeout) → medición OSM CABA quedá pendiente (`scripts/medir-osm-caba.py` creado, **aún sin correr**).
   - **Descubrimiento principal: Tejido Urbano del GCBA** — volúmenes edificados de TODA la ciudad con `altura` real en metros (Fotogrametría, restitución 2013/actualización 2017), `altos`/`bajos` pisos, SMP catastral, licencia CC-BY-2.5-AR. Verificado vía API CKAN: `data.buenosaires.gob.ar/api/3/action/package_show?id=tejido-urbano`.
3. **Descarga e instalación (aprobada por SOL, con registro)**:
   - `tejido.zip` (168 MB) desde `cdn.buenosaires.gob.ar/.../tejido-urbano/tejido.zip` → descomprimido en `Temp\opencode\tejido-caba\unzip\tejido\` (SHP 329 MB + DBF 237 MB).
   - pip install **pyshp 3.1.6**: cmd exacta `& "P:\Anaconda\envs\comfyenv\python.exe" -m pip install pyshp 2>&1 | Select-Object -Last 5` (PS 5.1). Instalación limpia, sin dependencias. Validado el import y el lector contra el SHP real ANTES de documentar.
   - CRS confirmado con `tejido.prj`: **EPSG:4326 (WGS84 lat/lon)** → cero reproyección, conversion equirectangular local directo.
   - Dump GeoJSON oficial descartado: pesa 1,09 GB (`Content-Length` verificado por HEAD).
4. **Filtro sector Obelisco 600×600** (`scripts/filtrar-tejido-caba.py`, bbox idéntico al test OSM: S -34.6065 / N -34.6015 / W -58.3846 / E -58.3786): **3020 volúmenes, 100 % con altura decodificable**, min 1.8 / mediana 16.8 / max 75.6 m. Nota: los ejemplos "2d8" de la metadata CKAN engañan — el campo `altura` del SHP viene flotante limpio (2.8, 5.6...).
   - Salida: `activos/research/2026-11-01-massing-caba/caba-tejido-obelisco.json` (1,5 MB, x/y ya en metros locales, origen 0,0 = -34.604, -58.3816).
5. **Builder Rhino** (`scripts/construir-massing-caba-rhino.py`, calco plano del builder Sagrada, fixes heredados: System.Guid.Empty? — en este se usa el patrón `Guid.Empty` de rhinoscriptsyntax igual que Sagrada, ExtrudeCurveStraight +Z, CapPlanarHoles, capas + cruz origen). **Bug corregido en caliente**: cabecera `#! python2` → `#! python3` (Rhino re-ruta al motor IronPython 2.7 con el shebang 2 y `open(encoding=)` no existe ahí — fallaba justo línea 40).
6. **Documento de evaluación**: `raw/research/2026-11-01-massing-caba-fuentes.md` (6 opciones comparadas, estado verificado/gap, cómo se maneja BA Data/CKAN). Ojo: se reescribió una vez — la primera versión salió con tokens corruptos y se reemplazó íntegra.
7. Rhino 8 lanzado con `Start-Process "C:\Program Files\Rhino 8\System\Rhino.exe" -ArgumentList "/documentunits=meters"`. Bridge MCP no arrancó (9876 cerrado; error de servidor legible pero no copiable por el usuario). Camino de mínima fricción elegido: `_RunPythonScript` directo del builder dentro de Rhino (sin bridge). Estado al cierre: **el usuario está re-corriendo el builder con la cabecera corregida**.

## Archivos tocados / creados

| Archivo | Qué |
|---|---|
| `raw/research/2026-11-01-massing-caba-fuentes.md` | NUEVO — evaluación de opciones CABA (verificada vía API/fetch) |
| `scripts/medir-osm-caba.py` | NUEVO — densidad OSM CABA (creado, **sin correr**) |
| `scripts/filtrar-tejido-caba.py` | NUEVO — SHP GCBA → JSON recorte Obelisco (corrido OK) |
| `scripts/construir-massing-caba-rhino.py` | NUEVO — builder Rhino del massing CABA (corrido pendiente del shebang fix) |
| `activos/research/2026-11-01-massing-caba/caba-tejido-obelisco.json` | NUEVO — 3020 volúmenes filtrados (1,5 MB) |
| `raw/sessions/2026-11-01-sesion-massing-caba.md` | este registro |

## Análisis cerebro-digital

- **Topics**: massing 2.5D (footprint+altura), fuentes abiertas por ciudad, datos oficiales municipales (GCBA CKAN), shapefile/CRS/EPSG:4326, conversion equirectangular, pyshp/pip, Overpass-TLS errores, _RunPythonScript.
- **Entidades**: GCBA Tejido Urbano / data.buenosaires.gob.ar / CDN cdn.buenosaires.gob.ar / Overpass / CADMapper / CAD ATLAS / Anyscape / pyshp 3.1.6 / Rhino 8 / shebang python3.
- **Hechos**: 1.386.616 volúmenes en el Tejido GCBA; 3020 volúmenes en el recorte Obelisco 600 m; techo 75,6 m en el sector; altura 100 % disponible; Overpass endpoints bloqueados para el entorno shell del día; massing listo para correr en Rhino con la cabecera corregida.
