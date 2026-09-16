---
tipo: software
software: git
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-07
tags: [glosario, software, git]
---

# git

> Índice interno — `git` como herramienta única del vault.

- [Config y precedencia](#config-y-precedencia)
- [includeIf gitdir](#includeif-gitdir)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Config y precedencia

- `git config --show-origin --get-all user.name` muestra origen por capa.
- Orden efectivo: `system < global < includeIf < local (.git/config)`. El `includeIf` se lee en el punto donde aparece en `~/.gitconfig`; un `[user]` posterior en el global lo sobreescribe (caso `pitautech` vs `proyectopi`).
- Verificación local: `git config user.name` / `user.email` debe dar `proyectopi / proyectopi.31416@gmail.com` en `vault-arquitectura` (`P:/00-repos/.git-config-tokens/gitconfig-proyecto-pi`).

## includeIf gitdir

```ini
[includeIf "gitdir:P:/00-repos/proyecto-pi/"]
  path = P:/00-repos/.git-config-tokens/gitconfig-proyecto-pi
```

`gitdir:` matchea cualquier repo debajo de ese prefijo. Usado para separar `proyectopi` vs `pitautech`.

## Conceptos relacionados

- [[wiki/glosario/conceptos/cerebro-digital-karpathy]]
- [[wiki/glosario/software/github-cli]]

## Referencias

- Doc oficial `git-config`: https://git-scm.com/docs/git-config (verificado 2026-09-07 — 200)
- Includes: https://git-scm.com/docs/git-config#_includes (verificado 2026-09-07 — 200)
