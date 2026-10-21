---
tipo: nota
set: SET_01-REP
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_02, SET_01, lisp, rotacion, viewport, npt, locales, horizonal]
---

# Notas — SET-01-HORIZ.lsp (horizontalización de rótulos de locales)

> Archivo: `lisp/SET-01-HORIZ.lsp` · AutoCAD LT 2027 / AutoCAD 2027 · carga con `APPLOAD`.

## 1. Qué encontré midiendo el DWG (dato, no impresión)

Medición sobre `G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg` (convertido a DXF con ODA File Converter 25.12 y leído con ezdxf 1.4.4 — sin AutoCAD abierto, porque LT no expone COM).

| Dato | Valor |
|---|---|
| Layouts | `Model`, `REP-PTipo-A1`, `REP-PTipo-A1-H` |
| Viewport del plano en `REP-PTipo-A1-H` | handle `1EC35`, **twist = 270°** |
| Viewport del plano en `REP-PTipo-A1` | handle `70FE`, twist = 0° |
| Rótulos de locales | 29 `INSERT` en capa `A-SIMBOLO-NPT-PLANTA` (bloques `*U323`/`*U324`) |
| Atributos del rótulo | `DESCRIPCION` (AMBIENTE, DORMITORIO, BAÑO, ESTAR-COM., COC.-LAV., TOILETTE, BALCON, PALIER, ESCALERA, ASCENSOR I/II) + `Nº` (01…28) |
| Giro actual de los rótulos | 28 de 29 en **0°**; 1 en **180°** (`ASCENSOR I` Nº 27) → ese queda invertido |
| Bloques con giro (siguen la orientación del elemento) | `SIMB-MURO` 53/89 en 90/180/270 · `C40.20` 15/21 · `A-CARP-02` 27/42 |

## 2. Por qué los rótulos no se leen horizontales

El **twist (giro de la vista) del viewport** rota *todo* el model space al imprimir.
Un texto dibujado a 0° en el modelo se ve a `0 + 270 = 270°` en la lámina: vertical, de abajo hacia arriba.

```
compensación = (- twist) mod 360
twist 270°  ->  compensación 90°   (el rótulo queda a 90+270 = 360 = 0° en la hoja)
twist 0°    ->  compensación 0°    (nada que hacer)
```

Por eso en `REP-PTipo-A1` (twist 0) se leen bien y en `REP-PTipo-A1-H` (twist 270) no: el `-H` es la versión apaisada del plano, y al girar la vista 90° los rótulos giran con ella.

## 3. Las tres salidas (elegí una; se pueden combinar)

| Opción | Qué toca | Resultado | Costo |
|---|---|---|---|
| **A. Compensar el modelo** (`HORIZ-APLICA`) | giro de los `INSERT` de la capa NPT (+ sus atributos) | rótulos horizontales en `-H`; en `REP-PTipo-A1` (twist 0) quedan verticales | el modelo queda atado a `-H` |
| **B. Twist del viewport = 0** (`HORIZ-VP0` o doble clic → View Settings → Rotation) | solo el viewport | todo el modelo se lee horizontal en ambas láminas, sin tocar entidades | el plano vuelve a quedar **vertical** en la hoja apaisada (el `-H` pierde el sentido) |
| **C. Anotativo "Match Orientation to Layout"** | definición del bloque `*U324` (+ estilo de texto de los atributos) | el rótulo se mantiene horizontal ante cualquier giro de vista, en las dos láminas | exige activar Annotative en el bloque: es el camino oficial, pero es un cambio estructural (y el bloque pasa a governar escalas anotativas) |

En la práctica: **A** si el `-H` es la lámina vigente; **B** si querés que el modelo sea la fuente única y que ambas láminas lean igual; **C** si querés la solución que resuelve las dos láminas a la vez y aceptás tocar la definición del bloque.

### Opción C en detalle (oficial)

Autodesk: *"Use Annotative objects with the Match Orientation to Layout option. This applies to Block References and Text objects (TEXT, MTEXT, Attributes, etc.)"*

- Rótulo de local = **block reference** → `Insert` → `Block Definition` → `Create Block` → *Name* → elegir `*U324` → en *Behavior*: **Annotative** + **Match Block Orientation to Layout** → *OK* → *Redefine Block*.
- Los **atributos** (`DESCRIPCION`, `Nº`) heredan la orientación del bloque; si se quieren horizontales por sí mismos, el estilo de texto debe llevar *Annotative* → *Match Text Orientation to Layout*.
- Ojo: activar *Annotative* en un bloque lo mete en el juego de escalas anotativas (hay que tener la escala 1:50 en la lista de escalas del dibujo).

Fuente: https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-keep-the-orientation-of-objects-when-rotating-a-layout-sheet-in-AutoCAD.html

### Bloques con ángulo: qué dice la práctica

- `SIMB-MURO` (tag de muro, 89 inserts), `C40.20` (columna) y las carpinterías están girados 90/180/270 **a propósito**: el tag acompaña la dirección del muro o del vano. Girarlos todos a 0 rompe la lectura "el tag está pegado al muro".
- Lo que sí conviene corregir es el **sentido de lectura**: un tag a 180° se lee al revés (de derecha a izquierda). El comando cubre eso: `HORIZ-APLICA` deja **todos** los rótulos de la capa NPT en el mismo ángulo de lectura.
- Si querés que los tags de muro también lean horizontal en la lámina, el mismo cálculo sirve (el giro del tag debería ser `90 - giro_actual`), pero conviene decidirlo **por tipo de elemento**, no en bloque.

## 5. Cómo se ejecuta (dentro de AutoCAD LT 2027)

1. `APPLOAD` → `P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\MVP_02-autocad-standards\SET_01-REP_Replanteo\lisp\SET-01-HORIZ.lsp` → *Load*.
2. `HORIZ-ANALIZA` → reporte: viewports, twist y giro actual de cada rótulo (no modifica nada).
3. `HORIZ-APLICA` → pide confirmación; guarda el giro original en XData `SET_HORIZ`.
4. `HORIZ-RESTAURA` → vuelve todo al giro original. `UNDO` también sirve.

> Antes de aplicar: `SAVEAS` una copia (`REP-ARAOZ.copia-trabajo.dwg`) — el archivo vivo está en `G:`.

## 6. Por qué AutoLISP y no el MCP `autocad` del vault

- El MCP `autocad` del vault (`tools/autocad-mcp`) habla **COM/ActiveX externo**. La doc oficial de AutoCAD LT 2027 es explícita: *"AutoCAD LT can internally utilize the AutoCAD ActiveX type library with AutoLISP, but itself cannot be accessed or manipulated by external applications"* → **LT no se puede automatizar desde afuera por COM**.
- El AutoCAD 2027 completo (el que se usó para la auditoría del 29/09, licencia "LMS Tech") ya no está instalado; queda el instalador en `P:\autocad\AutoCAD.2027_English_64bit`. Instalarlo devuelve el control por COM (y con él el MCP del vault).
- Mientras tanto, AutoLISP **dentro** de AutoCAD LT sí funciona (AutoLISP llegó a LT en la versión 2024): de ahí este archivo.
- Alternativa para control remoto: el **MCP Server oficial de Autodesk 2027** ya está instalado (`C:\Program Files\Autodesk\ApplicationPlugins\AutoCAD-MCP-Server-2027.bundle`, soporta `ACADLT`); se activa con `NETLOAD` de `acmcp.dll` + `MCPCONFIG` + `MCPHTTPSTART` (sirve en `http://localhost:5001/mcp`).

## 7. Referencias oficiales (Autodesk, es_AR, AutoCAD LT 2027)

- ActiveX en LT (limitación COM): https://help.autodesk.com/view/ACDLT/2027/ESP/?guid=GUID-9C082B2D-015E-43C1-9168-623A2EA91D94
- ActiveX Automation en LT (VBA no soportado): https://help.autodesk.com/view/ACDLT/2027/ESP/?guid=GUID-2090E4E8-9AE0-4E01-B5EB-0843A30EB0E9
- `Rotation` (Text, MText, BlockReference, AttributeReference — en radianes): https://help.autodesk.com/view/ACDLT/2027/ESP/?guid=GUID-ADD5CBF4-4C4A-4DE2-A686-4F4DD0CB8734
- Viewport (vista, giro, contenido): https://help.autodesk.com/view/ACDLT/2027/ESP/?guid=GUID-845E7DF4-A76C-4889-BD26-F606E7AA13BB
- `Viewport Object` (miembros ActiveX): https://help.autodesk.com/view/ACDLT/2027/ESP/?guid=GUID-2B609059-6B70-4C66-A442-F5917363462A
- Formato de texto (`Alignment`, `Rotation`, `TextGenerationFlag`): https://help.autodesk.com/view/ACDLT/2027/ESP/?guid=GUID-F0A5E115-9791-435B-B520-1253341B5E1B
