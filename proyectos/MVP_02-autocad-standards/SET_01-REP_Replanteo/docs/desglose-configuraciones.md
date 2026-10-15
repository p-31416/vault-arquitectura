---
tipo: metodologia
mvp: 02
set: SET_01-REP
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [mvp_02, SET_01, desglose, horas, ahorro, roi, pomodoros]
base_medicion: proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/REP-ARAOZ-capas-bloques
estado: v0.1
---

# Desglose de configuraciones SET_01 — ítems, horas y ahorro

> Todo ítem medido en `REP-ARAOZ.dwg` (ver doc madre). Costos de creación = estimación con supuestos explícitos, a validar en obra.

## 1. Desglose itemizado (87 + layout)

| Familia | Ítems | Detalle |
|---|---|---|
| Capas propias | 29 | §2.1–§2.4 del spec (replanteo, muros, carpinterías, base, paper) |
| Capas xref | 20 | `ARQ-ARAOZ\|*` (vienen con la referencia) |
| Bloques nombrados | 13 | 2 dinámicos + 5 tags/símbolos + corte + tabla + carátula + 4 puntas de cota |
| Estilos de cota | 3 | `COTAS-ARQ-50`, `REPLANTEO 150`, `Standard` |
| Estilos de texto | 9 | `cotas-50`, `COTAS`, `style2`, `Standard`, `MBA25`, `ROMANS`, `ROT` + 2 residuales |
| Tipos de línea | 12 | Continuous, DASHDOT, DASHDOTX2, DASHED + xref |
| Layout | 1 | `REP-PTipo-A1` + viewport 1:50 + escala custom |

## 2. Horas invertidas (reloj del estudio)

- Construcción manual del sistema: **10 h reloj** en pomodoros de 25' (≈24 pomodoros).
- Sesión de hoy (medición + docs + v2.2): **4 h mínimo**.
- **Total: 14 h**.

## 3. Ahorro por ítem creado (estimación)

Supuestos: costo manual incluye decisión + creación + prueba de plot. Reutilizar = abrir DWT e insertar.

| Ítem | Costo manual unitario | Cantidad | Costo total manual | Costo reutilizando | Ahorro por plano |
|---|---|---|---|---|---|
| Capa (nombre+color+tipo+estado) | 2' | 29 | 58' | ~0 (viene en DWT) | ~1 h |
| Estilo de texto | 5' | 9 | 45' | ~0 | ~45' |
| Estilo de cota (variables+flechas+prueba) | 20' | 3 | 60' | ~0 | ~1 h |
| Bloque tag/símbolo | 30' | 4 | 2 h | insertar 1' c/u | ~2 h |
| Bloque dinámico c/wipeout+atributos | 2 h | 2 | 4 h | insertar+estirar 2' c/u ×42 | ~10 h |
| Tabla + carátula c/FIELD | 1 h | 1 | 1 h | reutilizar | ~1 h |
| Layout + viewport + escala custom | 20' | 1 | 20' | ~0 | ~20' |
| CTB + DWT/DWS setup | 1 h | 1 | 1 h | ~0 | ~1 h |
| Cómputos `EXTRACDAT` vs manual | 2 h | 1 | 2 h | 10' | ~2 h |

- Suma del costo manual estimado: **~11,4 h** — cruza con las 10 h reloj medidas (el resto fue decisión y normalización). El modelo cierra.
- **Ahorro por plano futuro: ~12–15 h** (setup + inserciones + cómputos).
- **Payback: las 14 h invertidas se recuperan en el primer plano completo** que use el sistema.

## 4. Seguimiento

- Registrar por ítem en cada sesión (pomodoros por bloque/capa/estilo) para reemplazar estimaciones por medición real.
- Próxima medición: tiempo de dibujar un vano+puerta+tag con sistema vs sin sistema, en obra.
