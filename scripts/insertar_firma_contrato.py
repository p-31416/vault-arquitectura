#!/usr/bin/env python3
# NOTA ES: Inserta firma escaneada (PNG/JPG transparente) en el PDF del contrato
# Uso:
#   python scripts/insertar_firma_contrato.py --firma activos/firmas/sol_firma.png --salida proyectos/STUDIO_OS-Emilia/legal/contrato-studio-os-emilia_firmado-sol.pdf
# Requiere: pip install pypdf reportlab pillow
import argparse, pathlib, io
from pathlib import Path

CONTRATO_PDF = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia.pdf")

def crear_overlay(firma_path, page_w, page_h, x_mm=18, y_mm=42, w_mm=48):
    """NOTA ES: crea un PDF de 1 pág con solo la imagen de firma"""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader
    from PIL import Image
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    # NOTA ES: calcular alto proporcional
    im = Image.open(firma_path)
    iw, ih = im.size
    aspect = ih / iw
    w = w_mm * mm
    h = w * aspect
    x = x_mm * mm
    # NOTA ES: y desde abajo; A4 alto 297mm
    y = y_mm * mm
    # NOTA ES: fondo transparente se respeta si PNG tiene alpha
    c.drawImage(ImageReader(str(firma_path)), x, y, width=w, height=h, mask='auto', preserveAspectRatio=True)
    c.save()
    buf.seek(0)
    return buf

def insertar(firma_path, salida, pagina=-1):
    # NOTA ES: pagina -1 = última página (donde están las firmas)
    from pypdf import PdfReader, PdfWriter
    from reportlab.lib.pagesizes import A4
    reader = PdfReader(str(CONTRATO_PDF))
    writer = PdfWriter()
    n = len(reader.pages)
    target_idx = n + pagina if pagina < 0 else pagina
    overlay_buf = crear_overlay(firma_path, A4[0], A4[1])
    overlay_reader = PdfReader(overlay_buf)
    overlay_page = overlay_reader.pages[0]
    for i, page in enumerate(reader.pages):
        if i == target_idx:
            # NOTA ES: merge overlay encima
            page.merge_page(overlay_page)
        writer.add_page(page)
    # NOTA ES: copiar metadata
    writer.add_metadata(reader.metadata or {})
    Path(salida).parent.mkdir(parents=True, exist_ok=True)
    with open(salida, "wb") as f:
        writer.write(f)
    print(f"OK — PDF con firma: {salida} ({Path(salida).stat().st_size} bytes) — página {target_idx+1}/{n}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Pega firma escaneada en contrato PDF (última página, bloque Prestadora)")
    ap.add_argument("--firma", required=True, help="Ruta a firma PNG/JPG (ej: activos/firmas/sol_firma.png)")
    ap.add_argument("--salida", required=False, default=str(Path(r"P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\STUDIO_OS-Emilia\legal\contrato-studio-os-emilia_firmado-sol.pdf")), help="Ruta salida PDF firmado")
    ap.add_argument("--pagina", type=int, default=-1, help="Índice página (0-based, -1 última)")
    args = ap.parse_args()
    insertar(Path(args.firma), Path(args.salida), args.pagina)
