"""
NOTA ES: Script de auditoria DWG via COM directo contra AutoCAD abierto.
NOTA ES: Usa pywin32 (ya instalado en el venv de limuzi013).
NOTA ES: No necesita el MCP — abre la sesion AutoCAD, enumera layouts,
NOTA ES: layers, bloques y entidades en model space.
NOTA ES: Salida JSON + Markdown a raw/reports/.
"""

import sys
import json
from datetime import datetime
from pathlib import Path
from collections import Counter

import win32com.client

SPEC_LAYERS = [
    ("R-EJES",   3, "CONTINUOUS", 0.50, "Ejes de replanteo principales"),
    ("R-EJAX",   8, "DASHED",     0.25, "Ejes auxiliares"),
    ("R-COTP",   6, "CONTINUOUS", 0.25, "Cotas parciales"),
    ("R-COTA",   6, "CONTINUOUS", 0.35, "Cotas acumuladas"),
    ("R-PTOS",   4, "CONTINUOUS", 0.25, "Puntos con coordenadas"),
    ("R-NIVE",   5, "CONTINUOUS", 0.35, "Cotas de nivel"),
    ("R-FUND",  252, "CONTINUOUS", 0.50, "Fundacion (xref S-FUND)"),
    ("G-CART",    7, "CONTINUOUS", 0.50, "Caratula"),
    ("G-MARC",    7, "CONTINUOUS", 0.25, "Marco y rotulo"),
    ("G-TEXT",    7, "CONTINUOUS", 0.25, "Texto general"),
    ("G-COTA",    2, "CONTINUOUS", 0.25, "Cotas generales"),
    ("G-REFE",    9, "DASHED",     0.25, "Referencias de corte/detalle"),
    ("G-VPRT",    8, "CONTINUOUS", 0.18, "Ventanas graficas (no imprimible)"),
    ("G-AUXI",  250, "CONTINUOUS", 0.18, "Construccion auxiliar (no imprimible)"),
    ("A-MURO",    1, "CONTINUOUS", 0.50, "Muros"),
    ("A-TABI",    1, "CONTINUOUS", 0.35, "Tabiques"),
    ("A-ABER",    1, "CONTINUOUS", 0.25, "Aberturas"),
    ("A-LOCA",    7, "CONTINUOUS", 0.25, "Rotulos de locales"),
    ("S-EJES",    3, "CONTINUOUS", 0.35, "Ejes estructurales"),
    ("S-FUND",    1, "CONTINUOUS", 0.50, "Fundaciones estructurales"),
    ("S-COLU",    1, "CONTINUOUS", 0.50, "Columnas"),
    ("S-VIGA",    1, "CONTINUOUS", 0.50, "Vigas"),
]

OBJECT_NAME_BY_TYPE = {
    "AcDbLine": "LINE",
    "AcDbPolyline": "POLYLINE",
    "AcDb2dPolyline": "POLYLINE",
    "AcDbMText": "MTEXT",
    "AcDbText": "TEXT",
    "AcDbBlockReference": "INSERT",
    "AcDbAlignedDimension": "DIM",
    "AcDbRotatedDimension": "DIM",
    "AcDbCircle": "CIRCLE",
    "AcDbArc": "ARC",
    "AcDbHatch": "HATCH",
    "AcDbPoint": "POINT",
    "AcDbSolid": "SOLID",
    "AcDbFace": "3DFACE",
    "AcDbSpline": "SPLINE",
}


def main():
    print("Conectando a AutoCAD via COM...")
    acad = win32com.client.GetObject(Class="AutoCAD.Application")
    acad.Visible = True
    if acad.Documents.Count == 0:
        print("ERROR: AutoCAD no tiene documentos abiertos.")
        sys.exit(1)
    doc = acad.ActiveDocument
    import time
    time.sleep(0.5)  # dejar asentar el COM si el MCP ya tenía un handle
    name = doc.Name
    path = doc.FullName

    # Si el documento activo no es el que queremos, abrir REP-ARAOZ.copia-trabajo.dwg
    target_name = "REP-ARAOZ.copia-trabajo.dwg"
    if name != target_name:
        target_path = r"P:\00-repos\proyecto-pi\vault-arquitectura\activos\caddy-salidas\REP-ARAOZ.copia-trabajo.dwg"
        print(f"  Active doc es {name}, abriendo {target_path}")
        try:
            doc = acad.Documents.Open(target_path)
            acad.ActiveDocument = doc
            name = doc.Name
            path = doc.FullName
            print(f"  Abierto: {name}")
        except Exception as e:
            print(f"  ERROR abriendo {target_path}: {e}")
            print(f"  Continuo con el documento activo: {name}")
    print(f"  DWG activo: {name}")
    print(f"  Path: {path}")

    rep = {
        "archivo": name,
        "path": path,
        "fecha": datetime.now().isoformat(timespec="seconds"),
        "autocad_version": acad.Version,
        "insunits": None,
        "extmin": None,
        "extmax": None,
        "layouts": [],
        "layers": [],
        "blocks_defined": [],
        "entities_per_type": {},
        "entities_per_layer": {},
        "entities_per_layer_type": {},
        "sample_texts": [],
    }

    try:
        rep["insunits"] = doc.GetVariable("INSUNITS")
    except Exception as e:
        rep["insunits_error"] = str(e)
    try:
        rep["extmin"] = list(doc.GetVariable("EXTMIN"))
        rep["extmax"] = list(doc.GetVariable("EXTMAX"))
    except Exception as e:
        rep["extents_error"] = str(e)

    # Layouts
    for layout in doc.Layouts:
        info = {
            "name": layout.Name,
            "tab_order": layout.TabOrder,
            "is_model": layout.ModelType,
            "active": layout.Name == doc.ActiveLayout.Name,
        }
        rep["layouts"].append(info)

    # Layers
    for lay in doc.Layers:
        try:
            rep["layers"].append({
                "name": lay.Name,
                "color_aci": lay.Color,
                "linetype": lay.Linetype,
                "frozen": bool(lay.Freeze),
                "locked": bool(lay.Lock),
                "visible": bool(lay.Visible if hasattr(lay, "Visible") else (not lay.LayerOn * 0 + 1)),
                "on": bool(lay.LayerOn),
            })
        except Exception as e:
            print(f"  warn layer {lay.Name}: {e}")

    # Bloques definidos
    try:
        for blk in doc.Blocks:
            name_b = blk.Name
            if name_b in ("*Model_Space", "*Paper_Space") or name_b.startswith("*Model") or name_b.startswith("*Paper"):
                continue
            try:
                count = blk.Count
            except Exception:
                count = None
            rep["blocks_defined"].append({"name": name_b, "entity_count": count})
    except Exception as e:
        rep["blocks_error"] = str(e)

    # Entidades en model space
    print("  Contando entidades en model space (puede tardar)...")
    model = doc.ModelSpace
    total = model.Count
    print(f"  Total entidades: {total}")
    type_counter = Counter()
    layer_counter = Counter()
    layer_type = {}
    texts = []
    inserts = []
    for i in range(total):
        try:
            e = model.Item(i)
            ot = e.ObjectName
            t = OBJECT_NAME_BY_TYPE.get(ot, ot)
            layer = e.Layer if hasattr(e, "Layer") else "?"
            type_counter[t] += 1
            layer_counter[layer] += 1
            layer_type.setdefault(layer, Counter())[t] += 1
            if t == "TEXT" and len(texts) < 25:
                try:
                    texts.append((layer, e.TextString))
                except Exception:
                    pass
            if t == "INSERT" and len(inserts) < 50:
                try:
                    ins_pt = list(e.InsertionPoint)
                    inserts.append((layer, e.Name, ins_pt))
                except Exception:
                    pass
        except Exception as e:
            print(f"  warn entidad {i}: {e}")

    rep["entities_total"] = total
    rep["entities_per_type"] = dict(type_counter)
    rep["entities_per_layer"] = dict(layer_counter)
    rep["entities_per_layer_type"] = {k: dict(v) for k, v in layer_type.items()}
    rep["sample_texts"] = texts
    rep["sample_inserts"] = inserts

    # Guardar
    out_dir = Path("raw/reports")
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(name).stem
    json_path = out_dir / f"audit-{stem}.json"
    md_path = out_dir / f"audit-{stem}.md"
    json_path.write_text(json.dumps(rep, indent=2, default=str), encoding="utf-8")
    print(f"OK json -> {json_path}")

    # Delta vs spec
    spec_names = {row[0] for row in SPEC_LAYERS}
    layer_names = {L["name"] for L in rep["layers"]}
    missing = sorted(spec_names - layer_names)
    extra = sorted(layer_names - spec_names)
    matches = []
    spec_lookup = {row[0]: row for row in SPEC_LAYERS}
    for L in rep["layers"]:
        n = L["name"]
        if n in spec_lookup:
            s_color, s_ltype, s_lw, _ = spec_lookup[n][1:]
            ok_c = L["color_aci"] == s_color
            ok_l = (L["linetype"] or "").upper() == s_ltype.upper()
            matches.append((n, L["color_aci"], s_color, L["linetype"], s_ltype, ok_c and ok_l))

    # Markdown resumen
    md = []
    md.append(f"# Auditoria {stem} via COM directo\n")
    md.append(f"- AutoCAD version: **{rep['autocad_version']}**")
    md.append(f"- DWG activo: `{name}`")
    md.append(f"- Path: `{path}`")
    md.append(f"- INSUNITS: `{rep.get('insunits')}`")
    md.append(f"- EXTMIN: `{rep.get('extmin')}`")
    md.append(f"- EXTMAX: `{rep.get('extmax')}`")
    md.append(f"- Total entidades model: **{rep['entities_total']}**")
    md.append(f"- Layers: **{len(rep['layers'])}**")
    md.append(f"- Bloques definidos: **{len(rep['blocks_defined'])}**")
    md.append("")
    md.append(f"## Layouts\n")
    for L in rep["layouts"]:
        md.append(f"- `{L['name']}` {'(Model)' if L['is_model'] else '(Paper)'} {'ACTIVO' if L['active'] else ''}")
    md.append("")
    md.append(f"## Capas vs spec SET_01 (22 esperadas)\n")
    md.append(f"- Faltan del spec: {len(missing)} -> {missing}")
    md.append(f"- Sobrantes (no en spec): {len(extra)}")
    md.append(f"- Match exacto: {sum(1 for m in matches if m[5])}/{len(matches)}")
    md.append("")
    md.append("### Detalle capas (todas las del DWG)\n")
    md.append("| Capa | Color | Linetype | On | Frozen | Locked |")
    md.append("|---|---|---|---|---|---|")
    for L in rep["layers"]:
        md.append(f"| `{L['name']}` | {L['color_aci']} | `{L['linetype']}` | {L['on']} | {L['frozen']} | {L['locked']} |")
    md.append("")
    md.append("### Entidades por tipo\n")
    md.append("| Tipo | Cantidad |")
    md.append("|---|---|")
    for t, c in sorted(type_counter.items(), key=lambda kv: -kv[1]):
        md.append(f"| `{t}` | {c} |")
    md.append("")
    md.append("### Entidades por capa (top 20)\n")
    md.append("| Capa | Total |")
    md.append("|---|---|")
    for capa, total in sorted(layer_counter.items(), key=lambda kv: -kv[1])[:20]:
        md.append(f"| `{capa}` | {total} |")
    md.append("")
    md.append("### Bloques definidos (top 20 por nombre)\n")
    md.append("| Bloque | Entities |")
    md.append("|---|---|")
    for b in rep["blocks_defined"][:20]:
        md.append(f"| `{b['name']}` | {b['entity_count']} |")
    md.append("")
    if texts:
        md.append("### Muestra de textos (TEXT)\n")
        for capa, txt in texts:
            md.append(f"- `{capa}` -> {txt!r}")
        md.append("")
    if inserts:
        md.append("### Muestra de inserts (INSERT)\n")
        md.append("| Capa | Bloque | Insercion |")
        md.append("|---|---|---|")
        for capa, blk, pt in inserts[:20]:
            md.append(f"| `{capa}` | `{blk}` | {pt} |")
        md.append("")

    md_path.write_text("\n".join(md), encoding="utf-8")
    print(f"OK md   -> {md_path}")


if __name__ == "__main__":
    main()
