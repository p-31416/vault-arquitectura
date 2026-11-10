"""
referentes_tags.py — vuelca la planilla de tags (CSV) al inventario JSON y detecta
imagenes nuevas en la carpeta (las deja "sin-clasificar").

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/referentes_tags.py --slug aixgaudi

La planilla vive en raw/referentes/<slug>/tags.csv y se puede editar en Excel o
Google Sheets (separador ';'). Tags multiples separados por '|'.

Flujo compartido:
    Emilia sube imagenes al Drive -> carpeta activos/referentes/<slug>/
    -> este script las agrega como pendientes -> se editan en tags.csv
    -> referentes_dashboard.py regenera el tablero.
"""
import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path

EJES = ["tema", "estrategia", "material", "representacion", "programa", "escala", "uso", "estado"]
CAMPOS_TEXTO = ["obra", "autor", "anio", "ciudad", "nota", "fuente_original"]
EXT = {".jpg", ".jpeg", ".png", ".webp"}


def partir(valor):
    return [v.strip() for v in re.split(r"[|,]", valor or "") if v.strip()]


def main():
    ap = argparse.ArgumentParser(description="CSV de tags -> inventario JSON")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--raiz", default=".")
    args = ap.parse_args()

    raiz = Path(args.raiz).resolve()
    carpeta = raiz / "activos" / "referentes" / args.slug
    base = raiz / "raw" / "referentes" / args.slug
    csv_path = base / "tags.csv"
    json_path = base / "referentes.json"

    data = json.loads(json_path.read_text(encoding="utf-8")) if json_path.exists() else {
        "titulo": args.slug, "board": "", "ejes": EJES, "items": []}
    por_archivo = {i["archivo"]: i for i in data["items"]}

    if csv_path.exists():
        with csv_path.open(encoding="utf-8-sig", newline="") as fh:
            filas = list(csv.DictReader(fh, delimiter=";"))
        for fila in filas:
            arch = (fila.get("archivo") or "").strip()
            if not arch:
                continue
            it = por_archivo.get(arch)
            if not it:
                it = {"pin_id": "", "imagen_hash": "", "archivo": arch, "origen": "local",
                      "url": "", "titulo": "", "descripcion": "", "autor": "", "obra": "",
                      "fuente_original": "", "fecha_alta": datetime.now().strftime("%Y-%m-%d"),
                      "fecha_pin": "", "nota": "", "tags": {e: [] for e in EJES}}
                data["items"].append(it)
                por_archivo[arch] = it
            for c in CAMPOS_TEXTO:
                if c in fila and (fila[c] or "").strip():
                    it[c] = fila[c].strip()
            for e in EJES:
                if e in fila and (fila[e] or "").strip():
                    it["tags"][e] = partir(fila[e])
            if not it["tags"].get("uso"):
                it["tags"]["uso"] = [args.slug]
            if not it["tags"].get("estado"):
                it["tags"]["estado"] = ["shortlist"]

    nuevas = 0
    for p in sorted(carpeta.iterdir()) if carpeta.exists() else []:
        if p.suffix.lower() not in EXT or p.name in por_archivo:
            continue
        data["items"].append({
            "pin_id": "", "imagen_hash": "", "archivo": p.name, "origen": "local",
            "url": "", "titulo": "", "descripcion": "", "autor": "", "obra": "",
            "fuente_original": "", "fecha_alta": datetime.now().strftime("%Y-%m-%d"),
            "fecha_pin": "", "nota": "",
            "tags": {"tema": ["sin-clasificar"], "estrategia": [], "material": [],
                     "representacion": [], "programa": [], "escala": [],
                     "uso": [args.slug], "estado": ["shortlist"]},
        })
        nuevas += 1

    sin_csv = [i["archivo"] for i in data["items"] if i["archivo"] not in {
        (f.get("archivo") or "").strip() for f in (filas if csv_path.exists() else [])}]
    data["actualizado"] = datetime.now().strftime("%Y-%m-%d")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    con_tags = sum(1 for i in data["items"] if not (i["tags"]["tema"] == ["sin-clasificar"]))
    print(f"[ok] {len(data['items'])} fichas | clasificadas: {con_tags} | nuevas: {nuevas}")
    print(f"     planilla: {csv_path}")
    if sin_csv:
        print(f"[!] sin fila en tags.csv: {', '.join(sin_csv[:10])}")


if __name__ == "__main__":
    sys.exit(main())
