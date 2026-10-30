# NOTA ES: descarga las 3 fotos Commons elegidas a activos/.../ref (fuera de git).
import urllib.request
from pathlib import Path

REF = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\proyectos\concurso-gaudi-nexus\earth2rhino3d\ref")
FILES = {
    "sf-plaza-pasio-nne.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/82/Barcelona_-_Pla%C3%A7a_de_la_Sagrada_Fam%C3%ADlia_-_View_NNE_on_La_Sagrada_Fam%C3%ADlia_-_Passion_fa%C3%A7ade_I.jpg",
    "sf-plaza-pasio-ne.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/26/Barcelona_-_Pla%C3%A7a_de_la_Sagrada_Fam%C3%ADlia_-_View_NE_on_La_Sagrada_Fam%C3%ADlia_-_Passion_fa%C3%A7ade_I.jpg",
    "sf-plaza-general.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Place_de_la_Sagrada_Fam%C3%ADlia_2.jpg",
}
for nombre, url in FILES.items():
    dest = REF / nombre
    if dest.exists():
        print("existe:", nombre, dest.stat().st_size, "bytes")
        continue
    req = urllib.request.Request(url, headers={"User-Agent": "vault-arquitectura/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        f.write(r.read())
    print("ok:", nombre, dest.stat().st_size, "bytes")
