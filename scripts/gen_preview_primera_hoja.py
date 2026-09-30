#!/usr/bin/env python3
# NOTA ES: Genera un PDF nuevo de una sola hoja desde la preview Markdown.
# NOTA ES: No modifica el contrato completo ni sus PDFs existentes.
import pathlib
import subprocess
import markdown

md_path = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia-preview-primera-hoja.md")
html_path = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\temp\muestras-pdf\contrato-studio-os-emilia-preview-primera-hoja.html")
pdf_path = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia-preview-primera-hoja.pdf")
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

text = md_path.read_text(encoding="utf-8")
if text.startswith("---"):
    parts = text.split("---", 2)
    text = parts[2]
body = markdown.markdown(text, extensions=["extra", "tables", "sane_lists"])
css = """
@page { size: A4; margin: 14mm 15mm 14mm 15mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 9pt; line-height: 1.1; color: #1a1a1a; max-width: 180mm; margin: 0 auto; }
header { border-bottom: 2px solid #111; padding-bottom: 6px; margin-bottom: 9px; display: flex; justify-content: space-between; align-items: end; }
header .logo { font-weight: 700; font-size: 12pt; letter-spacing: .06em; }
header .meta { font-size: 7pt; color: #555; }
h1 { font-size: 12pt; text-align: center; margin: 5px 0 2px; }
.sub { text-align: center; font-size: 6.5pt; color: #555; margin-bottom: 8px; }
h2 { font-size: 9.5pt; background: #f2f2f2; padding: 3px 7px; margin: 8px 0 4px; border-left: 3px solid #111; page-break-after: avoid; }
p { margin: 3px 0; orphans: 3; widows: 3; }
strong { color: #111; }
"""
header = """
<header><div class="logo">PITAUTECH<br><span style="font-size:7pt;font-weight:400;color:#666;">Arq. M. Sol Azcona</span></div><div class="meta">Studio OS — Programa I+D · Preview primera hoja</div></header>
<h1 style="text-align:center;font-size:13pt;margin:5px 0 2px;">CONTRATO DE PRESTACIÓN DE SERVICIOS</h1>
<p class="sub">Studio OS — Programa I+D · 190 hs totales ~16 hs/sem · Firma 24/09/2026</p>
"""
html = f"<!doctype html><html lang='es'><head><meta charset='utf-8'><title>Preview primera hoja</title><style>{css}</style></head><body>{header}{body}</body></html>"
html_path.parent.mkdir(parents=True, exist_ok=True)
html_path.write_text(html, encoding="utf-8")
result = subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw", f"--print-to-pdf={pdf_path}", str(html_path)], capture_output=True, text=True)
print(result.stderr.strip())
print(f"PDF: {pdf_path} ({pdf_path.stat().st_size} bytes)")
