#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NOTA ES: este script LEE los PDFs de la bibliografia y escribe METADATOS + TRANSCRIPCION en el vault.
# NOTA ES: nunca modifica el PDF de origen (solo lectura) y nunca copia el binario a git.
# NOTA ES: uso -> P:\Anaconda\envs\comfyenv\python.exe scripts/pdf_scan_bibliografia.py --src "RUTA.pdf"
# NOTA ES: lote  -> ... --dir "CARPETA" --all
# NOTA ES: v2 (2026-10-20) - cambios frente a v1:
# NOTA ES:   1) el texto se extrae con GHOSTSCRIPT (txtwrite) pagina por pagina, no con pypdf:
# NOTA ES:      pypdf rompe los acentos (fonts Type1 sin fontTools) y no abre PDFs cifrados con AES.
# NOTA ES:   2) NO se extraen imagenes (decision B): la ficha lista las figuras con su pagina.
# NOTA ES:   3) la transcripcion completa se escribe en raw/pdf/<slug>-transcripcion.md (decision A).
# NOTA ES:   4) OCR opcional con tesseract para los PDF escaneados (sin capa de texto).

# NOTA ES: importamos librerias estandar + pypdf (que vive en el dir temporal, ver notas).
import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from datetime import datetime

# NOTA ES: forzamos UTF-8 en stdout para que los acentos no se rompan en la consola de Windows.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# NOTA ES: logging de pypdf esta en CRITICAL porque sus avisos de fuentes ensucian la salida.
import logging
logging.disable(logging.CRITICAL)

# NOTA ES: si las librerias no estan en el path del sistema, las buscamos en el dir temporal del usuario.
LIB_DIRS = [
    r"C:\Users\Solch16\AppData\Local\Temp\opencode\pdflibs",
    os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp", "opencode", "pdflibs"),
]
for _d in LIB_DIRS:
    # NOTA ES: agregamos el dir al sys.path SOLO si existe (no instalamos nada).
    if os.path.isdir(_d) and _d not in sys.path:
        sys.path.append(_d)

try:
    from pypdf import PdfReader
except ImportError:
    # NOTA ES: si falta pypdf, avisamos con el comando exacto para arreglarlo.
    print("FALTA pypdf. Proba: pip install --target " + LIB_DIRS[0] + " pypdf")
    raise


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

# NOTA ES: quitamos acentos para que los slugs y nombres de archivo sean portables.
def slugify(texto):
    # NOTA ES: normalizamos a NFD y filtramos los diacriticos combinantes.
    normal = unicodedata.normalize("NFD", texto)
    ascii_txt = "".join(c for c in normal if not unicodedata.combining(c))
    # NOTA ES: cualquier cosa que no sea letra o numero pasa a "_".
    ascii_txt = re.sub(r"[^A-Za-z0-9]+", "_", ascii_txt).strip("_").lower()
    # NOTA ES: evitamos slugs vacios o demasiado largos.
    ascii_txt = re.sub(r"_{2,}", "_", ascii_txt)
    return (ascii_txt or "pdf")[:60]


# NOTA ES: artefactos de edicion que aparecen como /Title en PDF exportados desde Word/InDesign.
TITULO_ARTEFACTO_RE = re.compile(
    r"^(microsoft\s+(word|powerpoint|excel|visio|works)|title of paper\b|untitled\b|"
    r"chapter[_\s]|.*\.(docx?|indd|pptx?|xlsx?)\s*$)",
    re.IGNORECASE)


# NOTA ES: un titulo sin espacios y con guion bajo ("LearningXDesign_post-review_CE_AS")
# es un nombre de archivo, no un titulo de documento.
def es_titulo_archivo(t):
    t = (t or "").strip()
    return bool(t) and " " not in t and "_" in t


# NOTA ES: prettificar convierte un slug en un titulo legible ("gaudi_and_cad" -> "Gaudi and cad").
def prettificar(slug):
    txt = slug.replace("_", " ").strip()
    return txt[:1].upper() + txt[1:] if txt else txt


# NOTA ES: titulo real del documento: metadata del PDF, salvo que sea un artefacto de edicion.
def titulo_de_documento(meta, nombre_archivo, slug):
    t = meta.get("/Title") or meta.get("Title") or ""
    # NOTA ES: "Chapter_00.indd", "Microsoft Word - X.doc", "Title of paper"... no son titulos.
    if not t or TITULO_ARTEFACTO_RE.search(t.strip()) or es_titulo_archivo(t):
        # NOTA ES: en ese caso usamos el nombre real del archivo, limpio.
        t = re.sub(r"\s+", " ", os.path.splitext(nombre_archivo)[0]).strip()
        return (t or prettificar(slug)), True
    return t, False


# NOTA ES: detectamos el idioma por palabras funcionales (heuristica simple, no un detector serio).
STOPWORDS = {
    "es": {"de", "la", "el", "los", "las", "que", "una", "con", "por", "para", "arquitectura", "es", "del"},
    "en": {"the", "of", "and", "to", "in", "for", "with", "is", "architecture", "gaudi", "that", "this"},
    "it": {"di", "che", "il", "per", "con", "una", "della", "architettura", "gaudi", "non", "sono"},
    "ca": {"de", "la", "el", "els", "les", "que", "una", "amb", "per", "arquitectura", "gaudi", "dels"},
}


def detectar_idioma(texto):
    # NOTA ES: tomamos una muestra de las primeras 40.000 caracteres para no recorrer todo.
    palabras = re.findall(r"[A-Za-zÀ-ÿ']+", texto[:40000].lower())
    # NOTA ES: contamos aciertos por idioma.
    puntajes = {lang: sum(1 for p in palabras if p in ws) for lang, ws in STOPWORDS.items()}
    # NOTA ES: gana el idioma con mas coincidencias; si nadie llega a 10, queda "desconocido".
    mejor = max(puntajes, key=puntajes.get)
    return mejor if puntajes[mejor] >= 10 else "desconocido"


# NOTA ES: busqueda de DOI/ISBN dentro del texto: son candidatos que @sherlock verifica por fuera.
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b")
ISBN_RE = re.compile(r"\b(?:ISBN(?:-1[03])?\s*[:]?\s*)?(?:97[89][-\s]?)?(?:\d[-\s]?){9}[\dXx]\b")

# NOTA ES: patrones de pie de figura: "Fig. 3", "Figure 12", "Figura 4", "PLATE 2", "Lám. 5".
FIG_RE = re.compile(
    r"^\s*(?:FIGURE|FIGURES|FIG|FIGURA|FIGURAS|IMAGEN|IMAGE|PLATE|LÁMINA|LAMINA|LÁM|LAM)"
    r"\s*\.?\s*[.:\-]?\s*(\d{1,3})\b(.{0,90})", re.MULTILINE | re.IGNORECASE)


# ---------------------------------------------------------------------------
# Ghostscript: extractor de texto y OCR
# ---------------------------------------------------------------------------

def buscar_gs():
    # NOTA ES: gswin64c es Ghostscript en Windows; lo buscamos en el PATH o en las rutas comunes.
    for cand in ["gswin64c", "gswin64c.exe", "gs"]:
        # NOTA ES: shutil.which busca el ejecutable en el PATH.
        ruta = shutil.which(cand)
        if ruta:
            return ruta
    for cand in [r"C:\Program Files\gs\gs10.08.0\bin\gswin64c.exe",
                 r"C:\Users\Solch16\scoop\shims\gswin64c.exe"]:
        # NOTA ES: fallback a rutas de instalacion conocidas.
        if os.path.isfile(cand):
            return cand
    return None


GS = buscar_gs()


def gs_texto_pagina(ruta, pagina):
    # NOTA ES: gs con -dFirstPage/-dLastPage extrae UNA pagina, para conservar la paginacion.
    cmd = [GS, "-q", "-dNOPAUSE", "-dBATCH", "-dSAFER",
           "-dFirstPage=%d" % pagina, "-dLastPage=%d" % pagina,
           "-sDEVICE=txtwrite", "-sOutputFile=-", ruta]
    # NOTA ES: subprocess.run ejecuta el comando y captura stdout en bytes.
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=120)
    except Exception:
        return ""
    # NOTA ES: txtwrite emite UTF-8; los caracteres raros se reemplazan en vez de romper.
    return res.stdout.decode("utf-8", errors="replace")


def gs_num_paginas(ruta):
    # NOTA ES: truco de Ghostscript: abrimos el PDF sin render y pedimos el conteo de paginas.
    cmd = [GS, "-q", "-dNODISPLAY", "-dNOSAFER", "-c",
           "(%s) (r) file runpdfbegin pdfpagecount = quit" % ruta.replace("\\", "/")]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=60)
        # NOTA ES: gs devuelve el numero como numero entero en stdout.
        return int(res.stdout.decode("utf-8", errors="ignore").strip().splitlines()[-1])
    except Exception:
        return 0


def gs_ocr_pagina(ruta, pagina, tmpdir, dpi=200, lang="eng"):
    # NOTA ES: renderizamos la pagina a PNG y se la pasamos a tesseract (OCR).
    png = os.path.join(tmpdir, "pg%04d.png" % pagina)
    cmd = [GS, "-q", "-dNOPAUSE", "-dBATCH", "-dSAFER",
           "-dFirstPage=%d" % pagina, "-dLastPage=%d" % pagina,
           "-sDEVICE=png16m", "-r%d" % dpi, "-sOutputFile=%s" % png, ruta]
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    except Exception:
        return ""
    if not os.path.isfile(png):
        return ""
    # NOTA ES: tesseract escribe el texto en stdout cuando le damos la salida con "stdout".
    try:
        res = subprocess.run(["tesseract", png, "stdout", "-l", lang],
                             stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=300)
        texto = res.stdout.decode("utf-8", errors="replace")
    except Exception:
        texto = ""
    # NOTA ES: borramos el PNG temporal (no queremos 200 MB de basura en disco).
    try:
        os.remove(png)
    except Exception:
        pass
    return texto


# ---------------------------------------------------------------------------
# pypdf: metadata, outline, cifras de control
# ---------------------------------------------------------------------------

def leer_outline(reader):
    # NOTA ES: el outline (marcadores) es una jerarquia; la aplanamos a una lista simple.
    marcadores = []
    try:
        outline = reader.outline
    except Exception:
        return marcadores

    def _recorrer(items, nivel):
        # NOTA ES: walk recursivo: cada item es un destino o una lista de hijos.
        for item in items:
            if isinstance(item, list):
                _recorrer(item, nivel + 1)
            else:
                try:
                    # NOTA ES: get_destination_page_number devuelve la pagina (0-based) del destino.
                    pagina = reader.get_destination_page_number(item) + 1
                    titulo = getattr(item, "title", str(item))
                    marcadores.append((nivel, str(titulo), pagina))
                except Exception:
                    continue

    _recorrer(outline, 0)
    return marcadores


def leer_meta_pypdf(ruta):
    # NOTA ES: metadata + outline. Si el PDF esta cifrado con AES, pypdf puede fallar: no es fatal.
    meta = {}
    marcadores = []
    paginas = 0
    try:
        reader = PdfReader(ruta)
        if reader.is_encrypted:
            # NOTA ES: probamos la contrasena vacia (algunos PDFs solo restringen la lectura).
            try:
                reader.decrypt("")
            except Exception:
                pass
        try:
            meta = {str(k): str(v) for k, v in (reader.metadata or {}).items()}
        except Exception:
            meta = {}
        try:
            paginas = len(reader.pages)
        except Exception:
            paginas = 0
        marcadores = leer_outline(reader)
    except Exception as e:
        print("   [warn] pypdf no pudo leer %s: %s" % (os.path.basename(ruta), type(e).__name__))
    return meta, marcadores, paginas


# ---------------------------------------------------------------------------
# Escaneo de un PDF
# ---------------------------------------------------------------------------

def escanear_pdf(ruta, ocr=False, ocr_lang="eng", progreso=True):
    # NOTA ES: 1) metadata y outline con pypdf.
    meta, marcadores, paginas_pypdf = leer_meta_pypdf(ruta)
    # NOTA ES: 2) numero de paginas: preferimos pypdf; si falla (AES), lo pide Ghostscript.
    paginas = paginas_pypdf or gs_num_paginas(ruta)
    if not paginas:
        return None

    # NOTA ES: 3) texto pagina por pagina con Ghostscript (acentos correctos).
    textos = []
    con_texto = 0
    for i in range(1, paginas + 1):
        t = gs_texto_pagina(ruta, i)
        if len(t.strip()) >= 50:
            con_texto += 1
        textos.append(t)
        if progreso and i % 25 == 0:
            print("   ... pág %d/%d" % (i, paginas))

    # NOTA ES: 4) si el PDF es un escaneo (sin texto), pasamos OCR a las paginas vacias.
    modo = "ghostscript-txtwrite"
    if paginas and con_texto / paginas < 0.4:
        modo = "ocr-tesseract"
        print("   [ocr] escaneo detectado (%d/%d con texto): OCR de %d págs" % (con_texto, paginas, paginas))
        with tempfile.TemporaryDirectory() as tmp:
            for i in range(paginas):
                if len(textos[i].strip()) < 50:
                    textos[i] = gs_ocr_pagina(ruta, i + 1, tmp, lang=ocr_lang)
                    print("   ... ocr pág %d/%d" % (i + 1, paginas))

    texto = "\n".join(textos)
    palabras = len(re.findall(r"\S+", texto))
    caracteres = len(texto)

    # NOTA ES: 5) figuras: las buscamos en el texto y guardamos pagina + rotulo.
    figuras = []
    for i, t in enumerate(textos, start=1):
        for m in FIG_RE.finditer(t):
            rotulo = re.sub(r"\s+", " ", m.group(0)).strip()
            # NOTA ES: evitamos duplicados de la misma figura en la misma pagina.
            if not any(f["pagina"] == i and f["rotulo"] == rotulo for f in figuras):
                figuras.append({"pagina": i, "rotulo": rotulo})

    return {
        "paginas": paginas,
        "paginas_con_texto": con_texto,
        "palabras": palabras,
        "caracteres": caracteres,
        "texto": texto,
        "textos": textos,
        "meta": meta,
        "marcadores": marcadores,
        "figuras": figuras,
        "modo": modo,
    }


# ---------------------------------------------------------------------------
# Escritura de ficha + transcripcion
# ---------------------------------------------------------------------------

def escribir_transcripcion(destino, datos, meta_archivo, slug, ruta_rel_bin, ruta_original, titulo, idioma):
    # NOTA ES: la transcripcion completa va a raw/pdf/ (decision A: versionada en git).
    hoy = datetime.now().strftime("%Y-%m-%d")
    lineas = []
    lineas.append("---")
    lineas.append("tipo: transcripcion")
    lineas.append(f"fecha: {hoy}")
    lineas.append(f"fuente_binaria: {ruta_rel_bin}")
    lineas.append(f"fuente_original: {ruta_original}")
    lineas.append(f"titulo: {titulo}")
    lineas.append(f"autor: {meta_archivo.get('autor') or ''}")
    lineas.append(f"idioma: {idioma}")
    lineas.append(f"paginas: {datos['paginas']}")
    lineas.append(f"palabras: {datos['palabras']}")
    lineas.append(f"metodo_extraccion: {datos['modo']}")
    lineas.append('aviso: "Texto con copyright - uso interno del estudio. Citar con atribucion; no redistribuir."')
    lineas.append(f"tags: [pdf, raw, transcripcion, gaudi, bibliografia-ai, fair-use]")
    lineas.append("---")
    lineas.append("")
    lineas.append(f"# Transcripción — {titulo}")
    lineas.append("")
    lineas.append(f"> Texto extraído para análisis interno del estudio. Origen (solo lectura): `{ruta_original}`. "
                  f"Binario local: [{ruta_rel_bin}].")
    lineas.append(f"> Extracción: {datos['modo']} · {datos['paginas']} págs · {datos['palabras']} palabras. "
                  f"Copyright del original: se cita con atribución, no se redistribuye.")
    lineas.append("")
    for i, t in enumerate(datos["textos"], start=1):
        lineas.append(f"## [p. {i}]")
        lineas.append("")
        lineas.append(t.strip() if t.strip() else "_(página sin capa de texto)_")
        lineas.append("")
    destino.write_text("\n".join(lineas), encoding="utf-8")


def construir_ficha(datos, meta_archivo, slug, ruta_rel_bin, ruta_original, slug_ficha, slug_transcripcion, nombre_archivo):
    # NOTA ES: los metadatos del PDF mandan; si faltan, usamos el nombre del archivo.
    meta = datos["meta"]
    # NOTA ES: titulo real del documento (los artefactos de edicion se descartan).
    titulo, provisional = titulo_de_documento(meta, nombre_archivo, slug)
    autor = meta.get("/Author") or meta.get("Author") or ""
    productor = meta.get("/Producer") or ""
    creador = meta.get("/Creator") or ""
    fecha_pdf = meta.get("/CreationDate") or meta.get("/ModDate") or ""
    idioma = meta.get("/Language") or datos["idioma"]

    # NOTA ES: cobertura = paginas con capa de texto / paginas totales.
    cobertura = (datos["paginas_con_texto"] / datos["paginas"] * 100) if datos["paginas"] else 0
    # NOTA ES: si la cobertura es bajisima, el PDF es un escaneo (se marca el metodo OCR).
    escaneado = datos["modo"].startswith("ocr")

    hoy = datetime.now().strftime("%Y-%m-%d")
    L = []
    L.append("---")
    L.append("tipo: raw")
    L.append(f"fecha: {hoy}")
    L.append(f"fuente_binaria: {ruta_rel_bin}")
    L.append(f"fuente_original: {ruta_original}")
    L.append(f"titulo: {titulo}")
    L.append(f"autor: {autor}")
    L.append(f"idioma: {idioma}")
    L.append(f"paginas: {datos['paginas']}")
    L.append(f"palabras: {datos['palabras']}")
    L.append(f"metodo_extraccion: {datos['modo']}")
    L.append(f"tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]")
    L.append("licencia_texto_completo: no (copyright, solo extractos breves)")
    L.append(f"estado: {'requiere-ocr' if escaneado else 'texto-extraible'}")
    L.append("---")
    L.append("")
    L.append(f"# RAW ficha — {titulo}")
    L.append("")
    L.append(f"> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. "
             f"Binario local: [{ruta_rel_bin}]. Origen (solo lectura): `{ruta_original}`.")
    L.append(f"> El PDF de origen **no se modifica**. Texto completo: [[{slug_transcripcion}|transcripción completa]] "
             f"(raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).")
    L.append("")
    L.append("## Metadata extraída")
    L.append("")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    L.append(f"| Título | {titulo} |")
    L.append(f"| Autor | {autor or '— (lo resuelve @sherlock por fuera)'} |")
    L.append(f"| Creator / Producer | {creador or '—'} / {productor or '—'} |")
    L.append(f"| CreationDate / ModDate | {fecha_pdf or '—'} |")
    L.append(f"| Páginas | {datos['paginas']} |")
    L.append(f"| Palabras (texto extraíble) | {datos['palabras']} |")
    L.append(f"| Caracteres | ~{datos['caracteres']} |")
    L.append(f"| Idioma (heurística) | {datos['idioma']} |")
    L.append(f"| Peso PDF | {meta_archivo['bytes']} bytes ({meta_archivo['mb']} MB) |")
    L.append(f"| Cobertura de texto | {datos['paginas_con_texto']}/{datos['paginas']} páginas ({cobertura:.0f}%) |")
    L.append(f"| Método de extracción | {datos['modo']} |")
    L.append(f"| Estado | {'ESCANEADO — transcrito por OCR' if escaneado else 'Texto extraíble (sin OCR)'} |")
    L.append(f"| Transcripción | [[{slug_transcripcion}\\|{slug_transcripcion}]] |")
    L.append("")
    L.append("## Índice extraído (marcadores del PDF)")
    L.append("")
    if datos["marcadores"]:
        for nivel, tit, pag in datos["marcadores"]:
            sangria = "  " * nivel
            L.append(f"- {sangria}**{tit}** — p. {pag}")
    else:
        L.append("- Sin marcadores/outline en el PDF (documento lineal o escaneado).")
    L.append("")
    L.append("## Figuras detectadas (referencia al PDF, sin extraer)")
    L.append("")
    L.append("> Cuenta **pies de figura** (`FIG. 3`, `Figure 12`, `Figura 4`, `Plate 2`, `Lám. 5`) "
             "encontrados en el texto. No son imágenes: sirven para saber en qué página ir a mirar. "
             "0 = el PDF no trae rótulos o es un escaneo.")
    L.append("")
    if datos["figuras"]:
        L.append("| # | Página del PDF | Pie detectado |")
        L.append("|---|---|---|")
        for n, f in enumerate(datos["figuras"][:60], start=1):
            L.append(f"| {n} | p. {f['pagina']} | {f['rotulo']} |")
        if len(datos["figuras"]) > 60:
            L.append(f"| … | | +{len(datos['figuras']) - 60} pies más |")
        L.append("")
        L.append(f"> Total: {len(datos['figuras'])} pies. Para ver la imagen: abrir el PDF y la página indicada. "
                 f"Las imágenes **no se extraen** (decisión B): la wiki referencia el PDF.")
    else:
        L.append("- Sin pies de figura detectados en el texto (puede ser un PDF con figuras vectoriales sin rótulo).")
    L.append("")
    L.append("## Candidatos a verificación exterior (sherlock)")
    L.append("")
    dois = sorted(set(DOI_RE.findall(datos["texto"])))[:8]
    isbns = sorted(set(re.sub(r"\s+", "-", i).strip("-") for i in ISBN_RE.findall(datos["texto"])))[:8]
    if dois:
        L.append("- DOI detectados (verificar 200 antes de citar): " + ", ".join("`%s`" % d for d in dois))
    if isbns:
        L.append("- ISBN detectados (verificar): " + ", ".join("`%s`" % i for i in isbns))
    if not dois and not isbns:
        L.append("- Sin DOI/ISBN detectables: la referencia completa la resuelve @sherlock (fuera).")
    L.append("")
    L.append("## Qué sí / qué no guarda esta ficha")
    L.append("")
    L.append("- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.")
    L.append("- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).")
    L.append("")
    L.append("## Metodología")
    L.append("")
    L.append(f"- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.")
    L.append(f"- PDF de origen abierto en solo lectura desde `{ruta_original}`; copia de trabajo en `activos/fuentes/{slug}/`.")
    L.append("- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).")
    L.append("- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.")
    L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------

def procesar(ruta, raiz, copiar=True, ocr=False, ocr_lang="eng"):
    from pathlib import Path
    Vault = Path(raiz)

    ruta = os.path.abspath(ruta)
    nombre = os.path.basename(ruta)
    slug = slugify(os.path.splitext(nombre)[0])

    print("[scan] %s" % nombre)
    datos = escanear_pdf(ruta, ocr=ocr, ocr_lang=ocr_lang)
    if not datos:
        print("[error] no se pudo leer %s" % nombre)
        return None
    # NOTA ES: idioma: si el PDF lo declara, lo usamos; si no, heuristica por palabras funcionales.
    datos["idioma"] = datos["meta"].get("/Language") or datos["meta"].get("Language") or detectar_idioma(datos["texto"])

    # NOTA ES: copia de trabajo del binario (gitignored), nunca sobreescribiendo.
    dir_activos = Vault / "activos" / "fuentes" / slug
    dir_activos.mkdir(parents=True, exist_ok=True)
    destino_bin = dir_activos / nombre
    if copiar and not destino_bin.exists():
        shutil.copy2(ruta, destino_bin)
        print("[copy] %s" % destino_bin)
    elif copiar:
        print("[copy] ya existe, se conserva")

    # NOTA ES: metadata del archivo en disco (peso en bytes y MB).
    bytes_pdf = os.path.getsize(ruta)
    meta_archivo = dict(datos["meta"])
    meta_archivo["bytes"] = bytes_pdf
    meta_archivo["mb"] = round(bytes_pdf / 1024 / 1024, 2)
    meta_archivo["autor"] = meta_archivo.get("/Author") or meta_archivo.get("Author") or ""

    # NOTA ES: la ficha y la transcripcion viven en raw/pdf/.
    hoy = datetime.now().strftime("%Y-%m-%d")
    dir_raw = Vault / "raw" / "pdf"
    dir_raw.mkdir(parents=True, exist_ok=True)
    ruta_rel_bin = "activos/fuentes/%s/%s" % (slug, nombre)
    slug_transcripcion = "%s-%s-transcripcion" % (hoy, slug)
    slug_ficha = "%s-%s-ficha" % (hoy, slug)

    # NOTA ES: titulo real del documento (mismo criterio que la ficha).
    titulo_doc, _prov = titulo_de_documento(datos["meta"], nombre, slug)

    # NOTA ES: primero la transcripcion (la ficha la referencia).
    escribir_transcripcion(dir_raw / (slug_transcripcion + ".md"), datos, meta_archivo, slug,
                            ruta_rel_bin, ruta, titulo_doc, datos["idioma"])
    print("[transcripcion] raw/pdf/%s.md" % slug_transcripcion)

    # NOTA ES: despues la ficha, que enlaza a la transcripcion.
    ficha = construir_ficha(datos, meta_archivo, slug, ruta_rel_bin, ruta, slug_ficha,
                            slug_transcripcion, nombre)
    (dir_raw / (slug_ficha + ".md")).write_text(ficha, encoding="utf-8")
    print("[ficha] raw/pdf/%s.md" % slug_ficha)

    # NOTA ES: actualizamos la tabla del indice raw/pdf/00-index.md.
    actualizar_indice(Vault, hoy, slug, datos, meta_archivo, ruta_rel_bin,
                      slug_ficha, slug_transcripcion)
    return dir_raw / (slug_ficha + ".md")


def _leer_ficha(path):
    # NOTA ES: leemos una ficha ya escrita para rehidratar el indice (fuente de verdad).
    txt = path.read_text(encoding="utf-8")
    # NOTA ES: el frontmatter va entre "---" inicial y el siguiente "---".
    partes = txt.split("---", 2)
    fm = partes[1] if len(partes) > 2 else ""
    meta = {}
    for linea in fm.splitlines():
        if ":" in linea:
            k, v = linea.split(":", 1)
            meta[k.strip()] = v.strip()
    cuerpo = partes[2] if len(partes) > 2 else txt
    # NOTA ES: cobertura de texto (patron v2) o "100% nativo" (patron v1).
    cob = re.search(r"Cobertura de texto \| (\d+)/(\d+) p[aá]ginas \((\d+)%\)", cuerpo)
    if cob:
        cobertura = int(cob.group(3))
    elif re.search(r"100% nativo", cuerpo):
        cobertura = 100
    else:
        cobertura = 0
    # NOTA ES: numero de figuras: "Total: N pies" (v2) o "Total: N imagen" (v1).
    figs = re.search(r"Total: (\d+) pies", cuerpo)
    if not figs:
        figs = re.search(r"Total: (\d+) imagen", cuerpo)
    # NOTA ES: palabras: frontmatter (v2) o tabla del cuerpo (v1).
    pals = meta.get("palabras")
    if not pals:
        mp = re.search(r"Palabras \(texto extra[ií]ble\) \| (\d+) \|", cuerpo)
        pals = mp.group(1) if mp else "0"
    # NOTA ES: enlace a la transcripcion (solo v2): capturamos el wikilink COMPLETO.
    tr = re.search(r"\| Transcripci[oó]n \| (\[\[[^\]]+\]\]) \|", cuerpo)
    # NOTA ES: titulo: frontmatter, si no el H1 de la ficha, si no el nombre del archivo.
    titulo = meta.get("titulo")
    if not titulo:
        h1 = re.search(r"^#\s+(?:RAW ficha|Transcripci[oó]n)\s+[—\-]\s+(.+)$", cuerpo, re.MULTILINE)
        titulo = h1.group(1).strip() if h1 else path.stem
    # NOTA ES: paginas: frontmatter (v2) o tabla del cuerpo (v1).
    pags = meta.get("paginas")
    if not pags:
        mp = re.search(r"\| P[aá]ginas \| (\d+) \|", cuerpo)
        pags = mp.group(1) if mp else "0"
    return {
        "fecha": meta.get("fecha", ""),
        "titulo": titulo,
        "paginas": pags,
        "palabras": pals,
        "cobertura": cobertura,
        "figuras": figs.group(1) if figs else "0",
        "transcripcion": tr.group(1) if tr else "—",
        "binario": meta.get("fuente_binaria", "—"),
        "estado": meta.get("estado", ""),
        "slug": path.stem.split("-ficha")[0],
    }


def actualizar_indice(Vault, hoy, slug, datos, meta_archivo, ruta_rel_bin, slug_ficha, slug_transcripcion):
    # NOTA ES: el indice se REHIDRATA desde las fichas escritas: no parseamos sus propias filas.
    dir_raw = Vault / "raw" / "pdf"
    indice = dir_raw / "00-index.md"
    if not indice.exists():
        print("[warn] no existe raw/pdf/00-index.md")
        return
    filas = []
    for f in sorted(dir_raw.glob("*-ficha.md")):
        try:
            filas.append(_leer_ficha(f))
        except Exception as e:
            print("   [warn] no se pudo leer %s: %s" % (f.name, e))
    # NOTA ES: orden alfabetico por titulo; la columna de fecha dice cuando se extrajo.
    filas.sort(key=lambda c: c["titulo"].lower())
    cabecera = ["| Fecha | PDF | Págs | Palabras | Texto | Figuras | Transcripción | Ficha | Binario | Estado |",
                "|---|---|---|---|---|---|---|---|---|---|"]
    lineas = cabecera[:]
    for c in filas:
        # NOTA ES: el wikilink lleva "|" escapado ("\|") para no romper la tabla.
        tr = c["transcripcion"]
        tr_cell = tr if tr != "—" else "—"
        fichalink = "%s-ficha" % c["slug"]
        ficha_cell = "[[raw/pdf/%s\\|%s]]" % (fichalink, fichalink)
        lineas.append("| %s | %s | %s | %s | %d%% | %s | %s | %s | `%s` | %s |" % (
            c["fecha"], c["titulo"], c["paginas"], c["palabras"], c["cobertura"],
            c["figuras"], tr_cell, ficha_cell, c["binario"], c["estado"] or "—"))
    # NOTA ES: reconstruimos el archivo: la prosa se conserva, la tabla se reemplaza.
    fuera = [l for l in indice.read_text(encoding="utf-8").splitlines() if not l.startswith("|")]
    out = []
    for l in fuera:
        out.append(l)
        if l.startswith("## Fichas"):
            out.append("")
            out.extend(lineas)
            out.append("")
    indice.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print("[index] tabla rehidratada con %d fichas" % len(filas))


# ---------------------------------------------------------------------------
# Enriquecimiento — pase sobre las transcripciones YA extraidas (sin Ghostscript)
# ---------------------------------------------------------------------------
# NOTA ES: Gate 0 extrae del texto: autores, datos de publicacion, secciones,
# referencias y figuras. @sherlock solo verifica DESPUES lo que vive fuera (DOI, edicion).

# NOTA ES: encabezado de la lista de referencias al final del documento.
RE_REF_HEAD = re.compile(
    r"^\s*(?:\d{1,2}\.?\s*)?(REFERENCES CITED|REFERENCES|BIBLIOGRAPHY|BIBLIOGRAF[IÍ]A|"
    r"REFERENCIAS|WORKS CITED|LITERATURA CITADA)\s*:?\s*$", re.I | re.M)

# NOTA ES: una entrada bibliografica arranca con Apellido y un año, con o sin parentesis
# (estilo APA "(2010)" o estilo español "2010,"), o con [n]/n).
RE_ENTRADA_REF = re.compile(
    r"^\s*(?:\[\d{1,3}\]|\d{1,2}[\.\)])?\s*[A-ZÁÉÍÓÚÑÜ][\wÀ-ÿ'’\-]+"
    r"[\w\s,\.'’\-]{0,70}[\s\(]((?:1[89]|20)\d{2})[a-z]?[\),\.]", re.MULTILINE)

# NOTA ES: autor declarado en portada ("Autor:", "Doctorando:", "Presentada por").
RE_AUTOR_DECL = re.compile(
    r"^\s*(?:AUTOR(?:/A)?|AUTORA|DOCTORANDO(?:/A)?|PRESENTADA? POR|POR)\s*:?\s*(.*)$", re.I | re.M)

# NOTA ES: encabezado de seccion: "1. INTRODUCTION", "3.1 Digital modelling".
RE_ENCABEZADO = re.compile(r"^\s*(\d{1,2}(?:\.\d{1,2})?)\.?\s{1,4}([^\n]{3,75})\s*$", re.M)

# NOTA ES: bloque de publicacion tipo ITcon/congreso.
RE_PUB = re.compile(
    r"^\s*(SUBMITTED|RECEIVED|REVISED|ACCEPTED|PUBLISHED|EDITOR|EDITORES?)\s*:\s*(.+?)\s*$",
    re.I | re.M)

RE_EMAIL = re.compile(r"[\w\.\-+]+@[\w\-]+(?:\.[\w\-]+)+")

# NOTA ES: palabras que delatan una afiliacion (no un nombre de persona).
AFILIACION_RE = re.compile(r"univers|depart|school|faculty|institute|college|polytechnic|"
                           r"architect|studio|office|research|laborator|email|@", re.I)


def _limpiar_nombre(s):
    # NOTA ES: "Jane R. Burry, Ms" -> "Jane R. Burry"; descarta afiliaciones y ruido.
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r",?\s*(Ms|Mr|Mrs|Dr|Dra|Prof|PhD|Ph\.D\.|Arq|Ing)\.?\s*$", "", s)
    if not s or len(s) > 60 or any(c.isdigit() for c in s):
        return ""
    if AFILIACION_RE.search(s):
        return ""
    toks = s.split()
    if not (2 <= len(toks) <= 5):
        return ""
    # NOTA ES: cada token empieza en mayuscula (admite iniciales "R.").
    if not all(t[0].isupper() or (len(t) <= 2 and t.endswith(".")) for t in toks):
        return ""
    return s


def detectar_autores(texto_p1):
    # NOTA ES: 1) autor declarado ("Autor: Nombre") o en la linea siguiente.
    lineas = [l.strip() for l in texto_p1.splitlines()]
    autores, afiliaciones = [], []
    for m in RE_AUTOR_DECL.finditer(texto_p1):
        n = _limpiar_nombre(m.group(1))
        if not n:
            # NOTA ES: "Autor:" solo en la linea, el nombre viene en la linea siguiente.
            resto = texto_p1[m.end():].splitlines()[:2]
            for r in resto:
                n = _limpiar_nombre(r)
                if n:
                    break
        if n and n not in autores:
            autores.append(n)
    if autores:
        return autores, afiliaciones
    # NOTA ES: 2) los emails de la portada suelen estar 1-3 lineas debajo de cada autor.
    idx_email = [i for i, l in enumerate(lineas) if RE_EMAIL.search(l)]
    for i in idx_email:
        for j in range(i - 1, max(-1, i - 5), -1):
            s = lineas[j]
            if not s:
                continue
            n = _limpiar_nombre(s)
            if n:
                if n not in autores:
                    autores.append(n)
                # NOTA ES: la afiliacion puede estar arriba o abajo del nombre (segun la maqueta).
                for rango in (range(j - 1, max(-1, j - 3), -1), range(j + 1, min(len(lineas), j + 4))):
                    for k in rango:
                        a = lineas[k]
                        if not a or RE_EMAIL.search(a):
                            continue
                        if AFILIACION_RE.search(a):
                            a = re.sub(r"\s+", " ", a).strip()
                            if a not in afiliaciones:
                                afiliaciones.append(a)
                            break
                break
    # NOTA ES: fallback: "by Jane Burry and Mark Burry".
    if not autores:
        m = re.search(r"\bby\s+([A-ZÁÉÍÓÚÑÜ][^\n]{3,80})", texto_p1)
        if m:
            for parte in re.split(r"\s+and\s+|,\s*", m.group(1)):
                n = _limpiar_nombre(parte)
                if n and n not in autores:
                    autores.append(n)
    return autores, afiliaciones


def detectar_publicacion(texto_p1):
    # NOTA ES: {SUBMITTED: "...", PUBLISHED: "...", URL: "..."} del bloque de portada.
    datos = {}
    for m in RE_PUB.finditer(texto_p1):
        clave = m.group(1).upper()
        valor = re.sub(r"\s+", " ", m.group(2)).strip()
        datos[clave] = valor
    # NOTA ES: URL de publicacion ("at http://itcon.org/2006/32/").
    for clave in list(datos):
        for u in re.findall(r"https?://\S+", datos[clave]):
            datos["URL"] = u.rstrip(".,;)")
    if "PUBLISHED" in datos:
        sin_url = re.sub(r"\s*at\s+https?://\S+", "", datos["PUBLISHED"]).strip()
        datos["PUBLISHED"] = sin_url
    return datos


def detectar_secciones(texto):
    # NOTA ES: solo tiene sentido si el PDF NO trae marcadores (outline).
    corte = None
    for mm in RE_REF_HEAD.finditer(texto):
        corte = mm.start()
    cuerpo = texto[:corte] if corte is not None else texto
    out, vistos = [], set()
    for m in RE_ENCABEZADO.finditer(cuerpo):
        num, tit = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()
        letras = re.sub(r"[^A-Za-zÁÉÍÓÚÑÜáéíóúñü]", "", tit)
        if len(letras) < 3:
            continue
        mayus = sum(1 for c in letras if c.isupper()) / len(letras)
        # NOTA ES: exigimos MAYUSCULAS (seccion) o numeracion con punto decimal (3.1).
        if mayus < 0.6 and "." not in num:
            continue
        rotulo = "%s  %s" % (num, tit)
        if rotulo in vistos:
            continue
        vistos.add(rotulo)
        out.append((cuerpo[:m.start()].count("## [p. "), rotulo))
    return out


def detectar_referencias(texto):
    # NOTA ES: elegimos el PRIMER encabezado seguido de entradas reales: en documentos largos
    # "BIBLIOGRAFÍA" aparece como running header en cada página y tomar el último nos deja al final.
    for mm in RE_REF_HEAD.finditer(texto):
        resto = texto[mm.end():mm.end() + 6000]
        if len(RE_ENTRADA_REF.findall(resto)) < 3:
            continue
        m = mm
        break
    else:
        return []
    cuerpo = texto[m.end():]
    # NOTA ES: cortamos en el pie de pagina tipo "ITcon Vol. 11 (2006), ..., pg. 446".
    corte = re.search(r"^\s*[A-Z][\w\.\s]{2,40}Vol\.\s*\d+.*?pg\.\s*\d+", cuerpo, re.M)
    if corte:
        cuerpo = cuerpo[:corte.start()]
    cuerpo = re.sub(r"^## \[p\. \d+\]\s*$", "", cuerpo, flags=re.M)
    entradas, actual = [], []
    for linea in cuerpo.splitlines():
        s = re.sub(r"\s+", " ", linea).strip()
        if not s:
            continue
        es_nueva = bool(RE_ENTRADA_REF.match(s))
        if es_nueva and actual:
            entradas.append(" ".join(actual))
            actual = [s]
        elif es_nueva:
            actual = [s]
        elif actual:
            actual.append(s)
    if actual:
        entradas.append(" ".join(actual))
    # NOTA ES: descartamos restos muy cortos (numeros de pagina, ruido).
    return [e for e in entradas if len(e) >= 25][:80]


def _bloque_seccion(txt, titulo):
    # NOTA ES: devuelve (inicio, fin) del bloque "## <titulo>..." hasta el proximo "## ".
    m = re.search(r"(?ms)^## %s[^\n]*\n.*?(?=^## |\Z)" % re.escape(titulo), txt)
    return (m.start(), m.end()) if m else (None, None)


def _reemplazar_seccion(txt, titulo, cuerpo):
    # NOTA ES: elimina TODAS las apariciones del bloque y deja una sola, en su lugar.
    patron = r"(?ms)^## %s[^\n]*\n.*?(?=^## |\Z)" % re.escape(titulo)
    m = re.search(patron, txt)
    bloque = "## %s\n\n%s\n\n" % (titulo, cuerpo.strip())
    if not m:
        return txt
    ini = m.start()
    return txt[:ini] + bloque + re.sub(patron, "", txt)[ini:]


def _insertar_antes_de(txt, titulo_ancla, bloque):
    # NOTA ES: inserta un bloque completo antes de una seccion conocida.
    ini, _ = _bloque_seccion(txt, titulo_ancla)
    if ini is None:
        return txt.rstrip() + "\n\n" + bloque.strip() + "\n"
    return txt[:ini] + bloque.strip() + "\n\n" + txt[ini:]


def _upsert_seccion(txt, titulo, cuerpo, ancla):
    # NOTA ES: si la seccion ya existe la reemplaza; si no, la inserta antes del ancla.
    if _bloque_seccion(txt, titulo)[0] is not None:
        return _reemplazar_seccion(txt, titulo, cuerpo)
    return _insertar_antes_de(txt, ancla, "## %s\n\n%s" % (titulo, cuerpo.strip()))


def enriquecer(Vault, solo=None):
    dir_raw = Vault / "raw" / "pdf"
    n_ok, n_sin_tr = 0, 0
    for f in sorted(dir_raw.glob("*-ficha.md")):
        base = f.stem.replace("-ficha", "")
        if solo and solo not in base:
            continue
        tr = dir_raw / (base + "-transcripcion.md")
        if not tr.exists():
            n_sin_tr += 1
            continue
        texto = tr.read_text(encoding="utf-8")
        # NOTA ES: separamos la portada (primeras 3 paginas) del resto.
        m_p1 = texto.find("## [p. 1]")
        portada = texto[m_p1:m_p1 + 4000] if m_p1 >= 0 else texto[:4000]
        autores, afiliaciones = detectar_autores(portada)
        publicacion = detectar_publicacion(portada)
        secciones = detectar_secciones(texto)
        referencias = detectar_referencias(texto)

        txt = f.read_text(encoding="utf-8")
        m_aut = re.search(r"^autor:[ \t]*(.*)$", txt, re.MULTILINE)
        autor_actual = (m_aut.group(1).strip() if m_aut else "")
        # NOTA ES: un valor con ":" no es un autor, es una linea de otro campo (defensa).
        if ":" in autor_actual or autor_actual.startswith("—"):
            autor_actual = ""
        m_org = re.search(r"^autor_origen:[ \t]*(.*)$", txt, re.MULTILINE)
        origen_previo = (m_org.group(1).strip() if m_org else "")
        autor_origen = "metadata" if autor_actual else "pendiente"
        # NOTA ES: si el autor ya se habia detectado en el texto, conservamos ese origen.
        if autor_actual and origen_previo == "texto":
            autor_origen = "texto"
        # NOTA ES: si coincide exactamente con lo detectado en la portada, su origen es el texto.
        if autor_actual and autores and autor_actual == "; ".join(autores):
            autor_origen = "texto"
        if not autor_actual and autores:
            autor_final = "; ".join(autores)
            autor_origen = "texto"
            txt = re.sub(r"^autor:.*$", "autor: %s" % autor_final, txt, count=1, flags=re.MULTILINE)
        else:
            autor_final = autor_actual or "—"
        # NOTA ES: el origen se actualiza siempre (si ya existia podia estar desactualizado).
        if "autor_origen:" in txt:
            txt = re.sub(r"^autor_origen:.*$", "autor_origen: %s" % autor_origen, txt, count=1, flags=re.MULTILINE)
        else:
            txt = re.sub(r"^(autor: .*)$", r"\1\nautor_origen: %s" % autor_origen,
                         txt, count=1, flags=re.MULTILINE)

        # NOTA ES: fila Autor de la tabla de metadata.
        detalle = autor_final
        if autor_origen == "texto" and afiliaciones:
            detalle = "%s — %s _(detectado en la portada; confirma @sherlock)_" % (
                autor_final, "; ".join(afiliaciones[:2]))
        elif autor_origen == "pendiente":
            detalle = "— (sin metadata y sin patrón en la portada; lo resuelve @sherlock)"
        txt = re.sub(r"^\| Autor \|.*$", "| Autor | %s |" % detalle, txt, count=1, flags=re.MULTILINE)

        # NOTA ES: datos de publicacion (revista, fechas, editor, URL).
        if publicacion:
            etiquetas = {"SUBMITTED": "Submitted", "RECEIVED": "Received", "REVISED": "Revised",
                         "ACCEPTED": "Accepted", "PUBLISHED": "Published", "EDITOR": "Editor",
                         "URL": "URL"}
            filas = ["| Campo | Valor |", "|---|---|"]
            for clave in ("SUBMITTED", "RECEIVED", "REVISED", "ACCEPTED", "PUBLISHED", "EDITOR", "URL"):
                if clave in publicacion:
                    filas.append("| %s | %s |" % (etiquetas[clave], publicacion[clave]))
            cuerpo_pub = ("\n".join(filas) +
                          "\n\n> Extraído de la portada del PDF. @sherlock verifica revista/volumen/páginas.")
            txt = _upsert_seccion(txt, "Datos de publicación", cuerpo_pub,
                                  "Índice extraído (marcadores del PDF)")

        # NOTA ES: indice de secciones SOLO si el PDF no trae outline.
        if secciones and "Sin marcadores/outline" in txt:
            filas = ["| Página | Sección detectada |", "|---|---|"]
            for pag, rot in secciones:
                filas.append("| p. %d | %s |" % (pag, rot))
            cuerpo_sec = ("\n".join(filas) +
                          "\n\n> El PDF no trae marcadores: estas secciones se detectaron por numeración"
                          " y mayúsculas en el texto. Puede faltar alguna.")
            txt = _upsert_seccion(txt, "Índice de secciones (detectado en el texto)", cuerpo_sec,
                                  "Figuras detectadas (referencia al PDF, sin extraer)")

        # NOTA ES: referencias citadas (crudas, sin verificar).
        if referencias:
            lineas = []
            for i, e in enumerate(referencias, start=1):
                lineas.append("%d. %s" % (i, e))
            lineas.append("")
            lineas.append("> %d entradas detectadas al final del documento, **sin verificar**. "
                          "@sherlock completa DOI/URL y edición; @contenidos decide cuáles cita la ficha wiki."
                          % len(referencias))
            txt = _upsert_seccion(txt, "Referencias citadas (crudo)", "\n".join(lineas),
                                  "Candidatos a verificación exterior (sherlock)")

        # NOTA ES: leyenda que explica que "figuras" son PIES de figura, no imagenes.
        if "Cuenta **pies de figura**" not in txt:
            ini, _ = _bloque_seccion(txt, "Figuras detectadas (referencia al PDF, sin extraer)")
            if ini is not None:
                leyenda = ("\n> Cuenta **pies de figura** (`FIG. 3`, `Figure 12`, `Figura 4`, `Plate 2`, `Lám. 5`) "
                           "encontrados en el texto. No son imágenes: sirven para saber en qué página ir a mirar. "
                           "0 = el PDF no trae rótulos o es un escaneo.\n")
                fin_linea = txt.find("\n", ini)
                txt = txt[:fin_linea] + "\n" + leyenda + txt[fin_linea:]

        # NOTA ES: normalizamos saltos triples que dejan las inserciones.
        txt = re.sub(r"\n{3,}", "\n\n", txt)
        f.write_text(txt, encoding="utf-8")
        n_ok += 1
        print("[ok] %s — autor: %s (%s) | secciones: %d | refs: %d"
              % (base[11:], autor_final, autor_origen, len(secciones), len(referencias)))
    actualizar_indice(Vault, "", "", {}, {}, "", "", "")
    print("[enriquecer] %d fichas · %d sin transcripción" % (n_ok, n_sin_tr))


def fix_titulos(Vault):
    # NOTA ES: modo --fix-titulos: corrige TITULOS y WIKILINKS de lo ya extraido, sin re-extraer texto.
    dir_raw = Vault / "raw" / "pdf"
    cambios = 0
    for f in sorted(dir_raw.glob("*-ficha.md")):
        txt = f.read_text(encoding="utf-8")
        txt_orig = txt
        # NOTA ES: 1) titulo actual y archivo de origen (para recalcular el titulo).
        m_tit = re.search(r"^titulo: (.*)$", txt, re.MULTILINE)
        m_org = re.search(r"^fuente_original: (.*)$", txt, re.MULTILINE)
        if not m_tit or not m_org:
            continue
        titulo_actual = m_tit.group(1).strip()
        origen = m_org.group(1).strip()
        nombre_archivo = os.path.basename(origen)
        # NOTA ES: 2) si el titulo era un artefacto de edicion, lo sustituimos por el nombre real.
        nuevo = titulo_actual
        if TITULO_ARTEFACTO_RE.search(titulo_actual) or es_titulo_archivo(titulo_actual):
            nuevo = re.sub(r"\s+", " ", os.path.splitext(nombre_archivo)[0]).strip()
        # NOTA ES: 3) el wikilink a la transcripcion debe ser absoluto (AGENTS.md).
        # OJO: en tablas Markdown el pipe va escapado ("\|"), asi que reemplazamos texto literal,
        # no con regex, y cubrimos las dos formas: "[[slug|" y "[[slug\|".
        base = f.stem.replace("-ficha", "")
        for sep in ("|", "\\|"):
            rel = "[[%s-transcripcion%s" % (base, sep)
            if rel in txt and ("[[raw/pdf/%s-transcripcion%s" % (base, sep)) not in txt:
                txt = txt.replace(rel, "[[raw/pdf/%s-transcripcion%s" % (base, sep))
        txt2 = txt
        # NOTA ES: 4) reescribimos titulo en el frontmatter y en el H1.
        slug_tr = base + "-transcripcion"
        txt2 = re.sub(r"^titulo: .*$", "titulo: %s" % nuevo, txt2, count=1, flags=re.MULTILINE)
        txt2 = re.sub(r"^# RAW ficha — .*$", "# RAW ficha — %s" % nuevo, txt2, count=1, flags=re.MULTILINE)
        if nuevo != titulo_actual:
            # NOTA ES: 5) marcamos el titulo como provisional: el definitivo lo trae @sherlock.
            if "titulo_provisional:" not in txt2:
                txt2 = re.sub(r"^(titulo: .*)$", r"\1\ntitulo_provisional: si", txt2, count=1, flags=re.MULTILINE)
        if txt2 != txt_orig:
            f.write_text(txt2, encoding="utf-8")
            cambios += 1
        # NOTA ES: 6) la transcripcion pareja: mismo titulo en frontmatter y H1.
        tr = dir_raw / (slug_tr + ".md")
        if tr.exists():
            txt3 = tr.read_text(encoding="utf-8")
            txt3 = re.sub(r"^titulo: .*$", "titulo: %s" % nuevo, txt3, count=1, flags=re.MULTILINE)
            txt3 = re.sub(r"^# Transcripci[oó]n — .*$", "# Transcripción — %s" % nuevo, txt3, count=1, flags=re.MULTILINE)
            tr.write_text(txt3, encoding="utf-8")
    # NOTA ES: 7) rehidratamos el indice con las fichas ya corregidas.
    actualizar_indice(Vault, "", "", {}, {}, "", "", "")
    print("[fix] %d fichas corregidas" % cambios)


# NOTA ES: Vault_raiz devuelve la raiz del vault (la carpeta que contiene scripts/ y raw/).
def Vault_raiz(args):
    from pathlib import Path
    return Path(args.raiz)


def main():
    ap = argparse.ArgumentParser(description="Escanea PDFs de bibliografia: ficha + transcripcion en raw/pdf/")
    ap.add_argument("--src", help="ruta a un PDF concreto")
    ap.add_argument("--dir", help="carpeta con PDFs")
    ap.add_argument("--all", action="store_true", help="procesa todos los PDF de --dir")
    ap.add_argument("--raiz", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    help="raiz del vault (por defecto: la carpeta del repo)")
    ap.add_argument("--no-copy", action="store_true", help="no copia el binario a activos/fuentes")
    ap.add_argument("--ocr", action="store_true", help="aplica OCR (tesseract) a las paginas sin texto")
    ap.add_argument("--ocr-lang", default="eng", help="idioma para tesseract (eng/spa)")
    ap.add_argument("--enriquecer", nargs="?", const="", default=None,
                    help="completa fichas (autor, secciones, referencias, publicacion) leyendo las transcripciones; slug opcional")
    ap.add_argument("--fix-titulos", action="store_true",
                    help="corrige titulos artefacto y wikilinks de lo ya extraido (sin re-extraer)")
    args = ap.parse_args()

    if args.enriquecer is not None:
        enriquecer(Vault_raiz(args), args.enriquecer or None)
        return

    if args.fix_titulos:
        fix_titulos(Vault_raiz(args))
        return

    if not GS:
        print("FALTA Ghostscript (gswin64c). Instalalo o pasalo por --gs.")
        return

    if args.src:
        procesar(args.src, args.raiz, copiar=not args.no_copy, ocr=args.ocr, ocr_lang=args.ocr_lang)
    elif args.dir and args.all:
        for f in sorted(os.listdir(args.dir)):
            if f.lower().endswith(".pdf"):
                # NOTA ES: "0. INDEX.pdf" es el indice de la carpeta: tambien se procesa, como mapa del corpus.
                procesar(os.path.join(args.dir, f), args.raiz,
                         copiar=not args.no_copy, ocr=args.ocr, ocr_lang=args.ocr_lang)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
