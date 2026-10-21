---
tipo: tabla
set: SET_01-REP
proyecto: REP-ARAOZ
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_02, SET_01, replanteo, niveles, planilla, npt, columnas]
---

# Planilla de niveles — REP-ARAOZ

> Fuente: dato del estudio (20/10/2026). Niveles **en metros**, con 2 decimales, sobre el nivel 0.00 de planta baja.
> Se dibuja dentro del DWG con `lisp/SET-01-CUADRO-NIVELES.lsp` → comando `CUADRO-NIVELES` (tabla de MTEXT + LINE en la capa `A-CUADRO-NIVELES`).

## Tabla

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

## Notas

- Niveles en metros, sobre el nivel 0.00 de planta baja.
- **Exterior y balcón: 5 cm por debajo del nivel interior terminado.**
- 9 PISO: plantas técnicas. **32.06 es la altura máxima (tanque).**

## Criterio de cálculo

| Piso | Interior | Exterior / balcón | Diferencia |
|---|---|---|---|
| 1 | 3.92 | 3.87 | −0.05 |
| 2 | 6.75 | 6.70 | −0.05 |
| 3 | 9.58 | 9.53 | −0.05 |
| 4 | 12.41 | 12.36 | −0.05 |
| 5 | 15.24 | 15.19 | −0.05 |
| 6 | 18.07 | 18.02 | −0.05 |
| 7 | 20.90 | 20.85 | −0.05 |
| 8 | 23.73 | 23.68 | −0.05 |

> **Regla confirmada por el estudio (20/10)**: exterior y balcón son **el mismo valor**, y ese valor es **el interior menos 0.05 m**.
>
> **A confirmar por el estudio**:
> 1. **PLANTA BAJA**: ¿el exterior y el balcón van en 0.00 o llevan otra cota?
> 2. **9 PISO**: los cuatro valores (26.56 / 28.26 / 30.66 / 32.06) son plantas técnicas: ¿el 32.06 es el tanque (altura máxima) y los otros tres son niveles intermedios de la misma planta técnica?

## Archivos relacionados

| Archivo | Qué |
|---|---|
| `lisp/SET-01-CUADRO-NIVELES.lsp` | comando `CUADRO-NIVELES` (dibuja la tabla) y `CUADRO-NIVELES-VAL` (muestra los datos) |
| `lisp/SET-01-CUADRO-NIVELES_notas.md` | notas del LSP (uso, parámetros, cómo corregir un dato) |
| `docs/planilla-niveles.csv` | la misma tabla en CSV |
