---
tipo: plan
proyecto: Proyecto Pi
cliente: Estudio (línea propia)
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: borrador
tags: [concurso, gaudi-nexus, comfyui, workflows, curso-ai-gaudi, runpod, comfy-cloud, rhino, lora, pomodoros, leantime, deadline]
idioma: es
---

# Workflows adaptados del curso AI×Gaudí — plan maestro de construcción y revisión

> Origen: transcripción completa de los 6 módulos con subtítulos del curso AI×Gaudí de Archademy (`raw/yt/transcripts/2026-10-21_mux-*.{es,en}.md`, 4.010 cues) + la página pública del concurso en competitions.archi + la verificación del estado real de la instalación local de ComfyUI del 2026-10-28. La transcripción del módulo 6 (Round Table) queda pendiente: el video no expone subtítulos y se transcribe localmente.
>
> Relacionado: [[specs/261019-plan-concurso-gaudi-nexus-ia|plan del concurso (milestones 537-542 ya cargados)]] · [[proyectos/STUDIO_OS-Emilia/presentacion/08-propuesta-mes2-cad-urbano|propuesta CAD → Rhino → ComfyUI → A1]] · [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|extracción del material del curso]] · [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] · [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] · [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas de workflows]]

## 1. SPEC

### 1.1 Objetivo

Convertir los siete módulos del curso AI×Gaudí en **siete workflows ejecutables, adaptados a la infraestructura del estudio**, y cerrarlos **uno por uno con revisión humana** antes de pasar al siguiente. El resultado esperado son los flujos que producen la lámina A1 del concurso "The Gaudí Nexus" y, con ellos, la demostración de método que el jurado evalúa: cada imagen de la entrega se puede regenerar con su grafo, su prompt y su seed.

Tres entregables:

1. **`specs/261028-plan-workflows-adaptados-curso-ai-gaudi.md`** (este documento) — el plan que describe los siete workflows, el método de trabajo y el calendario.
2. **`proyectos/concurso-gaudi-nexus/`** — la carpeta del concurso con las siete fichas de flujo (`flujos/`), los siete workflows (`workflows/`) y el criterio del jurado (`criterio/`).
3. **Siete workflows en estado v1.0**, cada uno con su JSON en API format, su documentación (`00-README` · `01-index` · `02-WF-log` · `03-nodos` · `04-backlog`), sus corridas registradas y su checklist de cierre satisfecho.

### 1.2 Estado real (medido el 2026-10-28)

**Infraestructura local**

| Dato | Valor |
|------|-------|
| GPU | AMD RX 570, 8 GB VRAM, DirectML (`--directml 0`) |
| ComfyUI | v0.28.0 (`b08e6cf3`) en `P:\00-repos\ComfyUI` |
| Servidor | apagado en la revisión (`127.0.0.1:8188` sin respuesta) |
| Arranque | `corre_comfyui.bat` → `main.py --listen 127.0.0.1 --port 8188 --force-fp16 --preview-method auto --disable-auto-launch --cache-ram 2 8 --lowvram --cpu-vae --directml 0 --disable-cuda-malloc --disable-dynamic-vram` |
| Nodos personalizados | 2: `ComfyUI-IC-Light`, `ComfyUI_IPAdapter_plus` |
| Nodos core útiles | `Canny`, `LoadDA3Model` / `DA3Render` (Depth Anything 3) |

**Modelos en disco**

| Carpeta | Contenido | Rol |
|---------|-----------|-----|
| `checkpoints` | `architecturerealmix_v11` (2,03 GB · SD1.5) · `Juggernaut-XL_v9_RunDiffusionPhoto_v2` (6,78 GB · SDXL) · `sd-v1-5-inpainting-fp16` (2,03 GB) | base local para iterar |
| `loras` | `archisketch-v1` (18,1 MB) · `markerhandsketch-V1` (9,1 MB) · **`rhino-to-image-lora.basic` (120,8 MB)** | el LoRA del curso ya está en la máquina |
| `controlnet` | canny (689 MB) · depth fp16 (689 MB) · scribble (1,38 GB) — los tres SD1.5 | control geométrico local |
| `clip_vision` + `ipadapter` | `CLIP-ViT-H-14-laion2B` · `ip-adapter-plus_sd15` | transferencia de estilo local |
| `geometry_estimation` | `depth_anything_3_small` | preprocesado de profundidad (nodo core) |
| `unet` | `IC-Light/iclight_sd15_fc` (1,64 GB) | re-iluminación |
| `upscale_models` | `RealESRGAN_x4plus` (63,9 MB) | upscale local |

**Lo que falta en la máquina** (cantidad medida, no estimada): `diffusion_models` vacío · `vae` vacío · `text_encoders` vacío · `clip` vacío · `embeddings` vacío · `frame_interpolation` vacío · `optical_flow` vacío. El stack FLUX.2 klein 9B son 18,3 GB repartidos en transformer fp8 (9,4 GB), text encoder Qwen3-8B (8,7 GB) y VAE Flux2 (238 MB). Faltan también `comfyui_controlnet_aux` (preprocesadores hed/lineart/mlsd/MiDaS) y `ComfyUI-GGUF` (variante local quantizada).

**Material del curso yaistered en el vault**

| Ítem | Estado |
|------|--------|
| Transcripciones de los módulos 1, 2, 3, 4, 5 y 7 | listas, EN + ES (12 pistas, 4.010 cues) |
| Módulo 6 (Round Table) | pendiente de transcripción local (el video expone 404 en sus subtítulos) |
| Tablero Miro del curso | inventariado: `AI-course.csv`, 219 filas, 72 secciones |
| Prompts oficiales (INSTRUCTION.md variante A y B, esqueleto JSON con *STRICT CAMERA LOCK*) | extraídos y archivados en `n_05-rhino-mcp/WF-rhino-to-image/` |
| LoRA `rhino-to-image` basic | en disco (120,8 MB) |
| LoRA `rhino-to-image` premium | pendiente de descarga (no está en el Drive del curso) |
| Workflow «Rhino-to-Image» | construido (23 nodos, API format) en `n_05-rhino-mcp/WF-rhino-to-image/` |
| Coursera: workflows importables del tablero | disponibles en el tablero; **Comfy Cloud Free** es la vía para probarlos sin costo |

**Reloj del concurso**: entrega **16/12/2026 23:59 GMT-7** · lámina **A1 online, máx. 15 MB, JPEG** (+ A4 opcional para el Premio de Diseño) · tema: Mercado de Proximidad + Centro de Cultura Digital en el entorno de la plaza de la Sagrada Família · premios 1.º US$6.000, 2.º US$2.000, 3.º US$1.000, Premio de Diseño US$1.000, 10 menciones, 50 finalistas. Hoy es **28/10/2026**: quedan 7 semanas.

### 1.3 Alcance

**Dentro**

- Los siete workflows, uno por módulo, en orden de curso.
- La adaptación de cada nodo cerrado o de pago del curso a la pila del estudio.
- El método de construcción y revisión (un gate humano por workflow).
- Las siete fichas de flujo, con valor de tiempo y con lo que el video deja vacío marcado.
- La transcripción del módulo 6 y el checklist de criterio del jurado.
- La actualización de las reglas de workflows del estudio (R2 y nomenclatura de salidas).

**Fuera**

- El entrenamiento del LoRA propio sobre material de la Fundació: es un ADR aparte con su presupuesto (klein 4B Apache 2.0, ~$1, 2-3 h de pod).
- La inscripción y la ampliación del equipo a cuatro personas: ya resueltas o en curso.
- La composición final de la lámina A1: es el WF-08 de diciembre, con su propio ciclo de revisión.
- El uso de Comfy Agent con material del concurso: las cuatro reglas de costo cero del §2.2 lo reservan para material que no sea del concurso.

### 1.4 Criterio de cierre del plan

El plan se cierra cuando **los siete workflows están en v1.0** (grafo + documentación + tres corridas A registradas + checklist del jurado satisfied) y **la lámina A1 candidata está compuesta** (M-C7). Cada workflow se cierra con la revisión humana registrada en su `02-WF-log`.

---

## 2. La decisión de plataforma

### 2.1 Veredicto

Se adopta el veredicto ya escrito en [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]]:

| Ruta | Para qué | Costo |
|------|----------|-------|
| **Local 8 GB** | iterar (SD1.5 / SDXL / ControlNet / upscale / preprocesado 3D) · toda la validación estática | $0 |
| **Comfy Cloud Free** | probar los workflows oficiales del curso tal cual y medir los nodos partner | $0 · 400 créditos/mes ≈ 25 min de GPU |
| **RunPod 3090** ($0,22/h) · 4090 ($0,34/h) · A40 48 GB ($0,35/h) | producción FLUX.2 klein 9B, render de la lámina, entrenamiento del LoRA propio | **$1-2** para todo el concurso |
| **Comfy Cloud Standard $20** | producción de imagen sin LoRA propio, con fricción de plataforma | $20/mes |
| **Comfy Cloud Creator $35** | importar modelos propios desde CivitAI/Hugging Face | $35/mes |

**Costo del concurso completo: $1-2** frente a $20-35/mes de suscripción permanente. Para una línea de trabajo que el 16/12 cierra, la forma razonable es **pagar por uso**.

### 2.2 Las cuatro reglas de costo cero (PI)

1. El material del concurso se procesa en el pod propio o en la PC: el Comfy Agent queda para material que no sea del concurso.
2. En el pod: disco de contenedor (no Network Volume) y el pod se termina al terminar el trabajo.
3. A Comfy Cloud suben **imágenes derivadas**, nunca los `.dwg` originales ni las fotos de material con licencia de la Fundació.
4. En los prompts no se escriben datos de cliente (nombres, superficies, dirección).

**Tensión a reconciliar (ADR-002):** el plan de Studio OS fija "nunca planos legales o de concurso en cloud, local por defecto" (`proyectos/STUDIO_OS-Emilia/04-plan-studio-os.md:36,189`), mientras el veredicto de infraestructura pone el render 9B en RunPod. La reconciliación propuesta: **lo que sale de la máquina son imágenes derivadas y grafos**, y el `.dwg` de Barcelona y el material con licencia de la Fundació permanecen en el Drive y en la PC. El ADR se escribe antes de la primera corrida en el pod (tarea S3).

### 2.3 Planes de Comfy Cloud para los nodos privados del curso

El curso usa nodos partner de pago: Nano Banana 2 y Pro, GPT Image, Seedance 2.0, Tripo 3.1, Topaz, Magnific, Grok y Google. Los precios que el video da (texto del módulo 4, `[00:02:33]-[00:04:26]`) son: Seedance 320 créditos por corrida a 720 px / 7 s; 1.600 en 4K; 3.400-3.500 en 4K de 15 s; ≈30 € por video 4K de 15 s.

| Nodo partner | Prueba | Producción |
|--------------|-------|------------|
| Seedance 2.0 | Comfy Cloud Free (400 cr ≈ 1 corrida) | Comfy Cloud Creator/Pro, o LTX en el pod |
| Nano Banana 2 / Pro | Comfy Cloud Free | sustitución local (FLUX.2 klein + SDXL/DA3) |
| Tripo 3.1 | Comfy Cloud Free | ComfyUI-3D-Pack en el pod |
| Topaz / Magnific / Grok / Google | Comfy Cloud Free | RealESRGAN + Hires fix en local |

**Criterio:** siempre se intenta primero el ComfyUI local; el nodo privado entra cuando la ruta local no cubre el caso, y su costo se pide antes de cada gasto.

---

## 3. La matriz de adaptación

El curso corre sobre Comfy Cloud con nodos cerrados. El estudio corre sobre ComfyUI propio con modelos abiertos. Cada diferencia se resuelve así:

| El curso usa | Adaptamos a | Por qué |
|--------------|-------------|---------|
| Comfy Cloud 96 GB | RunPod 3090 con nuestro ComfyUI | control de modelos propios y costo por uso |
| LoRA `rhino-to-image` (basic y premium) | local + pod | Comfy Cloud Standard no importa modelos propios y el LoRA del curso no está en CivitAI ni en Hugging Face |
| Nano Banana 2 (paso 1 del módulo 7, inpaint del módulo 3) | FLUX.2 klein 9B en modo edición + el prompt del agente (INSTRUCTION.md variante B, ya archivado) | la geometría se preserva igual y el paso queda dentro de la máquina |
| Nano Banana Pro (preparación del módulo 5) | SDXL + ControlNet depth/scribble + Depth Anything 3 (nodos core ya instalados) para AO, normal map y multiview de 4 tiles | el AO es la variante que el propio profesor llama favorita (`[00:13:50]`) |
| Seedance 2.0 | LTX en el pod; Seedance queda como prueba en Comfy Cloud Free | 1.600 cr en 4K y ≈30 € el clip de 15 s |
| Tripo 3.1 y su variante multiview | ComfyUI-3D-Pack (Tripo3D / Hunyuan3D-2) en el pod | el curso usa el nodo Hunyuan3D, así que la vía abierta reproduce el resultado |
| Topaz / Magnific / Grok / Google (upscale) | `RealESRGAN_x4plus` (en disco) + Hires fix (2.º KSampler, denoise 0,15-0,35) | el parámetro "creativity" del curso se traduce a denoise más prompt de detalle |
| Prompt coach en Claude | proyecto Claude con las instrucciones del tablero (ya inventariadas) | la vía ya está armada |
| Secret de Hugging Face en la nube | los modelos se suben al pod por scp/rsync | sin secretos en servicios externos |
| Marca de planos en negro para loggias | idem, en Rhino + Photoshop | es la técnica que el video enseña para que el modelo abra vanos donde corresponde |

---

## 4. Los siete workflows

Estructura común de cada workflow (variante canónica de [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas de workflows]]): `00-README.md` · `01-index.md` · `02-WF-log-WF<nn>.md` · `03-nodos-WF<nn>.md` · `04-backlog.md` · `salidas/` · `PLANS/` · `SPECS/` · `workflow_<nombre>.json` (API format, ids correlativos, `_meta.title` en los nodos con rol editorial).

### WF-01 · Base y lectura de nodos — módulo 1 (90 min 49 s)

- **Origen**: `[00:33:00]` (el flujo va de izquierda a derecha: input → generación → output) · `[00:34:05]` Load Checkpoint · `[00:34:39]` prompt positivo y negativo · `[00:35:33]` Empty Latent Image · `[00:36:13]` KSampler como "el fogón" · `[01:04:32]` seed fija / randomizada · `[01:07:11]` steps · `[01:08:48]` CFG · `[01:11:12]` las tres formas de escribir el prompt.
- **Grafo**: `CheckpointLoaderSimple` → `CLIPTextEncode` (pos) + `CLIPTextEncode` (neg) → `EmptyLatentImage` 512×512 → `KSampler` (seed 42, steps 20, cfg 8, `euler_ancestral` + `karras`) → `VAEDecode` → `SaveImage`.
- **Corre en**: local. Todo el stack está en disco.
- **Adaptación**: el video lo ejecuta en Comfy Cloud; nosotros en local, conservando el protocolo (una variable por corrida, prompt y seed constantes).
- **Entregable**: el grafo base + la tabla "nodo → qué hace" que el video explica en voz alta, que pasa a ser la primera versión del glosario de nodos del estudio.
- **Cierre**: tres corridas A (seeds 42 / 77 / 123) registradas con tiempo y VRAM.
- **Estado**: pendiente.

### WF-02 · Texto a imagen y comparativa de modelos — módulo 2 (47 min 09 s)

- **Origen**: `[00:04:02]` DreamShaper / SD1.5 · `[00:12:28]` SDXL · `[00:14:03]` FLUX.1 a 1024×1024 · `[00:17:03]` FLUX.2 klein 9B · `[00:25:16]` `Load LoRA` · `[00:30:05]-[00:40:24]` importación del LoRA desde Hugging Face · `[00:42:07]` fuerza 0,5 · `[00:43:13]` comparación sin LoRA / 50 % / 100 %.
- **Grafo**: tres ramas comparativas con el prompt constante `concrete house in desert rocky landscape` y la negativa `cat, dog, waterpark`; en la rama FLUX.2, `LoraLoaderModelOnly` con `rhino-to-image-lora.basic.safetensors` en 0,5 / 0,8 / 1,0.
- **Corre en**: local para SD1.5 y SDXL; pod para la rama FLUX.2.
- **Adaptación**: la importación del LoRA desde Hugging Face con token `read` (la vía del video) queda documentada como procedimiento para Comfy Cloud; en el pod el LoRA se sube por scp, que es más simple y evita dejar un secreto en la nube.
- **Entregable**: la **tabla de modelos del estudio** — qué modelo para qué lámina, con la evidencia de las corridas.
- **Cierre**: la tabla existe con las seis variantes (SD1.5, SDXL, FLUX.2, FLUX.2+LoRA 0,5, +0,8, +1,0).
- **Estado**: pendiente. Precondición: stack FLUX.2 en el pod.

### WF-03 · Rhino a imagen, upscale y edición — módulo 3 (1 h 22 min 14 s)

- **Origen**: `[00:01:58]` "upscale by" ×3 · `[00:06:18]` factor de escalado · `[00:14:52]` "creativity" del enhancer · `[00:25:19]` proyecto de LLM con el INSTRUCTION.md · `[00:31:18]` prompt JSON con *STRICT CAMERA LOCK* · `[00:33:19]` la geometría va en la primera imagen · `[00:39:45]` planos en negro = loggias · `[00:56:21]` LoRA conectado al CFG Guider · `[00:58:12]` fuerza 1,5 rompe la imagen · `[01:08:38]` inpainting con máscara.
- **Grafos**: tres. (a) `workflow_rhino_to_imagen.json`, que ya existe con 23 nodos — `UNETLoader` + `LoraLoaderModelOnly` + doble `ReferenceLatent` encadenado + `FluxKontextMultiReferenceLatentMethod` (`index`) + `Flux2Scheduler` (4 pasos) + `CFGGuider` (cfg 1,0) + `SamplerCustomAdvanced` (`euler`, seed 42) — y se versiona en la carpeta nueva. (b) `workflow_upscale_local.json`. (c) `workflow_edicion_inpaint.json`.
- **Corre en**: pod para (a); local para (b) y (c).
- **Adaptación**: el upscale con Topaz (`creativity` 1 a 9) se resuelve con `RealESRGAN_x4plus` + Hires fix, donde la creatividad se controla con el denoise del segundo sampler y con el prompt de detalle. La edición con Nano Banana 2 y el inpaint se resuelven con `sd-v1-5-inpainting-fp16` + IPAdapter + DA3.
- **Precondiciones**: las tres pasadas exportadas desde Rhino (`geo_shaded`, `geo_lines`, foto de material) y el stack FLUX.2 en el pod.
- **Cierre**: tres corridas A desde la volumetría del concurso, con la geometría verificada contra el modelo.
- **Estado**: el grafo (a) ya existe como JSON; falta documentarlo en la carpeta nueva y correrlo.

### WF-04 · Imagen a video — módulo 4 (26 min 22 s)

- **Origen**: `[00:01:42]` ramas en bypass · `[00:02:33]` escala de créditos · `[00:03:31]` resolución · `[00:03:58]` duración · `[00:04:41]` prompt coach · `[00:09:25]` probá en 480 y volvé a 1080 · `[00:11:17]` anotaciones de color sobre la imagen · `[00:12:03]` el prompt se escalona en tramos de segundos · `[00:13:22]` transición suave, plano continuo · `[00:16:36]` dos clips de 4 s montados · `[00:19:17]` time-lapse de trípode fijo · `[00:21:43]` interpolación de fotogramas 7 s → 14 s.
- **Grafos**: tres. `workflow_video_ltxi2v.json`, `workflow_timelapse.json`, `workflow_interpolacion.json`.
- **Corre en**: pod con LTX; Comfy Cloud Free para calibrar Seedance.
- **Adaptación**: Seedance 2.0 queda como referencia de costo y calidad; la producción usa LTX, que es la vía abierta y ya estaba prevista en `n_04-video`. Las anotaciones de color del curso (círculo rojo y círculo azul) se conservan como guía de encuadre y se traducen a máscara en el grafo local.
- **Cierre**: un clip de 15 s con la plaza del concurso, en 1080 y con la interpolación aplicada.
- **Estado**: pendiente. `n_04-video/README.md` tiene el pipeline LTX-2.3/WAN que se reconcilia con este workflow.

### WF-05 · Imagen a 3D — módulo 5 (19 min 33 s)

- **Origen**: `[00:00:49]` nodo Hunyuan3D (`3.0`, 500k, `low poly` / `normal` 105 cr / `geometry`) · `[00:02:08]` export OBJ · `[00:03:12]` escala a cota real · `[00:05:43]` multiview · `[00:07:27]` las nueve preparaciones · `[00:13:50]` el AO es la favorita · `[00:17:07]` multiview de 4 tiles · `[00:18:11]` frontal + izquierda + atrás + derecha.
- **Grafos**: dos. `workflow_prep_3d.json` (las nueve variantes de preparación, adaptadas a SDXL + ControlNet + DA3) y `workflow_img2_3d.json` (Hunyuan3D o Tripo3D del pack abierto).
- **Corre en**: local para la preparación; pod para el 3D.
- **Adaptación**: el AO, que el video llama "la favorita", se produce con profundidad de DA3 y se usa como imagen de entrada limpia; el multiview de 4 tiles se genera con cuatro prompts de encuadre.
- **Cierre**: una malla del objeto del proyecto importada en Rhino y escalada a cota.
- **Estado**: pendiente. Requiere instalar `ComfyUI-3D-Pack` y sus modelos en el pod.

### WF-06 · Criterio del jurado — módulo 6 (Round Table, sin subtítulos)

- **Origen**: el video expone 404 en sus dos pistas de subtítulos. El contenido es la apertura de Cas Esbach (SCAD, miembro del jurado): transferencia conceptual por encima de transferencia estilística.
- **Trabajo**: bajar el audio del CDN del curso (el archivo `play_720p.mp4` del módulo, 538 MB) a `activos/curso-ai-gaudi/videos/` y transcribirlo en local con faster-whisper mediante `scripts/transcribir-leccion-bunny.py`.
- **Entregable**: `flujos/flujo-06-round-table.md` + `criterio/criterio-jurado.md` con los cinco puntos que el jurado mira, convertidos en **checklist de cierre de cada workflow**.
- **Cierre**: el checklist existe y cada WF lo tiene copiado en su `04-backlog.md`.
- **Estado**: script listo para la primera corrida; la transcripción queda para la sesión del 29/10.

### WF-07 · Flujo Gaudí — módulo 7 (35 min 42 s)

- **Origen**: `[00:08:19]` la lógica de Gaudí, no su estética · `[00:09:34]` el asistente se exporta del tablero como markdown · `[00:12:47]` el dial de intensidad 0-10 (7 en el primer ejemplo, 8 en el segundo) · `[00:14:10]` paso 1: `Load Image` + Nano Banana 2 + `Save Image` + `Compare Images`, a 2K con razonamiento "high" · `[00:17:14]` la geometría se fija en el paso 1 y la estética en el paso 2 · `[00:21:29]` el encuadre que mejor funciona es el detalle de fachada o el primer plano · `[00:31:21]` el LoRA sigue la geometría exactamente · `[00:35:00]` el encuadre a la altura de los ojos.
- **Grafos**: `workflow_gaudi_paso1_arcilla.json` (nuevo) y el paso 2 es el WF-03 con el LoRA.
- **Corre en**: pod.
- **Adaptación**: el paso 1 del curso usa Nano Banana 2 (nodo partner); aquí se resuelve con FLUX.2 klein 9B en modo edición y el prompt que produce el agente a partir del INSTRUCTION.md variante B — el mismo texto que el video instala como instrucciones de proyecto. El dial 0-10 se documenta como parámetro de proyecto, con la tabla de bandas que ya está en `03-nodos-WFrhino_to_image.md`.
- **Cierre**: el par arcilla + hiperreal del proyecto del concurso, con la geometría verificada entre los dos pasos.
- **Estado**: el INSTRUCTION.md variante B ya está archivado; falta el grafo del paso 1.

---

## 5. Método: construcción y revisión, uno por uno

Cada workflow recorre seis pasos y frena en un gate humano.

| # | Paso | Qué produce | Quién |
|---|------|--------------|-------|
| 1 | **Ficha de flujo** | `flujos/flujo-0X-<slug>.md`: la transcripción volcada a flujo, con valor de tiempo y con "qué dice el video / qué hacemos nosotros" | ficha de la 2.ª sección de §3 |
| 2 | **Grafo** | `workflow_<nombre>.json` (API format, ids correlativos, `_meta.title` en los nodos con rol editorial) + `03-nodos-<nombre>.md` con una sección por nodo: *Campo · Valor · Justificación* | agente |
| 3 | **Validación estática** | cada `class_type` y cada widget contra `/object_info` del servidor destino; cada modelo contra el disco | agente (`create_workflow` validate, `node_info`, `resolve_missing`) |
| 4 | **Corridas** | tres corridas idénticas (letra A) más una variante (letra B), con el `02-WF-log` completo: seed, cfg, steps, modelo, strength, tiempo, VRAM | agente + Sol |
| 5 | **Revisión** | Sol ve las salidas y el `03-nodos`; decide seguir, ajustar o cambiar la adaptación | **gate HITL** |
| 6 | **Cierre** | `01-index` con configuración mínima y precondiciones, `04-backlog` con lo pendiente, checklist del jurado satisfied; el WF pasa a v1.0 | agente |

**Nomenclatura de salidas**: `gx-{LETRA}-{NN}.png` (A baseline · B prompt · C parámetros · D modelo · E resolución · F ControlNet/img2img), versión en el prefijo del workflow. Los binarios viven en `salidas/`, que entra al `.gitignore`.

**Lo que la revisión tiene que poder responder**: ¿el grafo hace lo que dice la ficha? · ¿la adaptación mantiene el resultado pedagógico del curso? · ¿qué valor queda como parameter de proyecto? · ¿qué se documenta como límite?

---

## 6. Estructura y convenciones

```
proyectos/concurso-gaudi-nexus/
├── index.md                     ← puerta de entrada (frontmatter de proyecto)
├── flujos/                      ← una ficha por módulo (la transcripción hecha flujo)
│   ├── 00-index.md
│   └── flujo-01…07-*.md
├── workflows/
│   ├── 00-index.md              ← mapa WF ↔ módulo ↔ estado
│   └── WF-01-base/ … WF-07-flujo-gaudi/
│       ├── 00-README.md · 01-index.md · 02-WF-log-WF<nn>.md
│       ├── 03-nodos-WF<nn>.md · 04-backlog.md
│       ├── salidas/ · PLANS/ · SPECS/
│       └── workflow_<nombre>.json
└── criterio/
    └── criterio-jurado.md       ← el checklist de cierre de cada WF
```

**Reglas nuevas para `reglas-workflows-comfy.md`:**

- **R2 — escala según el modelo.** R1 (ImageScale 512×512) sigue siendo la regla de SD1.5. En FLUX.2 el escalado es a megapíxeles con `ImageScaleToTotalPixels` (1,0 MP para la geometría, 0,5 MP para la referencia de material, `lanczos`) y el upscale final es `ImageUpscaleWithModel` + Hires fix. En los workflows de la carpeta del concurso, R1 queda en pausa y R2 manda.
- **R3 — nomenclatura de salidas del concurso.** `gx-{LETRA}-{NN}.png`, con `gx` por el proyecto y la letra con el mismo significado de A a F.
- **R4 — validación estática antes de la corrida.** Todo workflow se valida contra `/object_info` del servidor destino y contra el disco antes de encolar; el resultado de la validación queda en `02-WF-log`.

---

## 7. Milestones y calendario

| ID | Fecha | Gate Go / No-Go | Cierra |
|----|-------|-----------------|--------|
| M-C1 | 31/10 | Entorno verificado, WF-01 con tres corridas, criterio del jurado transcrito | sprint 1 |
| M-C2 | 07/11 | WF-02 completo y tabla de modelos del estudio | sprint 2 |
| M-C3 | 14/11 | WF-03 validado en pod, geometría verificada | sprint 3 |
| M-C4 | 21/11 | WF-04 con un clip de 15 s | sprint 4 |
| M-C5 | 28/11 | WF-05 con malla en Rhino a escala | sprint 5 |
| M-C6 | 05/12 | WF-07 con el par arcilla + hiperreal y la lámina candidata | sprint 6 |
| M-C7 | 12/12 | A1 compuesta (≤15 MB JPEG) y dossier de método | sprint 7 |
| — | **16/12** | **entrega (23:59 GMT-7)** | |

Cada sprint tiene su propio gate Go/No-Go: si un workflow no cierra en su sprint, el siguiente sprint empieza por el pendiente y el resto se reprograma. La prioridad ante un incumplimiento es la cadena de la entrega (WF-03 → WF-07 → lámina), y el resto se mueve.

---

## 8. TASKS

### Sprint 1 · 28/10 → 01/11 (22 pomodoros ≈ 9,2 h)

**Sol — infraestructura y corridas**

- [ ] **S1 — Levantar el ComfyUI local y verificar el entorno** · 2 pom · `P:\00-repos\ComfyUI\corre_comfyui_background.bat` → validar `/object_info`, `models/` y el inventario real contra lo que dice el §1.2 · **Cierre:** tabla de nodos disponibles y lista de class_type utilizables · M-C1
  - [ ] S1.1 Levantar el servidor y confirmar `127.0.0.1:8188/system_stats` · 15 min
  - [ ] S1.2 Listar `class_type` disponibles y cruzar con los workflows planeados · 30 min
  - [ ] S1.3 Confirmar en disco los modelos de §1.2 y los que faltan · 15 min
- [ ] **S2 — Transcribir el módulo 6 (Round Table)** · 3 pom · bajar el `play_720p.mp4` a `activos/curso-ai-gaudi/videos/` con el `Referer` del CDN y correr `scripts/transcribir-leccion-bunny.py` · **Cierre:** `flujos/flujo-06-round-table.md` con la transcripción en inglés y su resumen en español · M-C1
- [ ] **S3 — Armar el pod y subir el stack** · 2 pom · crear el pod desde la plantilla de RunPod, subir los 18,3 GB de FLUX.2 y el LoRA de 120,8 MB · **Cierre:** una corrida de humo en el pod · M-C2 · requiere OK de gasto
- [ ] **S4 — WF-01 completo** · 4 pom · grafo + `03-nodos` + tres corridas A + `02-WF-log` · **Cierre:** WF-01 en v1.0 con revisión registrada · M-C1

**Ambos — documentación**

- [ ] **B1 — Planes de Comfy Cloud y créditos de los nodos partner** · 2 pom · completar el §2.3 con los precios verificados en `comfy.org/pricing` y con el costo por corrida de cada partner node · **Cierre:** tabla de costos fechada · M-C1
- [ ] **B2 — Volcar las siete fichas de flujo** · 3 pom · `flujos/flujo-01…07` con valor de tiempo, tablas de modelos, prompts literales y la lista de vacíos que el video deja · **Cierre:** `flujos/00-index.md` con el mapa módulo ↔ ficha ↔ workflow · M-C1
- [ ] **B3 — Estructura de la carpeta del concurso** · 2 pom · `index.md`, `workflows/00-index.md`, `criterio/` y las reglas R2, R3 y R4 en `reglas-workflows-comfy.md` · **Cierre:** estructura navegable y `.gitignore` con `proyectos/concurso-gaudi-nexus/**/salidas/` · M-C1
- [ ] **B4 — Escribir este plan** · 2 pom · `specs/261028-plan-workflows-adaptados-curso-ai-gaudi.md` · **Cierre:** plan en el vault, con pregunta abierta incluida · M-C1

**Emilia — curaduría**

- [ ] **E1 — Depurar las fichas contra las transcripciones** · 2 pom · revisar los siete documentos: idioma rioplatense, nombres propios, timestamps y la lista de vacíos · **Cierre:** fichas corregidas y un anexo de vacíos por módulo · M-C1

### Sprints 2 a 7 (resumen)

| Sprint | Foco | Cierra |
|--------|------|--------|
| 2 · 04-10/11 | WF-02 comparativa (local + pod) + tabla de modelos | M-C2 |
| 3 · 11-17/11 | WF-03: render desde Rhino, upscale y edición | M-C3 |
| 4 · 18-24/11 | WF-04: video, timelapse e interpolación | M-C4 |
| 5 · 25/11-01/12 | WF-05: 3D, multiview y retorno a Rhino | M-C5 |
| 6 · 02-08/12 | WF-07: arcilla y estética; lámina candidata | M-C6 |
| 7 · 09-15/12 | Composición de la A1, dossier de método y entrega protegida | M-C7 |

---

## 9. Carga a Leantime

- **Tablero destino**: proyecto 6 "Proyecto Pi - Concurso Gaudi Nexus" (ya existe; el plan 261019 cargó ahí el sprint 28 con los milestones 537-542 y 13 cards).
- **Qué se carga de este plan**: un sprint nuevo por cada milestone M-C1 a M-C7, con las cards de las tareas de §8 y sus subtareas. Los milestones ya cargados se referencian, no se recrean.
- **Unidades**: 25 min por pomodoro; `planHours` = 0,42 h por pomodoro; máximo 16 pomodoros por día y por persona; WIP ≤ 2.
- **Orden de carga** (15 min): (1) sprint de M-C1 con las nueve tasks de §8; (2) los siete milestones como Go/No-Go con su fecha; (3) las cards de los sprints 2 a 7 como backlog con su criterio de cierre; (4) asentar en `log.md`.
- **Bloqueante**: la carga espera el `s` explícito.

---

## 10. Riesgos y avisos honestos

1. **El reloj**: 7 semanas y el WF-03 tiene bloqueantes conocidos (capturas de Rhino, stack en el pod, LoRA premium). El plan sostiene la prioridad en la cadena de la entrega.
2. **Licencias**: FLUX.2 klein 9B es Non-Commercial (admisible en concurso, no en trabajo de cliente) · el LoRA premium tiene licencia sin confirmar. Pregunta pendiente al instructor: trigger word, modelo base, variante `.advanced`, licencia y uso en concurso.
3. **PI y nube**: la tensión entre "nunca concurso en cloud" y el render en RunPod queda en el ADR-002, a escribir antes de la primera corrida en el pod.
4. **DirectML y VRAM**: `--lowvram` resulta inoperante con DirectML (`comfy/model_management.py:121` fuerza `lowvram_available = False`); el arranque para FLUX.2 es `--directml --disable-dynamic-vram --reserve-vram 1.0`. Los `.bat` actuales siguen mandando `--lowvram`: unificación pendiente.
5. **Preprocesadores**: `comfyui_controlnet_aux` no está instalado, así que hoy corren `Canny` y DA3 (core). El WF-05 se apoya en DA3 y el pack 3D cubre el resto.
6. **Documentación desactualizada**: la skill `corre-comfyui.md` usa un juego de flags reducido y una ruta vieja (`P:\00-repos\vault-arquitectura`); `pbk-comfyui.md:63` documenta un launch distinto al de los `.bat`.
7. **LoRA premium**: no está en el Drive del curso; la descarga es desde la web del instructor, con precio durante el concurso.
8. **Módulo 6 sin subtítulos**: el módulo depende de la transcripción local; el audio está en el CDN del curso y se baja con el `Referer` correspondiente.
9. **Los nodos partner pueden cambiar de precio o de disponibilidad**: cada workflow tiene su ruta local equivalente, y el plan de Comfy Cloud es el techo de gasto.
10. **Registro visual de la A1 sin cerrar**: el §1.2 de `261019` pide croquis con variación leve de perspectiva y `research:672` propone axonometría renderizada con before/after. La decisión define cuál workflow produce la imagen de la entrega.

---

## 11. Preguntas abiertas

1. **Registro visual de la A1**: ¿fotorreal (WF-03 + WF-07) o croquis + variación leve (WF-01 + WF-02)? Define la prioridad de los siete workflows.
2. **Equipo**: ¿el equipo se completa hasta cuatro personas? ¿Entra Kiki y con qué rol?
3. **Modelo IA de la Fundació**: ¿el LoRA del curso con mención cumple el requisito, o se entrena uno propio en el pod (klein 4B Apache 2.0, ~$1, 2-3 h)?
4. **Tope de gasto**: ¿cuánto autorizamos para los nodos partner de Comfy Cloud en total?
5. **LoRA premium**: ¿se compra, o el trabajo queda con el basic que ya está en disco?
6. **Cadencia**: ¿el plan operativo se abre en sprints quincenales (la forma que propone `261019`) o semanales (la que organizan los milestones M-C1 a M-C7)?

---

## 12. Fuentes

**Curso (transcripciones propias)**

- [[raw/yt/transcripts/2026-10-21_mux-intro-generative-ai.es|Transcripción M1]] · [[raw/yt/transcripts/2026-10-21_mux-text-to-image.es|M2]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-image.es|M3]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-video.es|M4]] · [[raw/yt/transcripts/2026-10-21_mux-image-to-3d.es|M5]] · [[raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.es|M7]] · [[raw/yt/transcripts/indice-curso-ai-gaudi|Índice del curso (playback IDs, tablero Miro, contraseña)]]
- [[proyectos/MVP_04-comfyui-arquitectura/extraccion-material-curso-ai-gaudi|Extracción del material del curso]] · [[raw/research/2026-10-20-miro-curso/miro-inventario|Inventario del tablero Miro]] · [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|Informe del LoRA y del curso]]

**Estudio**

- [[specs/261019-plan-concurso-gaudi-nexus-ia|Plan del concurso]] · [[proyectos/STUDIO_OS-Emilia/presentacion/08-propuesta-mes2-cad-urbano|Propuesta CAD → Rhino → ComfyUI → A1]] · [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image|WF-rhino-to-image]] · [[proyectos/MVP_04-comfyui-arquitectura/n_04-video|n_04-video]] · [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|Reglas de workflows]] · [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] · [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] · [[wiki/glosario/software/flux2-klein-9b|FLUX.2 Klein 9B]] · [[wiki/glosario/software/lora-rhino-to-image-gaudi|LoRA rhino-to-image]] · [[proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp|Rhino MCP]] · [[wiki/glosario/conceptos/payback|payback]]

**Web (verificada el 2026-10-21 y el 2026-10-28)**

- [AIxGaudi — competitions.archi](https://competitions.archi/competition/aixgaudi-a-new-format-integrating-advanced-ai-course-and-an-international-architecture-competition/) (200)
- [Comfy Cloud — Pricing (planes, créditos, límites, API)](https://comfy.org/pricing/) (200)
- [RunPod — Pricing (3090 $0,22/h, 4090 $0,34/h, A40 $0,35/h)](https://www.runpod.io/pricing) (200)
- [Comfy — Custom nodes on Cloud](https://support.comfy.org/articles/6791455062-custom-nodes-on-cloud) (200)
- [Comfy — Partner Node Data Retention (24 h y reenvío a terceros)](https://docs.comfy.org/tutorials/partner-nodes/data-retention) (200)
- [Fundació Antoni Gaudí — Briefing del concurso](https://fundacionantoniogaudi.org/concurso_arq_2026/GxAI_BRIEFING_ES.pdf) (verificado 2026-10-20)

---

## 13. Registro de cambios

| Fecha | Cambio |
|------|--------|
| 2026-10-28 | Primera versión. Siete workflows definidos en orden de curso, matriz de adaptación, método de revisión, milestones M-C1 a M-C7 y sprint 1 cargado con 22 pomodoros. |
