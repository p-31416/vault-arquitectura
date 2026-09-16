---
tipo: software
software: github
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-07
tags: [glosario, software, github]
---

# github

> GitHub como plataforma (web) — repos, PAT, scopes.

- [PAT classic](#pat-classic)
- [Scopes mínimos](#scopes-mínimos)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## PAT classic

`https://github.com/settings/tokens/new` (logueado como `p-31416`): Note `vault-arquitectura` + Expiration `90 days` + Generate → `ghp_…` (un solo mostrado). Guardado en `.env:GH_TOKEN` (gitignored, `P:/00-repos/proyecto-pi/vault-arquitectura/.env:9`) y en keyring vía `gh auth login --with-token`.

## Scopes mínimos

`repo` (+ hijos), `workflow`, `read:org`, `gist`, `read:user`/`user:email` (para `gh api user`).

## Conceptos relacionados

- [[wiki/glosario/software/github-cli]]
- [[wiki/glosario/software/git]]

## Referencias

- Creating PAT: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens (verificado 2026-09-07 — 200)
- Scopes: https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app (verificado 2026-09-07 — 200)
