#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
volcar-grafos-matriz.py — guarda los .json de workflow de las filas corridas.

Qué hace, en una frase:
    Reutiliza `armar_grafo` de matriz-txt2img.py para regenerar (sin correr)
    el grafo API exacto de cada fila ya ejecutada y lo guarda como
    `activos/web/galeria/workflows/matriz-<ID>.json`, para descargarlo desde
    el tablero del curso.

Por qué existe:
    Las corridas de la matriz se encolaron con grafos armados en memoria: el
    PNG guarda el resultado pero el .json del workflow no quedó en ningún
    archivo. Las fichas de `proyectos/concurso-gaudi-nexus/flujos/` explican
    el flujo, pero sin el .json no se puede reabrir ni re-correr. Este script
    cierra ese hueco de forma determinista (mismo prompt, misma seed).

Qué filas vuelca:
    Solo las ejecutadas el 2026-10-29 (bloque SD 1.5 + parámetros):
    M01, M03-M08, M14-M20. Las SDXL (M02, M09-M13) quedan pendientes de correr.

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\volcar-grafos-matriz.py

Notas:
    la explicación línea por línea está en scripts/volcar-grafos-matriz_notas.md
"""

import importlib.util
import json
import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent  # raíz del vault
OUT_DIR = RAIZ / "activos" / "web" / "galeria" / "workflows"

# NOTA ES: se importa matriz-txt2img como módulo (el nombre tiene guiones) y
# se reusan MATRIZ + armar_grafo + PROMPT_PROYECTO + SEED. Si la matriz cambia,
# los grafos volcados cambian con ella: una sola fuente de verdad.
EJECUTADAS = ["M01", "M03", "M04", "M05", "M06", "M07", "M08",
              "M14", "M15", "M16", "M17", "M18", "M19", "M20"]


def cargar_matriz():
    """Carga matriz-txt2img.py como módulo (el nombre tiene guiones)."""
    ruta = AQUI / "matriz-txt2img.py"
    spec = importlib.util.spec_from_file_location("matriz_txt2img", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    mat = cargar_matriz()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    for fila in mat.MATRIZ:
        if fila["id"] not in EJECUTADAS:
            continue
        grafo = mat.armar_grafo(fila, mat.PROMPT_PROYECTO, mat.SEED)
        destino = OUT_DIR / ("matriz-%s.json" % fila["id"])
        with open(destino, "w", encoding="utf-8") as f:
            json.dump(grafo, f, indent=2, ensure_ascii=False)
        print("  %s -> %s" % (fila["id"], destino.name))
        n += 1
    print("Grafos volcados: %d en %s" % (n, OUT_DIR))
    return 0


if __name__ == "__main__":
    sys.exit(main())
