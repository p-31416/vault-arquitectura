---
tipo: metodologia
mvp: 02
set: SET_01-REP
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [mvp_02, SET_01, computo, carpinterias, atributos, ventanas, puertas]
fuente: G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg (copia DXF 12:40, ODA + ezdxf)
metodo: scripts en %TEMP% (extrae-carpinterias.py)
estado: v0.1
---

# Cuadro de carpinterías — REP-ARAOZ (agrupado)

> Extraído de los `ATTRIB` de cada ejemplar (42/42 con valores). Cruza con §2 del doc madre: 20 ventanas + 22 puertas. Si editás atributos, se re-extrae en 1 minuto.

## Ventanas — `VENTANA BAJA SIMPLE` (20)

| TIPO | ANCHO (m) | Cantidad |
|---|---|---|
| V01 | 2.30 | 6 |
| V02 | 1.10 | 10 |
| PV01 | 1.75 | 4 |

## Puertas — `PUERTA BATIENTE` (22)

| ID | ANCHO (m) | ALTURA (m) | ALFEIZAR | Descripción | Cantidad |
|---|---|---|---|---|---|
| P-1 | 0.90 | 2.10 | - | Madera Contraplacada | 5 |
| P-2 | 0.80 | 2.10 | - | Madera Contraplacada | 16 |
| P-3 | 1.00 | 2.10 | - | Madera Contraplacada | 1 |

> Base del `EXTRACDAT` de obra (§13 doc madre): este cuadro es la salida agrupada de esa extracción.
> CSV: `cuadro-carpinterias.csv` (misma carpeta, 6 filas + header).

## Salida automática a Google Sheet

Pipe en n8n ([workflow](https://n8n.pitau.tech/workflow/VIQmMEZ9tkDBfKjd), 12 nodos, publicado y activo):

- `POST https://n8n.pitau.tech/webhook/set01-carpinterias` con `{"origen","fecha","rows":[...]}` → busca planilla `SET_01-REP-carpinterias` → si falta la crea (locale `es_AR`, hoja `cuadro`) y la mueve a la carpeta `OS-Emilia/W03-CAD` en Drive → limpia + escribe matriz header+filas por rango (`cuadro!A1:H100`, Sheets API) → responde 200 con `{spreadsheetId, updatedRange, updatedRows, updatedCells}`.
- Cada poste reemplaza el contenido: re-posteable sin duplicados. Verificado 2026-10-13 (56 celdas en `cuadro!A1:H7`).
- Planilla con datos: [SET_01-REP-carpinterias](https://docs.google.com/spreadsheets/d/1bzRI7-lKoQXElnspg2xeGTog5uWw7IiHaWU12joMcDk) — vive en la [carpeta W03-CAD](https://drive.google.com/drive/folders/1qJgNDKX_eJSr7M5JDKcpKrGVdBNPqzGm) (sincroniza a `G:\Mi unidad\OS-Emilia\W03-CAD`); las próximas planillas nuevas caen solas en esa carpeta. Incidente 2026-10-13: ambas copias terminaron en papelera y se restauró la con datos (verificada `trashed:false`, padre W03-CAD vía API).
- Credenciales OAuth del vault (Drive + Sheets `ppi-EmiliaOS_*`, solo IDs en este doc).
