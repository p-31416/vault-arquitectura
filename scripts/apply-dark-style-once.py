"""One-shot: aplica el sistema visual propuesta-oscuro al dashboard AutoCAD."""
import re

BASE = "P:/00-repos/proyecto-pi/vault-arquitectura/proyectos/STUDIO_OS-Emilia/presentacion/"
main = open(BASE + "dashboard-mes1-emilia.html", encoding="utf-8").read()
auto = open(BASE + "dashboard-autocad.html", encoding="utf-8").read()

mains = re.search(r"<style>(.*?)</style>", main, flags=re.S).group(1)
extra = """
.stepper{display:flex;align-items:center;gap:0;margin:18px 0;flex-wrap:wrap}
.step{text-align:center;min-width:110px}
.step .dot{width:38px;height:38px;border-radius:50%;margin:0 auto;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:16px;background:#2a2a2e;border:2px solid #555;color:#aaa}
.step.done .dot{background:#1d3a24;border-color:#7fd08a;color:#7fd08a}
.step.now .dot{background:#3a2f14;border-color:#ffb454;color:#ffb454}
.step small{color:var(--muted);font-size:11px}
.card{border-left:4px solid #6aa8ff}
.card.g{border-left-color:#7fd08a}.card.y{border-left-color:#ffb454}
.flow{display:flex;gap:0;align-items:stretch;flex-wrap:wrap;margin:14px 0}
.fnode{background:var(--surface);border:1px solid #6aa8ff;border-radius:10px;padding:10px 14px;font-size:13px;max-width:190px}
.farr{align-self:center;color:#ffb454;font-weight:800;padding:0 8px;font-size:18px}
ol li,ul li{margin:6px 0;font-size:14px}
"""
auto = re.sub(r"<style>.*?</style>", "<style>" + mains + extra + "</style>",
              auto, count=1, flags=re.S)

old_h1 = "<h1>Reporte AutoCAD"
assert old_h1 in auto
auto = auto.replace(
    "<body>",
    "<body>\n<header class=\"top\"><div class=\"wrap\">\n"
    "<div class=\"bar\"><div class=\"brand\">Studio OS <i>· AutoCAD</i></div></div>\n"
    "<nav class=\"tabs\"><a href=\"dashboard-mes1-emilia.html\">← Mes 1</a></nav>\n"
    "</div></header>\n<main class=\"wrap\">", 1)
auto = auto.replace(
    "</body>",
    "\n<p class=\"small\">Studio OS × Emilia Pimenta — Reporte AutoCAD Mes 1.</p>\n</main>\n</body>", 1)
auto = auto.replace(
    "<h1>Reporte AutoCAD",
    "<div class=\"hero\">\n<div class=\"eyebrow\">Reporte AutoCAD · REP-ARAOZ + SET_01</div>\n<h1>Plano, SET y <em>ventana dinámica.</em></h1>\n<p class=\"lead\">Extracción medida del plano, todo SET_01 instalado y la ventana paso a paso.</p>\n</div>\n<h1 style=\"display:none\">Reporte AutoCAD", 1)

open(BASE + "dashboard-autocad.html", "w", encoding="utf-8").write(auto)
print("OK estilo aplicado")

from html.parser import HTMLParser
HTMLParser().feed(auto)
print("HTML OK")
