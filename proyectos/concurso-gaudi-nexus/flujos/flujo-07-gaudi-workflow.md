---
tipo: flujo-curso
proyecto: concurso-gaudi-nexus
modulo: 7
slug: gaudi-workflow
titulo_curso: "The Gaudí Workflow"
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [mvp_04, comfyui, curso-ai-gaudi, modulo-7, gaudi, workflow, gaudi-nexus]
idioma: es
---

# Módulo 7 — The Gaudí Workflow (flujo del curso)

> Ficha de flujo del módulo 7 del curso AI×Gaudí, transcrita del video. Fuente verbatim: [[raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.es|transcripción ES]] · [[raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.en|EN]] · plan: [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro de workflows adapted]].

> Cierre del curso "AI×Gaudí" (Archademy). Fuentes: transcripción ES `raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.es.md` (454 cues) y EN `raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.en.md`, usadas en conjunto para resolver nombres propios y valores. Todo lo que sigue está anclado a un timestamp del video.

## Ficha

| Campo | Valor |
|-------|-------|
| **Duración** | 00:35:42 (pista de subtítulos: 00:35:37,168 → 00:35:42,130) — último turno hablado en [00:35:37] |
| **Idioma** | Video en inglés con subtítulos EN y ES (el vault guarda ambas transcripciones) [00:00:00] |
| **Profesor / figura central** | Thomas Nelissen presenta el módulo y conducts la demo; **Cas Esbach** (SCAD; antes arquitecto en BIG y MVRDV; miembro del jurado del concurso) hace la apertura conceptual sobre Gaudí [00:00:32]–[00:01:28], [00:01:38] |
| **Tema** | El "workflow Gaudí": convertir una volumetría 3D propia en un render fotorrealista aplicando la **lógica constructiva** de Gaudí, no su estética, mediante dos pasos image-to-image separados (geometría / estética) [00:08:19]–[00:08:35], [00:17:14]–[00:17:44] |

## Objetivo del módulo

Cerrar el curso mostrando el flujo completo de dos pasos que lleva de un modelo 3D propio a una imagen fotorrealista: el paso 1 fija la geometría con la lógica constructiva de Gaudí (agente + Nano Banana 2) y el paso 2 aplica textura y realismo (LoRA `rhino-to-image`) [00:17:14]–[00:17:44].

## El flujo, paso a paso

| # | Acción | Nodo / herramienta (nombre EXACTO en ComfyUI) | Valores que dice el video | Prompt / fórmula | Timestamp |
|---|--------|-------------------------------------------|---------------------------|------------------|-----------|
| 1 | Construir un modelo 3D propio (volumetría) y tomarle una captura | Captura de pantalla del modelo 3D — el comando de exportación **no se dice en el video** | "puede ser muy vago o muy abstracto" | — | [00:08:40]–[00:09:05] |
| 2 | Exportar el "asistente Gaudí" del tablero del curso | Miro → **"export as markdown"** (se descarga un `.md`) | "ahí encontrarás todo lo que necesitas" | — | [00:09:34]–[00:10:58] |
| 3 | Abrir el `.md`, seleccionar todo y copiar | Bloc de notas ("clic derecho, abrir con el Bloc de notas") | "mantiene mejor la estructura" que copiar el JSON crudo | — | [00:11:07]–[00:11:37] |
| 4 | Crear el proyecto en el LLM y pegar las instrucciones | LLM (el video menciona **Claude**): proyecto nuevo **"Rhino to Image Gaudí"** → Instructions → **"save instructions"** | nombre del proyecto: `Rhino to Image Gaudí` | INSTRUCTION.md variante B (ver sección de prompts) | [00:10:18]–[00:11:42] |
| 5 | Arrancar el agente con la captura del modelo | escribir **`start`** + imagen adjunta | — | `start` | [00:11:44]–[00:12:09] |
| 6 | Responder el interrogatorio: programa / uso | — | "museo del clima al aire libre, de varias plantas" / "edificio residencial y de uso mixto" | ver bloque de fragmentos | [00:09:17]–[00:09:28], [00:12:19]–[00:12:42] |
| 7 | Fijar la **Escala Gaudí** (dial de intensidad) | — | **7** en el primer ejemplo; **8** en el segundo | dial 0–10 | [00:12:47]–[00:13:01], [00:26:16] |
| 8 | Elegir los movimientos principales | — | "me quedo con mis tres propuestas" | — | [00:13:04]–[00:13:20] |
| 9 | Cargar contexto: muros, imágenes de referencia, programa, ubicación, dimensiones | — | "altura libre de tres metros"; "cada planta son tres metros"; "Barcelona" | ver bloque de fragmentos | [00:13:28]–[00:13:46], [00:24:00]–[00:26:08], [00:29:41]–[00:29:49] |
| 10 | El agente genera el prompt | — | "está generando otro prompt" | prompt según INSTRUCTION.md | [00:26:41] |
| 11 | Montar el grafo del paso 1 en ComfyUI | **`Load Image`** | se carga la misma imagen de la volumetría | — | [00:14:10]–[00:14:19] |
| 12 | Agregar el modelo de imagen | **`Nano Banana 2`** | "es el modelo que vamos a usar en este paso" | — | [00:14:24] |
| 13 | Conectar la imagen al modelo | — | — | — | [00:14:30]–[00:14:37] |
| 14 | Agregar el nodo de guardado | **`Save Image`** | — | — | [00:14:40]–[00:14:44] |
| 15 | Agregar el comparador antes/después | **`Compare Images`** (nodo de Comfy) | entradas **`Image A`** / **`Image B`** | — | [00:14:48]–[00:14:58] |
| 16 | Configurar el paso | Ajustes del nodo de imagen: resolución, nivel de razonamiento, relación de aspecto | resolución **2K** · **nivel de razonamiento "high"** · "el resto lo dejamos igual" · relación de aspecto opcional | — | [00:15:27]–[00:15:36] |
| 17 | Pegar el prompt y correr | **`run`** | — | prompt del agente Gaudí | [00:15:40]–[00:15:49] |
| 18 | Verificar el resultado | — | "la geometría principal se sigue casi exactamente"; "todo el relleno de los planos… ahí es donde se pone interesante" | — | [00:15:54]–[00:16:24] |
| 19 | Repetir la corrida para comparar | **`run`** (segunda vez) | "siempre recomiendo ejecutarlo otra vez para ver la diferencia" | — | [00:17:53] |
| 20 | Descargar la imagen y publicarla en el tablero | `Save Image` → descarga → Miro | — | — | [00:18:05]–[00:18:12], [00:09:46]–[00:09:58] |
| 21 | Pedir el prompt de materialidad (paso 2) | Proyecto **"Rhino to Image"** del LLM: volumetría generada + imagen de material | material de ejemplo: **mármol rojo** | "edificio residencial en Barcelona" | [00:19:05]–[00:19:57] |
| 22 | Traer el workflow del paso 2 a ComfyUI | arrastrar y soltar la imagen descargada (lleva el workflow incrustado) | "abres el workflow que usé para generar esta" | — | [00:15:05]–[00:15:23], [00:20:11]–[00:20:30] |
| 23 | Reemplazar el prompt de materialidad | nodo de prompt del workflow (nombre del nodo **no dicho en el video**) | "Como esas dos fueron también la entrada del agente, el prompt ya está listo" | prompt de materialidad del agente | [00:20:33]–[00:20:57] |
| 24 | Elegir la variante de LoRA | nodo de LoRA del workflow (nombre del nodo **no dicho en el video**) | "aquí eliges qué LoRA usas, el premium o el básico"; usa el **premium** | — | [00:21:01]–[00:21:08] |
| 25 | Correr el paso 2 | **`run`** | "aplicó el material exactamente sobre la geometría"; "en este paso la geometría no cambia, solo se aplica el material" | — | [00:21:16]–[00:21:27] |
| 26 | Elegir el encuadre del render | — | "un detalle de fachada como este, o un primer plano, funciona mejor"; "desde lejos, mostrando todo el edificio, no es el mejor enfoque" | — | [00:21:29]–[00:22:24] |
| 27 | (2.º ejemplo) Cambiar la referencia estética por una fachada de otro arquitecto | `Load Image` (referencia) | "una fachada muy expresionista… el azul y el color conecten un poco más con Gaudí" | — | [00:27:19]–[00:27:48] |
| 28 | Volver al workflow Rhino to Image, completar el prompt y correr | **`run`** | "residencial, el lateral… loggias" | ver bloque de fragmentos | [00:28:33]–[00:30:05], [00:30:24]–[00:31:11] |
| 29 | Descargar el resultado final | `Save Image` | "Siempre los puedes descargar así" | — | [00:32:06] |

## Modelos, LoRA y checkpoints

| Nombre | Qué dice el video de él | Strength / dial | Cuándo lo recomienda | Timestamp |
|--------|------------------------|-----------------|----------------------|-----------|
| **Nano Banana 2** | Modelo de imagen del **paso 1**: "el modelo que vamos a usar en este paso"; el que "considera más gaudiniano" el modelo 3D según el agente | **no dicho en el video** | Siempre en el paso 1 (geometría) | [00:14:24], [00:16:08] |
| **LoRA `rhino-to-image` premium** | "aquí eliges qué LoRA usas, el premium o el básico. Yo… lo voy a hacer con el premium"; "el de abajo está disponible en mi web" | **no dicho en el video** (no da valor de strength) | Paso 2, cuando se quiere ver el mejor resultado | [00:21:01]–[00:21:08], [00:34:17]–[00:34:36] |
| **LoRA `rhino-to-image` basic** | "Incluido en el curso está el básico, que encontrarás en la carpeta" | **no dicho en el video** | Paso 2, alternativa incluida en el material del curso | [00:34:17]–[00:34:23] |
| **LoRA de la Fundació Antoni Gaudí** | **No nombrado en el video.** El módulo menciona solo los dos LoRA `rhino-to-image` (basic y premium) | no dicho en el video | no dicho en el video | — |
| **Escala Gaudí / dial de intensidad 0–10** | Pregunta del agente: "¿Cuánto queremos que se parezca a Gaudí? Moderado, Gaudí estructural completo, casi máximo o sin límites" | **7** (1.er ejemplo) · **8** (2.º ejemplo) | En cada interrogatorio, antes de generar el prompt | [00:12:47]–[00:13:01], [00:26:16] |
| **Modelo base del workflow Rhino-to-Image** (FLUX.2 klein 9B) | **no dicho en el video**: el módulo solo llama "workflow Rhino to Image" al flujo heredado del módulo 3 | no dicho en el video | — | — |
| **Referencia estética** (material o fachada de otro arquitecto) | Entra en el paso 2 como "la referencia que le demos"; puede ser un material o una fachada ajena | no aplica | Paso 2, siempre | [00:17:39]–[00:17:44], [00:27:19]–[00:27:48] |

## Prompts y fórmulas

### 1. El comando de arranque del agente

```
start
```
[00:12:04] — seguido de la captura del modelo 3D [00:11:44].

### 2. La regla de estructura que enseña el video

El video define la cadena como **dos pasos image-to-image** y separa explícitamente geometría de estética:

```
PASO 1  geometría →  se fija aquí (agente Gaudí + Nano Banana 2)
PASO 2  estética    →  se aplica después    (referencia de material/fachada + LoRA)

"Tomamos el hecho de generar una imagen y lo partimos en geometría y estética.
 Y la geometría se basa entonces en Gaudí, y la estética se basa en la referencia que le demos."
```
[00:17:14]–[00:17:44], reformulado en la lámina de Miro [00:33:23]–[00:33:41].

Y el criterio de fondo, explícito en la apertura de Cas Esbach: **transferencia conceptual** (lógica constructiva) por encima de **transferencia estilística** (apariencia). "Entre copiar la apariencia y entender la lógica subyacente va a haber una brecha. Y esa es la que tenemos que cerrar" [00:05:38]–[00:05:54]. "No vamos a intentar reducir la esencia de Gaudí a, por ejemplo, un LoRA. Vamos a intentar encontrar la esencia de Gaudí en el siguiente workflow" [00:08:19]–[00:08:32]. "El LoRA está tan bien entrenado que sigue la geometría exactamente" [00:31:21]–[00:31:31].

### 3. Fragmentos literales que el profesor usa como respuesta al agente

Estos son los prompts tal como los dicta en la demo (no son un prompt completo: el prompt completo lo compone el agente):

```
# programa / uso (ejemplo 1)
"esto es un museo del clima al aire libre, de varias plantas,
 y la estructura está hecha de esta piedra natural"                     [00:09:21]–[00:09:28]

"es un edificio residencial y de uso mixto"                             [00:12:34]–[00:12:42]

# escala y dimensiones (ejemplo 2)
"la altura libre es de tres metros"                                    [00:25:43]–[00:26:01]
"cada planta son tres metros" [00:29:47]–[00:29:49]
"¿Dónde está ubicado el edificio? — Barcelona"                          [00:29:41]–[00:29:43]

# lectura de la imagen de referencia
"el gris es la estructura principal"                                   [00:24:03]
"la parte cian son ventanas"                                           [00:25:08]
"son las barandillas de los balcones"                                  [00:24:38]–[00:24:43]

# elementos sagrados
"el ritmo de la fachada y las dimensiones son sagrados"                  [00:25:27]–[00:25:37]

# materialidad (paso 2)
"edificio residencial en Barcelona"                                    [00:19:43]–[00:19:50]
"residencial, el lateral" + "loggias, no sé, lo que quieras poner"      [00:28:43]–[00:29:02]
```

### 4. INSTRUCTION.md — variante B "Rhino-to-Gaudi" (la estructura que instala el video)

El video no lee el INSTRUCTION.md en voz alta: lo instala desde Miro ("export as markdown") y lo usa como prompt de sistema del agente [00:10:02]–[00:10:09], [00:10:43]–[00:11:42]. La estructura está extraída y archivada en el vault: `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-gaudi-instruction-md.md`.

```
Massing → Sculptural Clay Reinterpretation — VARIANT B (names Gaudí)

A/B test variant. Identical to INSTRUCTION.md (variant A, name-free) except thisvariant may name Antoni Gaudí and his built works in the emitted prompt, letting
the image model tap its trained knowledge directly. Everything else — template
structure, morph scale, camera lock, clay style, word budget — is kept identical
so the only test variable is the name.

Workflow: color-coded Rhino massing screenshot → color-key + interview →
structural re-sculpt (this project) → hyperreal pass via the trained Flux.2 Klein edit LoRA.

The clay is the base for the edit LoRA: keep it clean, monochrome, edge-legible,
camera + footprint 1:1.

The two rules that make or break the render — GENERATIVE, not descriptive:
  1. Every move must make new structure appear.
     Never write "X becomes [what it already looks like]" — that recolors instead of transforming.
  2. Force emergence:
       openings     → tall parabolic voids
       joints       → material fans into ribbed vault clusters
       supports     → branch like trees
       flat soffits → chains of compression vaults

The highest-yield signal is material fanning/branching at the joints.

REVEAL and POPULATE the interior.
Remove glazing/void planes and open each bay into a deep programmed interior with
people and program props at true ceiling scale, same near-white clay. This is what
makes the branching columns and vaults actually appear.

Gaudí scale — morph-intensity dial (0–10, default 7)
Sets how far surfaces and supports are re-sculpted.
Fixed at every level: camera / perspective, footprint, floor count, program, bay rhythm.
In this variant the scale is named openly in the emitted prompt.
  0–2   supports rake, faces bow into shallow saddles, lintels arch slightly.
  3–5   catenary arches, parabolic openings, undulating soffits, tapering supports.
  6–8   full catenary ribs; joints fan into vault clusters; tree-columns; opened vaulted interior; hyperboloid-throat openings. Buildable but unmistakably
        Gaudí.  (default 7)
  9–10  maximal: la masa se disuelve en un organismo continuo
        (nave de la Sagrada Família / cripta de la Colònia Güell)
```
(Fuente: archivo del vault `prompt-rhino-to-gaudi-instruction-md.md` + `03-nodos-WFrhino_to_image.md`. El video solo confirma el uso del dial: "ponemos en las instrucciones del proyecto siete" [00:12:55], "Escala Gaudí. Pongámosla en ocho por ahora" [00:26:16], y que "esto es lo que a mí me parece bien y lo que yo creo que es la lógica constructiva de Gaudí" [00:32:26].)

### 5. El dial de intensidad 0–10 en la práctica del video

| Valor | Comportamiento (INSTRUCTION.md) | Uso en el video |
|-------|-------------------------------|-----------------|
| 0–2 | Soportes inclinados, superficies abombadas en sillas shallow, dinteles arqueados | no elegido |
| 3–5 | Arcos catenarios, aberturas parabólicas, intradorsos ondulantes, soportes afilados | no elegido |
| **6–8 (default 7)** | Costillas catenarias completas · juntas que se abren en ramificaciones de bóvedas · columnas arbóreas · interior abovedado abierto · bocas hiperboloides. Construible pero inconfundiblemente Gaudí | **7** en el primer ejemplo [00:12:55]; **8** en el segundo [00:26:16] |
| 9–10 | La masa se disuelve en un organismo continuo | no elegido |

Nivel 9–10 = "casi máximo o sin límites", que el video enumera como opción del dial [00:12:50]–[00:12:52].

## Reglas, buenas prácticas y trampas

- La IA se usa como herramienta para entender la lógica estructural y la forma [00:06:08]–[00:06:15]; la lógica constructiva de Gaudí es el objetivo, y su estética queda como segundo plano [00:05:57]–[00:06:08].
- La geometría se fija en el paso 1 y la estética se aplica en el paso 2: la separación de las dos cosas es lo que hace que el resultado sea utilizable [00:17:14]–[00:17:44].
- La parte de Gaudí vive sobre todo en el primer paso: "en este workflow, lo de Gaudí está sobre todo en este primer paso" [00:32:09].
- El paso 2 es esencialmente el workflow Rhino-to-Image del módulo 3, reutilizado tal cual [00:19:05]–[00:19:11].
- La logica del LoRA funciona mejor en primer plano o detalle de fachada que en vista lejana del edificio completo [00:21:29]–[00:22:24].
- El encuadre se resuelve a la altura de los ojos, porque el LoRA está entrenado con imágenes y fotografías tomadas a esa altura [00:35:00]–[00:35:07].
- La vista general del edificio deja lugar a la entrada, el detalle o el primer plano como encuadre recomendado [00:34:38]–[00:34:56].
- El prompt que genera el LLM se lee siempre: "a veces el LLM alucina y escribe cosas rarísimas. Y entonces te pones a buscar el fallo cuando es solo el prompt" [00:26:43]–[00:26:58].
- La respuesta al agente es lo que dirige el resultado: "cuanto mejor sea tu entrada, cuanta más información, mejor será el resultado" [00:30:01]–[00:30:05].
- El agente se responde con el máximo de especificidad: "Te recomiendo mucho que seas lo más específico posible. Añade mucha información aquí" [00:13:28]–[00:13:46].
- Las dimensiones van al prompt: sin cotas, el modelo no entiende la escala [00:25:43]–[00:26:08].
- Las instrucciones son el punto de partida personalizable: "no te limites a copiarlo y usarlo: cámbialo… cuanto más personalices este prompt, mejor será. Y mejor reflejará lo que tú entiendes por Gaudí" [00:32:31]–[00:33:02].
- La interpretación del enfoque biomimético de Gaudí se aplica al proyecto propio [00:21:49]–[00:22:02].
- Cada resultado se contrasta con una segunda corrida del mismo paso: "yo siempre recomiendo ejecutarlo otra vez para ver la diferencia" [00:17:53].
- Las imágenes descargadas llevan el workflow incrustado: se arrastran a ComfyUI y el grafo aparece tal cual [00:15:05]–[00:15:23], [00:20:16]–[00:20:30].
- El nodo `Save Image` es la red de seguridad del paso 1: permite recuperar el resultado aunque otro nodo no se haya ejecutado [00:28:14]–[00:28:19].
- El botón de regenerate del agente es idempotente: vuelve a hacer exactamente lo mismo y vuelve a preguntar lo mismo [00:25:01]–[00:25:18].
- La organización es parte del método: dos workflows en ComfyUI y dos proyectos en el LLM conviven, así que hace falta un sistema propio de orden [00:29:20]–[00:29:37].
- El tablero del curso es el punto de publicación: ahí van todos los resultados de la demo y los ejemplos [00:09:46]–[00:09:58], [00:31:31]–[00:31:45].
- La lectura del prompt generado es parte del criterio del arquitecto: el papel pasa de la producción al juicio [00:06:47]–[00:07:12].
- La IA es la maqueta colgante de Gaudí de hoy: un sistema capaz de generar posibilidades, con el criterio humano conservado [00:07:17]–[00:07:27].
- La fuente de la forma es la eficiencia del sistema estructural, y la forma es la respuesta a un problema físico [00:04:57]–[00:05:17].

## Qué NO dice el video (para implementarlo)

| Vacío | Estado |
|-------|--------|
| Archivo/modelo exacto de **Nano Banana 2** en el dropdown de ComfyUI (el video solo dicta el nombre que se escribe en el buscador) | no dicho en el video |
| **Sampler, scheduler, steps, cfg, denoise y seed** del paso 1 (Nano Banana 2) | no dicho en el video |
| **Strength del LoRA** (`rhino-to-image` premium o basic): el video elige variante, nunca da valor numérico | no dicho en el video |
| **Modelo base** del workflow Rhino-to-Image (el video no menciona FLUX.2 ni klein) | no dicho en el video |
| **Nombre exacto de los nodos** del paso 2 (nodo de LoRA, nodo de prompt) | no dicho en el video |
| **URL del LoRA premium**: el video solo dice "está disponible en mi web" | no dicho en el video |
| **LoRA de la Fundació Antoni Gaudí**: no aparece nombrado en el módulo | no dicho en el video |
| **Texto íntegro del INSTRUCTION.md**: el video lo instala y lo usa, no lo lee | no dicho en el video (está en el tablero y en el vault) |
| **Resolución en píxeles** del ajuste "2K" | no dicho en el video |
| **Relación de aspecto** concreta: el video la deja opcional | opcional, no dicho en el video |
| **Comando de exportación desde Rhino** (la captura del modelo 3D): el video solo dice "tomamos una captura" | no dicho en el video |
| **Tiempo de ejecución**: "siempre tarda unos 30 segundos" | [00:27:07]–[00:27:11] |
| **Formato de lámina** (A1), **peso** (15 MB), **formato de archivo** (JPEG), **fecha de entrega** (16/12/2026) | no dicho en el video |
| **Número de láminas o de imágenes** a entregar, y **criterios de evaluación** del concurso | no dicho en el video |
| **Relación entre el dial0–10 y las bandas textuales** (0–2, 3–5, 6–8, 9–10): el video da el número, las bandas están en el INSTRUCTION.md | no dicho en el video (ver vault) |

## Qué aporta al concurso AIxGaudi ("The Gaudí Nexus")

1. **La ideación inicial es del equipo participante**: el flujo arranca con un modelo 3D propio, que puede ser "muy vago o muy abstracto", y el concurso se juega ahí [00:08:40]–[00:09:05].
2. **Es el módulo que entrega el render final**: termina la cadena completa Rhino → geometría gaudiniana → material → render fotorreal [00:33:23]–[00:33:41].
3. **Define el criterio con el que va a mirar el jurado**: Cas Esbach es miembro del jurado y fija la vara — lógica constructiva sobre apariencia [00:01:38], [00:05:57]–[00:06:15].
4. **El dial 0–10 es el mando de coherencia**: habilita calibrar cuánto Gaudí entra en la propuesta y dejar registro de esa decisión [00:12:47]–[00:13:01], [00:26:16].
5. **Separa lo propio de lo prestado**: la geometría es del equipo, la estética viene de la referencia que el equipo elija — y esa elección (material propio, fachadas de otros arquitectos) es una decisión de proyecto [00:17:39]–[00:17:44], [00:27:19]–[00:27:48].
6. **Las instrucciones son la entrega conceptual**: personalizar el INSTRUCTION.md es el lugar donde el proyecto define su propia versión de Gaudí [00:32:31]–[00:33:02].
7. **Documenta el proceso en el tablero del curso**: el material de la demo y los ejemplos quedan publicados y son re-utilizables por el equipo [00:09:46]–[00:09:58], [00:31:54]–[00:32:04].
8. **Deja la capa fotorreal lista para la lámina**: el paso 2 entrega la imagen con material y realismo, lista para componer en A1 [00:34:12]–[00:34:27].

## Checklist de entrega que el video propone

**Preparación del flujo**

- [ ] Modelo 3D propio construido y capturado [00:08:40]–[00:09:05]
- [ ] Asistente Gaudí exportado desde Miro como **markdown** y pegado como *instructions* de un proyecto nuevo del LLM llamado **"Rhino to Image Gaudí"** [00:10:18]–[00:11:42]
- [ ] Agente arrancado con `start` + captura [00:11:44]–[00:12:09]
- [ ] Interrogatorio completo: programa, escala Gaudí, movimientos principales, elementos sagrados, ubicación, dimensiones [00:12:19]–[00:26:28]
- [ ] Prompt generado **leído** antes de pegarlo [00:26:43]–[00:26:58]

**Paso 1 — geometría (ComfyUI + Nano Banana 2)**

- [ ] `Load Image` con la captura de la volumetría [00:14:10]–[00:14:19]
- [ ] Nodo **Nano Banana 2** conectado a la imagen [00:14:24]–[00:14:37]
- [ ] `Save Image` agregado [00:14:40]
- [ ] `Compare Images` con `Image A` / `Image B` [00:14:48]–[00:14:58]
- [ ] Ajustes: resolución **2K**, nivel de razonamiento **high**, resto sin tocar [00:15:27]–[00:15:30]
- [ ] Prompt del agente pegado → `run` [00:15:40]–[00:15:49]
- [ ] Segunda corrida para comparar [00:17:53]
- [ ] Imagen descargada y subida al tablero [00:18:05]–[00:18:12]

**Paso 2 — estética y realismo (workflow Rhino-to-Image)**

- [ ] Prompt de materialidad pedido al proyecto Rhino to Image con volumetría + material [00:19:18]–[00:19:57]
- [ ] Workflow del paso 2 traído arrastrando la imagen descargada [00:20:16]–[00:20:30]
- [ ] Prompt de materialidad reemplazado [00:20:33]–[00:20:57]
- [ ] Variante de LoRA elegida (premium o basic) [00:21:01]–[00:21:08]
- [ ] `run` y verificación de que la geometría quedó intacta [00:21:16]–[00:21:27]
- [ ] Encuadre elegido: detalle de fachada o primer plano [00:21:37]–[00:22:24]
- [ ] Referencia estética evaluada (material propio o fachada de otro arquitecto) [00:27:19]–[00:27:48]
- [ ] Prompt del paso 2 ampliado con contexto (uso, ubicación, escala, loggias) [00:28:43]–[00:29:49]
- [ ] `run` → vista previa → resultado final [00:30:24]–[00:31:11]
- [ ] Resultado descargado y publicado junto con su imagen de referencia [00:31:31]–[00:32:06]

**Puesta a punto del material entregado**

- [ ] Instrucciones leídas y customizadas con la lectura personal de Gaudí [00:32:16]–[00:33:02]
- [ ] Imágenes con el workflow incrustado guardadas para reimportar en ComfyUI [00:15:05]–[00:15:23]
- [ ] Ejemplos del tablero probados por el equipo [00:31:54]–[00:32:04]
- [ ] Altura de ojo respetada en el encuadre final [00:35:00]–[00:35:19]

> Formato de lámina, peso, tipo de archivo y fecha de entrega: **no dicho en el video**. El módulo cierra con "mucha suerte con el concurso" [00:35:37]; los datos de entrega (A1 online, máx. 15 MB, JPEG, 16/12/2026) están en el briefing y en `proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi.md`.

## Conceptos relacionados

- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/01-index|WF-rhino-to-image]] — el flujo del módulo 3 que el paso 2 reutiliza
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-gaudi-instruction-md|INSTRUCTION.md Rhino-to-Gaudi (variante B)]] — la instrucción que instala el video
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/03-nodos-WFrhino_to_image|Nodos de WF-rhino-to-image]] — grafo, dial0–10 y strength del LoRA
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-esqueleto-json|Esqueleto JSON del prompt]] — la forma que toma el prompt del agente
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|LoRA rhino-to-image]] — ficha del LoRA (rank 16, FLUX.2 klein 9B, sin trigger word)
- [[wiki/glosario/software/flux2-klein-9b|FLUX.2 klein 9B]] — modelo base del paso 2
- [[wiki/glosario/software/comfyui|ComfyUI]] — nodos y flujo del estudio
- [[wiki/glosario/software/rhino|Rhino]] — de dónde sale la volumetría
- [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|Extracción del material del curso]] — dónde vive el tablero, el INSTRUCTION.md y los LoRA
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|Reglas de workflows ComfyUI]] — nomenclatura y convenciones de grafo
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — playbook operativo
- [[raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.es|Transcripción ES — Módulo 7]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-image.es|Transcripción ES — Módulo 3 (img2img)]]

## Cómo lo adaptamos

| Lo que hace el curso | Lo que hacemos nosotros | Por qué |
|---------------------|------------------------|---------|
| Paso 1: la geometría se re-esculta con lógica constructiva de Gaudí mediante el nodo partner **Nano Banana 2** dentro de ComfyUI | Lo resolvemos con **FLUX.2 klein 9B en modo edición** en el pod, alimentado por el prompt que produce el agente a partir del **INSTRUCTION.md variante B** que ya está archivado en el vault | El modelo base del estudio entra con licencia no comercial y memoria suficiente para editar; el INSTRUCTION.md archivado es la fuente de verdad del prompt, sin depender del tablero |
| Paso 2: estética y realismo con el LoRA sobre la geometría ya fijada | Reutilizamos el **workflow Rhino-to-Image con el LoRA**, ya construido y validado en `n_05-rhino-mcp/WF-rhino-to-image` | Es el flujo que ya liga la referencia de geometría con la de material; reutilizarlo evita reconstruir el grafo y sus ajustes |
| El dial de intensidad 0–10 del agente ("Escala Gaudí") | Lo documentamos como **parámetro de proyecto**, con su tabla de bandas (0–2, 3–5, 6–8, 9–10) y el valor por defecto 7, registrado junto a cada render | El dial queda como decisión documentada del concurso y no como un número que se pierde en la conversación con el LLM |
| El asistente Gaudí se exporta del tablero de Miro y se instala como *instructions* de un proyecto del LLM | Se exporta del tablero como **markdown** y se instala como **instrucciones de un proyecto de Claude**, con nombre propio del concurso | El archivo ya está en el vault y Claude es el LLM con sesión disponible: la instalación queda versionada y reutilizable por el equipo |
| Las imágenes descargadas conservan el workflow incrustado y se vuelven a importar arrastrándolas | Cada render descargado se conserva como **portador del workflow**: se arrastra a ComfyUI para recuperar el grafo exacto y se archiva en la carpeta del proyecto | El grafo viaja con el archivo: cualquier corrección posterior se retoma desde la configuración que generó la imagen |
| El paso 1 se configura con resolución **2K** y nivel de razonamiento **"high"** | Replicamos **2K + razonamiento "high"** en la configuración de edición de FLUX.2 klein 9B | Son los valores con los que el curso valida la calidad del reescultado; se conservan como línea base de calidad del render |
| El LoRA `rhino-to-image` premium queda **pendiente de compra** | La producción se cubre con el **basic** (120,8 MB, ya en disco) y el premium entra cuando se resuelva la descarga desde la web del profesor | El basic ya está disponible y es el que permite producir hoy; el premium queda anotado como mejora de calidad para la etapa de cierre |

## Checks contra el criterio del jurado

- Este módulo es el que mejor satisface el criterio que fija el jurado — lógica constructiva por encima de apariencia, según Cas Esbach en el módulo 6 — y por eso es el que sostiene la entrega.
- La geometría se re-esculta con **reglas constructivas** (catenarias, aberturas parabólicas, columnas arbóreas, bóvedas de compresión) y no con imitación de estilo [00:04:57]–[00:05:17], [00:06:08]–[00:06:15].
- El **dial 0–10** deja registro de cuánta lógica de Gaudí entra en la propuesta, con valor por defecto 7 [00:12:47]–[00:13:01], [00:26:16].
- El **prompt generado por el agente se lee antes de pegarlo**, para detectar alucinaciones antes de que lleguen al render [00:26:43]–[00:26:58].
- La **estética llega después** y es una elección de proyecto documentada: material propio o fachada de otro arquitecto, asumida como tal [00:17:39]–[00:17:44], [00:27:19]–[00:27:48].
- El **encuadre se resuelve a la altura de los ojos y en detalle de fachada**, que es donde el LoRA rinde [00:21:29]–[00:22:24], [00:35:00]–[00:35:19].
- Pendiente: la transcripción del módulo 6 (mesa redonda) todavía no está transcrita, así que el criterio del jurado queda documentado con el material del módulo 7 y con la apertura de Cas Esbach.
