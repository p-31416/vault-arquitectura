# miro_board_inventory — notas

Script para inventariar un tablero de Miro: qué videos tiene, qué workflows de ComfyUI, qué enlaces, qué tarjetas y qué módulos (frames).

> Uso:
> ```
> P:\Anaconda\envs\comfyenv\python.exe scripts\miro_board_inventory.py --url "https://miro.com/app/board/uXjVHRM2XQU=/" --token %MIRO_ACCESS_TOKEN%
> P:\Anaconda\envs\comfyenv\python.exe scripts\miro_board_inventory.py --file "C:\descargas\tablero.miro"
> ```

---

## 1. Qué es Miro y por qué hay dos formas de entrar

Un tablero de Miro es una **página web con objetos encima**. Los objetos se llaman *items* y cada uno tiene un `type`: `card`, `text`, `shape`, `sticky_note`, `image`, `document`, `frame`, `embed`, `link`.

Hay dos caminos para leerlos:

| Camino | Cómo | Requiere |
|--------|------|----------|
| **Export (offline)** | La UI permite bajar el tablero: **CSV** (export to spreadsheet), **backup `.rtb`**, **PDF** o imágenes | Sesión iniciada en el tablero |
| **API REST** | `GET https://api.miro.com/v2/boards/{board_id}/items` | Token OAuth con scope `boards:read` |

### Qué export conviene (verificado en la ayuda de Miro, 2026-10)

| Export | Qué trae | Para nosotros |
|--------|----------|---------------|
| **Export to spreadsheet (CSV)** | Una fila por item: texto, descripción/URL de la tarjeta, tags. Disponible en **todos los planes** (Chrome, Safari, Firefox, app de escritorio) | **El preferido**: el script lo parsea y sale la lista de videos y workflows |
| **Download board backup (`.rtb`)** | El tablero completo (los `.miro` antiguos). Solo **owner/co-owner** en equipos pagos, tope 1 GB | El más rico, si te habilitan la opción |
| **Save as PDF (Best/vector)** | Una página por frame. Los links son clicables solo en calidad vectorial | Para **leer** el tablero; el script rescata las URLs del PDF |
| **Save as image (PNG/JPG/SVG)** | Solo imagen | No aporta datos: sirve de archivo visual |
| **Board export API** | ZIP con SVG/HTML + recursos, PDFs, comentarios, colaboradores | Solo **Enterprise** |

La exportación puede estar **restringida por el dueño del tablero** (*board content settings*): si el menú no te muestra la opción, hay que pedirle al owner que habilite "Export board" para colaboradores.

### Cómo lo parsea el script según el archivo

```python
if ext == ".csv":  -> items_desde_csv(ruta)     # una fila por item
if ext == ".pdf":  -> items_desde_pdf(ruta)     # URLs y textos de las páginas
if es ZIP:         -> busca el JSON con más items
si no:             -> items_por_urls(ruta)      # escaneo binario de URLs
```

El **escaneo binario** es la red de seguridad: aunque el `.rtb` sea un formato propietario, las URLs (embeds de video, links a workflows) quedan escritas en el archivo y se recuperan con una expresión regular sobre los bytes.

## 2. El `board_id` y el `=` final

En la URL `https://miro.com/app/board/uXjVHRM2XQU=/`, el id del tablero es **`uXjVHRM2XQU=`**: un identificador en base64 con padding. El `=` del final es parte del id.

```python
m = re.search(r"/board/([^/?#]+)", entrada)   # captura "uXjVHRM2XQU="
```

Si se quita el `=` (por ejemplo, por normalizar el URL), la API responde **404** y parece un problema de permisos cuando en realidad es el id.

> Ojo: el material de los módulos del curso tiene derechos del curso y de la Fundació Antoni Gaudí. El vault guarda el **inventario** (qué hay, dónde está) y las transcripciones para curaduría interna; la redistribución de videos y materiales del curso queda fuera de lo que hacemos.

## 3. La paginación por cursor

Miro no usa `offset`: usa un **cursor opaco**.

```
GET /v2/boards/{id}/items?limit=50           -> {data:[...], total: 137, cursor:"MzQ1ODc2..."}
GET /v2/boards/{id}/items?limit=50&cursor=... -> siguiente tanda
```

El script corta cuando vuelve `cursor` vacío o cuando ya juntó `total` items.

## 4. Cómo se lee un item

```json
{
  "id": "3074457362577955300",
  "type": "embed",
  "data": {"url": "https://youtu.be/abc12345678", "html": "<iframe ...>"},
  "links": [{"rel": "preview", "url": "https://miro.com/app/board/..."}],
  "position": {"x": 120, "y": -430}
}
```

El script junta URLs de **tres lugares**: `links[]`, `data.url` y el `data.html` (los embeds traen el iframe como texto HTML), más las URLs que aparezcan escritas en el texto de la tarjeta.

## 5. La clasificación

Cada URL se pasa por una lista de patrones **en orden**, y gana el primero que matchea. Por eso los específicos van primero:

```python
("youtube", re.compile(r"(youtube\.com/(watch\?|embed/|playlist)|youtu\.be/)", re.I)),
...
("comfy_cloud", re.compile(r"(cloud\.comfy\.com|comfy\.cloud|app\.comfy\.org)", re.I)),
```

El orden importa: `comfy_cloud` tiene que ir **antes** que `comfy_wf` y antes que `otro`; y `youtube` antes que cualquier patrón genérico de http.

## 6. Salida

Dos archivos en la carpeta de salida:

- `miro-inventario.md` — para leer: conteo por tipo, listas con enlaces y títulos.
- `miro-inventario.json` — para máquinas: todos los items crudos + el índice clasificado.

Al final imprime los **ids de YouTube** deduplicados, listos para:

```cmd
P:\Anaconda\envs\comfyenv\python.exe scripts\transcribir_youtube.py <video_id>
```

## 7. Errores frecuentes

| Síntoma | Causa | Fix |
|---------|-------|-----|
| 404 en la API | `board_id` sin el `=` final | Volver a copiarlo de la URL |
| 401 / 403 | token sin scope `boards:read` o expirado | Regenerar el token con el scope correcto |
| Inventario vacío | tablero privado para ese token | Usar el modo `--file` (export desde la UI) |
| Faltan videos | los embeds de YouTube a veces guardan solo el `html` | El script ya lee `data.html`; si sigue faltando, revisar el embed a mano |

## 8. Verificación

Probado el 2026-10-20 con un `.miro` de laboratorio (4 items: frame, embed, card, link). Resultado: 2 videos con id de YouTube, 1 workflow, 1 tarjeta, 1 módulo. En modo API el flujo está contrastado contra la documentación oficial (`get-items`, `boards:read`, paginación por cursor).
