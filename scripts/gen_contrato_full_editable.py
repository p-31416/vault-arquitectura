#!/usr/bin/env python3
# NOTA ES: Toma el contrato PDF completo (5 pgs Chrome) y le agrega campos AcroForm editables encima de los [a completar]
# Salida: contrato-studio-os-emilia_FULL_EDITABLE.pdf — abrís en Reader/Foxit/Chrome y completás celeste
import fitz  # pymupdf
from pathlib import Path

SRC = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia.pdf")
OUT = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia_FULL_EDITABLE.pdf")

# NOTA ES: coordenadas en puntos PDF (A4 595x842), origen abajo-izq
# Medidas tomadas del PDF Chrome renderizado — ajustar si queda desplazado
FIELDS = [
    # página 0 — encabezado (coords fitz bottom-left, A4 842h)
    # Ajustado a zona superior del PDF Chrome (y ~680-730)
    {"page": 0, "name": "cuit_prestadora", "rect": [125, 680, 285, 697], "value": "23-34470567-4", "label": "CUIT Prestadora"},
    {"page": 0, "name": "domicilio_prestadora", "rect": [125, 662, 285, 679], "value": "Bolivia  - CABA", "label": "Domicilio"},
    {"page": 0, "name": "mail_prestadora", "rect": [125, 644, 285, 661], "value": "proyectopi.31416@gmail.com", "label": "Mail"},
    {"page": 0, "name": "cuit_clienta", "rect": [355, 680, 515, 697], "value": "20-08559705-2", "label": "CUIT Clienta"},
    {"page": 0, "name": "domicilio_clienta", "rect": [355, 662, 515, 679], "value": "Federico Lacroze  - CABA", "label": "Domicilio"},
    # página 1 — recuadro Datos para transferencia (mitad superior, gris)
    {"page": 1, "name": "banco", "rect": [95, 465, 200, 482], "value": "", "label": "Banco"},
    {"page": 1, "name": "cbu", "rect": [215, 465, 400, 482], "value": "", "label": "CBU"},
    {"page": 1, "name": "alias", "rect": [415, 465, 520, 482], "value": "", "label": "Alias"},
    {"page": 1, "name": "tipo_cuenta", "rect": [95, 447, 200, 464], "value": "", "label": "Tipo cuenta"},
    {"page": 1, "name": "titular_cbu", "rect": [215, 447, 400, 464], "value": "Maria Sol Azcona", "label": "Titular"},
]

doc = fitz.open(SRC)
for f in FIELDS:
    page = doc[f["page"]]
    # NOTA ES: rect en fitz es [x0,y0,x1,y1] con origen abajo-izq; convertimos desde arriba: y_fitz = 842 - y_top
    # Nuestras rect ya están en coords fitz directas (estimadas abajo)
    # Ajuste: fitz usa bottom-left, así que y0 < y1
    widget = fitz.Widget()
    widget.field_name = f["name"]
    widget.field_value = f["value"]
    widget.field_type = fitz.PDF_WIDGET_TYPE_TEXT
    widget.rect = fitz.Rect(f["rect"])
    widget.field_flags = 0
    widget.text_font = "helv"
    widget.text_font_size = 7
    # Color celeste claro
    widget.fill_color = [0.93, 0.95, 1.0]
    widget.text_color = [0, 0, 0]
    widget.border_color = [0.42, 0.65, 1.0]
    widget.border_width = 0.6
    page.add_widget(widget)

doc.save(str(OUT), garbage=4, deflate=True)
doc.close()
print(f"OK FULL_EDITABLE: {OUT} ({OUT.stat().st_size} bytes) — fields {len(FIELDS)} en {len(set(f['page'] for f in FIELDS))} páginas")
# Verificación
import fitz as f2
d2 = f2.open(OUT)
print("AcroForm fields:", [w.field_name for p in d2 for w in p.widgets()] )
