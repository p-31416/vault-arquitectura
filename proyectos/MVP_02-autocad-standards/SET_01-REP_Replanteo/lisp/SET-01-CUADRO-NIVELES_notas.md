---
tipo: nota
set: SET_01-REP
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_02, SET_01, lisp, planilla, niveles, npt, tabla, autolisp, lt, csv]
---

# Notas — `SET-01-CUADRO-NIVELES.lsp` (planilla de niveles desde un CSV)

> Archivo: `lisp/SET-01-CUADRO-NIVELES.lsp` · AutoCAD LT 2027 · `APPLOAD`.
> El **CSV es la fuente de verdad**: el LSP lo lee y dibuja la tabla en el DWG.
> Editás el CSV → `CUADRO-NIVELES-ACT` → la tabla del dibujo se actualiza.

## 0. Por qué no un DATA LINK de AutoCAD (y sí esto)

El *vínculo de datos* nativo de AutoCAD (`DATALINK` + `TABLE`) **no puede leer un
CSV en esta máquina**:

| Comprobación (20/10/2026) | Resultado |
|---|---|
| Excel instalado | **no** (`excel.exe` no existe) |
| Proveedor OLE DB (ACE / Jet) | **ninguno** |
| CSV con BOM UTF-8 | sí (se eliminó) |

El help oficial de AutoCAD LT lo dice: *"Microsoft Excel must be installed to
use Microsoft Excel data links"*. Sin Excel ni ACE, el diálogo **New Excel Data
Link** no arma el preview y el botón **OK** no hace nada (probado: el archivo
queda cargado, el preview vacío, OK inerte).

La vía que sí funciona en LT sin instalar nada: **el LSP lee el CSV** y dibuja
o actualiza la tabla. El resultado práctico es el mismo —el CSV manda sobre el
dibujo— y además funciona en LT.

> Si más adelante se instala Excel (o el *Microsoft Access Database Engine 2016
> Redistributable* x64, que instala el proveedor ACE sin Office), el vínculo
> nativo se puede usar: `DATALINK` → *New Excel Data Link* → el CSV →
> `TABLE` → *From a data link*.

## 1. Comandos

| Comando | Qué |
|---|---|
| `CUADRO-NIVELES` | dibuja la tabla desde el CSV (y si ya hay una, la **actualiza** en el sitio) |
| `CUADRO-NIVELES-ACT` | **actualiza** la tabla existente desde el CSV (borra la anterior y redibuja) |
| `CUADRO-NIVELES-NUEVO` | borra la tabla y la dibuja de nuevo en otro punto |
| `CUADRO-NIVELES-VAL` | **muestra el CSV** en la línea de comandos, sin dibujar nada |

## 2. Uso

```
APPLOAD → SET-01-CUADRO-NIVELES.lsp → Load
CUADRO-NIVELES-VAL          (opcional: revisar los números)
LAYOUT → REP-PTipo-A1-H → ESPACIO PAPER   (si va en el layout)
CUADRO-NIVELES → click en el punto
```

- La tabla queda en la capa **`A-CUADRO-NIVELES`** (se crea sola).
- Alto de fila: **7 mm en paper space / 0.70 m en modelo** (`SET-N:ALTO-FILA`,
  según `CVPORT`).
- Para actualizarla: se edita el CSV y se corre `CUADRO-NIVELES-ACT` → el LSP
  borra **solo** las entidades de la tabla anterior (las que están dentro de su
  caja) y la redibuja.
- Al dibujarla por primera vez, el comando hace **zoom** a la tabla.

## 3. Los datos

Fuente: dato del estudio (20/10/2026). Niveles en metros, 2 decimales, sobre el
nivel 0.00 de planta baja. El CSV: `docs/planilla-niveles.csv` (14 filas × 3
columnas, **sin BOM**).

| PISO | INTERIOR (NPT terminado) | EXTERIOR (BALCON) |
|---|---|---|
| PLANTA BAJA | 0.00 | – |
| 1 PISO | 3.92 | 3.87 |
| 2 PISO | 6.75 | 6.70 |
| 3 PISO | 9.58 | 9.53 |
| 4 PISO | 12.41 | 12.36 |
| 5 PISO | 15.24 | 15.19 |
| 6 PISO | 18.07 | 18.02 |
| 7 PISO | 20.90 | 20.85 |
| 8 PISO | 23.73 | 23.68 |
| 9 PISO (técnica) | 26.56 | – |
| 9 PISO (técnica) | 28.26 | – |
| 9 PISO (técnica) | 30.66 | – |
| 9 PISO (tanque) | **32.06** | – |

Notas al pie: niveles en metros sobre 0.00 de planta baja · exterior (balcón)
5 cm por debajo del interior terminado · 9 PISO: plantas técnicas, 32.06 es la
altura máxima (tanque).

> **Regla confirmada por el estudio (20/10)**: exterior y balcón son **el mismo
> valor** = interior − 0.05 m. Por eso la tabla tiene **3 columnas**.
>
> **A confirmar por el estudio**: (1) planta baja: ¿exterior y balcón en 0.00?;
> (2) los 4 valores del 9 PISO: ¿el 32.06 es el tanque y los otros tres niveles
> de la misma planta técnica?

## 4. Cómo está hecho (para leerlo)

| Parte | Qué |
|---|---|
| `SET-N:CSV` | la ruta del CSV (fuente de verdad) |
| `SET-N:LeeCSV` | lee el CSV → lista de filas; `SET-N:Separa` parte por comas y `SET-N:QuitaBOM` saca el BOM UTF-8 |
| `SET-N:ALTO-FILA` | alto de fila según el espacio (`CVPORT`: 1 = modelo, 0 = paper) |
| `SET-N:Linea` / `SET-N:MTexto` | `entmakex` de `LINE` y de `MTEXT` (código 71 = anclaje: 1 izq, 2 centro; 41 = ancho del rectángulo de referencia) |
| `SET-N:BorraTabla` | borra solo las entidades dentro de `SET-N:CAJA` (la caja de la tabla anterior) |
| `SET-N:DibujaTabla` | recorre filas y columnas: celdas → líneas horizontales y verticales → notas al pie |
| `SET-N:PUNTO` / `SET-N:CAJA` | dónde está la tabla, para poder actualizarla en el sitio |

El `MTEXT` en vez de `TEXT` porque permite **ancho de celda** (el texto se
ajusta al ancho de la columna) y multilínea, sin tener que calcular el ancho
del texto a mano.

**Ojo con la codificación**: el archivo está en **cp1252** (la codificación del
sistema) para que las tildes se lean bien en AutoCAD LT. Si se edita con un
editor que guarde en UTF-8, hay que volver a convertirlo. El CSV va **sin BOM**
(Excel lo abre igual y AutoCAD/ACE no se confunden).

## 5. Referencias oficiales

- Vínculo de datos de una tabla (y el requisito de Excel instalado): https://help.autodesk.com/view/ACDLT/2027/PTB/?guid=GUID-3A038CCF-A659-4E8A-AE6E-1D88D00D3A23
- Diálogo *New Excel Data Link* (ruta completa / relativa / sin ruta, hoja completa): https://help.autodesk.com/view/ACDLT/2027/RUS/?guid=GUID-A9C8C253-C947-4C17-BDE8-911FD3360FF5
- `entmakex` (crea entidad, devuelve `nil` si el dibujo la rechaza): https://help.autodesk.com/view/OARX/2027/RUS/?guid=GUID-D47983BA-1E5D-417D-85B8-6F3DE5F506BA
- AutoLISP en AutoCAD LT (desde LT 2024): https://help.autodesk.com/view/ACDLT/2027/RUS/?guid=GUID-5FB57480-C9BE-4E3D-BEDF-D86035928FFA

## 6. Archivos relacionados

| Archivo | Qué |
|---|---|
| `docs/planilla-niveles.md` / `.csv` | la tabla en el vault (el CSV es el que lee el LSP) |
| `lisp/SET-01-SIMB-LOC-ID.lsp` | bloque de locales (comando `SIMB-LOC_ID`) |
| `scripts/ordena-locales.py` | cuadro de locales (orden de lectura) |
