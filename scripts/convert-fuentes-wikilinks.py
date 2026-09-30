#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convierte notas [^n] en wikilinks [[#^fn|n]] con destino buscado por URL.

# NOTA ES: el problema es que el maestro unio 5 archivos que usaban los mismos
# NOTA ES: numeritos. Este script NO supone ningun corrimiento: para cada
# NOTA ES: referencia del Kit busca la definicion del maestro con la MISMA url.
# NOTA ES: Si alguna referencia queda sin destino unico, NO escribe nada.
"""
import re  # NOTA ES: 're' = expresiones regulares, para patrones como [^64].
from pathlib import Path  # NOTA ES: 'pathlib' maneja rutas de archivos.

# NOTA ES: __file__ es este script; .parents[1] sube a la raiz del vault.
BASE = Path(__file__).resolve().parents[1]
MAESTRO = BASE / "raw" / "docs" / "autocad-documento-maestro.md"
KIT = BASE / "raw" / "docs" / "Estudio Pi – Kit temático  SETs de estándar CAD.md"


def url_de(texto):
    # NOTA ES: extrae la primera URL; le quita signos pegados al final.
    m = re.search(r"https?://\S+", texto)
    if not m:
        return ""
    return m.group(0).rstrip(").,;]" "'")


def normaliza(texto):
    # NOTA ES: deja solo letras/numeros en minuscula para comparar textos.
    return re.sub(r"[^a-z0-9]", "", texto.lower())


def sin_refs(linea):
    # NOTA ES: borra los [^n] para comparar frases entre archivos.
    return normaliza(re.sub(r"\[\^\d+\]", "", linea))


def definiciones(lineas, desde):
    # NOTA ES: junta las lineas con forma [^64]: ... desde el indice dado.
    defs = {}
    for i in range(desde, len(lineas)):
        m = re.match(r"^\[\^(\d+)\]:(.*)$", lineas[i].rstrip())
        if m:
            defs[int(m.group(1))] = m.group(2).strip()
    return defs


# NOTA ES: leo ambos archivos separados por lineas.
m_lineas = MAESTRO.read_text(encoding="utf-8").split("\n")
k_lineas = KIT.read_text(encoding="utf-8").split("\n")

# NOTA ES: ubico ## 15. Fuentes y las secciones 3.2 / 4 / 5 (todo base 0).
fuentes_idx = next(i for i, l in enumerate(m_lineas) if l.strip() == "## 15. Fuentes")
sec4 = next(i for i, l in enumerate(m_lineas) if l.strip().startswith("## 4."))
sec5 = next(i for i, l in enumerate(m_lineas) if l.strip().startswith("## 5."))
cuerpo = m_lineas[:fuentes_idx]
defs_m = definiciones(m_lineas, fuentes_idx + 1)

# NOTA ES: el cuerpo del Kit termina donde empieza su lista de [^n]: final.
k_fidx = next(i for i, l in enumerate(k_lineas) if re.match(r"^\[\^\d+\]:", l.strip()))
k_defs = definiciones(k_lineas, k_fidx)
k_frases = {sin_refs(l) for l in k_lineas[:k_fidx] if sin_refs(l)}

# NOTA ES: indice URL -> numeros de definicion del maestro (clave de respaldo: texto).
por_clave = {}
for num, txt in defs_m.items():
    u = url_de(txt)
    por_clave.setdefault(u or ("T:" + normaliza(txt)), []).append(num)


def objetivo(kit_n, contexto):
    # NOTA ES: busca el numero maestro con la misma fuente que el Kit [^kit_n].
    base = k_defs.get(kit_n, "")
    if not base:
        return None, f"{contexto}: Kit [^{kit_n}] no existe en el Kit original"
    clave = url_de(base) or ("T:" + normaliza(base))
    cands = por_clave.get(clave, [])
    if not cands:
        return None, f"{contexto}: sin destino para Kit [^{kit_n}] ({clave[:70]})"
    pref = [c for c in cands if 68 <= c <= 105]
    elegido = sorted(pref or cands)[0]
    av = ""
    if len(cands) > 1:
        av = f"{contexto}: {len(cands)} destinos {cands}, uso [^{elegido}] (misma url)"
    return elegido, av


# NOTA ES: chequeos de anclaje: si el archivo cambio, corto antes de tocar nada.
assert cuerpo[121].startswith("1. **Núcleo"), cuerpo[121][:40]
assert cuerpo[129].startswith("9. **Checklist"), cuerpo[129][:40]
assert "[^39]" in cuerpo[263], cuerpo[263][:80]
assert "[^105]" in cuerpo[262], cuerpo[262][:80]

errores, avisos, plan = [], [], []
# NOTA ES: lineas con numeracion ORIGINAL del Kit: items 1-9 de 3.2 y linea 264.
for a, b in [(121, 129), (263, 263)]:
    for i in range(a, b + 1):
        for m in re.finditer(r"\[\^(\d+)\]", cuerpo[i]):
            n = int(m.group(1))
            t, av = objetivo(n, f"linea {i + 1}")
            if av:
                avisos.append(av)
            if t is None:
                errores.append(av)
            else:
                plan.append((i, n, t))

# NOTA ES: linea 263: ya trae numero final [^105]; verifico que sea Kit40/Wiley.
uk40, u105 = url_de(k_defs.get(40, "")), url_de(defs_m.get(105, ""))
if not (uk40 and uk40 == u105):
    errores.append(f"linea 263: [^105] no es la fuente Wiley del Kit40")

# NOTA ES: seccion 4 (ya corrida +67): recupero el Kit original restando, pero
# NOTA ES: SOLO toco lineas cuya frase existe en el cuerpo del Kit (anti-master).
for i in range(sec4, sec5):
    if 262 <= i <= 263:
        continue
    if sin_refs(cuerpo[i]) not in k_frases:
        if re.search(r"\[\^\d+\]", cuerpo[i]):
            avisos.append(f"linea {i + 1}: frase ajena al Kit, se conserva tal cual")
        continue
    for m in re.finditer(r"\[\^(\d+)\]", cuerpo[i]):
        n = int(m.group(1))
        if not (68 <= n <= 107):
            avisos.append(f"linea {i + 1}: [^{n}] fuera de rango Kit, se conserva")
            continue
        t, av = objetivo(n - 67, f"linea {i + 1} (era Kit [^{n - 67}])")
        if av:
            avisos.append(av)
        if t is None:
            errores.append(av)
        elif t != n:
            plan.append((i, n, t))

if errores:
    print("MAPEO INVALIDO, no se escribio nada:")
    print("\n".join(errores))
    raise SystemExit(1)

# NOTA ES: foto del indice antes de tocar (al final verifico que quedo igual).
indice_antes = [l for l in cuerpo if re.match(r"^- \[\[#", l)]

# NOTA ES: aplico los cambios de numero planificados, linea por linea.
cambios = 0
agrup = {}
for i, viejo, nuevo in plan:
    agrup.setdefault(i, {})[viejo] = nuevo
for i, mapa in agrup.items():
    # NOTA ES: .get(viejo, viejo) deja igual lo que ya estaba bien (ej: 68->68).
    cuerpo[i], c = re.subn(r"\[\^(\d+)\]", lambda m: f"[^{mapa.get(int(m.group(1)), int(m.group(1)))}]", cuerpo[i])
    cambios += c

# NOTA ES: convierto cada [^64] en [[#^f64|64]]; en tablas escapo el | como \|.
n_conv = 0
for i in range(len(cuerpo)):
    sep = "\\|" if cuerpo[i].lstrip().startswith("|") else "|"
    cuerpo[i], c = re.subn(r"\[\^(\d+)\]", lambda m: f"[[#^f{m.group(1)}{sep}{m.group(1)}]]", cuerpo[i])
    n_conv += c

# NOTA ES: agrego el ancla ^fN al final de cada definicion (salta si ya esta).
resto = m_lineas[fuentes_idx:]
n_ids = 0
for j in range(len(resto)):
    m = re.match(r"^(\[\^(\d+)\]:.*)$", resto[j].rstrip())
    if m and not re.search(r"\^f\d+\s*$", resto[j]):
        resto[j] = resto[j].rstrip() + f" ^f{m.group(2)}"
        n_ids += 1

# NOTA ES: recien ahora escribo el archivo.
MAESTRO.write_text("\n".join(cuerpo + resto), encoding="utf-8")

# NOTA ES: verificacion final sobre lo escrito.
final = MAESTRO.read_text(encoding="utf-8").split("\n")
f2 = next(i for i, l in enumerate(final) if l.strip() == "## 15. Fuentes")
sueltos = [(i + 1) for i, l in enumerate(final[:f2]) if re.search(r"\[\^\d+\]", l)]
alias = set(re.findall(r"\[\[#\^f(\d+)[\|]", "\n".join(final[:f2])))
anclas = set(re.findall(r"\^f(\d+)\s*$", "\n".join(final[f2 + 1:]), re.M))
indice_despues = [l for l in final[:f2] if re.match(r"^- \[\[#", l)]
print(f"remaps: {cambios} | convertidos: {n_conv} | anclas: {n_ids}")
print(f"alias distintos: {len(alias)} | anclas distintas: {len(anclas)}")
print(f"[^n] sueltos en cuerpo (lineas): {sueltos}")
print(f"alias sin ancla: {sorted(alias - anclas, key=int)}")
print(f"indice intacto: {indice_antes == indice_despues}")
for a in avisos:
    print("AVISO:", a)
