---
tipo: plan
proyecto: vault-arquitectura
fase: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [specs, planes, reuniones, fathom, contenidos, obs, leantime, milestones, okrs, agentes, pomodoro]
idioma: es
estado: plan
---

# PLAN — Dos agentes: @fathom-pm y @contenidos

> Decisión SOL 2026-09-09: UN solo agente no alcanza. DOS agentes separados con triggers propios. Nombres: `@fathom-pm` + `@contenidos`. Reemplaza el planteo de agente único anterior (ver `log.md`).

## SPEC

**Qué son:**
- `@fathom-pm` — agente de reuniones. Lee transcripción Fathom (vía MCP oficial `https://api.fathom.ai/mcp`, OAuth) en `raw/reuniones/` → 1 doc por reunión en `specs/YYMMDD-<tema>.md` (SPEC/PLAN/TASKS/MILESTONES-OKRs) → subdivide si hay varios temas → tasks aptas para Leantime. Entrenado en PM: `pbk-pm_vault` (Kanban+LPS, PPC, DoD, convenciones).
- `@contenidos` — agente de videos de academia IA (FASE 1: solo OBS). Graba con OBS → `activos/videos/<prefijo>-YYYY-MM-DD-<slug>.mkv` → `scripts/transcribir_ghl.py` (ffmpeg + faster-whisper) → extrae conceptos → salidas a `wiki/estudio/` + glosario + `pbooks/pbk-*`. FASE 2 (futuro): PDF + YouTube.

**Entradas:**
- Fathom: reuniones grabadas (hoy: par de reuniones con Emilia) → `raw/reuniones/YYYY-MM-DD-<tema>/` (carpeta a crear — hoy solo existen `sessions/`, `brainstorm/`, `vaultworm-arq/`).
- Contenidos: `.mkv/.mp4` OBS en `activos/videos/` (gitignored, carpeta única por prefijo+fecha) + audio/transcript vía `scripts/transcribir_ghl.py`. Piloto: video de hoy "entrega del servicio de IA".

**Salidas:**
- `@fathom-pm`: `specs/YYMMDD-<tema>.md` con estructura fija + propuesta de subdivisión multi-tema. Aprobado → Leantime (manual lunes 15 min hasta MCP Leantime).
- `@contenidos`: `wiki/estudio/<tema>.md` + propuestas glosario (vía vaultworm-arq) + `pbooks/pbk-*` cuando amerite (ej. Pbook "entrega del servicio de IA").
- vaultworm-arq NO se toca: sigue solo `wiki/glosario/` con revisión `¿Avanzo? (s/N)`.

**No hacen:**
- No escriben en `wiki/glosario/` directo (eso es vaultworm-arq).
- No crean `wiki/fuentes/` ni `tableros/t_NN` (schema Lidia descartado).
- No suben binarios a git (`/activos/` gitignored, solo referencias por ruta).

## PLAN

Estructura obligatoria del doc de reunión (`specs/YYMMDD-<tema>.md`):

```markdown
## SPEC (qué se decidió)
## PLAN (cómo, plan semanal)
## TASKS (tasks + subtasks diarias, con checkbox, regla pomodoro)
## MILESTONES y OKRs (alineación explícita)
## Fuentes (links a raw/ + activos/ + Fathom)
```

Reglas:
1. Cada reunión → 1 o N docs (1 por tema si se detectan varios).
2. Toda TASK cita milestone/OKR o se marca `sin-alineacion`.
3. Plan semanal Lun–Vie con subtasks diarias verificables.
4. **Regla pomodoro (decisión SOL 2026-09-09):** toda subtask completable en máx 25 min (1 pomodoro); tope 16 pomodoros/día **por persona** (Sol/Emilia); lo indivisible (ej. render 2 h) se parte en fases verificables. Reconciliado con `pbk-pm_vault`: WIP máx 2/persona, sprints Lun–Vie, PPC ≥ 80%.
5. Frontmatter `tipo: plan` + `estado: borrador|aprobado|en-leantime`.

## TASKS (construcción)

- [ ] MCP Fathom: declarado en `opencode.json` (remoto oficial + OAuth) — pendiente auth SOL (`opencode mcp auth fathom`) y descarga de reuniones con Emilia a `raw/reuniones/`
- [ ] Crear `.opencode/agents/fathom-pm.md` (mode subagent, temp 0.3, read/glob/grep/skill/webfetch allow, bash deny — espejo vaultworm-arq)
  - [ ] Intake: leer `raw/reuniones/<fecha>-<tema>/` + `specs/` existentes + milestones/OKRs vigentes + `pbk-pm_vault`
  - [ ] Análisis: transcripción → temas, decisiones, acuerdos, action items Fathom
  - [ ] Subdivisión: si >1 tema → proponer N planes
  - [ ] Output: 1 `.md` por tema en `specs/` con SPEC/PLAN/TASKS/MILESTONES-OKRs + regla pomodoro
  - [ ] Query+lint absorbidos: responde desde `index.md` + `specs/` + `wiki/` con `[[wikilinks]]`; verifica links/frontmatter/`specs/` con TASKS vacías o sin milestone
- [ ] Crear `.opencode/agents/contenidos.md` (misma base; temp 0.3)
  - [ ] Intake: `activos/videos/<prefijo>-YYYY-MM-DD-<slug>.mkv` → `transcribir_ghl.py` → `.mp3/.txt/.srt` + `wiki/raw/*.md`
  - [ ] Análisis: conceptos → propuestas `wiki/estudio/` + glosario (vía vaultworm) + `pbk-*`
  - [ ] FASE 1 solo OBS (PDF/YouTube → Fase 2)
  - [ ] Piloto: "entrega del servicio de IA" → Pbook
- [ ] Crear skills espejo `.opencode/skills/fathom-pm/SKILL.md` (`@fathom-pm`) y `.opencode/skills/contenidos/SKILL.md` (`@contenidos`)
- [ ] Registrar ambos en `pbk-agentes-vaultarq.md` (tabla + secciones) y `opencode.md` § Agentes
- [ ] Probar `@fathom-pm` con 1 reunión real de Emilia; probar `@contenidos` con video de hoy
- [ ] MCP Leantime (después de Fathom): usuario Emilia + URL/pass VPS → conectar → cierre del loop specs→Leantime

## MILESTONES y OKRs

- **M1 — Definido (este doc):** PLAN en dos tracks validado por SOL.
- **M2 — Fathom conectado:** MCP autenticado + reuniones con Emilia en `raw/reuniones/`.
- **M3 — Agentes implementados:** `agents/fathom-pm.md` + `agents/contenidos.md` + skills creados y probados (1 reunión real + video de hoy).
- **M4 — Loop semanal:** reunión/semana → specs/ → Leantime sin trabajo manual repetitivo.

**OKR:** 100% reuniones con PLAN en `specs/` en 24 h, 0 tareas sin milestone, 0 subtasks >25 min, 0 binarios en git.

## Fuentes

- MCP oficial Fathom: https://developers.fathom.ai/mcp-docs (server `https://api.fathom.ai/mcp`, OAuth; verificado 2026-09-09)
- Fathom API ref (meetings/transcripts): https://developers.fathom.ai/api-reference/meetings/list-meetings
- OpenCode MCP (remote + OAuth): https://opencode.ai/docs/mcp-servers/ (verificado 2026-09-09)
- PM canónico: [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]]
- Agentes: [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]]
- Pipeline academia: `specs/260907-ghl-extraccion-automatica.md`, `scripts/transcribir_ghl.py`
