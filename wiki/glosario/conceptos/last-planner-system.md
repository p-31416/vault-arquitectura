---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, last-planner, lean-construction, ppc, obra]
---

# Last Planner System (LPS)

> Sistema de planificación por compromisos de Ballard & Howell (años 90): produce flujo predecible y aprendizaje rápido. Es **el método de obra** del vault; Agile/Kanban gobiernan el estudio, LPS gobierna la obra y el legajo.

- [Definición](#definición)
- [Las 5 conversaciones](#las-5-conversaciones)
- [Los 8 elementos clave](#los-8-elementos-clave)
- [PPC y análisis de incumplidos](#ppc-y-análisis-de-incumplidos)
- [LPS en diseño](#lps-en-diseño)
- [LPS → Leantime + vault](#lps--leantime--vault)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Definición

LPS genera **workflow predecible + aprendizaje rápido** mediante conversación, coordinación y **promesas confiables** (no cronogramas impuestos). Principio: solo se promete lo que está **libre de restricciones**. Diseñado por Glenn Ballard y Greg Howell; base del Lean Project Delivery.

## Las 5 conversaciones

| Nivel | Pregunta | Horizonte | En obra | En estudio |
|-------|----------|-----------|---------|------------|
| 1 DEBE | ¿Qué **debe** hacerse? | Hitos + pull planning de fase | Master schedule, hitos municipales | Fases vault (concurso→entrega) |
| 2 PUEDE | ¿Qué **puede** hacerse? | Lookahead 6–8 sem, liberar restricciones | 8 flujos (materiales, mano obra, info…) | Faltan dwg base, decisión comitente… |
| 3 HARÁ | ¿Qué **haré**? | Plan semanal, promesas | "Termino losa nivel 3 el jueves" | "Entrego PB+2 cortes el viernes" |
| 4 HIZO | ¿Qué **se hizo**? | Daily huddles, seguimiento | (/) hecho, (X) hecho-verificado | Idem en daily 15 min |
| 5 APRENDIÓ | ¿Qué **aprendemos**? | Semanal: 5 porqués, plus/delta | Taller causa raíz | [[wiki/glosario/conceptos/retrospectivas|retrospectivas]] |

Analogía entrenadores Fauchier/Umstot: niveles = altura del avión (30.000 ft hitos → suelo daily).

## Los 8 elementos clave

1. **Milestone planning** — hitos incrementales dentro del master (Should).
2. **Pull planning** — planificar hacia atrás desde el hito, especificando handoffs y Conditions of Satisfaction (Should).
3. **Make-ready** — remover restricciones antes de prometer (Can).
4. **Weekly Work Planning** — promesas semanales de personas concretas (Will).
5. **Constraint management** — log de restricciones con responsable + Last Responsible Moment (Will).
6. **Daily huddles** — renovar compromiso diario (Did).
7. **Percent Plan Complete (PPC)** — % promesas cumplidas, medido en equipo (Did).
8. **Learning** — 5 porqués, Pareto de causas, talleres (Learn).

**Reglas de la promesa confiable:** estudiar factibilidad antes de prometer · entender condiciones de satisfacción · plazo realista (calidad+seguridad) · capacidad asignada · sin conflictos ocultos · aceptar responsabilidad del fallo.

## PPC y análisis de incumplidos

`PPC = tareas completadas / tareas prometidas × 100`. Se calcula diario, tendencia semanal con Pareto. **Regla Deming: ~94% de los fallos son del sistema, no de la persona** — se pregunta ¿Por qué? nunca ¿Quién?

Categorías típicas de incumplimiento: mala planificación · trabajo previo · diseño · inspección fallida · falta materiales/equipos/mano de obra/información · aprobaciones · contratos · clima · olvidos · condiciones imprevistas · CoS poco clara.

## LPS en diseño

En fase diseño el lookahead se reemplaza por **Design Cycle Planning** (ciclos de iteración). Las otras 4 conversaciones quedan igual. Ideal para DD/legajo del estudio.

## LPS → Leantime + vault

- Hitos LPS = **Milestones** Leantime (con fecha, visibles en Gantt).
- Plan semanal = **Sprint** Leantime de 1 semana con To-Dos = promesas.
- Restricciones = tasks etiquetadas `bloqueado` + subtask "liberar restricción X (responsable, fecha)".
- PPC = métrica semanal → alimenta [[wiki/glosario/conceptos/okr-goals|okr-goals]] (KR "PPC ≥ 80%") y [[wiki/glosario/conceptos/kaizen|kaizen]] semanal.
- Operativa completa en [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] §4.

## Conceptos relacionados

- [[wiki/glosario/conceptos/lean|lean]]
- [[wiki/glosario/conceptos/kanban|kanban]]
- [[wiki/glosario/conceptos/kaizen|kaizen]]
- [[wiki/glosario/conceptos/retrospectivas|retrospectivas]]

## Referencias

- Lean Construction Institute — Last Planner System: https://leanconstruction.org/lean-topics/last-planner-system/ (verificado 2026-09-09 — 5 conversaciones + 8 elementos)
- LCI — Last Planner for Design: https://leanconstruction.org/lean-topics/last-planner-system-for-design/ (verificado 2026-09-09 — Design Cycle Planning, PPC)
- LCI — Intro to LPS (PDF curso): https://leanconstruction.org/wp-content/uploads/2023/05/LCI-Introduction-to-the-Last-Planner-System.pdf (verificado 2026-09-09 — 200)
- Lean Construction Blog — 5 niveles Should/Can/Will/Did/Learn (Ballard & Howell): https://leanconstructionblog.com/5-Levels-of-the-Last-Planner-System-Should-Can-Will-Did-and-Learn.html (verificado 2026-09-09 — 200) + versión español: https://leanconstructionblog.com/espanol/Los-05-niveles-del-Sistema-Last-Planner-DEBO-PUEDO-HARE-HICE-APRENDI.html (verificado 2026-09-09 — 200)
