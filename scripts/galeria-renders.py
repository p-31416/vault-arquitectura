#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
galeria-renders.py — genera un sitio web para recorrer y comparar los renders.

Qué hace, en una frase:
    Escanea los PNG que ComfyUI escribe, lee la metadata que el propio ComfyUI
    graba dentro de cada archivo (el grafo completo) y arma una galería web con
    dos vistas (mosaico y lienzo infinito), agrupación por ejes, facetas filtrables,
    pantalla completa tipo Polaroid y actualización automática.

Por qué existe:
    Los renders traen la trazabilidad DENTRO del PNG: dos bloques tEXt ('prompt'
    y 'workflow') con el grafo en formato API. Eso ya está guardado; lo que faltaba
    era la capa de LECTURA: ver las imágenes, compararlas, recorrerlas y llegar con
    un clic a la de al lado. Un tablero tipo Miro no sirve para eso (hay que hacer
    zoom out cientos de veces para recorrerlo); una tabla tampoco (hay que abrir
    dos archivos y comparar de memoria).

Modos de uso:
    1) Generar el sitio (una vez):
         python scripts\\galeria-renders.py --dir "P:\\00-repos\\ComfyUI\\output"
    2) Generar + servir + actualizar solo (recomendado mientras se renderiza):
         python scripts\\galeria-renders.py --dir "P:\\00-repos\\ComfyUI\\output" --serve 8890
    En el modo --serve, cada PNG nuevo regenera el sitio y las pestañas abiertas
    se recargan solas (el sitio sondea datos.json y compara la versión).

Lo que NO hace:
    No publica nada en internet. Servir en localhost es distinto de publicar en
    un dominio: esa decisión (y sus reglas de privacidad) es de otra sección.

Salida:
    <out>/index.html   ← el sitio (HTML+CSS+JS en un archivo, sin dependencias)
    <out>/datos.json   ← los datos + la versión (para el sondeo de actualización)
    <out>/img/         ← las imágenes

Notas:
    la explicación línea por línea está en scripts/galeria-renders_notas.md
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
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# --- Dónde vive el indexador (se reusa, no se duplica) ----------------------
# NOTA ES: el indexador ya sabe leer los bloques tEXt de un PNG y deducir
# modelo/LoRA/seed/steps/cfg. Importarlo evita tener dos versiones de esa
# lógica (que es donde se cuelan los errores).
INDEXADOR = Path(__file__).with_name("indice-renders-comfy.py")


def cargar_indexador():
    """Carga indice-renders-comfy.py como módulo (el nombre tiene guiones)."""
    spec = importlib.util.spec_from_file_location("indice_renders", INDEXADOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# --- Clasificación del render ------------------------------------------------
# NOTA ES: el tipo se deduce de las clases de nodo que aparecen en el grafo.
# Es una heurística honesta: no pretende saber qué hizo el operador, sino qué
# clase de flujo se ejecutó.
def tipo_de(grafo):
    """Clasifica el render a partir de los class_type presentes en el grafo."""
    clases = {n.get("class_type") for n in grafo.values() if isinstance(n, dict)}
    tiene = lambda *cs: bool(clases & set(cs))  # noqa: E731
    if tiene("Hunyuan3D", "Hunyuan3Dv2", "Tripo", "Meshy", "TRELLIS"):
        return "3d"
    if tiene("VHS_VideoCombine", "AnimateDiff", "LTXVConditioning", "LTXVImgToVideo"):
        return "video"
    if tiene("InpaintModelLoader", "InpaintModelConditioning", "ImageInpaint"):
        return "inpaint"
    if tiene("Flux2Scheduler", "FluxKontextMultiReferenceLatentMethod", "SamplerCustomAdvanced"):
        return "dit"
    if tiene("ControlNetApplyAdvanced", "ControlNetApply", "ACN_AdvancedControlNetApply"):
        return "controlnet"
    if tiene("VAEEncode") and tiene("LoadImage"):
        return "img2img"
    if tiene("EmptyLatentImage", "EmptyFlux2LatentImage", "EmptySD3LatentImage"):
        return "txt2img"
    return "otro"


def base_de(modelo, loras):
    """La familia de modelo base: de ahí depende qué se puede hacer local."""
    n = (modelo or "").lower()
    if "juggernaut" in n or "xl" in n and "sd" in n:
        return "SDXL"
    if "flux" in n or "klein" in n or "flux2" in n:
        return "FLUX"
    if "v1-5" in n or "v15" in n or "1.5" in n or "realmix" in n:
        return "SD 1.5"
    if loras:
        return "LoRA"
    return "—"


def slug(texto, maximo=60):
    """Convierte un texto en un nombre de archivo seguro (sin acentos ni espacios)."""
    if not texto:
        return "sin-nombre"
    limpio = "".join(c if c.isalnum() or c in "-_." else "-" for c in str(texto))
    return limpio.strip("-")[:maximo] or "sin-nombre"


def tono_de(semilla):
    """Color estable a partir de una seed: el mismo seed siempre mismo color."""
    # NOTA ES: hashlib es estable entre máquinas y versiones (a diferencia de hash()).
    digest = hashlib.md5(str(semilla).encode("utf-8")).hexdigest()
    return int(digest[:6], 16) % 360


def escanear(origenes, indexador, raiz_manual):
    """Recorre las carpetas de renders y arma una fila por PNG."""
    filas = []
    for carpeta in origenes:
        if not os.path.isdir(carpeta):
            print("No existe la carpeta:", carpeta)
            continue
        for raiz, _, archivos in os.walk(carpeta):
            for nombre in sorted(archivos):
                if not nombre.lower().endswith(".png"):
                    continue
                ruta = os.path.join(raiz, nombre)
                try:
                    fila = indexador.fila_de(ruta, carpeta)
                except Exception as exc:  # noqa: BLE001
                    print("  (!) no se pudo leer", ruta, exc)
                    continue
                textos = indexador.leer_textos_png(ruta)
                grafo = {}
                if "prompt" in textos:
                    try:
                        grafo = json.loads(textos["prompt"])
                    except Exception:
                        grafo = {}
                loras = [l["nombre"] for l in fila.get("loras") or []]
                fila["tipo"] = tipo_de(grafo)
                fila["base"] = base_de(fila.get("modelo"), loras)
                fila["clases"] = sorted({n.get("class_type") for n in grafo.values()
                                         if isinstance(n, dict) and n.get("class_type")})
                fila["hsl"] = tono_de(fila.get("seed"))
                filas.append(fila)
    filas.sort(key=lambda f: (f.get("fecha") or "", f.get("archivo") or ""))
    return filas


def aplicar_tags_manuales(filas, archivo_tags):
    """Suma las etiquetas que el equipo asignó a mano (archivo JSON opcional)."""
    if not archivo_tags or not os.path.isfile(archivo_tags):
        return
    with open(archivo_tags, encoding="utf-8") as f:
        manual = json.load(f)
    for fila in filas:
        clave = os.path.basename(fila["archivo"])
        extra = manual.get(clave) or manual.get(fila["archivo"]) or {}
        for eje, valores in extra.items():
            fila.setdefault("tags", {}).setdefault(eje, [])
            for v in (valores if isinstance(valores, list) else [valores]):
                if v not in fila["tags"][eje]:
                    fila["tags"][eje].append(v)


# --- La plantilla HTML --------------------------------------------------------
HTML = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Galería de renders · estudio</title>
<style>
  :root {
    --fondo:#0d0f12; --panel:#16191f; --linea:#262b33; --texto:#e6e9ef;
    --tenue:#8d95a3; --acento:#7fd1c1; --sombra:0 10px 40px rgba(0,0,0,.55);
  }
  * { box-sizing:border-box; }
  html,body { margin:0; height:100%; background:var(--fondo); color:var(--texto);
    font:13px/1.45 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }
  button { font:inherit; color:inherit; }

  /* ---------- barra superior ---------- */
  #barra { position:fixed; inset:0 0 auto 0; height:52px; display:flex; gap:10px; align-items:center;
           padding:0 12px; background:rgba(13,15,18,.94); border-bottom:1px solid var(--linea);
           z-index:60; backdrop-filter:blur(8px); }
  #titulo { font-weight:600; }
  #stats { color:var(--tenue); white-space:nowrap; }
  input[type=search] { background:var(--panel); border:1px solid var(--linea); color:var(--texto);
                       border-radius:6px; padding:6px 9px; width:200px; }
  select { background:var(--panel); border:1px solid var(--linea); color:var(--texto);
           border-radius:6px; padding:5px 8px; }
  .btn { background:var(--panel); border:1px solid var(--linea); color:var(--texto);
         border-radius:6px; padding:5px 9px; cursor:pointer; line-height:1; }
  .btn:hover { border-color:var(--acento); color:var(--acento); }
  .btn.activo { border-color:var(--acento); color:var(--acento); }
  #zoombox { display:flex; gap:4px; align-items:center; }
  #zoombox .btn { min-width:30px; text-align:center; font-size:15px; padding:5px 7px; }
  #facetas { position:fixed; top:52px; left:0; bottom:0; width:210px; overflow:auto;
             border-right:1px solid var(--linea); background:var(--panel); padding:10px; z-index:40; }
  #facetas.oculto { display:none; }
  .fgrupo { margin-bottom:14px; }
  .fgrupo h3 { margin:0 0 6px; font-size:11px; text-transform:uppercase; letter-spacing:.6px; color:var(--tenue); }
  .fchip { display:flex; justify-content:space-between; gap:8px; width:100%; text-align:left;
           background:transparent; border:1px solid transparent; border-radius:6px; padding:4px 7px;
           cursor:pointer; color:var(--texto); }
  .fchip:hover { background:#1c2028; }
  .fchip.on { border-color:var(--acento); color:var(--acento); }
  .fchip .n { color:var(--tenue); font-size:11px; }
  #contenido { position:fixed; top:52px; left:210px; right:0; bottom:0; overflow:auto; }
  #contenido.lienzo { overflow:hidden; cursor:grab; background:
      radial-gradient(circle at 1px 1px,#1c2028 1px,transparent 0) 0 0/28px 28px; }
  #contenido.lienzo.arrastrando { cursor:grabbing; }

  /* ---------- mosaico ---------- */
  #mosaico { display:grid; grid-template-columns:repeat(auto-fill,minmax(210px,1fr)); gap:12px; padding:14px; }
  .seccion { grid-column:1/-1; margin:10px 0 2px; font-size:11px; text-transform:uppercase;
             letter-spacing:.7px; color:var(--tenue); display:flex; gap:10px; align-items:baseline; }
  .seccion b { color:var(--texto); font-size:13px; letter-spacing:0; text-transform:none; }
  .tarjeta { position:relative; border:1px solid var(--linea); border-radius:8px; overflow:hidden;
             background:var(--panel); cursor:pointer; }
  .tarjeta img { display:block; width:100%; height:auto; }
  .tarjeta .pie { padding:7px 9px; display:flex; justify-content:space-between; gap:8px;
                  font-size:11px; color:var(--tenue); }
  .badge { position:absolute; left:6px; top:6px; font-size:10px; padding:2px 6px; border-radius:4px;
           background:rgba(0,0,0,.62); color:#fff; }
  .pills { position:absolute; right:6px; bottom:6px; display:flex; gap:4px; }
  .pill { font-size:10px; padding:2px 6px; border-radius:4px; background:rgba(0,0,0,.62); color:#ddd; }

  /* ---------- lienzo infinito ---------- */
  #mundo { position:absolute; top:0; left:0; transform-origin:0 0; will-change:transform; }
  .col { position:absolute; }
  .colh { color:var(--tenue); font-size:11px; text-transform:uppercase; letter-spacing:.6px;
          margin:0 0 8px 2px; max-width:230px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
  .nodo { position:relative; margin-bottom:10px; border-radius:6px; overflow:hidden;
          border:1px solid var(--linea); background:var(--panel); cursor:pointer; }
  .nodo img { display:block; width:100%; height:auto; }

  /* ---------- pantalla completa (Polaroid) ---------- */
  #full { position:fixed; inset:0; background:rgba(6,7,9,.96); z-index:80; display:none;
          overflow:auto; padding:26px 20px 40px; }
  #full.on { display:block; }
  #polaroid { max-width:min(1100px, 92vw); margin:0 auto; background:#fbfbf8; color:#15171b;
              border-radius:3px; padding:16px 16px 0; box-shadow:var(--sombra); }
  #polaroid img { display:block; width:100%; height:auto; border-radius:2px; }
  #pie-polaroid { padding:14px 6px 18px; }
  #pie-polaroid h2 { margin:0 0 4px; font-size:19px; color:#15171b; }
  #pie-polaroid .meta { color:#5a6070; font-size:12.5px; margin-bottom:12px; }
  #pie-polaroid .meta span { display:inline-block; margin-right:14px; }
  #prompt-box { background:#f1f0ea; border:1px solid #ddd9cd; border-radius:4px; padding:11px 13px;
                white-space:pre-wrap; word-break:break-word; font-size:12.5px; color:#262a33;
                max-height:34vh; overflow:auto; }
  #prompt-box b { color:#15171b; }
  #cerrar-full { position:fixed; right:18px; top:14px; z-index:90; }
  #navfull { position:fixed; left:50%; transform:translateX(-50%); bottom:14px; display:flex; gap:8px;
             align-items:center; background:var(--panel); border:1px solid var(--linea);
             border-radius:999px; padding:6px 12px; z-index:90; }
  #navfull .btn { border-radius:999px; }
  #mini { position:fixed; right:18px; bottom:14px; display:flex; gap:4px; z-index:90;
          background:var(--panel); border:1px solid var(--linea); border-radius:8px; padding:6px; }
  #mini img { width:46px; height:46px; object-fit:cover; border:1px solid var(--linea);
              border-radius:4px; cursor:pointer; opacity:.55; }
  #mini img.on { opacity:1; border-color:var(--acento); }
  #toast { position:fixed; bottom:18px; left:50%; transform:translateX(-50%); background:var(--panel);
           border:1px solid var(--acento); color:var(--acento); border-radius:6px; padding:6px 12px;
           z-index:95; display:none; }
  #vivo { color:var(--acento); font-size:11px; }
  #vivo.pausa { color:var(--tenue); }
</style>
</head>
<body>
<div id="barra">
  <span id="titulo">Galería de renders</span>
  <span id="stats"></span>
  <span id="vivo">● en vivo</span>
  <input type="search" id="buscar" placeholder="buscar en el prompt…">
  <select id="agrupar" title="Agrupar por">
    <option value="workflow">Agrupar: workflow</option>
    <option value="base">Agrupar: base del modelo</option>
    <option value="modelo">Agrupar: modelo</option>
    <option value="lora">Agrupar: LoRA</option>
    <option value="tipo">Agrupar: tipo de flujo</option>
    <option value="tags">Agrupar: etiqueta manual</option>
    <option value="fecha">Agrupar: fecha</option>
    <option value="seed">Agrupar: seed</option>
  </select>
  <button class="btn" id="m-lienzo" title="Vista de lienzo infinito">Lienzo</button>
  <button class="btn activo" id="m-mosaico" title="Vista de mosaico">Mosaico</button>
  <div id="zoombox">
    <button class="btn" id="z-out" title="Alejar">−</button>
    <button class="btn" id="z-in" title="Acercar">+</button>
    <button class="btn" id="z-fit" title="Ver todo">⤢</button>
    <button class="btn" id="z-100" title="Tamaño real">1:1</button>
  </div>
  <button class="btn" id="f-toggle" title="Mostrar u ocultar filtros">Filtros</button>
</div>
<div id="facetas"></div>
<div id="contenido"><div id="mosaico"></div><div id="lienzo"><div id="mundo"></div></div></div>

<div id="full">
  <button class="btn" id="cerrar-full">cerrar ✕</button>
  <div id="polaroid">
    <img id="p-img" alt="">
    <div id="pie-polaroid">
      <h2 id="p-titulo"></h2>
      <div class="meta" id="p-meta"></div>
      <div id="prompt-box"></div>
    </div>
  </div>
</div>
<div id="navfull">
  <button class="btn" id="f-prev">◀ anterior</button>
  <span id="f-nav"></span>
  <button class="btn" id="f-next">siguiente ▶</button>
</div>
<div id="mini"></div>
<div id="toast"></div>

<script>
const DATOS = __DATOS__;
const IMG = __IMG__;
const VERSION = __VERSION__;
const EJES = ["base","modelo","lora","tipo","workflow","tags"];

let state = { q:"", facetas:{}, agrupar:"workflow", vista:"mosaico" };
let visibles = [], sel = -1;

// ---------------------------------------------------------------- utilidades
function esc(s){ return String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c])); }
function etq(render){ return Object.entries(render.tags||{}).flatMap(([e,v]) => (v||[]).map(x => e+":"+x)); }

// NOTA ES: normaliza un eje a LISTA. En la galería conviven campos de texto
// (workflow, base, modelo, tipo), la lista de LoRAs (loras: [{nombre, strength}])
// y las etiquetas manuales (tags: {eje: [valores]}). Sin esta normalización, un
// texto no tiene .forEach y el dibujado se rompe entero.
function listaDe(render, eje){
  if (eje === "lora") return (render.loras||[]).map(l => l.nombre);
  if (eje === "tags") return Object.values(render.tags||{}).flat();
  const v = render[eje];
  if (v === undefined || v === null) return [];
  return Array.isArray(v) ? v : [v];
}
function valsDe(eje){
  const m = new Map();
  visibles.forEach(r => { listaDe(r, eje).forEach(v => m.set(v, (m.get(v)||0)+1)); });
  return [...m.entries()].sort((a,b)=>b[1]-a[1]||String(a[0]).localeCompare(String(b[0])));
}
function coincide(r){
  if (state.q){
    const hay = [r.prompt, r.workflow, r.modelo, (r.loras||[]).map(l=>l.nombre).join(" "),
                 etq(r).join(" ")].join(" ").toLowerCase();
    if (!hay.includes(state.q.toLowerCase())) return false;
  }
  for (const [eje, sel] of Object.entries(state.facetas)){
    if (!sel || !sel.length) continue;
    const tiene = listaDe(r, eje);
    if (!sel.some(v => tiene.includes(v))) return false;
  }
  return true;
}

// ------------------------------------------------------------------ facetas
function pintarFacetas(){
  const html = EJES.map(eje => {
    const vals = valsDe(eje);
    if (!vals.length) return "";
    const sel = state.facetas[eje] || [];
    return `<div class="fgrupo"><h3>${esc(eje)}</h3>` + vals.map(([v,n]) => {
      const on = sel.includes(v);
      const nombre = eje === "lora" ? String(v).replace(/\.safetensors$/,"") : v;
      return `<button class="fchip ${on?"on":""}" data-eje="${esc(eje)}" data-v="${esc(v)}">
        <span>${esc(nombre)}</span><span class="n">${n}</span></button>`;
    }).join("") + `</div>`;
  }).join("");
  document.getElementById("facetas").innerHTML = html;
  document.querySelectorAll(".fchip").forEach(b => b.onclick = () => {
    const eje = b.dataset.eje, v = b.dataset.v;
    const cur = state.facetas[eje] = state.facetas[eje] || [];
    const i = cur.indexOf(v);
    if (i >= 0) cur.splice(i,1); else cur.push(v);
    pintar();
  });
}

// ------------------------------------------------------------------- mosaico
function seccionDe(r){
  switch (state.agrupar){
    case "base": return r.base || "—";
    case "modelo": return (r.modelo||"—").replace(/\.safetensors$/,"");
    case "lora": return (r.loras && r.loras.length) ? r.loras.map(l=>l.nombre.replace(/\.safetensors$/,"")).join(" + ") : "sin LoRA";
    case "tipo": return r.tipo || "—";
    case "tags": return (etq(r)[0] || "sin etiqueta").split(":").slice(1).join(":") || "sin etiqueta";
    case "fecha": return (r.fecha||"").slice(0,10) || "—";
    case "seed": return "seed " + (r.seed ?? "—");
    default: return r.workflow || "sin workflow";
  }
}
function pintarMosaico(){
  const m = document.getElementById("mosaico");
  m.innerHTML = "";
  const grupos = new Map();
  visibles.forEach((r,i) => { const k = seccionDe(r); if(!grupos.has(k)) grupos.set(k,[]); grupos.get(k).push(i); });
  [...grupos.entries()].sort((a,b)=>b[1].length-a[1].length).forEach(([k, idxs]) => {
    const h = document.createElement("div"); h.className = "seccion";
    h.innerHTML = `<b>${esc(k)}</b><span>${idxs.length}</span>`; m.appendChild(h);
    idxs.forEach(i => {
      const r = visibles[i];
      const art = document.createElement("article"); art.className = "tarjeta";
      const img = document.createElement("img");
      img.src = IMG[String(r.__i)] || ""; img.loading = "lazy"; img.alt = (r.prompt||"").slice(0,80);
      const b = document.createElement("div"); b.className = "badge";
      b.textContent = "seed " + (r.seed ?? "—");
      b.style.background = `hsla(${r.hsl},55%,45%,.85)`;
      const pills = document.createElement("div"); pills.className = "pills";
      (r.loras||[]).slice(0,1).forEach(l => {
        const p = document.createElement("span"); p.className="pill";
        p.textContent = l.nombre.replace(/\.safetensors$/,""); pills.appendChild(p);
      });
      if (!r.loras || !r.loras.length) {
        const p = document.createElement("span"); p.className="pill"; p.textContent = r.tipo || ""; pills.appendChild(p);
      }
      const pie = document.createElement("div"); pie.className="pie";
      pie.innerHTML = `<span>${esc((r.workflow||"render").slice(0,26))}</span><span>${esc(r.resolucion||"")}</span>`;
      art.appendChild(img); art.appendChild(b); art.appendChild(pills); art.appendChild(pie);
      art.onclick = () => abrir(i);
      m.appendChild(art);
    });
  });
}

// -------------------------------------------------------------------- lienzo
function pintarLienzo(){
  const mundo = document.getElementById("mundo"); mundo.innerHTML = "";
  const grupos = new Map();
  visibles.forEach((r,i) => { const k = seccionDe(r); if(!grupos.has(k)) grupos.set(k,[]); grupos.set(k,(grupos.get(k)||[]).concat(i)); });
  let x = 40;
  [...grupos.entries()].sort((a,b)=>b[1].length-a[1].length).forEach(([k, idxs]) => {
    const col = document.createElement("div"); col.className="col"; col.style.left = x+"px";
    const h = document.createElement("div"); h.className="colh"; h.textContent = k + " · " + idxs.length;
    col.appendChild(h);
    idxs.forEach(i => {
      const r = visibles[i];
      const n = document.createElement("div"); n.className="nodo"; n.style.width="230px";
      const img = document.createElement("img"); img.src = IMG[String(r.__i)]||""; img.loading="lazy";
      const b = document.createElement("div"); b.className="badge"; b.textContent="seed "+(r.seed??"—");
      b.style.background = `hsla(${r.hsl},55%,45%,.85)`;
      n.appendChild(img); n.appendChild(b);
      n.onclick = () => abrir(i);
      col.appendChild(n);
    });
    mundo.appendChild(col); x += 250;
  });
  aplicarZoom();
}

// ------------------------------------------------------------------- zoom
let escala = 1, tx = 0, ty = 0;
function aplicarZoom(){
  document.getElementById("mundo").style.transform = `translate(${tx}px,${ty}px) scale(${escala})`;
}
function zoom(factor, px, py){
  const c = document.getElementById("contenido").getBoundingClientRect();
  px = px ?? (c.width/2); py = py ?? (c.height/2);
  const nuevo = Math.min(3, Math.max(0.08, escala*factor));
  tx = px - (px - tx)*(nuevo/escala); ty = py - (py - ty)*(nuevo/escala);
  escala = nuevo; aplicarZoom();
}
function zoomAjustar(){
  const mundo = document.getElementById("mundo");
  escala = 1; tx = 0; ty = 0; aplicarZoom();
  const c = document.getElementById("contenido").getBoundingClientRect();
  const w = mundo.scrollWidth, h = mundo.scrollHeight;
  if (w && h){ escala = Math.min(1, (c.width-40)/w, (c.height-40)/h); tx = 20; ty = 20; aplicarZoom(); }
}
document.getElementById("z-in").onclick  = () => zoom(1.25);
document.getElementById("z-out").onclick = () => zoom(1/1.25);
document.getElementById("z-100").onclick = () => { escala = 1; tx = 0; ty = 0; aplicarZoom(); };
document.getElementById("z-fit").onclick = () => zoomAjustar();
const lienzo = document.getElementById("lienzo");
lienzo.addEventListener("wheel", e => { e.preventDefault(); const r = lienzo.getBoundingClientRect();
  zoom(e.deltaY<0?1.12:1/1.12, e.clientX-r.left, e.clientY-r.top); }, {passive:false});
let arrastrando=false, sx=0, sy=0, ox=0, oy=0;
lienzo.addEventListener("mousedown", e => { arrastrando=true; sx=e.clientX; sy=e.clientY; ox=tx; oy=ty;
  lienzo.classList.add("arrastrando"); });
window.addEventListener("mousemove", e => { if(!arrastrando) return;
  tx = ox+(e.clientX-sx); ty = oy+(e.clientY-sy); aplicarZoom(); });
window.addEventListener("mouseup", () => { arrastrando=false; lienzo.classList.remove("arrastrando"); });

// ------------------------------------------------------- pantalla completa
function abrir(i){
  sel = i; const r = visibles[i];
  document.getElementById("p-img").src = IMG[String(r.__i)] || "";
  document.getElementById("p-titulo").textContent = r.workflow || "render";
  const lora = (r.loras||[]).map(l => l.nombre.replace(/\.safetensors$/,"") + " @ " + l.strength).join(", ") || "—";
  document.getElementById("p-meta").innerHTML = [
    ["modelo", (r.modelo||"—").replace(/\.safetensors$/,"")], ["LoRA", lora],
    ["seed", r.seed], ["steps", r.steps], ["cfg", r.cfg], ["sampler", r.sampler],
    ["scheduler", r.scheduler], ["resolución", r.resolucion], ["tipo", r.tipo],
    ["fecha", r.fecha],
  ].map(([k,v]) => `<span><b>${esc(k)}:</b> ${esc(v ?? "—")}</span>`).join("");
  document.getElementById("prompt-box").innerHTML = `<b>PROMPT</b>\n${esc(r.prompt||"(sin prompt)")}`;
  document.getElementById("full").classList.add("on");
  document.getElementById("f-nav").textContent = (i+1)+" / "+visibles.length;
  const mini = document.getElementById("mini");
  mini.innerHTML = "";
  visibles.slice(Math.max(0,i-3), i+4).forEach((rr, k) => {
    const idx = Math.max(0,i-3)+k; const im = document.createElement("img");
    im.src = IMG[String(rr.__i)]||""; im.className = (idx===i?"on":"");
    im.onclick = () => abrir(idx); mini.appendChild(im);
  });
  window.scrollTo(0,0);
}
function mover(d){
  if (sel < 0) return;
  const n = (sel + d + visibles.length) % visibles.length;
  abrir(n);
}
document.getElementById("f-next").onclick = () => mover(1);
document.getElementById("f-prev").onclick = () => mover(-1);
document.getElementById("cerrar-full").onclick = () => document.getElementById("full").classList.remove("on");
document.getElementById("full").addEventListener("click", e => {
  if (e.target.id === "full") document.getElementById("full").classList.remove("on");
});
document.addEventListener("keydown", e => {
  const abierto = document.getElementById("full").classList.contains("on");
  if (e.key === "ArrowRight") { e.preventDefault(); mover(1); }
  else if (e.key === "ArrowLeft") { e.preventDefault(); mover(-1); }
  else if (e.key === "Escape") document.getElementById("full").classList.remove("on");
  else if (!abierto && (e.key === "+" || e.key === "=")) zoom(1.25);
  else if (!abierto && e.key === "-") zoom(1/1.25);
});

// ------------------------------------------------------------------ pintado
function pintar(){
  visibles = DATOS.filter(coincide);
  visibles.forEach((r,i) => r.__i = i);
  document.getElementById("stats").textContent =
    `${visibles.length} de ${DATOS.length} renders`;
  pintarFacetas();
  if (state.vista === "mosaico") pintarMosaico(); else pintarLienzo();
}
document.getElementById("buscar").oninput = e => { state.q = e.target.value; pintar(); };
document.getElementById("agrupar").onchange = e => { state.agrupar = e.target.value; pintar(); };
document.getElementById("m-mosaico").onclick = () => {
  state.vista = "mosaico";
  document.getElementById("m-mosaico").classList.add("activo");
  document.getElementById("m-lienzo").classList.remove("activo");
  document.getElementById("mosaico").style.display = "grid";
  document.getElementById("lienzo").style.display = "none";
  document.getElementById("contenido").classList.remove("lienzo");
  pintar();
};
document.getElementById("m-lienzo").onclick = () => {
  state.vista = "lienzo";
  document.getElementById("m-lienzo").classList.add("activo");
  document.getElementById("m-mosaico").classList.remove("activo");
  document.getElementById("mosaico").style.display = "none";
  document.getElementById("lienzo").style.display = "block";
  document.getElementById("contenido").classList.add("lienzo");
  pintar(); zoomAjustar();
};
document.getElementById("f-toggle").onclick = () =>
  document.getElementById("facetas").classList.toggle("oculto");

pintar();

// ------------------------------------------------- actualización automática
async function sondear(){
  try {
    const r = await fetch("datos.json?t=" + Date.now(), {cache:"no-store"});
    if (!r.ok) return;
    const j = await r.json();
    if (j.version && j.version !== VERSION) {
      location.reload();
    }
  } catch(e) { /* file:// no permite fetch: la actualización automática necesita --serve */ }
}
setInterval(sondear, 12000);
</script>
</body>
</html>
"""


# --- Generación ----------------------------------------------------------------
def copiar_y_generar(filas, out, indexador, origenes):
    """Copia las imágenes y escribe el sitio. Devuelve la versión (sello de tiempo)."""
    img_dir = os.path.join(out, "img")
    if os.path.isdir(img_dir):
        shutil.rmtree(img_dir)
    os.makedirs(img_dir, exist_ok=True)

    datos = []
    mapa = {}
    for i, f in enumerate(filas):
        # la ruta del índice es relativa a la carpeta indexada
        origen = None
        for carpeta in origenes:
            cand = os.path.join(carpeta, f["archivo"])
            if os.path.isfile(cand):
                origen = cand
                break
        if origen is None:
            cand = f.get("abs_archivo")
            origen = cand if cand and os.path.isfile(cand) else None
        if origen is None:
            continue
        nombre = "%03d_%s.png" % (i, slug(f.get("workflow") or os.path.basename(f["archivo"])))
        shutil.copy2(origen, os.path.join(img_dir, nombre))
        mapa[str(len(datos))] = "img/" + nombre
        datos.append(f)

    version = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    workflows = len({f.get("workflow") for f in datos})
    html = (HTML
            .replace("__DATOS__", json.dumps(datos, ensure_ascii=False))
            .replace("__IMG__", json.dumps(mapa, ensure_ascii=False))
            .replace("__VERSION__", json.dumps(version)))
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(out, "datos.json"), "w", encoding="utf-8") as f:
        json.dump({"version": version, "items": datos}, f, indent=2, ensure_ascii=False)
    return version, len(datos), workflows


def firma(origenes):
    """Huella del contenido de las carpetas de renders (para detectar cambios)."""
    partes = []
    for carpeta in origenes:
        if not os.path.isdir(carpeta):
            continue
        for raiz, _, archivos in os.walk(carpeta):
            for n in sorted(archivos):
                if n.lower().endswith(".png"):
                    p = os.path.join(raiz, n)
                    partes.append("%s:%d" % (p, os.stat(p).st_mtime_ns))
    return hashlib.md5("|".join(partes).encode("utf-8")).hexdigest()


def servir(out, puerto):
    """Sirve la carpeta del sitio por HTTP (necesario para la actualización automática).

    NOTA ES: `directory=` hay que pasarlo en la CONSTRUCTOR del handler, no como
    atributo de clase: `SimpleHTTPRequestHandler.__init__` recibe `directory=None`
    y, si viene None, se queda con os.getcwd() — el atributo de clase queda
    tapado y el servidor termina sirviendo otra carpeta (404 en todo).
    """
    class Handler(SimpleHTTPRequestHandler):
        def log_message(self, *args, **kwargs):  # silencia el log por request
            pass

    handler = functools.partial(Handler, directory=out)
    httpd = ThreadingHTTPServer(("127.0.0.1", puerto), handler)
    print("Galería en http://127.0.0.1:%d/index.html" % puerto, flush=True)
    httpd.serve_forever()


def main():
    ap = argparse.ArgumentParser(description="Genera la galería web de renders")
    ap.add_argument("--dir", action="append", default=[],
                    help="carpeta de renders (repetible). Ej: P:\\00-repos\\ComfyUI\\output")
    ap.add_argument("--indice", help="usar un índice JSON ya hecho en vez de escanear")
    ap.add_argument("--out", default="activos/web/galeria", help="carpeta del sitio")
    ap.add_argument("--tags", default="activos/web/galeria/tags.json",
                    help="etiquetas manuales (JSON: {archivo: {eje: [valores]}})")
    ap.add_argument("--serve", type=int, metavar="PUERTO",
                    help="servir en localhost y actualizar solo cuando cambien los renders")
    ap.add_argument("--una-vez", action="store_true", help="con --serve: generar y salir")
    args = ap.parse_args()

    indexador = cargar_indexador()
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    origenes = [os.path.abspath(d) for d in args.dir]

    def una_pasada():
        if args.indice:
            with open(args.indice, encoding="utf-8") as f:
                raw = json.load(f)
            filas = raw["items"] if isinstance(raw, dict) else raw
        else:
            filas = escanear(origenes, indexador, args.tags)
        # el indexador guarda rutas relativas a la carpeta indexada; guardamos la absoluta
        for f in filas:
            for carpeta in origenes:
                cand = os.path.join(carpeta, f["archivo"])
                if os.path.isfile(cand):
                    f["abs_archivo"] = cand
                    break
        aplicar_tags_manuales(filas, args.tags)
        return copiar_y_generar(filas, out, indexador, origenes)

    version, n, n_wf = una_pasada()
    print("Galería generada: %s" % out)
    print("  renders: %d | workflows: %d | versión: %s" % (n, n_wf, version))

    if not args.serve:
        print("  abrir: %s" % os.path.join(out, "index.html"))
        return 0

    if args.una_vez:
        return 0

    # Modo servidor: vigila las carpetas y regenera cuando aparece un render nuevo.
    hilo = threading.Thread(target=servir, args=(out, args.serve), daemon=True)
    hilo.start()
    print("  vigilando cambios… (Ctrl+C para salir)")
    ultima = firma(origenes)
    try:
        while True:
            time.sleep(15)
            actual = firma(origenes)
            if actual != ultima:
                ultima = actual
                v, n, _ = una_pasada()
                print("  [%s] %d renders (actualizado)" % (v, n), flush=True)
    except KeyboardInterrupt:
        print("  cerrado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
