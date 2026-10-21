"""One-shot: clases usadas en el body vs definidas en el CSS del dashboard."""
import re
import sys

BASE = ("P:/00-repos/proyecto-pi/vault-arquitectura/proyectos/STUDIO_OS-Emilia/"
        "presentacion/")
name = sys.argv[1] if len(sys.argv) > 1 else "dashboard-mes1-emilia.html"
b = open(BASE + name, encoding="utf-8", errors="replace").read()
css, body = b.split("<style>", 1)[1].split("</style>", 1)
used = set()
for m in re.findall(r'class="([^"]+)"', body):
    used.update(m.split())
print("USADAS:", sorted(used))
falt = [c for c in sorted(used)
        if not re.search(r"\." + re.escape(c) + r"[\{,:\s\.]", css)]
print("SIN ESTILO:", falt)
for tag in ['header class="top"', 'main class="wrap"', 'div class="hero"']:
    print(tag, "->", body.count(tag))
