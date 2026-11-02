# 2026-10-30 (cont.) — Sesión cortes plaza + documento único

## Qué se hizo

- **2 cortes por la plaza** (`scripts/cortes-plaza-rhino.py` + `_notas.md`): CORTE-A-A (plano XZ en y=0, vista Back, lámina A1 `SF-CORTE-AA`) + CORTE-B-B (plano YZ en x=0, vista Right, lámina A1 `SF-CORTE-BB`). Detalles a 1:2000 en Shaded, bloqueados; cada plano recorta solo su detalle. Capturas `sf-corte-aa-lamina.png` + `sf-corte-bb-lamina.png` (templo ~85 mm = 170 m ✓).
- **8 trampas de API sorteadas** (documentadas en notas): lista vacía en `AddClippingPlane` (exige viewport), clip en objeto no en `Attributes` con firma `(viewport, bool)`, `.PageName`/`.GetDetailViews()`/`Viewport.Name` en vez de `.Name`/`.Details`/`Attributes.Name`, `.Delete` en vez de `.Remove`, script 100 % plano sin `def`, secuencia V8 de `SetScale`.
- **Documento único**: `doc-massing-03d-sagrada.md` absorbió la bitácora (borrada); suma §2b con cadena de ejecución Antigravity→Rhino + reporte de 16 corridas; links ODbL (texto legal, resumen, OSMF, attribution guidelines) verificados en vivo.
- **Apoyo**: `activa-aa.py`, `activa-bb.py`, `detalles-shaded.py`; índice scripts + índice earth2rhino3d actualizados.

## Pendiente (sin cambio)

Refino Catastro, función Hermes location-agnóstica, composite plaza → WF-03. Guardar el `.3dm` (el arquitecto).

## Análisis cerebro-digital

**Topics:** cortes-plaza · layout-a1 · clippingplane · escala-1-2000 · doc-unico · odbl-links
**Entidades:** `SF-CORTE-AA`/`SF-CORTE-BB` (A1, Back/Right, Shaded, lock) · `cortes-plaza-rhino.py` (8 fixes API) · `doc-massing-03d-sagrada.md` (§2b reporte 16 corridas)
**Hechos:** AddClipViewport=(viewport,bool) en objeto; PageName/GetDetailViews/Viewport.Name son los accesos V8; templo 85 mm en hoja valida 1:2000; ODbL verificado en opendatacommons.org.
