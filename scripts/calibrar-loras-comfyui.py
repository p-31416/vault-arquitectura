"""
calibrar-loras-comfyui.py — calibra LoRAs instaladas contra los checkpoints locales.

Qué hace (paso a paso):
  1. Arma un grafo de ComfyUI en formato API por cada LoRA a probar:
     CheckpointLoaderSimple -> LoraLoader -> CLIPTextEncode(±) -> KSampler -> VAEDecode -> SaveImage.
  2. Manda ese grafo a la API HTTP de ComfyUI (POST /prompt) y espera a que termine.
  3. Copia la imagen generada desde la carpeta output/ de ComfyUI a la carpeta
     salidas/ del workflow, con la nomenclatura del vault: n_01-G-NN.png
     (G = nueva letra de la leyenda, ver 01-index.md del WF).
  4. Escribe un resumen (JSON + log de texto) con: LoRA, base, strength, seed,
     tiempo real de render, archivo de salida y si hubo error (ej: OOM).

Medio de transporte: requests-free, solo urllib de la libreria estandar.

Uso:
  P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py
  P:\Anaconda\envs\comfyenv\python.exe scripts\calibrar-loras-comfyui.py --solo SD1.5 --fuerzas 0.8
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# --- Rutas del estudio -------------------------------------------------------
# NOTA ES: el vault vive en P:, la instalacion de ComfyUI tambien.
VAULT = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura")
COMFY = Path(r"P:\00-repos\ComfyUI")
API = "http://127.0.0.1:8188"
WF_SALIDAS = VAULT / "proyectos" / "MVP_04-comfyui-arquitectura" / "A-txt2img" / "WF-loras-locales" / "salidas"
LOG_DIR = VAULT / "proyectos" / "MVP_04-comfyui-arquitectura" / "A-txt2img" / "WF-loras-locales"

# --- Configuracion por familia de checkpoint --------------------------------
# NOTA ES: SD 1.5 y SDXL no comparten parametros: el CFG de SDXL es mucho mas bajo
# (3-5) y su sampler optimo es dpmpp_2m con karras. Mezclarlos arruina el render.
BASES = {
    "SD1.5": {
        "ckpt": "architecturerealmix_v11.safetensors",
        "width": 768,
        "height": 512,
        "steps": 30,
        "cfg": 7.0,
        "sampler": "euler_ancestral",
        "scheduler": "karras",
        "pos": (
            "architecturerealmix style, modern architecture, concrete and glass facade, "
            "minimalist design, photorealistic, architectural photography, natural lighting, 8K"
        ),
        "neg": (
            "low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, deformed, "
            "watermark, text, signature, illustration, painting"
        ),
    },
    "SDXL": {
        "ckpt": "Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors",
        "width": 1216,
        "height": 832,
        "steps": 30,
        "cfg": 4.0,
        "sampler": "dpmpp_2m",
        "scheduler": "karras",
        "pos": (
            "photorealistic, raw photo, 8k uhd, architectural photography, modern building, "
            "concrete and glass facade, minimalist design, natural sunlight, sharp focus, "
            "highly detailed, masterpiece, canon r5, 24mm tilt-shift lens"
        ),
        "neg": (
            "blurry, low quality, distorted, ugly, bad architecture, cartoon, sketch, deformed, "
            "watermark, text, signature, grain, noise, overexposed, illustration, painting"
        ),
    },
}

# --- Catalogo de LoRAs a calibrar -------------------------------------------
# NOTA ES: 'trigger' se antepone al prompt positivo; 'nota' deja registro de por que
# ese LoRA esta en la lista (util para decidir descartes).
LORAS = [
    # SD 1.5
    {"base": "SD1.5", "file": "JJ_Archvizcg_v2.safetensors", "trigger": "archviz", "nota": "render clasico de visualizacion arquitectonica"},
    {"base": "SD1.5", "file": "sandiese.safetensors", "trigger": "architecture, building, grey_background", "nota": "conceptos de arquitectura sobre fondo gris"},
    {"base": "SD1.5", "file": "xsarchitectural-10superhighrisebuilding.safetensors", "trigger": "architectural renderings, bird's-eye view", "nota": "torres en vista aerea"},
    {"base": "SD1.5", "file": "room.safetensors", "trigger": "room", "nota": "interiores,trigger generico"},
    {"base": "SD1.5", "file": "landscape_architecture_sketch.safetensors", "trigger": "sketch, architecture, building", "nota": "croquis de paisaje"},
    {"base": "SD1.5", "file": "Le Corbusier 2.2.7.2_sd1.5-000016.safetensors", "trigger": "zhuai_pb, brutalism", "nota": "brutalismo publico Corbusier"},
    {"base": "SD1.5", "file": "BrutalistTech-20.safetensors", "trigger": "brutaltech, cement", "nota": "sustituye al brutalista de JJ (este ultimo pide login en CivitAI)"},
    {"base": "SD1.5", "file": "archisketch-v1.safetensors", "trigger": "linear", "nota": "ya instalado 2026-10-14: foto de arquitectura a croquis"},
    {"base": "SD1.5", "file": "markerhandsketch-V1.safetensors", "trigger": "marker painting, handsketch", "nota": "ya instalado 2026-10-14: croquis a marcador"},
    # SDXL
    {"base": "SDXL", "file": "Architectural_Massing.safetensors", "trigger": "", "nota": "masa y volumetria"},
    {"base": "SDXL", "file": "Architecture_Building.safetensors", "trigger": "", "nota": "edificio como sujeto, sustituye al ArchViz de ArteFactoryLab"},
    {"base": "SDXL", "file": "ArcvizXL_V01.safetensors", "trigger": "archviz 1", "nota": "archviz rank 128, el mas pesado del set"},
    {"base": "SDXL", "file": "bookstore-xl.safetensors", "trigger": "mrares, bookstore", "nota": "interior de libreria, rank 128"},
    {"base": "SDXL", "file": "isometric-v1.safetensors", "trigger": "isometric style", "nota": "axonometria, rank 16 (liviano)"},
    {"base": "SDXL", "file": "SLskyscraperrenderingXL_V1.0.safetensors", "trigger": "", "nota": "render de rascacielos, rank 128"},
    {"base": "SDXL", "file": "baroque_architecture-000006.safetensors", "trigger": "", "nota": "barroco, sustituye al brutalista XL de JJ"},
]

SEED = 42
FUERZAS = [0.6, 0.8]


def pedir_json(url: str, datos: dict | None = None) -> dict:
    """POST (o GET si datos es None) contra la API de ComfyUI y devuelve el JSON."""
    cuerpo = None
    cabeceras = {}
    if datos is not None:
        cuerpo = json.dumps(datos).encode("utf-8")
        cabeceras["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=cuerpo, headers=cabeceras)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def armar_grafo(base: str, lora: str, trigger: str, fuerza: float, prefijo: str) -> dict:
    """Construye el grafo en formato API. El LoraLoader va entre el checkpoint y el KSampler."""
    cfg = BASES[base]
    # NOTA ES: al prompt va el TRIGGER del LoRA (la palabra que el modelo aprendio),
    # nunca el nombre del archivo .safetensors.
    pos = f"{trigger}, {cfg['pos']}" if trigger else cfg["pos"]
    return {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": cfg["ckpt"]}},
        # LoraLoader: salida 0 = MODEL (con LoRA), salida 1 = CLIP (con LoRA)
        "2": {"class_type": "LoraLoader", "inputs": {
            "lora_name": lora, "strength_model": fuerza, "strength_clip": fuerza,
            "model": ["1", 0], "clip": ["1", 1]}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"text": pos, "clip": ["2", 1]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": cfg["neg"], "clip": ["2", 1]}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {
            "width": cfg["width"], "height": cfg["height"], "batch_size": 1}},
        "6": {"class_type": "KSampler", "inputs": {
            "seed": SEED, "steps": cfg["steps"], "cfg": cfg["cfg"],
            "sampler_name": cfg["sampler"], "scheduler": cfg["scheduler"], "denoise": 1.0,
            "model": ["2", 0], "positive": ["3", 0], "negative": ["4", 0], "latent_image": ["5", 0]}},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["1", 2]}},
        "8": {"class_type": "SaveImage", "inputs": {"filename_prefix": prefijo, "images": ["7", 0]}},
    }


def esperar(prompt_id: str, timeout_s: int = 1800) -> dict:
    """Consulta /history/{id} hasta que el render termine (o se agote el timeout)."""
    limite = time.time() + timeout_s
    while time.time() < limite:
        hist = pedir_json(f"{API}/history/{prompt_id}")
        if prompt_id in hist:
            return hist[prompt_id]
        time.sleep(5)
    raise TimeoutError(f"timeout esperando {prompt_id}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", choices=["SD1.5", "SDXL"], help="calibra solo una familia de base")
    ap.add_argument("--fuerzas", default="0.6,0.8", help="lista de strengths separados por coma")
    ap.add_argument("--dry-run", action="store_true", help="solo muestra el plan, no renderiza")
    args = ap.parse_args()

    fuerzas = [float(x) for x in args.fuerzas.split(",")]
    # El orden importa: primero SD 1.5 (barato, ~132s por render) y despues SDXL (pesado).
    # Ademas, dentro de cada base va primero la strength mas baja para tener data temprano.
    orden: list[tuple[dict, float]] = []
    for base in ("SD1.5", "SDXL"):
        if args.solo and args.solo != base:
            continue
        for lora in [l for l in LORAS if l["base"] == base]:
            for fuerza in fuerzas:
                orden.append((lora, fuerza))

    WF_SALIDAS.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / "PLANS" / "calibracion-loras.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    resumen: list[dict] = []

    # Numeracion de salida GLOBAL: n_01-G-NN.png (01-18 SD 1.5, 19-32 SDXL).
    # NOTA ES: un contador unico evita que los renders de SDXL pisen los de SD 1.5.
    contador = 0
    for lora, fuerza in orden:
        contador += 1
        nn = contador
        nombre_salida = f"n_01-G-{nn:02d}.png"
        prefijo = f"loras/{nombre_salida[:-4]}"
        tag = f"[{lora['base']} {fuerza}] {lora['file']} -> {nombre_salida}"
        if args.dry_run:
            print(tag)
            continue

        grafo = armar_grafo(lora["base"], lora["file"], lora["trigger"], fuerza, prefijo)
        t0 = time.time()
        try:
            resp = pedir_json(f"{API}/prompt", {"prompt": grafo, "client_id": "calibrar-loras"})
            pid = resp["prompt_id"]
            hist = esperar(pid)
            salida = hist.get("outputs", {}).get("8", {})
            archivos = salida.get("images", [])
            if not archivos:
                raise RuntimeError(f"sin imagen en la salida: {salida}")
            origen = COMFY / "output" / archivos[0].get("subfolder", "") / archivos[0]["filename"]
            destino = WF_SALIDAS / nombre_salida
            shutil.copy2(origen, destino)
            segundos = round(time.time() - t0, 1)
            print(f"OK   {tag} {segundos}s", flush=True)
            resumen.append({
                "lora": lora["file"], "base": lora["base"], "strength": fuerza,
                "seed": SEED, "trigger": lora["trigger"], "nota": lora["nota"],
                "salida": nombre_salida, "segundos": segundos, "error": None,
            })
        except Exception as exc:  # noqa: BLE001 - un render fallido no debe cortar la tanda
            segundos = round(time.time() - t0, 1)
            print(f"FALLA {tag} {segundos}s -> {type(exc).__name__}: {exc}", flush=True)
            resumen.append({
                "lora": lora["file"], "base": lora["base"], "strength": fuerza,
                "seed": SEED, "trigger": lora["trigger"], "nota": lora["nota"],
                "salida": None, "segundos": segundos, "error": f"{type(exc).__name__}: {exc}",
            })
        with log_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(resumen[-1], ensure_ascii=False) + "\n")

    if not args.dry_run:
        out = LOG_DIR / "PLANS" / "calibracion-loras.json"
        out.write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
        ok = sum(1 for r in resumen if not r["error"])
        print(f"\nResumen: {ok}/{len(resumen)} renders correctos -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
