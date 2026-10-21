"""
NOTA ES: Extractor de ATRIBUTOS de bloques a planillas (CSV + Markdown + JSON).
NOTA ES: Lee un DWG (convirtiendo con ODA File Converter) o un DXF directo,
NOTA ES: y vuelca los valores de los atributos de cada bloque, agrupados por capa.
NOTA ES:
NOTA ES: PARA QUE SERVE:
NOTA ES:   - Cuadro de carpinterias (vanos): TIPO / ANCHO / PUERTA / ALFEIZAR / ALTURA
NOTA ES:   - Cuadro de muros:  MURO (M1, M2, M3...)
NOTA ES:   - Cuadro de locales: DESCRIPCION + No (capa A-SIMBOLO-NPT-PLANTA)
NOTA ES:   - Cuadro de ejes:   EJE
NOTA ES:   Ojo: NO hace la cuenta de metros de muro (eso hay que sacarlo de la
NOTA ES:   geometria, no del atributo).
NOTA ES:
NOTA ES: USO:
NOTA ES:   python extrae-atributos-dwg.py <archivo.dwg|dxf> [--salida DIR] [--post-n8n]
NOTA ES:
NOTA ES: REQUISITOS:
NOTA ES:   - Python 3.10+ con ezdxf (pip install ezdxf)
NOTA ES:   - ODA File Converter solo si la entrada es .dwg
NOTA ES:     (busca "C:\\Program Files\\ODA\\ODAFileConverter *\\ODAFileConverter.exe")
NOTA ES:   - Para --post-n8n: acceso al webhook del estudio
NOTA ES:     (ver docs/cuadro-carpinterias.md del SET_01-REP)
"""

import argparse
import csv
import json
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import ezdxf

# Capas del SET_01-REP con atributosinteresting (lo que el estudio necesita medir).
CAPAS_INTERES = [
    "A-CARP-02",               # vanos: ventanas y puertas
    "SIMB-MURO",               # tags de muro (M1, M2, M3...)
    "A-SIMBOLO-NPT-PLANTA",    # rotulos de locales (DESCRIPCION + No)
    "E-EJES",                  # marcas de eje (EJE)
    "E-COL",                   # columnas (C40.20)
]


def normaliza_tag(tag):
    """Deja los nombres de atributo en ASCII y sin acentos.

    En el DWG conviven 'DESCRIPCIÓN' (con tilde) y 'DESCRIPCION' (sin tilde),
    y el numero de local es 'Nº' o 'N°' segun como se haya creado el bloque.
    Normalizar evita columnas duplicadas o vacias en la planilla.
    """
    t = unicodedata.normalize("NFKD", tag).encode("ascii", "ignore").decode("ascii")
    t = t.strip().upper()
    if t in ("NO", "N", "NUM", "NUMERO"):
        return "N"
    return t


def g(ent, nombre, default=None):
    """Lee un atributo DXF sin romper si la entidad no lo define."""
    try:
        return ent.dxf.get(nombre, default)
    except Exception:
        return default


def encuentra_oda():
    """Ruta del ODA File Converter (busca por version carpeta)."""
    base = Path(r"C:\Program Files\ODA")
    if not base.exists():
        return None
    candidatos = sorted(base.glob("ODAFileConverter*/ODAFileConverter.exe"))
    return str(candidatos[-1]) if candidatos else None


def dwg_a_dxf(dwg, destino):
    """Convierte un .dwg a .dxf con ODA File Converter y devuelve el DXF."""
    oda = encuentra_oda()
    if not oda:
        raise SystemExit("No se encontro ODA File Converter. Pasame un .dxf o instalalo.")
    entrada = destino / "in"
    salida = destino / "out"
    entrada.mkdir(parents=True, exist_ok=True)
    salida.mkdir(parents=True, exist_ok=True)
    shutil.copy2(dwg, entrada / dwg.name)
    # ODAFileConverter: <in> <out> <version> <tipo> <recurse> <audit> <filtro>
    subprocess.run([oda, str(entrada), str(salida), "ACAD2018", "DXF", "0", "1", "*.dwg"],
                   check=True, capture_output=True)
    dxf = salida / (dwg.stem + ".dxf")
    if not dxf.exists():
        raise SystemExit("La conversion no produjo %s" % dxf)
    return dxf


def filas_de_capa(msp, capa):
    """Una fila por INSERT de la capa, con sus atributos y su geometria."""
    filas = []
    for e in msp.query("INSERT"):
        if e.dxf.layer != capa:
            continue
        fila = {
            "capa": capa,
            "bloque": e.dxf.name,
            "rot_grados": round(g(e, "rotation", 0.0), 2),
            "x": round(e.dxf.insert[0], 3),
            "y": round(e.dxf.insert[1], 3),
            "handle": e.dxf.handle,
        }
        for a in e.attribs:
            fila[normaliza_tag(a.dxf.tag)] = a.dxf.text
        filas.append(fila)
    return filas


def columnas_de(filas):
    """Orden de columnas: primero las fijas, despues los tags de atributo."""
    fijas = ["capa", "bloque", "rot_grados", "x", "y", "handle"]
    tags = []
    for f in filas:
        for k in f:
            if k not in fijas and k not in tags:
                tags.append(k)
    return fijas + tags


def escribe_csv(ruta, filas):
    if not filas:
        return None
    cols = columnas_de(filas)
    with open(ruta, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    return cols


def resumen_agrupado(filas, tags):
    """Cuenta por combinacion de valores de los tags indicados."""
    c = Counter()
    for f in filas:
        clave = " | ".join("%s=%s" % (t, f.get(t, "")) for t in tags)
        c[clave] += 1
    return c


def main():
    ap = argparse.ArgumentParser(description="Extrae atributos de bloques a planillas")
    ap.add_argument("archivo", help="archivo .dwg o .dxf")
    ap.add_argument("--salida", default=".", help="carpeta de salida")
    ap.add_argument("--post-n8n", action="store_true", help="manda el CSV de carpinterias al webhook")
    args = ap.parse_args()

    origen = Path(args.archivo)
    if not origen.exists():
        raise SystemExit("No existe: %s" % origen)
    salida = Path(args.salida)
    salida.mkdir(parents=True, exist_ok=True)

    tmp = None
    if origen.suffix.lower() == ".dwg":
        tmp = Path(tempfile.mkdtemp(prefix="extrae-attrs-"))
        dxf = dwg_a_dxf(origen, tmp)
    else:
        dxf = origen

    doc = ezdxf.readfile(str(dxf))
    msp = doc.modelspace()
    ahora = datetime.now().isoformat(timespec="seconds")

    print("Fuente: %s" % origen)
    print("DXF  : %s" % dxf)
    print("INSUNITS=%s  (6 = metros)" % doc.header.get("$INSUNITS"))
    print()

    todas = {}
    for capa in CAPAS_INTERES:
        filas = filas_de_capa(msp, capa)
        if not filas:
            continue
        todas[capa] = filas
        csv_path = salida / ("atributos-%s.csv" % capa.lower())
        escribe_csv(csv_path, filas)
        print("== %-24s %3d bloques -> %s" % (capa, len(filas), csv_path.name))

    # Resumenes de negocio
    md = ["# Cuadros de atributos — %s" % origen.name, "",
          "> Extraído: %s · fuente: %s · INSUNITS=%s (metros)" % (ahora, origen, doc.header.get("$INSUNITS")), ""]

    if "A-CARP-02" in todas:
        carp = todas["A-CARP-02"]
        ventanas = [f for f in carp if "TIPO" in f]
        puertas = [f for f in carp if "PUERTA" in f]
        md += ["## Vanos — capa A-CARP-02", "",
               "### Ventanas (%d)" % len(ventanas), "",
               "| TIPO | ANCHO (m) | Cantidad |", "|---|---|---|"]
        for k, v in sorted(resumen_agrupado(ventanas, ["TIPO", "ANCHO"]).items()):
            md.append("| %s | %s |" % (k, v))
        md += ["", "### Puertas (%d)" % len(puertas), "",
               "| PUERTA | ANCHO | ALTURA | ALFEIZAR | DESCRIPCIÓN | Cantidad |",
               "|---|---|---|---|---|---|"]
        for k, v in sorted(resumen_agrupado(puertas, ["PUERTA", "ANCHO", "ALTURA", "ALFEIZAR", "DESCRIPCIÓN"]).items()):
            md.append("| %s | %s |" % (k, v))
        md.append("")

    if "SIMB-MURO" in todas:
        muros = todas["SIMB-MURO"]
        md += ["## Muros — capa SIMB-MURO (%d tags)" % len(muros), "",
               "| MURO | Cantidad |", "|---|---|"]
        for k, v in sorted(resumen_agrupado(muros, ["MURO"]).items()):
            md.append("| %s | %s |" % (k, v))
        md += ["", "Giros de los tags (siguen la dirección del muro):", "",
               "| Giro (°) | Cantidad |", "|---|---|"]
        for k, v in sorted(Counter(f["rot_grados"] for f in muros).items()):
            md.append("| %s | %s |" % (k, v))
        md.append("")

    if "A-SIMBOLO-NPT-PLANTA" in todas:
        loc = todas["A-SIMBOLO-NPT-PLANTA"]
        md += ["## Locales — capa A-SIMBOLO-NPT-PLANTA (%d rótulos)" % len(loc), "",
               "| Nº | DESCRIPCION | X | Y | Giro (°) |", "|---|---|---|---|---|"]
        for f in sorted(loc, key=lambda r: r.get("N", "")):
            md.append("| %s | %s | %s | %s | %s |" % (f.get("N", ""), f.get("DESCRIPCION", ""),
                                                     f["x"], f["y"], f["rot_grados"]))
        md += ["", "Por tipo de local:", "", "| DESCRIPCION | Cantidad |", "|---|---|"]
        for k, v in sorted(resumen_agrupado(loc, ["DESCRIPCION"]).items()):
            md.append("| %s | %s |" % (k, v))
        md.append("")

    if "E-EJES" in todas:
        ej = todas["E-EJES"]
        md += ["## Ejes — capa E-EJES (%d marcas)" % len(ej), "",
               "| EJE | X | Y |", "|---|---|---|"]
        for f in sorted(ej, key=lambda r: (r["y"], r["x"])):
            md.append("| %s | %s | %s |" % (f.get("EJE", ""), f["x"], f["y"]))
        md.append("")

    md_path = salida / "cuadros-atributos.md"
    md_path.write_text("\n".join(md), encoding="utf-8")
    print("\nResumen -> %s" % md_path)

    json_path = salida / "atributos.json"
    json_path.write_text(json.dumps({"fuente": str(origen), "fecha": ahora,
                                     "capas": todas}, indent=2, ensure_ascii=False, default=str),
                         encoding="utf-8")
    print("JSON   -> %s" % json_path)

    if args.post_n8n and "A-CARP-02" in todas:
        import urllib.request
        url = "https://n8n.pitau.tech/webhook/set01-carpinterias"
        carp = todas["A-CARP-02"]
        cols = columnas_de(carp)
        rows = [[c.get(c0, "") for c0 in cols] for c in carp]
        payload = json.dumps({"origen": origen.name, "fecha": ahora,
                               "header": cols, "rows": rows}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as r:
            print("n8n webhook -> %s %s" % (r.status, r.read().decode("utf-8", "replace")[:200]))

    if tmp:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
