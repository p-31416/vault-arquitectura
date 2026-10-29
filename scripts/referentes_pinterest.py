"""
referentes_pinterest.py â€” baja un tablero PUBLICO de Pinterest a una carpeta local
y mantiene un inventario JSON (una ficha por pin) que despues consume
referentes_dashboard.py.

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/referentes_pinterest.py ^
        --board https://ar.pinterest.com/usuario/tablero/ --slug aixgaudi

Salida:
    activos/referentes/<slug>/ref-01.jpg ...      (imagenes, gitignored)
    raw/referentes/<slug>/referentes.json         (inventario + tags)

El JSON se MERGEA por pin_id: si ya existe, conserva tags, nota y estado.
Requiere que el tablero sea publico (Pinterest expone /tablero.rss sin login).
"""
import argparse
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from html import unescape
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

EJES = ["tema", "estrategia", "material", "representacion", "uso", "estado"]


def fetch(url, timeout=40):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Referer": "https://ar.pinterest.com/",
        "Accept": "image/avif,image/webp,image/*,*/*;q=0.8",
    })
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def limpiar(html):
    txt = re.sub(r"<[^>]+>", " ", unescape(html or ""))
    return re.sub(r"\s+", " ", txt).strip()


def hash_imagen(item):
    html = item.findtext("description") or ""
    m = re.search(r"i\.pinimg\.com/\d+x/([a-f0-9]{2})/([a-f0-9]{2})/([a-f0-9]{2})/([a-f0-9]{32})\.jpg", html)
    if not m:
        return None
    return m.group(4)


def url_original(h):
    return f"https://i.pinimg.com/originals/{h[:2]}/{h[2:4]}/{h[4:6]}/{h}.jpg"


def parsear_rss(xml_bytes):
    root = ET.fromstring(xml_bytes)
    canal = root.find("channel")
    titulo = (canal.findtext("title") or "").strip()
    items = []
    for it in canal.findall("item"):
        link = (it.findtext("link") or "").strip()
        m = re.search(r"/pin/([^/]+)/", link)
        if not m:
            continue
        h = hash_imagen(it)
        if not h:
            continue
        items.append({
            "pin_id": m.group(1),
            "url": link,
            "imagen_hash": h,
            "titulo_pin": limpiar(it.findtext("title")),
            "descripcion_pin": limpiar(it.findtext("description")),
            "fecha_pin": (it.findtext("pubDate") or "").strip(),
        })
    return titulo, items


def cargar_json(path):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"titulo": "", "board": "", "ejes": EJES, "items": []}


def main():
    ap = argparse.ArgumentParser(description="Pinterest board -> carpeta local + inventario JSON")
    ap.add_argument("--board", required=True, help="URL publica del tablero")
    ap.add_argument("--slug", required=True, help="nombre de carpeta, ej: aixgaudi")
    ap.add_argument("--raiz", default=".", help="raiz del vault")
    ap.add_argument("--dry-run", action="store_true", help="no descarga, solo inventaria")
    args = ap.parse_args()

    raiz = Path(args.raiz).resolve()
    carpeta = raiz / "activos" / "referentes" / args.slug
    json_path = raiz / "raw" / "referentes" / args.slug / "referentes.json"
    carpeta.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)

    board = args.board.rstrip("/")
    print(f"[1/3] Leyendo {board}.rss")
    titulo, pins = parsear_rss(fetch(board + ".rss"))
    print(f"      tablero '{titulo}' -> {len(pins)} pins con imagen")

    data = cargar_json(json_path)
    data["titulo"] = data.get("titulo") or titulo
    data["board"] = board
    data["ejes"] = EJES
    existentes = {i["pin_id"]: i for i in data["items"]}
    por_hash = {i["imagen_hash"]: i for i in data["items"] if i.get("imagen_hash")}

    nuevo, descargado, salteado = 0, 0, 0
    for pin in pins:
        prev = existentes.get(pin["pin_id"]) or por_hash.get(pin["imagen_hash"])
        if prev:
            item = prev
        else:
            n = len(data["items"]) + 1
            item = {
                "pin_id": pin["pin_id"],
                "imagen_hash": pin["imagen_hash"],
                "archivo": f"ref-{n:02d}.jpg",
                "origen": "pinterest",
                "url": pin["url"],
                "titulo": pin["titulo_pin"],
                "descripcion": pin["descripcion_pin"],
                "autor": "",
                "obra": "",
                "fuente_original": "",
                "fecha_alta": datetime.now().strftime("%Y-%m-%d"),
                "fecha_pin": pin["fecha_pin"],
                "nota": "",
                "tags": {e: (["sin-clasificar"] if e == "tema" else []) for e in EJES},
            }
            item["tags"]["uso"] = [args.slug]
            item["tags"]["estado"] = ["shortlist"]
            data["items"].append(item)
            nuevo += 1

        destino = carpeta / item["archivo"]
        if destino.exists():
            salteado += 1
            continue
        if args.dry_run:
            continue
        try:
            destino.write_bytes(fetch(url_original(pin["imagen_hash"]), timeout=60))
            descargado += 1
        except Exception as e:  # 404 -> probamos 736x
            try:
                alt = f"https://i.pinimg.com/736x/{pin['imagen_hash'][:2]}/{pin['imagen_hash'][2:4]}/{pin['imagen_hash'][4:6]}/{pin['imagen_hash']}.jpg"
                destino.write_bytes(fetch(alt, timeout=60))
                descargado += 1
            except Exception:
                print(f"      ! fallo {item['archivo']}: {e}")

    data["actualizado"] = datetime.now().strftime("%Y-%m-%d")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[2/3] nuevas fichas: {nuevo} | imagenes bajadas: {descargado} | ya estaban: {salteado}")
    print(f"[3/3] inventario: {json_path}")
    print(f"      total en tablero: {len(data['items'])}")


if __name__ == "__main__":
    sys.exit(main())

