# import_drive_reuniones.py — copia .md nuevos de Drive Stream a raw/reuniones/
# Uso: python scripts/import_drive_reuniones.py [--dry-run]
# Lee G:\Mi unidad\OS-Emilia\Reuniones-{Internas,Clientes}\*.md (sincronizados
# por Drive Stream tras el Fathom Core de n8n) y los copia verbatim a
# raw/reuniones/ con la convención YYYY-MM-DD-<call_id>.md. Idempotente.
import json
import re
import shutil
import sys
from pathlib import Path

VAULT = Path(r"P:\00-repos\proyecto-pi\vault-arquitectura")
SRC_DIRS = [
    Path(r"G:\Mi unidad\OS-Emilia\Reuniones-Internas"),
    Path(r"G:\Mi unidad\OS-Emilia\Reuniones-Clientes"),
]
DST_DIR = VAULT / "raw" / "reuniones"
STATE_FILE = DST_DIR / ".import-state.json"

CALL_RE = re.compile(r"fathom\.video/calls/(\d+)")
DATE_FIELD_RE = re.compile(r"^- Fecha:\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE)
REC_FIELD_RE = re.compile(r"^- Recording ID:\s*(\d+)", re.MULTILINE)
DATE_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def dest_name_for(src: Path, text: str) -> str:
    m_call = CALL_RE.search(text)
    m_date = DATE_FIELD_RE.search(text)
    date = m_date.group(1) if m_date else None
    if not date:
        m_file = DATE_FILE_RE.match(src.name)
        date = m_file.group(1) if m_file else "sin-fecha"
    if m_call:
        return f"{date}-{m_call.group(1)}.md"
    m_rec = REC_FIELD_RE.search(text)
    if m_rec:
        return f"{date}-rec{m_rec.group(1)}.md"
    return f"{date}-{src.stem}.md"


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    state = load_state()
    imported, skipped, missing = [], [], []
    for src_dir in SRC_DIRS:
        if not src_dir.exists():
            missing.append(str(src_dir))
            continue
        for src in sorted(src_dir.glob("*.md")):
            key = f"{src_dir.name}/{src.name}"
            if key in state:
                skipped.append(key)
                continue
            text = src.read_text(encoding="utf-8", errors="replace")
            dest_name = dest_name_for(src, text)
            dest = DST_DIR / dest_name
            if dest.exists():
                # Ya existe con ese nombre: se registra y no se pisa (raw es append-only)
                state[key] = dest_name
                skipped.append(key + " (dest existe)")
                continue
            if not dry_run:
                shutil.copy2(src, dest)
                state[key] = dest_name
            imported.append(f"{key} -> {dest_name}")
    if not dry_run:
        save_state(state)
    print(f"importados: {len(imported)}")
    for line in imported:
        print(f"  + {line}")
    print(f"omitidos (ya estaban): {len(skipped)}")
    for line in skipped:
        print(f"  = {line}")
    if missing:
        print(f"origen no encontrado: {missing}")
    if dry_run:
        print("(dry-run: no se copió nada)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
