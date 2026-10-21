# axonometria-militar-rhino.py — Notas didacticas

Script **RhinoPython** (Rhino 8) que arma la axonometría militar 30/60 con un
ejemplo: cubo de 4×4×4 m con perforación circular + entramado tipo *platform
frame*, más dos planos de corte.

Cada bloque explica qué hace y por qué. Los comentarios `# NOTA ES:` del script
mismo son el resumen línea por línea.

---

## Cómo correrlo

**Opción A — dentro de Rhino (la que va a usar el estudio)**

1. Rhino 8 abierto.
2. `Tools > Script > Run...` (o `Menú > Archivo > Abrir script`).
3. Elegir `scripts/axonometria-militar-rhino.py`.
4. En la consola de Python de Rhino aparece el log con la verificación.

**Opción B — por MCP (community `reer-rhino-mcp`)**

La tool `execute_code` corre Python dentro de Rhino: se le pasa el contenido
del archivo y listo. Ver `wiki/glosario/software/rhino.md`.

El script es **idempotente**: borra y recrea las capas `AXO_*`, se puede
reejecutar sin ensuciar el archivo.

---

## Lo que produce (dos salidas, y por qué dos)

### (A) Vista axonométrica 3D — cámara paralela

Azimut 45°, elevación **35.264°**, proyección paralela, `CameraUp = +Z`.

- Los tres ejes se dibujan a **30° / 30° / 90°**: los dos de planta a 30 de la
  horizontal (60 de la vertical) y el vertical derecho.
- **Por qué 35.264° y no 30°**: con azimut 45° y elevación `t`, los ejes de
  planta se dibujan a `atan(sin t)` de la horizontal. Para que ese ángulo sea
  exactamente 30° hace falta `sin t = tan 30°` → `t = 35.264°`. Con `t = 30°`
  salen a 26.57° (dimétrica). Está verificado en el log del script.
- Es la axonometría **3D navegable**: admite planos delimitadores, cortes,
  sombras, render, thickened curves.
- Ojo: acá la altura se ve acortada (`cos 35.264° = 0.8165`). No es la militar
  estricta.
- **Estado final del script**: la cámara queda en esta axonometría 3D, con el
  modelo y el dibujo militar plano conviviendo (el dibujo está en `y = -6`).
  Para mirar el dibujo de frente: *Vista > Vistas > Frontal*.

### (B) Dibujo militar exacto — proyección paralela oblicua

Plano de dibujo = plano frontal (`y = 0`). Los rayos de proyección viajan en
dirección oblicua y el modelo se aplana sobre ese plano
(`Transform.ProjectAlong`).

| eje | como se dibuja | magnitud |
|-----|----------------|----------|
| X (ancho) | horizontal, a 0° | **verdadera** |
| Z (altura) | vertical, a 90° | **verdadera** |
| Y (profundidad) | inclinado **30°** (60° de la vertical) | escala 1 (militar) o ½ (cabinet) |

**Por qué dos salidas y no una**: la militar estricta es, por definición, un
sistema 2D (no hay punto de fuga, y las verticales verdaderas obligan a que el
fondo se dibuje inclinado). En un viewport 3D de Rhino no se puede ver "en
perspectiva" una proyección oblicua: la cámara de Rhino es ortogonal a su
dirección de vista. Entonces el script hace las dos cosas y las deja
separadas: la 3D para trabajar, la 2D para entregar.

La fórmula (en `direccion_proyeccion()`):

```
plano de dibujo:  y = 0
rayo:             p + t·d      con t = −y / dy
impacto:          U = x − y·(dx/dy)      V = z − y·(dz/dy)

requisitos:
  eje X → (U,V) = (1, 0)
  eje Z → (U,V) = (0, 1)
  eje Y → (U,V) = (k·cos a, k·sin a)

de ahí:
  dx = −k·cos(a)·dy
  dz = −k·sin(a)·dy
```

Con `a = 30°`, `k = 1` → `d = (−0.6124, 0.7071, −0.3536)`.

Valores verificados con el script (control de calidad, `verificar_angulo()`):

```
ang=30 k=1.0 mirror=False -> U(Y)=0.8660 V(Y)=0.5000  ang_real=30.00  largo=1.000
ang=30 k=1.0 mirror=True  -> U(Y)=-0.8660 V(Y)=0.5000 ang_real=150.00 largo=1.000
ang=60 k=1.0 mirror=False -> U(Y)=0.5000 V(Y)=0.8660  ang_real=60.00  largo=1.000
ang=30 k=0.5 mirror=False -> U(Y)=0.4330 V(Y)=0.2500  ang_real=30.00  largo=0.500
```

### (C) Cortes

Dos planos delimitadores (clipping planes) + las curvas de sección reales:

- **CORTE A**: horizontal a `z = 2.00` → muestra la perforación en planta.
- **CORTE B**: vertical en `x = 2.00` → perfil del hueco.
- Las curvas de sección se extraen del sólido con
  `Intersection.BrepPlane` y se proyectan al dibujo militar: el corte queda
  como geometría dibujable, no sólo como recorte visual.

La **normal del plano apunta hacia la mitad que queda visible**. Si el recorte
sale al revés: *Propiedades del plano delimitador > Invertir dirección*.

Para que la sección se rellene (el "poché" del corte): click derecho sobre el
sólido > *Estilo de sección = Por plano delimitador*. Es una propiedad de
objeto, no de la vista, y en Rhino 8 no está expuesta igual en el API, por eso
el script la deja indicada en el log en vez de tocarlo.

---

## Bloque por bloque

### Imports

- `Rhino` / `scriptcontext as sc`: `sc.doc` es el documento activo; en Rhino 8
  todo el trabajo ocurre sobre el documento abierto.
- `System`: sólo para `System.Guid.Empty` (comparar el GUID del plano
  delimitador).
- De `Rhino.Geometry` se importan sólo las clases usadas: `Point3d`,
  `Vector3d`, `Plane`, `Box`, `Cylinder`, `Brep`, `Transform`, `Interval`,
  `TextDot`.

### `paso(nombre, funcion)`

Ejecuta un paso dentro de un `try/except`: si uno falla (por ejemplo, si el
modelo booleano no compila en una versión de Rhino), **el resto del script
sigue**. Devuelve `None` en caso de fallo.

### `limpiar_capas()`

Busca las capas `AXO_MODELO`, `AXO_CORTES`, `AXO_MILITAR_2D`, `AXO_EJES`; si
existen, borra sus objetos; si no, las crea. Por eso el script se puede
reejecutar.

### `atributos(nombre, capa_nombre, color=None)`

Arma un `ObjectAttributes` con nombre y capa. Los nombres de objeto son los que
después aparecen en el panel de propiedades de Rhino.

### `crear_cubo_perforado()`

1. `Box(Interval, Interval, Interval)` → la caja de 4 m; `.ToBrep()` la pasa a
   Brep.
2. `Cylinder(Plane, height, radius)`: el **eje del cilindro es la normal del
   plano base**. Con plano base en `(2, −1, 2)` y normal `(0,1,0)` el cilindro
   corre a lo largo de **Y** (la profundidad), que es justo la dirección que
   después se dibuja a 30°.
3. `Brep.CreateBooleanDifference([cubo], [perforador], tolerancia)` → el
   volumen con el hueco.

### `crear_platform_frame()`

Cuatro vigas rectangulares (0.35 × 0.50 m) formando un marco con abertura
central sobre el cubo. Es el puente con el sistema constructivo real: misma
lógica que una losa de entrepiso con vacío.

### `direccion_proyeccion()` / `verificar_angulo()`

El corazón del script (ver la fórmula arriba). `verificar_angulo()` recalcula
el ángulo **a partir de la dirección realmente usada** y lo imprime: si el
número no da 30.00°, la matriz está mal y hay que revisarla.

### `proyectar_curvas()`

Aplica la transformación a cada curva con `curva.Transform(xform, False)` y las
 mete al documento. Las curvas quedan planas en `y = 0` (o sea, `y = DISTANCIA`
 tras la traslación): son curvas de dibujo, no geometría 3D.

### `crear_ejes_referencia()`

Dibuja la triada X/Y/Z proyectada, con etiquetas (`TextDot`). Es la prueba de
lectura del dibujo: X horizontal, Z vertical, **Y a 30°**.

### `crear_plano_delimitador()`

`doc.Objects.AddClippingPlane(plano, u, v, viewportId, attrs)`. Los dos
parámetros `u`/`v` son el tamaño del widget en unidades de modelo; el plano en
sí es infinito.

### `vista_axonometrica_3d()` / `vista_frontal()`

Mueven la cámara del viewport activo:
`ChangeToParallelProjection(True)`, `SetCameraTarget`, `SetCameraLocation`,
`CameraUp = (0,0,1)`, `ZoomBoundingBox`.

En la 3D, la cámara se ubica en `centro + dirección · (radio · 3)`: la
dirección sale de azimut y elevación (`cos(el)·sin(az)`, `cos(el)·cos(az)`,
`sin(el)`).

---

## Parámetros (bloque `CONFIGURACION`)

| parámetro | valor | para qué |
|-----------|-------|----------|
| `ANGULO_RECESO_GRADOS` | `30.0` | ángulo del fondo en el dibujo (30 o 60) |
| `ESCALA_RECESO` | `1.0` | 1 = militar, 0.5 = cabinet |
| `MIRRAR_PROFUNDIDAD` | `False` | `True` = el fondo retrocede a la izquierda |
| `LADO_CUBO` | `4.0` | arista del cubo (m) |
| `RADIO_PERFORACION` | `0.6` | radio del hueco (m) |
| `MOSTRAR_PLATFORM_FRAME` | `True` | entramado de vigas arriba |
| `DISTANCIA_DIBUJO_2D` | `-6.0` | separa el dibujo 2D del modelo 3D |
| `AZIMUT_AXONOMETRICA` | `45.0` | azimut de la cámara 3D |
| `ELEVACION_AXONOMETRICA` | `35.264389682754654` | elevación que da exactamente 30° |

---

## Verificación (hecho en Rhino 8.5 vía MCP, 2026-10-19)

- Log: `Angulo real sobre la horizontal: 30.00 grados (pedido 30.00)` ✓
- Geometría del dibujo (leída del documento):
  - `ARISTA_001` = (0,0)→(4,0) → base del alzado, largo real 4.00 ✓
  - `ARISTA_005` = (0,4)→(4,4) → coronamiento, largo real 4.00 ✓
  - `ARISTA_009` / `ARISTA_010` → montantes, 4.00 de alto ✓
  - `ARISTA_003` = (3.46,2)→(7.46,2) → el fondo: 4.00 m de profundidad dibujados
    como **3.46 horizontal + 2.00 vertical** → `atan(2/3.46) = 30.00°` ✓
  - `EJE_Y` = (0,0)→(1.73,1.00) → el eje de fondo a 30° ✓
- Imágenes: `activos/mvp_05-rhino-mcp/axonometria-militar-3d.png` (axonometría
  3D con el corte) y `...-2d.png` (el dibujo militar de frente).

---

## Trampas de la API de Rhino 8 (resumen de lo que costó)

1. **El script tiene que vivir dentro de una función.** El motor de MCP de
   Rhino ejecuta `exec(codigo, globals, locals)`: las funciones de primer nivel
   quedan en `locals` y no se encuentran entre sí (`NameError: log`).
2. `Box` es `Box(plano, Ix, Iy, Iz)` — no existe `Box(Interval, Interval, Interval)`.
3. `Cylinder` es `Cylinder(circulo, altura)` — no `Cylinder(plano, h, r)`.
4. `Cylinder.ToBrep()` pide los flags de tapa: `ToBrep(True, True)`.
5. `ObjectAttributes` no tiene `SetLayer`: se asigna `attrs.LayerIndex`.
6. `Layers.Add(nombre)` no existe: hay que crear `Rhino.DocObjects.Layer()` y
   agregarlo.
7. `GeometryBase.Transform(xform)` **muta** la geometría (no hay flag
   `inPlace`): hay que duplicar la curva antes.
8. `Line.ToCurve()` no existe: es `ToNurbsCurve()`. Y `curve.Points` devuelve
   `ControlPoint` (la posición es `.Location`).
9. `Intersection.BrepPlane(brep, plano, tol)` devuelve la tupla
   `(ok, curvas, puntos)` — las curvas van en la posición 1.
10. `AddClippingPlane` no resuelve con un solo Guid: hay que pasar la lista de
    viewports.
11. `Vector3d.Unitized` no existe: es `Unitize()`, que **muta** el vector.
12. `NamedViews.Add(nombre, vista_id)` pide el Guid del viewport.
13. `vp.Size` es el tamaño en píxeles del viewport; `vp.GetWorldToScreenScale(p)`
    devuelve `(ok, escala)`.
14. **La cámara en viewport paralelo no se deja manejar a mano.**
    `SetCameraLocation` + `Redraw` la deforman, y `ZoomBoundingBox` /
    `ZoomExtents` **restauran la cámara anterior**. La forma que sí funciona:
    `SetToPlanView(origen, ejeX, ejeY, False)` (define el plano de vista) y
    después `ZoomExtents()`.
15. **Corte selectivo**: los planos delimitadores recortan también el dibujo 2D
    que vive en el mismo modelo. Se resuelve con
    `ClippingPlaneGeometry.ParticipationListsEnabled = True` +
    `SetClipParticipation(ids, capas, True)` (lista de exclusión) +
    `CommitChanges()`.

## Checklist de verificación

- [ ] El log imprime `Angulo real sobre la horizontal: 30.00 grados`.
- [ ] En la vista 3D, la cube se ve en axonometría con los ejes a 30/30/90.
- [ ] En la capa `AXO_EJES`, la línea del eje **Y** sale a 30° de la horizontal.
- [ ] El ancho del cubo en el dibujo 2D mide 4.00 m (no 3.27): la magnitud es
      verdadera → `Transform.Distance` o medir con la tool de distancia.
- [ ] La altura mide 4.00 m.
- [ ] La perforación se ve como elipse inclinada a 30° (prueba de que la
      proyección es oblicua y no una axonometría ortogonal).
- [ ] Los planos delimitador `CORTE_A` y `CORTE_B` recortan el modelo.

---

## Referencias (verificadas)

- Rhino 8 — Plano delimitador, Secciones de corte, Dibujos de corte:
  https://docs.mcneel.com/rhino/8/help/es-es/commands/clippingplane.htm
- Corte selectivo:
  https://www.rhino3d.com/es/features/clipping/selective-clipping/
- API `Transform.ProjectAlong` (proyección paralela oblicua):
  https://mcneel.github.io/rhinocommon-api-docs/api/RhinoCommon/html/M_Rhino_Geometry_Transform_ProjectAlong.htm
- API `Intersection.BrepPlane` (curvas de sección):
  https://mcneel.github.io/rhinocommon-api-docs/api/RhinoCommon/html/M_Rhino_Geometry_Intersect_Intersection_BrepPlane.htm
- API `ObjectTable.AddClippingPlane` (plano delimitador):
  https://developer.rhino3d.com/api/rhinocommon/rhino.docobjects.tables.objecttable/addclippingplane
- Tutorial de perspectiva militar (referencia del estudio):
  https://www.youtube.com/watch?v=yXpm6yGVBI0

---

## Pendiente

- [ ] Probar el script dentro de Rhino 8.5 (el modelo local) y ajustar lo que
      falle (sobre todo el paso de booleanos y el de text dots).
- [ ] Probar la variante de 60° y la cabinet (escala 0.5).
- [ ] Versionar el script con el sistema constructivo real: cambiar el cubo
      por un módulo de platform frame y la perforación por el vacío entrepiso.
