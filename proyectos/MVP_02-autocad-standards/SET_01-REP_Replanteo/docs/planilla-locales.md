---
tipo: tabla
set: SET_01-REP
proyecto: REP-ARAOZ
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_02, SET_01, replanteo, locales, planilla, n_loc, txt_loc, csv]
---

# Planilla de locales — REP-ARAOZ

> Extraída del DWG `G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg` (guardado 20/10/2026 **14:47**) leyendo los atributos `Nº` y `DESCRIPCION` de los rótulos de la capa `A-SIMBOLO-NPT-PLANTA` (ODA File Converter → DXF → ezdxf, sin tocar el DWG).
> Números **puestos a mano por el estudio** (no se reasignan por posición).
> El bloque de los rótulos (`*U482`) define **exactamente dos atributos**: `DESCRIPCION` (nombre) y `Nº` (número) + un `LWPOLYLINE` (el rectángulo) → el CSV sale de ahí, sinalvía.
> CSV gemelo: `docs/planilla-locales.csv` (UTF-8 con BOM → Excel/Sheets lo abren con `ñ` y tildes).

## Tabla

| N_LOC | TXT_LOC (en el CAD) | TXT_LOC_PLANILLA | | N_LOC | TXT_LOC (en el CAD) | TXT_LOC_PLANILLA |
|---|---|---|---|---|---|---|
| 01 | DORMITORIO | DORMITORIO | | 15 | TOILETTE | TOILET |
| 02 | BAÑO | BAÑO | | 16 | COC. - LAV. | COCINA LAVADERO |
| 03 | DORMITORIO | DORMITORIO | | 17 | BALCON | BALCON |
| 04 | DORMITORIO | DORMITORIO | | 18 | ESTAR-COM. | LIVING COMEDOR |
| 05 | BAÑO | BAÑO | | 19 | ESTAR-COM. | LIVING COMEDOR |
| 06 | DORMITORIO | DORMITORIO | | 20 | BALCON | BALCON |
| 07 | BALCON | BALCON | | 21 | DORMITORIO | DORMITORIO |
| 08 | ESTAR-COM. | LIVING COMEDOR | | 22 | BAÑO | BAÑO |
| 09 | ESTAR-COM. | LIVING COMEDOR | | 23 | PALIER | PALIER |
| 10 | BALCON | BALCON | | 24 | ASCENSOR II | ASCENSOR II |
| 11 | COC. - LAV. | COCINA LAVADERO | | 25 | ASCENSOR I | ASCENSOR I |
| 12 | TOILETTE | TOILET | | 26 | ESCALERA | ESCALERA |
| 13 | COC. - LAV. | COCINA LAVADERO | | 27 | BAÑO | BAÑO |
| 14 | COC. - LAV. | COCINA LAVADERO | | 28 | DORMITORIO | DORMITORIO |

> **Las dos columnas de nombre**: `TXT_LOC` es **literalmente** lo que figura en el CAD (el atributo `DESCRIPCION`); `TXT_LOC_PLANILLA` es el mismo local con el nombre extendido que usa el estudio (**LIVING COMEDOR**, **COCINA LAVADERO**, **TOILET**). La numeración y el local son los mismos en las dos (verificado 28/28 contra la lista del estudio).

## Control

| Comprobación | Resultado |
|---|---|
| Locales numerados | **28** (`01`…`28`, del bloque `*U482`) |
| Números repetidos | ninguno |
| Números faltantes | ninguno |
| Rótulos **fuera** de la planilla | `N=00 AMBIENTE` (bloque `*U481`, 1 ejemplar) → es el rótulo de planta baja, no un local numerado (indicación del estudio, 20/10) |
| Nombres con espacios al final | **limpiados** en el CSV (`DORMITORIO `, `ESTAR-COM. `, `COC. - LAV. ` → sin espacio final) |
| Texto suelto en la capa | 1 solo (`NPT+7.634`, una nota de nivel) → los nombres del dibujo **son** los atributos `DESCRIPCION`, no textos aparte |
| Bloque `SIMB-LOC_ID` en el DWG | **0 ejemplares** → los 28 locales numerados son los rótulos `*U482` (con `DESCRIPCION` visible), no el bloque nuevo |

## Totales por denominación

| TXT_LOC | cantidad |
|---|---|
| DORMITORIO | 6 |
| BAÑO | 4 |
| BALCON | 4 |
| COC. - LAV. | 4 |
| ESTAR-COM. | 4 |
| TOILETTE | 2 |
| AMBIENTE | 1 *(planta baja, `N=00`, fuera de la planilla)* |
| PALIER | 1 |
| ESCALERA | 1 |
| ASCENSOR I | 1 |
| ASCENSOR II | 1 |
| **Total locales numerados** | **28** |

## Notas

- La numeración es **la del estudio** (puesta a mano). En orden de lectura (X+ / Y−, filas ΔY < 0.30 m) los números salen `00 02 05 01 06 03 04 07 10 08 09 12 15 16 13 14 18 19 17 20 23 21 25 26 28 22 24 27` → **la numeración a mano no sigue el orden de lectura** (informativo, no se corrige).
- Los rótulos se movieron: hoy agrupan en **14 filas** (antes 16, en la medición del 13/10).
- Con el paso del tiempo, el cuadro local del DWG pasó a tener un `TOILETTE` y un `BAÑO` más (29 rótulos en total, 28 numerados).

## Archivos relacionados

| Archivo | Qué |
|---|---|
| `docs/planilla-locales.csv` | la planilla en CSV (N_LOC, TXT_LOC) |
| `docs/cuadro-locales.csv` / `.md` | cuadro con X, Y y fila (generado por `scripts/ordena-locales.py`) |
| `docs/orden-locales.csv` / `.md` | lista de inserción con orden de lectura, giro, bloque y handle |
| `scripts/ordena-locales.py` | el script que extrae los atributos y arma los cuadros |
