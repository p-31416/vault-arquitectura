---
tipo: sesion
fecha: 2026-10-25
mvp: 05
participantes: [agente, Sol]
temas: [rhino8, mcp, cortes, clippingplane, sectionstyle, layout, escala, a3]
---

# Sesión — Corte 3D en hoja A3 a 1:50 (Rhino 8, caso AIZ)

## Qué se hizo

1. **Diagnóstico del puente MCP caído.** `get_rhino_scene_info` devolvía `WinError 10061`. Causa: `scripts/rhino-mcp-server-rhino.py` corre dentro del proceso Rhino y muere con él; Rhino se había reabierto a las 17:05 sin relanzar el script, así que el puerto 9876 no tenía listener. Se relanzó con `_RunPythonScript "…\scripts\rhino-mcp-server-rhino.py"` desde la línea de comandos de Rhino, vía SendKeys + SetForegroundWindow.

2. **Inspección del archivo en solo lectura** (`set-ej_corte.3dm`, 161 objetos): 159 mallas (158 cerradas + la abierta `Object_3` en `3D-REV-01`), 1 clipping plane `A-A` (plano vertical en X = 575, normal +X, `PlaneDepthEnabled = False`), 7 capas de material con section style solo en 3, bbox 10,37 × 22,00 × 18,15 m, y 4 viewports ya en proyección paralela (`axo3060` con la 30/60 en Shaded, más `Top`, `Front`, `Right`).

3. **Hoja A3 a 1:50 construida por MCP:** página `AIZ-CORTE-A` (420 × 297 mm), detalle de 400 × 270 mm en (10, 22)–(410, 292) mm, cámara heredada de `axo3060` (dir 0,743 · 0,577 · −0,339; up 0,268 · 0,208 · 0,941), modo Shaded, clipping `A-A` habilitado dentro del detalle y pie de hoja de 2 líneas en espacio papel.

4. **Composición calculada, no improvisada:** se proyectó el lado visible del corte (X ≥ 575) contra la cámara y se centra la composición con el objetivo de cámara. Resultado: 19,94 × 13,88 m proyectados → 398,8 × 277,5 mm a 1:50, dentro de la caja útil del A3.

5. **Escala verificada numéricamente:** dos puntos del modelo separados 1 m proyectados con `WorldToPageTransform` miden **20,0 mm** sobre el eje horizontal de la hoja → 1:50 confirmado.

6. **Documentación unificada** en un solo playbook: `proyectos/MVP_05-rhino-mcp/01-AIZ/01-playbook-cortes-rhino-8.md` (absorbe el protocolo AutoCAD→Rhino, el manual de corte/hatch/axonometría y el plan de la hoja). Se borraron `01-protocolo-cortes.md`, `02-playbook-corte-hatch-iso.md` y `03-plan-corte-3d-hoja-a3-1-50.md`, y se actualizaron los enlaces de `00-index.md`.

## Archivos modificados

| Archivo | Cambio |
|---|---|
| `proyectos/MVP_05-rhino-mcp/01-AIZ/01-playbook-cortes-rhino-8.md` | Nuevo: playbook único (≈31 KB) |
| `proyectos/MVP_05-rhino-mcp/01-AIZ/00-index.md` | Enlaces al playbook único + estado actualizado |
| `proyectos/MVP_05-rhino-mcp/01-AIZ/01-protocolo-cortes.md` | Eliminado (fusionado) |
| `proyectos/MVP_05-rhino-mcp/01-AIZ/02-playbook-corte-hatch-iso.md` | Eliminado (fusionado) |
| `proyectos/MVP_05-rhino-mcp/01-AIZ/03-plan-corte-3d-hoja-a3-1-50.md` | Eliminado (fusionado) |
| `log.md` | Entrada de la operación |
| `activos/mvp_05-rhino-mcp/01-AIZ/set-ej_corte.3dm` | Copia del modelo con la hoja verificada (816.585 bytes, gitignored) |

En Rhino (fuera de git): `set-ej_corte.3dm` con la página `AIZ-CORTE-A`; copia verificada en `G:\Mi unidad\E#E.EDU\mora\set-ej_corte_A3-1-50.3dm`.

## Cerebro digital — topics

- Corte arquitectónico en Rhino 8: `ClippingPlane` + `Section Style` por capa + `Layout`/`Detail`.
- Escala de detalle en Rhino 8: `DetailView.SetScale(papel, unidades, modelo, unidades)`; `PageToModelRatio` = 0,02Stored; verificación por proyección de 1 m.
- Axonometría 30/60 militar (`axo3060`) como cámara paralela de trabajo del estudio.
- Puentes MCP que viven dentro del proceso de la app: hay que relanzarlos en cada sesión.

## Cerebro digital — entidades

| Entidad | Rol |
|---|---|
| `set-ej_corte.3dm` | Modelo del set de AIZ (159 mallas, metro) |
| `A-A` (ClippingPlaneSurface) | Plano de corte vertical en X = 575 |
| `axo3060` | Viewport paralelo 30/60 en Shaded, cámara de trabajo |
| `AIZ-CORTE-A` | Página A3 con el detalle `CORTE-A` a 1:50 |
| `AIZ-ROTULOS` | Capa con las dos líneas del pie de hoja |
| `reer-rhino-mcp` | Cliente MCP que habla con el script dentro de Rhino |

## Cerebro digital — hechos

1. El modelo de AIZ es **malla**, no sólido ACIS: el corte funciona igual con mallas cerradas, pero `ExtractClippingSlices` y los rellenos de sección dependen de que la malla cierre.
2. El recorte que hace entrar el set en un A3 a 1:50 **no es un segundo plano**: lo hace el propio plano de corte, porque solo sobrevive el lado +X (4,17 m de profundidad).
3. En Rhino 8 no existe `doc.Layouts`: las páginas viven en `doc.Views` (`AddPageView`).
4. `CameraTarget` y `CameraLocation` de un viewport son de solo lectura; el orden que funciona es dirección → objetivo → `CameraUp`.
5. Para escribir texto en espacio papel hay que activar el espacio con `SetPageAsActive()` antes de crear el objeto; `ActiveView` no alcanza.
6. `doc.Save()` devuelve `False` cuando el documento quedó `IsLocked` (tras un `Open` interrumpido): la salida es `SaveAs` a otra ruta y copiar el archivo.

## Pendientes

- Section style en `3D-EP-MAD`, `3D-REV-01`, `3D-SOL-EXT01`, `3D-BASE`.
- Activar `Custom Depth = 1,00 m` en el plano `A-A`.
- Resolver la malla abierta `Object_3`.
- Imprimir el PDF vectorial desde `Print` (desmarcando "Clipping planes").
- Reemplazar `G:\Mi unidad\E#E.EDU\mora\set-ej_corte.3dm` por la versión verificada cuando Rhino libere el archivo.
- Corregir `pbook-rhino-mcp.md`: indica `MCPConnect`, que no existe en esta instalación.
