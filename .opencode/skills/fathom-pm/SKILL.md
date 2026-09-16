---
name: fathom-pm
description: "PM de reuniones Fathom: transcript → SPEC/PLAN/TASKS/MILESTONES-OKRs en specs/ → Leantime. Regla pomodoro (≤25 min, 16/día por persona). Se activa con @fathom-pm."
---

# Skill fathom-pm — espejo del agente

> Espejo operativo de `.opencode/agents/fathom-pm.md`. El agente es la definición viva; este skill es el trigger `@fathom-pm` + checklist rápida.

## Trigger

`@fathom-pm`, `@fathom-pm lee <fecha|tema>`, `fathom-pm procesa raw`

## Checklist

1. Leer `raw/reuniones/<fecha>-<tema>/` + `specs/` + milestones/OKRs + `pbk-pm_vault`
2. Extraer decisiones/acuerdos/action items (con dueño/fecha o a `## Preguntas`)
3. Multi-tema → N planes; 1 doc por tema en `specs/YYMMDD-<tema>.md`
4. Regla pomodoro: subtasks ≤25 min, 16/día por persona, citar milestone/OKR o `sin-alineacion`
5. Proponer → `¿Avanzo? (s/N)` → escribir → índices + `log.md` → `estado: aprobado` → Leantime

## Output contract

- `## SPEC` / `## PLAN` semanal / `## TASKS` checkbox / `## MILESTONES y OKRs` / `## Fuentes`
- Frontmatter `tipo: plan` + `estado: borrador|aprobado|en-leantime`

## Origen

`.opencode/agents/fathom-pm.md` + `specs/260909-agente-reuniones-fathom-specs.md` (Track F).
