---
tipo: nota
script: scripts/ordena-locales.py
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_02, SET_01, replanteo, locales, planilla, numeracion, csv]
---

# Notas — `scripts/ordena-locales.py`

> Ordena los locales del replanteo (izquierda→derecha, arriba→abajo) y arma la planilla de locales. Lee el DWG por ODA→DXF + ezdxf: **no necesita AutoCAD**.

## 1. Para qué sirve

El bloque `SIMB-LOC_ID` lleva el **número** del local visible (`N_LOC`) y el **nombre** oculto (`TXT_LOC`). Para que la numeración salga en orden de lectura —primero la fila de arriba, de izquierda a derecha, después la siguiente fila— hace falta un criterio explícito, no "a ojo". Este script:

1. agrupa los locales en **filas** (dos locales son de la misma fila si ΔY < tolerancia, 0.30 m por defecto),
2. ordena cada fila de **izquierda a derecha** (X creciente),
3. numera `01..N`,
4. escribe la lista de inserción **y** la planilla de locales.

## 2. Uso

```powershell
# generar la lista de inserción + la planilla (escribe archivos)
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\ordena-locales.py "G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg" `
       --salida "proyectos\MVP_02-autocad-standards\SET_01-REP_Replanteo\docs" [--tol 0.30]

# solo VERIFICAR la numeración (no escribe archivos)
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\ordena-locales.py "G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg" --check
```

- Fuente de datos: si ya hay ejemplares de `SIMB-LOC_ID`, usa sus atributos (`N_LOC` / `TXT_LOC`); si no, usa los rótulos viejos de `A-SIMBOLO-NPT-PLANTA` (`DESCRIPCION` / `N`).
- Al correrlo **después** de insertar los bloques, regenera la planilla con los valores reales.
- **`--check`**: comprueba que el `N_LOC` de cada bloque coincida con su posición de lectura y **no escribe nada**. Es el mismo criterio que usa `LOC-ID-CHECK` dentro de AutoCAD: sirve para revisar la numeración sin abrir el CAD.

> **Ojo — la fuente de datos importa**: si el DWG todavía tiene los rótulos viejos (no hay ejemplares de `SIMB-LOC_ID`), el script **reasigna** los números por posición → en ese caso `--check` no verifica nada. Solo verifica cuando la fuente es el bloque nuevo.

## 3. Qué escribe

| Archivo | Contenido |
|---|---|
| `docs/orden-locales.md` | lista de inserción por filas, con `orden`, número, nombre, X, Y, giro + control (repetidos, vacíos, orden de lectura) |
| `docs/orden-locales.csv` | la misma lista en CSV |
| `docs/cuadro-locales.md` | **planilla de locales** (número, nombre, X, Y, fila) |
| `docs/cuadro-locales.csv` | la planilla en CSV |

## 4. Detalles que importan

- **Tolerancia 0.30 m**: es la que define qué es "la misma fila". Si dos locales de la misma planta están a distinta altura (escalera, entrepiso), se leen en filas distintas. Se ajusta con `--tol`.
- **Y decreciente**: la primera fila es la de mayor Y (la de arriba en el plano).
- **Normalización de tags**: `Nº` / `N°` → `N`; `DESCRIPCIÓN` → `DESCRIPCION` (misma regla que el extractor de atributos).
- **Medición del 19/10 sobre el archivo guardado por el estudio**: 28 locales en 16 filas; el bloque se inserta en ese orden y los números no cambian.
- **La numeración legacy del dibujo no sigue el orden de lectura**: los `N` de los rótulos viejos (`*U323` / `*U324`) dan 28 de 28 fuera de orden (falta el `07`, hay un `12` duplicado). El bloque `SIMB-LOC_ID` (comando `SIMB-LOC_ID`) numera solo y en orden de lectura → el control da 0 desvíos.
- **`ezdxf` es requisito** y vive en el **Python 3.12 del sistema** (`C:\Users\Solch16\AppData\Local\Programs\Python\Python312`, ezdxf 1.4.4) → estos scripts **no** se corren con `P:\Anaconda\envs\comfyenv\python.exe` (ese env es de ComfyUI y no tiene `ezdxf`). Si algún día falta: `C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe -m pip install ezdxf`.

