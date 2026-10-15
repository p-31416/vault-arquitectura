"""Genera raw/yt/creadores.md: TODOS los creadores (suscriptos + solo-WL).

POR QUE EXISTE
--------------
El doc de canales solo con suscriptos (157) deja afuera a los creadores que
aparecen SOLO en Watch Later (Corridor Crew, Kyle Sinko, B:Side Academy,
BlessedArch, PixelArtistry...). El estudio ya los clasifico en esta
conversacion (veredictos 1-131), asi que este script los extrae del cache
de titulos y los lista con su veredicto.

FUENTES (solo lectura)
----------------------
- raw/yt/cache-titulos.json ........ video_id -> {titulo, canal, duracion}
- Takeout: Watch later-videos.csv ... los 259 IDs de WL
- Takeout: suscripciones.csv ........ los 157 suscriptos
- raw/yt/veredictos.json ........... veredictos dictados (por video)

SALIDA
------
- raw/yt/creadores.md con 3 partes:
  A. Suscriptos en scope (44) con categoria
  B. Creadores SOLO en Watch Later (no suscriptos), con cantidad de videos
     en WL + veredicto agregado de sus videos
  C. Suscriptos fuera de scope (113) con pista (remite a revision-manual P2)

COMO EJECUTARLO
---------------
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\yt_creadores.py
"""

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import yt_takeout_parser as P

VAULT = P.VAULT
OUT = VAULT / "raw" / "yt" / "creadores.md"


def leer_wl_ids():
    """Devuelve la lista ordenada de video_ids de Watch Later."""
    for f in P.LISTDIR.glob("*.csv"):
        if f.stem.lower().startswith("watch later"):
            return [vid for vid, _ in P.leer_videos_de_playlist(f)]
    raise SystemExit("ERROR: no encontre el CSV de Watch Later")


def leer_subs():
    """Devuelve {nombre_normalizado: {nombre, url, id}} de suscripciones."""
    subs = {}
    with open(P.SUBDIR / "suscripciones.csv", encoding="utf-8-sig", newline="") as fh:
        rd = csv.reader(fh)
        next(rd, None)
        for r in rd:
            if len(r) >= 3 and r[0].strip():
                subs[P._norm(r[2].strip())] = {
                    "nombre": r[2].strip(),
                    "url": r[1].strip().replace("http://", "https://"),
                    "id": r[0].strip(),
                }
    return subs


def clasificar_canal(nombre):
    """Primera categoria de CATS que matchea (igual que el parser)."""
    n = P._norm(nombre)
    for cat, kws in P.CATS.items():
        for k in kws:
            if P._norm(k) in n:
                return cat
    return None


def pista_fuera(nombre):
    """Sugerencia para canales fuera de scope (igual que el parser)."""
    n = P._norm(nombre)
    for etiqueta, kws in P.PISTAS_FUERA.items():
        for k in kws:
            if P._norm(k) in n:
                return etiqueta
    return "sin pista (revisar)"


def main():
    cache = json.loads(P.CACHE_TITULOS.read_text(encoding="utf-8"))
    wl_ids = leer_wl_ids()
    subs = leer_subs()
    vered = {}
    if (VAULT / "raw" / "yt" / "veredictos.json").exists():
        vered = json.loads(
            (VAULT / "raw" / "yt" / "veredictos.json").read_text(encoding="utf-8")
        ).get("videos", {})
    print(f"WL: {len(wl_ids)} | subs: {len(subs)} | cache: {len(cache)} | veredictos: {len(vered)}")

    # ---- videos de WL con canal conocido ----
    # NOTA ES: defaultdict(list) agrupa los video_ids por nombre de canal.
    por_canal = defaultdict(list)
    sin_canal = 0
    for vid in wl_ids:
        d = cache.get(vid, {})
        canal = (d.get("canal") or "").strip()
        if not canal:
            sin_canal += 1
            continue
        por_canal[canal].append(vid)
    print(f"Canales distintos en WL: {len(por_canal)} | sin canal (borrados): {sin_canal}")

    # ---- veredicto agregado por canal ----
    # NOTA ES: un canal puede tener videos con veredictos distintos (ej 2
    # rescatar + 1 otros). Mostramos el conteo por tipo para decidir.
    ORDEN_V = ["rescatar", "filosofia", "otros", "proyecto", "descartar"]

    def agregado(vids):
        c = Counter()
        for vid in vids:
            vv = vered.get(vid, {}).get("v")
            c[vv if vv else "pendiente"] += 1
        # el dominante primero (rescatar > resto, pendiente al final)
        partes = []
        for k in ORDEN_V + ["pendiente"]:
            if c.get(k):
                partes.append(f"{k} {c[k]}")
        return ", ".join(partes)

    # ---- dividir: suscriptos vs solo-WL ----
    # NOTA ES: comparamos por nombre normalizado (sin acentos/mayusculas).
    # Si YouTube escribe el canal distinto en cada lado puede fallar un
    # match puntual: se revisa en la columna 'Suscripto'.
    en_scope, fuera_scope, solo_wl = [], [], []
    for canal, vids in por_canal.items():
        s = subs.get(P._norm(canal))
        if s:
            cat = clasificar_canal(s["nombre"])
            (en_scope if cat else fuera_scope).append(
                {"canal": canal, "url": s["url"], "n": len(vids),
                 "cat": cat or pista_fuera(s["nombre"]), "ver": agregado(vids),
                 "vids": vids}
            )
        else:
            solo_wl.append({"canal": canal, "n": len(vids),
                            "ver": agregado(vids), "vids": vids})

    en_scope.sort(key=lambda x: (-x["n"], x["canal"].lower()))
    fuera_scope.sort(key=lambda x: (-x["n"], x["canal"].lower()))
    solo_wl.sort(key=lambda x: (-x["n"], x["canal"].lower()))
    print(f"En scope (con WL): {len(en_scope)} | fuera (con WL): {len(fuera_scope)} | solo-WL: {len(solo_wl)}")

    L = []
    A = L.append
    A("---")
    A("tipo: raw-cola")
    A("fecha_creacion: 2026-10-08")
    A("ultima_actualizacion: 2026-10-08")
    A("tags: [yt, canales, creadores, watch-later, hitl]")
    A("---")
    A("")
    A("# Creadores — suscriptos + Watch Later")
    A("")
    A("> Todos los creadores que aparecen en tu Watch Later (259 videos),")
    A("> cruzados con tus suscripciones. La columna **Veredicto WL** resume lo")
    A("> que ya juzgaste en esta conversacion (veredictos 1-131).")
    A(">")
    A("> Regenerar con: `scripts/yt_creadores.py`")
    A("")
    A("## Resumen")
    A("")
    A("| Metrica | Cantidad |")
    A("|---|---|")
    A(f"| Canales distintos en WL | {len(por_canal)} |")
    A(f"| Suscriptos en scope (con videos en WL) | {len(en_scope)} |")
    A(f"| Suscriptos fuera de scope (con videos en WL) | {len(fuera_scope)} |")
    A(f"| Solo en WL (NO suscriptos) | {len(solo_wl)} |")
    A(f"| Videos WL sin canal (borrados) | {sin_canal} |")
    A("")
    A("---")
    A("")
    A(f"## Parte A — Suscriptos en scope con videos en WL ({len(en_scope)})")
    A("")
    A("Canales del rubro a los que estas suscripto y que tenes en Watch Later.")
    A("Detalle completo en [[wiki/glosario/interno/canales-youtube|canales-youtube]].")
    A("")
    A("| # | Canal | Videos WL | Categoria | Veredicto WL | Link |")
    A("|---|---|---|---|---|---|")
    for i, c in enumerate(en_scope, 1):
        A(f"| {i} | {P.esc_md(c['canal'])} | {c['n']} | {c['cat']} | {c['ver']} | {c['url']} |")
    A("")
    A("---")
    A("")
    A(f"## Parte B — Solo en Watch Later, NO suscriptos ({len(solo_wl)})")
    A("")
    A("Creadores que descubriste guardando videos pero no seguis. Si alguno te")
    A("sirve, suscribite en YouTube y avisame para sumarlo al scope.")
    A("El link lleva al video mas reciente que guardaste de ese canal.")
    A("")
    A("| # | Canal | Videos WL | Veredicto WL | Link (video WL) |")
    A("|---|---|---|---|---|")
    for i, c in enumerate(solo_wl, 1):
        # NOTA ES: link al primer video (el mas reciente en WL, porque wl_ids
        # viene ordenado por fecha descendente del Takeout).
        link = f"https://www.youtube.com/watch?v={c['vids'][0]}"
        A(f"| {i} | {P.esc_md(c['canal'])} | {c['n']} | {c['ver']} | {link} |")
    A("")
    A("---")
    A("")
    A(f"## Parte C — Suscriptos fuera de scope con videos en WL ({len(fuera_scope)})")
    A("")
    A("Estas suscripto pero el canal no es del rubro. Revisalos en")
    A("[[raw/yt/revision-manual|revision-manual]] Parte 2 para el veredicto final.")
    A("")
    A("| # | Canal | Videos WL | Parece ser | Veredicto WL | Link |")
    A("|---|---|---|---|---|---|")
    for i, c in enumerate(fuera_scope, 1):
        A(f"| {i} | {P.esc_md(c['canal'])} | {c['n']} | {c['cat']} | {c['ver']} | {c['url']} |")
    A("")
    A("---")
    A("")
    A("## Metodologia y origen")
    A("")
    A("- Fuentes: Takeout (Watch Later + suscripciones) + `raw/yt/cache-titulos.json`")
    A("- Veredictos: `raw/yt/veredictos.json` (dictados 1-131 en conversacion)")
    A("- `Suscripto` se matchea por nombre normalizado; si un canal aparece como")
    A("  no-suscripto por error de escritura, avisame y lo corrijo a mano.")
    A("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"\nOK -> {OUT}")
    print(f"   {len(L)} lineas")


if __name__ == "__main__":
    main()