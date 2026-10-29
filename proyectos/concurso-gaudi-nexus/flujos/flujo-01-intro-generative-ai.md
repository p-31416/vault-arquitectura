---
tipo: flujo-curso
proyecto: concurso-gaudi-nexus
modulo: 1
slug: intro-generative-ai
titulo_curso: "Introduction to Generative AI"
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [mvp_04, comfyui, curso-ai-gaudi, modulo-1, ia-generativa, gaudi-nexus]
idioma: es
---

# Módulo 1 — Introduction to Generative AI (flujo del curso)

> Ficha de flujo del módulo 1 del curso AI×Gaudí, transcrita del video. Fuente verbatim: [[raw/yt/transcripts/2026-10-21_mux-intro-generative-ai.es|transcripción ES]] · [[raw/yt/transcripts/2026-10-21_mux-intro-generative-ai.en|EN]] · plan: [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro de workflows adapted]].

## Ficha

| Dato | Valor |
|------|-------|
| Duración de la pista de subtítulos | 01:30:46,679 → 01:30:49,341 (≈ 1 h 30 min 49 s) · 1.268 cues [00:00:01]-[01:30:46] |
| Idioma | Pista `es` (traducción automática del original en inglés) + pista `en` equivalente, 1.268 cues en cada una [00:00:01] |
| Profesor | Thomas Nelissen — arquitecto (Universidad de Amberes, Bélgica), especialista en IA generativa, junior architect en Davis (París); correo `info@thomasnelissen.ai` [00:00:07], [00:04:54]-[00:05:10], [00:05:54], [00:06:08]-[00:06:24] |
| Contexto institucional | Davis desarrolla **Gaudi One**, un modelo de difusión discreta de última generación [00:07:06]-[00:07:17] |
| Tema | Teoría mínima de la IA generativa (tokens, noise, seed, dataset, entrenamiento y generación por difusión, latent space, VAE) y lectura nodo a nodo del workflow básico de ComfyUI, más la puesta a punto de Comfy Cloud, del "Comfy Expert" y del "Prompt Coach" [00:00:21]-[00:00:30] |
| Herramienta principal | ComfyUI — "la mayor plataforma open source de IA generativa", scale-up iniciada en 2020 o 2021 [00:00:59]-[00:01:38] |

## Objetivo del módulo

Dar la base conceptual y operativa mínima para que los módulos siguientes (text to image, image to image, image to video, image to 3D) se puedan ejecutar entendiendo qué hace cada nodo del workflow estándar de ComfyUI [00:00:33]-[00:00:50].

## El flujo, paso a paso

| # | Acción | Nodo / herramienta (nombre EXACTO en ComfyUI) | Valores que dice el video | Prompt / fórmula | Timestamp |
|---|--------|-------------------------------------------|---------------------------|------------------|-----------|
| 1 | Presentar la plataforma del curso | ComfyUI | Versión gratuita local disponible; el curso usa la suscripción paga [00:00:59]-[00:01:38] | — | [00:00:59]-[00:01:38] |
| 2 | Recorrer el tablero de recursos | Miro | Todo organized por módulo; los recursos están arriba, en "resources" [00:02:52]-[00:04:37] | — | [00:02:52]-[00:04:37] |
| 3 | Verificar el workflow mínimo y el workflow caótico final | ComfyUI | El primero, de nivel principiante; al final del curso, "muchísimas más cosas" [00:01:44]-[00:02:15] | — | [00:01:44]-[00:02:15] |
| 4 | Armar el "Comfy Expert" como proyecto personalizado | LLM de elección (el suyo: Claude) | Las instrucciones son solo dos URLs: documentación de **Comfy Cloud** + **ComfyWiki**; con la captura de pantalla responde paso a paso [00:44:51]-[00:50:21] | Crear proyecto → Instructions → pegar → guardar → preguntar [00:46:52]-[00:47:48] | [00:44:51]-[00:50:21] |
| 5 | Elegir el modelo base con ranking externo | Arena (leaderboard de modelos) | Categorías: chat/text, image editing, open source [00:45:26]-[00:46:46] | — | [00:45:26]-[00:46:46] |
| 6 | Crear la cuenta de render | Comfy Cloud | Standard 20 USD/mes (~16 €); Creator, más créditos (~28 €); Pro "es 100"; Creator = 7.400 tokens/mes; login con Google [00:53:38]-[00:55:19] | — | [00:53:38]-[00:55:19] |
| 7 | Decidir dónde corre el render | ComfyUI local · Comfy Cloud | Local: GPU propia, gratis, FLUX.2 pide ~32 GB VRAM; su PC tiene 12 GB y no alcanza. Cloud: 96 GB de VRAM. Local ≈ 2 min/imagen; Cloud ≈ 5 s [00:50:29]-[00:52:56], [00:53:05]-[00:53:14] | — | [00:50:29]-[00:53:14] |
| 8 | Recorrer la barra lateral | Comfy Cloud (UI) | Activar la beta de **Nodes 2.0** (solo cambia el aspecto); secciones: Templates, Assets, Node library, Model library, Workflows, Apps, Templates [00:55:27]-[00:57:12] | Guardar workflows con "save as" [00:56:52]-[00:57:08] | [00:55:27]-[00:57:12] |
| 9 | Partir de una plantilla en vez de armar el grafo | Templates | "Comfy Cloud ofrece muchas plantillas ya hechas que puedes usar directamente"; en local la plantilla indica qué modelo y qué VAE bajar y en qué carpeta [00:57:12]-[00:58:56] | — | [00:57:12]-[00:58:56] |
| 10 | Ejecutar la plantilla y descargar | Run · Download | La plantilla de edición mete un gorro en la cabeza de una mujer [00:59:26]-[00:59:57] | "to add a beanie on her head" [00:59:34]-[00:59:41] | [00:59:26]-[00:59:57] |
| 11 | Regular la ejecución por vez | Batch count (UI) | Batch count = 1 (el videonobrinda 15 como opción que no recomienda); las imágenes encoladas se ven en la lista de espera [01:00:41]-[01:01:19] | — | [01:00:41]-[01:01:19] |
| 12 | Reproducir una imagen exacta desde Miro | Workflow importable desde Miro ("importable en Comfy") | Se descarga la imagen, se arrastra al workflow, aparecen el prompt y los ajustes exactos del autor; con la misma seed sale la misma imagen [01:01:36]-[01:03:11] | — | [01:01:36]-[01:03:11] |
| 13 | Cargar el modelo de difusión | Load Checkpoint | Puede ser Stable Diffusion 1.5, FLUX.2, FLUX.1 o cualquier modelo open source; en la pantalla de ejemplo se ve Stable Diffusion 1.5 [00:34:05]-[00:34:37] | — | [00:34:05]-[00:34:37] |
| 14 | Declarar lo que se quiere | Prompt (positivo) | El nodo tiene el mismo nombre en los dos casos; lo que define el rol es la salida conectada a "positive" [00:34:39]-[00:35:28] | Texto libre en frases [00:34:39]-[00:34:46] | [00:34:39]-[00:35:28] |
| 15 | Declarar lo que se quiere evitar | Prompt (negativo) | Lo que va ahí, el modelo lo evita; se reconoce por la salida conectada a "negative" [00:34:46]-[00:35:28] | "ajo" (en la analogía del restaurante) [00:39:06]-[00:39:18] | [00:34:46]-[00:35:28] |
| 16 | Fijar la proporción de la salida | Empty Latent Image | Ejemplo del video: 512 × 512; en la prueba, 1024 de ancho → salida rectangular [00:35:33]-[00:36:07], [01:10:18]-[01:10:26] | — | [00:35:33]-[00:36:07], [01:10:18]-[01:10:26] |
| 17 | Generar | KSampler | Es "el motor del auto" / "el fogón": recibe modelo, prompts y latente; de ahí sale la imagen [00:36:13]-[00:36:33] | — | [00:36:13]-[00:36:33] |
| 18 | Fijar o randomizar el ruido de partida | KSampler → seed | "Fixed value" = misma imagen siempre, click tras click; "randomize value" = seed nueva después de cada generación [01:04:32]-[01:07:11] | — | [01:04:32]-[01:07:11] |
| 19 | Definir las iteraciones | KSampler → steps | Valor de la plantilla: 20 (la diapositiva los muestra como "estos diez pasos"); con 4 pasos la imagen sale rota [01:07:11]-[01:08:45] | — | [01:07:11]-[01:08:45] |
| 20 | Definir la fidelidad al prompt | KSampler → CFG | SD 1.5: alrededor de 8. Con 20 el modelo se pasa de literal y rompe la imagen; con 1 hace lo que quiere [01:08:48]-[01:10:13] | — | [01:08:48]-[01:10:13] |
| 21 | Pedir varias salidas por corrida | KSampler → batch_size | 3 en la prueba: una, dos, tres imágenes; equivale a batch count [01:10:32]-[01:10:50] | — | [01:10:32]-[01:10:50] |
| 22 | Guardar el resultado | Save Image | Se asegura de que la imagen quede guardada en el programa [00:37:51]-[00:37:57] | — | [00:37:51]-[00:37:57] |
| 23 | Criterio: elegir la forma del prompt | Prompt (positivo) / (negativo) | Tres formas: **keyword prompting** (workflows antiguos), **lenguaje natural** (el modo actual) y **JSON prompting** (solo FLUX.2, lo escribe un asistente de IA). El curso usa las dos últimas [01:11:12]-[01:13:01] | "un plano gran angular de un hormigón brutalista minimalista" [01:11:50]-[01:11:56] | [01:11:12]-[01:13:01] |
| 24 | Ordenar lo importante al principio del prompt | Prompt (positivo) | "Cuanto antes pongas algo en el prompt, más en serio se lo va a tomar"; ejemplo: que sea Barcelona, al principio [01:11:56]-[01:12:17] | — | [01:11:56]-[01:12:17] |
| 25 | Instalar el "Prompt Coach" | LLM de elección (proyecto + instrucciones) | Dos variantes en el tablero: la sencilla (la que recomienda) y la ultradetallada; el asistente pide modelo y largo/corto, y adapta el prompt a ese modelo [01:13:45]-[01:15:38] | Escribir "start" + la idea ("un pabellón en Barcelona") [01:14:54]-[01:15:29] | [01:13:45]-[01:15:38] |
| 26 | Criterio: descargar los modelos | Hugging Face | En Comfy Cloud no se descarga nada; en local, desde Hugging Face (repo de Stability AI para SDXL, repo de Black Forest Labs para FLUX.2 klein 9B) o desde GitHub [00:52:03], [01:18:12]-[01:19:33] | — | [01:18:12]-[01:19:33] |
| 27 | Criterio: cuándo sumar un LoRA | LoRA | Archivo de ~100 MB entrenado con 20 o 30 imágenes; conoce una sola cosa (una estética, un carácter visual, un arquitecto) y dirige el modelo grande entre pasos [01:22:22]-[01:23:06], [01:28:00]-[01:29:31] | Prompt largo "como si la hubiera diseñado Calatrava" (solo ilustración) [01:23:11]-[01:23:20] | [01:22:22]-[01:29:31] |
| 28 | Criterio: dónde buscar LoRAs | Hugging Face · Civitai · GitHub | También están en la sección "LoRA links" del tablero Miro [01:27:01]-[01:27:29] | — | [01:27:01]-[01:27:29] |
| 29 | Criterio: qué modelo base se usa en el curso | Stable Diffusion 1 · Stable Diffusion XL · FLUX.1 · FLUX.2 klein 9B | "De Black Forest Labs vamos a usar FLUX.1 y FLUX.2 klein 9B. Muy concreto" [01:17:48]-[01:18:05] | — | [01:16:03]-[01:18:05] |

## Modelos y checkpoints mencionados

| Nombre | Qué dice el video de él | Cuándo lo recomienda | Cuándo lo descarta | Timestamp |
|--------|--------------------------|-----------------------|---------------------|-----------|
| Stable Diffusion 1.5 | Primer modelo realmente relevante (2022), entrenado con 860 millones de imágenes + captions [00:16:59]-[00:17:30]. Es el modelo que aparece cargado en el workflow que se ejecuta en pantalla [00:34:24]-[00:34:30] | Para el workflow básico del curso: con él se demuestra steps = 20 y CFG ≈ 8 [01:07:11]-[01:10:06] | Lo llama "el modelo antiguo"; la empresa que lo hizo, Stability AI, "ya no es muy relevante" [01:16:37]-[01:16:42]. Un LoRA entrenado con SD 1.5 no funciona en FLUX.2 [01:26:13]-[01:26:32] | [00:16:59]-[00:17:30], [01:07:11]-[01:10:06], [01:16:37]-[01:16:42] |
| Stable Diffusion 1 / 2 | Parte de la primera tanda de modelos open source grandes (con SDXL y Cascade) [01:16:03]-[01:16:06] | No hay recomendación explícita: "no dicho en el video" | No dicho en el video | [01:16:03]-[01:16:06] |
| SDXL / Stable Diffusion XL | Repo de Stability AI en Hugging Face; la descarga del modelo viejo pesa "seis, casi siete gigabytes" [01:18:54]-[01:19:12]. En la diapositiva de modelos entra como uno de los "cinco primeros, muy famosos" de Stability AI [01:16:33]-[01:16:54] | Entra en el lote de modelos que el curso va a usar ("Stable Diffusion 1 y Stable Diffusion XL") [01:17:48]-[01:17:56] | Lo ubica en "los modelos antiguos" [01:19:12]-[01:19:16] | [01:16:33]-[01:16:54], [01:17:48]-[01:19:12] |
| Cascade | Cuarto modelo de la línea de Stability AI en la diapositiva de historia [01:16:05]-[01:16:10] | No hay recomendación explícita: "no dicho en el video" | No dicho en el video | [01:16:05]-[01:16:10] |
| FLUX.1 | De Black Forest Labs (gente que se fue de Stability AI); salió en 2024 con muchos modelos, cada uno con una función específica [01:17:22]-[01:17:29]. "De Black Forest Labs vamos a usar FLUX.1" [01:18:00]-[01:18:05] | Modelo del curso junto a FLUX.2 klein 9B [01:18:00]-[01:18:05] | No dicho en el video | [01:17:22]-[01:18:05] |
| FLUX.2 | "El modelo de referencia, el mejor"; entrenado con 32.000 millones de imágenes [00:17:23]-[00:17:49]. "El modelo principal que vamos a usar" [00:52:33]-[00:52:39]. En local pide ~32 GB de VRAM [00:52:33]-[00:52:45]. Entiende códigos hex, JSON prompting, gran comprensión contextual y salida hasta 4K [01:20:43]-[01:21:16] | Modelo principal del curso; el JSON prompting es exclusivo suyo [01:12:17]-[01:13:19] | La versión grande "developer" de 64 GB es "gigantesca" y "bastante lenta de ejecutar"; en local, "seguramente explote" [01:19:46]-[01:20:13] | [00:17:23]-[00:17:49], [00:52:33]-[00:52:45], [01:19:46]-[01:21:16] |
| FLUX.2 klein 9B | Repo de Black Forest Labs en Hugging Face; 18 GB porque son 9.000 millones de parámetros [01:19:23]-[01:19:46] | "De Black Forest Labs vamos a usar FLUX.1 y FLUX.2 klein 9B. Muy concreto" [01:18:05]-[01:18:11] | El video lo opone al modelo grande de 64 GB; no lo descarta [01:19:38]-[01:20:05] | [01:18:05]-[01:19:46] |
| FLUX Kontext | Quinto modelo de la línea de Black Forest Labs en la diapositiva [01:16:13]-[01:16:16] | No hay recomendación explícita: "no dicho en el video" | No dicho en el video | [01:16:13]-[01:16:16] |
| Gaudi One | Modelo de difusión discreta de última generación que desarrolla Davis, la empresa del instructor [00:07:06]-[00:07:17] | Se menciona como parte del trabajo de Davis, no como herramienta del curso | No aplica (no es del flujo del curso) | [00:07:06]-[00:07:17] |
| ChatGPT | Caja negra: "escribes un prompt, aparece una imagen" y no tenés control del medio [00:43:46]-[00:43:55]. Primero en el ranking de Arena para edición de imagen [00:46:18]-[00:46:20] | Como alternativa simple frente a la plataforma de nodos [00:43:31]-[00:43:42] | Se lo descarta frente a open weights porque no se le puede "abrir el capó" ni cambiar el motor [00:43:55]-[00:44:23] | [00:43:31]-[00:46:20] |
| Nano Banana | Caja negra de Google; aparece en el ranking de edición de imagen de Arena [00:43:37]-[00:43:53], [00:46:25]-[00:46:28] | Como referencia de ranking | Igual que ChatGPT: control mínimo del proceso [00:43:55]-[00:44:23] | [00:43:37]-[00:46:28] |
| Nano Banana Pro | Comparación directa contra el mismo prompt con y sin LoRA: "tienes menos control, yo diría" [01:24:28]-[01:24:42] | Como termómetro de cuánto control aporta el LoRA frente a una caja negra | Se lo descarta por control, no por calidad [01:24:42] | [01:24:28]-[01:24:42] |
| Midjourney | Caja negra, junto con ChatGPT y Nano Banana [00:43:46]-[00:43:55] | Se lo menciona como la alternativa "sin este enredo" | Se lo descarta por falta de control [00:43:55]-[00:44:23] | [00:43:46]-[00:44:23] |
| Claude | LLM que el instructor usa para el "Comfy Expert" y el "Prompt Coach"; en Arena ocupa los primeros puestos en texto [00:45:12]-[00:46:46] | "Uso Claude porque ahora mismo es simplemente el mejor" [00:46:15]-[00:46:18] | No aplica: el video no lo descarta, solo muestra que ChatGPT o Gemini sirven igual [00:47:19]-[00:47:35] | [00:45:12]-[00:47:35] |
| Modelos de Stability AI (conjunto) | "La primera [empresa] ya no es muy relevante" [01:16:33]-[01:16:42] | — | Como empresa, el video la deja atrás; los modelos que hizo siguen en uso en el curso (SD 1.5, SDXL) [01:17:48]-[01:17:56] | [01:16:33]-[01:17:56] |

> Nota de fidelidad: en la tabla de resumen el video llama "parámetros" a las cifras que antesubló como imágenes de entrenamiento (860 millones en 2022 → 32.000 millones en 2025) [00:17:13]-[00:17:49] vs. [01:21:23]-[01:21:30]. Se conserva la formulación del video.

## Prompts y fórmulas

**Prompt de ejemplo para explicar la tokenización** — `[00:11:06]-[00:11:15]`

```text
a brutalist concrete pavilion at sunset
```

Se descompone en tokens ("a", "brutal", "ist", "concrete", "pavilion", "at", "sunset"), y cada token se traduce a un número. Regla general: 1 token ≈ 0,75 palabras en inglés o ~4 caracteres [00:10:56]-[00:11:04]. El tokenizer que nombra es CLIP [00:11:20]-[00:11:24].

**Caption de dataset (entrenamiento)** — `[00:15:14]-[00:15:17]`

```text
un edificio brutalista asomado al borde de un paisaje erosionado
```

**Caption de entrenamiento (ejemplo con ruido)** — `[00:20:08]-[00:20:11]`

```text
un edificio de apartamentos escultórico, azulejos azul profundo brillantes, pueblo español en verano
```

**Prompt de generación (proceso inverso)** — `[00:23:06]-[00:23:13]`

```text
estructura de fachada de mármol rojo con vetas blancas visibles. Montantes de ventana negros, reflejo en el vidrio.
```

**Prompt del workflow básico que se ejecuta en pantalla** — `[01:04:54]-[01:05:02]`

```text
beautiful scenery nature glass bottle landscape, purple galaxy bottle
```

El video lo llama "un prompt rarísimo" y muestra que la imagen sale así [01:05:02]-[01:05:06].

**Prompt de la plantilla de edición de imagen** — `[00:59:34]-[00:59:41]`

```text
to add a beanie on her head
```

**Lenguaje natural (forma recomendada)** — `[01:11:50]-[01:11:56]`

```text
un plano gran angular de un hormigón brutalista minimalista, etc.
```

**JSON prompting: misma información, otra estructura** — `[01:13:23]-[01:13:37]`

```text
crea una lista de cinco ideas de startup sobre sostenibilidad
```

```text
generar ideas, ámbito sostenibilidad, tipo startup, cantidad cinco
```

**Prompt negativo (analogía del restaurante)** — `[00:38:48]-[00:39:18]`

```text
[positivo] quiero pollo con papas
[negativo] ajo
```

**Fórmula de uso del Prompt Coach** — `[01:14:41]-[01:15:29]`

```text
start
+ idea o prompt propio ("un edificio en las Montañas Rocosas", "un pabellón en Barcelona")
→ el asistente pregunta: ¿qué modelo? ¿prompt largo o corto?
→ devuelve el prompt ya adaptado a ese modelo
```

### Regla de estructura que explica el video

1. **Orden**: lo importante va primero — "cuanto antes pongas algo en el prompt, más en serio se lo va a tomar" [01:11:56]-[01:12:17].
2. **Forma**: frases en lenguaje natural para los modelos actuales; el prompt por palabras clave pertenece a workflows antiguos [01:11:12]-[01:11:48].
3. **JSON**: estructura alternativa que el modelo entiende mejor; en el curso la escribe un asistente de IA y es exclusiva de FLUX.2 [01:12:20]-[01:13:19].
4. **Negativo**: lo que se quiere evitar se declara en el prompt negativo, que el modelo acata [00:34:46]-[00:34:54].
5. **Límite del conocimiento**: el modelo solo reconoce lo que estaba en su dataset o caption; "un modelo entrenado con millones de gatos etiquetados como gato aprende el concepto visual de gato, pero nunca va a aprender qué es un edificio de Zaha Hadid salvo que esa etiqueta estuviera en el dataset" [00:26:34]-[00:26:49].
6. **Correo al prompt**: el modelo solo ve tokens (números), nunca palabras [00:10:36]-[00:12:04].

## Reglas, buenas prácticas y trampas

- Las plantillas del curso y las de Comfy ya vienen con los mejores ajustes: dejalas como están y reservá el cambio para la experimentación [01:08:08]-[01:08:39].
- Para Stable Diffusion 1.5, el CFG se mantiene alrededor de 8 [01:10:00]-[01:10:06].
- Con seed en "fixed value", cada corrida devuelve la misma imagen: eso habilita la reproducibilidad del resultado [01:06:05]-[01:06:43].
- Con seed en "randomize value", cada generación parte de un ruido distinto y produce una imagen distinta [01:05:12]-[01:05:40].
- Los steps tienen que alcanzar para terminar la imagen: con 4 pasos, el resultado sale roto [01:07:18]-[01:07:37].
- El batch count queda en 1; 15 ejecuciones en un solo clic se respondió como opción que el video no recomienda [01:00:41]-[01:01:05].
- Cada LoRA se usa con el modelo base para el que fue entrenado: revisá siempre para qué modelo se creó [01:26:13]-[01:26:35].
- Un LoRA dirige al modelo grande entre los pasos: conoce una estética, un carácter visual o un arquitecto, y solo puede hacer eso [01:28:00]-[01:29:31].
- LoRA = ~100 MB entrenado con 20 o 30 imágenes, al alcance de cualquiera; el modelo grande queda fuera del alcance del usuario [01:22:30]-[01:23:06].
- Quien cura el dataset decide lo que el modelo puede imaginar: sesgos, vacíos y estética quedan horneados antes del primer prompt [00:15:41]-[00:15:57].
- En ComfyUI el flujo va siempre de izquierda a derecha: input → generación → output [00:33:00]-[00:33:32].
- Los nodos solo conectan tipos compatibles: al arrastrar un cable a un socket de otro tipo, el nodo queda transparente y el enganche se hace solo con el tipo correcto [01:03:47]-[01:04:14].
- Para resolver un bloqueo, el "Comfy Expert" con la documentación de Comfy Cloud y ComfyWiki alcanza: "el 99 % de las veces me ayuda a resolver el problema" [00:50:03]-[00:50:21].
- Para elegir modelo, Arena se actualiza todos los días: es la fuente de verdad sobre qué modelo está arriba hoy [00:46:36]-[00:46:40].
- Para renderizar, Comfy Cloud da 96 GB de VRAM y ~5 s por imagen frente a los ~2 min en local [00:52:52]-[00:53:14].
- El workflow importable desde Miro trae el prompt y los ajustes exactos del autor: arrastrarlo y correrlo reproduce la imagen exacta [01:02:35]-[01:03:11].
- Los LoRAs interesantes están en Hugging Face, Civitai y GitHub, indexados en el tablero del curso [01:27:01]-[01:27:29].
- La beta de Nodes 2.0 solo cambia el aspecto de la interfaz [00:56:04]-[00:56:12].
- Los workflows guardados con "save as" quedan disponibles en la sección Workflows [00:56:52]-[00:57:08].

## Qué NO dice el video (para implementarlo)

| Vacío | Estado |
|-------|--------|
| Resoluciones exactas por modelo | **no dicho en el video**. Solo aparecen 512 × 512 como ejemplo del nodo [00:35:44]-[00:35:53], 1024 de ancho en la prueba [01:10:18]-[01:10:26] y "hasta 4K" para FLUX.2 [01:21:08]-[01:21:10]. No hay tabla resolución → modelo. |
| Seeds concretas | **no dicho en el video**. Se explica que el noise lleva una seed de "14 números" y se muestra un ejemplo en pantalla [00:12:48]-[00:12:55], pero nunca se transcribe el valor. |
| Sampler y scheduler concretos | **no dicho en el video**. El nodo KSampler se nombra y se explican seed, steps y CFG [00:36:13]-[00:37:49]; sampler_name y scheduler no aparecen. |
| Nombres de archivo de modelos | **no dicho en el video**. Se nombran familias y repos (SD 1.5, SDXL, FLUX.1, FLUX.2, FLUX.2 klein 9B) y pesos en GB [01:18:54]-[01:19:46], nunca un `.safetensors`. |
| Valores de CFG y steps para FLUX.2, FLUX.1 o SDXL | **no dicho en el video**. El video dice "para modelos más nuevos, los ajustes son otros" y deja el tema para otro momento [01:10:11]-[01:10:13]. |
| Nombre exacto del nodo de LoRA | **no dicho en el video**. Solo se dice "LoRA" y que se aplica entre los pasos; el nombre de la interfaz no se pronuncia [01:28:00]-[01:29:31]. |
| Trigger word de los LoRAs | **no dicho en el video**. |
| Texto literal del prompt del "Comfy Expert" y del "Prompt Coach" | **no dicho en el video**: están en el tablero Miro, y el video solo los muestra y describe [00:47:37]-[00:47:48], [01:14:02]-[01:14:35]. |
| Prompt completo de la plantilla de edición de imagen | **no dicho en el video**: solo se menciona el efecto ("un gorro en la cabeza") [00:59:34]-[00:59:41]. |
| Nombre y carpeta de destino de los modelos en local | **no dicho en el video**: la plantilla muestra la carpeta en pantalla y el video la describe sin transcribir la ruta [00:58:46]-[00:58:56]. |
| Unidades de los planes de Comfy Cloud | **no dicho en el video**: el video alterna "créditos" y "tokens"; el Creator aparece con 7.400 tokens/mes y "el Pro son 100", sin fijar la unidad [00:54:34]-[00:55:19]. |
| Nombre del modelo de la talk "Fable 5" | **no dicho en el video**: la pista dice literalmente "Claude, Fable 5; después está Opus" [00:46:02]-[00:46:07]. |
| Tokenizer propio de FLUX.2 | **no dicho en el video**: el único tokenizer nombrado es CLIP, en el ejemplo de Stable Diffusion [00:11:20]-[00:11:24]. |
| Contenido del PDF de "models overview" | **no dicho en el video**: se menciona que existe y que el instructor lo escribió [01:21:54]-[01:22:11]. |

## Qué aporta al concurso AIxGaudi ("The Gaudí Nexus")

1. **Trazabilidad de la lámina**: seed fija + plantilla con sus ajustes = la imagen final se puede regenerar idéntica meses después; con el workflow importable desde Miro, la reproduce cualquiera del equipo [01:02:35]-[01:03:11], [01:04:32]-[01:06:43].
2. **Accesibilidad de FLUX.2 sin supercomputadora**: Comfy Cloud aporta 96 GB de VRAM frente a los ~32 GB que el modelo exige en local, y el plan Creator (~28 €) alcanza para el mes de concurso [00:52:33]-[00:53:14], [00:54:53]-[00:55:19].
3. **Dirección de la estética con LoRA**: un LoRA de ~100 MB entrenado con 20-30 fotos propias lleva la salida hacia el registro visual del estudio, en lugar de aceptar la estética genérica de una caja negra [01:22:22]-[01:23:06], [01:25:34]-[01:26:11].
4. **Regla de escritura del prompt**: el elemento decisivo (la ubicación, la materialidad) al principio del prompt, y el JSON como estructura para FLUX.2 [01:11:56]-[01:13:19].
5. **Agente de soporte propio**: el "Comfy Expert" con la documentación oficial resuelve los bloqueos durante la producción, con un 99 % de aciertos según el instructor [00:44:51]-[00:50:21].
6. **Selección de modelo con evidencia externa**: Arena como termómetro diario de qué modelo está arriba, para no elegir por costumbre [00:45:26]-[00:46:46].

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|ComfyUI]]
- [[wiki/glosario/software/comfy-cloud-vs-runpod|Comfy Cloud vs RunPod vs local — dónde renderizar]]
- [[wiki/glosario/software/flux2-klein-9b|FLUX.2 Klein 9B]]
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|LoRA rhino-to-image del curso AI×Gaudí]]
- [[wiki/glosario/software/grasshopper|Grasshopper]] — la analogía de programación visual que usa el video
- [[wiki/glosario/software/github|GitHub]] — vía de instalación local de ComfyUI
- [[wiki/fuentes/comfyui-for_architects-architutors|ComfyUI for Architects (fuentes del curso)]]
- [[proyectos/MVP_04-comfyui-arquitectura/00-index|MVP_04 — ComfyUI Arquitectura]]
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|Reglas para creación de workflows en ComfyUI]]
- [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|Extracción del material del curso AI×Gaudí (Miro + Archademy)]]
- [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|Modelos recomendados para render arquitectónico en ComfyUI]]

## Cómo lo adaptamos

| Lo que hace el curso | Lo que hacemos nosotros | Por qué |
|----------------------|-------------------------|---------|
| Renderiza en Comfy Cloud, con 96 GB de VRAM y ~5 s por imagen [00:52:52]-[00:53:14] | Corremos local, con SD1.5 `architecturerealmix_v11` ya en disco | El stack completo vive en la máquina: las corridas base del WF-01 salen sin gasto de cómputo y sin depender de la disponibilidad de la nube |
| Muestra los ajustes de la plantilla del curso: steps 20 y CFG ≈ 8 para SD1.5 [01:07:11]-[01:10:06] | Mantenemos el mismo protocolo de seed / steps / CFG y cambiamos una sola variable por corrida | El grafo queda comparable con el del video y cada diferencia de resultado queda atribuible a un único factor |
| Instala el "Prompt Coach" como proyecto de un LLM con sus instrucciones pegadas [01:13:45]-[01:15:38] | Lo implementamos como proyecto de Claude con las instrucciones del tablero del curso pegadas | El prompt se escribe una sola vez, con el mismo criterio de orden y de formato que enseña el módulo, y queda versionado con el equipo |
| Recorre plantillas de Comfy Cloud y modelos que corren en la nube [00:57:12]-[00:58:56] | El WF-01 se resuelve con los nodos locales del stack en disco; los nodos partner quedan reservados para los módulos donde aportan (imagen→3D, upscale, edición) | Cada workflow del concurso tiene su ruta local equivalente y el grafo base queda ejecutable en nuestra máquina |
| Valida la plantilla en la nube antes de correrla [00:58:30]-[00:58:56] | Antes de cada corrida validamos cada `class_type` y cada widget contra `/object_info` del servidor local | Cada corrida arranca con el grafo verificado contra los nodos realmente instalados, y el resultado de la validación queda en el `02-WF-log` |

## Checks contra el criterio del jurado

- **Reproducibilidad**: la misma seed devuelve exactamente la misma imagen, tal como demuestra el video [01:06:05]-[01:06:43]; en el WF-01 se verifica con las tres corridas A (seeds 42 / 77 / 123) y con la corrida de control de seed fija.
- **Registro del prompt en los metadatos de la imagen**: el prompt y la negativa viajan embebidos en el PNG de salida, de modo que cada imagen de la entrega queda con su prompt asociado y verificable.
- **Trazabilidad del grafo**: cada imagen se reconstruye desde su `workflow_*.json` en API format, su `03-nodos-<nombre>.md` (campo · valor · justificación) y su `02-WF-log` con seed, steps, CFG, modelo, tiempo y VRAM.
- **Criterio aplicado sobre la apariencia**: la lógica constructiva sobre la apariencia —el criterio que el jurado evaluates— se traduce en este WF de base en esas tres cosas: la imagen se regenera, se explica y se vuelve a producir con el mismo resultado.
- **Pendiente de fuente**: la transcripción del módulo 6 (Round Table, donde Cas Esbach explica el criterio del jurado) está pendiente; el checklist definitivo de este flujo se cierra contra esa transcripción.
