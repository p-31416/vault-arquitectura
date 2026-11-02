#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
dashboard-curso.py — tablero del curso AI×Gaudí: SOLO las imágenes repasadas.

Qué hace, en una frase:
    Lee el manifiesto curado (curso.json: las imágenes que ya repasamos del
    curso, una por una), copia esos PNG a img-curso/, sincroniza los workflows
    del concurso a la librería de ComfyUI con prefijo GX- y genera curso.html
    con el MISMO formato de la galería (mosaico, lienzo, facetas, Polaroid,
    auto-refresh) más dos piezas propias: caja de NOTAS por imagen (qué se
    puede cambiar) y panel de Flujos (video, transcripción, workflow, notas).

Por qué existe:
    La galería general muestra los 94 renders. Este tablero muestra solo lo
    repasado del curso, en orden de revisión (módulo 1 primero), con las notas
    de qué se puede cambiar en cada flujo. Crece a medida que repasamos:
    agregar una fila a curso.json y regenerar.

Modos de uso:
    1) Generar una vez (el usuario lo ejecuta en terminal):
         P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\dashboard-curso.py
    2) Generar + servir + actualizar solo:
         P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\dashboard-curso.py --serve 8891
    El tablero vive junto a la galería (activos/web/galeria/curso.html), así
    que el servidor de la galería (8890) también lo sirve; --serve aquí solo
    regenera cuando cambian curso.json o las imágenes.

Lo que NO hace:
    No toca la galería general. No publica en internet. No escribe wiki/.

Salidas:
    <out>/curso.html        <- el tablero
    <out>/curso-datos.json  <- los datos + la versión (sondeo de actualización)
    <out>/img-curso/        <- las imágenes repasadas

Notas:
    la explicación línea por línea está en scripts/dashboard-curso_notas.md
"""

import argparse
import functools
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent  # raíz del vault

# --- Se reusa la galería: un solo formato, sin duplicar ----------------------
# NOTA ES: la plantilla HTML/CSS/JS vive en galeria-renders.py. Importarla como
# módulo evita dos formatos que divergen (que es donde se cuelan los errores).
def cargar_galeria():
    """Carga galeria-renders.py como módulo (el nombre tiene guiones)."""
    ruta = AQUI / "galeria-renders.py"
    spec = importlib.util.spec_from_file_location("galeria_renders", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# --- Flujos del curso (ficha por módulo; crece el estado, no la lista) -------
# NOTA ES: video = área de participantes (requiere login del curso), transcript
# = ruta en el vault (texto de referencia, no link web), workflow_gx = nombre
# con el que el flujo aparece en la pestaña Workflows de ComfyUI tras el sync.
AREA_CURSO = "https://archademy.ai/my-account/my-competitions/214/?tab=course"
COMFY_URL = "http://127.0.0.1:8188"

FLUJOS = [
    {"modulo": "Módulo 1 · base", "titulo": "Flujo base (WF-01)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-intro-generative-ai.es.md",
     "workflow_fuente": "P:/00-repos/ComfyUI/user/default/workflows/WF04-1.0.0-txt2img-base.json",
     "workflow_gx": "GX-01-modulo1-base-txt2img.json", "estado": "repasado",
     "notas": ("Checkpoint SD1.5 fijo en este grafo (architecturerealmix_v11). / "
               "LoRA: sumar LoraLoader entre checkpoint y sampler + trigger en el prompt, "
               "strength 0.6–0.9 (matriz: 0.8). / Steps: 10 rápido (65 s) · 30 base (195 s) · "
               "50 fino (210 s). / cfg 3–12 (base 7). / Sampler euler+normal o dpmpp_2m+karras. / "
               "Resolución 768×512 base; 512² rápido; 768² detalle. / Seed 42 fija para comparar.")},
    {"modulo": "Módulo 2 · texto a imagen", "titulo": "Comparativa + LoRA strength (WF-02)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-text-to-image.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "pendiente", "notas": ""},
    {"modulo": "Módulo 3 · imagen a imagen", "titulo": "Rhino a imagen (WF-03)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-image-to-image.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "grafo (a) existe", "notas": ""},
    {"modulo": "Módulo 4 · imagen a video", "titulo": "Video LTX (WF-04)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-image-to-video.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "pendiente", "notas": ""},
    {"modulo": "Módulo 5 · imagen a 3D", "titulo": "Preparación + img23D (WF-05)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-image-to-3d.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "pendiente", "notas": ""},
    {"modulo": "Módulo 6 · criterio", "titulo": "Criterio del jurado (WF-06)",
     "video": AREA_CURSO, "transcript": "raw/2026-10-sesion-extraordinaria-aixgaudi-round-table.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "script listo", "notas": ""},
    {"modulo": "Módulo 7 · flujo Gaudí", "titulo": "Arcilla + WF-03 (WF-07)",
     "video": AREA_CURSO, "transcript": "raw/yt/transcripts/2026-10-21_mux-gaudi-workflow.es.md",
     "workflow_fuente": None, "workflow_gx": None, "estado": "pendiente", "notas": ""},
]

LINKS = {
    "area": AREA_CURSO,
    "miro": "https://miro.com/app/board/uXjVHRM2XQU=/ (contraseña: Gaudi2026)",
    "brief_es": "https://archademy.ai/wp-content/uploads/2026/01/GxAI_BRIEFING_ES.pdf",
    "criterio": "proyectos/concurso-gaudi-nexus/criterio/criterio-jurado.md",
    "comfy": COMFY_URL,
}


# --- Catálogo de LoRAs: descarga + qué observar --------------------------------
# NOTA ES: fuente de verdad = wiki/glosario/software/lora-locales-comfyui.md
# (URL CivitAI, trigger, rank) + sidecars .civitai.json (versiones exactas).
# "observar" dice qué característica mirar al repasar una imagen con ese LoRA.
LORAS = {
    # --- SD 1.5 ---
    "JJ_Archvizcg_v2.safetensors": {
        "url": "https://civitai.com/models/191596", "trigger": "archviz",
        "observar": "Render clásico de visualización arquitectónica (rank 128). "
                    "Verificado M03 @0.8: empuja el estilo archviz sin romper la composición."},
    "sandiese.safetensors": {
        "url": "https://civitai.com/models/134165", "trigger": "architecture, building, grey_background",
        "observar": "Conceptos de arquitectura sobre fondo gris (rank 32)."},
    "xsarchitectural-10superhighrisebuilding.safetensors": {
        "url": "https://civitai.com/models/25509", "trigger": "architectural renderings, bird's-eye view",
        "observar": "Torres en vista aérea (rank 32)."},
    "room.safetensors": {
        "url": "https://civitai.com/models/37483", "trigger": "room",
        "observar": "Interiores; trigger genérico (rank 64)."},
    "landscape_architecture_sketch.safetensors": {
        "url": "https://civitai.com/models/45218", "trigger": "sketch, architecture, building",
        "observar": "Croquis de paisaje (rank 32)."},
    "Le Corbusier 2.2.7.2_sd1.5-000016.safetensors": {
        "url": "https://civitai.com/models/67585", "trigger": "zhuai_pb, brutalism",
        "observar": "Brutalismo público, familia Villa Savoye / La Tourette (rank 32)."},
    "BrutalistTech-20.safetensors": {
        "url": "https://civitai.com/models/85252", "trigger": "brutaltech, cement",
        "observar": "Brutalismo técnico; sustituye al brutalista de JJ que pide login (rank 128)."},
    "archisketch-v1.safetensors": {
        "url": "https://civitai.com/models/32757?modelVersionId=39140", "trigger": "linear",
        "observar": "Foto de arquitectura → croquis lineal (rank 16, liviano)."},
    "markerhandsketch-V1.safetensors": {
        "url": "https://civitai.com/models/34384?modelVersionId=40665",
        "trigger": "marker painting, handsketch",
        "observar": "Croquis a marcador (rank 8, el más liviano)."},
    # --- SDXL ---
    "isometric-v1.safetensors": {
        "url": "https://civitai.com/models/151008", "trigger": "isometric style",
        "observar": "Axonometría; el más liviano del set SDXL (rank 16)."},
    "Architectural_Massing.safetensors": {
        "url": "https://civitai.com/models/724833", "trigger": "",
        "observar": "Masa y volumetría (rank 32)."},
    "Architecture_Building.safetensors": {
        "url": "https://civitai.com/models/731161", "trigger": "",
        "observar": "Edificio como sujeto; sustituye al ArchViz de ArteFactoryLab (rank 32)."},
    "baroque_architecture-000006.safetensors": {
        "url": "https://civitai.com/models/336095", "trigger": "",
        "observar": "Barroco; sustituye al brutalista XL de JJ (rank 64)."},
    "ArcvizXL_V01.safetensors": {
        "url": "https://civitai.com/models/549260", "trigger": "archviz 1",
        "observar": "Archviz interior/exterior; el más pesado (rank 128, 870 MB)."},
    "bookstore-xl.safetensors": {
        "url": "https://civitai.com/models/139539", "trigger": "mrares, bookstore",
        "observar": "Interior de librería (rank 128, 870 MB)."},
    "SLskyscraperrenderingXL_V1.0.safetensors": {
        "url": "https://civitai.com/models/198528", "trigger": "",
        "observar": "Render de rascacielos (rank 128, 870 MB)."},
    # --- FLUX (no local) ---
    "rhino-to-image-lora.basic.safetensors": {
        "url": "", "trigger": "",
        "observar": "LoRA del curso (FLUX.2). No corre local: va en pod (RunPod 24 GB)."},
}


# --- Solapa Curso: tema + tarjetas de lo que arma el curso --------------------
# NOTA ES: el tema es fijo (plaza Sagrada Familia) y las tarjetas salen del
# CSV del curso (AI-course.csv) cruzado con el catálogo LORAS. Variaciones de
# LoRA solo SD1.5 y SDXL: son las que corren en la máquina.
TEMA = {
    "titulo": "Plaça de la Sagrada Família — Barcelona",
    "sujeto": "Todo lo del curso se trabaja en torno a la plaza: renders, img2img, video y 3D parten de este sujeto.",
    "bases": ["SD 1.5 · architecturerealmix (local + ControlNet)",
              "SDXL · Juggernaut XL (local*, sin ControlNet)"],
}

SD15_NOMBRES = {
    "JJ_Archvizcg_v2.safetensors", "sandiese.safetensors",
    "xsarchitectural-10superhighrisebuilding.safetensors", "room.safetensors",
    "landscape_architecture_sketch.safetensors",
    "Le Corbusier 2.2.7.2_sd1.5-000016.safetensors", "BrutalistTech-20.safetensors",
    "archisketch-v1.safetensors", "markerhandsketch-V1.safetensors",
}
SDXL_NOMBRES = {
    "isometric-v1.safetensors", "Architectural_Massing.safetensors",
    "Architecture_Building.safetensors", "baroque_architecture-000006.safetensors",
    "ArcvizXL_V01.safetensors", "bookstore-xl.safetensors",
    "SLskyscraperrenderingXL_V1.0.safetensors",
}


def construir_curso():
    """Tarjetas 1:1 del tablero Miro: qué es, a qué refiere, dónde corre.

    NOTA ES: cada entrada del Miro tiene su tarjeta. Links SOLO verificados
    con HTTP 200 (2026-10-30): los del CSV, los del inventario Miro del vault
    y los 3 del curso (SDXL base, archmat, FLUX.2-4B). Lo no verificado
    (Topaz 403 anti-bots, Seedance sin DNS, guía BFL movida) queda SIN link
    con nota "ver Miro" — una tarjeta sin link es honesta, un link muerto no.
    """
    items = []

    def add(cat, titulo, detalle, modulo, corre, links=None):
        items.append({"cat": cat, "titulo": titulo, "detalle": detalle,
                      "modulo": modulo, "corre": corre, "links": links or []})

    U = lambda t, u: {"t": t, "u": u}
    MIRO = "https://miro.com/app/board/uXjVHRM2XQU=/"

    # --- Módulo 1 · base ---
    add("Módulo 1 · base", "SD 1.5 live demo",
        "Demo en vivo del flujo base de 7 nodos. Equivale a GX-01.", "Módulo 1 · base", "local")
    add("Módulo 1 · base", "3 ways of prompting",
        "Tres maneras de promptear del curso (tarjeta del tablero).", "Módulo 1 · base", "curso")
    add("Módulo 1 · base", "Prompt Coach setup",
        "Rol que interroga el prompt (modelo, conciso/largo) + guía de prompts.", "Módulo 1 · base", "curso",
        [U("guía de prompts", "https://stable-diffusion-art.com/prompt-guide/")])
    add("Módulo 1 · base", "Comfy Expert setup",
        "Rol experto en Comfy Cloud para responder con docs.", "Módulo 1 · base", "curso",
        [U("docs ComfyUI", "https://docs.comfy.org/"), U("wiki ComfyUI", "https://comfyui-wiki.com/en")])

    # --- Módulo 2 · texto a imagen (comparativas + LoRAs + upscaling) ---
    add("Módulo 2 · modelos", "SD 1.5",
        "Comparativa base del curso. Local: architecturerealmix.", "Módulo 2", "local")
    add("Módulo 2 · modelos", "SDXL base",
        "El curso lo propone como salto de calidad sobre SD1.5.",
        "Módulo 2", "local*", [U("stabilityai/sdxl-base-1.0", "https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0")])
    add("Módulo 2 · modelos", "archmat",
        "LoRA/materialidad arquitectónica. El curso lo marca para SDXL.",
        "Módulo 2", "local*", [U("civitai 656784", "https://civitai.com/models/656784/archmat")])
    add("Módulo 2 · modelos", "FLUX.1 dev",
        "Comparativa del curso; requiere text encoders (no local).",
        "Módulo 2", "pod", [U("FLUX.1-dev", "https://huggingface.co/black-forest-labs/FLUX.1-dev")])
    add("Módulo 2 · modelos", "FLUX.2 Klein 9B",
        "Stack 18,3 GB. Comparativa + LoRA 50% y 100%.", "Módulo 2", "pod")
    add("Módulo 2 · modelos", "FLUX.2 Klein 4B (adaptadores)",
        "Adaptadores livianos 4B que propone el curso.",
        "Módulo 2", "pod", [U("búsqueda HF", "https://huggingface.co/models?other=base_model:adapter:black-forest-labs/FLUX.2-klein-4B")])
    for nombre, info in LORAS.items():
        if nombre in SD15_NOMBRES:
            base, corre, mod = "SD 1.5", "local", "Módulo 2"
        elif nombre in SDXL_NOMBRES:
            base, corre, mod = "SDXL", "local*", "Módulo 2"
        else:
            base, corre, mod = "FLUX.2", "pod", "Módulo 7"
        trig = info["trigger"] or "sin trigger declarado"
        add("Módulo 2 · LoRAs " + base, nombre.replace(".safetensors", ""),
            info["observar"] + " Trigger: " + trig + ".", mod, corre,
            [U("descarga", info["url"])] if info["url"] else [])
    add("Módulo 2 · LoRAs", "rhino basic / premium",
        "LoRAs del curso (FLUX): basic incluido, premium. Con/sin LoRA en el canvas.", "Módulo 2", "pod")
    add("Módulo 2 · edición", "Nano Banana Pro",
        "Edición con IA sin metadata. Skill nano-banana en el CSV.", "Módulo 2", "nube")
    add("Módulo 2 · upscaling", "SeedVR2 (workflow 1)",
        "Upscaling del curso, nube paga.", "Módulo 2", "nube")
    add("Módulo 2 · upscaling", "Topaz (workflow 2)",
        "Upscaling pago. Reemplazo local: RealESRGAN x4plus (en disco). Sitio con anti-bots: ver Miro.", "Módulo 2", "local")
    add("Módulo 2 · upscaling", "FLUX.1 (workflow 3)",
        "Upscaling del curso, nube/pod.", "Módulo 2", "pod")
    add("Módulo 2 · upscaling", "Krea (workflow 4)",
        "Upscaling del curso.",
        "Módulo 2", "nube", [U("krea.ai", "https://www.krea.ai/")])
    add("Módulo 2 · método", "Spectrum + Creativity 1/10–9/10",
        "Ejes del canvas para comparar fidelidad vs creatividad.", "Módulo 2", "curso")

    # --- Módulo 3 · imagen a imagen ---
    add("Módulo 3 · método", "Imagen 1 — Massing",
        "De la imagen de massing se extrae: geometría, stacking, cantilevers, setbacks, voids, proporciones, cámara.", "Módulo 3", "curso")
    add("Módulo 3 · método", "Imagen 2 — Referencia estética",
        "De la referencia: materialidad, temperatura de color, luz, atmósfera, superficies.", "Módulo 3", "curso")
    add("Módulo 3 · método", "JSON camera-lock",
        "Plantilla del curso: massing de imagen 1 + materialidad de imagen 2, MATCH CAMERA EXACTLY.", "Módulo 3", "curso")
    add("Módulo 3 · video", "Kling website (alternativa)",
        "El curso da la web de Kling como alternativa al workflow.",
        "Módulo 3", "nube", [U("guía Kling", "https://kling.ai/quickstart/klingai-video-3-model-user-guide")])

    # --- Módulo 4 · imagen a video ---
    add("Módulo 4 · video", "Seedance 2.0 (single/multi/start)",
        "El curso propone Seedance: 1 imagen, varias o frame inicial. Guía con DNS caído al 2026-10-30: ver Miro.", "Módulo 4", "nube")
    add("Módulo 4 · video", "LTX (workflow 1)",
        "Video local-en-pod. Modelos LTX faltan; probar en Cloud Free.",
        "Módulo 4", "pod",
        [U("guía LTX-2.3", "https://ltx.io/model/model-blog/ltx-2-3-prompt-guide"),
         U("skill ltx-v2", "https://mcpmarket.com/tools/skills/ltx-v2-video-generation")])
    add("Módulo 4 · video", "Kling (workflow 2)",
        "Video en nube paga.",
        "Módulo 4", "nube", [U("guía Kling", "https://kling.ai/quickstart/klingai-video-3-model-user-guide")])
    add("Módulo 4 · video", "Interpolación 7s→14s",
        "Nota del curso: estirar el clip en edición.", "Módulo 4", "pod")
    add("Módulo 4 · video", "Timelapse trípode fijo",
        "Edificio estático; nubes, sol/sombras, gente y plantas en movimiento. Sin cámara.", "Módulo 4", "pod")
    add("Módulo 4 · video", "Preparation geométrica + Google Omni",
        "Paso para que el modelo entienda la geometría + skill import.", "Módulo 4", "pod")

    # --- Módulo 5 · imagen a 3D ---
    for prep in ["Clay blanco axonométrico", "Backside imaginado", "4 vistas en mosaico",
                 "Maqueta en concreto", "Normal map", "Hiperrealista→Rhino",
                 "Sin textura limpio", "Ambient occlusion"]:
        add("Módulo 5 · preparación", prep,
            "Prompt del curso. Todo IMPORTABLE IN COMFY.", "Módulo 5", "pod")
    add("Módulo 5 · workflow", "Workflow 2 + ComfyUI-3D-Pack",
        "Custom node + modelos faltan → pod.", "Módulo 5", "pod")

    # --- Módulo 6 · panel ---
    add("Módulo 6 · criterio", "Panel discussion",
        "Sin workflow: el jurado va por script + checklist.", "Módulo 6", "local")

    # --- Módulo 7 · Gaudí ---
    add("Módulo 7 · Gaudí", "VARIANT B (Gaudí nombrable)",
        "Igual a INSTRUCTION.md var. A pero puede nombrar a Gaudí y sus obras. Morph 0–10 (default 7), ADN constructivo, prohibido decorativo.", "Módulo 7", "pod")
    add("Módulo 7 · Gaudí", "CLAY STYLE fijo",
        "Arcilla blanca mate, camera lock, sin color ni trencadís.", "Módulo 7", "pod")
    add("Módulo 7 · Gaudí", "Rhino-to-Gaudí + live demo",
        "Flujo massing→arcilla→hyperreal con la LoRA del curso + calidades espaciales y de textura.", "Módulo 7", "pod")
    add("Módulo 7 · Gaudí", "LoRA rhino basic / premium",
        "Basic incluido en el curso; premium. Ambas FLUX → pod.", "Módulo 7", "pod")
    add("Módulo 7 · referente", "thomasnelissen.ai",
        "Sitio del instructor.",
        "Módulo 7", "curso", [U("thomasnelissen.ai", "https://thomasnelissen.ai")])

    # --- Recursos del curso ---
    add("Recursos", "Tablero Miro (login + Gaudi2026)",
        "Canvas completo del curso: el origen de estas tarjetas.",
        "Todos", "curso", [U("abrir Miro", MIRO)])
    add("Recursos", "Área de participantes (login)",
        "Videos, workflows y PDFs del curso.", "Todos", "curso", [U("archademy.ai", AREA_CURSO)])
    add("Recursos", "Prompt Coach + Comfy Expert",
        "Roles del curso (textos completos en el CSV).", "Módulo 1", "curso",
        [U("guía de prompts", "https://stable-diffusion-art.com/prompt-guide/"),
         U("docs ComfyUI", "https://docs.comfy.org/")])
    return items


# --- Cirugía de la plantilla (anclas exactas; falla fuerte si cambian) --------
# NOTA ES: cada reemplazo exige encontrar el ancla UNA sola vez. Si la galería
# cambia y el ancla desaparece o se duplica, el script grita en vez de generar
# un tablero roto a medias.
def inj(plantilla, ancla, reemplazo):
    """Reemplaza un ancla exacta una sola vez; si no, falla con mensaje claro."""
    n = plantilla.count(ancla)
    if n != 1:
        raise SystemExit("ancla rota (aparece %d veces, se esperaba 1): %r" % (n, ancla[:70]))
    return plantilla.replace(ancla, reemplazo, 1)


CSS_EXTRA = """
  /* ---------- tablero del curso ---------- */
  a.btn { text-decoration:none; display:inline-block; }
  #notas-titulo { margin:14px 0 6px; font-size:13px; text-transform:uppercase;
                 letter-spacing:.6px; color:#5a6070; }
  #notas-box { background:#eef3ec; border:1px solid #cfdcc9; border-radius:4px;
               padding:11px 13px; white-space:pre-wrap; word-break:break-word;
               font-size:12.5px; color:#262a33; }
  #lora-box { background:#eef3ec; border:1px solid #cfdcc9; border-radius:4px;
               padding:11px 13px; white-space:pre-wrap; word-break:break-word;
               font-size:12.5px; color:#262a33; }
  #lora-titulo { margin:14px 0 6px; font-size:13px; text-transform:uppercase;
                 letter-spacing:.6px; color:#5a6070; }
  #lora-box a { color:#0b6e5f; }
  #wf-titulo { margin:14px 0 6px; font-size:13px; text-transform:uppercase;
               letter-spacing:.6px; color:#5a6070; }
  #wf-box { background:#eef3ec; border:1px solid #cfdcc9; border-radius:4px;
            padding:11px 13px; font-size:12.5px; color:#262a33; }
  #wf-box a { color:#0b6e5f; }
  /* ---------- solapa Matriz ---------- */
  #matriz-panel { position:fixed; top:52px; left:0; right:0; bottom:0; overflow:auto;
                  padding:14px; background:var(--fondo); z-index:30; }
  #matriz-panel.oculto { display:none; }
  .mnota { color:var(--tenue); font-size:11.5px; margin:2px 0 8px; }
  .mbanda { position:relative; height:26px; background:var(--panel);
            border:1px solid var(--linea); border-radius:6px; margin:4px 0 10px; }
  .mbanda-work { position:absolute; top:0; bottom:0; background:rgba(127,209,193,.15);
                 border-left:1px dashed var(--acento); border-right:1px dashed var(--acento); }
  .mtick { position:absolute; top:4px; width:8px; height:18px; margin-left:-4px;
           background:#8d95a3; border-radius:2px; }
  .mtick.opt { background:var(--acento); }
  .moptflag { position:absolute; top:-17px; transform:translateX(-50%); font-size:10.5px;
              color:var(--acento); white-space:nowrap; }
  .mcards { display:flex; gap:10px; flex-wrap:wrap; margin-bottom:16px; }
  .mcard { width:150px; border:1px solid var(--linea); border-radius:8px; overflow:hidden;
           background:var(--panel); cursor:pointer; }
  .mcard img { display:block; width:100%; height:auto; }
  .mmeta { padding:5px 7px; font-size:11px; color:var(--tenue); display:flex; gap:6px;
           align-items:center; flex-wrap:wrap; }
  .mmeta b { color:var(--texto); }
  .mopt { color:#0b2b26; background:var(--acento); border-radius:4px; padding:0 5px; font-size:10px; }
  #flujos { position:fixed; top:52px; right:0; bottom:0; width:340px; overflow:auto;
            border-left:1px solid var(--linea); background:var(--panel);
            padding:10px 12px; z-index:40; }
  #flujos.oculto { display:none; }
  .flujo { border:1px solid var(--linea); border-radius:8px; padding:9px 10px; margin-bottom:10px; }
  .flujo-t { font-weight:600; margin-bottom:2px; }
  .flujo-e { color:var(--acento); font-size:11px; margin-bottom:6px; }
  .flujo a { color:var(--acento); }
  .flujo-ruta { color:var(--tenue); font-size:11px; margin-top:4px; word-break:break-word; }
  .flujo-ruta b { color:var(--texto); }
  .flujo-notas { margin-top:6px; font-size:11.5px; white-space:pre-wrap;
                 border-top:1px dashed var(--linea); padding-top:6px; }
  .flujo-links { font-size:11px; color:var(--tenue); margin-bottom:10px; }
  .flujo-links a { color:var(--acento); }
  /* ---------- solapa Curso ---------- */
  #curso-panel { position:fixed; top:52px; left:0; right:0; bottom:0; overflow:auto;
                 padding:14px; background:var(--fondo); z-index:30; }
  #curso-panel.oculto { display:none; }
  .tema { border:1px solid var(--acento); border-radius:8px; padding:10px 12px;
          margin-bottom:12px; background:var(--panel); }
  .tema-bases { color:var(--tenue); font-size:11.5px; margin-top:4px; }
  .cseccion { margin:10px 0 8px; font-size:11px; text-transform:uppercase;
              letter-spacing:.7px; color:var(--tenue); display:flex; gap:10px; align-items:baseline; }
  .cseccion b { color:var(--texto); font-size:13px; letter-spacing:0; text-transform:none; }
  .cgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr));
           gap:10px; margin-bottom:14px; }
  .ctarjeta { border:1px solid var(--linea); border-radius:8px; padding:9px 10px;
              background:var(--panel); }
  .ct-t { font-weight:600; margin-bottom:4px; }
  .ct-d { color:var(--tenue); font-size:11.5px; }
  .ct-pie { display:flex; gap:8px; align-items:center; margin-top:6px;
            font-size:11px; color:var(--tenue); }
  .ct-pie a { color:var(--acento); }
  .corre { color:#fff; border-radius:4px; padding:1px 6px; font-size:10px; }
  /* ---------- tarjeta fullscreen ---------- */
  #carta-full { position:fixed; inset:0; background:rgba(6,7,9,.94); z-index:85;
                overflow:auto; padding:30px 20px; }
  #carta-full.oculto { display:none; }
  #carta { max-width:640px; margin:0 auto; background:var(--panel);
           border:1px solid var(--linea); border-radius:10px; padding:18px 20px; }
  #carta h2 { margin:0 0 8px; font-size:20px; }
  #carta .ct-pie { margin:10px 0; }
  #carta .links a { display:block; margin:5px 0; color:var(--acento);
                    word-break:break-all; font-size:12.5px; }
  #carta .cerrar { float:right; }
"""

JS_FLUJOS = """
// ------------------------------------------------------- panel de flujos
function pintarFlujos(){
  const box = document.getElementById("flujos");
  if (!box) return;
  const links = `<div class="flujo-links">Fuentes del concurso: `
    + `<a href="${esc(LINKS.area)}" target="_blank" rel="noopener">área de participantes</a> · `
    + `<a href="${esc(LINKS.brief_es)}" target="_blank" rel="noopener">briefing ES</a> · `
    + `tablero Miro (ver NOTA en el vault) · criterio: ${esc(LINKS.criterio)}</div>`;
  box.innerHTML = `<div class="fgrupo"><h3>Flujos del curso</h3>` + links + FLUJOS.map(f =>
    `<div class="flujo"><div class="flujo-t">${esc(f.modulo)} — ${esc(f.titulo)}</div>`
    + `<div class="flujo-e">estado: ${esc(f.estado)}</div>`
    + `<div><a href="${esc(f.video)}" target="_blank" rel="noopener">video en el área de participantes</a></div>`
    + (f.transcript ? `<div class="flujo-ruta">transcripción: ${esc(f.transcript)}</div>` : "")
    + (f.workflow_gx
      ? `<div class="flujo-ruta">abrir en Comfy (pestaña Workflows): <b>${esc(f.workflow_gx)}</b> · `
        + `<a href="${esc(LINKS.comfy)}" target="_blank" rel="noopener">abrir ComfyUI</a></div>`
      : `<div class="flujo-ruta">workflow: pendiente</div>`)
    + (f.notas ? `<div class="flujo-notas"><b>NOTAS — qué se puede cambiar</b>\n${esc(f.notas)}</div>` : "")
    + `</div>`).join("") + `</div>`;
}
"""

JS_SOLAPA = """
// ------------------------------------------------------- solapa Curso
function pintarCurso(){
  const box = document.getElementById("curso-panel");
  if (!box) return;
  const grupos = new Map();
  CURSO.forEach((c, idx) => { c.__k = idx; if(!grupos.has(c.cat)) grupos.set(c.cat,[]); grupos.get(c.cat).push(c); });
  const color = {local:"#2fa47c", "local*":"#c9a227", pod:"#4f9cf0", nube:"#8d95a3", curso:"#6b7cff"};
  box.innerHTML = `<div class="tema"><b>${esc(TEMA.titulo)}</b><div>${esc(TEMA.sujeto)}</div>`
    + `<div class="tema-bases">${TEMA.bases.map(b => esc(b)).join(" · ")}</div>`
    + `<div class="tema-bases">tablero ${esc(VERSION)} · ${CURSO.length} tarjetas · clic en tarjeta = pantalla completa</div></div>`
    + [...grupos.entries()].map(([cat, arr]) =>
      `<div class="cseccion"><b>${esc(cat)}</b><span>${arr.length}</span></div><div class="cgrid">` + arr.map(c =>
        `<div class="ctarjeta" data-k="${c.__k}"><div class="ct-t">${esc(c.titulo)}</div>`
        + `<div class="ct-d">${esc(c.detalle)}</div>`
        + `<div class="ct-pie"><span class="corre" style="background:${color[c.corre]||"#666"}">${esc(c.corre)}</span>`
        + `<span>${esc(c.modulo)}</span>`
        + `<span>${(c.links||[]).length} link${(c.links||[]).length===1?"":"s"}</span>`
        + `</div></div>`).join("") + `</div>`).join("");
  box.querySelectorAll(".ctarjeta").forEach(el => el.onclick = () => abrirCarta(Number(el.dataset.k)));
}
// NOTA ES: la tarjeta abre en pantalla completa (overlay propio, no la
// Polaroid de imágenes): título, detalle, badge, módulo y TODOS los links.
function abrirCarta(k){
  const c = CURSO[k]; if(!c) return;
  const color = {local:"#2fa47c", "local*":"#c9a227", pod:"#4f9cf0", nube:"#8d95a3", curso:"#6b7cff"};
  document.getElementById("carta").innerHTML =
    `<button class="btn cerrar" id="carta-x">cerrar ✕</button>`
    + `<h2>${esc(c.titulo)}</h2>`
    + `<div class="ct-pie"><span class="corre" style="background:${color[c.corre]||"#666"}">${esc(c.corre)}</span>`
    + `<span>${esc(c.modulo)}</span><span>${esc(c.cat)}</span></div>`
    + `<div class="ct-d" style="font-size:13px;color:var(--texto)">${esc(c.detalle)}</div>`
    + `<div class="links">${(c.links||[]).map(l =>
        `<a href="${esc(l.u)}" target="_blank" rel="noopener">↗ ${esc(l.t)} — ${esc(l.u)}</a>`).join("")
        || "<span style='color:var(--tenue)'>sin link verificado: ver tablero Miro</span>"}</div>`;
  document.getElementById("carta-full").classList.remove("oculto");
  document.getElementById("carta-x").onclick = () =>
    document.getElementById("carta-full").classList.add("oculto");
  window.scrollTo(0,0);
}
document.getElementById("carta-full").addEventListener("click", e => {
  if (e.target.id === "carta-full") e.target.classList.add("oculto");
});
document.addEventListener("keydown", e => {
  if (e.key === "Escape") document.getElementById("carta-full").classList.add("oculto");
});
function solapa(nombre){
  ["repasadas", "curso", "matriz"].forEach(v => {
    document.getElementById("tab-" + v).classList.toggle("activo", v === nombre);
  });
  const rep = nombre === "repasadas";
  document.getElementById("contenido").style.display = rep ? "" : "none";
  document.getElementById("facetas").style.display = rep ? "" : "none";
  document.getElementById("flujos").classList.add("oculto");
  document.getElementById("curso-panel").classList.toggle("oculto", nombre !== "curso");
  document.getElementById("matriz-panel").classList.toggle("oculto", nombre !== "matriz");
}
// NOTA ES: sin estas dos líneas los botones existen pero el clic no hace
// nada (fue la causa del "la solapa no funciona": todo rendía bien en Node,
// pero ningún handler llamaba a solapa en el navegador).
document.getElementById("tab-repasadas").onclick = () => solapa("repasadas");
document.getElementById("tab-curso").onclick = () => solapa("curso");
document.getElementById("tab-matriz").onclick = () => solapa("matriz");
// NOTA ES: arranque con red: si una vista revienta en el navegador, el error
// queda ESCRITO en la página (barra roja) en vez de silencio. Sin F12.
function boot(){
  const errs = [];
  try { pintar(); } catch(e){ errs.push("repasadas: " + e.message); }
  try { pintarFlujos(); } catch(e){ errs.push("flujos: " + e.message); }
  try { pintarCurso(); } catch(e){ errs.push("curso: " + e.message); }
  try { pintarMatriz(); } catch(e){ errs.push("matriz: " + e.message); }
  if (errs.length) {
    const d = document.createElement("div");
    d.style.cssText = "position:fixed;bottom:0;left:0;right:0;background:#7a1f1f;color:#fff;"
      + "padding:8px 12px;z-index:99;font-size:12px";
    d.textContent = "ERRORES: " + errs.join(" | ");
    document.body.appendChild(d);
  }
}
// ------------------------------------------------------- solapa Matriz
// NOTA ES: grilla de ejes medidos vs óptimo. Cada miniatura abre la Polaroid
// (abrirMid traduce mid → índice visible). Sin librerías: divs + CSS.
function filaPorMid(mid){
  return DATOS.find(r => r.mid === mid);
}
function imgDims(r){
  const dm = String(r.resolucion || "").match(/(\d+)\s*x\s*(\d+)/i);
  return dm ? ` width="${dm[1]}" height="${dm[2]}"` : "";
}
function cartaMatriz(p, eje){
  const r = filaPorMid(p.mid);
  if (!r) return "";
  const seg = (r.segundos != null) ? `<span>${r.segundos}s</span>` : "";
  const esOpt = (eje.optimo != null && String(p.valor) === String(eje.optimo));
  return `<div class="mcard" data-mid="${esc(p.mid)}">`
    + `<img src="${esc(IMG[String(r.__k)] || "")}"${imgDims(r)} loading="lazy" alt="${esc(p.mid)}">`
    + `<div class="mmeta"><b>${esc(p.mid)}</b>`
    + `<span>${esc(String(p.valor))}${eje.unidad ? " " + esc(eje.unidad) : ""}</span>`
    + seg + (esOpt ? `<span class="mopt">óptimo</span>` : "") + `</div></div>`;
}
function abrirMid(mid){
  const r = filaPorMid(mid);
  if (!r) return;
  const vi = visibles.findIndex(x => x.__k === r.__k);
  if (vi >= 0) abrir(vi);
}
function pintarMatriz(){
  const box = document.getElementById("matriz-panel");
  if (!box) return;
  box.innerHTML = `<div class="tema"><b>Matriz de testeo — SD 1.5 · seed 42</b>`
    + `<div class="tema-bases">Lo MEDIDO (miniaturas, con segundos) contra el ÓPTIMO (bandera). Clic = Polaroid.</div></div>`
    + MATRIZ.map(eje => {
      const cards = eje.puntos.map(p => cartaMatriz(p, eje)).join("");
      let escala = "";
      if (eje.tipo === "numerico") {
        const vs = eje.puntos.map(p => p.valor);
        const lo = (eje.min != null) ? eje.min : Math.min.apply(null, vs);
        const hi = (eje.max != null) ? eje.max : Math.max.apply(null, vs);
        const pos = v => (hi === lo) ? 50 : ((v - lo) / (hi - lo) * 100);
        let banda = "";
        if (eje.banda) {
          const l = Math.max(0, Math.min(100, pos(eje.banda[0])));
          const rr = Math.max(0, Math.min(100, pos(eje.banda[1])));
          banda = `<div class="mbanda-work" style="left:${l}%;width:${Math.max(0, rr - l)}%" title="rango de trabajo"></div>`;
        }
        const ticks = eje.puntos.map(p => {
          const cl = (eje.optimo != null && String(p.valor) === String(eje.optimo)) ? "mtick opt" : "mtick";
          return `<div class="${cl}" style="left:${pos(p.valor)}%" title="${esc(p.mid)} = ${esc(String(p.valor))}"></div>`;
        }).join("");
        const flag = (eje.optimo != null)
          ? `<div class="moptflag" style="left:${pos(eje.optimo)}%">▼ óptimo ${esc(String(eje.optimo))}</div>` : "";
        escala = `<div class="mbanda">${banda}${ticks}${flag}</div>`;
      }
      return `<div class="cseccion"><b>${esc(eje.titulo)}</b><span>${eje.puntos.length}</span></div>`
        + `<div class="mnota">${esc(eje.nota)}</div>` + escala + `<div class="mcards">${cards}</div>`;
    }).join("");
  box.querySelectorAll(".mcard").forEach(el => el.onclick = () => abrirMid(el.dataset.mid));
}
"""


# --- Matriz de testeo: ejes medidos vs óptimo ----------------------------------
# NOTA ES: segundos medidos 2026-10-29 (matriz-txt2img.md). "optimo" es el
# default del flujo base salvo evidencia (steps: M15 no justifica 3× tiempo).
# La fuerza LoRA solo se midió @0.8: el rango 0.6–0.9 es de trabajo, no medido.
SEGUNDOS = {"M01": 195.4, "M03": 175.3, "M04": 160.3, "M05": 165.4, "M06": 175.3,
            "M07": 170.2, "M08": 160.3, "M14": 65.1, "M15": 210.4, "M16": 140.2,
            "M17": 135.2, "M18": 135.3, "M19": 120.2, "M20": 190.4}

EJES_MATRIZ = [
    {"titulo": "Steps (SD 1.5, resto fijo)", "tipo": "numerico", "unidad": "steps",
     "optimo": 30,
     "nota": "Medido 10→65s · 30→195s · 50→210s. Óptimo 30: el detalle extra de 50 no justifica 3× tiempo.",
     "puntos": [{"mid": "M14", "valor": 10}, {"mid": "M01", "valor": 30}, {"mid": "M15", "valor": 50}]},
    {"titulo": "CFG", "tipo": "numerico", "unidad": "cfg", "optimo": 7,
     "nota": "Medido 3 / 7 / 12. Óptimo 7.",
     "puntos": [{"mid": "M16", "valor": 3}, {"mid": "M01", "valor": 7}, {"mid": "M17", "valor": 12}]},
    {"titulo": "Resolución", "tipo": "categorias", "unidad": "", "optimo": "768×512",
     "nota": "512² rápido (120s) · base 768×512 · 768² detalle (190s).",
     "puntos": [{"mid": "M19", "valor": "512×512"}, {"mid": "M01", "valor": "768×512"}, {"mid": "M20", "valor": "768×768"}]},
    {"titulo": "Sampler", "tipo": "categorias", "unidad": "", "optimo": "euler + normal",
     "nota": "Base euler+normal vs dpmpp_2m+karras.",
     "puntos": [{"mid": "M01", "valor": "euler + normal"}, {"mid": "M18", "valor": "dpmpp_2m + karras"}]},
    {"titulo": "LoRA · fuerza", "tipo": "numerico", "unidad": "strength", "optimo": 0.8,
     "min": 0.5, "max": 1.0, "banda": [0.6, 0.9],
     "nota": "Medido SOLO @0.8 (160–175s). Rango de trabajo 0.6–0.9: falta barrerlo.",
     "puntos": [{"mid": m, "valor": 0.8} for m in ["M03", "M04", "M05", "M06", "M07", "M08"]]},
    {"titulo": "LoRA · identidad", "tipo": "categorias", "unidad": "", "optimo": None,
     "nota": "Misma seed y prompt en todo: el delta visible ES el LoRA.",
     "puntos": [{"mid": "M01", "valor": "sin LoRA"}, {"mid": "M03", "valor": "Archvizcg"},
                {"mid": "M04", "valor": "sandiese"}, {"mid": "M05", "valor": "BrutalistTech"},
                {"mid": "M06", "valor": "Le Corbusier"}, {"mid": "M07", "valor": "room"},
                {"mid": "M08", "valor": "XSarchitectural"}]},
]


def plantilla_curso(gal):
    """Deriva la plantilla del tablero desde la de la galería."""
    h = gal.HTML
    h = inj(h, "<title>Galería de renders · estudio</title>",
            "<title>Curso AI×Gaudí · imágenes repasadas</title>")
    h = inj(h, '<span id="titulo">Galería de renders</span>',
            '<span id="titulo">Curso AI×Gaudí · repasadas</span>'
            '<a class="btn" href="index.html" title="Volver a la galería general">← Galería</a>')
    h = inj(h, 'const EJES = ["base","modelo","lora","tipo","workflow","tags"];',
            'const EJES = ["modulo","flujo","base","modelo","lora","tipo"];\n'
            'const FLUJOS = __FLUJOS__;\nconst LINKS = __LINKS__;')
    h = inj(h, '<option value="workflow">Agrupar: workflow</option>',
            '<option value="modulo" selected>Agrupar: módulo</option>\n'
            '    <option value="flujo">Agrupar: flujo</option>\n'
            '    <option value="workflow">Agrupar: workflow</option>')
    h = inj(h, 'agrupar:"workflow"',
            'agrupar:"modulo"')
    # NOTA ES: el eje nuevo se suma al switch existente, no se reescribe.
    h = inj(h, '    case "seed": return "seed " + (r.seed ?? "—");',
            '    case "seed": return "seed " + (r.seed ?? "—");\n'
            '    case "modulo": return r.modulo || "—";\n'
            '    case "flujo": return r.flujo || "—";')
    h = inj(h, '`${visibles.length} de ${DATOS.length} renders`;',
            '`${visibles.length} de ${DATOS.length} repasadas`;')
    # NOTA ES: corrección del índice de imagen: la galería numera por posición
    # en la vista filtrada (__i) pero el mapa IMG se numera al generar. Con
    # filtros activos eso muestra la imagen de otra fila. Aquí cada fila trae
    # su clave estable __k desde la generación.
    h = inj(h, 'visibles.forEach((r,i) => r.__i = i);',
            'visibles.forEach((r) => r.__i = r.__k);')
    h = inj(h, 'fetch("datos.json?t="',
            'fetch("curso-datos.json?t="')
    h = inj(h, '<div id="prompt-box"></div>',
            '<div id="prompt-box"></div>\n'
            '      <h3 id="notas-titulo">Notas — qué se puede cambiar</h3>\n'
            '      <div id="notas-box"></div>')
    h = inj(h, '<h3 id="notas-titulo">Notas — qué se puede cambiar</h3>\n'
               '      <div id="notas-box"></div>',
            '<h3 id="notas-titulo">Notas — qué se puede cambiar</h3>\n'
            '      <div id="notas-box"></div>\n'
            '      <h3 id="lora-titulo">LoRA — descarga y qué observar</h3>\n'
            '      <div id="lora-box"></div>')
    h = inj(h, '<h3 id="lora-titulo">LoRA — descarga y qué observar</h3>\n'
               '      <div id="lora-box"></div>',
            '<h3 id="lora-titulo">LoRA — descarga y qué observar</h3>\n'
            '      <div id="lora-box"></div>\n'
            '      <h3 id="wf-titulo">Workflow .json</h3>\n'
            '      <div id="wf-box"></div>')
    # (inyección JS de la caja LoRA: más abajo, tras el render de notas,
    # porque su ancla es la salida de esa inyección)
    h = inj(h, 'document.getElementById("full").classList.add("on");',
            'const nb = document.getElementById("notas-box");\n'
            '  if (nb) nb.innerHTML = r.notas\n'
            '    ? `<b>NOTAS — qué se puede cambiar</b>\\n${esc(r.notas)}` : "";\n'
            '  document.getElementById("full").classList.add("on");')
    # NOTA ES: el render arma el HTML con concatenación (+), no con template
    # literals anidados: un backtick dentro de ${...} es legal pero ilegible.
    # En Python se escribe \\n para que al JS llegue \n (salto dentro del texto,
    # no salto real que rompería el literal "..." del JS).
    h = inj(h, '? `<b>NOTAS — qué se puede cambiar</b>\\n${esc(r.notas)}` : "";',
            '? `<b>NOTAS — qué se puede cambiar</b>\\n${esc(r.notas)}` : "";\n'
            '  const li = r.lora_info, lb = document.getElementById("lora-box"),\n'
            '        lt = document.getElementById("lora-titulo");\n'
            '  if (lb) lb.innerHTML = li\n'
            '    ? "<b>LoRA — " + esc(li.nombre) + (li.strength ? " @ " + li.strength : "") + "</b>"\n'
            '      + "\\ntrigger: " + esc(li.trigger || "sin trigger declarado")\n'
            '      + "\\nqué observar: " + esc(li.observar || "—")\n'
            '      + (li.url ? \'\\ndescarga: <a href="\' + esc(li.url) + \'" target="_blank" rel="noopener">\''
            ' + esc(li.url) + "</a>" : "") : "";\n'
            '  if (lt) lt.style.display = li ? "" : "none";\n'
            '  if (lb) lb.style.display = li ? "" : "none";')
    h = inj(h, '  if (lb) lb.style.display = li ? "" : "none";',
            '  if (lb) lb.style.display = li ? "" : "none";\n'
            '  const wb = document.getElementById("wf-box"), wt = document.getElementById("wf-titulo");\n'
            '  if (wb) wb.innerHTML = r.workflow\n'
            '    ? \'<a href="\' + esc(r.workflow) + \'" download>descargar \' + esc(r.workflow.split("/").pop()) + "</a>" : "";\n'
            '  if (wt) wt.style.display = r.workflow ? "" : "none";\n'
            '  if (wb) wb.style.display = r.workflow ? "" : "none";')
    # (la inyección del render de notas vive más arriba, junto a la de la caja LoRA)
    h = inj(h, '</style>', CSS_EXTRA + '</style>')
    h = inj(h, '<button class="btn" id="f-toggle" title="Mostrar u ocultar filtros">Filtros</button>',
            '<button class="btn" id="f-toggle" title="Mostrar u ocultar filtros">Filtros</button>\n'
            '  <button class="btn" id="j-toggle" title="Flujos del curso y notas">Flujos</button>')
    h = inj(h, '<div id="facetas"></div>',
            '<div id="facetas"></div>\n<div id="flujos" class="oculto"></div>')
    h = inj(h, 'document.getElementById("f-toggle").onclick = () =>\n'
               '  document.getElementById("facetas").classList.toggle("oculto");',
            'document.getElementById("f-toggle").onclick = () =>\n'
            '  document.getElementById("facetas").classList.toggle("oculto");\n'
            'document.getElementById("j-toggle").onclick = () =>\n'
            '  document.getElementById("flujos").classList.toggle("oculto");\n'
            + JS_FLUJOS)
    h = inj(h, '<button class="btn" id="j-toggle" title="Flujos del curso y notas">Flujos</button>',
            '<button class="btn" id="j-toggle" title="Flujos del curso y notas">Flujos</button>\n'
            '  <button class="btn activo" id="tab-repasadas" title="Imágenes repasadas">Repasadas</button>\n'
            '  <button class="btn" id="tab-curso" title="Tarjetas de lo que arma el curso">Curso</button>')
    # NOTA ES: reserva de espacio anti-CLS (el auditor lo exige): si la fila
    # trae resolución ("768x512"), se fija como width/height del <img>. Con el
    # CSS existente (width:100%; height:auto) no hay distorsión y el navegador
    # reserva la caja antes de cargar: cero saltos de layout.
    h = inj(h, 'img.src = IMG[String(r.__i)] || ""; img.loading = "lazy"; img.alt = (r.prompt||"").slice(0,80);',
            'img.src = IMG[String(r.__i)] || ""; img.loading = "lazy"; img.alt = (r.prompt||"").slice(0,80);\n'
            '      const dm = String(r.resolucion||"").match(/(\\d+)\\s*x\\s*(\\d+)/i);\n'
            '      if (dm) { img.width = +dm[1]; img.height = +dm[2]; }')
    h = inj(h, 'const img = document.createElement("img"); img.src = IMG[String(r.__i)]||""; img.loading="lazy";',
            'const img = document.createElement("img"); img.src = IMG[String(r.__i)]||""; img.loading="lazy";\n'
            '      const dm2 = String(r.resolucion||"").match(/(\\d+)\\s*x\\s*(\\d+)/i);\n'
            '      if (dm2) { img.width = +dm2[1]; img.height = +dm2[2]; }')
    h = inj(h, '<div id="facetas"></div>\n<div id="flujos" class="oculto"></div>',
            '<div id="facetas"></div>\n<div id="flujos" class="oculto"></div>\n'
            '<div id="curso-panel" class="oculto"></div>\n'
            '<div id="carta-full" class="oculto"><div id="carta"></div></div>')
    h = inj(h, 'const FLUJOS = __FLUJOS__;',
            'const FLUJOS = __FLUJOS__;\nconst CURSO = __CURSO__;\nconst TEMA = __TEMA__;')
    h = inj(h, 'document.getElementById("j-toggle").onclick = () =>\n'
               '  document.getElementById("flujos").classList.toggle("oculto");',
            'document.getElementById("j-toggle").onclick = () =>\n'
            '  document.getElementById("flujos").classList.toggle("oculto");\n'
            + JS_SOLAPA)
    h = inj(h, '\npintar();\n\n// ------------------------------------------------- actualización',
            '\nboot();\n\n// ------------------------------------------------- actualización')
    # NOTA ES: intensidad del LoRA en la tarjeta del mosaico y del lienzo
    # (la Polaroid ya la muestra). Sin strength (M01, parámetros), solo nombre/tipo.
    h = inj(h, 'p.textContent = l.nombre.replace(/\\.safetensors$/,""); pills.appendChild(p);',
            'p.textContent = l.nombre.replace(/\\.safetensors$/,"") + (l.strength != null ? " @" + l.strength : ""); pills.appendChild(p);')
    h = inj(h, 'n.appendChild(img); n.appendChild(b);',
            'const pl = document.createElement("div"); pl.className = "pills";\n'
            '      (r.loras||[]).slice(0,1).forEach(l => {\n'
            '        const pp = document.createElement("span"); pp.className = "pill";\n'
            '        pp.textContent = l.nombre.replace(/\\.safetensors$/,"") + (l.strength != null ? " @" + l.strength : ""); pl.appendChild(pp);\n'
            '      });\n'
            '      n.appendChild(img); n.appendChild(b); n.appendChild(pl);')
    h = inj(h, '<div id="curso-panel" class="oculto"></div>',
            '<div id="curso-panel" class="oculto"></div>\n<div id="matriz-panel" class="oculto"></div>')
    h = inj(h, '<button class="btn" id="tab-curso" title="Tarjetas de lo que arma el curso">Curso</button>',
            '<button class="btn" id="tab-curso" title="Tarjetas de lo que arma el curso">Curso</button>\n'
            '  <button class="btn" id="tab-matriz" title="Matriz de testeo: medido vs óptimo">Matriz</button>')
    h = inj(h, 'const TEMA = __TEMA__;',
            'const TEMA = __TEMA__;\nconst MATRIZ = __MATRIZ__;')
    return h


# --- Filas: metadata del PNG + curaduría del manifiesto ----------------------
def construir_filas(repasadas, indexador, gal):
    """Arma una fila por imagen repasada (metadata ComfyUI + campos del curso)."""
    filas = []
    for rep in repasadas:
        ruta = os.path.abspath(rep["archivo"])
        if not os.path.isfile(ruta):
            print("  (!) no existe:", ruta)
            continue
        try:
            fila = indexador.fila_de(ruta, os.path.dirname(ruta))
        except Exception as exc:  # noqa: BLE001
            print("  (!) no se pudo leer", ruta, exc)
            continue
        try:
            textos = indexador.leer_textos_png(ruta)
        except Exception:
            textos = {}
        grafo = {}
        if "prompt" in textos:
            try:
                grafo = json.loads(textos["prompt"])
            except Exception:
                grafo = {}
        loras = [l["nombre"] for l in fila.get("loras") or []]
        fila["tipo"] = gal.tipo_de(grafo)
        fila["base"] = gal.base_de(fila.get("modelo"), loras)
        fila["clases"] = sorted({n.get("class_type") for n in grafo.values()
                                 if isinstance(n, dict) and n.get("class_type")})
        fila["hsl"] = gal.tono_de(fila.get("seed"))
        # NOTA ES: lora_info cruza el LoRA del PNG con el catálogo LORAS
        # (descarga + trigger + qué observar). Solo el primero: un render
        # repasado tiene un LoRA protagonista.
        info = None
        for l in fila.get("loras") or []:
            if not isinstance(l, dict):
                continue
            cat = LORAS.get(l.get("nombre"))
            if cat:
                info = {"nombre": l.get("nombre"), "strength": l.get("strength"),
                        "url": cat.get("url"), "trigger": cat.get("trigger"),
                        "observar": cat.get("observar")}
                break
        fila["lora_info"] = info
        # NOTA ES: la curaduría manda sobre la metadata: módulo, flujo, título
        # y notas los escribe el equipo al repasar, no los adivina el script.
        fila["modulo"] = rep.get("modulo", "—")
        fila["flujo"] = rep.get("flujo", "—")
        fila["titulo"] = rep.get("titulo", os.path.basename(ruta))
        fila["notas"] = rep.get("notas", "")
        fila["workflow"] = rep.get("workflow", "")
        fila["mid"] = os.path.basename(rep.get("archivo", "")).split("_")[0]
        fila["segundos"] = SEGUNDOS.get(fila["mid"])
        fila["abs_archivo"] = ruta
        filas.append(fila)
    return filas


def copiar_y_generar(filas, out, gal, flujos, links, curso, tema):
    """Copia las imágenes a img-curso/ y escribe curso.html + curso-datos.json."""
    img_dir = os.path.join(out, "img-curso")
    if os.path.isdir(img_dir):
        shutil.rmtree(img_dir)
    os.makedirs(img_dir, exist_ok=True)

    datos, mapa = [], {}
    for f in filas:
        origen = f.get("abs_archivo")
        if not origen or not os.path.isfile(origen):
            continue
        nombre = "%03d_%s.png" % (len(datos), gal.slug(f.get("titulo") or os.path.basename(origen)))
        shutil.copy2(origen, os.path.join(img_dir, nombre))
        f["__k"] = len(datos)  # NOTA ES: clave estable para el mapa IMG (ver fix __i/__k).
        mapa[str(len(datos))] = "img-curso/" + nombre
        datos.append(f)

    version = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = (plantilla_curso(gal)
            .replace("__DATOS__", json.dumps(datos, ensure_ascii=False))
            .replace("__IMG__", json.dumps(mapa, ensure_ascii=False))
            .replace("__VERSION__", json.dumps(version))
            .replace("__FLUJOS__", json.dumps(flujos, ensure_ascii=False))
            .replace("__LINKS__", json.dumps(links, ensure_ascii=False))
            .replace("__CURSO__", json.dumps(curso, ensure_ascii=False))
            .replace("__TEMA__", json.dumps(tema, ensure_ascii=False))
            .replace("__MATRIZ__", json.dumps(EJES_MATRIZ, ensure_ascii=False)))
    with open(os.path.join(out, "curso.html"), "w", encoding="utf-8") as f:
        f.write(html)
    with open(os.path.join(out, "curso-datos.json"), "w", encoding="utf-8") as f:
        json.dump({"version": version, "items": datos}, f, indent=2, ensure_ascii=False)
    return version, len(datos)


# --- Anotaciones en el canvas (notas estilo n8n) -------------------------------
# NOTA ES: ComfyUI trae de fábrica dos nodos de nota — verificado en el fuente
# del frontend 1.45.21 instalado (comfyui_frontend_package/static, el archivo
# `src/extensions/core/noteNode.ts` dentro de core-kRheBl5O.js.map): `Note`
# (texto) y `MarkdownNote` (markdown). Son solo-frontend (`isVirtualNode`):
# la cola los salta y el backend nunca los ve. Consecuencias honestas:
# el validador los reporta como tipos faltantes (esperado), y para encolar
# sin interfaz hay que quitar los nodos "GX ·" antes de enviar el grafo.
# Las notas se hornean en la copia GX durante el sync; el sync no pisa tus
# retoques en el canvas (ver huella_contenido).
MARCA_NOTA = "GX ·"

ANOTACIONES = {
    "GX-01-modulo1-base-txt2img.json": {
        "titulos": {
            1: "1 · Checkpoint SD1.5 — FIJO",
            2: "2 · Prompt + TRIGGER del LoRA",
            3: "3 · Negativo",
            4: "4 · Resolución 768×512",
            5: "5 · KSampler — SE CALIBRA AQUÍ",
            6: "6 · VAE en CPU",
            7: "7 · Salida",
        },
        "notas": [
            {"titulo": "GX · Checkpoint FIJO",
             "texto": "**No se cambia en este flujo.**\n`architecturerealmix_v11` (SD1.5).\nCambiarlo = otro estilo = otro flujo.",
             "pos": [40, -170], "size": [280, 130]},
            {"titulo": "GX · Prompt + TRIGGER",
             "texto": "**Aquí entra el LoRA:** nodo `LoraLoader` entre checkpoint y sampler + palabra trigger en este prompt.\nStrength 0.6–0.9 (matriz: 0.8).",
             "pos": [420, -170], "size": [280, 150]},
            {"titulo": "GX · SE CALIBRA AQUÍ",
             "texto": "**Steps:** 10 rápido (65 s) · 30 base · 50 fino.\n**cfg** 3–12 · **sampler** euler+normal o dpmpp_2m+karras.\n**Seed 42 fija** para comparar.",
             "pos": [800, -170], "size": [280, 150]},
            {"titulo": "GX · Resolución",
             "texto": "**768×512** base · **512²** rápido · **768²** detalle.",
             "pos": [40, 400], "size": [280, 130]},
        ],
    },
}


def huella_contenido(datos, spec):
    """Huella del grafo SIN anotaciones GX (para no repisar tu canvas).

    NOTA ES: quita los nodos "GX ·" y los títulos que gestiona el script;
    lo demás (posiciones, widgets, tus títulos) sí cuenta. El sync solo
    reescribe cuando la FUENTE cambió; tus movimientos en Comfy sobreviven.
    """
    nodos = []
    for n in datos.get("nodes", []):
        if str(n.get("title", "")).startswith(MARCA_NOTA):
            continue
        n = dict(n)
        if spec and n.get("id") in (spec.get("titulos") or {}):
            n.pop("title", None)
        nodos.append(n)
    normal = {"nodes": nodos, "links": datos.get("links", []),
              "groups": datos.get("groups", []), "config": datos.get("config", {})}
    return hashlib.md5(json.dumps(normal, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def anotaciones_al_dia(datos, spec):
    """True si títulos y notas GX están presentes y con el texto vigente."""
    if not spec:
        return True
    nodos = {n.get("id"): n for n in datos.get("nodes", [])}
    for i, t in (spec.get("titulos") or {}).items():
        if nodos.get(i, {}).get("title") != t:
            return False
    textos = {str(n.get("title")): (n.get("widgets_values") or [""])[0]
              for n in datos.get("nodes", [])}
    for nota in spec.get("notas") or []:
        if textos.get(nota["titulo"]) != nota["texto"]:
            return False
    return True


def aplicar_anotaciones(datos, gx, pos_usuario=None):
    """Hornea títulos editoriales + notas MarkdownNote (idempotente)."""
    spec = ANOTACIONES.get(gx)
    if not spec:
        return datos
    nodos = [n for n in datos.get("nodes", [])
             if not str(n.get("title", "")).startswith(MARCA_NOTA)]
    for n in nodos:
        t = (spec.get("titulos") or {}).get(n.get("id"))
        if t:
            n["title"] = t
    ultimo_id = max([n.get("id", 0) for n in nodos] + [0])
    ultimo_orden = max([n.get("order", 0) for n in nodos] + [0])
    pos_usuario = pos_usuario or {}
    for nota in spec.get("notas") or []:
        ultimo_id += 1
        ultimo_orden += 1
        # NOTA ES: si moviste la nota en el canvas, se respeta tu posición;
        # el texto y el título sí se refrescan desde el spec.
        pos, tam = pos_usuario.get(nota["titulo"], (list(nota["pos"]), list(nota["size"])))
        nodos.append({
            "id": ultimo_id, "type": "MarkdownNote",
            "pos": list(pos), "size": list(tam),
            "flags": {}, "order": ultimo_orden, "mode": 0,
            "inputs": [], "outputs": [],
            "properties": {"Node name for S&R": "MarkdownNote", "text": nota["texto"]},
            "title": nota["titulo"], "widgets_values": [nota["texto"]],
        })
    datos["nodes"] = nodos
    datos["last_node_id"] = ultimo_id
    return datos


# --- Sync de workflows a la librería de ComfyUI -------------------------------
def sincronizar_workflows(flujos):
    """Copia los WF del concurso a user/default/workflows/ con prefijo GX-.

    NOTA ES: ComfyUI muestra en la pestaña Workflows del sidebar todo JSON que
    vive en esa carpeta. El sync escribe SOLO si falta el destino o si la
    fuente cambió (huella sin anotaciones): tus retoques en el canvas
    sobreviven a la regeneración. Las anotaciones GX se hornean al escribir.
    """
    for f in flujos:
        fuente = f.get("workflow_fuente")
        gx = f.get("workflow_gx")
        if not fuente or not gx:
            continue
        if not os.path.isfile(fuente):
            print("  (!) fuente ausente:", fuente)
            continue
        destino = os.path.join(os.path.dirname(os.path.abspath(fuente)), gx)
        with open(fuente, encoding="utf-8") as fh:
            datos_fuente = json.load(fh)
        spec = ANOTACIONES.get(gx)
        if os.path.isfile(destino):
            with open(destino, encoding="utf-8") as fh:
                datos_dest = json.load(fh)
            igual = huella_contenido(datos_dest, spec) == huella_contenido(datos_fuente, spec)
            if igual and anotaciones_al_dia(datos_dest, spec):
                print("  GX ya estaba al día:", gx)
                continue
            if igual:
                pos = {str(n.get("title")): (n.get("pos"), n.get("size"))
                       for n in datos_dest.get("nodes", [])
                       if str(n.get("title", "")).startswith(MARCA_NOTA)}
                datos = aplicar_anotaciones(datos_fuente, gx, pos_usuario=pos)
                print("  GX anotado (canvas respetado):", gx)
            else:
                datos = aplicar_anotaciones(datos_fuente, gx)
                print("  GX actualizado desde fuente:", gx)
        else:
            datos = aplicar_anotaciones(datos_fuente, gx)
            print("  GX sincronizado:", gx)
        with open(destino, "w", encoding="utf-8") as fh:
            json.dump(datos, fh, ensure_ascii=False)


def firma(filas, manifiesto):
    """Huella del manifiesto + las imágenes (para detectar cambios en --serve)."""
    partes = [manifiesto]
    try:
        partes.append(str(os.stat(manifiesto).st_mtime_ns))
    except OSError:
        pass
    for f in filas:
        ruta = os.path.abspath(f.get("archivo", ""))
        try:
            partes.append("%s:%d" % (ruta, os.stat(ruta).st_mtime_ns))
        except OSError:
            partes.append(ruta + ":ausente")
    return hashlib.md5("|".join(partes).encode("utf-8")).hexdigest()


def manifiesto_inicial(ruta):
    """Crea curso.json con las dos primeras repasadas (M01 baseline + M03)."""
    inicial = {
        "repasadas": [
            {"archivo": "P:/00-repos/ComfyUI/output/matriz/sd15/M01_00001_.png",
             "modulo": "Módulo 1 · base", "flujo": "WF-01 base",
             "titulo": "M01 baseline SD1.5 sin LoRA",
             "notas": ("Baseline del flujo base: sin LoRA, steps 30, cfg 7, euler/normal, "
                       "768×512, seed 42 (195 s). Punto de comparación para todo lo que cambies.")},
            {"archivo": "P:/00-repos/ComfyUI/output/matriz/sd15/M03_00001_.png",
             "modulo": "Módulo 1 · base", "flujo": "WF-01 base",
             "titulo": "M03 JJ's Archvizcg_v2 @0.8",
             "notas": ("Mismo grafo + LoRA JJ_Archvizcg_v2 @0.8 (175 s). Verificación visual "
                       "contra M01 hecha: el LoRA empuja el estilo archviz sin romper la composición.")},
        ]
    }
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(inicial, f, indent=2, ensure_ascii=False)
    print("manifiesto inicial creado:", ruta)
    return inicial


def main():
    ap = argparse.ArgumentParser(description="Tablero del curso AI×Gaudí (solo repasadas)")
    ap.add_argument("--out", default="activos/web/galeria", help="carpeta del sitio (junto a la galería)")
    ap.add_argument("--curso", default=None, help="manifiesto JSON (default: <out>/curso.json)")
    ap.add_argument("--serve", type=int, metavar="PUERTO", help="servir y regenerar ante cambios")
    ap.add_argument("--una-vez", action="store_true", help="con --serve: generar y salir")
    args = ap.parse_args()

    gal = cargar_galeria()
    indexador = gal.cargar_indexador()
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    ruta_curso = os.path.abspath(args.curso) if args.curso else os.path.join(out, "curso.json")

    if not os.path.isfile(ruta_curso):
        manifiesto = manifiesto_inicial(ruta_curso)
    else:
        with open(ruta_curso, encoding="utf-8") as f:
            manifiesto = json.load(f)
    repasadas = manifiesto.get("repasadas", [])

    def una_pasada():
        with open(ruta_curso, encoding="utf-8") as f:
            rep = json.load(f).get("repasadas", [])
        filas = construir_filas(rep, indexador, gal)
        sincronizar_workflows(FLUJOS)
        return copiar_y_generar(filas, out, gal, FLUJOS, LINKS, construir_curso(), TEMA)

    version, n = una_pasada()
    print("Tablero del curso generado: %s" % os.path.join(out, "curso.html"))
    print("  repasadas: %d | versión: %s" % (n, version))

    if not args.serve:
        print("  para agregar una repasada: editar %s y regenerar" % ruta_curso)
        return 0
    if args.una_vez:
        return 0

    hilo = threading.Thread(target=gal.servir, args=(out, args.serve), daemon=True)
    hilo.start()
    print("  vigilando cambios… (Ctrl+C para salir)")
    with open(ruta_curso, encoding="utf-8") as f:
        ultima = firma(json.load(f).get("repasadas", []), ruta_curso)
    try:
        while True:
            time.sleep(15)
            with open(ruta_curso, encoding="utf-8") as f:
                rep = json.load(f).get("repasadas", [])
            actual = firma(rep, ruta_curso)
            if actual != ultima:
                ultima = actual
                v, n = una_pasada()
                print("  [%s] %d repasadas (actualizado)" % (v, n), flush=True)
    except KeyboardInterrupt:
        print("  cerrado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
