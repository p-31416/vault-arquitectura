---
tipo: log
fecha_creacion: 2026-09-28
ultima_actualizacion: 2026-09-28
tags: [sesion, emilia, leantime, accesos, specs]
---

# Sesión 2026-09-28 — Alta Emilia en Leantime + spec para mañana

Más nuevo → más arriba

## 2026-09-28 noche — spec para mañana + cierre

- Pedido: dejar spec en `specs/` para ejecutar mañana 2026-09-29.
- Creado `specs/260929-alta-emilia-leantime.md` (tipo metodologia, estado plan): verificación EasyPanel, alta UI Read-Only + inherit en `STUDIO_OS-Emilia`, alternativa MCP/API con `$env:LEANTIME_TOKEN`, checklist lectura y cierre en log + sessions.
- Cierre de sesión con esta nota.

## 2026-09-28 noche — intento MCP y diagnóstico remoto

- Pedido con `si puedes usar el MCP adelante`: probar alta vía MCP Leantime.
- Verificado local: binario `P:/00-repos/npm-global/node_modules/leantime-mcp/bin/leantime-mcp.js` presente, `LEANTIME_TOKEN` en env (68 chars, valor nunca impreso), `opencode.json:33-36` apunta a `https://pitau.tech/mcp`.
- Payload existente: `P:\00-repos\pitau-tech\user-emilia.json` con `arq.emiliapimentalombardi@gmail.com` / Emilia Pimental Lombardi / member.
- Resultado remoto: `GET https://pitau.tech/` → 404 Laravel, `POST https://pitau.tech/mcp` válido → `{"error":"Not found"}`, `https://n8n.pitau.tech/` → 200. Puente MCP arranca pero remoto queda en revisión. `mcp list 5/5` previo solo confirma proceso stdio.
- Decisión: alta manual UI cuando el servicio vuelve + higiene pendiente (rotar token en claro en `create-user-emilia.ps1:4`).

## 2026-09-28 noche — pedido inicial y delegación

- Pedido: crear cuenta Leantime a Emilia para ver tareas, subtareas, goals y completados, vía @fathom-pm.
- Delegado a subagente `fathom-pm`: confirmó instancia `https://pitau.tech`, proyecto `STUDIO_OS-Emilia`, mails contractual `arq.emiliapimentalombardi@gmail.com` y operativo `vault.emilia.estudio@gmail.com`, rol propuesto Read-Only + inherit.
- Usuario confirma mail contractual.

## Archivos modificados

- `P:\00-repos\proyecto-pi\vault-arquitectura\specs\260929-alta-emilia-leantime.md` — creado con plan 2026-09-29
- `P:\00-repos\proyecto-pi\vault-arquitectura\raw\sessions\2026-09-28-sesion-alta-emilia-leantime.md` — esta nota

## Análisis cerebro-digital

### Topics

- Alta lectura Leantime (UI vs MCP/API) con servicio remoto en revisión
- Higiene secretos: token en claro hacia `{env:LEANTIME_TOKEN}` + rotación
- Rol mínimo (Read-Only + inherit) para visibilidad tareas/subtareas/Goals/completados

### Entidades

- Emilia Pimenta Lombardi, `arq.emiliapimentalombardi@gmail.com`, `STUDIO_OS-Emilia`, `https://pitau.tech/mcp`, `https://n8n.pitau.tech`, `leantime-mcp 1.6.5`, `opencode.json`, `create-user-emilia.ps1`, `P:\00-repos\pitau-tech\user-emilia.json`

### Hechos

- 2026-09-28 se confirma mail contractual Emilia y se deja spec fechado 2026-09-29 listo para ejecutar
- MCP local sano, remoto `pitau.tech` devuelve 404 en `/`, `/login`, `/api/*` y `Not found` en `/mcp`
- Ningún secreto impreso; mejora queda para siguiente ciclo
