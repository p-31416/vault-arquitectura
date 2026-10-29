#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
galeria-renders.py — genera un sitio web estático para recorrer los renders.

Qué hace, en una frase:
    Lee el índice JSON que produce `indice-renders-comfy.py`, copia las imágenes
    y arma una galería web navegable: un lienzo infinito (pan y zoom) donde cada
    render es una ficha, agrupadas por workflow, y un panel lateral con la
    metadata completa al hacer clic.

Por qué existe:
    Los renders tienen la trazabilidad DENTRO del PNG (bloques tEXt 'prompt' y
    'workflow' que graba ComfyUI). El índice traduce esa metadata a una tabla.
    Pero una tabla no se recorre: no se ve la imagen, no se compara de un
    vistazo, no se llega con un clic a "la de al lado". La galería es esa capa:
    el lugar donde el equipo mira lo que se generó y decide qué sigue.

Qué NO hace:
    No publica nada en internet. Genera archivos estáticos en una carpeta; el
    que decide si eso sale a un dominio es otro (Caddy, EasyPanel, rsync, lo que
    toque). Separation of concerns: el generador no sabe nada de servidores.

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\galeria-renders.py
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\galeria-renders.py --indice INDICE-RENDERS.json --out activos\\web\\galeria

Salida:
    <out>/index.html   ← la galería (HTML+JS en un solo archivo, sin dependencias)
    <out>/datos.json   ← los datos (por si otro programa quiere consumirlos)
    <out>/img/         ← las imágenes copiadas

Notas:
    la explicación línea por línea está en scripts/galeria-renders_notas.md
"""

import argparse
import hashlib
import json
import os
import shutil
from datetime import datetime

# ---------------------------------------------------------------------------
# 1) Helpers
# ---------------------------------------------------------------------------

def slug(texto, maximo=60):
    """Convierte un texto en un nombre de archivo seguro (sin acentos ni espacios)."""
    if not texto:
        return "sin-nombre"
    limpio = "".join(c if c.isalnum() or c in "-_." else "-" for c in str(texto))
    limpio = limpio.strip("-")
    return (limpio[:maximo] or "sin-nombre")


def tono_de(semilla):
    """Un color estable a partir de una seed: el mismo seed siempre same color."""
    # NOTA ES: hashlib es estable entre máquinas y versiones (a diferencia de hash()).
    digest = hashlib.md5(str(semilla).encode("utf-8")).hexdigest()
    return int(digest[:6], 16) % 360


def copiar_imagenes(filas, carpeta_indice, destino_img):
    """Copia cada PNG al sitio y devuelve el mapa {indice_original: ruta_web}."""
    os.makedirs(destino_img, exist_ok=True)
    mapa = {}
    for i, f in enumerate(filas):
        origen = os.path.join(carpeta_indice, f["archivo"])
        if not os.path.isfile(origen):
            continue
        nombre = "%03d_%s.png" % (i, slug(f.get("workflow") or Path_stem(f["archivo"])))
        shutil.copy2(origen, os.path.join(destino_img, nombre))
        mapa[str(i)] = "img/" + nombre
    return mapa


def Path_stem(nombre_archivo):
    """Nombre del archivo sin carpeta ni extensión (sin importar pathlib)."""
    base = os.path.basename(nombre_archivo)
    return os.path.splitext(base)[0]


# ---------------------------------------------------------------------------
# 2) La plantilla HTML
# ---------------------------------------------------------------------------

HTML = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Galería de renders · estudio</title>
<style>
  :root {
    --fondo: #0d0f12; --panel: #16191f; --linea: #262b33; --texto: #e6e9ef;
    --tenue: #8d95a3; --acento: #7fd1c1;
  }
  * { box-sizing: border-box; }
  html, body { margin:0; height:100%; background:var(--fondo); color:var(--texto);
               font:13px/1.45 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }
  #barra { position:fixed; top:0; left:0; right:0; height:48px; display:flex; gap:10px;
           align-items:center; padding:0 14px; background:rgba(13,15,18,.92);
           border-bottom:1px solid var(--linea); z-index:50; backdrop-filter:blur(6px); }
  #titulo { font-weight:600; letter-spacing:.2px; margin-right:6px; }
  #stats { color:var(--tenue); }
  input[type=search] { background:var(--panel); border:1px solid var(--linea); color:var(--texto);
                       border-radius:6px; padding:6px 9px; width:240px; }
  #filtros { display:flex; gap:6px; flex-wrap:wrap; overflow:auto; max-width:45vw; }
  .chip { border:1px solid var(--linea); background:var(--panel); color:var(--tenue);
          border-radius:999px; padding:4px 10px; cursor:pointer; white-space:nowrap; font-size:12px; }
  .chip.on { border-color:var(--acento); color:var(--acento); }
  #lienzo { position:fixed; inset:48px 0 0 0; overflow:hidden; cursor:grab;
            background:
              radial-gradient(circle at 1px 1px, #1c2028 1px, transparent 0) 0 0/28px 28px; }
  #lienzo.arrastrando { cursor:grabbing; }
  #mundo { position:absolute; top:0; left:0; transform-origin:0 0; will-change:transform; }
  .col { position:absolute; }
  .colh { color:var(--tenue); font-size:11px; text-transform:uppercase; letter-spacing:.6px;
          margin:0 0 8px 2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .nodo { position:relative; margin-bottom:10px; cursor:pointer; border-radius:6px;
          overflow:hidden; border:1px solid var(--linea); background:var(--panel); }
  .nodo img { display:block; width:100%; height:auto; }
  .nodo.sel { border-color:var(--acento); box-shadow:0 0 0 2px rgba(127,209,193,.25); }
  .badge { position:absolute; left:6px; top:6px; font-size:10px; padding:2px 6px; border-radius:4px;
           background:rgba(0,0,0,.62); color:#fff; backdrop-filter:blur(3px); }
  .tag { position:absolute; right:6px; bottom:6px; font-size:10px; padding:2px 6px; border-radius:4px;
         background:rgba(0,0,0,.62); color:#fff; max-width:70%; overflow:hidden; text-overflow:ellipsis;
         white-space:nowrap; }
  #panel { position:fixed; top:48px; right:0; width:360px; height:calc(100% - 48px); overflow:auto;
           background:var(--panel); border-left:1px solid var(--linea); z-index:40; padding:14px;
           display:none; }
  #panel.on { display:block; }
  #panel h3 { margin:0 0 4px; font-size:14px; }
  #panel img { width:100%; border-radius:6px; border:1px solid var(--linea); display:block; margin-bottom:10px; }
  #panel table { width:100%; border-collapse:collapse; font-size:12px; }
  #panel td { padding:4px 6px; border-bottom:1px solid var(--linea); vertical-align:top; }
  #panel td:first-child { color:var(--tenue); width:38%; }
  #prompt { margin-top:10px; padding:9px; background:var(--fondo); border:1px solid var(--linea);
            border-radius:6px; white-space:pre-wrap; word-break:break-word; font-size:12px; color:#cdd3dd; }
  #cerrar { position:absolute; right:10px; top:10px; cursor:pointer; color:var(--tenue);
            border:1px solid var(--linea); border-radius:6px; padding:2px 8px; background:var(--fondo); }
  #pie { position:fixed; left:0; right:0; bottom:0; height:64px; display:flex; align-items:center;
         gap:10px; padding:0 14px; background:rgba(13,15,18,.94); border-top:1px solid var(--linea);
         z-index:45; }
  #tira { display:flex; gap:6px; overflow-x:auto; flex:1; }
  #tira img { height:46px; border:1px solid var(--linea); border-radius:4px; cursor:pointer; opacity:.5; }
  #tira img.on { opacity:1; border-color:var(--acento); }
  #nav { color:var(--tenue); font-size:12px; white-space:nowrap; }
  .navbtn { background:var(--panel); border:1px solid var(--linea); color:var(--texto); border-radius:6px;
            padding:5px 10px; cursor:pointer; }
</style>
</head>
<body>
<div id="barra">
  <span id="titulo">Galería de renders</span>
  <span id="stats"></span>
  <input type="search" id="buscar" placeholder="buscar en el prompt…">
  <div id="filtros"></div>
</div>
<div id="lienzo"><div id="mundo"></div></div>
<div id="panel"><button id="cerrar">cerrar ✕</button><div id="panelc"></div></div>
<div id="pie">
  <button class="navbtn" id="prev">◀ anterior</button>
  <span id="nav"></span>
  <button class="navbtn" id="next">siguiente ▶</button>
  <div id="tira"></div>
</div>
<script>
const DATOS = __DATOS__;
const IMG = __IMG__;

// --- Layout: una columna por workflow, las imágenes apiladas dentro ---------
function agrupar() {
  const grupos = new Map();
  DATOS.forEach((d, i) => {
    const k = d.workflow || "sin-workflow";
    if (!grupos.has(k)) grupos.set(k, []);
    grupos.get(k).push(i);
  });
  return [...grupos.entries()].sort((a, b) => b[1].length - a[1].length);
}
let filtroWf = null, filtroLora = false, texto = "";
function visibles() {
  return DATOS.map((d, i) => i).filter(i => {
    const d = DATOS[i];
    if (filtroWf && d.workflow !== filtroWf) return false;
    if (filtroLora && !(d.loras && d.loras.length)) return false;
    if (texto && !(d.prompt || "").toLowerCase().includes(texto)) return false;
    return true;
  });
}
function construir() {
  const mundo = document.getElementById("mundo");
  mundo.innerHTML = "";
  const vis = visibles();
  let x = 40, maxY = 0;
  const grupos = new Map();
  vis.forEach(i => { const k = DATOS[i].workflow || "sin-workflow";
    if (!grupos.has(k)) grupos.set(k, []); grupos.get(k).push(i); });
  [...grupos.entries()].sort((a,b)=>b[1].length-a[1].length).forEach(([wf, idxs]) => {
    const col = document.createElement("div");
    col.className = "col";
    col.style.left = x + "px";
    const h = document.createElement("div"); h.className = "colh";
    h.textContent = wf + " · " + idxs.length; col.appendChild(h);
    idxs.forEach(i => {
      const d = DATOS[i];
      const n = document.createElement("div");
      n.className = "nodo"; n.dataset.i = i;
      n.style.width = "230px";
      const img = document.createElement("img");
      img.src = IMG[String(i)] || ""; img.loading = "lazy"; img.alt = d.prompt || "";
      const b = document.createElement("div"); b.className = "badge";
      b.textContent = "seed " + (d.seed ?? "—");
      b.style.background = "hsla(" + (d.hsl ?? 200) + ",55%,45%,.85)";
      const t = document.createElement("div"); t.className = "tag";
      t.textContent = d.loras && d.loras.length ? d.loras.map(l=>l.nombre).join(", ") : (d.modelo || "");
      n.appendChild(img); n.appendChild(b); n.appendChild(t);
      n.addEventListener("click", () => seleccionar(i));
      col.appendChild(n);
      maxY = Math.max(maxY, n.offsetHeight);
    });
    mundo.appendChild(col);
    x += 250;
  });
  // tira inferior
  const tira = document.getElementById("tira"); tira.innerHTML = "";
  vis.forEach(i => {
    const im = document.createElement("img"); im.src = IMG[String(i)] || ""; im.dataset.i = i;
    im.addEventListener("click", () => seleccionar(i));
    tira.appendChild(im);
  });
  document.getElementById("stats").textContent =
    vis.length + " de " + DATOS.length + " renders · " + new Set(DATOS.map(d=>d.workflow)).size + " workflows";
}

// --- Panel de detalle -------------------------------------------------------
let sel = -1;
function seleccionar(i) {
  sel = i; const d = DATOS[i];
  const p = document.getElementById("panel"), c = document.getElementById("panelc");
  const lora = (d.loras||[]).map(l=>l.nombre+" @ "+l.strength).join(", ") || "—";
  c.innerHTML =
    "<h3>" + (d.workflow || "render") + "</h3>" +
    "<img src='" + (IMG[String(i)]||"") + "'>" +
    "<table>" +
    row("fecha", d.fecha) + row("modelo", d.modelo) + row("LoRA", lora) +
    row("seed", d.seed) + row("steps", d.steps) + row("cfg", d.cfg) +
    row("sampler", d.sampler) + row("scheduler", d.scheduler) +
    row("resolución", d.resolucion) + row("archivo", d.archivo) +
    "</table><div id='prompt'>" + (d.prompt || "") + "</div>";
  p.classList.add("on");
  document.getElementById("nav").textContent = (i+1) + " / " + DATOS.length;
  document.querySelectorAll(".nodo").forEach(n => n.classList.toggle("sel", +n.dataset.i === i));
  document.querySelectorAll("#tira img").forEach(n => n.classList.toggle("on", +n.dataset.i === i));
}
function row(k, v) { return "<tr><td>" + k + "</td><td>" + (v ?? "—") + "</td></tr>"; }
document.getElementById("cerrar").addEventListener("click", () =>
  document.getElementById("panel").classList.remove("on"));

// --- Recorrido con teclado -------------------------------------------------
function mover(delta) {
  const vis = visibles(); if (!vis.length) return;
  let pos = vis.indexOf(sel);
  pos = pos < 0 ? 0 : (pos + delta + vis.length) % vis.length;
  seleccionar(vis[pos]);
}
document.getElementById("prev").addEventListener("click", () => mover(-1));
document.getElementById("next").addEventListener("click", () => mover(1));
document.addEventListener("keydown", e => {
  if (e.key === "ArrowRight") mover(1);
  if (e.key === "ArrowLeft") mover(-1);
  if (e.key === "Escape") document.getElementById("panel").classList.remove("on");
});

// --- Filtros y búsqueda ----------------------------------------------------
function construirFiltros() {
  const box = document.getElementById("filtros");
  const wfs = [...new Set(DATOS.map(d => d.workflow || "sin-workflow"))];
  const todos = document.createElement("div");
  todos.className = "chip"; todos.textContent = "todos"; todos.onclick = () => { filtroWf = null; marcar(); };
  box.appendChild(todos);
  wfs.forEach(w => {
    const c = document.createElement("div"); c.className = "chip"; c.dataset.wf = w;
    c.textContent = w; c.onclick = () => { filtroWf = filtroWf === w ? null : w; marcar(); };
    box.appendChild(c);
  });
  const lora = document.createElement("div");
  lora.className = "chip"; lora.textContent = "solo con LoRA";
  lora.onclick = () => { filtroLora = !filtroLora; marcar(); };
  box.appendChild(lora);
}
function marcar() {
  document.querySelectorAll("#filtros .chip").forEach(c => {
    if (c.dataset.wf) c.classList.toggle("on", c.dataset.wf === filtroWf);
    else if (c.textContent === "todos") c.classList.toggle("on", !filtroWf && !filtroLora);
    else c.classList.toggle("on", filtroLora);
  });
  construir();
}
document.getElementById("buscar").addEventListener("input", e => {
  texto = e.target.value.toLowerCase(); construir();
});

// --- Lienzo infinito: pan y zoom ------------------------------------------
let escala = 0.55, tx = 20, ty = 20, arrastrando = false, sx = 0, sy = 0, ox = 0, oy = 0;
const lienzo = document.getElementById("lienzo");
function aplicar() {
  document.getElementById("mundo").style.transform =
    "translate(" + tx + "px," + ty + "px) scale(" + escala + ")";
}
lienzo.addEventListener("mousedown", e => {
  arrastrando = true; sx = e.clientX; sy = e.clientY; ox = tx; oy = ty;
  lienzo.classList.add("arrastrando");
});
window.addEventListener("mousemove", e => {
  if (!arrastrando) return;
  tx = ox + (e.clientX - sx); ty = oy + (e.clientY - sy); aplicar();
});
window.addEventListener("mouseup", () => { arrastrando = false; lienzo.classList.remove("arrastrando"); });
lienzo.addEventListener("wheel", e => {
  e.preventDefault();
  const factor = e.deltaY < 0 ? 1.12 : 1/1.12;
  const nuevo = Math.min(3, Math.max(0.08, escala * factor));
  // zoom centrado en el puntero
  const r = lienzo.getBoundingClientRect();
  const px = e.clientX - r.left, py = e.clientY - r.top;
  tx = px - (px - tx) * (nuevo / escala);
  ty = py - (py - ty) * (nuevo / escala);
  escala = nuevo; aplicar();
}, { passive:false });

construirFiltros(); construir(); aplicar();
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="Genera la galería web de renders")
    ap.add_argument("--indice", default="proyectos/MVP_04-comfyui-arquitectura/INDICE-RENDERS.json",
                    help="JSON del índice (lo produce indice-renders-comfy.py)")
    ap.add_argument("--out", default="activos/web/galeria", help="carpeta del sitio")
    ap.add_argument("--raiz-indice", default=".", help="raiz relativa de las rutas del índice")
    args = ap.parse_args()

    with open(args.indice, encoding="utf-8") as f:
        filas = json.load(f)

    # Normalizamos: el índice guarda los LoRAs como lista de dicts; la galería
    # quiere además un color estable por seed para leer los grupos de un vistazo.
    for i, d in enumerate(filas):
        d["hsl"] = tono_de(d.get("seed"))

    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    mapa = copiar_imagenes(filas, os.path.abspath(args.raiz_indice), os.path.join(out, "img"))

    # Quitamos las filas cuya imagen no se encontró (no render links rotos).
    validas = []
    mapa_ok = {}
    for i, d in enumerate(filas):
        clave = str(i)
        if clave in mapa:
            validas.append(d)
            mapa_ok[str(len(validas) - 1)] = mapa[clave]

    html = (HTML
            .replace("__DATOS__", json.dumps(validas, ensure_ascii=False))
            .replace("__IMG__", json.dumps(mapa_ok, ensure_ascii=False)))
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(out, "datos.json"), "w", encoding="utf-8") as f:
        json.dump(validas, f, indent=2, ensure_ascii=False)

    tam = sum(os.path.getsize(os.path.join(out, "img", n)) for n in os.listdir(os.path.join(out, "img")))
    print("Galería generada: %s" % out)
    print("  renders: %d | workflows: %d | imágenes: %.1f MB" %
          (len(validas), len({d["workflow"] for d in validas}), tam / 1048576))
    print("  abrir: %s" % os.path.join(out, "index.html"))
    print("  generado: %s" % datetime.now().strftime("%Y-%m-%d %H:%M"))


if __name__ == "__main__":
    main()
