#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
archademy_curso_inventory.py — inventario del area de participantes de Archademy (curso AI x Gaudi)

Qué hace, en una frase:
    Lee la pagina del curso (guardada desde un navegador con sesion iniciada, o
    descargada con las cookies de la sesion) y arma el indice de todo el
    material: que lecciones hay, que videos, que workflows de ComfyUI, que
    tableros de Miro y que descargas.

Por que hay dos formas de entrada:
    1) --html <archivo>  -> guardas la pagina con Ctrl+S desde Chrome (con la
       sesion ya iniciada) y el script la parsea. NO requiere cookies.
    2) --url + --cookies -> el script descarga la pagina usando la cabecera
       Cookie que copias de DevTools (F12 > Network > cualquier peticion >
       Request Headers > Cookie).

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\archademy_curso_inventory.py --html "C:\\descargas\\curso.html"
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\archademy_curso_inventory.py --url "https://archademy.ai/my-account/my-competitions/214/?tab=course" --cookies-file "C:\\descargas\\cookies.txt"

Salida:
    archademy-curso-inventario.md + archademy-curso-inventario.json
"""

import argparse
import html
import json
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser

# ---------------------------------------------------------------------------
# 1) Parser: recorre el HTML y junta lo que interesa
# ---------------------------------------------------------------------------

URL_EN_TEXTO = re.compile(r"https?://[^\s\"'<>\)\]]+")
ID_YOUTUBE = re.compile(r"(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{11})")

CLASIFICADORES = [
    ("youtube",     re.compile(r"(youtube\.com/(watch\?|embed/|playlist)|youtu\.be/)", re.I)),
    ("vimeo",       re.compile(r"vimeo\.com/", re.I)),
    ("loom",        re.compile(r"loom\.com/(share|embed)", re.I)),
    ("wistia",      re.compile(r"(wistia\.(com|net)|fast\.wistia\.net)", re.I)),
    ("comfy_cloud", re.compile(r"(cloud\.comfy\.com|comfy\.cloud|app\.comfy\.org)", re.I)),
    ("comfy_wf",    re.compile(r"(\.json($|\?))", re.I)),
    ("miro_board",  re.compile(r"miro\.com/app/board/", re.I)),
    ("comfy_docs",  re.compile(r"docs\.comfy\.org", re.I)),
    ("huggingface", re.compile(r"huggingface\.co", re.I)),
    ("civitai",     re.compile(r"civitai\.com", re.I)),
    ("github",      re.compile(r"github\.com", re.I)),
    ("pdf",         re.compile(r"\.pdf($|\?)", re.I)),
    ("zip",         re.compile(r"\.zip($|\?)", re.I)),
    ("moodle",      re.compile(r"(moodle|/course/lesson|lesson_id=)", re.I)),
]


def clasificar(url):
    for etiqueta, patron in CLASIFICADORES:
        if patron.search(url or ""):
            return etiqueta
    return "otro"


class Extractor(HTMLParser):
    """Recorre el HTML guardando: titulo, encabezados, iframes, links y videos.

    NOTA ES: no hace falta BeautifulSoup: html.parser es de la libreria
    estandar y alcanza para un inventario. Se anotan los enlaces 'a' con su
    texto para poder nombrar cada recurso ("leccion 3 - Rhino to Image").
    """
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.titulo = ""
        self.en_headings = []      # (nivel, texto)
        self.iframes = []          # src de iframes (video embebido)
        self.links = []            # (href, texto)
        self.videos = []           # src de <video>
        self.texto = []
        self._en_texto = False
        self._buffer = []
        self._nivel = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._en_texto = True
        elif tag in ("h1", "h2", "h3", "h4", "h5"):
            self._nivel = tag
            self._buffer = []
            self._en_texto = True
        elif tag == "a":
            self._en_texto = True
            self._buffer = []
            self._href_actual = a.get("href", "")
        elif tag == "iframe":
            src = a.get("src") or a.get("data-src") or ""
            if src:
                self.iframes.append(src)
        elif tag == "video":
            src = a.get("src") or a.get("data-src") or ""
            if src:
                self.videos.append(src)
            for sub in a.get("source", []):
                pass

    def handle_endtag(self, tag):
        if tag == "title":
            self.titulo = "".join(self._buffer).strip()
            self._en_texto = False
        elif tag in ("h1", "h2", "h3", "h4", "h5"):
            txt = "".join(self._buffer).strip()
            if txt:
                self.en_headings.append((self._nivel, txt))
            self._en_texto = False
            self._nivel = None
        elif tag == "a":
            txt = "".join(self._buffer).strip()
            href = getattr(self, "_href_actual", "")
            if href:
                self.links.append((href, txt))
            self._en_texto = False
            self._href_actual = ""

    def handle_data(self, data):
        if self._en_texto:
            self._buffer.append(data)
        self.texto.append(data)


# ---------------------------------------------------------------------------
# 2) Descarga (opcional: si ya guardaste el HTML, no hace falta)
# ---------------------------------------------------------------------------

def descargar(url, cookies=None):
    """Descarga la pagina del curso con la cabecera Cookie de la sesion."""
    cabeceras = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    }
    if cookies:
        cabeceras["Cookie"] = cookies
    peticion = urllib.request.Request(url, headers=cabeceras)
    try:
        with urllib.request.urlopen(peticion, timeout=60) as r:
            return r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        print("ERROR %s al descargar %s" % (e.code, url))
        if e.code in (401, 403):
            print("  -> la pagina pide sesion: las cookies no son validas o faltan.")
            print("  -> proba el modo --html (guardar la pagina con Ctrl+S).")
        sys.exit(2)


# ---------------------------------------------------------------------------
# 3) Indice
# ---------------------------------------------------------------------------

def construir_indice(parser):
    """Clasifica lo encontrado en el HTML."""
    indice = {
        "videos": [], "workflows": [], "miro_boards": [], "docs": [],
        "pdfs": [], "zip": [], "modelos": [], "lecciones": [], "modulos": [],
        "otros": [],
    }

    def agregar(url, texto, origen):
        if not url:
            return
        url = html.unescape(url).strip()
        clase = clasificar(url)
        fila = {"url": url, "texto": (texto or "")[:200], "origen": origen}
        if clase == "youtube":
            m = ID_YOUTUBE.search(url)
            if m:
                fila["youtube_id"] = m.group(1)
            indice["videos"].append(fila)
        elif clase in ("vimeo", "loom", "wistia"):
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
        elif clase == "zip":
            indice["zip"].append(fila)
        elif clase in ("huggingface", "civitai", "github"):
            indice["modelos"].append(fila)
        elif clase == "moodle":
            indice["lecciones"].append(fila)
        else:
            indice["otros"].append(fila)

    for src in parser.iframes:
        agregar(src, "embed", "iframe")
    for src in parser.videos:
        agregar(src, "video", "video")
    for href, txt in parser.links:
        if href.startswith("mailto:") or href.startswith("#"):
            continue
        if href.startswith("/") and not href.lower().endswith((".json", ".pdf", ".zip")):
            continue  # links internos de navegacion: no son material
        agregar(href, txt, "link")
    for u in URL_EN_TEXTO.findall(" ".join(parser.texto)):
        agregar(u, "", "texto")

    for nivel, txt in parser.en_headings:
        indice["modulos"].append({"nivel": nivel, "titulo": txt})
    return indice


def recorrer_json(datos):
    """Recorre un JSON (respuesta de un XHR o salida del colector de consola)
    y devuelve (urls, titulos).

    NOTA ES: las paginas del curso son dinamicas: el listado de lecciones y
    los videos llegan por XHR, no en el HTML inicial. Copiando la respuesta
    del XHR (DevTools > Network > Copy response) o usando el colector de
    consola, se obtiene un JSON que se recorre aqui de forma recursiva: cada
    string que parece una URL se clasifica, y cada objeto con 'title'/'name'
    se toma como titulo de leccion.
    """
    urls, titulos = [], []

    def clave_titulo(d):
        for k in ("title", "name", "lesson_title", "lesson_name", "post_title", "label"):
            v = d.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
        return None

    def caminar(nodo):
        if isinstance(nodo, dict):
            t = clave_titulo(nodo)
            if t:
                titulos.append(t)
            for v in nodo.values():
                caminar(v)
        elif isinstance(nodo, list):
            for v in nodo:
                caminar(v)
        elif isinstance(nodo, str):
            for u in URL_EN_TEXTO.findall(nodo):
                urls.append((u, nodo[:160]))

    caminar(datos)
    # dedup conservando orden
    vistos, unicas = set(), []
    for u, ctx in urls:
        if u not in vistos:
            vistos.add(u)
            unicas.append((u, ctx))
    return unicas, titulos


def md_indice(titulo, indice):
    L = []
    L.append("# Archademy — inventario del curso")
    L.append("")
    if titulo:
        L.append("**Pagina:** %s" % titulo)
        L.append("")
    L.append("| Tipo | Cantidad |")
    L.append("|---|---|")
    for clave, etiqueta in (("videos", "Videos"), ("workflows", "Workflows de ComfyUI"),
                            ("miro_boards", "Tableros Miro"), ("docs", "Documentación ComfyUI"),
                            ("pdfs", "PDF"), ("zip", "ZIP"), ("modelos", "Modelos"),
                            ("lecciones", "Lecciones enlazadas"), ("modulos", "Encabezados"),
                            ("otros", "Otros enlaces")):
        L.append("| %s | %d |" % (etiqueta, len(indice.get(clave, []))))
    L.append("")

    def bloque(titulo_seccion, clave, con_id=False):
        filas = indice.get(clave) or []
        if not filas:
            return
        L.append("## %s (%d)" % (titulo_seccion, len(filas)))
        L.append("")
        for f in filas:
            extra = ""
            if con_id and f.get("youtube_id"):
                extra = "  · id: `%s`" % f["youtube_id"]
            L.append("- [%s](%s)%s" % ((f.get("texto") or f["url"]).replace("\n", " ")[:120], f["url"], extra))
        L.append("")

    bloque("Videos", "videos", con_id=True)
    bloque("Workflows de ComfyUI", "workflows")
    bloque("Tableros Miro", "miro_boards")
    bloque("Documentación", "docs")
    bloque("PDF", "pdfs")
    bloque("ZIP", "zip")
    bloque("Modelos", "modelos")
    bloque("Lecciones", "lecciones")

    if indice.get("modulos"):
        L.append("## Estructura de la pagina (%d encabezados)" % len(indice["modulos"]))
        L.append("")
        for m in indice["modulos"]:
            L.append("- `%s` %s" % (m["nivel"], m["titulo"]))
        L.append("")
    bloque("Otros enlaces", "otros")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Inventario del curso de Archademy")
    ap.add_argument("--html", help="archivo HTML guardado desde el navegador")
    ap.add_argument("--url", help="URL del curso (requiere --cookies o --cookies-file)")
    ap.add_argument("--cookies", help="cabecera Cookie de la sesion")
    ap.add_argument("--cookies-file", help="archivo con la cabecera Cookie")
    ap.add_argument("--out", help="carpeta de salida (por defecto ./)")
    args = ap.parse_args()

    cookies = args.cookies
    if args.cookies_file:
        with open(args.cookies_file, encoding="utf-8") as f:
            cookies = f.read().strip()

    if args.html:
        print("Leyendo archivo local:", args.html)
        with open(args.html, encoding="utf-8", errors="replace") as f:
            contenido = f.read()
    elif args.url:
        print("Descargando:", args.url)
        contenido = descargar(args.url, cookies)
    else:
        print("Falta --html o --url")
        sys.exit(2)

    # ¿es JSON? (respuesta de un XHR o salida del colector de consola)
    if contenido.lstrip()[:1] in ("{", "["):
        print("El archivo es JSON: recorriendolo en profundidad")
        try:
            datos = json.loads(contenido)
        except Exception as e:
            print("JSON invalido:", e)
            sys.exit(2)
        urls, titulos = recorrer_json(datos)
        indice = {"videos": [], "workflows": [], "miro_boards": [], "docs": [],
                  "pdfs": [], "zip": [], "modelos": [], "lecciones": [],
                  "modulos": [{"nivel": "json", "titulo": t} for t in titulos],
                  "otros": []}
        for url, ctx in urls:
            agregar = construir_indice  # noqa: F841 (se usa el patron de abajo)
            clase = clasificar(url)
            fila = {"url": url, "texto": ctx[:200], "origen": "json"}
            if clase == "youtube":
                m = ID_YOUTUBE.search(url)
                if m:
                    fila["youtube_id"] = m.group(1)
                indice["videos"].append(fila)
            elif clase in ("vimeo", "loom", "wistia"):
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
            elif clase == "zip":
                indice["zip"].append(fila)
            elif clase in ("huggingface", "civitai", "github"):
                indice["modelos"].append(fila)
            elif clase == "moodle":
                indice["lecciones"].append(fila)
            else:
                indice["otros"].append(fila)
        parser_titulo = "respuesta JSON"
    else:
        parser = Extractor()
        parser.feed(contenido)
        indice = construir_indice(parser)
        parser_titulo = parser.titulo or args.url or args.html
        titulos = []

    md = md_indice(parser_titulo, indice)

    carpeta = args.out or "."
    os.makedirs(carpeta, exist_ok=True)
    base_md = os.path.join(carpeta, "archademy-curso-inventario.md")
    base_json = os.path.join(carpeta, "archademy-curso-inventario.json")
    with open(base_md, "w", encoding="utf-8") as f:
        f.write(md)
    with open(base_json, "w", encoding="utf-8") as f:
        json.dump({"titulo": parser_titulo, "encabezados": indice.get("modulos", []),
                   "indice": indice}, f, indent=2, ensure_ascii=False)

    print()
    print("Videos: %d | Workflows: %d | Miro: %d | PDF: %d" % (
        len(indice["videos"]), len(indice["workflows"]),
        len(indice["miro_boards"]), len(indice["pdfs"])))
    print("Informe:", base_md)

    ids = []
    for v in indice["videos"]:
        if v.get("youtube_id") and v["youtube_id"] not in ids:
            ids.append(v["youtube_id"])
    if ids:
        print()
        print("Ids de YouTube para transcribir (scripts/transcribir_youtube.py):")
        for i in ids:
            print("  " + i)


if __name__ == "__main__":
    main()
