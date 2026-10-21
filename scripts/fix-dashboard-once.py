"""One-shot: tarjeta 03b fuera, tabla sesiones con MVP, reuniones por dia (rowspan), details colapsables. Solo stdlib."""
import re

P = ("P:/00-repos/proyecto-pi/vault-arquitectura/proyectos/STUDIO_OS-Emilia/"
     "presentacion/dashboard-mes1-emilia.html")
b = open(P, encoding="utf-8", errors="replace").read()

# 1. Fuera tarjeta MVP presupuestos (03b).
b = re.sub(r"<div class=\"mvp\"><b>MVP_03b presupuestos</b>.*?</div>\n?", "", b, count=1)

# 2. Tabla sesiones: quitar col Registrado (4ta td), agregar MVP.
MVPS = ["*", "*", "MVP_04", "n8n", "*", "n8n", "n8n",
        "MVP_02", "MVP_02", "vault", "*", "vault", "*",
        "MVP_01", "MVP_04", "*", "*", "MVP_02",
        "MVP_04", "vault", "MVP_06", "n8n", "MVP_04.02",
        "*", "vault", "*", "vault", "vault", "MVP_04.02",
        "vault", "*", "vault", "MVP_04", "MVP_06", "MVP_02"]
assert len(MVPS) == 35, len(MVPS)


def fix_ses(m):
    head, body = m.group(1), m.group(2)
    rows = [r for r in re.findall(r"<tr>(.*?)</tr>", body, flags=re.S)
            if "<td" in r]
    assert len(rows) == 35, f"filas sesiones: {len(rows)}"
    out = ["<tr><th>Fecha</th><th>Tema</th><th>Duración</th><th>MVP</th></tr>"]
    for r, mv in zip(rows, MVPS):
        tds = re.findall(r"<td.*?</td>", r, flags=re.S)
        out.append(f"<tr>{tds[0]}{tds[1]}{tds[2]}<td>{mv}</td></tr>")
    return head + "\n".join(out) + "\n</table>"


b = re.sub(r"((?:<h2> Sesiones).*?<table>)(.*?)(</table>)", fix_ses, b, count=1, flags=re.S)

# 3. Reuniones agrupadas por dia con rowspan.
GRUPOS = [
    ("11/09 ×4", [("Propuesta automatización + ROI 12h/mes", "s/d"),
                  ("Vault second brain + partnership", "s/d"),
                  ("TP3/TP4 experimentos IA", "s/d"),
                  ("Curso Marcela + plataforma", "s/d")]),
    ("16/09 presencial", [("Primer día presencial: playbook + inventario + stack", "3h")]),
    ("17/09", [("I · Estándares CAD + código gráfico", "59.9 min"),
               ("II · Fathom + Cal.com + disco", "59.9 min"),
               ("III · PC + Magenta + terreno", "42 min"),
               ("IV · PC Emilia + Brasil", "42 min")]),
    ("24/09", [("Emi.ArqOS#01", "60.1 min"),
               ("Flujo IA + bodega", "59.4 min"),
               ("Impromptu (más 1 Patri excluida)", "12.8 min")]),
    ("26/09", [("Corrección planos estudiante", "~60 min"),
               ("Replanteo académico", "~60 min"),
               ("Estándares + entrega", "~58 min")]),
    ("30/09 presencial", [("Sesión presencial semana anterior", "3h")]),
    ("03/10", [("Vinícola propuesta (Leticia+Vanessa)", "~59 min"),
               ("Vinícola concepto", "~57 min")]),
    ("09/10", [("Emi OS: estándares + prompt ChatGPT", "60 min"),
               ("Seguimiento Emi OS", "60 min"),
               ("Seguimiento Emi OS", "59.6 min")]),
    ("14/10 (mañana)", [("Presentación cierre Mes 1 (planificada)", "3h plan.")]),
]
rows = ["<tr><th>Fecha</th><th>Tema tratado</th><th>Duración</th></tr>"]
for fecha, items in GRUPOS:
    for j, (tema, dur) in enumerate(items):
        c0 = f"<td rowspan='{len(items)}'>{fecha}</td>" if j == 0 else ""
        rows.append(f"<tr>{c0}<td>{tema}</td><td class='med'>{dur}</td></tr>")
new_reu = ("\n".join(rows) + "\n</table>\n<p><b>Total medido: ~13.5hs en 13 "
           "Fathom + 6hs en 2 presenciales = ~19.5hs en reuniones.</b> "
           "(11/09 s/d, 14/10 planificada, no suman.)</p>")
b = re.sub(r"(<h2>Reuniones con Emilia.*?</h2>\n)(<table>.*?</table>\n<p><b>Total medido.*?</p>)",
           lambda m: m.group(1) + new_reu, b, count=1, flags=re.S)

# 4. Details colapsables desde SESIONES (semaforo y MVPs quedan visibles).
COLAPSABLES = [" Sesiones (35)", "Semanas (4 + pre)", "Despliegue IA",
               "Fichas por MVP", "Reuniones con Emilia", "Calculadora",
               "Mes 2"]
parts = re.split(r"(?=<h2>)", b)
head, out = parts[0], []
for p in parts[1:]:
    m = re.match(r"<h2>(.*?)</h2>\n?(.*)", p, flags=re.S)
    if m and any(m.group(1).startswith(c) for c in COLAPSABLES):
        out.append(f"<details><summary><b>{m.group(1)}</b> (tocar para desplegar)</summary>\n{m.group(2)}")
        if not out[-1].rstrip().endswith("</details>"):
            out[-1] += "\n</details>"
    else:
        out.append(p)
b = head + "".join(out)
open(P, "w", encoding="utf-8").write(b)

# checks
c = open(P, encoding="utf-8").read()
print("03b fuera:", "MVP_03b" not in c)
print("details:", c.count("<details>"), "| tablas MVP col:",
      len(re.findall(r"<td>(MVP_\S+|n8n|vault|\*)</td>", c)))
print("rowspan:", c.count("rowspan"))
from html.parser import HTMLParser
HTMLParser().feed(c)
print("HTML OK")
