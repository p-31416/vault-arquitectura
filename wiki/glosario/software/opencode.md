---
tipo: software
software: opencode
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-09
tags: [glosario, software, opencode, zen]
---

# opencode

> Agente del vault (Zen free tier) — `OPENCODE_API_KEY`.

- [Zen free tier](#zen-free-tier)
- [OPENCODE_API_KEY](#opencode_api_key)
- [Agentes del vault](#agentes-del-vault)
- [Subagents](#subagents)
- [Permissions y modo](#permissions-y-modo)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Zen free tier

Pay-as-you-go con modelos `cost=0` gratis incluso con key real. Anon: `OPENCODE_API_KEY=public` (solo 7 modelos free). Validado: `GET https://opencode.ai/zen/v1/models` con `sk-vXk…` → 70 modelos (2026-09-07).

## OPENCODE_API_KEY

`https://opencode.ai/auth` → `https://opencode.ai/zen`. En `P:/00-repos/proyecto-pi/vault-arquitectura/.env:5` (`sk-vXkO3…`, len 67). `OPENCODE_API_KEY` es canónico; `OPENCODE_ZEN_API_KEY` es alias futuro (issue openclaw#87790, no usar aún).

> **Esquema 2026-09-08 — config por repositorio (sin global):** `~/.config/opencode/opencode.jsonc` eliminado y `~/.local/share/opencode/auth.json` sin credenciales `opencode`/`opencode-go`. Cada vault declara su provider en su `opencode.json` con `apiKey: "{env:OPENCODE_API_KEY}"` → la key se lee de su `.env` local via `with-env.ps1` / `with-env.sh`. Verificado: `vault-arquitectura` → `sk-vXkO3…` (proyecto-pi, Zen free tier), `vault-lidia` → `sk-GvrwL…` (pitautech, Go — misma key sirve para Zen y Go en esa cuenta).

## Config por repositorio

- **Global eliminado:** `C:\Users\Solch16\.config\opencode\opencode.jsonc` → borrado (backup `.bak-20260908-1215`), `auth.json` solo conserva `openrouter`. Evita cruzar cuotas entre cuentas.
- **Por repo:** `opencode.json` en cada vault con `provider.opencode.options.apiKey: "{env:OPENCODE_API_KEY}"` (y `opencode-go` en `vault-lidia` con la misma `OPENCODE_API_KEY` de pitautech, porque en Opencode una cuenta = una key para ambos productos).
- **Carga del .env:** Opencode **no** carga `.env` solo — requiere `.\with-env.ps1 opencode` (Windows) o `.\with-env.sh opencode` (bash). Sin wrapper, `apiKey` queda `""` y el provider no autentica (verificado 2026-09-08 con `opencode debug config`).
- **Free tier proyecto-pi:** Zen con `sk-vXkO3…` tiene modelos `cost=0` gratis incluso con key real (70 modelos vs 7 anon). Compartir la key Go de pitautech (`sk-GvrwL…`) implica compartir también su Zen — misma key, misma cuenta, misma cuota. No compartir esa key si se quiere aislar.

## Agentes del vault

| Agente | Modo | Temp | Qué hace | Config |
|---|---|---|---|---|
| `@vaultworm-arq` | subagent | 0.3 | Digest `raw/sessions/` → propuesta wiki | `.opencode/agents/vaultworm-arq.md` |
| `@brainstormy` | subagent | 0.85 | Ideación divergente/convergente | `.opencode/agents/brainstormy.md` |
| `@fathom-pm` | subagent | 0.3 | Reuniones Fathom → `specs/` → Leantime (pomodoro) | `.opencode/agents/fathom-pm.md` |
| `@contenidos` | subagent | 0.3 | Videos academia OBS → `wiki/estudio/` + pbooks | `.opencode/agents/contenidos.md` |
| `@sherlock` | subagent | 0.2 | Investigador GENERAL tema libre bilingüe ES/EN+IT doc-oficial-primero → `raw/research/` HITL | `.opencode/agents/sherlock.md` |

Registro completo (misión, triggers, permisos, cómo agregar uno): [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]].

## Subagents

`mode: subagent` = el agente corre aislado y reporta al primary; `mode: primary` (default) = conversa directo. Se invocan con `@mención` (`@vaultworm-arq digest`, `@brainstormy scamper`). Lo que decide si el primary delega es el `description` del frontmatter de cada agente.

## Permissions y modo

Cada agente declara `permission:` por herramienta (`read/grep/glob` allow, `bash` deny en ambos). `edit: allow` con `write` restringido a sus rutas: vaultworm-arq solo `raw/vaultworm-arq/` + `wiki/glosario/**` con `¿Avanzo?`; brainstormy solo `raw/brainstorm/` + `wiki/` si hay teoría nueva. Secrets vía `{env:}` nunca hardcodeados — ver capa OpenCode en [[wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode|pbk-config_ctas_git_github_opencode]].

## Conceptos relacionados

- [[wiki/glosario/conceptos/cerebro-digital-karpathy]]
- [[wiki/glosario/software/github-cli]]

## Referencias

- Providers / Zen: https://opencode.ai/docs/providers (verificado 2026-09-07 — 200)
- Mastra Zen: https://mastra.ai/models/providers/opencode (verificado 2026-09-07 — 200)
- Docker Zen: https://docs.docker.com/ai/docker-agent/providers/opencode-zen (verificado 2026-09-07 — 200)
