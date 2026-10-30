#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
dashboard-curso.py — tablero del curso AI×Gaudí: SOLO las imágenes repasadas.

Qué hace, en una frase:
    Lee el manifiesto curado (curso.json: las imágenes que ya repasamos del
    curso, una por una), copia esos PNG a img-curso/, sincroniza los workflows
    del concurso a la librería de ComfyUI con prefijo GX- y genera curso.html
    con el MISMO formato de la galería (mosaico, lienzo, facetas, Polaroid,
    auto-refresh) más dos piezas propias: caja de NOTAS por imagen (qué se
    puede cambiar) y panel de Flujos (video, transcripción, workflow, notas).

Por qué existe:
    La galería general muestra los 94 renders. Este tablero muestra solo lo
    repasado del curso, en orden de revisión (módulo 1 primero), con las notas
    de qué se puede cambiar en cada flujo. Crece a medida que repasamos:
    agregar una fila a curso.json y regenerar.

Modos de uso:
    1) Generar una vez (el usuario lo ejecuta en terminal):
         P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\dashboard-curso.py
    2) Generar + servir + actualizar solo:
         P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\dashboard-curso.py --serve 8891
    El tablero vive junto a la galería (activos/web/galeria/curso.html), así
    que el servidor de la galería (8890) también lo sirve; --serve aquí solo
    regenera cuando cambian curso.json o las imágenes.

Lo que NO hace:
    No toca la galería general. No publica en internet. No escribe wiki/.

Salidas:
    <out>/curso.html        <- el tablero
    <out>/curso-datos.json  <- los datos + la versión (sondeo de actualización)
    <out>/img-curso/        <- las imágenes repasadas

Notas:
    la explicación línea por línea está en scripts/dashboard-curso_notas.md
"""

import argparse
import functools
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent  # raíz del vault

# --- Se reusa la galería: un solo formato, sin duplicar ----------------------
# NOTA ES: la plantilla HTML/CSS/JS vive en galeria-renders.py. Importarla como
# módulo evita dos formatos que divergen (que es donde se cuelan los errores).
def cargar_galeria():
    """Carga galeria-renders.py como módulo (el nombre tiene guiones)."""
    ruta = AQUI / "galeria-renders.py"
    spec = importlib.util.spec_from_file_location("galeria_renders", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# --- Flujos del curso (ficha por módulo; crece el estado, no la lista) -------
# NOTA ES: video = área de participantes (requiere login del curso), transcript
# = ruta en el vault (texto de referencia, no link web), workflow_gx = nombre
# con el que el flujo aparece en la pestaña Workflows de ComfyUI tras el sync.
AREA_CURSO = "https://archademy.ai/my-account/my-competitions/214/?tab=course"
COMFY_URL = "http://127.0.0.1:8188"

FLUJOS = [
    {"modulo": "Módulo 1 · base", "titulo": "Flujo base (WF-01)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-intro-generative-ai.es.md",
     "workflow_fuente": "P:/00-repos/ComfyUI/user/default/workflows/WF04-1.0.0-txt2img-base.json",
     "workflow_gx": "GX-01-modulo1-base-txt2img.json", "estado": "repasado",
     "notas": ("Checkpoint SD1.5 fijo en este grafo (architecturerealmix_v11). / "
               "LoRA: sumar LoraLoader entre checkpoint y sampler + trigger en el prompt, "
               "strength 0.6–0.9 (matriz: 0.8). / Steps: 10 rápido (65 s) · 30 base (195 s) · "
               "50 fino (210 s). / cfg 3–12 (base 7). / Sampler euler+normal o dpmpp_2m+karras. / "
               "Resolución 768×512 base; 512² rápido; 768² detalle. / Seed 42 fija para comparar.")},
    {"modulo": "Módulo 2 · texto a imagen", "titulo": "Comparativa + LoRA strength (WF-02)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-text-to-image.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "pendiente", "notas": ""},
    {"modulo": "Módulo 3 · imagen a imagen", "titulo": "Rhino a imagen (WF-03)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-image-to-image.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "grafo (a) existe", "notas": ""},
    {"modulo": "Módulo 4 · imagen a video", "titulo": "Video LTX (WF-04)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-image-to-video.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "pendiente", "notas": ""},
    {"modulo": "Módulo 5 · imagen a 3D", "titulo": "Preparación + img23D (WF-05)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-image-to-3d.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "pendiente", "notas": ""},
    {"modulo": "Módulo 6 · criterio", "titulo": "Criterio del jurado (WF-06)",
     "video": AREA_CURSO, "transcript": "raw/2026-10-sesion-extraordinaria-aixgaudi-round-table.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "script listo", "notas": ""},
    {"modulo": "Módulo 7 · flujo Gaudí", "titulo": "Arcilla + WF-03 (WF-07)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "pendiente", "notas": ""},
]

LINKS = {
    "area": AREA_CURSO,
    "miro": "https://miro.com/app/board/uXjVHRM2XQU=/ (contraseña: Gaudi2026)",
    "brief_es": "https://archademy.ai/wp-content/uploads/2026/01/GxAI_BRIEFING_ES.pdf",
    "criterio": "proyectos/concurso-gaudi-nexus/criterio/criterio-jurado.md",
    "comfy": COMFY_URL,
}


# --- Catálogo de LoRAs: descarga + qué observar --------------------------------
# NOTA ES: fuente de verdad = wiki/glosario/software/lora-locales-comfyui.md
# (URL CivitAI, trigger, rank) + sidecars .civitai.json (versiones exactas).
# "observar" dice qué característica mirar al repasar una imagen con ese LoRA.
LORAS = {
    # --- SD 1.5 ---
    "JJ_Archvizcg_v2.safetensors": {
        "url": "https://civitai.com/models/191596", "trigger": "archviz",
        "observar": "Render clásico de visualización arquitectónica (rank 128). "
                    "Verificado M03 @0.8: empuja el estilo archviz sin romper la composición."},
    "sandiese.safetensors": {
        "url": "https://civitai.com/models/134165", "trigger": "architecture, building, grey_background",
        "observar": "Conceptos de arquitectura sobre fondo gris (rank 32)."},
    "xsarchitectural-10superhighrisebuilding.safetensors": {
        "url": "https://civitai.com/models/25509", "trigger": "architectural renderings, bird's-eye view",
        "observar": "Torres en vista aérea (rank 32)."},
    "room.safetensors": {
        "url": "https://civitai.com/models/37483", "trigger": "room",
        "observar": "Interiores; trigger genérico (rank 64)."},
    "landscape_architecture_sketch.safetensors": {
        "url": "https://civitai.com/models/45218", "trigger": "sketch, architecture, building",
        "observar": "Croquis de paisaje (rank 32)."},
    "Le Corbusier 2.2.7.2_sd1.5-000016.safetensors": {
        "url": "https://civitai.com/models/67585", "trigger": "zhuai_pb, brutalism",
        "observar": "Brutalismo público, familia Villa Savoye / La Tourette (rank 32)."},
    "BrutalistTech-20.safetensors": {
        "url": "https://civitai.com/models/85252", "trigger": "brutaltech, cement",
        "observar": "Brutalismo técnico; sustituye al brutalista de JJ que pide login (rank 128)."},
    "archisketch-v1.safetensors": {
        "url": "https://civitai.com/models/32757?modelVersionId=39140", "trigger": "linear",
        "observar": "Foto de arquitectura → croquis lineal (rank 16, liviano)."},
    "markerhandsketch-V1.safetensors": {
        "url": "https://civitai.com/models/34384?modelVersionId=40665",
        "trigger": "marker painting, handsketch",
        "observar": "Croquis a marcador (rank 8, el más liviano)."},
    # --- SDXL ---
    "isometric-v1.safetensors": {
        "url": "https://civitai.com/models/151008", "trigger": "isometric style",
        "observar": "Axonometría; el más liviano del set SDXL (rank 16)."},
    "Architectural_Massing.safetensors": {
        "url": "https://civitai.com/models/724833", "trigger": "",
        "observar": "Masa y volumetría (rank 32)."},
    "Architecture_Building.safetensors": {
        "url": "https://civitai.com/models/731161", "trigger": "",
        "observar": "Edificio como sujeto; sustituye al ArchViz de ArteFactoryLab (rank 32)."},
    "baroque_architecture-000006.safetensors": {
        "url": "https://civitai.com/models/336095", "trigger": "",
        "observar": "Barroco; sustituye al brutalista XL de JJ (rank 64)."},
    "ArcvizXL_V01.safetensors": {
        "url": "https://civitai.com/models/549260", "trigger": "archviz 1",
        "observar": "Archviz interior/exterior; el más pesado (rank 128, 870 MB)."},
    "bookstore-xl.safetensors": {
        "url": "https://civitai.com/models/139539", "trigger": "mrares, bookstore",
        "observar": "Interior de librería (rank 128, 870 MB)."},
    "SLskyscraperrenderingXL_V1.0.safetensors": {
        "url": "https://civitai.com/models/198528", "trigger": "",
        "observar": "Render de rascacielos (rank 128, 870 MB)."},
    # --- FLUX (no local) ---
    "rhino-to-image-lora.basic.safetensors": {
        "url": "", "trigger": "",
        "observar": "LoRA del curso (FLUX.2). No corre local: va en pod (RunPod 24 GB)."},
}


# --- Cirugía de la plantilla (anclas exactas; falla fuerte si cambian) --------
# NOTA ES: cada reemplazo exige encontrar el ancla UNA sola vez. Si la galería
# cambia y el ancla desaparece o se duplica, el script grita en vez de generar
# un tablero roto a medias.
def inj(plantilla, ancla, reemplazo):
    """Reemplaza un ancla exacta una sola vez; si no, falla con mensaje claro."""
    n = plantilla.count(ancla)
    if n != 1:
        raise SystemExit("ancla rota (aparece %d veces, se esperaba 1): %r" % (n, ancla[:70]))
    return plantilla.replace(ancla, reemplazo, 1)


CSS_EXTRA = """
  /* ---------- tablero del curso ---------- */
  a.btn { text-decoration:none; display:inline-block; }
  #notas-titulo { margin:14px 0 6px; font-size:13px; text-transform:uppercase;
                 letter-spacing:.6px; color:#5a6070; }
  #notas-box { background:#eef3ec; border:1px solid #cfdcc9; border-radius:4px;
               padding:11px 13px; white-space:pre-wrap; word-break:break-word;
               font-size:12.5px; color:#262a33; }
  #lora-box { background:#eef3ec; border:1px solid #cfdcc9; border-radius:4px;
               padding:11px 13px; white-space:pre-wrap; word-break:break-word;
               font-size:12.5px; color:#262a33; }
  #lora-titulo { margin:14px 0 6px; font-size:13px; text-transform:uppercase;
                 letter-spacing:.6px; color:#5a6070; }
  #lora-box a { color:#0b6e5f; }
  #flujos { position:fixed; top:52px; right:0; bottom:0; width:340px; overflow:auto;
            border-left:1px solid var(--linea); background:var(--panel);
            padding:10px 12px; z-index:40; }
  #flujos.oculto { display:none; }
  .flujo { border:1px solid var(--linea); border-radius:8px; padding:9px 10px; margin-bottom:10px; }
  .flujo-t { font-weight:600; margin-bottom:2px; }
  .flujo-e { color:var(--acento); font-size:11px; margin-bottom:6px; }
  .flujo a { color:var(--acento); }
  .flujo-ruta { color:var(--tenue); font-size:11px; margin-top:4px; word-break:break-word; }
  .flujo-ruta b { color:var(--texto); }
  .flujo-notas { margin-top:6px; font-size:11.5px; white-space:pre-wrap;
                 border-top:1px dashed var(--linea); padding-top:6px; }
  .flujo-links { font-size:11px; color:var(--tenue); margin-bottom:10px; }
  .flujo-links a { color:var(--acento); }
"""

JS_FLUJOS = """
// ------------------------------------------------------- panel de flujos
function pintarFlujos(){
  const box = document.getElementById("flujos");
  if (!box) return;
  const links = `<div class="flujo-links">Fuentes del concurso: `
    + `<a href="${esc(LINKS.area)}" target="_blank" rel="noopener">área de participantes</a> · `
    + `<a href="${esc(LINKS.brief_es)}" target="_blank" rel="noopener">briefing ES</a> · `
    + `tablero Miro (ver NOTA en el vault) · criterio: ${esc(LINKS.criterio)}</div>`;
  box.innerHTML = `<div class="fgrupo"><h3>Flujos del curso</h3>` + links + FLUJOS.map(f =>
    `<div class="flujo"><div class="flujo-t">${esc(f.modulo)} — ${esc(f.titulo)}</div>`
    + `<div class="flujo-e">estado: ${esc(f.estado)}</div>`
    + `<div><a href="${esc(f.video)}" target="_blank" rel="noopener">video en el área de participantes</a></div>`
    + (f.transcript ? `<div class="flujo-ruta">transcripción: ${esc(f.transcript)}</div>` : "")
    + (f.workflow_gx
      ? `<div class="flujo-ruta">abrir en Comfy (pestaña Workflows): <b>${esc(f.workflow_gx)}</b> · `
        + `<a href="${esc(LINKS.comfy)}" target="_blank" rel="noopener">abrir ComfyUI</a></div>`
      : `<div class="flujo-ruta">workflow: pendiente</div>`)
    + (f.notas ? `<div class="flujo-notas"><b>NOTAS — qué se puede cambiar</b>\n${esc(f.notas)}</div>` : "")
    + `</div>`).join("") + `</div>`;
}
"""


def plantilla_curso(gal):
    """Deriva la plantilla del tablero desde la de la galería."""
    h = gal.HTML
    h = inj(h, "<title>Galería de renders · estudio</title>",
            "<title>Curso AI×Gaudí · imágenes repasadas</title>")
    h = inj(h, '<span id="titulo">Galería de renders</span>',
            '<span id="titulo">Curso AI×Gaudí · repasadas</span>'
            '<a class="btn" href="index.html" title="Volver a la galería general">← Galería</a>')
    h = inj(h, 'const EJES = ["base","modelo","lora","tipo","workflow","tags"];',
            'const EJES = ["modulo","flujo","base","modelo","lora","tipo"];\n'
            'const FLUJOS = __FLUJOS__;\nconst LINKS = __LINKS__;')
    h = inj(h, '<option value="workflow">Agrupar: workflow</option>',
            '<option value="modulo" selected>Agrupar: módulo</option>\n'
            '    <option value="flujo">Agrupar: flujo</option>\n'
            '    <option value="workflow">Agrupar: workflow</option>')
    h = inj(h, 'agrupar:"workflow"',
            'agrupar:"modulo"')
    # NOTA ES: el eje nuevo se suma al switch existente, no se reescribe.
    h = inj(h, '    case "seed": return "seed " + (r.seed ?? "—");',
            '    case "seed": return "seed " + (r.seed ?? "—");\n'
            '    case "modulo": return r.modulo || "—";\n'
            '    case "flujo": return r.flujo || "—";')
    h = inj(h, '`${visibles.length} de ${DATOS.length} renders`;',
            '`${visibles.length} de ${DATOS.length} repasadas`;')
    # NOTA ES: corrección del índice de imagen: la galería numera por posición
    # en la vista filtrada (__i) pero el mapa IMG se numera al generar. Con
    # filtros activos eso muestra la imagen de otra fila. Aquí cada fila trae
    # su clave estable __k desde la generación.
    h = inj(h, 'visibles.forEach((r,i) => r.__i = i);',
            'visibles.forEach((r) => r.__i = r.__k);')
    h = inj(h, 'fetch("datos.json?t="',
            'fetch("curso-datos.json?t="')
    h = inj(h, '<div id="prompt-box"></div>',
            '<div id="prompt-box"></div>\n'
            '      <h3 id="notas-titulo">Notas — qué se puede cambiar</h3>\n'
            '      <div id="notas-box"></div>')
    h = inj(h, '<h3 id="notas-titulo">Notas — qué se puede cambiar</h3>\n'
               '      <div id="notas-box"></div>',
            '<h3 id="notas-titulo">Notas — qué se puede cambiar</h3>\n'
            '      <div id="notas-box"></div>\n'
            '      <h3 id="lora-titulo">LoRA — descarga y qué observar</h3>\n'
            '      <div id="lora-box"></div>')
    # (inyección JS de la caja LoRA: más abajo, tras el render de notas,
    # porque su ancla es la salida de esa inyección)
    h = inj(h, 'document.getElementById("full").classList.add("on");',
            'const nb = document.getElementById("notas-box");\n'
            '  if (nb) nb.innerHTML = r.notas\n'
            '    ? `<b>NOTAS — qué se puede cambiar</b>\\n${esc(r.notas)}` : "";\n'
            '  document.getElementById("full").classList.add("on");')
    # NOTA ES: el render arma el HTML con concatenación (+), no con template
    # literals anidados: un backtick dentro de ${...} es legal pero ilegible.
    # En Python se escribe \\n para que al JS llegue \n (salto dentro del texto,
    # no salto real que rompería el literal "..." del JS).
    h = inj(h, '? `<b>NOTAS — qué se puede cambiar</b>\\n${esc(r.notas)}` : "";',
            '? `<b>NOTAS — qué se puede cambiar</b>\\n${esc(r.notas)}` : "";\n'
            '  const li = r.lora_info, lb = document.getElementById("lora-box"),\n'
            '        lt = document.getElementById("lora-titulo");\n'
            '  if (lb) lb.innerHTML = li\n'
            '    ? "<b>LoRA — " + esc(li.nombre) + (li.strength ? " @ " + li.strength : "") + "</b>"\n'
            '      + "\\ntrigger: " + esc(li.trigger || "sin trigger declarado")\n'
            '      + "\\nqué observar: " + esc(li.observar || "—")\n'
            '      + (li.url ? \'\\ndescarga: <a href="\' + esc(li.url) + \'" target="_blank" rel="noopener">\''
            ' + esc(li.url) + "</a>" : "") : "";\n'
            '  if (lt) lt.style.display = li ? "" : "none";\n'
            '  if (lb) lb.style.display = li ? "" : "none";')
    # (la inyección del render de notas vive más arriba, junto a la de la caja LoRA)
    h = inj(h, '</style>', CSS_EXTRA + '</style>')
    h = inj(h, '<button class="btn" id="f-toggle" title="Mostrar u ocultar filtros">Filtros</button>',
            '<button class="btn" id="f-toggle" title="Mostrar u ocultar filtros">Filtros</button>\n'
            '  <button class="btn" id="j-toggle" title="Flujos del curso y notas">Flujos</button>')
    h = inj(h, '<div id="facetas"></div>',
            '<div id="facetas"></div>\n<div id="flujos" class="oculto"></div>')
    h = inj(h, 'document.getElementById("f-toggle").onclick = () =>\n'
               '  document.getElementById("facetas").classList.toggle("oculto");',
            'document.getElementById("f-toggle").onclick = () =>\n'
            '  document.getElementById("facetas").classList.toggle("oculto");\n'
            'document.getElementById("j-toggle").onclick = () =>\n'
            '  document.getElementById("flujos").classList.toggle("oculto");\n'
            + JS_FLUJOS)
    h = inj(h, '\npintar();\n\n// ------------------------------------------------- actualización',
            '\npintar(); pintarFlujos();\n\n// ------------------------------------------------- actualización')
    return h


# --- Filas: metadata del PNG + curaduría del manifiesto ----------------------
def construir_filas(repasadas, indexador, gal):
    """Arma una fila por imagen repasada (metadata ComfyUI + campos del curso)."""
    filas = []
    for rep in repasadas:
        ruta = os.path.abspath(rep["archivo"])
        if not os.path.isfile(ruta):
            print("  (!) no existe:", ruta)
            continue
        try:
            fila = indexador.fila_de(ruta, os.path.dirname(ruta))
        except Exception as exc:  # noqa: BLE001
            print("  (!) no se pudo leer", ruta, exc)
            continue
        try:
            textos = indexador.leer_textos_png(ruta)
        except Exception:
            textos = {}
        grafo = {}
        if "prompt" in textos:
            try:
                grafo = json.loads(textos["prompt"])
            except Exception:
                grafo = {}
        loras = [l["nombre"] for l in fila.get("loras") or []]
        fila["tipo"] = gal.tipo_de(grafo)
        fila["base"] = gal.base_de(fila.get("modelo"), loras)
        fila["clases"] = sorted({n.get("class_type") for n in grafo.values()
                                 if isinstance(n, dict) and n.get("class_type")})
        fila["hsl"] = gal.tono_de(fila.get("seed"))
        # NOTA ES: lora_info cruza el LoRA del PNG con el catálogo LORAS
        # (descarga + trigger + qué observar). Solo el primero: un render
        # repasado tiene un LoRA protagonista.
        info = None
        for l in fila.get("loras") or []:
            if not isinstance(l, dict):
                continue
            cat = LORAS.get(l.get("nombre"))
            if cat:
                info = {"nombre": l.get("nombre"), "strength": l.get("strength"),
                        "url": cat.get("url"), "trigger": cat.get("trigger"),
                        "observar": cat.get("observar")}
                break
        fila["lora_info"] = info
        # NOTA ES: la curaduría manda sobre la metadata: módulo, flujo, título
        # y notas los escribe el equipo al repasar, no los adivina el script.
        fila["modulo"] = rep.get("modulo", "—")
        fila["flujo"] = rep.get("flujo", "—")
        fila["titulo"] = rep.get("titulo", os.path.basename(ruta))
        fila["notas"] = rep.get("notas", "")
        fila["abs_archivo"] = ruta
        filas.append(fila)
    return filas


def copiar_y_generar(filas, out, gal, flujos, links):
    """Copia las imágenes a img-curso/ y escribe curso.html + curso-datos.json."""
    img_dir = os.path.join(out, "img-curso")
    if os.path.isdir(img_dir):
        shutil.rmtree(img_dir)
    os.makedirs(img_dir, exist_ok=True)

    datos, mapa = [], {}
    for f in filas:
        origen = f.get("abs_archivo")
        if not origen or not os.path.isfile(origen):
            continue
        nombre = "%03d_%s.png" % (len(datos), gal.slug(f.get("titulo") or os.path.basename(origen)))
        shutil.copy2(origen, os.path.join(img_dir, nombre))
        f["__k"] = len(datos)  # NOTA ES: clave estable para el mapa IMG (ver fix __i/__k).
        mapa[str(len(datos))] = "img-curso/" + nombre
        datos.append(f)

    version = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = (plantilla_curso(gal)
            .replace("__DATOS__", json.dumps(datos, ensure_ascii=False))
            .replace("__IMG__", json.dumps(mapa, ensure_ascii=False))
            .replace("__VERSION__", json.dumps(version))
            .replace("__FLUJOS__", json.dumps(flujos, ensure_ascii=False))
            .replace("__LINKS__", json.dumps(links, ensure_ascii=False)))
    with open(os.path.join(out, "curso.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(out, "curso-datos.json"), "w", encoding="utf-8") as f:
        json.dump({"version": version, "items": datos}, f, indent=2, ensure_ascii=False)
    return version, len(datos)


# --- Anotaciones en el canvas (notas estilo n8n) -------------------------------
# NOTA ES: ComfyUI trae de fábrica dos nodos de nota — verificado en el fuente
# del frontend 1.45.21 instalado (comfyui_frontend_package/static, el archivo
# `src/extensions/core/noteNode.ts` dentro de core-kRheBl5O.js.map): `Note`
# (texto) y `MarkdownNote` (markdown). Son solo-frontend (`isVirtualNode`):
# la cola los salta y el backend nunca los ve. Consecuencias honestas:
# el validador los reporta como tipos faltantes (esperado), y para encolar
# sin interfaz hay que quitar los nodos "GX ·" antes de enviar el grafo.
# Las notas se hornean en la copia GX durante el sync; el sync no pisa tus
# retoques en el canvas (ver huella_contenido).
MARCA_NOTA = "GX ·"

ANOTACIONES = {
    "GX-01-modulo1-base-txt2img.json": {
        "titulos": {
            1: "1 · Checkpoint SD1.5 — FIJO",
            2: "2 · Prompt + TRIGGER del LoRA",
            3: "3 · Negativo",
            4: "4 · Resolución 768×512",
            5: "5 · KSampler — SE CALIBRA AQUÍ",
            6: "6 · VAE en CPU",
            7: "7 · Salida",
        },
        "notas": [
            {"titulo": "GX · Checkpoint FIJO",
             "texto": "**No se cambia en este flujo.**\n`architecturerealmix_v11` (SD1.5).\nCambiarlo = otro estilo = otro flujo.",
             "pos": [40, -170], "size": [280, 130]},
            {"titulo": "GX · Prompt + TRIGGER",
             "texto": "**Aquí entra el LoRA:** nodo `LoraLoader` entre checkpoint y sampler + palabra trigger en este prompt.\nStrength 0.6–0.9 (matriz: 0.8).",
             "pos": [420, -170], "size": [280, 150]},
            {"titulo": "GX · SE CALIBRA AQUÍ",
             "texto": "**Steps:** 10 rápido (65 s) · 30 base · 50 fino.\n**cfg** 3–12 · **sampler** euler+normal o dpmpp_2m+karras.\n**Seed 42 fija** para comparar.",
             "pos": [800, -170], "size": [280, 150]},
            {"titulo": "GX · Resolución",
             "texto": "**768×512** base · **512²** rápido · **768²** detalle.",
             "pos": [40, 400], "size": [280, 130]},
        ],
    },
}


def huella_contenido(datos, spec):
    """Huella del grafo SIN anotaciones GX (para no repisar tu canvas).

    NOTA ES: quita los nodos "GX ·" y los títulos que gestiona el script;
    lo demás (posiciones, widgets, tus títulos) sí cuenta. El sync solo
    reescribe cuando la FUENTE cambió; tus movimientos en Comfy sobreviven.
    """
    nodos = []
    for n in datos.get("nodes", []):
        if str(n.get("title", "")).startswith(MARCA_NOTA):
            continue
        n = dict(n)
        if spec and n.get("id") in (spec.get("titulos") or {}):
            n.pop("title", None)
        nodos.append(n)
    normal = {"nodes": nodos, "links": datos.get("links", []),
              "groups": datos.get("groups", []), "config": datos.get("config", {})}
    return hashlib.md5(json.dumps(normal, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def anotaciones_al_dia(datos, spec):
    """True si títulos y notas GX están presentes y con el texto vigente."""
    if not spec:
        return True
    nodos = {n.get("id"): n for n in datos.get("nodes", [])}
    for i, t in (spec.get("titulos") or {}).items():
        if nodos.get(i, {}).get("title") != t:
            return False
    textos = {str(n.get("title")): (n.get("widgets_values") or [""])[0]
              for n in datos.get("nodes", [])}
    for nota in spec.get("notas") or []:
        if textos.get(nota["titulo"]) != nota["texto"]:
            return False
    return True


def aplicar_anotaciones(datos, gx, pos_usuario=None):
    """Hornea títulos editoriales + notas MarkdownNote (idempotente)."""
    spec = ANOTACIONES.get(gx)
    if not spec:
        return datos
    nodos = [n for n in datos.get("nodes", [])
             if not str(n.get("title", "")).startswith(MARCA_NOTA)]
    for n in nodos:
        t = (spec.get("titulos") or {}).get(n.get("id"))
        if t:
            n["title"] = t
    ultimo_id = max([n.get("id", 0) for n in nodos] + [0])
    ultimo_orden = max([n.get("order", 0) for n in nodos] + [0])
    pos_usuario = pos_usuario or {}
    for nota in spec.get("notas") or []:
        ultimo_id += 1
        ultimo_orden += 1
        # NOTA ES: si moviste la nota en el canvas, se respeta tu posición;
        # el texto y el título sí se refrescan desde el spec.
        pos, tam = pos_usuario.get(nota["titulo"], (list(nota["pos"]), list(nota["size"])))
        nodos.append({
            "id": ultimo_id, "type": "MarkdownNote",
            "pos": list(pos), "size": list(tam),
            "flags": {}, "order": ultimo_orden, "mode": 0,
            "inputs": [], "outputs": [],
            "properties": {"Node name for S&R": "MarkdownNote", "text": nota["texto"]},
            "title": nota["titulo"], "widgets_values": [nota["texto"]],
        })
    datos["nodes"] = nodos
    datos["last_node_id"] = ultimo_id
    return datos


# --- Sync de workflows a la librería de ComfyUI -------------------------------
def sincronizar_workflows(flujos):
    """Copia los WF del concurso a user/default/workflows/ con prefijo GX-.

    NOTA ES: ComfyUI muestra en la pestaña Workflows del sidebar todo JSON que
    vive en esa carpeta. El sync escribe SOLO si falta el destino o si la
    fuente cambió (huella sin anotaciones): tus retoques en el canvas
    sobreviven a la regeneración. Las anotaciones GX se hornean al escribir.
    """
    for f in flujos:
        fuente = f.get("workflow_fuente")
        gx = f.get("workflow_gx")
        if not fuente or not gx:
            continue
        if not os.path.isfile(fuente):
            print("  (!) fuente ausente:", fuente)
            continue
        destino = os.path.join(os.path.dirname(os.path.abspath(fuente)), gx)
        with open(fuente, encoding="utf-8") as fh:
            datos_fuente = json.load(fh)
        spec = ANOTACIONES.get(gx)
        if os.path.isfile(destino):
            with open(destino, encoding="utf-8") as fh:
                datos_dest = json.load(fh)
            igual = huella_contenido(datos_dest, spec) == huella_contenido(datos_fuente, spec)
            if igual and anotaciones_al_dia(datos_dest, spec):
                print("  GX ya estaba al día:", gx)
                continue
            if igual:
                pos = {str(n.get("title")): (n.get("pos"), n.get("size"))
                       for n in datos_dest.get("nodes", [])
                       if str(n.get("title", "")).startswith(MARCA_NOTA)}
                datos = aplicar_anotaciones(datos_fuente, gx, pos_usuario=pos)
                print("  GX anotado (canvas respetado):", gx)
            else:
                datos = aplicar_anotaciones(datos_fuente, gx)
                print("  GX actualizado desde fuente:", gx)
        else:
            datos = aplicar_anotaciones(datos_fuente, gx)
            print("  GX sincronizado:", gx)
        with open(destino, "w", encoding="utf-8") as fh:
            json.dump(datos, fh, ensure_ascii=False)


def firma(filas, manifiesto):
    """Huella del manifiesto + las imágenes (para detectar cambios en --serve)."""
    partes = [manifiesto]
    try:
        partes.append(str(os.stat(manifiesto).st_mtime_ns))
    except OSError:
        pass
    for f in filas:
        ruta = os.path.abspath(f.get("archivo", ""))
        try:
            partes.append("%s:%d" % (ruta, os.stat(ruta).st_mtime_ns))
        except OSError:
            partes.append(ruta + ":ausente")
    return hashlib.md5("|".join(partes).encode("utf-8")).hexdigest()


def manifiesto_inicial(ruta):
    """Crea curso.json con las dos primeras repasadas (M01 baseline + M03)."""
    inicial = {
        "repasadas": [
            {"archivo": "P:/00-repos/ComfyUI/output/matriz/sd15/M01_00001_.png",
             "modulo": "Módulo 1 · base", "flujo": "WF-01 base",
             "titulo": "M01 baseline SD1.5 sin LoRA",
             "notas": ("Baseline del flujo base: sin LoRA, steps 30, cfg 7, euler/normal, "
                       "768×512, seed 42 (195 s). Punto de comparación para todo lo que cambies.")},
            {"archivo": "P:/00-repos/ComfyUI/output/matriz/sd15/M03_00001_.png",
             "modulo": "Módulo 1 · base", "flujo": "WF-01 base",
             "titulo": "M03 JJ's Archvizcg_v2 @0.8",
             "notas": ("Mismo grafo + LoRA JJ_Archvizcg_v2 @0.8 (175 s). Verificación visual "
                       "contra M01 hecha: el LoRA empuja el estilo archviz sin romper la composición.")},
        ]
    }
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(inicial, f, indent=2, ensure_ascii=False)
    print("manifiesto inicial creado:", ruta)
    return inicial


def main():
    ap = argparse.ArgumentParser(description="Tablero del curso AI×Gaudí (solo repasadas)")
    ap.add_argument("--out", default="activos/web/galeria", help="carpeta del sitio (junto a la galería)")
    ap.add_argument("--curso", default=None, help="manifiesto JSON (default: <out>/curso.json)")
    ap.add_argument("--serve", type=int, metavar="PUERTO", help="servir y regenerar ante cambios")
    ap.add_argument("--una-vez", action="store_true", help="con --serve: generar y salir")
    args = ap.parse_args()

    gal = cargar_galeria()
    indexador = gal.cargar_indexador()
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    ruta_curso = os.path.abspath(args.curso) if args.curso else os.path.join(out, "curso.json")

    if not os.path.isfile(ruta_curso):
        manifiesto = manifiesto_inicial(ruta_curso)
    else:
        with open(ruta_curso, encoding="utf-8") as f:
            manifiesto = json.load(f)
    repasadas = manifiesto.get("repasadas", [])

    def una_pasada():
        with open(ruta_curso, encoding="utf-8") as f:
            rep = json.load(f).get("repasadas", [])
        filas = construir_filas(rep, indexador, gal)
        sincronizar_workflows(FLUJOS)
        return copiar_y_generar(filas, out, gal, FLUJOS, LINKS)

    version, n = una_pasada()
    print("Tablero del curso generado: %s" % os.path.join(out, "curso.html"))
    print("  repasadas: %d | versión: %s" % (n, version))

    if not args.serve:
        print("  para agregar una repasada: editar %s y regenerar" % ruta_curso)
        return 0
    if args.una_vez:
        return 0

    hilo = threading.Thread(target=gal.servir, args=(out, args.serve), daemon=True)
    hilo.start()
    print("  vigilando cambios… (Ctrl+C para salir)")
    with open(ruta_curso, encoding="utf-8") as f:
        ultima = firma(json.load(f).get("repasadas", []), ruta_curso)
    try:
        while True:
            time.sleep(15)
            with open(ruta_curso, encoding="utf-8") as f:
                rep = json.load(f).get("repasadas", [])
            actual = firma(rep, ruta_curso)
            if actual != ultima:
                ultima = actual
                v, n = una_pasada()
                print("  [%s] %d repasadas (actualizado)" % (v, n), flush=True)
    except KeyboardInterrupt:
        print("  cerrado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
