---
tipo: log
fecha: 2026-09-07
sesion: glosario-vaultworm-arq-telegram
participantes: [SOL, vaultworm-arq, opencode]
tags: [glosario, referentes, vaultworm-arq, telegram, raw, karpathy]
---

# 2026-09-07 — Sesión glosario 4 ramas + vaultworm-arq + Telegram

## Objetivo
Corregir estructura `wiki/glosario/` a `wiki/glosario/software|entidades|referentes|conceptos`, añadir regla de calidad (conceptos relacionados + búsqueda web + referentes), renombrar agente a `vaultworm-arq` y diseñar flujo Telegram `vaultworm_arqbot` (PDF digest + feedback).

## Qué se hizo

### 1. AGENTS.md — glosario
- `AGENTS.md:157` reescrito de 2 → 4 ramas: `software/`, `entidades/`, `referentes/` (personas **y** estudios — simplifica, pedido SOL), `conceptos/`
- Regla nueva (toda entrada `wiki/glosario/**`): `## Conceptos relacionados` ≥2 wikilinks + `## Referencias` con ≥1 fuente externa verificada (websearch/webfetch, no 404) + si aparece figura/estudio → crear `wiki/glosario/referentes/<slug>.md`
- `AGENTS.md:32` estructura vault añadida `raw/sessions/` (ya estaba) verificada
- `AGENTS.md:208` cierre `raw/sessions/` ya con análisis cerebro-digital Karpathy (no se tocó, solo refs actualizadas a `wiki/glosario/software/`)

### 2. Filesystem wiki/glosario
- Físico: `wiki/software/glosario/` → `wiki/glosario/software/` (movido con `Move-Item`), creado `wiki/glosario/conceptos/` y `wiki/glosario/entidades/00-index.md` ya existía con `00-index` convention
- Creado `wiki/glosario/referentes/` + `00-index.md:1` (tabla Karpathy + BIG placeholder) + `template.md:1` (frontmatter `tipo: referente`)
- Seed `wiki/glosario/referentes/andrej-karpathy.md:1` — 3 fuentes verificadas 200: gist `llm-wiki`, Codersera, Ask Glitch; `## Conceptos relacionados` a `cerebro-digital-karpathy`
- `wiki/glosario/00-index.md:11` tabla 4 filas; `wiki/glosario/conceptos/00-index.md:14` link a referente; `wiki/glosario/conceptos/cerebro-digital-karpathy.md:12` corregido a `## Conceptos relacionados` + refs verificadas
- `wiki/software/index.md:30` link cambiado a `[[wiki/glosario/index|Glosario]]` con sublinks
- `.obsidian/workspace.json:190` `raw/bookworm` → `raw/vaultworm-arq`

### 3. Renombre bookworm → vaultworm-arq
- `raw/bookworm/` → `raw/vaultworm-arq/` + `digest-2026-09-07.md` parcheado
- `.opencode/agents/bookworm.md` → `vaultworm-arq.md:1` (`@vaultworm-arq`, `@vaultworm-arq digest`, `@vaultworm-arq avanza`, `raw/vaultworm-arq/digest-*.md`)
- `.github/workflows/bookworm.yml` → `vaultworm-arq.yml:1` (name, `npx opencode run "@vaultworm-arq digest"`, `git add raw/vaultworm-arq/`)
- `wiki/glosario/referentes/00-index.md:21` link a `[[.opencode/agents/vaultworm-arq|vaultworm-arq]]`

### 4. Agente vaultworm-arq + digest
- Creado `.opencode/agents/vaultworm-arq.md:1` (subagent temp 0.3, perm read/grep/glob/edit/webfetch, no bash) — misión: scanea `raw/sessions/`, extrae topics/entidades/referentes, verifica con web, genera `raw/vaultworm-arq/digest-YYYY-MM-DD.md`
- `raw/vaultworm-arq/` creado + `digest-2026-09-07.md:1` inicial (5 topics: git config precedencia, includeIf, gh auth GH_TOKEN, OPENCODE_API_KEY, raw/sessions; 3 fuentes 200 cada una) — patrón iterativo ✅/✏️/❌ → `@vaultworm-arq avanza`
- `.github/workflows/vaultworm-arq.yml:1` triggers: push `raw/sessions/**` + cron lunes 12:00 UTC + workflow_dispatch, usa `OPENCODE_API_KEY` + `GH_TOKEN`

### 5. Telegram vaultworm_arqbot (diseño)
- `.env:14` placeholders `TELEGRAM_BOT_TOKEN=` + `TELEGRAM_CHAT_ID=` (grupo con Emilia)
- Plan: workflow genera PDF (`pandoc digest.md -o digest.pdf`) + `curl api.telegram.org/bot$TOKEN/sendDocument` con inline keyboard ✅/✏️/❌; n8n futuro `getUpdates` → `/vaultworm` feedback → issue/commit → trigger `@vaultworm-arq avanza`

## Archivos modificados
- `AGENTS.md`
- `wiki/glosario/00-index.md`
- `wiki/glosario/software/00-index.md` (movido) + `template.md`
- `wiki/glosario/conceptos/00-index.md`, `wiki/glosario/conceptos/cerebro-digital-karpathy.md`
- `wiki/glosario/entidades/00-index.md` (preexistente)
- `wiki/glosario/referentes/00-index.md`, `template.md`, `andrej-karpathy.md`
- `wiki/software/index.md`
- `.obsidian/workspace.json`
- `.opencode/agents/vaultworm-arq.md` (renombrado)
- `.github/workflows/vaultworm-arq.yml`
- `raw/vaultworm-arq/digest-2026-09-07.md`
- `raw/sessions/2026-09-07-sesion-unificacion-cuentas-proyectopi.md` (refs parcheadas bookworm→vaultworm-arq)
- `.env`

## Análisis cerebro digital (Karpathy)

### Topics candidatos a `wiki/glosario/software/`
- `pandoc md→pdf` + `telegram bot sendDocument` → `wiki/glosario/software/telegram/vaultworm-bot.md` (cuando se implemente n8n)
- `n8n webhook telegram` → `wiki/glosario/software/n8n/telegram-workflow.md`
- `opencode agent` (subagent) → `wiki/glosario/software/opencode/agent.md`

### Entidades
- Personas: SOL, Emilia, p-31416
- Agentes: `vaultworm-arq` (ex-bookworm), `brainstormy`
- Bots: `vaultworm_arqbot` (Telegram)

### Referentes
- Andrej Karpathy (ya), BIG (pendiente ejemplo en `referentes/big-bjarke-ingels-group.md`)

### Hechos/decisiones reutilizables
- Decisión: `referentes/` cubre persona **y** estudio (no separar personas/estudios) — simplifica, pedido SOL
- Hecho: toda entrada glosario debe traer conceptos relacionados + web verificada — se auto-verifica vía vaultworm-arq digest + lint trimestral
- Reutilizable: `grep Select-String bookworm → 0` valida renombre completo

## Referencias
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (200)
- https://cli.github.com/manual/gh_auth_login (200)
- https://opencode.ai/docs/providers (200)
- https://core.telegram.org/bots/api#senddocument (a verificar al implementar)
