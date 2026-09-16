#!/usr/bin/env python3
# NOTA ES: Genera PDF firmable A4 desde contrato-studio-os-emilia.md usando reportlab (sin dependencias GTK)
# Uso: P:\Anaconda\envs\comfyenv\python.exe -> no, usa python base: python scripts/gen_contrato_pdf.py
import re
from pathlib import Path

MD = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia.md")
OUT = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia.pdf")
# Fallback activos para firma
OUT_ACTIVOS = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\documentos-legales\STUDIO_OS-Emilia\contrato-studio-os-emilia.pdf")

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.colors import HexColor, black
from reportlab.lib import colors

# NOTA ES: Leer markdown y extraer texto limpio
text = MD.read_text(encoding="utf-8")
# Quitar frontmatter
text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)

styles = getSampleStyleSheet()
# NOTA ES: Estilos
s_title = ParagraphStyle("Title", parent=styles["Title"], fontSize=14, leading=16, alignment=TA_CENTER, textColor=HexColor("#11120f"), spaceAfter=2*mm, fontName="Helvetica-Bold")
s_sub = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=7, leading=9, alignment=TA_CENTER, textColor=HexColor("#5a5e56"), spaceAfter=4*mm, fontName="Helvetica-Oblique")
s_h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=10, leading=12, textColor=HexColor("#11120f"), fontName="Helvetica-Bold", spaceBefore=5*mm, spaceAfter=2*mm, keepWithNext=True)
s_h3 = ParagraphStyle("H3", parent=styles["Heading3"], fontSize=9, leading=11, textColor=HexColor("#11120f"), fontName="Helvetica-Bold", spaceBefore=3*mm, spaceAfter=1.5*mm)
s_body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=8.5, leading=11, alignment=TA_JUSTIFY, fontName="Helvetica", spaceAfter=2*mm)
s_small = ParagraphStyle("Small", parent=s_body, fontSize=7.5, leading=10, textColor=HexColor("#333333"))
s_cell = ParagraphStyle("Cell", parent=styles["Normal"], fontSize=7, leading=8, fontName="Helvetica", alignment=TA_LEFT)
s_cell_b = ParagraphStyle("CellB", parent=s_cell, fontName="Helvetica-Bold", textColor=black)
s_aviso = ParagraphStyle("Aviso", parent=s_body, fontSize=6.5, leading=8, textColor=HexColor("#8a867e"), borderPadding=(2,2,4), alignment=TA_JUSTIFY, fontName="Helvetica-Oblique")

def p(txt, style=s_body):
    # NOTA ES: Escapar html basico y convertir markdown bold
    txt = txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    txt = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", txt)
    txt = re.sub(r"\*(.*?)\*", r"<i>\1</i>", txt)
    return Paragraph(txt, style)

story = []

# NOTA ES: Cabecera
story.append(p("CONTRATO DE PRESTACIÓN DE SERVICIOS — Studio OS · Emilia Pimenta", s_title))
story.append(p("Programa I+D embebido · Sistema operativo del estudio · Mín. 190hs trimestrales · 16/09/2026 → 16/12/2026", s_sub))
story.append(HRFlowable(width="100%", thickness=0.6, color=HexColor("#c9a98a"), spaceAfter=3*mm))
story.append(p("AVISO LEGAL IMPORTANTE: Esta es una plantilla de referencia adaptada y no constituye asesoramiento legal. Se recomienda que un abogado de su jurisdicción local revise este contrato antes de su uso.", s_aviso))
story.append(Spacer(1, 2*mm))

# NOTA ES: Partes
story.append(p("<b>Fecha de firma:</b> Miércoles 16 de septiembre de 2026", s_body))
story.append(p("<b>LA PRESTADORA:</b> María Sol Azcona (marca comercial Pitau-Tech) — CUIT [a completar] — Domicilio CABA [a completar] — Mail [a completar] (en adelante, la “Prestadora”)", s_body))
story.append(p("<b>LA CLIENTA:</b> Emilia Pimenta / Estudio Emilia Pimenta — CUIT [a definir con la Clienta] — Domicilio [a completar] — Mail [a completar] (en adelante, la “Clienta”)", s_body))
story.append(p("(La Prestadora y la Clienta se denominarán conjuntamente como las “Partes” e individualmente como la “Parte”).", s_small))
story.append(Spacer(1, 1*mm))

story.append(p("ANTECEDENTES", s_h2))
story.append(p("Que la Prestadora es autónoma con experiencia en el diseño e implementación de ecosistemas operativos para estudios de arquitectura (Vault, automatización, IA local). Que la Clienta desea contratar los servicios de la Prestadora para el desarrollo del sistema operativo del estudio, cuyas características se detallan en el presente Contrato y sus Anexos. Que ambas Partes, reconociéndose mutuamente la capacidad legal necesaria para ello, acuerdan celebrar el presente Contrato, el cual se regirá por las siguientes:", s_body))

# NOTA ES: Helper para tabla de hitos
def build_table(rows, col_widths, header=True):
    data = []
    for i, row in enumerate(rows):
        cells = [Paragraph(c, s_cell_b if (header and i==0) else s_cell) for c in row]
        data.append(cells)
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#d9d6d0")),
        ("BACKGROUND", (0,0), (-1,0), HexColor("#f6f4ef")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, HexColor("#fbfaf8")]),
    ]
    t.setStyle(TableStyle(style))
    return t

clausulas = [
    ("PRIMERA: OBJETO DEL CONTRATO", [
        "El objeto de este Contrato es la prestación de servicios por parte de la Prestadora para el diseño, desarrollo e implementación del sistema operativo del estudio (en adelante, el “Programa”), bajo modalidad de Investigación y Desarrollo embebido.",
        "El Programa se ejecuta mediante proyectos definidos con la Clienta, con investigación, lineamientos, entregas semanales y reuniones, a razón de ~16 horas semanales, de las cuales la Clienta dispone de 3 horas semanales para reuniones y validaciones. La distribución orientativa es: 25% coordinación y planificación semanal con la Clienta, 50% desarrollo e investigación, y 25% implementación y entrega enseñable para que la Clienta pueda operar con autonomía. El total mínimo trimestral es de 190 horas, con valor en lo producido — no es locación por horas.",
        "Las características y alcance del Mes 1 se definen en el Anexo I que forma parte integrante de este Contrato. Los Meses 2 y 3 se definirán en los Anexos II y III respectivamente, a coordinar con la Clienta, por el equivalente de horas hasta completar el mínimo trimestral.",
        "Queda expresamente aclarado que el objeto no comprende dibujo de planos, documentación ejecutiva, cómputos, presupuestos de obra, dirección de obra ni firma de documentación como instrumento legal. Solo lo detallado en los Anexos.",
    ]),
    ("SEGUNDA: ALCANCE DE LOS SERVICIOS Y ENTREGABLES", [
        "Los servicios a prestar por la Prestadora incluyen: (a) Investigación y desarrollo del sistema operativo del estudio mediante proyectos definidos con la Clienta. (b) Investigación, lineamientos, entregas semanales y reuniones de validación. (c) Desarrollo y configuración del Vault compartido, estándares CAD y flujos iniciales (ver Anexo I). (d) Capacitación y entrega enseñable para operación autónoma del equipo de la Clienta.",
        "Exclusiones: Quedan expresamente excluidos del alcance de este Contrato los siguientes puntos, salvo acuerdo escrito en contrario: Costos de licencias de software de terceros (ej. WhatsApp Business API, CRM, etc.). Costos de consumo de APIs externas (ej. OpenAI, Google Cloud, etc.). Desarrollos o funcionalidades no contemplados en los Anexos.",
        "Cualquier solicitud de trabajo adicional o fuera del alcance definido será considerada un “Cambio de Alcance” y requerirá una cotización y acuerdo por separado.",
    ]),
    ("TERCERA: DURACIÓN Y CRONOGRAMA", [
        "La duración del Programa es de 3 meses, comenzando el 16/09/2026 y finalizando el 16/12/2026 (mantenimiento bonificado hasta mediados de diciembre incluido). El cronograma detallado del Mes 1 se encuentra en el Anexo I. Los cronogramas de los Meses 2 y 3 se detallarán en los Anexos II y III respectivamente, a firmar por el equivalente de horas a coordinar con la Clienta. Hitos Mes 1: M1 día 5 Vault + Fathom · M2 día 10 sistema visual validado · M3 día 15 Nayara con estándares · M4 día 20 todo enseñable + roadmap. Ritmo: ~16hs semanales (mínimo 190hs trimestrales). Cualquier retraso no imputable a la Prestadora, como la falta de feedback o entrega de información por parte de la Clienta, podrá resultar en una extensión equivalente del cronograma.",
    ]),
    ("CUARTA: INVERSIÓN Y CONDICIONES DE PAGO", None), # tabla especial
    ("QUINTA: OBLIGACIONES DE LAS PARTES", [
        "<b>Obligaciones de la Prestadora:</b> Realizar los servicios con la diligencia y profesionalismo debidos. Cumplir con el cronograma acordado, salvo causas de fuerza mayor o retrasos imputables a la Clienta. Mantener una comunicación fluida y reportar el avance del Programa.",
        "<b>Obligaciones de la Clienta:</b> Proporcionar a la Prestadora toda la información, accesos y recursos necesarios para la correcta ejecución del Programa en los plazos solicitados. Designar un único punto de contacto o responsable para la toma de decisiones y validaciones. Realizar los pagos en las fechas y formas acordadas.",
    ]),
    ("SEXTA: GARANTÍA", [
        "La Prestadora ofrece una Garantía de Soporte Post-Producción de 30 días naturales a partir de la fecha de entrega final del Programa. Durante este período, la Prestadora se compromete a corregir, sin costo adicional, cualquier error o bug directamente atribuible a la implementación realizada. Esta garantía no cubre nuevos desarrollos o cambios de alcance.",
    ]),
    ("SÉPTIMA: TERMINACIÓN DEL CONTRATO", [
        "Cualquiera de las Partes podrá dar por terminado el presente Contrato mediante notificación escrita con 20 días de antelación en caso de incumplimiento grave de las obligaciones de la otra Parte.",
        "En caso de terminación anticipada por parte de la Clienta sin causa justificada, la Clienta deberá abonar a la Prestadora el trabajo realizado hasta la fecha de terminación —prorrateado sobre hitos vencidos y horas ejecutadas del hito en curso—, además de una penalización del 40% sobre el saldo pendiente de pago al momento de la terminación. Los importes ya abonados se imputarán a cuenta de dicha liquidación, debiendo la Clienta abonar únicamente el saldo remanente si lo hubiera, o la Prestadora reintegrar el excedente si los pagos superaran lo devengado más la penalización.",
    ]),
    ("OCTAVA: LEY APLICABLE Y JURISDICCIÓN", [
        "Este Contrato se regirá e interpretará de acuerdo con las leyes de la República Argentina. Para cualquier controversia que pudiera surgir en relación con este Contrato, las Partes se someten a la jurisdicción de los Tribunales Ordinarios de la Ciudad Autónoma de Buenos Aires (CABA).",
        "Y en prueba de conformidad, las Partes firman el presente Contrato por duplicado en el lugar y fecha indicados al inicio.",
    ]),
]

for title, paras in clausulas:
    story.append(p(title, s_h2))
    if title.startswith("CUARTA"):
        story.append(p("La inversión total por los servicios objeto de este Contrato asciende a la cantidad de <b>DÓLARES ESTADOUNIDENSES MIL OCHOCIENTOS (USD 1.800)</b>.", s_body))
        story.append(p("Las condiciones de pago serán las siguientes:", s_body))
        rows = [
            ["Hito", "Importe", "Vencimiento", "Concepto"],
            ["Hito 1 (Adelanto)", "USD 300", "16/09/2026", "A la firma del Contrato"],
            ["Hito 2 (Fin Mes 1)", "USD 600", "16/10/2026", "Cierre S4 + clase"],
            ["Hito 3 (Fin Mes 2)", "USD 600", "16/11/2026", "Cierre Mes 2"],
            ["Hito 4 (Saldo final)", "USD 300", "16/12/2026", "Entrega final Mes 3"],
        ]
        w = 152*mm
        story.append(build_table(rows, [32*mm, 22*mm, 24*mm, 74*mm]))
        story.append(Spacer(1, 2*mm))
        story.append(p("Las partes acuerdan que los pagos se realizarán exclusivamente en pesos argentinos de curso legal, calculados al tipo de cambio que resulte del promedio simple entre las siguientes cotizaciones correspondientes al mercado local: El tipo de cambio vendedor del Dólar Oficial billete (Banco de la Nación Argentina). El tipo de cambio del Dólar MEP (Mercado Electrónico de Pagos) en su punta vendedora, resultante de la liquidación de títulos públicos nacionales. A los fines del cálculo aritmético del promedio, ambos valores se tomarán de manera estricta de la cotización de cierre informada en la sección de Mercados del portal El Cronista Comercial (www.cronista.com) correspondiente al último día hábil anterior a la fecha de efectivo pago. Para el caso excepcional en que el portal principal mencionado no se encontrara disponible, presente fallas técnicas o discontinuara la publicación de dichos valores al momento del cálculo, se tomará como fuentes supletorias y en el siguiente orden de prioridad: en primer lugar, el portal financiero Ámbito Financiero (ambito.com) y, en segundo lugar, la cotización vendedora informada directamente por el Banco de la Nación Argentina (bna.com.ar) para el tramo oficial.", s_small))
        story.append(p("El pago se realizará mediante transferencia bancaria a la cuenta indicada por la Prestadora. La falta de pago en los plazos acordados generará un interés por mora del 5% mensual y facultará a la Prestadora a suspender los servicios hasta la regularización del pago.", s_body))
        story.append(p("Nota: La factura se emitirá al vencimiento aunque el pago no se acredite en el acto — el adelanto faculta a iniciar Vault/Drive y el servicio podrá pausarse hasta regularizar.", s_small))
    else:
        for para in paras:
            story.append(p(para, s_body))

# NOTA ES: Anexo I tabla
story.append(p("ANEXO I — MES 1 OBSERVAR (~64hs) — Alcance cerrado", s_h2))
rows_anexo = [
    ["Semana", "Foco", "Entregable verificable"],
    ["S1", "Vault compartido + Fathom + Drive dedicado", "Vault operativo + 1 reunión transcripta"],
    ["S2", "Casa en construcción + estándares CAD", "Estandarización sobre Casa Nayara (Brasil)"],
    ["S3", "ComfyUI 1 flujo + Vault visual", "1 flujo mínimo + moodboard curado"],
    ["S4", "Onboarding + rituales + Roadmap + demo", "Clase 2hs + roadmap Mes 2-3 + retro"],
]
story.append(build_table(rows_anexo, [18*mm, 54*mm, 80*mm]))
story.append(p("1 reunión semanal + 2 presenciales al mes a coordinar con la Clienta. Anexos II (Mes 2) y III (Mes 3) se firmarán por el equivalente de horas hasta completar el mínimo de 190 horas trimestrales.", s_small))
story.append(Spacer(1, 4*mm))

# NOTA ES: Firmas
story.append(HRFlowable(width="100%", thickness=0.4, color=HexColor("#d9d6d0"), spaceAfter=4*mm))
firmas = [
    [Paragraph("<b>María Sol Azcona (Pitau-Tech)</b><br/>(La Prestadora)<br/><br/><br/>Firma: _________________________<br/>Aclaración:<br/>CUIT: [a completar]<br/>Fecha: 16/09/2026", s_cell), Paragraph("<b>Emilia Pimenta / Estudio Emilia Pimenta</b><br/>(La Clienta)<br/><br/><br/>Firma: _________________________<br/>Aclaración:<br/>CUIT: [a definir]<br/>Fecha: 16/09/2026", s_cell)],
]
t_firmas = Table(firmas, colWidths=[76*mm, 76*mm])
t_firmas.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6)]))
story.append(t_firmas)
story.append(Spacer(1, 4*mm))
story.append(p("Original firmado por duplicado. Ejemplar Prestadora / Ejemplar Clienta. Guardar PDF firmado en <i>/activos/documentos-legales/STUDIO_OS-Emilia/</i> (fuera de git).", s_small))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 6)
    canvas.setFillColor(HexColor("#8a867e"))
    canvas.drawCentredString(A4[0]/2, 10*mm, "Studio OS · Programa I+D 90 días · Mín. 190hs · Confidencial · Vault Pitautech  |  Página %d" % doc.page)
    canvas.drawCentredString(A4[0]/2, 7*mm, "María Sol Azcona (Pitau-Tech)  ·  Emilia Pimenta / Estudio  ·  16/09/2026")
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=16*mm, rightMargin=16*mm, topMargin=14*mm, bottomMargin=16*mm, title="Contrato Studio OS - Emilia Pimenta - 16-09-2026", author="María Sol Azcona - Pitau-Tech")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
# NOTA ES: Copia a activos si existe carpeta
OUT_ACTIVOS.parent.mkdir(parents=True, exist_ok=True)
try:
    import shutil; shutil.copy2(OUT, OUT_ACTIVOS)
    print(f"PDF generado: {OUT} y copia en {OUT_ACTIVOS}")
except Exception as e:
    print(f"PDF generado: {OUT} (sin copia activos: {e})")
print("OK")
