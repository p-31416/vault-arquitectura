---
tipo: guia
mvp: 04
fecha_creacion: 2026-10-20
ultima_actualizacion: 2026-10-20
tags: [mvp_04, comfyui, curso-ai-gaudi, gaudi, miro, archademy, extraccion, workflows, videos]
---

# Extracción del material del curso AI×Gaudí (Miro + Archademy)

> Cómo se saca el material del curso: **videos** (para transcribir) y **workflows** (JSON importables). Verificado el 2026-10-20: las dos fuentes están **protegidas con login**, así que el trabajo humano es el de abrir sesión y bajar el export; el trabajo de máquina es el de inventariar y ordenar.

## 0. Qué hay en cada lado

| Fuente | URL | Qué guarda | Acceso |
|--------|-----|-----------|--------|
| Área de participantes | `https://archademy.ai/my-account/my-competitions/214/?tab=course` | Lecciones del curso, videos, enlaces a recursos, descargas | Login de participante |
| Tablero de workflows | `https://miro.com/app/board/uXjVHRM2XQU=/` | "Virtual Whiteboard": decenas de workflows de ComfyUI listos para importar, material de referencia | Login (tablero del curso) |

El curso entrega además: el **LoRA exclusivo** (el `rhino-to-image` que ya analizamos), el **LoRA de la Fundació Antoni Gaudí** (otro archivo, pendiente de pedir), **Comfy Cloud** (96 GB, ~US$25/mes) y el acceso a los mirrors de los modelos.

### Datos del concurso (verificados en la web pública, 2026-10-20)

| Dato | Valor |
|------|-------|
| Entrega | **16 de diciembre de 2026, 23:59 GMT-7** |
| Formato | Lámina **A1 online, máx. 15 MB, JPEG** (+ A4 opcional para el Premio de Diseño de la Fundació) |
| Tema | «Mercado de Proximidad» + «Centro de Cultura Digital» y la reconfiguración de la plaza de la Sagrada Família (exceso de turismo) |
| Premios | 1.º US$6.000 · 2.º US$2.000 · 3.º US$1.000 · Premio de Diseño de la Fundació US$1.000 · 10 menciones · 50 finalistas |
| Inscripción | US$175 por equipo (hasta 4 personas) hasta el 4/11 · US$295 del 5/11 al 2/12 · US$345 del 3 al 16/12 |
| Módulos | 7, **en inglés con subtítulos**: 1 IA generativa + tablero Miro · 2 texto→imagen · 3 imagen→imagen («Rhino-to-Image») · 4 imagen→vídeo · 5 imagen→3D · 6 mesa redonda · 7 flujo de trabajo de Gaudí |
| Profesor | Thomas Nelissen (Davis AI) + Cas Esbach (SCAD, módulo 7) |

Briefings públicos: [EN](https://archademy.ai/wp-content/uploads/2026/09/GxAI_BRIEFING_EN.pdf) · [ES](https://archademy.ai/wp-content/uploads/2026/08/GxAI_BRIEFING_ES.pdf) · bases del concurso en [gaudi2026.org](https://gaudi2026.org/es/index.html).

---

## 1. Miro — tres caminos, del más simple al más pro

### Vía A · Export desde la UI (sin tokens, la más rápida)

**Formato preferido: CSV** (`Export to spreadsheet`). Es el único disponible en **todos los planes** y para colaboradores, y trae una fila por item con el texto, la URL y los tags — justo lo que el script necesita.

1. Entrá al tablero con la sesión iniciada.
2. `⋯` → **Export** → **Export to spreadsheet (CSV)**.
3. Pasá el archivo al script:

```cmd
P:\Anaconda\envs\comfyenv\python.exe scripts\miro_board_inventory.py --file "C:\descargas\tablero.csv" --out "raw\research\2026-10-20-miro-curso"
```

**Alternativas** (según lo que te habiliten):

| Export | Cuándo | Cómo lo lee el script |
|--------|--------|----------------------|
| **Download board backup (`.rtb`)** | Si sos owner/co-owner del tablero: es el richest (todo el tablero) | ZIP → busca el JSON con más items; si no es ZIP, escaneo binario de URLs |
| **Save as PDF (Best/vector)** | Para **leer** el tablero: una página por frame, links clicables | Extrae las URLs y los textos de las páginas |
| **Save as image (PNG/JPG/SVG)** | Archivo visual del tablero | Sin datos: no aporta al inventario |
| **Board export API** | Solo planes Enterprise | No aplica al curso |

> Si el menú no te muestra la exportación, el dueño del tablero la tiene restringida (*board content settings*): hay que pedirle al owner que habilite "Export board" para colaboradores.

### Vía B · API REST (para automatizar y repetir)

1. Creá una app en <https://developers.miro.com> y autorizá el scope **`boards:read`**.
2. Guardá el token en `.env` como `MIRO_ACCESS_TOKEN=...`.
3. Corré:

```cmd
P:\Anaconda\envs\comfyenv\python.exe scripts\miro_board_inventory.py --url "https://miro.com/app/board/uXjVHRM2XQU=/" --out "raw\research\2026-10-20-miro-curso"
```

La API pagina con **cursor** (no offset): `GET https://api.miro.com/v2/boards/{board_id}/items?limit=50&cursor=...` → devuelve `data`, `total`, `cursor`. El `board_id` es el token de la URL (`uXjVHRM2XQU=`), **con el `=` final**: sin él la API responde 404.

### Vía C · Web SDK (sin salir del navegador)

Con el tablero abierto y la app creada: en la consola del navegador, `miro.board.getItems()` devuelve los items del tablero. Sirve para una mirada rápida o para prototipar sin instalar nada.

### Qué devuelve el inventario

| Bloque | Para qué |
|--------|----------|
| **Videos** | Con el **id de YouTube** listo para transcribir (also detecta Vimeo, Loom, Wistia) |
| **Workflows de ComfyUI** | Links a `cloud.comfy.com` y a `.json` (los importables) |
| **Tableros Miro** | Tableros hijos, PDFs y links a los cursos |
| **Tarjetas / frames** | Los títulos: cada frame suele ser un módulo del curso, cada tarjeta una instrucción |

---

## 2. Archademy — área de participantes

### Vía A · Guardar el HTML (la más simple)

**Tres teclas y un pegado:**

1. Abrí la página del curso con tu sesión y **esperá a que cargue todo** (hacé scroll hasta el final).
2. `Ctrl+A` → `Ctrl+C`.
3. Abrí el Bloc de notas, `Ctrl+V`, y guardá el archivo como **`curso.txt`** en `C:\Users\Solch16\Downloads\` (en "Tipo" elegí **Todos los archivos**, y en "Codificación" **UTF-8**, para que no se rompan los acentos).

El script lo lee igual (las URLs se buscan en el texto plano), así que **`.txt` sirve perfectamente**. Si preferís el HTML con formato, `Ctrl+S` → tipo **Páginas web completas (*.html)**.

```cmd
P:\Anaconda\envs\\comfyenv\\python.exe scripts\archademy_curso_inventory.py --html "C:\Users\Solch16\Downloads\curso.txt" --out "raw\research\2026-10-20-archademy-curso"
```

> Si con el pegado no salen los videos, es que la página los carga por AJAX: usá la Vía B (cookies) o pedime el HTML de cada lección.

### Vía B · Descarga con las cookies de la sesión

1. `F12` → pestaña **Network** → recargá la página → click en la primera peticion.
2. **Request Headers** → copiá el valor de `Cookie`.
3. Guardalo en un archivo (una línea) y corré:

```cmd
P:\Anaconda\envs\comfyenv\python.exe scripts\archademy_curso_inventory.py --url "https://archademy.ai/my-account/my-competitions/214/?tab=course" --cookies-file "C:\descargas\cookies.txt" --out "raw\research\2026-10-20-archademy-curso"
```

> Las cookies son credenciales de sesión: tratá el archivo como secreto, no lo subas al repo ni lo pegues en un canal. El vault no lo versiona.

### Por qué hacen falta las dos

La página del curso es un área de participantes: cada lección puede tener su propia URL y su propio video. Un solo guardado puede no traer todos los videos. La estrategia es: primero el índice (Vía A o B) para ver **qué lecciones existen**, y después ir lección por lección.

---

## 2.1 La página es dinámica: así se saca igual (y ya está hecho)

**Lo que quedó resuelto el 21/10/2026:** los videos del curso están embebidos con **Mux** (`iframe.mediadelivery.net/embed/{env}/{playback_id}`) y **cada módulo expone sus subtítulos en WebVTT** (`https://{prefijo}.b-cdn.net/{PLAYBACK_ID}/captions/{en|es}.vtt`), que se descargan **sin token** (200 directo). Los subtítulos **son** la transcripción: no hay que bajar video.

El HTML guardado por `Ctrl+S` ("páginas web completas") alcanza, porque los iframes y los `data-module` quedan en el markup. Con eso:

```cmd
P:\Anaconda\envs\comfyenv\python.exe scripts\mux_lecciones_curso.py "G:\Mi unidad\OS-Emilia\AIxGaudi\My account - Archademy.ai.html" --out "raw\yt\transcripts"
```

| Módulo | Cues EN | Cues ES |
|--------|---------|---------|
| Introduction to Generative AI | 1268 | 1268 |
| Text-to-Image | 659 | 659 |
| Image-to-Image | 1047 | 1047 |
| Image-to-Video | 333 | 333 |
| Image-to-3D | 249 | 249 |
| The Gaudí Workflow | 454 | 454 |
| Round Table | — (404, sin subtítulos) | — |

Salida: `raw/yt/transcripts/YYYY-MM-DD_mux-<slug>.<lang>.md+.srt+.txt` + `indice-curso-ai-gaudi.json`.

**Bonus**: la misma página trae la **contraseña del tablero Miro** (`archademy-miro-pw-code`): `Gaudi2026` — tablero `https://miro.com/app/board/uXjVHRM2XQU=/`.

### Si hay que repetirla (por si cambia algo)

**Forma 1 — colector de consola** (trae todo de una vez, incluso lo que carga por AJAX):

```javascript
(() => {
  const items = [];
  document.querySelectorAll('iframe,video,a[href]').forEach(e => {
    const src = e.src || e.href || '';
    if (src) items.push({tag: e.tagName, src, text: (e.innerText || '').slice(0,140)});
  });
  const out = {page: location.href, title: document.title, items, text: document.body.innerText};
  copy(JSON.stringify(out, null, 2));
  console.log('Copiado al portapapeles:', items.length, 'enlaces. Pegalo en un archivo.');
})()
```

Guardá el resultado como `curso.json` y:

```cmd
P:\Anaconda\envs\comfyenv\python.exe scripts\archademy_curso_inventory.py --html "C:\Users\Solch16\Downloads\curso.json" --out "raw\research\2026-10-20-archademy-curso"
```

**Forma 2 — copiar la respuesta del XHR**: `F12` → **Network** → filtrá **Fetch/XHR** → click en la petición del listado de lecciones → clic derecho → **Copy** → **Copy response** → `curso.json` → mismo comando.

**Atajo por lección**: `F12` → **Elements** → buscá `<iframe` → el `src` te da el video; si es `youtube.com/embed/XXXX`, el id es `XXXX` y se transcribe con `scripts\transcribir_youtube.py XXXX`.

## 3. De los videos al vault

**Dato clave del curso:** la web de Archademy dice *"siete módulos en inglés (con subtítulos)"*. Es decir: **los videos traen subtítulos**, y el camino más liviano no es descargar el video sino leer los subtítulos. Eso lo hace el script que ya tenemos, en 1-2 requests y sin bajar un solo byte de video.

```cmd
$env:PYTHONIOENCODING="utf-8"
P:\Anaconda\envs\comfyenv\python.exe scripts\transcribir_youtube.py <video_id_o_URL>
```

Qué hace, en orden: (1) busca **subtítulos manuales**; (2) si no hay, **subtítulos automáticos**; (3) si tampoco, **baja solo el audio** y transcribe con `faster-whisper` local (ya instalado en `comfyenv`).

Salida: `raw/yt/transcripts/YYYY-MM-DD_<id>.<lang>.md+.srt+.txt+.origen.json` (el `.md` es el envoltorio visible en Obsidian, con frontmatter). Después, `@contenidos` formatea la ficha y, con tu OK, la mueve a `wiki/fuentes/`.

### Si el video no está en YouTube

| Situación | Cómo |
|-----------|------|
| Vimeo u otra plataforma | `python -m yt_dlp --cookies-from-browser chrome "<url>" -o "raw\yt\videos\%(id)s.%(ext)s"` |
| MP4 propio del LMS (con token) | `F12` → Network → filtrar `media`/`.mp4` → copiar la URL → `python -m yt_dlp --referer "https://archademy.ai/" "<url>" -o "raw\yt\videos\%(id)s.%(ext)s"` |
| El player pide la sesión abierta | `--cookies-from-browser chrome` (cerrá Chrome antes: en Windows el profile está bloqueado) |

> Los videos del curso son material con derechos del curso y de la Fundació Antoni Gaudí: el vault guarda el **inventario** y las transcripciones para curaduría interna. La redistribución queda fuera.

### Los **workflows** van al revés

Se bajan los `.json` y se archivan en `proyectos/MVP_04-comfyui-arquitectura/` siguiendo la nomenclatura de cada WF, con su `00-README` y entradas en el log.

---

## 4. Estado

| Ítem | Estado |
|------|--------|
| LoRA `rhino-to-image` analizado | ✅ (rank 16, FLUX.2 klein 9B) |
| Workflow «Rhino-to-Image» montado y validado | ✅ (`n_05-rhino-mcp/WF-rhino-to-image/`) |
| **Tablero del curso exportado** | ✅ `AI-course.csv` (219 filas, 72 secciones) → `raw/research/2026-10-20-miro-curso/` |
| **Prompt oficial del curso extraído** | ✅ INSTRUCTION.md del módulo 3 y del módulo 7 + esqueleto JSON, en el WF |
| **Variante `.premium` detectada** | ✅ `rhino-to-image-lora-premium.safetensors` (descarga vía `thomasnelissen.ai`) |
| **Strength que usa el curso** | ✅ 50 % y 100 % (comparación del módulo 2) |
| `scripts/miro_board_inventory.py` | ✅ probado con CSV, backup binario y HTML de laboratorio |
| `scripts/archademy_curso_inventory.py` | ✅ probado con HTML de laboratorio |
| Índice del área de participantes (videos) | ⬜ requiere el texto de la página con la sesión abierta |
| LoRA de la Fundació Antoni Gaudí | ⬜ el tablero lo lista en el módulo 7 (sección `RHINO-TO-GAUDI`) |
| Token de la API de Miro | ⬜ opcional (solo para automatizar) |

## 4.1 Qué contiene el tablero del curso (hallazgo del 20/10)

El CSV no es un tablero de workflows: es el **índice de recursos y prompts** del curso. 72 secciones, 147 tarjetas. Lo que importa para el estudio:

| Sección | Contenido |
|---------|-----------|
| `MODULE 2 - TEXT-2-IMG` | Comparativa SD1.5 / SDXL / FLUX.1 / FLUX.2 Klein 9B / **+ LoRA 50 %** / **+ LoRA 100 %** · los dos LoRA (basic y premium) |
| `MODULE 3 - IMG-2-IMG` | **INSTRUCTION.md** del Rhino-to-Image + **esqueleto JSON** con *STRICT CAMERA LOCK* |
| `MODULE 4 - IMG-2-VIDEO` | Workflows LTX, Kling, Seedance 2.0 + el "Seedance director" (JSON, reglas de cámara y montaje) |
| `MODULE 5 - IMG-2-3D` | Prompts para pasar a 3D (modelo blanco, maqueta de hormigón, normal map, viewport Rhino, objeto en lightbox) |
| `MODULE 6 / 7 - GAUDI` | **INSTRUCTION.md** del Rhino-to-Gaudi (variante B, nombra a Gaudí) + el dial de intensidad 0-10 + los LoRA |
| `PROMPT COACH SETUP` / `COMFY EXPERT SETUP` | Los system prompts del curso (para conectar como assistants) |
| `CLAUDE SKILLS` | Extensiones Gemini CLI: `nanobanana`, `seedance-director` (instalables con `gemini extensions install`) |
| `RELEVANT WEBSITES` | docs.bfl.ai (guías de prompting de FLUX.2), comfyui-wiki, kling.ai, ltx.io, seedance2.ai, stable-diffusion-art |

Los **workflows importables** están etiquetados con `IMPORTABLE IN COMFY` (los que no, con `NOT IMPORTABLE IN COMFY`): IMAGE-EDIT FLUX.2 KLEIN 9B, RHINO-TO-IMAGE, SPECTRUM, UPSCALING 1-4 (SeedVR2, TOPAZ, FLUX.1, Krea).

## 5. Qué pedirle al instructor (una sola vez)

1. **Trigger word** del LoRA `rhino-to-image` y del LoRA de la Fundació.
2. **Modelo base** exacto (`klein-9B` destilado o `klein-base-9B`) y si existe la variante `.advanced`.
3. **Workflow JSON del módulo 3** (o acceso al tablero Miro).
4. **Licencia** del LoRA y del material de la Fundació para uso en concurso.
5. **Video del módulo 7** (Gaudí LoRA: lógica constructiva, no estética) — es el que explica cómo usar el LoRA sin copiar el estilo.

---

## Conceptos relacionados

- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image|WF-rhino-to-image]] — flujo que usa el LoRA del curso
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]] · [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]]
- [[wiki/glosario/software/comfyui|comfyui]] · [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]]
- [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|research 2026-10-20]] — informe del LoRA, el entrenamiento y el curso
- [[wiki/fuentes/comfyui-for_architects-architutors|comfyui-for-architects]] — fuentes del curso ya curadas

## Referencias

- [Miro Developer Platform — Get items on board](https://developers.miro.com/reference/get-items-1) (verificado 2026-10-20 — cursor pagination, scope `boards:read`)
- [Miro Developer Platform — Boards](https://developers.miro.com/reference/get-board) (verificado 2026-10-20)
- [Miro REST API v2 — items](https://developers.miro.com/reference/get-items) (verificado 2026-10-20 — 404 en el slug nuevo; el vigente es `get-items-1`)
- [Miro — Exportar un tablero (ayuda)](https://help.miro.com/hc/en-us/articles/360017730233-Board-export) (verificado 2026-10-20)
- [Archademy — AI×Gaudí](https://archademy.ai/es/) (verificado 2026-10-20)
- [Fundació Antoni Gaudí — Briefing del concurso](https://fundacionantoniogaudi.org/concurso_arq_2026/GxAI_BRIEFING_EN.pdf) (verificado 2026-10-20)
