---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, pm, pmbok, project-management]
---

# PM / Project Management

> Disciplina paraguas: alcance, cronograma, costo, calidad, riesgos, interesados. El vault usa PM liviano (Leantime) + LPS en obra; PMBOK como referencia, no como burocracia.

- [Definición](#definición)
- [Áreas mínimas para el estudio](#áreas-mínimas-para-el-estudio)
- [PMBOK vs Lean vs Agile (cuándo usar cada uno)](#pmbok-vs-lean-vs-agile-cuándo-usar-cada-uno)
- [PM → Leantime + vault](#pm--leantime--vault)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Definición

Project Management (PMI/PMBOK): aplicar conocimientos, habilidades y técnicas para cumplir requisitos del proyecto balanceando **alcance–tiempo–costo–calidad–riesgo**. En estudio chico argentino se reduce a 6 preguntas siempre respondidas: ¿qué entregamos? ¿cuándo? ¿a qué costo/horas? ¿con qué calidad (DoD)? ¿qué puede fallar? ¿quién decide?

## Áreas mínimas para el estudio

| Área PMBOK | Versión estudio (2–6 personas) | Dónde vive |
|------------|-------------------------------|------------|
| Alcance | Ficha proyecto + lista entregables por fase | `proyectos/<x>/index.md` + `entregables/` |
| Cronograma | Hitos + sprints semanales | Milestones + Sprints Leantime |
| Costos | Horas netas × tarifa + registro consumo IA | `financiero/` + `log.md` semanal |
| Calidad | Definition of Done por entregable (legal+técnico) | `wiki/estandares/` + checklist columna Kanban |
| Riesgos | Top-5 riesgos con dueño y plan B | Canvas Riesgos Leantime + spec del proyecto |
| Interesados | Mapa comitente/municipio/contratistas | `clientes/` + ficha proyecto |
| Comunicaciones | Rituales fijos (daily, demo, retro) | [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] §5 |

## PMBOK vs Lean vs Agile (cuándo usar cada uno)

| Enfoque | Gobierna | Momento |
|---------|----------|---------|
| **PM** | El **qué/cuándo/cuánto** contractual | Siempre de fondo (ficha, hitos, costos) |
| **Agile/Scrum** | El **ritmo** de diseño | Sprints 1–2 sem en estudio |
| **Kanban** | El **flujo** diario | Tablero siempre visible |
| **LPS** | Los **compromisos** de producción | Obra + legajo (promesas semanales, PPC) |
| **Kaizen/5S** | La **mejora** del sistema | Ritual semanal + orden permanente |

No compiten: **PM = mapa, Agile = paso, Kanban = tablero, LPS = palabra, Kaizen = motor.**

## PM → Leantime + vault

Leantime cubre el PM liviano sin ser PMI-ware: dashboards, Gantt por milestones, timesheets, reportes de estado, canvas (Lean, SWOT, riesgos), roles por proyecto. Operativa en [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]].

## Conceptos relacionados

- [[wiki/glosario/conceptos/kanban|kanban]]
- [[wiki/glosario/conceptos/agile-arquitectura|agile-arquitectura]]
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]
- [[wiki/glosario/conceptos/okr-goals|okr-goals]]

## Referencias

- PMI — PMBOK Guide & Standards: https://www.pmi.org/pmbok-guide-standards (verificado 2026-09-09 — 200)
- PMI — What is Project Management: https://www.pmi.org/about/learn-about-pmi/what-is-project-management (verificado 2026-09-09 — 200)
- Lean Construction Institute: https://www.leanconstruction.org/ (verificado 2026-09-09 — 200, delivery Lean como complemento a PM clásico)
