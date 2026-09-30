# audita-dwg.py — Notas didacticas (linea por linea en ES)

Este script audita un DWG de replanteo contra el spec SET_01-REP **sin abrir AutoCAD** (usa `ezdxf`, que lee el binario DWG). Pensado para vos, que estas leyendo Python: cada bloque explica que hace y por que.

## Como correrlo

```powershell
py -3 scripts/audita-dwg.py activos\caddy-salidas\REP-ARAOZ.dwg
```

Salida:
- `REP-ARAOZ.audit.md` — reporte legible, listo para pegar a `raw/reports/`
- `REP-ARAOZ.audit.json` — dump completo (para comparar / alimentar otro script)

---

## Bloque por bloque

### Imports + constantes

- `sys`, `json`, `Counter` (conteo eficiente), `datetime` (timestamp del reporte), `pathlib.Path`.
- `ezdxf` lee el DWG. `TextEntityAlignment` no se usa aca, lo dejo por si despues queremos detectar alineacion de TEXT.
- `SPEC_LAYERS` = las **22 capas** del spec `SET_01-REP_Replanteo.md` §2. La estructura es `(nombre, color_ACI, linetype, lineweight_mm, descripcion)`. Esta lista es la "verdad" contra la que comparamos el DWG.

### `audit(dwg_path)`

Abre el DWG y devuelve un dict con todo lo que necesitamos.

1. `ezdxf.readfile(path)` lee el archivo. **No abre AutoCAD.**
2. `doc.modelspace()` da la entidad iterable de model space (paper space se itera via `doc.layouts`).
3. **Metadata**: `doc.units` es el enum de ezdxf. `$INSUNITS` es la variable de AutoCAD que vale 6 = metros (clave para `mcp-autocad` y para que la conversion mm→drawing unit funcione bien). `$MEASUREMENT` 1 = metrico. `$EXTMIN`/`$EXTMAX` son las esquinas del rectangulo que envuelve la geometria — utiles para saber cuanto abarca el dibujo.
4. **Layouts**: iteramos todos los layouts, saltamos `Model` y guardamos nombres de paper space. Si la lista queda vacia, el DWG no tiene layouts (en SET_01 queres `REP-A1`).
5. **Layers**: por cada capa del DWG leemos nombre, color, linetype, on/frozen/locked. Esto es lo que se cruza contra `SPEC_LAYERS`.
6. **Conteo de entidades**: una pasada por model space, contamos por tipo (`LINE`, `LWPOLYLINE`, `TEXT`, `INSERT`...) y por capa. Ademas:
   - guardamos una muestra de textos (capa + contenido) para entender que dice el plano,
   - guardamos inserts de bloques (`INSERT` = referencia a un bloque; distinto de bloque definido).
7. **Bloques definidos**: `doc.blocks.names()` da los nombres de bloques creados en el DWG (con `BLOCK` o `WBLOCK`).
8. **Delta**: comparamos sets de nombres (`spec_names - existing_names` = faltan; `existing_names - spec_names` = sobrantes). Para los que existen y ademas estan en el spec, comparamos color y linetype.

### `to_markdown(rep)`

Convierte el dict en un reporte Markdown con secciones:
1. Metadata + unidades
2. Layouts
3. Capas: total, faltantes, sobrantes, OK, DELTA
4. Detalle por capa en tabla
5. Entidades (conteos por tipo)
6. Entidades por capa
7. Bloques definidos + inserts
8. Texto + muestra
9. **Areas de mejora** (subseccion "Lo que se llego a hacer" + "Gaps")
10. **Automatizacion sugerida** (AutoLISP, botonera, DWS, DWT, bloques dinamicos, extraccion, MCPs)

### `__main__`

- `sys.argv[1]` = ruta al DWG; `sys.argv[2]` opcional = salida MD (default: `<archivo>.audit.md`).
- Llama `audit`, escribe `.md` y `.json`. Imprime las rutas resultantes.

---

## Que hacer con el reporte

1. Pegar el `.md` en `raw/reports/<fecha>-audit-rep-araoz.md` y vincularlo desde el spec del SET_01.
2. Las secciones **"Gaps"** y **"Automatizacion"** se convierten 1:1 en fichas de `02-ft-SET_01.md` (segun la plantilla "que hace / sintaxis / en SET_01 / URL oficial / relacionados").
3. El `.json` se conserva como evidencia versionable (git-friendly) para comparar entre auditorias sucesivas.

---

## Extensiones futuras (siguiente ciclo)

- Extraer texto de `MTEXT` con sus chunks (mejor manejo de textos largos).
- Comparar bloques **definidos** contra la biblioteca esperada (`R-EJE-MARCA`, `R-PTO-ATTR`, etc.) — hoy solo listamos, no validamos.
- Detectar viewports en paper space y reportar su escala (`ac1_50` / custom).
- Diff entre dos auditorias (versionar el spec del SET_01 sin tocar el script).
