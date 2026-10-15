"""Calculadora costo replica de un flujo n8n (ej: OS-Emilia) — v0.1.
Uso: P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/calculadora-costo-flujo-n8n.py [--ejemplo-emilia]
Todo valor por defecto es editable por flags; ver --help. Solo stdlib.
"""
import argparse
import json

POMODORO_H = 25 / 60  # 1 pomodoro = 0.42h

# Despiece firmado: (nombre, pomodoros, tipo_hora). Suma = 27 pomodoros.
DESPIECE = [
    ("Router Telegram", 3, "n8n-build"),
    ("Agenda Cal.com", 6, "n8n-build"),
    ("Cancel/Modif", 4, "n8n-build"),
    ("Fathom Core", 8, "n8n-build"),
    ("Agente/voz/memoria", 6, "prompt-eng"),
]

# Tarifa USD/h por tipo (defaults, Sol ajusta).
TARIFAS = {"arq": 15.0, "n8n-build": 12.0, "api": 12.0, "data": 10.0,
           "prompt-eng": 12.0, "qa": 10.0, "docs": 10.0,
           "devops-vps": 12.0, "seguridad": 15.0}


def mezcla_por_tipos(pomos, tipo_principal):
    """Reparte pomodoros: 70% tipo principal, 30% qa (redondeo a pomodoro)."""
    qa = max(1, round(pomos * 0.3))
    return {tipo_principal: pomos - qa, "qa": qa}


def costo_replica(tarifas):
    """Costo unico de reimplementar el flujo en otro cliente."""
    total_h, total_usd, det = 0.0, 0.0, []
    for nombre, pomos, tipo in DESPIECE:
        mezcla = mezcla_por_tipos(pomos, tipo)
        h = pomos * POMODORO_H
        usd = sum(p * POMODORO_H * tarifas[t] for t, p in mezcla.items())
        total_h += h
        total_usd += usd
        det.append({"flujo": nombre, "pomodoros": pomos,
                    "horas": round(h, 2), "usd": round(usd, 2),
                    "tipos": mezcla})
    return total_h, total_usd, det


def costo_tokens_mes(tok_in, tok_out, precio_in_1m, precio_out_1m, exec_mes):
    """Costo mensual LLM: tokens por ejecucion x ejecuciones."""
    return exec_mes * (tok_in * precio_in_1m + tok_out * precio_out_1m) / 1e6


def main():
    ap = argparse.ArgumentParser(description="Costo replica + operativo de flujo n8n")
    ap.add_argument("--ejemplo-emilia", action="store_true",
                    help="Corre con los valores del caso Emilia OS")
    ap.add_argument("--exec-mes", type=int, default=900,
                    help="Ejecuciones/mes (default 900 = 30/dia, exagerado)")
    ap.add_argument("--tok-in", type=int, default=2000)
    ap.add_argument("--tok-out", type=int, default=500)
    ap.add_argument("--precio-in-1m", type=float, default=0.10,
                    help="USD por 1M tokens input (default modelo barato)")
    ap.add_argument("--precio-out-1m", type=float, default=0.40)
    ap.add_argument("--vps-mes", type=float, default=15.0,
                    help="USD/mes VPS n8n prorrateado (a confirmar)")
    ap.add_argument("--mantenimiento-hs", type=float, default=2.0,
                    help="hs/mes seguridad + updates + analisis modelos")
    ap.add_argument("--tarifa-mantenimiento", type=float, default=12.0)
    ap.add_argument("--ahorro-hs-mes", type=float, default=12.0,
                    help="hs/mes liberadas medidas (O3)")
    ap.add_argument("--tarifa-hora-liberada", type=float, default=15.0,
                    help="USD/h valor hora arquitecta liberada")
    ap.add_argument("--cuota-mes", type=float, default=600.0,
                    help="Solo informativo: cuota programa I+D (incluye 60hs, no solo el flujo)")
    ap.add_argument("--inversion-referencia", type=float, default=1800.0,
                    help="Inversion trimestral contra la que se mide el retorno")
    a = ap.parse_args()

    h_rep, usd_rep, det = costo_replica(TARIFAS)
    usd_tok = costo_tokens_mes(a.tok_in, a.tok_out, a.precio_in_1m,
                               a.precio_out_1m, a.exec_mes)
    usd_mant = a.mantenimiento_hs * a.tarifa_mantenimiento
    operativo_mes = usd_tok + a.vps_mes + usd_mant
    valor_mes = a.ahorro_hs_mes * a.tarifa_hora_liberada
    retiro_12m = valor_mes * 12
    payback_replica = usd_rep / valor_mes if valor_mes else None
    reporte = {
        "replica_unica": {"horas": round(h_rep, 2), "usd": round(usd_rep, 2),
                          "detalle": det},
        "operativo_mensual": {"tokens_llm": round(usd_tok, 2),
                              "vps": a.vps_mes,
                              "mantenimiento": round(usd_mant, 2),
                              "total": round(operativo_mes, 2)},
        "valor_mensual_liberado": round(valor_mes, 2),
        "retorno_12m": {"valor_liberado": round(retiro_12m, 2),
                        "inversion_referencia": a.inversion_referencia,
                        "multiplo": round(retiro_12m / a.inversion_referencia, 2),
                        "payback_replica_meses": round(payback_replica, 1)},
    }
    print(json.dumps(reporte, indent=2, ensure_ascii=False))
    print(f"\nReplica: {h_rep:.2f}hs = USD {usd_rep:.2f} (una vez por cliente nuevo)")
    print(f"Operativo: USD {operativo_mes:.2f}/mes (tokens {usd_tok:.2f} + "
          f"VPS {a.vps_mes:.2f} + mant. {usd_mant:.2f})")
    print(f"Valor liberado: USD {valor_mes:.2f}/mes = {retiro_12m:.2f}/año "
          f"({retiro_12m / a.inversion_referencia:.2f}x la inversion de referencia)")
    print(f"Payback replica: {payback_replica:.1f} mes(es) de ahorro para pagar "
          f"la reimplementacion")


if __name__ == "__main__":
    main()
