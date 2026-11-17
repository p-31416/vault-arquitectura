#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
dashboard-casa.py — mosaico de corridas MVP 04.03 casa moderna.

Que hace, en una frase:
    Junta los PNG casa-{WF}-v{NN}-*.png en un HTML mosaico agrupado por flujo.

Como se usa:
    P:\Anaconda\envs\comfyenv\python.exe scripts/dashboard-casa.py
    P:\Anaconda\envs\comfyenv\python.exe scripts/dashboard-casa.py --out activos/web/casa-moderna

Salida:
    activos/web/casa-moderna/index.html + img/ (copias PNG)
"""
# NOTA ES: argparse = opciones de linea de comandos sin if/else manual.
import argparse
# NOTA ES: os.path = armar rutas portable (join, basename, splitext).
import os
# NOTA ES: shutil.copy2 = copiar conservando fecha y permisos.
import shutil
# NOTA ES: struct.unpack = leer bytes binarios como numeros (cabecera PNG).
import struct
# NOTA ES: glob = buscar archivos por patron casa-*.png.
import glob
# NOTA ES: html.escape = mostrar nombres con tildes sin romper el HTML.
import html

# NOTA ES: raiz del vault = carpeta que contiene scripts/ (este archivo).
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# NOTA ES: donde viven las salidas versionadas de la casa.
SALIDAS = os.path.join(RAIZ, "proyectos", "MVP_08-casa-moderna", "flujos", "salidas")

# NOTA ES: orden de presentacion por flujo.
ORDEN_WF = ["F0", "F1cam", "F2sol", "F3inp", "F4mat", "F5"]


# NOTA ES: lee ancho x alto de un PNG desde su cabecera IHDR (bytes 16-24).
def medir_png(ruta):
    try:
        with open(ruta, "rb") as f:
            head = f.read(26)
        if head[:8] != b"\x89PNG\r\n\x1a\n":
            return (0, 0)
        w, h = struct.unpack(">II", head[16:24])
        return (w, h)
    except OSError:
        return (0, 0)


# NOTA ES: wf sale del nombre: casa-{WF}-v{NN}-resto.png -> {WF}.
# NOTA ES: F0b (RealVis canonico) se agrupa como F0.
def wf_de(nombre):
    base = os.path.splitext(os.path.basename(nombre))[0]
    partes = base.split("-")
    if len(partes) >= 2 and partes[0] == "casa":
        return "F0" if partes[1] == "F0b" else partes[1]
    return "otros"


# NOTA ES: arma index.html + copia PNGs a out/img/.
def generar(out):
    os.makedirs(os.path.join(out, "img"), exist_ok=True)
    archivos = sorted(glob.glob(os.path.join(SALIDAS, "casa-*.png")))
    grupos = {}
    for ruta in archivos:
        grupos.setdefault(wf_de(ruta), []).append(ruta)
    # NOTA ES: ordena grupos segun ORDEN_WF; lo desconocido va al final.
    ordenadas = sorted(grupos, key=lambda w: (ORDEN_WF.index(w) if w in ORDEN_WF else 99, w))
    tarjetas = []
    for wf in ordenadas:
        tarjetas.append("<h2>%s</h2><div class='fila'>" % html.escape(wf))
        for ruta in sorted(grupos[wf]):
            nombre = os.path.basename(ruta)
            w, h = medir_png(ruta)
            destino = os.path.join(out, "img", nombre)
            # NOTA ES: copia solo si cambio (fecha/tamano) para no reescribir de mas.
            if not os.path.exists(destino) or os.path.getmtime(ruta) > os.path.getmtime(destino):
                shutil.copy2(ruta, destino)
            estrella = "⭐ " if "keeper" in nombre else ""
            tarjetas.append(
                "<figure><img loading='lazy' src='img/%s'><figcaption>%s%s<br>%dx%d</figcaption></figure>"
                % (html.escape(nombre), estrella, html.escape(nombre), w, h)
            )
        tarjetas.append("</div>")
    cuerpo = "\n".join(tarjetas) if tarjetas else "<p>Sin corridas todavia. Encola F0 y corre este script.</p>"
    pagina = (
        "<!doctype html><html lang='es'><head><meta charset='utf-8'>"
        "<title>Casa moderna MVP 08 — tablero</title>"
        "<style>body{background:#111;color:#eee;font-family:system-ui;padding:20px}"
        ".fila{display:flex;flex-wrap:wrap;gap:12px}figure{margin:0;width:300px}"
        "img{width:100%;border-radius:6px}figcaption{font-size:12px;color:#bbb}</style>"
        "</head><body><h1>MVP 08 — casa moderna (todo local $0)</h1><p>Serie F0 = txt2img RealVisXL v5.0 (seed 42 salvo T2). ⭐ = keeper.</p>" + cuerpo + "</body></html>"
    )
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(pagina)
    print("OK: %d imagenes -> %s" % (len(archivos), os.path.join(out, "index.html")))


def main():
    # NOTA ES: --out permite cambiar la carpeta de salida del tablero.
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(RAIZ, "activos", "web", "casa-moderna"))
    args = ap.parse_args()
    generar(args.out)


if __name__ == "__main__":
    main()
