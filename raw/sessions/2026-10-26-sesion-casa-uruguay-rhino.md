---
tipo: sesion
fecha: 2026-10-26
mvp: 05
participantes: [agente, Sol]
temas: [rhino8, casa_uruguay, arraigada, pdf, escala_grafica, capas, sectionstyle, comandos, modelado]
---

# Sesión — Casa Uruguay: arranque del 3D en Rhino 8 (import, escala, capas, comandos)

## Qué se hizo

1. **Diagnóstico del puente MCP**: Rhino se había reiniciado (06:14) con documento vacío y sin el script → puerto 9876 sin listener. Relanzado con `_RunPythonScript` desde la línea de comandos. Log: `RhinoMCP script loaded. Server started automatically.`

2. **Descubrimiento**: el usuario ya tenía abierto `G:\Mi unidad\E#E.EDU\mora\set-01-uy.3dm` con el **PDF de Arraigada ya importado** (100.557 objetos: 96.136 polylines, 3.001 hatches, 845 nurbs, 559 polylines, 1 brep, 1 extrusión), 34,8 MB, **en metros**, con las capas `Default`, `Layer 01` y `3D-EST-MAD`. Se respetó su trabajo en vez de reimportar.

3. **Calibración verificada** (el dato clave): la escala gráfica de cada planta mide **exactamente 5,000000 m** en el archivo:
   - PLANTA 1: x 13,281836 → 18,281836 (y −4,959)
   - PLANTA 2: x 13,281836 → 18,281836 (y 18,746)
   Los ticks interiores caen a 1,000 m y 2,000 m de la marca 0 → es la barra `0·1·2·5` publicada. **El import ya está a escala real**: no hay que reescalar. Contraste visual: el ala de la casa mide ~10 m, el doble de la barra.

4. **17 capas creadas** con Section Style propio: 13 de material con los nombres exactos del usuario (`EST-MAD`, `CARP-MET`, `CARP-VID`, `MAD-MARCO_PINO`, `01-PLACA YESO`, `02-FENOLICO`, `03-FILM_POL`, `04-BAST-2.6`, `05-AISL-LANAVID`, `06 TYVEK`, `07-CALV-2.2`, `08-CHAPA-NEGRO`, `09-ZING-CHAPA_GALV`) + 4 de referencia (`REF-PDF-P5`, `REF-PDF-P6`, `REF-TXT`, `00-EJES`). Patrones del documento: Solid, Hatch1, Hatch2, Hatch3, HatchDash, Grid, Grid60, Plus, Squares.

5. **Guardado** con el nombre acordado `G:\Mi unidad\E#E.EDU\mora\3D-casa_uruguay.3dm` (SaveAs; el original `set-01-uy.3dm` queda intacto). La escritura a Drive tardó ~6 min (≈0,1 MB/s).

6. **Guía de comandos escrita**: `proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/01-comandos-rhino-8.md` — importar PDF, `Line`, `Polyline`, `InterpCrv`, `Box` (parantes), `ExtrudeCrv` (opciones `Solid`, `BothSides`, `Direction`), `Offset` + `PlanarSrf` (espesor desde polilínea), **chapa sinusoidal** de alto de onda 0,036 m en 6 pasos, zinguerías con `Sweep1`, `PushPull` / `MoveFace` / `Gumball` para editar caras de un sólido, cheatsheet y errores frecuentes.

## Archivos modificados

| Archivo | Cambio |
|---|---|
| `proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/00-index.md` | Nuevo: ficha del proyecto con el estado verificado y la calibración |
| `proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/01-comandos-rhino-8.md` | Nuevo: guía de comandos Rhino 8 (363 líneas) |
| `log.md` | Entrada de la operación |
| `activos/mvp_05-rhino-mcp/02-CASA-URUGUAY/` | Copia del `.3dm` (pendiente de copiar, ver abajo) |

Fuera de git: `G:\Mi unidad\E#E.EDU\mora\3D-casa_uruguay.3dm` (35 MB, nuevo) y `set-01-uy.3dm` (original del usuario, intacto).

## Cerebro digital — topics

- Rhino 8: import de PDF vectorial (opciones de escala, fills, texto, line weights), calibración por escala gráfica, Section Style por capa, PushPull / MoveFace / Gumball para editar caras, `Offset` + `PlanarSrf` + `ExtrudeCrv` para dar espesor a una polilínea, `Sweep1` con `Solid` y `Rebuild cross sections`.
- Casa frente al mar (Diego Arraigada, Manantiales, Uruguay, 2011, 140 m²): construcción en madera de pino/eucalipto, cubierta a dos aguas, dos alas en ángulo con terraza entre medio, exterior en chapa de fibras vegetales.
- Sistem constructivo del proyecto: `EST-MAD`, `MAD-MARCO_PINO`, `04-BAST-2.6`, `05-AISL-LANAVID`, `02-FENOLICO`, `03-FILM_POL`, `06 TYVEK`, `07-CALV-2.2`, `08-CHAPA-NEGRO`, `09-ZING-CHAPA_GALV`, `01-PLACA YESO`, `CARP-MET`, `CARP-VID`.

## Cerebro digital — entidades

| Entidad | Rol |
|---|---|
| `3D-casa_uruguay.3dm` | Archivo Rhino del proyecto (nuevo, con el PDF importado y las 17 capas) |
| `set-01-uy.3dm` | Archivo previo del usuario con el mismo import (35 MB) |
| `3D-casa_uruguay.dwg` | Gemelo en AutoCAD LT 2027 (cerrado durante la sesión) |
| `Casa frente al mar - Diego Arraigada….pdf` | Fuente del 2D: 6 págs, págs. 5 (plantas + escala gráfica) y 6 (cortes con cotas) |
| Escala gráfica 0·1·2·5 | Referencia de calibración, medida 5,000000 m en ambas plantas |

## Cerebro digital — hechos

1. El PDF de la publicación trae las plantas a una escala gráfica de ~1:175, no 1:50: el dato de calibración es la barra, no la escala nominal.
2. El import del PDF en Rhino 8 puede venir con "line weights" que hacen las curvas aparecer muy gruesas → importarlos desactivados.
3. Las barras de escala se detectan geométricamente: línea horizontal exacta con ticks verticales a 1,000 m de separación; dos barras de 5,000000 m con el mismo span en X confirman la escala.
4. En Rhino 8, `PushPull` (con `Mode = Extend`) y `MoveFace` son las vías para alargar o desplazar una cara de un sólido; el asa Extrude/Extend del Gumball hace lo mismo en vivo.
5. En Rhino 8, `PushPull` (con `Mode = Extend`) y `MoveFace` son las vías para alargar o desplazar una cara de un sólido; el asa Extrude/Extend del Gumball hace lo mismo en vivo.
6. El MCP de AutoCAD no conecta con AutoCAD LT 2027: `PROG_IDS` en `tools/autocad-mcp/autocad_mcp/acad_core.py:60` solo prueba `25.1`, `25` y el genérico; el registro de Windows tiene `AutoCAD.Application.26`. **Corregido al cierre**: se agregó `Application.26` (en el fuente y en la copia instalada del venv); entra en vigor al reiniciar el servidor MCP.
6. Rhino 8 crea *extrusion* (liviana) cuando la curva es plana y la extrusión perpendicular; para cortes conviene polysurface (`Options > General > Uses Extrusions when possible = No`).

## Pendientes

- Copiar el `.3dm` a `activos/mvp_05-rhino-mcp/02-CASA-URUGUAY/` (el guardado en Drive seguía escribiendo al cerrar la sesión).
- Separar el PDF importado en `REF-PDF-P5` / `REF-PDF-P6`.
- Redibujar la planta en las capas de material y extruir a sólidos (alturas desde la pág. 6: +250, +263, +285, +295, +300 cm).
- Construir chapa sinusoidal (alto de onda 0,036 m), zinguerías y parantes según la guía de comandos.
- Hoja A3 con corte 3D y pie de página (procedimiento de AIZ).
