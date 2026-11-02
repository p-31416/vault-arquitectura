#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
dashboard-quincena.py — tablero HTML del trabajo de la quincena (reporte de sesiones).

Qué hace, en una frase:
    Lee las sesiones, el log, los commits y los archivos nuevos del período y
    genera un tablero estático con KPIs, línea de tiempo por día y reporte
    de sesiones, sin base de datos y sin dependencias.

Por qué existe:
    specs/261102-dashboard-resumen-15d.md es el reporte en markdown para
    Obsidian. Faltaba la vista visual: un HTML que se abre con doble clic
    y muestra el trabajo de la semana/quincena de un vistazo, como los
    tableros del curso y del concurso.

Cómo se usa:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\dashboard-quincena.py
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\dashboard-quincena.py --desde 2026-10-18 --hasta 2026-11-02 --out activos/web/quincena

Salida:
    activos/web/quincena/index.html   (HTML + CSS + JS en un solo archivo)
    activos/web/quincena/datos.json   (los datos, por si se quieren reusar)
"""

# NOTA ES: argparse = leer opciones de la línea de comandos sin if/else manual.
import argparse
# NOTA ES: datetime/date = fechas del período y de los archivos.
from datetime import date, datetime
# NOTA ES: html.escape = convertir <>& en entidades para no romper el HTML.
import html
# NOTA ES: json = escribir datos.json y embeber los datos en el HTML.
import json
# NOTA ES: os = rutas, listado de carpetas y fechas de modificación.
import os
# NOTA ES: re = expresiones regulares para fechas y encabezados markdown.
import re
# NOTA ES: subprocess = correr git log y leer su salida sin bloquear.
import subprocess


# NOTA ES: ficha por tema — descripción breve (dónde vive, qué trae, plans). Editable.
TEMAS = {
    "rhino": {
        "titulo": "Rhino 3D + massing",
        "desc": "Modelado y láminas en Rhino 8: corte A3 1:50 de AIZ, Casa Uruguay "
                "con Section Styles por material, y massing 2.5D de Sagrada (OSM/CADMapper) "
                "y CABA (Tejido Urbano GCBA).",
        "rutas": ["proyectos/MVP_05-rhino-mcp",
                  "proyectos/concurso-gaudi-nexus/earth2rhino3d",
                  "scripts/cortes-plaza-rhino.py",
                  "scripts/construir-massing-caba-rhino.py"],
        "plans": ["Correr el builder de massing CABA en Rhino 8",
                  "Lámina de cortes de plaza + detalles a 1:2000",
                  "Matriz del concurso, WF-03 (Rhino → render)"],
    },
    "comfy": {
        "titulo": "ComfyUI + concurso",
        "desc": "Generación local en RX 570: matriz txt2img con seed fijo, galería web, "
                "tableros del curso y del concurso, 17 LoRAs validadas, set sdxl-vista "
                "de 7 WF y research de modelos, catenarias y plaza.",
        "rutas": ["proyectos/MVP_04-comfyui-arquitectura",
                  "proyectos/concurso-gaudi-nexus/workflows",
                  "activos/web/galeria", "activos/web/concurso"],
        "plans": ["Cerrar la tanda de calibración de LoRAs (32 renders)",
                  "Activar RunPod para FLUX.2 klein 9B + LoRA rhino-to-image",
                  "Plan de continuación de pruebas, Fases A–H"],
    },
    "autocad": {
        "titulo": "AutoCAD 2D",
        "desc": "Dibujo y cómputos en AutoCAD LT 2027: SET_01 de replanteo, bloque "
                "SIMB-LOC_ID, planillas de locales y dashboard de CAD.",
        "rutas": ["proyectos/MVP_02-autocad-standards",
                  "proyectos/STUDIO_OS-Emilia/presentacion/dashboard-autocad.html"],
        "plans": ["Propuesta SET_04-URB sobre el 2D de Barcelona",
                  "Cadena CAD → Rhino → ComfyUI → lámina A1"],
    },
    "hermes": {
        "titulo": "Hermes + Sistema Operativo",
        "desc": "El agente del estudio y su sistema: VISION/ESTRUCTURA/REQUISITOS, "
                "plan maestro T1-T9, overview, ingeniería C4, guion Remotion con "
                "holoarquitecto, Telegram + n8n + Leantime, y VPS verificado.",
        "rutas": ["proyectos/MVP_07-studio-os-sistema",
                  "specs/261102-plan-maestro-pi-por-temas.md",
                  "specs/261102-system-overview-pi.md",
                  "diagramas/pi-system-ingenieria.md"],
        "plans": ["Crear key Pollinations sk_ y pipe Telegram de 3 nodos",
                  "Fases F0–F6 del Studio OS",
                  "Plan 24 h: croquis → LoRA → láminas"],
    },
    "otros": {
        "titulo": "Otros",
        "desc": "Sesiones que alimentan varios frentes a la vez.",
        "rutas": ["raw/sessions"],
        "plans": [],
    },
}

# NOTA ES: orden de chequeo — hermes primero (vocabulario más específico),
# NOTA ES: rhino antes que autocad (una sesión de Rhino nombra a AutoCAD LT de contexto).
_REGLAS_TEMA = [
    ("hermes", ["hermes", "studio-os", "os-studio", "pitau", "plan-hermes",
                "empresa sint", "tabula rasa", "remotion", "fathom",
                "telegram", "n8n", "jina", "pollinations", "leantime",
                "contabo", "monitoreo", "presentacion pi", "meta-arquitecto",
                "puerta", "agente", "agenda"]),
    ("rhino", ["rhino", "massing", "clipping", "hatch", "trama", "corte",
               "uruguay", "caba", "obelisco", "osm", "overpass", "cadmapper",
               "earth2rhino", "grasshopper", "hops", "malla",
               "seccion", "tejido urbano", "grasshopper"]),
    ("autocad", ["autocad", "replanteo", "autolisp", "lisp", "araoz",
                 "locales", "set_01", "set-01", "cuadro-locales", "bloque"]),
    ("comfy", ["comfy", "txt2img", "img2img", "img2video", "lora", "galeria",
               "matriz", "flux", "sdxl", "higgsfield", "concurso", "gaudi",
               "nexus", "catenaria", "fractal", "render", "hires", "baseline",
                "curso", "muestra", "video", "heygen", "sagrada", "pasion",
                "escher", "mosaico", "fachada"]),
]


def clasificar(sesion):
    """Devuelve la clave de tema por tags + título (una sesión, un tema)."""
    texto = (" ".join(sesion["tags"]) + " " + sesion["titulo"]).lower()
    # NOTA ES: se parte también por : @ . ( ) para que "tim:" y "@tim" valgan como "tim".
    palabras = set(re.split(r"[\s\-_/,.:@()]+", texto))
    # NOTA ES: claves cortas (pi, cad, set, cal, tim) solo valen como palabra
    # NOTA ES: completa: así "pip-install" queda fuera de hermes y "último" fuera de comfy.
    # NOTA ES: "3d" quedó fuera a propósito: también nombra al grafo 3D web, que es hermes.
    if "pi" in palabras or "cal" in palabras or "agenda" in palabras:
        return "hermes"
    if "cad" in palabras or "set" in palabras:
        return "autocad"
    if "tim" in palabras:
        return "comfy"
    # NOTA ES: el LoRA se llama "rhino-to-image" pero corre en Comfy: el nombre
    # NOTA ES: del LoRA no decide, decide el modelo que lo ejecuta.
    if "lora" in palabras or "flux" in texto or "txt2img" in texto:
        return "comfy"
    for tema, claves in _REGLAS_TEMA:
        if any(c in texto for c in claves):
            return tema
    return "otros"


# NOTA ES: lista editable — lo que queda para el siguiente ciclo.
PENDIENTES = [
    "Localizar el dashboard solo-imágenes del concurso y enlazarlo desde el índice",
    "Crear key Pollinations sk_ y armar el pipe Telegram de 3 nodos en n8n",
    "Correr el builder de massing CABA dentro de Rhino 8",
    "Cerrar la tanda de calibración de LoRAs (32 renders, arranque SD1.5 0.8)",
    "Activar RunPod para FLUX.2 klein 9B + LoRA rhino-to-image",
    "Completar las filas Fuentes-Inbox con título pendiente",
]


def leer_texto(ruta):
    """Lee un archivo como texto; si falla, devuelve cadena vacía."""
    try:
        # NOTA ES: errors="replace" = ningún archivo rompe el tablero por un byte raro.
        with open(ruta, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def parsear_sesion(ruta):
    """Extrae fecha, título, tags y bullets de una sesión de raw/sessions/."""
    texto = leer_texto(ruta)
    if not texto:
        return None
    base = os.path.basename(ruta)
    # NOTA ES: la fecha vive en el prefijo del nombre: 2026-11-02-sesion-....md.
    m = re.match(r"(\d{4}-\d{2}-\d{2})", base)
    fecha = m.group(1) if m else ""
    titulo = base
    # NOTA ES: el título es la primera línea que arranca con "# ".
    for linea in texto.splitlines():
        if linea.startswith("# "):
            titulo = linea[2:].strip()
            break
    tags = []
    # NOTA ES: el frontmatter va entre los dos primeros "---"; los tags van en una línea.
    partes = texto.split("---")
    if len(partes) >= 3:
        for linea in partes[1].splitlines():
            if linea.strip().startswith("tags:"):
                dentro = re.search(r"\[(.*)\]", linea)
                if dentro:
                    tags = [t.strip() for t in dentro.group(1).split(",") if t.strip()]
                break
    bullets = []
    # NOTA ES: se recogen los bullets de la primera sección de trabajo ("Qué se hizo").
    en_seccion = False
    for linea in texto.splitlines():
        if linea.startswith("## "):
            # NOTA ES: lower() evita que la tilde de "Qué" rompa la detección.
            en_seccion = "se hizo" in linea.lower()
            continue
        if en_seccion:
            s = linea.strip()
            if s.startswith("- ") or re.match(r"^\d+\.\s", s):
                limpio = re.sub(r"^\d+\.\s", "", s[2:] if s.startswith("- ") else s)
                bullets.append(limpio[:220])
                if len(bullets) >= 6:
                    break
    return {"archivo": base, "fecha": fecha, "titulo": titulo,
            "tags": tags, "bullets": bullets}


def parsear_log(ruta, desde, hasta):
    """Extrae las entradas de log.md dentro del período: fecha + título + bullets."""
    texto = leer_texto(ruta)
    entradas = []
    actual = None
    for linea in texto.splitlines():
        # NOTA ES: cada entrada arranca con "## AAAA-MM-DD ...".
        m = re.match(r"##\s+(\d{4}-\d{2}-\d{2})\s*(.*)", linea)
        if m:
            if actual:
                entradas.append(actual)
            actual = {"fecha": m.group(1), "titulo": m.group(2).strip(),
                      "bullets": []}
            continue
        if actual is not None and linea.strip().startswith("- ") \
                and len(actual["bullets"]) < 4 and desde <= actual["fecha"] <= hasta:
            actual["bullets"].append(linea.strip()[2:][:220])
    if actual:
        entradas.append(actual)
    # NOTA ES: el log trae lo nuevo arriba; se filtra por rango de fechas ISO (comparan bien como texto).
    return [e for e in entradas if desde <= e["fecha"] <= hasta]


def commits_git(raiz, desde, hasta):
    """Lee el git log del período; si git falla, devuelve lista vacía."""
    try:
        # NOTA ES: --oneline = una línea por commit: hash + mensaje.
        r = subprocess.run(
            ["git", "log", "--oneline", "--since=" + desde, "--until=" + hasta],
            capture_output=True, text=True, timeout=60, cwd=raiz)
        if r.returncode != 0:
            return []
        return [l.strip() for l in r.stdout.splitlines() if l.strip()]
    except (OSError, subprocess.SubprocessError):
        return []


def archivos_nuevos(raiz, carpeta, ext, desde, hasta):
    """Lista archivos por fecha de modificación dentro del período (título + fecha)."""
    base = os.path.join(raiz, carpeta)
    items = []
    if not os.path.isdir(base):
        return items
    for nombre in sorted(os.listdir(base)):
        if not nombre.endswith(ext):
            continue
        ruta = os.path.join(base, nombre)
        if not os.path.isfile(ruta):
            continue
        # NOTA ES: fromtimestamp convierte la fecha del archivo a AAAA-MM-DD.
        f = datetime.fromtimestamp(os.path.getmtime(ruta)).strftime("%Y-%m-%d")
        if desde <= f <= hasta:
            titulo = nombre
            # NOTA ES: en los .md el título es la primera línea "# ...".
            if ext == ".md":
                for linea in leer_texto(ruta).splitlines():
                    if linea.startswith("# "):
                        titulo = linea[2:].strip()
                        break
            items.append({"archivo": carpeta + "/" + nombre, "fecha": f,
                          "titulo": titulo})
    return items


def contar_renders(raiz):
    """Cuenta los PNG del concurso generados en el período (fractal-hires + sdxl-vista)."""
    total = 0
    base = os.path.join(raiz, "activos", "proyectos", "concurso-gaudi-nexus")
    for dirpath, _dirs, files in os.walk(base):
        total += sum(1 for n in files if n.lower().endswith(".png"))
    return total


HTML = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quincena __DESDE__ → __HASTA__ — reporte de trabajo</title>
<style>
  :root { --fondo:#101216; --papel:#fbfbf8; --tinta:#15171b; --gris:#8b9099; --acento:#e8b04b; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--fondo); color:#e9ebef;
         font-family:ui-sans-serif,system-ui,"Segoe UI",Roboto,sans-serif; }
  header { padding:28px 24px 6px; max-width:1200px; margin:0 auto; }
  h1 { margin:0 0 6px; font-size:22px; font-weight:650; }
  header p { margin:0; color:var(--gris); font-size:13px; }
  #busca { display:block; width:min(560px,100%); margin:14px auto 0; padding:10px 14px;
           border-radius:8px; border:1px solid #2a2e35; background:#171a20; color:#e9ebef; font-size:14px; }
  .tabs { display:flex; gap:8px; max-width:1200px; margin:16px auto 0; padding:0 24px; }
  .tabs button { flex:1; padding:11px; font-size:14px; font-weight:650; letter-spacing:.06em;
           border-radius:10px; border:1px solid #2a2e35; background:#171a20; color:var(--gris); cursor:pointer; }
  .tabs button.on { background:var(--acento); border-color:var(--acento); color:#15171b; }
  .kpis { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px;
          max-width:1200px; margin:18px auto 0; padding:0 24px; }
  .kpi { background:#171a20; border:1px solid #242932; border-radius:10px; padding:14px; text-align:center; }
  .kpi b { display:block; font-size:26px; color:var(--acento); }
  .kpi span { font-size:12px; color:var(--gris); }
  main { max-width:1200px; margin:0 auto; padding:10px 24px 60px; }
  h2 { font-size:16px; margin:30px 0 12px; color:var(--acento); font-weight:650; }
  .dia { background:var(--papel); color:var(--tinta); border-radius:10px; padding:16px 18px; margin:0 0 14px; }
  .dia h3 { margin:0 0 8px; font-size:15px; }
  .dia h3 small { color:#6b717b; font-weight:400; }
  .ses { border-top:1px solid #e3e1da; padding:10px 0 4px; }
  .ses:first-of-type { border-top:0; }
  .ses b { font-size:13.5px; }
  .ses code { font-size:11.5px; color:#6b717b; }
  .tags { margin:4px 0; }
  .tags i { display:inline-block; font-style:normal; font-size:11px; background:#efede6;
            border-radius:20px; padding:2px 9px; margin:0 4px 4px 0; color:#5d636d; }
  .ses ul { margin:6px 0 6px; padding-left:20px; font-size:12.5px; color:#3c424b; }
  .ses li { margin:2px 0; }
  table { width:100%; border-collapse:collapse; background:var(--papel); color:var(--tinta);
          border-radius:10px; overflow:hidden; font-size:12.5px; }
  th, td { text-align:left; padding:8px 12px; border-bottom:1px solid #e3e1da; vertical-align:top; }
  th { background:#efede6; font-size:11.5px; text-transform:uppercase; letter-spacing:.04em; color:#5d636d; }
  tr:last-child td { border-bottom:0; }
  .pend { background:var(--papel); color:var(--tinta); border-radius:10px; padding:6px 18px 10px; }
  .pend li { font-size:13px; margin:6px 0; }
  footer { text-align:center; color:var(--gris); font-size:12px; padding:0 0 40px; }
</style>
</head>
<body>
<header>
  <h1>Reporte de trabajo — __DESDE__ → __HASTA__</h1>
  <p>__RESUMEN__</p>
  <input id="busca" type="search" placeholder="Filtrar por palabra (modelo, tema, flujo…)">
  <nav class="tabs">
    <button id="tab-ses" class="on" onclick="solapa('ses')">SESSIONS</button>
    <button id="tab-tem" onclick="solapa('tem')">TEMAS</button>
  </nav>
</header>
<div class="kpis" id="kpis"></div>
<main>
<div id="vista-ses">
  <h2>Línea de tiempo por día</h2>
  <div id="dias"></div>
  <h2>Sesiones del período</h2>
  <table><thead><tr><th>Fecha</th><th>Sesión</th><th>Tags</th></tr></thead><tbody id="sesiones"></tbody></table>
</div>
<div id="vista-tem" style="display:none">
  <h2>Temas</h2>
  <div id="temas"></div>
</div>
  <h2>Specs nuevos</h2>
  <table><thead><tr><th>Fecha</th><th>Spec</th></tr></thead><tbody id="specs"></tbody></table>
  <h2>Scripts nuevos</h2>
  <table><thead><tr><th>Fecha</th><th>Script</th></tr></thead><tbody id="scripts"></tbody></table>
  <h2>Commits</h2>
  <table><thead><tr><th>Commit</th></tr></thead><tbody id="commits"></tbody></table>
  <h2>Pendientes del siguiente ciclo</h2>
  <ol class="pend" id="pend"></ol>
</main>
<footer>Generado __GENERADO__ · datos en datos.json</footer>
<script>
const D = __DATOS__;
const esc = s => s;
function fila3(a, b, c) { return `<tr><td>${a}</td><td>${b}</td><td>${c}</td></tr>`; }
// NOTA JS: KPIs arriba, un número por tarjeta.
document.getElementById("kpis").innerHTML = D.kpis.map(k =>
  `<div class="kpi"><b>${k.n}</b><span>${k.t}</span></div>`).join("");
// NOTA JS: un bloque por día con sus sesiones, tags y bullets.
document.getElementById("dias").innerHTML = D.dias.map(d =>
  `<div class="dia" data-t="${(d.sesiones.map(s => s.titulo + " " + s.tags.join(" ")).join(" ")).toLowerCase()}">
    <h3>${d.fecha} <small>· ${d.sesiones.length} sesión(es)${d.log ? " · " + d.log : ""}</small></h3>
    ${d.sesiones.map(s => `<div class="ses"><b>${s.titulo}</b><br><code>${s.archivo}</code>
      <div class="tags">${s.tags.map(t => `<i>${t}</i>`).join("")}</div>
      <ul>${s.bullets.map(b => `<li>${b}</li>`).join("")}</ul></div>`).join("")}
  </div>`).join("");
document.getElementById("sesiones").innerHTML = D.sesiones.map(s =>
  fila3(s.fecha, `${s.titulo}<br><code>${s.archivo}</code>`, s.tags.join(", "))).join("");
// NOTA JS: una tarjeta por tema con descripción, rutas, sesiones y plans.
document.getElementById("temas").innerHTML = D.temas.map(t =>
  `<div class="dia" data-t="${(t.titulo + " " + t.sesiones.map(s => s.titulo + " " + s.tags.join(" ")).join(" ")).toLowerCase()}">
    <h3>${t.titulo} <small>· ${t.n} sesión(es)</small></h3>
    <p style="font-size:12.5px;color:#3c424b;margin:6px 0">${t.desc}</p>
    <div class="tags">${t.rutas.map(r => `<i><code>${r}</code></i>`).join("")}</div>
    ${t.sesiones.map(s => `<div class="ses"><b>${s.fecha}</b> — ${s.titulo}<br><code>${s.archivo}</code></div>`).join("")}
    ${t.plans.length ? `<ul>${t.plans.map(p => `<li>${p}</li>`).join("")}</ul>` : ""}
  </div>`).join("");
// NOTA JS: las solapas muestran una vista por vez.
function solapa(cual) {
  const ses = cual === "ses";
  document.getElementById("vista-ses").style.display = ses ? "" : "none";
  document.getElementById("vista-tem").style.display = ses ? "none" : "";
  document.getElementById("tab-ses").classList.toggle("on", ses);
  document.getElementById("tab-tem").classList.toggle("on", !ses);
}
document.getElementById("specs").innerHTML = D.specs.map(s =>
  `<tr><td>${s.fecha}</td><td>${s.titulo}<br><code>${s.archivo}</code></td></tr>`).join("");
document.getElementById("scripts").innerHTML = D.nscripts.map(s =>
  `<tr><td>${s.fecha}</td><td><code>${s.archivo}</code></td></tr>`).join("");
document.getElementById("commits").innerHTML = D.commits.map(c =>
  `<tr><td><code>${c}</code></td></tr>`).join("");
document.getElementById("pend").innerHTML = D.pendientes.map(p => `<li>${p}</li>`).join("");
// NOTA JS: el buscador filtra los bloques de día y las tarjetas de tema.
document.getElementById("busca").addEventListener("input", e => {
  const q = e.target.value.toLowerCase();
  document.querySelectorAll(".dia").forEach(d => {
    d.style.display = d.dataset.t.includes(q) ? "" : "none";
  });
});
</script>
</body>
</html>
"""


def generar(raiz, desde, hasta, out):
    """Junta todas las fuentes y escribe datos.json + index.html."""
    ses_dir = os.path.join(raiz, "raw", "sessions")
    sesiones = []
    for nombre in sorted(os.listdir(ses_dir)):
        if not nombre.endswith(".md"):
            continue
        # NOTA ES: el rango se filtra por el prefijo de fecha del nombre.
        if not (desde <= nombre[:10] <= hasta):
            continue
        s = parsear_sesion(os.path.join(ses_dir, nombre))
        if s:
            sesiones.append(s)
    # NOTA ES: orden nuevo → viejo, igual que el log del vault.
    sesiones.sort(key=lambda s: s["fecha"] + s["archivo"], reverse=True)

    entradas_log = parsear_log(os.path.join(raiz, "log.md"), desde, hasta)
    log_por_fecha = {e["fecha"]: e["titulo"] for e in entradas_log}
    commits = commits_git(raiz, desde, hasta)
    # NOTA ES: los mensajes de commit también se escapan (pueden traer < >).
    commits = [html.escape(c) for c in commits]
    specs = archivos_nuevos(raiz, "specs", ".md", desde, hasta)
    nscripts = archivos_nuevos(raiz, "scripts", ".py", desde, hasta)
    renders = contar_renders(raiz)

    dias = []
    # NOTA ES: se recorren todos los días del rango para mostrar también los huecos.
    d0 = date.fromisoformat(desde)
    d1 = date.fromisoformat(hasta)
    paso = d0
    while paso <= d1:
        f = paso.isoformat()
        dias.append({"fecha": f, "log": log_por_fecha.get(f, ""),
                     "sesiones": [s for s in sesiones if s["fecha"] == f]})
        # NOTA ES: date.replace no existe para sumar días; se suma con ordinal.
        paso = date.fromordinal(paso.toordinal() + 1)
    dias.sort(key=lambda d: d["fecha"], reverse=True)

    kpis = [
        {"n": len(sesiones), "t": "sesiones registradas"},
        {"n": len([d for d in dias if d["sesiones"] or d["log"]]), "t": "días con actividad"},
        {"n": len(specs), "t": "specs nuevos"},
        {"n": len(nscripts), "t": "scripts nuevos"},
        {"n": renders, "t": "renders del concurso en disco"},
        {"n": len(commits), "t": "commits"},
    ]
    # NOTA ES: cada sesión cae en un solo tema; "otros" recoge lo que queda.
    temas = []
    for clave, ficha in TEMAS.items():
        propias = [s for s in sesiones if clasificar(s) == clave]
        temas.append({"clave": clave, "titulo": ficha["titulo"],
                      "desc": ficha["desc"], "rutas": ficha["rutas"],
                      "plans": ficha["plans"], "n": len(propias),
                      "sesiones": propias})
    # NOTA ES: html.escape en títulos y bullets para que un "<" no rompa la página.
    # NOTA ES: se escapa todo texto del vault ANTES de volcarlo, en un solo pase.
    for s in sesiones:
        s["titulo"] = html.escape(s["titulo"])
        s["bullets"] = [html.escape(b) for b in s["bullets"]]
        s["tags"] = [html.escape(t) for t in s["tags"]]
        s["archivo"] = html.escape(s["archivo"])
    for d in dias:
        d["log"] = html.escape(d["log"])
    for s in specs:
        s["titulo"] = html.escape(s["titulo"])
        s["archivo"] = html.escape(s["archivo"])
    for t in temas:
        t["titulo"] = html.escape(t["titulo"])
        t["desc"] = html.escape(t["desc"])
        t["rutas"] = [html.escape(r) for r in t["rutas"]]
        t["plans"] = [html.escape(p) for p in t["plans"]]
    datos = {"desde": desde, "hasta": hasta,
             "generado": datetime.now().strftime("%Y-%m-%d %H:%M"),
             "kpis": kpis, "dias": dias, "sesiones": sesiones,
             "temas": temas,
             "specs": specs, "nscripts": nscripts, "commits": commits,
             "pendientes": [html.escape(p) for p in PENDIENTES]}
    # NOTA ES: json separá datos (datos.json) de presentación (index.html con datos embebidos).
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "datos.json"), "w", encoding="utf-8") as fh:
        json.dump(datos, fh, indent=1, ensure_ascii=False)

    seguro = json.dumps(datos, ensure_ascii=False)
    # NOTA ES: se escapan los datos embebidos para que el JSON no cierre el <script>.
    seguro = seguro.replace("<", "\\u003c").replace(">", "\\u003e")
    resumen = ("%d sesiones · %d specs · %d scripts · %d renders · %d commits · %s" %
               (len(sesiones), len(specs), len(nscripts), renders,
                len(commits), datos["generado"]))
    pagina = (HTML.replace("__DESDE__", html.escape(desde))
                   .replace("__HASTA__", html.escape(hasta))
                   .replace("__RESUMEN__", html.escape(resumen))
                   .replace("__GENERADO__", html.escape(datos["generado"]))
                   .replace("__DATOS__", seguro))
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(pagina)
    print("Sesiones: %d · specs: %d · scripts: %d · commits: %d" %
          (len(sesiones), len(specs), len(nscripts), len(commits)))
    print("Listo: %s" % os.path.join(out, "index.html"))


def main():
    ap = argparse.ArgumentParser(description="Tablero HTML del trabajo de la quincena.")
    ap.add_argument("--desde", default="2026-10-18", help="inicio del período (AAAA-MM-DD)")
    ap.add_argument("--hasta", default="2026-11-02", help="fin del período (AAAA-MM-DD)")
    ap.add_argument("--out", default="activos/web/quincena", help="carpeta del sitio")
    args = ap.parse_args()
    # NOTA ES: la raíz del vault es la carpeta padre de scripts/.
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.abspath(os.path.join(raiz, args.out))
    print("Generando %s (%s a %s)" % (out, args.desde, args.hasta))
    generar(raiz, args.desde, args.hasta, out)


if __name__ == "__main__":
    main()
