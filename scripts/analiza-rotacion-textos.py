"""
NOTA ES: Analiza la orientacion de textos y bloques de un plano de replanteo
NOTA ES: (lectura del DXF convertido con ODA File Converter, sin AutoCAD abierto).
NOTA ES:
NOTA ES: Responde tres preguntas de una lamina:
NOTA ES:   1. Que layouts (espacios de presentacion) existen y como estan rotados
NOTA ES:      sus VIEWPORT (angulo de giro = "twist" del viewport).
NOTA ES:   2. Que textos (TEXT / MTEXT) y que bloques (INSERT) tienen angulo
NOTA ES:      de rotacion distinto de 0, agrupados por capa.
NOTA ES:   3. Que bloques contienen texto (para saber si al girar el bloque
NOTA ES:      el texto gira con el o no).
NOTA ES:
NOTA ES: Uso:  python analiza-rotacion-textos.py <archivo.dxf> [<salida.json>]
NOTA ES: No modifica nada: solo lee y escribe un JSON de reporte.
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import ezdxf


def dxf_get(ent, nombre, default=None):
    """Lee un atributo DXF sin romper si la entidad no lo define (TEXT vs MTEXT)."""
    try:
        return ent.dxf.get(nombre, default)
    except Exception:
        return default


def rot_degree(valor):
    """DXF guarda los angulos (grupo 50) en GRADOS, no en radianes."""
    if valor is None:
        return None
    return round(float(valor), 3)


def entidades_por_tipo(space):
    """Cuenta entidades por tipo DXF dentro de un space (modelspace o paperspace)."""
    conteo = Counter(e.dxftype() for e in space)
    return dict(conteo)


def viewports_de(paperspace):
    """Extrae datos clave de cada VIEWPORT de un espacio papel.

    NOTA ES: en DXF, el grupo 50 del VIEWPORT es el angulo de giro de la vista
    NOTA ES: (twist). Si no es 0, TODO lo que hay en model space se ve
    NOTA ES: inclinado en la lamina, incluidos los textos.
    """
    datos = []
    for vp in paperspace.query("VIEWPORT"):
        d = {
            "handle": vp.dxf.handle,
            "center": list(vp.dxf.center) if vp.dxf.hasattr("center") else None,
            "id": vp.dxf.get("id", None),
            "twist_grados": rot_degree(vp.dxf.get("view_twist_angle", 0.0)),
            "view_center": list(vp.dxf.view_center_point) if vp.dxf.hasattr("view_center_point") else None,
            "view_height": vp.dxf.get("view_height", None),
            "view_target": list(vp.dxf.view_target_point) if vp.dxf.hasattr("view_target_point") else None,
            "status": vp.dxf.get("status", None),
            "es_rectangular": bool(vp.dxf.get("status", 0) & 1),
            "layer": vp.dxf.layer,
        }
        try:
            d["escala"] = round(d["view_height"] * 1000.0, 3)
        except TypeError:
            d["escala"] = None
        datos.append(d)
    return datos


def textos_rotados(space):
    """TEXT / MTEXT con angulo de rotacion, agrupados por capa."""
    por_capa = defaultdict(list)
    for e in space:
        if e.dxftype() == "TEXT":
            rot = rot_degree(e.dxf.get("rotation", 0.0))
            align = e.dxf.get("halign", 0)
            por_capa[e.dxf.layer].append({
                "tipo": "TEXT",
                "handle": e.dxf.handle,
                "rot": rot,
                "halign": align,
                "valign": dxf_get(e, "valign", 0),
                "texto": e.dxf.get("text", ""),
            })
        elif e.dxftype() == "MTEXT":
            rot = rot_degree(e.dxf.get("rotation", 0.0))
            por_capa[e.dxf.layer].append({
                "tipo": "MTEXT",
                "handle": e.dxf.handle,
                "rot": rot,
                "halign": dxf_get(e, "halign", dxf_get(e, "attachment_point", 0)),
                "texto": (e.dxf.get("text", "") or "")[:40],
            })
    return por_capa


def inserts_rotados(space):
    """INSERT (referencias a bloque) con su angulo de rotacion, agrupados por capa."""
    por_capa = defaultdict(list)
    for e in space.query("INSERT"):
        por_capa[e.dxf.layer].append({
            "bloque": e.dxf.name,
            "handle": e.dxf.handle,
            "rot": rot_degree(e.dxf.get("rotation", 0.0)),
            "x": round(e.dxf.insert[0], 3),
            "y": round(e.dxf.insert[1], 3),
        })
    return por_capa


def bloques_con_texto(doc):
    """Lista los bloques definidos que contienen TEXT o MTEXT (giran con el bloque)."""
    con_texto = []
    for blk in doc.blocks:
        if blk.name.startswith("*"):
            continue
        tipos = Counter(e.dxftype() for e in blk)
        if tipos.get("TEXT") or tipos.get("MTEXT"):
            con_texto.append({
                "bloque": blk.name,
                "textos": tipos.get("TEXT", 0),
                "mtexts": tipos.get("MTEXT", 0),
                "total_entidades": sum(tipos.values()),
            })
    return con_texto


def main():
    if len(sys.argv) < 2:
        print("Uso: python analiza-rotacion-textos.py <archivo.dxf> [<salida.json>]")
        sys.exit(1)

    dxf_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else dxf_path.with_suffix(".rotacion.json")

    doc = ezdxf.readfile(str(dxf_path))
    msp = doc.modelspace()

    rep = {
        "archivo": str(dxf_path),
        "insunits": doc.header.get("$INSUNITS", None),
        "limites": {
            "extmin": list(doc.header.get("$EXTMIN", [])),
            "extmax": list(doc.header.get("$EXTMAX", [])),
        },
        "layouts": [],
        "capas_con_textos_rotados": {},
        "capas_con_inserts_rotados": {},
        "bloques_con_texto": [],
        "resumen_rotaciones": {},
    }

    # Layouts y viewports
    for layout in doc.layouts:
        ps = layout.query("VIEWPORT")
        entrada = {
            "nombre": layout.name,
            "entidades": entidades_por_tipo(layout),
            "viewports": viewports_de(layout) if layout.name != "Model" else [],
        }
        rep["layouts"].append(entrada)

    # Textos y bloques del model space
    textos = textos_rotados(msp)
    inserts = inserts_rotados(msp)

    for capa, lista in textos.items():
        con_rot = [t for t in lista if abs(t["rot"] or 0) > 0.001]
        if con_rot:
            rep["capas_con_textos_rotados"][capa] = {
                "total_textos": len(lista),
                "rotados": len(con_rot),
                "angulos": dict(Counter(t["rot"] for t in con_rot)),
                "muestra": con_rot[:8],
            }

    for capa, lista in inserts.items():
        con_rot = [i for i in lista if abs(i["rot"] or 0) > 0.001]
        if con_rot:
            rep["capas_con_inserts_rotados"][capa] = {
                "total_inserts": len(lista),
                "rotados": len(con_rot),
                "angulos": dict(Counter(i["rot"] for i in con_rot)),
                "bloques": dict(Counter(i["bloque"] for i in con_rot)),
                "muestra": con_rot[:8],
            }

    rep["bloques_con_texto"] = bloques_con_texto(doc)

    # Resumen global de angulos de texto por capa (incluye rot=0 para ver el estado)
    rep["resumen_rotaciones"] = {
        capa: dict(Counter(t["rot"] for t in lista))
        for capa, lista in textos.items()
    }

    out_path.write_text(json.dumps(rep, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(f"OK -> {out_path}")
    print(f"Layouts: {[l['nombre'] for l in rep['layouts']]}")
    for lay in rep["layouts"]:
        for vp in lay["viewports"]:
            print(f"  {lay['nombre']}: viewport {vp['handle']} twist={vp['twist_grados']} "
                  f"escala~{vp['escala']}")
    print(f"Capas con textos rotados: {list(rep['capas_con_textos_rotados'])}")
    print(f"Capas con inserts rotados: {list(rep['capas_con_inserts_rotados'])}")


if __name__ == "__main__":
    main()
