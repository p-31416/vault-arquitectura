---
tipo: reporte
fecha: 2026-10-22
tema: Rhino 8 — flujo para la casa de la entrega + mapa de creadores
slug: rhino-flujo-entrega-y-creadores
investigador: sherlock
fuente_madre: raw/research/2026-10-22-modelar-casa-rhino.md
estado: propuesta
---

# Rhino 8: flujo para la entrega y mapa de creadores

Fecha: 2026-10-22 · Zona: `-03:00 America/Argentina/Buenos_Aires`
Objetivo: modelar una casa de tres niveles (planta baja, entrepiso, primer piso y segundo piso barra-terraza; sin planta de servicio) a partir de un plano 2D de AutoCAD LT, con **reunión de entrega mañana 2026-10-23 a las 09:00**, y producir plantas, cortes y una lámina A3 exportada a PDF.

> Restricción vigente: **AutoCAD LT no modela en 3D**. LT se usa para verificar unidades, limpiar (`AUDIT`, `PURGE`, `WBLOCK`) y exportar el 2D; todo el 3D se hace en Rhino.

Este documento sintetiza la investigación de [[raw/research/2026-10-22-modelar-casa-rhino]], cruza los creadores con los videos que ya están en el vault y aterriza el flujo en pasos con comandos.

---

## 1. Síntesis de la investigación

### 1.1 Hallazgo central

Rhino 8 ordena el trabajo arquitectónico en **tres rutas**, y la elección depende del punto de partida:

| Ruta | Cuándo conviene | Secuencia | Respaldo |
|---|---|---|---|
| **A. PushPull nativo** | Modelar desde cero, sin CAD | sólido base → `PushPull` / `SplitFace` / `Inset` → aberturas → cubierta | Guía oficial McNeel + video de Kyle Houchens |
| **B. DWG → sólidos** | Ya existe plano 2D (nuestro caso) | importar DWG → `Join` / `CloseCrv` → `ExtrudeSrf` → `BooleanUnion` → detalles | How to Rhino (EN), Hakan y Diego Pascual (ES) |
| **C. Caso de estudio** | Aprender viendo una obra | imagen/plano → volumen → detalle | Ruben Borup (Azuma), Flavio Bevilacqua (Le Corbusier) |

Para la entrega manda la **ruta B**, con PushPull para retoques de caras y `BooleanDifference` para vanos. La ruta A queda como alternativa si el DWG viene sucio.

### 1.2 El tramo que define la entrega: 3D → planos

`Make2D` proyecta aristas y siluetas como curvas planas sobre el plano Top del mundo. Opciones que importan para nuestra lámina:

- **Projection: View** (proyecta la vista activa) o **CPlane** (usa el plano de construcción).
- **Third angle** (EE. UU.) o **First angle** (europeo). Para Argentina conviene **First angle**.
- **Hidden lines**, **Tangent edges**, **Scene silhouette** y **Clipping plane intersections** (dibuja las intersecciones de planos de corte).
- **Register with previous**: alinea la salida con un Make2D anterior de la misma vista; sirve para repetir plantas sin que se corran.
- **Layer name**: capa madre de salida, con subcapas por tipo de curva.

Dos avisos de la doc oficial: `Make2D` **aplana las cotas** y **no genera la intersección** entre objetos que se atraviesan (para eso hay que correr `Intersect` antes). La lámina se arma después en `Layout` (espacio papel) con detalles a escala y se exporta con `Print` → **Rhino PDF**, tamaño de página del layout y salida vectorial.

### 1.3 Bloques: la pieza que faltaba

- `Block` define el bloque a partir de geometría seleccionada.
- `Insert` inserta un archivo externo; con **Insert as: Block instance** el DWG entra como **una sola instancia** (no como miles de curvas sueltas) y con **Block definition type: Embedded and linked** queda vinculado al archivo.
- La instancia cae en la capa actual y su punto de inserción es el punto base del bloque.
- `BlockEdit` edita la definición (todos los ejemplares cambian juntos); `BlockManager` administra definiciones; `Explode` desarma una instancia; `Purge` limpia definiciones sin uso.

Esto resuelve dos necesidades del brief: **la base CAD en una capa removible** y el **mobiliario repetido** de cocina y baño.

### 1.4 Vacíos declarados

- Cubierta inclinada y escalera aparecen sólo como fragmentos, sin serie cerrada.
- Ningún recurso verificado cubre el mapeo de capas CAD → capas Rhino con estándar de oficina.
- Sin fuente argentina de dibujo (POSGAR 2007, Ley 24.335).
- Duraciones de los videos nuevos sin verificar (YouTube devuelve sólo el shell a `webfetch`; requiere `yt-dlp` en Fase 2).
- Italiano: sin material específico de vivienda.

---

## 2. Mapa de creadores

### 2.1 Ya en el vault (veredicto y videos)

| Creador / canal | Idioma | Videos en vault | Veredicto | Para qué sirve |
|---|---|---|---|---|
| **Rhino 3D (oficial)** | EN | 13 | pendiente | Serie Studio: setup, site plans, floor plans, elevaciones, masa, 3D |
| **How to Rhino** | EN | 5 | pendiente | Puente DWG→3D, importar ubicación, plugins |
| **Gediminas Kirdeikis** | EN | 3 | rescatar | Secciones dinámicas, envolvente, cursos largos |
| **David Copete Parametric** | ES | 3 | pendiente | Planta paramétrica (29:42), tiny home (3:10:04) |
| **Urban Decoders** | EN | 3 | rescatar | Rhino + IA/MCP, Cesium/Unreal |
| **ArchiTech Network** | EN | 3 | rescatar | AR con Fologram, animación, defensa de Rhino |
| **McNeel Europe** | EN | 1 | rescatar | Webinar de machine learning en Rhino 8 (40:11) |
| **Algorithmix Design** | EN | 1 | rescatar | GH + IA que genera plantas (1:38) |
| **Arturo Tedeschi** | EN | 1 | rescatar | ChatGPT conectado a Grasshopper |
| **The Different Design** | EN | 1 | sin veredicto | ChatGPT + GH |
| **Nate's Studio Desk** | EN | 1 | sin veredicto | ChatGPT para diseñar en Rhino |
| **Andrew Friedenberg** | EN | 2 | sin veredicto | Geometric workflows, pixelado tipo MVRDV |
| **Arkpe** | ES | 1 | sin veredicto | De superficie a sólido, 3 métodos (2:20) |
| **ThinkParametric** | EN | 1 | sin veredicto | Stadium + RhinoScript/Python |
| **Philipp Galvan Design** | EN | 1 | sin veredicto | "Rhino AI": panorama, tono clickbait |
| **PlanFinder / McNeel Europe** | EN | 1 | sin veredicto | Webinar de plantas de departamentos (1:03:29) |

### 2.2 Nuevos (no están en los 47 videos)

| Creador / recurso | Idioma | Por qué seguirlo | Prioridad |
|---|---|---|---|
| **McNeel — PushPull for Architects** | EN | Única guía oficial que modela una casa completa en Rhino 8; trae `.3dm` de partida | **Seguir** |
| **Diego Pascual — Modelar casa (1/4 → 4/4)** | ES | Única serie en castellano de casa completa con comandos nombrados | **Seguir** |
| **Tom Budd — Planos de Arquitectura (1/4 → 4/4) + espacio papel** | ES | Cubre el tramo legal: modelo → lámina, pesos de línea, layout | **Seguir** |
| **Kyle Houchens — House with Push Pull** | EN | Demostración en vivo del flujo PushPull sobre vivienda | Ver |
| **Hakan Architecture** | ES | Planta 2D → 3D en vivienda; playlist de escaleras | Ver |
| **Flavio Bevilacqua — Le Corbusier (1/3 → 3/3)** | ES | CAD → Rhino resuelto sobre referencia clásica | Ver |
| **Ruben Borup — Azuma House (1/4 → 4/4)** | ES | Caso de estudio con detalle | Referencia |
| **SMlab UGR — índice de tutoriales** | ES | Reúne ~20 autores con series completas; mejor puerta de entrada en castellano | **Seguir** |
| **McNeel Discourse — Layouts** | EN | Hilo curado que apunta al Level 1 Training Guide y a un tutorial de layouts | Referencia |
| **rhinomcp (Food4Rhino)** | EN | Automatización por socket: objetos, capas, scripts; sin tutorial de vivienda | Referencia |

### 2.3 Cómo leer este mapa

- **Seguir** = aporta exactamente lo que falta para esta entrega.
- **Ver** = complemento puntual; conviene saltear introducciones.
- **Referencia** = consulta cuando aparece un problema concreto, sin maratón.
- La serie oficial Studio ya cubre masas, plantas y elevaciones: sirve para **repasar el estándar**, no para aprender la casa completa.

---

## 3. Cruce con los 47 videos del vault

El índice del vault suma **31 videos** de la playlist `ARQ/Rhino+Grasshopper` y los etiquetados `rhino` en Watch Later, con solapamientos (Copete 29:42, Urban Decoders/Cesium): total **47**.

**Lo que ya está cubierto:**

- Flujo oficial completo: `How to Get Started`, `Top 10 Setup Tricks`, `Drafting Site Plans & Context` (13:32), `Drafting Floor Plans` (17:40), `How to Think in 3D` (17:57), `3D Massing Iterations` (20:55), `Beyond the 3D Box` (20:00), más shorts de estándar de dibujo y elevaciones.
- Interoperabilidad y contexto: importar ubicación (How to Rhino), Cesium/Unreal (Urban Decoders), AR con Fologram (ArchiTech).
- IA aplicada: MCP con Claude (Urban Decoders), ML en Rhino 8 (McNeel Europe), GH + IA para plantas (Algorithmix), ChatGPT + GH (Tedeschi, The Different Design, Nate's).
- Secciones y envolvente: Gediminas (`Dynamic Sections` 22:01, `Carve Building Envelope` 38:02).
- Paramétrico: Copete (planta 29:42, tiny home 3:10:04, estadio), cursos de Gediminas (5 h y 11 h).

**Lo que falta y justifica los nuevos:**

- Una **serie de casa completa**, en cualquier idioma: la oficial modela masas y plantas, no la vivienda entera.
- **Espacio papel y lámina** explicados en castellano: Tom Budd.
- **DWG insertado como bloque**: ningún video lo trata como flujo principal.
- **Bloques de mobiliario** (cocina/baño): aparece de pasada.
- **Escalera**: sólo playlists genéricas.
- **Cubierta inclinada**: fragmentos, sin secuencia.

Conclusión operativa: para mañana alcanza con **2 fuentes** —la guía oficial PushPull para el criterio de modelado y Tom Budd para la lámina— y **1 serie** de apoyo (Diego Pascual) para los comandos en español. El resto es archivo para después de la entrega.

---

## 4. Flujo para la entrega (paso a paso)

Supuesto: modelo en **metros**, tolerancia `0.001` (1 mm), plano DWG con cotas verificables.

### Paso 0 — Setup (15 min)

1. `New` con template **Small Objects – Meters**.
2. `Units` → metros, tolerancia absoluta `0.001`.
3. Capas: `00-EJES`, `CAD-BASE`, `A-MUROS`, `A-ABERTURAS`, `A-LOSAS`, `A-CUBIERTA`, `A-ESCALERA`, `A-MOBILIARIO`, `A-ANOTACION`, `A-CORTES`, `LAYOUT`.
4. `SaveAs` → `casa-<cliente>-v01.3dm`.

### Paso 1 — DWG como bloque (20 min)

1. `Insert` → archivo DWG → **Insert as: Block instance** → **Block definition type: Embedded and linked**.
2. Insertar en la capa `CAD-BASE`, con el punto base en el origen o en un eje conocido.
3. Verificar escala con `Distance` contra una cota del plano. Si el DWG viene en milímetros, escalar la instancia por `0.001` (o fijar unidades de inserción).
4. **Lock** a `CAD-BASE` y `Hide` cuando estorbe. La base queda entera, removible y sin contaminar el modelo.
5. Duplicar la instancia, mover la copia a `CAD-WORK` y `Explode` **sólo esa copia**; `Join`/`CloseCrv` para obtener curvas editables. La base original no se toca.
6. `Purge` al final, sólo si aparece una definición duplicada.

### Paso 2 — Ejes, muros y losas (60–90 min)

1. Copiar los ejes del bloque a `00-EJES` (`Insert` del bloque + `Explode` sólo de una copia, o `DupBorder` sobre las curvas necesarias).
2. Muros: `Offset` de las líneas de eje a las caras, `CloseCrv` y `ExtrudeSrf` con `Solid=Yes`; unir con `BooleanUnion`. Alternativa: sólido base + `PushPull` por cara.
3. Entrepiso y losas: `PlanarSrf` + `ExtrudeSrf` (espesor real) o `ExtrudeCrv` con `Solid=Yes`.
4. Revisar con `ShowEdges` que los sólidos estén cerrados antes de boolear.

### Paso 3 — Aberturas (45 min)

1. Crear sólidos de corte por vano (dimensiones de carpintería) y restar con `BooleanDifference`.
2. Para ajustes rápidos sobre fachada: `PushPull` con `Inset`, o `SplitFace` + `PushPull`.
3. Nombrar los vanos repetidos y convertirlos en bloque (Paso 5) para copiar por piso.

### Paso 4 — Segundo piso barra-terraza y cubierta (60 min)

1. Repetir muros y losa del nivel superior; la barra-terraza se resuelve como volumen propio con su losa.
2. Cubierta: `Loft` entre bordes o `Sweep1` sobre el perímetro; `OffsetSrf` para el espesor y `ExtrudeSrf` para el alero.
3. Verificar encuentros con `BooleanUnion` y `ShowEdges`.

### Paso 5 — Bloques de mobiliario (45 min)

1. Modelar un módulo de cocina (bajo + alto + mesada) en `A-MOBILIARIO`.
2. `Block` → nombre `MOB-COCINA-01`, punto base en el vértice inferior izquierdo contra muro.
3. `BlockEdit` para variantes; `Copy` de la instancia por ambiente.
4. Baño: bloque de inodoro, lavatorio y ducha por separado (permite combinarlos).
5. `BlockManager` para revisar nombres y cantidades antes de la lámina.

### Paso 6 — Escalera (45–60 min)

1. Definir huella y contrahuella (verificar contra el entrepiso).
2. Zanca: `Sweep1` sobre el perfil y la trayectoria; peldaños: `Box` + `ArrayLinear`.
3. Alternativa paramétrica: definición mínima en Grasshopper (huella, contrahuella, ancho, cantidad) y `Bake` del resultado.
4. Comprobar el paso libre con un corte rápido (`ClippingPlane`).

### Paso 7 — Make2D por planta (60 min)

1. Vista `Top` paralela, encuadre fijo, guardar vista con nombre (`NamedView`).
2. Seleccionar el nivel + el mobiliario, `Make2D`:
   - Projection: **View**
   - **First angle**
   - Hidden lines: activado
   - Clipping plane intersections: activado si hay corte
   - Layer name: `A-ANOTACION`
3. Ocultar `CAD-BASE` antes de proyectar para evitar líneas duplicadas.
4. Repetir con **Register with previous** para entrepiso, primer y segundo piso.
5. `Intersect` donde haga falta la línea de encuentro entre sólidos.

### Paso 8 — Lámina A3 y PDF (90 min)

1. `Layout` → nueva lámina, tamaño **A3 (420 × 297 mm)**, horizontal.
2. Insertar `Detail` por planta; escala **1:50** (o 1:75 si no entra). Bloquear la vista del detalle.
3. Cotas con `Dim`, textos con `Text`, materialidad con `Hatch`, norte y rótulo en `LAYOUT`.
4. Título: cliente, proyecto, planta, escala, fecha, lámina.
5. `Print` → **Rhino PDF** → página del layout → salida **vectorial** → guardar `casa-<cliente>-A3.pdf`.
6. Revisar el PDF a 100 %: textos legibles, cotas fuera del dibujo, líneas negras.

### Paso 9 — Cortes (45 min)

1. `ClippingPlane` sobre el modelo, paralelo a la fachada principal y por la escalera.
2. `Make2D` con **Clipping plane intersections** activado; `Hatch` en los muros cortados.
3. Dos cortes como mínimo: longitudinal por escalera y transversal por cocina/baño.

### Checklist de entrega

- [ ] Unidades y escala verificadas contra una cota del DWG.
- [ ] `CAD-BASE` en bloque, bloqueada y oculta en la lámina.
- [ ] Sólidos cerrados (`ShowEdges`) y sin caras duplicadas.
- [ ] Cuatro plantas: PB, entrepiso, 1° y 2° barra-terraza (sin planta de servicio).
- [ ] Escalera con paso libre verificado.
- [ ] Bloques de cocina y baño insertados y nombrados.
- [ ] Dos cortes acotados.
- [ ] A3 en PDF vectorial, rótulo completo.
- [ ] `.3dm` guardado con versión y `.pdf` exportado a la carpeta del proyecto.

---

## 5. Cronograma propuesto (editable)

| Bloque | Ventana | Contenido | Corte de alcance |
|---|---|---|---|
| A | hoy 18:30–21:30 | Setup, limpieza en LT, `Insert` DWG, ejes, muros PB | Si el DWG está sucio: modelar con ejes propios |
| B | hoy 21:30–00:00 | Entrepiso, 1° piso, aberturas | Vanos sólo en fachada principal |
| C | hoy 00:00–01:30 | 2° piso barra-terraza, cubierta, escalera | Cubierta como losa inclinada simple |
| D | hoy 01:30–03:00 | `Make2D` 4 plantas, `Layout` A3, 1 corte, **PDF v1** | Mobiliario mínimo: 1 bloque por ambiente |
| E | mañana 06:30–08:30 | Correcciones, 2° corte si entra, re-export, backup | PDF cerrado a las 08:30 |

Regla de oro: **el PDF v1 se exporta esta noche**. Mañana se corrige y se re-exporta; a las **08:30** el archivo está cerrado y copiado a Drive/USB.

---

## 6. Riesgos y decisiones

| Riesgo | Señal | Mitigación |
|---|---|---|
| AutoCAD LT sin 3D | Sin sólidos ni extrusión | LT sólo limpia/exporta 2D; todo el 3D en Rhino |
| Plantas superpuestas en Z=0 | Muros de distintos niveles coinciden | Separar por capa/nivel con `SelLayer` + `Move` en Z |
| Xrefs sin bindear | Geometría faltante al insertar | `WBLOCK` del área o pedir copia con xrefs bindeadas |
| DWG en unidades equivocadas | Medidas 1000× | `Distance` contra cota conocida y escalar la instancia |
| DWG explotado por accidente | Miles de curvas sueltas | `Undo`; explotar sólo la copia en `CAD-WORK` y conservar `CAD-BASE` bloqueada |
| Make2D lento o sucio | Minutos de espera, líneas duplicadas | Ocultar `CAD-BASE`, proyectar por nivel y por vista guardada |
| Bloques que no se actualizan | Cambio en un ejemplar y no en el resto | `BlockEdit`, nunca `Explode` + copiar |
| Escalera mal resuelta | Paso libre bajo el entrepiso | Verificar con corte antes de la lámina |
| GH consume el tiempo | Definición que no cierra | GH sólo para escalera; el resto manual |

Decisiones tomadas: **ruta B** (DWG→sólidos) + PushPull para retoques; **bloques** para DWG y mobiliario; **Make2D + Layout** para la lámina; **A3 PDF vectorial** como único entregable gráfico.

---

## 7. Pendientes (post-entrega)

- Transcribir los 4 videos de Diego Pascual y los 5 de Tom Budd con `scripts/transcribir_youtube.py` para verificar duraciones y extraer comandos.
- Verificar la guía oficial PushPull contra el DWG real y anotar diferencias de flujo.
- Propuestas wiki: ampliar [[wiki/glosario/software/rhino]] con PushPull + 3D→planos; crear `modelado-vivienda-rhino` y `planos-como-documento-legal`.
- Registrar `rhinomcp` como herramienta del ecosistema, con la salvedad de que no hay tutorial de vivienda.
- Fase 2 de `@contenidos` sobre los 8 candidatos cuando la entrega esté cerrada.

---

## 8. Fuentes verificadas

1. McNeel. *PushPull for Architects | Modeling a House*. https://www.rhino3d.com/en/docs/guides/push-pull/push-pull-for-architects/ — 200
2. McNeel. *Make2D | Rhino 8*. https://docs.mcneel.com/rhino/8/help/en-us/commands/make2d.htm — 200
3. McNeel. *Block | Rhino 8*. https://docs.mcneel.com/rhino/8/help/en-us/commands/block.htm — 200
4. McNeel. *Insert | Rhino 8*. https://docs.mcneel.com/rhino/8/help/en-us/commands/insert.htm — 200
5. McNeel. *Layout | Rhino 8*. https://docs.mcneel.com/rhino/8/help/en-us/commands/layout.htm — 200
6. McNeel. *Print | Rhino 8*. https://docs.mcneel.com/rhino/8/help/en-us/commands/print.htm — 200
7. Cvetkovic, D. *House from CAD Drawings*. https://howtorhino.com/rhino-grasshopper-tutorials/house-from-cad-drawings/ — 200
8. SMlab, Universidad de Granada. *Tutoriales de RHINOCEROS*. https://blogs.ugr.es/smlab/miscelanea-miscellany/tutoriales-rhinoceros/ — 200
9. McNeel Discourse. *Layouts – Learning Resources*. https://discourse.mcneel.com/t/layouts-learning-resources/176929 — 200
10. McNeel Discourse. *Rhino for Architectural Modeling – Learning Resources*. https://discourse.mcneel.com/t/rhino-for-architectural-modeling-learning-resources/162144 — 200
11. Food4Rhino. *rhinomcp*. https://www.food4rhino.com/en/app/rhinomcp — 200
12. YouTube (título confirmado, duración sin verificar): Diego Pascual `ZYcY-cB-DRA`; Tom Budd `NuK0SX93J4E`; Kyle Houchens `pwAqZH9b85E`; How to Rhino `aqotuhPejiA`; Hakan `rUb-mPL6KQw`.

---

**Estado:** propuesta. Sin tocar `wiki/`. Pendiente de aprobación para guardar la ruta en `specs/` y encadenar `@contenidos`.
