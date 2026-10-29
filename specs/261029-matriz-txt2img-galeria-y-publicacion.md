---
tipo: spec
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [spec, comfyui, matriz, txt2img, galeria, publicacion, pitau, skill, agentes, concurso]
estado: activo
---

# Matriz txt2img, galería de renders y publicación en pitau.tech

> Documento maestro de tres cosas que se apoyan entre sí: (1) el **protocolo de matriz** para entender el flujo de text-to-image con prompt y seed fijos, (2) la **galería web** que convierte los renders en algo que se recorre con un clic, y (3) el **plan de publicación** para que esa galería viva en `pitau.tech` y la vea Emilia. Cierra con el **reemplazo de los nodos de proveedor pagos** por alternativas open source y con la **skill del agente constructor de flujos**.

- [[#1 · La matriz txt2img]]
- [[#2 · La galería de renders]]
- [[#3 · Publicación en pitau.tech]]
- [[#4 · Nodos de proveedor pagos y su reemplazo open source]]
- [[#5 · El agente que construye flujos]]
- [[#6 · Decisiones abiertas]]

---

## 1 · La matriz txt2img

### El protocolo

Un prompt. Una seed. Una variable por fila. Con eso, la diferencia entre dos imágenes **es** la variable — y se puede atribuir.

| Elemento | Valor |
|---|---|
| **Prompt** (del proyecto) | *"a contemporary market and digital culture centre in Barcelona beside the Sagrada Familia, board-formed concrete and glass facade, colonnade of inclined columns, deep loggias, warm stone paving with market stalls, people for scale, photorealistic, architectural photography, morning light, sharp focus, highly detailed, 8k"* |
| **Prompt alternativo** (del curso, para comparar) | `concrete house in desert rocky landscape` |
| **Negativo** | `low quality, blurry, distorted, deformed, bad architecture, cartoon, sketch, watermark, text, signature, illustration, painting, oversaturated` |
| **Seed** | 42 en todas las filas |

### Las filas

| # | Bloque | Variable | Qué cambia | Corre en |
|---|---|---|---|---|
| M01–M02 | modelo | base | SD 1.5 (architecturerealmix) vs SDXL (Juggernaut XL) | local |
| M03–M08 | LoRAs SD 1.5 | LoRA | archviz · concepts · brutaltech · corbusier · room · superhighrise | local |
| M09–M13 | LoRAs SDXL | LoRA | massing · building · isometric · archviz XL · skyscraper | local (justo) |
| M14–M20 | parámetros | steps · cfg · sampler · resolución | 10/50 steps · cfg 3/12 · dpmpp_2m · 512² / 768² | local |

### Cómo corre

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\matriz-txt2img.py --bloque sd15
P:\Anaconda\envs\comfyenv\python.exe scripts\matriz-txt2img.py --bloque loras_sdxl
P:\Anaconda\envs\comfyenv\python.exe scripts\matriz-txt2img.py --dry-run --bloque todos
```

Los renders caen en `P:\00-repos\ComfyUI\output\matriz\` con prefijo `matriz/<base>/<ID>`, así que el índice y la galería los recogen solos. La tabla de resultados queda en `activos/web/galeria/matriz-txt2img.md`.

> **Por qué el bloque SDXL va aparte:** con `--lowvram --cpu-vae` y LoRAs rank 128, cada render SDXL tarda varios minutos y es el que mide el techo real de VRAM. Se corre cuando el bloque SD 1.5 ya dio la lectura rápida.

---

## 2 · La galería de renders

### El problema que resuelve

El índice (`INDICE-RENDERS.md`) tiene la trazabilidad completa de los 80 renders: prompt, seed, modelo, LoRA, sampler, steps, cfg. **Pero una tabla no se recorre**: no se ve la imagen, no se compara de un vistazo, no se llega con un clic a "la de al lado". El problema real con un tablero tipo Miro es ese: todo pegado en un lienzo infinito, y para recorrerlo hay que hacer zoom out cientos de veces.

### Qué es

Un sitio estático (HTML + JS en un archivo, sin dependencias) con:

- **Lienzo infinito** con pan y zoom, al estilo Magnific: arrastre para mover, rueda para zoom centrado en el puntero.
- **Una columna por workflow**, imágenes apiladas: la comparación por familia es inmediata.
- **Color estable por seed**: los renders de la misma seed comparten tono → se reconoce un grupo de un vistazo.
- **Clic en una ficha → panel lateral** con la imagen grande y toda la metadata (modelo, LoRA y fuerza, seed, steps, cfg, sampler, scheduler, resolución, prompt literal).
- **Recorrido lineal** con `◀ ▶` o las flechas del teclado, y una tira de miniaturas al pie: se avanza de una imagen a la siguiente sin volver al lienzo.
- **Filtros** por workflow y por "solo con LoRA", y **búsqueda de texto** dentro de los prompts.

### Qué no es

No publica nada. Genera archivos. Quien decide si eso sale a un dominio es otro (sección 3).

### Cómo se genera

```powershell
# 1. Reindexar (lee la metadata que ComfyUI graba dentro de cada PNG)
P:\Anaconda\envs\comfyenv\python.exe scripts\indice-renders-comfy.py --dir "P:\00-repos\ComfyUI\output" --out "proyectos\MVP_04-comfyui-arquitectura"

# 2. Generar la galería (copia las imágenes y arma el sitio)
P:\Anaconda\envs\comfyenv\python.exe scripts\galeria-renders.py --indice "proyectos\MVP_04-comfyui-arquitectura\INDICE-RENDERS.json" --out "activos\web\galeria" --raiz-indice "P:\00-repos\ComfyUI\output"
```

Salida: `activos/web/galeria/` → `index.html` (63 KB) · `datos.json` · `img/` (80 PNG, 45 MB). La carpeta está en `activos/`, o sea **fuera de git**.

---

## 3 · Publicación en pitau.tech

### El encaje con lo que ya existe

El VPS del estudio ya está montado como **EasyPanel + Traefik** con el dominio `pitau.tech` (n8n vive en `n8n.pitau.tech`). La galería encaja como un **servicio estático más**: un `nginx:alpine` que sirve una carpeta.

### El camino

| # | Paso | Qué | Dónde |
|---|------|-----|--------|
| 1 | Generar el sitio en la PC | `scripts/galeria-renders.py` | PC |
| 2 | Subirlo al VPS | `rsync`/`scp` de `activos/web/galeria/` al volumen del servicio | PC → VPS |
| 3 | Servirlo | servicio nginx + labels de Traefik (`rendes.pitau.tech` → `renders.pitau.tech`) | EasyPanel |
| 4 | Publicar el enlace | el agente lo anuncia en Telegram y queda en el log del vault | bot + vault |

### Tres decisiones que hay que tomar antes

1. **Público o con acceso.** El vault tiene una regla dura: *"para material del concurso, no usar el Comfy Agent: pasar el workflow por el chat online es mandar el grafo del concurso a un servicio externo"* y *"si se usa Comfy Cloud para material del concurso, subir solo imágenes derivadas, nunca los `.dwg` originales"*. Los renders **son** imágenes derivadas, pero son de un concurso con PI de la Fundació. La recomendación: **la galería del concurso va con basic auth** (Traefik o Caddy), y una galería de renders no sensibles puede quedar abierta.
2. **Sincronización.** Manual (uno empuja y avisa) o automática (un job que reindexa y sube). Automatizar tiene un costo: cada render nuevo sale a internet sin que nadie lo mire.
3. **Quién mira qué.** Emilia y Sol dentro del estudio; el jurado solo recibe la lámina A1, no la galería de proceso.

### Lo que la galería NO debe incluir

Los `.dwg`, los modelos de Rhino, las fotos de material con licencia de la Fundació y el prompt JSON del agente. Solo renders.

---

## 4 · Nodos de proveedor pagos y su reemplazo open source

### La tabla

| Módulo | Nodo pago del curso | Para qué | Reemplazo open source | Dónde corre | Qué se pierde | Qué se gana |
|---|---|---|---|---|---|---|
| 3 | **Topaz** (enhancer, creativity 1–9) | upscale con reinterpretación | RealESRGAN x4plus + Hires Fix (2º KSampler, denoise 0,15–0,35) | local | La reinterpretación semántica con prompt ("make details hyper realistic") | Gratis, determinista, ya en disco |
| 3 | **Magnific / Grok / Google** (upscale API) | upscale de alta calidad | Ídem, o FLUX.2 en pod para el upscale "de verdad" | local / pod | Calidad de detalle de los APIs | Sin créditos, sin que la imagen viaje a un tercero |
| 3 | **Nano Banana 2** (inpaint + image edit) | edición semántica de imagen | `sd-v1-5-inpainting-fp16` (ya en disco) + IC-Light (ya en disco) para re-iluminación | local | La lectura semántica de Gemini | Control total, costo cero, material que no sale de la máquina |
| 3 | **GPT Image** (partner node OpenAI) |同上 | Ídem | local | Ídem | Ídem |
| 3 | **FLUX.1** (upscale extra) | upscale de muy baja calidad | FLUX.2 klein 9B (el mismo del LoRA) | pod | Ídem | Un solo modelo base para todo |
| 4 | **Seedance 2.0** (320 créd por 7 s en 720p; 1.600 en 4K; 3.400 en 4K/15 s) | imagen → video | **LTX-2** con LoRAs de control (Depth/Canny/Pose) | pod | La calidad de movimiento de Seedance | Control de cámara por prompt, costo por imagen en vez de por video |
| 4 | **Google Omni** | video de alto nivel | LTX-2 / Wan 2.2 | pod | Idem | Mismo stack |
| 4 | **Kling 3.0** |同上 | LTX-2 | pod | Idem | Idem |
| 4 | **After Effects** (interpolación manual) | duplicar la duración del clip | ffmpeg + nodo de interpolación de fotogramas | local / pod | La interfaz de AE | Automatizable y versionable |
| 5 | **Hunyuan3D** (105–126 créd) | imagen → malla 3D | **ComfyUI-3D-Pack** (Hunyuan3D / TRELLIS, pesos abiertos) | pod | La simplicidad del partner | Sin créditos, malla local, se puede reentrenar |
| 5 | **Tripo 3.1 / Tripo multiview** (API) | imagen → malla, multiview | Ídem + 4 tiles con Depth Anything 3 (ya en disco) | pod | Idem | Ídem |
| 5 | **Nano Banana Pro** (preparación de imagen) | 9 variantes: maqueta blanca, hormigón, AO, normales, viewport Rhino, multiview | Depth Anything 3 + IC-Light + SD1.5 img2img; AO con el nodo nativo de oclusión | local | La lectura semántica de la variante | Las nueve variantes salen gratis y quedan documentadas |
| 2 | — | comparativa de modelos | — | local + pod | — | El módulo 2 **no tiene nodos pagos**: es la comparativa de checkpoints |

### Lectura del conjunto

El patrón es claro: **el curso paga por acceso a modelos cerrados donde nosotros tenemos un equivalente abierto o ya instalado**. La única fila donde el reemplazo es realmente peor es Seedance (video): la calidad de movimiento de un modelo cerrado no se iguala con un LoRA de control. Todo lo demás se resuelve con lo que ya está en la máquina o con el pod.

**Regla que sale de la tabla:** lo que entra a un nodo pago **sale de la máquina** (el prompt, la imagen y el resultado pasan por el proveedor). Con material del concurso, cada fila de la tabla tiene alternativa local o en pod — y por eso la regla "nada de material sensible a APIs de terceros" se puede cumplir sin resignar el flujo.

---

## 5 · El agente que construye flujos

### El problema con el Prompt Coach

El curso propone un "Prompt Coach": un proyecto de Claude con instrucciones pegadas que devuelve prompts JSON. Es un LLM disfrazado de asistente — y para lo que hace (traducir una idea a un prompt) está bien. **Lo que el curso no tiene es la otra mitad**: un agente que *construya el grafo* y lo *corra*, con acceso a la documentación oficial de ComfyUI.

Eso es lo que propose el estudio:

| | Prompt Coach (curso) | Agente constructor (estudio) |
|---|---|---|
| Entrada | una idea | una especificación ("un flujo que hace X con Y") |
| Salida | un prompt JSON | un `workflow_*.json` en API format, validado y ejecutado |
| Conocimiento | las instrucciones pegadas del tablero | `docs.comfy.org` + el `/object_info` del servidor destino + el inventario de modelos del disco |
| Dónde vive | en la nube (Claude / Comfy Cloud) | en el vault (skill versionada con el equipo) |
| Qué corre | el prompt en Comfy Cloud | el grafo en local, pod o cloud |

### El método (5 pasos, sin nodos de adivinación)

1. **Documentación** — leer `docs.comfy.org` del nodo que hace falta (el patrón `/built-in-nodes/<PascalCase>`).
2. **Especificación** — escribir qué hace el flujo, con qué nodos, con qué valores.
3. **Validación estática** — cada `class_type` contra el `/object_info` del servidor destino y cada archivo de modelo contra el disco (regla R4 del vault). Si un nodo no existe, se cambia la especificación; no se improvisa en la corrida.
4. **Construcción** — el grafo en API format, con ids correlativos y links `["id", salida]`.
5. **Corrida y log** — se ejecuta, se registra seed/prompt/tiempo/error en el `02-WF-log`, y las salidas van a `salidas/`.

### El método primero, la skill después

El orden que se decidió: **probar el método a mano con el video 1** (que es un grafo de 7 nodos del core, sin nodos pagos) y recién después escribir la skill. Así la skill describe un método que ya funcionó, no una intención.

La skill vivirá en `.opencode/skills/comfy-flow-builder/SKILL.md` y, cuando Hermes esté desplegado, se publica al volumen del agente con el mismo mecanismo de `scripts/studio_os_publicar_hermes.py` que usa `SOUL.md`. Para que Hermes construya flujos hace falta el **proxy de MCPs** del banco (F2.2 del MVP_07: `autocad`, `rhino`, `comfyui`).

---

## 6 · Decisiones abiertas

| Decisión | Estado | Nota |
|---|---|---|
| Dominio de la galería (`renders.pitau.tech`) | a definir | easy: servicio nginx + labels de Traefik |
| Pública o con basic auth | **a definir** | recomendación: auth para todo lo que sea del concurso |
| Sincronización manual o automática | a definir | automática implica publicar sin revisar |
| ¿Comfy Cloud de pago? | **diferido** | hasta gastar los 400 créditos gratis y medir qué falta |
| Cuándo la matriz SDXL | después del bloque SD 1.5 | es el que mide el techo de VRAM |
| Skill del agente: ¿en el vault o en Hermes? | en el vault, se publica a Hermes | un solo original, dos destinos |

## Conceptos relacionados

- [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]] — catálogo de los 17 LoRAs locales
- [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] — dónde renderizar y qué se puede
- [[proyectos/concurso-gaudi-nexus/index|concurso-gaudi-nexus]] — los siete workflows del concurso
- [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|Studio OS]] — Hermes, el vault como memoria y el proxy de MCPs
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/00-README|WF-loras-locales]] — calibración de LoRAs
- [[scripts/galeria-renders_notas|galeria-renders notas]] · [[scripts/matriz-txt2img_notas|matriz-txt2img notas]]
