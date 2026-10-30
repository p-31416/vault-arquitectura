# NOTA ES: audita de donde salen las alturas del massing (pregunta del estudio:
# manzana mide 34 m y parte baja 39 m, parece alto para Eixample ~20 m).
import json
from collections import Counter

P = r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\proyectos\concurso-gaudi-nexus\earth2rhino3d\base\sagrada_overpass.json"
data = json.load(open(P, encoding="utf-8"))
ways = [e for e in data["elements"] if e.get("type") == "way"]

POR_NIVEL = 3.1
DEFAULT = 21.0

def altura(tags):
    tags = tags or {}
    if "height" in tags:
        try:
            return float(str(tags["height"]).replace("m", "").strip().split(" ")[0]), "height"
        except Exception:
            pass
    for k in ("building:levels", "levels"):
        if k in tags:
            try:
                return max(3.0, float(str(tags[k]).split(";")[0]) * POR_NIVEL), k
            except Exception:
                pass
    return DEFAULT, "default-21"

alturas = []
fuente = Counter()
niveles = Counter()
altos = []
for w in ways:
    h, f = altura(w.get("tags", {}))
    alturas.append(h)
    fuente[f] += 1
    tags = w.get("tags", {}) or {}
    lv = tags.get("building:levels", tags.get("levels", "-"))
    niveles[str(lv)] += 1
    if h >= 30:
        altos.append((h, lv, tags.get("name", tags.get("addr:street", "-"))))

alturas.sort()
print("ways:", len(ways))
print("fuente altura:", dict(fuente))
print("min/mediana/max:", alturas[0], alturas[len(alturas)//2], alturas[-1])
print("distribucion levels:", dict(sorted(niveles.items(), key=lambda x: str(x[0]))))
print("edificios >= 30 m:", len(altos))
for h, lv, nombre in sorted(altos, reverse=True)[:15]:
    print("  %.1f m | levels=%s | %s" % (h, lv, nombre))
