#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcribir-leccion-bunny.py — transcribe en local una leccion del curso AIxGaudi
que NO tiene subtitulos (hoy: el modulo 6, "Round Table").

Que hace, en una frase:
    Lee el indice del curso (raw/yt/transcripts/indice-curso-ai-gaudi.json), baja el
    video del modulo desde el CDN, le extrae el audio con ffmpeg y lo transcribe con
    faster-whisper en la PC, dejando la transcripcion con la convencion del vault.

Por que hace falta:
    El CDN del curso (Bunny Stream) expone los subtitulos .vtt de cada modulo, pero el
    modulo 6 responde 404 en sus dos pistas. La transcripcion es la unica via para
    tener el criterio del jurado, que es el checklist de cierre de los 7 workflows.

Como lo corro:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts\\transcribir-leccion-bunny.py --modulo round-table --language en

Salida:
    - El video (mp4) y el audio (mp3) quedan en activos/curso-ai-gaudi/videos/ (fuera de git).
    - La transcripcion queda en raw/yt/transcripts/YYYY-MM-DD_mux-<slug>.<lang>.md + .srt + .txt
      (misma convencion que scripts/mux_lecciones_curso.py).
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

# NOTA ES: la raiz del vault se deduce de la ubicacion de este archivo (scripts/ esta
#          un nivel arriba del proyecto). Asi el script funciona desde cualquier carpeta.
VAULT = Path(__file__).resolve().parent.parent

# NOTA ES: la carpeta donde viven los binarios. activo/ esta en el .gitignore: los videos
#          y audios del curso son material con derechos y no entran al repositorio.
ACTIVOS_VIDEOS = VAULT / "activos" / "curso-ai-gaudi" / "videos"

# NOTA ES: el indice del curso lo escribio scripts/mux_lecciones_curso.py. Tiene, por
#          cada modulo, su playback id (el identificador del video en el CDN).
INDICE_CURSO = VAULT / "raw" / "yt" / "transcripts" / "indice-curso-ai-gaudi.json"

# NOTA ES: el CDN del curso responde 403 si la peticion no trae el Referer del player.
#          Este es el dominio del iframe de Bunny que embebe los videos.
REFERER = "https://iframe.mediadelivery.net/"

# NOTA ES: la base del CDN se puede leer del propio indice (el script que lo genero la
#          guardo ahi). Si el indice no la trae, usamos esta de respaldo.
CDN_BASE_FALLBACK = "https://vz-4ced3a48-15e.b-cdn.net"


def buscar_ffmpeg():
    """Devuelve la ruta al ejecutable de ffmpeg, o None si no esta."""
    # NOTA ES: ffmpeg se prueba primero en los dos lugares donde lo dejamos antes
    #          (dentro del vault y en P:\\00-repos), y al final en el PATH del sistema.
    candidatos = [
        VAULT / "ffmpeg" / "bin" / "ffmpeg.exe",
        Path(r"P:\00-repos\ffmpeg\bin\ffmpeg.exe"),
    ]
    for c in candidatos:
        if c.exists():
            return c
    # NOTA ES: 'where' es el comando de Windows que lista los ejecutables del PATH.
    try:
        r = subprocess.run(["where", "ffmpeg"], capture_output=True, text=True, shell=True)
        if r.returncode == 0 and r.stdout.strip():
            return Path(r.stdout.strip().splitlines()[0])
    except Exception:
        pass
    return None


def playback_id_del_modulo(indice, modulo):
    """Busca el playback id de un modulo en el indice del curso."""
    # NOTA ES: el indice es una lista de modulos; cada uno trae 'modulo' y, si tiene
    #          video, el playback id dentro de la URL de los subtitulos.
    for mod in indice.get("modulos", []):
        if mod.get("modulo") != modulo:
            continue
        url = mod.get("url", "")
        if url:
            # NOTA ES: la URL tiene la forma BASE/<playback_id>/captions/<lang>.vtt.
            #          Partirla por "/" y quedarse con el quinto elemento (indice 4)
            #          devuelve el id del video.
            partes = url.split("/")
            if len(partes) > 4:
                return partes[4]
    return None


def bajar_video(url_destino, url_origen):
    """Descarga el video del CDN con el Referer que exige."""
    # NOTA ES: si el archivo ya esta y es mas nuevo que nada, se reutiliza: asi una
    #          segunda corrida del script no vuelve a bajar 538 MB.
    if url_destino.exists():
        print("[video] ya existe, se reutiliza: %s" % url_destino.name)
        return url_destino
    # NOTA ES: urllib es la libreria estandar de Python para HTTP. No necesita instalar
    #          nada: por eso el script es reproducible en cualquier maquina con Python.
    req = urllib.request.Request(url_origen, headers={"User-Agent": "Mozilla/5.0", "Referer": REFERER})
    print("[video] bajando (puede tardar varios minutos): %s" % url_origen)
    with urllib.request.urlopen(req, timeout=300) as r, open(url_destino, "wb") as f:
        # NOTA ES: se lee en bloques de 1 MB para no cargar el archivo entero en memoria.
        while True:
            bloque = r.read(1024 * 1024)
            if not bloque:
                break
            f.write(bloque)
    print("[video] listo: %s (%.1f MB)" % (url_destino.name, url_destino.stat().st_size / 1048576))
    return url_destino


def extraer_audio(video, ffmpeg):
    """Saca el audio del video con ffmpeg (a mp3)."""
    # NOTA ES: whisper trabaja con audio; el video es mucho mas pesado. El mp3 es
    #          suficiente para reconocer voz y ocupa una fraccion del espacio.
    audio = video.with_suffix(".mp3")
    if audio.exists() and audio.stat().st_mtime > video.stat().st_mtime:
        print("[audio] reutilizando: %s" % audio.name)
        return audio
    print("[audio] extrayendo con ffmpeg: %s" % video.name)
    cmd = [str(ffmpeg), "-y", "-i", str(video), "-vn", "-acodec", "libmp3lame", "-q:a", "2", str(audio)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        # NOTA ES: algunos builds de ffmpeg vienen sin libmp3lame; el re-encode a mp3
        #          genérico cubre ese caso.
        print("[audio] re-encode con mp3 generico")
        cmd2 = [str(ffmpeg), "-y", "-i", str(video), "-vn", "-acodec", "mp3", str(audio)]
        r2 = subprocess.run(cmd2, capture_output=True, text=True)
        if r2.returncode != 0:
            print(r2.stderr)
            sys.exit(1)
    return audio


def transcribir(audio, modelo, idioma):
    """Transcribe con faster-whisper en CPU y devuelve (texto_con_timestamps, srt)."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("ERROR: faster-whisper no esta instalado. Instalalo con:")
        print('  P:\\Anaconda\\envs\\comfyenv\\python.exe -m pip install faster-whisper')
        sys.exit(1)
    # NOTA ES: device=cpu + compute_type=int8 es la combinacion que corre en la PC
    #          sin GPU dedicada. 'medium' es el equilibrio entre precision y tiempo
    #          (un modulo de 35 min tarda unos minutos).
    print("[whisper] modelo=%s idioma=%s (corre en CPU, puede tardar)" % (modelo, idioma))
    whisper = WhisperModel(modelo, device="cpu", compute_type="int8")
    segmentos, info = whisper.transcribe(str(audio), language=idioma, vad_filter=True)
    print("[whisper] detectado: idioma=%s prob=%.2f duracion=%.1fs"
          % (info.language, info.language_probability, info.duration))
    lineas_txt, lineas_srt = [], []
    for i, seg in enumerate(segmentos, 1):
        # NOTA ES: whisper devuelve tiempos en segundos con decimales; el formato SRT
        #          pide HH:MM:SS,mmm (con coma).
        ini = "%02d:%02d:%06.3f" % (int(seg.start // 3600), int((seg.start % 3600) // 60), seg.start % 60)
        fin = "%02d:%02d:%06.3f" % (int(seg.end // 3600), int((seg.end % 3600) // 60), seg.end % 60)
        ini = ini.replace(".", ",")
        fin = fin.replace(".", ",")
        texto = seg.text.strip()
        lineas_srt.append("%d\n%s --> %s\n%s\n" % (i, ini, fin, texto))
        lineas_txt.append("[%s] %s" % (ini[:8], texto))
    return "\n".join(lineas_txt), "\n".join(lineas_srt)


def escribir_transcripcion(carpeta, slug, titulo, lang, txt, srt, origen):
    """Escribe .md + .srt + .txt con la convencion del vault."""
    hoy = date.today().isoformat()
    base = "%s_mux-%s.%s" % (hoy, slug, lang)
    ruta_md = os.path.join(carpeta, base + ".md")
    ruta_srt = os.path.join(carpeta, base + ".srt")
    ruta_txt = os.path.join(carpeta, base + ".txt")
    with open(ruta_srt, "w", encoding="utf-8") as f:
        f.write(srt)
    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write(txt)
    cab = """---
tipo: transcript
proyecto: concurso-gaudi-nexus
fuente: archademy.ai (curso AI x Gaudi, area de participantes)
modulo: %s
titulo: %s
idioma: %s
fecha_creacion: %s
tags: [yt, transcript, curso-ai-gaudi, mux, gaudi-nexus, %s]
---

# %s — %s

> Transcripcion local del modulo del curso (faster-whisper en CPU, sin subtitulos en el origen).
> Origen: %s
> Duracion de la pista: %s

""" % (slug, titulo, lang, hoy, slug, titulo, lang, origen, txt.strip().split("\n")[-1][:8])
    with open(ruta_md, "w", encoding="utf-8") as f:
        f.write(cab + txt + "\n")
    return ruta_md, ruta_srt, ruta_txt


def main():
    ap = argparse.ArgumentParser(description="Transcribe en local una leccion del curso (sin subtitulos)")
    ap.add_argument("--modulo", required=True, help="slug del modulo, ej: round-table")
    ap.add_argument("--language", default="en", help="idioma del audio (default en)")
    ap.add_argument("--model", default="medium", help="modelo de whisper: tiny/base/small/medium/large-v3")
    ap.add_argument("--out", default=str(VAULT / "raw" / "yt" / "transcripts"))
    args = ap.parse_args()

    if not INDICE_CURSO.exists():
        print("ERROR: no existe el indice del curso:", INDICE_CURSO)
        sys.exit(1)
    with open(INDICE_CURSO, encoding="utf-8") as f:
        indice = json.load(f)

    pid = playback_id_del_modulo(indice, args.modulo)
    if not pid:
        print("ERROR: el modulo '%s' no tiene video en el indice." % args.modulo)
        sys.exit(1)
    titulo = next((m.get("titulo", args.modulo) for m in indice.get("modulos", [])
                   if m.get("modulo") == args.modulo), args.modulo)

    cdn = indice.get("cdn", CDN_BASE_FALLBACK)
    url_video = "%s/%s/play_720p.mp4" % (cdn, pid)
    print("Modulo: %s (%s)" % (args.modulo, titulo))
    print("Video:  %s" % url_video)

    ffmpeg = buscar_ffmpeg()
    if not ffmpeg:
        print("ERROR: ffmpeg no encontrado. Descargalo portable de")
        print("  https://github.com/BtbN/FFmpeg-Builds/releases -> ffmpeg-master-latest-win64-gpl.zip")
        print("  y poné ffmpeg.exe en P:\\00-repos\\ffmpeg\\bin\\")
        sys.exit(1)
    print("[ffmpeg] %s" % ffmpeg)

    ACTIVOS_VIDEOS.mkdir(parents=True, exist_ok=True)
    video = bajar_video(ACTIVOS_VIDEOS / ("mux-%s.mp4" % args.modulo), url_video)
    audio = extraer_audio(video, ffmpeg)
    txt, srt = transcribir(audio, args.model, args.language)

    os.makedirs(args.out, exist_ok=True)
    md, srt_f, txt_f = escribir_transcripcion(args.out, args.modulo, titulo, args.language, txt, srt, url_video)
    print("\n[out] md:  %s" % md)
    print("[out] srt: %s" % srt_f)
    print("[out] txt: %s" % txt_f)
    print("\nSIGUIENTE: volcarla a proyectos/concurso-gaudi-nexus/flujos/ y escribir el checklist del jurado.")


if __name__ == "__main__":
    main()
