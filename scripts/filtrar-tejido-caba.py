# NOTA ES: filtra el Tejido Urbano del GCBA (SHP oficial CC-BY-2.5) a un recorte 600x600 m
# y lo deja listo para Rhino (x,y en metros locales, altura real del catastro).
# Primer paso del flujo CABA — hermana de descargar-osm-sagrada.py pero con fuente GCBA.
import json
import math
import os
import shapefile
from pathlib import Path

# NOTA ES: mismos cuatro bordes que el test OSM (Obelisco centro -34.604, -58.3816),
# el mismo cuadrado que la prueba de Sagrada (600 m a cada lado del centro).
SHP = r"C:\Users\Solch16\AppData\Local\Temp\opencode\tejido-caba\unzip\tejido\tejido.shp"
OUT = r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\research\2026-11-01-massing-caba\caba-tejido-obelisco.json"
S, N, W, E = -34.6065, -34.6015, -58.3846, -58.3786

_lat0 = -34.604
_lon0 = -58.3816
_cos0 = math.cos(math.radians(_lat0))
# NOTA ES: conversion equirectangular local, la misma del massing Sagrada
# (y este es plan de que no se pida de > 1 m en 600 m).

# NOTA ES: alturas del Tejido ya vienen en metros reales (Fotogrametria GCBA),
# NO hace falta la regla levels x 3.1 de OSM (la dejamos solo como fallback).
_piso_fallback = 3.1

vols = []
_nulos = 0

r = shapefile.Reader(SHP)
fields = [f[0] for f in r.fields[1:]]
i_alt = fields.index("altura")
i_smp = fields.index("smp")
i_id = fields.index("id")

print("leyendo shp (%d registros totales)..." % len(r))
for shp, rec in zip(r.iterShapes(), r.iterRecords()):
    b = shp.bbox
    if b[0] >= W and b[2] <= E and b[1] >= S and b[3] <= N:
        # NOTA ES: nos quedamos SOLO con el anillo exterior de la primera pieza
        # (los patios son huecos; para massing alcanza el contorno mayor).
        pts = shp.points
        if len(pts) < 3: continue
        h = rec[i_alt]
        # NOTA ES: altura cruda viene decimal clara (2.8, 5.6...). Fallback si viniera nula.
        try:
            h_float = float(str(h).strip().replace(",", "."))
        except ValueError:
            h_float = None
        if h_float is None:
            _nulos += 1
            h_float = 3.0  # PB simple; nunca default 21 m aqui
        x = [(p[0] - _lon0) * 111320.0 * _cos0 for p in pts]
        y = [(p[1] - _lat0) * 110540.0 for p in pts]
        vols.append({
            "x": x, "y": y,
            "h": round(h_float, 2),
            "id": rec[i_id],
            "smp": rec[i_smp],
        })

hs = sorted(dict((v["h"], 1) for v in vols))
med = max(min(v["h"] for v in vols), 0.0)
alturas = sorted(v["h"] for v in vols)
print("volumenes en recorte:", len(vols), "| sin altura:", _nulos)
print("min/med/max:", alturas[0], alturas[len(alturas) // 2], alturas[-1])

Path(OUT).parent.mkdir(parents=True, exist_ok=True)
# NOTA ES: mismo patron sagrada_overpass.json — Rhino lee este JSON sin pings.
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"origen": [_lat0, _lon0], "bbox": [S, W, N, E], "vols": vols}, f, ensure_ascii=False)
print("saved:", OUT, "|", os.path.getsize(OUT), "bytes")
