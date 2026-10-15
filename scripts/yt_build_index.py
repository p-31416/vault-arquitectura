"""
yt_build_index.py — Genera wiki/fuentes/00-index-yt.md: UN solo archivo con
3 vistas (por listado, por creador, por tag) sobre un tag filtro.

DISENO (decision del estudio 2026-10-09)
---------------------------------------
- Un solo archivo, no 3: `wiki/fuentes/00-index-yt.md` (prefijo 00- = aparece primero).
- Alcance inicial: SOLO videos con tag `comfyui` (piloto). El filtro se pasa
  por linea de comandos para ampliar despues (ej `rhino`, o `all`).
- Columna Estado: los videos entran como ⏳ pendiente y pasan a ✅ procesado
  (con link al reporte) cuando `@contenidos` los procesa. El estado vive en
  `raw/yt/index-state.json` para sobrevivir regeneraciones.

FUENTES (solo lectura)
----------------------
- raw/yt/cache-titulos.json .... titulo/canal/duracion por video
- Takeout: playlists ........... orden de aparicion por lista
- raw/yt/veredictos.json ....... veredictos (se aplican a los tags)
- raw/yt/index-state.json ...... {video_id: ruta-reporte} (creado a mano)

SALIDA
------
- wiki/fuentes/00-index-yt.md

COMO EJECUTARLO
---------------
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\yt_build_index.py [tag]
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\yt_build_index.py comfyui
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\yt_build_index.py all

Cuando `@contenidos` termina un video, SOL aprueba y el reporte se MUEVE a
`wiki/fuentes/<slug>.md` (ver protocolo en .opencode/agents/contenidos.md).
Actualizar index-state.json a la nueva ruta:
    {"procesados": {"<video_id>": "wiki/fuentes/<slug>.md"}}
y re-correr este script.
"""

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import yt_takeout_parser as P

VAULT = P.VAULT
OUT = VAULT / "wiki" / "fuentes" / "00-index-yt.md"
STATE = VAULT / "raw" / "yt" / "index-state.json"


def leer_playlists():
    """Devuelve [(titulo_lista, [(video_id, fecha), ...]), ...] en orden.

    NOTA ES: el orden de listas es el que definio el estudio: Watch Later
    primero, despues sus carpetas tematicas. Dentro de cada lista se respeta
    el orden de aparicion del Takeout (mas nuevo primero en WL).
    """
    # maestro: id -> (titulo, descripcion)
    maestro_path = None
    for p in sorted(P.LISTDIR.glob("*.csv")):
        if not p.stem.lower().endswith(("-videos", "-vídeos")):
            maestro_path = p
            break
    if maestro_path is None:
        raise SystemExit("ERROR: no se encontro el CSV maestro de listas")
    maestro = {}
    with open(maestro_path, encoding="utf-8-sig", newline="") as f:
        rd = csv.reader(f)
        next(rd, None)  # saltear header
        for r in rd:
            if len(r) >= 4 and r[0].strip():
                maestro[r[0].strip()] = (r[3].strip(), r[2].strip() if len(r) > 2 else "")

    # emparejar titulo -> archivo (misma logica que el parser)
    stems = {}
    for real in P.LISTDIR.glob("*.csv"):
        ns = P._norm(real.stem)
        if ns.startswith("listas de reproduccion") or ns.startswith("lista de reproduccion"):
            continue
        stems.setdefault(ns, real)

    listas = []
    for pid, (titulo, _desc) in maestro.items():
        clave = P._norm(titulo.replace("/", "_"))
        if clave in stems:
            listas.append((titulo, P.leer_videos_de_playlist(stems[clave])))

    # Watch Later primero, resto alfabetico
    listas.sort(key=lambda t: (0 if t[0].strip().lower() == "watch later" else 1, t[0].lower()))
    return listas


def main():
    filtro = sys.argv[1].lower() if len(sys.argv) > 1 else "comfyui"

    cache = {}
    if P.CACHE_TITULOS.exists():
        cache = json.loads(P.CACHE_TITULOS.read_text(encoding="utf-8"))
    print(f"Cache: {len(cache)} titulos")

    vered = {}
    vf = VAULT / "raw" / "yt" / "veredictos.json"
    if vf.exists():
        vered = json.loads(vf.read_text(encoding="utf-8")).get("videos", {})

    estado = {}
    if STATE.exists():
        estado = json.loads(STATE.read_text(encoding="utf-8")).get("procesados", {})
    print(f"Procesados registrados: {len(estado)}")

    # ---- recolectar videos del filtro ----
    # NOTA ES: se aplica veredicto igual que en el parser, para que el indice
    # muestre exactamente los mismos tags que el doc unico.
    def tags_de(vid, tit, can, carpeta):
        d = vered.get(vid)
        if d and d.get("v") == "rescatar" and d.get("tema"):
            temas = d["tema"]
            base = P.inferir_tags(tit, can, carpeta)
            return (temas + [t for t in base if t not in temas])[:4]
        if d and d.get("v") in ("filosofia", "personal", "otros"):
            return [d["v"]]
        if d and d.get("v") == "descartar":
            return ["descartado"]
        if d and d.get("v") == "proyecto":
            return ["proyecto"]
        return P.inferir_tags(tit, can, carpeta)

    listas = leer_playlists()
    # video_id -> {titulo, canal, dur, listas:[...], tags:[...], cat}
    videos = {}
    orden_listas = []
    for titulo_lista, items in listas:
        orden_listas.append((titulo_lista, []))
        for vid, fecha in items:
            dd = cache.get(vid, {})
            tit = P.esc_md(dd.get("titulo", "") or "")
            can = P.esc_md(dd.get("canal", "") or "")
            dur = dd.get("duracion", "") or ""
            tags = tags_de(vid, tit.replace("\\|", "|"), can, titulo_lista)
            if filtro != "all" and filtro not in tags:
                continue
            if vid not in videos:
                videos[vid] = {"titulo": tit, "canal": can, "dur": dur,
                               "listas": [], "tags": tags,
                               "cat": P.categoria_de(tags)}
            videos[vid]["listas"].append((titulo_lista, fecha[:10] if fecha else ""))
            orden_listas[-1][1].append(vid)

    print(f"Videos con tag '{filtro}': {len(videos)}")

    def fila_estado(vid):
        rep = estado.get(vid)
        if rep:
            return f"✅ [reporte]({rep})"
        return "⏳ pendiente"

    def link_yt(vid):
        return f"https://www.youtube.com/watch?v={vid}"

    L = []
    A = L.append
    A("---")
    A("tipo: indice")
    A("fecha_creacion: 2026-10-09")
    A("ultima_actualizacion: 2026-10-09")
    A(f"tags: [yt, indice, {filtro}]")
    A("---")
    A("")
    A(f"# Index YT — {filtro} ({len(videos)} videos)")
    A("")
    A("> UN solo indice con 3 vistas. Alcance actual: SOLO videos con tag")
    A(f"> `{filtro}` (piloto). Los videos entran como ⏳ y pasan a ✅ cuando")
    A("> `@contenidos` los procesa (estado en `raw/yt/index-state.json`).")
    A(">")
    A("> Regenerar con: `scripts/yt_build_index.py [tag|all]`")
    A("")
    A("## Vistas")
    A("")
    A("- [[#Vista 1 — Por listado|Vista 1 — Por listado]] (orden de aparicion)")
    A("- [[#Vista 2 — Por creador|Vista 2 — Por creador]]")
    A("- [[#Vista 3 — Por tag|Vista 3 — Por tag]]")
    A("")
    A("---")
    A("")
    # ---- Vista 1: por listado ----
    A("## Vista 1 — Por listado")
    A("")
    A("Mismo orden que tus carpetas de YouTube. Estado ⏳/✅ por video.")
    A("")
    for titulo_lista, vids in orden_listas:
        en_filtro = [v for v in vids if v in videos]
        if not en_filtro:
            continue
        A(f"### {titulo_lista} ({len(en_filtro)})")
        A("")
        A("| # | Titulo | Canal | Dur | Tags | Estado | Link |")
        A("|---|---|---|---|---|---|---|")
        for i, vid in enumerate(en_filtro, 1):
            d = videos[vid]
            A(f"| {i} | {d['titulo']} | {d['canal']} | {d['dur']} | "
              f"{', '.join(d['tags'])} | {fila_estado(vid)} | {link_yt(vid)} |")
        A("")
    A("---")
    A("")
    # ---- Vista 2: por creador ----
    A("## Vista 2 — Por creador")
    A("")
    por_creador = defaultdict(list)
    for vid, d in videos.items():
        por_creador[d["canal"] or "(sin canal)"].append(vid)
    A(f"| Creador | Videos | Procesados | Videos |")
    A("|---|---|---|---|")
    for canal in sorted(por_creador, key=lambda c: (-len(por_creador[c]), c.lower())):
        vids = por_creador[canal]
        n_ok = sum(1 for v in vids if v in estado)
        links = " · ".join(
            f"[{videos[v]['titulo'][:45]}]({link_yt(v)})" for v in vids[:12]
        )
        if len(vids) > 12:
            links += f" · _...y {len(vids) - 12} mas_"
        A(f"| {canal} | {len(vids)} | {n_ok}/{len(vids)} | {links} |")
    A("")
    A("---")
    A("")
    # ---- Vista 3: por tag ----
    A("## Vista 3 — Por tag")
    A("")
    por_tag = defaultdict(list)
    for vid, d in videos.items():
        for t in d["tags"]:
            por_tag[t].append(vid)
    for tag in sorted(por_tag, key=lambda t: (-len(por_tag[t]), t)):
        vids = por_tag[tag]
        n_ok = sum(1 for v in vids if v in estado)
        A(f"### #{tag} ({len(vids)} videos, {n_ok} procesados)")
        A("")
        for vid in vids:
            d = videos[vid]
            A(f"- [{d['titulo']}]({link_yt(vid)}) — {d['canal']} ({d['dur']}) "
              f"| {fila_estado(vid)}")
        A("")
    A("---")
    A("")
    A("## Origen")
    A("")
    A("- Fuentes: Takeout + `raw/yt/cache-titulos.json` + `raw/yt/veredictos.json`")
    A("- Estado: `raw/yt/index-state.json` (cuando `@contenidos` termina un video,")
    A("  agregar su ID ahi y re-correr este script)")
    A("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"\nOK -> {OUT}")
    print(f"   {len(L)} lineas | {len(videos)} videos | "
          f"{len(por_creador)} creadores | {len(por_tag)} tags")


if __name__ == "__main__":
    main()