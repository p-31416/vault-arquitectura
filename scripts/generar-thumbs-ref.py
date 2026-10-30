# NOTA ES: genera thumbs 800px (jpg q70) de ref/ para el doc visual.
from pathlib import Path
from PIL import Image

REF = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\proyectos\concurso-gaudi-nexus\earth2rhino3d\ref")
TH = REF / "thumbs"
TH.mkdir(exist_ok=True)

for src in sorted(REF.glob("*.jpg")):
    dst = TH / (src.stem + "_th.jpg")
    if dst.exists():
        print("existe:", dst.name)
        continue
    im = Image.open(src)
    im.thumbnail((800, 800), Image.LANCZOS)
    im.save(dst, "JPEG", quality=70)
    print("ok:", dst.name, im.size, dst.stat().st_size, "bytes")
