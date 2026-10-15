# Notas de `yt_takeout_parser.py`

> Lectura linea por linea del script. Cuando hagas el proximo Takeout, corre este
> mismo script y tu documento se regenera solo.

## Comando para ejecutarlo

```
P:\Anaconda\envs\comfyenv\python.exe scripts\yt_takeout_parser.py
```

Si ves errores de emojis en la consola (aparecen como `??`), agrega esto antes:

```
$env:PYTHONIOENCODING="utf-8"
P:\Anaconda\envs\comfyenv\python.exe scripts\yt_takeout_parser.py
```

## Que hace, paso a paso

### 1. Encuentra las carpetas del Takeout

```python
LISTDIR = _find(YTDIR, "*reproducci*n*")
```

Google Takeout nombra las carpetas segun el idioma de tu sistema. Puede venir
`listas de reproducción` o `listas de reproduccion`. En vez de escribir el nombre
a mano (y que se rompa si tenes Windows en otro idioma), usamos `glob()` que
busca por patron.

`_find()` te da un error claro si no encuentra nada, en vez de un traceback raro.

### 2. El truco de los sufijos (`_norm`)

Este es el bug mas importante que resolvi. Fijate:

| En el maestro de Takeout | En el archivo de videos |
|---|---|
| `IA/🎨gen_Img` | `IA_🎨gen_Img-vídeos.csv` |
| `Watch later` | `Watch later-vídeos.csv` |

El maestro tiene el **titulo de YouTube** (con `/`), el archivo tiene el **mismo
titulo pero con `_` en vez de `/` y el sufijo `-vídeos`** (con tilde!).

`_norm()` hace tres cosas para que puedas compararlos:
1. pasa a minusculas
2. quita acentos (`í` -> `i`)
3. saca el sufijo `-vídeos`

Entonces ambos lados quedan como `ia_🎨gen_img` y el match es exacto.

### 3. Los headers con tilde (el otro bug)

Cuando csv.DictReader no encuentra la clave exacta, tira `KeyError`. Los headers
del maestro tienen tildes:

```python
# MAL (no existe esa clave exacta por la tilde)
meta["Titulo de la lista de reproduccion (original)"]

# BIEN (indice posicional)
titulo = meta[list(meta.keys())[3]]
```

Por eso el script usa indices (`[0]`, `[1]`, `[2]`, `[3]`) en vez de nombres. Es
menos legible pero no se rompe.

**Si Takeout cambia el orden de columnas**, mira la primera linea del CSV y
ajusta los numeros.

### 4. Cruza Watch Later con las listas tematicas

```python
en_wl = "Si" if vid in wl_set else ""
```

`wl_set` es un `set` de IDs. Buscar en un set es instantaneo (no recorre la lista
entera). Por eso con 259 videos y 450 tematicos no se traba.

### 5. Filtra los canales por keywords

```python
def clasificar(canal):
    n = _norm(canal["nombre"])
    for cat in CATS:
        for k in CATS[cat]:
            if _norm(k) in n:
                return cat
    return None
```

Cada canal va a la **primera** categoria que matchee. El orden de `CATS` importa:
las keywords especificas van primero. Si pones `"bim"` antes de `"revit"`, todos
los canales de Revit caen en la categoria de "bim" en vez de "software arq".

### 6. Escribe el markdown

```python
OUT.write_text("\n".join(L), encoding="utf-8")
```

Acumula todas las lineas en una lista `L` y las junta con `"\n"` al final. Es mas
rapido que escribir linea por linea al archivo.

## Como actualizar las keywords

Edita el diccionario `CATS` en el script. Cada categoria es una lista de palabras
que se buscan dentro del nombre del canal (no hace falta que coincidan exactas,
con que aparezca la palabra alcanza).

Ejemplo: si te subscribiste a `Rhino Grasshopper Tutoriales`, agregas
`"grasshopper tutorial"` a la lista de `software arq`.

Despues corres el script de nuevo y el documento se regenera con la nueva
clasificacion.

## Que falta (Nivel 2)

- **Canales nuevos despues del Takeout**: Takeout es una foto del momento en que lo
  exportaste. Si subscribiste a un canal nuevo despues, no aparece hasta el
  proximo Takeout. Para eso es el CRON de n8n con RSS (`yt_rss_check.py`, pendiente).
- **Titulos**: resuelto el 2026-10-08 con `scripts/yt_titles.py` (YouTube Data API v3,
  cache en `raw/yt/cache-titulos.json`). Si el cache no existe, el parser sale
  sin titulos (solo IDs) y avisa en el doc.

## Ampliacion 2026-10-08 (parte 2): tags + categorias amplias

### Keywords nuevas

Se agregaron tags que faltaban y tus propios titulos usaban:

| Tag nuevo | Keywords | Por que |
|---|---|---|
| `3dsmax` | 3ds max, v-ray, corona | Adan Martin usa 3ds Max con IA |
| `video-ia` | sora, runway, kling, veo 3, pika, luma, hailuo | Tu carpeta IA/gen_Vid no tenia tag |
| `audio-ia` | suno, elevenlabs, udio | El video de Suno caia en sin-clasificar |
| `opencode` | opencode | MoureDev, Darellanodev, kiburld hablan de eso |
| `remotion` | remotion | Hiciste sesion de Remotion el 05-10 |
| `dibujo` | pixelart, procreate, dibujo, sketching | Conecta con MVP_01 (dibujo con IA) |
| `gestion` | power bi, notion, gantt, leantime | Grid Studio: Python + Power BI para proyectos |
| `whatsapp` | whatsapp | Nicolas Dubois: bots de WhatsApp |
| + en `vibe-coding` | windsurf, copilot, codex, claude code, spec-kit, mouredev | Tus WL hablan de eso |
| + en `llm` | gpt-6, gpt astra, deepseek | GPT-6 Astra salio este mes |
| + en `metaverso` | quest, vision pro, steam vr | VrPatch: Quest 3, Steam Frame |
| + en `viz` / `planos` | 3d model, fachada, facade | PlanFinder: floor plans en browser |

Efecto medido: `sin-clasificar` 157 -> 131, `vibe-coding` 9 -> 39,
`agents` 25 -> 41, `llm` 67 -> 86.

### Stemming de plurales (`_kw_pat`)

El bug: `floor plan` no matcheaba `floor plans`. La solucion: singularizar la
keyword (quitar la `s` final, salvo `ss`) y agregar `s?` opcional al regex:

```python
"agents"  ->  patron "agents?"  ->  matchea "agent" y "agents"
"floor plan" -> patron "floor plans?" -> matchea ambas formas
```

Sin esto, cada keyword habria que escribirla dos veces (singular + plural).

### Filtro de fechas (`_es_fecha`)

Algunos titulos traen la fecha adentro y el fallback del slug la recogia como
tag (`2026-09-15`). Ahora se filtra con regex `^\d{4}(-\d{2}(-\d{2})?)?$`.

### Categorias amplias (`CATEGORIAS_AMPLIAS` + columna `Cat`)

Los ~40 tags son lo fino; las 7 categorias son lo grueso para filtrar rapido:

| Categoria | Tags que incluye |
|---|---|
| `software-arq` | rhino, grasshopper, revit, autocad, twinmotion, unreal, blender, freecad, sketchup, lumion, maket, 3dsmax |
| `ia-imagen` | comfyui, stable-diffusion, midjourney, nanobanana, flux, upscaling |
| `ia-video-audio` | video-ia, audio-ia, remotion |
| `ia-agentes-code` | llm, agents, vibe-coding, opencode, n8n, whatsapp |
| `construccion` | 3d-print, concreto, modular, aislamiento, madera |
| `diseno-arq` | viz, dibujo, planos, interior, parametrico, sostenibilidad, metaverso, nft |
| `gestion` | marketing, gestion |

`categoria_de()` devuelve la primera categoria que matchea (el orden del dict
define la prioridad). Los slugs de carpeta se resuelven con `SLUG_CAT` (mapeo
manual de tus 16 carpetas, ej `ia-workflowsautom` -> `ia-agentes-code`).

Distribucion medida por fila: ia-agentes-code 196, software-arq 134,
ia-imagen 124, diseno-arq 70, construccion 28, ia-video-audio 14,
gestion 12, vacio 131 (= los sin-clasificar).

## Veredictos manuales 1-60 (2026-10-08, parte 3)

### Formato (`raw/yt/veredictos.json`)

```json
{"videos": {"<video_id>": {"v": "filosofia|personal|otros|descartar|rescatar|proyecto",
                           "tema": ["tag-forzado"], "nota": "..."}}}
```

El parser lo carga en PASO 0b y `aplicar_veredicto()` lo aplica DESPUES de
inferir (el veredicto manda sobre el algoritmo):

| Veredicto | Tags resultantes | Cat |
|---|---|---|
| `filosofia` / `personal` / `otros` | solo ese tag | vacia (listado, no analizado) |
| `descartar` | `descartado` | vacia (archivado, sigue en Takeout) |
| `rescatar` + tema | tema primero + inferidos sin duplicar | la del tema |
| `proyecto` | `proyecto` + inferidos como contexto | la del contexto |

Regla de oro: **un video juzgado no vuelve a sin-clasificar al regenerar**.
Por eso los veredictos viven en JSON aparte, no en el .md generado.

Los items 1-60 de `revision-manual.md` quedaron backfilleados en su columna
veredicto (los inferidos 18/36/45/55 van marcados como tales).

### Tags nuevos de esta tanda

| Tag | Keywords clave | Origen (veredicto) | Categoria |
|---|---|---|---|
| `magnific` | magnific | #15: soft generacion imagen | ia-imagen |
| `charlas` | charla, masterclass, documental, documentary, keynote, ted talk, tedx, conferencia, summit, tim fu | #16,27,35-40,55: apartado propio de charlas | (ninguna: cruza categorias, se filtra por tag) |
| `ai-3d` | 3d ai, text/image to 3d, tripo, triposplat, meshy | #31 TripoSplat | ia-imagen |
| `diagramas` | diagrama, diagram | #29 Kyle Sinko | diseno-arq |
| `repos` | github, repositorio | #19: listar repos interesantes | ia-agentes-code |
| `notebook` | notebook, commonplace, segundo cerebro, da vinci, obsidian | #14 proyecto davinci-notebook, #33 | gestion |
| `hardware` | router, hardware, servidor, nas, raspberry | #20 router viejo | gestion |
| `arq` | arquitectura, architecture, architectural, architect, arquitecto, mvrdv, zaha, bauhaus | faltaba lo obvio: 118 videos la usan | diseno-arq |
| `filosofia` | jung, schopenhauer, tao, huxley, seneca, budd, meditacion... | #1-10,30,32,41,46,47 | (ninguna: listado, no analizado) |
| en `llm` | gemini (bare), nicolas dubois, reemplazar/reemplazo | #28 profesor IA, #34, #57 | ia-agentes-code |
| en `vibe-coding` | josema | #11 Josema Fernandez | ia-agentes-code |
| en `n8n` | automatizacion/automatizar/automatizado/automatic/automation/automated/automatico/automatica | #42 facturacion ARCA | ia-agentes-code |
| en `nft` | decentraland, tokenizacion | #21, bugfix -cion | diseno-arq |

Efecto medido: `sin-clasificar` 131 -> 62. `arq` nuevo con 118. `charlas` 20.

### Ideas de proyecto detectadas (no son tags, van a sesion)

- **#14 davinci-notebook**: version digital del cuaderno de Da Vinci con todo
  (commonplace book + segundo cerebro + vault). Proyecto a scafoldear.
- **#19 repos**: extraer links de GitHub de descripciones de videos (requiere
  API/transcripts: Nivel 2).

## Veredictos 1-60 dictados (2026-10-08, parte 4)

Distribucion: filosofia 13, otros 22, rescatar 21, descartar 3, proyecto 1.
Mas el video MAGNIFIC real (WL#135, `qWB7p_n-jDA`): rescatar magnific.
Total en `veredictos.json`: 61.

Aclaracion importante: el #15 de revision-manual NO es MAGNIFIC (es Show It
Better, workflows arq+IA, tema arq+agents). El MAGNIFIC real esta en WL#135.

### Tags agregados en esta tanda

| Tag | Keywords | Origen |
|---|---|---|
| `decentraland` | decentraland (sacado de `nft`, tag propio pedido) | #21 |
| `tecnologia` | via `hardware`: tecnologia, tecnologico | #20 router viejo |
| `arq` | + `architettura` (italiano, DAD Dipartimento) | #35 MVRDV |
| `llm` | + `ia` suelto (con limites de palabra es seguro), `gemini` bare | #28, #34, #57 |
| `vibe-coding` | + `josema` | #11 |
| `n8n` | ya tenia automatizacion/* (cubre #42 ARCA) | #42 |

Efecto medido: `sin-clasificar` 131 -> 51. `llm` 86 -> 202 (el "ia" suelto
en titulos ES es casi siempre IA real; los limites de palabra evitan
falsos como via/guia/energia). `arq` 118. `charlas` 20.

### Regla filosofia/personal (decision del estudio)

`filosofia`, `personal`, `otros`, `proyecto`, `descartado` y `charlas` NO
tienen categoria amplia a proposito (`categoria_de` devuelve vacio):
se LISTAN pero no se analizan en este vault. Las charlas cruzan todas las
categorias (una charla puede ser de IA, de arq o de filosofia): se filtran
por tag `charlas`, no por Cat. Los co-tags igual dan Cat (ej
`charlas`+`arq` -> `diseno-arq`).

## Veredictos 61-131 dictados (2026-10-08, parte 5)

Distribucion de la tanda: rescatar 19, otros 46, descartar 8.
Total en `veredictos.json`: 132 (131 Parte 1 + MAGNIFIC WL#135).

Veredictos clave:

| # | Video | Veredicto |
|---|---|---|
| 61-63 | Gaussian Splatting x3 (Corridor, Postshot, 3DGS) | rescatar gaussian-splatting+repos |
| 64, 66 | Videos largos IA | rescatar video-ia |
| 65 | Charla Latorre IA sin miedo | rescatar charlas+llm |
| 67 | Xavier cerebro digital | rescatar llm+notebook |
| 68, 69 | Webs / Google Maps leads | descartar |
| 70-73 | Gemma 4, academia Medina, herramientas, Entrala | rescatar llm |
| 74 | AI Studio apps (no dictado) | rescatar vibe-coding+llm (inferido) |
| 75 | NotebookLM MIT | rescatar llm+notebook |
| 76, 77 | CapCut / novedades viejas | descartar |
| 78 | 10 AI tools architects (Salmaan) | rescatar arq+llm |
| 79 | Alejavi clickbait | descartar (canal sigue) |
| 80-82, 84-85, 89, 92-105 | Cursos, INFJ, Mayim, Veritasium, etc. | otros |
| 83 | ArchiTech Talk BIG+D5 | rescatar charlas+arq |
| 86-88 | Xavier x2, Migue Baena | descartar video (keep creators) |
| 90-91 | Bloomberg, Filo News Rieznik | rescatar llm |
| 106-111 | Bucket personal (incluye 110 IA-cuantica: respetar dictado) | otros |
| 112 | Illustrator (no dictado) | otros, confirmar |
| 113-120 | Bucket personal (120 TEDx: confirmar vs regla TED) | otros |
| 121-130 | Bucket personal (121 arq-tech 3D mouse: confirmar) | otros |
| 131 | Tom Bilyeu AI reset | rescatar charlas+llm |

### Tags/keywords agregados en esta tanda

| Cambio | Por que |
|---|---|
| `gaussian-splatting`: gaussian, splatting, splating, nerf, postshot, fotogrametria, photogrammetry, lidar, escaneo 3d, 3d scan | 61-63: 3D no-IA con repo |
| `llm` += `gemma`, `herramienta`, `tools`, `academia ia`, `ai agency` | 70, 72, 71 |
| `notebook` += `cerebro digital` | 67 |
| `viz` += `d5` | 83 BIG+D5 |
| `decentraland` ya existia (verificado en doc: 1 fila) | 21 |

`gaussian-splatting` mapeado a `diseno-arq` (tecnica de viz 3D).

Tres conflictos marcados para confirmar (dictado vs reglas previas):
`rPh3c8Sa37M` (TEDx en bucket personal), `8TBoQdE91CE` (arq-tech en bucket
personal), `fH8Bu3RpaL8` (IA-cuantica en bucket personal). Se respeto el
dictado; el estudio confirma.

## Veredictos Parte 2: 47 canales rescatados (2026-10-08, parte 6)

El estudio dicto veredictos para 47 de los 113 canales fuera de scope.
Registro en `raw/yt/canales-veredictos.json` (formato espejo de
`veredictos.json`: `{channel_id: {v, categoria, nombre, nota}}`).

Distribucion: arq+IA 14, software arq 16, IA general 5, construccion 4,
creadores 3, estudios intl. 1, metaverso 4 (nueva categoria).

### Nueva categoria `metaverso` en CATS

Spatial, Decentraland, VrPatch y Jacobsen no encajaban en las 9 categorias.
Se agrego `metaverso` al FINAL del dict para no mover matches existentes
(ej Metaverse Architecture Biennale sigue en NFTs/tokens: `metaverso` no
matchea `metaverse`). Keywords especificas, nada generico como `vr` suelto
(romperia todo por substring).

### Keywords agregadas por categoria

| Categoria | Keywords nuevas |
|---|---|
| arq+IA | paul hansen, adan martin, salmaan, alphonso peluso, za_lab, future architecture, myn3d, archi lab, design input, bydavidparra, urban decoders, atelier designa, landspace, tedeschi |
| software arq | ifc, architecture vanguard, architechtures, tokar, alex luna, show it better, planfinder, algorithmix, render reboot, marco virtual, martin cipoletta, kirdeikis, architech network, mcneel, especialista 3d |
| estudios intl. | schumacher |
| IA general | pixeleasel, nicolas dubois, ai search, monzon, xr ai spotlight |
| construccion | slant 3d, formlabs, anycubic, bugeo |
| creadores | ted, archizoom, digitalfutures |

Efecto medido: scope 44 -> 91, fuera 113 -> 66. Conciliado exacto:
47 IDs del JSON = 47 dictados (script de conciliacion, 0 faltantes, 0 sobrantes).

### Bugs de matching encontrados y corregidos

1. **Faltaba `tedeschi`**: el keyword `ted` (para TED) capturaba a Arturo
   Tedeschi en `creadores` antes de llegar a su categoria. Fix: keyword
   `tedeschi` en arq+IA (el dict se evalua en orden, arq+IA gana).
2. **Faltaba `especialista 3d`**: el #100 no tenia keyword (se dicto la fila
   pero se omitio el keyword). Fix: agregado.
3. **`pixeleasel` sin espacio**: el keyword viejo `pixel easel` nunca matcheaba
   `PixelEasel`. Fix: keyword sin espacio en IA general.
4. **`za_lab` con guion bajo**: `_norm` conserva `_`, el keyword lleva `_`.
5. **`ifc` trae un auto-incluido**: Ifc Architect (#93, dictado) entra por el
   mismo keyword. Correcto y registrado.