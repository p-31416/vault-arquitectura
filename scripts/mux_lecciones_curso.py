#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mux_lecciones_curso.py — extrae las transcripciones de las lecciones del curso (Mux)

Qué hace, en una frase:
    Lee la pagina guardada del area de participantes del curso, encuentra los
    videos (embebidos con Mux) de cada modulo, baja los subtitulos en WebVTT y
    los escribe como transcripcion en raw/yt/transcripts/ con el formato del
    vault (md + srt + txt + origen.json).

Por que funciona con la pagina "dynamic":
    El area de participantes (WooCommerce) arma la lista de modulos en el
    servidor, pero cada video es un iframe de Mux con la URL en el atributo
    data-src. Con la pagina completa guardada (Ctrl+S) esa informacion YA esta
    en el HTML, y los subtitulos cuelgan del CDN de Mux sin token.

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\mux_lecciones_curso.py "G:\\Mi unidad\\OS-Emilia\\AIxGaudi\\My account - Archademy.ai.html"
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\mux_lecciones_curso.py <html> --langs en es --out raw\\yt\\transcripts
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import date

# ---------------------------------------------------------------------------
# 1) Expresiones regulares del HTML del curso
# ---------------------------------------------------------------------------

# El nav lateral tiene un <span class="archademy-course-nav-title"> por modulo,
# en el mismo orden que los paneles (data-module).
RE_NAV = re.compile(r'class="archademy-course-nav-title"[^>]*>(.*?)<', re.S)
RE_PANEL = re.compile(r'class="archademy-course-panel[^"]*"\s+data-module="([^"]+)"')
RE_IFRAME = re.compile(r'data-src="https://iframe\.mediadelivery\.net/embed/[^/"]+/([^"?]+)')
RE_BOARD_PW = re.compile(r'class="archademy-miro-pw-code"[^>]*>([^<]+)<')
RE_BOARD_URL = re.compile(r'href="(https://miro\.com/app/board/[^"]+)"')

# El CDN de Mux donde cuelgan los subtitulos (el prefijo vz-<hash> puede
# cambiar por entorno: se toma del propio HTML si aparece).
RE_CDN = re.compile(r'(https://[a-z0-9\-]+\.b-cdn\.net)/[0-9a-f\-]{8,}')
RE_VTT_IN_HTML = re.compile(r'(https://[a-z0-9\-]+\.b-cdn\.net/[0-9a-f\-]{8,}/captions/([a-z]{2})\.vtt)')


def texto_de(html):
    """Quita tags y colapsa espacios (para los titulos del nav)."""
    limpio = re.sub(r"<[^>]+>", " ", html)
    limpio = re.sub(r"&amp;", "&", limpio)
    limpio = re.sub(r"&#8217;|&rsquo;", "'", limpio)
    return re.sub(r"\s+", " ", limpio).strip()


# ---------------------------------------------------------------------------
# 2) WebVTT -> SRT y TXT (mismo formato que scripts/transcribir_youtube.py)
# ---------------------------------------------------------------------------

RE_TIME = re.compile(r"(\d+):(\d+):(\d+)[.,](\d+)\s*-->\s*(\d+):(\d+):(\d+)[.,](\d+)")
RE_TAG = re.compile(r"<[^>]+>")


def hhmmss(t):
    h, m, s, ms = (int(x) for x in t)
    return "%02d:%02d:%02d,%03d" % (h, m, s, ms)


def vtt_a_srt(vtt):
    """Convierte WebVTT en SRT (queda igual salvo el formato del separador)."""
    bloques = []
    actual = []
    for linea in vtt.replace("\r\n", "\n").split("\n"):
        if linea.strip() == "":
            if actual:
                bloques.append(actual)
                actual = []
        else:
            actual.append(linea)
    if actual:
        bloques.append(actual)

    out, n = [], 0
    for bloque in bloques:
        texto = " ".join(l for l in bloque if not RE_TIME.search(l) and not l.strip().isdigit())
        texto = RE_TAG.sub("", texto).strip()
        tiempos = [l for l in bloque if RE_TIME.search(l)]
        if not tiempos or not texto:
            continue
        m = RE_TIME.search(tiempos[0])
        inicio, fin = hhmmss(m.groups()[:4]), hhmmss(m.groups()[4:])
        n += 1
        out.append("%d\n%s --> %s\n%s\n" % (n, inicio, fin, texto))
    return "\n".join(out)


def srt_a_txt(srt):
    """SRT -> texto con [HH:MM:SS] al inicio de cada cue."""
    lineas, salida, actual = srt.split("\n"), [], ""
    for linea in lineas:
        if "-->" in linea:
            actual = linea.split("-->")[0].strip()[:8]
        elif linea.strip() and not linea.strip().isdigit():
            if actual:
                salida.append("[%s] %s" % (actual, linea.strip()))
                actual = ""
    return "\n".join(salida)


# ---------------------------------------------------------------------------
# 3) Descarga
# ---------------------------------------------------------------------------

def descargar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def cdn_base(html):
    """Deduce la base del CDN de Mux (el prefijo vz-xxxx cambia por entorno)."""
    m = RE_CDN.search(html)
    if m:
        return m.group(1)
    # fallback: el prefijo se puede leer del src de los <source> del player
    m2 = re.search(r'(https://[a-z0-9\-]+\.b-cdn\.net)', html)
    return m2.group(1) if m2 else "https://vz-4ced3a48-15e.b-cdn.net"


# ---------------------------------------------------------------------------
# 4) Escritura en el vault (mismo formato que transcribir_youtube.py)
# ---------------------------------------------------------------------------

def escribir_transcripcion(carpeta, slug, titulo, lang, srt, url_vtt):
    """Escribe .md + .srt + .txt + .origen.json con la convencion del vault."""
    hoy = date.today().isoformat()
    base = "%s_mux-%s.%s" % (hoy, slug, lang)
    ruta_md = os.path.join(carpeta, base + ".md")
    ruta_srt = os.path.join(carpeta, base + ".srt")
    ruta_txt = os.path.join(carpeta, base + ".txt")
    ruta_json = os.path.join(carpeta, "%s_mux-%s.origen.json" % (hoy, slug))

    with open(ruta_srt, "w", encoding="utf-8") as f:
        f.write(srt)
    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write(srt_a_txt(srt))

    duracion = srt.strip().split("\n")[-2] if srt.strip() else ""
    cab = """---
tipo: transcript
fuente: archademy.ai (curso AI x Gaudi, area de participantes)
modulo: %s
titulo: %s
idioma: %s
fecha_creacion: %s
tags: [yt, transcript, curso-ai-gaudi, mux, %s]
---

# %s — %s

> Transcripcion automatica de los subtitulos del modulo del curso (Mux).
> Origen: %s
> Duracion de la pista de subtitulos: %s

""" % (slug, titulo, lang, hoy, slug, titulo, lang, url_vtt, duracion)
    with open(ruta_md, "w", encoding="utf-8") as f:
        f.write(cab + srt_a_txt(srt) + "\n")
    return ruta_md, ruta_srt, ruta_txt


def main():
    ap = argparse.ArgumentParser(description="Transcripciones del curso (Mux)")
    ap.add_argument("html", help="HTML guardado de la pagina del curso")
    ap.add_argument("--langs", nargs="+", default=["en", "es"], help="idiomas a bajar")
    ap.add_argument("--out", default=os.path.join("raw", "yt", "transcripts"))
    args = ap.parse_args()

    if not os.path.isfile(args.html):
        print("No existe:", args.html)
        sys.exit(1)

    with open(args.html, encoding="utf-8", errors="replace") as f:
        html = f.read()

    nav = [texto_de(m) for m in RE_NAV.findall(html)]
    paneles = RE_PANEL.findall(html)
    vids = RE_IFRAME.findall(html)
    cdn = cdn_base(html)
    pw = RE_BOARD_PW.search(html)
    board = RE_BOARD_URL.search(html)

    print("Modulos en el nav : %d" % len(nav))
    print("Paneles con data-module: %d" % len(paneles))
    print("Videos Mux detectados  : %d" % len(vids))
    print("Base CDN de subtitulos  : %s" % cdn)
    if pw:
        print("Password del tablero Miro: %s" % pw.group(1).strip())
    if board:
        print("Tablero Miro: %s" % board.group(1))
    print()

    # Empareja nav (titulos) con paneles (slugs) por orden
    modulos = []
    for i, slug in enumerate(paneles):
        titulo = nav[i] if i < len(nav) else slug
        modulos.append((slug, titulo))

    # Los ids de video se asignan al panel que los contiene: se busca el
    # PRIMER iframe que cae dentro del tramo del panel (entre ese panel y el
    # siguiente). Ojo: data-module aparece tambien en los tabs del nav, asi
    # que hay que usar la posicion del PANEL, no la del primer data-module.
    paneles_pos = list(RE_PANEL.finditer(html))
    asignados = []
    for i, m in enumerate(paneles_pos):
        slug = m.group(1)
        fin_panel = paneles_pos[i + 1].start() if i + 1 < len(paneles_pos) else len(html)
        frag = html[m.end():fin_panel]
        pid = None
        vid = RE_IFRAME.search(frag)
        if vid:
            pid = vid.group(1)
        titulo = nav[i] if i < len(nav) else slug
        asignados.append((slug, titulo, pid))

    os.makedirs(args.out, exist_ok=True)
    indice = []
    for slug, titulo, pid in asignados:
        if not pid:
            indice.append({"modulo": slug, "titulo": titulo, "estado": "sin video"})
            print("%-22s %-55s (sin video)" % (slug, titulo[:55]))
            continue
        print("\n%-22s %s" % (slug, titulo))
        for lang in args.langs:
            url_vtt = "%s/%s/captions/%s.vtt" % (cdn, pid, lang)
            try:
                vtt = descargar(url_vtt)
            except Exception as e:
                print("   [%s] sin subtitulos (%s)" % (lang, getattr(e, "code", "error")))
                indice.append({"modulo": slug, "titulo": titulo, "lang": lang,
                               "estado": "sin subtitulos", "url": url_vtt})
                continue
            srt = vtt_a_srt(vtt)
            md, srt_f, txt_f = escribir_transcripcion(args.out, slug, titulo, lang, srt, url_vtt)
            cues = srt.count(" --> ")
            print("   [%s] OK  %d cues  ->  %s" % (lang, cues, os.path.basename(md)))
            indice.append({"modulo": slug, "titulo": titulo, "lang": lang,
                           "cues": cues, "md": md, "url": url_vtt})

    with open(os.path.join(args.out, "indice-curso-ai-gaudi.json"), "w", encoding="utf-8") as f:
        json.dump({"origen_html": args.html, "cdn": cdn,
                   "miro_board": board.group(1) if board else None,
                   "miro_password": pw.group(1).strip() if pw else None,
                   "modulos": indice}, f, indent=2, ensure_ascii=False)

    print("\nIndice: %s" % os.path.join(args.out, "indice-curso-ai-gaudi.json"))
    print("SIGUIENTE: @contenidos curaduria de las fichas (formato spec v3).")


if __name__ == "__main__":
    main()
