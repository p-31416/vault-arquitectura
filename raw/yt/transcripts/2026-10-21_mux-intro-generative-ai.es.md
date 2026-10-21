---
tipo: transcript
fuente: archademy.ai (curso AI x Gaudi, area de participantes)
modulo: intro-generative-ai
titulo: Introduction to Generative AI
idioma: es
fecha_creacion: 2026-10-21
tags: [yt, transcript, curso-ai-gaudi, mux, intro-generative-ai]
---

# Introduction to Generative AI — es

> Transcripcion automatica de los subtitulos del modulo del curso (Mux).
> Origen: https://vz-4ced3a48-15e.b-cdn.net/35e568e8-6e1d-4fa6-9f27-17ab889df703/captions/es.vtt
> Duracion de la pista de subtitulos: 01:30:46,679 --> 01:30:49,341

[00:00:01] Hola a todos y bienvenidos a este curso de IA generativa en la arquitectura.
[00:00:07] Me llamo Thomas Nelissen y voy a ser el instructor
[00:00:12] de este curso. Y este primer video que estás viendo,
[00:00:17] este primer módulo, es una introducción general.
[00:00:21] Vamos a hablar de qué programas vamos a usar,
[00:00:25] un poco de historia, un poco de teoría,
[00:00:27] y esta es una base realmente importante
[00:00:30] para entender los módulos siguientes.
[00:00:33] Entonces, ¿qué es la IA? Y en los siguientes vamos a ver text to image,
[00:00:38] image to video, image to image,
[00:00:40] image to 3D y muchas cosas más.
[00:00:45] Pero el primero, este, es importante para poder
[00:00:50] entender todo lo que haremos después.
[00:00:54] Así que empecemos.
[00:00:59] Antes de presentarme, quiero mencionar el programa principal que vamos a usar,
[00:01:04] que es Comfy. ComfyUI.
[00:01:08] Actualmente es una scale-up.
[00:01:12] Creo que empezaron en 2020 o 2021,
[00:01:18] y es increíble lo que han construido.
[00:01:21] Es la mayor plataforma open source de IA generativa.
[00:01:25] De hecho, se puede usar gratis. Voy a explicar
[00:01:28] todo a fondo: cómo funciona,
[00:01:30] por qué lo usamos, la diferencia entre la versión gratuita y las que
[00:01:35] vamos a usar, o sea, la suscripción de pago,
[00:01:38] etc. Recuerda: el software principal que vamos a usar es Comfy.
[00:01:44] Ahora, solo para que te vayas haciendo una idea,
[00:01:48] así se ve un workflow en ComfyUI.
[00:01:53] Este es más bien de nivel principiante.
[00:01:55] Vamos a
[00:01:56] profundizar mucho en este. Lo vamos a estudiar muy de cerca.
[00:02:01] Pero terminaremos con workflows que se ven así.
[00:02:05] Como ves, ya es más complicado, más caótico,
[00:02:10] y pasan muchísimas más cosas.
[00:02:11] Pero te voy a llevar paso a paso por todo el proceso para que entiendas qué
[00:02:15] tienes que hacer. Y preparé un tablero completo en Miro.
[00:02:19] Te lo muestro. Este es el tablero completo de Miro.
[00:02:26] Ahí tienes todos los recursos para poder usar todos los workflows que
[00:02:31] te doy gratis. Y, como dije, en este primer módulo,
[00:02:37] en esta introducción, vamos a ver bastante teoría,
[00:02:40] pero en realidad no necesitas la teoría.
[00:02:44] Puedes usarlo también sin la teoría,
[00:02:47] pero ayuda a entender mejor lo que está pasando.
[00:02:52] Un poco sobre este tablero de Miro.
[00:02:55] La idea es que empezamos arriba, con los recursos.
[00:02:59] Cada vez que mencione algo,
[00:03:02] un enlace o lo que sea, lo vas a encontrar aquí, en "resources".
[00:03:06] Después, esto está organizado por módulo.
[00:03:09] Ahora estamos en el módulo uno, la introducción.
[00:03:12] Aquí está todo lo que vamos a ver y lo que vas a necesitar en cuanto
[00:03:16] a enlaces, recursos o cosas así.
[00:03:20] Luego, en el siguiente módulo, text to image,
[00:03:23] veremos este.
[00:03:25] O estas imágenes, módulo 3,
[00:03:28] image to image; verás que es el que va a llevar más tiempo.
[00:03:34] Image to video e image to 3D.
[00:03:37] Todo lo que necesitas está aquí.
[00:03:40] Vas a tener acceso a este tablero de Miro,
[00:03:42] así que vas a poder acceder a todo.
[00:03:45] También es importante que incluí mucho material extra.
[00:03:51] Son las cosas de aquí, del lado derecho.
[00:03:55] No están necesariamente incluidas en la clase,
[00:03:58] pero sé que al menos la mitad de quienes están viendo esto
[00:04:04] tiene interés en explorar y experimentar bastante con ello.
[00:04:09] Así que dejé mucho material que puedes revisar.
[00:04:15] Por ejemplo, estas imágenes, donde estaba probando uno
[00:04:22] de mis modelos de IA, donde
[00:04:25] pasé de esta volumetría a una imagen hiperrealista.
[00:04:30] Todo está aquí. Échale un vistazo si te
[00:04:34] interesa.
[00:04:37] Volvamos a la presentación.
[00:04:45] Todas las imágenes que viste se crearon con ComfyUI.
[00:04:51] ¿Y quién soy yo? Probablemente nunca oíste hablar de mí.
[00:04:54] Me llamo Thomas Nelissen. Soy arquitecto.
[00:04:58] Me describiría como especialista en IA generativa y también arquitecto junior.
[00:05:04] Estudié y me gradué en la Universidad de Amberes, en Bélgica,
[00:05:10] porque soy de Bélgica.
[00:05:15] Entré en contacto con la IA durante mi tesis.
[00:05:20] No sabía nada de IA.
[00:05:23] No tenía formación técnica,
[00:05:25] tenía formación en arquitectura,
[00:05:26] pero tuve la oportunidad de hacer mi tesis sobre IA generativa,
[00:05:32] y enseguida decidí simplemente probarlo.
[00:05:38] Este fue el resultado final, la portada de nuestra tesis.
[00:05:42] La hice junto con Sebastian van Dri.
[00:05:45] Y esto es lo que me lanzó en el campo
[00:05:51] de la IA generativa. Si quieres contactarme,
[00:05:54] aquí están mis datos. Mi Instagram y mi sitio web
[00:05:58] se llaman thomasnelissen.ai y mi correo es info@thomasnelissen.ai.
[00:06:08] Esta es la URL. Profesionalmente, a tiempo completo, soy
[00:06:14] arquitecto junior en Davis. Davis es una de,
[00:06:17] si no la más interesante, las startups AI native de Europa.
[00:06:24] Actualmente estamos en París.
[00:06:28] Lo que ves aquí es el equipo fundador.
[00:06:29] Yo entré en Davis un poco después. Y lo que hace Davis es marcar un nuevo
[00:06:36] estándar de tiempos para el desarrollo inmobiliario y la arquitectura.
[00:06:39] Mientras que la mayoría de los estudios,
[00:06:42] los estudios de arquitectura, parten del viejo paradigma,
[00:06:46] Davis parte de la IA y, dentro del paradigma de la IA,
[00:06:52] la aplicamos al entorno construido, y con eso logramos
[00:06:58] un estándar de tiempos de otro nivel, realmente insuperable.
[00:07:06] Además, mientras hacemos proyectos,
[00:07:10] también desarrollamos nuestro propio modelo.
[00:07:12] Se llama Gaudi One, un modelo de difusión discreta de última generación.
[00:07:17] Es superinteresante formar parte de este equipo increíble.
[00:07:21] Así que ese es un poco mi recorrido.
[00:07:25] Si te interesa, entra al sitio web,
[00:07:31] que se llama Meet Davis.
[00:07:34] Y puedes ver lo que hacemos,
[00:07:36] cómo funciona, la tecnología.
[00:07:40] Gaudi One, algo sobre el equipo,
[00:07:45] etc. La verdad, es un honor formar parte de este equipo,
[00:07:49] y estoy muy contento por ello.
[00:07:54] Sobre este curso: por qué este curso es importante.
[00:07:58] La siguiente parte puede sonar un poco cursi.
[00:08:02] Pero es realmente lo que pienso.
[00:08:03] La IA va a cambiar todas las industrias.
[00:08:07] De hecho, ya las está cambiando y ya las cambió mucho.
[00:08:11] Quienes la ignoren se van a convertir en dinosaurios.
[00:08:16] Esto significa que hay que adaptarse o morir.
[00:08:19] Creo mucho en elegir una especialización,
[00:08:24] un nicho, algo en lo que llegues a ser muy bueno.
[00:08:27] Para mí, elegir la IA
[00:08:29] generativa en arquitectura como tema de tesis fue el primer paso.
[00:08:33] Entrar en Davis fue el siguiente paso,
[00:08:36] y creo de verdad que todos deberían hacerlo y volverse AI native por naturaleza.
[00:08:43] La IA está transformando la arquitectura,
[00:08:46] y el open source es un motor del desarrollo de la IA.
[00:08:51] ¿Qué es el open source? Para quien no lo tenga claro,
[00:08:55] open source es que hay gente construyendo cosas
[00:08:59] y poniéndolas a disposición de la comunidad, es decir, dejando que se usen gratis.
[00:09:08] Lo voy a explicar mejor sobre la marcha.
[00:09:11] Pero, como el open source es un motor del desarrollo de la IA,
[00:09:15] creo que ComfyUI llegó para quedarse.
[00:09:18] ComfyUI es el programa que vamos a usar.
[00:09:21] Es la mayor plataforma open source.
[00:09:23] Lo que hacen es tomar todos los modelos que otras empresas
[00:09:28] u otras personas desarrollan y reunirlos en una sola plataforma para que los uses.
[00:09:37] Antes de meternos de lleno a generar
[00:09:42] imágenes y demás —ya te mostré el tablero de Miro—,
[00:09:47] vamos a ver algunas definiciones.
[00:09:50] Como este primer módulo va a ser un poco más teórico,
[00:09:53] necesitamos algunas definiciones para entendernos bien.
[00:09:58] Si no, voy a hablar mucho de cosas que no entiendes
[00:10:02] y no llegamos a ningún lado. Estas son algunas de las cosas que vamos
[00:10:07] a repasar rápidamente. Voy a ir bastante despacio.
[00:10:11] Más adelante iré acelerando.
[00:10:14] Pero no te preocupes si no entiendes algo o si no todo queda claro.
[00:10:20] Porque voy a repetir esto en cada módulo,
[00:10:23] y con el tiempo todo se va aclarando.
[00:10:26] Los tokens. ¿Cómo funcionan los tokens?
[00:10:31] Los modelos de IA, solo para asegurarnos
[00:10:36] de que vamos bien: los modelos de IA no leen texto,
[00:10:39] leen números. Un tokenizer es un traductor que convierte tu prompt
[00:10:46] en una secuencia de números que el modelo sí puede procesar.
[00:10:51] Los modelos leen números. Regla general:
[00:10:56] no hace falta que memorices esto,
[00:10:57] pero es interesante. Un token equivale a 0,75
[00:11:04] palabras en inglés, o unos cuatro caracteres.
[00:11:06] Un ejemplo: digamos que tienes el prompt "a brutalist concrete pavilion
[00:11:12] at sunset". Eso es lo que escribimos los humanos,
[00:11:15] pero no es lo que el modelo lee en realidad.
[00:11:18] El modelo leería algo así:
[00:11:20] CLIP, que es solo el nombre de un tokenizer,
[00:11:24] traduce esta frase
[00:11:29] en "a", "brutal"... perdón, "a", "brutal",
[00:11:34] "ist", "concrete", "pavilion", "at", "sunset".
[00:11:38] Y por cada token —"brutal" es
[00:11:43] un token, "ist" es un token— da
[00:11:48] un número. Así que esta secuencia de números es simplemente
[00:11:54] cómo la computadora lee
[00:11:59] esta frase. Tenlo en cuenta cada vez que veas la palabra tokens.
[00:12:04] Los tokens son una traducción de palabras a números.
[00:12:10] Siguiente definición: el noise, el ruido.
[00:12:14] El noise es importantísimo, porque vamos a hablar mucho de él.
[00:12:19] El noise es un montón de píxeles distribuidos al azar dentro de un cuadro,
[00:12:25] como puedes ver en esta imagen.
[00:12:28] Este es un ejemplo de noise.
[00:12:30] La seed del noise es la configuración exacta
[00:12:36] de ese noise, siempre un número.
[00:12:40] Un ejemplo de esto es este.
[00:12:43] Vimos que lo que ves al fondo es el noise.
[00:12:48] Esta es la seed de ese noise.
[00:12:51] Son solo 14 números. Parecen aleatorios,
[00:12:55] pero no lo son.
[00:12:57] Puedes verlo como un número de documento de identidad.
[00:13:02] Creé este personaje ficticio solo para este curso,
[00:13:07] no es una persona real. La seed del noise es como ese número de identidad.
[00:13:14] Miras este número y, si solo miras el número,
[00:13:17] dirías que es un número aleatorio.
[00:13:19] Pero no lo es, porque si esta persona fuera a la policía o fuera
[00:13:24] a cualquier otro lugar,
[00:13:27] por ejemplo al banco,
[00:13:29] los dos la identifican por ese número de documento.
[00:13:34] Así que no es aleatorio, porque si cambias un número,
[00:13:39] ya no es la persona correcta.
[00:13:41] Digamos que es el documento de identidad del noise.
[00:13:47] Eso significa que si yo o cualquiera,
[00:13:50] cualquier otra persona, mira estas dos imágenes,
[00:13:53] no ve la diferencia,
[00:13:55] ¿verdad? Pero son completamente distintas.
[00:13:58] La estructura es completamente distinta.
[00:14:01] Este noise tiene la seed de este número.
[00:14:07] O sea, este número es la seed de este noise.
[00:14:10] Espero que quede claro. Y aunque no veas ninguna diferencia entre estas
[00:14:15] dos, esta
[00:14:17] tiene una seed completamente distinta.
[00:14:20] Esta está ligada exactamente a esta, y esta, exactamente a aquella.
[00:14:27] Recuerda esto. Lo voy a repetir después.
[00:14:31] La siguiente: dataset. Un dataset, en este contexto, es simplemente
[00:14:37] una carpeta gigante de imágenes, cada una con un caption de texto que describe lo que
[00:14:43] contiene. Es un conjunto de datos.
[00:14:47] Esta es una representación visual de lo que es.
[00:14:50] Si hacemos zoom en una, vemos que siempre hay dos componentes.
[00:14:56] Tenemos una imagen, que es lo más importante,
[00:14:59] y tenemos el caption. Es simplemente
[00:15:04] un archivo de texto que contiene un texto
[00:15:08] que describe el contenido de la imagen.
[00:15:14] Aquí ves: un edificio brutalista
[00:15:17] asomado al borde de un paisaje erosionado.
[00:15:19] Eso es lo que ves aquí. Normalmente tiene más o menos esta longitud.
[00:15:26] A veces es más largo, a veces más corto.
[00:15:29] Pero, en general, el caption se ve así.
[00:15:33] ¿Y por qué te muestro esto?
[00:15:36] Porque, en realidad, no necesitas saberlo para pasar a la siguiente fase.
[00:15:41] Pero es importante entender
[00:15:45] que quien cura el dataset decide lo que el modelo puede imaginar.
[00:15:50] Los sesgos, los vacíos, la estética:
[00:15:53] todo queda incorporado antes de que escribas un solo prompt.
[00:15:57] Así que ningún medio es neutral.
[00:16:04] Siempre tiene una dirección y, en este caso, la marca la empresa o las personas
[00:16:09] que hicieron el dataset.
[00:16:14] Puede sonar negativo, pero no lo es.
[00:16:17] Lo explico más adelante. Insisto tanto en esto porque la tabla
[00:16:23] que vemos aquí es una evolución. Esto es el nombre de un modelo.
[00:16:28] Todos estos son modelos de difusión de IA que fueron saliendo.
[00:16:33] Este salió en 2022; este, en 2023,
[00:16:37] 2024, 2025. Así que, más o menos cada año,
[00:16:42] sale un nuevo modelo de difusión open source muy grande.
[00:16:47] De hecho, ahora que estamos en 2026 va todavía más rápido:
[00:16:52] ahora es cada mes o cada pocas semanas.
[00:16:56] Lo que quiero mostrarte es esto.
[00:16:59] En 2022 salió el primer modelo realmente relevante.
[00:17:04] Fue Stable Diffusion 1.5. Este modelo se entrenó,
[00:17:10] como vimos antes, con datasets:
[00:17:13] imágenes más captions. Y se entrenó
[00:17:17] con 860 millones. Puede parecer mucho,
[00:17:23] pero hoy FLUX.2 es el modelo de referencia,
[00:17:27] el mejor, y está entrenado con 32.000 millones.
[00:17:30] En tres años pasamos de 860 millones a 32.000 millones,
[00:17:36] lo que significa que este modelo, FLUX,
[00:17:41] FLUX.2, fue entrenado
[00:17:45] con 32.000 millones de imágenes.
[00:17:49] Así te lo puedes imaginar.
[00:17:51] Eso significa que vio muchísimas más cosas que Stable Diffusion 1.5.
[00:17:57] Yo diría que es más inteligente.
[00:18:01] Si a un niño le enseñas solo 8 cosas,
[00:18:04] está claro que otro niño al que le enseñaron 32 es más listo, porque
[00:18:10] ha visto
[00:18:11] muchísimo más. Ahora bien,
[00:18:14] esta es una representación muy simple,
[00:18:16] es algo más complejo, pero esto es lo que quiero que recuerdes de esta diapositiva.
[00:18:21] Siguiente definición:
[00:18:25] el entrenamiento del modelo de difusión.
[00:18:28] El entrenamiento del modelo de difusión es el proceso durante el cual
[00:18:34] el modelo de IA se expone a un dataset enorme.
[00:18:38] Recuerda: imágenes más captions.
[00:18:41] Y así aprende la correlación entre palabras y píxeles.
[00:18:45] Para que quede claro: nosotros no vamos a entrenar un modelo de difusión.
[00:18:50] Es algo que pasa, como dije, una vez al año o cada pocos meses.
[00:18:55] No es algo que podamos hacer nosotros.
[00:18:58] Requiere una enorme cantidad de cómputo,
[00:19:02] muchísimo tiempo, muchos recursos,
[00:19:06] mucho dinero.
[00:19:08] Pero así es como empresas como Stability AI, o incluso Google
[00:19:13] y ChatGPT, entrenan sus modelos.
[00:19:16] Esto no tiene nada que ver con lo que vamos a hacer nosotros,
[00:19:20] pero sí con los modelos que vamos a usar.
[00:19:24] Tenlo presente. Esto ya lo vimos:
[00:19:29] un dataset, o una imagen más su caption.
[00:19:33] Y te voy a dar una explicación
[00:19:37] muy detallada usando una de las imágenes que creé.
[00:19:40] Digamos que quisiera hacer mi propio modelo de difusión.
[00:19:44] No va a pasar, pero supongamos que sí.
[00:19:50] ¿Cómo sería el proceso para incluir esta imagen en el entrenamiento
[00:19:56] de un modelo de difusión? El paso principal sería añadir noise.
[00:20:00] ¿Qué significa eso? Digamos que tomamos esta imagen y un caption,
[00:20:05] ¿sí? Los dos elementos esenciales.
[00:20:08] Decimos: un edificio de apartamentos escultórico,
[00:20:11] azulejos azul profundo brillantes, pueblo español en verano.
[00:20:20] ¿Cómo se entrena el modelo?
[00:20:22] Toma esta imagen y le añade noise.
[00:20:27] Recuerda: el noise eran píxeles distribuidos al azar,
[00:20:30] pero lo hace en X cantidad de pasos.
[00:20:34] Primero añade un poco de noise.
[00:20:36] Todavía se ve más o menos la misma imagen.
[00:20:38] Después añade más noise, más,
[00:20:41] más, hasta que no queda estructura alguna.
[00:20:45] Así que ves:
[00:20:47] en uno, dos, tres, cuatro, cinco,
[00:20:50] seis, siete, ocho, nueve pasos,
[00:20:53] pasamos de una imagen que contiene nuestro edificio
[00:20:59] a algo completamente aleatorio.
[00:21:01] Aquí, en este paso, todavía se ven un poco las líneas de la estructura,
[00:21:08] pero aquí ya no queda nada. Descompone
[00:21:12] nuestra imagen en puro caos.
[00:21:17] Llamemos a esta parte orden completo,
[00:21:21] y a esta, caos completo. A esto lo llamamos
[00:21:25] el proceso de difusión directa.
[00:21:28] De nuevo, no hace falta que lo memorices,
[00:21:30] pero, si te interesa, así se llama.
[00:21:33] Un repaso. Durante el entrenamiento del modelo de IA,
[00:21:38] que no es algo que vayamos a hacer,
[00:21:40] pasamos de una imagen —en realidad,
[00:21:44] de miles de millones de imágenes—
[00:21:47] a noise. Cada imagen se reduce
[00:21:52] a noise puro en X cantidad de pasos, como vemos aquí, hasta que
[00:21:59] tenemos noise completamente puro. Esto es noise puro.
[00:22:07] Lo hicimos con una imagen, pero pasa con miles de millones de imágenes.
[00:22:12] Esta imagen de un bloque de mármol rojo pasa por el mismo proceso.
[00:22:18] Cada vez se añade un poco más de noise hasta que no queda nada.
[00:22:23] Y eso es durante el entrenamiento.
[00:22:26] Lo que a nosotros nos va a importar,
[00:22:29] lo que vamos a hacer, es durante la generación,
[00:22:32] cuando generamos una imagen.
[00:22:34] Durante la parte de generación,
[00:22:36] esto es lo que vamos a estar haciendo.
[00:22:40] Le damos la vuelta al proceso.
[00:22:44] Durante el entrenamiento, vamos de imagen a noise puro.
[00:22:47] Durante la generación, o sea, lo que escribimos en el prompt y generamos,
[00:22:53] es al revés. Partimos de noise puro y llegamos a una imagen final.
[00:22:59] Ya no tenemos un caption.
[00:23:02] Ya no
[00:23:03] hablamos de captions, sino de prompts.
[00:23:06] Digamos que escribimos: estructura de fachada de mármol rojo con vetas blancas visibles.
[00:23:13] Montantes de ventana negros, reflejo en el vidrio.
[00:23:16] El modelo va a partir de noise puro.
[00:23:20] Es solo una imagen llena de píxeles de color,
[00:23:25] como una imagen real, pero sin estructura.
[00:23:29] Son píxeles distribuidos al azar.
[00:23:31] Y luego,
[00:23:33] en X cantidad de pasos, va a crear una imagen muy detallada.
[00:23:38] Primero hace un paso,
[00:23:42] dos pasos...
[00:23:45] Uno, dos, tres, cuatro,
[00:23:48] cinco, seis, siete, ocho, nueve.
[00:23:50] Y en el último paso, el resultado es una imagen detallada.
[00:23:56] Espero que se vea aquí, detrás de mi cabeza.
[00:24:02] Los steps. ¿Qué son? Los steps son simplemente la cantidad de veces
[00:24:08] que se corrige a sí mismo hasta llegar a la imagen final.
[00:24:11] Solo eso: la cantidad de iteraciones que hace el modelo para
[00:24:16] pasar de noise puro a la imagen final.
[00:24:18] Para que te hagas una idea, este es otro workflow, con otros pesos.
[00:24:23] Esto también es noise. Primer paso,
[00:24:27] segundo, tercero, etc.
[00:24:31] Cada vez encuentra un poco más de estructura en el caos, hasta que tenemos una imagen.
[00:24:40] Y mientras genera, mientras da esos pasos,
[00:24:45] recuerda todo lo que vio durante el entrenamiento.
[00:24:48] Digamos que escribes, no sé, un castillo en una colina con algo de
[00:24:55] vegetación y cielo azul. Todas esas palabras se traducen a tokens,
[00:25:01] como vimos antes. Esos tokens son números,
[00:25:05] y esos números están vinculados a imágenes
[00:25:09] que el modelo vio durante el entrenamiento.
[00:25:11] Así que, en este proceso de generación,
[00:25:16] mientras genera, el modelo piensa:
[00:25:19] bueno, ¿qué vi durante mi entrenamiento que me recuerde a un castillo?
[00:25:24] ¿Qué significa que algo esté sobre una colina?
[00:25:27] ¿Qué significa vegetación verde?
[00:25:30] Cuanto más ve durante el entrenamiento,
[00:25:33] mejor, o más referencias tiene, a la hora de generar algo.
[00:25:43] Lo que ves aquí es otra representación
[00:25:48] del proceso de difusión directa, el de ir añadiendo noise.
[00:25:52] Recuerda: esto es durante el entrenamiento.
[00:25:55] No es cuando estamos generando algo.
[00:25:59] Ves que partimos de la imagen de un perro sonriendo,
[00:26:03] y cada vez se añade un poco más de noise hasta que
[00:26:09] tenemos noise puro.
[00:26:12] Al final, el modelo sabe:
[00:26:16] esta estructura de píxeles
[00:26:20] es lo que significa un perro sonriendo.
[00:26:23] Simplemente aprende la relación entre cómo se estructuran los píxeles
[00:26:29] y una palabra.
[00:26:34] Un modelo entrenado con millones de imágenes de gatos,
[00:26:38] etiquetadas como gato, aprende el concepto visual de gato,
[00:26:43] pero nunca va a aprender qué es un edificio de Zaha Hadid salvo que esa etiqueta
[00:26:49] estuviera en el dataset, o sea, salvo que estuviera en el caption.
[00:26:55] Claro, esto no es nada del otro mundo,
[00:26:56] es como enseñarle algo a un niño.
[00:26:59] Si a un niño solo le enseñas chino y luego
[00:27:04] le haces una pregunta en francés,
[00:27:08] claro que no va a entender, porque no le enseñaste francés.
[00:27:13] Entrenar el modelo es como aprender un idioma.
[00:27:21] Un modelo de difusión genera imágenes a partir de noise puro.
[00:27:25] Esto es un repaso. Encuentra estructura en el caos, encuentra patrones en el caos.
[00:27:31] Puede hacerlo porque pasó meses mirando miles de millones de imágenes junto con
[00:27:38] descripciones de texto, aprendiendo qué aspecto suelen tener las palabras.
[00:27:42] Pasamos a la siguiente definición,
[00:27:46] que es el latent space. Esta es un poco más técnica.
[00:27:50] Si no queda del todo claro, no te preocupes.
[00:27:53] Lo vamos a repasar muchas veces.
[00:27:57] El latent space es un mundo comprimido, resumido, donde la IA hace
[00:28:02] todo su razonamiento y que, al final, se traduce de vuelta a píxeles reales
[00:28:08] en el último paso. Seguramente no queda claro,
[00:28:12] pero no te preocupes. Recuerda: eso era el latent space.
[00:28:16] Ahora, la empty latent image.
[00:28:21] La empty latent image se explica sola:
[00:28:24] es un lienzo en blanco. Un lienzo en blanco dentro
[00:28:29] del latent space, con el tamaño de una imagen pero todavía sin contenido.
[00:28:36] Créeme, esto se va a ir aclarando.
[00:28:40] ¿Por qué lo hace así?
[00:28:43] Porque añadir noise a un millón de píxeles,
[00:28:47] por ejemplo,
[00:28:48] y quitárselo paso a paso llevaría una eternidad y sería
[00:28:52] durísimo para tu computadora.
[00:28:55] Así que, en lugar de eso, lo comprime.
[00:29:00] Digamos que tomas una imagen:
[00:29:02] en vez de regenerar esa imagen,
[00:29:05] lo que tardaría muchísimo porque tendría que recalcular cada píxel,
[00:29:11] primero la comprime en un archivo mucho más pequeño.
[00:29:15] Después ese archivo se
[00:29:19] modifica y, en el último paso, ese archivo pequeño vuelve a hacerse grande.
[00:29:28] Una metáfora que siempre uso para explicarlo es compararlo con un archivo zip.
[00:29:33] Para que no haya confusión:
[00:29:37] no funciona literalmente con un zip,
[00:29:39] es una metáfora. Digamos que tienes esta imagen y
[00:29:45] quieres hacer algo con ella.
[00:29:48] La subes a un bot de IA,
[00:29:52] por ejemplo. Es una imagen pesada,
[00:29:55] tiene un millón de píxeles.
[00:29:58] Si la generamos entera otra vez,
[00:30:01] será demasiado exigente para el hardware y tardará 10 minutos.
[00:30:06] Entonces, ¿qué hacemos? La convertimos en un archivo pequeño.
[00:30:12] ¿Sí? Un archivo pequeño que ya no puedes mirar, porque es
[00:30:17] demasiado pequeño. Y esto lo hacemos con un VAE Encode.
[00:30:22] Recuerda este nombre para más adelante, porque va a volver a aparecer.
[00:30:25] VAE ENCODE.
[00:30:28] VAE significa variational autoencoder.
[00:30:31] Codifica automáticamente esta imagen en
[00:30:36] un archivo muy pequeño. Pasa de un millón de píxeles
[00:30:42] a 16.000 números. Ya no son píxeles,
[00:30:47] se convierten en números. Todo esto de la parte del medio
[00:30:55] no lo vemos: pasa detrás de escena,
[00:30:57] detrás de escena del modelo de IA.
[00:31:00] Nunca lo vemos. Pero es lo que pasa cuando haces clic en generar.
[00:31:05] Bien. Luego, en el siguiente paso,
[00:31:09] cuando la IA ya modificó este archivo comprimido,
[00:31:15] lo decodifica. Hace lo contrario de codificar, otra vez con un VAE,
[00:31:21] variational autoencoder.
[00:31:24] Lo decodifica. ¿Qué significa eso?
[00:31:27] Es como descomprimir la imagen.
[00:31:28] Hace que una imagen de 16.000 números
[00:31:34] vuelva a tener un millón de píxeles,
[00:31:38] y entonces podemos verla otra vez. Esta parte puedes verla como la primera.
[00:31:44] Este es el mundo humano. Se traduce al mundo de la IA,
[00:31:50] y después se
[00:31:54] decodifica de nuevo en píxeles visibles para los humanos.
[00:31:58] No hace falta que lo entiendas demasiado a fondo,
[00:32:03] pero así es como hay que pensarlo.
[00:32:06] Lo que vemos aquí es una captura de un workflow muy básico,
[00:32:11] el más estándar de ComfyUI. Vamos
[00:32:17] a profundizar mucho en esto antes de abrir Comfy nosotros mismos.
[00:32:25] Cómo funciona: si alguna vez usaste Grasshopper, o sabes qué es,
[00:32:30] Grasshopper y Comfy
[00:32:33] son plataformas de programación visual.
[00:32:38] Funciona con nodos. Todo lo que ves aquí,
[00:32:42] estas cosas, son nodos,
[00:32:46] bloques, y los conectas entre sí con hilos.
[00:32:50] Los conectas con estas líneas y entonces
[00:32:54] los datos de este pasan al siguiente, y tienes una especie de cadena.
[00:33:00] Lo que siempre se mantiene es que va de izquierda a derecha.
[00:33:05] Espero que quede claro con esta flecha.
[00:33:10] La parte izquierda es la de entrada, el input.
[00:33:15] Aquí introduces el modelo, el prompt,
[00:33:18] la proporción. La segunda parte es siempre la generación,
[00:33:24] y la tercera es siempre el output.
[00:33:28] Puede verse distinto, pero, en general,
[00:33:29] esto forma parte de cualquier workflow.
[00:33:32] Input, generación, output. Si hacemos zoom en un nodo,
[00:33:39] vemos que en el lado izquierdo tenemos el input.
[00:33:45] Otra vez, va de izquierda a derecha.
[00:33:47] El nodo recibe el input por la izquierda y
[00:33:52] entrega el output por la derecha,
[00:33:55] igual que en Grasshopper.
[00:34:01] Ahora, nodo por nodo: ¿qué significan realmente estos nodos?
[00:34:05] El primero es Load Checkpoint.
[00:34:08] Carga el modelo de difusión,
[00:34:11] que está entrenado con el dataset.
[00:34:13] Puede ser, por ejemplo, Stable Diffusion 1.5, FLUX.2
[00:34:18] o FLUX.1, o cualquier modelo que sea open source.
[00:34:24] Aquí ves una pista de que esto es Stable Diffusion 1.5,
[00:34:28] pero hay
[00:34:30] muchísimos modelos, y vamos a ver unos cuantos.
[00:34:37] Este lo vamos a saltar por ahora.
[00:34:39] La siguiente parte es el prompt positivo.
[00:34:42] ¿Qué hace? Aquí escribes tu prompt,
[00:34:46] muy fácil. El siguiente es el prompt negativo,
[00:34:51] o sea, lo contrario. Lo que pongas aquí,
[00:34:54] el modelo lo va a evitar. ¿Y qué hace que uno sea positivo y el otro negativo?
[00:35:00] Te preguntarás, porque el nodo se llama igual en los dos casos.
[00:35:04] Es porque la salida
[00:35:06] de este está conectada a "negative".
[00:35:11] No se ve muy claro, pero fíjate que este hilo
[00:35:16] va a "negative". Y la salida de este otro nodo
[00:35:23] está conectada a "positive". Eso significa que esto se va a recibir
[00:35:28] como prompt positivo, y esto, como negativo.
[00:35:33] Este nodo, Empty Latent Image,
[00:35:35] es del que hablábamos antes.
[00:35:37] Antes de generar algo,
[00:35:41] definimos la proporción de la imagen.
[00:35:44] Digamos que tenemos estos ajustes:
[00:35:47] 512 por 512. Es solo un contenedor vacío
[00:35:53] de 512 píxeles por 512 píxeles.
[00:35:57] Si cambiamos este ajuste,
[00:36:03] el ancho y el alto, así, ves que se convierte en un rectángulo.
[00:36:07] Esto es simplemente cómo se va a crear tu imagen de salida.
[00:36:13] El KSampler es donde realmente se genera la imagen.
[00:36:19] Puedes verlo como el motor del auto.
[00:36:22] Todas las entradas llegan aquí, por el lado izquierdo.
[00:36:27] Hay un montón de ajustes aquí abajo.
[00:36:33] Y la salida es la imagen.
[00:36:39] Tenemos el KSampler, y la entrada de este nodo es la proporción.
[00:36:45] Es este de aquí. Lo que acabamos de ver.
[00:36:51] El KSampler le va a añadir noise.
[00:36:55] Aquí vas a ver "seed", y acabamos de ver la definición de seed:
[00:36:59] es el documento de identidad de un noise.
[00:37:03] En el primer paso, añade noise a esta imagen vacía.
[00:37:09] Ya no está vacía. Y a partir de ese noise,
[00:37:12] va a dar X cantidad de steps.
[00:37:16] Recuerda: los steps son
[00:37:18] cuántas iteraciones hacen falta para pasar del noise a una imagen.
[00:37:22] Aquí está acelerado, de una sola vez,
[00:37:26] pero normalmente son muchos pasos pequeños hasta tener una imagen realista.
[00:37:33] O sea, la cantidad de iteraciones para hacer una imagen.
[00:37:36] El CFG es un parámetro concreto.
[00:37:39] Es cuánto sigue tu prompt frente a cuánto
[00:37:45] se pone creativo, pero no te preocupes por eso en esta etapa.
[00:37:49] Ese también lo vamos a saltar.
[00:37:51] Y Save Image simplemente se asegura de que tu imagen se guarde
[00:37:57] en el programa.
[00:38:01] Ahora vamos a rehacer todo este esquema, pero como metáfora.
[00:38:06] Y la metáfora es la de una cocina.
[00:38:10] Tienes que ver ComfyUI como un restaurante o una cocina.
[00:38:15] Da igual. Si ComfyUI es un restaurante,
[00:38:21] el Load Checkpoint es el chef.
[00:38:24] Así que
[00:38:28] lo que cargas aquí es el chef.
[00:38:30] Este es el modelo, el modelo de difusión,
[00:38:33] como Stable Diffusion 1.5 o FLUX.2.
[00:38:36] Y ha visto muchísimas imágenes.
[00:38:40] El chef ha visto muchísimos platos.
[00:38:42] Lleva 20 años cocinando,
[00:38:44] así que conoce casi todos los platos del mundo.
[00:38:48] El prompt positivo es como el pedido del cliente.
[00:38:55] El cliente llega al restaurante
[00:38:57] y dice: quiero pollo con papas.
[00:38:59] Muy simple. El prompt negativo puedes verlo como la alergia del cliente.
[00:39:06] Es como decir: soy el cliente,
[00:39:09] quiero pollo con papas,
[00:39:12] pero soy alérgico al ajo, o algo así.
[00:39:16] Entonces escribiría "ajo" en el prompt negativo.
[00:39:18] Así el chef, el modelo de difusión,
[00:39:22] sabe que tiene que evitar el ajo.
[00:39:29] La Empty Latent Image, que es dificilísima de entender,
[00:39:34] es simplemente el plato. Puedes verlo como el plato vacío en el que
[00:39:40] el chef va a servir la comida al final.
[00:39:43] Si el plato es muy grande,
[00:39:48] así, el chef sabe:
[00:39:50] tengo que hacer mucha comida.
[00:39:53] Quizá necesite hacer un pollo entero, mientras que,
[00:39:58] cuando el plato es pequeñísimo,
[00:40:00] sabe que con medio pollo alcanza.
[00:40:04] Aquí cambias el tamaño del plato en el que el chef va a cocinar después.
[00:40:08] El KSampler, en esta metáfora, es el fogón.
[00:40:14] Aquí llega el chef: sabe el pedido del cliente,
[00:40:19] sabe la alergia del cliente,
[00:40:21] sabe qué tamaño tiene el plato
[00:40:27] en el que debe servir la comida.
[00:40:29] También sabe los steps.
[00:40:32] ¿Cuántos pasos tengo que dar para hacer este plato?
[00:40:37] Cortar el pollo, condimentarlo, etcétera.
[00:40:40] Eso son los steps: cuántos pasos doy.
[00:40:42] El factor de creatividad, el CFG,
[00:40:47] es cuánto sigue el chef la receta frente a cuánto
[00:40:53] improvisa. Si lo pones en 10,
[00:40:57] el chef sigue la receta al pie de la letra.
[00:40:59] Si pones el CFG en uno,
[00:41:03] es como decirle al chef: haz lo que quieras.
[00:41:07] Es carta blanca, haz lo que quieras.
[00:41:09] Es un poco ridículo,
[00:41:12] pero me di cuenta de que esto ayuda mucho a la gente a
[00:41:18] ver cada nodo como una función.
[00:41:21] Y el último nodo.
[00:41:25] Save Image es la comida,
[00:41:27] el plato con el pollo y las papas, sin ajo.
[00:41:33] Me salté dos muy importantes a propósito:
[00:41:37] los VAE. El VAE es más bien el mesero.
[00:41:42] Al principio, el VAE Encode
[00:41:47] es la persona que va al cliente,
[00:41:50] al comensal, y le pregunta:
[00:41:53] ¿qué quieres comer? Porque
[00:41:55] el cliente nunca habla directamente con el chef.
[00:41:57] El cliente habla con el mesero,
[00:42:01] el mesero lo convierte en una comanda,
[00:42:04] y esa comanda va al chef.
[00:42:06] No hay contacto entre el cliente y el chef.
[00:42:11] Siempre hay algo en medio.
[00:42:15] Y, en este caso, la forma en que se transforma el lenguaje
[00:42:20] del cliente en esa comanda,
[00:42:23] la descripción escrita de lo que pide el cliente, eso es el VAE.
[00:42:29] Puedes verlo como el mesero.
[00:42:31] Aquí, en el VAE Decode,
[00:42:35] también es un mesero, pero otro: cuando el plato está listo,
[00:42:40] lo saca de la cocina y se lo lleva
[00:42:45] al cliente, y le quita esa
[00:42:52] esa tapa, no sé cómo se llama,
[00:42:55] esa cosa tan de cliché al servir un plato,
[00:42:58] y la tapa se retira en la mesa para que el cliente
[00:43:03] pueda comer. Por eso es un poco más difícil
[00:43:08] explicar el VAE, pero es simplemente la forma en que la información pasa
[00:43:15] entre el cliente, que hace el prompt, y el chef,
[00:43:21] que es el modelo de difusión.
[00:43:25] Bien, ¿y por qué son interesantes los modelos open source?
[00:43:31] Seguramente pienses: ya, bueno,
[00:43:33] ¿pero para qué necesito todo esto tan complicado?
[00:43:37] Puedo usar ChatGPT o Nano Banana de Google.
[00:43:42] ¿Para qué va a servir esto realmente?
[00:43:46] Herramientas como Midjourney, Nano Banana
[00:43:50] o ChatGPT son cajas negras. Escribes un prompt,
[00:43:53] aparece una imagen.
[00:43:55] Y no tienes casi ningún control sobre lo que pasa en medio.
[00:43:59] Es como comprar un auto al que no puedes abrirle el capó ni cambiarle el motor.
[00:44:05] Con open source, u open weights,
[00:44:09] que es solo otro nombre, modelos como FLUX,
[00:44:12] sí puedes abrir el capó y ajustar el motor,
[00:44:16] la transmisión o el escape,
[00:44:18] o pintar el auto: puedes hacer lo que quieras, porque tienes el control total
[00:44:23] sobre él.
[00:44:25] Pero quizá esté yendo demasiado rápido,
[00:44:28] así que, si todavía no está del todo claro,
[00:44:31] no pasa nada. Vamos a configurar dos agentes,
[00:44:37] o dos expertos, que te van a ayudar cuando estés trabajando
[00:44:44] con esto y algo se rompa o algo no quede claro.
[00:44:51] Vamos a Miro.
[00:44:58] Se trabó un poco. Cuando vas al módulo uno, a la introducción,
[00:45:03] verás que lo primero que vamos a hacer es crear un experto en Comfy.
[00:45:08] No es más que crear un proyecto personalizado.
[00:45:12] Vas al LLM que prefieras;
[00:45:16] el mío es Claude.
[00:45:19] Vamos a "resources". Quiero mostrarte algo rapidísimo.
[00:45:26] En "models overview" tienes un enlace a un sitio que se llama Arena,
[00:45:32] y lo que hace Arena es clasificar...
[00:45:40] Aquí, el resumen. Clasifica todos los modelos.
[00:45:44] Puedes ir, por ejemplo, a "chat" y elegir "text".
[00:45:53] Es una tabla de clasificación de qué modelos son mejores generando texto.
[00:46:02] Ves que en el número uno está Claude,
[00:46:05] Fable 5; después está Opus.
[00:46:07] Los cinco primeros puestos son todos de Anthropic,
[00:46:13] así que es Claude, y por eso yo también lo uso.
[00:46:15] Uso Claude porque ahora mismo es simplemente el mejor.
[00:46:18] Puedes mirar edición de imagen.
[00:46:20] Ahí es ChatGPT el que está en el primer puesto.
[00:46:25] También está Nano Banana, por aquí,
[00:46:28] y también...
[00:46:31] Haz clic en "open source" y verás que FLUX también está entre los mejores.
[00:46:36] Échale un vistazo a este sitio, porque cambia todos los días y lo mantienen
[00:46:40] actualizado con qué modelos son realmente buenos.
[00:46:43] Esa es la razón por la que
[00:46:46] elegí Claude como mi LLM.
[00:46:52] Lo que vamos a hacer, sigue mis pasos:
[00:46:55] copia este prompt tan simple,
[00:46:58] entra en
[00:47:00] tu LLM y haz clic en nuevo proyecto,
[00:47:03] está aquí. Después ves esta pestaña,
[00:47:08] le pones un nombre, lo llamas...
[00:47:14] ¿Experto en Comfy?
[00:47:19] Vas a instrucciones. Puede verse un poco distinto en tu caso,
[00:47:24] o si usas ChatGPT, también sirve,
[00:47:27] o Gemini, da igual.
[00:47:28] Pregunta cómo hacer un proyecto personalizado en Gemini y te dará
[00:47:33] todos los pasos. Si usas Claude,
[00:47:35] esto es lo que tienes que hacer.
[00:47:37] Lo pegas aquí y guardas las instrucciones.
[00:47:42] Ahora todos los chats dentro de este proyecto van a tener esto como contexto.
[00:47:48] Y es algo supersimple.
[00:47:50] Es una URL a la documentación de Comfy Cloud.
[00:47:55] Si voy a internet y escribo Comfy Cloud...
[00:48:10] Bien, se abre directamente.
[00:48:11] ...
[00:48:17] Documentación, aquí está. En este sitio
[00:48:21] vas a encontrar toda la información que puedas necesitar si tienes dudas.
[00:48:26] Así que, antes de preguntarme a mí,
[00:48:30] puedes mirar este sitio web.
[00:48:34] Este enlace está también,
[00:48:38] por supuesto, en "resources", en sitios web relevantes.
[00:48:42] Aquí ves la documentación oficial de ComfyUI.
[00:48:46] Si haces clic aquí, te lleva a la misma página.
[00:48:50] Aquí puedes decir:
[00:48:53] quiero Comfy Cloud, o quiero instalarlo en local,
[00:48:57] que lo explico más adelante.
[00:49:00] O nodos:
[00:49:04] cualquier duda que tengas, tutoriales,
[00:49:08] tutoriales de text to image; te guía por todo lo que necesitas saber.
[00:49:17] Si volvemos a las instrucciones,
[00:49:19] es solo un enlace a esa página y a otro sitio llamado ComfyWiki,
[00:49:27] que también tiene mucha documentación.
[00:49:30] Si haces una pregunta: ¿por qué
[00:49:33] no me funciona ComfyUI?
[00:49:40] seguramente te dirá algo como: ¿puedes subir una captura de pantalla?
[00:49:44] Y si le das la captura, te va a decir que pruebes esto
[00:49:49] y aquello. No lo voy a ejecutar, pero
[00:49:53] te puedes imaginar por qué esto
[00:49:58] es utilísimo.
[00:50:03] Es una solución rápida y muy fácil.
[00:50:06] Yo la uso todo el tiempo porque, aunque esto sea mi trabajo a tiempo completo,
[00:50:12] a veces pasa algo que no entiendo del todo y siempre
[00:50:16] voy a mi experto en Comfy antes de preguntarle a nadie.
[00:50:21] Y el 99 % de las veces me ayuda a resolver el problema.
[00:50:29] ¿Qué es Comfy? Lo que ves aquí son dos versiones distintas.
[00:50:36] A la izquierda, ComfyUI corriendo en local,
[00:50:41] lo que significa que, cuando generas una imagen,
[00:50:44] usa tu propia computadora para generarla.
[00:50:48] O sea, va a necesitar tu propia
[00:50:55] GPU, tu
[00:50:57] unidad de procesamiento gráfico, para hacer la imagen.
[00:51:02] Eso significa que también es gratis. Puedes ir a Comfy,
[00:51:07] hacer clic en descargar, y usarlo es completamente gratis.
[00:51:11] Sin embargo, no vamos a usar esto, sino Comfy Cloud.
[00:51:17] Es decir, la parte de la derecha.
[00:51:23] El motivo es que
[00:51:25] estos modelos más nuevos, que veremos más adelante,
[00:51:28] se han vuelto tan grandes que, si quieres ejecutarlos en local,
[00:51:33] necesitas una supercomputadora. Una computadora carísima.
[00:51:37] Antes se podía ejecutar en local,
[00:51:40] pero ahora necesitas una muy,
[00:51:43] muy, muy, muy buena para hacerlo.
[00:51:47] Si estás viendo esto y eres renderista o tienes una computadora buenísima,
[00:51:54] probablemente, si la tienes muy buena,
[00:51:56] puedas averiguar cómo descargarlo todo desde el sitio web.
[00:52:03] Es un poco más técnico, pero también puedes instalarlo desde GitHub.
[00:52:09] Supongo que, si no tienes una supercomputadora,
[00:52:13] te va a interesar más Comfy Cloud.
[00:52:16] En vez de ejecutarlo en local en tu propia computadora,
[00:52:21] simplemente
[00:52:22] compras una suscripción y usas su nube y
[00:52:28] sus GPU. Para que te hagas una idea de por qué hace falta:
[00:52:33] si quieres ejecutar FLUX.2,
[00:52:36] que es el modelo principal que vamos a usar,
[00:52:39] necesitarías unos 32 gigabytes de VRAM,
[00:52:45] que es muchísimo. Yo tengo una computadora muy buena,
[00:52:48] con 12 gigabytes de VRAM, y no alcanza.
[00:52:52] Con Comfy Cloud pagas una suscripción mensual,
[00:52:56] pero tienes acceso a 96 GB de VRAM.
[00:53:01] Es una locura. Lo que significa que también es rapidísimo.
[00:53:05] En local, tardas unos dos minutos en hacer
[00:53:11] una imagen; en Comfy Cloud, con esta GPU,
[00:53:14] tarda unos cinco segundos. Y también te voy a mostrar cómo crear
[00:53:21] una cuenta, así que tranquilo.
[00:53:24] Entra al sitio web si tienes dudas,
[00:53:29] copia la URL, pégala en tu LLM y así tienes un asistente virtual que
[00:53:35] sabe muchísimo más del tema que nadie.
[00:53:38] Vamos a crear una cuenta de Comfy Cloud.
[00:53:47] Ve al sitio web de Comfy desde Miro,
[00:53:52] el mismo de siempre; todos estos llevan al mismo sitio.
[00:53:57] Este es un poco distinto, pero ve a Comfy Cloud,
[00:54:01] haz clic en la URL de origen. De nuevo,
[00:54:06] si quieres hacerlo en local, haz clic aquí.
[00:54:08] Eso no lo voy a cubrir; nosotros vamos a usar la nube.
[00:54:12] Si ves esto con una cuenta nueva,
[00:54:15] simplemente te
[00:54:16] va a pedir que te crees una cuenta.
[00:54:19] Inicia sesión con Google, como hice yo,
[00:54:23] y verás esta interfaz.
[00:54:27] Verás los planes y los precios.
[00:54:34] Ves que el estándar son 20 dólares al mes,
[00:54:38] unos 16 euros más o menos.
[00:54:40] Con el plan Creator tienes más créditos,
[00:54:44] y el Pro son 100. Funciona así: cada mes recibes
[00:54:50] X cantidad de créditos que puedes usar.
[00:54:53] Pero para las cosas que voy a mostrar,
[00:54:57] necesitarías el plan Creator.
[00:55:00] Así que, si lo haces
[00:55:02] para un concurso o solo para ti,
[00:55:04] puedes contratarlo un solo mes:
[00:55:06] son unos 28 euros.
[00:55:09] O lo ejecutas en local, pero entonces necesitas una buena computadora.
[00:55:14] Así tienes 7.400 tokens.
[00:55:19] Normalmente sobra para experimentar cada mes.
[00:55:27] Cuando abres el workflow,
[00:55:30] se ve así. Aquí, a la izquierda, tienes la barra de tareas.
[00:55:36] Te recomiendo mucho hacer esto en paralelo conmigo
[00:55:42] y ver directamente qué hace cada cosa.
[00:55:44] Puedes crear un archivo nuevo, importar o exportar algo,
[00:55:49] editar, lo que sea.
[00:55:54] Poner el tema claro u oscuro,
[00:55:58] da bastante igual.
[00:56:04] Todo lo mismo. Esta, la versión beta de nodos 2.0,
[00:56:08] actívala. Solo cambia un poco el aspecto.
[00:56:13] Puedes explorar plantillas, ajustes,
[00:56:15] etc. En "assets", a ti te va a aparecer vacío,
[00:56:20] pero estas son algunas imágenes que generé antes.
[00:56:24] También ves cuánto tardó en generarse.
[00:56:26] Esta la vas a ver más adelante en el tutorial: la vamos a generar.
[00:56:32] Tardó cincuenta segundos porque es una imagen bastante grande.
[00:56:40] Aquí, la biblioteca de nodos. Esta no la vas a usar
[00:56:46] mucho. La biblioteca de modelos la usaremos en el siguiente módulo,
[00:56:52] el de text to image. En Workflows
[00:56:55] puedes guardar todos tus workflows.
[00:56:58] ¿Cómo? Digamos que tienes un workflow y haces clic en "save as",
[00:57:03] le pones un nombre y lo encuentras en workflows.
[00:57:08] Apps no lo vas a usar en este curso.
[00:57:12] Templates es importantísimo.
[00:57:16] Probablemente sea lo más importante que te voy a decir hoy.
[00:57:20] Todo lo que te voy a mostrar son plantillas mías,
[00:57:23] pero Comfy Cloud ofrece muchas plantillas ya hechas que puedes usar directamente.
[00:57:30] Todo esto, si haces clic,
[00:57:33] por ejemplo, voy a
[00:57:38] buscar una que sea bastante accesible.
[00:57:40] Digamos que queremos un modelo
[00:57:46] de edición de imagen, por ejemplo.
[00:57:58] Da igual cuál, pero estoy buscando una...
[00:58:09] Esta. Esta es una de las más básicas.
[00:58:14] Veo que se está trabando, así que lo voy a refrescar.
[00:58:18] A veces pasa.
[00:58:27] Ahora sí está. Puedes cerrar esto.
[00:58:30] Esto es solo para usuarios locales. Si lo ejecutas en local,
[00:58:34] aquí te dice qué modelo.
[00:58:37] Haces clic y descarga este VAE.
[00:58:43] Yo no lo necesito, pero puedes descargarlo directamente aquí.
[00:58:46] Y después
[00:58:49] te dice en qué carpeta tienes que poner los modelos y demás.
[00:58:54] Pero para este tutorial da igual,
[00:58:56] así que lo voy a borrar. Así se ve un workflow.
[00:59:01] Puedes tomar todos los nodos que vimos antes,
[00:59:04] arrastrarlos, hacerlos más pequeños o más grandes.
[00:59:07] Si haces clic aquí, arriba.
[00:59:12] Puedes darle un color si quieres.
[00:59:14] Es cuestión de gustos. Hacerlo más grande,
[00:59:20] lo que quieras. A mí me gusta ordenarlos así.
[00:59:26] Y cuando haces clic en "run",
[00:59:30] veamos qué pasa. La entrada es la imagen de una mujer.
[00:59:34] Esto es solo la plantilla. El prompt dice
[00:59:41] que le ponga un gorro en la cabeza, y lo hace.
[00:59:45] Este es el primer ejemplo del workflow
[00:59:50] más famoso ahora mismo. Y aquí puedes hacer clic en descargar si
[00:59:57] quieres bajar la imagen.
[00:59:58] Aquí hay algunos ajustes que no vamos a ver ahora.
[01:00:02] Podría guardar este workflow con "save as",
[01:00:05] podría exportarlo o borrarlo, si quisiéramos.
[01:00:11] Lo que sea. Como tengo muchos workflows abiertos,
[01:00:15] y esto es solo un ejemplo,
[01:00:16] lo voy a cerrar antes de borrarlo,
[01:00:21] y así queda vacío otra vez. Esto es solo un repaso rápido.
[01:00:26] Si necesitas algo, tu cuenta está aquí arriba.
[01:00:29] Ves cuántos créditos tienes,
[01:00:31] puedes cambiar de plan, cerrar sesión,
[01:00:33] ajustes de la cuenta. Y esto es importante:
[01:00:38] es ejecutar el workflow.
[01:00:41] Aquí, el batch count, el número que está justo antes de "run".
[01:00:49] Es cuántas veces se va a ejecutar.
[01:00:51] Si pones quince, cosa que no recomiendo,
[01:00:55] al hacer clic una vez en "run", se repite 15 veces.
[01:00:59] Genera una imagen, luego otra,
[01:01:02] y otra, y así hasta 15 veces.
[01:01:05] Déjalo en uno. Aquí puedes ver qué imágenes
[01:01:10] están en la cola. Digamos que generas cinco imágenes:
[01:01:14] cada vez
[01:01:16] se añade a la lista de espera.
[01:01:19] Esa es una introducción breve. Vamos a usar esto muchísimo,
[01:01:23] así que no te preocupes si no queda todo claro.
[01:01:28] Ya configuramos Comfy Cloud. Algunas cosas prácticas.
[01:01:32] ¿Por qué usamos Comfy? Más o menos ya lo expliqué.
[01:01:36] ¿Pero por qué uso Miro para compartir documentos o imágenes?
[01:01:42] Porque si vas a Miro
[01:01:49] y abres una imagen —todas las imágenes de aquí funcionan así,
[01:01:52] por eso solo pongo esas imágenes—,
[01:01:55] digamos que estás aquí. También pone "importable en Comfy".
[01:02:01] Cuando haces clic, puedes descargarla.
[01:02:05] Digamos que descargamos esta.
[01:02:13] Descargada; a mí ya me aparece, así que...
[01:02:21] Tomamos esta imagen y la arrastramos a nuestro workflow.
[01:02:31] Y entonces vemos el workflow entero.
[01:02:35] Este es exactamente el workflow,
[01:02:40] el prompt y los ajustes exactos que usé para generar esta imagen.
[01:02:46] Lo que significa que, si hacemos clic en "run",
[01:02:49] estos nodos se van a activar.
[01:02:52] Verás un borde azul alrededor.
[01:02:55] Y al final va a aparecer exactamente la misma imagen que esta.
[01:03:02] Veamos qué pasa.
[01:03:06] ¿Ves lo rápido que se genera?
[01:03:08] Es exactamente la misma imagen que esta.
[01:03:11] ¿Por qué? Porque la seed era exactamente
[01:03:16] la misma que usé. Y aquí vemos todos los nodos que
[01:03:22] expliqué muy a fondo antes,
[01:03:25] así que puedes moverte por ahí, hacerlo más pequeño o más grande.
[01:03:31] Mira esto.
[01:03:34] Este noodle está conectado a ese.
[01:03:37] No se ve bien porque está detrás.
[01:03:41] Sepáralo y mira cuáles están conectados.
[01:03:44] El modelo de aquí está conectado a ese modelo.
[01:03:47] Digamos que lo rompes.
[01:03:52] No te puedes equivocar demasiado, porque si arrastras este
[01:03:57] y quieres conectarlo aquí,
[01:03:59] no se puede. Ves que se vuelve transparente.
[01:04:02] Porque este es otro tipo de información.
[01:04:05] Si te acercas por aquí, se engancha,
[01:04:10] va solo a su sitio, porque está hecho para eso.
[01:04:14] Y al soltarlo, queda conectado.
[01:04:20] Añadir un nodo en medio. Puedes añadir lo que quieras.
[01:04:24] Es algo avanzado, pero esta es la idea general.
[01:04:30] Este es el workflow más básico de todos.
[01:04:32] Lo importante aquí es la seed.
[01:04:37] Recuerda que es como el documento de identidad de la imagen,
[01:04:40] que...
[01:04:44] Si haces clic aquí, puedes fijarla en este valor.
[01:04:49] Si la pones en aleatorio, cada vez es una seed distinta.
[01:04:54] Siempre va a seguir el prompt,
[01:04:57] que es "beautiful scenery nature glass bottle landscape,
[01:05:02] purple galaxy bottle". Es un prompt rarísimo,
[01:05:06] pero ves que hizo justo eso.
[01:05:12] Si lo volvemos a ejecutar, ahora tiene otra seed, porque la última vez
[01:05:19] estaba en "randomize value":
[01:05:24] cambia el valor al azar después de cada generación.
[01:05:27] Hacemos clic en "run" y va a seguir siendo "beautiful scenery,
[01:05:33] nature glass bottle landscape",
[01:05:35] pero será una imagen distinta a esta.
[01:05:40] Mira: si lo hago otra vez, siempre sale una distinta.
[01:05:51] Ves que está activo, o sea, generando.
[01:05:54] A veces es rapidísimo, a veces tarda un poco.
[01:06:01] Siempre es este.
[01:06:05] ¿Por qué muestro esto? Porque cuando haces clic aquí y eliges
[01:06:09] "fixed value", lo ejecutamos otra vez.
[01:06:13] Esta vez todavía va a ser una imagen distinta.
[01:06:16] Pero a partir de ahora,
[01:06:19] si hacemos clic en "run", va a ser exactamente la misma imagen siempre.
[01:06:26] Ves que no cambió. Trabajo terminado y sigue siendo la misma imagen porque
[01:06:30] bloqueamos la seed. Ya no genera una seed nueva.
[01:06:35] Usa exactamente la misma. Podemos hacer clic mil veces
[01:06:39] y la imagen de salida va a ser siempre esta.
[01:06:43] Siempre. Si descargo...
[01:06:49] Ves, trabajo terminado, la misma imagen.
[01:06:51] Si descargo esta y la tomo
[01:06:57] y la meto aquí...
[01:07:01] Puedes descargar esta y probarlo,
[01:07:03] y será exactamente igual.
[01:07:05] Lo mismo aquí. Mira la seed
[01:07:09] y verás un número de seed distinto.
[01:07:11] Bien. Digamos que dejamos la seed bloqueada o fija.
[01:07:18] Y cambiamos los steps a cuatro.
[01:07:23] Ahora el modelo solo tiene cuatro pasos para generar la imagen,
[01:07:28] lo que da como resultado
[01:07:30] una imagen rota, porque no tuvo pasos suficientes para generarla.
[01:07:37] Voy a volver rápido a las diapositivas
[01:07:42] para mostrarte...
[01:07:47] Aquí. Es como decir que, en vez de tener estos diez pasos,
[01:07:53] tienes que parar aquí.
[01:07:58] Claro que la imagen no va a ser buena, porque todavía se estaba generando,
[01:08:02] la cortamos antes de tiempo. Eso es lo que acabo de hacer.
[01:08:08] Y ahora, ¿cómo sabes cuántos steps poner?
[01:08:14] La regla general es que las plantillas que yo te doy, o las plantillas que
[01:08:20] vienen con Comfy, ya tienen los mejores ajustes,
[01:08:26] así que no los cambies. Cambiarlos es algo más avanzado,
[01:08:30] no algo que tengas que hacer tú como principiante.
[01:08:36] Así que no los cambies,
[01:08:39] salvo que estés simplemente experimentando.
[01:08:40] Si lo vuelves a poner en veinte y generas otra vez,
[01:08:45] verás que es exactamente la misma imagen que antes.
[01:08:48] El CFG, recuerda, es cuánto
[01:08:55] sigue el modelo el prompt frente a cuánta creatividad puede aplicar.
[01:08:59] Si lo ponemos en veinte, muy alto,
[01:09:04] va a intentar seguir el prompt de forma extremadamente literal.
[01:09:09] Extremadamente literal.
[01:09:18] Generando...
[01:09:29] Lo que hace es romper la imagen, porque intenta
[01:09:32] seguirlo de forma tan exacta que se pasa.
[01:09:35] De nuevo, si lo ponemos otra vez en ocho y ejecutamos,
[01:09:40] vuelve a ser la misma imagen. Ahora digamos que lo ponemos en uno.
[01:09:45] Uno significa que puede hacer lo que quiera.
[01:09:51] No tiene por qué seguir el prompt,
[01:09:53] no tiene que hacer una botella de vidrio,
[01:09:56] tiene muchísima libertad.
[01:09:58] Ves que no lo sigue bien,
[01:10:00] hace cualquier cosa. Por eso es importante mantener el CFG alrededor de 8.
[01:10:06] Para este modelo, para Stable Diffusion 1.5.
[01:10:11] Para modelos más nuevos, los ajustes son otros,
[01:10:13] pero no te preocupes por eso. Lo último que vamos a ver es
[01:10:18] la empty latent image. Digamos que la ponemos en 1024
[01:10:22] de ancho.
[01:10:26] Verás que la imagen de salida se vuelve un rectángulo.
[01:10:32] Experimenta y mira qué pasa. El batch size:
[01:10:36] digamos que lo ponemos en tres; es lo mismo que si lo pones aquí.
[01:10:44] Ahora va a generar tres imágenes.
[01:10:46] Una,
[01:10:50] dos, tres.
[01:10:56] Espero que haya quedado un poco más claro.
[01:11:04] Avancemos un poco más.
[01:11:08] ¿Qué pasó en el workflow?
[01:11:09] Ya lo vimos. Lo siguiente:
[01:11:12] las formas de hacer prompts. Hay tres principales.
[01:11:16] La primera es el prompting por palabras clave,
[01:11:18] keyword prompting,
[01:11:23] perdón; es simplemente poner palabras.
[01:11:25] Ya no lo hacemos así.
[01:11:27] Es más bien como se hacía antes.
[01:11:30] Es algo que acabas de ver.
[01:11:35] Aquí son solo las palabras "beautiful scenery,
[01:11:37] nature, glass". Así se escribían los prompts en workflows antiguos
[01:11:43] como este.
[01:11:48] Después, el lenguaje natural: así lo hacemos ahora.
[01:11:50] Son frases: un plano gran angular de un hormigón brutalista minimalista,
[01:11:56] etc. La regla general es que cuanto antes pongas algo en el prompt,
[01:12:02] más en serio se lo va a tomar.
[01:12:06] Si es algo importantísimo,
[01:12:08] digamos que es clave que sea Barcelona,
[01:12:11] ponlo al principio del prompt, porque cuanto más atrás esté,
[01:12:16] menos
[01:12:17] en serio se lo va a tomar. Pero es solo una regla general.
[01:12:20] La tercera forma se llama JSON prompting, y
[01:12:26] la vamos a usar; no la haremos nosotros, sino que un asistente de IA
[01:12:32] escribirá el prompt así. Estas tres formas
[01:12:37] dicen lo mismo. Hablan de Barcelona,
[01:12:40] brutalismo, hormigón y demás,
[01:12:41] pero con otra manera de
[01:12:45] estructurar la información para que el modelo la entienda mejor.
[01:12:49] Nosotros vamos a usar sobre todo estas dos.
[01:12:57] Estas dos.
[01:13:01] ¿Por qué las muestro todas? Porque estos son modelos más antiguos
[01:13:06] y, cuando hablemos un poco de historia,
[01:13:08] van a aparecer estos nombres.
[01:13:13] El lenguaje natural es más de los modelos nuevos,
[01:13:17] y el asistente de IA es solo para FLUX.2,
[01:13:19] que es el más reciente. El JSON prompting
[01:13:23] es solo una estructura. Es como decir: crea una lista de cinco ideas de startup
[01:13:30] sobre sostenibilidad.
[01:13:31] También puedes decir: generar ideas,
[01:13:34] ámbito sostenibilidad, tipo startup,
[01:13:37] cantidad cinco. Es la misma información, pero con otra estructura.
[01:13:45] La configuración del prompt coach. Vamos a Miro.
[01:13:53] Aquí vemos lo siguiente.
[01:13:57] Puedes saltarte esto,
[01:13:59] es solo informativo. Configuración del prompt coach.
[01:14:02] Hay dos formas de hacerlo.
[01:14:05] Vamos a usar bastantes modelos y preparé este prompt.
[01:14:16] Como ves aquí, tengo dos variantes del prompt coach.
[01:14:21] Esta es sencilla. De hecho, es la mejor.
[01:14:23] Es la que voy a usar yo también.
[01:14:26] Y luego está esta ultradetallada,
[01:14:29] que es larguísima. Pero te da una idea; puedes leerla
[01:14:35] y repasarla. Lo que vamos a hacer:
[01:14:41] copiar y pegar,
[01:14:44] crear un proyecto nuevo
[01:14:48] en el LLM que prefieras, da igual cuál.
[01:14:54] Lo copias y lo pegas aquí,
[01:14:55] guardas las instrucciones y luego solo escribes "start".
[01:14:59] Y si tienes un prompt,
[01:15:03] o simplemente una idea,
[01:15:05] como, no sé, un edificio en las Montañas Rocosas,
[01:15:09] o un pabellón en Barcelona, pones tu prompt aquí,
[01:15:12] te va a preguntar para qué modelo y después
[01:15:17] si quieres un prompt largo o corto.
[01:15:19] Y después, según el modelo que
[01:15:24] hayas dicho, adapta automáticamente el prompt a ese modelo.
[01:15:29] Así no tienes que escribir tú el prompt y lo usas directamente.
[01:15:33] Lo vamos a usar más adelante.
[01:15:38] Dicho esto, el prompt coach ya está listo.
[01:15:46] Ahora vamos a ver un repaso rápido de la historia de los modelos de difusión.
[01:15:51] En la metáfora de la cocina o el restaurante,
[01:15:55] estos son los chefs. Lo que ves aquí son
[01:16:00] los modelos que se fueron lanzando.
[01:16:03] Todo empezó con Stable Diffusion 1,
[01:16:05] Stable Diffusion 2, SDXL, Cascade,
[01:16:10] y después llegó FLUX.1,
[01:16:13] FLUX Kontext, FLUX.2.
[01:16:16] Son todos modelos que se lanzaron
[01:16:24] entre 2022 y 2024.
[01:16:27] Estas son solo imágenes de ejemplo.
[01:16:33] Lo principal que tienes que recordar es que hubo dos empresas muy
[01:16:37] importantes. La primera ya no es muy relevante.
[01:16:42] Es Stability AI. Es la empresa detrás de
[01:16:51] todos estos modelos,
[01:16:54] los cinco primeros, muy famosos. Y los
[01:17:00] últimos cuatro, o tres, de esta imagen son todos
[01:17:06] de Black Forest Labs. La idea es que gente de Stability AI
[01:17:12] se fue y fundó Black Forest Labs.
[01:17:19] Esto seguramente no te diga mucho,
[01:17:22] pero lo que ves aquí es que FLUX.1,
[01:17:25] cuando salió en 2024,
[01:17:29] vino con muchos modelos, cada uno con una función específica.
[01:17:34] Ahora, en 2025 y principios de 2026,
[01:17:38] lanzaron FLUX.2,
[01:17:41] y hay muchos modelos distintos,
[01:17:45] en los que no vamos a profundizar.
[01:17:48] Vamos a usar SDXL, que es el workflow que ya usamos.
[01:17:53] Usamos SDXL aquí; perdón,
[01:17:56] Stable Diffusion 1 y Stable Diffusion XL.
[01:18:00] De Black Forest Labs vamos a usar FLUX.1
[01:18:05] y FLUX.2 klein 9B. Muy concreto.
[01:18:12] ¿Dónde encuentras estos modelos?
[01:18:14] Si usas Comfy Cloud, no necesitas descargar nada.
[01:18:17] Todo está ya en Comfy Cloud.
[01:18:20] Pero, si te interesa,
[01:18:22] puedes ir a este enlace.
[01:18:31] Ve a Hugging Face y escribe... empecemos
[01:18:35] por SD 1.5.
[01:18:45] Pongamos Stability.
[01:18:51] Esta es la empresa Stability AI.
[01:18:54] Aquí ves su repositorio, Stable Diffusion XL, por ejemplo.
[01:19:00] Era uno de los modelos antiguos.
[01:19:04] Si lo descargas aquí, son seis, casi siete gigabytes,
[01:19:09] ¿de acuerdo?
[01:19:12] Ese es este,
[01:19:16] los modelos antiguos. Si vamos a FLUX.2 klein 9B...
[01:19:23] Lo buscamos en Hugging Face.
[01:19:28] De Black Forest Labs, FLUX.2 klein 9B.
[01:19:31] Si vas a "files and versions",
[01:19:33] puedes descargarlo desde aquí.
[01:19:38] Este son dieciocho gigabytes,
[01:19:42] que no es tanto, porque son solo 9.000 millones de parámetros.
[01:19:46] Pero si vas al de desarrollo,
[01:19:49] este de aquí, que es el modelo grande,
[01:19:52] grande, grandísimo que lanzaron...
[01:19:57] Ves que son 64 gigabytes.
[01:20:00] Es gigantesco. Está entrenado con 32.000 millones de imágenes.
[01:20:05] Es enorme y además bastante lento de ejecutar.
[01:20:09] Si lo ejecuto en esta laptop, seguramente explote.
[01:20:13] Es solo para demostrar que estos modelos se volvieron enormes.
[01:20:20] Todo esto no hace falta que lo entiendas.
[01:20:24] Es más bien que, cuando salieron estos modelos nuevos,
[01:20:28] la diferencia es que al principio había modelos de texto
[01:20:34] y modelos de imagen, y ahora están cada vez más combinados.
[01:20:38] Entienden el texto muy bien,
[01:20:40] y la imagen también muy,
[01:20:43] muy bien. FLUX.2 entiende códigos hex.
[01:20:48] Si quieres un color concreto,
[01:20:50] buscas su código hex y va a entender exactamente ese color.
[01:20:55] Entiende el JSON prompting,
[01:20:57] como vimos antes.
[01:21:01] Tiene una gran comprensión contextual,
[01:21:04] lo que significa que sabe muchísimo,
[01:21:08] y la calidad de salida es buenísima:
[01:21:10] puedes llegar a 4K. Todo esto lo voy a saltar porque es
[01:21:16] demasiado teórico, pero puedes mirarlo si te interesa.
[01:21:20] Esta tabla ya la vimos,
[01:21:23] es un resumen. Pasamos de 860 millones de parámetros en 2022
[01:21:30] a 32.000 millones de parámetros en 2025.
[01:21:37] Estas son algunas estadísticas y diferencias entre los modelos.
[01:21:46] Si te interesa, échale un vistazo.
[01:21:48] No necesitas saber todo esto para usarlo ni para usar las plantillas.
[01:21:54] Este PDF, por cierto, también lo vas a encontrar
[01:22:00] en "models overview"; es un resumen que hice yo.
[01:22:04] Puedes ir alternando aquí para entender
[01:22:11] mejor algunas cosas.
[01:22:15] Ya entendemos por qué el open source puede ser interesante,
[01:22:18] pero ¿cómo lo aprovecho yo?
[01:22:22] Algo muy importante son los LoRA.
[01:22:25] LoRA es low rank adaptation, adaptación de bajo rango;
[01:22:28] ese es el significado de la palabra.
[01:22:30] Cuando hablamos de modelos de IA,
[01:22:35] de modelos de difusión, están entrenados con miles de millones de imágenes,
[01:22:38] y eso no es algo que hagamos nosotros como usuarios,
[01:22:44] porque no tenemos los recursos y es demasiado grande.
[01:22:48] Un LoRA lo puede hacer cualquiera, porque se entrena con 20 o 30 imágenes.
[01:22:55] Por eso se llama adaptación de bajo rango.
[01:22:58] Es un archivo muy pequeño, de unos 100 megabytes.
[01:23:02] Y ese archivo solo sabe una cosa,
[01:23:06] y es un estilo. Digamos que tenemos este prompt,
[01:23:11] solo
[01:23:12] un prompt largo para hacer una imagen como si
[01:23:17] la hubiera diseñado Calatrava, o algo así.
[01:23:20] Es solo para ilustrar la idea.
[01:23:24] Sin LoRA se ve así.
[01:23:29] No se parece mucho a Calatrava,
[01:23:31] es más bien arquitectura blob.
[01:23:33] Pero ves que la estética es bastante plástica,
[01:23:37] se nota que es de IA. Yo hice un LoRA
[01:23:42] entrenado específicamente con imágenes reales fotografiadas
[01:23:48] en analógico. Así no parece tan generado por IA.
[01:23:53] Si tomamos el mismo prompt pero usamos mi LoRA...
[01:24:00] Este modelo está entrenado solo con estas veinte o treinta imágenes hechas
[01:24:06] con una cámara concreta que me gusta mucho.
[01:24:12] Este es el resultado, que otra vez se ve parecido:
[01:24:17] sigue siendo blob, sigue teniendo una carretera delante,
[01:24:21] sigue teniendo árboles o algo de vegetación,
[01:24:24] pero ves que esto ya se ve mucho más realista,
[01:24:27] y es justo como a mí me gusta.
[01:24:28] No es mejor ni peor; es solo un ejemplo de cómo dirigir la imagen de salida
[01:24:35] hacia el estilo que prefieras. Y aquí está Nano Banana Pro, para comparar,
[01:24:40] con el mismo prompt.
[01:24:42] Tienes menos control, yo diría.
[01:24:47] Y este es otro ejemplo de una imagen con el mismo prompt, sin
[01:24:53] y con mi LoRA personalizado.
[01:24:56] Para explicarlo un poco mejor:
[01:24:58] entrenar un LoRA no es tan difícil.
[01:25:01] Creo que ya entrené unos 20.
[01:25:04] Solo hay que saber cómo hacerlo.
[01:25:06] No vamos a ver cómo entrenar un LoRA, porque eso
[01:25:11] es un curso en sí mismo. Pero en
[01:25:16] el archivo y la carpeta que recibes de esta clase
[01:25:19] habrá una carpeta de LoRA, y en el siguiente módulo,
[01:25:24] el de text to image, te voy a mostrar cómo importarlos,
[01:25:28] cómo usarlos, cómo ajustarlos,
[01:25:31] etcétera.
[01:25:34] Por ejemplo, si tomamos esta volumetría
[01:25:39] del tercer módulo, que es image to image,
[01:25:43] y tenemos esta imagen de estilo de referencia,
[01:25:47] y queremos aplicarla sobre la geometría.
[01:25:51] Sin el LoRA, en FLUX.2 se ve así.
[01:25:54] Queda bastante plástico.
[01:25:56] Gráficamente no es gran cosa.
[01:25:58] Con mi LoRA puede verse así.
[01:26:01] No diría que es perfecto, pero
[01:26:04] es mucho más realista, tiene estas sombras suaves y
[01:26:11] no esa estética de plástico.
[01:26:13] Muy importante: los LoRA son específicos de cada modelo.
[01:26:18] Un LoRA entrenado con Stable Diffusion 1.5,
[01:26:22] el modelo antiguo, no va a funcionar en FLUX.2, y viceversa.
[01:26:28] Es como hablarle en neerlandés a un francés.
[01:26:31] No
[01:26:32] entiende de qué hablas y no va a funcionar.
[01:26:35] Así que revisa siempre para qué modelo se creó el LoRA.
[01:26:39] En general, si encuentras un workflow y lo descargas, va a quedar
[01:26:45] claro qué LoRA y qué modelo usa.
[01:26:51] No te preocupes por eso, pero ten claro que no puedes tomar un LoRA
[01:26:56] entrenado con SD 1.5 y aplicarlo a FLUX.2.
[01:27:01] ¿Dónde encontrar LoRA interesantes? En estos sitios: Hugging Face y Civitai, que
[01:27:08] también están en el tablero de Miro: si subes a "LoRA links",
[01:27:14] los encuentras en Hugging Face, Civitai, GitHub o directamente en internet.
[01:27:20] Dicho esto, échale un vistazo.
[01:27:29] O pídele a tu LLM que te dé algunas URL.
[01:27:33] Este esquema de denoising es un poco confuso,
[01:27:38] así que lo voy a saltar y paso directamente a este.
[01:27:43] Lo que vemos aquí es exactamente lo mismo que vimos antes.
[01:27:48] Tienes una entrada, digamos texto o imagen,
[01:27:52] y en X cantidad de pasos llegas a una salida.
[01:27:56] Es simplemente el proceso de difusión.
[01:28:00] Lo que hace un LoRA es meterse entre los pasos.
[01:28:06] Digamos que tenemos un prompt de texto que dice
[01:28:14] gato. Muy simple: decimos gato.
[01:28:17] Sin LoRA, va dando pasos y hace cualquier cosa parecida a un gato,
[01:28:24] pero no tenemos control, porque puede ser una foto de un gato,
[01:28:27] puede ser
[01:28:29] un boceto de un gato, un gato corriendo, acostado o saltando,
[01:28:35] puede ser cualquier cosa, no lo sabemos.
[01:28:37] Si entrenamos un LoRA específicamente con gatos,
[01:28:42] gatos negros acostados boca arriba,
[01:28:47] el LoRA va a decir, entre cada paso:
[01:28:51] bien, sigues haciendo la imagen de un gato,
[01:28:54] pero
[01:28:55] recuerda que tiene que ser negro y estar boca arriba.
[01:29:00] O, no sé, un LoRA entrenado con bocetos de gatos solo va a hacer eso.
[01:29:05] Ves que el LoRA solo sabe una cosa.
[01:29:08] Conoce una estética, un carácter visual o un arquitecto, por ejemplo,
[01:29:14] y solo puede hacer eso. Dirige al modelo grande,
[01:29:20] al gran modelo de difusión, que son, digamos, sesenta y cuatro
[01:29:25] gigabytes, mientras que el LoRA son solo cien megabytes, y lo dirige
[01:29:31] en una dirección estética.
[01:29:33] Y aquí ves el "sin" y el "con", simplemente porque lo entrené
[01:29:39] con fotografía analógica de treinta y cinco milímetros.
[01:29:46] Solo algunos ejemplos.
[01:29:50] Si te interesa, síguelo, porque he recibido
[01:29:56] muchas peticiones de un curso sobre entrenamiento de LoRA,
[01:29:59] así que puede que lo montemos en detalle para enseñarte cómo
[01:30:05] hacerlo en el futuro. Sigue la plataforma,
[01:30:09] sígueme a mí, y te avisaremos cuando lo hagamos.
[01:30:17] Esto es solo un adelanto de cómo lo hago yo y de cómo automatizo mucho
[01:30:21] del trabajo aburrido que conlleva entrenar un LoRA.
[01:30:32] Bien, dicho esto, ya cubrimos todo el módulo uno,
[01:30:37] que es la introducción. Voy a cerrar este módulo,
[01:30:42] y el siguiente será el módulo 2,
[01:30:46] Text to Image. ¡Gracias!
