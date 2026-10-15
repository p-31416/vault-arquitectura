# Notas didácticas — `calculadora-costo-flujo-n8n.py` (línea a línea, NOTA ES)

> Runnable: `P:\Anaconda\envs\comfyenv\python.exe scripts/calculadora-costo-flujo-n8n.py --ejemplo-emilia`. Solo stdlib (`argparse`, `json`).

## Constantes

* `POMODORO_H = 25/60` — 1 pomodoro son 0.42h. Es la unidad que une plan ↔ Leantime (`planHours 0.42`).
* `DESPIECE` — los 27 pomodoros firmados (Router 3 + Agenda 6 + Cancel/Modif 4 + Fathom 8 + agente 6), cada uno con su tipo de hora principal.
* `TARIFAS` — USD/h por tipo. Defaults de Sol; se ajustan y el script recalcula.

## Funciones

* `mezcla_por_tipos` — 70% del flujo al tipo principal + 30% a `qa` (todo flujo real lleva prueba). Mínimo 1 pomodoro de qa.
* `costo_replica` — multiplica pomodoros × 0.42 × tarifa y suma. Devuelve horas, USD y detalle por flujo. Es el "cuadrito" de costo réplica por cliente nuevo.
* `costo_tokens_mes` — `exec × (in×precio_in + out×precio_out) / 1e6`. Con 900 exec/mes exageradas y modelo barato da centavos: esa es la demo de "ínfimo".
* `main` — lee flags, calcula réplica + operativo (tokens + VPS + mantenimiento) + valor liberado (ahorro × tarifa hora) + múltiplo a 12 meses contra `--inversion-referencia` (1800 trimestral) + payback de la réplica en meses de ahorro, e imprime JSON + 4 líneas resumen.

## Salida

* `replica_unica`: lo que cuesta reimplementar (una vez por cliente).
* `operativo_mensual`: lo que cuesta tenerlo corriendo (tokens + VPS + mantenimiento).
* `valor_mensual_liberado` y `retorno_12m.multiplo`: el argumento comercial (valor vs cuota).
