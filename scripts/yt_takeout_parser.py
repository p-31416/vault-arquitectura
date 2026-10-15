"""
yt_takeout_parser.py — Parsea Google Takeout de YouTube + Chrome y genera
un documento unico de curacion en el vault.

QUE HACE
--------
1. Lee la lista de tus playlists (Listas de reproduccion.csv) y sus videos.
2. Lee tus suscripciones (canales que seguis) y filtra los que estan "en scope".
3. Cruza los videos de Watch Later con los de las listas tematicas para saber
   cuales ya estaban clasificados por vos.
4. Escribe UN solo markdown en raw/yt/ con:
   - Parte A: todos los videos guardados, agrupados por tu carpeta/listado
   - Parte B: los canales que quedaron fuera de scope, para que los revises

COMO EJECUTARLO
---------------
    P:\Anaconda\envs\comfyenv\python.exe scripts\yt_takeout_parser.py

Salida esperada: raw/yt/videos-y-canales-guardados.md

NOTA IMPORTANTE
---------------
No descarga nada de internet. Solo lee los CSV/HTML que Google Takeout dejo
en tu disco. Los titulos de los videos NO aparecen (solo video_id + fecha)
porque para eso haria falta la YouTube Data API. Eso llega en Nivel 2.
"""

import csv
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------- NOTA ES:
# Las rutas base. Ajustar si tu Takeout esta en otro lado.
# Path() es la forma "correcta" de manejar rutas en Python: no rompe con
# barras invertidas ni con espacios en los nombres de carpeta.
VAULT = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura")
TAKEOUT = Path(r"C:\Users\Solch16\Downloads\Takeout")

YTDIR = TAKEOUT / "YouTube y YouTube Music"
CHROME = TAKEOUT / "Chrome" / "Marcadores.html"

# Chrome puede exportar el archivo con o sin tilde en el nombre ('marcadores' vs
# 'Marcadores'). Buscamos por patron para no romper con el idioma del sistema.
def _buscar_marcadores():
    d = TAKEOUT / "Chrome"
    if not d.exists():
        return None
    for p in d.glob("*.html"):
        if "marcador" in p.stem.lower():
            return p
    return None

CHROME_FILE = _buscar_marcadores()

OUT = VAULT / "raw" / "yt" / "videos-y-canales-guardados.md"

# Cache de titulos que genera scripts/yt_titles.py con la YouTube Data API.
# Si no existe, el documento sale sin titulos (solo IDs), que es lo que pasaba
# antes de tener la APIkey.
CACHE_TITULOS = VAULT / "raw" / "yt" / "cache-titulos.json"


def _find(base, patron):
    """Busca un subdirectorio/archivo sin depender de acentos ni mayusculas.

    Takeout_exporta los nombres con la idioma del sistema, asi que pueden venir
    'listas de reproduccion', 'Listas de reproducción' o 'Listas De Reproduccion'.
    En vez de adivinar, buscamos por patron con glob().
    """
    hits = [p for p in base.glob(patron) if p.is_dir()]
    if not hits:
        raise SystemExit(f"ERROR: no se encontro '{patron}' dentro de {base}")
    return hits[0]


# NOTA ES: glob() es como un "buscar archivos" tolerante. El patron '*reproducci*n*'
# matchea tanto 'reproduccion' como 'reproducción' porque 'n' cubre la ene con o sin
# tilde... en realidad glob no distingue. Por eso usamos dos comodines alrededor.
LISTDIR = _find(YTDIR, "*reproducci*n*")
SUBDIR = _find(YTDIR, "suscrip*")
CHROME_DIR = _find(TAKEOUT, "Chrome") if TAKEOUT.exists() else None

# ---------------------------------------------------------------- NOTA ES:
# El orden en que aparecen las secciones del documento. Vos ya tenias un
# criterio: primero lo urgente (Watch Later), despues arquitectura (ARQ/),
# luego IA, y al final lo peripheral (libros, marketing).
# El nombre de cada seccion es el NOMBRE DEL ARCHIVO del Takeout (que lleva
# "_" donde vos usaste "/" en YouTube). Se usa asi para que los wikilinks
# internos de Obsidian no se rompan con el caracter "/".
ORDEN_LISTAS = [
    "Watch later-videos",
    "ARQ_3D-Print-videos",
    "ARQ_AutoCAD2D-videos",
    "ARQ_docs-videos",
    "ARQ_IA-videos",
    "ARQ_Rhino+Grasshopper-videos",
    "ARQ_Twinmotion-Unreal_Engine-videos",
    "IA_Metaverso-VR_AR-videos",
    "IA_Workflows(Autom.)-videos",
    "IA_gen_Agents-videos",
    "IA_gen_Img-videos",
    "IA_gen_Txt (LLMs)-videos",
    "IA_gen_Vid-videos",
    "IA_Vibe_Coding-videos",
    "libros-videos",
    "MKT_SEM_SEO-videos",
]

# ---------------------------------------------------------------- NOTA ES:
# Keywords por categoria. El orden de CATS importa: un canal se asigna a la
# PRIMERA categoria con la que matchea, asi que las mas especificas van primero.
# Esto se tunes con el feedback del estudio (2026-10-08): se eligio filtrar
# el ruido y dejar solo lo que es del rubro arquitectura + IA.
CATS = {
    "arq+IA": [
        "comfyui", "parametric", "archviz", "ai architect", "arquitectura",
        "architecture design", "midjourney architect",
        # Rescatados Parte 2 (2026-10-08, veredictos estudio):
        "paul hansen", "adan martin", "salmaan", "alphonso peluso",
        "za_lab", "future architecture", "myn3d", "archi lab",
        "design input", "bydavidparra", "urban decoders", "atelier designa",
        "landspace", "tedeschi",
    ],
    "software arq": [
        "autocad", "revit", "rhino", "grasshopper", "twinmotion",
        "unreal engine", "freecad", "archicad", "sketchup", "lumion",
        "vectary", "blender arch", "dynamo", "bim", "cad", "parametric house",
        "the revit kid", "scott detweiler", "lenscode", "maket",
        "hakan architecture", "arquitecto", "archdaily", "dezeen", "archinect",
        "designboom", "architizer", "how to rhino",
        # Rescatados Parte 2:
        "ifc", "architecture vanguard", "architechtures", "tokar",
        "alex luna", "show it better", "planfinder", "algorithmix",
        "render reboot", "marco virtual", "martin cipoletta", "kirdeikis",
        "architech network", "mcneel", "especialista 3d",
    ],
    "estudios intl.": [
        "big ", "zaha hadid", "oma", "foster", "renzo piano",
        "santiago calatrava", "herzog", "mvr", "snohetta", "sergison bates",
        "el croquis", "adjaye", "wiel arets", "david chipperfield",
        "tadao ando", "kengo kuma", "sou fujimoto", "studio gang", "bogdan",
        "shigeru ban", "sanaa",
        # Rescatados Parte 2:
        "schumacher",
    ],
    "IA general": [
        "llm", "chatgpt", "gpt", "claude", "gemini", "openai", "anthropic",
        "sora", "pika", "runway", "kling", "agent", "prompt", "llama",
        "mistral", "hugging face", "langchain", "crewai", "autogpt",
        "autogen", "vector db", "rag", "machine learning", "deep learning",
        "neural", "transformer", "ai art", "ai underground", "grid studio",
        "kedar undale", "the ai art", "beeyond ideas", "progress pursuit",
        "neurodivulgadores", "vibecoding", "vibe coding", "aideator",
        "prompting pixels",
        # Rescatados Parte 2:
        "pixeleasel", "nicolas dubois", "ai search", "monzon",
        "xr ai spotlight",
    ],
    "NFTs/tokens": [
        "nft", "tokeniz", "blockchain architecture", "web3 architecture",
        "crypto architecture", "metaverse architect", "metaverse architecture",
        "smart contract",
    ],
    "construccion": [
        "construction tech", "the b1m", "corning", "prefabric",
        "modular build", "concrete tech", "sustainable build",
        "lean construction", "casablanca", "durlock", "anacaflex", "revear",
        "sinteplast", "kekol", "weber", "obra", "construccion", "building tech",
        # Rescatados Parte 2:
        "slant 3d", "formlabs", "anycubic", "bugeo",
    ],
    "creadores": [
        "donebylaura", "kishimisu", "pixel easel", "uj studio", "uh studio",
        "argentina programa", "filo news", "psicolog",
        # Rescatados Parte 2:
        "ted", "archizoom", "digitalfutures",
    ],
    "noticias intl.": [
        "archdaily", "dezeen", "archinect", "architectural digest",
        "architectural review", "e-architect", "designboom", "architizer",
    ],
    "metaverso": [
        # Nueva categoria (2026-10-08, veredictos Parte 2: Spatial,
        # Decentraland, VrPatch, Jacobsen). Ultima en orden para no mover
        # matches existentes (ej Metaverse Architecture Biennale sigue en
        # NFTs/tokens porque "metaverso" no matchea "metaverse").
        "spatial", "decentraland", "metaverso", "vrpatch", "jacobsen",
    ],
}

# ---------------------------------------------------------------- NOTA ES:
# Palabras clave SOLO para escribir la columna "Parece ser" de la Parte B.
# No decide inclusion/exclusion: es una sugerencia para que el estudio lea
# rapido y sepa que mirar.
PISTAS_FUERA = {
    "IA / tech": ["ia ", "builder", "ai ", "coding", "mouredev", "ringa",
                  "cisco", "decoders", "xr ", "quantum", "alphonso", "alerta"],
    "Software arq / 3D": ["ifc", "formlabs", "anycubic", "render", "planfinder",
                          "3d", "architect", "archi", "slant", "vatros"],
    "Creatores arq": ["tedeschi", "algorithmix", "sawan", "salmaan", "tokus",
                       "toker", "tokar", "designa", "architect", "archi", "design"],
    "Arq vanguardia / teoria": ["digitalfutures", "futuro", "vanguard",
                                 "schumacher", "gabor", "carl", "jason lewis"],
    "Ciencia": ["schmidt", "nasa", "webb", "startalk", "veritasium", "3blue1brown",
                 "museo", "3blue", "quantum"],
    "Filosofia / espiritualidad": ["krishnamurti", "buddha", "meditaci",
                                     "melod", "luz interior", "consciencia"],
    "TV / entertainment": ["ted", "chopra", "house", "pawn", "celda", "misterios",
                            "cache", "comic", "anime", "gaming", "game"],
    "Musica / arte": ["piano", "guitar", "spatial", "paul hansen", "sonic"],
    "Negocios / podcasts": ["bilyeu", "ceo", "sherman", "judge", "mind amend"],
    "Educacion general": ["u-tad", "matemat", "analyst", "aprendemos"],
    "Estudio AR": ["laurini", "mouredev", "alura", "coderhouse", "imagecampus"],
}


def _norm(s):
    """Quita acentos, pasa a minusculas y saca el sufijo '-videos'/'-vídeos'.

    Takeout en español nomebra los archivos 'X-vídeos.csv'. Para comparar contra
    el maestro (que tiene el titulo sin sufijo) normalizamos ambos lados.
    """
    t = str.maketrans("áéíóúüñÁÉÍÓÚÜÑ", "aeiouunAEIOUUN")
    s = str(s).lower().translate(t)
    for suf in ("-videos", "-videos", "-vídeos", "-videos"):
        if s.endswith(suf):
            s = s[: -len(suf)]
            break
    return s


def esc_md(s):
    """Escapa los caracteres que rompen una tabla markdown.

    El separador de columnas de una tabla markdown es el pipe '|'. Si un titulo
    de YouTube lo contiene (muy comun en titulos con separadores de capitulo),
    rompe el renderizado de la tabla. Lo escapamos con una barra invertida.

    Tambien convertimos los saltos de linea en espacios: un titulo con '\n'
    partiria la fila en dos.
    """
    s = str(s).replace("\r", " ").replace("\n", " ")
    s = s.replace("|", "\\|")
    return s.strip()


# ---------------------------------------------------------------- NOTA ES:
# TAGS: tabla de keywords -> etiqueta. Se aplican contra el TITULO del video
# (y el nombre del canal) para deduplicar同类 temas que vos ya separaste en
# carpetas distintas. Ej: un video de ComfyUI en la carpeta ARQ/IA y otro en
# IA/gen_Img van a llevar los mismos tags, y asi los podes encontrar juntos.
#
# El orden importa: el primer tag que matchea se pone primero (es el mas
# especifico porque las listas van de lo particular a lo general).
TAGS = {
    # --- Software de arquitectura ---
    "rhino": ["rhino", "rhino3d", "rhinoceros", "grasshopper"],
    "grasshopper": ["grasshopper", "gh plugin", "gptool"],
    "revit": ["revit", "bim 360", "dynamo"],
    "autocad": ["autocad", "autolisp", "dwg", "dcl"],
    "twinmotion": ["twinmotion"],
    "unreal": ["unreal engine", "unreal", "ue5"],
    "blender": ["blender"],
    "freecad": ["freecad", "openscad"],
    "sketchup": ["sketchup"],
    "lumion": ["lumion", "d5 render", "vectary", "enscape"],
    "maket": ["maket.ai", "maket"],
    "3dsmax": ["3ds max", "3dsmax", "3d studio", "v-ray", "vray",
               "corona renderer", "chaos vantage"],
    "magnific": ["magnific"],
    # --- IAtools ---
    "comfyui": ["comfyui", "comfy ui"],
    "stable-diffusion": ["stable diffusion", "sdxl", "sampler", "checkpoint"],
    "midjourney": ["midjourney"],
    "nanobanana": ["nano banana", "gemini image", "gemini 2.5 flash image"],
    "flux": ["flux.1", "flux ai", "flux kontext"],
    "ai-3d": ["3d ai", "ai 3d", "3d generator", "generador 3d", "text to 3d",
              "image to 3d", "tripo", "triposplat", "meshy"],
    "video-ia": ["sora", "runway", "kling", "veo 3", "google veo", "pika",
                 "luma dream", "gen-3", "gen 4", "hailuo", "vidu", "pixverse"],
    "audio-ia": ["suno", "elevenlabs", "eleven labs", "udio"],
    "llm": ["llm", "rag", "ia", "gemma", "gpt-6", "gpt 6", "gpt astra", "gpt-4",
            "gpt-5", "chatgpt", "claude", "gemini", "llama", "mistral",
            "deepseek", "qwen", "grok", "nicolas dubois", "reemplazar",
            "reemplazo", "herramienta", "tools", "academia ia",
            "ai agency"],
    "agents": ["agent", "crewai", "langgraph", "autogen", "mcp", "openai sdk"],
    "vibe-coding": ["vibe coding", "vibe coding", "cursor", "lovable",
                    "bolt.new", "windsurf", "copilot", "codex", "claude code",
                    "spec kit", "spec-kit", "mouredev", "josema"],
    "opencode": ["opencode"],
    "remotion": ["remotion"],
    "repos": ["github", "repositorio"],
    "n8n": ["n8n", "make.com", "zapier", "automatizacion", "automatizar",
            "automatizado", "automatic", "automation", "automated",
            "automatico", "automatica"],
    "whatsapp": ["whatsapp"],
    "upscaling": ["upscale", "topaz"],
    "notebook": ["notebook", "commonplace", "segundo cerebro", "second brain",
                 "cerebro digital", "da vinci", "leonardo", "obsidian"],
    "hardware": ["router", "hardware", "servidor", "nas", "raspberry",
                 "tecnologia", "tecnologico"],
    # --- Construccion / materiales ---
    "3d-print": ["3d print", "impresion 3d", "formlabs", "anycubic", "bambu"],
    "concreto": ["concreto", "hormigon", "concrete"],
    "modular": ["modular", "prefabricadas", "prefabricados", "prefabricada",
                "prefabricado", "prefabric"],
    "aislamiento": ["aislamiento", "termic", "insulation"],
    "madera": ["madera", "wood", "timber", "lvl", "clt"],
    # --- Arquitectura / diseno ---
    "arq": ["arquitectura", "architettura", "architecture", "architectural",
            "architect", "arquitecto", "mvrdv", "zaha", "bauhaus"],
    "gaussian-splatting": ["gaussian", "splatting", "splating", "nerf",
                           "postshot", "fotogrametria", "photogrammetry",
                           "lidar", "escaneo 3d", "3d scan"],
    "charlas": ["charla", "masterclass", "documental", "documentary",
                "keynote", "ted talk", "tedx", "conferencia", "summit",
                "tim fu"],
    "diagramas": ["diagrama", "diagram"],
    "parametrico": ["parametric", "parametrico", "algorithmic design"],
    "viz": ["archviz", "visualizacion", "render", "visualization",
            "3d model", "d5"],
    "dibujo": ["pixelart", "pixel art", "procreate", "dibujo", "drawing",
               "sketching", "sketch"],
    "planos": ["floor plan", "plano", "planta baja", "layout", "plantas",
               "fachada", "facade"],
    "interior": ["interior", "interiores", "amoblamiento", "furniture"],
    "sostenibilidad": ["sostenible", "sustainable", "sustentable", "verde",
                         "green building", "certificacion", "leed",
                         "passive house"],
    "gestion": ["power bi", "powerbi", "notion", "gantt", "leantime"],
    # --- tendencias ---
    "metaverso": ["metaverso", "metaverse", "vr", "ar", "xr", "realidad virtual",
                   "realidad aumentada", "quest", "meta quest", "vision pro",
                   "steam vr"],
    "nft": ["nft", "tokenizacion", "tokeniz", "blockchain", "web3", "crypto"],
    "decentraland": ["decentraland"],
    "marketing": ["marketing", "seo", "sem", "seo local", "posicionamiento"],
    # --- Listados, NO analizados en el vault (decision del estudio 2026-10-08) ---
    # filosofia/personal/otros se LISTAN pero no se analizan: son intereses
    # legitimos fuera del rubro del estudio. No entran en ninguna categoria
    # amplia a proposito (categoria_de los deja con Cat vacio).
    # 'personal' no tiene keywords (es miscelaneo por naturaleza): esos videos
    # llegan via veredictos.json, no por matching.
    "filosofia": ["jung", "schopenhauer", "tao", "lao tzu", "huxley",
                  "filosofia", "estoico", "seneca", "marco aurelio",
                  "krishnamurti", "alan watts", "buda", "budd", "meditacion",
                  "mindfulness"],
}


# ---------------------------------------------------------------- NOTA ES:
# CATEGORIAS AMPLIAS: cada tag especifico pertenece a una categoria madre.
# Sirven para filtrar rapido ("mostrame todo lo de software-arq") sin perderse
# entre 40 tags. El orden del diccionario define la prioridad: si un video
# tiene tags de dos categorias, gana la que aparece primero.
CATEGORIAS_AMPLIAS = {
    "software-arq": ["rhino", "grasshopper", "revit", "autocad", "twinmotion",
                     "unreal", "blender", "freecad", "sketchup", "lumion",
                     "maket", "3dsmax"],
    "ia-imagen": ["comfyui", "stable-diffusion", "midjourney", "nanobanana",
                  "flux", "upscaling", "magnific", "ai-3d"],
    "ia-video-audio": ["video-ia", "audio-ia", "remotion"],
    "ia-agentes-code": ["llm", "agents", "vibe-coding", "opencode", "n8n",
                        "whatsapp", "repos"],
    "construccion": ["3d-print", "concreto", "modular", "aislamiento",
                     "madera"],
    "diseno-arq": ["viz", "dibujo", "planos", "interior", "parametrico",
                   "sostenibilidad", "metaverso", "nft", "decentraland",
                   "diagramas", "arq", "gaussian-splatting"],
    "gestion": ["marketing", "gestion", "notebook", "hardware"],
    # NOTA: 'charlas' y 'filosofia' NO estan en ninguna categoria a proposito.
    # Las charlas cruzan todas las categorias (una charla puede ser de IA, de
    # arq o de filosofia): se filtran por tag, no por categoria.
    # filosofia/personal/otros son listados, no analizados (decision estudio).
}


def categoria_de(tags):
    """Devuelve la categoria amplia de una lista de tags (o '' si no hay).

    Recorre CATEGORIAS_AMPLIAS en orden: el primer tag que matchea define la
    categoria. Los slugs de carpeta (ej 'arq-docs') no estan en ninguna
    categoria: para esos se usa SLUG_CAT (mapeo manual de tus 16 carpetas) y,
    en ultimo caso, el prefijo ('arq-' -> diseno-arq, 'ia-' -> ia-agentes-code).
    Si nada matchea, devuelve '' (vacio).
    """
    for cat, miembros in CATEGORIAS_AMPLIAS.items():
        if any(t in miembros for t in tags):
            return cat
    for t in tags:
        if t in SLUG_CAT:
            return SLUG_CAT[t]
    for t in tags:
        if t.startswith("arq-"):
            return "diseno-arq"
        if t.startswith("ia-"):
            return "ia-agentes-code"
    return ""


# ---------------------------------------------------------------- NOTA ES:
# SLUG_CAT: tus 16 carpetas de YouTube mapeadas a categoria amplia.
# El slug se genera asi: minusculas + sin acentos + '/' -> '-' + sin emojis.
# Ej: 'IA/⚙️Workflows(Autom.)' -> 'ia-workflowsautom'.
# Si renombras o agregas una carpeta en YouTube, agrega su slug aca.
SLUG_CAT = {
    "ia-workflowsautom": "ia-agentes-code",
    "arq-3d-print": "construccion",
    "arq-autocad2d": "software-arq",
    "arq-docs": "diseno-arq",
    "arq-ia": "diseno-arq",
    "arq-rhinograsshopper": "software-arq",
    "arq-twinmotion-unrealengine": "software-arq",
    "ia-metaverso-vr-ar": "diseno-arq",
    "ia-gentxt-llms": "ia-agentes-code",
    "ia-genimg": "ia-imagen",
    "ia-genvid": "ia-video-audio",
    "ia-genagents": "ia-agentes-code",
    "ia-vibecoding": "ia-agentes-code",
    "mkt-semseo": "gestion",
    "libros": "gestion",
}


def _kw_pat(k):
    """Arma el regex de una keyword con stemming de plural y limites de palabra.

    - Singulariza: 'agents' -> 'agent', para matchear ambas formas.
    - El 's?' final matchea singular y plural ('floor plan' y 'floor plans').
    - Los lookarounds evitan matches dentro de otras palabras ('ar' en
      'generar').
    """
    base = _norm(k)
    if base.endswith("s") and not base.endswith("ss") and len(base) > 3:
        base = base[:-1]
    return rf"(?:(?<![a-z0-9]){re.escape(base)}s?(?![a-z0-9]))"


def _es_fecha(s):
    """True si el string parece una fecha (para no usarla como tag).

    Algunos titulos traen la fecha adentro ('... 2026-09-15') y el fallback del
    slug la recogia como tag. Es ruido: se filtra.
    """
    return bool(re.match(r"^\d{4}(-\d{2}(-\d{2})?)?$", (s or "").strip()))


def inferir_tags(titulo, canal="", carpeta=""):
    """Devuelve una lista de tags (max 4) segun el titulo, el canal y la carpeta.

    Usa TAGS de arriba. La busqueda es sin acentos y en minusculas, con
    LIMITES DE PALABRA: es essential para los tags cortos como 'ar', 'vr',
    '3d' o 'ia'. Sin limites, 'ar' matchearia dentro de 'generar', 'hacer',
    'comparar' y cada video del vault saldria con el tag 'metaverso'.

    El parametro 'carpeta' es tu lista de YouTube. Sirve de contexto: un video
    en 'IA/gen_Img' ya esta clasificado por vos como generacion de imagen,
    aunque el titulo no mencione ComfyUI ni Stable Diffusion. Sin esto, la mitad
    de los videos caia en 'sin-clasificar'.
    """
    texto = _norm(f"{titulo} {canal}")
    tags = []
    for etiqueta, keywords in TAGS.items():
        for k in keywords:
            if re.search(_kw_pat(k), texto):
                tags.append(etiqueta)
                break

    # Si no hubo match por titulo, probamos con el nombre de la carpeta.
    if not tags and carpeta:
        c = _norm(carpeta)
        for etiqueta, keywords in TAGS.items():
            for k in keywords:
                if re.search(_kw_pat(k), c):
                    tags.append(etiqueta)
                    break

    # Ultimo recurso: el slug de tu propia carpeta. Si el video esta en
    # 'ARQ/docs', vos ya lo clasificaste como documentacion de arquitectura:
    # usamos eso como tag aunque el titulo no diga nada. Asi 'sin-clasificar'
    # queda solo para los videos de Watch Later sin tema claro.
    if not tags and carpeta and _norm(carpeta) not in ("watch later", ""):
        slug = _norm(carpeta).replace("/", "-").replace(" ", "-")
        slug = re.sub(r"-+", "-", slug).strip("-")
        # sacamos prefijos de emoji que quedaron como texto suelto
        slug = re.sub(r"[^a-z0-9-]+", "", slug)
        # ...pero nunca una fecha: 'IA/gen_Vid 2026-09-15' no es un tag
        if slug and not _es_fecha(slug):
            tags.append(slug)

    if not tags:
        return ["sin-clasificar"]
    return tags[:4]


# ---------------------------------------------------------------- NOTA ES:
# Parseo del HTML de marcadores de Chrome. El export de Chrome es un HTML
# medio raro: los <A> (links) cuelgan de carpetas <H3>. Lo parseamos con un
# parser de pila para ir anotando en que carpeta estamos.
def parsear_marcadores(html_path):
    """Devuelve una lista [(carpeta, titulo, url), ...] de los bookmarks."""
    try:
        from html.parser import HTMLParser
    except ImportError:
        return []

    class MarcadorParser(HTMLParser):
        def __init__(self):
            # NOTA ES: super().__init__() inicializa HTMLParser. Guardamos la
            # 'pila' de carpetas abiertas y una lista para los links.
            super().__init__()
            self.pila = []          # carpetas abiertas
            self.resultado = []     # (carpeta, titulo, url)
            self.en_h3 = False
            self.h3_texto = ""
            self.en_a = False
            self.a_href = ""
            self.a_texto = ""

        def handle_starttag(self, tag, attrs):
            d = dict(attrs)
            if tag == "h3":
                self.en_h3 = True
                self.h3_texto = ""
            elif tag == "a":
                self.en_a = True
                self.a_href = d.get("href", "")
                self.a_texto = ""

        def handle_endtag(self, tag):
            if tag == "h3":
                self.en_h3 = False
                self.pila.append(self.h3_texto.strip())
            elif tag == "a":
                self.en_a = False
                carpeta = self.pila[-1] if self.pila else "Sin carpeta"
                self.resultado.append((carpeta, self.a_texto.strip(), self.a_href))

        def handle_data(self, data):
            if self.en_h3:
                self.h3_texto += data
            elif self.en_a:
                self.a_texto += data

        # NOTA ES: handle_startendtag se llama para tags auto-cerrados como <br>.
        # No hacemos nada especial con ellos.

    try:
        html = html_path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return []

    parser = MarcadorParser()
    parser.feed(html)
    return parser.resultado


def leer_videos_de_playlist(path):
    """Lee un CSV de playlist y devuelve [(video_id, fecha_iso), ...]."""
    out = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # saltear header
        for row in reader:
            if len(row) >= 2 and row[0].strip():
                out.append((row[0].strip(), row[1].strip()))
    return out


def main():
    # Verificar que exista todo antes de escribir nada
    if not LISTDIR.exists():
        print("ERROR: no existe", LISTDIR)
        sys.exit(1)
    if not SUBDIR.exists():
        print("ERROR: no existe", SUBDIR)

    # ------------------------------------------------------------------
    # PASO 1: mapear playlists
    # ------------------------------------------------------------------
    # El archivo "Listas de reproduccion.csv" tiene los datos maestro de cada
    # lista: id, titulo original, descripcion original, visibilidad.
    maestro = {}
    # NOTA ES: el archivo maestro se llama 'Listas de reproducción.csv' con tilde en
    # 'reproducción'. En vez de escribirlo a mano (y que se rompa si el sistema esta
    # en otro idioma), buscamos el CSV que NO termina en '-videos.csv' (o sea, el indice).
    maestro_path = None
    for p in sorted(LISTDIR.glob("*.csv")):
        if not p.stem.lower().endswith("-videos") and not p.stem.lower().endswith("-vídeos"):
            maestro_path = p
            break
    if maestro_path is None:
        raise SystemExit("ERROR: no se encontro el CSV maestro de listas")
    print("CSV maestro:", maestro_path.name)
    with open(maestro_path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            maestro[r[list(r.keys())[0]]] = r

    # Emparejear cada lista (por titulo) con su archivo de videos.
    # Takeout llama al archivo como el titulo con "/" -> "_" y sufijo "-vídeos.csv".
    # _norm() ya saca acentos y el sufijo, asi que comparamos solo el "corazon":
    #   titulo "IA/🎨gen_Img"  -> norm -> "ia_🎨gen_img"
    #   archivo "IA_🎨gen_Img-vídeos" -> norm -> "ia_🎨gen_img"
    #
    # NOTA ES: los headers del CSV maestro traen tildes y no coinciden con lo que
    # escribimos a mano. Para evitar KeyError usamos indices posicionales.
    # El orden de columnas del maestro (ver takeout real) es:
    #   0=ID lista, 1=Add new, 2=Descripcion, 3=Titulo, 4=Idioma, 5=Fecha creacion,
    #   6=Fecha actualizacion, 7=Orden, 8=Visibilidad
    K_ID, K_TITLE = 0, 3

    # Pre-calculamos el stem normalizado de cada archivo de videos, una sola vez.
    stems = {}
    for real in LISTDIR.glob("*.csv"):
        if _norm(real.stem) != _norm(real.stem.replace("Watch later", "")):  # no-op guard
            pass
        norm_stem = _norm(real.stem)
        # el maestro no es un archivo de videos
        if norm_stem.startswith("listas de reproduccion") or norm_stem.startswith("lista de reproduccion"):
            continue
        stems.setdefault(norm_stem, real)

    archivos = {}
    for pid, meta in maestro.items():
        titulo = meta[list(meta.keys())[K_TITLE]].strip()
        clave = _norm(titulo.replace("/", "_"))
        if clave in stems:
            archivos[pid] = (stems[clave], meta)
        else:
            print(f"  [aviso] no encontre archivo para la lista '{titulo}' (clave='{clave}')")

    print("Listas emparejadas:", len(archivos), "de", len(maestro))

    # ------------------------------------------------------------------
    # PASO 2: cargar videos
    # ------------------------------------------------------------------
    # wl_set = set de video_ids en Watch Later (para marcar).
    wl_set = set()
    wl_orden = []
    wl_pid = None
    for pid, meta in maestro.items():
        tit = meta[list(meta.keys())[3]].strip().lower()
        if tit == "watch later":
            wl_pid = pid
            break

    if wl_pid and wl_pid in archivos:
        datos = leer_videos_de_playlist(archivos[wl_pid][0])
        wl_orden = datos
        wl_set = {vid for vid, _ in datos}

    print("Watch Later:", len(wl_orden), "videos")

    # Para cada lista tematica, guardamos sus videos (ordenados por fecha desc)
    temas = []
    for pid, (real, meta) in archivos.items():
        if pid == wl_pid:
            continue
        datos = leer_videos_de_playlist(real)
        datos.sort(key=lambda t: t[1], reverse=True)
        titulo = meta[list(meta.keys())[3]].strip()
        desc = meta[list(meta.keys())[2]].strip()
        temas.append({
            "pid": pid,
            "archivo": real.stem,
            "titulo": titulo,
            "desc": desc,
            "videos": datos,
        })

    # Ordenar las listas por nuestro orden manual (ORDEN_LISTAS).
    # _norm() ya saco el sufijo '-videos', asi que comparamos solo el corazon.
    def orden_key(t):
        # Convertimos "IA/🎨gen_Img" a la clave que usamos en ORDEN_LISTAS
        clave = _norm(t["titulo"].replace("/", "_"))
        for i, pref in enumerate(ORDEN_LISTAS):
            # ORDEN_LISTAS tiene "Watch later-videos", "ARQ_3D-Print-videos", etc.
            # quitamos el sufijo para comparar
            p = _norm(pref)
            if clave.startswith(p) or p.startswith(clave):
                return i
        return 999

    temas.sort(key=orden_key)
    total_tematicos = sum(len(t["videos"]) for t in temas)
    print("Listas tematicas:", len(temas), "con", total_tematicos, "videos")

    # ------------------------------------------------------------------
    # PASO 3: suscripciones
    # ------------------------------------------------------------------
    subs = []
    # Mismo problema de tildes que en las playlists. El CSV de suscripciones tiene
    # 3 columnas: 0=ID del canal, 1=URL del canal, 2=Titulo del canal.
    with open(SUBDIR / "suscripciones.csv", encoding="utf-8-sig", newline="") as f:
        rd = csv.reader(f)
        next(rd)  # saltear header
        for r in rd:
            if len(r) >= 3 and r[0].strip():
                subs.append({
                    "id": r[0].strip(),
                    "url": r[1].strip().replace("http://", "https://"),
                    "nombre": r[2].strip(),
                })
    print("Suscripciones:", len(subs))

    def clasificar(canal):
        n = _norm(canal["nombre"])
        for cat in CATS:
            for k in CATS[cat]:
                if _norm(k) in n:
                    return cat
        return None

    en_scope = [s for s in subs if clasificar(s)]
    fuera = [s for s in subs if not clasificar(s)]
    print("Canales en scope:", len(en_scope), "| fuera:", len(fuera))

    def pista_fuera(nombre):
        n = _norm(nombre)
        for etiqueta, kws in PISTAS_FUERA.items():
            for k in kws:
                if _norm(k) in n:
                    return etiqueta
        return "sin pista (revisar)"

    # ------------------------------------------------------------------
    # PASO 0: cache de titulos (opcional, viene de scripts/yt_titles.py)
    # ------------------------------------------------------------------
    titulos = {}
    if CACHE_TITULOS.exists():
        titulos = json.loads(CACHE_TITULOS.read_text(encoding="utf-8"))
        print(f"Cache de titulos: {len(titulos)} entradas")
    else:
        print("Sin cache de titulos (corre scripts/yt_titles.py con la APIkey)")

    def info_video(vid):
        """Devuelve (titulo, canal, duracion) desde el cache, o placeholders."""
        d = titulos.get(vid)
        if not d:
            return ("_(sin titulo)_", "", "")
        return (esc_md(d.get("titulo", "")), esc_md(d.get("canal", "")), d.get("duracion", ""))

    # ------------------------------------------------------------------
    # PASO 0b: veredictos manuales (raw/yt/veredictos.json)
    # ------------------------------------------------------------------
    # Fuente de verdad de las decisiones del estudio. Al regenerar, los
    # veredictos se conservan: un video ya juzgado no vuelve a sin-clasificar.
    VEREDICTOS_FILE = VAULT / "raw" / "yt" / "veredictos.json"
    if VEREDICTOS_FILE.exists():
        VEREDICTOS = json.loads(VEREDICTOS_FILE.read_text(encoding="utf-8")).get("videos", {})
        print(f"Veredictos cargados: {len(VEREDICTOS)} videos juzgados")
    else:
        VEREDICTOS = {}

    def aplicar_veredicto(vid, tags):
        """Aplica el veredicto manual sobre los tags inferidos.

        - filosofia/personal/otros/proyecto -> el veredicto ES el tag (listados,
          no analizados). En proyecto se suma lo inferido detras como contexto.
        - descartar -> tag 'descartado' (sigue listado, archivado).
        - rescatar + tema -> el tema primero, despues lo inferido (sin duplicar).
        - sin veredicto -> tags inferidos tal cual.
        """
        v = VEREDICTOS.get(vid)
        if not v:
            return tags
        tipo = v.get("v")
        if tipo in ("filosofia", "personal", "otros"):
            return [tipo]
        if tipo == "descartar":
            return ["descartado"]
        if tipo == "proyecto":
            return ["proyecto"] + [t for t in tags if t != "sin-clasificar"][:3]
        if tipo == "rescatar":
            temas = v.get("tema", [])
            if isinstance(temas, str):
                temas = [temas]
            return (temas + [t for t in tags if t not in temas and t != "sin-clasificar"])[:4] or temas[:4]
        return tags

    con_titulos = bool(titulos)

    # ------------------------------------------------------------------
    # PASO 4: escribir el markdown
    # ------------------------------------------------------------------
    L = []
    A = L.append

    A("---")
    A("tipo: raw-cola")
    A("fecha_creacion: 2026-10-08")
    A("ultima_actualizacion: 2026-10-08")
    A("tags: [yt, takeout, watch-later, playlists, canales, revision, hitl]")
    A("---")
    A("")
    A("# Videos y canales guardados — YouTube + Chrome")
    A("")
    A("> Documento unico de curacion generado desde Google Takeout (2026-10-08).")
    A("> **Parte A**: todos los videos que tenes guardados, agrupados por tu carpeta/listado, con link directo.")
    A("> **Parte B**: los canales que quedaron fuera del scope del estudio, para que revises si los sumar o descartar.")
    A("")
    A("Regenerar con: `scripts/yt_takeout_parser.py`")
    A("")
    A("## Resumen")
    A("")
    A("| Metrica | Cantidad |")
    A("|---|---|")
    A(f"| Videos en Watch Later | {len(wl_orden)} |")
    A(f"| Videos en listas tematicas | {total_tematicos} |")
    A(f"| Videos que estan en Watch Later Y en alguna tematica | {sum(1 for v in wl_orden if v[0] in set(x for t in temas for x, _ in t['videos']))} |")
    A(f"| Canales suscritos totales | {len(subs)} |")
    A(f"| Canales en scope | {len(en_scope)} |")
    A(f"| Canales fuera de scope (Parte B) | {len(fuera)} |")
    A("")

    # Resumen de tags: cuantos videos hay de cada tema. Sirve para ver de un
    # vistazo si hay mucho material de ComfyUI, Rhino, etc.
    if con_titulos:
        conteo_tags = defaultdict(int)
        for vid, _ in wl_orden:
            t, c, _d = info_video(vid)
            tgs = aplicar_veredicto(vid, inferir_tags(t.replace("\\|", "|"), c, "watch later"))
            for tag in tgs:
                conteo_tags[tag] += 1
        for tt in temas:
            for vid, _ in tt["videos"]:
                t, c, _d = info_video(vid)
                tgs = aplicar_veredicto(vid, inferir_tags(t.replace("\\|", "|"), c, tt["titulo"]))
                for tag in tgs:
                    conteo_tags[tag] += 1
        top_tags = sorted(conteo_tags.items(), key=lambda kv: -kv[1])[:20]
        if top_tags:
            A("### Top tags en tus videos")
            A("")
            A("Tags especificos (lo fino). Para lo grueso, ver Por categoria amplia abajo.")
            A("")
            A("| Tag | Videos |")
            A("|---|---|")
            for tag, n in top_tags:
                A(f"| `{tag}` | {n} |")
            A("")

        # Resumen por categoria amplia: lo grueso para filtrar rapido.
        # Se calcula re-agrupando los mismos tags ya contados.
        conteo_cats = defaultdict(int)
        for tag, n in conteo_tags.items():
            cat = categoria_de([tag])
            conteo_cats[cat or "(sin categoria)"] += n
        top_cats = sorted(conteo_cats.items(), key=lambda kv: -kv[1])
        if top_cats:
            A("### Por categoria amplia")
            A("")
            A("| Categoria | Videos | Que incluye |")
            A("|---|---|---|")
            for cat, n in top_cats:
                miembros = ", ".join(f"`{t}`" for t in CATEGORIAS_AMPLIAS.get(cat, [])[:8])
                A(f"| `{cat}` | {n} | {miembros} |")
            A("")
    A("---")
    A("")

    # ---------------- PARTE A ----------------
    A("## Parte A — Videos guardados")
    A("")
    A("Cada seccion es una de tus listas de YouTube. Los links van directo al video.")
    A("Columnas: **Tags** = tema fino (ej `comfyui`, `rhino`); **Cat** = categoria")
    A("amplia (ej `ia-imagen`, `software-arq`) para filtrar rapido; **En WL** = si")
    A("ademas esta en Watch Later.")
    A("")
    if con_titulos:
        A("> Titulos, canal y duracion traidos con la YouTube Data API v3")
        A("> (cache en `raw/yt/cache-titulos.json`, generado por `scripts/yt_titles.py`).")
    else:
        A("> **Sin titulos todavia**: Takeout solo guarda el `video_id`.")
        A("> Para completar titulo/canal/duracion hace falta la YouTube Data API v3.")
        A("> Pasos: [[wiki/glosario/interno/youtube-data-api-key|youtube-data-api-key]]")
        A("> Mientras tanto, hovering el link en el navegador te muestra el titulo.")
    A("")

    # indice
    # NOTA ES: wikilink interno de Obsidian = [[#Encabezado Exacto]]. El encabezado
    # de cada seccion es el titulo de la lista tal cual quedo en YouTube, asi que el
    # enlace tiene que ser identico, emojis y barras incluidos.
    A("### Indice de listas")
    A("")
    A(f"- [[#0. Watch Later]] — {len(wl_orden)} videos")
    for t in temas:
        A(f"- [[#{t['titulo']}]] — {len(t['videos'])} videos")
    A("")
    A("---")
    A("")

    # Watch Later primero
    A("### 0. Watch Later")
    A("")
    A(f"Tu cola general de videos para ver. {len(wl_orden)} videos, ordenados por fecha de agregado (mas nuevo primero).")
    A("")
    if con_titulos:
        A("| # | Titulo | Canal | Dur | Fecha | Tags | Cat | Link |")
        A("|---|---|---|---|---|---|---|---|")
        for i, (vid, fecha) in enumerate(wl_orden, 1):
            tit, can, dur = info_video(vid)
            lista_tags = aplicar_veredicto(vid, inferir_tags(tit.replace("\\|", "|"), can, "watch later"))
            tags = ", ".join(lista_tags)
            cat = categoria_de(lista_tags)
            A(f"| {i} | {tit} | {can} | {dur} | {fecha[:10]} | {tags} | {cat} | https://www.youtube.com/watch?v={vid} |")
    else:
        A("| # | Fecha | Link | Video ID |")
        A("|---|---|---|---|")
        for i, (vid, fecha) in enumerate(wl_orden, 1):
            A(f"| {i} | {fecha[:10]} | https://www.youtube.com/watch?v={vid} | `{vid}` |")
    A("")
    A("---")
    A("")

    # Listas tematicas
    for t in temas:
        titulo = t["titulo"]
        A(f"### {titulo}")
        A("")
        if t["desc"]:
            A(f"**Tu descripcion:** {t['desc']}")
            A("")
        A(f"Archivo Takeout: `{t['archivo']}.csv` · Videos: {len(t['videos'])}")
        A("")
        if con_titulos:
            A("| # | Titulo | Canal | Dur | Fecha | En WL | Tags | Cat | Link |")
            A("|---|---|---|---|---|---|---|---|---|")
            for i, (vid, fecha) in enumerate(t["videos"], 1):
                tit, can, dur = info_video(vid)
                en_wl = "Si" if vid in wl_set else ""
                lista_tags = aplicar_veredicto(vid, inferir_tags(tit.replace("\\|", "|"), can, titulo))
                tags = ", ".join(lista_tags)
                cat = categoria_de(lista_tags)
                A(f"| {i} | {tit} | {can} | {dur} | {fecha[:10]} | {en_wl} | {tags} | {cat} | https://www.youtube.com/watch?v={vid} |")
        else:
            A("| # | Fecha | Link | Video ID | En Watch Later |")
            A("|---|---|---|---|---|")
            for i, (vid, fecha) in enumerate(t["videos"], 1):
                en_wl = "Si" if vid in wl_set else ""
                A(f"| {i} | {fecha[:10]} | https://www.youtube.com/watch?v={vid} | `{vid}` | {en_wl} |")
        A("")
        A("---")
        A("")

    # ---------------- PARTE B ----------------
    A("## Parte B — Canales fuera de scope (para tu revision)")
    A("")
    A(f"Estos {len(fuera)} canales de tus {len(subs)} suscripciones no matchearon las keywords")
    A("del scope (arquitectura + IA + software arq + construccion + NFTs).")
    A("")
    A("**La columna *Parece ser* es una sugerencia mia para que puedas escanear rapido.**")
    A("Vos completes la columna *Tu veredicto*: sumar a `<categoria>`, descartar, o dejar pendiente.")
    A("")
    A("| # | Canal | Link | Parece ser | Tu veredicto | Notas |")
    A("|---|---|---|---|---|---|")
    for i, s in enumerate(fuera, 1):
        pista = pista_fuera(s["nombre"])
        A(f"| {i} | {esc_md(s['nombre'])} | {s['url']} | {pista} |  |  |")
    A("")
    A("---")
    A("")
    A("## Parte C — Canales en scope (resumen)")
    A("")
    A("Estos si matchearon. Ya esta el detalle en [[wiki/glosario/interno/canales-youtube|canales-youtube]].")
    A("")
    por_cat = defaultdict(list)
    for s in en_scope:
        por_cat[clasificar(s)].append(s)
    A("| Categoria | Canales |")
    A("|---|---|")
    for cat in CATS:
        if por_cat[cat]:
            A(f"| {cat} | {len(por_cat[cat])} |")
    A(f"| **total** | **{len(en_scope)}** |")
    A("")
    A("## Metodologia y origen")
    A("")
    A("- Fuente: `C:\\Users\\Solch16\\Downloads\\Takeout\\YouTube y YouTube Music\\`")
    A("- Marcadores: `C:\\Users\\Solch16\\Downloads\\Takeout\\Chrome\\Marcadores.html`")
    A("- Generado: 2026-10-08")
    A("- Decision HITL: filtrar el ruido (quedan solo los canales del rubro)")
    A("- Proximo paso: completar Parte B (veredictos) y regenerar el script si actualizas el Takeout")
    A("")

    # ---------------- PARTE D: marcadores ----------------
    marcadores = parsear_marcadores(CHROME_FILE) if CHROME_FILE.exists() else []
    if marcadores:
        # agrupar por carpeta
        por_carpeta = defaultdict(list)
        for carpeta, tit, url in marcadores:
            por_carpeta[carpeta].append((tit, url))

        # categorizar carpetas por keywords del nombre (mismo criterio que los canales)
        CATS_BM = {
            "software arq": ["comfyui", "cad", "bim", "rhino", "sketch", "archviz",
                             "eac", "alde", "programas", "workflows"],
            "ia": ["ia", "agents", "ai"],
            "construccion": ["presupuestos", "casablanca", "durlock", "ancaflex",
                              "revear", "sinteplast", "kekol", "weber", "hon",
                              "muebles", "aviso_obra", "gcba"],
            "educacion": ["c#", "e#", "g#", "a#", "tec", "alura"],
            "libros": ["libros", "alde"],
            "personal": ["busqueda", "pc", "vps", "bookmark", "synced", "other"],
        }

        def cat_bm(carpeta):
            n = _norm(carpeta)
            for cat, kws in CATS_BM.items():
                for k in kws:
                    if _norm(k) in n:
                        return cat
            return "sin categoria"

        A("---")
        A("")
        A("## Parte D — Marcadores de Chrome")
        A("")
        A(f"{len(marcadores)} bookmarks en {len(por_carpeta)} carpetas, agrupados por tu carpeta de origen.")
        A("Cada link tiene un tag inferido por el nombre del sitio (para filtrar rapido).")
        A("")

        # indice de carpetas
        A("### Carpetas")
        A("")
        A("| Carpeta | Bookmarks | Categoria |")
        A("|---|---|---|")
        for carpeta in sorted(por_carpeta, key=lambda c: -len(por_carpeta[c])):
            A(f"| {esc_md(carpeta)} | {len(por_carpeta[carpeta])} | {cat_bm(carpeta)} |")
        A("")

        # detalle por carpeta (solo las que tienen bookmarks)
        A("### Links por carpeta")
        A("")
        for carpeta in sorted(por_carpeta, key=lambda c: -len(por_carpeta[c])):
            links = por_carpeta[carpeta]
            if not links:
                continue
            A(f"**{esc_md(carpeta)}** ({len(links)} bookmarks · {cat_bm(carpeta)})")
            A("")
            for tit, url in links:
                t = esc_md(tit[:70]) if tit else "(sin titulo)"
                A(f"- [{t}]({url})")
            A("")
        A("---")
        A("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"\nOK -> {OUT}")
    print(f"   {len(L)} lineas")


if __name__ == "__main__":
    main()