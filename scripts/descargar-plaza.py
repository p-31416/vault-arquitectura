# NOTA ES: descarga vistas de la PLAZA (espacio urbano) a activos/.../ref.
import time
import urllib.request
from pathlib import Path

REF = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\proyectos\concurso-gaudi-nexus\earth2rhino3d\ref")
FILES = {
    "sf-plaza-gaudi-nw.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/15/Barcelona_-_Pla%C3%A7a_de_Gaud%C3%AD_-_View_NW.jpg",
    "sf-plaza-gaudi-provenza.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Barcelona_-_Pla%C3%A7a_de_Gaud%C3%AD_-_View_West_on_Carrer_de_Proven%C3%A7a.jpg",
    "sf-plaza-gaudi-panorama.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Placa_de_Gaudi_panorama.jpg",
}
for nombre, url in FILES.items():
    dest = REF / nombre
    if dest.exists():
        print("existe:", nombre, dest.stat().st_size, "bytes")
        continue
    time.sleep(10)
    req = urllib.request.Request(url, headers={"User-Agent": "vault-arquitectura/1.0"})
    with urllib.request.urlopen(req, timeout=180) as r, open(dest, "wb") as f:
        f.write(r.read())
    print("ok:", nombre, dest.stat().st_size, "bytes")
