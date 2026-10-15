# Diagnóstico de disponibilidad Cal.com (SOLO LECTURA, no crea/modifica nada).
# Lee la key desde .env (CAL_COM_SOL_API_KEY) y consulta 3 endpoints v2:
#   1) event-types/7467793 -> scheduleId del evento
#   2) schedules/{id}      -> días/horas laborables (0=dom..6=sáb)
#   3) selected-calendars  -> calendarios conectados que SÍ bloquean disponibilidad
# Uso: P:\Anaconda\envs\comfyenv\python.exe scripts/diag_calcom_disp.py

import json
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
ENV = BASE / ".env"
API = "https://api.cal.com/v2"


def get_key() -> str:
    for line in ENV.read_text(encoding="utf-8").splitlines():
        for prefix in ("CAL_COM_SOL_API_KEY=", "CAL_COM_PPI_API_KEY="):
            if line.startswith(prefix):
                key = line.split("=", 1)[1].strip()
                if key:
                    return key
    raise SystemExit("CAL_COM_SOL_API_KEY vacía en .env")


def api_get(path: str, key: str, version: str = "2024-08-13"):
    req = urllib.request.Request(
        API + path,
        headers={"Authorization": "Bearer " + key, "cal-api-version": version},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            return res.status, json.load(res)
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode()[:500]
        except Exception:
            body = "<sin cuerpo>"
        return e.code, {"error": body}


def main() -> None:
    key = get_key()

    st, me = api_get("/me", key)
    print("== me ->", st)
    md = me.get("data", {}) if isinstance(me, dict) else {}
    print(json.dumps(
        {"email": md.get("email"), "username": md.get("username"),
         "id": md.get("id")}, indent=1, ensure_ascii=False))

    st, event = api_get("/event-types/7467793", key)
    print("== event-type 7467793 ->", st)
    ed = event.get("data", {}) if isinstance(event, dict) else {}
    print(json.dumps(
        {"slug": ed.get("slug"), "lengths": ed.get("lengths"),
         "length": ed.get("length"), "scheduleId": ed.get("scheduleId")},
        indent=1, ensure_ascii=False))

    sched_id = ed.get("scheduleId")
    if sched_id:
        st, sched = api_get(f"/schedules/{sched_id}", key)
        print("== schedule", sched_id, "->", st)
        sd = sched.get("data", {}) if isinstance(sched, dict) else {}
        print(json.dumps(sd.get("availability", sd), indent=1, ensure_ascii=False)[:2000])

    st, sels = api_get("/selected-calendars", key)
    print("== selected-calendars ->", st)
    print(json.dumps(sels, indent=1, ensure_ascii=False)[:2000])


if __name__ == "__main__":
    main()
