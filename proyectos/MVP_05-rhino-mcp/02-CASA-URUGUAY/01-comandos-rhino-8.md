---
tipo: metodologia
fecha_creacion: 2026-10-26
ultima_actualizacion: 2026-10-27
tags: [mvp_05, rhino8, casa_uruguay, comandos, modelado, chapa_sinusoide, zingueria, sweep, extrude, box, sectionstyle, corte, clippingplane, secciones, bitacora]
idioma: es
---

# Comandos Rhino 8 — guía de modelado (Casa Uruguay)

> Referencia práctica de los comandos que usamos en este proyecto, con el paso a paso de los tres modelos que hay que construir: **chapa sinusoidal** (alto de onda 0,036 m), **zinguerías** (perfil Z galvanizado) y **parantes de madera**.
> Todos los ejemplos están en **metros** (modelo) y los layers de layout en **mm**.
>
> **Convención de nombres:** los comandos se nombran **en inglés primero** (es lo que se tipea) y, entre paréntesis, la traducción de Rhino en español.
>
> **Dónde estás hoy:** §9 es el capítulo del **corte 3D** (`ClippingPlane`: insertar, prender, apagar, configurar) + las **vistas por defecto**, los **estilos visuales**, el redibujado y el **diagnóstico del corte a medias**; §10 el de los **Section Styles** por capa; §11 el de la **hoja** (lámina, viewport de detalle, **tabla de escalas** y texto en papel). §14 es la **bitácora viva** de `3D-casa_uruguay_02.3dm`, con el paso a paso del día y las casillas para marcar.

---

## 0. Reglas del proyecto

| Regla | Por qué |
|---|---|
| Todo lo modelado es **sólido cerrado**, nunca malla | En AIZ el corte **salió bien** (la hoja a 1:50 quedó hecha y renderizada). Lo que quedó pendiente fue el **relleno por material** —solo 3 de las 7 capas tenían Section Style— y una geometría abierta. Con sólidos, cada capa lleva su hatch solo |
| Un material por capa | El Section Style se hereda de la capa → el corte sale con hatch por material sin tocar nada |
| El PDF importado vive en capas `REF-PDF-P5` / `REF-PDF-P6` | No se modela encima del trazo importado: el trazo es referencia |
| Se dibuja en el plano del corte y se extruye | La geometría nace en 2D veraz (la planta) y se extruye: así las cotas del PDF se pueden cotejar |
| Toda cota nueva se verifica contra la escala gráfica de 5,000 m | La escala real está probada en el archivo |

Capas de material con su Section Style (patrón/color):

| Capa | Patrón | Color |
|---|---|---|
| `EST-MAD` | líneas | 140 · 95 · 60 |
| `MAD-MARCO_PINO` | líneas (otro ángulo) | 105 · 72 · 43 |
| `04-BAST-2.6` | líneas | 160 · 160 · 160 |
| `05-AISL-LANAVID` | trama | 235 · 215 · 120 |
| `02-FENOLICO` | sólido | 90 · 60 · 40 |
| `03-FILM_POL` | sólido | 215 · 215 · 215 |
| `06 TYVEK` | sólido | 240 · 240 · 235 |
| `07-CALV-2.2` | sólido | 150 · 150 · 150 |
| `08-CHAPA-NEGRO` | sólido | 30 · 30 · 30 |
| `09-ZING-CHAPA_GALV` | sólido | 180 · 185 · 190 |
| `CARP-MET` | sólido | 70 · 70 · 70 |
| `CARP-VID` | sólido | 170 · 200 · 210 |
| `01-PLACA YESO` | sólido | 235 · 235 · 235 |

---

## 1. Importar el PDF

```
Import  →  "G:\Mi unidad\E#E.EDU\mora\Casa frente al mar - Diego Arraigada….pdf"
```

**PDF Select Page**: `5,6` (plantas + cortes). Para el emplazamiento, sumar `2`.

**PDF Import Options**:

| Opción | Valor | Motivo |
|---|---|---|
| Scale | *Fit to default screen* | la escala se fija después, con la barra |
| Import line weights from PDF | **OFF** | bug de Rhino 8: las curvas importadas se ven muy gruesas |
| Import fills as | *Hatches* | los rellenos de las tablas sirven de guía de espesores |
| Load Text | **ON** | para leer rótulos y cotas |

**Calibración con la escala gráfica** (la barra 0·1·2·5):

1. En la planta, identificar la barra (línea horizontal con ticks a 1 y 2 m y la "5" al extremo).
2. `Distance` entre el tick 0 y el tick 5 → por ejemplo `5`.
3. `Scale1D` toda la geometría importada: base = tick 0, referencia = tick 5, distancia = `5`.
4. Verificar con la **otra** planta: su barra debe dar 5,000 m.

> En este proyecto la importación **ya quedó calibrada**: las dos barras miden 5,000000 m exactos.

**Separar por página**: `Select` por ventanas (o por capa de origen) → `ChangeLayer` a `REF-PDF-P5` / `REF-PDF-P6`.

---

## 2. Trazado 2D

| Comando | Opciones clave | Uso |
|---|---|---|
| `Line` | `BothSides`, `FourPoint`, `Vertical` | Aristas rectas del corte |
| `Polyline` | `Close` (cierra la polilínea), `Tangent`, `BothSides` | **El comando clave**: perfiles, ondas, contornos |
| `Rectangle` / `Circle` / `Arc` | | Vanos, pernos, radios |
| `InterpCrv` | | Suavizar una polilínea leída (la onda de la chapa) |

Para copiar el trazo del PDF al modelo: `Copy` con `Paste` en la capa del material, o `InterpCrv` sobre los vértices que interestan.

---

## 3. `Box` — parantes de madera

Opciones de creación: `Default` (2 esquinas opuestas + altura) · `Vertical` (rectángulo perpendicular al CPlane) · `3Point` · `Center` · `Cube` · `Diagonal`.

### Ejemplo: parante de 45 × 145 mm, alto 2,40 m

```
Box
  Vertical            → el rectángulo se dibuja perpendicular al plano actual
  0,0                 → esquina base
  0.045,0.145         → ancho y fondo
  2.4                 → alto
```

VUELTA: la altura se escribe como número plano (`2.4`), no como `2,4` (coma = separador de argumentos).

Alternativa con polilínea (más control del perfil):

```
Polyline  →  4 vértices del perfil  →  Close = Yes
ExtrudeCrv →  Distance 2.4  →  Solid = Yes
```

### Modificar / extender una cara de un box ya hecho

| Objetivo | Comando | Cómo |
|---|---|---|
| **Alargar una cara** (empujar una cara del sólido) | `PushPull` | Seleccionar la cara → mover el cursor → click. Opciones: `Mode = Extrude` (solo extrude) o `Extend` (extiende también las caras vecinas) · `Direction` (2 puntos) · `Invert` |
| **Mover una cara** (mover un muro) | `MoveFace` | Seleccionar la cara → punto de origen → punto de destino. Opciones: `DirectionConstraint = Normal` (solo normal) o `None` · `ToBoundary` (la cara se recorta contra un objeto) |
| Igual, con el widget | `Gumball` | El asa **Extrude/Extend** hace lo mismo que `PushPull` en modo Extend, arrastrando en vivo |
| Alargar una cara hacia otro punto exacto | `ExtrudeSrf` de esa cara + `BooleanUnion` | Opción `Direction` con 2 puntos; `DeleteInput = Yes` |
| Engrosar / dar espesor a un sólido | `Shell` (lo deja hueco con paredes de espesor dado) · `OffsetSurface` (engrosa una superficie) | `Shell` pide espesor y caras a eliminar |
| Tapar una abertura | `Cap` | Cierra huecos de un sólido |

> `PushPull` es la vía directa para "extender una cara"; `MoveFace` es la vía para "mover una cara y que las vecinas acompañen" (mover un muro en la planta).

---

## 4. `ExtrudeCrv` — extruir una curva

Crea una superficie siguiendo la curva en línea recta.

| Opción | Qué hace |
|---|---|
| `Height` / distancia | Distancia de extrusión (se escribe `2.4`; `0` lleva al origen del CPlane, `w0` al origen world) |
| `Direction` | Dos puntos que definen la dirección (útil si la extrusión no es perpendicular al plano de la curva) |
| `BothSides` | Extruye a los dos lados |
| `Solid` | **Si la curva es cerrada y plana, tapa los extremos → sólido cerrado**. Es la opción que hace el trabajo |
| `DeleteInput` | Borra la curva original (o la conserva) |
| `Output` | `Surface` · `SubD` |
| `ToBoundary` | Extruye hasta una superficie límite |
| `SplitAtTangents` | En aristas tangentes: unión (Yes) o quiebre (No) |
| `SetBasePoint` | Fija el primer punto de la dirección |

**Reglas que hacen que funcione:**

1. Para que salga **sólido**: curva **cerrada** (`Polyline` con `Close = Yes`) **y plana** (en el CPlane).
2. Si la curva no es plana, el resultado es polysurface, no sólido → hay que aplanarla o usar `PlanarSrf` + `ExtrudeSrf`.
3. Rhino crea **extrusion** (liviana) si la curva es plana y la extrusión es perpendicular; para cortes conviene polysurface: `Options > General > Uses Extrusions when possible = No`.
4. Una curva plana extruye **vertical al plano de la curva**; si se quiere otro sentido, usar `Direction`.

---

## 5. Darle espesor a una polilínea

Este es el patrón base para chapa, zinguería, perfil Z, placa de yeso, etc.

### Receta general (curva abierta → banda con espesor)

```
1  Polyline / InterpCrv        → trazar el perfil (abierto)
2  Offset  →  Distance = espesor (0.0006)
             Corner = Sharp       (o Round / Smooth / Chamfer)
             Cap = None
             BothSides = No
3  PlanarSrf → entre la curva y su offset  →  banda con espesor
4  ExtrudeCrv → sobre la banda: Direction = 2 puntos a lo largo del largo
                Solid = Yes
```

### Receta corta (si ya tenés el contorno cerrado con el espesor incluido)

```
Polyline (perfil cerrado con el espesor ya dibujado, Close = Yes)
  →  ExtrudeCrv  →  Solid = Yes  →  Distance = largo
```

### Si el recorrido no es recto

```
Offset → PlanarSrf → Sweep1
  riel       = línea de recorrido (cumbrera, correa)
  sección    = la banda con espesor
  Solid = Yes
```

---

## 6. Chapa sinusoidal — alto de onda 0,036 m (ejemplo paso a paso)

**Datos de partida**: la onda de la chapa ya está dibujada en la pág. 5 del PDF (detalle de muro), como polilínea. Alto de onda 0,036 m, paso ≈ 0,10–0,15 m, espesor de chapa ≈ 0,6 mm (el dato exacto sale de la ficha técnica; si es chapa de fibras vegetales, ~8–12 mm).

```
PASO 1 — Traer el perfil
  En la vista Top, zoom al detalle de la pág. 5
  Osnap = Curve / Point sobre la onda del PDF
  Copy  →  Paste  →  capa del material (02-FENOLICO u 08-CHAPA-NEGRO)
  Si el trazo del PDF no se deja copiar limpio:
     Polyline con Close = No clicking los vértices de la onda
     InterpCrv para suavizarla

PASO 2 — Afinar el alto de onda
  La onda debe medir 0,036 m entre valle y cresta:
     Distance entre un valle y la cresta contigua = 0.036
  Si el trazo viene del PDF y mide distinto, corregir con:
     Move de los vértices (o rehacer la Polyline)

PASO 3 — Crear el espesor
  Offset
    Distance = 0.0006        (espesor de chapa)
    Corner   = Sharp
    Cap      = None
    BothSides = No
  → queda la onda original + su offset

PASO 4 — Cerrar la banda
  PlanarSrf
    seleccionar la onda y su offset
    DeleteInput = No          (conviene conservarlas hasta ver el resultado)

PASO 5 — Darle largo
  ExtrudeCrv
    seleccionar la banda
    Direction = 2 puntos en la dirección del largo de la chapa
    Solid = Yes
    DeleteInput = Yes
  → chapa corrugada SÓLIDA, lista para cortar

PASO 6 — Chequeo
  Volume > 0                 (sólido real, no superficie)
  BoundingBox                (el largo debe ser el de la chapa)
  Shaded / Rendered          (la onda se lee)
  En un corte con Section Style, la chapa aparece con su material
```

**Variantes**

| Caso | Cómo |
|---|---|
| La chapa sigue una cubierta curva | `Sweep1`: riel = cumbrera, sección = la banda con espesor, `Solid = Yes` |
| Chapa trapezoidal en vez de sinusoidal | Mismo procedimiento; el perfil son rectas y el `Offset` va con `Corner = Sharp` |
| Se necesita la onda exacta (no la del PDF) | `Polyline` con los vértices calculados sobre la senoide y `InterpCrv` para suavizar |
| Chapa perforada | `BooleanDifference` con cilindros de los_POS |

---

## 7. `Sweep1` / `Sweep2` — zinguerías (perfil Z galvanizado)

**Sweep1** barre una sección transversal a lo largo de un riel.
**Sweep2** barre una sección entre dos rieles.

### Zinguería recta (perfil Z)

```
1  Polyline  →  perfil Z en sección (cerrado: Close = Yes)
2  ExtrudeCrv  →  Direction = 2 puntos a lo largo de la línea de apoyo
                 Solid = Yes
```
Perfil típico: 200 × 75 mm con alma de 2 mm, o el que figure en la ficha.

### Zinguería que sigue la pendiente de la cubierta

```
1  Polyline (perfil Z, cerrado)  →  una sola curva
2  Sweep1
     riel        = línea de la cubierta (curva)
     sección     = el perfil Z
     Solid       = Yes
     Frame Style = Roadlike  (o Freeform)
     Rebuild cross sections = No
     Align cross sections = Yes
```

### Reglas de `Sweep1` que evitan surfaces raras

| Opción | Qué hace |
|---|---|
| `Solid` | Con secciones cerradas genera sólido; sin esto genera superficie |
| `Rebuild cross sections with N control points` | Reconstruye las secciones antes de barrer (resuelve secciones con distinta estructura) |
| `Refit cross sections within N` | Ajusta las secciones a la tolerancia |
| `Align cross sections` | Invierte la dirección de las secciones para que no se inviertan |
| `Frame Style = Freeform / Roadlike` | Freeform mantiene el ángulo con el riel; Roadlike usa un eje |
| `Closed sweep` | Cierra el barrido en loop (solo con 2 secciones) |
| `Global shape blending` | Mezcla linealmente de una sección a la otra |
| `Tangent` / `Point` | Sección que arranca en punto o con tangencia |

> Las secciones transversales deben tener **la misma estructura**: copiá la misma curva y mové la copia, no la redibujes.

---

## 8. Edición de sólidos y booleanas

| Comando | Para qué |
|---|---|
| `BooleanUnion` / `BooleanDifference` / `BooleanIntersection` | Unir, restar, intersecar (perfiles, recortes de vanos) |
| `Split` / `Trim` | Partir un sólido por una superficie o curva de corte |
| `Cap` | Cerrar un sólido abierto |
| `Shell` | Dejar hueco un sólido con espesor de pared dado |
| `Fill` | Rellenar un hueco con una superficie |
| `Simplify` / `Rebuild` | Limpiar curvas de un import |
| `FilletEdge` / `BlendEdge` | Redondeos de arista |
| `MoveFace` / `PushPull` / `Gumball` | Editar caras de un sólido en el espacio |
| `ExtractSrf` / `SplitAtTangents` | Descomponer un sólido en caras para editarlo |
| `Volume` / `Area` / `MassProperties` | Chequeo de que el sólido es real |

---

## 9. Corte 3D — el Clipping Plane

> Capítulo de trabajo en curso (27/10/2026). Toda la información viene de la ayuda oficial de Rhino 8, verificada el 2026-10-27: `docs.mcneel.com/rhino/8/help/en-us/commands/clippingplane.htm` y su versión en español `…/help/es-es/commands/clippingplane.htm`.
>
> **Convención de nombres:** los comandos van **en inglés primero** (es lo que se tipea y lo que muestra la interfaz del Rhino en inglés) y, entre paréntesis, el nombre en español del Rhino traducido. Las opciones y las rutas de menú van en inglés, tal como aparecen en pantalla.

### 9.1 Los tres comandos que se confunden

| English (lo que se tipea) | Español | Toolbar | Menú | Qué hace |
|---|---|---|---|---|
| **`ClippingPlane`** | `PlanoDelimitador` | **Display** · Viewport Layout · Visibility | View > (viewport title) > Clipping plane | Recorta la geometría **a la vista**. Es el plano de corte clásico |
| **`CutPlane`** | `PlanoDeCorte` | **Plane** · Surface Creation · Surface sidebar | Surface > Plane > Cut plane | Crea una **superficie** que atraviesa los objetos: sirve de cortador real (booleanas, `Trim`) |
| **`ClippingSections`** | `SeccionesDeCorte` | **Sections** · Clipping section creation · Drafting · New in V8 | **Drafting > Sections > Create** | Nuevo en V8. Crea el plano atravesando los objetos, con nombre, etiqueta y vista guardada |

**La barra `Sections` no viene abierta** en Rhino 8: clic derecho sobre cualquier barra → **Sections**. Trae los 12 comandos de la familia de cortes.

### 9.2 Insertar el plano: las variantes

| Variante (inglés) | Español | Qué hace | Cuándo |
|---|---|---|---|
| **`Vertical`** | `Vertical` | Dibuja el rectángulo **perpendicular al plano de construcción** | **La más simple para un corte de obra**: desde la vista Plan (CPlane = Top) da un plano vertical. Igual que el `A-A` de AIZ |
| **`Default`** | `(Predeterminado)` | Rectángulo con dos esquinas opuestas | Control total del tamaño y la posición del plano |
| **`3Point`** | `3Puntos` | Dos esquinas adyacentes + un punto del lado opuesto | Cortes oblicuos, o cuando el modelo se ve de canto |
| **`Center`** | `Centro` | Rectángulo desde el punto central y una esquina | Un plano centrado en el modelo |
| **`EdgeMidpoint`** | `PuntoMedioDeBorde` | Desde el punto medio del primer borde | Poco usado |
| **`AroundCurve`** | `AlrededorDeCurva` | Rectángulo perpendicular a una curva | Cortes perpendiculares a una alineación |

**El rectángulo del widget define la zona de influencia**: si queda más chico que el modelo, las partes que caen afuera **no se recortan**. El rectángulo tiene que ser más grande que la planta.

### 9.3 Cómo se trabaja con los clipping planes, día a día

| Quiero… | Cómo |
|---|---|
| **Mover** el plano | Arrastrar el **punto de translación** (funciona con referencias a objetos, incluso en una vista que no está recortada) |
| **Redimensionar** el widget | Arrastrar el **punto de escala** |
| **Ver un corte con espesor** en vez de la sección fina | Properties → **Custom Depth** activado + **Depth** = un número en unidades del modelo. **Depth = 0 dibuja la sección fina** (lo que necesita el dibujo) |
| **Dar vuelta** el corte | Properties → **Invert direction** (los triángulos del widget siempre apuntan al lado visible) |
| **Recortar solo algunos objetos** | Properties → **Objects Clipped** → `Include Selected` / `Exclude Selected` + las listas de Objects y Layers |
| **Recortar solo un objeto** | Object Properties → **Clip** (Rhino 8, por objeto, independiente de la vista) |
| **Recortar solo en algunas vistas** | Properties → **Views Clipped** → las tildas de *Model Space* y *Layout Space* |
| **Apagarlo en todas las vistas** | Properties → **Reset Views** |
| **Copiar la configuración** de otro plano | Properties → **Match** (`Igualar`) |
| **Nombrarlo** para que se vea en la vista | Properties → **Name** + **Label** (`None` / `Dot` / `Text`) |
| **Guardarlo como vista o como CPlane** | `SaveClippingSectionViews` (Drafting > Sections > Save views) · `SaveClippingSectionCPlanes` (Save CPlanes) |
| **Apagar una sección** | `ClearClippingSections` (Drafting > Sections > Clear all) |
| **Borrar el plano** | Seleccionar el widget + `Del` |
| **Definir el relleno** del corte | Properties → **Section Style**: `By Layer` (cada material conserva el suyo) o `Custom` (el plano impone el suyo) → ver §10 |

### 9.4 Por qué el corte no aparece en la isométrica

| Síntoma | Causa | Solución |
|---|---|---|
| **Lo hice en Plan y en la isométrica no se ve el corte** | Un clipping plane recorta **solo las vistas donde está habilitado**; se habilita en la vista donde se creó, y en las demás hay que prenderlo | Seleccionar el plano → **Properties > "Views Clipped"** → tildar la isométrica. O: seleccionar el plano, dejar la isométrica activa y correr `EnableClippingPlane` (`ActivarPlanoDelimitador`) |
| Se ve **la mitad equivocada** | Los triángulos del widget apuntan al lado visible | Properties → **Invert direction** |
| **No se ve nada** en ninguna vista | El rectángulo del widget quedó más chico que el modelo, o el widget está rojo | `Vertical` desde la vista Plan, con rectángulo ≥ la planta. **El widget se pone rojo cuando no intersecta la caja de los objetos**: es la alerta de que el corte no toca la geometría |
| El corte se ve **sin relleno** | La capa no tiene Section Style, o el objeto es malla | Section Style por capa (ver §10) y geometría sólida |
| Se ve **solo en la vista donde lo creé** | Es el comportamiento por defecto de Rhino | Lo esperado: el recorte se controla vista por vista |
| El corte **desaparece al mover el widget** | El widget se movió fuera de la caja del modelo | Volver a colocarlo con osnap sobre la cota conocida |

### 9.5 Prender y apagar los clipping planes: todos los interruptores

| Quiero… | Cómo |
|---|---|
| **Prender** el corte en la vista activa | `EnableClippingPlane` (`ActivarPlanoDelimitador`) — seleccionar el plano, dejar la vista activa, correr el comando (barra **Display** / **Visibility**) |
| **Apagar** el corte en la vista activa | `DisableClippingPlane` (`DesactivarPlanoDelimitador`), mismo lugar |
| **Apagarlo en todas las vistas** | Properties → **Reset Views** |
| Prender o apagar **una vista puntual** | Properties → **Views Clipped** → las tildas |
| **Borrar** el plano | Seleccionar el widget + `Del` |
| Recortar **solo algunos objetos** | Properties → **Objects Clipped** → `Include Selected` / `Exclude Selected` + las listas de Objects y Layers |
| Apagar **todas las secciones V8** de una vista | `ClearClippingSections` (Drafting > Sections > Clear all) |
| **Copiar la configuración** de otro plano | Properties → **Match** (`Igualar`) |

### 9.6 El camino corto de la sección al dibujo

| # | Comando (inglés / español) | Menú | Qué hace |
|---|---|---|---|
| 1 | `ClippingSections` / `SeccionesDeCorte` | Drafting > Sections > Create | Crea el plano atravesando los objetos. Opciones: `Dir` (`CPlane` / `X` / `Y` / `Custom`), `CustomDepth`, `Depth`, `Clip`, `Name` (prefijo: `A-` → `A_01`), `LabelMode`, `SaveToNamedView`, `Flip` |
| 2 | `ViewClippingSections` / `VerSeccionesDeCorte` | Drafting > Sections > View | Muestra la sección en una vista alineada con ella. Opciones: `Clip`, `ClearOtherSections`, `SetView`, `SetCPlane` |
| 3 | `ExtractClippingSections` / `ExtraerSeccionesDeCorte` | Drafting > Sections > Extract sections | Extrae el corte como **curvas y tramas**. Opciones: `Curve`, `Hatch`, `Group` |
| 4 | `ExtractClippingSlices` / `ExtraerSegmentosDeCorte` | Drafting > Sections > Extract slices | Extrae el corte con **grosor** (sólidos 3D). Opciones: `Thickness`, `Location` (`Front` / `Center` / `Back`), `UseClippingPlaneDepth` |
| 5 | `ClippingDrawings` / `DibujosDeCorte` | Drafting > Sections > Create drawings | Dibujo 2D en el plano XY universal, con fondo, ocultas y silueta. Opciones: `ShowHatch`, `ShowSolid`, `AddBackground`, `AddHidden`, `AddSilhouette`, `Angle`, `Projection` |
| 6 | `NestedClippingDrawing` / `DibujoDeCorteAnidado` | Drafting > Sections > Nested drawings | Varios cortes ordenados en fila o columna. Opciones: `Arrangement` (`WorldX` / `WorldY`), `Spacing`, `Width`, `ShowLabel` |
| 7 | `SaveClippingSectionViews` / `GuardarVistasDeSecciónDeCorte` | Drafting > Sections > Save views | Guarda la sección como **Vista guardada**. Opciones: `Projection`, `Clip`, `SetCPlane` |
| 8 | `UpdateClippingDrawings` / `ActualizarDibujosDeCorte` | Drafting > Sections > Update drawings | Refresca los dibujos cuando cambia la geometría (se refrescan solos al mover el plano) |
| 9 | `ExportClippingDrawings` / `ExportarDibujosDeCorte` | Drafting > Sections > Export drawings | Guarda los cortes en archivos `.3dm` o `.dwg` separados |

**Clásico para un corte puntual:** `Section` (`Sección`) — barra *Curve from Object*, menú *Curve > Curve From Objects > Section*. Interseca un plano con los objetos y crea curvas planas, puntos o tramas. Opciones: `ExtendSection`, `BySectionPlane`.

### 9.7 Receta: el corte `A-A` de este proyecto

| Paso | Qué hacés | Qué verificás |
|---|---|---|
| 1 | `ClippingPlane` → `Vertical` desde la vista **Plan** | el widget queda vertical y su dirección "arriba" es la del corte |
| 2 | Rectángulo ≥ la planta, con un extremo sobre la cota conocida del corte | el widget **no** se pone rojo |
| 3 | Properties → **Name**: `A-A` | el corte queda identificado |
| 4 | Properties → **Depth**: `0` | se dibuja la sección fina, lista para el dibujo |
| 5 | Properties → **Section Style**: `By Layer` | el relleno sale del Section Style de cada material (ver §10) |
| 6 | Properties → **Views Clipped** → tildar **View** e **Isometric** | el corte se ve en las dos |
| 7 | doble clic en la isométrica → `ViewClippingSections` → `SetView=Yes` | la vista queda alineada al corte |
| 8 | `ExtractClippingSections` → `Curve=Yes`, `Hatch=Yes`, `Group=Yes` | el 2D del corte con el hatch por material |

### 9.8 Las vistas por defecto: `SetView`, `Isometric` y navegación

**`SetView`** (menú *View / título del viewport > Set View*, barra **Set View**) cambia la vista a una vista **estándar**, del plano de construcción actual o del sistema world. Opciones de línea de comandos: `CPlane` (la vista del PlanoC vigente) y `World` (las del sistema).

| Vista | Comando | Para qué |
|---|---|---|
| Planta (world) | `SetView` → `World` → `Top` | la vista de trabajo del plano |
| Inferior (world) | `SetView` → `World` → `Bottom` | el corte visto desde abajo |
| Alzado frontal | `SetView` → `World` → `Front` | corte vertical |
| Alzado lateral derecho | `SetView` → `World` → `Right` | corte vertical |
| Alzado lateral izquierdo | `SetView` → `World` → `Left` | corte vertical |
| Alzado posterior | `SetView` → `World` → `Back` | corte vertical |
| Perspectiva | `SetView` → `World` → `Perspective` | render |
| Planta sobre el PlanoC | `Plan` (Set View > Plan) | planta alineada al PlanoC en 0,0 |
| Dos puntos de perspectiva | `ViewportProperties` → *Set 2-Point Perspective* | perspectiva con dos escapes |

**`Isometric`** (barra **Isometric**, menú *View > Set View > Isometric*): "changes the current viewport properties to a **parallel projection** isometric view looking from a specified quadrant toward 0".

| Opción | Vista | Nota |
|---|---|---|
| `SE` | **Sureste** | **la que usamos en este proyecto** |
| `SW` | Suroeste | |
| `NE` | Noreste | |
| `NW` | Noroeste | |
| `ZoomExtents` | — | hace zoom para que entre todo el modelo |

`Isometric SE` deja la vista **en proyección paralela** mirando desde el cuadrante sureste hacia el origen: es la axonométrica de trabajo.

**Navegación** (barra **Set View**): `Pan` · `RotateView` (gira la cámara alrededor del objetivo) · `RotateCamera` (gira el objetivo alrededor de la cámara) · `Zoom` (`Dynamic` · `Extents` · `Selected` · `1To1`) · `ZoomLens` (lente, solo perspectiva) · `DollyZoom` · `UndoView` / `RedoView` · `Turntable` · `WalkAbout` · `MoveTargetToObjects` (centra el objetivo en lo seleccionado) · `OrientCameraToSrf` (alinea a la normal de una superficie) · `PerspectiveMatch` · `Zoom1To1Calibrate` · `ReadViewportsFromFile` (copia el layout de vistas de otro modelo). `Ctrl`+`Tab` cambia de viewport.

### 9.9 Las vistas guardadas: `NamedView`

`NamedView` (barra **Set View** / **Render Sidebar**, menú *View > Set View > Named Views*, panel *Window > Panels > Named Views*).

| Acción | Cómo |
|---|---|
| **Guardar** la vista actual | `NamedView` → **Save as** (le poné nombre) |
| **Restaurar** | doble clic en el nombre, o **Restore → To current viewport**. También se puede **arrastrar** la vista desde el panel a cualquier viewport |
| Restaurar en una vista flotante nueva | **Restore → To new floating viewport** |
| Traer vistas de otro archivo | **Import from 3dm file** (o `Import Named Views from 3dm File` en el menú contextual) |
| Crear con cámara y objetivo a mano | **Create Using Widget** (pick de location, target y field of view) |
| Editar la cámara de una vista guardada | **Edit by looking** (abre una vista temporal para navegar) |
| Ajustes del panel | *Auto-update thumbnails* · *Restore aspect ratio* · *Show named view widget* |
| Animación | **Animation** (transición suave entre vistas, para presentaciones) |

> El título de la vista muestra un **\*** cuando la vista actual difiere de la vista guardada.

**En este proyecto:** la axonométrica 30/60 de AIZ (`axo3060`) **no es una vista estándar** → es una vista guardada con cámara propia. Se trae al archivo nuevo con **Import from 3dm file** sobre `set-ej_corte_A3-1-50.3dm`, y sirve tanto para el viewport de modelo como para el detalle de la lámina.

### 9.10 Los estilos visuales (display modes)

Los modos de visualización están en *Tools > Options > View > **Display Modes***, y se eligen con `SetDisplayMode` (`Viewport` = `Active` / `All`, `Mode` = lista) o con el título del viewport.

| Modo | Qué es | Para qué en este proyecto |
|---|---|---|
| `Wireframe` | solo líneas, sin sombreado | ver la geometría sin tapar nada |
| **`Shaded`** | sombreado opaco con los **colores de capa** | **el modo del corte** (el que usa la hoja AIZ) |
| `Rendered` | simulación de render con luces y materiales | presentación |
| `Raytraced` | render en tiempo real por GPU | imágenes, no para la lámina |
| `Ghosted` | superficies translúcidas | ver el interior sin cortar |
| `X-Ray` | con isocurvas y lo que queda delante | transparentar para leer el interior |
| **`Technical`** | simula el **dibujo técnico**: siluetas, intersecciones, aristas y bordes con líneas punteadas, en tiempo real | **el mejor para revisar un corte**: las aristas del corte se ven |
| `Artistic` | fondo de imagen y líneas suaves, efecto lápiz | presentación |
| `Pen` | blanco con líneas negras, como un dibujo a pluma | presentación |
| `Monochrome` | todo en escala de grises, con siluetas y aristas negras | presentación monocroma |
| `Arctic` | blanco con sombras suaves | presentación |

Atajos: `Ctrl`+`Alt`+`W` wireframe · `+S` shaded · `+R` rendered · `+G` ghosted · `+X` X-Ray.

**Configurar un modo** (*Options > View > Display Modes*): `New` (crea uno a partir de otro) · `Copy` · `Delete` · `Import` / `Export` (archivo `.ini`, para compartir la configuración) · `Restore Defaults`. Grupos de ajustes:

| Grupo | Qué se configura |
|---|---|
| **Viewport** | Background: *Use application settings* · *Solid color* · *Image file* · *Gradient 2 colors* · *Gradient 4 colors* · *Use render settings* · *Transparent* |
| **Shading** | *Shade objects* · *X-Ray all wires* · *Flat shading* · *Shade vertex colors* · **Color and material usage** (*Object's color* · *Single color for all objects* · *Single object color* · *Rendering material* · *Custom material for all objects*) · **Backface settings** · **Shading effects** (standard / parallel lines) |
| **Visibility** | *Show surface edges* · *isocurves* · *tangent edges* · *seams* · SubD wires/creases/boundaries/symmetry · *mesh wires* · *curves* · *lights* · **clipping planes** · *text* · *annotations* · *points* · *pointclouds* |
| **Lighting scheme / Grid / Objects** | luces, grilla y los ajustes por tipo de objeto (Points, Curves, Surfaces, SubD, Meshes, Lights, **Clipping Planes**, Lines) |
| **Shadows / Other** | sombras y opciones varias |

#### Los planos de corte dentro de un modo visual

*Options > View > Display Modes > [modo] > **Objects > Clipping Planes***:

| Ajuste | Qué hace | Por qué importa acá |
|---|---|---|
| **Use section styles** | la apariencia de los rellenos y las aristas de la sección sale de las propiedades **Section Style** de los objetos | **Apagado, el corte se dibuja con un color genérico y no con el hatch del material** |
| **Show fills** (solo modos shaded) | cuando el plano corta un objeto 3D y la sección es cerrada, la sección **se rellena** | Apagado, el corte sale solo con líneas |
| **Color usage** | *Viewport* · *Render material* · *Plane's material* · *Solid color* | de dónde sale el color del relleno |
| **Show edges** | dibuja las aristas entre el plano y los objetos cortados | **es la línea del corte** |
| **Edge thickness** | el grosor de esa arista, en píxeles | el peso del corte en la vista |
| **Shade selected plane** + **Transparency %** | colorea el plano seleccionado | para ver de qué lado está el corte |

### 9.11 Cómo se regenera la vista

Cuando el corte no se actualiza en la pantalla, hay que forzar el redibujado:

| Quiero… | Cómo |
|---|---|
| **Forzar el redibujado** | cambiar el modo de visualización y volver al mismo (`SetDisplayMode` → *Shaded* → *Shaded*) |
| Recalcular el encuadre | `Zoom` → `Extents` en esa vista |
| **Apagar y prender** el corte | `DisableClippingPlane` → `EnableClippingPlane` |
| Forzar el recálculo moviendo el plano | arrastrar el punto de translación un poco y volver |
| Restaurar la vista | doble clic en una vista guardada (`NamedView`) |
| Recargar todo | cerrar y abrir el archivo (último recurso) |
| **Redibujar desde la API** (scripts) | `doc.Views.Redraw()` — recalcula todas las vistas; también `SetRedrawOff` / `SetRedrawOn` para desactivar el redibujado durante un script |

### 9.12 Diagnóstico: en el layout de corte A no se ve la mitad del corte

| Lo que se ve | Causa | Cómo se comprueba | Solución |
|---|---|---|---|
| **Se ve el corte de un plano que ya no existe** (el plano fue borrado y el corte sigue, "como si hubiera dos") | **Las Named views guardan el estado de los planos de corte**: la opción *Named views set clipping planes* hace que al restaurar una vista se restaure también el estado de clipping que tenía. Si esa vista se guardó cuando el plano viejo estaba activo, el corte vuelve con ella | 1) `SelClippingPlaneInViewport`: si selecciona **un solo** plano, el segundo corte no es real → es estado guardado o redibujado. 2) Revisá el panel **Named Views**: ¿esa vista se guardó con el plano viejo? | 1) *Tools > Options > View* → desmarcar **Named views set clipping planes** (y, si hace falta, *Named views set CPlane* y *set projection*). 2) Volver a restaurar la vista. 3) O **re-crear la vista guardada**: `NamedView` → *Save as* con un nombre nuevo, desde el estado actual. 4) Forzar el redibujado (§9.11) |
| El corte sale a medias y **no se va con `DisableClippingPlane`** | La vista quedó con un **redibujado viejo** (la caché de la sección) | — | Forzar el redibujado (§9.11): cambiar el modo de visualización · `Zoom Extents` · apagar y prender el plano · restaurar una vista guardada · cerrar y abrir el archivo |
| **`SelClippingPlaneInViewport` responde "No objects added to selection"** | **Ningún plano de corte está recortando esa vista** → lo que se ve como corte no es un recorte vivo: (a) el comando se corrió en una vista que no es la del corte, (b) el plano recorta el modelo pero **no el detalle**, (c) lo que se ve es **geometría** (el corte 2D del DWG importado como superficies), o (d) es un redibujado viejo | Ver **§9.13**: 3 pruebas para separar las cuatro causas | según la prueba: tildar el detalle en *Views Clipped* · apagar la capa de la geometría · forzar el redibujado |
| El detalle muestra el modelo **entero**, sin corte | El clipping plane **no está habilitado en ese detalle** | Properties del plano → **Views Clipped** → *Layout Space* | tildar el detalle; o `EnableClippingPlane` con el detalle activo |
| Se ve **una franja con espesor** en vez del corte | **Custom Depth** activado con `Depth` > 0 | Properties → *Custom Depth* / *Depth* | `Depth = 0` → sección fina |
| El corte se ve **sin relleno**, solo líneas | En el modo del detalle: **Use section styles** apagado, o **Show fills** apagado, o el objeto es malla sin sección cerrada | *Options > View > Display Modes > [modo del detalle] > Objects > Clipping Planes* | activar **Use section styles** y **Show fills**; trabajar con sólidos |
| Se ve **media casa**, como si hubiera **otro plano de corte** | Hay **dos** planos de corte activos en esa vista | `SelClippingPlaneInViewport` (selecciona los planos que recortan la vista actual) | `DisableClippingPlane` sobre el que sobra, o desmarcar esa vista en *Views Clipped* del otro |
| El corte se ve pero **miráis la cara de atrás** | Los triángulos del widget apuntan al lado visible; desde el otro lado se ve el exterior sin cortar | Properties → *Invert direction* | invertir la dirección, o apuntar la cámara del detalle al lado correcto |
| La vista **no se regenera** | La vista quedó con el resultado anterior de la sección | — | ver **§9.11** |
| El corte se imprime con **otro color** que el de la capa | Los **colores del Section Style pisan los print colors** | Properties del objeto → *Section Style* | objeto en `By Layer` + plano en `By Layer` (§10.1) |
| El corte se ve en el modelo pero **no en el PDF** | En `Print` está marcado *Clipping planes*, o la lámina no está elegida | `Print` → *View list* / *Visibility* | desmarcar *Clipping planes*; elegir la lámina |
| El corte se ve **sin hatch en el detalle** (pero sí en la vista de trabajo) | El detalle tiene **su propio modo de visualización**, y ahí pueden estar apagados *Show fills* o *Use section styles* | Properties del detalle → *Display mode*; y *Options > View > Display Modes > [modo] > Objects > Clipping Planes* | §9.14: mismo modo (Shaded) · **Show fills** ON · **Use section styles** ON · capas con *Detail On* · objetos sólidos cerrados |

### 9.13 El corte que no es un corte: 3 pruebas para separar las causas

Cuando `SelClippingPlaneInViewport` responde **"No objects added to selection"**, el hecho es concluyente: **ningún plano de corte está recortando esa vista**. Lo que se ve como "corte" puede ser otra cosa. Las tres pruebas, en orden:

**Prueba 1 · ¿En qué vista estabas?**

El comando actúa sobre la **vista activa** (de modelo o de detalle), así que el resultado depende de dónde se corrió:

| Corrido en… | Resultado | Lectura |
|---|---|---|
| en el **detalle del corte A** (doble clic para activarlo) | selecciona el plano | el plano recorta el detalle → el corte real está. Si además ves un segundo corte, **ese segundo es geometría** (prueba 3) |
| en el **detalle** | *No objects* | el plano recorta el modelo pero **no el detalle** → el detalle muestra el modelo entero |
| en la **isométrica del modelo** | selecciona el plano | el plano recorta la vista de modelo; el detalle hay que habilitarlo aparte |
| en la **isométrica** | *No objects* | el plano no recorta en absoluto: lo que se ve no es clipping |

**Corrección del caso "el detalle no está recortado":** seleccionar el plano → Properties → **Views Clipped** → *Layout Space* → tildar el detalle. O: `EnableClippingPlane` con el detalle activo.

**Prueba 2 · ¿Es geometría o un redibujado viejo?**

`Zoom` → `Extents` en esa vista (fuerza el redibujado):

| Resultado | Diagnóstico | Solución |
|---|---|---|
| el corte fantasma **desaparece** | era un **redibujado viejo**: la vista quedó pintada con la sección del plano borrado | re-crear la vista guardada (`NamedView` → *Save as*, nombre nuevo) y revisar *Named views set clipping planes* en *Options > View* |
| el corte fantasma **sigue** | es **geometría real** | prueba 3 |

**Prueba 3 · Si es geometría: ¿de dónde viene?**

El DWG trajo **el corte 2D de inicio** junto con la base 3D. Según las opciones de importación, ese 2D puede haber entrado como **superficies** en vez de curvas — y una superficie metida dentro del modelo se ve **exactamente como un plano de corte**.

| Qué mirar | Cómo |
|---|---|
| Qué objeto es | Ventana de selección sobre la zona del corte → `What` (tipo, capa, si es superficie o poliesuperficie) |
| En qué capa está | la capa sale en el `What`; apagarla en el panel **Layers** y ver si el fantasma desaparece |
| Cuántos hay de cada tipo | panel **Objects** (*Window > Panels > Objects*) filtrado por tipo |
| La opción de importación culpable | **`Convert wide polylines to surfaces`**: si estuvo **ON**, las polilíneas anchas del corte 2D entraron como superficies. Volver a importar con la opción **OFF** (§14.2) deja el 2D como polilínea |

**Cómo se deja prolijo:** mover esa geometría 2D a una capa de referencia (`REF-2D`) y apagarla, o borrarla si ya se modeló. El corte de verdad lo hace el clipping plane, no la geometría importada.

### 9.14 El corte se ve en el detalle pero **sin hatch**

Síntoma: en la **vista de trabajo** el corte sale con el hatch por material, pero en el **detalle de la lámina** el corte aparece **sin relleno** (o con un color plano). El relleno de la sección lo dibuja el **modo de visualización**, y el detalle tiene **su propio modo**.

| # | Qué revisar | Cómo | Lo que tiene que estar |
|---|---|---|---|
| 1 | **El modo de visualización del detalle** | Properties del detalle → **Display mode** | el **mismo** que el de la vista de trabajo (**Shaded**). El relleno de sección solo se dibuja en **modos shaded**; en `Rendered`/`Raytraced` se usa el material de render, y en `Wireframe`/`X-Ray` no hay relleno |
| 2 | **Los ajustes de clipping plane del modo** | *Tools > Options > View > Display Modes > [modo del detalle] > **Objects > Clipping Planes*** | **Show fills** = ON (solo en modos shaded: "when a clipping plane intersects a 3-D object **and the section is closed**, the section is filled") y **Use section styles** = ON ("the appearances of clipping fills and edges are based on objects' **section style** properties") |
| 3 | **El estilo del plano de corte** | Properties del clipping plane → **Section Style** | `By Layer` (cada material con su relleno) |
| 4 | **El estilo de los objetos** | Properties del objeto → **Section Style** | `By Layer` — si están en `By Clipping Plane` y el plano en `Custom`, el relleno es el del plano, no el del material |
| 5 | **La capa** | panel **Layers** → columna **Detail On** | encendida para las capas de material, y la capa con **Section Style** ≠ `None` |
| 6 | **Que la sección sea cerrada** | `What` sobre el objeto | si el objeto es una **superficie abierta** o una **malla**, la sección no se rellena: hay que trabajar con sólidos cerrados |
| 7 | **El relleno sale plano, sin trama** | es el punto 2 | con *Use section styles* apagado, el relleno usa un color genérico en vez del patrón del material |

**Cómo se lee el resultado:** si el detalle muestra el corte **con un color plano** → es el punto 7 (*Use section styles* apagado en ese modo). Si no muestra **nada** de relleno → son los puntos 1, 5 o 6.

> El relleno de la sección es de pantalla: el **Print** usa los colores de impresión de la capa, salvo que el Section Style tenga color propio (los colores del Section Style **pisan** los print colors, ver §10.1).

### 9.15 La trama no se lee en la lámina: el ajuste que la manda

**Hay dos escalas de trama, y no son la misma.** La que se toca en el diálogo *Section Style* no es la que decide lo que pasa en la lámina:

| Ajuste | Dónde | Qué controla |
|---|---|---|
| `Pattern Scale` | diálogo **Section Style** (por capa u objeto) | la escala **propia del patrón** de ese material |
| **Enable hatch scaling** + **Model space hatch scale** | *File > Properties > **Hatch*** (o el comando `HatchScale`) | el **escalado global** de las tramas |

El manual de Rhino 8 lo dice literalmente:

> **Enable hatch scaling → Enabled**: "Hatch patterns in model viewports are scaled by the **Model space hatch scale** value" · **"Hatch patterns in detail views print with the same scale regardless of the zoom factor"**.
> **Disabled**: "Hatch patterns will not scale."

**Por eso el corte se veía en la vista de trabajo y no en la lámina:** con el escalado **desactivado**, la trama se dibuja en el **espacio del modelo** → a 1:30 mide **0,03 mm en el papel** → invisible. Con el escalado **activado**, el patrón en el detalle **no depende del zoom**.

**La receta que recomienda McNeel** (wim, en el foro de McNeel): *primero* dejar la escala que se ve bien **en papel**, *después* la que se ve bien **en modelo**.

**Cómo se cambia**

1. *File > Properties > **Hatch*** → **Enable hatch scaling** = **Enabled**.
2. **Model space hatch scale**: el factor global. Se calibra mirando el resultado (abajo).
3. En cada capa: el **Pattern Scale** propio del material (para diferenciar materiales que comparten patrón, se cambian **rotación** y **escala**).

**Si el escalado está desactivado**, la cuenta del patrón en espacio de modelo es:

```
Pattern Scale = (separación deseada en el papel × escala) / separación base del patrón
```

| Separación deseada en el papel | a 1:30 | a 1:50 | a 1:20 |
|---|---|---|---|
| 1 mm | 30 | 50 | 20 |
| 2 mm | 60 | 100 | 40 |
| 3 mm | 90 | 150 | 60 |
| 5 mm | 150 | 250 | 100 |

**La calibración (con el escalado activado)**: el *Model space hatch scale* es el factor que controla la separación de la trama en el papel → se parte de **3** (3 mm entre líneas) y se corrige midiendo con `Distance` sobre la lámina hasta que la trama se lea.

**Y si el relleno no aparece directamente** (ni liso ni tramado), el problema no es la escala sino el **modo de visualización**: ver §9.14 (puntos 1, 2, 5 y 6).

> **Ojo:** esto afecta también a la hoja AIZ, que se construyó con `Pattern Scale` = 1,0 a 1:50. Conviene revisarlo ahí también.

---

## 10. Section Styles — cómo se hace el relleno por material

> Nuevo en Rhino 8. Un **Section Style** es una propiedad de los **objetos, de las capas y de los planos de corte**: guarda los ajustes del *hatch* (patrón, color, rotación, escala, fondo) y del *borde* (visible, tipo de línea, ancho, color). El plano de corte lee esas propiedades para rellenar la sección.
>
> Fuentes: `…/help/en-us/popup_moreinformation/sectionstyle.htm` · `…/help/en-us/commands/layer.htm` · `…/help/en-us/properties/object.htm` · User's Guide de McNeel, *Clip & Section | Intro to Section Styles*.

### 10.1 Los tres niveles: cuál manda

| Nivel | Dónde vive | Valores | Para qué |
|---|---|---|---|
| **Por clipping plane** | Properties del plano → **Section Style** | `By Layer` · `Custom` | `By Layer` = cada material conserva su relleno (**la forma de trabajar**). `Custom` = el plano impone un relleno único para todo |
| **Por capa** | Properties de la capa → **Section Style** | `None` · `Custom` | **El principal en este proyecto**: un estilo por capa de material |
| **Por objeto** | Properties del objeto → **Section Style** | `By Layer` · `By Parent` · `By Clipping Plane` · `Custom` | La excepción: un objeto que necesita un relleno distinto del de su capa |

**Orden de resolución:** un plano en `By Layer` toma el estilo de la capa; un objeto en `By Layer` toma el de su capa; un objeto en `By Clipping Plane` toma el del plano. Una capa en `None` = **su sección sale vacía**.

> **Sobre los colores:** los colores del Section Style **pisan los colores de impresión**.

### 10.2 El diálogo Section Style, campo por campo

**Hatch**

| Campo | Valores | Notas |
|---|---|---|
| **Pattern** | patrón de trama · `Solid` · `None` | Los patrones disponibles en el documento: `Solid`, `Hatch1`, `Hatch2`, `Hatch3`, `HatchDash`, `Grid`, `Grid60`, `Plus`, `Squares` (se pueden sumar más desde las propiedades de Hatch) |
| **Pattern Color** | `By Object` (del objeto, de la capa o del plano de corte) · `Custom color` | `By Object` hereda el color de la capa: práctico, pero con `Custom` cada material conserva su propia tinta |
| **Pattern Rotation** | ángulo | La segunda forma de diferenciar dos materiales que comparten patrón |
| **Pattern Scale** | factor | La tercera |
| **Background** | `Viewport` (toma el color de las opciones de plano de corte del modo de visualización) · un color propio | El color del fondo dentro de la trama |
| **Section open objects** | on / off | Rellena la sección cerrada de un objeto **abierto** (una superficie sin volumen) |

**Boundary**

| Campo | Valores | Notas |
|---|---|---|
| **Show** | on / off | Dibuja las curvas de borde de la trama: la línea gruesa que se lee como "corte" |
| **Linetype** | `By Layer` · `Custom` | Un tipo de línea propio en la arista del corte |
| **Width Scale** | factor | Escala el ancho de la línea: lo que le da el peso al corte en el dibujo |
| **Color** | `By Object` (del objeto, de la capa o del plano) · `Custom color` | El color de la arista del corte |

### 10.3 Paso a paso: el estilo de una capa

| Paso | Qué hacés | Qué ves |
|---|---|---|
| 1 | Abrir el panel **Layers** (Window > Panels > Layers) o el comando `Layer` (barra **Layer** / **Standard**, menú *Edit > Layers > Edit Layers*) | la lista de capas |
| 2 | Click en la columna **Section Style** de la capa | la celda muestra `None` |
| 3 | Click en la celda → **Custom** | se abre el diálogo **Section Style** |
| 4 | Pestaña **Hatch**: `Pattern` (por ejemplo `Hatch1`), `Pattern Color` → Custom color, `Pattern Rotation` (por ejemplo `45`), `Pattern Scale` (por ejemplo `2`), `Background` → el color que quieras | el diálogo muestra los ajustes |
| 5 | Pestaña **Boundary**: `Show` on, `Linetype` → `By Layer`, `Width Scale` (por ejemplo `1,5`), `Color` → Custom color | la arista del corte toma su peso |
| 6 | **OK / Apply** | la capa ya lleva el estilo |
| 7 | Repetir en cada capa de material | cada material corta con su propia trama |

**Atajo para varias capas:** seleccionar varias con `Ctrl`+click en el panel de capas y editar **una sola vez** la columna **Section Style** para todas.

### 10.4 Paso a paso: el estilo de un objeto

1. Seleccionar el objeto.
2. Panel **Properties** → **Section Style** → `Custom` (o `By Clipping Plane` para que siga al plano).
3. Se abre el diálogo **Section Style** → los mismos campos que §10.2 → **OK / Apply**.

### 10.5 Por qué cada capa tiene que estar diferenciada

El plano de corte llena cada objeto que corta **con el estilo de la capa a la que pertenece**. Entonces:

- Si una capa está en **`None`**, los objetos que están en ella salen **sin relleno** → el corte se lee como un hueco.
- Si todas las capas llevan **el mismo estilo**, el corte sale **uniforme** → el dibujo pierde la distinción de materiales, que es justamente el sentido de un corte.

**Esto es lo que pasó en AIZ:** el modelo se cortó bien y la hoja A3 salió, pero solo **3 de las 7 capas de material** tenían Section Style → el resto del corte quedó sin rellenar. La regla que queda: **una capa por material, cada una con su Section Style, configurado antes del primer corte**.

### 10.6 Las 13 capas de material y sus estilos

Patrones y colores fijados el 26/10 (rotación 0°, escala 1,0). La rotación y la escala son los dos mandos para separar dos materiales que comparten patrón.

| Capa | Pattern | Pattern color | Rotation | Scale | Width scale del borde |
|---|---|---|---|---|---|
| `EST-MAD` | `Hatch1` (líneas) | 140 · 95 · 60 | 0° | 1,0 | 1,0 |
| `MAD-MARCO_PINO` | `Hatch2` | 105 · 72 · 43 | 45° | 1,0 | 1,5 |
| `04-BAST-2.6` | `Hatch1` | 160 · 160 · 160 | 90° | 1,0 | 1,0 |
| `05-AISL-LANAVID` | `Hatch3` | 235 · 215 · 120 | 0° | 1,0 | 1,0 |
| `02-FENOLICO` | `Solid` | 90 · 60 · 40 | — | — | 1,0 |
| `03-FILM_POL` | `Solid` | 215 · 215 · 215 | — | — | 0,5 |
| `06 TYVEK` | `Solid` | 240 · 240 · 235 | — | — | 0,5 |
| `07-CALV-2.2` | `Solid` | 150 · 150 · 150 | — | — | 1,0 |
| `08-CHAPA-NEGRO` | `Solid` | 30 · 30 · 30 | — | — | 1,5 |
| `09-ZING-CHAPA_GALV` | `Solid` | 180 · 185 · 190 | — | — | 1,0 |
| `CARP-MET` | `Solid` | 70 · 70 · 70 | — | — | 1,5 |
| `CARP-VID` | `Solid` | 170 · 200 · 210 | — | — | 1,0 |
| `01-PLACA YESO` | `Solid` | 235 · 235 · 235 | — | — | 1,0 |

Las capas de referencia (`REF-PDF-P5`, `REF-PDF-P6`, `REF-TXT`, `00-EJES`) quedan con **Section Style = `None`**: son trazado, no material.

### 10.7 Cómo llevar los estilos al archivo nuevo

Los Section Styles son **propiedades del documento**: **no viajan con el import de un DWG**, así que hay que configurarlos de nuevo en `3D-casa_uruguay_02.3dm`. Dos vías:

| Vía | Cómo | Cuándo |
|---|---|---|
| **A mano** | Las 13 capas + los 13 estilos, siguiendo §10.3 | 13 capas, una sola pasada |
| **Con `LayerStateManager`** (Layer States) | En `3D-casa_uruguay.3dm` (donde los estilos ya existen): *Window > Panels > Layer States* → **Save** (nombre: `CASA-UY-SECCION`) → en el archivo nuevo: **Import** → elegir el `.3dm` → **Restore**. El **Section Style** es uno de los ajustes de capa que el Layer State guarda y restaura | Un solo import trae las capas, sus colores y sus section styles |

### 10.8 Verificación

| Qué verificar | Cómo | Lo esperable |
|---|---|---|
| El corte rellena con materiales distintos | Mover el clipping plane | cada material muestra su propia trama, y el patrón cambia en vivo |
| Una capa no rellena | Layers panel → la columna Section Style de esa capa | no puede estar en `None` |
| El corte sale uniforme | Todas las capas llevan el mismo estilo | darle a cada material su patrón / rotación / color |
| La arista del corte no tiene peso | Boundary → `Show` y `Width Scale` | la línea del corte se lee como corte |
| El estilo no cambia | Los objetos están en `By Clipping Plane` o el plano en `Custom` | poner el plano en `By Layer` y los objetos en `By Layer` |

### 10.9 La API de los Section Styles en Rhino 8

Ruta verificada con un probe sobre Rhino 8.5 (26/10/2026) — sirve para configurar las 13 capas de un tirón por script:

| Qué | Cómo |
|---|---|
| **Poner el estilo a una capa** | `capa.SetCustomSectionStyle(Rhino.DocObjects.SectionStyle())` → devuelve `Void` |
| Leer / quitar el estilo | `capa.GetCustomSectionStyle()` · `capa.RemoveCustomSectionStyle()` |
| Miembros escribibles del `SectionStyle` | `HatchIndex` (**índice** del patrón, no el nombre) · `HatchScale` · `HatchRotationRadians` (**en radianes**) · `HatchPatternColor` · `HatchPatternPrintColor` · `BoundaryVisible` · `BoundaryColor` · `BoundaryPrintColor` · `BoundaryWidthScale` · `BackgroundFillColor` · `BackgroundFillMode` · `BackgroundFillPrintColor` · `SectionFillRule` · `Name` |
| Patrones disponibles | `doc.HatchPatterns` → `Solid`, `Hatch1`, `Hatch2`, `Hatch3`, `HatchDash`, `Grid`, `Grid60`, `Plus`, `Squares` |
| En el **plano de corte** | `plano.Attributes.SetCustomSectionStyle(...)` · `plano.Attributes.SectionAttributesSource` (`By Layer` / `By Clipping Plane` / `Custom`) · `plano.Attributes.HatchBackgroundFillColor` |
| **Habilitar el corte en una vista** | `plano.Attributes.AddClipViewport(id_del_viewport)` y `RemoveClipViewport(id)` → es el "Views Clipped" del panel de propiedades |
| Escala de tramas del documento | `doc.ModelSpaceHatchScalingEnabled` · `doc.ModelSpaceHatchScale` (comando `HatchScale`) |
| Redibujar | `doc.Views.Redraw()` |

Los scripts que usan todo esto: `scripts/configurar-corte-hatch-rhino.py` (notas en `scripts/configurar-corte-hatch-rhino_notas.md`) y `scripts/inspeccionar-seccion-rhino.py` (inspección de solo lectura).

---

## 11. La hoja: layout, viewport de detalle, escala y texto en papel

> Fuentes oficiales: `commands/layout.htm` · `commands/detail.htm` · `commands/copyviewporttodetail.htm` · `commands/text.htm` · `documentproperties/annotation.htm` · `commands/print.htm` (verificadas 200 el 2026-10-27).
> La configuración de referencia es la **hoja AIZ** (`set-ej_corte_A3-1-50.3dm`), que quedó construida y verificada.

### 11.1 La lámina: `Layout` (`Layout` / LayoutProperties)

`Layout` (barra **Drafting** / **Viewport Layout**, menú *View > Layout > New Layout*) abre el diálogo **New Layout**:

| Campo | Valores | En este proyecto |
|---|---|---|
| **Name** | texto | `UY-CORTE-A` |
| **Initial Detail Count** | 1 a 4 | 1 (la sección) — el 4 vistas de Rhino 8 usan además *First/Third Angle Projection* |
| **Printers** | lista de impresoras | la que definirá el `Print` (Rhino PDF) |
| **Size** | tamaños de la impresora | **A3** |
| **Portrait / Landscape** | — | **Landscape** (420 × 297 mm) |
| **Width / Height** | medidas + unidades de papel | 420 × 297 mm |

`LayoutProperties` (Edit Layout) repite esos mismos campos para corregir la lámina después.

El orden que fija el manual: 1) diálogo New Layout · 2) dibujar el borde o insertar el cajetín · 3) agregar anotaciones · 4) **crear los detalles** · 5) **configurar en cada detalle la vista, la orientación y la escala** · 6) agregar texto y cotas en la vista de layout · 7) definir la visibilidad del borde del detalle en la impresión (Properties → **Print Width** / **No Print**) · 8) `Print`.

### 11.2 El viewport de detalle: las 3 formas de crearlo

| Camino | Cómo | Cuándo |
|---|---|---|
| **A — a mano** | `Detail` (barra **Drafting**, menú *Layout > Add Detail View*) → `Add` → se dibuja el rectángulo → `Projection` → `Scale` → `Lock` | Control total del encuadre, la orientación y la escala |
| **B — traicionar un viewport del modelo** | `CopyViewportToDetail`: click dentro del viewport de modelo → queda como detalle en la lámina. Opciones: `Transfer` = `Copy` (deja el viewport) o `Move` (lo elimina del modelo) | Cuando el viewport de modelo ya tiene la cámara exacta que querés (la axonometría 30/60 de AIZ) |
| **C — importar la lámina entera** | `ImportLayout` (menú *Layout > Import*): trae una o más láminas de otro `.3dm` | Para heredar la página A3 con su detalle ya a 1:50 |

**Opciones de `Detail`:** `Add` (dibuja el rectángulo) · `Center` (desde el punto central) · `Projection` (`Top` / `Bottom` / `Left` / `Right` / `Front` / `Back` / `Perspective`) · `Enable` (activar el detalle) · `FromDetail` (nuevo detalle con la dirección relativa al seleccionado) · `Projection First/Third Angle` · `Scale` · `Lock` / `Unlock` · `EnablePage`.

**Mecánica de trabajo con los detalles:**

- Doble clic sobre un detalle → **lo activa** (en la zona donde se superponen, doble clic cerca del centro).
- **Girar el contenido** de un detalle: doble clic para activarlo → `RotateView`. Para **mantener la dirección de vista**: `TiltView`, o `Shift`+`Alt` + arrastrar con el botón derecho.
- **Girar el marco** del detalle: seleccionar el borde → `Gumball` o `Rotate`.
- `SelDetail` selecciona todos los rectángulos de detalle de una lámina.
- `HideInDetail` / `ShowInDetail` / `HideLayersInDetail` / `ShowLayersInDetail` controlan qué se ve **solo** en un detalle.

### 11.3 Las variantes de configuración del viewport (la que usamos)

| Propiedad del detalle | Valores | **Configuración elegida (AIZ)** | Por qué |
|---|---|---|---|
| **Title / Name** | texto | `AIZ-CORTE-A` | Identifica el corte en la lámina y en el panel |
| **Projection** | `Top` / `Bottom` / `Left` / `Right` / `Front` / `Back` / `Perspective` | axonometría 30/60 en **proyección paralela** | La cámara de AIZ: `axo3060`, parallel, Shaded |
| **Display mode** | los modos de visualización | **Shaded** | Los sólidos se leen; `Technical` sirve si hay que ver las aristas |
| **Scale Value** | `___ <units> on layout` / `___ <units> in model` | **1:50** (1 m del modelo = 20,0 mm en el papel) | Escala de obra para este tipo de casa |
| **Locked** | on / off | **ON** | La vista no se mueve por accidente al navigate |
| **Enable** | — | Activo | El detalle muestra la cámara |
| **Print Width / No Print** (propiedades del objeto) | — | `No Print` en el marco | El rectángulo del detalle no se imprime |
| **Capa del detalle** | la capa activa al crearlo | capa de la lámina | Para apagar el detalle entero si hace falta |
| **Clipping plane en el detalle** | *Views Clipped* → *Layout Space* | `A-A` habilitado **dentro del detalle** | El corte se ve en la lámina, no solo en el modelo |

**Variantes según para qué sirve el detalle:**

| Variante | Projection | Display mode | Scale | Uso |
|---|---|---|---|---|
| **Corte de obra** | `Right` o `Front` (según la orientación del corte) | Shaded | 1:50 | la lámina de construcción |
| **Axonométrica de presentación** | `Perspective` o la 30/60 en paralelo | Shaded / Rendered | 1:100 | carátula y nombre |
| **Planta de obra** | `Top` | Shaded + líneas | 1:50 | el corte horizontal |
| **Detalle constructivo** | `Right` / `Front` | Technical | 1:5 / 1:10 | encuentro de carpintería |

### 11.4 La escala: cómo se configura y cómo se verifica

El detalle tiene su propia escala, independiente de la escala de impresión:

| Prompt | Qué significa | Para 1:50 con layout en **mm** y modelo en **m** |
|---|---|---|
| `___ <units> on layout` | la distancia **en la lámina** | `20` (o `20mm`) |
| `___ <units> in model` | la distancia **en el modelo** que le corresponde | `1` (o `1m`) |

**El número que se tipea en cada prompt está en las unidades de ese espacio**: por eso 1:50 con lámina en mm y modelo en m es **20 y 1**, y no 1 y 50. Escribir las unidades explícitas (`20mm` y `1m`) es la forma segura: Rhino las convierte.

**Qué significa la escala:** 1:X = **1 milímetro en la hoja son X milímetros en el modelo** (o sea X/1000 metros). Ejemplo del enunciado: si **1 mm en la hoja son 0,01 m en el modelo**, la escala es **1:10** (0,01 m = 10 mm).

#### La tabla de escalas

Con **lámina en mm** y **modelo en metros**:

| Escala | on layout | in model | 1 mm en la hoja = | 1 m del modelo mide | Sirve para |
|---|---|---|---|---|---|
| **1:500** | `2` mm | `1` m | 0,50 m | 2,0 mm | implantación, contexto urbano |
| **1:200** | `5` mm | `1` m | 0,20 m | 5,0 mm | terreno, conjunto de casas |
| **1:100** | `10` mm | `1` m | 0,10 m | 10,0 mm | axonométrica de presentación, planta general |
| **1:50** | `20` mm | `1` m | 0,05 m | **20,0 mm** | corte de obra |
| **1:40** | `25` mm | `1` m | 0,04 m | 25,0 mm | corte de obra con la casa entera |
| **1:30** | `33,3` mm | `1` m | **0,03 m** | **33,3 mm** | **el corte A de este proyecto** |
| **1:25** | `40` mm | `1` m | 0,025 m | 40,0 mm | corte con más detalle |
| **1:20** | `50` mm | `1` m | 0,02 m | 50,0 mm | corte de obra en detalle |
| **1:10** | `100` mm | `1` m | 0,01 m | 100,0 mm | encuentro constructivo |

La forma de leerla al revés: **1 m del modelo mide (1000 ÷ X) mm en la hoja**. Para 1:50 → 1000/50 = 20 mm ✓. Para 1:30 → 1000/30 = 33,3 mm ✓.

**El corte A quedó en 1:30**: 1 unidad de layout en **mm** equivalen a **0,03 m** del modelo (o sea 30 mm). En el prompt se escribe `1` (on layout) y `0.03` (in model) — **con el punto decimal, no la coma**. La equivalencia: 1 mm de papel = 30 mm de modelo, y 1 m del modelo mide **33,3 mm** en la hoja.

**Verificación (la que usamos en AIZ):** medir sobre la lámina con `Distance` **1,00 m del modelo** → tiene que dar el valor de la columna "1 m del modelo mide". Es el número que confirma que la escala quedó bien.

Después de fijarla: `Lock` al detalle, para que el zoom no la mueva.

> La escala del diálogo `Print` (campo *Scale → On paper = In model*) es otra cosa: es la escala de impresión del viewport o layout que se imprime. Para una lámina con detalle a 1:50 no se toca: la escala ya la lleva el detalle.

#### Cuánto modelo entra en el detalle

El detalle es un rectángulo de papel; la escala define qué tramo de modelo se ve adentro. Con la A3 de este proyecto (detalle de **400 × 270 mm**):

| Escala | Ancho de modelo que entra | Alto de modelo que entra | ¿Alcanza la casa (≈14 × 10 m)? |
|---|---|---|---|
| 1:500 | 200 m | 135 m | sobra, es un contexto |
| 1:200 | 80 m | 54 m | sobra |
| 1:100 | 40 m | 27 m | sobra |
| 1:50 | 20 m | 13,5 m | sí, con margen |
| **1:40** | **16 m** | **10,8 m** | **sí, justa** |
| **1:30** ← *la del corte A* | **12 m** | **8,1 m** | **no alcanza el largo de la casa (≈14 m)** |
| 1:25 | 10 m | 6,75 m | no |
| 1:20 | 8 m | 5,4 m | no |
| 1:10 | 4 m | 2,7 m | solo un encuentro |

Este cálculo es el control previo: **elegí la escala según lo que querés que entre en el rectángulo**, no al revés.

> **Ojo con el 1:30 del corte A:** con un detalle de 400 × 270 mm a 1:30 se ve **12 × 8,1 m** de modelo. Si el corte A tiene que mostrar la casa completa (≈14 m de largo), **no entra**: o el detalle se agranda (a 1:30, para 15 m de ancho harían falta 500 mm de papel — más que el A3), o la escala pasa a **1:40** (16 × 10,8 m, entra justa) o **1:50** (20 × 13,5 m, entra con aire). Si en cambio el corte A es de **una parte** de la casa, el 1:30 está perfecto y más legible.

#### Los tres sitios donde hay escala (y cuál manda)

| Dónde | Qué define | En este proyecto |
|---|---|---|
| **El detalle** (Properties → *Scale Value*) | la escala de dibujo de ese viewport | **el que manda** (1:50) |
| El diálogo `Print` (*Scale → On paper = In model*) | la escala de impresión de un viewport de modelo o de una lámina | no se toca en una lámina con detalle a 1:50 |
| El **estilo de anotación** (*Model space scale*) | el tamaño del texto y las flechas: normalmente la **inversa** de la escala de impresión | se ajusta para que el texto mida 2,5 mm en el papel |

### 11.5 Escribir en el espacio de papel

Para escribir en la lámina hay que tener **activa la vista de layout** (la pestaña de abajo del área de modelado).

`Text` (barra **Dimension** / **Drafting**, menú *Drafting > Text Block*): **1)** se escribe el texto · **2)** se especifican las propiedades · **3)** se designates la ubicación.

| Propiedad del texto | Qué es | En papel |
|---|---|---|
| **Style** | el estilo de anotación que usa | el que define la altura y la fuente |
| **Height** | la altura del texto | **en unidades de layout (mm)** → 2,5 mm es 2,5 mm en la lámina, no se escala con el detalle |
| **Font** | la tipografía | — |
| **Mask** | fondo opaco detrás del texto | `None` · `Background` (el color del fondo del viewport) · `Solid Color` |
| **Frame around text** | `No frame` · `Rectangular frame` · `Capsule frame` | para destacar un rótulo |
| **Text alignment** | izquierda / centro / derecha y arriba / medio / abajo | — |
| **B / I / U** | negrita, cursiva, subrayado | — |
| **Text Field** | campo dinámico: `%<Area("id")\*2>%` | texto que se actualiza solo |
| **Degree / Radius / Diameter / PlusMinus / Exponent** | símbolos | — |
| **Horizontal to view** | el texto siempre plano a la pantalla | desmarcarlo solo si hay que orientarlo |

**Texto en el detalle vs. texto en la lámina:** el texto que se escribe **dentro** de un detalle pertenece al espacio de modelo y **se escala con el detalle**; el que se escribe en la lámina (fuera del rectángulo) es texto de papel y tiene su tamaño real. Para rótulos dentro del dibujo, conviene el texto de papel.

### 11.6 Los estilos de anotación (y el detalle que se desactiva al abrir un DWG)

`File > Properties > Annotation properties` (o `DocumentProperties`) → pestaña **Annotation Styles**:

| Ajuste | Qué hace |
|---|---|
| **Current** | el estilo vigente |
| **Annotation Styles** + `New` / `Match` / `Import` / `Edit` / `Delete` | la lista de estilos del documento. **`Import`** trae estilos desde otro `.3dm` (comando `ImportAnnotationStyles`, *File > Import From File > Annotation Styles from 3dm File*) |
| **Enable model space scaling** | las anotaciones se multiplican por el *Model space scale* |
| **Enable layout space scaling** | el texto y las flechas en los detalles se ven con **tamaño fijo** en la lámina, se zoom que se haga |
| **Model space scale** | el tamaño mostrado = tamaño del componente × este valor. Normalmente es la inversa de la escala de impresión |
| **Adjusted text height** | la altura de texto ya ajustada |
| **Scale all sizes** | un factor que redimensiona todos los elementos de la anotación |
| **Font / Height / Text gap** | la tipografía, la altura (en unidades de modelo) y el margen |
| **Fit text** | `Auto` / `Inside` / `Right` / `Left` / `HintLeft` / `HintRight` (dónde va el texto de la cota) |
| **Arrows / Arrow size** | el estilo y el tamaño de las flechas |
| **Length units / Unit-Format** | unidades y formato de las cotas lineales |
| **Decimal separator** | `.` o `,` |
| **Tolerances / Leaders** | tolerancias y líneas de referencia |

**El flujo que recomienda el manual:** 1) fijar en el estilo una **altura de fuente adecuada para la lámina** → 2) activar **Enable model space scaling** si está apagado → 3) ajustar el **Model space scale**.

> **Ojo con este archivo:** el comando `Open` **desactiva el "layout space scaling"** cuando se abre un DWG/DXF en Rhino. Este archivo viene de un import de DWG → hay que **activar "Enable layout space scaling"** para que los textos de las cotas dentro del detalle conserven un tamaño fijo en el papel.

### 11.7 Imprimir: `Print` (`Print`)

| Bloque | Ajuste | Para esta lámina |
|---|---|---|
| **Destination** | Printer | **Rhino PDF** (es el que puede guardar capas en el PDF) |
| | Size + **Use layout page size** | A3, tomado del layout |
| | Orientation | Landscape |
| **Output type** | **Vector output** | el raster no permite guardar capas en PDF |
| **Output color** | **Print color** | sale el *Print Color* de cada capa (el de los materiales) |
| **View and Output Scale** | View list → la lámina | `Viewport/Layout` |
| **Linetypes** | **Match pattern definition** | el patrón se imprime a su tamaño de definición, no al del viewport |
| **Line width** | **Linetype units are model/page lengths** → `Page lengths` | el ancho se mantiene constante en el papel |
| | Scale by / Default line width | el peso de la línea del corte |
| **Visibility** | **desmarcar `Clipping planes`** | que no se imprima el widget del plano de corte |
| | desmarcar `Background color`, `Lights` | la lámina va en blanco |
| **Text** | Notes / Filename | `None` salvo que el pie de hoja se haga con notas |

El orden de impresión de tramas, anotaciones y geometría lo define el manual (*Print order*).

#### La lámina en blanco y negro, con los hatches del corte

Son cuatro cosas distintas que se confunden. Esta es la guía:

| Quiero… | Dónde | Ajuste |
|---|---|---|
| **Ver en la pantalla cómo va a salir impreso** | `PrintDisplay` (o el menú del título del viewport → **Print Preview**) | `PrintDisplay` = ON: la vista muestra los **colores y anchos de impresión** en vez de los de pantalla. La **vista previa del diálogo `Print`** muestra el resultado final, con la conversión a gris incluida |
| **Imprimir en blanco y negro** | `Print` → **Output color** | **Black and white**: "converts colors to gray scale" |
| **Fondo blanco** (sin el gris del fondo del viewport) | `Print` → **Visibility** | desmarcar **Background color** (y *Background bitmap* / *Wallpaper*). En la lámina el fondo ya es blanco; en el **detalle** el fondo lo define el modo de visualización → *Options > View > Display Modes > [modo] > Viewport > Background* → *Solid color* blanco o *Transparent* |
| **Que los hatches del corte se vean igual que en la pantalla** | el **modo de visualización del detalle** | *Objects > Clipping Planes* → **Use section styles** ON + **Show fills** ON (ver §9.14). El relleno toma el color del **Section Style** de la capa, y ese color **pisa el color de impresión** (§10.1) |

**Los colores y anchos de la lámina salen de la capa, pero los de layout:**

| Propiedad de la capa | Dónde se aplica |
|---|---|
| `Print Color` / `Print Width` | impresión desde el **espacio de modelo** |
| **`Layout / Detail Print Color`** / **`Layout / Detail Print Width`** | impresión desde la **lámina y sus detalles** ← las que cuentan para la hoja |

**El detalle que cambia la lectura del dibujo:** en blanco y negro los materiales **no se distinguen por color** → se distinguen **por patrón**. Por eso las dos reglas que ya están documentadas se vuelven críticas:

1. **Un patrón por material** (las 13 capas con su Section Style propio, §10.6).
2. **El `Pattern Scale` tiene que estar a la escala del papel** (§9.15): con 1,0 el patrón mide 1 mm en el modelo → 0,03 mm en el papel a 1:30 → liso. Para 3 mm de papel a 1:30 → **90**.

Para que el corte se lea en **línea negra clásica** (no gris): en el Section Style de la capa → **Boundary → Color** = negro y **Hatch → Pattern Color** = negro o `By Object` con la capa en negro; el `Width Scale` del borde (1,0 / 1,5) es el peso de la línea del corte.

### 11.8 Reusar la hoja AIZ

| Camino | Cómo | Qué trae |
|---|---|---|
| **A — `ImportLayout`** | *Layout > Import* → `set-ej_corte_A3-1-50.3dm` | la página A3 entera con su detalle a 1:50 y su cámara 30/60 |
| **B — `Detail` a mano** | `Add` → `Projection` → `Scale` (`20` / `1`) → `Lock` | control total, y el detalle queda con la cámara que elijamos |
| **C — `CopyViewportToDetail`** | click en el viewport de modelo con la axonometría | la cámara exacta, sin repetir la escala |
| **Extra — estilos de anotación** | `ImportAnnotationStyles` desde el mismo `.3dm` | los tamaños de texto y de flecha de la hoja AIZ |

### 11.9 Checklist de la hoja

- [ ] `Layout` nuevo, A3 landscape 420 × 297 mm, nombre `UY-CORTE-A`
- [ ] Bordes / cajetín en la lámina
- [ ] `Detail` → `Add` → rectángulo → `Projection` → `Scale` (`20` / `1`) → `Lock`
- [ ] **Verificar la escala**: `Distance` sobre 1,00 m del modelo → **20,0 mm** en el papel
- [ ] Clipping plane `A-A` habilitado **dentro del detalle** (*Views Clipped* → *Layout Space*)
- [ ] Textos de papel con el estilo de anotación correcto y `Enable layout space scaling` **activado**
- [ ] `Print` → Rhino PDF · Vector output · Print color · Match pattern definition · sin `Clipping planes`

### 11.12 Receta completa: el viewport de detalle de la hoja, de principio a fin

**Paso 0 · Preparar el documento**

| Qué | Cómo |
|---|---|
| Unidades | *Tools > Options > Document Properties > Units*: modelo en **metros**, layout en **mm** |
| Estilo de anotación | *File > Properties > Annotation* → activar **Enable layout space scaling** (en este archivo, que viene de un DWG, viene apagado) |
| Section Styles | uno por capa de material (§10), antes del primer corte |

**Paso 1 · La lámina**

`Layout` → *Name* `UY-CORTE-A` · *Printer* Rhino PDF · *Size* **A3** · *Landscape* · *Width* **420** / *Height* **297** (mm) · *Initial Detail Count* **1**.
Luego el borde: `Rectangle` de (0, 0) a (420, 297) en la lámina, o insertar el cajetín.

**Paso 2 · El detalle**

| Sub | Acción | Valor |
|---|---|---|
| a | `Detail` → `Add` → dibujar el rectángulo | de (10, 22) a (410, 292) → **400 × 270 mm** |
| b | `Projection` | `Top` / `Right` / `Front` / `Left` / `Bottom` / `Back` / `Perspective` — según de qué lado se mira el corte |
| c | `Scale` | `20` (on layout, mm) → `1` (in model, m) → **1:50** |
| d | `Lock` | el detalle queda fijo |
| e | Properties → *Title* | `A-A` |
| f | Properties → *Display mode* | **Shaded** (o **Technical** para ver las aristas del corte) |

> **Trampa importante:** las opciones de `Projection` del detalle **no incluyen la axonométrica 30/60** (esa es una cámara propia, no una vista estándar). Para la 30/60 hay dos caminos: `CopyViewportToDetail` desde el viewport de modelo que ya tiene esa cámara, o importar la vista guardada `axo3060` con `NamedView` → *Import from 3dm file* y luego `CopyViewportToDetail`.

**Paso 3 · El corte dentro del detalle**

1. Seleccionar el clipping plane → Properties → **Views Clipped** → *Layout Space* → **tildar el detalle**.
2. Properties → **Depth** = `0` (sección fina).
3. Properties → **Section Style** = `By Layer` (el relleno sale del material de cada capa).
4. Comprobar: en el detalle aparece el corte con el hatch por material.

**Paso 4 · Verificar la escala (el control que no falla)**

`Distance` sobre la lámina: pick dos puntos que en el modelo estén a **1,00 m** → tiene que leer **20,0 mm**. Si no, la escala del detalle está mal (§11.4).

**Paso 5 · El marco del detalle**

Properties del objeto "detalle" → **Print Width**: `No Print` si el rectángulo no debe imprimirse, o un ancho de línea si el marco es parte del dibujo.

**Paso 6 · El texto** → §11.13.

**Paso 7 · Imprimir** → §11.7.

#### Si lo hacés por script: la secuencia que funciona en Rhino 8

`SetScale` **no fija la escala** si se lo llama solo (reportado por un usuario de McNeel en junio 2024 y publicado por Dale Fugier). La secuencia que sí funciona:

```python
pagina.SetActiveDetail(detalle.Id)          # 1) el detalle tiene que estar activo
detalle.Viewport.ZoomExtents()              # 2) encuadrar
detalle.DetailGeometry.IsProjectionLocked = True    # 3) bloquear la proyección
detalle.DetailGeometry.SetScale(1, doc.ModelUnitSystem, 33.3333, doc.PageUnitSystem)  # 4) escala
detalle.CommitChanges()                     # 5) CONFIRMAR  <-- sin esto no aplica
```

`SetScale(distanciaEnModelo, unidadesModelo, distanciaEnLamina, unidadesLamina)`. Con el modelo en metros y la página en mm: **1 m del modelo = 33,3333 mm en la lámina → 1:30**.

Y para armar el detalle desde cero: `doc.Views.AddPageView(nombre, 420, 297)` → `pagina.AddDetailView(nombre, Point2d(10,22), Point2d(410,292), DefinedViewportProjection.Right)` → la secuencia de arriba → `doc.Views.Redraw()`. Para habilitar el corte adentro: `plano.Attributes.AddClipViewport(detalle.Id)`.

### 11.13 El texto de la hoja: rótulos, escala y referencias

Hay **tres familias** de texto, y cada una va en un espacio distinto:

| Familia | Para qué | Dónde | Comando |
|---|---|---|---|
| **Datos de la lámina** | proyecto, lámina, fecha, autor, **título del corte** (`CORTE A-A`) y **escala** (`1:50`) | **espacio de papel** (la lámina, fuera del rectángulo del detalle) | `Text` |
| **Leyenda de materiales** | lista de materiales con su muestra de trama | espacio de papel | `Text` + `Hatch` |
| **Referencias numeradas** | los números 1, 2, 3… sobre el dibujo y sus llamadas | **dentro del detalle** (espacio de modelo) | `Dot` y `Leader` |

**1 · Datos de la lámina** — `Text`: escribir el texto → Enter → pick la ubicación. Alturas recomendadas (son **mm de papel**, no del modelo):

| Texto | Altura en el papel |
|---|---|
| Título de la vista (`CORTE A-A`) | **5 mm** |
| Nombre de la lámina / proyecto | 3,5 mm |
| Escala (`1:50`) | 3 mm |
| Notas al pie | 3 mm |
| Leyenda | 2,5 mm |

> La hoja AIZ quedó con un pie de 2 líneas: **5 mm** la primera y **3 mm** la segunda. Es el mismo criterio.

**2 · Leyenda de materiales** — en la lámina, una columna de textos (2,5 mm) con, al lado de cada uno, una **muestra de trama**: un `Hatch` en espacio de papel con el mismo patrón y color que el Section Style del material (§10.6), de unos 8 × 8 mm.

**3 · Referencias numeradas dentro del dibujo**

| Comando | Qué hace | Cómo |
|---|---|---|
| **`Dot`** (Drafting > Other Annotations > Annotation Dot) | un punto de anotación con el número dentro | 1) se escribe el texto (el número) · 2) se designa la ubicación. **Se dibuja en espacio de pantalla**: hacer zoom o girar no cambia su tamaño ni su orientación, y siempre se ve por delante de los objetos. Doble clic para editar texto, fuente y altura. `Alt`+doble clic edita el punto cuando se superpone con objetos. El texto puede tener varias líneas y un *Secondary text* |
| **`Leader`** (Drafting > Leader) | una llamada con flecha y texto | 1) pick de la **cabeza** (la punta de la flecha) · 2) pick de los puntos de la línea de llamada · 3) **Enter** para terminar · 4) se escribe el texto en el diálogo. El *Text gap* del estilo de anotación define la distancia entre el final de la línea y el texto; la opción *Landing* agrega un tramo horizontal antes del texto |

**El tamaño del texto dentro del detalle — la regla que hay que Respectar**

El texto y los puntos que están **dentro** del rectángulo del detalle pertenecen al **espacio de modelo**, así que se escalan con el detalle: a 1:50, un texto de 3 mm en el papel necesita **150 mm** en el modelo. Hay dos salidas:

| Salida | Cómo | Cuándo |
|---|---|---|
| **Layout space scaling** (recomendado) | *File > Properties > Annotation* → **activar Enable layout space scaling**: el texto y las flechas de los detalles se muestran con **tamaño fijo** en la lámina, se zoom que se haga | siempre, y sobre todo en este archivo (importado de DWG) |
| Calcular la altura en el modelo | altura en el modelo = altura en el papel × escala (3 mm × 50 = **150 mm**) | cuando el estilo de anotación no se puede tocar |

| Texto | Altura en el papel | Altura en el modelo a 1:50 (sin layout space scaling) |
|---|---|---|
| Referencia numerada (`Dot`) | 3 mm | 150 mm |
| Rótulo de cota | 2,5 mm | 125 mm |
| Llamada (`Leader`) | 2,5 mm | 125 mm |

**4 · Texto dinámico (Text Field)** — los text fields se evalúan mientras Rhino corre y muestran el resultado; la sintaxis es `%<campo opciones>%`:

| Campo | Ejemplo |
|---|---|
| Área | `%<Area("d90815b8...80c59a")%` |
| Longitud de curva | `%<CurveLength("07c73fde...8a5c7b")%` |
| Volumen | `%<Volume("…")%` |
| Aritmética | `%<Area("d90815b8...80c59a")\*2>%` (el doble del área) |

Si un campo no se puede evaluar, en pantalla aparece `####`. Sirve para los rótulos de la leyenda que dependen de una superficie (área de unajo, volumen de un muro) — la cifra se actualiza sola cuando cambia la geometría.

**5 · El rótulo de la escala** — no hay text field de escala: se escribe a mano (`1:50`) y se controla con el paso 4 de §11.12.

---

## 12. Cheatsheet

| Comando | Para qué | Opciones clave |
|---|---|---|
| `Import` | Traer el PDF | página, `line weights OFF`, `Load Text ON` |
| `Scale1D` | Calibrar con la escala gráfica | base, referencia, distancia |
| `Line` | Arista | `Vertical` |
| `Polyline` | Perfil, onda, contorno | `Close = Yes` |
| `InterpCrv` | Suavizar una onda | puntos de control |
| `Rectangle` | Vano, sección | |
| `Box` | Parante, bloque | `Vertical`, `Center`, `Cube` |
| `ExtrudeCrv` | Extruir curva | `Solid`, `BothSides`, `Direction`, `DeleteInput` |
| `ExtrudeSrf` | Extruir una cara | `Direction` |
| `Offset` | Espesor de una polilínea | `Distance`, `Corner`, `Cap`, `BothSides` |
| `PlanarSrf` | Cerrar la banda | `DeleteInput` |
| `Sweep1` | Barrer sección sobre riel | `Solid`, `Rebuild cross sections`, `Frame Style` |
| `Sweep2` | Barrer entre dos rieles | `Vertical`, `Cross-section` |
| `PushPull` | Extender una cara | `Mode = Extend`, `Direction` |
| `MoveFace` | Mover una cara | `DirectionConstraint`, `ToBoundary` |
| `Gumball` | Transformar en vivo | asa Extrude/Extend |
| `Boolean*` | Unir / restar | |
| `Shell` / `Cap` | Engrosar / cerrar | |
| `ClippingPlane` | Corte 3D en la vista | `Vertical` · `Profundidad=0` · `Estilo de sección=Por capa` · `Vistas delimitadas` |
| `ActivarPlanoDelimitador` / `DesactivarPlanoDelimitador` | Prender / apagar el corte por vista | barra Visualización · Visibilidad |
| `ClippingSections` | Crear el corte atravesando los objetos | `Dir` (X / Y / Personalizado) · `Nombre` · `GuardarEnVistaGuardada` |
| `ViewClippingSections` | Ver la sección en una vista alineada | `DefinirVista` · `Recortar` |
| `ExtractClippingSections` | Sacar el corte 2D | `Curva` · `Trama` · `Agrupar` |
| `ClippingDrawings` | Dibujo 2D con fondo y ocultas | `MostrarTrama` · `AñadirFondo` · `AñadirOcultas` |
| `NestedClippingDrawing` | Varios cortes en fila | `Disposición` · `Espaciado` |
| `Section` | Corte clásico por intersección | `ExtendSection` · `BySectionPlane` |
| `Layout` | Lámina de impresión | A3 landscape 420 × 297 mm · `Initial Detail Count` |
| `LayoutProperties` | Editar la lámina | `Name` · `Size` · `Width`/`Height` |
| `Detail` | Viewport de detalle en la lámina | `Add` · `Projection` · `Scale` · `Lock` |
| `CopyViewportToDetail` | Traer un viewport de modelo como detalle | `Transfer` = `Copy` / `Move` |
| `ImportLayout` | Traer una lámina entera de otro `.3dm` | — |
| `Text` | Texto en el espacio de papel | `Height` en mm de layout · `Mask` · `Text Field` |
| `Dot` | Referencia numerada sobre el dibujo | se dibuja en espacio de pantalla (no cambia con el zoom) · *Secondary text* |
| `Leader` | Llamada con flecha y texto | pick de la cabeza → puntos → Enter → texto · `Landing` · *Text gap* |
| `Hatch` | Muestra de trama de la leyenda | en espacio de papel, patrón del material |
| `DocumentProperties > Annotation` | Estilos de anotación | `Enable layout space scaling` · `Model space scale` |
| `ImportAnnotationStyles` | Traer estilos de anotación de otro `.3dm` | — |
| `Print` | Salida a PDF | Rhino PDF · `Vector output` · `Print color` · `Match pattern definition` |
| `PrintDisplay` | Ver en la vista cómo se va a imprimir | colores y anchos de impresión en pantalla |
| `Print` → *Output color* | Blanco y negro | **Black and white** (convierte a gris) |
| `Print` → *Visibility* | Fondo blanco en la lámina | desmarcar *Background color* · *Clipping planes* |
| `SetView` | Vista estándar (world o PlanoC) | `World Top` · `World Bottom` · `World Left` · `World Right` · `World Front` · `World Back` |
| `Isometric` | Axonométrica **en paralelo** | **`SE`** (la nuestra) · `SW` · `NE` · `NW` · `ZoomExtents` |
| `NamedView` | Guardar y restaurar vistas | *Save as* · *Restore* · *Import from 3dm file* |
| `SetDisplayMode` | Modo de visualización | `Viewport` = `Active`/`All` · `Ctrl`+`Alt`+`S`/`R`/`W`/`G`/`X` |
| `SelClippingPlaneInViewport` | Ver qué planos cortan la vista actual | clave para el diagnóstico del corte |
| `Zoom` | Encuadre | `Extents` · `Dynamic` · `Selected` · `1To1` |
| `DisableClippingPlane` / `EnableClippingPlane` | Apagar / prender el corte en la vista | barra Display / Visibility |

### Navegación con el mouse (vista en perspectiva / isométrica)

| Quiero… | En la **isométrica** (perspectiva) | En una vista **paralela** (Top / Front / Right) |
|---|---|---|
| **Orbitar** (girar la vista) | arrastrar con el **botón derecho** | `Shift` + botón derecho (operación poco usada) |
| **Desplazar** (pan) | `Shift` + **botón derecho** | arrastrar con el **botón derecho** |
| **Zoom in / out** | `Ctrl` + **botón derecho** (zoom suave) o la **rueda** del mouse (zoom escalonado) | igual |
| **Menú contextual** | clic derecho sin arrastrar | igual |
| Ejecutar el comando activo | botón izquierdo | igual |

El **botón izquierdo** es siempre para el comando que esté corriendo; el derecho es navegación. El botón del medio se puede asignar a Popup menu / Popup this toolbar / Run this macro (Tools > Options > Mouse), donde también se cambian los roles Pan / Rotate / Zoom y sus modificadores (Shift, Ctrl, Alt) y el intercambio pan ↔ zoom.

Comandos sueltos de navegación: `Pan` (desplazar), `Zoom` (acercar/alejar), `RotateView` (girar el contenido de una vista de detalle).
| `Layout` + `Detail` | Hoja de impresión | escala 1:50, `Lock` |
| `Print` | PDF vectorial | `Rhino PDF`, `Vector output`, desmarcar `Clipping planes` |

---

## 13. Errores frecuentes (y su solución)

| Síntoma | Causa | Solución |
|---|---|---|
| Las curvas del PDF se ven muy gruesas | Bug de Rhino 8 con line weights | Importar con `Import line weights from PDF = OFF` |
| El corte no muestra relleno | La capa no tiene Section Style, o el objeto es malla | Asignar Section Style a la capa; trabajar con sólidos |
| **El corte no aparece en la isométrica** | El plano delimitador recorta solo las vistas donde está habilitado | Propiedades → "Vistas delimitadas" → tildar la isométrica; o `ActivarPlanoDelimitador` con la isométrica activa |
| El corte no aparece en ninguna vista | El rectángulo del widget quedó más chico que el modelo | Rehacerlo con `Vertical` y rectángulo ≥ la planta; **el widget en rojo avisa que no toca la geometría** |
| Se ve la mitad equivocada | El lado visible del plano está invertido | Propiedades → "Invertir dirección" |
| El corte se ve sin espesores | Profundidad ≠ 0 | Propiedades → "Profundidad" = `0` para sección fina |
| `ExtrudeCrv` no tapa los extremos | La curva no es cerrada o no es plana | `Polyline` con `Close = Yes` en el CPlane; si no, `PlanarSrf` + `ExtrudeSrf` |
| El `Sweep` sale retorcido | Secciones con distinta estructura o riel paralelo a la dirección fija | Copiar la misma sección; `Rebuild cross sections`; `Frame Style = Roadlike` |
| El sólido tiene caras invertidas | Normal mal orientado | `Flip` en la selección, o `BooleanDifference` con un cilindro grande |
| El perfil Z se deforma al barrer | Sección rotada respecto del riel | `Align cross sections = Yes` y `Refit cross sections` |
| La escala no cierra | Import sin calibrar | Medir la barra de 5 m con `Distance` y `Scale1D` |
| **El detalle sale con otra escala** | El número del prompt está en las unidades de ese espacio: con lámina en mm y modelo en m, 1:50 es **20** y **1** | `Scale` → `20` (on layout) → `1` (in model), o con unidades explícitas `20mm` y `1m`. Verificar: 1,00 m del modelo = 20,0 mm en el papel |
| El texto de las cotas **cambia de tamaño** al zoomear el detalle | "Enable layout space scaling" desactivado (el comando `Open` lo desactiva al abrir un DWG) | File > Properties > Annotation → activar **Enable layout space scaling** |
| Los textos de la lámina salen **chiquitos o gigantes** | La altura del texto está en unidades de layout, y el estilo de anotación trae su propio *Model space scale* | En el estilo, fijar la **Height** en mm de layout y activar *Enable model space scaling* con el *Model space scale* invertido a la escala de impresión |
| Se imprime **el widget del plano de corte** | La opción *Clipping planes* está activa en `Print` | `Print` → Visibility → desmarcar **Clipping planes** (y `Background color`, `Lights`) |
| El PDF sale **rasterizado** | `Raster output` seleccionado | `Print` → **Vector output** (el raster no guarda capas en PDF) |
| El patrón de línea sale con **otro grosor** en el papel | `Match viewport display` | `Print` → Linetype: **Match pattern definition**; y *Linetype units* = **Page lengths** |
| El corte **no aparece en el detalle** de la lámina | El plano no está habilitado en esa vista | *Views Clipped* → *Layout Space* → tildar el detalle; o `EnableClippingPlane` con el detalle activo |
| El corte sale como **un plano con espesor** | `Custom Depth` activado | Properties → **Depth** = `0` → sección fina |
| El corte sale **sin relleno** en el detalle | En el modo del detalle: *Use section styles* o *Show fills* apagados | *Options > View > Display Modes > [modo] > Objects > Clipping Planes* → activar ambos |
| Se ve **media casa**, como con **otro plano de corte** | Hay **dos** planos de corte activos en esa vista | `SelClippingPlaneInViewport` → `DisableClippingPlane` sobre el que sobra |
| El corte se ve **desde el lado equivocado** | Los triángulos del widget apuntan al lado visible | Properties → **Invert direction** |
| La vista **no se regenera** | Quedó el resultado anterior de la sección | §9.11: cambiar el modo de visualización · `Zoom Extents` · apagar y prender el plano |
| La **escala del detalle** no es la esperada | El número del prompt va en las unidades de ese espacio | Tabla §11.4: 1:50 = `20` (mm en la lámina) y `1` (m en el modelo) |
| En la lámina el corte sale **liso o gris** y en la pantalla se ve con trama | La trama se dibuja en el **espacio del modelo**: con `Pattern Scale` 1,0 mide 1 mm en el modelo → 0,03 mm en el papel a 1:30 | §9.15: `Pattern Scale` = (papel × escala) / base → **90** para 3 mm a 1:30 |
| La lámina sale **en color** y querías blanco y negro | `Print` → Output color | **Black and white** (convierte a escala de grises) |
| El detalle sale con **fondo gris** | El fondo del viewport lo define el modo de visualización | *Options > View > Display Modes > [modo] > Viewport > Background* → *Solid color* blanco, o `Print` → Visibility → desmarcar *Background color* |
| Los colores de la lámina **no son los de la capa** | En layout mandan el **Layout / Detail Print Color**, no el `Print Color` | Properties de la capa → *Layout / Detail Print Color* y *Layout / Detail Print Width* |

---

## 14. Bitácora de modelado — `3D-casa_uruguay_02.3dm`

> Registro vivo de la sesión del 27/10/2026. Cada paso lleva lo hecho, lo verificado y lo que falta. Los comandos citados están explicados en §1–§11 de esta misma guía.

### 14.1 Estado

| # | Paso | Estado | Resultado / falta |
|---|---|---|---|
| 1 | Importar `CAD-UY-xa-RHINO_02.dwg` (5,3 MB) | ✅ | Importado con `File > Import`; el DWG venía en **metros** → entra 1:1, sin conversión |
| 2 | Escala | ✅ | El usuario verificó que ya estaba escalado |
| 3 | Verificar qué entró | ⏳ | Falta `What` / `SelClosedPolysrf` / `SelMesh` / `Layer` |
| 4 | El plano de corte (`ClippingPlane`) | ✅ parcial | El plano ya está creado y los **Section Styles ya configurados**; falta verlo en la isométrica y alinearlo (ver §9.4) y sacar el 2D con `ExtractClippingSections` |
| 5 | Capas de material + Section Style | ✅ | Los Section Styles ya están configurados por el usuario en `3D-casa_uruguay_02.3dm` (ver §10) |
| 6 | La hoja: layout + viewport de detalle | ⏳ | En curso — ver §11 y §14.7 |
| 7 | Análisis del **layout de corte A** (falta la mitad del corte) | ✅ **resuelto 27/10** | `SelClippingPlaneInViewport` → "No objects added to selection" (ningún plano recorta esa vista). **Causa: el viewport quedó mal armado.** Solución del usuario: **re-armar el detalle** (`Detail` → `Add`) y volver a poner la escala |
| 8 | La escala del corte A | ✅ | **1:30** — 1 unidad de layout en mm = **0,03 m** del modelo (se escribe `1` y `0.03`, con punto decimal) |
| 9 | **Los hatch del corte no se ven en el detalle** (sí en la vista de trabajo) | ⏳ | En curso — ver §9.14: el detalle tiene su propio modo de visualización y ahí pueden estar apagados *Show fills* y *Use section styles* |

### 14.2 Paso 1 — Importar el DWG ✅

`File > Import` → `G:\Mi unidad\E#E.EDU\mora\CAD-UY-xa-RHINO_02.dwg` → botón **Options**.

**DWG/DXF Import Options** (valores oficiales de Rhino 8, ayuda `fileio/autocad_dwg_dxf_import_export.htm`):

| Opción | Valor | Por qué |
|---|---|---|
| `Convert regions to curves` | **ON** | Las regiones no importan: sin esta opción, un corte 2D guardado como región no entra |
| `Ignore thickness` | **ON** | El corte 2D llega con grosor de plumón; se lo queremos como línea |
| `Convert wide polylines to surfaces` | OFF | Con OFF, las polilíneas más angostas que la tolerancia entran como polilínea |
| `Import unreferenced layers` / `blocks` / `linetypes` | OFF | Solo capas con contenido |
| `Mesh precision` | `Automatic` | Rhino decide simple o doble precisión |
| `Model units` | **Model units** | El DWG entra al modelo (no a una lámina) |
| `Set layer material to layer color` | ON | Los colores de AutoCAD pasan a material: el 3D se lee antes de mapear capas |
| `Always use these settings` | **OFF** la primera vez | Así el diálogo vuelve a abrir si algo hay que corregir |

**Avisos del manual que aplican a este caso:** las capas apagadas o congeladas en AutoCAD **entran apagadas** en Rhino (hay que prendlas); los **hatches pueden correrse de posición**; el **paperspace entra como layout** (si el corte 2D está en paperspace, cae en una lámina, no en el modelo); **3DFace y polyface entran como malla**, no como NURBS; el formato de DWG más nuevo que Rhino 8 lee es **AutoCAD 2018**.

### 14.3 Paso 2 — Escala ✅

El DWG está en metros y el documento también → **entra 1:1**. Verificado por el usuario.

### 14.4 Paso 3 — Verificar qué entró ⏳

| Comando | Qué responde | Para qué decidir |
|---|---|---|
| `What` | Tipo de objeto, capa,closed/open | Saber si el 3D son sólidos, mallas o curvas |
| `SelClosedPolysrf` | Cantidad de sólidos cerrados | Si el corte se va a poder rellenar con hatch |
| `SelMesh` | Cantidad de mallas | Si hay mallas, el relleno por material sale limitado |
| `SelCurve` | Cantidad de curvas | Cuánto del corte 2D entró como trazado |
| `Layer` | Lista de capas con contenido | Punto de partida del mapeo a las 13 capas de material |
| `BoundingBox` | Caja del modelo | Saber el tamaño del rectángulo que necesita el widget del corte |

### 14.5 Paso 4 — El plano de corte ⏳

Receta completa en **§9**. Checklist de esta sesión:

> **Para revisar el corte en la isométrica** (mapping oficial de Rhino 8, ver §12): botón derecho = **orbitar** · `Shift` + botón derecho = **pan** · `Ctrl` + botón derecho = **zoom** · rueda = zoom escalonado. El botón izquierdo es siempre para el comando activo.

- [x] `ClippingPlane` creado (el usuario lo tiene en el archivo)
- [x] Section Styles configurados (ver §10)
- [ ] `Vertical` desde la vista **Plan**, con rectángulo ≥ la planta
- [ ] Widget **not red** (if red, the cut misses the geometry)
- [ ] Properties → **Name** `A-A` · **Depth** `0` · **Section Style** `By Layer`
- [ ] Properties → **Views Clipped** → tick the **isometric** (that is why the cut was not showing)
- [ ] `EnableClippingPlane` with the isometric active, if the tick does not do it
- [ ] **Invert direction** if the wrong half is visible
- [ ] `ViewClippingSections` → `SetView=Yes` for the view aligned with the cut
- [ ] `ExtractClippingSections` → `Curve=Yes`, `Hatch=Yes`, `Group=Yes` → the 2D cut

### 14.6 Paso 5 — Capas y Section Style ✅

Los **Section Styles ya están configurados** por el usuario en `3D-casa_uruguay_02.3dm` (27/10). El procedimiento queda documentado en **§10**: los tres niveles (plano / capa / objeto), los campos del diálogo (Hatch y Boundary), el paso a paso por capa, la tabla de los 13 materiales y cómo llevarlos de un archivo a otro con `LayerStateManager`.

Recordatorio del manual: el Section Style **no viaja con el import de un DWG** — es propiedad del documento, así que en cada archivo hay que configurarlo.

### 14.7 Paso 6 — La hoja y el viewport de detalle ⏳

En curso. Receta completa en **§11**. Configuración de referencia (la de la hoja AIZ, verificada):

| Elemento | Configuración | Nota |
|---|---|---|
| Lámina | A3 landscape 420 × 297 mm | `Layout` → Name `UY-CORTE-A` |
| Viewport | un solo detalle con el corte | `Detail` → `Add` → `Projection` → `Scale` → `Lock` |
| Escala | **1:50** → `20` (on layout, mm) y `1` (in model, m) | se verifica con `Distance`: 1,00 m del modelo = 20,0 mm en el papel |
| Display mode | Shaded (axonometría 30/60 en paralelo) | el mismo criterio que en AIZ |
| Clipping plane | `A-A` habilitado **dentro del detalle** | *Views Clipped* → *Layout Space* |
| Texto | estilo de anotación con altura en mm de layout | activar **Enable layout space scaling** (el import de DWG lo desactiva) |

Checklist:

- [ ] `Layout` nuevo A3 landscape 420 × 297 mm
- [ ] Bordes / cajetín
- [ ] `Detail` → `Add` → rectángulo → `Projection` → `Scale` (`20` / `1`) → `Lock`
- [ ] Verificación de escala: 1,00 m del modelo = 20,0 mm en el papel
- [ ] Clipping plane habilitado en el detalle
- [ ] Texto de papel con el estilo de anotación correcto
- [ ] `Print` → Rhino PDF · Vector output · Print color · sin `Clipping planes`

### 14.8 Paso 7 — El layout de corte A: diagnóstico y resolución ✅

**Síntoma inicial:** en el layout de corte A no se ve la mitad del corte; como si hubiera **otro plano de corte** o como si la vista **no se regenerara**.

**Resultado de las pruebas (27/10):** `SelClippingPlaneInViewport` → **"No objects added to selection"** → ningún plano recorta esa vista. La batería de 3 pruebas quedó documentada en **§9.13**.

**Resolución:** el viewport estaba mal armado. El usuario **lo re-armó** y quedó:

| Paso | Qué se hizo | Resultado |
|---|---|---|
| 1 | **Nuevo detalle**: `Detail` → `Add` → dibujar el rectángulo | el detalle se rehace desde cero (sin el estado heredado) |
| 2 | `Scale` → `1` (on layout, mm) → `0.03` (in model, m) | **escala 1:30** |
| 3 | `Projection` + `Lock` + *Title* | el detalle queda fijo y con su nombre |
| 4 | Propiedades del clipping plane → *Views Clipped* → *Layout Space* → tildar el detalle | el corte aparece en la lámina |

**La escala del corte A: 1:30** — 1 unidad de layout en milímetros equivale a **0,03 m** del modelo (30 mm). En el prompt se escribe `1` y `0.03`, **con punto decimal**. Equivalencias: 1 mm de papel = 30 mm de modelo · 1 m del modelo mide **33,3 mm** en la hoja · el detalle de 400 × 270 mm cubre **12 × 8,1 m** de modelo.

> **Control de encuadre:** a 1:30 el detalle muestra 12 × 8,1 m. Si el corte A tiene que abarcar la casa completa (≈14 m de largo), no alcanza con 400 mm de papel: habría que pasar a **1:40** (16 × 10,8 m, entra justa) o **1:50** (20 × 13,5 m, entra con aire). Si el corte A es de una parte de la casa, el 1:30 es el correcto y más legible.

**Lo que se aplica en este proyecto:**

- La axonométrica 30/60 de AIZ (`axo3060`) **no es una vista estándar**: es una vista guardada → se trae con `NamedView` → *Import from 3dm file* sobre `set-ej_corte_A3-1-50.3dm`, o se replica con `CopyViewportToDetail`. (Ojo: `Projection` del detalle **no** tiene 30/60.)
- Vistas de trabajo: `Isometric SE` (paralela, desde el cuadrante sureste) + `SetView World Top` / `World Bottom` / `World Left` para las ortogonales.
- El modo de visualización del detalle: **Shaded** (o **Technical** para revisar el corte con sus aristas punteadas).

**Pendiente abierto:** el corte se ve **sin hatch en el detalle** (sí se ve en la vista de trabajo) → §9.14.

### 14.9 Paso 8 — Vista nueva con la madera cortada y los materiales con hatch ⏳

**Decisiones del usuario (27/10):** una **lámina nueva aparte** (el corte A queda intacto) · las **13 capas de material** con patrón · **el agente no guarda el documento**.

**Causa raíz hallada (27/10):** no era el `Pattern Scale` del Section Style sino el ajuste **"Enable hatch scaling"** de *File > Properties > Hatch*, que Rhino 8 documenta así:

> **Enabled** → "Hatch patterns in model viewports are scaled by the **Model space hatch scale** value" · **"Hatch patterns in detail views print with the same scale regardless of the zoom factor"**.
> **Disabled** → "Hatch patterns will not scale."

Con el escalado apagado, la trama se dibuja en el espacio del modelo → a 1:30 mide 0,03 mm en el papel → **invisible en la lámina pero visible en la vista de trabajo** (que se navega con zoom). §9.15 quedó reescrito con el mecanismo correcto.

**Dos hallazgos técnicos que habilitan el trabajo por script:**

1. **`SetScale` está "roto" en Rhino 8** → hace falta la secuencia de 5 pasos con `CommitChanges` (publicada por Dale Fugier, McNeel, 2024) → §11.12.
2. **API de Section Styles de Rhino 8** verificada con un probe: `capa.SetCustomSectionStyle(SectionStyle())` con los 14 miembros escribibles, `plano.Attributes.AddClipViewport(id)` para habilitar el corte en una vista, y `doc.ModelSpaceHatchScalingEnabled` / `doc.ModelSpaceHatchScale` para la escala de tramas → §10.9.

**Lo que se va a hacer (Fases 1–3 del plan):**

| Fase | Qué | Script |
|---|---|---|
| 1 | Inspección de solo lectura: `ModelSpaceHatchScalingEnabled`, Section Styles de las 13 capas, tipo de los objetos de madera (sólido cerrado o malla), display modes, estado del clipping plane | `scripts/inspeccionar-seccion-rhino.py` |
| 2 | `ModelSpaceHatchScalingEnabled = True` + `ModelSpaceHatchScale` + los 13 Section Styles (patrón, rotación, escala, colores de trama y borde) | `scripts/configurar-corte-hatch-rhino.py` |
| 3 | Lámina `UY-CORTE-HATCH` (A3) + detalle `A-A-HATCH` a 1:30, cámara copiada del detalle existente, clipping plane habilitado en el detalle nuevo, `doc.Views.Redraw()` | ídem |

**Bloqueo actual:** el **puente MCP está caído** (puerto 9876 sin listener; el log del puente termina el 26/10 08:36) → hace falta que el usuario corra en la línea de comandos de Rhino:

```
_RunPythonScript "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\rhino-mcp-server-rhino.py"
```

**Riesgo abierto:** si la madera del DWG entró como **malla** o superficie abierta, **no hay sección que rellenar** (el manual: la sección se rellena solo si es **cerrada**) → la Fase 1 lo define y ahí hay que decidir (convertir con `MeshToNurbs` o trabajar el corte como contorno).

**Hallazgo del 27/10 — el corte fantasma (un solo plano, pero se ven dos):**

El usuario tiene **un solo** clipping plane, pero en el corte A se ve **como si fueran dos**. El plano anterior fue borrado y su corte sigue apareciendo. La causa documentada:

> *Tools > Options > View* → **Named views set clipping planes**: "Restoring a named view also restores the **enable state** of the clipping planes saved with the view."

Es decir: **las Named views guardan el estado de recorte**. Si la vista guardada se creó con el plano viejo activo, al restaurarla vuelve el corte de ese plano — y borrar el plano no lo saca de la vista guardada.

**Prueba 1 · ¿En qué vista estabas?** — el 27/10/2026 el usuario corrió `SelClippingPlaneInViewport` y la respuesta fue **"No objects added to selection"** → **ningún plano recorta esa vista**. Quedan tres hipótesis, y las pruebas las separan (§9.13):

| # | Hipótesis | Prueba | Resultado esperado |
|---|---|---|---|
| 1 | El comando se corrió en una vista que **no es la del corte** (o el plano recorta el modelo pero **no el detalle**) | doble clic en el **detalle del corte A** para activarlo → `SelClippingPlaneInViewport`; después en la isométrica | *No objects* en el detalle → tildar el detalle en *Views Clipped* → *Layout Space* |
| 2 | Es un **redibujado viejo** (la vista quedó pintada con la sección del plano borrado) | `Zoom` → `Extents` en esa vista | si el fantasma desaparece → es eso: re-crear la vista guardada y revisar *Named views set clipping planes* |
| 3 | Es **geometría real**: el corte 2D del DWG entró como **superficies** (opción `Convert wide polylines to surfaces`) y se ve como un plano de corte | ventana de selección sobre la zona → `What` (tipo y capa) → apagar esa capa | si al apagar la capa desaparece → mover esa geometría a `REF-2D` o borrar, y reimportar con la opción **OFF** |

**El texto de la hoja** quedó documentado en §11.13: `Text` en papel para los datos de la lámina (título del corte 5 mm, escala 3 mm, notas 3 mm, leyenda 2,5 mm), `Dot` para las referencias numeradas (se dibujan en espacio de pantalla: no cambian con el zoom) y `Leader` para las llamadas con flecha. La regla de tamaño: **con "Enable layout space scaling" activado** el texto dentro del detalle imprime a su tamaño nominal; sin eso, a 1:50 un texto de 3 mm en el papel necesita **150 mm** en el modelo.

---

## 15. Referencias (Rhino 8)

- *ExtrudeCrv*: https://docs.mcneel.com/rhino/8/help/en-us/commands/extrudecrv.htm
- *Sweep1*: https://docs.mcneel.com/rhino/8/help/en-us/commands/sweep1.htm
- *Box*: https://docs.mcneel.com/rhino/8/help/en-us/commands/box.htm
- *PushPull*: https://docs.mcneel.com/rhino/8/help/en-us/commands/pushpull.htm
- *MoveFace*: https://docs.mcneel.com/rhino/8/help/en-us/commands/moveface.htm
- *Offset*: https://docs.mcneel.com/rhino/8/help/en-us/commands/offset.htm
- *PlanarSrf*: https://docs.mcneel.com/rhino/8/help/en-us/commands/planarsrf.htm
- *Cap*: https://docs.mcneel.com/rhino/8/help/en-us/commands/cap.htm
- *Gumball*: https://docs.mcneel.com/rhino/8/help/en-us/commands/gumball.htm
- *Polyline*: https://docs.mcneel.com/rhino/8/help/en-us/commands/polyline.htm
- *Line*: https://docs.mcneel.com/rhino/8/help/en-us/commands/line.htm
- *Import/Export PDF*: https://docs.mcneel.com/rhino/8/help/en-us/fileio/portable_document_format_pdf_import_export.htm

**Corte 3D y Section Styles — ayuda oficial (verificada 200 el 2026-10-27):**

- *ClippingPlane (PlanoDelimitador)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/clippingplane.htm · [es](https://docs.mcneel.com/rhino/8/help/es-es/commands/clippingplane.htm)
- *CutPlane (PlanoDeCorte)*: https://docs.mcneel.com/rhino/8/help/es-es/commands/cutplane.htm
- *Section (Sección)*: https://docs.mcneel.com/rhino/8/help/es-es/commands/section.htm
- *ClippingSections (SeccionesDeCorte)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/clippingsections.htm
- *ViewClippingSections (VerSeccionesDeCorte)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/viewclippingsections.htm
- *ExtractClippingSections (ExtraerSeccionesDeCorte)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/extractclippingsections.htm
- *ExtractClippingSlices (ExtraerSegmentosDeCorte)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/extractclippingslices.htm
- *ClippingDrawings (DibujosDeCorte)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/clippingdrawings.htm
- *NestedClippingDrawing (DibujoDeCorteAnidado)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/nestedclippingdrawing.htm
- *Section Style (diálogo)*: https://docs.mcneel.com/rhino/8/help/en-us/popup_moreinformation/sectionstyle.htm
- *Layer (propiedad Section Style)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/layer.htm
- *Object properties (Section Style del objeto)*: https://docs.mcneel.com/rhino/8/help/en-us/properties/object.htm
- *LayerStateManager (Layer States)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/layerstatemanager.htm
- *Mouse options (navegación y botón del medio)*: https://docs.mcneel.com/rhino/8/help/en-us/options/mouse.htm
- *User's Guide — Navigation & Display*: https://www.rhino3d.com/docs/guides/user-guide/navigation-display/
- *Barra Secciones*: https://docs.mcneel.com/rhino/8/help/es-es/toolbarmap/sections_toolbar.htm
- *User's Guide — Intro to Section Styles*: https://www.rhino3d.com/docs/guides/drafting/clipping-sectioning/intro-to-section-styles/
- *Import/Export DWG (opciones de importación)*: https://docs.mcneel.com/rhino/8/help/en-us/fileio/autocad_dwg_dxf_import_export.htm
- *Detail (viewport de la hoja)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/detail.htm
- *Layout (lámina)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/layout.htm
- *LayoutProperties (editar la lámina)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/layoutproperties.htm
- *ImportLayout (traer una lámina de otro 3dm)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/importlayout.htm
- *CopyViewportToDetail (traer un viewport de modelo como detalle)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/copyviewporttodetail.htm
- *SelDetail*: https://docs.mcneel.com/rhino/8/help/en-us/commands/seldetail.htm
- *RotateView / TiltView (girar el contenido de un detalle)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/rotateview.htm · https://docs.mcneel.com/rhino/8/help/en-us/commands/tiltview.htm
- *Text (texto en papel)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/text.htm
- *Annotation properties (estilos de anotación)*: https://docs.mcneel.com/rhino/8/help/en-us/documentproperties/annotation.htm
- *ImportAnnotationStyles*: https://docs.mcneel.com/rhino/8/help/en-us/commands/importannotationstyles.htm
- *Print (imprimir la lámina)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/print.htm
- *PrintDisplay*: https://docs.mcneel.com/rhino/8/help/en-us/commands/printdisplay.htm
- *SetView (vistas estándar)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/setview.htm
- *Isometric (NE / NW / SE / SW)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/isometric.htm
- *Set View (barra de herramientas)*: https://docs.mcneel.com/rhino/8/help/en-us/toolbarmap/set_view_toolbar.htm
- *NamedView*: https://docs.mcneel.com/rhino/8/help/en-us/commands/namedview.htm
- *SetDisplayMode*: https://docs.mcneel.com/rhino/8/help/en-us/options/view_displaymode_options.htm
- *Display modes (opciones de cada modo)*: https://docs.mcneel.com/rhino/8/help/en-us/options/view_displaymode_options.htm
- *Clipping Planes dentro de un modo visual*: https://docs.mcneel.com/rhino/8/help/en-us/options/view_display_mode_clippingplanes.htm
- *SelClippingPlaneInViewport*: https://docs.mcneel.com/rhino/8/help/en-us/commands/selclippingplaneinviewport.htm
- *Zoom*: https://docs.mcneel.com/rhino/8/help/en-us/commands/zoom.htm
- *View options (Named views set clipping planes)*: https://docs.mcneel.com/rhino/8/help/en-us/options/view.htm
- *Dot (referencia numerada)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/dot.htm
- *Leader (llamada con flecha)*: https://docs.mcneel.com/rhino/8/help/en-us/commands/leader.htm
- *Text fields*: https://docs.mcneel.com/rhino/8/help/en-us/information/text_fields.htm
- *Hatch*: https://docs.mcneel.com/rhino/8/help/en-us/commands/hatch.htm

> URLs verificadas 200 el 2026-10-27. Producto y protocolo de cortes: [[proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/00-index|00-index]] y [[proyectos/MVP_05-rhino-mcp/01-AIZ/01-playbook-cortes-rhino-8|01-playbook-cortes-rhino-8]].
