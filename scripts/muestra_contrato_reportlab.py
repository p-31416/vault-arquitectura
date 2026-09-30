# NOTA ES: Muestra B — ReportLab puro (simula LibreOffice/OnlyOffice sin necesitar Writer instalado)
# Qué hace: genera PDF A4 con Platypus (Paragraph, Table, PageTemplate con header/footer, page-break control)
# Por qué: ReportLab ya está instalado (5.0.1) y es 100% Python; demuestra alternativa 100% programática vs HTML->PDF
# Uso: P:\Anaconda\envs\comfyenv\python.exe scripts/muestra_contrato_reportlab.py
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
import pathlib

out = pathlib.Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\temp\muestras-pdf\contrato-muestra-reportlab.pdf")

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 9)
    canvas.setFillColor(HexColor("#111111"))
    canvas.drawString(20*mm, 277*mm, "PITAUTECH")
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(HexColor("#555555"))
    canvas.drawRightString(190*mm, 277*mm, "Studio OS — Programa I+D  •  Vault + automatización + IA local")
    canvas.setStrokeColor(HexColor("#111111"))
    canvas.setLineWidth(0.6)
    canvas.line(20*mm, 275*mm, 190*mm, 275*mm)
    # footer
    canvas.setFont("Helvetica", 6)
    canvas.setFillColor(HexColor("#777777"))
    canvas.drawCentredString(105*mm, 12*mm, "Plantilla de referencia — no constituye asesoramiento legal  •  Original en /activos/documentos-legales/STUDIO_OS-Emilia/  •  Muestra B ReportLab")
    canvas.drawRightString(190*mm, 12*mm, f"Pág. {doc.page}")
    canvas.restoreState()

styles = getSampleStyleSheet()
s_title = ParagraphStyle("title", parent=styles["Heading1"], fontSize=13, leading=15, alignment=TA_CENTER, textColor=HexColor("#111111"), spaceAfter=2)
s_sub = ParagraphStyle("sub", parent=styles["Normal"], fontSize=7, leading=9, alignment=TA_CENTER, textColor=HexColor("#555555"), spaceAfter=10)
s_h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontSize=10.5, leading=13, backColor=HexColor("#f2f2f2"), borderPadding=(4,0,4,8), textColor=HexColor("#111111"), spaceBefore=10, spaceAfter=6, borderColor=HexColor("#111111"), borderWidth=0, leftIndent=0)
s_body = ParagraphStyle("body", parent=styles["Normal"], fontSize=9.5, leading=13.5, alignment=TA_JUSTIFY, spaceAfter=6, textColor=HexColor("#1a1a1a"))
s_nota = ParagraphStyle("nota", parent=styles["Normal"], fontSize=8, leading=10.5, backColor=HexColor("#f9f9f9"), borderPadding=(6,6,6,10), textColor=HexColor("#444444"), spaceAfter=6, leftIndent=0)
s_cell = ParagraphStyle("cell", parent=styles["Normal"], fontSize=8.5, leading=10.5, alignment=TA_LEFT)
s_cell_c = ParagraphStyle("cellc", parent=s_cell, alignment=TA_CENTER)
s_footer = ParagraphStyle("footer", parent=styles["Normal"], fontSize=7, leading=9, alignment=TA_CENTER, textColor=HexColor("#777777"))

doc = SimpleDocTemplate(str(out), pagesize=A4, leftMargin=22*mm, rightMargin=22*mm, topMargin=28*mm, bottomMargin=18*mm, title="Contrato Studio OS — Muestra B ReportLab", author="PitauTech")

story = []
story.append(Paragraph("CONTRATO DE PRESTACIÓN DE SERVICIOS", s_title))
story.append(Paragraph("Muestra B — ReportLab puro (simula LibreOffice sin Writer) · 190 hs totales ~16 hs/sem  ·  A4 20mm  ·  Tabla con keep-together", s_sub))
story.append(Paragraph('Se celebra el <b>lunes 21 de septiembre de 2026</b>, entre: <b>LA PRESTADORA:</b> María Sol Azcona (Pitau-Tech) — CUIT [a completar] — Domicilio CABA [a completar] — Mail [a completar] y <b>LA CLIENTA:</b> Emilia Pimenta / Estudio Emilia Pimenta — CUIT [a definir] — Domicilio [a completar] — Mail [a completar]. Las Partes iniciaron trabajos anticipados el <b>miércoles 16/09/2026</b> (revisión hardware e instalación) por acuerdo verbal, con efectos económicos desde 16/09 y jurídicos desde la firma.', s_body))
story.append(Paragraph("PRIMERA — Objeto", s_h2))
story.append(Paragraph('Programa I+D embebido Studio OS. Capacidad global <b>190 horas trimestrales totales, ~16 hs semanales promedio</b> — valor en lo producido, no locación por horas. Incluye 3 hs/sem de disponibilidad de la Clienta. Distribución 25% coordinación / 50% desarrollo / 25% entrega enseñable. <b>Anexo I cerrado</b> Mes 1; <b>Anexos II y III se completan la última semana de cada mes</b> hasta completar 190 hs. Rigen como anexos: NDA, DPA y Política. No incluye planos ejecutivos ni dirección de obra (Ley 24.335).', s_body))
story.append(Paragraph("<b>Anexo I Mes 1 OBSERVAR (~64hs):</b> S1 Vault+Fathom+Drive · S2 Casa Nayara Alvares Campos (Brasil) estándares CAD · S3 ComfyUI 1 flujo + moodboard · S4 Onboarding + roadmap. Ritmo ~16hs/sem promedio.", s_nota))
story.append(Paragraph("TERCERA — Duración", s_h2))
story.append(Paragraph('Vigencia <b>21/09/2026 al 21/12/2026</b> (mantenimiento bonificado hasta mediados dic). Inicio operativo anticipado 16/09 reconocido. Hitos Mes 1: M1 día 5 Vault+Fathom · M2 día 10 sistema visual · M3 día 15 Nayara · M4 día 20 todo enseñable + roadmap. Ritmo <b>~16hs/sem promedio (global 190hs)</b>.', s_body))
story.append(Paragraph("CUARTA — Inversión USD 1.800 (siempre fecha 16 → vencimiento 23)", s_h2))
# Tabla hitos — keepTogether
data = [
    [Paragraph("<b>Hito</b>", s_cell_c), Paragraph("<b>Concepto</b>", s_cell_c), Paragraph("<b>Fecha</b>", s_cell_c), Paragraph("<b>Vencimiento</b>", s_cell_c), Paragraph("<b>USD</b>", s_cell_c)],
    [Paragraph("H1", s_cell_c), Paragraph("Adelanto", s_cell), Paragraph("16/09/2026*", s_cell_c), Paragraph("23/09/2026", s_cell_c), Paragraph("300", s_cell_c)],
    [Paragraph("H2", s_cell_c), Paragraph("Fin Mes 1", s_cell), Paragraph("16/10/2026", s_cell_c), Paragraph("23/10/2026", s_cell_c), Paragraph("600", s_cell_c)],
    [Paragraph("H3", s_cell_c), Paragraph("Fin Mes 2", s_cell), Paragraph("16/11/2026", s_cell_c), Paragraph("23/11/2026", s_cell_c), Paragraph("600", s_cell_c)],
    [Paragraph("H4", s_cell_c), Paragraph("Saldo Mes 3", s_cell), Paragraph("16/12/2026", s_cell_c), Paragraph("23/12/2026", s_cell_c), Paragraph("300", s_cell_c)],
]
col_w = [18*mm, 42*mm, 32*mm, 32*mm, 18*mm]
t = Table(data, colWidths=col_w, repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), HexColor("#111111")),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("GRID", (0,0), (-1,-1), 0.4, HexColor("#bbbbbb")),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, HexColor("#fafafa")]),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
]))
story.append(t)
story.append(Spacer(1, 4))
story.append(Paragraph('*Factura H1 con fecha 16/09 emitida 21/09. Tipo de cambio: <b>promedio Oficial BNA vendedor + MEP vendedor vía El Cronista del día de facturación (fecha 16)</b> — fallback Ámbito/BNA. Pago por transferencia. <b>Mora 5% mensual + suspensión.</b>', s_nota))
story.append(Paragraph("Factura fecha 16 vence 23 (margen 1 semana). Vigencia jurídica desde firma 21/09; efectos económicos desde 16/09.", s_nota))
story.append(Paragraph("SÉPTIMA — Terminación", s_h2))
story.append(Paragraph('20 días de aviso por incumplimiento grave. Si la Clienta termina sin causa: prorrateo hitos vencidos + horas del hito en curso + <b>40% sobre saldo pendiente</b>.', s_body))
story.append(Paragraph("OCTAVA — Ley aplicable", s_h2))
story.append(Paragraph('República Argentina, Tribunales Ordinarios CABA. Servicio independiente, sin relación laboral. Firma escaneada simple válida.', s_body))
# Firmas
firma_data = [
    [Paragraph("María Sol Azcona — Pitau-Tech<br/>La Prestadora<br/><br/><br/>Firma: ___________________", s_cell_c),
     Paragraph("Emilia Pimenta / Estudio<br/>La Clienta<br/><br/><br/>Firma: ___________________", s_cell_c)]
]
ft = Table(firma_data, colWidths=[71*mm, 71*mm])
ft.setStyle(TableStyle([
    ("LINEABOVE", (0,0), (-1,0), 0.6, HexColor("#111111")),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
]))
story.append(Spacer(1, 12))
story.append(ft)

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("OK", out, out.stat().st_size, "bytes")
