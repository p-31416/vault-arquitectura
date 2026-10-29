#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
matriz-txt2img.py — corre la matriz de variantes de text-to-image con prompt y seed fijos.

Qué hace, en una frase:
    Genera N imágenes cambiando UNA sola variable por vez (modelo, LoRA, sampler,
    steps, cfg, resolución) y siempre con el mismo prompt y la misma seed, para
    que la diferencia entre dos imágenes sea atribuible a esa variable y nada más.

Por qué importa:
    Comparar modelos o LoRAs "en general" no dice nada: cambia el prompt, la
    seed y el estilo. Con prompt y seed fijos, el delta visible ES la variable.
    Es el mismo protocolo que el curso (mismo prompt, misma seed, una variable
    por corrida) y el mismo que usa nuestro WF-loras-locales.

Qué escribe:
    1. Los renders en la carpeta output/ de ComfyUI (con prefijo `matriz/`), para
       que el índice y la galería los recojan solos.
    2. Una tabla Markdown + JSON con la definición de cada fila y su resultado
       (archivo, segundos, error).

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\matriz-txt2img.py --bloque sd15
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\matriz-txt2img.py --bloque sd15 --dry-run
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\matriz-txt2img.py --bloque todos

Notas:
    la explicación línea por línea está en scripts/matriz-txt2img_notas.md
"""

import argparse
import json
import os
import shutil
import sys
import time
import urllib.request
from pathlib import Path

# --- Rutas ------------------------------------------------------------------
VAULT = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura")
COMFY = Path(r"P:\00-repos\ComfyUI")
API = "http://127.0.0.1:8188"
SALIDA_MD = VAULT / "activos" / "web" / "galeria" / "matriz-txt2img.md"

# --- El prompt único de la matriz ------------------------------------------
# NOTA ES: es el MISMO texto para todas las filas. El del proyecto (Mercado de
# Proximidad + Centro de Cultura Digital en el entorno de la Sagrada Família).
# Se puede cambiar por el del curso (--prompt curso) para comparar.
PROMPT_PROYECTO = (
    "a contemporary market and digital culture centre in Barcelona beside the Sagrada Familia, "
    "board-formed concrete and glass facade, colonnade of inclined columns, deep loggias, "
    "warm stone paving with market stalls, people for scale, photorealistic, "
    "architectural photography, morning light, sharp focus, highly detailed, 8k"
)
PROMPT_CURSO = "concrete house in desert rocky landscape"

NEGATIVO = (
    "low quality, blurry, distorted, deformed, bad architecture, cartoon, sketch, "
    "watermark, text, signature, illustration, painting, oversaturated"
)

SEED = 42  # una sola seed para toda la matriz

# --- Configuración por base --------------------------------------------------
BASES = {
    "sd15": {
        "ckpt": "architecturerealmix_v11.safetensors",
        "res": (768, 512), "steps": 30, "cfg": 7.0,
        "sampler": "euler_ancestral", "scheduler": "karras",
        "prefijo": "matriz/sd15",
    },
    "sdxl": {
        "ckpt": "Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors",
        "res": (1216, 832), "steps": 30, "cfg": 4.0,
        "sampler": "dpmpp_2m", "scheduler": "karras",
        "prefijo": "matriz/sdxl",
    },
}

# --- La matriz --------------------------------------------------------------
# NOTA ES: cada fila declara QUÉ variable cambia. "loras" y "trigger" son opcionales.
# Las filas con lora usan el LoRA con su trigger en el prompt (el trigger va en el
# prompt, nunca el nombre del archivo).
MATRIZ = [
    # --- Bloque 1: modelo (el salto de base, con todo lo demás fijo) ---
    {"id": "M01", "bloque": "modelo", "base": "sd15", "titulo": "SD 1.5 sin LoRA (baseline)",
     "variable": "modelo base", "loras": [], "trigger": ""},
    {"id": "M02", "bloque": "modelo", "base": "sdxl", "titulo": "SDXL sin LoRA",
     "variable": "modelo base", "loras": [], "trigger": ""},

    # --- Bloque 2: LoRAs de SD 1.5 (fuerza 0,8) ---
    {"id": "M03", "bloque": "loras_sd15", "base": "sd15", "titulo": "JJ's Archvizcg_v2",
     "variable": "LoRA", "loras": [("JJ_Archvizcg_v2.safetensors", 0.8)], "trigger": "archviz"},
    {"id": "M04", "bloque": "loras_sd15", "base": "sd15", "titulo": "sandiese (Concepts)",
     "variable": "LoRA", "loras": [("sandiese.safetensors", 0.8)],
     "trigger": "architecture, building, grey_background"},
    {"id": "M05", "bloque": "loras_sd15", "base": "sd15", "titulo": "BrutalistTech-20",
     "variable": "LoRA", "loras": [("BrutalistTech-20.safetensors", 0.8)], "trigger": "brutaltech, cement"},
    {"id": "M06", "bloque": "loras_sd15", "base": "sd15", "titulo": "Le Corbusier",
     "variable": "LoRA", "loras": [("Le Corbusier 2.2.7.2_sd1.5-000016.safetensors", 0.8)],
     "trigger": "zhuai_pb, brutalism"},
    {"id": "M07", "bloque": "loras_sd15", "base": "sd15", "titulo": "room (interiores)",
     "variable": "LoRA", "loras": [("room.safetensors", 0.8)], "trigger": "room"},
    {"id": "M08", "bloque": "loras_sd15", "base": "sd15", "titulo": "XSarchitectural-10 superhighrise",
     "variable": "LoRA", "loras": [("xsarchitectural-10superhighrisebuilding.safetensors", 0.8)],
     "trigger": "architectural renderings, bird's-eye view"},

    # --- Bloque 3: LoRAs de SDXL ---
    {"id": "M09", "bloque": "loras_sdxl", "base": "sdxl", "titulo": "Architectural_Massing",
     "variable": "LoRA", "loras": [("Architectural_Massing.safetensors", 0.8)], "trigger": ""},
    {"id": "M10", "bloque": "loras_sdxl", "base": "sdxl", "titulo": "Architecture_Building",
     "variable": "LoRA", "loras": [("Architecture_Building.safetensors", 0.8)], "trigger": ""},
    {"id": "M11", "bloque": "loras_sdxl", "base": "sdxl", "titulo": "isometric-v1",
     "variable": "LoRA", "loras": [("isometric-v1.safetensors", 0.8)], "trigger": "isometric style"},
    {"id": "M12", "bloque": "loras_sdxl", "base": "sdxl", "titulo": "ArcvizXL_V01 (rank 128)",
     "variable": "LoRA", "loras": [("ArcvizXL_V01.safetensors", 0.8)], "trigger": "archviz 1"},
    {"id": "M13", "bloque": "loras_sdxl", "base": "sdxl", "titulo": "SLskyscraperrenderingXL",
     "variable": "LoRA", "loras": [("SLskyscraperrenderingXL_V1.0.safetensors", 0.8)], "trigger": ""},

    # --- Bloque 4: parámetros (la misma base, el mismo prompt) ---
    {"id": "M14", "bloque": "parametros", "base": "sd15", "titulo": "steps 10",
     "variable": "steps", "loras": [], "trigger": "", "over": {"steps": 10}},
    {"id": "M15", "bloque": "parametros", "base": "sd15", "titulo": "steps 50",
     "variable": "steps", "loras": [], "trigger": "", "over": {"steps": 50}},
    {"id": "M16", "bloque": "parametros", "base": "sd15", "titulo": "cfg 3",
     "variable": "cfg", "loras": [], "trigger": "", "over": {"cfg": 3.0}},
    {"id": "M17", "bloque": "parametros", "base": "sd15", "titulo": "cfg 12",
     "variable": "cfg", "loras": [], "trigger": "", "over": {"cfg": 12.0}},
    {"id": "M18", "bloque": "parametros", "base": "sd15", "titulo": "sampler dpmpp_2m + karras",
     "variable": "sampler", "loras": [], "trigger": "",
     "over": {"sampler": "dpmpp_2m", "scheduler": "karras"}},
    {"id": "M19", "bloque": "parametros", "base": "sd15", "titulo": "resolución 512x512",
     "variable": "resolución", "loras": [], "trigger": "", "over": {"res": (512, 512)}},
    {"id": "M20", "bloque": "parametros", "base": "sd15", "titulo": "resolución 768x768",
     "variable": "resolución", "loras": [], "trigger": "", "over": {"res": (768, 768)}},
]

BLOQUES = ["modelo", "loras_sd15", "loras_sdxl", "parametros"]


# --- Utilidades -------------------------------------------------------------
def pedir_json(url, datos=None):
    """POST/GET contra la API de ComfyUI y devuelve el JSON."""
    cuerpo = None
    cabeceras = {}
    if datos is not None:
        cuerpo = json.dumps(datos).encode("utf-8")
        cabeceras["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=cuerpo, headers=cabeceras)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def armar_grafo(fila, prompt, seed):
    """Monta el grafo API de la fila: checkpoint -> LoRAs -> prompt -> sampler -> save."""
    cfg = BASES[fila["base"]]
    over = fila.get("over", {})
    ancho, alto = over.get("res", cfg["res"])
    steps = over.get("steps", cfg["steps"])
    valor_cfg = over.get("cfg", cfg["cfg"])
    sampler = over.get("sampler", cfg["sampler"])
    scheduler = over.get("scheduler", cfg["scheduler"])
    prefijo = "%s/%s" % (cfg["prefijo"], fila["id"])

    grafo = {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": cfg["ckpt"]}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {
            "width": ancho, "height": alto, "batch_size": 1}},
    }

    # -- MODEL: checkpoint -> LoRA(s) en cadena -> KSampler
    modelo_ref = ["1", 0]
    clip_ref = ["1", 1]
    n = 10
    for nombre, fuerza in fila.get("loras", []):
        grafo[str(n)] = {"class_type": "LoraLoader", "inputs": {
            "lora_name": nombre, "strength_model": fuerza, "strength_clip": fuerza,
            "model": modelo_ref, "clip": clip_ref}}
        modelo_ref = [str(n), 0]
        clip_ref = [str(n), 1]
        n += 1

    # -- PROMPT: el trigger del LoRA va adelante del prompt del proyecto
    texto = ("%s, %s" % (fila["trigger"], prompt)) if fila["trigger"] else prompt
    grafo["3"] = {"class_type": "CLIPTextEncode", "inputs": {"text": texto, "clip": clip_ref}}
    grafo["4"] = {"class_type": "CLIPTextEncode", "inputs": {"text": NEGATIVO, "clip": clip_ref}}
    grafo["6"] = {"class_type": "KSampler", "inputs": {
        "seed": seed, "steps": steps, "cfg": valor_cfg,
        "sampler_name": sampler, "scheduler": scheduler, "denoise": 1.0,
        "model": modelo_ref, "positive": ["3", 0], "negative": ["4", 0], "latent_image": ["5", 0]}}
    grafo["7"] = {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}}
    grafo["8"] = {"class_type": "SaveImage", "inputs": {"filename_prefix": prefijo, "images": ["7", 0]}}
    return grafo


def esperar(prompt_id, timeout_s=1800):
    """Espera a que termine el render consultando /history."""
    limite = time.time() + timeout_s
    while time.time() < limite:
        hist = pedir_json("%s/history/%s" % (API, prompt_id))
        if prompt_id in hist:
            return hist[prompt_id]
        time.sleep(5)
    raise TimeoutError(prompt_id)


def md_tabla(filas):
    """Arma la tabla Markdown de la matriz."""
    L = ["# Matriz txt2img — prompt y seed fijos", "",
         "> Generado por `scripts/matriz-txt2img.py`. Mismo prompt y misma seed en todas las filas: "
         "la diferencia entre dos imágenes es la variable de la fila.", "",
         "| # | Bloque | Variable | Qué cambia | Base | LoRA | Archivo | Segundos | Error |",
         "|---|---|---|---|---|---|---|---|---|"]
    for f in filas:
        lora = ", ".join("%s @%s" % (l, s) for l, s in f["loras"]) or "—"
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            f["id"], f["bloque"], f["variable"], f["titulo"], f["base"], lora,
            f.get("salida") or "—", f.get("segundos") or "—", f.get("error") or ""))
    L += ["", "## Prompt común", "", "```", f["prompt"], "```", "",
          "**Negativo:**", "", "```", NEGATIVO, "```", "",
          "**Seed:** %d (fija en todas las filas)" % SEED, ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Corre la matriz de variantes de text-to-image")
    ap.add_argument("--bloque", default="sd15",
                    help="sd15 | modelo | loras_sd15 | loras_sdxl | parametros | todos")
    ap.add_argument("--prompt", default="proyecto", choices=["proyecto", "curso"])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    prompt = PROMPT_PROYECTO if args.prompt == "proyecto" else PROMPT_CURSO

    if args.bloque == "todos":
        seleccion = MATRIZ
    elif args.bloque == "sd15":
        seleccion = [f for f in MATRIZ if f["base"] == "sd15"]
    elif args.bloque == "modelo":
        seleccion = [f for f in MATRIZ if f["bloque"] == "modelo"]
    else:
        seleccion = [f for f in MATRIZ if f["bloque"] == args.bloque]

    for f in seleccion:
        f["prompt"] = prompt

    if args.dry_run:
        for f in seleccion:
            print(f["id"], f["bloque"], "|", f["titulo"], "|", BASES[f["base"]]["ckpt"])
        return 0

    print("Matriz: %d filas | prompt=%s | seed=%d" % (len(seleccion), args.prompt, SEED))
    filas = []
    for f in seleccion:
        t0 = time.time()
        try:
            grafo = armar_grafo(f, prompt, SEED)
            resp = pedir_json("%s/prompt" % API, {"prompt": grafo, "client_id": "matriz-txt2img"})
            hist = esperar(resp["prompt_id"])
            imgs = hist.get("outputs", {}).get("8", {}).get("images", [])
            if not imgs:
                raise RuntimeError("sin imagen")
            origen = COMFY / "output" / imgs[0].get("subfolder", "") / imgs[0]["filename"]
            f["salida"] = ("output/%s/%s" % (imgs[0].get("subfolder", ""), imgs[0]["filename"])).lstrip("/").replace("\\", "/")
            f["segundos"] = round(time.time() - t0, 1)
            f["error"] = None
            print("OK   %s %-46s %6ss" % (f["id"], f["titulo"][:46], f["segundos"]), flush=True)
        except Exception as exc:  # noqa: BLE001
            f["segundos"] = round(time.time() - t0, 1)
            f["error"] = "%s: %s" % (type(exc).__name__, exc)
            print("FALLA %s %-46s %s" % (f["id"], f["titulo"][:46], f["error"]), flush=True)
        filas.append(f)
        SALIDA_MD.parent.mkdir(parents=True, exist_ok=True)
        SALIDA_MD.write_text(md_tabla(filas), encoding="utf-8")

    ok = sum(1 for f in filas if not f["error"])
    print("\nResumen: %d/%d correctos -> %s" % (ok, len(filas), SALIDA_MD))
    return 0


if __name__ == "__main__":
    sys.exit(main())
