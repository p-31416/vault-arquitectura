# NOTA ES: descarga segunda tanda (plaza como espacio, ronda 2) a ref/.
import time
import urllib.request
from pathlib import Path

REF = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\proyectos\concurso-gaudi-nexus\earth2rhino3d\ref")
FILES = {
    "sf-plaza-gaudi-sw-pond.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/04/Barcelona_-_Pla%C3%A7a_de_Gaud%C3%AD_-_View_SW_on_La_Sagrada_Fam%C3%ADlia_II.jpg",
    "sf-plaza-queue-se.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/85/Barcelona_-_Pla%C3%A7a_de_la_Sagrada_Fam%C3%ADlia_-_View_SE%2C_Waiting_in_Queue.jpg",
    "sf-plaza-square.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Place_de_la_Sagrada_Fam%C3%ADlia.jpg",
    "sf-plaza-aerea.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/79/Sagrada_Familia%2C_Barcelona_%28P1170690%29.jpg",
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
