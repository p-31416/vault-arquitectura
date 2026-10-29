---
tipo: flujo-curso
proyecto: concurso-gaudi-nexus
modulo: 4
slug: image-to-video
titulo_curso: "Image-to-Video"
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [mvp_04, comfyui, curso-ai-gaudi, modulo-4, image-to-video, ltx, seedance, gaudi-nexus]
idioma: es
---

# Módulo 4 — Image-to-Video (flujo del curso)

> Ficha de flujo del módulo 4 del curso AI×Gaudí, transcrita del video. Fuente verbatim: [[raw/yt/transcripts/2026-10-21_mux-image-to-video.es|transcripción ES]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-video.en|EN]] · plan: [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro de workflows adapted]].

## Ficha

- **Duración de la pista:** 00:26:18,946 → 00:26:22,222 (26 min 22 s) [00:26:18]
- **Idioma:** español (transcripción automática de los subtítulos del módulo; la versión `.en` es la traducción del mismo audio)
- **Profesor:** no identificado en el video. Es el módulo 4 del curso AI×Gaudí de Archademy, con material de la Fundació Antoni Gaudí
- **Tema:** llevar una imagen de partida a video dentro de ComfyUI con Seedance 2.0 vía API, y aprender a dirigir cámara y montaje (encuadre de un detalle, secuencia de planos, time-lapse) escribiendo el prompt y anotando la imagen de entrada.

> **Nota de fuentes:** todo lo técnico de este documento sale de la transcripción ES del módulo (`[[raw/yt/transcripts/2026-10-21_mux-image-to-video.es|transcripción ES]]`), con timestamp `[HH:MM:SS]`. Cuando el texto literal de un prompt aparece en el tablero Miro del curso y el video solo lo muestra en pantalla, se marca como «texto del tablero» con su wikilink a `[[raw/research/2026-10-20-miro-curso/miro-inventario|miro-inventario]]`.

## Objetivo del módulo

Convertir una imagen estática en un video controlado —encuadre, secuencia y montaje— dentro de ComfyUI con Seedance 2.0, sabiendo cuánto cuesta cada ejecución y cómo dirigir el modelo con el prompt y con anotaciones sobre la imagen.

## El flujo, paso a paso

| # | Acción | Nodo / herramienta (nombre EXACTO) | Valores que dice el video | Prompt / fórmula | Timestamp |
|---|--------|------------------------------------|---------------------------|------------------|-----------|
| 1 | Abrir la plantilla de image-to-video | plantillas de ComfyUI, filtradas por «Seedance 2.0» | tres plantillas: varias imágenes de referencia para enlazarlas; primer y último fotograma; la más simple (una sola imagen) | — | [00:06:41]–[00:07:18] |
| 2 | Sacar de servicio las ramas de imagen que no se usan | `bypass` (Ctrl+B o clic derecho → «bypass») sobre «image four» y «image three» | — | — | [00:01:42]–[00:02:26] |
| 3 | Cargar la imagen de partida | nodo de imagen base (arrastrar y soltar) | la fachada con la barandilla editada y la loggia, generada en el módulo 3 con image to image | — | [00:02:04], [00:07:24]–[00:07:44] |
| 4 | Vaciar el prompt que trae la plantilla | nodo de prompt | — | — | [00:02:38]–[00:02:44], [00:07:22] |
| 5 | Fijar la proporción | widget de proporción | «adaptive» (o la proporción exacta si la conocés) | — | [00:03:44]–[00:03:58], [00:09:14]–[00:09:20] |
| 6 | Fijar la duración | widget de duración | 7 s (prueba) · 8 s (ejemplo anotado) · 15 s (duplica el costo) | — | [00:03:58]–[00:04:13], [00:09:20]–[00:09:26], [00:12:01] |
| 7 | Fijar la resolución | widget de resolución | 720 px mientras se prueba · 480 para probar y 1080 después (video de cliente o del concurso) · 4K (el más caro) | — | [00:03:31]–[00:03:38], [00:09:09]–[00:09:14], [00:09:45] |
| 8 | Definir si el video lleva audio | widget «generate audio» | activado: desactivarlo no abarata | — | [00:09:30]–[00:09:38] |
| 9 | Fijar la semilla | widget `seed` | la que viene por defecto (en este workflow no importa) | — | [00:09:38]–[00:09:45] |
| 10 | Redactar la intención en el prompt coach | prompt coach (dentro de Claude) | se escribe «start», se sube la imagen y se nombra el modelo | «Seedance 2.0» + la acción pedida | [00:04:41]–[00:05:44] |
| 11 | Copiar el prompt que devuelve | salida del prompt coach | prompt larguísimo en JSON, con una parte en chino que se puede borrar | — | [00:05:59]–[00:06:24] |
| 12 | Pegar y ejecutar | nodo de prompt + «run» | el nodo se pone azul mientras genera y el video de salida aparece en el workflow | — | [00:05:50]–[00:06:34] |
| 13 | Leer la escala de créditos antes de correr | contador de créditos del workflow | 320 créditos por ejecución · 148 a baja resolución · 1.600 en 4K · ~170 por 7–8 s · 3.400–3.500 en 4K (15 s) · 4K + 15 s ≈ 30 € por video (el instructor estima «unos veinte euros») | — | [00:02:33]–[00:04:26], [00:09:45]–[00:10:14] |
| 14 | Anotar la imagen para dirigir el encuadre | imagen de entrada anotada (dos colores: círculo rojo y círculo azul) | el video dura 8 s | «Primero haz que el video haga zoom en el detalle de la barandilla marcado en rojo, y después que haga zoom en el círculo azul. El video dura ocho segundos.» | [00:11:17]–[00:12:13] |
| 15 | Iterar el prompt con la corrección de cámara | prompt coach | el primer zoom fue exacto; el segundo se fue al montante de la ventana en vez de la esquina | «hazlo más específico… asegúrate de que hace zoom en la esquina marcada con el círculo azul… transición suave… todo un plano continuo y sin cortes» | [00:13:22]–[00:15:18] |
| 16 | Alternativa de montaje: dos clips y se pegan | dos renders separados + montaje | un plano de ~4 s + otro de ~4 s | «un plano de unos cuatro segundos con zoom sobre el detalle rojo, y después otro con zoom sobre el azul, el círculo azul, y montarlos juntos» | [00:16:36]–[00:16:47] |
| 17 | Camino alterno: varias imágenes → secuencia de planos | plantilla de ComfyUI que toma más de una imagen | un único video de 7 s | varias tomas del edificio → el prompt coach escribe el prompt → se pega en ComfyUI | [00:17:53]–[00:19:12] |
| 18 | Camino alterno: time-lapse de trípode fijo | plantilla de ComfyUI con una sola imagen de entrada | resultado bueno: el edificio queda estático y las cosas se mueven | «trípode fijo, time lapse, el edificio permanece completamente estático, las nubes se desplazan lentamente por el cielo» | [00:19:17]–[00:21:29] |
| 19 | Camino alterno: video a video con interpolación de fotogramas | workflow de interpolación de fotogramas | convierte un video de 7 s en uno de 14 s (duplica la cantidad de fotogramas) | — | [00:21:43]–[00:23:10] |
| 20 | Instalar la skill de Seedance | skill de Claude («more» → exportar como markdown → importar en Claude como skill) | genera prompts específicamente para Seedance 2.0 | — | [00:24:04]–[00:24:55] |
| 21 | Probar el modelo más avanzado de Google | Google Omni | un prompt para conseguir las cuatro estaciones | — | [00:24:59]–[00:25:18] |
| 22 | Inspirarse con el banco de prompts | web de prompts de Seedance 2.0 (en «resources») | prompts en tendencia; filtros por «arquitectura» o «animación» | — | [00:25:39]–[00:26:08] |

## Modelos y servicios mencionados

| Nombre | Local o API | Qué dice el video de él | Cuándo lo recomienda | Cuándo lo descarta | Timestamp |
|--------|-------------|------------------------|-----------------------|--------------------|-----------|
| Seedance 2.0 | API, se paga con créditos | «Esto funciona por API»; 320 créditos por ejecución a 720 px / 7 s; 1.600 en 4K; 3.400–3.500 en 4K de 15 s; ≈30 € por video | image → video con control del encuadre vía prompt + anotaciones sobre la imagen | cuando el prompt largo del coach no aporta: un prompt simple y corto rindió mejor | [00:02:33]–[00:04:26], [00:21:19] |
| LTX | no dicho en el video | «Este es otro modelo, llamado LTX»; se lo muestra como otro ejemplo junto a Seedance; el video no enseña el workflow entero | como alternativa de modelo de video | no dicho en el video | [00:23:27]–[00:23:45] |
| Google Omni | no dicho en el video (el video no aclara si es local o API) | «el modelo de video más avanzado de Google»; con él probó el prompt de las cuatro estaciones | cuando se quiere un video de alto nivel | no dicho en el video | [00:24:59]–[00:25:18] |
| Kling | no dicho en el video | no aparece en este módulo (el tablero del curso sí enlaza `kling.ai`) | no dicho en el video | no dicho en el video | — |
| ComfyUI («Comfy») | no dicho en el video (local o cloud, no aclara) | plantillas, `bypass`, arrastrar y soltar, «open as workflow in a new tab», metadatos con el prompt del video | es el entorno de los tres workflows del módulo | no dicho en el video | [00:01:11], [00:20:42] |
| Claude + prompt coach | no dicho en el video (el video no aclara el tipo de cuenta) | assistant que devuelve un prompt JSON larguísimo, con una parte en chino, y a veces avisa cosas («subí el render limpio, no el PNG anotado») | para escribir el prompt de Seedance 2.0 sin(necesitar) la sintaxis del modelo | cuando su prompt largo «no era nada del otro mundo»: un prompt simple dio mejor resultado | [00:04:41]–[00:05:15], [00:12:21], [00:21:19]–[00:21:25] |
| Adobe After Effects / Adobe Premiere Pro | no dicho en el video | al ralentizar un video ahí, los fotogramas se estiran y el resultado se ve muy entrecortado | — | el workflow de interpolación de fotogramas reemplaza esa lentitud | [00:22:04]–[00:23:10] |
| Miro | tablero | del lado derecho de Miro están los recursos del módulo: workflows, prompts y enlaces | donde está el catálogo de recursos | — | [00:21:35]–[00:21:43] |
| Web de prompts de Seedance 2.0 | web, dentro de «resources» | «un montón de prompts para Seedance 2.0», con tendencias y filtros | inspiración y banco de estructuras de cámara | — | [00:25:39]–[00:26:08] |
| Skill de Seedance (exportable como markdown) | servicio (Claude) | genera prompts específicamente para Seedance 2.0 | como atajo frente a las instrucciones del prompt coach | es opcional: es «un poco como las instrucciones del proyecto… pero de otra manera» | [00:24:04]–[00:24:55] |

## Prompts y fórmulas

### 1. Prompt mínimo en el prompt coach

```
Quiero un zoom cinematográfico sobre la barandilla de la loggia.
```

[00:05:18]–[00:05:35]. El detalle es un punto importante que se quiere mostrar en la presentación.

### 2. El mismo prompt nombrando el modelo (el coach escribe para ese modelo)

```
Seedance 2.0: quiero un zoom cinematográfico sobre la barandilla de la loggia.
```

[00:08:19]–[00:08:24]. Nombrar el modelo alcanza para que el coach aplique las instrucciones de prompting de ese modelo [00:04:56]–[00:05:15].

### 3. Con anotaciones sobre la imagen, secuencia y duración

```
[describir en voz alta los dos detalles marcados, con dos colores distintos]

Primero haz que el video haga zoom en el detalle de la barandilla marcado en rojo,
y después que haga zoom en el círculo azul.
El video dura ocho segundos.
```

[00:11:17]–[00:12:13]. Los detalles que nombra: cómo la barandilla se conecta al muro y cómo el panel (los montantes de la ventana) se conecta a la esquina [00:11:28]–[00:11:40].

### 4. Iteración: control de cámara y de montaje

```
Hazlo más específico.
Asegúrate de que hace zoom en la esquina marcada con el círculo azul.
Asegúrate de que haga una transición suave entre el primer plano,
el zoom sobre el detalle rojo, y el segundo plano, el detalle de la esquina azul.
Asegúrate de que sea todo un plano continuo y sin cortes.
```

[00:13:22]–[00:15:18]. La instrucción nació de un resultado que cortaba de golpe entre encuadres [00:13:45]–[00:14:03].

### 5. Recorrido con flecha

```
Después del primer zoom, sigue la flecha verde hasta este detalle.
```

[00:16:24]–[00:16:31]. «Probablemente lo hará» [00:16:31].

### 6. Dividir en dos clips y montar

```
...un plano de unos cuatro segundos con zoom sobre el detalle rojo,
y después otro con zoom sobre el azul, el círculo azul,
y montarlos juntos.
```

[00:16:36]–[00:16:47]. «Hay infinitas formas de hacerlo» [00:16:47].

### 7. Time-lapse de trípode fijo

```
Trípode fijo, time lapse, el edificio permanece completamente estático,
las nubes se desplazan lentamente por el cielo, etc.
```

[00:19:34]–[00:19:46]. La versión en inglés que el curso deja escrita en el tablero (texto del tablero, el video lo muestra):

```
Fixed tripod time-lapse. Building remains completely static. Clouds drift across the sky.
Sunlight and shadows shift from morning to night time. Movement of people on the balcony.
Trees and plants sway gently. No camera movement.
```

### 8. Las cuatro estaciones con Google Omni (texto del tablero; el video lo muestra)

```
Cinematically zoom in on the facade tiles, end in extreme close-up.
Use this image as the start frame.
During the zoom-in, all 4 seasons pass dramatically.
It starts with summer (start frame), then rainy autumn, then snowwy winter
and then spring (end frame which is the close-up)
```

[00:24:59]–[00:25:18].

### 9. La fórmula de escalonado temporal que el modelo escribe en el prompt

```
del segundo uno al cuatro, haz esto; del cuatro al ocho, haz aquello.
```

[00:12:03]–[00:12:13]. Es la forma que adopta el prompt cuando hay más de un movimiento: la duración declarada se reparte en tramos de segundos [00:12:01]–[00:12:13].

### Reglas de estructura que da el video

- **Nombrar el modelo** al pedir el prompt («Seedance 2.0»), para que el coach escriba para ese modelo [00:04:56]–[00:05:15].
- **Declarar la duración** en segundos junto con la acción, para que el prompt se escalone en tramos [00:12:01]–[00:12:13].
- **Anotar la imagen de entrada** con dos colores, uno por detalle, para quitar la ambigüedad de las palabras [00:11:46]–[00:11:52], [00:16:51].
- **Pedir continuidad** («transición suave», «todo un plano continuo», «sin cortes») cuando el corte entre encuadres queda brusco [00:14:48]–[00:15:04].
- **Releer el prompt devuelto** antes de pegarlo, porque a veces afirma cosas que no son ciertas [00:06:13]–[00:06:17].
- **Borrar la parte en chino** del prompt si molesta (el instructor la deja) [00:06:19]–[00:06:24].
- **Probar la vía corta** —un prompt simple— cuando el prompt largo no aporta [00:21:19]–[00:21:25].

## Reglas, buenas prácticas y trampas

- Probá a 480 y volvé a 1080 después: es la estrategia declarada para un video de cliente o del concurso [00:03:25]–[00:03:38].
- Mientras no sepás la proporción exacta de la imagen, dejala en «adaptive»: es más seguro [00:03:44]–[00:03:58], [00:09:14]–[00:09:20].
- Arrancá en 7 s y 720 px mientras probás; el costo escala con resolución y con duración [00:09:45]–[00:10:14].
- Dejá «generate audio» activado: apagarlo no abarata la corrida [00:09:30]–[00:09:38].
- Dejá la `seed` como viene: en este workflow no aporta [00:09:38]–[00:09:45].
- Poné en `bypass` las ramas de imagen que no usás, así el grafo queda de una sola entrada [00:01:42]–[00:02:26].
- Anotá la imagen de entrada con un color por detalle: es la vía de control del encuadre [00:11:46], [00:16:51].
- Sumale una flecha de color para indicar el recorrido entre detalles [00:16:24]–[00:16:31].
- Declará la duración para que el coach reparta la acción en tramos de segundos [00:12:01]–[00:12:13].
- Pedí «transición suave», «plano continuo» y «sin cortes» cuando el paso entre encuadres quede duro [00:13:45]–[00:15:04].
- Como plan B, armá dos clips de ~4 s y montalos: el control por fragmento es más seguro que por video largo [00:16:36]–[00:16:47].
- Releé el prompt largo antes de pegarlo: el coach a veces mete afirmaciones que no son ciertas [00:06:13]–[00:06:17].
- Cuando el prompt largo no dé resultado, escribí un prompt corto y probá así [00:21:19]–[00:21:25].
- Los videos descargados se arrastran a ComfyUI y muestran el prompt con el que se generaron [00:15:41]–[00:16:05].
- Al abrir un workflow descargado, los errores de imágenes faltantes suelen ser falsos positivos: las imágenes de entrada no siempre quedan en los metadatos [00:17:31]–[00:17:49].
- El workflow de interpolación duplica la cantidad de fotogramas (7 s → 14 s) y evita el look entrecortado de ralentizar en After Effects o Premiere Pro [00:21:43]–[00:23:10].
- El morph de la primera imagen a la última tiene aire de «AI slop»: sirve para arrancar, no como pieza de concurso [00:00:43]–[00:01:00].
- La skill de Seedance es opcional: hace lo mismo que las instrucciones del prompt coach, por otra vía [00:24:49]–[00:24:55].
- El tablero tiene los tres workflows completos y los ejemplos descargables [00:21:33]–[00:21:43], [00:23:45].
- Filtrá el banco de prompts por «arquitectura» o «animación» según el objetivo [00:25:54]–[00:26:02].

### Trampas y límites por herramienta

- **Seedance 2.0 (API):** el costo es el límite real — 320 créditos por ejecución, 1.600 en 4K, 3.400–3.500 en 4K de 15 s, ≈30 € por video [00:02:41]–[00:04:26], [00:09:45]–[00:10:08].
- **Seedance 2.0 (encuadre):** el acierto del encuadre no está garantizado — el primer zoom fue exacto, el segundo se fue al montante de la ventana en vez de la esquina, y se corrigió iterando [00:13:07]–[00:13:22].
- **Prompt coach:** devuelve un JSON larguísimo que hay que leer antes de pegar, y a veces empeora el prompt en lugar de mejorarlo [00:05:59]–[00:06:17], [00:21:19]–[00:21:25].
- **Prompt coach (feedback):** su aviso fue «subí el render limpio, no el PNG anotado»; el instructor no lo siguió y usó la imagen anotada [00:12:21]–[00:12:34].
- **LTX:** el video no muestra el workflow entero, así que no hay valores para replicar [00:23:31]–[00:23:38].
- **Google Omni:** el video no da costos ni requisitos [00:24:59]–[00:25:18].

## Qué NO dice el video (para implementarlo)

- **Nombre exacto del nodo de ComfyUI para Seedance 2.0** — el video solo dice «una imagen base, este nodo» y «el prompt lo vamos a borrar» — no dicho en el video.
- **Nombre de las plantillas** — solo se indica filtrar por «Seedance 2.0» y que son tres — no dicho en el video.
- **El texto del prompt JSON que devuelve el prompt coach** — se muestra en pantalla pero no se lee — no dicho en el video.
- **El precio en euros del crédito y el nombre del plan** — el video solo dice «depende un poco de tu plan» y estima «al menos cinco o diez euros» por video — no dicho en el video.
- **La URL del banco de prompts de Seedance 2.0** — se llega por los enlaces de «resources» — no dicho en el video.
- **Si LTX corre local o por API, y con qué checkpoint** — no dicho en el video.
- **El contenido de la skill de Seedance y sus reglas de cámara por arquetipo** — el video solo menciona que existe y que se puede exportar como markdown e importar en Claude — no leído en el video.
- **Kling** — no aparece en este módulo; el tablero del curso sí enlaza `kling.ai` — no dicho en el video.
- **Cómo se abre la cuenta, se contratan los créditos o se configura el acceso a la API** — no dicho en el video.
- **Qué ocurre con el audio al desactivar «generate audio», más allá de que no abarata** — no dicho en el video.
- **La duración mínima y máxima admitidas y el listado completo de resoluciones** — solo se nombran 480, 720, 1080 y 4K, y duraciones de 7, 8 y 15 s — no dicho en el video.
- **Si el prompt en chino es obligatorio u opcional** — el video solo dice que se puede borrar — no dicho en el video.
- **El texto literal del prompt de las cuatro estaciones** — el video lo muestra en pantalla; el texto está en el tablero del curso — no leído en el video.

## Qué aporta al concurso AIxGaudi ("The Gaudí Nexus")

- **Escala de costo para presupuestar el video del concurso:** 320 créditos a 720 px / 7 s, 1.600 en 4K y ≈30 € por un video 4K de 15 s, con la receta «probá en 480 y volvé a 1080» para las piezas finales [00:02:33]–[00:04:26], [00:03:25]–[00:03:38], [00:09:45]–[00:10:14].
- **Disclosure de detalle constructivo con control de cámara:** zoom cinematográfico sobre la barandilla de la loggia y sobre la unión montante-esquina, dirigido con anotaciones de color sobre la imagen y con escalonado en tramos de segundos [00:05:18]–[00:05:35], [00:11:17]–[00:12:13], [00:16:51].
- **Recorrido narrativo del proyecto en un solo video:** varias tomas del edificio alimentan un workflow que arma una secuencia de planos de 7 s [00:17:53]–[00:19:12].
- **Animación de un render estático:** el time-lapse de trípode fijo mantiene el edificio quieto y mueve nubes, sol y personas, dando vida a la imagen sin tocar la arquitectura [00:19:34]–[00:21:29].
- **Ralentización limpia en el montaje:** la interpolación de fotogramas (7 s → 14 s) evita el look entrecortado al ralentizar en After Effects o Premiere Pro [00:21:43]–[00:23:10].
- **Banco de estructuras de cámara reutilizables:** la web de prompts de Seedance 2.0, filtrable por «arquitectura» o «animación», sirve para extraer estructuras de cámara y de montaje antes de producir [00:25:39]–[00:26:08].

## Conceptos relacionados

- [[proyectos/MVP_04-comfyui-arquitectura/00-index|MVP 04 ComfyUI arquitectura]]
- [[wiki/glosario/software/comfyui|ComfyUI]]
- [[wiki/glosario/software/comfy-cloud-vs-runpod|Comfy Cloud vs RunPod]]
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — la vía local de video (LTX i2v) que este módulo no cubre
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]]
- [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|extracción del material del curso AI×Gaudí]]
- [[raw/research/2026-10-20-miro-curso/miro-inventario|miro-inventario]] — tarjetas del módulo 4: skill `seedance-director`, prompts de cámara y de montaje, enlaces a `kling.ai`, `ltx.io` y `seedance2.ai`
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]] — módulo 3: de dónde sale la imagen de partida
- [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]]
- [[wiki/fuentes/comfyui-for_architects-architutors|comfyui-for-architects-architutors]]
- [[specs/261019-plan-concurso-gaudi-nexus-ia|plan del concurso Gaudí Nexus]]
- [[raw/yt/transcripts/2026-10-21_mux-image-to-video.es|transcripción ES del módulo 4]]

## Cómo lo adaptamos

| Lo que hace el curso | Lo que hacemos nosotros | Por qué |
|-----------------------|-------------------------|---------|
| Genera el video con Seedance 2.0 por API, con créditos por corrida (320 a 720 px / 7 s) | La producción de video se resuelve con LTX en el pod de RunPod, la vía abierta ya prevista en `n_04-video` | LTX corre en nuestra GPU y nos da iterations sin sumar créditos por cada render; el flujo completo queda en el pod |
| Usa Seedance 2.0 como modelo de referencia de calidad y de costo (1.600 créditos en 4K, ≈30 € por video de 15 s) | Seedance 2.0 queda como referencia de costo y calidad, con calibración puntual en Comfy Cloud Free (400 créditos por mes) | Los 400 créditos mensuales alcanzan para validar encuadre y continuidad de los clips clave, y el grueso de la producción sigue en el pod |
| Ralentiza en After Effects o Premiere Pro, con los fotogramas estirados y el video entrecortado | La interpolación de fotogramas (7 s → 14 s) se implementa con nodos de interpolación de código abierto en ComfyUI | Doblamos la cantidad de fotogramas con interpolación limpia y el clip entra al montaje sin el look entrecortado |
| Usa el time-lapse de trípode fijo y la secuencia de planos con varias imágenes como plantillas de ComfyUI | El time-lapse y la secuencia de planos se resuelven con plantillas locales, sobre los renders del proyecto | Son el ritmo del video del concurso y ambos parten de imágenes que ya tenemos en el vault |
| Marca la imagen de entrada con un círculo rojo y un círculo azul para dirigir el encuadre | Las anotaciones de color se conservan como guía de encuadre y se traducen a máscara dentro del grafo | La anotación deja de ser una convención del curso y pasa a ser un input real: la máscara define la región que el modelo encuadra |
| Redacta en el prompt coach de Claude y pega el prompt JSON largo, con parte en chino | El prompt se genera con un proyecto de Claude; el prompt largo convive con la versión corta de 50 palabras | La versión corta es la que rinde en la fase divergente (el propio curso lo muestra: un prompt simple dio mejor resultado que el largo [00:21:19]); el largo queda para las piezas finales donde hace falta estructura |
| Deja el video de 7 s tal cual y ralentiza después en el editor | El workflow de interpolación reemplaza la ralentización en el editor | Un solo camino: generar, interpolar y montar, con el archivo intermedio ya en la resolución de salida |

## Checks contra el criterio del jurado

- **Lógica constructiva por encima de la apariencia** (criterio de Cas Esbach, módulo 6): en el time-lapse el edificio permanece completamente estático y lo que se mueve es el entorno — la arquitectura es la fija y el video cuenta el proyecto [00:19:34]–[00:19:46].
- **El encuadre se elige a la altura de los ojos:** el zoom sobre la barandilla de la loggia y sobre la unión montante-esquina muestra el detalle constructivo a escala humana, con el círculo rojo y el círculo azul señalando las encuentro [00:11:17]–[00:12:13].
- **El costo por clip se registra como dato de proyecto:** cada corrida con sus créditos (320 a 720 px / 7 s, 1.600 en 4K) queda anotada en la ficha del clip, con su resolución, su duración y su modelo.
- **Continuidad de plano:** «transición suave», «todo un plano continuo y sin cortes» sostienen la lectura del proyecto entre encuadres [00:14:48]–[00:15:04].
- **Pendiente:** la transcripción del módulo 6 (mesa redonda con Cas Esbach) está pendiente de ingesta; el criterio se toma de esa cita y se revalida cuando el material esté disponible.
