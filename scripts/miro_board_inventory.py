#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
miro_board_inventory.py — inventario de un tablero de Miro (videos, workflows, enlaces)

Qué hace, en una frase:
    Lee un tablero de Miro y lo ordena en un indice util: que videos hay, que
    workflows de ComfyUI hay, que enlaces y que tarjetas, con la posicion de
    cada cosa en el tablero.

Dos modos de entrada:
    1) API   -> necesita un token de Miro (boards:read)
    2) OFFLINE -> parsea el archivo exportado: CSV (export to spreadsheet),
       backup .rtb/.miro (ZIP o binario) o PDF (solo URLs embebidas)

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\miro_board_inventory.py --url "https://miro.com/app/board/uXjVHRM2XQU=/" --token $env:MIRO_ACCESS_TOKEN
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\miro_board_inventory.py --file "C:\\descargas\\tablero.csv"

Salida:
    --out carpeta\\  (por defecto escribe el .md y el .json en la carpeta actual)
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile

API = "https://api.miro.com/v2"

# ---------------------------------------------------------------------------
# 1) Clasificadores: que es cada cosa dentro del tablero
# ---------------------------------------------------------------------------

# NOTA ES: un patron es una tupla (etiqueta, expresion regular compilada).
# Se prueban en orden y gana el primero que matchea: por eso los patrones
# mas especificos (youtube) van antes que los genericos (http).
PATRONES = [
    ("youtube",     re.compile(r"(youtube\.com/(watch\?|embed/|playlist)|youtu\.be/)", re.I)),
    ("vimeo",       re.compile(r"vimeo\.com/", re.I)),
    ("loom",        re.compile(r"(loom\.com/(share|embed))", re.I)),
    ("wistia",      re.compile(r"(wistia\.(com|net)|fast\.wistia\.net)", re.I)),
    ("scrive",      re.compile(r"scrive\.com/", re.I)),
    ("comfy_cloud", re.compile(r"(cloud\.comfy\.com|comfy\.cloud|app\.comfy\.org)", re.I)),
    ("comfy_wf",    re.compile(r"(comfyworkflows|workflow.*\.json|\.json$)", re.I)),
    ("miro_board",  re.compile(r"miro\.com/app/board/", re.I)),
    ("comfy_docs",  re.compile(r"docs\.comfy\.org", re.I)),
    ("huggingface", re.compile(r"huggingface\.co", re.I)),
    ("civitai",     re.compile(r"civitai\.com", re.I)),
    ("github",      re.compile(r"github\.com", re.I)),
    ("pdf",         re.compile(r"\.pdf($|\?)", re.I)),
    ("archademy",   re.compile(r"archademy\.ai", re.I)),
]

# NOTA ES: los items de Miro que nos interesan para extraer material.
# 'embed' = video incrustado; 'link' = link pegado; 'card' = tarjeta con texto;
# 'frame' = marco (modulo del curso); 'image' = captura; 'document' = PDF.
INTERESAN = {"embed", "link", "card", "frame", "image", "document", "text", "sticky_note"}


def clasificar(url):
    """Devuelve la etiqueta de un URL, o 'otro' si no matchea ningún patrón."""
    for etiqueta, patron in PATRONES:
        if patron.search(url or ""):
            return etiqueta
    return "otro"


def id_de_board(entrada):
    """Saca el board_id de una URL de Miro o lo usa tal cual.

    NOTA ES: en las URLs de Miro el id va después de /board/ y termina con '='
    (es un id en base64 con padding). Hay que conservarlo tal cual, con el
    '=' final: si se quita, la API responde 404.
    """
    if "miro.com" in entrada:
        m = re.search(r"/board/([^/?#]+)", entrada)
        if m:
            return m.group(1)
        return None
    return entrada.strip() or None


# ---------------------------------------------------------------------------
# 2) Lectura de los items
# ---------------------------------------------------------------------------

def items_desde_api(board_id, token, limite=50):
    """Descarga todos los items del tablero paginando con cursor.

    NOTA ES: la paginacion de Miro es por cursor, no por offset. Cada respuesta
    trae 'cursor' (el siguiente) y 'total' (cuantos hay en total). Se corta
    cuando vuelve el cursor vacio o cuando ya se stitched todo el total.
    """
    items, cursor, total = [], None, None
    while True:
        url = "%s/boards/%s/items?limit=%d" % (API, urllib.parse.quote(board_id), limite)
        if cursor:
            url += "&cursor=" + urllib.parse.quote(cursor)
        peticion = urllib.request.Request(url, headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/json",
        })
        try:
            with urllib.request.urlopen(peticion, timeout=60) as r:
                datos = json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            print("ERROR Miro API %s: %s" % (e.code, e.reason))
            if e.code in (401, 403):
                print("  -> token invalido o sin scope boards:read")
            if e.code == 404:
                print("  -> board_id incorrecto o el tablero no es visible para ese token")
            sys.exit(2)

        lote = datos.get("data") or []
        items.extend(lote)
        total = datos.get("total", total)
        cursor = datos.get("cursor")
        print("  descargados %d/%s items" % (len(items), total if total is not None else "?"))
        if not lote or not cursor:
            break
    return items


def items_desde_archivo(ruta):
    """Parsea un archivo exportado de Miro: CSV, backup .rtb/.miro (ZIP) o PDF.

    NOTA ES: hoy Miro exporta el backup como .rtb (antes .miro). Si es un ZIP
    se busca dentro el JSON con mas items; si no es ZIP (o no hay JSON legible)
    se cae a un escaneo binario de URLs, que sigue sirviendo para localizar
    los videos y los links a workflows aunque el formato sea propietario.
    """
    ext = os.path.splitext(ruta)[1].lower()

    if ext == ".csv":
        return items_desde_csv(ruta)
    if ext == ".pdf":
        return items_desde_pdf(ruta)

    if zipfile.is_zipfile(ruta):
        mejor = []
        with zipfile.ZipFile(ruta) as z:
            for nombre in z.namelist():
                if not nombre.lower().endswith(".json"):
                    continue
                try:
                    contenido = json.loads(z.read(nombre).decode("utf-8"))
                except Exception:
                    continue
                candidatos = []
                if isinstance(contenido, list):
                    candidatos = contenido
                elif isinstance(contenido, dict):
                    for clave in ("items", "data", "elements"):
                        if isinstance(contenido.get(clave), list):
                            candidatos = contenido[clave]
                            break
                if len(candidatos) > len(mejor):
                    mejor = candidatos
                    print("  items leidos de %s (%d)" % (nombre, len(candidatos)))
        if mejor:
            return mejor
        print("  el ZIP no traia items en JSON: escaneo binario de URLs")
        return items_por_urls(ruta)

    print("  formato no ZIP: escaneo binario de URLs")
    return items_por_urls(ruta)


def items_desde_csv(ruta):
    """Parsea el CSV de 'Export to spreadsheet' de Miro.

    NOTA ES: el CSV de Miro trae, por item, el texto, la descripcion/URL de la
    tarjeta y los tags. Las columnas pueden venir con o sin encabezado, asi
    que se leen todas las celdas y de cada fila se toma la primera no vacia
    como titulo y el resto como material.

    Detalle propio de los tableros del curso: las secciones del tablero son
    tarjetas cuyo texto esta TODO EN MAYUSCULAS y sin URL. Se detectan y se
    guardan como 'frame' (modulo), y cada item posterior queda anotado con la
    seccion a la que pertenece.
    """
    import csv

    items = []
    seccion = None
    with open(ruta, encoding="utf-8-sig", errors="replace", newline="") as f:
        for i, fila in enumerate(csv.reader(f)):
            celdas = [c.strip() for c in fila if c and c.strip()]
            if not celdas:
                continue
            titulo = celdas[0]
            resto = " | ".join(celdas[1:])
            letras = [c for c in titulo if c.isalpha()]
            mayus = sum(1 for c in letras if c.isupper())
            ratio_mayus = (mayus / len(letras)) if letras else 0
            es_seccion = (len(titulo) <= 80
                          and "http" not in titulo
                          and ratio_mayus >= 0.7
                          and " " in titulo)
            if es_seccion:
                seccion = titulo
                items.append({"id": str(i), "type": "frame",
                              "data": {"title": titulo}, "position": {},
                              "seccion": titulo})
                continue
            items.append({"id": str(i), "type": "card",
                          "data": {"title": titulo, "description": resto},
                          "position": {}, "seccion": seccion})
    print("  filas leidas del CSV: %d" % len(items))
    return items


def items_por_urls(ruta):
    """Escaneo binario: encuentra todas las URLs del archivo y las devuelve
    como items sinteticos (tipo 'link').

    NOTA ES: es la red de seguridad. Aunque el formato del backup sea
    propietario, las URLs (de los embeds de video y de los links a los
    workflows) quedan escritas en el archivo y se pueden recuperar con una
    expresion regular sobre los bytes.
    """
    with open(ruta, "rb") as f:
        datos = f.read()
    patron = re.compile(rb"https?://[\x20-\x7e]{6,400}")
    vistas, items = set(), []
    for m in patron.finditer(datos):
        url = m.group(0).decode("ascii", "ignore").rstrip(".,;'\")]}>")
        url = url.split('"')[0].split("\\")[0]
        if url in vistas:
            continue
        vistas.add(url)
        items.append({"id": str(len(items)), "type": "link",
                      "data": {"url": url}, "position": {}})
    print("  URLs encontradas en el binario: %d" % len(items))
    return items


def items_desde_pdf(ruta):
    """De un PDF solo se pueden sacar las URLs visibles (enlaces y QR).

    NOTA ES: el PDF sirve para leer el tablero, no para extraer la estructura.
    Lo que se rescata son los links (workflows, Miro, docs) y los titulos.
    """
    try:
        from pypdf import PdfReader
    except ImportError:
        try:
            from PyPDF2 import PdfReader
        except ImportError:
            print("  (sin pypdf instalado: el PDF no aporta URLs)")
            return []
    items = []
    lector = PdfReader(ruta)
    for i, pagina in enumerate(lector.pages):
        texto = pagina.extract_text() or ""
        for url in URL_EN_TEXTO.findall(texto):
            items.append({"id": "%d-%d" % (i, len(items)), "type": "text",
                          "data": {"content": texto[:120], "url": url}, "position": {}})
    print("  paginas leidas: %d" % len(lector.pages))
    return items


# ---------------------------------------------------------------------------
# 3) Extraccion de URLs y texto de cada item
# ---------------------------------------------------------------------------

URL_EN_TEXTO = re.compile(r"https?://[^\s\"'<>\)\]]+")
ID_YOUTUBE = re.compile(r"(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{11})")


def texto_de(item):
    """Saca el texto plano de un item, sea del tipo que sea."""
    data = item.get("data") or {}
    partes = []
    for clave in ("title", "content", "description", "text"):
        valor = data.get(clave)
        if isinstance(valor, str) and valor.strip():
            partes.append(valor)
    return "\n".join(partes).strip()


def urls_de(item):
    """Saca todas las URLs de un item: de sus links, de su data y de su texto."""
    encontradas = []
    for link in item.get("links") or []:
        url = link.get("url")
        if url:
            encontradas.append(url)
    data = item.get("data") or {}
    for clave in ("url", "imageUrl", "resourceId"):
        valor = data.get(clave)
        if isinstance(valor, str) and valor.startswith("http"):
            encontradas.append(valor)
    html = data.get("html")
    if isinstance(html, str):
        encontradas.extend(URL_EN_TEXTO.findall(html))
    encontradas.extend(URL_EN_TEXTO.findall(texto_de(item)))
    # deduplicar conservando orden
    vistas, unicas = set(), []
    for u in encontradas:
        limpio = u.rstrip(".,;")
        if limpio not in vistas:
            vistas.add(limpio)
            unicas.append(limpio)
    return unicas


def posicion_de(item):
    pos = item.get("position") or {}
    return {"x": pos.get("x"), "y": pos.get("y")}


def id_youtube(url):
    m = ID_YOUTUBE.search(url or "")
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# 4) Informe
# ---------------------------------------------------------------------------

def construir_indice(items):
    """Clasifica los items y arma el indice por tipo de material."""
    indice = {
        "videos": [], "workflows": [], "miro_boards": [], "docs": [],
        "pdfs": [], "modelos": [], "cursos": [], "otros": [], "tarjetas": [],
        "modulos": [],
    }
    for item in items:
        tipo = item.get("type")
        urls = urls_de(item)
        texto = texto_de(item)
        if tipo == "frame" and texto:
            indice["modulos"].append({"titulo": texto, "id": item.get("id")})
        if tipo in ("card", "sticky_note", "text") and texto:
            indice["tarjetas"].append({"tipo": tipo, "texto": texto, "id": item.get("id"),
                                       "seccion": item.get("seccion")})
        for url in urls:
            clase = clasificar(url)
            fila = {"url": url, "tipo": item.get("type"), "texto": texto[:200]}
            if clase == "youtube":
                fila["youtube_id"] = id_youtube(url)
                indice["videos"].append(fila)
            elif clase in ("vimeo", "loom", "wistia", "scrive"):
                fila["plataforma"] = clase
                indice["videos"].append(fila)
            elif clase in ("comfy_cloud", "comfy_wf"):
                indice["workflows"].append(fila)
            elif clase == "miro_board":
                indice["miro_boards"].append(fila)
            elif clase == "comfy_docs":
                indice["docs"].append(fila)
            elif clase == "pdf":
                indice["pdfs"].append(fila)
            elif clase in ("huggingface", "civitai", "github"):
                indice["modelos"].append(fila)
            elif clase == "archademy":
                indice["cursos"].append(fila)
            else:
                indice["otros"].append(fila)
    return indice


def md_indice(board_id, titulo, indice, total_items):
    """Arma el informe en Markdown."""
    L = []
    L.append("# Miro — inventario del tablero")
    L.append("")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    L.append("| Board id | `%s` |" % board_id)
    if titulo:
        L.append("| Título | %s |" % titulo)
    L.append("| Items leídos | %d |" % total_items)
    L.append("")
    L.append("## Conteo por tipo de material")
    L.append("")
    L.append("| Tipo | Cantidad |")
    L.append("|---|---|")
    for clave, etiqueta in (("videos", "Videos"), ("workflows", "Workflows de ComfyUI"),
                            ("miro_boards", "Tableros Miro"), ("docs", "Documentación ComfyUI"),
                            ("pdfs", "PDF"), ("modelos", "Modelos (HF/Civitai/GitHub)"),
                            ("cursos", "Curso Archademy"), ("tarjetas", "Tarjetas con texto"),
                            ("modulos", "Módulos (frames)"), ("otros", "Otros enlaces")):
        L.append("| %s | %d |" % (etiqueta, len(indice.get(clave, []))))
    L.append("")

    def bloque(titulo_seccion, clave, con_id_youtube=False):
        filas = indice.get(clave) or []
        if not filas:
            return
        L.append("## %s (%d)" % (titulo_seccion, len(filas)))
        L.append("")
        for f in filas:
            extra = ""
            if con_id_youtube and f.get("youtube_id"):
                extra = "  · id: `%s`" % f["youtube_id"]
            etiqueta = f.get("texto") or ""
            L.append("- [%s](%s)%s" % (etiqueta.replace("\n", " ")[:120] or f["url"], f["url"], extra))
        L.append("")

    bloque("Videos", "videos", con_id_youtube=True)
    bloque("Workflows de ComfyUI", "workflows")
    bloque("Tableros Miro", "miro_boards")
    bloque("Documentación ComfyUI", "docs")
    bloque("PDF", "pdfs")
    bloque("Modelos", "modelos")
    bloque("Curso", "cursos")

    if indice.get("modulos"):
        L.append("## Módulos / frames (%d)" % len(indice["modulos"]))
        L.append("")
        for m in indice["modulos"]:
            L.append("- %s" % m["titulo"].replace("\n", " "))
        L.append("")

    if indice.get("tarjetas"):
        L.append("## Tarjetas con texto (%d)" % len(indice["tarjetas"]))
        L.append("")
        seccion_actual = None
        for t in indice["tarjetas"]:
            sec = t.get("seccion")
            if sec and sec != seccion_actual:
                seccion_actual = sec
                L.append("")
                L.append("### %s" % sec)
                L.append("")
            L.append("- **[%s]** %s" % (t["tipo"], t["texto"].replace("\n", " ")[:300]))
        L.append("")

    bloque("Otros enlaces", "otros")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Inventario de un tablero de Miro")
    grupo = ap.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--url", help="URL del tablero o board_id")
    grupo.add_argument("--file", help="archivo exportado de Miro: .csv, .rtb/.miro (backup) o .pdf")
    ap.add_argument("--token", help="token de Miro (o usá la variable MIRO_ACCESS_TOKEN)")
    ap.add_argument("--out", help="carpeta de salida (por defecto ./)")
    args = ap.parse_args()

    token = args.token or os.environ.get("MIRO_ACCESS_TOKEN")

    titulo, board_id, items = "", None, []
    if args.file:
        print("Leyendo export de Miro:", args.file)
        items = items_desde_archivo(args.file)
    else:
        board_id = id_de_board(args.url)
        if not board_id:
            print("No pude deducir el board_id de:", args.url)
            sys.exit(2)
        if not token:
            print("Falta el token: usá --token o la variable de entorno MIRO_ACCESS_TOKEN.")
            print("  Como obtenerlo: https://developers.miro.com -> OAuth app -> scope boards:read")
            sys.exit(2)
        print("Consultando API Miro, board:", board_id)
        items = items_desde_api(board_id, token)

    indice = construir_indice(items)
    md = md_indice(board_id or "archivo local", titulo, indice, len(items))

    carpeta = args.out or "."
    os.makedirs(carpeta, exist_ok=True)
    base_md = os.path.join(carpeta, "miro-inventario.md")
    base_json = os.path.join(carpeta, "miro-inventario.json")
    with open(base_md, "w", encoding="utf-8") as f:
        f.write(md)
    with open(base_json, "w", encoding="utf-8") as f:
        json.dump({"board_id": board_id, "total_items": len(items),
                   "indice": indice, "items": items},
                  f, indent=2, ensure_ascii=False)

    print()
    print("Videos: %d | Workflows: %d | Tarjetas: %d | Módulos: %d" % (
        len(indice["videos"]), len(indice["workflows"]),
        len(indice["tarjetas"]), len(indice["modulos"])))
    print("Informe:", base_md)
    print("Datos crudos:", base_json)

    # NOTA ES: los ids de YouTube salen listos para transcribir con
    # scripts/transcribir_youtube.py <video_id>
    ids = []
    for v in indice["videos"]:
        vid = v.get("youtube_id")
        if vid and vid not in ids:
            ids.append(vid)
    if ids:
        print()
        print("Ids de YouTube para transcribir:")
        for i in ids:
            print("  " + i)


if __name__ == "__main__":
    main()
