#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
indice-renders-comfy.py — indexa los renders de ComfyUI con su metadata

Qué hace, en una frase:
    Lee cada PNG que ComfyUI escribe, saca la metadata que el propio ComfyUI
    graba dentro del archivo (el prompt y el workflow completo) y arma un
    indice con modelo, LoRA, seed, sampler, steps, cfg y prompt de cada
    imagen, en Markdown y JSON.

Por qué sirve:
    ComfyUI guarda en cada PNG dos bloques tEXt: 'prompt' (el grafo en formato
    API) y 'workflow' (el grafo en formato de interfaz). Con ahi esta toda la
    trazabilidad: que modelo se uso, con que LoRA y que fuerza, que seed, que
    sampler, que prompt. Ese dato vive en la imagen, no en un archivo aparte:
    leerlo es lo que permite que el indice se regenere solo.

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\indice-renders-comfy.py --dir "P:\\00-repos\\ComfyUI\\output" --out "proyectos\\MVP_04-comfyui-arquitectura"
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\indice-renders-comfy.py --dir "P:\\00-repos\\ComfyUI\\output" --out "." --since 2026-10-01

Notas:
    la explicacion linea por linea esta en scripts/indice-renders-comfy_notas.md
"""

import argparse
import json
import os
import struct
from datetime import date, datetime

# ---------------------------------------------------------------------------
# 1) Lectura de los bloques de texto de un PNG
# ---------------------------------------------------------------------------

def leer_textos_png(ruta):
    """Devuelve un dict {clave: valor} con los chunks tEXt/iTXt del PNG.

    NOTA ES: el formato PNG es una cadena de chunks: [longitud 4B][tipo 4B]
    [datos][CRC 4B]. Los tEXt traen 'clave\\0valor' en latin-1. ComfyUI escribe
    dos: 'prompt' y 'workflow'.
    """
    salida = {}
    with open(ruta, "rb") as f:
        cabecera = f.read(8)
        if cabecera != b"\x89PNG\r\n\x1a\n":
            return salida
        while True:
            cabecera = f.read(8)
            if len(cabecera) < 8:
                break
            longitud = struct.unpack(">I", cabecera[:4])[0]
            tipo = cabecera[4:8]
            datos = f.read(longitud)
            f.read(4)  # CRC
            if tipo == b"tEXt":
                clave, _, valor = datos.partition(b"\x00")
                salida[clave.decode("latin-1")] = valor.decode("utf-8", "replace")
            elif tipo == b"iTXt":
                partes = datos.split(b"\x00")
                if len(partes) >= 2:
                    clave = partes[0].decode("latin-1")
                    salida[clave] = partes[-1].decode("utf-8", "replace")
            elif tipo == b"IEND":
                break
    return salida


# ---------------------------------------------------------------------------
# 2) Lectura del grafo (formato API: {id: {class_type, inputs}})
# ---------------------------------------------------------------------------

def del_grafo(grafo, clase):
    """Devuelve la lista de nodos de una clase, en orden."""
    if not isinstance(grafo, dict):
        return []
    return [n for n in grafo.values() if isinstance(n, dict) and n.get("class_type") == clase]


def primero(grafo, clases, campo="widgets_values"):
    """Primer valor util de un nodo de las clases indicadas."""
    for c in clases:
        nodos = del_grafo(grafo, c)
        if not nodos:
            continue
        nodo = nodos[0]
        if isinstance(nodo.get("inputs"), dict):
            for clave in ("ckpt_name", "unet_name", "lora_name", "sampler_name",
                          "scheduler", "filename_prefix", "text", "model_name"):
                if clave in nodo["inputs"]:
                    return nodo["inputs"][clave]
    return None


def valor_de(grafo, clase, campo):
    """Valor de un input concreto del primer nodo de esa clase."""
    nodos = del_grafo(grafo, clase)
    if not nodos:
        return None
    entradas = nodos[0].get("inputs") or {}
    if campo in entradas and not isinstance(entradas[campo], (list, dict)):
        return entradas[campo]
    return None


def prompt_textual(grafo):
    """Concatenacion de los prompts positivos (CLIPTextEncode)."""
    textos = []
    for nodo in del_grafo(grafo, "CLIPTextEncode"):
        t = (nodo.get("inputs") or {}).get("text")
        if isinstance(t, str) and t.strip():
            textos.append(t.strip())
    return " | ".join(textos)


def loras_de(grafo):
    """Lista de (nombre, strength) de los nodos LoraLoader*."""
    salida = []
    for nodo in grafo.values() if isinstance(grafo, dict) else []:
        if not isinstance(nodo, dict):
            continue
        clase = nodo.get("class_type") or ""
        if not clase.startswith("LoraLoader"):
            continue
        entradas = nodo.get("inputs") or {}
        nombre = entradas.get("lora_name")
        fuerza = entradas.get("strength_model", entradas.get("strength"))
        if nombre:
            salida.append((nombre, fuerza))
    return salida


def tamano_latente(grafo):
    """(width, height) del latent vacio, si esta."""
    for clase in ("EmptyFlux2LatentImage", "EmptyLatentImage", "EmptySD3LatentImage"):
        nodos = del_grafo(grafo, clase)
        if nodos:
            e = nodos[0].get("inputs") or {}
            return e.get("width"), e.get("height")
    return None, None


# ---------------------------------------------------------------------------
# 3) Fila del indice
# ---------------------------------------------------------------------------

def fila_de(ruta, base):
    """Construye la fila de indice de un PNG."""
    textos = leer_textos_png(ruta)
    grafo = {}
    if "prompt" in textos:
        try:
            grafo = json.loads(textos["prompt"])
        except Exception:
            grafo = {}

    loras = loras_de(grafo)
    modelo = primero(grafo, ("CheckpointLoaderSimple", "UNETLoader", "UnetLoaderGGUF"))
    if modelo is None:
        modelo = primero(grafo, ("CheckpointLoaderSimple",))
    ancho, alto = tamano_latente(grafo)

    stat = os.stat(ruta)
    return {
        "archivo": os.path.relpath(ruta, base).replace("\\", "/"),
        "fecha": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
        "workflow": primero(grafo, ("SaveImage",)),
        "modelo": modelo,
        "loras": [{"nombre": n, "strength": s} for n, s in loras],
        "sampler": valor_de(grafo, "KSampler", "sampler_name") or primero(grafo, ("KSamplerSelect",)),
        "scheduler": valor_de(grafo, "KSampler", "scheduler") or primero(grafo, ("Flux2Scheduler", "BasicScheduler")),
        "steps": valor_de(grafo, "KSampler", "steps") or valor_de(grafo, "Flux2Scheduler", "steps"),
        "cfg": valor_de(grafo, "KSampler", "cfg") or valor_de(grafo, "CFGGuider", "cfg"),
        "seed": valor_de(grafo, "KSampler", "seed") or valor_de(grafo, "RandomNoise", "noise_seed"),
        "denoise": valor_de(grafo, "KSampler", "denoise"),
        "resolucion": ("%sx%s" % (ancho, alto)) if ancho and alto else None,
        "prompt": prompt_textual(grafo)[:400],
        "tiene_metadata": bool(grafo),
    }


# ---------------------------------------------------------------------------
# 4) Informe
# ---------------------------------------------------------------------------

def md_indice(filas, carpeta):
    con_meta = [f for f in filas if f["tiene_metadata"]]
    sin_meta = [f for f in filas if not f["tiene_metadata"]]

    L = []
    L.append("# Índice de renders — metadata leída de los propios PNG")
    L.append("")
    L.append("> Generado por `scripts/indice-renders-comfy.py` leyendo los bloques `prompt` y `workflow` que ComfyUI graba dentro de cada PNG. "
             "No hay base de datos: **la trazabilidad vive en la imagen**.")
    L.append("")
    L.append("| Campo | Valor |")
    L.append("|---|---|")
    L.append("| Carpeta indexada | `%s` |" % carpeta)
    L.append("| Renders totales | %d |" % len(filas))
    L.append("| Con metadata | %d |" % len(con_meta))
    L.append("| Sin metadata | %d |" % len(sin_meta))
    L.append("| Fecha del índice | %s |" % date.today().isoformat())
    L.append("")

    if con_meta:
        L.append("## Renders con metadata")
        L.append("")
        L.append("| Fecha | Workflow | Modelo | LoRA | Steps/cfg | Sampler | Seed | Resolución |")
        L.append("|---|---|---|---|---|---|---|---|")
        for f in con_meta:
            lora = ", ".join("%s %s" % (l["nombre"], l["strength"]) for l in f["loras"]) or "—"
            L.append("| %s | `%s` | %s | %s | %s/%s | %s | %s | %s |" % (
                f["fecha"], f["workflow"] or "—", f["modelo"] or "—", lora,
                f["steps"] if f["steps"] is not None else "—",
                f["cfg"] if f["cfg"] is not None else "—",
                f["sampler"] or "—", f["seed"] if f["seed"] is not None else "—",
                f["resolucion"] or "—"))
        L.append("")

    L.append("## Prompts (para reusar)")
    L.append("")
    for f in con_meta:
        if f["prompt"]:
            L.append("- **%s** — `%s`" % (f["workflow"] or f["archivo"], f["prompt"].replace("\n", " ")[:220]))
    L.append("")

    if sin_meta:
        L.append("## Sin metadata (revisar: exports o descargas externas)")
        L.append("")
        for f in sin_meta:
            L.append("- `%s` (%s)" % (f["archivo"], f["fecha"]))
        L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Indexa los renders de ComfyUI con su metadata")
    ap.add_argument("--dir", action="append", required=True,
                    help="carpeta de renders (repetible)")
    ap.add_argument("--out", default=".", help="carpeta donde escribir el índice")
    ap.add_argument("--nombre", default="INDICE-RENDERS", help="prefijo de los archivos")
    ap.add_argument("--since", help="solo indexar archivos modificados desde YYYY-MM-DD")
    args = ap.parse_args()

    desde = None
    if args.since:
        desde = datetime.strptime(args.since, "%Y-%m-%d").timestamp()

    filas = []
    for carpeta in args.dir:
        if not os.path.isdir(carpeta):
            print("No existe la carpeta:", carpeta)
            continue
        base = carpeta
        for raiz, _, archivos in os.walk(carpeta):
            for nombre in sorted(archivos):
                if not nombre.lower().endswith(".png"):
                    continue
                ruta = os.path.join(raiz, nombre)
                if desde and os.stat(ruta).st_mtime < desde:
                    continue
                try:
                    filas.append(fila_de(ruta, base))
                except Exception as e:
                    print("  (!) no se pudo leer", ruta, e)

    filas.sort(key=lambda f: (f["fecha"], f["archivo"]))
    os.makedirs(args.out, exist_ok=True)
    ruta_md = os.path.join(args.out, args.nombre + ".md")
    ruta_json = os.path.join(args.out, args.nombre + ".json")
    with open(ruta_md, "w", encoding="utf-8") as f:
        f.write(md_indice(filas, ", ".join(args.dir)))
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(filas, f, indent=2, ensure_ascii=False)

    con_meta = sum(1 for f in filas if f["tiene_metadata"])
    print("Renders indexados: %d (con metadata: %d)" % (len(filas), con_meta))
    print("Indice:", ruta_md)
    print("Datos:", ruta_json)


if __name__ == "__main__":
    main()
