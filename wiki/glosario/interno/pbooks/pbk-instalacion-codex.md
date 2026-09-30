---
tipo: metodologia
codigo: pbk-instalacion-codex
fecha_creacion: 2026-09-30
ultima_actualizacion: 2026-09-30
tags: [codex, chatgpt-desktop, mcp, fathom, leantime, autodesk-help, autocad, windows, sandbox, rutina-matutina, n8n, github-actions, brais-moure]
idioma: es
---

# pbk-instalacion-codex — Réplica vault con Codex (Windows) — canónico

> Canónico de instalación Codex para replicar `vault-arquitectura` en PC nueva (Emilia/Studio OS) sin repetir Git/GH/Node/Obsidian/Drive. Fuente: `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault.md` v1.0 + **Brais Moure — Codex + GPT-5.6** https://www.youtube.com/watch?v=af1KAQCD7mk como referencia primaria (corrige reporte previo que citaba opencode).

- [[#Qué llevar]]
- [[#Verificación previa]]
- [[#Instalar Codex — nativo Windows]]
- [[#Configurar sandbox Windows]]
- [[#MCPs — espejo de opencode.json sin tocar json]]
- [[#Clonar replicar vault]]
- [[#Problema PC tiene que estar prendida — soluciones sin PC prendida]]
- [[#Verificación final]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Qué llevar

- Este playbook impreso (1 carilla) + birome
- Acceso a cuenta ChatGPT Plus/Pro de Emilia (para `Sign in with ChatGPT`)
- Internet del estudio — installers se bajan con `winget` / `irm`, no llevar USB pesado

Links para usar allá:
- Codex https://github.com/openai/codex — install `irm https://chatgpt.com/codex/install.ps1 | iex` — guía https://developers.openai.com/codex/windows
- Codex CLI https://developers.openai.com/codex/cli
- Remote https://learn.chatgpt.com/docs/remote-connections
- Brais Codex 101 https://www.youtube.com/watch?v=af1KAQCD7mk

## Verificación previa

```powershell
git --version; gh auth status; node -v; npm -v
# Esperado: git >=2.23, gh logueado p-31416/proyectopi, node LTS
obsidian --version  # o abrir Obsidian → vault-emilia existe
# Drive Stream: GoogleDriveFS corriendo, carpeta 00-PROYECTOS/ visible
```

Si algo falta, volver a `playbook-instalacion-windows-emilia.md:3.1-3.2`.

> Ver Brais Codex 101 para demo en vivo de install.ps1 + Sign in with ChatGPT

## Instalar Codex — nativo Windows

> Codex ya no exige WSL2. Nativo trae sandbox `elevated` (preferido, 1 prompt admin) vs `unelevated` (fallback). Verificado ago 2026. Ver Brais Codex 101 para demo en vivo.

**Opción A — Standalone installer (recomendado, no necesita Node):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
codex --version
```
Instalador cae en `%LOCALAPPDATA%\Programs\OpenAI\Codex\bin`. Re-ejecutar mismo comando actualiza. Para install desatendido: `$env:CODEX_NON_INTERACTIVE=1`.

**Opción B — npm (si Node ya está):**
```powershell
npm install -g @openai/codex
codex --version
# paquete correcto es @openai/codex, no "codex" sin scope
```

**Auth (usa su plan pago, sin API key):**
```powershell
codex
# → elige "Sign in with ChatGPT" → abre browser → loguea con cuenta Emilia Plus/Pro
codex auth status
```

**Desktop (Remote + Voice):** instalar ChatGPT Desktop https://chatgpt.com/download → loguear misma cuenta → `Settings > Connections > Control this Mac or PC > Set up` → QR móvil.

## Configurar sandbox Windows

Recomendado `elevated` por defecto. Si política bloquea creación de usuarios sandbox, cae a `unelevated` (más débil, solo ACL).

Archivo `%USERPROFILE%\.codex\config.toml`:
```toml
[windows]
sandbox = "elevated"   # o "unelevated" si bloquea IT
# sandbox_private_desktop = false # solo si rompe UI, dejar default true
```

Verificar con `/status` dentro de `codex` o:
```powershell
codex mcp list
```

## MCPs — espejo de opencode.json sin tocar json

> `opencode.json` queda intacto en el repo. Codex lee `~/.codex/config.toml` (global) o `.codex/config.toml` (proyecto de confianza). Comandos espejo: `opencode mcp add/list` ↔ `codex mcp add/list`, `codex mcp login <nombre>` para OAuth.

```powershell
# Fathom remoto OAuth (Emilia)
codex mcp add fathom --url https://api.fathom.ai/mcp
codex mcp login fathom   # browser OAuth

# Fathom local API key proyectopi (FATHOM_API_KEY_PROYECTOPI en .env)
codex mcp add fathom-proyectopi -- npx -y @luminarylane/fathom-mcp-server
# env se toma de .env via with-env.ps1 o variable entorno: FATHOM_API_KEY_PROYECTOPI

# n8n (pitau.tech, N8N_MCP_TOKEN en .env)
codex mcp add n8n-mcp --url https://n8n.pitau.tech/mcp-server/http
# header Authorization Bearer se configura en config.toml con {env:N8N_MCP_TOKEN}

# Leantime (cuando toque futuro, LT token en .env)
codex mcp add leantime -- node P:/00-repos/npm-global/node_modules/leantime-mcp/bin/leantime-mcp.js https://pitau.tech/mcp --token {env:LEANTIME_TOKEN} --insecure

# Autodesk help (siempre)
codex mcp add autodesk-help --url https://developer.api.autodesk.com/knowledge/public/v1/mcp

# Autocad local (requiere .venv + AutoCAD)
codex mcp add autocad -- P:/00-repos/proyecto-pi/tools/autocad-mcp/.venv/Scripts/autocad-mcp.exe
# env ACAD_MCP_OUTPUT_ROOT=P:/00-repos/proyecto-pi/vault-arquitectura/activos/caddy-salidas

codex mcp list
```

Referencia tabla completa en `raw/docs/Estudio Pi – Guía de conexiones MCP.md`.

## Clonar replicar vault

```powershell
cd P:\00-repos\proyecto-pi
gh repo clone p-31416/vault-arquitectura
cd vault-arquitectura
# .env NO viene por git — copiar desde tu .env plantilla (OPENCODE_API_KEY, GH_TOKEN, FATHOM_API_KEY_PROYECTOPI, N8N_MCP_TOKEN, LEANTIME_TOKEN)
# No commitear .env (ya en .gitignore)
.\with-env.ps1 codex --version
.\with-env.ps1 opencode --version
```

Binarios nunca a git — solo refs `activos/...` o `C:\BIM\...` `AGENTS.md:44`.

## Problema PC tiene que estar prendida — soluciones sin PC prendida

> **Remote Codex (teléfono → host) y Drive Stream sí exigen host despierto/online/logueado** `learn.chatgpt.com/docs/remote-connections`. Para rutina matutina automática sin depender de eso, usar worker cloud.

**Solución recomendada — n8n en pitau.tech (ya lo tenés, always-on):**
- n8n Workflow Cron 07:00 AR → `Fathom list_calls` (usa `FATHOM_API_KEY_PROYECTOPI`) → filtra `created_after=yesterday` → `download transcript` → escribe `raw/reuniones/YYYY-MM-DD-{id}.md` directo a GitHub vía API (`GH_TOKEN`) **y** a Google Drive vía API (sin necesitar Drive Stream prendido). Commit `git add raw/reuniones/ && git push`.
- Teléfono no necesita estar. Cuando Emilia prende PC, hace `git pull` o Drive sync y ve todo.
- Voz “descargala” queda como disparo manual opcional vía Remote, no como rutina.

**Alternativa sin n8n — GitHub Actions (gratis, también always-on):**
- Clonar ` .github/workflows/vaultworm-arq.yml` (cron `0 2 * * *` 23:00 AR) en nuevo `fathom-pull.yml` cron `0 10 * * *` (07:00 AR = 10:00 UTC).
- Runner `ubuntu-latest` con secrets `FATHOM_API_KEY_PROYECTOPI`, `GH_TOKEN` → `curl https://api.fathom.ai/...` → `raw/reuniones/` → `git commit/push`.
- Ventaja: sin mantener workflow n8n. Desventaja: menos visual que n8n.

**Siempre-on dedicado (solo si necesitás ejecutar Codex, no solo bajar transcript):**
- Mini PC / VPS / Mac mini con ChatGPT desktop + Codex host 24/7 para que Remote y ejecución pesada no dependan de su notebook. Evaluar costo vs n8n/Actions si solo es “bajar reunión”.

**Qué proponer mañana:** Fase 1 n8n o Actions para Fathom→GitHub (sin PC), Fase 2 teléfono “descargala” solo como botón manual, Fase 3 Leantime `leantime` MCP cuando esté operativo (mismo worker).

## Verificación final

```powershell
codex --version; codex auth status; codex mcp list
gh auth status
git config user.email
Get-ChildItem raw/reuniones | Select-Object -Last 2 Name,LastWriteTime
# Probar 1 prompt lectura (no escritura):
codex exec "lista los .md en raw/reuniones de los últimos 2 días"
```

- [ ] Codex instalado + login Plus/Pro OK
- [ ] `codex mcp list` muestra fathom connected + autocad
- [ ] `raw/reuniones/` accesible + 1 transcript bajado
- [ ] Decisión: n8n vs GitHub Actions para rutina 07:00 (agendar fin de mes)
- [ ] CRD/Quick Assist sigue vigente como backup (`playbook-instalacion-windows-emilia.md:4`)
- [ ] Desktop ChatGPT Remote online + QR

## Conceptos relacionados

- [[wiki/glosario/interno/pbooks/pbk-codex_101_Brais|pbk-codex_101_Brais]]
- [[wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode|pbk-config_ctas_git_github_opencode]]
- [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]]
- [[wiki/glosario/software/codex|codex]]
- [[wiki/glosario/software/mcp-autodesk-help|mcp-autodesk-help]]
- [[wiki/glosario/software/mcp-autocad|mcp-autocad]]

## Referencias

- **Brais Moure — Codex + GPT-5.6: https://www.youtube.com/watch?v=af1KAQCD7mk (200) — fuente primaria**
- Codex Windows sandbox: https://developers.openai.com/codex/windows/windows-sandbox (200)
- Codex CLI: https://developers.openai.com/codex/cli (200)
- Codex Quickstart: https://developers.openai.com/codex/quickstart (200)
- Codex GitHub: https://github.com/openai/codex (200)
- Guía MCPs: `raw/docs/Estudio Pi – Guía de conexiones MCP.md`
- Matriz cuentas: [[wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode|pbk-config_ctas_git_github_opencode]]

> Alias `pbk-codex-instalacion.md` redirige aquí.
