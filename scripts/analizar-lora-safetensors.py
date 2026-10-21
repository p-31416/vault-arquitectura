#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
analizar-lora-safetensors.py — auditoría de un archivo .safetensors (LoRA o checkpoint)

Qué hace, en una frase:
    Abre el header de un .safetensors, lo lee como un diccionario, y responde
    tres preguntas: (1) ¿qué contiene el archivo?, (2) ¿sobre qué modelo base
    fue entrenado?, (3) ¿los pesos aprendieron algo o están vacíos?

No modifica el archivo: solo lo lee.

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\analizar-lora-safetensors.py <archivo.safetensors> [--json SALIDA.json]

Notas y explicacion linea por linea: scripts/analizar-lora-safetensors_notas.md
"""

import argparse
import json
import os
import struct
import sys

# ---------------------------------------------------------------------------
# 1) Constantes de interpretación
# ---------------------------------------------------------------------------

# Perfiles de modelos FLUX/FLUX.2 conocidos, para deducir el base de un LoRA
# a partir de los shapes de sus tensores. La clave es (hidden, duales, simples).
# Fuente: black-forest-labs/flux2 (src/flux2/model.py) y ComfyUI
# (comfy/model_detection.py).
PERFILES = [
    ("FLUX.2 [dev] 32B",      6144,  8, 48, 15360),
    ("FLUX.2 [klein] 9B",     4096,  8, 24, 12288),
    ("FLUX.2 [klein] 4B",     3072,  5, 20,  7680),
    ("FLUX.1 [dev]/[schnell]", 3072, 19, 38,  4096),
]

# Fórmulas de shapes de los módulos de FLUX.2, para verificar la deducción:
#   linear1 (bloque simple) = 3*hidden + 2*mlp_hidden  (mlp_silu_act = True)
#   linear2 (bloque simple) = hidden + mlp_hidden
#   modulation doble        = 6*hidden
#   txt_in                  = context_in_dim -> hidden
#   img_in                  = in_channels -> hidden
def shapes_de_referencia(hidden, duales, simples, contexto):
    mlp = int(hidden * 3.0)
    return {
        "single_blocks.N.linear1": (3 * hidden + 2 * mlp, hidden),
        "single_blocks.N.linear2": (hidden, hidden + mlp),
        "double_stream_modulation_img.lin": (6 * hidden, hidden),
        "txt_in": (hidden, contexto),
        "img_in": (hidden, 128),
    }


# ---------------------------------------------------------------------------
# 2) Lectura del header .safetensors
# ---------------------------------------------------------------------------

def leer_header(ruta):
    """Devuelve (header_dict, offset_datos).

    Formato del archivo .safetensors:
        [8 bytes]  N  = tamaño del header en bytes (uint64 little-endian)
        [N bytes]  header JSON = {"tensor_name": {"dtype":..., "shape":[...],
                                                   "data_offsets":[inicio,fin]}, ...,
                                  "__metadata__": {...}   (opcional)}
        [resto]    datos binarios de los tensores

    Los `data_offsets` son absolutos respecto del inicio de la zona de datos
    (o sea, 8 + N).
    """
    with open(ruta, "rb") as f:
        n = struct.unpack("<Q", f.read(8))[0]      # tamaño del header
        header = json.loads(f.read(n).decode("utf-8"))
    return header, 8 + n


def nombre_real(nombre, prefijo="diffusion_model."):
    """Quita el prefijo de comfy ('diffusion_model.') si está."""
    return nombre[len(prefijo):] if nombre.startswith(prefijo) else nombre


# ---------------------------------------------------------------------------
# 3) Inferencia del modelo base
# ---------------------------------------------------------------------------

def inferir_base(tensores):
    """Deduce el modelo base a partir de los shapes de los tensores del LoRA.

    Los LoRA guardan matrices A y B. La forma de A es [rank, in_features] y la
    de B es [out_features, rank]. Con la forma de B de 'txt_in' obtenemos el
    hidden_size, y contando bloques 'double_blocks.N' y 'single_blocks.N'
    obtenemos la profundidad.
    """
    info = {}

    # hidden_size: B de txt_in tiene forma [hidden, rank]
    for nombre, t in tensores.items():
        limpio = nombre_real(nombre)
        if limpio.endswith("txt_in.lora_B.weight") and len(t["shape"]) == 2:
            info["hidden"] = t["shape"][0]
            info["rank"] = t["shape"][1]
            break

    # profundidad: se cuentan los índices distintos de bloque
    duales, simples = set(), set()
    for nombre in tensores:
        limpio = nombre_real(nombre)
        partes = limpio.split(".")
        if partes[0] == "double_blocks" and len(partes) > 1 and partes[1].isdigit():
            duales.add(int(partes[1]))
        if partes[0] == "single_blocks" and len(partes) > 1 and partes[1].isdigit():
            simples.add(int(partes[1]))
    info["duales"] = len(duales)
    info["simples"] = len(simples)

    # context_in_dim: A de txt_in tiene forma [rank, context_in_dim]
    for nombre, t in tensores.items():
        limpio = nombre_real(nombre)
        if limpio.endswith("txt_in.lora_A.weight") and len(t["shape"]) == 2:
            info["contexto"] = t["shape"][1]
            break

    # ¿es un LoRA o un checkpoint completo? Un LoRA tiene pares A/B.
    tiene_lora = any(".lora_A." in n for n in tensores)
    info["es_lora"] = tiene_lora

    # perfil conocido
    info["perfil"] = "desconocido"
    for etiqueta, hidden, dd, ss, ctx in PERFILES:
        if (info.get("hidden") == hidden and info.get("duales") == dd
                and info.get("simples") == ss):
            info["perfil"] = etiqueta
            break

    # verificación cruzada de shapes con la fórmula del modelo
    info["verificacion"] = []
    if info.get("hidden"):
        ref = shapes_de_referencia(info["hidden"], info["duales"], info["simples"],
                                   info.get("contexto", 0))
        for nombre, t in tensores.items():
            limpio = nombre_real(nombre)
            for patron, (out_esp, in_esp) in ref.items():
                if limpio.endswith(patron.replace("N", "0") + ".lora_B.weight"):
                    esperado_out, esperado_in = out_esp, in_esp
                    if t["shape"] == [esperado_out, info.get("rank")]:
                        info["verificacion"].append(
                            "OK  %-42s %s" % (patron, t["shape"]))
    return info


# ---------------------------------------------------------------------------
# 4) Salud de los pesos (lectura binaria de las matrices B)
# ---------------------------------------------------------------------------

def estadisticas(ruta, offset_datos, tensores, limite=12):
    """Calcula media, desvío y máximo absoluto de las matrices B muestreadas.

    Se lee el binario a mano (sin numpy) para no depender del entorno.
    Se muestrea para no recorrer 120 MB en cada corrida.
    """
    import array

    candidatas = [n for n in tensores if ".lora_B." in n]
    candidatas.sort()
    paso = max(1, len(candidatas) // limite)
    muestra = candidatas[::paso][:limite]

    filas = []
    with open(ruta, "rb") as f:
        for nombre in muestra:
            t = tensores[nombre]
            inicio, fin = t["data_offsets"]
            n = (fin - inicio) // 4
            f.seek(offset_datos + inicio)
            datos = array.array("f")
            datos.frombytes(f.read(n * 4))
            if not len(datos):
                continue
            suma = sum(datos)
            suma2 = sum(d * d for d in datos)
            maxabs = max(abs(d) for d in datos)
            ceros = sum(1 for d in datos if d == 0.0)
            filas.append({
                "tensor": nombre_real(nombre),
                "n": len(datos),
                "media": suma / len(datos),
                "sigma": (max(suma2 / len(datos), 0.0)) ** 0.5,
                "max_abs": maxabs,
                "ceros_pct": 100.0 * ceros / len(datos),
            })
    return filas


# ---------------------------------------------------------------------------
# 5) Informe
# ---------------------------------------------------------------------------

def imprimir(ruta, header, tensores, base, stats, metadata):
    print("=" * 78)
    print("ANALISIS SAFETENSORS:", os.path.basename(ruta))
    print("=" * 78)
    print("Tamano archivo : %.2f MB" % (os.path.getsize(ruta) / 1024 / 1024))
    print("Tensores       : %d" % len(tensores))

    params = 0
    for t in tensores.values():
        n = 1
        for d in t["shape"]:
            n *= d
        params += n
    print("Parametros     : %.2f M (dtype %s)" % (
        params / 1e6, next(iter(tensores.values()))["dtype"]))

    print()
    print("--- METADATA EMBEBIDA ---")
    if metadata:
        for k, v in metadata.items():
            print("  %-28s %s" % (k, str(v)[:120]))
    else:
        print("  (ausente: no hay __metadata__ en el header)")

    print()
    print("--- DEDUCCION DEL MODELO BASE ---")
    print("  Tipo de archivo  : %s" % ("LoRA (pares A/B)" if base["es_lora"] else "checkpoint"))
    print("  hidden_size      : %s" % base.get("hidden"))
    print("  rank             : %s" % base.get("rank"))
    print("  context_in_dim   : %s" % base.get("contexto"))
    print("  bloques duales   : %s" % base.get("duales"))
    print("  bloques simples  : %s" % base.get("simples"))
    print("  perfil recognized: %s" % base["perfil"])
    for linea in base["verificacion"]:
        print("  " + linea)

    print()
    print("--- MODULOS AFINADOS ---")
    grupos = {}
    for nombre in tensores:
        limpio = nombre_real(nombre)
        if ".lora_A." in limpio or ".lora_B." in limpio:
            clave = limpio.replace(".lora_A.weight", "").replace(".lora_B.weight", "")
            grupos.setdefault(clave.split(".")[0], set()).add(clave)
    for grupo in sorted(grupos):
        print("  %-28s %d modulos" % (grupo, len(grupos[grupo])))

    print()
    print("--- SALUD DE LOS PESOS (muestra de matrices B) ---")
    if not stats:
        print("  (no hay matrices B: no es un LoRA)")
    for f in stats:
        print("  %-44s n=%-8d sigma=%.3e  max|v|=%.3e  ceros=%.1f%%" % (
            f["tensor"][:44], f["n"], f["sigma"], f["max_abs"], f["ceros_pct"]))
    if stats:
        sigmas = [f["sigma"] for f in stats]
        ceros = [f["ceros_pct"] for f in stats]
        print("  Diagnostico: sigma medio %.3e | ceros max %.1f%%" % (
            sum(sigmas) / len(sigmas), max(ceros)))
        if max(ceros) > 99.0:
            print("  -> matrices B vacias: el LoRA no aporta delta (entrenamiento sin terminar o stripped)")
        else:
            print("  -> matrices B con contenido: el LoRA aporta delta real")

    print()
    print("--- QUE FALTA EN LA FICHA ---")
    faltan = []
    if not metadata:
        faltan.append("metadata embebida (trigger word, dataset, base, licencia)")
    if not metadata or "ss_base_model_version" not in metadata:
        faltan.append("modelo base exacto (revisar tags ss_* o pedir al autor)")
    faltan.append("licencia de uso y permiso comercial")
    for f in faltan:
        print("  - " + f)
    print()


def main():
    ap = argparse.ArgumentParser(description="Audita un .safetensors (LoRA o checkpoint)")
    ap.add_argument("archivo", help="ruta al .safetensors")
    ap.add_argument("--json", help="guarda el informe completo en un JSON")
    args = ap.parse_args()

    if not os.path.isfile(args.archivo):
        print("No existe el archivo:", args.archivo)
        sys.exit(1)

    header, offset_datos = leer_header(args.archivo)
    metadata = header.pop("__metadata__", None)
    tensores = header

    base = inferir_base(tensores)
    stats = estadisticas(args.archivo, offset_datos, tensores)

    imprimir(args.archivo, header, tensores, base, stats, metadata)

    if args.json:
        informe = {
            "archivo": args.archivo,
            "tamano_mb": os.path.getsize(args.archivo) / 1024 / 1024,
            "tensores": len(tensores),
            "metadata": metadata,
            "base_deducido": base,
            "salud_pesos": stats,
        }
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(informe, f, indent=2, ensure_ascii=False)
        print("Informe JSON guardado en:", args.json)


if __name__ == "__main__":
    main()
