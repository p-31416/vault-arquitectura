# NOTA ES: Genera PDF fiel desde proyectos/STUDIO_OS-Emilia/legal/contrato-studio-os-emilia.md
# Qué hace: lee el .md real, lo convierte a HTML con markdown (passthrough HTML), lo envuelve con CSS paged media igual que la muestra, y lo imprime via Chrome headless
# Por qué: garantiza que .md y .pdf tengan EXACTAMENTE la misma info (no muestra paralela)
# Uso: C:\Users\Solch16\AppData\Local\Programs\Python\Python312\python.exe scripts/md_a_pdf_contrato.py
import pathlib, subprocess, markdown

md_path = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia.md")
html_tmp = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\temp\muestras-pdf\contrato-studio-os-emilia.tmp.html")
pdf_out = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia.pdf")
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

text = md_path.read_text(encoding="utf-8")
# NOTA ES: quitamos el frontmatter YAML (--- ... ---) porque no debe aparecer en el PDF
if text.startswith("---"):
    parts = text.split("---", 2)
    if len(parts) >= 3:
        text = parts[2]
# NOTA ES: markdown con extras para tablas y saltos
html_body = markdown.markdown(text, extensions=["extra", "tables", "sane_lists"])

# NOTA ES: CSS compacto legible — margen reducido para <5 páginas
css = """
  @page { size: A4; margin: 14mm 15mm 18mm 15mm; }
  @page { @bottom-center { content: "Hoja " counter(page) " de " counter(pages); font-family: Arial, sans-serif; font-size: 7pt; color: #666; } }
  * { box-sizing: border-box; }
  body { font-family: 'Georgia','Times New Roman',serif; font-size: 9.25pt; line-height: 1.12; color:#1a1a1a; max-width:180mm; margin:0 auto; }
  header { border-bottom:2px solid #111; padding-bottom:6px; margin-bottom:10px; display:flex; justify-content:space-between; align-items:end; }
  header .logo { font-weight:700; font-size:12pt; letter-spacing:0.06em; line-height:1.1; }
  header .meta { font-size:7pt; color:#555; text-align:right; }
  h1 { font-size:12pt; text-align:center; margin:6px 0 2px; letter-spacing:0.04em; }
  .sub { text-align:center; font-size:6.5pt; color:#555; margin-bottom:10px; }
  h2 { font-size:9.5pt; background:#f2f2f2; padding:3px 7px; margin:10px 0 4px; page-break-after:avoid; border-left:3px solid #111; }
  h3 { font-size:9pt; margin:8px 0 4px; page-break-after:avoid; background:#f2f2f2; padding:2px 7px; border-left:3px solid #666; }
  p { margin:4px 0; orphans:3; widows:3; }
  ul.novena-bullets { font-size:9pt; line-height:1.06; margin-top:2px; margin-bottom:3px; page-break-inside:avoid; break-inside:avoid; }
  li { margin-bottom:2px; }
  table { width:100%; border-collapse:collapse; margin:6px 0; font-size:8.5pt; page-break-inside:avoid; }
  th { background:#111; color:#fff; text-align:left; padding:4px 6px; font-weight:600; }
  td { border:1px solid #bbb; padding:4px 6px; background:#fff !important; }
  tr:nth-child(even) td { background:#fff !important; }
  blockquote { font-size:8pt; color:#444; border-left:3px solid #999; padding:4px 8px; margin:6px 0; background:#f9f9f9; page-break-inside:avoid; }
  .nota { font-size:8pt; color:#444; border-left:3px solid #999; padding:4px 8px; margin:6px 0; background:#f9f9f9; page-break-inside:avoid; }
  .badge { display:inline-block; font-size:6.5pt; background:#111; color:#fff; padding:2px 5px; border-radius:3px; letter-spacing:0.06em; }
  .firmas { display:flex; justify-content:space-between; gap:18px; margin-top:18px; page-break-inside:avoid; }
  .firma { flex:1; border:1px solid #bbb; background:#fff; padding:10px 8px 14px; text-align:center; font-size:8pt; min-height:80px; }
  h2.page-break-heading { page-break-before: auto; break-before: auto; }
  .signature-table { margin-top:10px !important; margin-bottom:10px !important; page-break-inside:avoid; background:#fff !important; }
  .signature-table td { background:#fff !important; }
  .signature-table .signature-row td { height:92px; vertical-align:bottom; padding-bottom:12px; }
  footer { margin-top:12px; border-top:1px solid #ccc; padding-top:4px; font-size:6pt; color:#777; text-align:center; }
"""

header_html = """
<header>
  <div class="logo">PITAUTECH<br><span style="font-size:7pt; font-weight:400; letter-spacing:0.06em; color:#666;">Arq. M. Sol Azcona</span></div>
  <div class="meta">Studio OS — Programa I+D</div>
</header>
<h1 style="text-align:center; font-size:13pt; margin:8px 0 2px; letter-spacing:0.04em;">CONTRATO DE PRESTACIÓN DE SERVICIOS</h1>
<p style="text-align:center; font-size:7pt; color:#555; margin-bottom:14px;">Studio OS — Programa I+D · 190 hs totales ~16 hs/sem · Vigencia 16/09–16/12/2026 (16→16) · Firma 24/09/2026</p>
"""

footer_html = ""

full_html = f"<!DOCTYPE html><html lang='es'><head><meta charset='UTF-8'><title>Contrato Studio OS — PDF fiel del .md</title><style>{css}</style></head><body>{header_html}{html_body}{footer_html}</body></html>"
html_tmp.write_text(full_html, encoding="utf-8")
print(f"HTML temporal: {{html_tmp}} {{html_tmp.stat().st_size}} bytes")

cmd = [chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw", f"--print-to-pdf={pdf_out}", str(html_tmp)]
print("CMD:", " ".join(cmd))
r = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", r.stdout[:500])
print("STDERR:", r.stderr[:1000])
print("PDF fiel:", pdf_out, "existe:", pdf_out.exists(), "bytes:", pdf_out.stat().st_size if pdf_out.exists() else 0)
# NOTA ES: verificación rápida que el HTML contiene las marcas clave del md
checks = ["ANEXO I", "Datos para transferencia", "Comunicaciones y entrega", "190 horas", "16/09/2026", "22/09/2026", "23/09/2026", "5% mensual", "20 días", "30%"]
for c in checks:
    print(c, "->", "OK" if c in html_body else "FALTA")
