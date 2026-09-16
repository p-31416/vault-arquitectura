---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, okr, goals, metricas, leantime]
---

# OKR + Goals (Leantime)

> Objectives & Key Results (Doerr/Grove): objetivos inspiradores + 3–5 resultados clave medibles. En Leantime viven como **GOALS**; en el vault se revisan mensualmente junto a la retro grande.

- [Definición](#definición)
- [Anatomía de un buen OKR](#anatomía-de-un-buen-okr)
- [OKRs propuestos para el estudio](#okrs-propuestos-para-el-estudio)
- [Cadencia de revisión](#cadencia-de-revisión)
- [OKR → Goals de Leantime](#okr--goals-de-leantime)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Definición

OKR (Intel/Grove, popularizado por John Doerr en Google): **Objective** = qué quiero lograr (cualitativo, inspirador, con fecha); **Key Results** = cómo sé que llegué (3–5, cuantitativos, con meta y sourcing de dato). Regla: si no se puede medir semanalmente, no es KR — es deseo. Stretch goal sano ≈ 70% de cumplimiento; 100% siempre = objetivos tibios.

## Anatomía de un buen OKR

- **O:** verbo de impacto + plazo ("Al cerrar Mes 2, el vault ahorra 5 hs/sem de gestión").
- **KR:** número + baseline + target + fuente ("KR1: reuniones con minuta wiki en 24 hs pasan de 20% → 100% — fuente: `raw/reuniones/`").
- **Anti-patrones:** KR = tarea ("hacer 10 planos" es output, no outcome); demasiados (máx 5 por objetivo, 3 objetivos por trimestre); sin dueño; sin fecha.

## OKRs propuestos para el estudio

**O1 — Vault vivo (trimestre 1):**

| KR | Meta | Fuente |
|----|------|--------|
| KR1 reuniones transcriptas→wiki 24 hs | 100% | `raw/reuniones/` vs wiki |
| KR2 horas gestión liberadas/semana | ≥ 5 hs | timesheets Leantime |
| KR3 activos con ficha wiki | ≥ 8 + prompt-packs | `wiki/` |

**O2 — Producción predecible:**

| KR | Meta | Fuente |
|----|------|--------|
| KR1 PPC semanal promedio | ≥ 80% | sprint Leantime |
| KR2 retrabajo de planos (versiones >3 por causa interna) | −50% | log entregables |
| KR3 demos con comitente por mes | ≥ 2 | actas demo |

**O3 — Representación (casa en construcción):**

| KR | Meta | Fuente |
|----|------|--------|
| KR1 sistema representación documentado y aplicado | 1 proyecto real | `wiki/estandares/` |
| KR2 referentes curados con ficha | 20–30 | carpeta referentes |
| KR3 renders ControlNet validados (Canny/Depth) | ≥ 5 | `activos/.../renders/` |

## Cadencia de revisión

- **Semanal:** KR operativos (PPC, minutas) en la retro — 5 min, semáforo verde/amarillo/rojo.
- **Mensual:** los 3 objetivos completos, con decisión (seguir / corregir / matar).
- **Trimestral:** se reescriben O + KR (nunca se arrastran sin revisión).

## OKR → Goals de Leantime

Leantime es "goals-focused": módulo **Goals** con métricas trackeadas, y los To-Dos cuelgan de goals (cada tarea muestra a qué objetivo contribuye). Milestones agrupan tasks con fecha (Gantt); Goals miden outcome. Operativa + convención de nombres en [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] §3.

## Conceptos relacionados

- [[wiki/glosario/conceptos/pm-project-management|pm-project-management]]
- [[wiki/glosario/conceptos/retrospectivas|retrospectivas]]
- [[wiki/glosario/conceptos/kaizen|kaizen]]
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]

## Referencias

- Doerr, J. — *Measure What Matters* / WhatMatters.com (OKR playbook + ejemplos): https://www.whatmatters.com/ (verificado 2026-09-09 — 200)
- Atlassian — Guide to OKRs: https://www.atlassian.com/agile/project-management/okrs (verificado 2026-09-09 — 200, anatomía + anti-patrones)
- Leantime — Goal & metrics tracking (goals-focused PM): https://leantime.io/ (verificado 2026-09-09 — 200) y https://github.com/Leantime/leantime (verificado 2026-09-09 — feature list con Goals/Milestones/Sprints)
