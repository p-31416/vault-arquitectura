---
tipo: playbook
codigo: pbk-agentes-vaultarq
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [pbook, agentes, opencode, vaultworm-arq, brainstormy, subagent]
---

# pbk-agentes-vaultarq — Agentes del vault

> Registro de qué agentes existen, qué hacen, cómo están configurados (código) y cuándo corren. Definición viva en `.opencode/agents/*.md`; este pbook es el índice razonado.

- [Agentes (tabla)](#agentes-tabla)
- [vaultworm-arq — bibliotecario](#vaultworm-arq--bibliotecario)
- [brainstormy — facilitador](#brainstormy--facilitador)
- [fathom-pm — PM de reuniones](#fathom-pm--pm-de-reuniones)
- [contenidos — curador academia](#contenidos--curador-academia)
- [Comparativa](#comparativa)
- [Cómo agregar un agente nuevo](#cómo-agregar-un-agente-nuevo)
- [Ejecución online (backlog)](#ejecución-online-backlog)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Agentes (tabla)

| Agente | Modo | Temp | Qué hace | Cuándo corre | Config |
|---|---|---|---|---|---|
| `@vaultworm-arq` | subagent | 0.3 | Digest `raw/sessions/` → propone qué va a `wiki/` | Digest UNICO/día 23:00 AR + on-demand | `.opencode/agents/vaultworm-arq.md` |
| `@brainstormy` | subagent | 0.85 | Sesiones divergentes/convergentes → Top 3 + wildcards | On-demand (`brainstorm`, `idear`, `concurso`…) | `.opencode/agents/brainstormy.md` |
| `@fathom-pm` | subagent | 0.3 | Reuniones Fathom → `specs/` (SPEC/PLAN/TASKS/OKRs) → Leantime, regla pomodoro | Tras cada reunión + on-demand | `.opencode/agents/fathom-pm.md` |
| `@contenidos` | subagent | 0.3 | Videos OBS + PDF/video manual → reporte `raw/contenidos/` legible HITL → `wiki/estudio/` directo + glosario vía `@vaultworm-arq` (F1 = OBS + manual con invocación) | Tras grabar/transcribir o entrega manual + on-demand | `.opencode/agents/contenidos.md` |
| `@sherlock` | subagent | 0.2 | Investigador GENERAL tema libre (humano/redes/legado/papers/software manual-primero) bilingüe ES/EN+IT → `raw/research/` → `¿Avanzo?` → `@vaultworm-arq` + código paralelo anotado | On-demand (`@sherlock investiga <tema>`) | `.opencode/agents/sherlock.md` |

## vaultworm-arq — bibliotecario

**Cómo está conformado (código):** frontmatter `description` (drive de delegación) + `mode: subagent` + `temperature: 0.3` + `permission: {read, grep, glob, edit: allow; bash: deny; task, skill, webfetch: allow}`. Cuerpo: Misión (5 pasos: scan → extrae → verifica → digest → no escribe sin `¿Avanzo?`), Capacidades, Reglas duras (raw append-only, no inventar URLs, UNICO .md por tool, excluye p-31416/Emilia/Sol), Flujo automático (Intake → Digest → Review → Improve), Invocación, Restricciones.

**Qué hace:** lee `raw/sessions/*.md`, extrae topics/entidades/referentes/decisiones, verifica con web, genera `raw/vaultworm-arq/digest-YYYY-MM-DD.md` (Resumen + Topics→destino + Entidades + Referentes + Propuestas + Estado wiki + Decisiones + Preguntas). **Cuándo:** schedule diario 23:00 AR (UNICO digest/día unificando sesiones) + `workflow_dispatch` + `@vaultworm-arq digest` local. **No escribe** en `wiki/` sin aprobación (`@vaultworm-arq avanza`).

## brainstormy — facilitador

**Cómo está conformado (código):** frontmatter igual esquema + `temperature: 0.85` (divergencia cantidad > calidad). Cuerpo: Misión (divergir 25' → converger Impacto×Esfuerzo + JTBD → crudo `raw/brainstorm/` → `¿Avanzo a spec/proyecto?`), skill `brainstorming` (router 8 frameworks: Double Diamond default, Design Thinking, SCAMPER, Six Hats, Reverse, Brainwriting/Crazy 8s, JTBD, TRIZ lite), pensamiento lateral como sello.

**Qué hace:** sesiones de ideación para concursos/obra/servicios con Top 3 + wildcards + próximos pasos. **Cuándo:** on-demand manual o por mención (`brainstorm`, `idear`, `SCAMPER`, `concurso`, tarea sin ficha). Escribe `wiki/` solo si surge teoría/entidad nueva (con Referencias + wikilinks).

## fathom-pm — PM de reuniones

**Cómo está conformado (código):** frontmatter igual esquema + `temperature: 0.3` (criterio) + skill espejo `fathom-pm` (trigger `@fathom-pm`). Cuerpo: Misión (6 pasos: intake → analiza → planifica → pomodoro → query+lint → gate `¿Avanzo?`), entrenado en `pbk-pm_vault`.

**Qué hace:** lee `raw/reuniones/<fecha>-<tema>/`, genera `specs/YYMMDD-<tema>.md` (SPEC/PLAN/TASKS/MILESTONES-OKRs), subdivide multi-tema, aplica regla pomodoro (subtasks ≤25 min, 16/día por persona, WIP 2/persona). **Cuándo:** tras cada reunión + on-demand. Carga a Leantime manual (lunes 15 min) hasta MCP. Skills downstream: `architecture-decision-records`, `deep-research`.

## contenidos — curador academia

**Cómo está conformado (código):** frontmatter igual esquema + `temperature: 0.3` + skill espejo `contenidos` (trigger `@contenidos`). Cuerpo: Misión (6 pasos: intake OBS + manual → analiza → propone → reporte `raw/contenidos/` legible HITL → gate `¿Avanzo?` → escribe `wiki/estudio` / deriva glosario), FASE 1 = OBS + material manual con invocación explícita (`@contenidos procesa <path>`).

**Qué hace:** videos OBS **o PDF/video manual entregado por SOL** → reporte `raw/contenidos/YYYY-MM-DD-<slug>.md` (Resumen + Destino wiki + Contenidos extraídos + Ruta+frontmatter + Tags + Referencias 200) → con `s` escribe `wiki/estudio/**` y `pbooks/pbk-*` directo, glosario vía `@vaultworm-arq`. `@sherlock` solo BUSCA (web/redes/YouTube/PDFs); `@contenidos` es quien PROCESA. **Cuándo:** tras grabar/transcribir o entrega manual + on-demand. Piloto: "entrega del servicio de IA". Skills downstream: `article-writing`+`brand-voice`, `deep-research`.

## Comparativa

| | vaultworm-arq | brainstormy | fathom-pm | contenidos | sherlock |
|---|---|---|---|---|---|
| Temp | 0.3 (criterio) | 0.85 (cantidad) | 0.3 (criterio) | 0.3 (criterio) | 0.2 (criterio) |
| Output | digest + propuestas wiki | ideas + Top 3 + JTBD | specs/ + plan pomodoro | reporte `raw/contenidos/` + `wiki/estudio/` | informe `raw/research/` + `00-index` |
| Escribe wiki | solo `glosario/**` con `avanza` | solo si hay teoría nueva | `specs/` con `¿Avanzo?` | `wiki/estudio/**` directo + glosario vía vaultworm | nunca — propone, delega a vaultworm |
| Trigger auto | sí (schedule diario) | no (mención) | no (tras reunión) | no (tras grabar/manual) | no (`@sherlock investiga <tema>`) |
| Intake | `raw/sessions/` | prompt | `raw/reuniones/` | `activos/videos/` + manual SOL | web (`websearch/webfetch`) |

## Cómo agregar un agente nuevo

1. Crear `.opencode/agents/<slug>.md` con frontmatter (`description` = drive de delegación, `mode: subagent`, `temperature`, `permission:` mínimo).
2. Secciones: Misión (pasos numerados), Capacidades, Reglas duras, Invocación, Restricciones, Referencias internas.
3. Registrarlo en esta tabla + en [[wiki/glosario/software/opencode|opencode]] § Agentes del vault.
4. Probar on-demand antes de darle schedule.

## Ejecución online (backlog)

Agentes corriendo sin PC encendida ni VPS: ver `specs/260909-github-actions-agentes-online.md` (estado backlog, recuperable). Aplica a `@vaultworm-arq digest` vía `npx opencode run` con `OPENCODE_API_KEY` como secret.

## Workflows del vault (movidos de `AGENTS.md` 2026-09-10)

### Ingest de documento

1. El usuario sube un raw file (minuta, PDF extraído, transcript) a la carpeta correspondiente
2. Lees el archivo, identificas conceptos, tareas, decisiones
3. Creas/actualizas la entrada en `wiki/` correspondiente
4. Si aplica a un proyecto → actualizas `proyectos/<proyecto>/`
5. Si genera tareas → las registra el agente del flujo ingest→tasks en el tablero (ver [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]]; no duplicar: ese flujo ya lo corre otro agente)
6. Actualizas `00-index.md` y `log.md`

### Query

1. Lees `00-index.md` para identificar páginas relevantes
2. Lees las páginas identificadas
3. Sintetizas respuesta con `[[wikilinks]]` a fuentes usadas

### Lint (trimestral, `@vaultworm-arq lint`)

1. Revisar índices contra páginas existentes
2. Detectar páginas huérfanas
3. Verificar que referencias a activos sigan existiendo
4. Identificar proyectos que deberían archivarse
5. Reportar hallazgos

## Conceptos relacionados

- [[wiki/glosario/software/opencode|opencode]]
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]
- [[wiki/glosario/conceptos/design-thinking|design-thinking]]

## Referencias

- Opencode docs — agentes: https://opencode.ai/docs/agents/ (verificado 2026-09-08 — 200)
