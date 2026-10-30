# NOTA ES: descarga footprints OSM (building=*) del entorno Sagrada via Overpass.
# Generado para: proyectos/concurso-gaudi-nexus/earth2rhino3d (Fase C base open).
import json
import urllib.request
from pathlib import Path

OUT = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\proyectos\concurso-gaudi-nexus\earth2rhino3d\base\sagrada_overpass.json")

# Bbox Eixample entorno Sagrada REAL (templo 41.4036, 2.1744):
# 600 m utiles para PC 8 GB: S=41.4005 N=41.4065 W=2.1705 E=2.1785
QUERY = """
[out:json][timeout:90];
(
  way["building"](41.4005,2.1705,41.4065,2.1785);
  relation["building"](41.4005,2.1705,41.4065,2.1785);
);
out body;
>;
out skel qt;
""".strip()

ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]

print("querying overpass...")
data = None
for ep in ENDPOINTS:
    try:
        req = urllib.request.Request(
            ep,
            data=QUERY.encode("utf-8"),
            headers={"User-Agent": "vault-arquitectura-earth2rhino/1.0"},
        )
        with urllib.request.urlopen(req, timeout=90) as r:
            data = json.loads(r.read().decode("utf-8"))
        print("OK:", ep)
        break
    except Exception as e:
        print("FAIL:", ep, "->", str(e)[:120])
if data is None:
    raise SystemExit("ERROR: todos los endpoints Overpass fallaron (502/429 típico). Reintentar en 5 min.")

els = data.get("elements", [])
print("elements:", len(els))
ways = [e for e in els if e.get("type") == "way"]
nodes = {e["id"]: e for e in els if e.get("type") == "node"}
with_height = sum(1 for w in ways if "height" in (w.get("tags") or {}))
with_levels = sum(1 for w in ways if "building:levels" in (w.get("tags") or {}))
print("ways:", len(ways), "nodes:", len(nodes), "con height:", with_height, "con levels:", with_levels)
OUT.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
print("saved:", OUT)
