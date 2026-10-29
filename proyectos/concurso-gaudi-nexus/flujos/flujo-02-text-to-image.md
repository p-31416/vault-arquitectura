---
tipo: flujo-curso
proyecto: concurso-gaudi-nexus
modulo: 2
slug: text-to-image
titulo_curso: "Text-to-Image"
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [mvp_04, comfyui, curso-ai-gaudi, modulo-2, text-to-image, gaudi-nexus]
idioma: es
---

# Módulo 2 — Text-to-Image (flujo del curso)

> Ficha de flujo del módulo 2 del curso AI×Gaudí, transcrita del video. Fuente verbatim: [[raw/yt/transcripts/2026-10-21_mux-text-to-image.es|transcripción ES]] · [[raw/yt/transcripts/2026-10-21_mux-text-to-image.en|EN]] · plan: [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro de workflows adapted]].

## Ficha

| Campo | Valor |
|-------|-------|
| **Duración de la pista de subtítulos** | 00:47:07 → 00:47:09 (≈ 47 min) `[00:47:07]` |
| **Idioma** | Video en inglés (curso "seven modules in English with subtitles"); transcripción en español disponible + versión EN para resolver ambigüedades |
| **Profesor** | No se nombra en el video. El presentador habla desde su propia web de workflows y como autor del LoRA premium que entrenó él mismo `[00:31:47–00:32:05]`; el vault lo identifica como **Thomas Nelissen (Davis AI)** — ver [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|extraccion-material-curso-ai-gaudi]]. En el video se acredita a **Ismail Salid** por el PDF de importación de modelos a Comfy Cloud `[00:28:07–00:28:11]` |
| **Entorno** | Comfy Cloud (nodos nativos de Comfy + plantillas oficiales) `[00:03:22]` |
| **Tema (1)** | Comparativa práctica de generación de imágenes desde texto con el mismo prompt sobre cuatro modelos: SD 1.5 (DreamShaper), SDXL, FLUX.1 y FLUX.2 klein 9B. |
| **Tema (2)** | Aporte visual real de un LoRA (rhino-to-image) al 50 % y al 100 %, con el proceso completo de importación desde Hugging Face hasta la Model Library de Comfy Cloud. |

---

## Objetivo del módulo

Generar imágenes desde texto en ComfyUI con un prompt constante y ver, de forma controlada, cuánto aporta cada modelo (SD 1.5 → SDXL → FLUX.1 → FLUX.2 klein 9B) y cuánto aporta un LoRA de estilo al 50 % y al 100 % `[00:03:03–00:03:35]` `[00:18:07–00:18:35]` `[00:43:13–00:43:17]`.

---

## El flujo, paso a paso

| # | Acción | Nodo / herramienta (nombre EXACTO en ComfyUI) | Valores que dice el video | Prompt / fórmula | Timestamp |
|---|--------|-------------------------------------------|---------------------------|------------------|-----------|
| 1 | Descargar los workflows del módulo desde el tablero de cursos | Miro (tablero del curso, frame "módulo 2, text to image") | Al entrar al tablero está lleno de imágenes para descargar los workflows | — | `[00:03:08–00:03:16]` |
| 2 | Abrir el workflow de trabajo en Comfy Cloud | Comfy Cloud | "Te lo dejé preparado aquí en Comfy" | — | `[00:03:22]` |
| 3 | Reconocer la cadena del workflow más básico | Checkpoint → Prompt → Prompt negativo → Empty Latent Image → KSampler → Decode → Save Image | El `Empty Latent Image` define la proporción de salida; el `KSampler` es "el fogón" donde van los ajustes; el `Decode` vuelve a crear la imagen | — | `[00:03:29–00:03:56]` |
| 4 | Primera corrida (modelo DreamShaper = SD 1.5) | Run | Modelo superligero → "rapidísimo" | Positivo: `concrete house in desert rocky landscape` · Negativo: `cat, dog, waterpark` | `[00:04:02–00:05:13]` |
| 5 | Probar la seed | `KSampler` → control de seed (`fixed value` / `randomize value`) | `fixed value` = misma seed siempre → misma imagen exacta; `randomize value` = seed nueva en cada corrida. Duplica el nodo para comparar los dos comportamientos | — | `[00:05:40–00:08:16]` |
| 6 | Probar los steps | `KSampler` → `steps` | 5 → imagen "completamente sin terminar" (generación cortada); 10 → mucho mejor; 20 → idéntica a la de 10. Es determinista: "puedes rastrear por qué pasó lo que pasó" | Mismo prompt + misma seed en los tres casos | `[00:09:08–00:10:01]` |
| 7 | Probar el CFG | `KSampler` → `cfg` | 1 → "completamente crudo"; 8 → mejor para este workflow; 20 → "sobresatura y machaca los píxeles". El CFG es "la cantidad de creatividad" | — | `[00:10:05–00:11:08]` |
| 8 | Diagnosticar con captura de pantalla | Comfy expert (el "otro" asistente, distinto del prompt coach) | Respuesta tipo: "el CFG está demasiado bajo, ponlo en 8" | Pregunta: "por qué mi imagen de salida no es buena" | `[00:11:12–00:12:17]` |
| 9 | Cambiar solo el modelo a SDXL (el workflow no cambia) | Checkpoint (SDXL) + `KSampler` | "Lo único que cambia es el modelo". Resultado "visualmente mucho más interesante" | Mismo prompt, misma seed | `[00:12:28–00:13:41]` |
| 10 | Buscar el equivalente en plantillas oficiales | Templates → filtro de modelos → SDXL → "SDXL simple" | El de Templates abruma; para el tutorial se queda con los del curso porque son "los más puros. Es la esencia" | — | `[00:12:42–00:13:18]` |
| 11 | Cargar el workflow de FLUX.1 (arrastrar y soltar) | Workflow FLUX.1 (con subgraph) | Resolución `1024 × 1024`: "el modelo FLUX está entrenado con imágenes de más resolución", mejor a 1024 que a 512×512. Dentro del subgraph "no tienes que cambiar nada" | `concrete house in desert, rocky landscape` | `[00:14:03–00:14:48]` |
| 12 | Correr FLUX.1 | Run | Más calidad y resolución mayor que los modelos anteriores; "si haces mucho zoom, sigue estando pixelado" | Mismo prompt | `[00:14:53–00:15:35]` |
| 13 | Localizar FLUX.2 en plantillas | Templates → FLUX → klein | `FLUX.2` = familia de modelos · `klein 4B` = 4.000 millones de parámetros, archivo chico · `klein 9B` = 9.000 millones, "más inteligente pero también más pesado" | — | `[00:15:41–00:16:41]` |
| 14 | Correr FLUX.2 klein 9B | Run | `1024 × 1024`; "tarda mucho más en generarse" por ser más pesado y estar entrenado con muchas más imágenes | `Concrete house in desert rocky landscape` | `[00:17:03–00:17:46]` |
| 15 | Cierre de la comparativa y decisión de plataforma | Comfy Cloud | SD 1.5 y SDXL: "no son interesantes hoy en día porque les falta calidad"; FLUX.1 "en algunos casos todavía puede interesar"; FLUX.2 (klein 9B) "de lejos la mejor opción". Recomienda Comfy Cloud porque en local "tardaría muchísimo" | — | `[00:18:07–00:18:42]` |
| 16 | Iterar el prompt con el prompt coach | Prompt coach (configurado en Claude) | Las instrucciones son las del frame "prompt coach setup" de Miro, copiadas y pegadas en el LLM; se escribe "start" y el bot pregunta modelo + qué mejorar | Modelo declarado: `FLUX.2 klein` · Idea: `concrete house in desert, rocky landscape` | `[00:18:48–00:19:46]` |
| 17 | Elegir referencia de estilo | Prompt coach | 3 opciones: `Tadao Ando`, `Rick Joy`, `Kogan` → elige la 01 (Tadao Ando) | — | `[00:20:00–00:20:14]` |
| 18 | Pegar el prompt JSON que devuelve el coach | Prompt (nodo de texto) | "FLUX.2 entiende el JSON prompting" → "Yo copiaría esto… y después pegaría el prompt JSON aquí" | Prompt JSON (el texto literal no se lee en pantalla: "No he leído el prompt entero") | `[00:20:19–00:21:14]` |
| 19 | Editar el prompt por bloques (edición quirúrgica) | Prompt JSON | Bloques: escena · descripción · estilo y colores · iluminación · ambiente · fondo · composición | — | `[00:21:22–00:21:54]` |
| 20 | Volver a simplicidad | Prompt coach | "El prompt coach tiende a complicarlo demasiado" → pedir: "máximo cincuenta palabras, sin estructura JSON", porque en la fase inicial todavía no se conocen las restricciones | Prompt resultante: `deep focus` | `[00:22:03–00:22:37]` |
| 21 | Insertar el nodo de LoRA en el subgraph | `Load LoRA` (nodo oficial de Comfy — logo Comfy) | Doble clic en el lienzo → escribir "load LoRA" → arrastrarlo arriba. Los nombres alternativos son nodos de terceros que Comfy verifica: "son todos seguros" | — | `[00:25:16–00:26:13]` |
| 22 | Enlazar el LoRA al modelo | `Load LoRA` → MODEL | Hay una sola forma de enlazarlo: la salida que dice "model" (la del checkpoint). En entradas que no son de modelo la conexión se pone gris | — | `[00:26:22–00:27:44]` |
| 23 | Crear el repositorio del LoRA en Hugging Face | Hugging Face → "New Model" | Nombre libre · visibility = `private` (no `public`) → "create model". Antes: "agree and access repository" en Black Forest Labs / FLUX.2 klein 9B y aceptar los términos | — | `[00:30:05–00:33:59]` |
| 24 | Subir el archivo del LoRA | Hugging Face → "contribute" → "upload files" → "commit changes" | Archivo `.safetensors` de ~127 MB; el repo queda como `Thomas Rhino to Image LoRA Premium` | — | `[00:34:02–00:35:14]` |
| 25 | Crear el token de acceso | Hugging Face → "access tokens" → "create new token" | Permiso `read` solamente (no "fine-grained", no "write") · nombre p. ej. `comfycloud` → "create token" → "copy" | — | `[00:35:20–00:36:48]` |
| 26 | Pegar el token en Comfy Cloud | Comfy Cloud → Settings → "secrets" → "add secrets" | Antes de "save", el provider debe ser `Hugging Face` | — | `[00:36:54–00:37:48]` |
| 27 | Copiar el link del archivo | Hugging Face → "files and versions" → clic derecho en el botón de descarga → "copy link address" | Clic derecho (el doble clic no sirve) | — | `[00:38:24–00:38:53]` |
| 28 | Importar el LoRA en Comfy | Comfy Cloud → "model library" → "import" → "continue" | Después, refrescar la página | — | `[00:39:04–00:39:21]` `[00:40:01]` |
| 29 | Activar el LoRA en el nodo | `Load LoRA` → "my models" | El LoRA ya aparece disponible en "my models" | — | `[00:40:07–00:40:24]` |
| 30 | Correr con LoRA al 100 % | Run | "esto es con la fuerza del LoRA al 100 %". Cambia el estilo: aparece "ligero grano analógico" porque el LoRA está entrenado con fotografía de arquitectura de 35 mm | Mismo prompt | `[00:40:44–00:41:49]` |
| 31 | Bajar la fuerza del LoRA al 50 % | `Load LoRA` → strength `0,5` → Run | "este LoRA solo se activará al 50 %, así que no será tan dominante a la hora de cambiar la imagen" | Mismo prompt | `[00:42:07–00:42:29]` |
| 32 | Comparar las tres corridas lado a lado | Miro | Izquierda: sin LoRA · Centro: 50 % · Derecha: 100 % | — | `[00:43:13–00:43:17]` |
| 33 | Descargar la plantilla del curso y arrastrarla a Comfy | Comfy Cloud (drag & drop) | "tendrás exactamente el mismo prompt, ajustes y seed que yo" | — | `[00:45:53–00:46:18]` |
| 34 | Recoger los recursos extra del tablero | Miro (extremo derecho del frame) | Imagen descargable con el workflow entero (prompt, ajustes y seed) de una torre usada para probar ideas | — | `[00:46:31–00:46:59]` |

---

## Modelos y checkpoints mencionados

| Nombre | Qué dice el video de él | Cuándo lo recomienda | Cuándo lo descarta | Timestamp |
|--------|--------------------------|----------------------|--------------------|-----------|
| **DreamShaper** | "Es un modelo Stable Diffusion 1.5"; salió en 2022; "a día de hoy es un modelo viejísimo"; visualmente decepciona pero "va bien para aprender lo básico" | Como demostración de los controles del `KSampler` (seed, steps, CFG) | Como resultado de producción: la calidad no alcanza | `[00:04:10–00:04:37]` `[00:18:19–00:18:22]` |
| **Stable Diffusion 1.5** | El motor del workflow más básico; el workflow de SDXL es "el mismo workflow con otro modelo" | Para aprender la interfaz y la lectura de los parámetros | "Los dos primeros no son interesantes hoy en día porque les falta calidad" | `[00:04:17–00:04:23]` `[00:12:30–00:12:36]` `[00:18:19–00:18:22]` |
| **Stable Diffusion XL** | "Visualmente mucho más interesante" que SD 1.5 con el mismo prompt y la misma seed | Cuando se quiere ver el salto de calidad manteniendo el workflow intacto | "No son interesantes hoy en día porque les falta calidad" | `[00:12:28–00:12:39]` `[00:13:23–00:13:41]` `[00:18:19–00:18:22]` |
| **FLUX.1** | "Está entrenado con imágenes de más resolución": mejor a 1024×1024 que a 512×512. Calidad claramente superior, aunque con zoom sigue pixelado | "En algunos casos todavía puede interesar" | Cuando se prioriza calidad y control de estilo sobre costo/tiempo | `[00:14:20–00:14:36]` `[00:15:13–00:15:21]` `[00:18:27]` |
| **FLUX.2 (familia)** | Es la familia de modelos que aparece en el filtro de plantillas; "ves la diferencia entre modelos" | Como familia de referencia del salto de calidad | — | `[00:16:09–00:16:15]` |
| **FLUX.2 klein 4B** | "Klein es solo una forma de decir que es un archivo pequeño, o sea que no carga tu computadora como los otros". Entrenado con 4.000 millones de parámetros | Cuando importa el consumo de recursos en local | El video elige el 9B para la demostración | `[00:16:19–00:16:30]` |
| **FLUX.2 klein 9B** | Entrenado con 9.000 millones de parámetros: "más inteligente, pero también más pesado"; tarda mucho más; en Templates "FLUX.2 → klein" | "De lejos la mejor opción para ti" / "sobre todo este". Se recomienda correr en Comfy Cloud porque en local tardaría muchísimo | — | `[00:16:33–00:16:41]` `[00:17:31–00:17:38]` `[00:18:31–00:18:42]` |
| **Rhino to Image LoRA Basic** | LoRA **incluido en el curso**: archivo `.safetensors` en la carpeta que se recibe. Se puede usar sin problema; la diferencia con el premium es solo la calidad visual | Cuando se quiere la alternativa incluida en el material del curso | — | `[00:31:29–00:31:43]` `[00:33:08–00:33:22]` `[00:41:55–00:41:59]` |
| **Rhino to Image LoRA Premium** | LoRA del presentador, "lo entrené durante mucho tiempo", calidad "buenísima"; descarga en su web (de 100 a 49 con descuento mientras dure el concurso). En HF el repo queda como `Thomas Rhino to Image LoRA Premium` (~127 MB) | Cuando se busca el máximo aporte de estilo (el video lo usa para la demo) | — | `[00:31:51–00:32:47]` `[00:33:25–00:34:40]` `[00:35:03–00:35:10]` |
| **LoRA al 100 % (strength)** | Resultado con "ligero grano analógico" y mayor dominancia sobre el resultado | Cuando querés que el estilo del LoRA se imponga sobre la imagen | — | `[00:41:31–00:41:49]` `[00:43:17]` |
| **LoRA al 50 % (strength `0,5`)** | "Solo se activará al 50 %, así que no será tan dominante a la hora de cambiar la imagen" | Punto intermedio de control: con LoRA la imagen se sigue corrigiendo, pero sin que el LoRA domine | — | `[00:42:14–00:42:29]` `[00:43:15]` |
| **Sin LoRA (línea base)** | Sin LoRA el resultado queda "un poco plástico, saturado, superduro de contraste"; con LoRA es "mucho más suave, mucho más sutil arquitectónicamente" | Como referencia de comparación | — | `[00:44:12–00:44:34]` `[00:43:13]` |
| **FLUX.2 klein 9B en Hugging Face (Black Forest Labs)** | Modelo gated: "agree and access repository" y aceptar los términos de FLUX / Black Forest Labs. Da el modelo card (cómo ejecutarlo, limitaciones, documentación) | Para quien corre el modelo en local: ahí se descarga el archivo grande | En Comfy Cloud, el modelo ya está descargado por el servicio | `[00:29:28–00:29:48]` `[00:30:05–00:31:09]` |
| **Comfy Cloud** | Plataforma de ejecución del curso: "si no, seguramente tardaría muchísimo generarlo en local" | Toda la demostración; además es donde viven los secrets y la Model Library | — | `[00:18:37–00:18:42]` `[00:24:38–00:24:48]` |
| **LoRA "Spectrum"** | Solo se nombra: "También viene Spectrum. Explicaré qué es en el siguiente módulo" | — | — | `[00:44:41–00:44:48]` |

---

## Prompts y fórmulas

### Prompt de trabajo (constante en toda la comparativa)

```
concrete house in desert rocky landscape
```
`[00:04:04]` · reaparece en FLUX.1 como `concrete house in desert, rocky landscape` `[00:14:18]` y en FLUX.2 como `Concrete house in desert rocky landscape` `[00:17:15]`

### Prompt negativo (modelo SD 1.5 / DreamShaper)

```
cat, dog, waterpark
```
`[00:04:37–00:04:42]`

### Fórmula del prompt coach (Claude)

```
start
→ modelo: FLUX.2 klein
→ qué mejorar: concrete house in desert, rocky landscape
→ referencias ofrecidas: Tadao Ando / Rick Joy / Kogan
```
`[00:19:04–00:20:14]`

### Regla de simplificación que el video enseña

```
máximo cincuenta palabras, sin estructura JSON
```
`[00:22:09–00:22:16]` — el prompt resultante se titula `deep focus` `[00:22:34]`

### Estructura del prompt JSON que devuelve el coach para FLUX.2

```
escena
descripción
estilo + colores
iluminación
ambiente
fondo
composición
```
`[00:21:22–00:21:54]`

### Reglas de estructura / qué pesa / qué no va

- **FLUX.2 entiende JSON prompting**: es "la forma en que esto está organizado, la información estructurada así" `[00:20:26–00:20:40]`.
- **El JSON da control quirúrgico**: si hay una idea clara, se cambia un bloque y el resto queda intacto `[00:21:51–00:21:54]`.
- **Orden de edición por bloques**: escena → descripción → estilo/colores → iluminación → ambiente → fondo → composición `[00:21:28–00:21:48]`.
- **En fase inicial manda la simplicidad**: el prompt coach "tiende a complicarlo demasiado"; en el doble diamante inicial todavía no se conocen las restricciones, así que el prompt corto rinde más `[00:22:03–00:22:26]`.
- **Qué NO va**: la sobre-complicación del coach (JSON + referencias + paleta completa) cuando todavía no hay restricciones definidas — la salida de 50 palabras sin JSON es la que el video ejecuta y aprueba `[00:22:09–00:23:14]`.
- **Referentes admitidos**: Tadao Ando, Rick Joy, Kogan `[00:20:00–00:20:14]`.
- **El texto literal del prompt JSON**: no transcribible — el video lo muestra en pantalla sin leerlo ("No he leído el prompt entero") `[00:21:00–00:21:05]`.

---

## Reglas, buenas prácticas y trampas

- Para medir un parámetro, mantené prompt, prompt negativo y `Empty Latent Image` intactos: así sabés que el cambio viene solo del ajuste `[00:05:20–00:05:35]`.
- `fixed value` en la seed = la imagen es siempre idéntica; `randomize value` = seed nueva en cada corrida `[00:05:44–00:07:37]` `[00:08:01–00:08:11]`.
- Los `steps` son iteraciones: 5 deja la imagen sin terminar, 10 cierra bien, 20 no agrega diferencia visible — el sampler es determinista y se puede rastrear por qué pasó lo que pasó `[00:09:08–00:10:01]`.
- El `cfg` es "la cantidad de creatividad": con 1 la imagen queda cruda, con 20 se sobresatura y machaca los píxeles; para ese workflow el valor es 8 `[00:10:05–00:11:08]`.
- Para recordar qué hace un parámetro: pasá el cursor por encima del valor, o consultá al "experto en Comfy" `[00:10:09–00:10:22]`.
- Para diagnosticar: hacé una captura de la página, pegala en el "experto en Comfy" y preguntá "¿por qué mi imagen de salida no es buena?" — responde en ~1 minuto con el veredicto y el valor corregido `[00:11:27–00:12:17]`.
- Usá los workflows que entrega el curso: son "los más puros. Es la esencia y nada más" `[00:13:14–00:13:18]`.
- FLUX rinde mejor a 1024×1024 que a 512×512, porque está entrenado con imágenes de más resolución `[00:14:26–00:14:36]`.
- Para FLUX.2 klein 9B, la plataforma recomendada es Comfy Cloud: en local el tiempo se dispara `[00:18:37–00:18:42]`.
- El prompt coach se arma **una vez** (las instrucciones están en el frame "prompt coach setup" de Miro) y después se pega en tu LLM; el LLM elegido en el video es Claude `[00:19:04–00:19:25]`.
- Al prompt coach hay que declararle siempre el modelo y qué se quiere mejorar `[00:19:29–00:19:46]`.
- Pedí siempre simplicidad al coach: "máximo cincuenta palabras, sin estructura JSON" `[00:22:09–00:22:16]`.
- Usá el nodo con logo de Comfy (aquí, `Load LoRA`): los nombres alternativos son nodos de terceros verificados por Comfy, todos seguros `[00:25:40–00:25:58]`.
- Para conectar un LoRA, buscá la salida que dice "model": hay una única forma de enlazarlo, y las entradas incompatibles se muestran en gris `[00:26:33–00:27:04]`.
- En Hugging Face, creá el repositorio en modo `private` (no `public`), así el LoRA no queda expuesto `[00:33:45–00:33:55]`.
- El token de Hugging Face lleva permiso `read` solamente — "no fine-grained ni write" `[00:35:44–00:36:01]`.
- El token es una contraseña: mantenelo privado, nunca pegado en internet `[00:36:13–00:36:42]`.
- En Comfy Cloud, el provider del secret tiene que ser `Hugging Face` antes de guardar `[00:37:25–00:37:40]`.
- Para copiar el link del archivo: clic derecho sobre el botón de descarga → "copy link address" (el doble clic no sirve) `[00:38:29–00:38:43]`.
- Si Comfy Cloud queda lento y no muestra código de error, refrescá la página: la conexión en la nube a veces tarda unos segundos `[00:24:38–00:25:01]`.
- Con el LoRA al 50 % la imagen sigue generándose y el modelo se va corrigiendo, con menos dominancia del LoRA que al 100 % `[00:42:14–00:42:37]`.
- La importación de un LoRA es un trámite de una sola vez: después queda disponible en tu cuenta de Comfy siempre `[00:45:14–00:45:32]`.
- Descargá la plantilla del curso y arrastrala a Comfy: reproduce exactamente el mismo prompt, ajustes y seed `[00:45:53–00:46:18]`.
- En el tablero hay un bloque de recursos extra (workflow completo de una torre de ejemplo) para seguir practicando `[00:46:31–00:46:59]`.
- El LoRA `Spectrum` queda para el módulo siguiente `[00:44:41–00:44:48]`.

---

## Qué NO dice el video (para implementarlo)

| Vacío | Detalle | Estado |
|-------|---------|--------|
| `sampler_name` y `scheduler` de cada workflow | No se nombra ninguno de los cuatro workflows | no dicho en el video |
| `steps` de SDXL, FLUX.1 y FLUX.2 | Los steps solo se varían en el workflow SD 1.5 (5 / 10 / 20) | no dicho en el video |
| `cfg` de SDXL, FLUX.1 y FLUX.2 | El 8 es explícito solo para el workflow SD 1.5 | no dicho en el video |
| Nombres exactos de los checkpoints SDXL y FLUX.1 | Solo se dice "un modelo Stable Diffusion XL" y "el modelo FLUX" | no dicho en el video |
| Resolución del `Empty Latent Image` en SD 1.5 y SDXL | Solo se da 1024×1024 para FLUX.1 y FLUX.2 | no dicho en el video |
| Lista de nodos del subgraph de FLUX.1 / FLUX.2 | El video solo afirma que no hay nada que cambiar adentro | no dicho en el video |
| Texto literal del prompt JSON | Se muestra en pantalla pero el presentador no lo lee | no dicho en el video |
| Las instrucciones de "prompt coach setup" y "comfy expert setup" | Viven en Miro; el video solo las muestra pegadas en Claude | no dicho en el video |
| Trigger word / frase de activación del LoRA | El LoRA se activa por el nodo y el `strength`, sin frase | no dicho en el video |
| Por qué el negativo es `cat, dog, waterpark` | El video promete "después verás por qué" y no lo explica en este módulo | no dicho en el video |
| Peso relativo de los términos dentro del prompt | El video enseña a editar por bloques JSON, no a ordenar términos por peso | no dicho en el video |
| Nombre exacto del archivo `.safetensors` del LoRA premium | Solo el nombre del repo en HF (`Thomas Rhino to Image LoRA Premium`) | no dicho en el video |
| VRAM, tiempo de generación y costo por imagen | Solo la percepción cualitativa "tarda mucho más" | no dicho en el video |
| Detalles del LoRA "Spectrum" | Remitido al módulo siguiente | no dicho en el video |
| Flujo del módulo 3 (image to image / Rhino-to-Image) | Solo se menciona como "el siguiente módulo" | no dicho en el video |

---

## Qué aporta al concurso AIxGaudi ("The Gaudí Nexus")

- **Fija la línea de base técnica del render de concepto**: FLUX.2 klein 9B a 1024×1024 en Comfy Cloud, con SD 1.5 y SDXL relegados a material de aprendizaje y FLUX.1 como opción secundaria `[00:15:41–00:17:43]` `[00:18:07–00:18:42]`.
- **Estandariza el protocolo de comparación**: prompt y seed constantes, y variación de una sola variable (steps, CFG, fuerza del LoRA). Es exactamente la tabla que el tablero del curso documenta: FLUX.2 klein 9B / + LoRA 50 % / + LoRA 100 % `[00:05:20–00:05:35]` `[00:09:08–00:11:08]` `[00:43:13–00:43:17]`.
- **Da el método de iteración de prompt**: prompt coach en Claude con modelo declarado, referencias de autor (Tadao Ando / Rick Joy / Kogan), prompt JSON por bloques para edición quirúrgica y tope de 50 palabras en la fase divergente del doble diamante `[00:18:48–00:22:37]`.
- **Resuelve la capa de fotorrealismo**: deja operativo el LoRA `rhino-to-image` (basic incluido en el curso) como ajuste de estilo y material con control de fuerza 0,5–1,0, que es la base del módulo 3 (Rhino-to-Image) y del pase de arcilla `[00:31:29–00:31:43]` `[00:42:07–00:44:34]`.
- **Desbloquea la importación de LoRAs para todo el equipo**: Hugging Face (repo privado + token `read`) → secret en Comfy Cloud → Model Library → `Load LoRA`. Es un trámite único por participante que después queda en la cuenta `[00:27:54–00:40:24]` `[00:45:14–00:45:32]`.
- **Entrega la biblioteca de referencia**: los workflows del tablero de Miro (los "más puros") son importables y reproducibles con el mismo prompt, ajustes y seed, y hay un workflow extra de una torre como material de práctica `[00:03:08–00:03:16]` `[00:45:53–00:46:59]`.

---

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|ComfyUI]] — nodos, modelos y flujos del estudio
- [[wiki/glosario/software/comfy-cloud-vs-runpod|Comfy Cloud vs RunPod]] — la decisión de plataforma que este módulo resuelve a favor de Comfy Cloud
- [[wiki/glosario/software/flux2-klein-9b|FLUX.2 Klein 9B]] — modelo base del flujo y del LoRA
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|LoRA rhino-to-image (curso AI×Gaudí)]] — ficha del LoRA basic y premium, strengths y activación
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/README|A-txt2img]] — módulo txt2img del MVP_04
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/plans/comparativa-sd15-vs-sdxl|comparativa-sd15-vs-sdxl]] — el antecedente interno de esta comparativa de modelos
- [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|Extracción del material del curso AI×Gaudí]] — inventario del tablero Miro, datos del concurso y dónde queda cada módulo
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/00-README|WF-rhino-to-image]] — el flujo del módulo 3 que este LoRA habilita
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — playbook operativo de la herramienta
- [[wiki/glosario/conceptos/vault-visual|vault-visual]] — iteración asistida por IA
- [[specs/261019-plan-concurso-gaudi-nexus-ia|Concurso Gaudí Nexus + modelo de honorarios]] — dónde aterriza esta línea técnica en el concurso
- [[wiki/glosario/conceptos/design-thinking|design-thinking]] — el marco de doble diamante que el video usa para ubicar el text-to-image
- [[wiki/glosario/conceptos/hitl-human-in-the-loop|HITL]] — el loop humano↔IA que el prompt coach explota

> Nota de enlace: el archivo real es `proyectos/MVP_04-comfyui-arquitectura/A-txt2img/README.md` (no `00-README.md`); se usa la ruta que resuelve.

---

## Cómo lo adaptamos

| Lo que hace el curso | Lo que hacemos nosotros | Por qué |
|----------------------|-------------------------|---------|
| Compara los cuatro modelos en Comfy Cloud con el mismo prompt y la misma seed `[00:13:23–00:13:35]` `[00:17:15–00:17:22]` | Corremos la comparativa completa con el prompt y la seed constantes del curso; la rama SD 1.5 usa `architecturerealmix_v11` y la rama SDXL usa `Juggernaut-XL_v9_RunDiffusionPhoto_v2`, los dos checkpoints ya en disco, en la máquina local | Los dos checkpoints legacy son livianos y corren en el equipo local sin costo de GPU: la comparativa queda completa y reproducible en el mismo entorno |
| FLUX.2 klein 9B corre en Comfy Cloud, con el modelo ya descargado por el servicio `[00:18:37–00:18:42]` `[00:29:32–00:29:37]` | La rama FLUX.2 klein 9B corre en un pod de RunPod | El modelo de 9B con su text encoder no entra en la VRAM local; el pod aporta la memoria necesaria y deja registro de seeds, horarios y costos de cada corrida |
| La variante del LoRA (50 % y 100 %) se compara sobre FLUX.2 klein 9B en Comfy Cloud `[00:40:44–00:43:17]` | La rama del LoRA corre en el mismo pod, sobre el mismo checkpoint FLUX.2 klein 9B, con los tres pasos: sin LoRA, `strength` 0,5 y `strength` 1,0 | El LoRA se aplica sobre la base FLUX.2: comparar 0 / 0,5 / 1,0 en un único entorno hace la tabla directamente atribuible |
| El LoRA se importa desde Hugging Face: repo privado + token de lectura + secret en Comfy Cloud `[00:27:54–00:40:24]` | El `rhino-to-image-lora.basic.safetensors` (120,8 MB) ya está en la máquina y sube al pod por `scp` | El binario viaja una sola vez y directo al entorno de ejecución: cada participante evita multiplicar repos privados, tokens y secretos, y el equipo trabaja sobre el mismo archivo |
| La importación a Comfy Cloud es el mecanismo para activar el LoRA en la nube del curso `[00:38:57–00:40:24]` | El procedimiento de importación queda documentado en el plan, listo para activarse cuando el LoRA esté publicado en CivitAI o Hugging Face | Con el LoRA publicado, cualquiera del equipo activa el nodo `Load LoRA` con un clic, sin depender de una cuenta personal ni de tokens compartidos |
| El prompt coach es un bot en Claude armado con las instrucciones del frame "prompt coach setup" de Miro `[00:19:04–00:19:25]` | El prompt coach se mantiene como proyecto de Claude con esas mismas instrucciones, y se le declara siempre el modelo y el objetivo de la iteración `[00:19:29–00:19:46]` | Conserva la trazabilidad de las iteraciones de prompt y el JSON prompting propio de FLUX.2, que es el formato que el módulo 3 exige para el flujo Rhino-to-Image |

---

## Checks contra el criterio del jurado

- El criterio del jurado pone la **lógica constructiva por delante de la apariencia** (Cas Esbach, módulo 6). En este módulo eso se traduce en comparar **una variable por vez y registrar el resultado**: cada fila de la tabla de modelos del estudio —SD 1.5, SDXL, FLUX.1, FLUX.2 klein 9B, + LoRA 50 %, + LoRA 100 %— sale de acá, con su prompt, su seed y su timestamp de corrida `[00:05:20–00:05:35]` `[00:43:13–00:43:17]`.
- **No confundir la estética prestada con la propia**: el grano analógico del LoRA es la firma de un modelo entrenado con fotografía de arquitectura de 35 mm, y cada LoRA deja su marca en la imagen. La suma de firmas se documenta como recurso ajeno a la propuesta, para que el jurado pueda leer el origen de cada gesto `[00:41:35–00:41:49]` `[00:44:12–00:44:34]`.
- **La referencia de autor que propone el prompt coach —Tadao Ando, Rick Joy, Kogan— es una decisión de proyecto**: se anota en la ficha del render con quién es y por qué se eligió, de modo que el criterio se lea además de la imagen `[00:20:00–00:20:14]`.
- **El aporte de cada capa es auditable**: la comparación sin LoRA / 50 % / 100 % se publica como tabla con el valor exacto de `strength` y el mismo prompt, para que el jurado pueda auditar cuánto aporta cada ajuste `[00:42:07–00:43:17]`.
- **Pendiente**: la transcripción del módulo 6 (round table, donde expone Cas Esbach) todavía no está en el vault. Cuando llegue, este checklist se contrasta contra el criterio textual y se ajusta lo que corresponda.
