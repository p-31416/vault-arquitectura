# Notas — `cortes-plaza-rhino.py`

Dos cortes por la plaza (uno en cada sentido), cada uno con su lámina A1 y su viewport de detalle a 1:2000, sobre el massing Sagrada (`mcp-plaza.3dm`).

## Cómo se usa

En la terminal (puente Rhino levantado):

```
C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts\rhino-mcp-cli.py exec scripts\cortes-plaza-rhino.py
```

El script NO guarda. Re-ejecutable: borra y rehace planos y detalles homónimos.

## Qué crea

| Corte | Plano | Vista del detalle | Lámina | Detalle | Escala |
|---|---|---|---|---|---|
| A-A longitudinal E-O | XZ en y=0, normal −Y, 1100×340 m | Back | `SF-CORTE-AA` A1 | `A-A` | 1:2000 |
| B-B transversal N-S | YZ en x=0, normal +X, 1100×340 m | Right | `SF-CORTE-BB` A1 | `B-B` | 1:2000 |

Cada plano recorta **solo su detalle** (`AddClipViewport` del detalle + `RemoveClipViewport` de la vista del modelo). Detalles en Shaded (script `detalles-shaded.py`), proyección bloqueada, detalle bloqueado. Capturas: `activos/.../earth2rhino3d/salidas/sf-corte-aa-lamina.png` + `sf-corte-bb-lamina.png`.

## Para imprimir sin los widgets rojos

En el diálogo `Print` → *Visibility* → desmarcar **Clipping planes** (y *Background color*). Los widgets se ven en pantalla pero no salen en el PDF. El marco del detalle: *No Print* si no debe imprimirse.

## Limitaciones conocidas (puente MCP + Rhino 8)

1. `AddClippingPlane` con lista vacía devuelve `Guid.Empty`: hay que pasar al menos un viewport (se usa la vista activa) y después mover el plano solo al detalle.
2. `AddClipViewport` / `RemoveClipViewport` viven en el **objeto** `ClippingPlaneObject` con firma `(viewport, bool)` — NO en `Attributes` (el playbook AIZ decía Attributes: vale para otra versión).
3. `RhinoPageView` no tiene `.Name` ni `.Details`: usar `.PageName` y `.GetDetailViews()`; el nombre del detalle vive en `Viewport.Name`, no en `Attributes.Name`.
4. `ObjectTable` no tiene `.Remove`: usar `.Delete(guid, True)`.
5. El puente ejecuta sin `def` ni variables de módulo visibles en funciones: script 100 % plano, solo `print` (la salida la captura el puente).
6. `SetScale` exige la secuencia V8: `SetActiveDetail` → `ZoomExtents` → `IsProjectionLocked=True` → `SetScale` → `CommitChanges`.
7. Profundidad de corte infinita (todo lo que está detrás del plano se ve). Si se quiere recorte de fondo: `Custom Depth` a mano por detalle.
8. Sin rótulos ni cajetín todavía: agregar texto/cotas en espacio de papel a mano.

Scripts chicos de apoyo: `activa-aa.py` · `activa-bb.py` (activan la lámina para captura) · `detalles-shaded.py` (pone ambos detalles en Shaded).
