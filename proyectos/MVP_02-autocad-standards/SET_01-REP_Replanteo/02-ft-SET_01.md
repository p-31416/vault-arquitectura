---
tipo: ft
mvp: 02
set: SET_01-REP
fecha_creacion: 2026-09-27
ultima_actualizacion: 2026-09-27
tags: [mvp_02, SET_01, ft, metodologia, comandos]
---

# 02-ft — SET_01-REP: cómo se hace (manual, con MCPs)

> Metodología paso a paso. El usuario la completa manualmente apoyado en MCP `autocad` (ejecución) y `autodesk-help` (documentación oficial). Estructura espeja `01-spec-SET_01.md` §0 (10 items DoD).

## 1. SETEO — Unidades, escalas, layout (valores en spec §4.2)

Base: dibujo NUEVO desde `acadiso.dwt` (QNEW). NO tocar el DWG de proyecto abierto.

1. **Metros**: `-DWGUNITS` → unidad 6 (Meters) → decimal → precisión 2 → escalar objetos: No → igualar INSUNITS: Sí. Alternativa por diálogo: `UNITS` (Type Decimal, Precision 0.00) + `INSUNITS` → 6 (Meters).
2. **Verificar**: `autocad_status` → `insunits: 6` (meters), sin `unit_warning`.
3. **Escala custom**: `SCALELISTEDIT` → Add → nombre `1:50 (m)` → Paper units 1 → Drawing units 0.05 → OK.
4. **Layout A1**: `LAYOUT` → New → renombrar `REP-A1` → `PAGESETUP` → `DWG To PDF.pc3` → ISO A1 841×594 apaisado → trazado 1:1.
5. **Viewport**: `MVIEW` → dibujar ventana → clic dentro → `ZOOM 1000/50 XP` (equivale a Custom scale 20 o Standard `1:50 (m)`) → verificar escala → Properties → Display locked: Yes.
6. **Guardar template**: `SAVEAS` → tipo DWT → `activos/proyectos/mvp_02-autocad-standards/SET_01-REP/SET_01-REP.dwt` (NO en git).
7. **Duda de comando**: `autodesk-help_search_help_content` (p. ej. "SCALELISTEDIT custom scale paper drawing units").

## 2. LAYERS — Creación

_Completar: `LAYER` por cada una de las 22 capas §2 del spec. O ejecutar `lisp/SET_01-REP.lsp` (`SET-01-REP`). Verificar con `autocad_query_entities` / capa._

## 3. CTB — Asignación

_Completar: `PAGESETUP` + `EP-ISO.ctb` o fallback `monochrome.ctb`._

## 4. TEXTSTYLES — `EP-2.5`, `EP-3.5`

_Completar: `STYLE`. Duda → `autodesk-help_search_help_content` ("AutoCAD text style annotative")._

## 5. DIMSTYLES — `EP-ARQ`

_Completar: `DIMSTYLE`. 20+ variables — crear vía DWT base o documentar una por una._

## 6. BLOQUES — Biblioteca

_Completar: `BLOCK`/`WBLOCK` para `R-EJE-MARCA`, `R-PTO`, `R-NIVEL` → `activos/.../SET_01-REP_bloques.dwg`._

## 7. ATRIBUTOS + DATAEXTRACTION

_Completar: `ATTDEF` en `R-PTO-ATTR` (ID,X,Y,Z) → `DATAEXTRACTION` → cuadro coordenadas._

## 8. TEMPLATE — Guardar DWT

_Completar: con 1–7 listo, `SAVEAS` → `activos/.../SET_01-REP.dwt`._

## 9. AUTOLISP — Verificación

_Completar: `APPLOAD lisp/SET_01-REP.lsp` → `SET-01-REP` en dibujo limpio → verificar 22 capas._

## 10. GLOSARIO — Diferido

_Pendiente hasta evaluar SET_01 (decisión SOL)._
