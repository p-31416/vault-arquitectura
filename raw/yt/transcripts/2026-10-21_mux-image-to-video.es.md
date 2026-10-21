---
tipo: transcript
fuente: archademy.ai (curso AI x Gaudi, area de participantes)
modulo: image-to-video
titulo: Image-to-Video
idioma: es
fecha_creacion: 2026-10-21
tags: [yt, transcript, curso-ai-gaudi, mux, image-to-video]
---

# Image-to-Video — es

> Transcripcion automatica de los subtitulos del modulo del curso (Mux).
> Origen: https://vz-4ced3a48-15e.b-cdn.net/b0e1ea14-2be9-47ae-8515-cf3c5cbe00ea/captions/es.vtt
> Duracion de la pista de subtitulos: 00:26:18,946 --> 00:26:22,222

[00:00:04] Bienvenidos a la parte cuatro, image to video.
[00:00:12] Lo que vemos aquí es un pequeño repaso del capítulo anterior,
[00:00:18] que era image to image, donde tomamos una imagen y la transformamos
[00:00:21] en otra imagen. El último paso de una presentación suele ser
[00:00:27] hacer un video con esto. Probablemente no sea nuevo para todos,
[00:00:32] pero quizá te sigas preguntando: ¿cómo se hace exactamente?
[00:00:37] ¿Cómo lo hacemos bien, y qué técnicas hay para hacerlo bien?
[00:00:43] Un ejemplo muy básico es hacer una transición entre la primera imagen
[00:00:49] y la última, y que se fundan.
[00:00:53] Esto ya tiene un poco de sensación de "AI slop",
[00:00:58] así que no es un gran ejemplo,
[00:01:00] pero es lo más fácil para empezar.
[00:01:05] Y esto es lo que llamamos image to video.
[00:01:11] Cuando abrimos la plantilla, vemos lo siguiente.
[00:01:14] Es un dibujo de una mujer, tres conjuntos de ropa y el prompt.
[00:01:20] Si lo reordenamos para poder leerlo,
[00:01:24] es un prompt muy detallado sobre cómo
[00:01:29] el modelo debe ponerle esa ropa.
[00:01:33] Para nosotros no es muy interesante, porque vamos a usar solo una imagen.
[00:01:39] Así que lo que haremos...
[00:01:42] Podemos arrastrarlas. Esta,
[00:01:45] la que está conectada a "image four" y a "image three",
[00:01:50] le damos a Ctrl+B, o clic derecho y clic en "bypass".
[00:01:56] Porque no la vamos a usar en este tutorial.
[00:02:04] En esta simplemente arrastramos y soltamos una imagen.
[00:02:08] Por ahora te voy a mostrar un ejemplo con una imagen que generamos
[00:02:13] en el módulo anterior, que era esta fachada con la barandilla
[00:02:19] que editamos. Y, de hecho,
[00:02:23] vamos a poner en bypass también la tercera.
[00:02:26] Clic en "bypass".
[00:02:33] Esto funciona por API.
[00:02:36] Así que podemos ver la cantidad de créditos que va a costar.
[00:02:41] Es mucho. 320 créditos por ejecución es muchísimo.
[00:02:47] Tiene que ver con la resolución.
[00:02:49] Si quisiéramos baja resolución, son solo 148.
[00:02:53] Si lo subimos a 4K,
[00:02:57] un video en 4K a partir de esta imagen va a costar
[00:03:02] 1.600 créditos.
[00:03:04] Eso es muchísimo. Si calculo rápido,
[00:03:09] depende un poco de tu plan,
[00:03:14] pero son al menos cinco o diez euros solo por
[00:03:19] un video. Así que, por ahora, lo vamos a mantener bastante
[00:03:25] bajo, como ejemplo. Si lo tienes claro y quieres
[00:03:31] hacer un video de verdad para un cliente o para el concurso,
[00:03:34] prueba primero a 480 y siempre puedes volver
[00:03:38] a 1080 después. Este prompt hay que quitarlo, porque no nos sirve.
[00:03:44] La proporción la pondría en "adaptive", porque no sé cuál es exactamente.
[00:03:51] Si tú sabes qué proporción es, puedes hacer clic en la que corresponda.
[00:03:58] Otra cosa que impacta mucho en los créditos es cuánto quieres que dure el video.
[00:04:03] Si pones siete u ocho segundos,
[00:04:06] son unos 170 créditos.
[00:04:10] Si lo subimos a 15, claro,
[00:04:13] será el doble. El video más caro que podrías hacer sería en 4K.
[00:04:19] Eso son unos 3.400 o 3.500 créditos,
[00:04:26] que es muchísimo.
[00:04:28] Así que no hagamos eso y dejémoslo en
[00:04:34] algo así.
[00:04:37] Para probar. Y lo más importante es el prompt.
[00:04:41] ¿Cómo lo escribimos? Vamos a nuestro prompt coach.
[00:04:46] Escribí "start" y ahora voy a
[00:04:53] subir esta imagen y
[00:04:56] decir Seedance
[00:04:59] 2.0, porque al configurar este prompt coach dijimos que, con solo
[00:05:06] decir Seedance 2.0, el modelo ya sabe cómo escribir
[00:05:10] el prompt específicamente para ese modelo, así que no nos tenemos que preocupar
[00:05:15] de cómo redactarlo. Quiero
[00:05:18] hacer un zoom cinematográfico
[00:05:24] sobre la barandilla de la loggia.
[00:05:30] Digamos que es un detalle importante que quiero mostrar en mi presentación,
[00:05:35] por el motivo que sea. Lo escribo aquí.
[00:05:38] Ahora el agente ya sabe cuál es la imagen de partida y sabe
[00:05:44] cómo indicarle a Seedance que haga esa acción.
[00:05:50] Así que venimos aquí y
[00:05:54] pegamos el prompt cuando lo tengamos.
[00:05:59] Bien, el modelo terminó y dio este prompt JSON larguísimo.
[00:06:03] No lo he leído, así que hago clic en copiar.
[00:06:09] Vengo aquí y lo pego.
[00:06:13] Te recomiendo mucho leerlo entero, porque a veces
[00:06:17] dice cosas que no son ciertas.
[00:06:19] Por ahora voy a dejar la parte en chino que hay aquí,
[00:06:24] pero la puedes borrar si quieres.
[00:06:27] Hacemos clic en "run".
[00:06:29] Y el modelo empieza a generar;
[00:06:33] como vemos, se pone azul,
[00:06:34] y el video de salida aparecerá aquí.
[00:06:41] El workflow que vamos a usar:
[00:06:44] si vas a las plantillas y filtras por
[00:06:48] Seedance 2.0, es este último.
[00:06:53] Todas indican lo que hacen.
[00:06:56] Si tienes varias imágenes de referencia y quieres enlazarlas,
[00:07:02] usa esta. Si tienes un primer y un último fotograma,
[00:07:06] como vimos en el PowerPoint,
[00:07:08] usa esta.
[00:07:11] La más simple es esta.
[00:07:14] Hacemos clic aquí y lo que vemos es una imagen base,
[00:07:18] este nodo.
[00:07:22] El prompt lo vamos a borrar.
[00:07:24] Voy a poner la
[00:07:31] imagen de partida. Esta es la que generamos en el módulo tres con
[00:07:37] image to image, donde editamos la barandilla e hicimos esta loggia.
[00:07:44] Ahora, lo que tendríamos que hacer
[00:07:47] es ir a nuestro prompt coach.
[00:07:52] Recuerda el módulo uno: esto lo configuramos juntos,
[00:07:56] y en las instrucciones pusimos...
[00:07:59] Bueno, dimos toda la información, que también incluía las instrucciones
[00:08:04] sobre cómo escribir prompts para Seedance 2.0.
[00:08:11] Bien, yo diría algo así.
[00:08:19] Seedance 2.0: quiero un zoom cinematográfico sobre la barandilla
[00:08:24] de la loggia. Aunque esto no está muy bien redactado,
[00:08:31] porque, claro, solo hay una loggia,
[00:08:33] así que es un poco confuso, pero se entiende la idea.
[00:08:35] Me dio este prompt larguísimo,
[00:08:38] lo copio.
[00:08:41] Después venimos aquí, y yo ya lo hice, porque,
[00:08:47] como ves, ¿está aquí la información?
[00:08:51] No. Esto tardaba unos dos minutos en generarse, para no perder tiempo,
[00:08:57] pero simplemente tomé este prompt
[00:09:02] y lo puse en esta parte de texto.
[00:09:05] Los ajustes que usé fueron Seedance 2.0.
[00:09:09] El prompt está aquí. La resolución la puse en 720 píxeles.
[00:09:14] La proporción, en "adaptive", porque no sé exactamente cuál es.
[00:09:20] Es más seguro usar "adaptive". La duración son los segundos que durará el video.
[00:09:26] Claro, cuanto más largo, más caro.
[00:09:30] Dejo activado
[00:09:32] "generate audio" porque, si lo desactivo,
[00:09:34] no sale más barato. Así que lo dejo encendido.
[00:09:38] La seed es algo que en este workflow no me importa mucho,
[00:09:43] así que la dejo como está.
[00:09:45] Si queremos alta resolución,
[00:09:48] por ejemplo 4K, ves que los créditos se disparan.
[00:09:54] Si lo ponemos en 15 segundos,
[00:09:58] en 4K son casi 30 euros por un video.
[00:10:02] Es mucho; o unos veinte euros, creo, por un video si lo generamos
[00:10:08] así. Por eso lo dejo en siete segundos y 720 píxeles, porque
[00:10:14] por ahora estamos probando y con eso basta.
[00:10:20] Y este es el resultado.
[00:10:30] Como ves, hace lo que se le pidió:
[00:10:35] hace zoom sobre la imagen. Pero, como nuestro prompt no era muy interesante,
[00:10:42] el resultado tampoco lo es.
[00:10:49] La pregunta podría ser: ¿cómo consigo más control sobre lo que
[00:10:55] el video está mostrando?
[00:10:57] Porque en esta imagen de entrada es bastante obvio que la barandilla
[00:11:02] que queremos mostrar está aquí. No es muy difícil hacerle zoom.
[00:11:08] ¿Y si queremos algo más específico que es difícil de explicar con palabras?
[00:11:14] Por ejemplo...
[00:11:17] Otro ejemplo, en el prompt coach que acabo de abrir,
[00:11:23] fue que hice unas anotaciones sobre la imagen y dije:
[00:11:28] este detalle rojo de aquí, cómo la barandilla se conecta a este muro,
[00:11:34] y cómo el panel, o los montantes de la ventana,
[00:11:40] se conectan a esta esquina,
[00:11:45] diría
[00:11:46] yo.
[00:11:46] Le pongo dos colores y después digo Seedance 2.0, para que sepa para qué
[00:11:52] modelo es. Primero haz que el video haga zoom en el detalle de la barandilla
[00:11:57] marcada en rojo, y después que haga zoom en el círculo azul.
[00:12:01] El video dura ocho segundos.
[00:12:03] Esto también es importante, porque así el modelo puede escribir el prompt
[00:12:09] de forma específica y decir algo como: del segundo uno al cuatro,
[00:12:13] haz esto; del cuatro al ocho, haz aquello.
[00:12:16] Así que tomé este prompt. Como ves aquí,
[00:12:21] la nota, el comentario del prompt coach, era: sube
[00:12:25] el render limpio, no el PNG anotado.
[00:12:28] Yo no le hice caso a ese consejo,
[00:12:30] así que
[00:12:34] si venimos aquí, le di la misma imagen.
[00:12:40] Tomé este prompt,
[00:12:45] le di a copiar,
[00:12:48] lo pegué aquí, los ajustes eran los mismos,
[00:12:51] lo puse en ocho segundos, y este es el resultado.
[00:12:59] Hace muy bien el zoom exactamente sobre ese punto y, después,
[00:13:04] hace zoom sobre el montante de la ventana.
[00:13:07] Estoy muy contento con la primera parte, donde va exactamente ahí.
[00:13:14] Esta me la imaginaba más como la esquina,
[00:13:17] pero es mi primer intento. Entonces volvería a Claude,
[00:13:22] a mi prompt coach, y le diría: hazlo más específico.
[00:13:28] ...
[00:13:33] Y asegúrate de que hace zoom
[00:13:40] en la esquina marcada con el círculo azul.
[00:13:45] Por ejemplo, algo que yo esperaba que hiciera,
[00:13:49] sinceramente, en vez de hacer zoom primero
[00:13:59] y después cortar de golpe a la siguiente escena,
[00:14:01] pensaba que haría una transición extra,
[00:14:03] pero no lo especifiqué. Así que diría: asegúrate
[00:14:08] de que haga una transición suave
[00:14:18] entre el primer plano, el zoom sobre el
[00:14:31] detalle rojo,
[00:14:37] y el segundo plano,
[00:14:43] el detalle de la esquina azul.
[00:14:48] Asegúrate de que sea
[00:14:50] todo un plano continuo
[00:14:56] y sin
[00:15:04] cortes.
[00:15:08] Algo así. Puede que, otra vez, no sea la mejor forma de decirlo,
[00:15:14] pero mi prompt coach me puede dar
[00:15:18] un nuevo prompt y lo vuelvo a intentar.
[00:15:23] Otra cosa que podrías hacer es descargar este video y meterlo aquí.
[00:15:29] No lo voy a hacer, pero es una opción si quieres.
[00:15:37] No voy a ejecutar este video, pero se entiende la idea.
[00:15:41] Voy a dejar todos los videos
[00:15:48] que generamos aquí; los descargo.
[00:15:55] Y así tú también tienes acceso.
[00:15:57] Con estos videos pasa lo mismo.
[00:16:00] Si los descargas y los arrastras a Comfy, también puedes
[00:16:05] ver el prompt. Así que tranquilo.
[00:16:09] El ejemplo que vimos aquí era, primero, describir dónde quieres hacer zoom.
[00:16:14] El segundo era anotar directamente: quiero que haga zoom exactamente en esta parte.
[00:16:21] Y después este.
[00:16:24] También podemos añadir una flecha aquí y decir:
[00:16:27] después del primer zoom, sigue la flecha verde hasta este detalle, y
[00:16:31] probablemente lo hará. También podríamos, para hacerlo más simple,
[00:16:36] hacer un plano de unos cuatro segundos con zoom sobre el detalle rojo,
[00:16:41] y después otro con zoom sobre el azul,
[00:16:44] el círculo azul, y montarlos juntos.
[00:16:47] Hay infinitas formas de hacerlo.
[00:16:49] ...
[00:16:51] Pero la idea para tener control es hacer anotaciones sobre la imagen de entrada.
[00:17:03] Bien, espero que esto haya quedado un poco más claro.
[00:17:07] Partimos de una sola imagen y llegamos a un video.
[00:17:11] La siguiente plantilla que vamos a usar ya está preparada,
[00:17:18] así que descargamos el video.
[00:17:24] Y lo arrastramos a Comfy.
[00:17:27] Y ves el workflow.
[00:17:31] No hagas caso de estos errores:
[00:17:34] es porque las imágenes de entrada que le di ya
[00:17:39] no están ahí, porque a veces no las recuerda
[00:17:45] en los metadatos,
[00:17:49] pero da igual, porque es solo un ejemplo.
[00:17:53] Este workflow toma más de una imagen y la convierte en una secuencia de planos.
[00:17:59] En esencia, este es el resultado.
[00:18:04] Esto es un solo video de siete segundos.
[00:18:08] Toma varios planos y hace algo así
[00:18:15] como esto. Lo hice yendo a las plantillas; es esta plantilla.
[00:18:22] Ves que esta es casi igual que esta otra.
[00:18:28] El prompt, otra vez. Fui a mi prompt coach.
[00:18:33] Subí varias tomas del edificio.
[00:18:44] Las añadí aquí abajo para que las veas.
[00:18:47] Puedes probarlo tú mismo:
[00:18:49] descarga estas y ponlas en estos espacios.
[00:18:55] Puedes arrastrarlas ahí o hacer clic en este botón para añadirlas.
[00:19:01] Toma las mismas imágenes que le diste al prompt coach,
[00:19:06] dile lo que quieras, escribirá el prompt y lo pegas en Comfy.
[00:19:12] Y obtendrás el resultado que se ve aquí.
[00:19:17] Eso por un lado. Hay otro workflow que
[00:19:23] vamos a probar nosotros, que otra vez es con una sola
[00:19:30] imagen de entrada.
[00:19:34] Y es este prompt: trípode
[00:19:39] fijo, time lapse, el edificio permanece completamente estático, las nubes
[00:19:46] se desplazan lentamente por el cielo, etc. Así que lo voy
[00:19:50] a preparar. Bien, avanzamos: cambié un poco el prompt
[00:19:57] y lo que quiero mostrarte aquí es que primero probé
[00:20:03] a meterlo en el prompt coach: trípode fijo, time lapse.
[00:20:09] Y el resultado no estuvo nada mal.
[00:20:12] Voy a quitar la música.
[00:20:18] No estuvo mal, porque es un time lapse y ves que las cosas se mueven.
[00:20:22] Esto se
[00:20:28] hizo con un prompt muy largo,
[00:20:32] creo.
[00:20:38] Este no. Si te lo muestro aquí,
[00:20:42] "open as workflow in a new tab", puedo volver al prompt.
[00:20:47] Ves que, otra vez, era un prompt larguísimo.
[00:20:49] Esa era la salida del prompt coach.
[00:20:52] No era nada del otro mundo, así que probé otra cosa.
[00:20:57] Quizá debería usar esto como prompt,
[00:21:00] sin complicarlo tanto, y ver cuál es el resultado.
[00:21:05] ...
[00:21:15] Y esto se parecía mucho más a lo que yo esperaba.
[00:21:19] Así que a veces el prompt coach no es siempre la mejor forma de mejorar
[00:21:25] un prompt. Prueba de otra manera.
[00:21:29] Y este, en mi opinión, es un buen resultado.
[00:21:33] Aquí vimos tres workflows.
[00:21:35] En el lado derecho de Miro, otra vez,
[00:21:38] puse un montón de recursos distintos.
[00:21:43] Por ejemplo, aquí: video to video.
[00:21:46] Lo que hace es tomar un video;
[00:21:50] el workflow convierte un video de siete segundos en uno de 14,
[00:21:56] lo que puede ser interesante al editar videos.
[00:21:59] Puede que para mucha gente no sea aplicable,
[00:22:04] pero muchas veces, cuando editas algo y quieres ralentizar un video,
[00:22:08] y lo haces
[00:22:10] en Adobe After Effects o Adobe Premiere Pro o similar,
[00:22:13] empieza a verse muy entrecortado, porque los fotogramas se estiran.
[00:22:19] Se nota que está ralentizado.
[00:22:22] Con este workflow, si descargas este video y lo importas en Comfy...
[00:22:28] Hagámoslo.
[00:22:31] Descargamos este y entramos en Comfy.
[00:22:41] Lo arrastramos aquí. Ves que este es mi workflow
[00:22:45] de interpolación de fotogramas, y los resultados.
[00:22:53] Es el mismo video;
[00:22:56] bueno, esta es otra prueba que hice.
[00:22:59] Pero dura el doble, porque por cada fotograma del video
[00:23:04] el modelo genera otro fotograma.
[00:23:08] Simplemente duplica la cantidad de fotogramas,
[00:23:10] lo cual está muy bien para editar. Échale un vistazo si te parece interesante.
[00:23:16] Y aquí hay más videos, como este,
[00:23:21] por ejemplo.
[00:23:27] También con Seedance. Este es otro modelo, llamado LTX.
[00:23:31] No te voy a mostrar el workflow entero,
[00:23:38] pero puedes mirarlo. Estos ejemplos también son interesantes.
[00:23:45] Descárgalos y mira si puedes hacer algo con ellos.
[00:23:49] Puedo borrar este.
[00:23:52] Aquí había otro proyecto que hicimos.
[00:24:01] Un poco raro, pero puede ser interesante.
[00:24:04] Y una cosa extra: si trabajas con Claude y tienes
[00:24:10] algo más de experiencia, conocerás las skills.
[00:24:13] Si no sabes qué es una skill,
[00:24:15] tranquilo, lo puedes buscar en internet.
[00:24:17] Pero hay una skill específica hecha para Seedance.
[00:24:24] Si quieres, puedes hacer clic aquí, en "more".
[00:24:36] Exportar como markdown y después importarlo en Claude como skill,
[00:24:41] y así hará prompts
[00:24:43] específicamente para Seedance 2.0.
[00:24:49] Pero no es necesario; es un poco como las instrucciones del proyecto,
[00:24:52] como el prompt coach que hicimos,
[00:24:55] pero de otra manera. Échale un vistazo.
[00:24:59] Después tienes Google Omni, que es el modelo de video más avanzado de
[00:25:05] Google, donde probé este prompt para conseguir las cuatro estaciones.
[00:25:12] Sí.
[00:25:15] Y, como ves, es bastante capaz.
[00:25:18] Por si te interesa.
[00:25:21] También puedes entrar en estos enlaces y mirar estos ejemplos.
[00:25:26] Pero muchas veces es lo mismo:
[00:25:29] simplemente hacer un video a partir de una imagen.
[00:25:39] Una última cosa que quiero añadir: en "resources" encontrarás los enlaces
[00:25:44] de los modelos. Y esta web es bastante interesante, si la abres.
[00:25:48] Hay un montón de prompts para Seedance 2.0.
[00:25:52] Puedes ver los prompts en tendencia,
[00:25:54] y aquí puedes
[00:25:58] ordenar o filtrar, quizá por algo como arquitectura
[00:26:02] o animación.
[00:26:06] No sé cuál sea tu objetivo,
[00:26:08] pero es una web muy buena para inspirarte y ver un montón de cosas
[00:26:15] que son posibles.
[00:26:18] Dicho esto, cierro aquí el módulo cuatro.
