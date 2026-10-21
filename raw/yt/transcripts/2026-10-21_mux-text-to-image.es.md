---
tipo: transcript
fuente: archademy.ai (curso AI x Gaudi, area de participantes)
modulo: text-to-image
titulo: Text-to-Image
idioma: es
fecha_creacion: 2026-10-21
tags: [yt, transcript, curso-ai-gaudi, mux, text-to-image]
---

# Text-to-Image — es

> Transcripcion automatica de los subtitulos del modulo del curso (Mux).
> Origen: https://vz-4ced3a48-15e.b-cdn.net/b4331c95-55f3-422a-a313-e498cb0a01bb/captions/es.vtt
> Duracion de la pista de subtitulos: 00:47:07,000 --> 00:47:09,927

[00:00:01] Hola a todos y bienvenidos a la parte dos.
[00:00:03] Esta parte es sobre text to image y estará más enfocada en la aplicación práctica:
[00:00:10] vamos a usar workflows de verdad,
[00:00:13] vamos a probar mucho. Como la parte uno,
[00:00:15] la introducción, era más teórica y de fundamentos.
[00:00:18] Aquí vamos a generar de verdad,
[00:00:21] vamos a usar Comfy Cloud, LoRA, etc.
[00:00:29] Antes de empezar, quiero contextualizar un poco lo que vamos a hacer.
[00:00:34] Lo que ves aquí delante es una representación esquemática de
[00:00:39] la fase de diseño o, en general, del proceso creativo.
[00:00:43] A la izquierda ves que todo lo que hacemos los arquitectos o diseñadores
[00:00:49] siempre parte de una idea. Después de esa idea,
[00:00:53] ves que hay una fase grande, no
[00:00:57] lineal, que va entre el intercambio de conocimiento,
[00:01:03] las tareas de diseño y la comunicación.
[00:01:05] Y luego se endereza otra vez hacia la fabricación y la visualización.
[00:01:10] Y este ciclo se repite X veces,
[00:01:13] pero, en general, es un enfoque no lineal.
[00:01:18] Donde el text to image suele ser muy aplicable
[00:01:24] es en las fases iniciales, cuando solo tienes una idea
[00:01:27] y quieres comunicar lo que estás pensando,
[00:01:29] pero todavía no necesitas mucho control.
[00:01:32] En general, ese control
[00:01:36] hace falta más en las fases posteriores.
[00:01:41] Pero para text to image, las fases iniciales son más adecuadas.
[00:01:46] Y la razón es que al principio no necesitamos ese control
[00:01:51] para cambiar cosas concretas,
[00:01:54] solo queremos comunicar
[00:01:56] una idea.
[00:01:59] Lo que vemos aquí es el modelo del doble diamante.
[00:02:01] Es un marco teórico que muestra que siempre empezamos en
[00:02:06] un punto concreto y después empezamos a divergir.
[00:02:11] Divergir significa abrirse, probar muchas cosas,
[00:02:15] ver qué opciones hay. Y en algún momento le damos la vuelta y
[00:02:20] empezamos a converger otra vez. El text to image es aplicable en la
[00:02:25] fase inicial, cuando queremos
[00:02:27] ver qué opciones tenemos y probar muchas cosas.
[00:02:32] Después, el image to image es más adecuado.
[00:02:36] Ese es el siguiente módulo, donde tendremos mucho más control que con text to image.
[00:02:42] Pero también es otra fase, así que por ahora nos vamos a centrar
[00:02:46] en text to image; más adelante, image to image, image to video, todo eso
[00:02:51] será más adecuado ahí.
[00:02:57] Como dije, esto iba a ser más práctico.
[00:03:00] Así que vamos a
[00:03:01] entrar directamente en Miro.
[00:03:08] Como ves, preparé el módulo 2, text to image.
[00:03:12] Por ahora está vacío. Pero cuando entres al tablero,
[00:03:16] estará lleno de imágenes para que puedas descargar los workflows.
[00:03:22] Te lo dejé preparado aquí en Comfy.
[00:03:27] Y, como viste en el módulo anterior,
[00:03:29] este es el workflow más básico posible.
[00:03:33] Empezamos con el checkpoint, después el prompt,
[00:03:35] el prompt negativo, la empty latent image,
[00:03:38] que define la proporción de salida de nuestra imagen.
[00:03:42] Después tenemos el KSampler,
[00:03:44] que era el fogón, ¿recuerdas?, donde ponemos los ajustes y afinamos un poco.
[00:03:50] Luego el decode, que vuelve a crear una imagen a partir de nuestro
[00:03:56] mundo de IA, y después el Save Image.
[00:04:02] Este tutorial lo voy a hacer con un prompt
[00:04:04] muy, muy simple: "concrete house in desert rocky landscape".
[00:04:10] El motivo es que este workflow que ves aquí es para un modelo
[00:04:17] que se llama DreamShaper, pero que en esencia es un modelo Stable Diffusion 1.5,
[00:04:23] lo que significa que a día de hoy es un modelo viejísimo.
[00:04:27] Salió en 2022. Así que
[00:04:31] visualmente va a decepcionar un poco,
[00:04:34] pero va bien para aprender lo básico.
[00:04:37] El prompt positivo ya lo vimos. El negativo es gato,
[00:04:42] perro y parque acuático. Después verás por qué.
[00:04:46] Como vimos, hacemos clic en "run".
[00:04:49] Esto activa todo lo que hay en el lienzo.
[00:04:53] Ves que el trabajo está en cola y la imagen se está generando.
[00:04:59] Como es un modelo
[00:05:01] superligero, fue rapidísimo. Lo que vemos es una casa de hormigón en el desierto
[00:05:07] y un paisaje rocoso. Claro que no hace falta que te explique que esto
[00:05:10] visualmente no es gran cosa.
[00:05:13] ¿Por qué te lo muestro? Para enseñarte todas las funciones de aquí.
[00:05:20] Si entramos en el KSampler y mantenemos el prompt,
[00:05:24] el prompt negativo, la empty latent image,
[00:05:26] lo dejamos todo intacto para saber que los cambios que vamos
[00:05:31] a ver no se deben al prompt,
[00:05:35] sino solo a los ajustes. Empecemos por arriba.
[00:05:40] Vemos la seed. Recuerda:
[00:05:42] es la posición de partida de los píxeles.
[00:05:44] Si hacemos clic aquí, podemos cambiar cómo gestiona el workflow
[00:05:51] la seed. Por ahora está en "fixed value".
[00:05:54] Como dice, cuando generamos una imagen,
[00:05:58] la seed siempre será la misma.
[00:05:59] Siempre partirá de la misma configuración de píxeles.
[00:06:04] Si pasamos a "randomize value",
[00:06:07] siempre será una seed completamente distinta,
[00:06:11] lo que significa...
[00:06:14] Vamos a hacer clic derecho aquí,
[00:06:17] duplicar, y te muestro cuál es el impacto.
[00:06:21] Así mantenemos nuestro workflow intacto.
[00:06:25] Y en el segundo hago clic aquí y elijo "randomize value".
[00:06:32] Por ahora no ha cambiado, porque dice que mezcla
[00:06:37] el valor al azar después de cada generación.
[00:06:40] Así que, por ahora, la seed sigue siendo
[00:06:43] la misma. Si hacemos clic en "run"...
[00:06:47] Vemos que la seed ya cambió.
[00:06:52] Ahora se está generando.
[00:07:03] Déjame mirar.
[00:07:07] Tuve que recargar la página porque mi internet iba un poco lento,
[00:07:11] pero, como ves, es una imagen distinta.
[00:07:15] También hizo una casa de hormigón en el desierto con un paisaje rocoso,
[00:07:20] pero es otra imagen. Si generamos otra vez,
[00:07:23] fíjate en esta parte:
[00:07:26] veremos que vuelve a cambiar la seed.
[00:07:30] Y cada vez que haces clic aquí,
[00:07:32] la seed cambia, porque elegimos "randomize value".
[00:07:37] Ahora, si elegimos "fixed value" y volvemos a ejecutar
[00:07:47] el workflow...
[00:07:55] Verás que genera una imagen distinta,
[00:07:57] pero ahora la seed está fija.
[00:08:01] Si hacemos clic en "run" otra vez, será la misma imagen, porque bloqueamos la seed,
[00:08:05] ¿sí? No cambió nada.
[00:08:09] Podemos hacer clic un millón de veces:
[00:08:11] siempre será exactamente la misma imagen.
[00:08:13] No cambiamos el prompt,
[00:08:16] no cambiamos el prompt negativo.
[00:08:20] Y ahora no vamos a cambiar la seed,
[00:08:24] porque sabemos que, si la cambiamos,
[00:08:26] será otra imagen. Si la mantenemos,
[00:08:29] siempre será más o menos parecida.
[00:08:31] Volvamos a nuestro ejemplo anterior.
[00:08:35] Para asegurarnos: si hago clic en "run",
[00:08:39] vuelve a salir la misma imagen de partida.
[00:08:41] Y voy a ir a Miro y
[00:08:51] poner esta imagen aquí para que podamos ver la comparación con los workflows
[00:08:57] y los modelos más nuevos.
[00:09:03] Bien.
[00:09:07] Ya sabemos qué hace la seed.
[00:09:08] Vamos a jugar con los steps. Los steps,
[00:09:10] recuerda, son las iteraciones que hace el modelo para crear la imagen.
[00:09:16] Si los ponemos en cinco,
[00:09:20] con el mismo prompt, la misma seed,
[00:09:21] todo igual, veremos que la imagen queda completamente sin terminar.
[00:09:28] ¿Por qué? Porque cortamos la generación.
[00:09:31] Todavía estaba generando y dijimos: para,
[00:09:33] para en cinco pasos. Claro,
[00:09:35] ves que el resultado no es bueno.
[00:09:37] Si ponemos 10 y lo repetimos,
[00:09:41] va a seguir el mismo camino de generación y se detendrá en 10.
[00:09:45] Y ya ves que es mucho mejor que antes.
[00:09:50] Si lo volvemos a poner en veinte...
[00:09:56] Otra vez, es exactamente igual que antes.
[00:09:59] Así que es determinista.
[00:10:01] No es aleatorio. Puedes rastrear por qué pasó lo que pasó.
[00:10:05] El CFG es la cantidad de creatividad.
[00:10:09] Si pasas el cursor por aquí, también te dice qué es.
[00:10:13] Así que, si no te acuerdas o no lo sabes,
[00:10:16] pregúntale a tu experto en Comfy o simplemente pasa el cursor
[00:10:22] por encima del valor.
[00:10:26] Si ponemos esto en uno...
[00:10:30] Veamos qué pasa.
[00:10:35] Queda completamente crudo, porque los valores más altos dan
[00:10:39] imágenes que se ajustan más al prompt,
[00:10:42] lo que significa que, si lo ponemos muy bajo,
[00:10:44] el modelo puede hacer lo que quiera.
[00:10:46] Tiene mucha libertad, pero en este caso no es suficiente.
[00:10:50] Si lo ponemos en 20...
[00:10:57] Intenta hacer tan literalmente lo que dice el prompt que sobresatura
[00:11:04] y machaca los píxeles. Y por eso, para este workflow,
[00:11:08] 8 es lo mejor. ¿Cómo lo sé?
[00:11:12] Es muy simple. Voy al prompt coach,
[00:11:19] o mejor al otro: voy al experto en Comfy y entonces,
[00:11:25] por ejemplo...
[00:11:27] Digamos que tenemos una imagen muy mala,
[00:11:31] así que lo ponemos en uno.
[00:11:38] Haría una captura de esta página.
[00:11:44] Tenemos la captura y entonces la pegaría aquí y
[00:11:48] diría: por qué
[00:11:52] mi imagen de salida no es buena.
[00:11:57] Ni siquiera hace falta que escribas perfecto.
[00:12:03] Y en más o menos un minuto me dirá:
[00:12:07] vale, veo que estás usando un workflow de Stable Diffusion 1.5.
[00:12:12] Está intentando diagnosticarlo.
[00:12:14] Y después dirá: el CFG está demasiado bajo,
[00:12:17] ponlo en 8, por ejemplo. Dicho esto,
[00:12:22] vamos al siguiente workflow para ver el impacto de uno distinto.
[00:12:28] Ya lo tengo preparado aquí.
[00:12:30] Y lo que ves es que el workflow en sí no es distinto.
[00:12:33] Lo único que cambia es el modelo.
[00:12:36] Este es un modelo Stable Diffusion XL,
[00:12:39] y lo ves aquí.
[00:12:42] También puedes ir a Templates y al filtro de modelos.
[00:12:48] Haces clic en SDXL y ahí tienes, por ejemplo, "SDXL simple".
[00:12:53] Este no es un workflow simple,
[00:12:56] así que abruma un poco.
[00:12:58] Vamos a cerrarlo.
[00:13:02] También puedes probar este. Aquí ves que ya es, si
[00:13:08] borramos esto...
[00:13:12] Ya es más simple. Pero, por ahora,
[00:13:14] para este tutorial, yo me quedaría con los que te doy, porque son
[00:13:18] los más puros. Es la esencia y nada más.
[00:13:23] Si tomamos el mismo prompt,
[00:13:26] etc., todo igual, y lo ejecutamos...
[00:13:35] Veremos que esta imagen ya es visualmente mucho más interesante que
[00:13:41] la anterior. No hace falta que lo explique todo otra vez, porque es
[00:13:47] lo mismo. Así que voy a dejar esta imagen
[00:13:54] aquí para que puedas revisarla.
[00:13:56] Después vamos a pasar a FLUX.1.
[00:14:03] De nuevo, te preparé los workflows.
[00:14:08] Si lo arrastramos aquí, ves que este workflow es muy distinto.
[00:14:13] Cerremos este archivo markdown.
[00:14:15] Y aquí tenemos el mismo prompt:
[00:14:18] "concrete house in desert, rocky landscape".
[00:14:20] Como vemos, la resolución está puesta en 1024 por 1024.
[00:14:26] Esto es porque el modelo FLUX está entrenado con imágenes de más resolución.
[00:14:32] Así que funciona mejor a 1024
[00:14:36] que a 512 por 512.
[00:14:38] Pero, en general, puedes experimentar con esto.
[00:14:42] Si entramos en el subgraph, vemos que este es el workflow real que hay detrás
[00:14:48] del subgraph. Pero, por ahora, si hacemos clic en "run",
[00:14:53] veremos el aumento de calidad de imagen respecto a los modelos antiguos.
[00:15:03] Aquí vemos cómo se va generando.
[00:15:10] Como ves, esto es otra vez mucho más interesante.
[00:15:13] Quizá, si haces mucho zoom, sigue estando pixelado,
[00:15:18] no es superrealista, yo diría,
[00:15:21] pero, en general, es una buena imagen.
[00:15:30] Además, fíjate: es una resolución mayor,
[00:15:32] así que tengo que reducirla un poco.
[00:15:35] Esto era solo la preparación, porque estamos llegando a FLUX.2.
[00:15:41] El modelo que vamos a usar se llama klein 9B.
[00:15:45] Otra vez, puedes usar el workflow que dejo aquí,
[00:15:49] o te vas al apartado de plantillas
[00:15:55] y buscas FLUX.
[00:16:00] Klein... Bueno, eso fue sin querer.
[00:16:09] Todos los workflows nativos de Comfy
[00:16:12] los encuentras aquí. Y ves la diferencia entre modelos.
[00:16:15] Esto es FLUX.2. Esta es la familia de modelos.
[00:16:19] Después tenemos klein 4B. Klein es solo una forma de decir que es
[00:16:26] un archivo pequeño, o sea, que no carga tu computadora como los otros.
[00:16:30] Y está entrenado con 4.000 millones de parámetros.
[00:16:33] Aquí vemos klein
[00:16:36] 9B, que es el que vamos a usar.
[00:16:38] Está entrenado con 9.000 millones. Es un modelo más inteligente,
[00:16:41] pero también más pesado. Si hacemos clic aquí,
[00:16:45] vemos que este workflow tiene
[00:16:51] un aspecto bastante básico. Si entramos en el subgraph,
[00:16:54] no es nada del otro mundo, y no tienes que cambiar nada aquí dentro,
[00:16:58] así que quédate con este. Bien,
[00:17:03] voy a traer mi plantilla.
[00:17:09] Solo para mantener la coherencia.
[00:17:15] "Concrete house in desert rocky landscape",
[00:17:18] 1024 por 1024 píxeles, nada especial.
[00:17:22] Si hacemos clic en "run", verás que esta calidad de salida,
[00:17:25] arquitectónica, visual, todo, es otra vez mucho más interesante que
[00:17:31] las anteriores. Pero también tarda mucho más en generarse, porque es
[00:17:36] un modelo más pesado, más nuevo,
[00:17:38] entrenado con muchas más imágenes que los antiguos.
[00:17:43] O sea, esta imagen está muy bien.
[00:17:46] Así que perfecto. Otra vez, la dejo aquí.
[00:17:48] ...
[00:18:07] Esta fue una demostración muy rápida de los modelos antiguos frente a los nuevos.
[00:18:14] Y ves que hay un motivo por el que estos modelos nuevos
[00:18:18] son mucho más interesantes de usar.
[00:18:19] Estos, digamos los dos primeros,
[00:18:22] no son interesantes hoy en día porque les falta calidad.
[00:18:27] Yo diría que FLUX.1 en algunos casos todavía puede interesar,
[00:18:31] pero la mayoría de las veces, FLUX.2,
[00:18:33] sobre todo este,
[00:18:35] es de lejos la mejor opción para ti.
[00:18:37] Y por eso recomiendo mucho usar Comfy Cloud, porque si no
[00:18:42] seguramente tardaría muchísimo generarlo en local.
[00:18:48] Ahora hay un par de cosas que podríamos hacer aquí.
[00:18:52] Una es iterar mucho sobre el prompt.
[00:18:55] Para eso irías a tu experto en Comfy o a tu prompt coach.
[00:19:01] Te lo muestro.
[00:19:04] Fui al prompt coach que configuramos juntos,
[00:19:08] que en general eran solo estas instrucciones,
[00:19:12] tal como las encuentras en Miro.
[00:19:17] En "prompt coach setup", simplemente copié y pegué esto
[00:19:23] en mi LLM favorito, que es Claude.
[00:19:25] Lo pego aquí. Escribo "start".
[00:19:29] Me preguntará para qué modelo estoy intentando hacer algo.
[00:19:34] Y
[00:19:37] también qué quiero mejorar. Así que diré: "concrete house in desert,
[00:19:42] rocky landscape", y el modelo es FLUX.2 klein.
[00:19:46] Y si vamos...
[00:19:51] Piensa en todo lo que sabe,
[00:19:53] claro, nada especial.
[00:20:00] Aquí me dio tres opciones:
[00:20:02] referencia a Tadao Ando, Rick Joy
[00:20:05] o Kogan. Yo diría, por ejemplo, la cero uno.
[00:20:14] Me gusta Tadao Ando, y me dará algo así.
[00:20:19] Pero específicamente para FLUX.2.
[00:20:24] Y como ves aquí, para FLUX.2
[00:20:26] este prompt coach sabe que FLUX.2 entiende el JSON prompting.
[00:20:32] Y, como vimos antes, el JSON prompting es solo la forma
[00:20:35] en que esto está organizado.
[00:20:40] La información, estructurada así.
[00:20:44] Yo copiaría esto.
[00:20:51] Lo haría un poco más grande y después pegaría el prompt JSON aquí.
[00:20:57] ¿Qué va a pasar cuando generemos esto?
[00:21:00] No he leído el prompt entero.
[00:21:02] Se está trabando un poco.
[00:21:05] Así que la verdad es que no sé qué va a generar.
[00:21:09] Veo que tomó algunas paletas de color.
[00:21:14] Hizo este volumen de aspecto muy básico.
[00:21:22] La ventaja de este prompt JSON es que, si quiero
[00:21:28] cambiar algo de la escena,
[00:21:30] lo haría aquí. Si quiero cambiar algo de la descripción,
[00:21:34] está aquí. Si quiero cambiar el estilo o los colores,
[00:21:39] la iluminación, el ambiente, el fondo,
[00:21:41] la composición, todo, sabría exactamente dónde tengo que tocar el prompt.
[00:21:48] Bien, eso es lo que puedes hacer aquí.
[00:21:51] Si tienes una idea clara de lo que quieres,
[00:21:54] puedes cambiar el prompt de forma casi quirúrgica.
[00:22:03] Ahora bien, el prompt coach tiende a complicarlo demasiado.
[00:22:09] Así que yo le diría: hazlo de máximo cincuenta palabras,
[00:22:16] sin estructura JSON.
[00:22:22] Para mantenerlo más simple, porque en esta fase inicial de diseño
[00:22:26] no sé cuáles son las restricciones.
[00:22:34] Bien, me dio este prompt, "deep focus".
[00:22:37] Probemos este.
[00:22:44] Y veamos qué pasa.
[00:22:47] Claro, esta es una idea bastante básica: una estructura de hormigón en
[00:22:53] el desierto. Puedes ser mucho más experimental con esto e intentar
[00:22:59] llevar los límites más lejos.
[00:23:06] Como ves, las cualidades visuales son bastante interesantes con
[00:23:12] el sol y el fondo.
[00:23:14] Me gusta mucho la estética visual de aquí.
[00:23:17] Ahora, la siguiente parte de la presentación.
[00:23:25] Lo cambio así.
[00:23:31] Bien, es el workflow de FLUX.2 klein,
[00:23:37] el impacto de los tipos de prompt que acabamos de ver.
[00:23:39] Y otra cosa que voy a añadir es mostrarte
[00:23:44] cómo implementar un LoRA en este workflow.
[00:23:50] Y así ves el impacto real del LoRA mientras generamos imágenes.
[00:23:59] Bien, vimos cómo hacer estas imágenes
[00:24:03] interesantes solo a partir de texto.
[00:24:08] Ahora vamos a avanzar hacia implementar un LoRA.
[00:24:11] Vamos al workflow y volvemos
[00:24:17] al que teníamos antes, que era
[00:24:25] este. Lo voy a dejar en
[00:24:31] la posición de partida que tenía antes para que lo reconozcas.
[00:24:38] Como ves, a veces va un poco lento,
[00:24:43] también porque estás usando un servicio en la nube,
[00:24:46] así que a veces la conexión tarda unos segundos.
[00:24:48] En general es rapidísimo.
[00:24:51] Si va lento, si no genera y no da ningún código de error,
[00:24:56] puedes refrescar y probablemente se arregle,
[00:25:01] aunque diga esto. Veamos qué pasa.
[00:25:11] Lo refresqué y tenemos esta imagen.
[00:25:16] Ahora vamos a añadir un LoRA a este workflow.
[00:25:20] Entramos en el subgraph; esto va a ser un poco más técnico,
[00:25:23] pero sigue mis pasos. Lo que hacemos es ponernos aquí arriba y hacer doble clic.
[00:25:29] Vamos a escribir
[00:25:34] "load LoRA". Y, como ves aquí en el lado derecho,
[00:25:40] es el logo de Comfy, o sea, es un nodo oficial que hizo el propio Comfy,
[00:25:45] así que funciona muy bien. A veces ves otros nombres.
[00:25:48] Son otras personas que hacen
[00:25:53] sus propios nodos, y después Comfy los verifica.
[00:25:58] Son todos seguros, así que no tienes que preocuparte.
[00:26:02] Pero, por ahora, haz clic en este primero.
[00:26:06] Después puedes arrastrarlo donde quieras. Para este
[00:26:10] workflow, yo lo pondría arriba.
[00:26:13] Desapareció. Probemos otra vez.
[00:26:19] Lo pegamos aquí. Ahora,
[00:26:22] claro, como no está enlazado al workflow,
[00:26:24] no va a funcionar. Tu pregunta puede ser: ¿dónde lo enlazo
[00:26:30] en medio de todo esto sin romper el workflow?
[00:26:33] Es supersimple. Ves que necesitamos una entrada de modelo y tenemos
[00:26:39] una salida de modelo. Si buscas dónde hay
[00:26:44] una salida que diga "model", solo está esta.
[00:26:48] Así que, digamos que quieres conectarlo.
[00:26:50] Solo hay una manera de conectarlo,
[00:26:53] y es esta. Digamos que quiero conectarlo aquí.
[00:26:57] No se puede. Se pone gris porque es otra entrada,
[00:27:02] ¿sí? Es otro tipo de información.
[00:27:04] Así que no te puedes equivocar, porque esta es la única forma de enlazarlo.
[00:27:09] Digamos que quiero enlazarlo aquí y lo suelto:
[00:27:14] no pasa nada.
[00:27:17] También lo puedo tomar de aquí y enlazarlo.
[00:27:20] Ves que este está enlazado, pero detrás,
[00:27:23] detrás de este, si lo muevo,
[00:27:27] todavía ves que este modelo está enlazado al siguiente.
[00:27:32] Así que, si haces esto, se salta y ahora esta cadena queda conectada.
[00:27:41] No te intimides, parece más difícil de lo que es.
[00:27:44] Ahora vemos que el modelo está enlazado,
[00:27:50] o que el nodo está enlazado dentro del workflow.
[00:27:54] Lo que tenemos que hacer ahora es importar un LoRA a nuestra cuenta para activarlo.
[00:28:00] Cómo lo vamos a hacer
[00:28:02] está bien explicado en Miro.
[00:28:07] Es este documento, un PDF
[00:28:11] hecho por Ismail Salid, así que un gran agradecimiento para él.
[00:28:14] Si no queda claro, puedes seguir este
[00:28:18] y así sabrás cómo importar modelos a tu cuenta
[00:28:25] de Comfy Cloud. Pero lo vamos a hacer juntos.
[00:28:28] Esto es solo un respaldo por si no queda claro:
[00:28:31] síguelo aquí. Vas al sitio web llamado Hugging Face.
[00:28:39] Como ves aquí arriba, dejé el enlace para que puedas
[00:28:44] usarlo si no queda claro. Te creas una cuenta nueva,
[00:28:49] o sea, haces clic en "sign up".
[00:28:52] Cuando ya tienes tu cuenta,
[00:28:54] la ves aquí arriba. Yo me hice una nueva aquí.
[00:28:57] Hay muchísima información en este sitio web,
[00:29:01] y Hugging Face, en esencia,
[00:29:02] es la mayor plataforma de IA. Puedes venir aquí, hacer clic en "models",
[00:29:07] y encontrarás muchísimos modelos open source,
[00:29:10] y LoRA también. Es supertécnico en cierto modo,
[00:29:16] pero nosotros lo vamos a usar para buscar,
[00:29:20] por ejemplo, FLUX.2.
[00:29:24] Si haces clic aquí...
[00:29:28] Aquí podrías descargar FLUX.2 klein 9B,
[00:29:32] y no hace falta que lo hagas, porque Comfy Cloud ya lo hizo por nosotros.
[00:29:37] Pero para quien intente ejecutarlo en local,
[00:29:40] o sea, usarlo en su propia computadora,
[00:29:43] entonces sí tendría que descargarlo:
[00:29:45] este archivo enorme de aquí. Pero, por ahora,
[00:29:48] no hace falta. Lo que queremos hacer, si volvemos, es
[00:29:55] poder cargar un LoRA
[00:29:57] en nuestro workflow. Los pasos que hay que dar son los siguientes.
[00:30:05] Lo primero es ir a Black Forest Labs, FLUX.2 klein 9B.
[00:30:11] Si no sabes cómo,
[00:30:12] haz clic aquí: FLUX.2 klein.
[00:30:19] Y aparecerá arriba. Haces clic aquí,
[00:30:23] y esta es la ficha del modelo.
[00:30:26] Tiene mucha información sobre el modelo:
[00:30:29] cómo ejecutarlo, limitaciones, documentación.
[00:30:32] Si te interesa, puedes mirarlo aquí.
[00:30:34] Lo que tenemos que hacer es clic en "agree and access repository".
[00:30:42] "Files and versions". Esto es solo con fines educativos,
[00:30:46] para enseñarte cómo se hace. Está vinculado a
[00:30:53] Black Forest Labs, así que también ves cuántas descargas
[00:30:59] tuvieron el mes pasado, etc. Ahora decimos que aceptamos
[00:31:05] los términos de FLUX, o de Black Forest Labs.
[00:31:09] Así que lo más difícil ya está hecho.
[00:31:11] Ahora vamos aquí, al lado derecho,
[00:31:14] vamos a "New Model",
[00:31:18] le ponemos un nombre.
[00:31:21] El nombre depende un poco de cuál estés usando.
[00:31:24] En Miro he preparado algo.
[00:31:29] En este curso va incluido un LoRA.
[00:31:34] Se llama Rhino to Image LoRA Basic.
[00:31:37] Es un archivo safetensors que vas a encontrar en la carpeta que recibes
[00:31:43] del curso. Ahora bien, como esto es mi trabajo a tiempo completo
[00:31:47] y pruebo muchísimos LoRA,
[00:31:49] hago muchos yo mismo.
[00:31:51] También hice un LoRA premium que te voy a enseñar.
[00:31:56] No tienes que comprarlo, pero si te interesa,
[00:32:00] lo encuentras en mi web y te lo muestro rápidamente aquí.
[00:32:05] Es una web muy, muy sencilla.
[00:32:08] Lo único que vas a encontrar son mis workflows.
[00:32:13] Y es este.
[00:32:17] Aquí, en el lado derecho, como ves,
[00:32:19] puse un descuento muy grande.
[00:32:22] Normalmente son 100, ahora van a ser 49.
[00:32:25] Y creo que vale la pena porque, si haces clic aquí,
[00:32:31] verás el antes y el después.
[00:32:33] Esto es parte del segundo... perdón, del tercer módulo,
[00:32:38] que es image to image, pero ves la calidad de este LoRA.
[00:32:42] Es buenísima, y es porque lo entrené durante mucho tiempo. Puedes
[00:32:47] pasar de esto
[00:32:51] a esto, pero también podemos usarlo para text to image.
[00:32:54] Si te interesa, haz clic aquí, en "add to cart".
[00:32:57] Este descuento solo estará mientras dure el concurso.
[00:33:02] Después, el descuento desaparece.
[00:33:08] Cuál uses da igual.
[00:33:11] Puedes seguir los pasos con los dos,
[00:33:13] tanto con el gratuito como con el premium.
[00:33:16] La diferencia es solo la calidad visual: la del premium
[00:33:22] es mejor, claro.
[00:33:25] Así que tomas ese archivo. En mi caso,
[00:33:28] va a ser el premium.
[00:33:33] Le pones un nombre, el que sea,
[00:33:35] eso es...
[00:33:38] Tomo este.
[00:33:44] Da igual cómo lo llames,
[00:33:45] lo que quieras. Lo dejamos en privado.
[00:33:49] No hacemos clic en "public", porque si no quedaría expuesto
[00:33:52] a todo el mundo. Hacemos clic en "private",
[00:33:55] esto es importantísimo. Y después hacemos clic en "create model".
[00:33:59] Y ya hemos creado un modelo nuevo.
[00:34:02] Como todavía no hemos subido nada,
[00:34:04] está vacío. Vamos a "files and versions" y vemos que no hay nada aún.
[00:34:09] Solo hay
[00:34:11] un commit inicial y algunos atributos de git,
[00:34:13] pero está vacío. El siguiente paso es hacer clic en "contribute", a la derecha,
[00:34:19] y aquí podemos hacer clic en "upload files".
[00:34:23] En la carpeta que recibiste está el gratuito,
[00:34:28] se verá muy claro dónde está,
[00:34:30] o en mi web tienes el premium.
[00:34:34] Así que
[00:34:38] lo arrastras aquí dentro.
[00:34:40] Como ves, Rhino to Image LoRA premium ya está ahí.
[00:34:45] Y después hacemos clic en "commit changes".
[00:34:52] Como ves, se está subiendo:
[00:34:54] subimos el archivo del LoRA,
[00:34:57] que es un safetensors, a nuestra cuenta de Hugging Face.
[00:35:01] Y ahora vemos que está aquí.
[00:35:03] Se llama Thomas Rhino to Image LoRA Premium.
[00:35:07] Y este es el archivo en sí.
[00:35:10] Como ves, son unos 127 megabytes.
[00:35:14] Puedes volver a descargarlo desde aquí,
[00:35:16] pero, claro, no hace falta.
[00:35:20] ¿Y cuál es el siguiente paso?
[00:35:24] Otra vez, hacer clic en la cuenta,
[00:35:27] y ahora tenemos que hacer clic en "access tokens", porque tenemos que dar
[00:35:32] a nuestra cuenta de Comfy Cloud acceso a este repositorio.
[00:35:37] Hacemos clic en "access tokens", "create new token".
[00:35:44] Le pones un nombre, pero antes de ponerle el nombre,
[00:35:47] tenemos que hacer clic en "read". No "fine-grained" ni "write",
[00:35:52] solo "read". Esto significa que el repositorio de Hugging Face solo da acceso
[00:35:59] a leer nuestros archivos, nada más.
[00:36:01] Le ponemos un nombre, por ejemplo "comfycloud";
[00:36:07] da igual cuál sea el nombre,
[00:36:09] y haces clic en "create token".
[00:36:12] Ahora bien,
[00:36:13] este token que ves aquí tienes que mantenerlo privado.
[00:36:18] Como esta es una cuenta falsa, da igual que tú veas cuál es,
[00:36:23] pero es importantísimo que tú lo mantengas privado, porque es
[00:36:27] un token que da acceso a tu cuenta,
[00:36:33] a todo lo que hayas subido. Si se publica en internet,
[00:36:38] otras personas pueden acceder. Es como una contraseña.
[00:36:42] Llamémosle contraseña. Pero, por ahora, da igual que lo veas en mi caso.
[00:36:48] Yo haría clic en "copy".
[00:36:54] Después vuelvo a Comfy, a Comfy Cloud,
[00:36:58] voy a ajustes y aquí ves "secrets".
[00:37:03] Ves que yo ya lo he hecho,
[00:37:07] claro, porque si no, no podría dar este curso.
[00:37:11] Yo haría clic en "add secrets".
[00:37:17] Le pones un nombre y aquí pegas tu nuevo valor, así,
[00:37:25] y haces clic en "save". El proveedor:
[00:37:28] antes de hacer clic en "save", tienes que seleccionar Hugging Face.
[00:37:33] Eso es importantísimo. Yo no puedo hacerlo porque ya tengo
[00:37:37] mi token seleccionado, pero haz clic en Hugging Face,
[00:37:40] ponle un nombre cualquiera y haz clic en "save".
[00:37:48] Después volvemos a Comfy y ya casi hemos terminado.
[00:37:52] Esto solo tienes que hacerlo una vez;
[00:37:55] después es mucho más simple.
[00:37:57] Volvemos a nuestra cuenta. Hacemos clic en nuestra cuenta.
[00:38:02] Aquí vemos el modelo que acabamos de subir,
[00:38:06] el LoRA. Si lo pruebas primero con el básico
[00:38:12] y después con el premium,
[00:38:14] solo tienes que repetir los pasos dos veces;
[00:38:16] entonces,
[00:38:17] claro, aquí habrá dos modelos.
[00:38:19] Tiene sentido. No es nada del otro mundo.
[00:38:24] Vamos a "files and versions", y aquí
[00:38:29] tienes que hacer clic derecho en el botón de descarga,
[00:38:34] ¿sí? No doble clic. También puedes hacerlo aquí,
[00:38:39] pero tiene que ser clic derecho, o en este botón o aquí,
[00:38:43] y después haces clic en "copy link address".
[00:38:47] Bien. Hacemos clic aquí,
[00:38:52] dice "link address".
[00:38:53] ¿Copiado?
[00:38:57] Por última vez, vamos a Comfy.
[00:38:59] ...
[00:39:04] Hacemos clic en "model library", "import",
[00:39:10] y aquí pegamos el enlace.
[00:39:14] Si hacemos clic en "continue", en mi caso no va a funcionar,
[00:39:18] pero a ti sí te va a funcionar.
[00:39:21] Si algo no funciona, puede pasar,
[00:39:26] quizá te saltaste un paso o un detalle.
[00:39:28] No te preocupes, ve a
[00:39:35] este documento: aquí está explicado cada paso que dimos,
[00:39:42] de otra manera.
[00:39:45] Solo sigue los pasos. Y si aun así no funciona,
[00:39:52] vuelve a ver este video. Y si todavía no funciona,
[00:39:55] usa tu experto en Comfy, porque te va a guiar por el proceso.
[00:40:01] Bien, si hiciste todo esto correctamente y refrescas la página,
[00:40:07] puedes hacer clic en "load LoRA".
[00:40:12] Vas a "my models" y ahí ya estará disponible este LoRA.
[00:40:17] En mi caso tiene otro nombre porque esto fue durante las pruebas.
[00:40:24] Y ahora el LoRA está enlazado a nuestro workflow.
[00:40:26] Entiendo que puedan parecer muchos pasos.
[00:40:29] Parece supertécnico,
[00:40:33] pero solo sigue los pasos sencillos que di yo,
[00:40:35] y vas a poder enlazar el LoRA en este workflow
[00:40:40] de text to image. Veamos cuál es el impacto.
[00:40:44] Hacemos clic en "run". Y ahora el prompt,
[00:40:48] todo, sigue igual, solo estamos añadiendo el LoRA sobre nuestro
[00:40:55] modelo base, que es FLUX.2, y verás cuál es el impacto en cuanto
[00:41:01] al estilo.
[00:41:05] Bien, el workflow ya cargó y este es el resultado.
[00:41:08] Ahora te puedes preguntar: ¿cuál es la gran diferencia?
[00:41:12] Porque, claro, vemos que el edificio es distinto,
[00:41:14] pero ahora hablo solo de las características visuales.
[00:41:18] Así que lo voy a añadir
[00:41:23] a Miro para ponerlas una al lado de la otra.
[00:41:31] Y esto es con la fuerza del LoRA al 100 %.
[00:41:35] La diferencia es que las dos
[00:41:39] son imágenes interesantes. La única diferencia es que esta, la de
[00:41:45] la derecha, está influida por este ligero grano analógico,
[00:41:49] y eso es porque mi LoRA está entrenado con fotografía de arquitectura de 35 mm.
[00:41:55] Así que puedes seguir usando el básico,
[00:41:59] no hace falta que uses un LoRA.
[00:42:01] Pero, si te interesa, lo encuentras aquí.
[00:42:07] Entramos en el workflow y entramos en el subgraph.
[00:42:10] Verás que podemos jugar con la fuerza.
[00:42:14] Si la ponemos en 0,5, pulsamos enter
[00:42:18] y hacemos clic en "run", ahora este LoRA solo se activará al 50 %,
[00:42:24] así que no será tan dominante a la hora de cambiar la imagen como
[00:42:29] lo fue antes. Otra vez,
[00:42:32] puedes ver cómo se genera la imagen,
[00:42:35] cómo el modelo se va
[00:42:37] corrigiendo para darte una imagen buena.
[00:42:42] Y este es el resultado. Es interesante porque,
[00:42:48] si lo comparamos aquí en Miro,
[00:42:51] lo voy a poner aquí.
[00:42:57] Así.
[00:43:13] La de la izquierda es sin LoRA,
[00:43:15] esta es con el cincuenta por ciento,
[00:43:17] y esta es con el cien por cien.
[00:43:24] Pues eso es todo. Ahora puedes buscar LoRA nuevos,
[00:43:27] puedes encontrar otros distintos, y cada,
[00:43:30] cada LoRA tiene un impacto diferente.
[00:43:33] Y te preguntarás por qué soy tan fan
[00:43:37] de este LoRA. Es porque en el siguiente módulo
[00:43:43] veremos que podemos convertir esta imagen básica de Rhino en este render
[00:43:50] de alta resolución
[00:43:53] con solo dar una imagen de referencia de un bloque de mármol.
[00:43:58] Y aquí es donde el LoRA
[00:44:02] resulta realmente útil. Porque, si no lo usas,
[00:44:05] queda un poco plástico.
[00:44:07] Te doy un ejemplo.
[00:44:12] Por ejemplo, esto es cuando no usas un LoRA.
[00:44:17] Es un poco plástico, saturado,
[00:44:20] superduro de contraste.
[00:44:23] Y el mismo workflow, el mismo prompt,
[00:44:25] pero con LoRA es este. Es mucho más suave,
[00:44:29] es mucho más sutil arquitectónicamente,
[00:44:34] es mucho más interesante, en mi opinión.
[00:44:37] Así que échale un vistazo.
[00:44:41] También viene Spectrum.
[00:44:44] Explicaré qué es en el siguiente módulo,
[00:44:48] y también otro LoRA distinto. Pero para
[00:44:52] el curso he dado un cincuenta por ciento de descuento mientras
[00:44:57] dure el concurso.
[00:45:03] Volvamos al text to image. Vimos cuatro modelos:
[00:45:08] Stable Diffusion 1.5,
[00:45:10] Stable Diffusion XL, FLUX.1 y FLUX.2.
[00:45:14] Hemos visto cómo usar un LoRA,
[00:45:19] que es un proceso con muchos pasos distintos,
[00:45:25] pero solo tienes que hacerlo una vez,
[00:45:26] y después tu LoRA está en tu cuenta de Comfy y puedes acceder siempre
[00:45:32] muy fácilmente. Lo siguiente que podríamos hacer es jugar un poco más con
[00:45:39] el prompt coach. Si tienes una idea concreta,
[00:45:42] pásala siempre primero por el prompt coach,
[00:45:44] dale vueltas a tus ideas con el bot de IA,
[00:45:49] y después copia, pega y pruébalo.
[00:45:53] Juega un poco con los parámetros.
[00:45:56] Si no funciona, vuelve a los ajustes anteriores,
[00:46:00] y siempre puedes descargar
[00:46:02] esta plantilla de aquí. Descárgala.
[00:46:10] Mm.
[00:46:13] Entra en Comfy.
[00:46:18] Arrastra y suelta, y tendrás exactamente el mismo prompt, ajustes y seed que yo.
[00:46:28] Bien, esto es el final del módulo dos,
[00:46:31] text to image. En el lado derecho del tablero de Miro,
[00:46:36] del todo aquí, dejé recursos extra para quien tenga interés.
[00:46:41] Puedes hacer clic aquí,
[00:46:44] descargar la imagen, y verás el workflow entero con el prompt,
[00:46:50] etc. Porque esto es algo que yo usaba para probar ideas,
[00:46:56] como por ejemplo esta torre.
[00:46:59] Así que échale un vistazo, es un extra del curso.
[00:47:07] Gracias, y nos vemos en el módulo tres.
