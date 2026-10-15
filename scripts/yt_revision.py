"""
yt_revision.py — Genera el archivo de REVISION MANUAL: solo lo pendiente.

QUE HACE
--------
Lee el Takeout + el cache de titulos y escribe UN archivo chico con SOLO lo
que el estudio tiene que decidir:

  Parte 1: videos de Watch Later con tag 'sin-clasificar' (los que el script
           no pudo ubicar). El estudio marca rescatar o descartar.
  Parte 2: canales fuera de scope, con la pista 'Parece ser'. El estudio marca
           sumar a <categoria>, descartar o pendiente.

COMO SE REVISA (dos modos, a eleccion del estudio)
--------------------------------------------------
  Modo A (en Obsidian): abrir raw/yt/revision-manual.md y completar la columna
  'Tu veredicto' directamente en la tabla. Guardar. Avisar al agente.

  Modo B (en el chat): pasar los numeros. Ej: 'videos rescato 3, 7, 15;
  canales sumo 5 (software-arq) y 12 (creadores); el resto se descarta'.

COMO EJECUTARLO
---------------
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\yt_revision.py

Salida: raw/yt/revision-manual.md

Requiere: raw/yt/cache-titulos.json (correr scripts/yt_titles.py antes).
Si no hay cache, sale con IDs en vez de titulos (igual revisable).
"""

import csv
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------- NOTA ES:
# Reusamos todo lo del parser (tags, categorias, normalizacion) importandolo
# como modulo. Asi no duplicamos las tablas de keywords: si las ajustas en
# yt_takeout_parser.py, este script las hereda solo.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import yt_takeout_parser as P

VAULT = P.VAULT
OUT = VAULT / "raw" / "yt" / "revision-manual.md"


def leer_cache():
    """Lee el cache de titulos. Si no existe, devuelve {} (modo sin titulos)."""
    if P.CACHE_TITULOS.exists():
        return json.loads(P.CACHE_TITULOS.read_text(encoding="utf-8"))
    print("AVISO: sin cache de titulos. Corre scripts/yt_titles.py primero.")
    print("       (igual genero el archivo, pero con IDs en vez de titulos)")
    return {}


def leer_watch_later():
    """Devuelve [(video_id, fecha), ...] de Watch Later."""
    for f in P.LISTDIR.glob("*.csv"):
        if f.stem.lower().startswith("watch later"):
            return P.leer_videos_de_playlist(f)
    raise SystemExit("ERROR: no encontre el CSV de Watch Later")


def leer_subs():
    """Devuelve [{'id','url','nombre'}, ...] de suscripciones.csv."""
    subs = []
    with open(P.SUBDIR / "suscripciones.csv", encoding="utf-8-sig", newline="") as fh:
        rd = csv.reader(fh)
        next(rd, None)
        for r in rd:
            if len(r) >= 3 and r[0].strip():
                subs.append({
                    "id": r[0].strip(),
                    "url": r[1].strip().replace("http://", "https://"),
                    "nombre": r[2].strip(),
                })
    return subs


def clasificar_canal(nombre):
    """Replica la logica del parser: primera categoria de CATS que matchea."""
    n = P._norm(nombre)
    for cat, kws in P.CATS.items():
        for k in kws:
            if P._norm(k) in n:
                return cat
    return None


def pista_fuera(nombre):
    """Replica la logica del parser: sugerencia para la columna 'Parece ser'."""
    n = P._norm(nombre)
    for etiqueta, kws in PISTAS_FUERA.items():
        for k in kws:
            if P._norm(k) in n:
                return etiqueta
    return "sin pista (revisar)"


# NOTA ES: PISTAS_FUERA vive en el modulo parser, lo referenciamos con P.
PISTAS_FUERA = P.PISTAS_FUERA


def main():
    cache = leer_cache()
    wl = leer_watch_later()
    subs = leer_subs()
    print(f"Watch Later: {len(wl)} | Suscripciones: {len(subs)} | Cache: {len(cache)}")

    # ---- Parte 1: WL sin clasificar ----
    pendientes = []
    for vid, fecha in wl:
        d = cache.get(vid, {})
        tit = d.get("titulo", "") if d else ""
        can = d.get("canal", "") if d else ""
        dur = d.get("duracion", "") if d else ""
        if not tit:
            # sin titulo (no esta en cache): igual va a revision, con el ID
            pendientes.append((vid, f"_(sin titulo: {vid})_", "", "", fecha[:10]))
            continue
        tags = P.inferir_tags(tit, can, "watch later")
        if tags == ["sin-clasificar"]:
            pendientes.append((vid, tit, can, dur, fecha[:10]))

    fuera = [s for s in subs if not clasificar_canal(s["nombre"])]
    print(f"WL sin-clasificar: {len(pendientes)} | Canales fuera: {len(fuera)}")

    L = []
    A = L.append
    A("---")
    A("tipo: raw-cola")
    A("fecha_creacion: 2026-10-08")
    A("ultima_actualizacion: 2026-10-08")
    A("tags: [yt, revision-manual, watch-later, hitl]")
    A("---")
    A("")
    A("# Revision manual — solo lo pendiente")
    A("")
    A("> Este archivo tiene SOLO lo que el script no pudo ubicar solo.")
    A("> Todo lo demas ya esta clasificado en")
    A("> [[raw/yt/videos-y-canales-guardados|videos-y-canales-guardados]].")
    A("")
    A("## Como revisar (elegi un modo)")
    A("")
    A("**Modo A — en Obsidian:** completa la columna `Tu veredicto` en cada tabla,")
    A("guarda el archivo y avisame (`listo la revision`). Yo aplico los cambios.")
    A("")
    A("**Modo B — en el chat:** pasame los numeros. Ejemplo:")
    A("`videos rescato 3, 7, 15; canales sumo 5 (software-arq) y 12 (creadores);")
    A("el resto se descarta`. Yo aplico los cambios.")
    A("")
    A("Valores validos para videos: `rescatar` / `descartar` (vacio = pendiente).")
    A("Valores validos para canales: `sumar a <categoria>` / `descartar` / `pendiente`.")
    A("Categorias validas: arq+IA, software arq, estudios intl., IA general,")
    A("NFTs/tokens, construccion, creadores, noticias intl., libros.")
    A("")
    A("---")
    A("")
    A(f"## Parte 1 — Watch Later sin clasificar ({len(pendientes)} videos)")
    A("")
    A("Videos que no matchearon ningun tag ni por titulo ni por carpeta.")
    A("Si lo rescatas, decime tambien a que tema va (ej `rescatar, rhino`) y lo")
    A("sumo a las keywords para que no vuelva a quedar afuera.")
    A("")
    A("| # | Titulo | Canal | Dur | Fecha | Tu veredicto | Notas |")
    A("|---|---|---|---|---|---|---|")
    for i, (vid, tit, can, dur, fecha) in enumerate(pendientes, 1):
        link = f"https://www.youtube.com/watch?v={vid}"
        A(f"| {i} | [{P.esc_md(tit[:90])}]({link}) | {P.esc_md(can)} | {dur} | {fecha} |  |  |")
    A("")
    A("---")
    A("")
    A(f"## Parte 2 — Canales fuera de scope ({len(fuera)} canales)")
    A("")
    A("Canales que no matchearon las keywords del rubro.")
    A("La columna *Parece ser* es mi sugerencia para escanear rapido.")
    A("")
    A("| # | Canal | Link | Parece ser | Tu veredicto | Notas |")
    A("|---|---|---|---|---|---|")
    for i, s in enumerate(fuera, 1):
        A(f"| {i} | {P.esc_md(s['nombre'])} | {s['url']} | {pista_fuera(s['nombre'])} |  |  |")
    A("")
    A("---")
    A("")
    A("## Que pasa despues de tu veredicto")
    A("")
    A("1. Los `rescatar`/`sumar` entran al scope (ajusto keywords y regenero).")
    A("2. Los `descartar` quedan archivados en el Takeout original (no se pierden).")
    A("3. Genero `raw/yt/triage-watch-later.md` y `raw/yt/catalogo-watch-later.md`.")
    A("4. Recien despues: homepage `wiki/estudio/noticias/` + edicion piloto.")
    A("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"\nOK -> {OUT}")
    print(f"   {len(L)} lineas")


if __name__ == "__main__":
    main()