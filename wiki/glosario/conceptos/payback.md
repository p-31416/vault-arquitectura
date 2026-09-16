---
tipo: concepto
fecha_creacion: 2026-09-11
ultima_actualizacion: 2026-09-11
tags: [glosario, concepto, payback, roi, metricas, ptech]
idioma: es
---

# Payback — período de recupero

> El payback mide en cuánto tiempo una inversión recupera su costo inicial mediante los ahorros que libera cada mes.

- [Definición](#definición)
- [Fórmula Pitautech](#fórmula-pitautech)
- [Cómo se lee en el programa Studio OS](#cómo-se-lee-en-el-programa-studio-os)
- [Ejemplo trimestral vigente](#ejemplo-trimestral-vigente)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Definición

**Payback** = mes en que el `acumulado liberado` iguala o supera la `inversión acumulada`. Desde ese mes, cada hora liberada avanza como ganancia neta permanente.

En finanzas corporativas equivale al *payback period*: `Costo de inversión / Flujo promedio` — aquí el flujo avanza como `Ahorro_mes` en horas.

## Fórmula Pitautech

| Métrica | Fórmula | Lectura |
|---|---|---|
| **Ahorro por flujo** | `T_manual − T_sistema` | Lo que libera una ejecución |
| **Ritmo mensual** | `suma Ahorro_mes de flujos activos` | Hs/mes que permanecen |
| **Acumulado liberado** | `suma de ritmos hasta el mes` | Total recuperado a la fecha |
| **Payback** | `primer mes con acumulado >= inversión` | Mes de recupero |
| **ROI acumulado** | `acumulado / inversión` | Veces recuperada la inversión |

## Cómo se lee en el programa Studio OS

Inversión trimestral **+190hs (1.800 USD)**. Ritmo medido Mes 1: **12hs/mes con 3 agentes** (agendar + transcripción + Vault). Cada mes del trimestre suma +12hs de sistemas nuevos. Ritmo desde Mes 3: **36hs/mes fijas**. Payback en **mes 7** con **216hs acumuladas (1.14x)**. Año: **396hs (2.08x ≈ 3.960 USD/año a 10 USD/h)**.

Detalle completo en [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-metricas-friccion]] y plan vigente en [[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral unificado]].

## Ejemplo trimestral vigente

| Mes | Ritmo | Acumulado | ROI |
|---|---|---|---|
| 1 | 12hs/mes | 12hs | 0.20 |
| 2 | 24hs/mes | 36hs | 0.30 |
| 3 | 36hs/mes | 72hs | 0.38 |
| 6 | 36hs/mes | 180hs | 0.95 |
| **7 (payback)** | 36hs/mes | **216hs** | **1.14** |
| 12 | 36hs/mes | 396hs | 2.08 |

Escenario conservador previo (+10hs/mes → ritmo 30hs/mes → payback mes 8, 330hs/año 1.74x) queda como referencia mínima en la ficha de métricas.

## Conceptos relacionados

- [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-metricas-friccion]]
- [[wiki/glosario/conceptos/okr-goals|okr-goals]]
- [[wiki/glosario/conceptos/lean|lean]]
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]

## Referencias

- Investopedia — Payback Period: Definition, Formula, and Calculation: https://www.investopedia.com/terms/p/paybackperiod.asp (verificado 2026-09-11 — 200)
- Detalle operativo: [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-metricas-friccion]] — desglose 12.2hs/mes Mes 1
- Plan vigente: [[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral unificado]] §6
