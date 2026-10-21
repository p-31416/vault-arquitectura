---
tipo: sesion
proyecto: estudio-pi
mvp: 02
set: SET_01-REP
software: [autocad, autocad-lt, oda, ezdxf, com]
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [sesion, mvp_02, rep-araoz, replanteo, lisp, anotativo, viewport, planilla]
---

# Sesión 2026-10-20 (arrancó el 19/10 a la tarde) — REP-ARAOZ: horizontalización, giro de viewport, bloque de locales

## 1. Qué se hizo

1. **Diagnóstico del archivo real** `G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg`: lectura sin AutoCAD vía ODA File Converter 25.12 → DXF → ezdxf 1.4.4 (LT no expone COM).
2. **Descubrimiento del twist**: el layout `REP-PTipo-A1-H` tenía su viewport de plano (`1EC35`) con **twist 270°** → todo el model space se imprimía girado 90° y los rótulos de locales se leían verticales. Regla: `compensación = (−twist) mod 360`.
3. **Estado v1 (guardado 13/10)**: 3 layouts, 50 capas, 14 bloques nombrados, 312 anónimos, 203 inserts, 273 cotas, 29 rótulos de locales.
4. **Entrega de automatización**: `lisp/SET-01-HORIZ.lsp` (analiza/compensa/restaura/viewport a 0) y `lisp/SET-01-SIMB-LOC-ID.lsp` (bloque `SIMB-LOC_ID` con `N_LOC` visible + `TXT_LOC` invisible).
5. **Scripts nuevos**: `scripts/analiza-rotacion-textos.py`, `scripts/extrae-atributos-dwg.py` (atributos → CSV/MD/JSON, con push opcional a n8n → Google Sheet), `scripts/ordena-locales.py` (orden de lectura + planilla de locales), `scripts/chequea-lisp.py`.
6. **Medición del archivo guardado por el estudio (v2)**: 2 layouts (se eliminó `REP-PTipo-A1`), viewport `1EC35` con **twist 360°**, modelo rotado a landscape, 28 rótulos (26 en 0°), 95 tags `SIMB-MURO` (79 rotados), 41 vanos (33 rotados), 17 `C40.20` rotados.

## 2. Archivos creados / modificados

| Archivo | Qué |
|---|---|
| `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/lisp/SET-01-HORIZ.lsp` | horizontalización por compensación de viewport |
| `.../lisp/SET-01-HORIZ_notas.md` | notas + fuentes oficiales |
| `.../lisp/SET-01-SIMB-LOC-ID.lsp` | bloque `SIMB-LOC_ID` + `LOC-ID-CHECK` |
| `.../lisp/SET-01-SIMB-LOC-ID_notas.md` | notas + fuentes oficiales |
| `scripts/analiza-rotacion-textos.py` | viewports con su twist + giros de textos/bloques por capa |
| `scripts/extrae-atributos-dwg.py` (+`_notas.md`) | atributos → planillas (vanos, muros, locales, ejes, columnas) |
| `scripts/ordena-locales.py` (+`_notas.md`) | orden de lectura + planilla de locales |
| `scripts/chequea-lisp.py` | valida paréntesis de los `.lsp` |
| `.../SET_01-REP_Replanteo/docs/orden-locales.md` + `.csv` | lista de inserción de los 28 locales en 16 filas |
| `.../docs/cuadro-locales.md` + `.csv` | planilla de locales (N_LOC / TXT_LOC / X / Y) |
| `.../docs/cuadros-atributos.md`, `atributos-*.csv`, `atributos.json` | cuadros por capa |
| `proyectos/MVP_02-autocad-standards/03-log-mvp_02.md` | entrada de bitácora |

## 3. Cerebro digital

**Topics**: giro de viewport (twist) vs rotación de modelo · anotativos (Match Orientation to Layout) · bloques dinámicos con atributo bloqueado · cotas anotativas · viewport layer freeze vs capa "trampa" · DATAEXTRACTION vs extracción offline · AutoCAD LT sin COM (ActiveX solo interno) · MCP oficial de Autodesk 2027 (bundle instalado, `MCPHTTPSTART` → `localhost:5001/mcp`).

**Entidades**: `REP-ARAOZ.dwg` · `REP-PTipo-A1-H` · `SIMB-LOC_ID` · `N_LOC` / `TXT_LOC` · `SIMB-MURO` · `A-CARP-02` · `A-SIMBOLO-NPT-PLANTA` · `A-COTA-1-50` · `E-COL-TXT` · viewport `1EC35` · ODA File Converter · ezdxf · n8n `set01-carpinterias`.

**Hechos (verificados)**:
- AutoCAD LT **no** se puede automatizar desde afuera por COM (help oficial ACDLT 2027): *"AutoCAD LT can internally utilize the AutoCAD ActiveX type library with AutoLISP, but itself cannot be accessed or manipulated by external applications"*. El MCP `autocad` del vault (COM) queda inutilizable mientras solo haya LT.
- El registro de Windows apunta `AutoCAD.Application.26` a `C:\Archivos de programa\Autodesk\...` (ruta obsoleta en español) → CoCreateInstance falla aunque la clase exista.
- La instalación real es `C:\Program Files\Autodesk\AutoCAD LT 2027` (LT 2027.1, 26.0.118.0). El AutoCAD 2027 full (lic. "LMS Tech", usado en la auditoría del 29/09) ya no está; el instalador quedó en `P:\autocad\AutoCAD.2027_English_64bit`.
- Está instalado el **MCP Server oficial de Autodesk 2027** (`ApplicationPlugins\AutoCAD-MCP-Server-2027.bundle`, soporta `ACADLT`): `NETLOAD acmcp.dll` + `MCPCONFIG` + `MCPHTTPSTART` → `http://localhost:5001/mcp`.
- El archivo v2 del estudio ya trae la numeración de locales `01..28` en el mismo orden de lectura que calcula el script (filas ΔY < 0.30 m, izq→der).
- La numeración de atributos mezcla `Nº`/`N°` y `DESCRIPCIÓN`/`DESCRIPCION` → hay que normalizar antes de armar planillas.

## 4. Pendientes

- [ ] INSERTar los 28 ejemplares de `SIMB-LOC_ID` (el estudio lo hace en AutoCAD: `APPLOAD` → `MK-SIMB-LOC-ID` → `INSERTAR` → `LOC-ID-CHECK`).
- [ ] **Extracción dentro del mismo DWG** (decisión del estudio 20/10): nada de Google Sheets ni n8n. El cuadro de locales se genera desde el DWG y queda en el DWG.
- [ ] Planilla de niveles: faltan los datos (pisos + NPT) → los transcribe el estudio.

## 5. DÓNDE QUEDAMOS — para retomar (20/10, cierre de sesión)

**Decisiones del estudio (20/10):**
- Los giros de los textos (muros, carpintería, columnas) **ya los movió a mano** → `SET-01-NORM-TEXTOS.lsp` queda como herramienta para los próximos planos, no hace falta correrlo en este.
- Los locales pasan a ser **el bloque nuevo** `SIMB-LOC_ID`: rectángulo 0.30×0.20 m + `N_LOC` visible (el número) + `TXT_LOC` **invisible** (el nombre, solo para cómputo y planilla).
- **Sin planillas en Google Sheet**: la extracción se hace **en el mismo DWG**.
- La numeración `01..28` que ya traía el plano coincide con el orden de lectura calculado (filas ΔY < 0.30 m, izq→der) → no hay que renumerar.

**Bloque listo para insertar** (lo corre el estudio):

| Paso | Comando | Qué |
|---|---|---|
| 1 | `APPLOAD` → `SET-01-SIMB-LOC-ID.lsp` | carga |
| 2 | `MK-SIMB-LOC-ID` | crea `SIMB-LOC_ID` (idempotente) |
| 3 | `INSERTAR` → `SIMB-LOC_ID` | en cada local, en el orden de `docs/orden-locales.md`: `N_LOC` = número (01…28), `TXT_LOC` = nombre |
| 4 | `LOC-ID-CHECK` | verifica que la numeración corre 01→28 sin huecos ni repetidos |

**Ojo — `DATAEXTRACTION` NO existe en AutoCAD LT** (artículo oficial de Autodesk): *"AutoCAD LT doesn't support data extraction commands"*; en LT dan *Unknown command* `DATAEXTRACTION`, `ATTIN` y `ATTOUT`. La alternativa oficial en LT es **`ATTEXT`** (extrae valores de atributos a un archivo de texto con plantilla) y `LIST`. Como la extracción tiene que quedar **dentro del DWG**, la vía es un LISP que:
1. lea los atributos `N_LOC` / `TXT_LOC` de los ejemplares de `SIMB-LOC_ID`,
2. escriba el CSV (para el cómputo),
3. **dibuje el cuadro como tabla en el propio dibujo** (filas `MTEXT` en paper space del layout `REP-PTipo-A1-H`).

**Siguiente paso al retomar:** construir `lisp/SET-01-CUADRO-LOCALES.lsp` con el comando `CUADRO-LOCALES` (CSV + tabla dibujada en el DWG) y probarlo en AutoCAD LT.
