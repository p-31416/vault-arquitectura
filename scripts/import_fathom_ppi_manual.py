"""Import manual Fathom Proyecto Pi -> raw/reuniones/ + Drive Reuniones-Internas.

Replica a mano lo que el Fathom Core hace solo para la cuenta Emilia:
misma plantilla ## Datos / ## Resumen / ## Action items / ## Transcripcion,
mismo nombre fecha_participantes_recid, misma carpeta Internas.

Uso:
  P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/import_fathom_ppi_manual.py <list-json>
Donde <list-json> es la respuesta de GET /external/v1/meetings guardada en disco.
Idempotente: si el .md ya existe en raw, lo salta (salvo --force).
"""
import json
import shutil
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
RAW = VAULT / "raw" / "reuniones"
DRIVE = Path(r"G:\Mi unidad\OS-Emilia\Reuniones-Internas")
STATE = RAW / ".import-state.json"


def build_md(item: dict) -> str:
    rid = item.get("recording_id")
    title = item.get("meeting_title") or item.get("title") or "Reunion"
    start = (item.get("recording_start_time") or "")[:10]
    url = item.get("share_url") or item.get("url") or ""
    tx = item.get("transcript") or []
    speakers = sorted({(t.get("speaker") or {}).get("display_name", "?") for t in tx})
    lines = [
        f"# {title}",
        "",
        "## Datos",
        "",
        f"- Fecha: {start}",
        f"- Recording ID: {rid}",
        f"- URL: {url}",
        f"- Participantes: {', '.join(speakers)}",
        "- Clasificacion: Internas",
        "- Origen: Fathom Proyecto Pi (import manual, cuenta Emilia sin estas reuniones)",
        "",
        "## Resumen",
        "",
        ((item.get("default_summary") or {}).get("markdown_formatted") or "").strip(),
        "",
        "## Action items",
        "",
    ]
    for a in item.get("action_items") or []:
        who = (a.get("assignee") or {}).get("name") or "sin asignar"
        lines.append(f"- [{a.get('recording_timestamp', '?')}] {a.get('description', '')} (responsable: {who})")
    lines += ["", "## Transcripcion", ""]
    for t in tx:
        who = (t.get("speaker") or {}).get("display_name", "?")
        lines.append(f"**[{t.get('timestamp', '?')}] {who}:** {t.get('text', '')}")
    return "\n".join(lines) + "\n"


def main() -> None:
    force = "--force" in sys.argv
    src = Path([a for a in sys.argv[1:] if not a.startswith("-")][0])
    data = json.loads(src.read_text(encoding="utf-8-sig"))
    state = json.loads(STATE.read_text(encoding="utf-8"))
    for item in data.get("items", []):
        rid = str(item.get("recording_id"))
        start = (item.get("recording_start_time") or "")[:10]
        name = f"{start}_emilia-proyectopi_{rid}.md"
        dest_raw = RAW / name
        if dest_raw.exists() and not force:
            print(f"salta (existe): {name}")
            continue
        dest_raw.write_text(build_md(item), encoding="utf-8")
        shutil.copy2(dest_raw, DRIVE / name)
        state[f"Reuniones-Internas/{name}"] = name
        print(f"ok: {name} ({len(item.get('transcript') or [])} turnos)")
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    print("state actualizado")


if __name__ == "__main__":
    main()
