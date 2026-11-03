#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
dashboard-concurso.py — tablero polaroid SOLO de las corridas del concurso.

Qué hace, en una frase:
    Toma las imágenes del concurso que ya están en el vault, les cruza el
    tiempo real de generación leyéndolo de /history de ComfyUI, y escribe un
    HTML autocontenido con vista de mosaico y vista polaroid (clic = grande).

Por qué existe:
    galeria-renders.py muestra TODO el output de ComfyUI y no sabe de tiempos.
    dashboard-curso.py es el del curso (SD 1.5, matriz M01-M20). Faltaba una
    vista chica y enfocada: solo las imágenes del concurso, con modelo y
    segundos medidos, para decidir sin ruido.

Cómo se usa:
    python scripts\\dashboard-concurso.py
    python scripts\\dashboard-concurso.py --out activos/web/concurso --comfy http://127.0.0.1:8188
    python scripts\\dashboard-concurso.py --embebido proyectos/STUDIO_OS-Emilia/presentacion/dashboard-concurso.html

Salida:
    activos/web/concurso/index.html   (HTML + CSS + JS en un solo archivo)
    activos/web/concurso/datos.json   (los datos, por si se quieren reusar)
    activos/web/concurso/img/         (copia de los PNG, sin reescalar)
    Con --embebido: un solo HTML autocontenido (miniaturas base64) en la ruta
    pedida, listo para compartir y commitear.
"""

# NOTA ES: argparse = leer opciones de la línea de comandos sin if/else manual.
import argparse
# NOTA ES: base64 = embeber la miniatura dentro del HTML (vista para compartir).
import base64
# NOTA ES: io.BytesIO = guardar el JPEG en memoria sin archivo temporal.
import io
# NOTA ES: json = escribir y leer datos estructurados (el datos.json y el embed).
import json
# NOTA ES: os.path = armar rutas de archivos de forma portable (join, dirname).
import os
# NOTA ES: shutil.copy2 = copiar un archivo conservando fecha y permisos.
import shutil
# NOTA ES: struct.unpack = leer bytes binarios como números (cabecera del PNG).
import struct
# NOTA ES: urllib.request = pedir una URL por HTTP sin instalar nada extra.
import urllib.request
from datetime import datetime

# --- Qué se muestra -----------------------------------------------------------
# NOTA ES: cada entrada es una imagen del concurso. "prompt_id" es el id que
# NOTA ES: devolvió ComfyUI al encolar; con él se busca el tiempo en /history.
ITEMS = [
    {
        "slug": "r-01-baseline",
        "archivo": "activos/proyectos/concurso-gaudi-nexus/fractal-hires/r-01-baseline.png",
        "modelo": "Juggernaut-XL v9",
        "checkpoint": "Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors",
        "prompt_id": "abafea6c-7941-44c0-b974-30e0657afe31",
            "workflow": "WF-vivienda R-01",
            "nota": "Baseline 1216x832. Se encolaron 3 seeds iguales: solo la primera renderizo, las otras dos salieron de cache.",
            "segundos_fijo": 609.26,
    },
    {
        "slug": "t-h1-juggernaut",
        "archivo": "activos/proyectos/concurso-gaudi-nexus/fractal-hires/t-h1-juggernaut.png",
        "modelo": "Juggernaut-XL v9",
        "checkpoint": "Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors",
        "prompt_id": "1d6703a6-1769-4895-ad39-063975585d8d",
            "workflow": "fractal-hires T-H1",
            "nota": "Hires 2016x1152: base 1344x768 + latent upscale x1.5 con denoise 0.35.",
            "segundos_fijo": 1073.69,
    },
    {
        "slug": "t-h2-realvisxl",
        "archivo": "activos/proyectos/concurso-gaudi-nexus/fractal-hires/t-h2-realvisxl.png",
        "modelo": "RealVisXL v5.0",
        "checkpoint": "realvisxlV50_v50Bakedvae.safetensors",
        "prompt_id": "3bed5556-3bd9-4cff-b3c6-c3a57392f1f2",
            "workflow": "fractal-hires T-H2",
            "nota": "Mismo grafo y mismo prompt que T-H1: cambia solo el checkpoint.",
            "segundos_fijo": 1165.06,
    },
    {
        "slug": "t-h3-lightning",
        "archivo": "activos/proyectos/concurso-gaudi-nexus/fractal-hires/t-h3-lightning.png",
        "modelo": "RealVisXL v5.0 Lightning",
        "checkpoint": "realvisxlV50_v50LightningBakedvae.safetensors",
        "prompt_id": "710be756-1bec-4f3c-b8f7-1414c77c7261",
            "workflow": "fractal-hires T-H3",
            "nota": "Checkpoint Lightning (destilado): menos pasos, mas rapido, mas pictorico.",
            "segundos_fijo": 409.36,
        },
        {
            "slug": "w01-juggernaut-512",
            "archivo": "activos/proyectos/concurso-gaudi-nexus/sdxl-vista/w01-juggernaut-512.png",
            "modelo": "Juggernaut-XL v9",
            "checkpoint": "Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors",
            "prompt_id": "ecd27a03-3115-4d6d-a660-63d1a3672b34",
            "workflow": "WF-01 baseline 512",
            "nota": "WF-01 2026-11-02: prompt protocolo catenarias, seed 7, 512², 30 steps cfg 4 dpmpp_2m. Prueba de receta de la casa.",
            "segundos_fijo": 354.32,
        },
        {
            "slug": "w01-realvisxl-512",
            "archivo": "activos/proyectos/concurso-gaudi-nexus/sdxl-vista/w01-realvisxl-512.png",
            "modelo": "RealVisXL v5.0",
            "checkpoint": "realvisxlV50_v50Bakedvae.safetensors",
            "prompt_id": "c918cf29-0896-4239-8555-eee9e2d2c3db",
            "workflow": "WF-01 baseline 512",
            "nota": "Mismo prompt y grafo que w01-juggernaut: cambia solo el checkpoint. Seed aleatoria.",
            "segundos_fijo": 390.29,
        },
        {
            "slug": "w01-lightning-mosaicos-512",
            "archivo": "activos/proyectos/concurso-gaudi-nexus/sdxl-vista/w01-lightning-mosaicos-512.png",
            "modelo": "RealVisXL v5.0 Lightning",
            "checkpoint": "realvisxlV50_v50LightningBakedvae.safetensors",
            "prompt_id": "51d4e33d-0d46-4298-ac18-a431a4fc9413",
            "workflow": "WF-01 exploratoria 512",
            "nota": "Prompt en español: camino de mosaicos teselados Escher, colores tierra fachada Pasión, Sagrada de fondo. 30 steps cfg 4.",
            "segundos_fijo": 333.68,
        },
        {
            "slug": "w01-lightning-pasion-512",
            "archivo": "activos/proyectos/concurso-gaudi-nexus/sdxl-vista/w01-lightning-pasion-512.png",
            "modelo": "RealVisXL v5.0 Lightning",
            "checkpoint": "realvisxlV50_v50LightningBakedvae.safetensors",
            "prompt_id": "1548b647-a686-4234-9584-9bba72b91286",
            "workflow": "WF-01 exploratoria 512",
            "nota": "Prompt corto fachada Pasión + receta del autor: dpmpp_sde, 30 steps, cfg 1.5.",
            "segundos_fijo": 444.68,
        },
    ]


try:
    # NOTA ES: PIL solo hace falta para el modo embebido (miniaturas JPEG).
    from PIL import Image
except ImportError:
    Image = None


def thumb_b64(ruta, ancho=520):
    """Devuelve la imagen como data URI JPEG de hasta 520 px de ancho.

    NOTA ES: 520 px con calidad 80 deja cada thumb en ~50-80 KB: las 8
    NOTA ES: corridas entran en ~0,5 MB y el HTML viaja por mail/WhatsApp.
    """
    if Image is not None:
        im = Image.open(ruta).convert("RGB")
        if im.width > ancho:
            im = im.resize((ancho, round(im.height * ancho / im.width)))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=80, optimize=True, progressive=True)
        return "data:image/jpeg;base64," + base64.b64encode(
            buf.getvalue()).decode("ascii")
    # NOTA ES: sin PIL se embebe el PNG tal cual (pesa más, pero no se pierde nada).
    with open(ruta, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode(
            "ascii")


def medir_png(ruta):
    """Devuelve (ancho, alto) leyendo la cabecera IHDR del PNG.

    NOTA ES: un PNG arranca con 8 bytes de firma y despues el bloque IHDR, que
    NOTA ES: guarda ancho y alto como enteros de 4 bytes (big-endian) en los
    NOTA ES: offsets 16 y 20. Asi no hace falta Pillow para saber el tamaño.
    """
    with open(ruta, "rb") as f:
        cabecera = f.read(24)          # NOTA ES: solo hacen falta los primeros 24 bytes.
    ancho, alto = struct.unpack(">II", cabecera[16:24])  # NOTA ES: ">" = big-endian, "II" = dos enteros.
    return ancho, alto


def segundos_de_history(comfy, prompt_id):
    """Pide /history al ComfyUI y devuelve la duración real en segundos.

    NOTA ES: ComfyUI anota en status.messages dos eventos: execution_start y
    NOTA ES: execution_success, cada uno con su timestamp en milisegundos.
    NOTA ES: la resta / 1000 es el tiempo que estuvo la GPU trabajando.
    """
    url = "%s/history/%s" % (comfy.rstrip("/"), prompt_id)   # NOTA ES: rstrip evita "//" si la URL viene con barra final.
    try:
        with urllib.request.urlopen(url, timeout=20) as r:   # NOTA ES: with = cerrar la conexión al salir.
            datos = json.loads(r.read().decode("utf-8"))
    except Exception as e:                                   # NOTA ES: si el server está apagado, no rompemos el tablero.
        print("  aviso: sin /history (%s)" % e)
        return None
    entrada = datos.get(prompt_id)
    if not entrada:
        return None
    inicio = fin = None
    for nombre, payload in entrada.get("status", {}).get("messages", []):
        if nombre == "execution_start":
            inicio = payload.get("timestamp")
        elif nombre == "execution_success":
            fin = payload.get("timestamp")
    if inicio is None or fin is None:
        return None
    return round((fin - inicio) / 1000.0, 2)                 # NOTA ES: redondeo a 2 decimales, como en los logs.


HTML = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Concurso Gaudí Nexus — corridas</title>
<style>
  :root { --tinta:#15171b; --papel:#fbfbf8; --fondo:#101216; --gris:#8b9099; --acento:#e8b04b; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--fondo); color:#e9ebef;
         font-family:ui-sans-serif,system-ui,"Segoe UI",Roboto,sans-serif; }
  header { padding:28px 24px 10px; max-width:1400px; margin:0 auto; }
  h1 { margin:0 0 6px; font-size:22px; font-weight:650; letter-spacing:-.01em; }
  header p { margin:0; color:var(--gris); font-size:13px; }
  .grilla { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr));
            gap:16px; padding:18px 24px 60px; max-width:1400px; margin:0 auto; }
  .card { background:var(--papel); color:var(--tinta); border-radius:4px; padding:10px 10px 0;
          cursor:zoom-in; box-shadow:0 10px 24px rgba(0,0,0,.35); transition:transform .16s ease; }
  .card:hover { transform:translateY(-3px); }
  .card img { width:100%; display:block; border-radius:2px; background:#ddd; }
  .pie { padding:9px 2px 11px; display:flex; justify-content:space-between; gap:10px; align-items:baseline; }
  .pie b { font-size:13px; font-weight:650; }
  .pie span { font-size:12px; color:#5d636d; font-variant-numeric:tabular-nums; }
  #polaroid { position:fixed; inset:0; display:none; background:rgba(8,9,11,.92);
              padding:22px; overflow:auto; z-index:10; }
  #polaroid.on { display:block; }
  .marco { max-width:min(1200px,94vw); margin:0 auto; background:var(--papel); color:var(--tinta);
           padding:14px 14px 0; border-radius:4px; box-shadow:0 30px 80px rgba(0,0,0,.6); }
  .marco img { width:100%; display:block; border-radius:2px; }
  .meta { padding:12px 4px 16px; display:flex; flex-wrap:wrap; gap:6px 18px; font-size:12.5px; color:#4c525c; }
  .meta b { color:var(--tinta); }
  .meta .nota { flex-basis:100%; color:#6b717b; font-size:12px; line-height:1.45; }
  .nav { position:fixed; top:50%; transform:translateY(-50%); font-size:30px; color:#cfd3da;
         background:none; border:0; cursor:pointer; padding:10px 14px; opacity:.75; }
  .nav:hover { opacity:1; }
  #prev { left:6px; } #next { right:6px; }
  .cerrar { position:fixed; top:14px; right:18px; font-size:22px; color:#cfd3da;
            background:none; border:0; cursor:pointer; }
</style>
</head>
<body>
<header>
  <h1>Concurso Gaudí Nexus — corridas del 2026-11-01</h1>
  <p>__RESUMEN__</p>
</header>
<div class="grilla" id="grilla"></div>

<div id="polaroid">
  <button class="cerrar" id="cerrar" title="Cerrar (Esc)">&times;</button>
  <button class="nav" id="prev" title="Anterior (&larr;)">&lsaquo;</button>
  <button class="nav" id="next" title="Siguiente (&rarr;)">&rsaquo;</button>
  <div class="marco">
    <img id="grande" alt="">
    <div class="meta" id="meta"></div>
  </div>
</div>

<script>
const DATOS = __DATOS__;
const grilla = document.getElementById("grilla");
const overlay = document.getElementById("polaroid");
const grande = document.getElementById("grande");
const meta = document.getElementById("meta");
let actual = 0;

function segundos(r) {
  if (r.segundos == null) return "sin dato";
  const m = Math.floor(r.segundos / 60), s = Math.round(r.segundos % 60);
  return m ? `${m} min ${s} s` : `${s} s`;
}

DATOS.forEach((r, i) => {
  const card = document.createElement("div");
  card.className = "card";
  card.innerHTML = `<img src="${r.img}" alt="${r.modelo}" loading="lazy">
    <div class="pie"><b>${r.modelo}</b><span>${segundos(r)}</span></div>`;
  card.addEventListener("click", () => abrir(i));
  grilla.appendChild(card);
});

function abrir(i) {
  actual = (i + DATOS.length) % DATOS.length;
  const r = DATOS[actual];
  grande.src = r.img;
  meta.innerHTML = `<span><b>${r.modelo}</b></span>
    <span>${r.ancho}x${r.alto}</span>
    <span>${segundos(r)}</span>
    <span>${r.workflow}</span>
    <span class="nota">${r.nota || ""}</span>`;
  overlay.classList.add("on");
}
function cerrar() { overlay.classList.remove("on"); }

document.getElementById("cerrar").addEventListener("click", cerrar);
document.getElementById("prev").addEventListener("click", e => { e.stopPropagation(); abrir(actual - 1); });
document.getElementById("next").addEventListener("click", e => { e.stopPropagation(); abrir(actual + 1); });
overlay.addEventListener("click", e => { if (e.target === overlay) cerrar(); });
document.addEventListener("keydown", e => {
  if (!overlay.classList.contains("on")) return;
  if (e.key === "Escape") cerrar();
  if (e.key === "ArrowLeft") abrir(actual - 1);
  if (e.key === "ArrowRight") abrir(actual + 1);
});
</script>
</body>
</html>
"""


def generar(raiz, out, comfy, embebido=False, nombre_html="index.html"):
    """Copia las imágenes y escribe el sitio. Devuelve cuántas entradas hizo.

    NOTA ES: con embebido=True no se copian PNG: cada imagen viaja como
    NOTA ES: miniatura base64 dentro del HTML (versión para compartir).
    """
    img_dir = os.path.join(out, "img")
    if not embebido:
        os.makedirs(img_dir, exist_ok=True)   # NOTA ES: exist_ok=True = si ya existe, no falla.

    datos = []
    for item in ITEMS:
        origen = os.path.join(raiz, item["archivo"])
        if not os.path.isfile(origen):
            print("  falta: %s" % item["archivo"])
            continue
        ancho, alto = medir_png(origen)
        seg = segundos_de_history(comfy, item["prompt_id"])
        if seg is None:
            seg = item.get("segundos_fijo")   # NOTA ES: respaldo medido 2026-11-01; /history se vacia al reiniciar ComfyUI.
            if seg is not None:
                print("  %s: tiempo de respaldo %ss" % (item["slug"], seg))
        print("  %-16s %sx%s  %ss" % (item["slug"], ancho, alto, seg))
        if embebido:
            img = thumb_b64(origen)   # NOTA ES: data URI lista para el <img src>.
            nombre = "(embebido)"
        else:
            nombre = item["slug"] + ".png"
            shutil.copy2(os.path.join(raiz, item["archivo"]),
                         os.path.join(img_dir, nombre))   # NOTA ES: copia byte a byte: NO se reescala.
            img = "img/" + nombre
        datos.append({
            "img": img,
            "modelo": item["modelo"],
            "checkpoint": item["checkpoint"],
            "workflow": item["workflow"],
            "nota": item["nota"],
            "ancho": ancho,
            "alto": alto,
            "segundos": seg,
            "prompt_id": item["prompt_id"],
        })

    con_tiempo = [d["segundos"] for d in datos if d["segundos"]]
    total = sum(con_tiempo)
    resumen = "%d imágenes · %.1f min de GPU en total · %s" % (
        len(datos), total / 60.0, datetime.now().strftime("%Y-%m-%d %H:%M"))

    html = (HTML
            .replace("__DATOS__", json.dumps(datos, ensure_ascii=False))
            .replace("__RESUMEN__", resumen))
    with open(os.path.join(out, nombre_html), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(out, "datos.json"), "w", encoding="utf-8") as f:
        json.dump({"generado": datetime.now().isoformat(timespec="seconds"),
                   "resumen": resumen, "items": datos}, f, indent=2, ensure_ascii=False)
    return len(datos)


def main():
    ap = argparse.ArgumentParser(description="Tablero polaroid de las corridas del concurso.")
    ap.add_argument("--out", default="activos/web/concurso", help="carpeta del sitio")
    ap.add_argument("--comfy", default="http://127.0.0.1:8188", help="URL del ComfyUI")
    ap.add_argument("--embebido", default=None, metavar="RUTA.html",
                    help="genera versión autocontenida (miniaturas base64) en RUTA.html, lista para compartir")
    args = ap.parse_args()

    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # NOTA ES: la raíz del vault es el padre de scripts/.
    if args.embebido:
        # NOTA ES: el HTML compartible vive en presentacion/ (commiteado); las
        # NOTA ES: imágenes full-res quedan en activos/ (fuera de git).
        destino = os.path.abspath(os.path.join(raiz, args.embebido))
        out = os.path.dirname(destino)
        os.makedirs(out, exist_ok=True)
        print("Generando embebido %s" % destino)
        n = generar(raiz, out, args.comfy, embebido=True,
                    nombre_html=os.path.basename(destino))
        print("Listo: %d imágenes (miniaturas embebidas)" % n)
        return
    out = os.path.abspath(os.path.join(raiz, args.out))
    os.makedirs(out, exist_ok=True)

    print("Generando %s" % out)
    n = generar(raiz, out, args.comfy)
    print("Listo: %d imágenes" % n)
    print("Abrir: %s" % os.path.join(out, "index.html"))


if __name__ == "__main__":
    main()
