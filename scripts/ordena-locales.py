"""
NOTA ES: Ordena los locales del plano de replanteo (izquierda a derecha,
NOTA ES: arriba a abajo) y arma la lista de insercion del bloque SIMB-LOC_ID.
NOTA ES:
NOTA ES: PARA QUE SERVE:
NOTA ES:   El bloque nuevo (SIMB-LOC_ID) lleva el numero del local (N_LOC) y
NOTA ES:   el nombre en un atributo invisible (TXT_LOC). Para que la numeracion
NOTA ES:   salga en orden de lectura (primero la fila de arriba, de izquierda a
NOTA ES:   derecha, despues la siguiente fila), hace falta un criterio claro.
NOTA ES:
NOTA ES: COMO FUNCIONA:
NOTA ES:   1. Lee el DWG (lo convierte con ODA File Converter) o un DXF.
NOTA ES:   2. Toma los locales: si ya existen ejemplares de SIMB-LOC_ID, usa
NOTA ES:      sus atributos (N_LOC / TXT_LOC); si no, usa los rótulos viejos
NOTA ES:      de la capa A-SIMBOLO-NPT-PLANTA (DESCRIPCION + Nº).
NOTA ES:   3. Agrupa en filas: dos locales son de la misma fila si la
NOTA ES:      diferencia de Y es menor a TOLERANCIA_FILA (0.30 m por defecto).
NOTA ES:   4. Dentro de cada fila ordena de izquierda a derecha (X growing).
NOTA ES:   5. Numera 01..N y escribe el resultado en Markdown y CSV.
NOTA ES:
NOTA ES: USO:
NOTA ES:   python ordena-locales.py <archivo.dwg|dxf> [--salida DIR] [--tol 0.30]
NOTA ES:   python ordena-locales.py <archivo.dwg|dxf> --check
NOTA ES:     --check solo VERIFICA que la numeracion de los bloques SIMB-LOC_ID
NOTA ES:     coincida con el orden de lectura (X+ / Y-) y no escribe archivos.
"""

import argparse
import csv
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import ezdxf

CAPA_LOCALES = "A-SIMBOLO-NPT-PLANTA"
BLOQUE_NUEVO = "SIMB-LOC_ID"


def normaliza_tag(tag):
    """'Nº' o 'N°' -> 'N'; 'DESCRIPCIÓN' -> 'DESCRIPCION'."""
    import unicodedata
    t = unicodedata.normalize("NFKD", tag).encode("ascii", "ignore").decode("ascii")
    t = t.strip().upper()
    if t in ("NO", "N", "NUM", "NUMERO"):
        return "N"
    return t


def g(ent, nombre, default=None):
    try:
        return ent.dxf.get(nombre, default)
    except Exception:
        return default


def encuentra_oda():
    base = Path(r"C:\Program Files\ODA")
    if not base.exists():
        return None
    cands = sorted(base.glob("ODAFileConverter*/ODAFileConverter.exe"))
    return str(cands[-1]) if cands else None


def dwg_a_dxf(dwg, destino):
    oda = encuentra_oda()
    if not oda:
        raise SystemExit("No se encontro ODA File Converter. Pasame un .dxf.")
    ent = destino / "in"
    sal = destino / "out"
    ent.mkdir(parents=True, exist_ok=True)
    sal.mkdir(parents=True, exist_ok=True)
    shutil.copy2(dwg, ent / dwg.name)
    subprocess.run([oda, str(ent), str(sal), "ACAD2018", "DXF", "0", "1", "*.dwg"],
                   check=True, capture_output=True)
    dxf = sal / (dwg.stem + ".dxf")
    if not dxf.exists():
        raise SystemExit("La conversion no produjo %s" % dxf)
    return dxf


def locales_del_dibujo(msp):
    """Devuelve (lista_de_locales, fuente_Usada).

    Cada local: dict con numero, nombre, x, y, bloque, giro, handle.
    Fuente preferida: ejemplares de SIMB-LOC_ID (N_LOC / TXT_LOC).
    Fuente de reserva: rótulos viejos de la capa (DESCRIPCION / N).
    """
    nuevos = []
    for e in msp.query("INSERT"):
        if e.dxf.name != BLOQUE_NUEVO:
            continue
        attrs = {normaliza_tag(a.dxf.tag): a.dxf.text for a in e.attribs}
        nuevos.append({
            "numero": attrs.get("N_LOC", ""),
            "nombre": attrs.get("TXT_LOC", ""),
            "x": round(e.dxf.insert[0], 3),
            "y": round(e.dxf.insert[1], 3),
            "bloque": e.dxf.name,
            "giro": round(g(e, "rotation", 0.0), 2),
            "handle": e.dxf.handle,
        })
    if nuevos:
        return nuevos, "SIMB-LOC_ID (N_LOC / TXT_LOC)"

    viejos = []
    for e in msp.query("INSERT"):
        if e.dxf.layer != CAPA_LOCALES:
            continue
        attrs = {normaliza_tag(a.dxf.tag): a.dxf.text for a in e.attribs}
        if "DESCRIPCION" not in attrs:
            continue
        viejos.append({
            "numero": attrs.get("N", ""),
            "nombre": attrs.get("DESCRIPCION", ""),
            "x": round(e.dxf.insert[0], 3),
            "y": round(e.dxf.insert[1], 3),
            "bloque": e.dxf.name,
            "giro": round(g(e, "rotation", 0.0), 2),
            "handle": e.dxf.handle,
        })
    return viejos, "rotulos %s (DESCRIPCION / N)" % CAPA_LOCALES


def en_filas(locales, tolerancia):
    """Agrupa en filas (mismo Y dentro de la tolerancia) y ordena izq->der."""
    if not locales:
        return []
    ys = sorted({l["y"] for l in locales}, reverse=True)
    filas = []
    for y in ys:
        members = [l for l in locales if abs(l["y"] - y) <= tolerancia]
        if not members:
            continue
        # una fila ya usada no se vuelve a agregar
        if any(m in [x for f in filas for x in f] for m in members):
            continue
        members.sort(key=lambda l: l["x"])
        filas.append(members)
    return filas


def control_orden(orden, filas):
    """Compara la numeracion de cada local con su posicion de lectura.

    Devuelve (desviaciones, sin_fila):
      - desviaciones: lista de (numero, nombre, x, y, numero_esperado)
      - sin_fila: locales que no entraron en ninguna fila
    """
    desviaciones = []
    for i, l in enumerate(orden, 1):
        esperado = "%02d" % i
        if l["numero"] != esperado:
            desviaciones.append((l["numero"], l["nombre"], l["x"], l["y"], esperado))
    en_filas = [l for f in filas for l in f]
    sin_fila = [l for l in orden if l not in en_filas]
    return desviaciones, sin_fila


def main():
    ap = argparse.ArgumentParser(description="Ordena los locales del replanteo")
    ap.add_argument("archivo", help="archivo .dwg o .dxf")
    ap.add_argument("--salida", default=".", help="carpeta de salida")
    ap.add_argument("--tol", type=float, default=0.30, help="tolerancia de fila en metros")
    ap.add_argument("--check", action="store_true",
                    help="solo verifica la numeracion contra el orden de lectura (no escribe archivos)")
    args = ap.parse_args()

    origen = Path(args.archivo)
    if not origen.exists():
        raise SystemExit("No existe: %s" % origen)
    salida = Path(args.salida)
    salida.mkdir(parents=True, exist_ok=True)

    tmp = None
    if origen.suffix.lower() == ".dwg":
        tmp = Path(tempfile.mkdtemp(prefix="ordena-locales-"))
        dxf = dwg_a_dxf(origen, tmp)
    else:
        dxf = origen

    doc = ezdxf.readfile(str(dxf))
    msp = doc.modelspace()
    locales, fuente = locales_del_dibujo(msp)

    if not locales:
        raise SystemExit("No se encontraron locales (ni %s ni rotulos en %s)"
                         % (BLOQUE_NUEVO, CAPA_LOCALES))

    filas = en_filas(locales, args.tol)
    orden = []
    for f in filas:
        orden.extend(f)

    # numeracion 01..N (se respeta el numero ya puesto si el bloque nuevo existe)
    usar_numeros_existentes = fuente.startswith(BLOQUE_NUEVO)
    for i, l in enumerate(orden, 1):
        l["orden"] = i
        if not usar_numeros_existentes:
            l["numero"] = "%02d" % i

    # --check: verificar la numeracion contra el orden de lectura y salir
    if args.check:
        desviaciones, sin_fila = control_orden(orden, filas)
        print("Fuente: %s" % fuente)
        print("Locales: %d en %d filas" % (len(orden), len(filas)))
        if usar_numeros_existentes:
            print("Numeracion: %s" % ("01..%02d" % len(orden) if not desviaciones
                                      else "FUERA DE ORDEN"))
        else:
            print("Numeracion: la fuente NO tiene bloque SIMB-LOC_ID -> los numeros "
                  "se reasignan por posicion, el control de orden no aplica.")
        for num, nombre, x, y, esperado in desviaciones:
            print("  FUERA DE ORDEN: N_LOC %s (%s) en (%.2f, %.2f) le corresponde %s"
                  % (num, nombre, x, y, esperado))
        for l in sin_fila:
            print("  SIN FILA: %s en (%.2f, %.2f): a mas de %.2f m de otra fila"
                  % (l["nombre"], l["x"], l["y"], args.tol))
        if not desviaciones and not sin_fila and usar_numeros_existentes:
            print("OK: los %d locales estan en orden de lectura (X+ / Y-)." % len(orden))
        return

    # control: repetidos
    nums = [l["numero"] for l in orden if l["numero"]]
    rep = sorted({n for n in nums if nums.count(n) > 1})
    vacios = [l for l in orden if not l["nombre"]]

    csv_path = salida / "orden-locales.csv"
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["orden", "N_LOC", "TXT_LOC", "x", "y", "giro", "bloque", "handle", "fila"])
        for i, l in enumerate(orden):
            fila = next((n + 1 for n, f in enumerate(filas) if l in f), 0)
            w.writerow([l["orden"], l["numero"], l["nombre"], l["x"], l["y"],
                        l["giro"], l["bloque"], l["handle"], fila])

    # Planilla de locales (mismos datos, en formato de cuadro)
    plan_csv = salida / "cuadro-locales.csv"
    with open(plan_csv, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(["N_LOC", "TXT_LOC", "x", "y", "fila"])
        for l in orden:
            fila = next((n + 1 for n, f in enumerate(filas) if l in f), 0)
            w.writerow([l["numero"], l["nombre"], l["x"], l["y"], fila])

    plan_md = ["# Cuadro de locales — %s" % origen.name, "",
               "> Fuente: %s · lectura %s · INSUNITS=%s (metros)" % (fuente, origen, doc.header.get("$INSUNITS")), "",
               "| N_LOC | TXT_LOC | X | Y | fila |", "|---|---|---|---|---|"]
    for l in orden:
        fila = next((n + 1 for n, f in enumerate(filas) if l in f), 0)
        plan_md.append("| %s | %s | %s | %s | %d |" % (l["numero"], l["nombre"], l["x"], l["y"], fila))
    plan_md += ["", "Totales: **%d locales** en **%d filas**." % (len(orden), len(filas)), ""]
    (salida / "cuadro-locales.md").write_text("\n".join(plan_md), encoding="utf-8")

    md = ["# Orden de locales — %s" % origen.name, "",
          "> Fuente: %s · tolerancia de fila: %.2f m · INSUNITS=%s (metros)" % (fuente, args.tol, doc.header.get("$INSUNITS")),
          "> Archivo de trabajo: `activos/.../W03-CAD` (binario externo al vault).", "",
          "## Filas (de arriba hacia abajo, de izquierda a derecha)", ""]
    for n, f in enumerate(filas, 1):
        md.append("### Fila %d" % n)
        md.append("")
        md.append("| orden | N_LOC | TXT_LOC | X | Y | giro |")
        md.append("|---|---|---|---|---|---|")
        for l in f:
            md.append("| %02d | %s | %s | %s | %s | %s |" % (
                l["orden"], l["numero"], l["nombre"], l["x"], l["y"], l["giro"]))
        md.append("")

    desviaciones, sin_fila = control_orden(orden, filas)
    md += ["## Control", "",
           "- Locales detectados: **%d** en **%d filas**" % (len(orden), len(filas)),
           "- Números repetidos: %s" % (", ".join(rep) if rep else "ninguno"),
           "- Locales sin nombre: %d" % len(vacios),
           "- Orden de lectura (X+ / Y-, filas ΔY < %.2f m): %s" % (
               args.tol,
               "OK, la numeración coincide con el orden de lectura" if not desviaciones
               else "%d local(es) fuera de orden" % len(desviaciones)),
           "- Insertar `SIMB-LOC_ID` en este orden (número = N_LOC, nombre = TXT_LOC).", ""]

    md_path = salida / "orden-locales.md"
    md_path.write_text("\n".join(md), encoding="utf-8")

    print("Fuente: %s" % fuente)
    print("Locales: %d en %d filas" % (len(orden), len(filas)))
    for l in orden:
        print("  %02d  %-4s %-16s  x=%-8s y=%-8s" % (l["orden"], l["numero"], l["nombre"], l["x"], l["y"]))
    print("OK -> %s" % md_path)
    print("OK -> %s" % csv_path)
    print("OK -> %s" % (salida / "cuadro-locales.md"))
    print("OK -> %s" % plan_csv)

    if tmp:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
