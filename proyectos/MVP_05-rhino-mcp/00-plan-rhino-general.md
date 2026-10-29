---
tipo: plan
proyecto: Rhino general — del modelado 3D al corte constructivo
cliente: Estudio (interno)
fase: plan
fecha_creacion: 2026-10-25
ultima_actualizacion: 2026-10-25
estado: propuesta
tags: [rhino8, modelado-3d, platform-frame, corte-constructivo, make2d, layout, curso, configuracion]
idioma: es
---

# Plan — Rhino general: del modelado 3D al corte constructivo y la lámina

> Documento único para leer y discutir. Reúne el plan completo: qué modelar, en qué orden, qué configurar y qué preguntas resolver antes de tocar Rhino.
>
> **Estado: propuesta.** No se ejecutó ninguna configuración en Rhino, no se creó ningún `.3dm` y no se tocó `wiki/`. El documento vive en `proyectos/MVP_05-rhino-mcp/`, junto al pbook del puente Rhino-MCP.

---

## 0. Resumen ejecutivo

La ruta que propongo tiene cinco peldaños: **volumen → pieza → capa → sección → lámina**. Se aprende modelado 3D común sobre una casa didáctica, después se baja al detalle constructivo de un testigo de platform frame, y recién entonces se corta, se sombrea y se imprime. El curso y el entregable comparten el mismo archivo: cada módulo deja una parte del modelo terminada.

El resultado es un `.3dm` limpio, dos cortes generales a 1:50, un corte-detalle a 1:10 con todas las capas del sistema, una axonometría de lectura y un PDF A3 vectorial. Rhino resuelve modelado, secciones dinámicas, `Make2D`, `Layout` e impresión; el cálculo estructural se apoya en CIRSOC 601 y la normativa argentina de entramado de madera.

La decisión central es **modelo híbrido**: la casa completa se modela simplificada y un sector de dos módulos se modela estratificado pieza por pieza. Ese sector es el que produce el corte constructivo y el que se usa para aprender. Así se llega al detalle real sin modelar cada montante de toda la casa.

---

## 1. Resultado esperado

| # | Entregable | Formato | Criterio |
|---|---|---|---|
| 1 | Modelo de la casa | `casa-didactica-v01.3dm` | Sólidos cerrados, capas nombradas, unidades en metros |
| 2 | Planta general | En la lámina A3 | 1:50, con marcas de corte A-A y B-B |
| 3 | Corte general longitudinal | En la lámina A3 | 1:50, casa completa, espacios y alturas |
| 4 | Corte general transversal | En la lámina A3 | 1:50, encuentro muro-entrepiso-cubierta |
| 5 | Corte-detalle D-1 | En la lámina A3 | 1:10, platform frame estratificado con hatches |
| 6 | Axonometría | En la lámina o aparte | Explica el sistema constructivo |
| 7 | Lámina | `casa-didactica-A3-v01.pdf` | A3 420×297, vectorial, rótulo completo |
| 8 | Documento de curso | Este archivo + anexo de módulos | 8 módulos con comandos y ejercicios |

---

## 2. Decisión de alcance: casa didáctica + testigo

### 2.1 Casa didáctica

- Planta **8 × 12 m**, dos niveles, cubierta a dos aguas.
- Planta baja: living-comedor, cocina, baño, acceso.
- Planta alta: dos dormitorios, baño, hall.
- Altura de piso a piso: **2,70 m**.
- Cubierta: pendiente simple, chapa ondulada sobre cabios.
- Fundación: platea con aislación perimetral, para mantener el ejercicio simple.

### 2.2 Testigo constructivo

Un sector de **dos módulos** (aproximadamente 1,20 × 2,40 m) en el encuentro de muro exterior, entrepiso y cubierta. Se modela completo:

- Solera inferior, montantes, solera superior doble.
- Bloqueo o riostra, dintel si hay abertura.
- OSB exterior, membrana hidrófuga, rastrel y revestimiento.
- Aislación entre montantes, barrera de vapor y placa interior.
- Viga de entrepiso, OSB de piso, aislación y cielorraso.
- Cabio de cubierta, OSB, membrana, clavaderas y chapa.

Ese testigo se copia una vez para el corte-detalle y se referencia en la axonometría. El resto de la casa se modela como volumen con espesores reales de conjunto, suficiente para los cortes 1:50.

### 2.3 Qué queda afuera

- Cálculo estructural y dimensionado de piezas: se consulta CIRSOC 601, pero el curso no lo resuelve.
- Render fotorrealista: la gráfica del curso es técnica, con sombras y hatches. Un render puede sumarse después con ComfyUI.
- Instalaciones, sanitarios y eléctricos: aparecen como espacio reservado, sin desarrollo.
- Terreno y entorno: solo una plataforma de apoyo para dar escala.

---

## 3. Progresión pedagógica: cinco peldaños

| Peldaño | Qué se aprende | Qué se produce | Dónde se ve |
|---|---|---|---|
| 1. Volumen | Mover, copiar, extruir, boolear | Casa como masa | Perspectiva |
| 2. Pieza | Modulación, bloques, matrices | Muro con montantes | Axonometría |
| 3. Capa | Espesores, materiales, orden | Testigo estratificado | Detalle 1:10 |
| 4. Sección | Planos delimitadores, hatches | Corte A-A / B-B | Lámina 1:50 |
| 5. Lámina | Layout, escalas, rótulo, PDF | A3 vectorial | PDF |

La regla es: **primero se entiende el volumen, después se entiende la pieza, después se entiende la capa**. El corte constructivo aparece cuando las tres cosas ya están resueltas.

---

## 4. Ruta de 8 módulos (~16 h)

| # | Módulo | Objetivo | Comandos principales | Salida | Horas |
|---|---|---|---|---|---|
| 0 | Interfaz y setup | Navegar y preparar el archivo | `Units`, `Options`, `Layer`, `SaveAs` | `.3dm` vacío con capas | 1,5 |
| 1 | Dibujo 2D preciso | Dibujar la planta con medidas reales | `Line`, `Rectangle`, `Offset`, `Trim`, `Join`, `Dim` | Planta 8×12 | 2 |
| 2 | Sólidos comunes | Pasar de curvas a volumen | `ExtrudeCrv`, `BooleanUnion`, `BooleanDifference`, `PushPull`, `ShowEdges` | Casa en volumen | 2 |
| 3 | Platform frame | Entender modulación y piezas | `Block`, `BlockEdit`, `ArrayLinear`, `Copy`, `Move` | Testigo de dos módulos | 2,5 |
| 4 | Aberturas y cubierta | Resolver vanos y faldón | `BooleanDifference`, `Loft`, `Sweep1`, `OffsetSrf`, `Cap` | Casa completa | 2 |
| 5 | Cortes y hatches | Cortar y leer materiales | `ClippingPlane`, `ClippingSections`, `Section Style`, `Hatch` | A-A, B-B y D-1 | 2 |
| 6 | Gráfica | Sombras, grosores, `Make2D` | `Shaded`, `Pen`, `Make2D`, `Text`, `Leader` | Lámina de dibujo | 2 |
| 7 | Layout e impresión | Armar la lámina y exportar | `Layout`, `Detail`, `Print` | PDF A3 vectorial | 2 |

Cada módulo tiene 20 minutos de explicación y el resto de práctica sobre el mismo archivo. Los módulos 3 y 5 son los que más tiempo consumen y los que más valor didáctico aportan.

---

## 5. El corte constructivo: qué muestra y a qué escala

### 5.1 Tres cortes, tres lecturas

| Corte | Ubicación | Escala | Qué muestra |
|---|---|---|---|
| A-A | Longitudinal, por la escalera y el frente principal | 1:50 | Alturas, entrepiso, cubierta, relación espacio-constructivo |
| B-B | Transversal, por un ventana y el encuentro de fachada | 1:50 | Muro exterior, entrepiso, cubierta, fundación |
| D-1 | Ampliación del encuentro muro-entrepiso-cubierta | 1:10 | Capas, espesores, orden, fijaciones, aislación |

### 5.2 Por qué 1:50 y 1:10

- A **1:50** se lee la casa: los montantes son líneas y las capas se agrupan por familia. Es la escala de proyecto.
- A **1:10** se lee el sistema: cada montante es un rectángulo de 38×140 mm, cada placa tiene su espesor y cada membrana su línea. Es la escala de obra.
- El corte 1:50 se genera con `ClippingPlane` sobre el modelo completo. El 1:10 se genera con un segundo plano sobre el testigo, con `ClippingSections` o `Make2D`.

### 5.3 Composición del sistema

**Muro exterior (de afuera hacia adentro):**

| Capa | Espesor típico | Material |
|---|---|---|
| Revestimiento | 10–20 mm | Chapa, siding o madera |
| Rastrel + cámara | 25 + 25 mm | Madera + aire |
| Membrana hidrófuga | 0,5 mm | WRB |
| OSB | 11,1 mm | Tablero estructural |
| Montantes | 38 × 140 mm | 2×6 @400/600 mm |
| Aislación | 140 mm | Lana mineral |
| Barrera de vapor | 0,2 mm | Polietileno |
| Placa interior | 12,5 mm | Yeso |

**Entrepiso:**

| Capa | Espesor típico | Material |
|---|---|---|
| Piso | 15 mm | Madera o laminado |
| OSB | 18 mm | Tablero estructural |
| Vigas | 38 × 184 mm | 2×8 @400 mm |
| Aislación | 184 mm | Lana mineral |
| Cielorraso | 12,5 mm | Yeso |

**Cubierta:**

| Capa | Espesor típico | Material |
|---|---|---|
| Chapa | 0,5 mm | Ondulada o trapezoidal |
| Clavaderas | 38 × 38 mm | Madera |
| Membrana | 0,5 mm | Bajo cubierta |
| OSB | 11,1 mm | Tablero estructural |
| Cabios | 38 × 140 mm | 2×6 @400/600 mm |
| Aislación | 140 mm | Lana mineral |
| Barrera de vapor | 0,2 mm | Polietileno |
| Placa | 12,5 mm | Yeso |

**Fundación:**

| Capa | Espesor típico | Material |
|---|---|---|
| Platea | 100 mm | Hormigón armado |
| Aislación perimetral | 50 mm | XPS |
| Solera inferior | 38 × 89 mm | 2×4 anclada |
| Barrera hidrófuga | 0,5 mm | Membrana |

> Los espesores son de referencia didáctica. El dimensionado real se verifica con CIRSOC 601 y el proyecto ejecutivo.

---

## 6. Arquitectura de capas y estilos en Rhino

### 6.1 Capas propuestas

| Capa | Color | Uso |
|---|---|---|
| `00-EJES` | Rojo | Ejes y niveles |
| `01-FUNDACION` | Gris oscuro | Platea, soleras, anclajes |
| `02-MONTANTES` | Marrón claro | Montantes y soleras |
| `03-ENTREPISO` | Marrón medio | Vigas y bloqueos |
| `04-CUBIERTA` | Marrón oscuro | Cabios y clavaderas |
| `05-PLACAS` | Ocre | OSB y yeso |
| `06-AISLACION` | Amarillo | Lana mineral y XPS |
| `07-MEMBRANAS` | Azul | WRB, vapor, bajo cubierta |
| `08-REVESTIMIENTO` | Verde | Chapa, siding, madera |
| `09-ABERTURAS` | Celeste | Marcos y vidrios |
| `10-ANOTACION` | Negro | Cotas, textos, símbolos |
| `11-CORTES` | Magenta | Planos delimitadores y curvas de sección |
| `CAD-BASE` | Gris claro | DWG de referencia, bloqueado y oculto |
| `LAYOUT` | Blanco | Rótulo y armado de lámina |

### 6.2 Estilos de sección

Cada familia de material recibe un hatch distinto en `Section Style`:

- **Madera:** líneas paralelas a 45°, escala media.
- **Aislación:** trama ondulada o cruzada, escala fina.
- **OSB:** punto o trama densa.
- **Membrana:** línea fina continua, sin relleno.
- **Hormigón:** relleno gris sólido.
- **Yeso:** relleno gris muy claro.
- **Chapa:** línea gruesa, sin relleno.

El objetivo es que el corte se lea en blanco y negro, sin depender del color. El color queda para la axonometría.

---

## 7. Flujo técnico paso a paso

1. **Setup** — unidades en metros, tolerancia 0,001, template, capas y estilos.
2. **Planta** — ejes, muros, aberturas, escalera; cotas verificadas contra una medida conocida.
3. **Volumen** — extrusión de muros y losas, booleanas, `ShowEdges` para confirmar sólidos cerrados.
4. **Testigo** — dos módulos de muro, entrepiso y cubierta, con todas las capas.
5. **Aberturas** — vanos con sólidos de corte; marcos y vidrios en capa aparte.
6. **Cubierta** — faldón con `Loft` o `Sweep1`, espesor con `OffsetSrf`, alero por extensión.
7. **Cortes** — `ClippingPlane` A-A y B-B; `ClippingSections` para D-1; `Section Style` por capa.
8. **Make2D** — vista paralela, `Projection: View`, líneas ocultas, intersecciones de planos; `CAD-BASE` oculta.
9. **Gráfica** — modo `Shaded` con sombras suaves para la axo; modo `Monochrome` para la lámina; grosores 0,50 / 0,25 / 0,13 mm.
10. **Lámina** — `Layout` A3, `Detail` a 1:50 y 1:10, cotas y textos en espacio papel, rótulo completo.
11. **PDF** — `Print` → Rhino PDF, página del layout, salida vectorial, revisión al 100 %.

---

## 8. Configuración punto a punto (para responder en orden)

> Estas son las decisiones que necesito tomar con vos antes de ejecutar. Cada punto tiene una opción recomendada. Las vamos respondiendo de a una, no todas juntas.

### Bloque A — Archivo y base

| # | Punto | Opciones | Recomendado |
|---|---|---|---|
| Q1 | Unidades | Metros / milímetros | **Metros** |
| Q2 | Tolerancia absoluta | 0,001 / 0,01 / 0,1 | **0,001 m (1 mm)** |
| Q3 | Template | `Small Objects - Meters` / template propio del estudio | **Template propio** si existe; si no, el de McNeel |
| Q4 | Ruta de guardado | `activos/rhino-general/` / otra | **`activos/rhino-general/`** |
| Q5 | Nombre y versión | `casa-didactica-v01.3dm` / otro | **`casa-didactica-v01.3dm`** |

### Bloque B — Casa y sistema

| # | Punto | Opciones | Recomendado |
|---|---|---|---|
| Q6 | Medidas de la casa | 8×12 m / otra | **8×12 m** |
| Q7 | Niveles | PB + PA + cubierta / PB + cubierta | **PB + PA + cubierta** |
| Q8 | Altura piso a piso | 2,70 m / 2,80 m / otra | **2,70 m** |
| Q9 | Modulación de montantes | 400 mm / 600 mm | **400 mm** para el curso; 600 mm en obra |
| Q10 | Sección de montantes | 2×4 / 2×6 | **2×6 exterior, 2×4 interior** |
| Q11 | Fundación | Platea / pilotines | **Platea con aislación perimetral** |

### Bloque C — Cortes y lámina

| # | Punto | Opciones | Recomendado |
|---|---|---|---|
| Q12 | Cortes generales | A-A + B-B / uno solo | **A-A y B-B** |
| Q13 | Detalle | D-1 muro-entrepiso-cubierta / D-2 fundación | **D-1 y, si entra, D-2** |
| Q14 | Escalas | 1:50 + 1:10 / 1:50 + 1:20 | **1:50 + 1:10** |
| Q15 | Lámina | A3 / A2 | **A3 horizontal** |
| Q16 | Cotas | En layout / en modelo | **En layout (espacio papel)** |
| Q17 | Rótulo | Estándar del estudio / simple del curso | **Simple del curso**, con campos completos |

### Bloque D — Gráfica

| # | Punto | Opciones | Recomendado |
|---|---|---|---|
| Q18 | Estilo de lámina | Monocromo + hatches / color | **Monocromo + hatches** |
| Q19 | Axonometría | Color por material / monocromo | **Color suave por material** |
| Q20 | Sombras | Sí en axo / sí en corte / sin sombras | **Sí en axo; corte con hatches limpios** |
| Q21 | Grosores | 0,50 / 0,25 / 0,13 mm / otro juego | **0,50 corte, 0,25 visible, 0,13 oculto** |
| Q22 | Textos y cotas | 2,5 mm / 3,5 mm | **2,5 mm cotas, 3,5 mm títulos** |

### Bloque E — Flujo de trabajo

| # | Punto | Opciones | Recomendado |
|---|---|---|---|
| Q23 | Configuración por MCP | Paso a paso con `s` / todo junto | **Paso a paso, mostrando el código antes** |
| Q24 | Guardado | Cada 20 min + backup / al final | **Cada 20 min + backup al cerrar cada módulo** |
| Q25 | Curso | En este mismo documento / anexo aparte | **Anexo dentro de este documento** |
| Q26 | Idioma de comandos | Inglés (nativo de Rhino) / traducción | **Inglés con explicación en español** |

---

## 9. Qué configuro yo por MCP y qué hacés vos en Rhino

### 9.1 Estado actual del puente

El puente MCP está cerrado: `get_rhino_scene_info` devuelve `WinError 10061`. Para abrirlo:

1. Abrir Rhino 8.
2. `Tools > Script > Run...` → `P:\00-repos\proyecto-pi\vault-arquitectura\scripts\rhino-mcp-server-rhino.py`.
3. Esperar el mensaje `RhinoMCP script loaded. Server started automatically.`
4. Verificar con `get_rhino_scene_info`.

### 9.2 División de tareas

| Tarea | Quién | Cómo |
|---|---|---|
| Unidades, tolerancia, capas y colores | MCP | `execute_code` con RhinoCommon |
| Vistas guardadas y planos de corte | MCP | `execute_code`, mostrando el código |
| Layout A3 y detalles | MCP + ajuste manual | `execute_code` para crear; ajuste fino en pantalla |
| Estilos de sección y hatches | MCP + diálogo | Se intenta por API; si Rhino 8.5 no lo expone, guía paso a paso |
| Modelado y decisiones de diseño | Vos | Rhino, con el curso |
| Impresión y revisión visual | Vos | `Print` y control de la lámina |

> Cada operación por MCP se muestra como código antes de ejecutarse y se aprueba con `s`. El puente corre Python dentro de Rhino: la regla es no ejecutar nada que no hayas visto.

---

## 10. Criterios de aceptación

- [ ] Unidades en metros y escala verificada contra una cota conocida.
- [ ] Sólidos cerrados (`ShowEdges`) y capas nombradas.
- [ ] Casa completa en volumen, con aberturas y cubierta.
- [ ] Testigo platform frame con todas las capas y espesores.
- [ ] Cortes A-A y B-B a 1:50, con hatch por material.
- [ ] Detalle D-1 a 1:10, legible en blanco y negro.
- [ ] Axonometría con sombras suaves y colores por material.
- [ ] Lámina A3 con rótulo completo y cotas.
- [ ] PDF vectorial revisado al 100 %.
- [ ] `.3dm` guardado y versionado en `activos/rhino-general/`.

---

## 11. Riesgos y decisiones abiertas

| Riesgo | Mitigación |
|---|---|
| El detalle 1:10 consume más tiempo que la casa | Modelar solo dos módulos y copiar el testigo |
| Los hatches no aparecen | Cada capa debe ser un sólido cerrado; `Section Style` por capa, no por objeto |
| El corte general se ensucia | `CAD-BASE` oculta, `Make2D` por vista guardada, `Intersect` donde falte línea |
| La escala del PDF sale mal | Verificar con una cota de 1,00 m impresa y medirla en el PDF |
| El archivo se vuelve pesado | Bloques para piezas repetidas; mallas solo en el entorno |
| Cambios de alcance | Congelar la casa didáctica en v01 y dejar las variantes para v02 |

**Decisiones abiertas:** medidas finales de la casa, cantidad de módulos del testigo, nivel de detalle de fijaciones (clavos, anclajes, herrajes), inclusiones de instalaciones y estilo del rótulo.

---

## 12. Referencias verificadas (200, 2026-10-25)

### Rhino 8 — modelado, secciones y láminas

| Fuente | URL |
|---|---|
| McNeel — *PushPull for Architects* | https://www.rhino3d.com/en/docs/guides/push-pull/push-pull-for-architects/ |
| McNeel — *Concept Modeling for Architects* | https://www.rhino3d.com/docs/guides/architecture/concept-modeling/ |
| McNeel — *Rhino in Architecture* (curso) | https://wiki.mcneel.com/training/rhino_for_arch/rhino_in_architecture_course |
| McNeel — *Architectural Drawings* | https://www.rhino3d.com/docs/guides/user-guide/drafting-architecture |
| McNeel — *Intro to Section Styles* | https://www.rhino3d.com/docs/guides/drafting/clipping-sectioning/intro-to-section-styles/ |
| McNeel — *ClippingPlane* (Rhino 8) | https://docs.mcneel.com/rhino/8/help/en-us/commands/clippingplane.htm |
| Rhino 8 — *2D Technical Drawing from 3D Model* | https://www.youtube.com/watch?v=YkS4kye5A34 |

### Platform frame — detalles técnicos

| Fuente | URL |
|---|---|
| AWC — *WCD1 Details for Conventional Wood Frame Construction* | https://boonelumber.com/wp-content/uploads/2022/02/AWC_Details_Conventional_Wood_Framing_Construction.pdf |
| AWC — *DCA3 Wood-Frame Wall and Floor/Ceiling Assemblies* | https://awc.org/resources/dca-3-fire-resistance-rated-wood-frame-wall-and-floor-ceiling-assemblies |
| WoodWorks — *Five-Story Light-Frame Wood Structure* | https://www.woodworks.org/wp-content/uploads/design_example_Five_Story_Light-Frame_Wood_Structure_Over-Podium_10.2025.pdf |

### Argentina — normativa y manuales

| Fuente | URL |
|---|---|
| Resolución 3/2018 — Entramado de Madera | https://www.argentina.gob.ar/normativa/nacional/resoluci%C3%B3n-3-2018-305849/texto |
| CIRSOC 601 — Reglamento Argentino de Estructuras de Madera | https://www.inti.gob.ar/assets/uploads/files/cirsoc/aprobados%20en%202016/CIRSOC601-completo.pdf |
| CIRSOC 601 — Manual de aplicación | https://www.inti.gob.ar/assets/uploads/files/cirsoc/aprobados%20en%202016/manual601-completo.pdf |
| INTI — Guía para el proyecto de estructuras de madera | https://www.inti.gob.ar/assets/uploads/files/cirsoc/aprobados%20en%202016/guia-CIRSOCMADERA-24ABRIL_compressed.pdf |
| INPRES — Disposición 2/2019 | https://www.inti.gob.ar/assets/uploads/files/madera-y-muebles/cem/disposicion-inpres-madera-y-steel-frame.pdf |

### Antecedentes internos

- `raw/research/2026-10-22-modelar-casa-rhino.md`
- `raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md`
- `scripts/axonometria-militar-rhino_notas.md` — incluye `crear_platform_frame()`, reutilizable.
- `proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp.md` — operación del puente.

---

## 13. Próximo paso

1. Leer este documento y marcar qué se cambia, qué se suma y qué se quita.
2. Responder los puntos Q1–Q26 en orden, de a uno.
3. Con las respuestas cerradas, abrir el puente MCP y ejecutar el setup con aprobación paso a paso.
4. Recién después crear el `.3dm` y empezar el módulo 0.

> **Ahora:** el documento queda para lectura e intercambio. Decime qué ajustamos y arrancamos por Q1 cuando quieras.
