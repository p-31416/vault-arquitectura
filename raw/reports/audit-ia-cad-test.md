# Auditoria ia-cad-test via COM directo

- AutoCAD version: **26.0s (LMS Tech)**
- DWG activo: `ia-cad-test.dwg`
- Path: `P:\00-repos\proyecto-pi\vault-arquitectura\activos\caddy-salidas\ia-cad-test.dwg`
- INSUNITS: `6`
- EXTMIN: `[-3.2589759656081503, -0.5024999999999545, -1.3552527156068805e-18]`
- EXTMAX: `[4.149999581451993, 4.383584486725191, 0.0]`
- Total entidades model: **10**
- Layers: **11**
- Bloques definidos: **9**

## Layouts

- `Layout1` (Paper) 
- `Layout2` (Paper) 
- `Model` (Model) ACTIVO

## Capas vs spec SET_01 (22 esperadas)

- Faltan del spec: 21 -> ['A-ABER', 'A-LOCA', 'A-TABI', 'G-AUXI', 'G-CART', 'G-COTA', 'G-MARC', 'G-REFE', 'G-TEXT', 'G-VPRT', 'R-COTA', 'R-COTP', 'R-EJAX', 'R-EJES', 'R-FUND', 'R-NIVE', 'R-PTOS', 'S-COLU', 'S-EJES', 'S-FUND', 'S-VIGA']
- Sobrantes (no en spec): 10
- Match exacto: 0/1

### Detalle capas (todas las del DWG)

| Capa | Color | Linetype | On | Frozen | Locked |
|---|---|---|---|---|---|
| `0` | 7 | `Continuous` | True | False | False |
| `A-MURO` | 7 | `Continuous` | True | False | False |
| `A-PTA-` | 1 | `Continuous` | True | False | False |
| `A-AREA` | 5 | `Continuous` | True | False | False |
| `A-CARP` | 1 | `Continuous` | True | False | False |
| `A-MOB` | 3 | `Continuous` | True | False | False |
| `Defpoints` | 7 | `Continuous` | True | False | False |
| `SIMB-CARP` | 33 | `Continuous` | True | False | False |
| `A-COTA-1-50` | 250 | `Continuous` | True | False | False |
| `A-CARP-02` | 251 | `Continuous` | True | False | False |
| `AR-CUADRO DE VANO` | 1 | `Continuous` | True | False | False |

### Entidades por tipo

| Tipo | Cantidad |
|---|---|
| `POLYLINE` | 4 |
| `LINE` | 3 |
| `INSERT` | 2 |
| `TEXT` | 1 |

### Entidades por capa (top 20)

| Capa | Total |
|---|---|
| `A-MURO` | 5 |
| `A-AREA` | 2 |
| `A-CARP` | 2 |
| `A-MOB` | 1 |

### Bloques definidos (top 20 por nombre)

| Bloque | Entities |
|---|---|
| `M2_COTA` | 3 |
| `_Open90` | 3 |
| `_ArchTick` | 1 |
| `PUERTA BATIENTE` | 46 |
| `*U6` | 46 |
| `_DotSmall` | 1 |
| `VENTANA BAJA SIMPLE` | 14 |
| `_None` | 0 |
| `*U10` | 14 |

### Muestra de textos (TEXT)

- `A-AREA` -> 'LOCAL 4x4 - 16m2'

### Muestra de inserts (INSERT)

| Capa | Bloque | Insercion |
|---|---|---|
| `A-CARP` | `PUERTA BATIENTE` | [1.5, 0.0, 0.0] |
| `A-MURO` | `VENTANA BAJA SIMPLE` | [2.0, 4.0, 0.0] |
