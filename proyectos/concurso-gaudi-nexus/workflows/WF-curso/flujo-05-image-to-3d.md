---
tipo: flujo-curso
proyecto: concurso-gaudi-nexus
modulo: 5
slug: image-to-3d
titulo_curso: "Image-to-3D"
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [mvp_04, comfyui, curso-ai-gaudi, modulo-5, image-to-3d, 3d, gaudi-nexus]
idioma: es
---

# Módulo 5 — Image-to-3D (flujo del curso)

> Ficha de flujo del módulo 5 del curso AI×Gaudí, transcrita del video. Fuente verbatim: [[raw/yt/transcripts/2026-10-21_mux-image-to-3d.es|transcripción ES]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-3d.en|EN]] · plan: [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro de workflows adapted]].

## Ficha

| Dato | Valor |
|------|-------|
| **Duración total de la pista** | 00:19:32 → 00:19:33 (19 min 33 s) [00:00:02]-[00:19:32] |
| **Idioma** | Subtítulos en español (track `es`); el módulo tiene track `en` equivalente. El curso se publica en inglés con subtítulos |
| **Profesor** | No dicho en el video. Según el material del curso archivado en el vault: Thomas Nelissen (Davis AI) — el módulo 7 es de Cas Esbach (SCAD) |
| **Modalidad** | Demo en vivo, sin PowerPoint: "este va a ser rápido, y te voy a mostrar los ejemplos en directo" [00:00:09]-[00:00:15] |
| **Tema** | Convertir una imagen 2D en geometría 3D con nodos de Hunyuan3D y workflows de Tripo, con un paso intermedio de preparación de imagen en ComfyUI (Nano Banana Pro). |
| **Cierre** | El resultado vuelve a Rhino, se escala a la cota real del producto y se documenta con capturas en Miro [00:03:51]-[00:04:10], [00:19:19]-[00:19:26] |

## Objetivo del módulo

Llevar una imagen 2D hasta un modelo 3D medible en Rhino, y entender que la calidad del 3D se decide en la **preparación de la imagen de entrada**, no en el modelo 3D.

## El flujo, paso a paso

| # | Acción | Nodo / herramienta (nombre EXACTO) | Valores que dice el video | Prompt / fórmula | Timestamp |
|---|--------|-------------------------------------|----------------------------|------------------|-----------|
| 1 | Importar la imagen 2D en el workflow (foto de un mueble) | ComfyUI · nodo **Hunyuan3D** | — | — | [00:00:42]-[00:00:49] |
| 2 | Configurar el nodo de 3D | **Hunyuan3D** | model `3.0` · face count `500k` (se corrige en el audio: "50k… Perdón, 500k") · `low poly` | — | [00:00:49]-[00:01:04] |
| 3 | Elegir el tipo de polígono (calidad vs. costo) | **Hunyuan3D** | `geometry` = más barato · `normal` = 105 créditos · `low poly` = 126 créditos · `normal` y `geometry` tardan más | — | [00:01:04]-[00:01:16] |
| 4 | Decidir si hace falta el 3D | Rhino (criterio) | Forma simple → se modela a mano; forma compleja → image-to-3D | "¿Para qué necesito un modelo 3D de esto? Lo puedo modelar yo mismo en Rhino" | [00:01:32]-[00:01:58] |
| 5 | Exportar el modelo | **Export** → **Export Model** | `OBJ` — "Yo siempre uso OBJ porque está bastante bien soportado" | — | [00:02:08]-[00:02:20] |
| 6 | Importar en el software 3D | Rhino: Archivo → Importar | Los ajustes de importación no son relevantes en este flujo | — | [00:02:24]-[00:02:47] |
| 7 | Encuadrar para comparar | Rhino, comando `zoom` | Se arrastra un rectángulo pequeño y hace zoom | — | [00:02:50]-[00:03:01] |
| 8 | Poner la escala real | Rhino + ficha/web del producto | Ej.: "el diámetro es de 150 centímetros" → se escala y "esto mide 1,5" | — | [00:03:12]-[00:03:51] |
| 9 | Documentar el resultado | **Miro** | Captura pegada al lado del material | — | [00:03:55]-[00:04:10] |
| 10 | Repetir con un mueble más complejo | **Hunyuan3D** (mismo workflow) | Sale `low poly` (redujo todas las caras) y "perfectamente simétrico" | — | [00:04:29]-[00:05:08] |
| 11 | Workflow multiview | **Tripo multiview to model** (plantilla "Tripo") | Requiere **al menos dos imágenes** del mismo modelo: vista frontal + vista trasera | — | [00:05:43]-[00:06:43] |
| 12 | Diagnosticar el ruido de entrada | — | El 3D arrastra el contexto: coches, edificios vecinos, vegetación | — | [00:06:46]-[00:07:19] |
| 13 | Listar las opciones de preparación | **Miro** (tablero del curso) | **Nueve** opciones distintas de preparación | — | [00:00:29]-[00:00:36], [00:07:27]-[00:07:32] |
| 14 | **Variante A** — borrar los detalles (opción 1) | ComfyUI + **Nano Banana Pro** | El resultado todavía deja ver edificios vecinos y árboles del fondo | "que parezca que todos los detalles han desaparecido / sin vegetación" | [00:07:49]-[00:08:48] |
| 15 | **Variante B** — maqueta de hormigón | **Nano Banana Pro** | "solo muestra la forma más básica" | "convertimos el edificio como si estuviera modelado en hormigón" | [00:09:00]-[00:09:08] |
| 16 | **Variante C** — que parezca un modelo 3D | **Nano Banana Pro** | "entiende mejor cómo convertir esto en un archivo 3D que con la otra" | "hacemos que parezca un modelo 3D" | [00:09:17]-[00:09:28] |
| 17 | **Variante D** — mapa de normales | **Nano Banana Pro** | "hacemos un mapa de normales de esto" | "mapa de normales" | [00:09:31] |
| 18 | **Variante E (la favorita)** — mapa de oclusión ambiental | ComfyUI + **Nano Banana Pro** | "quita mucho ruido… deja la geometría pura, quita todos los detalles"; resultado "mucho más limpio que puedes importar en Rhino" | "crea un mapa de oclusión ambiental de esta imagen" (es la "opción de preparación siete") | [00:09:33]-[00:10:26], [00:13:50]-[00:14:43] |
| 19 | Modelo 3D desde la imagen | **Tripo 3.1 image to model** (buscar "3D" en plantillas) | Funciona por **API** · con `texture` + `PBR` cuesta una cantidad de créditos (cifra no dicha) · los modelos antiguos cuestan lo mismo → conviene el más reciente | — | [00:10:56]-[00:11:38] |
| 20 | Exportar el 3D | **Export Model** | `FBX` u `OBJ`, indistinto ("da igual") | — | [00:12:16]-[00:12:26], [00:15:01]-[00:15:06] |
| 21 | Verificar el resultado | Rhino: modo sombreado / **Arctic mode** | "el modelo 3D funcionó bastante bien"; queda "algo más abstracto" | — | [00:12:27]-[00:12:55], [00:15:13]-[00:15:24] |
| 22 | Corregir la escala en el 3D | Rhino | La escala difiere porque no se miraron bien los ajustes de importación | — | [00:15:35]-[00:15:58] |
| 23 | Multiview de 4 perspectivas | **Nano Banana Pro** → **Tripo v1, que es multiview to model** | El nodo principal pide: una imagen + imagen del lado izquierdo + de atrás + del lado derecho | "hacer una imagen dividida en cuatro, con una perspectiva distinta en cada parte" | [00:17:07]-[00:18:21] |
| 24 | Dejar el material del módulo | **Miro** | "Voy a dejar las capturas y los workflows de esto también en Miro" | — | [00:19:19]-[00:19:26] |

### Variantes de salida (los "estilos" del curso)

Cada variante es una **imagen de preparación** que se descarga del tablero, se importa en Comfy y se pasa por el mismo workflow de image-to-3D. El tablero del curso (`MODULE 5 - IMG-2-3D`, inventario en [[raw/research/2026-10-20-miro-curso/miro-inventario]]) tiene **nueve tarjetas** que coinciden en número con las nueve opciones que anuncia el video [00:00:29].

| Variante | Qué produce | Cómo la nombra el video | Prompt literal (texto de la tarjeta del tablero) | Timestamp del video |
|---------|--------------|----------------------------|----------------------------------------------|-------------------|
| Modelo blanco con contexto | Maqueta blanca museográfica con el entorno urbano | "que parezca un modelo 3D" / variante de museo | `High-resolution totally white architectural model, axonometric view from above, on urban context white base, showing all volumetric details, window openings, terraces, circulation paths, and structural articulation. Maintain consistent details and proportions from the image reference. Uniform matte white material with soft shadows. Neutral daylight environment, seamless white background. Style of museum architectural model photography exhibitions.` | [00:09:17]-[00:09:28] |
| Modelo blanco sin contexto | Maqueta blanca, fondo blanco, sin entorno | "que todos los detalles han desaparecido" | `High-resolution totally white architectural model, axonometric view from above, on white base, NO CONTEXT, showing no details, just window openings, terraces, and structural articulation. Maintain consistent proportions from the image reference. Uniform matte white material with soft shadows. Neutral daylight environment, seamless white background. Style of museum architectural model photography exhibitions.` | [00:07:49]-[00:08:05] |
| Maqueta de hormigón | Maqueta bruta de hormigón, forma básica | "como si estuviera modelado en hormigón" | `Physical architectural scale model cast in raw concrete, displayed in professional studio environment. Focus on pure volumetric geometry and spatial relationships. Handmade brutalist maquette showing essential building form - no excessive detail, only fundamental massing and major openings. Rough concrete texture with visible formwork marks and slight surface imperfections. Neutral gray concrete color with subtle variations. Studio photography with soft diffuse lighting creating gentle shadows that emphasize volume. Minimalist presentation on white surface against neutral background. Architectural study model aesthetic - emphasizes three-dimensional form, proportions, and spatial composition. Tactile object quality with honest material expression. Museum exhibition photography style.` | [00:09:00]-[00:09:08] |
| Normal map | Mapa de normales tangencial | "hacemos un mapa de normales de esto" | `3D Normal Map texture of the building view. Tangent space normal map colors (purple/blue/pink gradients). Flat lighting, no shadows, no diffuse colors. Surface geometry encoded in color values: facing up (green), facing right (red), facing forward (blue). High-fidelity representation of surface bumps, recesses, and geometric details as a texture map for 3D rendering. Clean, technical output suitable for PBR workflows. Maintain exact geometry.` | [00:09:31] |
| Viewport de Rhino | Captura de viewport CAD con líneas de arista | — (la muestra en el tablero, no la nombra en el video) | `Convert the uploaded hyperrealistic image into a 3D Rhinoceros viewport screenshot. Abstract the volumes while maintaining the exact geometry and proportions of the original architecture. Exclude all super fine details, textures, and photorealistic materials. Render the building as a clean, digital 3D model in shaded or rendered view mode characteristic of Rhino software, with soft gray or white default materials and subtle ambient occlusion shadows. Display clear, clean edge lines (isocurves or structural edges) typical of a CAD viewport. Abstract all vegetation and entourage, general massing of trees and vegetation. The final image should look exactly like a work-in-progress digital 3D model viewport screenshot, focusing purely on volumetric composition and exact geometric form.` | — |
| Objeto en lightbox | Maqueta de arcilla, objeto aislado, como foto de producto | — (la muestra en el tablero, no la nombra en el video) | `Transform this architectural image into a clean, untextured 3D model render of a standalone, holdable object — as if the subject were modeled in Rhino and exists as a discrete, physical maquette that could be picked up and rotated in your hand. Object definition (critical): Treat the subject as a finite, closed 3D volume with clearly defined boundaries on ALL sides — top, bottom, left, right, front, AND back. The object must have explicit thickness and depth — not a flat facade or relief, but a fully bounded mass with a clear back face. Define sharp, terminating edges on all corners where the object ends — no surfaces that dissolve, fade, or extend infinitely. If the source is a facade or partial view, intelligently close it off into a complete, self-contained block/mass with logical depth (e.g., a facade becomes a slab-like volume with thickness; a building becomes a sealed massing study). Think: architectural maquette, Rhino "Cap" command applied, watertight mesh, 3D print–ready solid. Geometry: Crisp, hard edges at every corner and surface intersection. Clean planar surfaces with visible extrusion on all detail elements (window reveals, balconies, ornamentation, openings). Preserve original proportions and architectural features faithfully. All silhouettes must be unambiguous and sharply defined against the background. Framing & isolation (critical): The object must be fully contained within the image with generous empty margin on all sides — approximately 15–20% padding between the object's outermost edges and the image border. The object must NOT touch, bleed into, or be cropped by any image edge. Center the object in the composition. Render from a three-quarter perspective view (rotated ~20–30° off-axis horizontally and tilted ~10–15° downward) so depth, side faces, and top are all clearly visible — this reveals the object's three-dimensionality and aids image-to-3D reconstruction. Material & surface: Single uniform matte clay material across the entire object — light neutral gray (#C8C8C8 to #D5D5D5). No textures, no patterns, no color variation, no material differentiation. Smooth, diffuse, slightly chalky surface — classic Rhino/Blender clay render aesthetic. Lighting: Soft, even studio lighting with subtle key light from upper-front-left. Gentle ambient occlusion in corners and recesses to enhance depth and edge readability. Soft, contained cast shadow directly beneath the object (small, tight — reinforces that it's a discrete object sitting in space). No harsh contrast, no specular highlights, no reflections. Background: Pure flat white background (#FFFFFF). Fully isolated subject, no ground plane texture, no context, no surroundings, no people, no vegetation, no atmosphere. Critical constraints: Output must read unambiguously as a single, complete, holdable 3D object floating in white space — like a product photo of a clay maquette in a lightbox. Every edge of the object must be visible and terminate cleanly within the frame. No artistic interpretation, no stylization, no environmental effects.` | — |
| Mapa de oclusión ambiental (AO) | Modelo en software de modelado, fondo limpio, geometría pura | "esta es mi favorita" / "opción de preparación siete" | `Create an ambient occlusion map for this image and show it as if it was modelled in a digital modelling software against a solid clear background. Remove all textures and materials, make it in white render mode. Remove context and plants.` | [00:09:33]-[00:10:21], [00:13:50]-[00:14:43] |
| Multiview en 4 tiles | Cuatro perspectivas del mismo objeto | "generar cuatro perspectivas distintas a partir de ella" | `Make a 4-tiled image of which each tile is a different perspective of the object (front view, side view, top view, back view) Keep the character of the input image consistent.` | [00:17:09]-[00:17:46] |
| Contraluz (backside) | La cara que no se ve | — | `Imagine the backside of the building. Keep the character of the input image consistent.` | — |

> Los prompts de arriba son **el texto literal de las tarjetas del tablero del curso** (fuente: [[raw/research/2026-10-20-miro-curso/miro-inventario|inventario Miro]]), no lectura en voz alta del video: el video muestra la imagen en pantalla y remite a Comfy para ver el prompt [00:08:08]-[00:08:34]. Solo dos verbaliza el profesor (AO y 4-tiles).

## Modelos y servicios mencionados

| Nombre | Local o API | Qué dice el video de él | Cuándo lo recomienda | Cuándo lo descarta | Timestamp |
|--------|-------------|-------------------------|----------------------|--------------------|-----------|
| **Hunyuan3D** (nodo) | No dicho en el video; el video habla de que consume créditos | Model 3.0, face count 500k, tipo de polígono `low poly` / `normal` / `geometry`; el modelo arma el objeto 3D a partir de la imagen | Muebles y formas complejas que no conviene modelar a mano; en el tutorial usa `low poly` por velocidad | No lo descarta en el video. Aclara que `normal` y `geometry` tardan más y cuestan más créditos, y que `geometry` es el más barato | [00:00:49]-[00:01:26] |
| **Tripo** (marca) | Para *Tripo 3.1 image to model* dice que funciona por **API**; del multiview no lo dice | "Tripo es simplemente una marca" | Ambas ramas (multiview y single view) | — | [00:06:02]-[00:06:19], [00:11:13] |
| **Tripo 3.1 image to model** (workflow) | **API** | Con `texture` + `PBR` cuesta una cantidad de créditos (la cifra queda en pantalla, no se dice); los modelos antiguos cuestan lo mismo | Torre/edificio a partir de una imagen; "te aconsejo usar el más reciente" | La versión anterior queda como opción de mismo precio, no como descarte | [00:11:08]-[00:11:38] |
| **Tripo multiview to model** (workflow; "Tripo v1" en la segunda vuelta) | No dicho en el video | Necesita al menos dos imágenes del mismo modelo; en la versión v1 el nodo pide imagen + izquierda + atrás + derecha | Formas complejas donde una sola vista no alcanza | Con una forma simple "una sola imagen basta" | [00:05:59]-[00:06:43], [00:18:04]-[00:19:02] |
| **Nano Banana Pro** (workflow en Comfy) | No dicho en el video (corre como modelo dentro de Comfy) | Es la herramienta de preparación de imagen: "esto es simplemente Nano Banana Pro"; sirve para cualquier workflow image-to-image | Todas las variantes de preparación | — | [00:08:34]-[00:08:42], [00:14:08]-[00:14:26], [00:17:35] |
| **Rhino** | Software 3D de escritorio | Archivo → Importar; comando `zoom`; escalado a cota real; modo sombreado / **Arctic mode** | Forma simple (modelar a mano) y destino obligatorio del 3D generado | — | [00:01:43]-[00:01:58], [00:02:24]-[00:03:01], [00:12:27]-[00:12:33] |
| **SketchUp** | No dicho en el video | Alternativa a Rhino en el mismo paso de importación | "o puedes usar SketchUp o cualquier software 3D que uses" | — | [00:02:05]-[00:02:27] |
| **ComfyUI** | Plataforma (todo el flujo de preparación vive adentro) | "la importas en Comfy y puedes ver el prompt que usé" | Descargar el prompt de cada preparación y ejecutarlo | — | [00:08:29], [00:14:01], [00:17:30] |
| **Miro** | Plataforma externa (tablero del curso) | Aloja las nueve preparaciones, las capturas de resultado y los workflows; además, la web/ficha del producto donde está la cota | Consulta de preparaciones, documentación de resultados, fuente de cotas | — | [00:03:12]-[00:03:22], [00:07:27], [00:13:42], [00:19:19] |
| **OBJ** / **FBX** | Formatos de intercambio | OBJ "porque está bastante bien soportado"; FBX u OBJ "da igual" | Exportación desde ComfyUI y Tripo | — | [00:02:17]-[00:02:20], [00:12:22]-[00:12:26], [00:15:01]-[00:15:06] |

## Prompts y fórmulas

### Regla de estructura que enseña el video

Todo prompt de preparación tiene **tres partes**, en este orden:

1. **Qué tiene que ser la salida** (maqueta blanca, hormigón, viewport, objeto aislado, AO, multiview) — es lo que le dice al modelo "cómo leer la geometría" [00:07:46]-[00:08:05], [00:09:13]-[00:09:31].
2. **Qué hay que eliminar** (contexto, vegetación, texturas, materiales, detalles finos) — es lo que saca el ruido [00:08:48]-[00:09:08], [00:14:33]-[00:14:43].
3. **Anclaje a la referencia** ("Keep the character of the input image consistent", "Maintain consistent proportions from the image reference") — mantiene el carácter y las proporciones del original (texto de las tarjetas del tablero).

El nodo multiview agrega una regla de **cobertura**: la imagen preparada tiene que llegar en cuatro direcciones (frontal + izquierda + atrás + derecha), porque el nodo principal las pide una por una [00:18:11]-[00:18:21].

### Lo que el video verbaliza (texto literal del profesor)

```
crea un mapa de oclusión ambiental de esta imagen, etcétera.
```
[00:14:20]-[00:14:26] — el paso que llama "opción de preparación siete" y que usa para generar la imagen limpia del edificio.

```
vale, deja la geometría pura, quita todos los detalles.
```
[00:14:40]-[00:14:43] — el criterio con el que describe el resultado del prompt de AO.

```
El prompt va de hacer una imagen dividida en cuatro,
con una perspectiva distinta en cada parte.
```
[00:17:37]-[00:17:46] — la fórmula del multiview en 4 tiles.

```
convertimos el edificio como si estuviera modelado en hormigón,
y solo muestra la forma más básica.
```
[00:09:02]-[00:09:08] — variante de maqueta de hormigón.

```
o hacemos que parezca un modelo 3D.
```
[00:09:17]-[00:09:28] — variante "modelo blanco / modelo 3D".

```
que parezca que todos los detalles han desaparecido.
Ya no hay vegetación aquí que ensucie el resultado.
```
[00:07:55]-[00:08:05] — variante 1 (opción de preparación).

### Fórmulas del flujo (no textual, derivadas de lo que muestra)

```
imagen 2D  →  [preparación con Nano Banana Pro]  →  imagen limpia →  [Hunyuan3D | Tripo 3.1 image to model]  →  malla 3D
           →  [Export Model: OBJ | FBX]  →  [Rhino: Importar → escalar → comparar]
```
[00:07:46]-[00:10:26], [00:12:16]-[00:12:33], [00:15:01]-[00:15:58]

```
imagen 2D  →  [Nano Banana Pro: 4 tiles]  →  [Tripo v1 multiview to model:
 frontal + izquierda + atrás + derecha]  →  malla 3D
```
[00:17:07]-[00:18:48]

```
escala real = cota de la ficha del producto
ej.: diámetro 150 cm  →  escala hasta que "esto mide 1,5"
```
[00:03:25]-[00:03:51]

## Reglas, buenas prácticas y trampas

- La pregunta previa a generar 3D es "¿para qué necesito un modelo 3D de esto?": con una forma simple, modelarla en Rhino alcanza [00:01:37]-[00:01:45].
- La escala del polígono se elige con criterio de costo: `geometry` es el más barato, `normal` cuesta 105 créditos, `low poly` cuesta 126 [00:01:08]-[00:01:16].
- `low poly` reduce caras y aun así conserva la simetría: sirve como primera aproximación rápida [00:05:00]-[00:05:08].
- El formato de salida universal es `OBJ`, por su soporte; `FBX` funciona igual [00:02:17]-[00:02:20], [00:15:01]-[00:15:06].
- Los ajustes de importación de Rhino pueden dejarse como vienen en este flujo; lo que sí importa es el comando `zoom` para encuadrar y comparar [00:02:41]-[00:03:01].
- La escala real se toma de la **ficha o web del producto** (ej. diámetro 150 cm) y se aplica escalando el objeto importado [00:03:12]-[00:03:51].
- Cada resultado se documenta con una captura pegada en Miro junto al material de referencia [00:03:55]-[00:04:10].
- La diferencia entre una imagen buena y una image-to-3D buena está en el **contenido**: coches, edificios vecinos y vegetación se cuelan en la malla [00:06:46]-[00:07:19].
- Preparar la imagen antes de pasarla al 3D es lo que da el salto de calidad: "un modelo 3D mucho más limpio que puedes importar en Rhino" [00:10:13]-[00:10:21].
- Con una sola vista frontal, el modelo se queda en abstracto y "no sabe nada de la parte de atrás" [00:13:15]-[00:13:29].
- Con formas complejas conviene un paso de preparación; con formas simples, una sola imagen alcanza [00:18:55]-[00:19:13].
- Cuando la forma es redondeada o estrellada, conviene dar el multiview: el modelo deja de "hacerlo ovalado" [00:18:27]-[00:18:43].
- El modelo más reciente conviene siempre: los más antiguos cuestan lo mismo [00:11:26]-[00:11:33].
- El contexto se quita porque "no me parecía que el contexto fuera relevante para conseguir un modelo 3D"; la geometría queda "más pura" [00:16:01]-[00:16:11].
- El paso intermedio sirve para muebles y para todos los casos [00:16:55]-[00:16:53].
- **Trampa 1 — escala:** al importar, la escala puede venir distinta porque los ajustes de importación no se revisaron [00:15:35]-[00:15:45].
- **Trampa 2 — "bonita ≠ buena entrada":** una imagen con mucho ruido, baja resolución y artefactos produce un 3D abstracto y con artefactos [00:12:33]-[00:12:55].
- **Trampa 3 — objetos del contexto deformados:** los coches se transforman "en algo que no es un coche" [00:13:02]-[00:13:10].
- **Trampa 4 — una sola variante no alcanza:** la primera preparación (borrar detalles) todavía deja ver edificios vecinos y árboles [00:08:48]-[00:08:51].
- **Trampa 5 — créditos:** `low poly` aparece como la opción más cara (126) frente a `normal` (105), a pesar de entregar menos caras [00:01:08]-[00:01:16].
- **Trampa 6 — smoothed vs. real:** en modo Arctic la forma se ve "bastante suave"; sirve para leer volumen, no para medir detalle [00:05:31]-[00:05:35].
- **Cámara:** este módulo no trabaja el bloqueo de cámara al re-renderizar; lo resuelve indirectamente generando vistas (frontal / izquierda / atrás / derecha) con el multiview [00:17:09]-[00:18:21]. El control de cámara propiamente dicho no se explica acá (es materia del módulo 3, `STRICT CAMERA LOCK`).

## Qué NO dice el video (para implementarlo)

- **Dónde corre cada cosa:** si Hunyuan3D, Nano Banana Pro y los workflows de Tripo corren en local o por API. Para Tripo 3.1 lo dice (API) [00:11:13]; para Hunyuan3D y Nano Banana Pro: **no dicho en el video**.
- **Nombre del modelo/checkpoint** de Hunyuan3D más allá de "modelo 3.0" [00:00:54]: **no dicho en el video**.
- **Cantidad de créditos** del workflow Tripo 3.1 con `texture` + `PBR`: la cifra queda en pantalla, **no dicho en el video** [00:11:17]-[00:11:23].
- **Precio exacto de `geometry`** en Hunyuan3D (solo se dice que es más barato que `normal` = 105): **no dicho en el video** [00:01:11]-[00:01:13].
- **Texto literal de los prompts** de las nueve variantes: el video los muestra en pantalla y remite a Comfy, solo verbaliza el de AO y el de 4 tiles [00:08:08]-[00:08:34], [00:17:37]-[00:17:46]. El resto se toma del tablero (ver sección anterior).
- **Parámetros de generación** (resolución de entrada, seed, sampler, denoise, batch): **no dicho en el video**.
- **Unidades y campo de escala** con el que se escala en Rhino: solo se dice "esto mide 1,5" [00:03:40]-[00:03:46] — **no dicho en el video**.
- **Cómo se controla la cámara al volver a renderizar** (cámara bloqueada): **no dicho en este módulo**.
- **Cómo se texturiza el modelo final**: solo se menciona el toggle `texture` + `PBR` de Tripo 3.1 [00:11:17]-[00:11:23] — **no dicho en el video**.
- **Limpieza de la malla en Rhino**: el video solo muestra importar, zoom, escalar y mirar en modo sombreado; no hay pasos de reparación de malla — **no dicho en el video**.
- **Nombre de los nodos internos** del workflow de Tripo (solo se describe el nodo principal y sus cuatro entradas) [00:18:11]-[00:18:21] — **no dicho en el video**.
- **Qué plataforma contabiliza los créditos** (qué servicio cobra los 105 / 126 / Tripo): **no dicho en el video**.
- **Nomenclatura exacta de las nueve opciones** en el tablero (cuál es "la número 1", "la número 7"): solo se identifica explícitamente la **opción 7 = mapa de oclusión ambiental** [00:13:50]-[00:14:26]; el resto **no dicho en el video**.

## Qué aporta al concurso AIxGaudi ("The Gaudí Nexus")

- **Convierte una imagen en geometría medible cuando no existe archivo 3D**: es la respuesta directa al hueco entre el render 2D y el modelo del built, y el propio profesor lo marca como "el que de verdad te ahorra tiempo" [00:05:08]-[00:05:26].
- **El paso de preparación es lo que separa una maqueta limpia de una maqueta sucia**: sacar contexto y vegetación antes del 3D es la diferencia entre "un modelo 3D mucho más limpio" y uno "abstracto" [00:10:13]-[00:10:21], [00:12:55]-[00:13:29].
- **La escala real se resuelve con la cota del producto**: sirve tanto para mobiliario como para verificar proporciones de un volumen generado [00:03:12]-[00:03:51].
- **Multiview como economía de información**: con cuatro perspectivas generadas de una sola imagen, el modelo deja de inventar la parte de atrás y deja de "hacerlo ovalado" [00:17:09]-[00:18:48].
- **Los estilos de salida hablan el idioma del concurso**: modelo blanco de museo, maqueta bruta de hormigón, viewport Rhino y objeto aislado en lightbox son exactamente los registros de representación que pide una lámina A1 de maqueta [00:09:02]-[00:09:31] + prompts del tablero.
- **Todo queda trazado**: capturas y workflows en el mismo tablero donde el curso expone sus prompts, que es el circuito de documentación que el estudio ya usa para el concurso [[specs/261019-plan-concurso-gaudi-nexus-ia|Plan del concurso Gaudí Nexus]] [00:19:19]-[00:19:26].

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|ComfyUI]] — donde corren los workflows de preparación (Nano Banana Pro) y el nodo Hunyuan3D.
- [[wiki/glosario/software/rhino|Rhino]] — destino del 3D: importar, `zoom`, escalar a cota real, modo sombreado / Arctic.
- [[wiki/glosario/software/impresion-3d|Impresión 3D]] — el prompt de "objeto en lightbox" pide malla cerrada estanca ("watertight mesh, 3D print–ready solid"), el mismo requisito de un volumen imprimible.
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|LoRA rhino-to-image (curso AI×Gaudí)]] — el módulo inverso (3D → imagen) que cierra el circuito con este.
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — wiki técnica de ComfyUI del estudio, para montar los workflows localmente.
- [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|Extracción del material del curso AI×Gaudí]] — de dónde salen las capturas, los workflows y el tablero Miro.
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|Reglas de workflows ComfyUI (MVP_04)]] — normas del estudio para bajar y archivar un workflow del curso.
- [[raw/research/2026-10-20-miro-curso/miro-inventario|Inventario del tablero Miro del curso]] — contiene los nueve prompts literales de `MODULE 5 - IMG-2-3D`.
- [[raw/research/2026-10-08-comfyui-workflows-arq|ComfyUI-3D: estado del arte]] — ComfyUI-3D-Pack, Hunyuan3D-2 y Tripo3D como alternativas locales del stack del curso.
- [[raw/yt/transcripts/2026-10-21_mux-image-to-3d.es|Transcripción ES del módulo 5]] y [[raw/yt/transcripts/2026-10-21_mux-image-to-3d.en|EN]] — fuente verbatim de esta ficha.
- **Sin ficha propia en el glosario todavía:** Tripo, Hunyuan3D, Nano Banana Pro, SketchUp y Miro → quedan como candidatas a crear en `wiki/glosario/software/`.

## Cómo lo adaptamos

| Lo que hace el curso | Lo que hacemos nosotros | Por qué |
|----------------------|------------------------|---------|
| Las nueve preparaciones de imagen con **Nano Banana Pro** (variantes de modelo blanco, hormigón, normal map, objeto aislado y AO) | Las generamos **en local** con **SDXL** (`Juggernaut-XL_v9`), **ControlNet** depth fp16 y scribble (ya en disco) y **Depth Anything 3** (nodo core) | Cubrimos las cinco variantes que el video usa como entrada al 3D —incluida el AO, la que el profesor llama favorita— corriendo sobre nuestra propia GPU, con el control de encuadre y de profundidad en manos del estudio |
| El **AO map** como paso intermedio (opción 7 del tablero) | **Depth Anything 3 + ControlNet depth/scribble** producen la profundidad y el AO localmente | Es el paso que separa la maqueta limpia de la maqueta sucia: "deja la geometría pura, quita todos los detalles" [00:14:33]-[00:14:43] |
| La generación 3D con **Tripo 3.1 image to model** por API | La resolvemos con el **pack abierto ComfyUI-3D-Pack** (**Tripo3D / Hunyuan3D-2**) en el **pod** | Llevamos la etapa 3D a nuestra infraestructura, con la VRAM que pide el stack 3D y sin depender del saldo de créditos externo |
| La variante **multiview** (**Tripo v1 multiview to model**) | La misma línea del pack, alimentada con las cuatro vistas | Es la economía de información del módulo: le da al modelo la parte de atrás y evita que la invente [00:13:15]-[00:13:29], [00:18:43]-[00:19:13] |
| El **multiview en 4 tiles** generado con un único prompt | Las **cuatro perspectivas se generan con cuatro prompts de encuadre** a partir de la imagen ya preparada | Controlar el encuadre por prompt lleva el multiview al terreno del control de cámara y deja cada vista documentada por separado |
| El export **OBJ o FBX** y la importación en **Rhino** con `zoom`, la escala a cota real y el modo sombreado | **Se conservan tal cual**: OBJ/FBX, Archivo → Importar, comando `zoom`, escalado contra la cota de la ficha y modo sombreado / Arctic | Es el tramo ya verificado del flujo: el formato único de intercambio y la cota real son la evidencia de escala del modelo |
| El catálogo de **capturas y workflows** en el tablero del curso | Se documenta en el **tablero del curso** y en el **vault** (`proyectos/concurso-gaudi-nexus/workflows/WF-curso/`) | Cada módulo deja ficha en el vault: la trazabilidad del método es parte de lo que se presenta |

## Checks contra el criterio del jurado

- **Geometría pura antes que estética.** El criterio que el jurado prioriza es la lógica constructiva sobre la apariencia (Cas Esbach, módulo 6); en este módulo se traduce en un paso concreto: el **AO map** es el que separa la maqueta limpia de la maqueta sucia, porque elimina contexto, vegetación y texturas antes de generar el 3D [00:07:46]-[00:08:05], [00:09:33]-[00:10:21].
- **Multiview como economía de información.** Darle al modelo la parte de atrás (frontal + izquierda + atrás + derecha) evita que la invente, y con eso la volumetría deja de ser una aproximación y pasa a ser una lectura verificada del objeto [00:13:15]-[00:13:29], [00:18:11]-[00:18:48].
- **Escala verificada contra la cota.** El modelo se escala contra la dimensión de la ficha del producto (ej. diámetro 150 cm → "esto mide 1,5") y recién ahí deja de ser una imagen con volumen y pasa a ser un objeto medible [00:03:12]-[00:03:51].
- **El 3D como evidencia del método.** Cuando la volumetría propia todavía no existe, el par *imagen preparada + prompt + modelo 3D* documenta el camino completo (imagen 2D → preparación → 3D → Rhino a escala) que después sostiene el proyecto [00:05:08]-[00:05:26].
- **Pendiente:** la transcripción del **módulo 6** (mesa redonda, con Cas Esbach) está pendiente de lectura; el criterio del jurado se transcribirá ahí y se cruzará contra este módulo para cerrar los checks.
