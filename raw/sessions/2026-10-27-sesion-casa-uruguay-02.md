---
tipo: sesion
fecha: 2026-10-27
mvp: 05
participantes: [agente, Sol]
temas: [rhino8, casa_uruguay, dwg, import, clippingplane, plano_delimitador, secciones_de_corte, bitacora, correccion_aiz]
---

# Sesión — Casa Uruguay: import del DWG en archivo nuevo + documentación del plano delimitador

## Qué se hizo

1. **Replanteo del encargo.** El usuario trabaja sobre `G:\Mi unidad\E#E.EDU\mora\3D-casa_uruguay_02.3dm` (archivo nuevo de 0,8 MB, 27/10 07:14) e importa con `File > Import` el AutoCAD `CAD-UY-xa-RHINO_02.dwg` (5,3 MB, 27/10 01:51), que trae **entidades 3D de base y el corte 2D de inicio**. El DWG está dibujado en **metros** → entra 1:1 en un documento en metros, sin conversión. Los viewports ya establecidos de la hoja **AIZ** se reutilizan.

2. **Corrección de un error propio (no del usuario).** La guía de comandos afirmaba que *"en AIZ el corte falló porque el modelo era malla"*. El usuario lo desmintió: **el corte de AIZ salió bien**. Lo que quedó pendiente fue el **relleno por material** (solo 3 de 7 capas con Section Style) y una geometría abierta. El texto se reescribió en la guía (§0) y en la ficha del proyecto, con la regla que queda para Casa Uruguay: cada material con su Section Style desde el arranque. La afirmación sobre mallas frente a sólidos se retiró del texto: lo que se conserva es el resultado (el corte salió) y la causa pendiente (el relleno por capa).

3. **Investigación en la ayuda oficial de Rhino 8 en español** (`docs.mcneel.com/rhino/8/help/es-es/`), 13 páginas verificadas 200:
   - `PlanoDelimitador` (`ClippingPlane`) — barras **Visualización**, Disposición de las vistas y Visibilidad; menú *Ver > (título del viewport) > Plano delimitador*. Es el recorte a la vista.
   - `PlanoDeCorte` (`CutPlane`) — barras **Plano**, Creación de superficies y Superficies (lateral); menú *Superficie > Plano > Plano de corte*. Crea una **superficie** que atraviesa los objetos (cortador real para booleanas).
   - `SeccionesDeCorte` (`ClippingSections`), nuevo en V8 — barras **Secciones**, Creación de secciones de corte, Dibujo y Novedades V8; menú *Dibujo > Secciones > Crear*.
   - La barra **Secciones** (12 comandos) no viene abierta en Rhino 8: se abre con clic derecho sobre cualquier barra.
   - Opciones verificadas de `SeccionesDeCorte`: `Dir` (`PlanoC`/`X`/`Y`/`Personalizado`), `ProfundidadPersonalizada`, `Profundidad`, `Clip`, `Nombre`, `ModoEtiqueta`, `GuardarEnVistaGuardada`, `Invertir`.
   - Propiedades del plano delimitador: `Nombre`, `Etiqueta`, `Profundidad personalizada` + `Profundidad`, `Estilo de sección` (Por capa / Personalizado), `Invertir dirección`, `Objetos recortados` (Todos / Incluir selección / Excluir selección), `Vistas delimitadas`, `Restablecer vistas`, `Igualar`.
   - Comandos de la familia: `VerSeccionesDeCorte`, `ExtraerSeccionesDeCorte` (Curva / Trama / Agrupar), `ExtraerSegmentosDeCorte` (Grosor / Posición), `DibujosDeCorte` (MostrarTrama / AñadirFondo / AñadirOcultas / AñadirSilueta / Ángulo / Proyección), `DibujoDeCorteAnidado`, `ExportarDibujosDeCorte`, `ExportarInfoDeSecciónDeCorte`, `GuardarVistasDeSecciónDeCorte`, `GuardarPlanosCDeSecciónDeCorte`, `ActualizarDibujosDeCorte`, `BorrarSegmentosDeCorte`, `ActivarPlanoDelimitador`, `DesactivarPlanoDelimitador`.
   - Opciones oficiales de importación DWG: `Import unreferenced layers/blocks/linetypes`, `Convert wide polylines to surfaces`, `Ignore thickness`, `Convert regions to curves`, `Mesh precision`, `Model units` / `Layout units`, `Set layer material to layer color`.

4. **Diagnóstico del corte invisible en la isométrica** (pregunta del usuario): un plano delimitador recorta **solo las vistas donde está habilitado** — al crearlo en Planta, la isométrica queda sin recortar. Se prende en *Propiedades > "Vistas delimitadas"* (tildando la isométrica) o con `ActivarPlanoDelimitador` teniendo la isométrica activa. Causas secundarias documentadas: el rectángulo del widget define la zona de influencia (si queda más chico que el modelo, partes del modelo no se recortan; **el widget se pone rojo** cuando el plano no intersecta la caja de los objetos), lado visible invertido (`Invertir dirección`) y `Profundidad` ≠ 0 (se ve masa, no sección fina).

5. **Documentación escrita** — un solo archivo, `proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/01-comandos-rhino-8.md`:
   - **§9 Corte 3D — el plano delimitador** (nuevo): los tres comandos que se confunden, las 5 variantes de inserción con cuál usar en cada caso, la tabla de "por qué no se ve el corte" con su solución, los 6 interruptores de prender/apagar, la configuración completa con sus 12 propiedades, el camino corto de la sección al dibujo (9 comandos) y la receta del corte `A-A` de este proyecto.
   - **§12 Bitácora de modelado — `3D-casa_uruguay_02.3dm`** (nuevo): registro vivo con estado por paso, la tabla de opciones de importación del DWG con el porqué de cada una, los comandos de verificación del contenido, el checklist del plano de corte y el estado de las capas.
   - Cheatsheet ampliado con los 9 comandos de corte; §11 Errores frecuentes con 4 filas nuevas del plano delimitador; §13 Referencias con las 13 URLs nuevas; frontmatter actualizado a `2026-10-27`.

6. **Modo de trabajo acordado:** el agente documenta y guía; el modelado lo ejecuta el usuario. Sin ejecuciones de Rhino y sin llamadas al MCP, para no enlentecer el trabajo.

## Continuación (tarde) — Section Styles por capa y convención de nombres

7. **Convención de nombres fijada por el usuario:** los comandos se nombran **en inglés primero** (es lo que se tipea) y, entre paréntesis, la traducción de Rhino en español. Se aplicó al §9 y §10 completos y quedó anotada en el encabezado de la guía.

8. **Nuevo §10 — Section Styles** (fuentes oficiales: `popup_moreinformation/sectionstyle.htm`, `commands/layer.htm`, `properties/object.htm` y el User's Guide *Clip & Section | Intro to Section Styles*):
   - Los tres niveles y su orden de resolución: clipping plane (`By Layer` / `Custom`) → layer (`None` / `Custom`) → object (`By Layer` / `By Parent` / `By Clipping Plane` / `Custom`).
   - Diálogo campo por campo: **Hatch** (Pattern, Pattern Color, Pattern Rotation, Pattern Scale, Background, Section open objects) y **Boundary** (Show, Linetype, Width Scale, Color).
   - Paso a paso por capa y por objeto, con el atajo multi-capa (`Ctrl`+click en el panel de capas).
   - Por qué cada capa debe estar diferenciada: capa en `None` → corte sin relleno; mismo estilo en todas → corte uniforme. Es la lección de AIZ (3 de 7 capas con Section Style).
   - Tabla de los 13 materiales con patrón, color, rotación, escala y ancho de borde; las capas `REF-*` en `None`.
   - Los Section Styles **no viajan con el import de un DWG**: la vía para llevarlos al archivo nuevo es `LayerStateManager` (Save → Import → Restore), que restaura también el Section Style.

9. **§9 ampliado**: se agregó §9.3 "how to work with clipping planes, day to day" (mover, redimensionar, profundidad, invertir, recorte por objeto/capa/vista, nombre y etiqueta, Named View / Named CPlane, borrar) y se reescribieron todas las tablas con nombres en inglés primero.

10. **Avance registrado del usuario:** el `ClippingPlane` ya está creado en `3D-casa_uruguay_02.3dm` y los Section Styles ya configurados → §13.5 y §13.6 actualizados con el estado real.

11. **Verificación de enlaces:** las 32 URLs del documento comprobadas por HTTP HEAD → todas 200.

12. **Navegación documentada** (a pedido del usuario): en la isométrica (perspectiva) el **botón derecho orbita**, `Shift` + botón derecho hace **pan**, `Ctrl` + botón derecho hace **zoom** y la rueda hace zoom escalonado; en las vistas paralelas el botón derecho hace pan. Verificado contra el *User's Guide — Navigation & Display* de McNeel y la página *Mouse options* (ambas 200). Quedó en la subsección "Navegación con el mouse" del cheatsheet (§11) y como nota en la bitácora §13.5.

13. **Idioma del documento:** la prosa de §9 y §10 se tradujo al español (el vault es en español) conservando en inglés los **comandos, opciones y rutas de menú** — que es como los ve el usuario en su Rhino — con la traducción del comando entre paréntesis. La convención quedó escrita en el encabezado del documento.

14. **Nuevo §11 — La hoja: layout, viewport de detalle, escala y texto en papel** (fuentes oficiales: `layout.htm`, `detail.htm`, `copyviewporttodetail.htm`, `text.htm`, `documentproperties/annotation.htm`, `print.htm`):
    - La lámina: `Layout` (nombre, cantidad inicial de detalles, impresora, tamaño, orientación, ancho/alto en mm) y `LayoutProperties` para corregirla después, con el orden de trabajo que fija el manual.
    - Las **3 formas de crear el viewport de detalle**: `Detail` a mano (`Add` → `Projection` → `Scale` → `Lock`), `CopyViewportToDetail` (trae la cámara de un viewport de modelo) e `ImportLayout` (trae la lámina entera de otro `.3dm`).
    - **Tabla de variantes de configuración** con la elegida (la de AIZ, verificada) y las variantes según el uso de la lámina.
    - **Escala:** el número de cada prompt va en las unidades de ese espacio → con lámina en mm y modelo en m, **1:50 = 20 y 1**; tabla 1:20 / 1:50 / 1:100 y verificación con `Distance` (1,00 m del modelo = 20,0 mm en el papel).
    - **Texto en papel:** `Text` (texto → propiedades → ubicación), altura en unidades de layout, `Mask`, `Text Field`, alineación, y la diferencia entre texto de papel y texto dentro del detalle.
    - **Estilos de anotación** y el gotcha: `Open` desactiva **Enable layout space scaling** al abrir un DWG → hay que activarlo en este archivo.
    - **Print:** Rhino PDF · `Use layout page size` · Vector output · Print color · Match pattern definition · Page lengths · desmarcar Clipping planes.

15. **Numeración corrida** al insertar el capítulo: la guía quedó 0–15 y se ajustaron las referencias cruzadas (bitácora §14, referencias §15, cheatsheet §12).

16. **Corrección técnica:** una edición dejó 8 caracteres corruptos (armenio) en la tabla de variantes → se reemplazaron por PowerShell a nivel de bytes; verificado que los cuatro archivos editados no tienen caracteres fuera del latino.

17. **Nuevo bloque §9.8–§9.12 — vistas, estilos visuales y diagnóstico del corte a medias** (fuentes oficiales: `setview.htm`, `isometric.htm`, `toolbarmap/set_view_toolbar.htm`, `namedview.htm`, `options/view_displaymode_options.htm`, `options/view_display_mode_clippingplanes.htm`, `selclippingplaneinviewport.htm`):
    - Vistas por defecto: `SetView` (World y PlanoC) e `Isometric` (`NE`/`NW`/**`SE`**/`SW` + `ZoomExtents`, siempre en paralelo). La del proyecto: **`Isometric SE`** + `SetView World Top/Bottom/Left`.
    - La axonométrica 30/60 de AIZ (`axo3060`) es una **vista guardada**, no una vista estándar → se importa con `NamedView` → *Import from 3dm file*.
    - Los 11 estilos visuales con su uso en el proyecto y cómo se configuran; dentro de cada modo, el bloque **Objects > Clipping Planes** (`Use section styles`, `Show fills`, `Show edges`, `Edge thickness`).
    - Cómo se regenera una vista (6 métodos).
    - **Diagnóstico del layout de corte A** (8 causas con comprobación y solución) — el pedido central del usuario.
    - Bitácora §14.8 con el procedimiento de comprobación en 6 pasos.

18. **Tabla de escalas del viewport** (§11.4 ampliada): 1:500 / 1:200 / 1:100 / **1:50** / 1:25 / 1:20 / 1:10, con los valores que se tipean en `Scale Value` (on layout / in model), la equivalencia "1 mm en la hoja = X/1000 m en el modelo" y la tabla de cuánto modelo entra en el detalle de 400 × 270 mm.

19. **Corte fantasma (un solo plano, se ven dos) — causa documentada:** *Tools > Options > View* → **"Named views set clipping planes"**: al restaurar una vista guardada se restaura también el **estado de enable de los planos de corte** que tenía. Si esa vista se guardó con el plano viejo activo, el corte vuelve con ella y **borrar el plano no lo saca de la vista guardada**. Test decisivo: `SelClippingPlaneInViewport` → si selecciona uno solo, el segundo corte es estado guardado o redibujado viejo. Solución: desmarcar la opción, re-crear la vista guardada (`NamedView` → *Save as*, nombre nuevo) y forzar el redibujado.

20. **Nuevo §11.12 — Receta completa del viewport de detalle** (7 pasos: preparar el documento → lámina → detalle → corte dentro del detalle → verificación de escala con `Distance` → marco → texto → impresión), con la trampa de que `Projection` no incluye la axonométrica 30/60 (esa viene por `CopyViewportToDetail` o por `NamedView` → *Import from 3dm file*).

21. **Nuevo §11.13 — El texto de la hoja** en tres familias: datos de la lámina (`Text` en papel, alturas 5/3,5/3/2,5 mm), leyenda de materiales (`Text` + `Hatch` de muestra) y referencias numeradas (`Dot` en espacio de pantalla, `Leader` para llamadas). Regla de tamaño documentada: con *Enable layout space scaling* el texto del detalle imprime a su tamaño nominal; sin eso, 3 mm de papel a 1:50 = 150 mm de modelo. Text Fields para rótulos dinámicos.

22. **Prueba del usuario sobre el corte A:** `SelClippingPlaneInViewport` → **"No objects added to selection"** → ningún plano recorta esa vista. Se documentó **§9.13** con las 3 pruebas que separan las causas: (1) en qué vista se corrió (el detalle puede no estar habilitado → *Views Clipped* → *Layout Space*), (2) `Zoom` → `Extents` para distinguir redibujado viejo de geometría real, (3) si es geometría, localizar el corte 2D del DWG importado como superficies con `What` + capa, y la opción de importación **`Convert wide polylines to surfaces`** como causa.

23. **Resolución del corte A (usuario):** el viewport estaba mal armado → se **re-armó** con `Detail` → `Add` (detalle nuevo) + `Scale` + `Projection` + `Lock`, y se volvió a tildar el detalle en *Views Clipped* → *Layout Space*. Quedó funcionando.

24. **Escala del corte A = 1:30:** 1 unidad de layout en mm = **0,03 m** del modelo (`1` y `0.03`, con punto decimal). Se amplió la tabla de escalas (§11.4) con 1:30 y 1:40, y con la tabla de cobertura del detalle: a 1:30 el detalle de 400 × 270 mm muestra **12 × 8,1 m** → no alcanza para la casa completa (≈14 m); las escalas que sí alcanzan son 1:40 (16 × 10,8 m) y 1:50 (20 × 13,5 m).

25. **Nuevo §9.14 — el corte sin hatch en el detalle** (síntoma abierto): checklist de 7 puntos. El relleno de la sección lo dibuja el modo de visualización y el detalle tiene el suyo → mismo modo (Shaded) · *Show fills* ON · *Use section styles* ON · plano y objetos en `By Layer` · capa con *Detail On* · sección cerrada (sólidos) · si el relleno sale plano, es *Use section styles* apagado.

26. **Intento de leer el `.3dm` sin Rhino:** el formato va **comprimido** (solo se lee el encabezado "3D Geometry File Format 80 / Rhinoceros 8.5") → el escaneo de cadenas no sirve. `rhino3dm` **no está instalado** en los tres Python del equipo y tampoco alcanzaría (no expone Estilos de sección ni modos de visualización). El **puente MCP está caído** (puerto 9876 sin listener, log termina el 26/10). → hace falta un comando del usuario en Rhino: `_RunPythonScript "…\scripts\rhino-mcp-server-rhino.py"`.

27. **Nuevo script de solo lectura** `scripts/inspeccionar-seccion-rhino.py` (+ notas): vuelca planos de corte con sus propiedades, capas con Estilo de sección, objetos por tipo y cerrados, láminas/detalles con modo y escala, y dónde están *Show fills* / *Use section styles*.

28. **Nuevo §9.15 — el patrón de la trama no se lee en la lámina:** la trama se dibuja en el espacio del modelo → con `Pattern Scale` 1,0 (1 mm) a 1:30 mide **0,03 mm en el papel**. Fórmula `Pattern Scale = (papel × escala) / base` → **90** para 3 mm a 1:30. La hoja AIZ tiene el mismo problema (1,0 a 1:50).

29. **Regeneración de la vista:** Rhino 8 **no tiene comando `Redraw`**; las vías son `SetDisplayMode`, `Zoom` → `Extents`, apagar/prender el plano, restaurar una vista guardada, y `SetRedrawOff`/`SetRedrawOn` para scripting. El control decisive es **File > Print > Preview**: si la trama sale en la vista previa y no en pantalla, el archivo está bien y falla la caché de pantalla.

30. **La lámina en blanco y negro con los hatches** (§11.7, subsección nueva): las cuatro palancas (ver en pantalla con `PrintDisplay` / Print Preview · imprimir B&W con *Black and white* · fondo blanco con *Background color* desmarcado · hatches con *Use section styles* + *Show fills* en el modo del detalle) y el matiz de que en la lámina mandan **Layout / Detail Print Color** y **Layout / Detail Print Width**. Consecuencia: en B&W los materiales se distinguen **por patrón**, no por color → un patrón por material + `Pattern Scale` a la escala del papel (90 para 3 mm a 1:30).

31. **CAUSA RAÍZ del corte sin hatch:** no era el `Pattern Scale` sino **"Enable hatch scaling"** (*File > Properties > Hatch*). El manual: **Enabled** → "Hatch patterns in detail views print with the same scale regardless of the zoom factor"; **Disabled** → no escalan. Con el escalado apagado, la trama vive en el espacio del modelo → 0,03 mm en el papel a 1:30 → invisible en la lámina, visible en la vista de trabajo. **§9.15 reescrito**.

32. **`SetScale` roto en Rhino 8** (McNeel, junio 2024, con el script de Dale Fugier como referencia): la secuencia que funciona es `SetActiveDetail` → `ZoomExtents` → `IsProjectionLocked` → `SetScale` → **`CommitChanges()`**. Documentado en §11.12.

33. **API de Section Styles de Rhino 8** verificada por probe propio (26/10): `SectionStyle` con 14 miembros escribibles, `Layer.SetCustomSectionStyle(SectionStyle)`, `Layer.GetCustomSectionStyle()`, `plano.Attributes.AddClipViewport(id)`, `doc.ModelSpaceHatchScalingEnabled`, `doc.ModelSpaceHatchScale`, `doc.Views.Redraw()` → nuevo §10.9.

34. **Nuevo script `scripts/configurar-corte-hatch-rhino.py`** (+ notas): 7 fases para la lámina `UY-CORTE-HATCH` con el detalle `A-A-HATCH` a 1:30, la cámara copiada del detalle existente, el clipping plane habilitado en el detalle nuevo y el redibujado. **No guarda el documento.**

35. **Bloqueo:** el puente MCP está caído (log del 26/10) y el MCP responde `WinError 10061`. Rhino corre con `3D-casa_uruguay_clase.3dm` (12 MB, `[iso]`). Falta el comando `_RunPythonScript "…\scripts\rhino-mcp-server-rhino.py"` del usuario → después se ejecutan las fases 1-3 y se calibra el `ModelSpaceHatchScale` midiendo la trama con `Distance`.

## Archivos modificados

| Archivo | Cambio |
|---|---|
| `proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/01-comandos-rhino-8.md` | §0 corregido · **§9 reescrito en inglés primero** (corte 3D: 3 comandos, 6 variantes de inserción, trabajo diario con el plano, 6 causas de "no se ve el corte", 8 interruptores, 9 comandos de sección a dibujo, receta `A-A`) · **§10 nuevo** (Section Styles: 3 niveles, diálogo campo por campo, paso a paso por capa y por objeto, por qué cada capa debe diferenciarse, tabla de los 13 materiales, traspaso entre archivos con `LayerStateManager`) · §11 cheatsheet ampliado · §12 errores frecuentes +4 · **§13 bitácora** con el estado real · §14 referencias +9 URLs |
| `proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/00-index.md` | Corrección de la cita de AIZ · fuentes del DWG y del archivo nuevo · §2.2 estado del `3D-casa_uruguay_02.3dm` · pendientes actualizados a 10 tareas |
| `log.md` | Entrada del 2026-10-27 (nueva, sin tocar las anteriores) |
| `raw/sessions/2026-10-27-sesion-casa-uruguay-02.md` | Este registro |

Fuera de git (binarios): `G:\Mi unidad\E#E.EDU\mora\3D-casa_uruguay_02.3dm` (0,8 MB) y `G:\Mi unidad\E#E.EDU\mora\CAD-UY-xa-RHINO_02.dwg` (5,3 MB), ambos propiedad del usuario.

## Cerebro digital — topics

- Rhino 8: familia de cortes en la barra **Secciones** (nueva en V8) — `PlanoDelimitador` (recorte visual) vs `PlanoDeCorte` (superficie cortadora) vs `SeccionesDeCorte` (sección que atraviesa los objetos con nombre y vista guardada); el recorte se habilita **por vista**; el rectángulo del widget define la zona de influencia y el widget rojo avisa que el plano no toca la geometría; `Profundidad = 0` dibuja la sección fina; `Estilo de sección` por capa o propio del plano.
- Importación DWG: `Convert regions to curves` (las regiones no importan), `Ignore thickness`, `Convert wide polylines to surfaces`, `Model units` vs `Layout units`, capas apagadas que entran apagadas, paperspace que entra como layout, 3DFace/polyface que entra como malla, DWG 2018 como formato máximo de lectura.
- Casa frente al mar (Diego Arraigada, Manantiales, Uruguay, 2011, 140 m²): el usuario ya dispone del modelo 3D avanzado en AutoCAD (5,3 MB) y del corte 2D de inicio; en Rhino trabaja sobre un archivo nuevo, con el PDF de la publicación como referencia de cotas.

## Cerebro digital — entidades

| Entidad | Rol | Estado |
|---|---|---|
| `3D-casa_uruguay_02.3dm` | Archivo de trabajo del 27/10 | import ✅ · escala ✅ · corte ⏳ |
| `CAD-UY-xa-RHINO_02.dwg` | AutoCAD origen (3D base + corte 2D), en metros | importado ✅ |
| `3D-casa_uruguay.3dm` | Archivo del 26/10 con el PDF calibrado (35 MB) | intacto, sirve de referencia |
| `set-ej_corte_A3-1-50.3dm` | Hoja AIZ a 1:50 → fuente de los viewports a reutilizar | verificado |
| `01-comandos-rhino-8.md` | Guía única del proyecto (§9 corte, §12 bitácora) | en crecimiento |

## Cerebro digital — hechos

1. El corte de AIZ **funcionó**; la lección no es "mallas vs sólidos" sino **el relleno por material**: cada capa necesita su Section Style.
2. Un plano delimitador en Rhino 8 recorta **solo las vistas habilitadas** → de ahí que el corte no apareciera en la isométrica.
3. `Vertical` desde la vista Planta es la variante más simple para un corte de obra, y coincide con lo hecho en AIZ (`A-A`, plano vertical en X = 575).
4. Las regiones de un DWG no importan salvo que se active `Convert regions to curves` → verificar cómo está guardado el corte 2D.
5. El DWG en metros entra 1:1 en el documento en metros: no hay conversión de escala que revisar.
6. El Estilo de sección **no viaja con el import** de un DWG: las 13 capas de material hay que recrearlas con el suyo en el archivo nuevo.

## Pendientes

- [ ] Verificar qué entró: `What`, `SelClosedPolysrf`, `SelMesh`, `SelCurve`, `Layer`, `BoundingBox`.
- [ ] Terminar el plano de corte: `Vertical` desde Plan, `Name = A-A`, `Depth = 0`, `Section Style = By Layer`, tildar la isométrica en *Views Clipped* (el `ClippingPlane` ya existe y los Section Styles ya están configurados).
- [ ] Armar la hoja: `Layout` A3 landscape 420 × 297 mm → `Detail` → `Add` → `Projection` → `Scale` (`20` / `1`) → `Lock` → verificar la escala (1,00 m del modelo = 20,0 mm en el papel) → habilitar el clipping plane dentro del detalle → activar **Enable layout space scaling** → textos de papel.
- [ ] Confirmar en el archivo nuevo que las 13 capas de material existen con su Section Style (no viajan con el import del DWG → §10.7).
- [ ] Traer la vista de la hoja AIZ si hace falta (`ImportLayout` o `ImportAnnotationStyles` desde `set-ej_corte_A3-1-50.3dm`).
- [ ] `Print` → Rhino PDF vectorial y verificar el PDF.
- [ ] Continuar la bitácora §14 a medida que avanza el modelado.
