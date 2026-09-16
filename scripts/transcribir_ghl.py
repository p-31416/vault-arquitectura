#!/usr/bin/env python3
"""
transcribir_ghl.py — Pipeline 100% libre (sin licencia) para GHL Academia → vault

Flujo: OBS mp4/mkv → ffmpeg extrae audio → faster-whisper transcribe → wiki/raw/*.md

Uso:
  P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/videos/ghl-2026-09-09-mi-captura.mkv"
  P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/videos/ghl-2026-09-09-mi-captura.mkv" --model medium --language es

Requisitos libres (una vez):
  1. ffmpeg portable (sin instalar): descargar de https://github.com/BtbN/FFmpeg-Builds/releases → extraer bin/ffmpeg.exe → poner en P:\00-repos\ffmpeg\bin\ o en PATH
  2. pip install faster-whisper

Todo MIT/Apache 2.0 — sin licencia paga.
"""
import argparse
import subprocess
import sys
from pathlib import Path
from datetime import date

VAULT = Path(__file__).resolve().parent.parent
FFMPEG_CANDIDATES = [
    VAULT / "ffmpeg" / "bin" / "ffmpeg.exe",
    Path(r"P:\00-repos\ffmpeg\bin\ffmpeg.exe"),
    Path("ffmpeg"),  # PATH
    Path("ffmpeg.exe"),
]

def find_ffmpeg() -> Path | None:
    for p in FFMPEG_CANDIDATES:
        try:
            # PATH candidates need shell lookup
            if p.name in ("ffmpeg", "ffmpeg.exe") and len(p.parts) == 1:
                r = subprocess.run(["where", p.name], capture_output=True, text=True, shell=True)
                if r.returncode == 0 and r.stdout.strip():
                    return Path(r.stdout.strip().splitlines()[0])
                continue
            if p.exists():
                return p
        except Exception:
            continue
    return None

def extract_audio(video: Path, ffmpeg: Path) -> Path:
    audio = video.with_suffix(".mp3")
    # si ya existe y es más nuevo que el video, reutilizar
    if audio.exists() and audio.stat().st_mtime > video.stat().st_mtime:
        print(f"[audio] reutilizando {audio}")
        return audio
    print(f"[audio] extrayendo con ffmpeg: {video.name} → {audio.name}")
    cmd = [str(ffmpeg), "-y", "-i", str(video), "-vn", "-acodec", "libmp3lame", "-q:a", "2", str(audio)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        # fallback sin re-encode si libmp3lame no está
        print(f"[audio] re-encode falló, probando copy: {r.stderr[:300]}")
        cmd2 = [str(ffmpeg), "-y", "-i", str(video), "-vn", "-acodec", "mp3", str(audio)]
        r2 = subprocess.run(cmd2, capture_output=True, text=True)
        if r2.returncode != 0:
            print(r.stderr)
            print(r2.stderr)
            sys.exit(1)
    return audio

def transcribe(audio: Path, model: str, language: str) -> tuple[str, str]:
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("ERROR: faster-whisper no instalado. Instalá con:")
        print("  P:\\Anaconda\\envs\\comfyenv\\python.exe -m pip install faster-whisper")
        sys.exit(1)

    print(f"[whisper] modelo={model} idioma={language} audio={audio.name} (corre en CPU, puede tardar 2-5 min para 30 min)")
    # CPU + int8 = liviano para tu máquina. Si ves errores, cambiá compute_type a "int8" o "float32"
    whisper = WhisperModel(model, device="cpu", compute_type="int8")
    segments, info = whisper.transcribe(str(audio), language=language, vad_filter=True)
    print(f"[whisper] detectado: idioma={info.language} prob={info.language_probability:.2f} duracion={info.duration:.1f}s")

    srt_lines = []
    txt_lines = []
    for i, seg in enumerate(segments, 1):
        h, m, s = int(seg.start // 3600), int((seg.start % 3600) // 60), seg.start % 60
        he, me, se = int(seg.end // 3600), int((seg.end % 3600) // 60), seg.end % 60
        ts = f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")
        te = f"{he:02d}:{me:02d}:{se:06.3f}".replace(".", ",")
        text = seg.text.strip()
        srt_lines.append(f"{i}\n{ts} --> {te}\n{text}\n")
        txt_lines.append(f"[{h:02d}:{m:02d}:{int(s):02d}] {text}")

    txt = "\n".join(txt_lines)
    srt = "\n".join(srt_lines)
    return txt, srt

def write_raw(video: Path, audio: Path, txt: str, srt: str):
    raw_dir = VAULT / "wiki" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    stem = video.stem  # sin extensión
    today = date.today().isoformat()
    raw_md = raw_dir / f"{today}-ghl-{stem}.md"
    srt_path = audio.with_suffix(".srt")
    txt_path = audio.with_suffix(".txt")

    txt_path.write_text(txt, encoding="utf-8")
    srt_path.write_text(srt, encoding="utf-8")
    print(f"[out] txt: {txt_path}")
    print(f"[out] srt: {srt_path}")

    raw_content = f"""---
tipo: raw
fecha_creacion: {today}
ultima_actualizacion: {today}
tags: [ghl, transcripcion, raw, 6-etapas]
fuente_binaria: activos/videos/{video.name}
fuente_audio: activos/videos/{audio.name}
idioma: es
---

# RAW — GHL {stem} (verbatim)

> Fuente: academia GHL, captura OBS local. Uso interno Pitau Tech, no redistribuir.
> Binario: `activos/videos/{video.name}` → audio `activos/videos/{audio.name}`
> Transcript generado con faster-whisper (CPU, modelo medium, libre). Revisar nombres propios y anglicismos antes de procesar.

## Transcript (con timestamps)

{txt}

---

## Notas captura

- Captura: OBS Studio (libre) + audio sistema
- Fecha: {today}
- Próximo paso: procesar a `wiki/estudio/metodologia-ciclo-6-etapas.md` + `wiki/estudio/servicios-pitau-tech-arquitectura.md` + 6 entradas `wiki/software/glosario/gohighlevel/` + `proyectos/STUDIO_OS-Emilia/documentacion/07-propuesta-diagnostico-emilia-6-etapas.md`
- Ver plan: [[proyectos/STUDIO_OS-Emilia/documentacion/06-plan-ingest-ghl-6-etapas]]
"""
    raw_md.write_text(raw_content, encoding="utf-8")
    print(f"[out] raw: {raw_md}")
    print("\n=== SIGUIENTE PASO (sin licencia) ===")
    print("Pegame el contenido de wiki/raw/*.md o del .txt y ejecuto el ingest al vault (metodología + glosario + servicios + propuesta Emilia).")
    print("O si querés automatizar el resumen local sin API, instalá Ollama (https://ollama.com) y corre: ollama run qwen2.5:7b")

def main():
    ap = argparse.ArgumentParser(description="GHL → vault (100% libre)")
    ap.add_argument("video", help="ruta al mp4/mkv capturado con OBS (ej: activos/videos/ghl-2026-09-09-captura.mkv)")
    ap.add_argument("--model", default="medium", help="tiny/base/small/medium/large-v3 (default medium)")
    ap.add_argument("--language", default="es", help="idioma (default es)")
    args = ap.parse_args()

    video = (VAULT / args.video).resolve() if not Path(args.video).is_absolute() else Path(args.video)
    if not video.exists():
        print(f"ERROR: no existe {video}")
        sys.exit(1)

    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        print("ERROR: ffmpeg no encontrado. Descargá portable:")
        print("  https://github.com/BtbN/FFmpeg-Builds/releases → ffmpeg-master-latest-win64-gpl.zip → extraer bin/ffmpeg.exe a P:\\00-repos\\ffmpeg\\bin\\ffmpeg.exe")
        print("  (no requiere instalador ni licencia)")
        sys.exit(1)
    print(f"[ffmpeg] {ffmpeg}")

    audio = extract_audio(video, ffmpeg)
    txt, srt = transcribe(audio, args.model, args.language)
    write_raw(video, audio, txt, srt)

if __name__ == "__main__":
    main()
