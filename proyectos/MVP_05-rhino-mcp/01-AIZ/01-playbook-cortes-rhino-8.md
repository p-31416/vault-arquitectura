---
tipo: playbook
mvp: 05
version: 2.0.0
fecha_creacion: 2026-10-25
ultima_actualizacion: 2026-10-25
tags: [mvp_05, rhino8, aiz, cortes, clippingplane, sectionstyle, hatch, axonometria, layout, a3, escala, planilla]
idioma: es
---

# Playbook Rhino 8 — cortes, hatch y hoja A3 (caso AIZ)

> Documento único del trabajo con Rhino 8 en el MVP_05. Reúne en un mismo lugar el protocolo de preparación desde AutoCAD, el manual de corte 3D con hatch por material y el plan de la hoja de impresión A3 a escala 1:50, con el **resultado verificado** del 2026-10-25.
>
> Operación del puente MCP (cómo se le habla a Rhino desde el asistente): [[proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp|pbook-rhino-mcp]].
> Ficha del experimento: [[proyectos/MVP_05-rhino-mcp/01-AIZ/00-index|00-index]].

---

## 0. Cómo usar este documento

| Parte | Qué resuelve | Estado |
|---|---|---|
| **1–3** | El caso, la pregunta central y el estado real del archivo | Documentado y medido |
| **4** | De AutoCAD a Rhino: limpiar el DWG, importar, mapear capas | Procedimiento (pendiente de ejecutar en el DWG de AIZ) |
| **5** | El corte 3D: plano de corte, orientación, hatch por material, profundidad, axonometría | Procedimiento + estado parcial ejecutado |
| **6** | La hoja de impresión A3 a 1:50 con pie de hoja | **Ejecutado y verificado** |

Los ítems de la parte 6 que ya se ejecutaron llevan la marca ✅ y su criterio de aceptación cumplido.

---

## 1. El caso AIZ

### 1.1 Pregunta central

**¿un modelo 3D hecho en AutoCAD sirve para producir cortes en Rhino, o conviene remodelar?**

El caso AIZ es un referente: el 3D nace de un PDF vectorizado, se modela a mano en AutoCAD y hoy se pasa a Rhino como planta 2D. Acá se prueba el paso siguiente: usar ese 3D para cortar.

### 1.2 Alcance

- Importar el DWG 3D de AIZ en Rhino.
- Producir un corte general a 1:50 y un corte-detalle a 1:10 o 1:20.
- Comparar el resultado con el mismo corte hecho en AutoCAD.
- Medir ventajas, fricciones y tiempos.

**Fuera de alcance:** modelado completo de la casa, renders, instalaciones, cálculo estructural y lámina final de entrega.

### 1.3 Material de partida

| Insumo | Formato | Ubicación |
|---|---|---|
| Modelo AIZ en AutoCAD | `.dwg` 3D | `activos/mvp_05-rhino-mcp/01-AIZ/` |
| Modelo de trabajo | `.3dm` | `activos/mvp_05-rhino-mcp/01-AIZ/set-ej_corte.3dm` |
| PDF vectorizado de origen | `.pdf` | `activos/mvp_05-rhino-mcp/01-AIZ/` |
| Plantas 2D de referencia | `.dwg` / `.pdf` | `activos/mvp_05-rhino-mcp/01-AIZ/` |

> Los binarios viven en `activos/` (gitignored). En el vault solo se referencian por ruta.

### 1.4 Hipótesis

1. **Sí, si el DWG tiene sólidos 3D cerrados.** Rhino importa los sólidos ACIS de AutoCAD como polysuperficies cerradas y puede cortarlos con `ClippingPlane`, `ClippingSections` y `Make2D`.
2. **El corte general 1:50 sale rápido.** A esa escala, un modelo de masa con espesores de conjunto alcanza para leer espacios, alturas y encuentros.
3. **El corte constructivo 1:10 exige capas separadas.** Si el modelo de AutoCAD es un sólido único por muro, el hatch por material se resuelve partiendo el sólido o remodelando un testigo en Rhino.
4. **La ventaja grande de Rhino está en la sección dinámica y en la lámina.** `Section Style` por capa, `Make2D` con líneas ocultas y `Layout` con detalles a distinta escala en una sola hoja.

### 1.5 Criterio de decisión (go / partial / no-go)

| Resultado | Condición | Decisión |
|---|---|---|
| **GO** | ≥80 % del área del corte proviene de sólidos cerrados; los hatches funcionan; la limpieza lleva ≤30 min | Usar el DWG de AutoCAD como base y cortar en Rhino |
| **PARTIAL** | El modelo sirve como masa, pero las capas no están separadas | Usar AutoCAD para 1:50 y modelar el testigo 1:10 en Rhino |
| **NO-GO** | El DWG trae mallas o superficies abiertas; el corte no cierra | Remodelar en Rhino desde el PDF vectorizado |

### 1.6 Rhino vs AutoCAD para cortes

| Criterio | AutoCAD | Rhino 8 | Lectura |
|---|---|---|---|
| Corte dinámico | `SECTIONPLANE` | `ClippingPlane` + `ClippingSections` | Ambos; Rhino suma estilos |
| Hatch por material | Manual, después de generar la sección | `Section Style` por capa u objeto | **Rhino** |
| Líneas ocultas | `FLATSHOT` | `Make2D` | **Rhino** |
| Varios detalles a escalas distintas | Layouts con viewports | `Layout` + `Detail` | **Rhino** |
| Edición del modelo | Sólidos ACIS nativos | Breps importados | Empate |
| Precisión y booleanas | Sólidos ACIS | NURBS y polysuperficies | **Rhino** |
| Dibujo 2D puro | Nativo y rápido | Correcto, con más pasos | **AutoCAD** |
| Interoperabilidad | DWG nativo | Importa y exporta DWG | **AutoCAD** |
| Curva de aprendizaje | Conocida por el estudio | Nueva | **AutoCAD** |
| PDF vectorial | `EXPORTPDF` / `PLOT` | `Print` → Rhino PDF | Empate |

**Conclusión provisoria:** AutoCAD sigue siendo el lugar del modelo 3D base y del dibujo 2D; Rhino aporta el corte dinámico, el hatch por material y la lámina.

### 1.7 Entregables y riesgos

| # | Entregable | Formato | Criterio |
|---|---|---|---|
| 1 | DWG limpio de AIZ | `.dwg` | Sin xrefs sueltas, unidades verificadas |
| 2 | Modelo importado | `.3dm` | Sólidos cerrados, capas mapeadas |
| 3 | Corte general A-A | En lámina | 1:50, legible |
| 4 | Corte-detalle D-1 | En lámina | 1:10 o 1:20, con hatch por material |
| 5 | Lámina de prueba | `.pdf` A3 | Vectorial, rótulo mínimo |
| 6 | Planilla comparativa | En este documento | Tiempos, fricciones, veredicto |

| Riesgo | Mitigación |
|---|---|
| El DWG trae mallas en lugar de sólidos | Verificar con `SelMesh` y `What` antes de cortar |
| El modelo está en milímetros | Verificar con `Units` y `Distance` contra una cota conocida |
| Un solo sólido por muro | Partir con `BooleanSplit` o modelar el testigo en Rhino |
| Xrefs sin bindear | `XREF` → Bind, o `WBLOCK` del área |
| El hatch no aparece | Cada capa debe ser un sólido cerrado y tener `Section Style` asignado |
| El PDF sale con escala incorrecta | Medir una cota de 1,00 m impresa en el PDF |

---

## 2. Estado verificado del archivo (medido por MCP, 2026-10-25)

### 2.1 Documento

| Dato | Valor |
|---|---|
| Archivo | `set-ej_corte.3dm` |
| Rutas | `G:\Mi unidad\E#E.EDU\mora\set-ej_corte.3dm` (Drive) y copia en `activos/` |
| Unidades | metros |
| Objetos | 161 → **159 mallas** (158 cerradas + 1 abierta) + 1 plano de corte |
| Sólidos ACIS | ninguno: la geometría es mesh |
| Layouts | 1 → `AIZ-CORTE-A` (A3, ver parte 6) |

### 2.2 Capas con contenido y su section style

| Capa | Objetos | Section style | Patrón / color / rotación / escala |
|---|---|---|---|
| `3D-EP-MAD` | 84 | no | — |
| `3D-MURÒ` | 45 | sí | sólido (0), gris 105,105,105, 0°, esc 1,0 |
| `3D-REV-01` | 15 | no (contiene la única malla abierta, `Object_3`) | — |
| `3D-LOSA` | 8 | sí | patrón 1, blanco, 45°, esc 0,5 |
| `3D-VIDRIO` | 5 | sí | patrón 3, rojo, 45°, esc 0,05 |
| `3D-SOL-EXT01` | 1 | no | — |
| `3D-BASE` | 1 | no | — |
| `Default` | 1 | — | contiene el plano de corte `A-A` |
| `Layer 01`–`Layer 05` | 0 | — | vacías, disponibles para organización |
| `AIZ-ROTULOS` | 2 | — | rótulos de la hoja (parte 6) |

### 2.3 Plano de corte

| Propiedad | Valor | Lectura |
|---|---|---|
| Nombre | `A-A` | en capa `Default` |
| Geometría | `Origin=(575, −60, 14)`, `XAxis=(0,0,1)`, `YAxis=(0,−1,0)`, `ZAxis=(1,0,0)` | plano vertical en **X = 575**, normal +X |
| `PlaneDepthEnabled` | False | el corte es "thin": la profundidad se abre en la parte 5.4 |
| `PlaneDepth` | 1,0 m | valor preparado |

### 2.4 Extensión del modelo

| Eje | Mínimo | Máximo | Largo |
|---|---|---|---|
| X | 568,80 | 579,17 | 10,37 m |
| Y | −75,88 | −53,88 | 22,00 m |
| Z | −4,07 | 14,07 | 18,15 m |

El corte en X = 575 deja **4,17 m** de set del lado +X (el que queda visible) y 6,19 m del lado −X.

### 2.5 Viewports

| Viewport | Proyección | Modo | Cámara |
|---|---|---|---|
| `axo3060` | **Paralela** | Shaded | dir (0,743 · 0,577 · −0,339) → axonometría 30/60 |
| `Top` | Paralela | — | dir (0,0,−100) |
| `Front` | Paralela | — | dir (0,100,0) |
| `Right` | Paralela | — | dir (−100,0,0) |

`axo3060` es la vista de trabajo: axonometría 30/60 con el corte A–A activo y el relleno por capa visible.

---

## 3. Parte A — De AutoCAD a Rhino

### 3.1 Preparar el DWG en AutoCAD

| Paso | Comando | Qué verificar |
|---|---|---|
| 1.1 | `AUDIT` → `Y` | Errores corregidos |
| 1.2 | `PURGE` → `All` | Capas, bloques y estilos vacíos fuera |
| 1.3 | `XREF` → Bind | Sin referencias externas sueltas |
| 1.4 | `INSUNITS` | Unidad correcta (mm o m) |
| 1.5 | `MASSPROP` sobre un muro | Devuelve volumen: es un sólido 3D |
| 1.6 | `PROPERTIES` | Dice "3D Solid", no "Mesh" |
| 1.7 | `SAVEAS` → DWG 2018 | Copia limpia y compatible |

**Señales de alarma**

- `PROPERTIES` dice **Mesh** → Rhino importará una malla; el corte será menos limpio.
- `MASSPROP` falla → el objeto es una superficie abierta.
- Todo está en una sola capa → el hatch por material va a requerir trabajo extra.
- Las plantas están superpuestas en Z=0 → separar por nivel antes de cortar.

### 3.2 Importar a Rhino

| Paso | Comando | Qué verificar |
|---|---|---|
| 2.1 | `New` → template en metros | Unidades del documento |
| 2.2 | `Import` → DWG/DXF | Opción de importar como bloques o geometría |
| 2.3 | `Units` | Metros, tolerancia 0,001 |
| 2.4 | `Distance` contra una cota conocida | Escala correcta |
| 2.5 | `SelClosedPolysrf` | Cantidad de sólidos cerrados |
| 2.6 | `SelMesh` | Si hay mallas, anotar cuántas |
| 2.7 | `What` sobre un muro | Tipo de objeto importado |
| 2.8 | `Layer` | Mapear capas de AutoCAD a capas Rhino |

### 3.3 Mapeo de capas propuesto

| Capa AutoCAD | Capa Rhino | Uso |
|---|---|---|
| Muros / Walls | `AIZ-MUROS` | Sólidos de muro |
| Losas / Floors | `AIZ-LOSAS` | Entrepisos |
| Cubierta / Roof | `AIZ-CUBIERTA` | Faldones |
| Aberturas / Openings | `AIZ-ABERTURAS` | Vanos y marcos |
| Mobiliario | `AIZ-MOBILIARIO` | Referencia |
| Ejes | `AIZ-EJES` | Ejes y niveles |
| Base 2D | `AIZ-CAD-BASE` | Planta de referencia, bloqueada |

### 3.4 El mismo corte en AutoCAD (comparación)

| Paso | Comando | Qué obtiene |
|---|---|---|
| 4.1 | `SECTIONPLANE` | Sección viva para revisar |
| 4.2 | `SECTIONPLANE` → Generate section | Sección 2D o 3D |
| 4.3 | `SECTION` | Región de intersección |
| 4.4 | `FLATSHOT` | Dibujo 2D con líneas ocultas |
| 4.5 | `HATCH` | Relleno manual por material |
| 4.6 | `LAYOUT` + `PLOT` | Lámina PDF |

Anotar: tiempo total, cantidad de hatches manuales, correcciones de línea y calidad de la lámina.

---

## 4. Parte B — El corte 3D

### 4.1 Validar el plano de corte

| Verificación | Comando | Qué mirar |
|---|---|---|
| El plano existe y está activo | `SelClippingPlaneInViewport` | Selecciona el plano que corta la vista activa |
| Tipo de objeto | `What` | Dice `Clipping plane` y muestra su plano |
| Dirección del corte | `Dir` sobre la superficie del plano | Normal del plano; los triángulos del widget apuntan al lado visible |
| El corte atraviesa el modelo | `BoundingBox` del plano vs. del modelo | El rectángulo del plano supera el ancho del modelo |
| El corte es perpendicular al muro | Vista `Top` + `Distance` | La línea de corte coincide con el eje A-A |

**Regla práctica:** si en `Top` el plano se ve como una línea recta sobre el eje y el corte muestra espesores parejos, está bien orientado. Si se ve como un paralelogramo, quedó inclinado.

### 4.2 Orientar el `ClippingPlane`

`Rotate` sirve para corregir, pero para dejarlo exacto conviene crear el plano con la opción correcta.

| Opción al crear | Cuándo usarla | Cómo |
|---|---|---|
| **Vertical** | Corte recto sobre un eje, perpendicular al CPlane | `ClippingPlane` → `Vertical` → dos puntos sobre la línea de corte en `Top` |
| **3Point** | Corte diagonal o sobre un plano inclinado | `ClippingPlane` → `3Point` → esquina, esquina adyacente y punto opuesto |
| **EdgeMidpoint** | Plano centrado en un borde conocido | `ClippingPlane` → `EdgeMidpoint` → tres puntos |
| **Center** | Plano centrado en un punto | `ClippingPlane` → `Center` → centro y esquina |
| **AroundCurve** | Corte perpendicular a una curva (ejes curvos) | `ClippingPlane` → `AroundCurve` → curva y centro |
| **Default** | Ajuste libre en perspectiva | Dos esquinas opuestas |

**Opciones de `ClippingSections` (Rhino 8)** — crean varios planos de sección de una vez y los guardan como vistas:

| Opción | Resultado |
|---|---|
| `Dir=CPlane` | Sección paralela al CPlane actual |
| `Dir=X` | Sección vertical, paralela al eje X del CPlane |
| `Dir=Y` | Sección vertical, paralela al eje Y del CPlane |
| `Dir=Custom` | Sección vertical en la dirección de dos puntos |
| `Depth` | Espesor visible; `0` deja un corte fino |
| `Name` | Prefijo de las secciones (`SEC_01`, `SEC_02`…) |
| `SaveToNamedView=Yes` | Guarda la vista de cada sección |
| `Flip` | Invierte el lado visible |

**Corregir un plano ya rotado**

1. Activar `Top` y dibujar una `Line` sobre el eje definitivo del corte.
2. Seleccionar el `ClippingPlane`.
3. `Rotate` → primer punto y segundo punto sobre la línea → ángulo `0` para alinear, o el necesario.
4. Verificar con `Dir` que la normal queda horizontal y perpendicular al eje.
5. Si quedó al revés, `ClippingPlaneProperties` → `Flip Direction`.

> **Atajo:** borrar el plano y recrearlo con `Vertical` suele ser más rápido que corregir dos rotaciones.

**Alinear la vista al plano**

- `ViewClippingSections` → seleccionar plano → `SetView=Yes` → `SetCPlane=Yes`: deja la vista mirando el corte de frente.
- `SaveClippingSectionViews`: guarda esa vista en Named Views.
- `SaveClippingSectionCPlanes`: guarda el CPlane alineado al plano.
- `ClippingPlaneProperties` → `Views Clipped`: elige en qué viewports y detalles corta.

### 4.3 Hatch por material

El relleno de sección sale de **Section Style**, no de un `Hatch` 2D dibujado a mano. Hay tres niveles:

| Nivel | Dónde | Uso |
|---|---|---|
| **Capa** | Propiedades de capa → Section Style | Estrategia principal: una capa por material |
| **Objeto** | Propiedades del objeto → Section Style | Excepción puntual |
| **Clipping plane** | Propiedades del plano → Section Style | Cuando el plano define el estilo de todo lo que corta |

**Jerarquía**

1. Objeto con `Section Style = Custom` → manda el objeto.
2. Objeto con `By Clipping Plane` → manda el plano.
3. Objeto con `By Layer` → manda la capa.
4. Capa en `None` → el corte sale sin relleno.

> La combinación más estable para un corte constructivo es **capas por material + plano en `By Layer`**: el hatch viaja con la geometría y se mantiene al mover el corte.

**Capas sugeridas para una casa de madera**

| Capa | Material | Patrón sugerido | Color | Escala orientativa |
|---|---|---|---|---|
| `MAT-MADERA` | Pino, MLC, entramado | Líneas paralelas 45° | Ocre claro | 0,5–1 |
| `MAT-OSB` | Tablero OSB | Hexágono o líneas cruzadas | Amarillo pálido | 0,5–1 |
| `MAT-AISLACION` | Lana mineral | Zigzag u ondas | Amarillo claro | 1–2 |
| `MAT-MEMBRANA` | Hidrófuga / barrera | Sólido | Gris oscuro | — |
| `MAT-HORMIGON` | Platea, bases | Puntos / áridos | Gris medio | 1–2 |
| `MAT-YESO` | Placa de yeso | Sólido | Blanco grisáceo | — |
| `MAT-ACERO` | Conectores, refuerzos | Sólido o líneas densas | Negro | — |
| `MAT-TIERRA` | Relleno, terreno | Puntos dispersos | Marrón | 2–4 |

> Los nombres exactos de patrón dependen de la lista cargada en Rhino. Si el patrón buscado no aparece, se carga un `.pat` compatible o se crea uno propio con `Hatch` → `Pattern`.

**Pasos**

1. `Layer` → crear una capa por material.
2. Seleccionar los sólidos del modelo y asignarlos con `ChangeLayer`.
3. En cada capa, abrir Section Style y elegir patrón, color, rotación y escala.
4. Seleccionar el `ClippingPlane` → Propiedades → `Section Style = By Layer`.
5. Activar `Shaded` o `Rendered` para que el relleno se vea; en `Wireframe` el hatch queda oculto.
6. Ajustar `Pattern Scale`: si el hatch se ve como una mancha, subir la escala; si desaparece, bajarla.
7. Revisar el corte en `Top` y en la vista alineada.

**Propuesta de relleno para las capas de AIZ**

| Capa | Patrón | Color | Rotación | Escala |
|---|---|---|---|---|
| `3D-EP-MAD` | líneas | marrón 140 · 95 · 60 | 45° | 1,0 |
| `3D-REV-01` | líneas | gris 150 · 150 · 150 | 45° | 0,8 |
| `3D-SOL-EXT01` | puntos | arena 205 · 185 · 140 | 0° | 1,5 |
| `3D-BASE` | puntos gruesos | gris 120 · 120 · 120 | 0° | 1,0 |

**Si el DWG trae un sólido único por muro**

1. Duplicar el testigo.
2. `BooleanSplit` con superficies en los planos de cada capa.
3. Asignar cada porción a su capa de material.
4. Verificar con `What` que cada pieza es un polysurface cerrado.
5. Si el corte no cierra, modelar dos módulos en Rhino antes de seguir.

**Criterio:** si separar capas lleva más de 30 minutos, conviene modelar el testigo 1:10 en Rhino y dejar el DWG para el corte 1:50.

### 4.4 Abrir la profundidad del corte

`Custom Depth` es el interruptor que convierte el corte "thin" en un corte con volumen.

| Campo | Detalle |
|---|---|
| Acción | Activar `Custom Depth` en el plano `A-A` con `Depth = 1,00` m |
| API | `PlaneDepthEnabled = True`, `PlaneDepth = 1.0` sobre la geometría del plano |
| Aceptación | La vista muestra la cara de corte con hatch **y** 1 m de interior detrás del plano |
| Nota | Con la profundidad apagada se ve la cara cortada + todo el interior: ese es el corte abierto de entrega |

### 4.5 Del corte vivo al dibujo 2D

Rhino 8 tiene tres caminos; conviene elegir según el destino.

| Comando | Resultado | Cuándo usarlo |
|---|---|---|
| `ClippingDrawings` | Dibujo 2D con hatch y fondo, se actualiza al mover el plano | Lámina de corte constructivo |
| `ExtractClippingSections` | Curvas y hatches del corte, sin fondo | Editar el dibujo a mano |
| `Make2D` | Curvas planas con líneas ocultas y siluetas | Lámina isométrica y cortes de línea |

**`ClippingDrawings` (recomendado para el corte 1:50 / 1:10)**

1. Seleccionar el `ClippingPlane`.
2. `ClippingDrawings`.
3. Elegir punto de inserción en `World Top`.
4. Opciones: `ShowHatch=Yes`, `ShowSolid=Yes`, `AddBackground=Yes`, `AddHidden=Yes`, `AddSilhouette=Yes`.
5. El dibujo queda en capas propias y se actualiza al mover el plano.
6. Si cambia la geometría, ejecutar `UpdateClippingDrawings`.

> `AddBackground` proyecta lo que está delante del plano: es lo que da la sensación de corte arquitectónico y no solo una silueta.

**`ExtractClippingSections`**

1. Seleccionar el plano.
2. `ExtractClippingSections`.
3. `Curve=Yes`, `Hatch=Yes`, `Group=Yes`.
4. Editar las curvas y hatches resultantes como dibujo 2D.

**`Make2D` para isométrica**

1. Activar la vista isométrica.
2. Seleccionar el modelo.
3. `Make2D` → `Projection=View`.
4. `Hidden lines=Yes` si se quieren líneas ocultas.
5. `Clipping plane intersections=Yes`.
6. `Scene silhouette=Yes` para remarcar el contour.
7. `Register with previous=Yes` para repetir el encuadre.

### 4.6 Axonometría: la isométrica nativa y la 30/60

`Isometric` cambia la vista activa a **proyección paralela isométrica** mirando desde un cuadrante hacia el origen.

| Opción | Vista |
|---|---|
| `NE` | Noreste |
| `NW` | Noroeste |
| `SE` | Sureste |
| `SW` | Suroeste |
| `ZoomExtents` | Ajusta el encuadre |

**Dato clave:** la isométrica nativa es la isométrica verdadera, con los tres ejes a 120° y las aristas de planta a 30° respecto de la horizontal. Su elevación es 35,264°.

La clásica **30/60** es una axonométrica distinta y se resuelve por fuera del comando:

1. **Cámara personalizada:** `ViewportProperties` → `Projection=Parallel` → `Target` y `Camera` en la dirección deseada.
2. **Alinear cámara a una superficie:** `OrientCameraToSrf`.
3. **Script del vault:** [[scripts/axonometria-militar-rhino_notas|axonometria-militar-rhino_notas]] ya tiene la función `crear_platform_frame()` y la explicación de la axonométrica militar 30/60 con `Transform.ProjectAlong`.

> Para la lámina de entrega, la isométrica nativa `NE` suele alcanzar. La 30/60 se justifica cuando el estudio quiere una axonometría de estilo propio.

---

## 5. Parte C — Hoja A3 a escala 1:50

### 5.1 El encaje de la escala: el hallazgo

Cálculo hecho desde la cámara real de `axo3060` (dir 0,743 · 0,577 · −0,339, elevación ≈ 20°, azimut ≈ 38°):

| Magnitud | En modelo | A 1:50 | A 1:100 |
|---|---|---|---|
| Ancho proyectado del set completo | ≈ 22,3 m | **447 mm** | 223 mm |
| Alto proyectado del set completo | ≈ 24,4 m | **488 mm** | 244 mm |
| Área útil de A3 con márgenes 10 mm | — | 400 × 277 mm | 400 × 277 mm |

**Lectura:** el set completo a 1:50 necesita 447 × 488 mm y el A3 útil ofrece 400 × 277 mm. El alto del set (18,15 m → 362 mm a 1:50) es el que no entra.

**Corrección con el corte aplicado (medición real):** el clipping `A-A` deja visible **solo el lado +X del plano (X ≥ 575)**, y esa porción proyecta:

| Magnitud | En modelo | A 1:50 |
|---|---|---|
| Ancho proyectado del lado visible | 19,94 m | **398,8 mm** |
| Alto proyectado del lado visible | 13,88 m | **277,5 mm** |

El recorte no lo hace un segundo plano: **lo hace el propio plano de corte**. La porción que sobrevive a la sección ya entra en el ancho útil del A3 con 1,2 mm de margen.

**Caja del detalle finalmente usada: (10, 22) → (410, 292) mm** = 400 × 270 mm → ventana de modelo de **20,00 × 13,50 m**. Deja 22 mm de pie de hoja y 5 mm de margen superior.

Alternativas para una hoja de presentación:

| Opción | Descripción | Resultado |
|---|---|---|
| **O1** *(la usada)* | A3 a 1:50 con el fragmento que deja el propio corte | 400 × 270 mm, entra entero |
| **O2** | A3 con dos escalas: axonométrica general a 1:100 + detalle a 1:50 | Hoja completa y legible |
| **O3** | A1 a 1:50 (área útil 821 × 574 mm) | El set completo entra sin recortes |

### 5.2 Los ocho ítems y su estado

| # | Ítem | Cómo se ejecuta | Aceptación | Estado |
|---|---|---|---|---|
| 1 | Custom Depth de 1,00 m | Propiedades del plano → Custom Depth | Cara de corte + 1 m de interior detrás | Pendiente |
| 2 | Section Style en las 4 capas sin estilo | Propiedades de capa → Section Style | Cada material se lee con su relleno | Pendiente |
| 3 | Malla abierta `Object_3` (`3D-REV-01`) | `RebuildMesh` / `RepairMesh` u ocultarla en el detalle | La cara del corte no muestra huecos | Pendiente |
| 4 | Crear la hoja A3 | `Layout` → `AIZ-CORTE-A`, `Rhino PDF`, A3, horizontal | Pestaña de layout A3 | ✅ Hecho |
| 5 | Volcar la vista 3D al detalle a 1:50 | `AddDetailView` + cámara de `axo3060` + escala + `Lock` | Detalle en paralelo, 1:50, corte visible | ✅ Hecho |
| 6 | Composición dentro de la caja | Cálculo de la proyección y centrado en el objetivo de cámara | ≤ 400 × 270 mm a 1:50 | ✅ Hecho |
| 7 | Pie de hoja | Texto en espacio papel: 5 mm + 3 mm | Visible en la previsualización del print | ✅ Hecho |
| 8 | Cerrar la hoja | Borde en `No Print`, `PrintDisplay`, `Print` → Rhino PDF vectorial | PDF de 1 página; 1,00 m = 20 mm | Pendiente (lo hace el usuario) |

### 5.3 Configuración de la hoja

| Parámetro | Valor |
|---|---|
| Formato | A3, horizontal |
| Tamaño | 420 × 297 mm |
| Unidades de layout | mm |
| Margenes | 5 mm arriba, 22 mm abajo (banda de pie) |
| Detalle | (10, 22) → (410, 292) mm = 400 × 270 mm |
| Escala del detalle | 1:50 → 1,00 m de modelo = 20 mm de papel |
| Ventana de modelo | 20,00 × 13,50 m |
| Cámara | `axo3060`: dir (0,743 · 0,577 · −0,339), up (0,268 · 0,208 · 0,941), paralela |
| Modo de display | Shaded |
| Corte | `ClippingPlane` `A-A` habilitado en el detalle |
| Pie de hoja | 2 líneas: título 5 mm + subtítulo 3 mm |
| Salida | Rhino PDF, vectorial, una página por layout |

Textos del pie:

- `CORTE 3D A-A | SET E.J. | AXONOMETRIA 30/60 | ESC. 1:50` (5 mm)
- `ESTUDIO | HOJA AX-01 | 2026-10-25 | PROYECCION PARALELA` (3 mm)

### 5.4 Resultado verificado

| Comprobación | Resultado |
|---|---|
| Página | `AIZ-CORTE-A` — 420 × 297 mm |
| Detalle | `CORTE-A` — 400 × 270 mm, en (10, 22)–(410, 292) |
| Escala | **1:00 m del modelo = 20,0 mm sobre el eje horizontal de la hoja** |
| Cámara | paralela, up correcto, Shaded |
| Corte | activo en el detalle, cara de corte con relleno por capa |
| Pie de hoja | 2 líneas en espacio papel, en la banda inferior |
| Capturas | hoja renderizada y verificada visualmente |

**Archivos con la versión verificada:**

| Ubicación | Archivo | Bytes |
|---|---|---|
| Vault (respaldo) | `activos/mvp_05-rhino-mcp/01-AIZ/set-ej_corte.3dm` | 816.585 |
| Google Drive | `G:\Mi unidad\E#E.EDU\mora\set-ej_corte_A3-1-50.3dm` | 816.585 |

**Pendiente del usuario:** imprimir (`Print` → `Rhino PDF` → `Use layout page size` → `Vector output`) y **desmarcando "Clipping planes"** en el bloque Visibility, para que no se imprima la arista del plano de corte.

### 5.5 Lecciones técnicas de la API de Rhino 8

Trucos que costaron tiempo y quedan documentados:

| Tema | Cómo queda |
|---|---|
| Crear la página | `doc.Views.AddPageView(nombre, ancho, alto)` — no existe `doc.Layouts` en Rhino 8 |
| Crear el detalle | `pageView.AddDetailView(nombre, Point2d, Point2d, DefinedViewportProjection.None)`; el enum `None` no es accesible como atributo en Python 3: usar `System.Enum.Parse(tipo, "None")` |
| Escala del detalle | `det.Geometry.SetScale(papel, unidades, modelo, unidades)` → con `1 m` de papel y `20 m` de modelo da 1:50. El valor guardado es `PageToModelRatio = 0,02` (modelo por mm de papel) |
| Verificar la escala | proyectar dos puntos del modelo separados 1 m con `det.WorldToPageTransform` y medir la distancia en la hoja: debe dar 20,0 mm |
| Cámara del detalle | `CameraTarget` y `CameraLocation` son **de solo lectura**: usar `SetCameraTarget(pt, bool)`, `SetCameraLocation(pt, bool)`, `SetCameraDirection(dir, bool)`. El orden correcto es dirección → objetivo → `CameraUp`: cada setter recalcula el otro extremo conservando la dirección vigente |
| Up vector | asignarlo **último**: `SetCameraTarget` lo vuelve a (0,0,1) |
| Corte dentro del detalle | `clipObject.AddClipViewport(rhinoViewport, True)` — necesita el `RhinoViewport` de la página (`pageView.ActiveViewport`), no el `Viewport` del detalle |
| Texto en espacio papel | hay que activar el espacio **antes** de crear: `pageView.SetPageAsActive()` (no alcanza con `ActiveView`). Creado en modelo, el objeto queda fuera de la lámina |
| Altura del texto | el `DimensionScale` del estilo puede venir en 1,5 y dejar el texto a 0,2 mm: poner `DimensionScale = 1.0` |
| Posición del texto | el origen del texto es su borde **superior**: la línea base queda por debajo del punto de inserción |
| Guardar en Drive | `doc.Save()` puede devolver `False` si el documento quedó `IsLocked` (por ejemplo, tras un `Open` interrumpido): usar `SaveAs` a otra ruta y copiar el archivo |
| MCP | el puente vive dentro de Rhino: relanzarlo con `_RunPythonScript "…\scripts\rhino-mcp-server-rhino.py"` en la línea de comandos |

---

## 6. Checklist de cierre

### Corte

- [ ] El `ClippingPlane` corta perpendicular al eje y muestra espesores parejos.
- [ ] Custom Depth activo con 1,00 m y el corte muestra profundidad.
- [ ] Las 7 capas con contenido tienen section style.
- [ ] El plano está en `By Layer`.
- [ ] La cara del corte se lee en la vista `axo3060`.
- [ ] Malla abierta resuelta.

### Hoja

- [x] Layout A3 creado (`AIZ-CORTE-A`).
- [x] Detalle con la cámara de `axo3060`, en paralelo, bloqueado, a 1:50.
- [x] El detalle muestra el corte.
- [x] Composición dentro de 400 × 270 mm.
- [x] Texto de pie de hoja en espacio papel.
- [x] 1,00 m = 20,0 mm medidos sobre la hoja.
- [ ] Borde del detalle en `No Print` confirmado en la previsualización.
- [ ] PDF vectorial de una página impreso y verificado.
- [ ] `.3dm` guardado y respaldado en `activos/`.

---

## 7. Planilla de comparación y registro de tiempos

| Criterio | AutoCAD | Rhino | Diferencia |
|---|---|---|---|
| Tiempo hasta el primer corte | | | |
| Tiempo hasta el corte constructivo | | | |
| Ajustes manuales | | | |
| Calidad del hatch | | | |
| Calidad de líneas ocultas | | | |
| Facilidad para cambiar el corte | | | |
| Armado de lámina multi-escala | | | |
| Peso del archivo | | | |
| Curva de aprendizaje | | | |

| Ítem | Fecha | Responsable | Tiempo | Observaciones |
|---|---|---|---|---|
| Inspección del archivo por MCP | 2026-10-25 | Agente | ~40 min | El puente MCP no estaba levantado: relanzar el script dentro de Rhino |
| Hoja A3 + detalle 1:50 + pie | 2026-10-25 | Agente | ~90 min | La escala del detalle y el texto en espacio papel requirieron calibración por API |
| Verificación de escala y captura | 2026-10-25 | Agente | ~20 min | 1,00 m = 20,0 mm medidos sobre la hoja |
| Impresión del PDF | | | | |

---

## 8. Referencias

### Rhino 8 (verificadas 200 el 2026-10-25)

- McNeel — *ClippingPlane*: https://docs.mcneel.com/rhino/8/help/en-us/commands/clippingplane.htm
- McNeel — *Section Style*: https://docs.mcneel.com/rhino/8/help/en-us/popup_moreinformation/sectionstyle.htm
- McNeel — *Isometric*: https://docs.mcneel.com/rhino/8/help/en-us/commands/isometric.htm
- McNeel — *Make2D*: https://docs.mcneel.com/rhino/8/help/en-us/commands/make2d.htm
- McNeel — *Detail*: https://docs.mcneel.com/rhino/8/help/en-us/commands/detail.htm
- McNeel — *Layout*: https://docs.mcneel.com/rhino/8/help/en-us/commands/layout.htm
- McNeel — *Text*: https://docs.mcneel.com/rhino/8/help/en-us/commands/text.htm
- McNeel — *Print*: https://docs.mcneel.com/rhino/8/help/en-us/commands/print.htm
- McNeel — *ViewportProperties*: https://docs.mcneel.com/rhino/8/help/en-us/commands/viewportproperties.htm
- McNeel — *Intro to Section Styles*: https://www.rhino3d.com/docs/guides/drafting/clipping-sectioning/intro-to-section-styles/
- McNeel — *Architectural Drawings*: https://www.rhino3d.com/docs/guides/user-guide/drafting-architecture

### AutoCAD

- Autodesk — *SECTIONPLANE (Command)*: https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-3AC2CA12-2085-4782-B66A-7964B73B55EA.htm
- Autodesk — *SECTION (Command)*: https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-C649EE10-5FE3-4703-9301-C97AEF7C5BD7.htm
- Autodesk — *FLATSHOT (Command)*: https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-746F10D2-7CFD-412D-B51F-33574C773B95.htm
- Autodesk — *Section Settings Dialog Box*: https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-D061EB7A-6B8D-4CB9-9C2F-6C68B711FA33.htm

### Internos

- Operación del puente: [[proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp|pbook-rhino-mcp]]
- Axonométrica militar 30/60: [[scripts/axonometria-militar-rhino_notas|axonometria-militar-rhino_notas]]
- Ficha del experimento: [[proyectos/MVP_05-rhino-mcp/01-AIZ/00-index|00-index]]
