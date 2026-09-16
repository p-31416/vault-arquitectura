---
tipo: software
software: github-cli
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-07
tags: [glosario, software, gh]
---

# github-cli (gh)

> CLI `gh` separada de `github` (web).

- [Auth — GH_TOKEN vs GITHUB_TOKEN](#auth--gh_token-vs-github_token)
- [Login](#login)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Auth — GH_TOKEN vs GITHUB_TOKEN

`gh` lee `GH_TOKEN` primero, luego `GITHUB_TOKEN` (fallback Actions). En este vault: solo `GH_TOKEN` en `P:/00-repos/proyecto-pi/vault-arquitectura/.env:9`. `gh auth status` muestra activo `p-31416`.

## Login

Web expira rápido: `gh auth login --web` (código `XXXX-XXXX`, 3 min). Preferido headless: `gh auth login --with-token < <(grep GH_TOKEN .env)` o `echo $GH_TOKEN | gh auth login --with-token`.

## Conceptos relacionados

- [[wiki/glosario/software/github]]
- [[wiki/glosario/software/git]]

## Referencias

- Manual `gh auth login`: https://cli.github.com/manual/gh_auth_login (verificado 2026-09-07 — 200)
- Environment: https://cli.github.com/manual/gh_help_environment (verificado 2026-09-07 — 200)
