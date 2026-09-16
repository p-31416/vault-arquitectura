---
tipo: playbook
codigo: pbk-pm_vault
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [pbook, pm, leantime, kanban, sprints, okr, vault, operacion]
---

# pbk-pm_vault — Cómo usamos PM + Lean + Agile en el vault (con Leantime)

> Playbook operativo canónico: qué va en Leantime, qué va en el vault (git), cómo se hablan, rituales semanales y convenciones de nombres. Si hay duda entre este pbook y una ficha conceptual, **manda este pbook**.

- [Principio: Leantime gestiona, el vault recuerda](#principio-leantime-gestiona-el-vault-recuerda)
- [Mapa de objetos Leantime ↔ vault](#mapa-de-objetos-leantime--vault)
- [Goals (OKR), Milestones y Sprints](#goals-okr-milestones-y-sprints)
- [Kanban + LPS en el día a día](#kanban--lps-en-el-día-a-día)
- [Rituales semanales](#rituales-semanales)
- [Convenciones de nombres y etiquetas](#convenciones-de-nombres-y-etiquetas)
- [MCP Leantime + agente del vault](#mcp-leantime--agente-del-vault)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Principio: Leantime gestiona, el vault recuerda

| Leantime (VPS, vivo) | Vault git (memoria) |
|---|---|
| Tasks + subtasks (ilimitadas) + dependencias | Ficha proyecto `proyectos/<x>/index.md` con link al proyecto Leantime |
| Sprints (tiempo) + retrospectivas | Nota `raw/sessions/YYYY-MM-DD-retro-sprint-N.md` + 3 victorias a `log.md` |
| Milestones (metas con fecha, Gantt) | Hitos en spec + `entregables/` |
| GOALS = OKRs con métricas | OKRs del trimestre en spec + revisión mensual |
| Timesheets (horas) | `financiero/` + registro consumo IA en `log.md` |
| Idea Board, Canvas (Lean/SWOT/riesgos) | Decisiones promovidas a `wiki/` con `[[wikilinks]]` |

Regla: **nada vive solo en Leantime** — toda decisión/métrica que importe termina en el vault en 24 hs (flujo raw → wiki del cerebro digital).

## Mapa de objetos Leantime ↔ vault

```
GOAL trimestral (ej. "Vault vivo")
 └─ Milestone (ej. "Mes 1: estructura + estándares")
     └─ Sprint semanal (ej. "S1 Vault encendido")
         └─ Task = entregable/promesa (ej. "Fathom Meet→vault")
             ├─ Subtask = paso verificable (ej. "conectar MCP Fathom")
             ├─ Subtask = DoD (ej. "guía en wiki + demo a Emilia")
             └─ Bloqueo = restricción LPS (ej. "falta pass VPS")
```

- **Task** = una promesa LPS (dueño + fecha + Conditions of Satisfaction en la descripción).
- **Subtasks** = tantas como hagan falta; la task se cierra solo con todas hechas (= "hecho-verificado X", no solo "/").
- **Dependencias** = handoffs del pull planning (B depende de A).
- **Proyecto Leantime** = 1 por proyecto vault real + 1 proyecto "ESTUDIO-OPS" (mejora interna, Kaizen, 5S, academia).

## Goals (OKR), Milestones y Sprints

**Goals:** crear 3 por trimestre (O1 Vault vivo, O2 Producción predecible, O3 Representación — ver [[wiki/glosario/conceptos/okr-goals|okr-goals]]). Cada Goal lleva sus KR como métricas; cada task relevante se vincula a su Goal (así Leantime muestra "a qué objetivo contribuye").

**Milestones:** 1 por mes/proyecto con fecha dura (ej. "Clase cierre Mes 1 — 2026-10-02"). Agrupan tasks; se ven en Gantt/Program Plan. Convención: `[PROYECTO] Mes N — resultado`.

**Sprints:** 1 semana, lunes→viernes, mismo nombre siempre: `S<N> <foco> (dd/mm–dd/mm)`. Capacidad = WIP Kanban (no se mete más de lo que el equipo puede terminar). Cierre = retro 30 min (módulo Retrospectives) + nota al vault.

## Kanban + LPS en el día a día

Columnas del tablero por proyecto (estados Leantime mapeados):

`Backlog (debe) → Make-ready (puede, con restricción) → Sprint actual (hará) → En curso WIP-limitado → Revisión → Bloqueado ⚠️ → Hecho ✓`

- WIP: En curso máx 2 por persona; Revisión máx 3 (Sol/Emilia).
- Todo lo que entra a "Sprint actual" pasó make-ready: **sin restricciones abiertas** (o con plan de liberación + dueño + fecha).
- Daily 15 min: tablero a la vista, cada uno mueve lo suyo + declara 1 restricción nueva si apareció.
- PPC semanal = hechas/prometidas; KR "PPC ≥ 80%"; incumplidas → causa sistema (lista LPS) → 5 porqués en retro.

## Rituales semanales

| Ritual | Cuándo | Dónde | Salida vault |
|---|---|---|---|
| Planning sprint | Lun 9:00, 45 min | Leantime sprint nuevo | Sprint creado + tasks asignadas |
| Daily | Lun–Vie 9:00, 15 min | Tablero | Nada (solo mover) |
| Demo comitente | Vie 12:00 quincenal | Meet + Fathom | Transcript → `raw/reuniones/` → minuta wiki 24 hs |
| Retro + Victoria/Mejora | Vie 16:30, 30 min | Leantime retro | `raw/sessions/*-retro-*.md` + 3 victorias `log.md` + 1 task kaizen |
| Revisión OKR | 1er lun mes, 30 min | Goals Leantime | Semáforo en spec proyecto |

## Convenciones de nombres y etiquetas

- Tasks: verbo + entregable + fecha: `Entregar PB+cortes casa Emilia (vie 19/09)`.
- Etiquetas: `kaizen` · `bloqueado` · `demo` · `legal` (plano con valor jurídico) · `obra` · `academia`.
- Clases de servicio: estándar / **urgente** (fecha legal) / bloqueado visible (nunca escondido).
- Definition of Done por columna (ejemplo Revisión→Hecho): sello + PDF en `activos/` + entrada `entregables/` + link en ficha proyecto.

## MCP Leantime + agente del vault

Estado actual: Leantime **ya instalado en VPS**; pendiente (Semana 1): crear usuario Emilia, compartir URL/pass, conectar MCP Leantime al vault.

Automatizaciones objetivo (agente del vault):

1. Minuta Fathom → tasks Leantime (cada decisión = task con dueño/fecha).
2. Cierre de sprint → nota retro + victorias a `log.md` sin copiar a mano.
3. Alerta WIP/PPC: si PPC < 70% dos semanas, crear task `kaizen` automática.
4. Spec nuevo → proyecto Leantime espejo (Goals + Milestones + Sprint 1) en 1 comando.

Mientras el MCP no esté: carga manual lunes (15 min) con este pbook impreso al lado.

## Conceptos relacionados

- [[wiki/glosario/conceptos/kanban|kanban]]
- [[wiki/glosario/conceptos/agile-arquitectura|agile-arquitectura]]
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]
- [[wiki/glosario/conceptos/okr-goals|okr-goals]]
- [[wiki/glosario/conceptos/kaizen|kaizen]]
- [[wiki/glosario/conceptos/retrospectivas|retrospectivas]]

## Referencias

- Leantime — producto (Goals, Sprints, Milestones, Retrospectives, subtasks ilimitadas): https://leantime.io/ (verificado 2026-09-09 — 200)
- Leantime — repo open source + docs: https://github.com/Leantime/leantime (verificado 2026-09-09 — 200) y https://docs.leantime.io/ (verificado 2026-09-09 — responde, app JS)
- LCI — Last Planner (promesas, PPC): https://leanconstruction.org/lean-topics/last-planner-system/ (verificado 2026-09-09 — 200)
- Scrum.org — Sprint Retrospective: https://www.scrum.org/resources/what-is-a-sprint-retrospective (verificado 2026-09-09 — 200)
