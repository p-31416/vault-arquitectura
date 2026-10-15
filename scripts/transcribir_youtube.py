#!/usr/bin/env python3
"""
transcribir_youtube.py — Transcript de un video de YouTube a raw/yt/transcripts/.

Flujo liviano primero (subtitulos de YouTube: 1-2 requests, sin descargar nada);
si el video no trae subtitulos, descarga solo el audio y transcribe con
faster-whisper local (mismo motor que transcribir_ghl.py).

Uso:
  P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/transcribir_youtube.py RAMs89SS6cM
  P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/transcribir_youtube.py "https://www.youtube.com/watch?v=RAMs89SS6cM" --model small --lang en

Salida (todo UTF-8, crudo verbatim, nunca se edita a mano).
Archivos prefijados con fecha de ingesta ISO (orden cronologico nativo por texto):
  raw/yt/transcripts/YYYY-MM-DD_<video_id>.<lang>.md   (envoltorio visible en Obsidian)
  raw/yt/transcripts/YYYY-MM-DD_<video_id>.<lang>.srt  (subtitulos con timestamps)
  raw/yt/transcripts/YYYY-MM-DD_<video_id>.<lang>.txt  (texto con [HH:MM:SS])
  raw/yt/transcripts/YYYY-MM-DD_<video_id>.origen.json (fuente + fecha + modelo)

Reglas del vault: throttling liviano (sleep 5s entre videos si se procesa un lote),
max ~10 transcripciones Whisper por dia (el limite lo pone la CPU, no YouTube).
"""
import argparse
import json
import re
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
TRANSCRIPTS = VAULT / "raw" / "yt" / "transcripts"

ID_RE = re.compile(r"(?:v=|youtu\.be/|shorts/)?([A-Za-z0-9_-]{11})")


def video_id(arg: str) -> str:
    m = ID_RE.search(arg.strip())
    if not m:
        print(f"ERROR: no pude extraer video_id de: {arg}")
        sys.exit(1)
    return m.group(1)


def clean_sub_text(s: str) -> str:
    """Normaliza artefactos tipicos de subtitulos YT: NBSP, guion inseparable
    y apóstrofos mutilados a à (solo entre letras, para no tocar otros idiomas)."""
    s = s.replace("\xa0", " ").replace("\u2011", "-")
    s = re.sub(r"(\w)à(\w)", r"\1'\2", s)
    return re.sub(r" {2,}", " ", s)


def vtt_to_srt(vtt: str) -> str:
    """Conversion minima VTT -> SRT (renumera cues, cambia . por ,)."""
    cues, cur = [], []
    for ln in vtt.splitlines():
        s = ln.strip()
        if not s or s == "WEBVTT" or s.startswith("Kind:") or s.startswith("Language:"):
            continue
        if "-->" in s:
            if cur:
                cues.append(cur)
            cur = [s.replace(".", ",")]
        else:
            cur.append(re.sub(r"<[^>]+>", "", s))
    if cur:
        cues.append(cur)
    out = []
    for i, cue in enumerate(cues, 1):
        out.append(str(i))
        out.append(cue[0])
        out.append(" ".join(cue[1:]))
        out.append("")
    return "\n".join(out)


def srt_to_txt(srt: str) -> str:
    """Mismo formato txt que transcribir_ghl.py: [HH:MM:SS] texto."""
    txt_lines = []
    for block in srt.strip().split("\n\n"):
        parts = block.splitlines()
        if len(parts) >= 3:
            ts = parts[1].split(" --> ")[0].split(",")[0]  # HH:MM:SS
            txt_lines.append(f"[{ts}] {' '.join(parts[2:])}")
    return "\n".join(txt_lines)


def fetch_subtitles(vid: str, tmp: Path) -> tuple[str, str, str] | None:
    """Intenta bajar subtitulos (manuales primero, automaticos despues). Devuelve (srt, lang, fuente) o None."""
    try:
        import yt_dlp
    except ImportError:
        print("ERROR: yt-dlp no instalado.")
        sys.exit(1)
    for auto, fuente in ((False, "manual-sub"), (True, "auto-sub")):
        for lang in ("es", "en"):  # por idioma: un 429 en 'en' no descarta el 'es' ya ok
            opts = {
                "skip_download": True,
                "writesubtitles": True,
                "writeautomaticsub": auto,
                "subtitleslangs": [lang],
                "subtitlesformat": "srt/best",
                "outtmpl": str(tmp / f"{vid}.%(ext)s"),
                "quiet": True,
                "no_warnings": True,
            }
            with yt_dlp.YoutubeDL(opts) as ydl:
                try:
                    ydl.download([f"https://www.youtube.com/watch?v={vid}"])
                except Exception as e:
                    print(f"[subs] intento {fuente}/{lang} fallo: {str(e)[:150]}")
                    continue
            for ext in ("srt", "vtt"):
                f = tmp / f"{vid}.{lang}.{ext}"
                if f.exists():
                    blob = f.read_bytes()
                    raw = None
                    for enc in ("utf-8-sig", "utf-8", "cp1252"):  # yt-dlp a veces entrega latin-1
                        try:
                            raw = blob.decode(enc)
                            break
                        except UnicodeDecodeError:
                            continue
                    raw = (raw or blob.decode("utf-8", errors="replace")).replace("\ufeff", "")
                    srt = raw if ext == "srt" else vtt_to_srt(raw)
                    print(f"[subs] OK via {fuente} ({lang})")
                    return srt, lang, fuente
    return None


def whisper_transcribe(vid: str, tmp: Path, model: str, lang: str | None) -> tuple[str, str, str]:
    """Descarga solo audio y transcribe local. Devuelve (srt, lang, 'whisper')."""
    try:
        import yt_dlp
    except ImportError:
        print("ERROR: yt-dlp no instalado.")
        sys.exit(1)
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("ERROR: faster-whisper no instalado.")
        sys.exit(1)
    audio_path = tmp / f"{vid}.%(ext)s"
    opts = {"format": "bestaudio/best", "outtmpl": str(audio_path), "quiet": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([f"https://www.youtube.com/watch?v={vid}"])
    audios = [p for p in tmp.glob(f"{vid}.*") if p.suffix.lower() not in (".srt", ".vtt", ".json")]
    if not audios:
        print("ERROR: no se pudo descargar el audio.")
        sys.exit(1)
    print(f"[whisper] modelo={model} audio={audios[0].name} (CPU int8, puede tardar varios minutos)")
    whisper = WhisperModel(model, device="cpu", compute_type="int8")
    segments, info = whisper.transcribe(str(audios[0]), language=lang, vad_filter=True)
    lang = lang or info.language
    print(f"[whisper] idioma={info.language} prob={info.language_probability:.2f} duracion={info.duration:.1f}s")
    srt_lines = []
    for i, seg in enumerate(segments, 1):
        h, m, s = int(seg.start // 3600), int((seg.start % 3600) // 60), seg.start % 60
        he, me, se = int(seg.end // 3600), int((seg.end % 3600) // 60), seg.end % 60
        ts = f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")
        te = f"{he:02d}:{me:02d}:{se:06.3f}".replace(".", ",")
        srt_lines.append(f"{i}\n{ts} --> {te}\n{seg.text.strip()}\n")
    for p in audios:  # el mp3 temporal se borra; el crudo es el transcript
        p.unlink(missing_ok=True)
    return "\n".join(srt_lines), lang, "whisper"


def main():
    ap = argparse.ArgumentParser(description="YouTube -> raw/yt/transcripts/ (subs primero, whisper si no hay)")
    ap.add_argument("video", help="video_id (11 chars) o URL completa")
    ap.add_argument("--model", default="small", help="modelo whisper fallback (default small)")
    ap.add_argument("--lang", default=None, help="forzar idioma whisper (default autodetect)")
    args = ap.parse_args()

    vid = video_id(args.video)
    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    stem = f"{today}_{vid}"  # prefijo ISO: orden cronologico nativo por texto
    existentes = sorted(TRANSCRIPTS.glob(f"*{vid}.*.srt"))  # tolera con o sin prefijo
    if existentes:
        print(f"[cache] ya existe: {existentes[0].name} (borralo para re-generar)")
        return

    time.sleep(5)  # throttling liviano entre videos
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        got = fetch_subtitles(vid, tmp)
        if got is None:
            print("[subs] sin subtitulos -> fallback whisper local")
            srt, lang, fuente = whisper_transcribe(vid, tmp, args.model, args.lang)
        else:
            srt, lang, fuente = got

    srt = clean_sub_text(srt)
    txt = clean_sub_text(srt_to_txt(srt))
    (TRANSCRIPTS / f"{stem}.{lang}.srt").write_text(srt, encoding="utf-8")
    (TRANSCRIPTS / f"{stem}.{lang}.txt").write_text(txt, encoding="utf-8")
    (TRANSCRIPTS / f"{stem}.{lang}.md").write_text(f"""---
tipo: raw
video_id: {vid}
fecha_ingesta: {today}
url: https://www.youtube.com/watch?v={vid}
idioma: {lang}
fuente_origen: {fuente}
tags: [youtube, transcripcion, raw]
transcript_srt: raw/yt/transcripts/{stem}.{lang}.srt
transcript_txt: raw/yt/transcripts/{stem}.{lang}.txt
---

# RAW — YouTube {vid} ({today}, verbatim)

> Transcript verbatim vía {fuente}. Crudo append-only: no editar a mano.
> Ver ficha en `raw/contenidos/` cuando @contenidos la genere.

## Transcript (con timestamps)

{txt}
""", encoding="utf-8")
    (TRANSCRIPTS / f"{stem}.origen.json").write_text(
        json.dumps({"video_id": vid, "fuente": fuente, "idioma": lang,
                    "fecha": today, "modelo_whisper": args.model if fuente == "whisper" else None},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[out] raw/yt/transcripts/{stem}.{lang}.md + .srt + .txt + .origen.json")
    print("SIGUIENTE: @contenidos ficha este transcript (formato spec v3 §13).")


if __name__ == "__main__":
    main()
