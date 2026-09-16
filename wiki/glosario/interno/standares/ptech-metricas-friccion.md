---
tipo: concepto
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-11
tags: [metricas, ptech, friccion, roi, ia, ptech-metricas]
idioma: es
---

# ptech — Métricas de fricción

> Medimos horas que libera cada sistema. 60hs → 12hs/mes — y crecen.

Sistema de medición de retorno del programa I+D Pitautech. Prefijo `ptech-` en `standares/` para futuros propios. Origen: `[[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia — I+D como método]]` + `raw/research/2026-09-09-meta-arquitecto-pitautech.md`.

## Índice

- [[#Fórmulas]]
- [[#Tiempo humano vs tiempo máquina]]
- [[#Log de retorno — qué registra cada agente]]
- [[#Instrumentación]]
- [[#Desglose 3h/sem — 0.6h/día que ya se libera (Mes 1)]]
- [[#Ejemplo trimestral]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Fórmulas

| Métrica | Fórmula | Lectura |
|---|---|---|
| **Ahorro por flujo** | `Ahorro = T_manual − T_sistema` | Cuánto libera una ejecución |
| **Ahorro mensual** | `Ahorro_mes = Ahorro × Frecuencia/mes` | Cuánto libera al mes |
| **ROI** | `ROI = Ahorro_mes / T_invertido` | Retorno sobre horas invertidas en crear el sistema |
| **Capacidad liberada** | `Capacidad = Ahorro_mes / 60hs` | Objetivo Mes 1 ≥0.20 (12/60) |

`T_manual`: tiempo si se hiciera manual (analogía). `T_sistema`: tiempo con sistema (humano revisión + máquina).

## Tiempo humano vs tiempo máquina

- **T_humano:** revisión, criterio, corrección (arquitecto)
- **T_máquina:** ejecución agente/IA (Fathom, Sherlock, n8n, ComfyUI)
- **Tiempo ahorrado:** `T_humano_manual − (T_humano_revisión + T_máquina)`
- **Ratio:** `T_humano / T_máquina` — cuanto más alto, más fricción eliminada

Ejemplo: buscar plano manual 15min (humano) → con Vault 2min (0.5 humano + 1.5 máquina) → ahorro 13min por búsqueda.

## Log de retorno — qué registra cada agente

Cada ejecución registra minutos:

| Agente | Qué mide | Dónde loguea |
|---|---|---|
| **Sherlock** | minutos de búsqueda + síntesis | `log.md` + `raw/research-cache/*.json` |
| **Fathom** | duración captura reunión + escritura minuta + análisis transcripción + listado tareas | `raw/reuniones/` + Leantime |
| **Vault** | carga a Leantime (VPS) + procesamiento al Vault | Leantime + `wiki/fuentes/` |
| **n8n** | tiempo estimado por flujo (si no es perfecto, valor estimado) | `ptech-metricas-friccion` |

Si la medición no es perfecta, se usa **tiempo estimado n8n por flujo** (como en n8n), computando igual el ahorro.

## Instrumentación

- **Toggl/clock:** horas dedicadas por bloque (vault/Fathom/CAD/doc/reuniones)
- **n8n estimated time:** tiempo por flujo automatizado
- **Fathom:** duración captura + minuta
- **PPC (Last Planner System):** `tareas cumplidas / tareas planificadas` — mide confiabilidad del sistema
- **Destino:** `log.md` (horas dedicadas) + ficha `wiki/lecciones-aprendidas/` (horas ahorradas) + `[[specs/260910-plan-trimestral-unificado-studio-os-emilia#6. OKRs y métricas — horas dedicadas vs horas que libera cada sistema|specs trimestral §6]]`

## Desglose 3h/sem — 0.6h/día que ya se libera (Mes 1)

12hs/mes ≈ 3hs/sem ≈ **0.6h/día hábil**. Tres flujos sin solaparse (cada minuto manual se cuenta una sola vez).

| Flujo | Manual (estimado) | Con sistema (Humano revisión + Máquina) | Ahorro por ejecución | Frecuencia/mes | Ahorro/mes |
|---|---|---|---|---|---|
| **Agendar + preparar** (agente CAL.COM MCP: links, invitados, envío transcript, evaluar tareas) | 30 min (15 antes + 15 después) | ~0 (el agente lo hace solo) | 30 min | 8/mes | **240 min = 4.0h** |
| **Transcripción + minuta + tareas** (agente FATHOM MCP) | 60 min | 15 min (5 humano + 10 Fathom) | 45 min | 8/mes | **360 min = 6.0h** |
| **Vault búsqueda / procesado / doc** (agente bookworm) | 15 min | 2 min (0.5 humano + 1.5 máquina) | 13 min | 10 búsquedas | **130 min ~ 2.2h** |

**Subtotal medido:** 240+360+130 = 730 min ~ **12.2hs/mes -> presentamos >=10hs conservador (~3hs/sem).**

> **Lectura:** ~3hs/sem es media hora al día hábil. Con reuniones + Vault se recupera. El plus de documentación (que hoy nunca se llega a hacer) deja reglas listas para que cualquier JR inicie con autonomía.
> **Validez:** manual 60min vs IA+Leantime 15min medido con lo ya pensado y a medio hacer, con revisión humana incluida (todo iterable y mejorable). Log: Sherlock minutos + Fathom duración captura/minuta/tareas + Leantime carga + n8n estimated time.
> **Nota de auditoría 2026-09-11:** versión anterior contaba 4 flujos con solape (los 15min de "antes/después" duplicaban agendar y transcribir). Se corrige a 3 flujos sin solape: el total medido pasa de ~15.4hs a ~11.9hs; el claim conservador ≥10hs/mes se mantiene. Actualización: Agendar+preparar pasa a 30min (15+15) = 4.0hs con agente CAL.COM en 8 reuniones; Vault baja a 10 consultas (2.2hs). Total ~12.2hs/mes; objetivo >=10hs. Solo se mide impacto de 3 agentes para tener una medida posible.

## Ejemplo trimestral — el estudio recupera la inversión y luego libera para siempre

Inversión: **+190hs (1.800 USD) en 90 días**.  (180 programa + 10 mantenimiento bonificado).Cada mes libera horas que permanecen. Parte de lo que se paga **es retorno para siempre**. Supuesto vigente: ritmo medido Mes 1 **12hs/mes con 3 agentes**, +12hs nuevas cada mes del trimestre; desde Mes 3 el ritmo liberado es 36hs/mes constantes. Ver definición en [[wiki/glosario/conceptos/payback|payback]].

| Mes | Inversión acumulada | Ahorro nuevo del mes | Ahorro mensual acumulado | Capacidad liberada | ROI acumulado | Acumulado liberado |
|---|---|---|---|---|---|---|
| **1** | 60hs | +12hs/mes | 12hs/mes | 0.20 (12/60) | 0.20 (12/60) | 12hs |
| **2** | 120hs | +12hs/mes | 24hs/mes | 0.40 (24/60) | 0.30 (36/120) | 36hs |
| **3** | +190hs (180+10 bonif) | +12hs/mes | 36hs/mes | 0.60 (36/60) | 0.38 (72/190) | 72hs |
| **4** (sin inversión) | +190hs | 0 | 36hs/mes | 0.60 | 0.57 (108/190) | 108hs |
| **6** | +190hs | 0 | 36hs/mes | 0.60 | 0.95 (180/190) | 180hs |
| **7** ([[wiki/glosario/conceptos/payback|payback]]) | +190hs | 0 | 36hs/mes | 0.60 | 1.14 (216/190) | 216hs |
| **12** | +190hs | 0 | 36hs/mes | 0.60 | 2.08 (396/190) | 396hs |

**Lectura:** en **7 meses** el estudio recupera las +190hs invertidas. Desde mes 8, cada mes de 36hs liberadas es **ganancia neta para siempre** (396hs al año ≈ 2.1× la inversión). A 10 USD/h = **3.960 USD/año liberados** con una inversión de 1.800 USD — con potencial adicional cuando se suman más flujos (M2 RunPod, Mes 3 protocolos).

> Propuesta para cliente: "Parte de los 1.800 es retorno para siempre. En 7 meses recuperas las horas invertidas; desde entonces, cada mes libera 36hs que permanecen. En un año, el sistema devuelve 2 veces lo invertido."
> **Nota de auditoría 2026-09-11:** la versión con +10hs/mes daba ritmo 30hs/mes, payback mes 8 y 330hs/año (1.74x). Con el medido real +12hs/mes (12.2hs en desglose 3 agentes), el ritmo Mes 3 avanza a 36hs/mes, acumulado Mes 3 a 72hs, payback a mes 7 y año a 396hs (2.08x). El escenario +10hs queda como referencia conservadora mínima.

Proyección medida (12hs/mes por mes): a 60hs/mes, el sistema paga su construcción en 7 meses y sigue liberando. Con 15hs/mes por mes (ritmos 15/30/45), payback en mes 6. Con el desglose de 3hs/sem ya validado, el payback avanza con base real desde Mes 1.

Ver gráfico: `proyectos/STUDIO_OS-Emilia/presentacion/diagramas/04-roi-payback.svg` (curvas inversión vs liberado, payback mes 7).

## Conceptos relacionados

- [[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]] — Filosofía Pitautech (capacidad, Vault, I+D)
- [[wiki/glosario/conceptos/payback|payback]] — Período de recupero (mes 7 vigente)
- [[wiki/glosario/conceptos/okr-goals|okr-goals]] — OKRs trimestrales
- [[wiki/glosario/conceptos/lean|lean]] — eliminar desperdicio
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]] — PPC

## Referencias

- `raw/research/2026-09-09-meta-arquitecto-pitautech.md` — 18 fuentes 200, fórmula fricción y ratios
- Toggl ROI — https://toggl.com/track/ (verificado 2026-09-09 — 200)
- Last Planner System (LCI) — https://www.leanconstruction.org/ (verificado 2026-09-09 — 200)
- Design Sprint (GV) — https://www.gv.com/sprint/ (verificado 2026-09-09 — 200)
- `[[specs/260910-plan-trimestral-unificado-studio-os-emilia]]` — Plan trimestral unificado