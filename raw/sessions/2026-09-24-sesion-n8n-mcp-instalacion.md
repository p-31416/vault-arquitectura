---
tipo: log
fecha_creacion: 2026-09-24
ultima_actualizacion: 2026-09-24
tags: [sesion, n8n, mcp, opencode, with-env, vault-lidia, playbook]
---

# Sesión 2026-09-24 — n8n MCP instance-level en vault-arquitectura + playbook vault-lidia

## Qué se hizo

- Pedido inicial (vault-lidia): verificar MCP n8n funcional en `P:\00-repos\pitau-tech\vault-lidia` + docs oficiales a wiki como playbook.
- Verificado `vault-lidia/opencode.json:16` → `n8n-mcp` remote `https://n8n.pitau.tech/mcp-server/http` + `Bearer {env:N8N_MCP_TOKEN}` enabled:true; `.env:2` con `N8N_MCP_TOKEN` presente (272 chars, solo metadata len+prefijo, valor nunca impreso).
- Docs oficiales verificadas via webfetch 200 OK: `docs.n8n.io/connect/connect-to-n8n-mcp-server` (+ `.md`), `mcp-server-tools-reference`, `mcp-client-examples`, `blog.n8n.io/n8n-mcp-server` (2026-04-29, requiere ≥2.18.4), `github.com/n8n-io/skills`.
- Aclaradas 2 credenciales distintas: `N8N_MCP_TOKEN` (MCP instance-level, JWT eyJ, la que usa OpenCode) vs `N8N_API_KEY` (REST `X-N8N-API-KEY` para `/api/v1/*`, no la usa el MCP, no existe en ningún `.env` y no hace falta).
- Detectado: ESTE repo (vault-arquitectura) no tenía ni entrada `n8n-mcp` en `opencode.json` ni `N8N_MCP_TOKEN` en `.env` (solo OPENCODE_API_KEY, GH_TOKEN, TELEGRAM_*, FATHOM_API_KEY_PROYECTOPI).
- Agregado a ESTE repo (con aprobación explícita "agrega el MCP"): bloque `mcp.n8n-mcp` remote en `opencode.json` + línea `N8N_MCP_TOKEN=` vacía en `.env` para que el usuario pegue el token. JSON validado (`comfyui, n8n-mcp, fathom, fathom-proyectopi`).
- Explicado `with-env.ps1:1-46` (carga `.env` → `env:` → ejecuta comando; necesario porque `opencode.json` usa `{env:...}` que OpenCode no resuelve sin env cargado).
- Aclarado reinicio: VPS/n8n no se reinicia; el cliente OpenCode sí debe recargar (cada `.\with-env.ps1 ...` es proceso fresco; sesión persistente requiere restart/reload MCP).

## Archivos modificados

- `P:\00-repos\proyecto-pi\vault-arquitectura\opencode.json` — agregado `mcp.n8n-mcp` (remote, `https://n8n.pitau.tech/mcp-server/http`, `Bearer {env:N8N_MCP_TOKEN}`)
- `P:\00-repos\proyecto-pi\vault-arquitectura\.env` — agregada línea `N8N_MCP_TOKEN=` vacía + comentario (gitignored, no aparece en `git status`)
- `P:\00-repos\pitau-tech\vault-lidia\wiki\glosario\interno\playbooks\Pbook-n8n-mcp-instalacion.md` — creado (instance-level + OAuth vs API key + exponer workflows + skills + tools reference + Anexo B comunitario)
- `P:\00-repos\pitau-tech\vault-lidia\wiki\glosario\interno\playbooks\README.md` — índice MCPs + fecha 2026-09-24
- `P:\00-repos\pitau-tech\vault-lidia\wiki\glosario\entidades\n8n.md` — sección MCP + referencias + fecha 2026-09-24

## Análisis cerebro-digital

### Topics

- n8n instance-level MCP vs MCP Server Trigger (`mcpTrigger`) vs MCP Client Tool vs servidor comunitario `czlonkowski/n8n-mcp` (docs 2.616 nodos)
- OAuth recomendado vs API key Bearer; `Available in MCP` por workflow; bulk proyecto/carpeta; auto-expose 2.36.0; headers proxy `MCP-Protocol-Version/Mcp-Method/Mcp-Name`
- `using-n8n-skills-official` como router obligatorio + protocolo validate-verify-publish; `with-env.ps1/.sh` como única fuente `.env`
- Cross-repo `.env`: no se comparte ni se copia archivo; cada repo su `.env`, token reusable si misma instancia/usuario

### Entidades

- n8n.pitau.tech (self-hosted EasyPanel), OpenCode MCP client, `N8N_MCP_TOKEN`, `with-env.ps1`, `n8n-io/skills`, vault-lidia, vault-arquitectura

### Hechos

- 2026-09-24 vault-lidia MCP n8n ya funcional (token 272 chars presente); vault-arquitectura quedó cableado pendiente solo de pegar token + `opencode mcp list` → `✓ connected`
- `.env` de arquitectura gitignored (no figura en `git status`); `opencode.json` sí trackeado (M opencode.json)
- Ningún secreto completo impreso en chat ni en playbook (solo len/prefijo header JWT público)

## Próximo

- Usuario pega token en `.env` → `.\with-env.ps1 opencode mcp list` → `n8n-mcp ✓ connected`
- Recargar sesión OpenCode persistente para que levante el nuevo server
- Opcional: agregar `N8N_API_KEY=` solo si se quiere REST directo fuera del MCP
