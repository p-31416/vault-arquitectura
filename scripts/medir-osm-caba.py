# NOTA ES: mide la densidad OSM de CABA (equivalente del test Sagrada: 1054 footprints, 474 con levels).
# Calca del flujo Barcelona: scripts/descargar-osm-sagrada.py — mismo Overpass, mismo estilo, bbox CABA.
# Hoy (2026-11-01) shell Windows falló por TLS; esta vía python con POST es la que anda bien.
import json
import urllib.request
from pathlib import Path

# NOTA ES: salida del informe bruto en activos/research/ (binarios nunca van a git).
OUT = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\research\2026-11-01-massing-caba\osm-caba-obelisco.json")

# Bbox de prueba ~600 m en el microcentro/Obelisco (-34.6037, -58.3816):
# S=-34.6065 N=-34.6015 W=-58.3846 E=-58.3786
QUERY = """
[out:json][timeout:90];
(
  way["building"](-34.6065,-58.3846,-34.6015,-58.3786);
  relation["building"](-34.6065,-58.3846,-34.6015,-58.3786);
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

print("querying overpass (CABA Obelisco 600m)...")
data = None
for ep in ENDPOINTS:
    try:
        req = urllib.request.Request(
            ep,
            # NOTA ES: Overpass acepta POST con la query como body (igual que el script Sagrada).
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
    raise SystemExit("ERROR: todos los endpoints Overpass fallaron (429/502 típico). Reintentar en 5 min.")

els = data.get("elements", [])
ways = [e for e in els if e.get("type") == "way"]
nodes = {e["id"]: e for e in els if e.get("type") == "node"}
with_height = sum(1 for w in ways if "height" in (w.get("tags") or {}))
with_levels = sum(1 for w in ways if "building:levels" in (w.get("tags") or {}))
print("elements:", len(els))
print("ways:", len(ways), "nodes:", len(nodes), "con height:", with_height, "con levels:", with_levels)

# NOTA ES: guardamos el JSON completo para reuso (mismo patrón sagrada_overpass.json).
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
print("saved:", OUT)
