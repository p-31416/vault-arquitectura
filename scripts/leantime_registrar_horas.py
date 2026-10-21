"""Registra horas trabajadas en Leantime (timesheets) via JSON-RPC.

Que resuelve: Leantime no expone "time tracking" por el MCP (/mcp = 0 tools) ni
hay una tool de "registrar horas" en el flujo Fathom -> specs -> Leantime. La via
real es el servicio `Timesheets` de la API JSON-RPC.

Metodo usado (leido del codigo de Leantime, app/Domain/Timesheets/Services/Timesheets.php):
    logTime(int $ticketId, array $params)
      - $params['dateString']  (o 'date'+'time', o 'timestamp')  -> obligatorio
      - $params['hours']       -> obligatorio
      - $params['kind']        -> obligatorio (GENERAL, GENERAL_BILLABLE,
                                   GENERAL_NOT_BILLABLE, PROJECTMANAGEMENT,
                                   DEVELOPMENT, BUGFIXING_NOT_BILLABLE, TESTING)
      - $params['description'] -> opcional
      - $params['userId']      -> opcional; si el token no tiene permiso
                                   timesheets.manage, el server lo fuerza al
                                   usuario de la sesion (nosotros: Sol, userId 3)

El `ticketId` es la TARJETA (o milestone) contra la que se imputa la hora.
El `kind` es el tipo de hora: las 15 entradas previas del estudio usan "GENERAL"
(valor legacy, fuera del vocabulario actual de la UI), asi que se mantiene.

Uso:
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/leantime_registrar_horas.py --dry
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/leantime_registrar_horas.py
    P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/leantime_registrar_horas.py --verificar

Rollback:
    leantime.rpc.Timesheets.Timesheets.deleteTime(<id de la entrada>)
"""
import io
import json
import sys

sys.path.insert(0, r"P:\00-repos\proyecto-pi\vault-arquitectura\scripts")
from leantime_rpc import rpc  # noqa: E402  (el cliente JSON-RPC ya hecho del vault)

METODO = "leantime.rpc.Timesheets.Timesheets.logTime"

# --------------------------------------------------------------------------
# LAS HORAS A REGISTRAR (Decidido por Sol el 2026-10-20)
#
# Reparto: 1 h por area por dia + 1 h extra de reparto el lunes, de modo que
# cada tema queda en 3 h (lunes 2 h + martes 1 h).
#   cad      -> ticket 452  (proyecto 4) Estandares CAD DWT-layers-bloques-rotulos
#   fuentes  -> ticket 517  (proyecto 4) Sistema de procesamiento de libros
#   rhino    -> ticket 571  (proyecto 6) Flujo Rhino + ComfyUI con estilo propio
#   agentes  -> ticket 448  (proyecto 4) Fathom en raw-reuniones + ficha-sem Emilia
#               ticket 504  (proyecto 4) Clonar agente + subflujo de agenda (20/10)
#   reunion  -> ticket 533  (proyecto 4) Cita presencial miercoles 21/10 13:00
# --------------------------------------------------------------------------
KIND = "GENERAL"          # igual que las 15 entradas previas

# OJO con la fecha: por RPC hay que mandar SIETE HORAS MENOS de la hora que
# querés ver. Medido el 2026-10-20 en esta instancia (timezone UTC+7):
#     dateString "2026-10-19 12:00:00"  ->  se lee  2026-10-19 19:00:00  OK
#     dateString "2026-10-19 00:00:00"  ->  se lee  2026-10-19 07:00:00
#     dateString "2026-10-19 19:00:00"  ->  se lee  2026-10-20 02:00:00  (un dia despues)
# La UI manda la hora local y por eso las 15 entradas previas se leen a las 19:00.
FECHA_LUNES = "2026-10-19 12:00:00"    # se lee 2026-10-19 19:00:00
FECHA_MARTES = "2026-10-20 12:00:00"   # se lee 2026-10-20 19:00:00
FECHA_MIERCOLES = "2026-10-21 12:00:00"  # se lee 2026-10-21 19:00:00
EXTRA = "Extra lunes 19/10 - 1 h por tema"   # las 4 h de reparto del lunes

ENTRADAS = [
    # --- lunes 19/10 : 8 h ---
    {"ticketId": 452, "dateString": FECHA_LUNES, "hours": 1, "kind": KIND,
     "description": "CAD: estandares DWT-layers-bloques-rotulos (M3)"},
    {"ticketId": 452, "dateString": FECHA_LUNES, "hours": 1, "kind": KIND,
     "description": EXTRA},
    {"ticketId": 517, "dateString": FECHA_LUNES, "hours": 1, "kind": KIND,
     "description": "Fuentes: procesamiento de libros + pipeline Fathom"},
    {"ticketId": 517, "dateString": FECHA_LUNES, "hours": 1, "kind": KIND,
     "description": EXTRA},
    {"ticketId": 571, "dateString": FECHA_LUNES, "hours": 1, "kind": KIND,
     "description": "Rhino: flujo Rhino + ComfyUI con estilo propio"},
    {"ticketId": 571, "dateString": FECHA_LUNES, "hours": 1, "kind": KIND,
     "description": EXTRA},
    {"ticketId": 448, "dateString": FECHA_LUNES, "hours": 1, "kind": KIND,
     "description": "Fathom en raw-reuniones + ficha-sem Emilia"},
    {"ticketId": 448, "dateString": FECHA_LUNES, "hours": 1, "kind": KIND,
     "description": EXTRA},
    # --- martes 20/10 : 4 h ---
    {"ticketId": 452, "dateString": FECHA_MARTES, "hours": 1, "kind": KIND,
     "description": "CAD: estandares DWT-layers-bloques-rotulos (M3)"},
    {"ticketId": 517, "dateString": FECHA_MARTES, "hours": 1, "kind": KIND,
     "description": "Fuentes: procesamiento de libros"},
    {"ticketId": 571, "dateString": FECHA_MARTES, "hours": 1, "kind": KIND,
     "description": "Rhino: flujo Rhino + ComfyUI con estilo propio"},
    {"ticketId": 504, "dateString": FECHA_MARTES, "hours": 1, "kind": KIND,
     "description": "Clonar agente + subflujo de agenda con perfil Emilia"},
    # --- miercoles 21/10 : 3 h (reunion presencial con Emilia) ---
    {"ticketId": 533, "dateString": FECHA_MIERCOLES, "hours": 3, "kind": KIND,
     "description": "Reunion presencial con Emilia 13:00 - agenda de Emilia viva"},
]


def registrar(entrada):
    """Manda UNA entrada de horas. Devuelve (ok, mensaje).

    El RPC puede resolver los argumentos por nombre (ticketId + params) o por
    posicion ([ticketId, params]). Se prueba el nominal y, si el server lo
    rechaza, se cae al posicional.
    """
    ticket = entrada["ticketId"]
    cuerpo = {k: v for k, v in entrada.items() if k != "ticketId"}

    # 1) argumentos por nombre
    salida = rpc(METODO, {"ticketId": ticket, "params": cuerpo})
    if "result" in salida:
        return True, "nominal"

    # 2) argumentos por posicion
    salida2 = rpc(METODO, [ticket, cuerpo])
    if "result" in salida2:
        return True, "posicional"

    return False, json.dumps(salida2.get("error", salida), ensure_ascii=False)[:300]


def verificar():
    """Relee las entradas de octubre y muestra las de las tarjetas tocadas."""
    tickets = {e["ticketId"] for e in ENTRADAS}
    salida = rpc("leantime.rpc.Timesheets.Timesheets.getAll",
                 {"dateFrom": "2026-10-01", "dateTo": "2026-10-31"})
    filas = salida.get("result") or []
    print("id  | fecha              | hs | ticket | proyecto | descripcion")
    for f in filas:
        if f.get("ticketId") in tickets and str(f.get("workDate", "")) >= "2026-10-19":
            print("{:<3} | {:<18} | {:<3} | {:<6} | {:<8} | {}".format(
                f.get("id"), f.get("workDate"), f.get("hours"), f.get("ticketId"),
                f.get("projectId"), str(f.get("description"))[:60]))
    total = sum(float(f.get("hours") or 0) for f in filas
                if f.get("ticketId") in tickets and str(f.get("workDate", "")) >= "2026-10-19")
    print("total registrado (19/10 a 31/10) sobre esas tarjetas: {} h".format(total))


if __name__ == "__main__":
    dry = "--dry" in sys.argv

    # --borrar 36,38,40  -> borra entradas de horas por id (rollback)
    if "--borrar" in sys.argv:
        ids = sys.argv[sys.argv.index("--borrar") + 1].split(",")
        for i in ids:
            salida = rpc("leantime.rpc.Timesheets.Timesheets.deleteTime", {"id": int(i.strip())})
            print("borrada {} -> {}".format(i, "OK" if "result" in salida else salida))
        sys.exit(0)

    if "--verificar" in sys.argv:
        verificar()
        sys.exit(0)

    total = sum(float(e["hours"]) for e in ENTRADAS)
    print("entradas: {} | horas: {}".format(len(ENTRADAS), total))
    if dry:
        for e in ENTRADAS:
            print("  [dry] ticket {ticketId} | {dateString} | {hours} h | {description}".format(**e))
        sys.exit(0)

    for i, e in enumerate(ENTRADAS, 1):
        ok, msg = registrar(e)
        print("[{}/{}] ticket {} {}h {} -> {}".format(
            i, len(ENTRADAS), e["ticketId"], e["hours"], e["dateString"][:10],
            "OK (" + msg + ")" if ok else "FALLO " + msg))
        if not ok:
            print("  (se corta: no seguir cargando a ciegas)")
            break
    print("--- verificacion ---")
    verificar()
