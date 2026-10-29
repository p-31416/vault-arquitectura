# Notas — `configurar-corte-hatch-rhino.py`

Script que **configura el relleno de los cortes con trama** y arma una **lámina nueva**
con el corte de madera, **sin tocar el viewport que ya existe**.

## Cómo se ejecuta

En la **línea de comandos de Rhino 8**:

```
_RunPythonScript "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\configurar-corte-hatch-rhino.py"
```

O a través del puente MCP (que es como lo ejecuta el asistente). **El script no guarda
el documento**: eso queda a mano del usuario.

## Las 7 fases del script

| # | Fase | Qué hace |
|---|---|---|
| 1 | **Escalado de tramas** | `doc.ModelSpaceHatchScalingEnabled = True` y `doc.ModelSpaceHatchScale = 3.0` |
| 2 | **Section Styles** | por cada una de las 13 capas de material: `SectionStyle` con patrón, rotación, escala y colores → `capa.SetCustomSectionStyle(ss)` |
| 3 | **Lámina + detalle** | `doc.Views.AddPageView("UY-CORTE-HATCH", 420, 297)` → `pagina.AddDetailView(...)` |
| 4 | **Cámara** | copia la del detalle que ya existe (`dirección` → `objetivo` → `CameraUp`) |
| 5 | **Escala** | la secuencia de Rhino 8 (abajo) |
| 6 | **Corte** | `plano.Attributes.AddClipViewport(detalle.Id)` → habilita el clipping plane en el detalle nuevo |
| 7 | **Redibujado** | `doc.Views.Redraw()` |

## Los tres hallazgos que hacen que esto funcione

### 1 · La escala de trama tiene dos knobs (y el que se tocan no es el correcto)

| Ajuste | Dónde | Qué controla |
|---|---|---|
| `Pattern Scale` (por Section Style) | diálogo *Section Style* | la escala **propia del patrón** de ese material |
| **`Enable hatch scaling`** + **`Model space hatch scale`** | *File > Properties > **Hatch*** (o el comando `HatchScale`) | el escalado **global** de las tramas |

El manual de Rhino 8 lo dice así:

> **Enable hatch scaling → Enabled**: "Hatch patterns in model viewports are scaled by the
> Model space hatch scale value" · **"Hatch patterns in detail views print with the same
> scale regardless of the zoom factor"**.
> **Disabled**: "Hatch patterns will not scale."

**Por eso el corte se veía en la vista de trabajo y no en la lámina:** con el escalado
desactivado, la trama se dibuja en el espacio del modelo → a 1:30 mide 0,03 mm en el papel.
Con el escalado **activado**, el patrón en el detalle **no depende del zoom**.

La receta que recomienda McNeel (wim, en el foro): *primero* dejar la escala que se ve bien
**en papel**, *después* la que se ve bien **en modelo**.

### 2 · `SetScale` está "roto" en Rhino 8 → hay que hacer 5 pasos, no 1

Un usuario de McNeel (Ludovic, junio 2024) reportó que `SetScale` ya no fija la escala en V8;
Dale Fugier publicó el script que sí funciona. La secuencia es:

```python
pagina.SetActiveDetail(detalle.Id)      # 1) el detalle tiene que estar activo
detalle.Viewport.ZoomExtents()          # 2) encuadrar
detalle.DetailGeometry.IsProjectionLocked = True   # 3) bloquear la proyección
detalle.DetailGeometry.SetScale(1, doc.ModelUnitSystem, 33.3333, doc.PageUnitSystem)  # 4) escala
detalle.CommitChanges()                 # 5) CONFIRMAR  <-- sin esto no aplica
```

Firmas: `SetScale(distanciaEnModelo, unidadesModelo, distanciaEnLamina, unidadesLamina)`.
Con el modelo en metros y la página en mm, **1 m del modelo = 33,3333 mm en la lámina = 1:30**.

### 3 · La API de Section Styles en Rhino 8

Vía de la API (confirmada con un probe el 26/10 sobre Rhino 8.5):

| Qué | Cómo |
|---|---|
| **Poner el estilo a una capa** | `capa.SetCustomSectionStyle(Rhino.DocObjects.SectionStyle())` → `Void` |
| Leer el estilo de una capa | `capa.GetCustomSectionStyle()` / `capa.RemoveCustomSectionStyle()` |
| Miembros escribibles del `SectionStyle` | `HatchIndex` (índice del patrón, no el nombre) · `HatchScale` · `HatchRotationRadians` (**en radianes**) · `HatchPatternColor` · `HatchPatternPrintColor` · `BoundaryVisible` · `BoundaryColor` · `BoundaryPrintColor` · `BoundaryWidthScale` · `BackgroundFillColor` · `BackgroundFillMode` · `BackgroundFillPrintColor` · `SectionFillRule` · `Name` |
| Patrones disponibles | `doc.HatchPatterns` → `Solid`, `Hatch1`, `Hatch2`, `Hatch3`, `HatchDash`, `Grid`, `Grid60`, `Plus`, `Squares` |
| En el **plano de corte** | `plano.Attributes.SetCustomSectionStyle(...)` · `plano.Attributes.SectionAttributesSource` (`By Layer` / `By Clipping Plane` / `Custom`) |
| Habilitar el corte en una vista | `plano.Attributes.AddClipViewport(id_del_viewport)` y `RemoveClipViewport(id)` — es el "Views Clipped" del panel de propiedades |
| Escala de tramas del documento | `doc.ModelSpaceHatchScalingEnabled` · `doc.ModelSpaceHatchScale` (también el comando `HatchScale`) |
| Redibujar | `doc.Views.Redraw()` |

## Notas de código (para aprender)

- `seguro(fn, defecto)` ejecuta y devuelve el error como texto: la API de Rhino cambia entre
  versiones y una llamada que falle no debe abortar el script entero.
- `indice_patron(doc, nombre)` traduce el nombre del patrón a su índice, porque
  `SectionStyle.HatchIndex` guarda un índice, no un nombre.
- La rotación va en **radianes**: `math.radians(45)`.
- La cámara se copia en tres pasos (dirección → objetivo → `CameraUp`) y en ese orden.
- El script **no** llama `doc.Save()`: los cambios quedan en el documento abierto y el
  usuario los guarda (o los deshace con `Ctrl`+`Z`).

## Verificación

- Sintaxis verificada con `ast.parse` (Python 3).
- **Todavía no ejecutado**: falta levantar el puente MCP o correrlo a mano en Rhino.
- Después de correrlo, hay que **calibrar** `MODEL_SPACE_HATCH_SCALE` mirando el resultado:
  se mide la separación real de la trama con `Distance` sobre la lámina y se ajusta el valor
  (el objetivo: ~3 mm entre líneas de trama en el papel).
