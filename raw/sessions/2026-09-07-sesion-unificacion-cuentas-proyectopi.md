---
tipo: log
fecha: 2026-09-07
sesion: unificacion-cuentas-proyectopi
participantes: [SOL, opencode]
tags: [infra, git, github, opencode-zen, env, raw]
---

# 2026-09-07 — Sesión unificación cuentas a proyectopi.31416@gmail.com

## Objetivo
Unificar git / GitHub CLI / Opencode Zen bajo la cuenta única `proyectopi.31416@gmail.com` (login `p-31416`) y dejar `.env` de secrets operativo para free tier.

## Qué se hizo

### 1. Diagnóstico usuarios vigentes
- Git global `C:\Users\Solch16\.gitconfig` → `pitautech / pitau.tech@gmail.com`
- `includeIf gitdir:P:/00-repos/proyecto-pi/` → `P:\00-repos\.git-config-tokens\gitconfig-proyecto-pi` → `proyectopi / proyectopi.31416@gmail.com`
- Git local `vault-arquitectura/.git/config:9` solo tenía `user.email=proyectopi...` → efectivo híbrido `pitautech / proyectopi.31416@gmail.com` (inconsistente)
- `gh auth status` → `pitautech` activo (gho_***)
- `opencode.json:1` solo tenía `COMFYUI_URL`, sin provider
- `ANTHROPIC_API_KEY` en `Env:` (no usado en este repo)
- `.env` inexistente (`glob **/.env*` → 0)

### 2. Corrección Git
- `git config user.name "proyectopi"` + `git config user.email "proyectopi.31416@gmail.com"` en `vault-arquitectura/.git/config`
- Verificado: `git config user.name → proyectopi`, `user.email → proyectopi.31416@gmail.com` (efectivo local gana a global)

### 3. .env de secrets
- `.gitignore:22` ya contiene `.env` (no se commitea)
- Creado `P:\00-repos\proyecto-pi\vault-arquitectura\.env`:
  ```
  OPENCODE_API_KEY=sk-vXkO3... (zen pay-as-you-go, 70 modelos verificados via GET https://opencode.ai/zen/v1/models)
  GH_TOKEN=ghp_... (PAT classic)
  ```
- Inicial con `GITHUB_TOKEN` duplicado → removido, dejado solo `GH_TOKEN` (canónico para `gh`)
- `OPENCODE_API_KEY` validada: 70 modelos (ej. claude-fable-5) → free tier OK sin billing para modelos cost=0

### 4. GitHub CLI a p-31416
- Flujo `gh auth login --web` falló por timeout (códigos 7483-12B8, 5322-2482, 81BB-0FA5)
- Usuario creó PAT classic en https://github.com/settings/tokens/new con scopes `repo, workflow, read:org, gist, read:user`
- Pegado en `.env:9` `GH_TOKEN=ghp_TwDjkiW...`
- `cat .env | gh auth login --with-token` → `gh auth status` ahora:
  - `p-31416` activo (ghp_***, scopes gist,read:org,repo,user,workflow)
  - `pitautech` inactivo

### 5. Verificación final unificada
- Git: `proyectopi / proyectopi.31416@gmail.com`
- GH: `p-31416` activo
- Opencode Zen: `OPENCODE_API_KEY` operativa (free tier)

## Archivos afectados
- `P:\00-repos\proyecto-pi\vault-arquitectura\.git\config`
- `P:\00-repos\proyecto-pi\vault-arquitectura\.env` (gitignored)
- Keyring Windows (gh credentials)

## Pendiente / recordatorio
- Documentar cierre de sesión en `raw/` (esta nota) — pedido explícito de SOL.
- No se modificó `log.md` (inmutable, solo añade entradas arriba).

## Análisis cerebro digital (Karpathy — extrapolación)

### Topics candidatos a `wiki/glosario/software/`
- `gh auth login --with-token` / `gh auth status` → candidato `wiki/glosario/software/github-cli/gh-auth.md`
- `GH_TOKEN` vs `GITHUB_TOKEN` (precedencia gh) → nota en glosario github-cli
- `OPENCODE_API_KEY` (Zen) + `public` (anon free) → `wiki/glosario/software/opencode/zen-api-key.md`
- `git config includeIf gitdir:` (override order global vs local) → `wiki/glosario/software/git/includeif.md` + `wiki/glosario/software/git/git-config-precedencia.md`

### Entidades
- Personas: SOL (proyectopi.31416@gmail.com), pitautech (cuenta secundaria)
- Cuentas: `p-31416` (GitHub), `proyectopi` (git)
- Herramientas: `gh CLI`, `opencode Zen`, `ComfyUI` (`http://127.0.0.1:8188`)
- Vault: `vault-arquitectura`, `AGENTS.md`, `raw/sessions/`, `.env`

### Hechos/decisiones reutilizables
- Decisión: `.env` es gitignored (`.gitignore:22`) y centraliza `OPENCODE_API_KEY` + `GH_TOKEN` — patrón para todos los secrets del estudio
- Hecho: `gh` lee `GH_TOKEN` antes que `GITHUB_TOKEN`; `git config` local gana a `includeIf` si global define `[user]` después
- Reutilizable: `GET https://opencode.ai/zen/v1/models` con `Authorization: Bearer <key>` valida Zen sin TUI

## Referencias
- https://opencode.ai/docs/providers (OPENCODE_API_KEY)
- https://github.com/settings/tokens/new
- AGENTS.md estructura vault-arquitectura
