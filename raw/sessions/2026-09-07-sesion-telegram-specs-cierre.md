---
tipo: log
fecha: 2026-09-07
sesion: telegram-specs-cierre
participantes: [SOL, opencode]
tags: [telegram, bot, specs, vault, cierre]
---

# 2026-09-07 — Sesión Telegram bot + planes a specs + cierre día

## Objetivo
Analizar comunicación Telegram con Emilia (canales vs grupos vs foro con topics) y generar plan de bot que vuelque a `raw/telegram/` por día/tema marcando tareas pendientes. Luego normalizar que todos los planes viven en `/specs`.

## Qué se hizo

### 1. Análisis Telegram
- Pregunta SOL: ¿Telegram tiene canales? ¿Cómo volcar a `raw/telegram/` por día, separando temas y tareas?
- Respuesta: Tabla Canal vs Grupo vs Supergrupo Foro (Topics). Foro con `General/Diseño/Obra X/Admin` es ideal para Emilia (1 grupo, 4 pestañas, `message_thread_id` por topic). Canal solo broadcast. Bot `@StudioOSBot` con privacy off.

### 2. Plan bot Telegram
- Creado `wiki/estudio/plan-telegram-vault.md` (164 líneas): arquitectura polling vs webhook (Tailscale), estructura `raw/telegram/YYYY-MM-DD.md` por día separado por `## #topic`, job 22:00 extrae `→ [ ]` con regex + Ollama local, comandos `/resumen` `/tareas` `/vault`, seguridad `.env` gitignored.

### 3. Normalización specs
- SOL: "los planes iban en /specs"
- Movidos: `wiki/estudio/plan-telegram-vault.md` → `specs/260907-telegram-vault.md`; `wiki/estudio/plan-extraccion-automatica-ghl.md` → `specs/260907-ghl-extraccion-automatica.md`
- SOL: "si, todos los planes en spec"
- Movido: `proyectos/STUDIO_OS-Emilia/documentacion/06-plan-ingest-ghl-6-etapas.md` → `specs/260907-ghl-ingest-6-etapas.md`
- Bulk fix refs `wiki/estudio/plan-*` y `proyectos/.../06-plan*` → `specs/260907-*` (30 archivos). Corrupción UTF8 en `proyectos/STUDIO_OS-Emilia/00-index.md` y `log.md` por PowerShell bulk → restaurado `00-index.md` via `default.write` UTF8 limpio, `log.md` header corregido via `default.edit`.

### 4. Estado final specs
- `specs/` contiene: `260907-vault_cerebro.md`, `260907-ghl-ingest-6-etapas.md`, `260907-ghl-extraccion-automatica.md`, `260907-telegram-vault.md` (convención `YYMMDD-{tema_snake}`)

## Archivos modificados

- **Creados:** `specs/260907-telegram-vault.md` (movido), `specs/260907-ghl-extraccion-automatica.md` (movido), `specs/260907-ghl-ingest-6-etapas.md` (movido)
- **Eliminados:** `wiki/estudio/plan-telegram-vault.md`, `wiki/estudio/plan-extraccion-automatica-ghl.md`, `proyectos/STUDIO_OS-Emilia/documentacion/06-plan-ingest-ghl-6-etapas.md`
- **Corregidos:** `proyectos/STUDIO_OS-Emilia/00-index.md` (encoding), `log.md` (header)
- **Sesión:** `raw/sessions/2026-09-07-sesion-telegram-specs-cierre.md` (este archivo)

## Análisis cerebro digital (Karpathy)

### Topics candidatos a `wiki/glosario/software/`

- `telegram-bot` → `wiki/glosario/software/telegram/bot.md` (BotFather, privacy, polling vs webhook, `message_thread_id`)
- `telegram-foro` → `wiki/glosario/software/telegram/foro-topics.md` (supergrupo foro, topics, canal vs grupo)
- `specs` → concepto `wiki/glosario/conceptos/specs.md` (convención `YYMMDD-{tema}`, planes en specs, no en wiki/estudio ni proyectos)

### Entidades

- Personas: SOL, Emilia Pimenta
- Proyecto: `STUDIO_OS-Emilia` (Supergrupo Foro `Studio OS — Emilia` con 4 topics)
- Bot: `@StudioOSBot` (token `TELEGRAM_BOT_TOKEN` en `.env`)
- Vault: `specs/` (4 planes), `raw/telegram/` (destino bot), `wiki/glosario/software/telegram/` (futuro)

### Hechos/decisiones reutilizables

- Decisión: **todos los planes en `/specs`** con prefijo `YYMMDD-` — no en `wiki/estudio/` ni `proyectos/.../documentacion/`. Si se crea plan en otro lado, lint lo mueve.
- Decisión: `proyectos/STUDIO_OS-Emilia/00-index.md` es índice cliente, no lugar de planes — linkea a `specs/` via wikilink.
- Hecho: PowerShell `Set-Content` sin `-Encoding UTF8` corrompe `→` `—` `á` → usar `default.write`/`default.edit` para .md con acentos.
- Reutilizable: Supergrupo Foro + bot polling es patrón para cualquier cliente chico (2-4 personas) — 1 grupo, N topics por obra, 1 bot, 1 archivo `raw/telegram/YYYY-MM-DD.md` por día.
- Pendiente: implementar `scripts/telegram-bot/bot.py` (polling) + `raw/telegram/` cuando SOL cree el foro y pegue token.

## Referencias

- `specs/260907-telegram-vault.md`
- `specs/260907-ghl-ingest-6-etapas.md`
- `specs/260907-ghl-extraccion-automatica.md`
- `AGENTS.md` (estructura vault, glosario 5 ramas)
