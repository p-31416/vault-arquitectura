# archademy_curso_inventory — notas

Script para inventariar el área de participantes del curso AI×Gaudí (Archademy): lecciones, videos, workflows, PDFs y enlaces.

> Uso:
> ```
> P:\Anaconda\envs\comfyenv\python.exe scripts\archademy_curso_inventory.py --html "C:\descargas\curso.html"
> P:\Anaconda\envs\comfyenv\python.exe scripts\archademy_curso_inventory.py --url "https://archademy.ai/my-account/my-competitions/214/?tab=course" --cookies-file "C:\descargas\cookies.txt"
> ```

---

## 1. Por qué no alcanza con un `webfetch`

El área de participantes es una zona **con login**. Sin sesión, la respuesta es el formulario de acceso (verificado el 2026-10-20: `https://archademy.ai/my-account/my-competitions/214/?tab=course` devuelve el form de login, no el curso).

Por eso el script tiene dos entradas:

| Modo | Qué necesita | Cuándo usarlo |
|------|--------------|---------------|
| `--html` | Guardar la página con `Ctrl+S` desde el navegador con sesión | Simple, sin credenciales en la terminal |
| `--url` + `--cookies` | La cabecera `Cookie` de la sesión | Para bajar la página directo, o cuando el HTML guardado quedó incompleto |

## 2. Cómo se saca la cabecera Cookie

1. `F12` → pestaña **Network** → recargar la página → click en la petición principal (document).
2. **Request Headers** → copiar el valor completo de `Cookie`.
3. Guardarlo en un archivo de texto (una línea) y pasarlo con `--cookies-file`.

> **El archivo de cookies es una credencial de sesión**: no va al repo, no va a un canal, y se borra cuando termina la extracción. El vault no lo versiona.

## 3. Cómo funciona el parser

`html.parser` (librería estándar) alcanza: no hace falta BeautifulSoup.

### Modo HTML / texto

El `Extractor` es un `HTMLParser` que va anotando:

| Qué | Para qué |
|-----|----------|
| `title` | identificar la página |
| `h1..h5` | la **estructura del curso**: cada encabezado es un módulo o una lección |
| `iframe[src]` | el **video embebido** (YouTube/Vimeo/Loom) |
| `a[href]` + su texto | enlaces con nombre ("Leccion 3 - Rhino to Image") |
| `video[src]` | video en HTML5 |
| URLs sueltas en el texto | links escritos en párrafos |

En `handle_starttag` se abre el "buffer" de texto y en `handle_endtag` se cierra: por eso cada link queda con su etiqueta.

### Modo JSON (páginas dinámicas)

Cuando el archivo empieza por `{` o `[`, el script lo trata como **respuesta de un XHR** (o salida del colector de consola) y lo recorre **en profundidad**:

```python
def caminar(nodo):
    if isinstance(nodo, dict):   # busca title/name/lesson_title y sigue bajando
        ...
    elif isinstance(nodo, list): # lista de lecciones
        ...
    elif isinstance(nodo, str):  # cada string puede contener URLs
        ...
```

Motivo: el área de participantes del curso (WooCommerce) arma la pestaña `course` por sesión; el listado de lecciones y los videos llegan por XHR, no en el HTML inicial. Por eso el HTML guardado "a pelo" sale incompleto y lo que sirve es la respuesta JSON.

## 4. Qué se filtra (y qué no)

- Se **descartan** los `mailto:` y las anclas internas (`#...`).
- Se **descartan** los links internos que no apuntan a un archivo (`/mi-cuenta/`, `/catalogo/`), porque son navegación, no material.
- Se **conservan** los que terminan en `.json`, `.pdf` o `.zip`: son descargas (workflows importables, briefings, paquetes).

## 5. La clasificación

Igual que en el script de Miro, una lista de patrones en orden. Lo que importa para este curso:

| Etiqueta | Qué es | Para qué sirve |
|----------|--------|----------------|
| `youtube` | `youtube.com/watch`, `youtu.be`, `embed/` | **transcribir** con `scripts/transcribir_youtube.py` |
| `comfy_cloud` / `comfy_wf` | `cloud.comfy.com`, `.json` | **workflows importables** |
| `miro_board` | `miro.com/app/board/...` | el tablero de workflows → `scripts/miro_board_inventory.py` |
| `comfy_docs` | `docs.comfy.org` | documentación oficial |
| `pdf` | briefing, fichas | archivo en `raw/` |

El **id de YouTube** se saca con una expresión regular sobre la URL (`v=`, `youtu.be/`, `embed/`), y sale listo para pasarle al transcriptor.

## 6. Salida

- `archademy-curso-inventario.md` — índice legible con conteos y listas.
- `archademy-curso-inventario.json` — el índice en datos, para procesar.

## 7. Estrategia de uso (una pasada, tres pasos)

1. **Índice general**: guardar la página del curso → correr el script → ver la lista de lecciones y videos.
2. **Videos**: transcribir los ids con `scripts/transcribir_youtube.py` (de ahí a `raw/yt/transcripts/`).
3. **Workflows**: bajar cada `.json` y archivarlo en el WF que le corresponde en `proyectos/MVP_04-comfyui-arquitectura/`, con entrada en su `02-WF-log`.

## 8. Verificación

Probado el 2026-10-20 con un HTML de laboratorio que simulaba la página del curso: 3 videos (2 con id de YouTube, 1 Vimeo), 2 workflows (Comfy Cloud + `.json`), 1 tablero Miro, 1 PDF, 1 modelo en HF y la estructura de encabezados.
