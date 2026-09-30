"""
NOTA ES: Script didactico que audita un DWG de replanteo contra el spec del SET_01.
NOTA ES: Corre sin AutoCAD usando ezdxf (lee el archivo binario DWG directo).
NOTA ES: Salida: reporte Markdown con layers, entidades, bloques, unidades, layouts
NOTA ES: y delta contra las 22 capas del spec SET_01-REP §2.
"""

import sys
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

import ezdxf
from ezdxf.enums import TextEntityAlignment

SPEC_LAYERS = [
    # SET-REP nucleo (7)
    ("R-EJES",   3, "CONTINUOUS", 0.50, "Ejes de replanteo principales"),
    ("R-EJAX",   8, "DASHED",     0.25, "Ejes auxiliares"),
    ("R-COTP",   6, "CONTINUOUS", 0.25, "Cotas parciales"),
    ("R-COTA",   6, "CONTINUOUS", 0.35, "Cotas acumuladas"),
    ("R-PTOS",   4, "CONTINUOUS", 0.25, "Puntos con coordenadas"),
    ("R-NIVE",   5, "CONTINUOUS", 0.35, "Cotas de nivel"),
    ("R-FUND",  252, "CONTINUOUS", 0.50, "Fundacion (xref S-FUND)"),
    # GEN comunes (7)
    ("G-CART",    7, "CONTINUOUS", 0.50, "Caratula"),
    ("G-MARC",    7, "CONTINUOUS", 0.25, "Marco y rotulo"),
    ("G-TEXT",    7, "CONTINUOUS", 0.25, "Texto general"),
    ("G-COTA",    2, "CONTINUOUS", 0.25, "Cotas generales"),
    ("G-REFE",    9, "DASHED",     0.25, "Referencias de corte/detalle"),
    ("G-VPRT",    8, "CONTINUOUS", 0.18, "Ventanas graficas (no imprimible)"),
    ("G-AUXI",  250, "CONTINUOUS", 0.18, "Construccion auxiliar (no imprimible)"),
    # ARQ referenciadas (4)
    ("A-MURO",    1, "CONTINUOUS", 0.50, "Muros"),
    ("A-TABI",    1, "CONTINUOUS", 0.35, "Tabiques"),
    ("A-ABER",    1, "CONTINUOUS", 0.25, "Aberturas"),
    ("A-LOCA",    7, "CONTINUOUS", 0.25, "Rotulos de locales"),
    # EST referenciadas (4)
    ("S-EJES",    3, "CONTINUOUS", 0.35, "Ejes estructurales"),
    ("S-FUND",    1, "CONTINUOUS", 0.50, "Fundaciones estructurales"),
    ("S-COLU",    1, "CONTINUOUS", 0.50, "Columnas"),
    ("S-VIGA",    1, "CONTINUOUS", 0.50, "Vigas"),
]

def audit(dwg_path: Path) -> dict:
    doc = ezdxf.readfile(str(dwg_path))
    msp = doc.modelspace()

    # 1. Metadata + unidades
    units = doc.units  # ezdxf enum
    insunits = doc.header.get("$INSUNITS", "?")
    measurement = doc.header.get("$MEASUREMENT", "?")
    extmin = doc.header.get("$EXTMIN", "?")
    extmax = doc.header.get("$EXTMAX", "?")

    # 2. Layouts
    layouts = []
    for layout in doc.layouts:
        if layout.name == "Model":
            continue
        layouts.append(layout.name)

    # 3. Layers: existentes en el DWG
    existing_layers = []
    for layer in doc.layers:
        existing_layers.append({
            "name": layer.dxf.name,
            "color": layer.dxf.color,
            "linetype": layer.dxf.linetype,
            "on": layer.is_on(),
            "frozen": layer.is_frozen(),
            "locked": layer.is_locked(),
        })

    spec_names = {row[0] for row in SPEC_LAYERS}
    existing_names = {row["name"] for row in existing_layers}

    # 4. Conteo de entidades por tipo y por capa
    entity_types = Counter()
    per_layer_count = Counter()
    per_layer_types = {}
    text_contents = []
    insert_blocks = []
    mtext_count = 0

    for e in msp:
        t = e.dxftype()
        entity_types[t] += 1
        layer = e.dxf.layer if hasattr(e.dxf, "layer") else "?"
        per_layer_count[layer] += 1
        per_layer_types.setdefault(layer, Counter())[t] += 1
        if t == "TEXT":
            try:
                text_contents.append((layer, e.dxf.text))
            except Exception:
                pass
        if t == "INSERT":
            try:
                insert_blocks.append((layer, e.dxf.name, e.dxf.insert))
            except Exception:
                pass
        if t == "MTEXT":
            mtext_count += 1

    # 5. Bloques definidos
    defined_blocks = sorted(doc.blocks.names())

    # 6. Delta contra spec
    missing = sorted(spec_names - existing_names)
    extra = sorted(existing_names - spec_names)
    spec_lookup = {row[0]: row for row in SPEC_LAYERS}

    layer_detalle = []
    for L in existing_layers:
        name = L["name"]
        if name in spec_lookup:
            s_color, s_ltype, s_lw, _ = spec_lookup[name][1:]
            ok_color = L["color"] == s_color
            ok_ltype = (L["linetype"] or "").upper() == s_ltype.upper()
            layer_detalle.append({
                "name": name,
                "color_dwg": L["color"],
                "color_spec": s_color,
                "ok_color": ok_color,
                "linetype_dwg": L["linetype"],
                "linetype_spec": s_ltype,
                "ok_ltype": ok_ltype,
                "estado": "OK" if (ok_color and ok_ltype) else "DELTA",
            })

    return {
        "archivo": dwg_path.name,
        "fecha": datetime.now().isoformat(timespec="seconds"),
        "ezdxf_version": ezdxf.__version__,
        "units": str(units),
        "insunits": insunits,
        "measurement": measurement,
        "extmin": list(extmin) if isinstance(extmin, tuple) else extmin,
        "extmax": list(extmax) if isinstance(extmax, tuple) else extmax,
        "layouts": layouts,
        "layers_total": len(existing_layers),
        "layers_existentes": existing_layers,
        "layers_delta_ok": [d for d in layer_detalle if d["estado"] == "OK"],
        "layers_delta_ko": [d for d in layer_detalle if d["estado"] == "DELTA"],
        "missing": missing,
        "extra": extra,
        "entity_types": dict(entity_types),
        "per_layer_count": dict(per_layer_count),
        "per_layer_types": {k: dict(v) for k, v in per_layer_types.items()},
        "defined_blocks": defined_blocks,
        "insert_blocks_count": len(insert_blocks),
        "mtext_count": mtext_count,
        "text_ejemplos": text_contents[:15],
    }


def to_markdown(rep: dict) -> str:
    L = []
    L.append(f"# Auditoria DWG vs SET_01-REP")
    L.append("")
    L.append(f"- **Archivo:** `{rep['archivo']}`")
    L.append(f"- **Fecha:** {rep['fecha']}")
    L.append(f"- **ezdxf:** {rep['ezdxf_version']}")
    L.append(f"- **Unidad drawing (ezdxf):** `{rep['units']}`")
    L.append(f"- **`$INSUNITS`:** `{rep['insunits']}`  (4=mm, 6=m)")
    L.append(f"- **`$MEASUREMENT`:** `{rep['measurement']}`  (0=imperial, 1=metric)")
    L.append(f"- **`$EXTMIN`:** `{rep['extmin']}`")
    L.append(f"- **`$EXTMAX`:** `{rep['extmax']}`")
    L.append("")
    L.append(f"## Layouts (paper-space, no Model)")
    L.append("")
    if rep["layouts"]:
        for ln in rep["layouts"]:
            L.append(f"- `{ln}`")
    else:
        L.append("- _Sin layouts definidos_ (recomendado crear `REP-A1` con plantilla)")
    L.append("")
    L.append("## Capas contra spec SET_01 (22 esperadas)")
    L.append("")
    L.append(f"- **Existentes en DWG:** {rep['layers_total']}")
    L.append(f"- **Faltan del spec:** {len(rep['missing'])} -> {rep['missing'] or 'ninguna'}")
    L.append(f"- **Sobrantes (no en spec):** {len(rep['extra'])} -> {rep['extra'] or 'ninguna'}")
    L.append(f"- **OK (color + linetype coinciden):** {len(rep['layers_delta_ok'])}")
    L.append(f"- **DELTA (color o linetype distinto):** {len(rep['layers_delta_ko'])}")
    L.append("")
    L.append("### Detalle por capa (existentes en DWG)")
    L.append("")
    L.append("| Capa | Color DWG | Color spec | Linetype DWG | Linetype spec | Estado |")
    L.append("|---|---|---|---|---|---|")
    for d in rep["layers_delta_ok"] + rep["layers_delta_ko"]:
        L.append(f"| `{d['name']}` | {d['color_dwg']} | {d['color_spec']} | `{d['linetype_dwg']}` | `{d['linetype_spec']}` | {d['estado']} |")
    L.append("")
    L.append("## Entidades en model space")
    L.append("")
    L.append("| Tipo | Cantidad |")
    L.append("|---|---|")
    for t, c in sorted(rep["entity_types"].items(), key=lambda kv: -kv[1]):
        L.append(f"| `{t}` | {c} |")
    L.append("")
    L.append("## Entidades por capa")
    L.append("")
    L.append("| Capa | Total | Tipos |")
    L.append("|---|---|---|")
    for capa, total in sorted(rep["per_layer_count"].items(), key=lambda kv: -kv[1]):
        tipos = ", ".join(f"{t}={c}" for t, c in rep["per_layer_types"][capa].items())
        L.append(f"| `{capa}` | {total} | {tipos} |")
    L.append("")
    L.append("## Bloques")
    L.append("")
    L.append(f"- **Definidos en DWG:** {len(rep['defined_blocks'])}")
    L.append(f"- **Inserts (`INSERT`) usados:** {rep['insert_blocks_count']}")
    if rep["defined_blocks"]:
        L.append("- Lista:")
        for b in rep["defined_blocks"]:
            L.append(f"  - `{b}`")
    L.append("")
    L.append("## Texto (TEXT / MTEXT)")
    L.append("")
    L.append(f"- **`TEXT` count (via entidades iteradas):** _incluido arriba_")
    L.append(f"- **`MTEXT` count:** {rep['mtext_count']}")
    if rep["text_ejemplos"]:
        L.append("")
        L.append("### Muestra de textos (capa, contenido)")
        for capa, txt in rep["text_ejemplos"]:
            L.append(f"- `{capa}` -> {txt!r}")
    L.append("")
    L.append("## Areas de mejora")
    L.append("")
    L = _append_areas_mejora(L, rep)
    L.append("## Automatizacion sugerida")
    L.append("")
    L = _append_automatizacion(L, rep)
    return "\n".join(L)


def _append_areas_mejora(L, rep):
    L.append("### Lo que se llego a hacer")
    if rep["layers_total"] > 0:
        L.append(f"- DWG con {rep['layers_total']} capas y {sum(rep['entity_types'].values())} entidades; cubre el SET_REP.")
    if rep["defined_blocks"]:
        L.append(f"- Bloques definidos: {len(rep['defined_blocks'])}.")
    L.append("")
    L.append("### Gaps contra SET_01")
    if rep["missing"]:
        L.append(f"- **Faltan del spec:** {', '.join('`'+n+'`' for n in rep['missing'])}.")
    if rep["extra"]:
        L.append(f"- **Capas fuera del spec:** {', '.join('`'+n+'`' for n in rep['extra'])} (revisar uso real).")
    if rep["layers_delta_ko"]:
        nombres = ", ".join("`"+d['name']+"`" for d in rep["layers_delta_ko"])
        L.append(f"- **Capas con color o linetype distinto al spec:** {nombres}.")
    if not rep["layouts"]:
        L.append("- **Sin layouts (paper-space).** SET_01 define layout `REP-A1` en A1 apaisado con viewport 1:50.")
    if rep["mtext_count"] == 0:
        L.append("- **Sin `MTEXT`.** Si tenes descripciones largas conviene migrar de `TEXT` a `MTEXT`.")
    if rep["insert_blocks_count"] == 0:
        L.append("- **Sin inserts de bloques.** SET_01 pide `R-EJE-MARCA`, `R-PTO-ATTR`, etc.")
    L.append("")
    return L


def _append_automatizacion(L, rep):
    L.append("### AutoLISP (scripts `lisp/`)")
    L.append("- **Aplicador de spec:** `SET-01-REP` crea las 22 capas (color/ltype/lineweight) segun `02-ft-SET_01.md` §1 y spec §2. Idempotente: si existe, no la duplica.")
    L.append("- **LAYER audits:** `AUDIT-LAYERS` compara el dibujo activo contra `EP-REP.dws` y reporta delta (coincide / falta / sobra) via `acet-laytrans` o `LAYTRANS` UI.")
    L.append("- **Bloques con atributos:** `MK-R-PTO` inserta `R-PTO-ATTR` con prompts ID,X,Y,Z y aplica `R-PTOS`.")
    L.append("- **Bloques dinamicos:** puerta (`R-ABER-DYN`) con parametros Linear + Visibility (abierta/cerrada/90).")
    L.append("")
    L.append("### Botonera (paleta CUI/.cui o `.cuix`)")
    L.append("- Cargar desde W03-CAD; agrega botones para `SET-01-REP`, `AUDIT-LAYERS`, `MK-R-PTO`, `R-EJE-MARCA`.")
    L.append("")
    L.append("### DWS (Drawing Standards)")
    L.append("- `EP-REP.dws` con las 22 capas, estilos de texto y de cota del SET; verificar con `CHECKSTANDARDS` y Batch Standards Checker (`.chx`).")
    L.append("")
    L.append("### DWT (template)")
    L.append("- `EP-REP.dwt`: DWGUNITS 6 (m), INSUNITS 6, layout `REP-A1` A1 apaisado con viewport a 1:50 Display Locked, escala custom `1:50 (m)` en `SCALELISTEDIT`.")
    L.append("")
    L.append("### Bloques dinamicos")
    L.append("- `R-EJE-MARCA` (letra o numero), `R-PTO-ATTR` (ID/X/Y/Z), `R-NIVEL-TAG` (cota).")
    L.append("- `R-ABER-DYN` puerta con Visibility States (0.60 / 0.70 / 0.80 / 0.90 / 1.00 m).")
    L.append("")
    L.append("### Extraccion de datos (planillas)")
    L.append("- `DATAEXTRACTION` desde bloques con atributos `R-PTO-ATTR` -> CSV/XLS de coordenadas replanteo.")
    L.append("- `EATTEXT` / `ATTEXT` (CDF/CSV) si no se quiere la UI.")
    L.append("")
    L.append("### Auditoria viva (MCP `autocad`)")
    L.append("- `list_layers` + `query_entities(layer=R-EJES)` -> comparar contra este spec.")
    L.append("- `autodesk-help_search_help_content` con `product_code=ACD, release_code=2027, locale=es_ES` para citas oficiales.")
    L.append("")
    return L


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python audita-dwg.py <archivo.dwg> [salida.md]")
        sys.exit(1)
    src = Path(sys.argv[1])
    if not src.exists():
        print(f"No existe: {src}")
        sys.exit(2)
    rep = audit(src)
    md = to_markdown(rep)
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".audit.md")
    out.write_text(md, encoding="utf-8")
    print(f"OK -> {out}")
    # Ademas volcar JSON para procesamiento posterior
    json_out = out.with_suffix(".json")
    json_out.write_text(json.dumps(rep, indent=2, default=str), encoding="utf-8")
    print(f"OK -> {json_out}")
