# Auditoria DWG vs SET_01-REP

- **Archivo:** `Barcelona-2D.dxf`
- **Fecha:** 2026-10-21T01:27:22
- **ezdxf:** 1.4.4
- **Unidad drawing (ezdxf):** `6`
- **`$INSUNITS`:** `6`  (4=mm, 6=m)
- **`$MEASUREMENT`:** `0`  (0=imperial, 1=metric)
- **`$EXTMIN`:** `[409692.71, 4560548.975000001, 0.0]`
- **`$EXTMAX`:** `[450136.531, 4599261.38, 0.0]`

## Layouts (paper-space, no Model)

- `Layout1`

## Capas contra spec SET_01 (22 esperadas)

- **Existentes en DWG:** 96
- **Faltan del spec:** 22 -> ['A-ABER', 'A-LOCA', 'A-MURO', 'A-TABI', 'G-AUXI', 'G-CART', 'G-COTA', 'G-MARC', 'G-REFE', 'G-TEXT', 'G-VPRT', 'R-COTA', 'R-COTP', 'R-EJAX', 'R-EJES', 'R-FUND', 'R-NIVE', 'R-PTOS', 'S-COLU', 'S-EJES', 'S-FUND', 'S-VIGA']
- **Sobrantes (no en spec):** 96 -> ['0', 'Accés Rondes (sentit horari)', 'Accés Rondes (sentit no horari)', 'Ascensors', 'Camins ús restringit vehicles', 'Camps Esportius', 'Carrers amplada GRAN Districte 1', 'Carrers amplada GRAN Districte 10', 'Carrers amplada GRAN Districte 2', 'Carrers amplada GRAN Districte 3', 'Carrers amplada GRAN Districte 4', 'Carrers amplada GRAN Districte 5', 'Carrers amplada GRAN Districte 6', 'Carrers amplada GRAN Districte 7', 'Carrers amplada GRAN Districte 8', 'Carrers amplada GRAN Districte 9', 'Carrers amplada MITJANA Districte 1', 'Carrers amplada MITJANA Districte 10', 'Carrers amplada MITJANA Districte 2', 'Carrers amplada MITJANA Districte 3', 'Carrers amplada MITJANA Districte 4', 'Carrers amplada MITJANA Districte 5', 'Carrers amplada MITJANA Districte 6', 'Carrers amplada MITJANA Districte 7', 'Carrers amplada MITJANA Districte 8', 'Carrers amplada MITJANA Districte 9', 'Carrers amplada PETITA Districte 1', 'Carrers amplada PETITA Districte 10', 'Carrers amplada PETITA Districte 2', 'Carrers amplada PETITA Districte 3', 'Carrers amplada PETITA Districte 4', 'Carrers amplada PETITA Districte 5', 'Carrers amplada PETITA Districte 6', 'Carrers amplada PETITA Districte 7', 'Carrers amplada PETITA Districte 8', 'Carrers amplada PETITA Districte 9', 'Cobertes Edificis', 'Corbes de nivell', 'Cotes', 'Defpoints', 'Edificació en Cementiris', 'Edificis Culturals', 'Edificis Educatius', 'Edificis Esportius', 'Edificis Religiosos', 'Edificis Sanitaris', 'Edificis en Illes parcialment edificades', 'Edificis singulars (Genèrics)', 'Elements Constructius (Parcs i Via pública)', 'Escales Mecàniques', 'Estacio marítima', 'Estacions FGC', 'Estacions Metro', 'Estacions RENFE', 'Estació Ferrocarril Aeroport', 'Funicular', 'Hospitals', 'Illa Edificada', 'Illes Peatonals i voreres', 'Límit port autònom', 'Límits aigua (mar - rius)', 'Límits aigua (piscines - fonts)', 'Línies de Projectes', 'Mercats Municipals', 'Monuments', 'Numeració postal Districte 1', 'Numeració postal Districte 10', 'Numeració postal Districte 2', 'Numeració postal Districte 3', 'Numeració postal Districte 4', 'Numeració postal Districte 5', 'Numeració postal Districte 6', 'Numeració postal Districte 7', 'Numeració postal Districte 8', 'Numeració postal Districte 9', 'Parades taxi', 'Parterres (Carrers i Places)', 'Parterres (Parcs i Jardins)', 'Pistes forestals', 'Punt altimetria (trama urbana)', 'Punt altimetria (turons)', 'Separadors Vials', 'Seus de Districte', 'Solars', 'Sortides Rondes (sentit horari)', 'Sortides Rondes (sentit no horari)', 'Telefèric', 'Torres de Comunicació', 'Tramvia Blau', 'Tramvies (TramBaix i TramBesos)', 'Tramvies (vies)', 'Túnels - Rondes - Vies ferries - Escales', 'Zona Forestal', 'Zona Verd Privat', 'Zona Verd Públic', 'Zones Peatonals']
- **OK (color + linetype coinciden):** 0
- **DELTA (color o linetype distinto):** 0

### Detalle por capa (existentes en DWG)

| Capa | Color DWG | Color spec | Linetype DWG | Linetype spec | Estado |
|---|---|---|---|---|---|

## Entidades en model space

| Tipo | Cantidad |
|---|---|
| `LWPOLYLINE` | 75228 |
| `HATCH` | 43032 |
| `TEXT` | 34574 |
| `LINE` | 7213 |
| `INSERT` | 1344 |
| `MTEXT` | 547 |
| `SOLID` | 316 |
| `CIRCLE` | 99 |
| `POINT` | 42 |
| `SPLINE` | 1 |

## Entidades por capa

| Capa | Total | Tipos |
|---|---|---|
| `Edificis en Illes parcialment edificades` | 28118 | HATCH=14054, LWPOLYLINE=14063, LINE=1 |
| `Parterres (Parcs i Jardins)` | 10681 | HATCH=5336, LWPOLYLINE=5345 |
| `Túnels - Rondes - Vies ferries - Escales` | 10625 | LWPOLYLINE=9072, LINE=1552, POINT=1 |
| `Camps Esportius` | 10311 | LWPOLYLINE=9041, LINE=1270 |
| `Elements Constructius (Parcs i Via pública)` | 9285 | LINE=3213, LWPOLYLINE=6049, POINT=23 |
| `Corbes de nivell` | 8660 | LWPOLYLINE=8659, POINT=1 |
| `Parterres (Carrers i Places)` | 7324 | HATCH=3655, LWPOLYLINE=3668, LINE=1 |
| `Illa Edificada` | 7185 | HATCH=3591, LWPOLYLINE=3593, POINT=1 |
| `Zona Verd Públic` | 4097 | HATCH=2047, LWPOLYLINE=2050 |
| `Solars` | 3937 | HATCH=1967, LWPOLYLINE=1970 |
| `Edificació en Cementiris` | 3830 | HATCH=1915, LWPOLYLINE=1915 |
| `Límits aigua (piscines - fonts)` | 3474 | HATCH=1734, LWPOLYLINE=1740 |
| `Illes Peatonals i voreres` | 3303 | HATCH=1651, LWPOLYLINE=1652 |
| `Numeració postal Districte 5` | 3285 | TEXT=3285 |
| `Edificis singulars (Genèrics)` | 2961 | HATCH=1480, LWPOLYLINE=1481 |
| `Separadors Vials` | 2650 | HATCH=1322, LWPOLYLINE=1327, SPLINE=1 |
| `Numeració postal Districte 10` | 2571 | TEXT=2571 |
| `Numeració postal Districte 7` | 2494 | TEXT=2494 |
| `Numeració postal Districte 8` | 2326 | TEXT=2326 |
| `Zona Verd Privat` | 2183 | HATCH=1090, LWPOLYLINE=1092, POINT=1 |
| `Numeració postal Districte 3` | 1992 | TEXT=1992 |
| `Numeració postal Districte 6` | 1934 | TEXT=1934 |
| `Numeració postal Districte 9` | 1804 | TEXT=1804 |
| `Numeració postal Districte 2` | 1798 | TEXT=1798 |
| `Carrers amplada PETITA Districte 5` | 1524 | TEXT=1518, MTEXT=6 |
| `Cobertes Edificis` | 1380 | LWPOLYLINE=898, LINE=479, POINT=3 |
| `Zones Peatonals` | 1358 | HATCH=1048, SOLID=304, POINT=2, LWPOLYLINE=3, LINE=1 |
| `Carrers amplada PETITA Districte 1` | 1325 | TEXT=1325 |
| `Edificis Educatius` | 1220 | HATCH=610, LWPOLYLINE=610 |
| `Numeració postal Districte 4` | 1208 | TEXT=1208 |
| `Numeració postal Districte 1` | 1079 | TEXT=1079 |
| `Carrers amplada PETITA Districte 7` | 999 | TEXT=996, MTEXT=3 |
| `Carrers amplada MITJANA Districte 3` | 814 | TEXT=814 |
| `Carrers amplada PETITA Districte 6` | 810 | TEXT=810 |
| `Carrers amplada PETITA Districte 10` | 786 | TEXT=785, MTEXT=1 |
| `Carrers amplada MITJANA Districte 5` | 748 | TEXT=748 |
| `Carrers amplada MITJANA Districte 7` | 742 | TEXT=742 |
| `Carrers amplada PETITA Districte 3` | 726 | TEXT=726 |
| `Carrers amplada MITJANA Districte 8` | 665 | TEXT=665 |
| `Línies de Projectes` | 661 | LINE=616, LWPOLYLINE=38, POINT=7 |
| `Estacions Metro` | 642 | INSERT=492, TEXT=146, MTEXT=4 |
| `Carrers amplada PETITA Districte 9` | 628 | TEXT=624, MTEXT=4 |
| `Carrers amplada PETITA Districte 8` | 621 | TEXT=620, MTEXT=1 |
| `Carrers amplada MITJANA Districte 10` | 618 | TEXT=618 |
| `Carrers amplada MITJANA Districte 9` | 482 | TEXT=482 |
| `Carrers amplada PETITA Districte 4` | 435 | TEXT=435 |
| `Punt altimetria (trama urbana)` | 432 | INSERT=185, MTEXT=247 |
| `Carrers amplada MITJANA Districte 2` | 423 | TEXT=423 |
| `Edificis Esportius` | 418 | HATCH=209, LWPOLYLINE=209 |
| `Edificis Sanitaris` | 370 | HATCH=185, LWPOLYLINE=185 |
| `Carrers amplada MITJANA Districte 4` | 362 | TEXT=362 |
| `Límits aigua (mar - rius)` | 353 | SOLID=11, HATCH=342 |
| `Punt altimetria (turons)` | 302 | INSERT=124, MTEXT=178 |
| `Edificis Religiosos` | 262 | HATCH=131, LWPOLYLINE=131 |
| `Carrers amplada PETITA Districte 2` | 259 | TEXT=257, MTEXT=2 |
| `Zona Forestal` | 252 | HATCH=125, LWPOLYLINE=127 |
| `Edificis Culturals` | 224 | HATCH=112, LWPOLYLINE=112 |
| `Carrers amplada MITJANA Districte 1` | 214 | TEXT=214 |
| `Carrers amplada MITJANA Districte 6` | 207 | TEXT=207 |
| `Tramvies (TramBaix i TramBesos)` | 199 | INSERT=147, TEXT=52 |
| `Monuments` | 185 | HATCH=92, LWPOLYLINE=93 |
| `Parades taxi` | 184 | INSERT=184 |
| `Pistes forestals` | 181 | HATCH=179, SOLID=1, LWPOLYLINE=1 |
| `Tramvies (vies)` | 119 | LINE=66, LWPOLYLINE=50, POINT=3 |
| `Cotes` | 101 | MTEXT=101 |
| `Estacions FGC` | 91 | INSERT=65, TEXT=26 |
| `Accés Rondes (sentit horari)` | 87 | HATCH=29, CIRCLE=29, TEXT=29 |
| `Mercats Municipals` | 82 | HATCH=41, LWPOLYLINE=41 |
| `Sortides Rondes (sentit no horari)` | 78 | HATCH=26, CIRCLE=26, TEXT=26 |
| `Sortides Rondes (sentit horari)` | 72 | HATCH=24, CIRCLE=24, TEXT=24 |
| `Hospitals` | 69 | INSERT=69 |
| `Accés Rondes (sentit no horari)` | 60 | HATCH=20, CIRCLE=20, TEXT=20 |
| `Carrers amplada GRAN Districte 10` | 58 | TEXT=58 |
| `Carrers amplada GRAN Districte 3` | 57 | TEXT=57 |
| `Carrers amplada GRAN Districte 2` | 55 | TEXT=55 |
| `Carrers amplada GRAN Districte 5` | 39 | TEXT=39 |
| `Carrers amplada GRAN Districte 7` | 38 | TEXT=38 |
| `Seus de Districte` | 34 | HATCH=12, LWPOLYLINE=12, INSERT=10 |
| `Carrers amplada GRAN Districte 9` | 32 | TEXT=32 |
| `Carrers amplada GRAN Districte 8` | 32 | TEXT=32 |
| `Carrers amplada GRAN Districte 6` | 27 | TEXT=27 |
| `Escales Mecàniques` | 26 | INSERT=26 |
| `Carrers amplada GRAN Districte 1` | 20 | TEXT=20 |
| `Estacions RENFE` | 19 | INSERT=14, TEXT=5 |
| `Carrers amplada GRAN Districte 4` | 18 | TEXT=18 |
| `Límit port autònom` | 15 | LINE=14, LWPOLYLINE=1 |
| `Funicular` | 15 | INSERT=8, TEXT=7 |
| `Estacio marítima` | 8 | INSERT=8 |
| `Telefèric` | 6 | INSERT=6 |
| `Camins ús restringit vehicles` | 5 | HATCH=5 |
| `Tramvia Blau` | 3 | INSERT=2, TEXT=1 |
| `Torres de Comunicació` | 2 | INSERT=2 |
| `Ascensors` | 1 | INSERT=1 |
| `Estació Ferrocarril Aeroport` | 1 | INSERT=1 |

## Bloques

- **Definidos en DWG:** 46
- **Inserts (`INSERT`) usados:** 1344
- Lista:
  - `*model_space`
  - `*paper_space`
  - `*u11`
  - `*u13`
  - `*u15`
  - `*u17`
  - `*u19`
  - `*u34`
  - `*u36`
  - `*u38`
  - `aeropo`
  - `ascens`
  - `blau`
  - `escala`
  - `ffcc`
  - `funicu`
  - `hospi`
  - `l1`
  - `l10`
  - `l11`
  - `l2`
  - `l3`
  - `l4`
  - `l5`
  - `l6`
  - `l7`
  - `l8`
  - `l9`
  - `mariti`
  - `metro`
  - `ptoalt`
  - `ptoalt_1`
  - `renfe`
  - `seu`
  - `t1`
  - `t2`
  - `t3`
  - `t4`
  - `t5`
  - `t6`
  - `taxi`
  - `telefe`
  - `terminatoropen_0.5`
  - `torre1`
  - `torre2`
  - `tramvi`

## Texto (TEXT / MTEXT)

- **`TEXT` count (via entidades iteradas):** _incluido arriba_
- **`MTEXT` count:** 547

### Muestra de textos (capa, contenido)
- `Carrers amplada MITJANA Districte 5` -> 'C. de Lázaro    Cárdenas'
- `Carrers amplada MITJANA Districte 5` -> 'C.  de  Jacinto    Benavente'
- `Numeració postal Districte 5` -> '18'
- `Numeració postal Districte 1` -> '26'
- `Numeració postal Districte 1` -> '23'
- `Numeració postal Districte 1` -> '21'
- `Numeració postal Districte 1` -> '29'
- `Numeració postal Districte 1` -> '8'
- `Numeració postal Districte 1` -> '20'
- `Numeració postal Districte 1` -> '17'
- `Numeració postal Districte 1` -> '14'
- `Numeració postal Districte 1` -> '8'
- `Numeració postal Districte 1` -> '5'
- `Numeració postal Districte 1` -> '2'
- `Numeració postal Districte 1` -> '28'

## Areas de mejora

### Lo que se llego a hacer
- DWG con 96 capas y 162396 entidades; cubre el SET_REP.
- Bloques definidos: 46.

### Gaps contra SET_01
- **Faltan del spec:** `A-ABER`, `A-LOCA`, `A-MURO`, `A-TABI`, `G-AUXI`, `G-CART`, `G-COTA`, `G-MARC`, `G-REFE`, `G-TEXT`, `G-VPRT`, `R-COTA`, `R-COTP`, `R-EJAX`, `R-EJES`, `R-FUND`, `R-NIVE`, `R-PTOS`, `S-COLU`, `S-EJES`, `S-FUND`, `S-VIGA`.
- **Capas fuera del spec:** `0`, `Accés Rondes (sentit horari)`, `Accés Rondes (sentit no horari)`, `Ascensors`, `Camins ús restringit vehicles`, `Camps Esportius`, `Carrers amplada GRAN Districte 1`, `Carrers amplada GRAN Districte 10`, `Carrers amplada GRAN Districte 2`, `Carrers amplada GRAN Districte 3`, `Carrers amplada GRAN Districte 4`, `Carrers amplada GRAN Districte 5`, `Carrers amplada GRAN Districte 6`, `Carrers amplada GRAN Districte 7`, `Carrers amplada GRAN Districte 8`, `Carrers amplada GRAN Districte 9`, `Carrers amplada MITJANA Districte 1`, `Carrers amplada MITJANA Districte 10`, `Carrers amplada MITJANA Districte 2`, `Carrers amplada MITJANA Districte 3`, `Carrers amplada MITJANA Districte 4`, `Carrers amplada MITJANA Districte 5`, `Carrers amplada MITJANA Districte 6`, `Carrers amplada MITJANA Districte 7`, `Carrers amplada MITJANA Districte 8`, `Carrers amplada MITJANA Districte 9`, `Carrers amplada PETITA Districte 1`, `Carrers amplada PETITA Districte 10`, `Carrers amplada PETITA Districte 2`, `Carrers amplada PETITA Districte 3`, `Carrers amplada PETITA Districte 4`, `Carrers amplada PETITA Districte 5`, `Carrers amplada PETITA Districte 6`, `Carrers amplada PETITA Districte 7`, `Carrers amplada PETITA Districte 8`, `Carrers amplada PETITA Districte 9`, `Cobertes Edificis`, `Corbes de nivell`, `Cotes`, `Defpoints`, `Edificació en Cementiris`, `Edificis Culturals`, `Edificis Educatius`, `Edificis Esportius`, `Edificis Religiosos`, `Edificis Sanitaris`, `Edificis en Illes parcialment edificades`, `Edificis singulars (Genèrics)`, `Elements Constructius (Parcs i Via pública)`, `Escales Mecàniques`, `Estacio marítima`, `Estacions FGC`, `Estacions Metro`, `Estacions RENFE`, `Estació Ferrocarril Aeroport`, `Funicular`, `Hospitals`, `Illa Edificada`, `Illes Peatonals i voreres`, `Límit port autònom`, `Límits aigua (mar - rius)`, `Límits aigua (piscines - fonts)`, `Línies de Projectes`, `Mercats Municipals`, `Monuments`, `Numeració postal Districte 1`, `Numeració postal Districte 10`, `Numeració postal Districte 2`, `Numeració postal Districte 3`, `Numeració postal Districte 4`, `Numeració postal Districte 5`, `Numeració postal Districte 6`, `Numeració postal Districte 7`, `Numeració postal Districte 8`, `Numeració postal Districte 9`, `Parades taxi`, `Parterres (Carrers i Places)`, `Parterres (Parcs i Jardins)`, `Pistes forestals`, `Punt altimetria (trama urbana)`, `Punt altimetria (turons)`, `Separadors Vials`, `Seus de Districte`, `Solars`, `Sortides Rondes (sentit horari)`, `Sortides Rondes (sentit no horari)`, `Telefèric`, `Torres de Comunicació`, `Tramvia Blau`, `Tramvies (TramBaix i TramBesos)`, `Tramvies (vies)`, `Túnels - Rondes - Vies ferries - Escales`, `Zona Forestal`, `Zona Verd Privat`, `Zona Verd Públic`, `Zones Peatonals` (revisar uso real).

## Automatizacion sugerida

### AutoLISP (scripts `lisp/`)
- **Aplicador de spec:** `SET-01-REP` crea las 22 capas (color/ltype/lineweight) segun `02-ft-SET_01.md` §1 y spec §2. Idempotente: si existe, no la duplica.
- **LAYER audits:** `AUDIT-LAYERS` compara el dibujo activo contra `EP-REP.dws` y reporta delta (coincide / falta / sobra) via `acet-laytrans` o `LAYTRANS` UI.
- **Bloques con atributos:** `MK-R-PTO` inserta `R-PTO-ATTR` con prompts ID,X,Y,Z y aplica `R-PTOS`.
- **Bloques dinamicos:** puerta (`R-ABER-DYN`) con parametros Linear + Visibility (abierta/cerrada/90).

### Botonera (paleta CUI/.cui o `.cuix`)
- Cargar desde W03-CAD; agrega botones para `SET-01-REP`, `AUDIT-LAYERS`, `MK-R-PTO`, `R-EJE-MARCA`.

### DWS (Drawing Standards)
- `EP-REP.dws` con las 22 capas, estilos de texto y de cota del SET; verificar con `CHECKSTANDARDS` y Batch Standards Checker (`.chx`).

### DWT (template)
- `EP-REP.dwt`: DWGUNITS 6 (m), INSUNITS 6, layout `REP-A1` A1 apaisado con viewport a 1:50 Display Locked, escala custom `1:50 (m)` en `SCALELISTEDIT`.

### Bloques dinamicos
- `R-EJE-MARCA` (letra o numero), `R-PTO-ATTR` (ID/X/Y/Z), `R-NIVEL-TAG` (cota).
- `R-ABER-DYN` puerta con Visibility States (0.60 / 0.70 / 0.80 / 0.90 / 1.00 m).

### Extraccion de datos (planillas)
- `DATAEXTRACTION` desde bloques con atributos `R-PTO-ATTR` -> CSV/XLS de coordenadas replanteo.
- `EATTEXT` / `ATTEXT` (CDF/CSV) si no se quiere la UI.

### Auditoria viva (MCP `autocad`)
- `list_layers` + `query_entities(layer=R-EJES)` -> comparar contra este spec.
- `autodesk-help_search_help_content` con `product_code=ACD, release_code=2027, locale=es_ES` para citas oficiales.
