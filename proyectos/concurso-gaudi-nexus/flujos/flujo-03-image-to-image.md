---
tipo: flujo-curso
proyecto: concurso-gaudi-nexus
modulo: 3
slug: image-to-image
titulo_curso: "Image-to-Image (Rhino-to-Image)"
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [mvp_04, comfyui, curso-ai-gaudi, modulo-3, image-to-image, rhino-to-image, gaudi-nexus]
idioma: es
---

# Módulo 3 — Image-to-Image (Rhino-to-Image) (flujo del curso)

> Ficha de flujo del módulo 3 del curso AI×Gaudí, transcrita del video. Fuente verbatim: [[raw/yt/transcripts/2026-10-21_mux-image-to-image.es|transcripción ES]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-image.en|EN]] · plan: [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro de workflows adapted]].

## Ficha

| Dato | Valor |
|---|---|
| Duración total de la pista | 01:22:13,439 → 01:22:14,580 (~1h22min) [declarado en el encabezado del subtítulo] |
| Idioma | Español (subtítulos `es`); el curso publica además la pista `en` para resolver términos técnicos |
| Profesor | Thomas Nelissen, arquitecto (se identifica como autor de "mi app Spectrum" y del sitio `thomasnelissen.ai`) [01:19:28]-[01:19:38], [01:21:50] |
| Tema | Image-to-image: upscaling, el flujo **Rhino-to-Image** (el workflow principal del curso), image-edit con FLUX.2 klein 9B e inpainting con Nano Banana dentro de ComfyUI |
| Contexto del módulo | Text-to-image es para ideación y fases iniciales; image-to-image entra más tarde, en tareas de diseño iterativas y en visualización (upscaling y renders finales) [00:00:18]-[00:00:58] |

## Objetivo del módulo

Llevar la volumetría de Rhino hasta una imagen fotorreal manteniendo el control: el modelo bloquea la geometría en su sitio y aplica encima la materialidad de una imagen de referencia [00:23:38]-[00:24:18], [00:29:39]-[00:29:52].

## El flujo, paso a paso

| # | Acción | Nodo / herramienta (nombre EXACTO en ComfyUI) | Valores que dice el video | Prompt / fórmula | Timestamp |
|---|---|---|---|---|---|
| A1 | **UPSCALING** — descargar el workflow de upscaling del tablero Miro y arrastrarlo a ComfyUI: ComfyUI arma el workflow solo | arrastre y soltar en el canvas (ComfyUI genera el grafo) | — | — | [00:04:38]-[00:05:09] |
| A2 | Volver a cargar la imagen de baja resolución (ComfyUI a veces no recuerda la imagen subida): arrastrar o seleccionar desde el nodo | nodo de carga de imagen | — | — | [00:05:13]-[00:05:48] |
| A3 | Dejar la estructura interna del subgraph tal cual (no es el foco) | subgraph | — | — | [00:05:51]-[00:06:14] |
| A4 | Fijar el factor de escalado | parámetro **"upscale by"** | ×3 en el ejemplo (1280×720 → 3840×2160; cada píxel pasa a 3×3 = 9 píxeles); ×4 → cada píxel pasa a 16 [00:01:58]-[00:03:24] | — | [00:06:18]-[00:06:54] |
| A5 | Cargar o fijar la seed | control de seed | "randomize" (aleatorio) en el ejemplo | — | [00:06:58]-[00:07:12] |
| A6 | Ejecutar y ver el salto de resolución | botón "run" | de 1K a casi 4K | — | [00:07:08]-[00:08:10] |
| A7 | Controlar el peso del archivo | — | imagen original 1,8 MB → escalada casi 25 MB | — | [00:08:43]-[00:09:05] |
| A8 | Buscar workflows alternativos en la galería oficial | **Templates → "use cases"** / **Templates → "tasks"** (buscar "upscale", "image upscale") | filtro automático de workflows equivalentes | — | [00:09:14]-[00:10:42] |
| A9 | Distinguir ejecución local de ejecución por API | ícono en la tarjeta de la plantilla | sin símbolo = local / Comfy Cloud; con **Grok, Magnific o Google** = se envía a esa API | — | [00:10:46]-[00:11:19] |
| A10 | Llevar la cuenta de créditos | créditos de Comfy Cloud | 7.000 créditos/mes en el plan normal; 4K = 50 créditos, 2K = 28, 1K = lo mismo; 2K es el mínimo práctico | — | [00:11:24]-[00:12:25] |
| A11 | Segundo workflow de upscaling (motor **Topaz**): acá la resolución de salida se escribe a mano | nodo de enhancer Topaz (entrada 1024×1024) | ×2 → escribir 2048 × 2048 | — | [00:13:02]-[00:14:45] |
| A12 | Escribir el prompt del enhancer y fijar la creatividad | parámetro **"creativity"** | 1 = literal ("al pie de la letra"); 9 = interpreta mucho más e inventa detalles | "mejora esta fotografía de una casa de hormigón en un desierto con un paisaje rocoso… Haz todos los detalles hiperrealistas" (EN: "enhance this photograph of a concrete house in a desert with rocky landscape. Make all details hyper realistic") | [00:14:52]-[00:16:24] |
| A13 | Comparar antes/después: salida del enhancer a "image A", original a "image B" | nodo **"compare images"** (el de Comfy, "ComfyUI tools") | el orden A/B se puede invertir | — | [00:16:37]-[00:20:13] |
| A14 | Guardar / reabrir el workflow | **"Save image as"** · **"open as workflow in new tab"** | — | — | [00:21:04]-[00:21:42] |
| A15 | Workflow de upscaling extra del archivo del tablero | — | usa **FLUX.1** | — | [00:22:06]-[00:22:41] |
| B1 | **RHINO-TO-IMAGE** — crear en el LLM un proyecto llamado "Rhino to image" y pegar el documento de instrucciones en "instructions" (focus mode → Ctrl+A → copiar → pegar en Project instructions) | proyecto de LLM (instrucciones del proyecto) | — | el documento que se pega es el **INSTRUCTION.md** del curso | [00:25:19]-[00:26:49] |
| B2 | Exportar de Rhino la captura del viewport y elegir una foto de referencia (material / atmósfera) | captura del viewport de Rhino o de cualquier 3D | — | — | [00:26:52]-[00:27:33] |
| B3 | Disparar el agente | chat del proyecto LLM | se escribe solo **"start"** | "start" | [00:27:41]-[00:27:57] |
| B4 | Cargar las dos entradas que pide el agente | imagen 1 = captura de Rhino/3D; imagen 2 = fotografía de referencia estética | — | — | [00:27:57]-[00:28:25] |
| B5 | Responder el contexto: tipo de edificio y ubicación | — | "edificio residencial"; "sur de Europa, clima cálido, iluminación neutra"; el agente puede pedir a qué parte del sur de Europa anclar luz y contexto | — | [00:28:34]-[00:29:20], [00:31:06]-[00:31:16] |
| B6 | Copiar el prompt JSON que devuelve el agente | salida del agente | FLUX.2 entiende ese prompt JSON: combina toda la información de la geometría + todos los detalles de la referencia estética en un solo prompt | — | [00:31:18]-[00:31:40] |
| B7 | Importar el workflow del tablero Miro a ComfyUI (arrastrar y soltar). Aparece un error de nombre de LoRA: es esperable | arrastre y soltar | — | — | [00:31:49]-[00:32:13] |
| B8 | Elegir el LoRA ya instalado | **Load LoRA** (dropdown de LoRA) | "en mi caso se llama así; en el tuyo se llamará un poco distinto" | — | [00:32:16]-[00:32:33] |
| B9 | Elegir el modelo | nodo de carga del **UNET** (parámetro "UNET name") | **FLUX.2 klein 9B** (9.000 millones de parámetros); existe además "base 9B FP8" y el curso pide elegir el klein 9B | — | [00:32:39]-[00:33:16] |
| B10 | Cargar la geometría en la PRIMERA imagen y duplicarla en la segunda | entrada **"image"** (1ª) y 2ª entrada | la 1ª imagen = geometría; la 2ª = exactamente la misma imagen | — | [00:33:19]-[00:33:38] |
| B11 | Pegar el prompt del agente en el nodo de texto | nodo de texto (text) | copiar y pegar, nada más | prompt JSON | [00:33:42]-[00:33:52] |
| B12 | Limpiar el subgraph: hay dos nodos Load LoRA; el morado/transparente está en **bypass** (desactivado) y se puede borrar. El workflow se reacomoda solo | Load LoRA (dentro del subgraph) | se pueden encadenar varios LoRA, uno detrás del otro, y combinarlos | — | [00:34:04]-[00:34:52] |
| B13 | Ajustar la fuerza del modelo y los megapíxeles | parámetro **"strength of the model"** y **"megapixels"** | strength = 1 (100 %); megapixels: dejarlo donde está, no cambiar nada al arrancar | — | [00:34:56]-[00:35:21] |
| B14 | Agregar el control antes/después: "image A" = salida generada, "image B" = volumetría original | nodo **"compare images"** | — | — | [00:35:24]-[00:35:56] |
| B15 | Ejecutar | botón "run" | tarda más porque FLUX.2 es un modelo muy grande | — | [00:35:59]-[00:36:24] |
| B16 | Decidir megapíxeles finales | parámetro "megapixels" | subir a "16 o algo así" da más resolución, pero lleva muchísimo tiempo y muchísimos créditos; a mayor resolución, más exigencia y más créditos | — | [00:36:34]-[00:36:58] |
| B17 | Control por planos: en Photoshop, seleccionar los planos que serán ventanas o loggias y pintarlos de **negro** (retícula o distribución aleatoria) | Photoshop (o Photopea) | hay que probar colores; en general el negro funciona bien | — | [00:39:45]-[00:40:48] |
| B18 | Explicarle al agente qué significa el negro | chat del proyecto LLM | "start" + las dos imágenes; después: geometría de Rhino, superficies negras = ventanas o loggias, planos gris claro = paneles cerrados; ubicación: Madrid | "la geometría viene de Rhino, las superficies negras son ventanas o loggias, y los planos gris claro son paneles cerrados… torre residencial en España, luz de día soleada" | [00:40:56]-[00:41:32] |
| B19 | Pegar el prompt JSON y ejecutar | nodo de texto + "run" | el modelo convierte la parte negra en loggias/ventanas y el resto en fachadas cerradas; un plano no marcado en negro terminó siendo ventana | prompt JSON | [00:41:35]-[00:42:37] |
| B20 | Ver dónde está la seed: clic derecho en el subgraph → **"edit subgraph widgets"** | panel derecho de widgets del subgraph | muestra lo marcado como "shown on node" (UNET name, clip name, VAE name, LoRA name) y permite exponer lo oculto | — | [00:43:08]-[00:44:40] |
| B21 | Exponer la seed o fijarla | **"noise seed"** (oculto) / dentro del subgraph, nodo **"random noise"** | "randomize" genera una seed nueva cada vez; "fixed value" la deja fija (el subgraph es caótico y cuesta encontrar el nodo) | — | [00:43:44]-[00:45:33] |
| B22 | Verificar el efecto de la seed | — | con seed fija se regenera exactamente la misma imagen; con seed libre, otra interpretación de la misma imagen | — | [00:45:41]-[00:46:15] |
| C1 | **IMAGE EDIT** (una imagen de partida) — arrastrar la imagen a ComfyUI y subirla al workflow | arrastre y soltar + carga de imagen | el workflow se descarga junto con la imagen | — | [00:47:28]-[00:48:56] |
| C2 | Pedir el borrado de un elemento | nodo de texto | hay una parte rosa = **bypass**, que no se activa al pulsar "run" | "quita al hombre de la imagen" | [00:48:41]-[00:49:10] |
| C3 | Ver el resultado del borrado | — | el modelo quitó también el reflejo de la persona (inpainting; no perfecto pero bien hecho) | — | [00:49:20]-[00:50:17] |
| C4 | Pasar a 2 imágenes de referencia: puentear el workflow de una imagen | clic derecho → **"Bypass"**; o seleccionar nodos y **Ctrl+B** | — | — | [00:50:25]-[00:50:54] |
| C5 | Reactivar la imagen de partida y subir el estilo de referencia (azulejo azul) en la 2ª entrada | entradas **"reference image 1"** y **"reference image 2"** | hay que nombrar las imágenes con el nombre del nodo | "aplica el material de fachada de la imagen de referencia 2, esta, sobre la geometría de la imagen de referencia uno" | [00:51:12]-[00:52:14] |
| C6 | Afinar brillo y escala del material | nodo de texto | — | "los azulejos azules son brillantes y miden 3 por 12 centímetros. Haz que la escala coincida" + "sigue la geometría exactamente" | [00:52:48]-[00:53:39] |
| C7 | Exponer y subir los megapíxeles | "edit subgraph widgets" → nodo de megapíxeles | estaba en **1** (de ahí la baja calidad al hacer zoom) → subir a **2** | — | [00:53:46]-[00:54:39] |
| C8 | Corregir el desplazamiento de píxeles | Photoshop | la imagen sale corrida unos píxeles hacia arriba: se corrige bajando la imagen | — | [00:55:10]-[00:55:50] |
| D1 | **LoRA EN IMAGE EDIT** — entrar al subgraph, agregar un LoRA y conectarlo | nodo **LoRA** (doble clic → "LoRA", el de Comfy) → conectar al **"CFG Guider"** (es la única conexión posible) | — | — | [00:56:21]-[00:57:05] |
| D2 | Elegir el LoRA de image edit | dropdown → **"My Models"** → **"image edit"** | — | — | [00:57:11]-[00:57:21] |
| D3 | Ajustar la fuerza del LoRA y el lote | **strength** · **"batch count"** | strength 1 (valor inicial) → 1,5 rompe la imagen; 0,5 conserva; batch count se puede subir a 20, pero dejarlo en 1 | — | [00:58:12]-[00:58:47] |
| D4 | Leer el resultado del LoRA | — | con 1,5 la imagen queda supercrujiente: el LoRA sobreedita y rompe los píxeles; con 0,5 la imagen queda mejor | — | [00:58:54]-[00:59:58] |
| E1 | Componer el resultado final por collage | Photoshop (o **Photopea**, editor online gratuito) | la capa de fondo es la imagen base; arriba la editada; la geometría coincide casi exactamente → máscara y borrar lo que no se quiere | — | [01:01:28]-[01:04:15] |
| E2 | Agregar modelos externos al grafo | doble clic → **"nano banana"** → **"Nano Banana 2"**; en Templates escribir **"GPT"** (no "ChatGPT") → **"GPT Image"** | los modelos open source (FLUX) justifican Comfy Cloud; Nano Banana también se usa, pero dentro de ComfyUI | — | [01:04:44]-[01:07:03] |
| E3 | Inpainting con máscara | **"load image"** → clic derecho → **"open in mask editor"** (o **"open Mask Editor / Image Canvas"**) | pintar la zona un poco más grande; opacidad 100 % → mejor Around **75 %** | — | [01:08:38]-[01:09:47] |
| E4 | Describir el inpainting y pegar el prompt del coach | prompt coach → pregunta por el modelo y por la cantidad de máscaras | responde "Nano Banana 2"; es **una sola** máscara; devuelve un prompt que describe tu inpainting → copiar y pegar | "añade una loggia en esta parte, solo en esta parte. Añade una barandilla metálica vertical fina" | [01:09:52]-[01:10:55] |
| E5 | Alternativa sin máscara: dibujar un círculo rojo sobre la imagen base y se lo pasar al agente | chat del agente | el agente escribe un prompt completo que además pide quitar el círculo de la salida | "te doy esta imagen de entrada. El círculo rojo es solo una indicación, así que quítalo de la imagen de salida. Está para señalar la zona que quiero cambiar" | [01:13:31]-[01:15:06] |
| E6 | Fijar la resolución de salida | selector de resolución del workflow | 2K en el trabajo diario; 4K para la imagen final (consume más créditos) | — | [01:15:11]-[01:15:26] |
| E7 | Anotaciones cromáticas para editar de forma quirúrgica | dibujo sobre la imagen base | círculo azul y rectángulo rojo como códigos de la consigna | "en este círculo azul añade una persona; en la anotación del rectángulo rojo, añade un árbol" | [01:18:34]-[01:18:51] |

## Modelos, LoRA y checkpoints

| Nombre | Qué dice el video de él | Strength / valores | Cuándo lo recomienda | Timestamp |
|---|---|---|---|---|
| **FLUX.2 klein 9B** | Modelo grande, lento y exigente; "está entrenado para transformar modelos 3D en imágenes hiperrealistas" y para bloquear la geometría exacta | UNET con strength 1 = 100 % | Es el UNET del workflow rhino-to-image; el video pide elegirlo por nombre ("FLUX.2 klein, 9.000 millones de parámetros") | [00:23:38]-[00:24:18], [00:32:55]-[00:33:16], [00:35:08]-[00:35:13], [00:36:15]-[00:36:24] |
| **FLUX.2 base 9B FP8** | Existe en el dropdown junto al klein | — | Mencionado como alternativa disponible; el curso indica elegir el klein 9B | [00:32:59]-[00:33:05] |
| **FLUX.1** | Workflow de upscaling extra, archivado en el fondo del tablero Miro | — | Upscaling de imagen de muy baja calidad a muy detallada | [00:22:06]-[00:22:41] |
| **LoRA del curso (rhino-to-image)** | Ya instalado por el usuario; dentro del subgraph hay dos nodos Load LoRA (se pueden encadenar). El módulo 3 no da el nombre del archivo: "en el tuyo se llamará un poco distinto" | strength = 1 (100 %) como punto de partida; en image edit: 1 / 1,5 / 0,5 | Workflow rhino-to-image (nodo Load LoRA) e image edit (dropdown My Models → "image edit") | [00:32:05]-[00:32:33], [00:34:04]-[00:34:52], [00:35:08]-[00:35:13], [00:57:11]-[00:58:30] |
| **Topaz** | "Empresa que se llama Topaz y que tiene un motor muy bueno"; motor de upscaling (API) | salida en píxeles manual (×2 → 2048×2048); "creativity" 1 vs 9 | Upscaling; el instructor elige este para la demo | [00:13:04]-[00:13:45], [00:14:32]-[00:16:24] |
| **Google (imagen)** | Se envía a Google por API, no lo escala Comfy Cloud | 4K = 50 créditos, 2K = 28, 1K = lo mismo | Upscaling por API; el curso advierte que algunos motores funcionan mejor con fotos y otros con renders de arquitectura | [00:11:02]-[00:11:19], [00:12:02]-[00:12:25], [00:13:24]-[00:13:42] |
| **Magnific / Grok** | Íconos que indican que el workflow corre por API | — | Upscaling por API (equivalentes en Templates) | [00:11:02]-[00:11:16] |
| **WaveSpeed** | "A algunos les gusta mucho WaveSpeed" | — | Alternativa de upscaling | [00:13:15]-[00:13:21] |
| **Krea** | "Krea es otro distinto"; hay formas casi ilimitadas de hacer upscaling | — | Alternativa de upscaling | [00:23:06]-[00:23:20] |
| **Nano Banana 2** | Se integra dentro de ComfyUI (nodo propio); "Nano Banana es buenísimo" en inpainting | 2K en el día a día, 4K para la imagen final | Inpainting quirúrgico con máscara y con anotaciones sobre la imagen | [01:05:26]-[01:05:38], [01:08:43]-[01:08:49], [01:10:10], [01:15:11]-[01:15:26] |
| **GPT Image** | Nodo de API de OpenAI dentro de Comfy; se busca escribiendo "GPT" en vez de "ChatGPT" | — | Alternativa a Nano Banana; a veces hay que refrescar para que funcione | [01:06:22]-[01:07:03] |
| **Comfy Cloud** | Plataforma donde corren los modelos open source; modelo de suscripción | 7.000 créditos/mes en el plan normal | Ejecución de FLUX.2 y de los workflows de upscaling | [00:11:24]-[00:11:56], [01:04:44]-[01:04:56] |

## Prompts y fórmulas

### 1) Prompt de upscaling (motor Topaz) — literal [00:14:52]-[00:15:06]

```text
enhance this photograph of a concrete house in a desert with rocky landscape.
Make all details hyper realistic.
```

En el audio en español el instructor lo dicta como: "mejora esta fotografía de una casa de hormigón en un desierto con un paisaje rocoso… Haz todos los detalles hiperrealistas", y quita la parte "the whole image" porque ya no aplica [00:15:00]-[00:15:02].

### 2) Chat con el agente del flujo Rhino-to-image — literal [00:40:56]-[00:41:32]

```text
start
[imagen 1: geometría de Rhino con planos pintados de negro]
[imagen 2: foto de referencia del material]

la geometría viene de Rhino, las superficies negras son ventanas o loggias,
y los planos gris claro son paneles cerrados. En este caso, los ladrillos
azules de la imagen de referencia. Torre residencial en España, luz de día
soleada.
[ubicación: Madrid]
```

Variante sin marcado de planos (solo "start" + las dos imágenes) [00:27:41]-[00:29:20]:

```text
start
[imagen 1: captura del viewport de Rhino]
[imagen 2: foto de referencia estética]

¿Qué tipo de edificio es? → edificio residencial
¿Dónde está ubicado? → el sur de Europa, clima cálido, iluminación neutra
```

### 3) Estructura de la instrucción de sistema (INSTRUCTION.md) que entrega el curso

El video **no lee** el contenido del documento: solo muestra que hay que pegar "todo este documento" en las instrucciones del proyecto [00:25:44]-[00:26:49]. La estructura está copiada en el vault: [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-instruction-md|prompt-rhino-to-image-instruction-md]].

Lo que sí afirma el video sobre ese documento:

- El agente pide **dos** imágenes: la captura del viewport de Rhino/3D y una fotografía de referencia estética [00:27:57]-[00:28:15].
- Siempre pregunta **dos preguntas de contexto** antes de generar: tipo de edificio y ubicación [00:28:34]-[00:28:49].
- Cuanto más contexto se dé, mejor; la ubicación debeRIX de luz y contexto (el agente incluso repregunta a qué parte del sur de Europa anclar la luz) [00:28:49]-[00:29:13], [00:31:06]-[00:31:16].
- La salida es **un prompt JSON** que FLUX.2 entiende, y combina toda la información de la geometría con todos los detalles de la referencia estética en un solo prompt [00:31:18]-[00:31:40].

### 4) Esqueleto JSON de salida (el que va al nodo de texto) — entregable del curso

El video muestra el JSON en pantalla pero **no lo transcribe**. Copia oficial en el vault: [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-esqueleto-json|prompt-rhino-to-image-esqueleto-json]].

```json
{
  "scene": "[1–2 sentences. 'A professional highly detailed realistic architecture photography of {typology}. STRICT CAMERA LOCK: Match Image 1 perspective.' Then one sentence naming the transformation: the massing of Image 1 re-skinned in the materiality of Image 2.]",

  "subjects": [
    {
      "description": "[1–2 sentences. State massing preserved exactly from Image 1, then name the facade/material system taken directly from Image 2 (its surfaces, colour, finish). Replace pink figures with realistic pedestrians. No joint details or mm dimensions.]",
      "position": "[1 sentence. Spatial placement relative to Image 1's composition.]",
      "action": "[1 short phrase. Static quality or kinetic impression.]"
    }
  ],

  "style": "[Single sentence. Name the aesthetic/materiality character read directly from Image 2 (no architect reference). Photography by Iwan Baan and {one other photographer}. Phase One IQ4, {lens}, {film stock}, grain/aberration notes.]",

  "color_palette": ["#______","#______","#______","#______","#______","#______"],

  "lighting": "[1–2 sentences. Light quality taken from Image 2: time of day, diffusion, shadow character, interior glow if visible.]",

  "mood": "[2–3 adjectives, then one sentence connecting the mood directly to the atmosphere of Image 2.]",

  "background": "[1–2 sentences. Site, terrain, sky — regionally authentic to the user's stated location. Replace green massing volumes with Piet Oudolf-style vegetation appropriate to that region. Keep brief.]",

  "composition": "[1–2 sentences. 'MATCH CAMERA OF IMAGE 1 EXACTLY.' Then name the perspective type and what it emphasises.]",

  "camera": {
    "angle": "[Short phrase matching Image 1.]",
    "lens": "[Lens choice only.]",
    "depth_of_field": "[Aperture and focus in one phrase.]"
  }
}
```

**Regla de estructura que el video enseña (lo que sí dice, textualmente):**

1. **Primero la geometría, después la materialidad.** En el JSON, `scene` arranca con el tipo de proyecto y el `STRICT CAMERA LOCK` de Image 1, y recién ahí nombra "the massing of Image 1 re-skinned in the materiality of Image 2"; en `subjects.description`, primero "massing preserved exactly from Image 1" y después el sistema de materiales tomado de Image 2 [00:31:18]-[00:31:40] + esqueleto JSON del tablero].
2. **La cámara va antes que el estilo.** `STRICT CAMERA LOCK: Match Image 1 perspective` es lo primero de `scene`, y `MATCH CAMERA OF IMAGE 1 EXACTLY` abre `composition` [esqueleto JSON del tablero].
3. **Un solo prompt, sin alternativas.** El agente no ofrece varias direcciones estéticas: combina geometría + referencia en un solo prompt que se copia y pega tal cual en el nodo de texto [00:31:25]-[00:31:52].
4. **En el chat con imágenes, se las llama por el nombre del nodo.** "reference image 1" = geometría, "reference image 2" = material; el prompt tiene que usar esos nombres [00:51:40]-[00:52:10].
5. **El contexto (ubicación) precede al resultado.** Tipo de edificio y ubicación se responden antes de que el agente escriba el JSON [00:28:34]-[00:29:20].

### 5) Prompts literales de image edit

Borrar un elemento [00:48:56]:

```text
quita al hombre de la imagen
```

Aplicar material de una segunda referencia [00:51:33]-[00:52:10]:

```text
aplica el material de fachada de la imagen de referencia 2, esta,
sobre la geometría de la imagen de referencia uno.
```

Afinar brillo y escala del material [00:52:29]-[00:53:39]:

```text
los azulejos azules son brillantes y miden 3 por 12 centímetros.
Haz que la escala coincida.
sigue la geometría exactamente.
```

Poblado [01:01:12]-[01:01:16]:

```text
añade muchas personas mayores en sus balcones, y algunas tendiendo la ropa
```

Inpainting con máscara (prompt del prompt coach) [01:09:52]-[01:09:59]:

```text
añade una loggia en esta parte, solo en esta parte.
Añade una barandilla metálica vertical fina.
```

Inpainting por anotación sobre la imagen base [01:13:57]-[01:14:39]:

```text
te doy esta imagen de entrada. El círculo rojo es solo una indicación,
así que quítalo de la imagen de salida. Está para señalar la zona que quiero cambiar.
```

Anotaciones múltiples [01:18:40]-[01:18:51]:

```text
en este círculo azul añade una persona;
en la anotación del rectángulo rojo, añade un árbol.
```

## Reglas, buenas prácticas y trampas

- La geometría va primero y la cámara va con ella: el modelo aplica la imagen de referencia sobre la geometría y deja la geometría exactamente en su sitio; está entrenado para hacerlo exacto [00:29:39]-[00:29:52].
- La fidelidad es bidireccional: el modelo es tan bueno siguiendo la geometría que también reproduce las líneas de Rhino en el render (despiece de paneles en vez de una sola superficie) — buena noticia para el despiece, aviso para la limpieza del modelo [00:37:47]-[00:38:19].
- La entrada define la salida: si tu entrada no es buena, la salida tampoco lo será [00:38:24]-[00:38:28].
- Volumetría mínima: alcanza con un modelo volumétrico muy básico con la expresión arquitectónica y las dimensiones correctas [00:37:19]-[00:37:37].
- La primera imagen que se carga es la geometría y la segunda tiene que ser exactamente la misma imagen: si no coinciden, la referencia no es coherente [00:33:19]-[00:33:38].
- El error de LoRA y de UNET al importar el workflow es esperable y se resuelve re-eligiendo el LoRA instalado y escribiendo "FLUX.2" en el dropdown del UNET [00:31:59]-[00:33:16].
- Los nodos morados y transparentes están en bypass y no participan; los rosados tampoco se activan con "run" [00:34:30]-[00:34:39], [00:49:03]-[00:49:06].
- Para pasar de una a dos referencias: Bypass con clic derecho o Ctrl+B sobre varios nodos [00:50:34]-[00:50:52].
- Se pueden encadenar varios LoRA uno detrás del otro y combinarlos; el workflow se ajusta solo al borrar un nodo [00:34:23]-[00:34:52].
- Con strength 1 el LoRA no agrega nada: en 1,5 la imagen se rompe y a 1,0 no aporta — el LoRA solo suma cuando el modelo base ya funciona [00:58:06]-[00:59:20].
- El batch count se puede subir a 20, pero conviene dejarlo en 1 [00:58:34]-[00:58:47].
- La seed se controla desde "edit subgraph widgets" (exponiendo "noise seed") o escribiendo el número en el nodo "random noise" dentro del subgraph [00:43:08]-[00:45:33].
- Seed fija = mismo resultado; seed libre = interpretaciones distintas de la misma imagen [00:45:41]-[00:46:15].
- "upscale by" es el único parámetro que realmente importa en el workflow de upscaling; ×3 multiplica por 3 cada lado, ×4 convierte cada píxel en 16 [00:06:18]-[00:06:54].
- El upscaling multiplica el peso del archivo (1,8 MB → casi 25 MB): a veces queda demasiado grande para trabajar [00:08:43]-[00:09:05].
- Creatividad = 1 es literal; = 9 inventa detalles que no estaban (rocas extra, por ejemplo) [00:15:13]-[00:19:03].
- En la galería de Templates, el ícono del workflow dice si corre local o por API: Grok, Magnific y Google son API [00:10:46]-[00:11:19].
- La resolución de salida se escribe a mano en los workflows tipo Topaz (×2 → 2048×2048) [00:14:32]-[00:14:42].
- Los megapíxeles mandan sobre la nitidez final: 1 MP explica que la imagen se vea mal al hacer zoom; 2 mejora y 16 daría más resolución con muchísimo tiempo y créditos [00:36:34]-[00:36:58], [00:54:16]-[00:54:39].
- En 2K y 4K para outputs finales (Nano Banana): 2K en el trabajo diario, 4K para la lámina final, asumiendo el gasto de créditos [01:15:11]-[01:15:26].
- El negro es el color que mejor funciona para marcar ventanas y loggias; hay que probar otros si hace falta [00:40:32]-[00:40:48].
- El prompt en el chat sigue muy bien las instrucciones, pero un plano no marcado puede terminar siendo ventana: se puede reintentar o cambiar el color [00:42:21]-[00:42:37].
- Enmascarar con la zona un poco más grande y opacidad ~75 % en lugar de 100 % [01:09:15]-[01:09:30].
- Nano Banana mete un filtro rosa muy suave: iterar sobre su propia salida apila rosa y lava los píxeles; la forma sana es conservar la imagen base original en Photoshop y pegar solo la zona lograda [01:16:36]-[01:17:39].
- El desplazamiento de píxeles de la salida se corrige bajando la imagen unos píxeles en Photoshop [00:55:35]-[00:55:50].
- El collage en Photoshop (base abajo + editada arriba + máscara) da control real sobre qué se conserva, aunque no sea el método más perfecto [01:01:28]-[01:03:14].
- ComfyUI guarda el prompt en los metadatos de la imagen descargada: a diferencia de Google AI Studio, siempre queda registro de qué se pidió [01:17:56]-[01:18:19].
- El punto de partida son las plantillas de ComfyUI, no un workflow inventado: el instructor toma una plantilla y la ajusta [00:09:50]-[00:10:07].
- La mejor forma de aprender es rehacer el flujo uno mismo, con la captura de Rhino y el material que uno elige [00:38:52]-[00:39:01], [00:46:58]-[00:47:08].
- Photopea cubre el caso de no tener Photoshop [01:03:20]-[01:04:15].

## Qué NO dice el video (para implementarlo)

- **Nombre del archivo del LoRA del curso**: el video solo dice "en mi caso se llama así; en el tuyo se llamará un poco distinto" [00:32:27]-[00:32:33]. No dicho en el video.
- **Distinción basic vs premium del LoRA**: el módulo 3 no la hace; solo dice "selecciona el que quieras usar" [00:32:18]-[00:32:21]. No dicho en el video (la distinción basic/premium aparece en el módulo 2 del curso).
- **Contenido literal del INSTRUCTION.md**: se pega entero, nunca se lee [00:25:44]-[00:26:49]. No dicho en el video.
- **Contenido literal del esqueleto JSON con STRICT CAMERA LOCK**: se ve en pantalla y se copia, no se transcribe [00:31:18]-[00:31:40]. No dicho en el video.
- **Sampler, scheduler, steps y cfg** de los workflows: no dichos en el video.
- **Denoise / strength de img2img**: el módulo no usa un nodo de img2img clásico con denoise; el control de fidelidad pasa por la referencia (ReferenceLatent) y por los megapíxeles. No dicho en el video.
- **Resolución en píxeles exactos** del workflow rhino-to-image: solo se habla de megapíxeles ("déjalo donde está", "16 o algo así"). No dicho en el video.
- **Nombre literal del archivo UNET en el dropdown** (más allá de "FLUX.2 klein 9B"). No dicho en el video.
- **Comando o ExportSize exactos de la captura de Rhino**: el video solo dice "captura del viewport de Rhino o de cualquier 3D" y que se descarga una captura de un archivo de Rhino [00:27:06], [00:28:05]. No dicho en el video.
- **Modelo de upscaling local por defecto** (el que se ejecuta en Comfy Cloud sin API): el video muestra el workflow pero no identifica el modelo que hay dentro. No dicho en el video.
- **Nombre de los nodos internos del subgraph** (salvo "random noise", "megapixels", "strength of the model", "UNET name", "clip name", "VAE name", "LoRA name"): no dichos en el video.
- **Precio y costo en créditos del LoRA premium** y del workflow: no dichos en el video.
- **Formato de salida de los archivos** (PNG/JPEG), dpi o gestión de color: no dichos en el video.

## Qué aporta al concurso AIxGaudi ("The Gaudí Nexus")

- El flujo convierte la volumetría en lámina fotorreal sin salir de ComfyUI: basta un modelo volumétrico muy básico con la expresión arquitectónica y las dimensiones correctas para obtener la imagen final del concurso [00:37:15]-[00:37:42].
- La cámara queda garantizada por texto: `STRICT CAMERA LOCK` y `MATCH CAMERA OF IMAGE 1 EXACTLY` fijan el encuadre de tu modelo, que es el activo del proyecto cuando el render se usa como lámina A1 [00:29:39]-[00:29:52].
- Control programático de la grilla de aberturas: marcar en negro los planos que son loggias o ventanas en el modelo permite que el render convierta esas superficies en aberturas y deje el resto en fachada cerrada [00:40:11]-[00:42:37].
- El contexto se vuelve argumento de proyecto: la ubicación declarada (sur de Europa, Tokio, Kinshasa, Madrid) define vegetación, luz, cielo y materialidad, con el mismo modelo de partida [00:30:15]-[00:30:52], [00:28:49]-[00:29:13].
- Iteración barata para la selección de láminas: seed, batch y collage en Photoshop permiten quedarse con la mejor iteración por zonas y conservar la imagen base original [00:45:41]-[00:46:15], [01:01:28]-[01:03:14].
- Inpainting quirúrgico dentro del mismo grafo (Nano Banana 2) para sumar la loggia, la barandilla o el arbolado de la plaza en el punto exacto, con el prompt registrado en los metadatos de la imagen entregable [01:09:52]-[01:11:13], [01:17:56]-[01:18:19].

## Conceptos relacionados

- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/01-index|WF-rhino-to-image]]
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/03-nodos-WFrhino_to_image|03-nodos-WFrhino_to_image]]
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-instruction-md|prompt-rhino-to-image-instruction-md]]
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-esqueleto-json|prompt-rhino-to-image-esqueleto-json]]
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|LoRA rhino-to-image]]
- [[wiki/glosario/software/flux2-klein-9b|FLUX.2 Klein 9B]]
- [[wiki/glosario/software/comfyui|ComfyUI]]
- [[wiki/glosario/software/comfy-cloud-vs-runpod|Comfy Cloud vs RunPod]]
- [[wiki/glosario/software/rhino|Rhino]]
- [[wiki/glosario/software/grasshopper|Grasshopper]]
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]]
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]]
- [[specs/261019-plan-concurso-gaudi-nexus-ia|Plan del concurso Gaudí Nexus]]

## Cómo lo adaptamos

| Lo que hace el curso | Lo que hacemos nosotros | Por qué |
|---|---|---|
| Grafo rhino-to-image de un subgraph del curso (UNET + Load LoRA + doble referencia + sampler) | Ya tenemos el grafo armado: 23 nodos en API format con doble `ReferenceLatent` encadenado, `FluxKontextMultiReferenceLatentMethod` en método `index`, `Flux2Scheduler` de 4 pasos, `CFGGuider` con cfg 1,0 y `SamplerCustomAdvanced` con `euler` y seed 42 | Partimos de una estructura probada y versionada en vez de reconstruir el subgraph del video: queda trazado, comparable y reproducible entre versiones |
| Render con FLUX.2 klein 9B sobre Comfy Cloud | El render corre en un pod de RunPod con el stack de 18,3 GB subido: transformer fp8 (9,4 GB) + text encoder Qwen3-8B (8,7 GB) + VAE Flux2 (238 MB) | El modelo open source pesa y Comfy Cloud no importa nuestros modelos propios: el pod nos da control del stack y costo por uso |
| Upscale con Topaz y su parámetro "creativity" (1 a 9) | `RealESRGAN_x4plus` (ya en disco) + Hires fix con un segundo KSampler y denoise 0,15-0,35 | El upscale local conserva la imagen en nuestra máquina; la "creativity" del curso se traduce en el denoise del segundo sampler más el prompt de detalle |
| Edición de imagen con Nano Banana 2 (nodo de API dentro de ComfyUI) | `sd-v1-5-inpainting-fp16` en local + IPAdapter (`ip-adapter-plus_sd15` con `CLIP-ViT-H-14-laion2B`) | La edición pasa a ser un paso local y reejecutable: los prompts y las semillas quedan versionados junto al grafo |
| Inpainting con máscara (editor de máscara, opacidad ~75 %) | `sd-v1-5-inpainting-fp16` con Depth Anything 3 (`LoadDA3Model` / `DA3Render`) para sostener la coherencia de profundidad en la zona editada | La coherencia geométrica es el criterio del jurado: la profundidad calculada desde nuestro modelo evita que la zona parcheada se despegue de la volumetría |
| Importación del LoRA desde Hugging Face con token `read` | Queda documentado como procedimiento para Comfy Cloud; en el pod el LoRA (120,8 MB) sube por scp | Documentar la vía del video nos deja la puerta abierta a Comfy Cloud, y en el pod evitamos dejar un secreto en servicios externos |
| Collage final: imagen base abajo + editada arriba + máscara, en Photoshop | Se conserva tal cual en Photoshop, con Photopea como alternativa online gratuita en la lista de recursos del curso | Es la técnica de cierre de imagen que el instructor usa en la práctica: da control sobre qué se conserva de la base y qué se descarta |

## Checks contra el criterio del jurado

- **Criterio de fondo (Cas Esbach, módulo 6 — transcripción pendiente):** el jurado pide lógica constructiva por encima de apariencia. En este módulo, eso se traduce en cinco chequeras operativas.
- **La geometría es del equipo y el LoRA no la altera.** El video lo pide literalmente cuando aparece un desplazamiento de píxeles: "sigue la geometría exactamente" [00:53:25]-[00:53:39]; nosotros verificamos cada salida contra la volumetría con el nodo "compare images" (image A = render, image B = volumetría) [00:35:43]-[00:35:56].
- **El encuadre es un parámetro de proyecto, no una lábia de la IA.** El `STRICT CAMERA LOCK` y el `MATCH CAMERA OF IMAGE 1 EXACTLY` fijan el punto de vista del modelo de Rhino, y eso se lee en el prompt antes de correr [00:31:18]-[00:31:52].
- **El negro en los planos es una decisión proyectual documentada.** Cada plano que se marca en negro queda declarado como ventana o loggia en el prompt que se pega al nodo de texto, con su justificación en la memoria del proyecto [00:40:11]-[00:41:21], [00:41:53]-[00:42:14].
- **La escala real se toma de la cota del producto.** La consigna al modelo incluye el tamaño del material ("3 por 12 centímetros", "haz que la escala coincida"), y el modeloRhino se trabaja a cota antes de exportar la captura [00:52:48]-[00:52:57].
- **El prompt que genera el agente se lee antes de pegarlo.** El JSON sale de un INSTRUCTION.md fijo y de un contexto declarado (tipología y ubicación), y se revisa como documento de proyecto antes de entrar al grafo: es la diferencia entre usar ComfyUI o una plataforma donde el prompt queda en el olvido [00:31:18]-[00:31:52], [01:17:56]-[01:18:19].

_Transcripción del módulo 6 pendiente: el criterio de Cas Esbach se cita de segunda mano hasta que ese módulo esté transcrito y verificado en el vault._
