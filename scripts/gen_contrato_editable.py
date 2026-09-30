#!/usr/bin/env python3
# NOTA ES: Genera PDF EDITABLE (AcroForm) del contrato — campos rellenables para datos sensibles
# No commitea datos sensibles a git (.md queda con placeholders, el PDF editable lo completás local en Acrobat/Reader/Foxit/navegador)
# Uso: python scripts/gen_contrato_editable.py
# Salida: proyectos/STUDIO_OS-Emilia/legal/contrato-studio-os-emilia_EDITABLE.pdf
import pathlib

OUT = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia_EDITABLE.pdf")

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib import colors

styles = getSampleStyleSheet()
s_title = ParagraphStyle("Title", parent=styles["Title"], fontSize=14, leading=16, alignment=TA_CENTER, textColor=HexColor("#11120f"), spaceAfter=2*mm, fontName="Helvetica-Bold")
s_sub = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=7, leading=9, alignment=TA_CENTER, textColor=HexColor("#5a5e56"), spaceAfter=4*mm, fontName="Helvetica-Oblique")
s_h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=10, leading=12, textColor=HexColor("#11120f"), fontName="Helvetica-Bold", spaceBefore=5*mm, spaceAfter=2*mm, keepWithNext=True)
s_body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=8.5, leading=11, alignment=TA_JUSTIFY, fontName="Helvetica", spaceAfter=2*mm)
s_small = ParagraphStyle("Small", parent=s_body, fontSize=7.5, leading=10, textColor=HexColor("#333333"))
s_cell = ParagraphStyle("Cell", parent=styles["Normal"], fontSize=7, leading=8, fontName="Helvetica", alignment=TA_LEFT)
s_aviso = ParagraphStyle("Aviso", parent=s_body, fontSize=6.5, leading=8, textColor=HexColor("#8a867e"), alignment=TA_JUSTIFY, fontName="Helvetica-Oblique")
s_field_label = ParagraphStyle("FieldLabel", parent=styles["Normal"], fontSize=7, leading=9, textColor=HexColor("#111"), fontName="Helvetica-Bold")
s_hint = ParagraphStyle("Hint", parent=styles["Normal"], fontSize=6.5, leading=8, textColor=HexColor("#666"), fontName="Helvetica-Oblique")

def p(txt, style=s_body):
    import re
    txt = txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    txt = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", txt)
    return Paragraph(txt, style)

story = []
story.append(p("CONTRATO DE PRESTACIÓN DE SERVICIOS — Studio OS · Emilia Pimenta", s_title))
story.append(p("Programa I+D embebido · Sistema operativo del estudio · Vigencia 16/09–16/12/2026 (16→16) · Firma 24/09/2026 · 190hs trimestrales", s_sub))
story.append(HRFlowable(width="100%", thickness=0.6, color=HexColor("#c9a98a"), spaceAfter=3*mm))
story.append(p("INSTRUCCIONES: Este PDF es <b>rellenable</b>. Completá los campos celestes a continuación en tu lector PDF (Adobe Acrobat Reader, Foxit, Chrome/Edge) y luego <b>Imprimir → Guardar como PDF</b> para aplanar. El .md del vault queda sin datos sensibles (no se commitea).", s_hint))
story.append(Spacer(1, 2*mm))

# NOTA ES: Caja editable — los campos reales se dibujan en onFirstPage via AcroForm; aquí solo dejamos etiquetas + espacio visual
# Usamos Table con celdas que dirán [rellenar en campo]
story.append(p("DATOS DE LAS PARTES — completar antes de firmar", s_h2))
# No ponemos tabla con campos acá; los campos van como AcroForm overlay (ver footer func)
story.append(p("<b>LA PRESTADORA:</b> María Sol Azcona (marca comercial Pitau-Tech) — ver campos editables abajo. <b>LA CLIENTA:</b> Emilia Pimenta / Estudio Emilia Pimenta — ver campos editables abajo. <b>Antecedentes:</b> inicio 16/09/2026, adelanto USD 300 abonado 22/09/2026, firma 24/09/2026 ratifica efectos desde 16/09.", s_body))
story.append(p("TERCERA: Vigencia 16/09/2026 al 16/12/2026 (16→16), bonificado hasta 16/12 inclusive. CUARTA: adelanto 16/09 vto 23/09 (abonado 22/09), 16/10, 16/11, 16/12 vto 23/12. QUINTA: mails y entrega por Drive. Resto de cláusulas idénticas al contrato base — ver contrato-studio-os-emilia.md para texto completo.", s_small))
story.append(Spacer(1, 3*mm))
story.append(p("— CAMPOS EDITABLES — completá y luego reimprimí este PDF —", s_hint))
story.append(Spacer(1, 1*mm))

# NOTA ES: Dejamos una tabla visual de referencia (no editable) para que se vea dónde va cada dato
ref_rows = [
    [p("<b>Campo</b>", s_cell), p("<b>Valor a completar (campo celeste arriba del texto)</b>", s_cell)],
    [p("CUIT Prestadora", s_cell), p("23-34470567-4 (ver campo)", s_cell)],
    [p("Domicilio Prestadora", s_cell), p("Bolivia [altura/CP] — CABA", s_cell)],
    [p("Mail Prestadora", s_cell), p("proyectopi.31416@gmail.com / sol@pitautech.com.ar", s_cell)],
    [p("CUIT Clienta", s_cell), p("20-08559705-2", s_cell)],
    [p("Domicilio Clienta", s_cell), p("Federico Lacroze [altura/CP]", s_cell)],
    [p("Banco / CBU / Alias", s_cell), p("[completar — datos sensibles]", s_cell)],
]
# Convertir a data para Table
from reportlab.platypus import Table as T
data = [[c for c in row] for row in ref_rows]
t = T(data, colWidths=[42*mm, 110*mm], repeatRows=1)
t.setStyle(TableStyle([
    ("GRID", (0,0), (-1,-1), 0.4, HexColor("#d9d6d0")),
    ("BACKGROUND", (0,0), (-1,0), HexColor("#111")),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 4),
    ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, HexColor("#fbfaf8")]),
]))
story.append(t)
story.append(Spacer(1, 4*mm))
story.append(p("Nota: Este PDF editable es solo para carga manual local. El original firmable sin campos queda en <i>contrato-studio-os-emilia.pdf</i>. No subas este editable con datos a git.", s_small))
story.append(Spacer(1, 6*mm))
story.append(HRFlowable(width="100%", thickness=0.4, color=HexColor("#d9d6d0"), spaceAfter=4*mm))
story.append(p("Firmas — completar fecha 24/09/2026 y firmar a mano o pegar firma PNG (ver scripts/insertar_firma_contrato.py)", s_hint))

# NOTA ES: Definición de campos AcroForm — coordenadas en mm desde esquina inferior izquierda
FIELDS = [
    # (name, x_mm, y_mm, w_mm, h_mm, default)
    ("cuit_prestadora", 28, 232, 62, 9, "23-34470567-4"),
    ("domicilio_prestadora", 28, 220, 82, 9, "Bolivia  - CABA"),
    ("mail_prestadora", 28, 208, 82, 9, "proyectopi.31416@gmail.com"),
    ("cuit_clienta", 118, 232, 62, 9, "20-08559705-2"),
    ("domicilio_clienta", 118, 220, 62, 9, "Federico Lacroze  - CABA"),
    ("mail_clienta", 118, 208, 62, 9, "arq.emiliapimentalombardi@gmail.com"),
    ("banco", 28, 185, 52, 9, ""),
    ("cbu", 84, 185, 62, 9, ""),
    ("alias", 150, 185, 30, 9, ""),
    ("tipo_cuenta", 28, 172, 52, 9, ""),
    ("titular", 84, 172, 62, 9, "Maria Sol Azcona"),
    ("cuit_titular", 150, 172, 30, 9, "23-34470567-4"),
]

FIELD_LABELS = {
    "cuit_prestadora": "CUIT Prestadora",
    "domicilio_prestadora": "Domicilio Prestadora",
    "mail_prestadora": "Mail Prestadora",
    "cuit_clienta": "CUIT Clienta",
    "domicilio_clienta": "Domicilio Clienta",
    "mail_clienta": "Mail Clienta",
    "banco": "Banco",
    "cbu": "CBU",
    "alias": "Alias",
    "tipo_cuenta": "Tipo cuenta",
    "titular": "Titular",
    "cuit_titular": "CUIT Titular",
}

def draw_fields(canvas, doc):
    canvas.saveState()
    # Fondo celeste suave para campos
    for name, x_mm, y_mm, w_mm, h_mm, default in FIELDS:
        x = x_mm * mm
        y = y_mm * mm
        w = w_mm * mm
        h = h_mm * mm
        # Etiqueta
        canvas.setFont("Helvetica-Bold", 5)
        canvas.setFillColor(HexColor("#111"))
        canvas.drawString(x, y + h + 1.5*mm, FIELD_LABELS[name])
        # Campo
        canvas.acroForm.textfield(
            name=name,
            x=x, y=y, width=w, height=h,
            borderWidth=0.6, borderColor=HexColor("#6aa6ff"),
            fillColor=HexColor("#eef4ff"),
            textColor=black,
            fontName="Helvetica", fontSize=7,
            fieldFlags="",
            value=default,
            maxlen=0,
        )
    # Título de sección sobre los campos
    canvas.setFont("Helvetica-Bold", 7)
    canvas.setFillColor(HexColor("#111"))
    canvas.drawCentredString(A4[0]/2, 252*mm, "CAMPOS EDITABLES — completá acá (queda solo local, no se commitea)")
    canvas.setFont("Helvetica-Oblique", 5)
    canvas.setFillColor(HexColor("#555"))
    canvas.drawCentredString(A4[0]/2, 248*mm, "Tip: Abrí en Acrobat Reader / Foxit / Chrome, completá los celestes, luego Imprimir -> Guardar como PDF para aplanar")
    canvas.restoreState()

def footer(canvas, doc):
    draw_fields(canvas, doc)
    canvas.saveState()
    canvas.setFont("Helvetica", 5)
    canvas.setFillColor(HexColor("#8a867e"))
    canvas.drawCentredString(A4[0]/2, 10*mm, "Studio OS · EDITABLE — completar local y reimprimir (no subir con datos a git) · Página %d" % doc.page)
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=16*mm, rightMargin=16*mm, topMargin=14*mm, bottomMargin=16*mm, title="Contrato Studio OS — EDITABLE — Emilia Pimenta", author="Pitau-Tech")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f"OK — editable: {OUT} ({OUT.stat().st_size} bytes)")
