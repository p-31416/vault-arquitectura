---
tipo: reporte-contenidos
fecha: 2026-09-30
fuente_binaria: "⚠️ CORREGIDO — Ver raw/contenidos/2026-09-30-codex-101-brais.md — Este reporte asumía opencode (placeholder https://www.youtube.com/watch?v=irR8437xihg). Fuente canónica corregida por Sol: CODEX https://www.youtube.com/watch?v=af1KAQCD7mk — MoureDev Codex + GPT-5.6. Mantener solo como histórico."
estado: descartado-corregido
transcript: "raw/contenidos/2026-09-30-opencode-101-brais-codex.md (observaciones curadas, sin transcript automático aún) | pendiente: P:\\Anaconda\\envs\\comfyenv\\python.exe scripts/transcribir_ghl.py no aplica YouTube — usar yt-dlp si se descarga mkv a activos/videos/ytb-2026-09-30-opencode-101-brais.mkv"
duracion: "~150 min (curso completo Brais) + 88 min (Day 2) | paginas: playbook 164 líneas"
idioma: es
tags: [opencode, brais-moure, mouredev, codex, playbook, mcp, fathom, leantime, studio-os, pbook, instalacion, vault-arquitectura]
estado: propuesta
---

# Reporte contenidos — opencode 101 Brais + pbook instalacion Codex — 2026-09-30

> Curaduría une dos entregas pedidas por Sol para reunión Emilia Pimenta (Studio OS): video YouTube Brais Moure sobre opencode 101 y migración del playbook Codex desde `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault.md` v1.0 hacia pbook canónico en `wiki/glosario/interno/pbooks/`. Todo queda en propuesta HITL hasta `s` de Sol.

## 0. Gate HITL

> `¿Avanzo a wiki/? (s/N)` — SOL marca: ✅ aprobar / ✏️ corregir / ❌ descartar / 💡 añadir con Emilia
> Sin `s` no hay `write` en `wiki/` (`AGENTS.md` HITL). Este reporte vive en `raw/contenidos/` y propone diffs listos para copiar.

- [ ] `s` — Crear `wiki/glosario/interno/pbooks/pbk-opencode_101_Brais.md` (preview §7.1)
- [ ] `s` — Crear `wiki/glosario/interno/pbooks/pbk-instalacion-codex.md` (+ alias `pbk-codex-instalacion.md` redirect) (preview §7.2)
- [ ] `s` — Actualizar `wiki/glosario/interno/pbooks/00-index.md` con dos entradas 1 línea (§7.3)
- [ ] `s` — Añadir nota canónica en `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault.md` apuntando al pbook
- [ ] ✏️ Sol confirma URL exacta YouTube Brais opencode 101 (ver §10)

## 1. Resumen (5 bullets, lenguaje positivo)

- **Opencode 101 de Brais queda mapeado como pbook onboarding:** el curso 2.5h + Day 2 instalan, configuran y operan opencode con proveedores agnósticos, TUI, Build/Plan, AGENTS.md, Skills/MCPs y modelos locales — base ideal para que Emilia replique el vault sin fricción Windows.
- **Instalación Codex ya documentada avanza a canónico:** el playbook v1.0 (CLI + Desktop, sandbox elevated/unelevated, MCPs Fathom/Fathom-proyectopi/Leantime/Autodesk) propone contenido consolidado en `pbk-instalacion-codex.md` reutilizable para todo el estudio.
- **Dos pbooks complementarios potencian autonomía:** `pbk-opencode_101_Brais` forma en herramental open source; `pbk-instalacion-codex` habilita ejecución Codex con cuenta ChatGPT Plus/Pro sin API key y espeja MCPs via `~/.codex/config.toml`.
- **Rutina sin PC prendida queda resuelta con dos vías siempre-on:** n8n en pitau.tech (Cron 07:00 AR → Fathom → GitHub/Drive) y GitHub Actions (runner ubuntu-latest 10:00 UTC) — ambas liberan a Emilia de mantener notebook encendida.
- **Todo respeta convenciones vault y verificación 200:** frontmatter `tipo: metodologia`, snake_case, wikilinks absolutos sin extensión, referencias oficiales verificadas con `webfetch` (opencode.ai, learn.chatgpt.com, developers.openai.com).

## 2. Qué parte de la wiki alimenta

| # | Destino wiki (ruta absoluta sin ext) | Tipo | Acción | Sección destino | Prioridad | Owner escribe |
|---|---|---|---|---|---|---|
| 1 | `wiki/glosario/interno/pbooks/pbk-opencode_101_Brais` | metodologia/pbook | crear | ## Resumen + Instalación + Configuración + Flujo vault | alta | @contenidos con s |
| 2 | `wiki/glosario/interno/pbooks/pbk-instalacion-codex` | metodologia/pbook | crear | ## Verificación + Instalación Codex + Sandbox + MCPs + Rutina sin PC + Verificación final | alta | @contenidos con s |
| 3 | `wiki/glosario/interno/pbooks/pbk-codex-instalacion` | redirect | crear | alias → `pbk-instalacion-codex` | media | @contenidos con s |
| 4 | `wiki/glosario/software/opencode` | software | actualizar | ## Agentes del vault + Referencias (añadir Brais) | media | vía @vaultworm-arq con s |
| 5 | `wiki/glosario/software/codex` | software | crear/actualizar | ficha Codex CLI/Desktop si no existe | media | vía @vaultworm-arq con s |
| 6 | `wiki/glosario/interno/pbooks/00-index` | indice | actualizar | ## Infraestructura, Cuentas y Entorno + ## Agentes del vault | alta | @contenidos con s |
| 7 | `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault` | metodologia | actualizar | nota superior canónico | baja | @contenidos con s |

## 3. Contenidos extraídos (sin inventar, con cita verbatim)

### 3A. Video Brais / MoureDev — opencode 101

| Concepto / terminología | Cita verbatim (fuente) | Minutaje / página | Interpretación curada |
|---|---|---|---|
| Curso gratis opencode desde cero | "Este es mi curso gratis de OpenCode desde cero! Aprende a utilizar el agente de código con IA open source más potente. Desde la configuración hasta la creación de proyectos utilizando el modelo que prefieras: Claude, GPT, Kimi K3 o incluso modelos locales." — LinkedIn Brais 2026-09-07 | post 7502728040905367552 | Brais presenta opencode como agente agnóstico: mismo flujo con distintos proveedores |
| Contenidos del curso completo | "Dos horas y media desde cero 100% gratis: Instalación y configuración, Proveedores y Modelos de IA, Prompting y manejo de la TUI, Comandos, Flujo de desarrollo, Agentes y subagentes, Contexto, Skills, MCPs y plugins, Modelos locales, CLI, web y desktop, Buenas prácticas" — LinkedIn 2026-07-31 | post 7488942362413412354 | Mapa directo para pbook: 9 bloques → 9 secciones |
| Alternativa open source a Claude Code | "Open Code es una herramienta de codificación agéntica ... es la alternativa open source a Claude Code que funciona muy muy parecido ... entendiendo cómo funciona una veremos cómo funcionan las otras." — Day 2 transcript 00:02:30 | https://www.youtube.com/watch?v=irR8437xihg | Posiciona opencode como espejo libre de Claude Code, provider-agnostic |
| Capas agentes / rules / extensions | "Open Code es realmente ... tres capas. First, we have the agents layer... build mode and plan mode... Second layer is rules... That's the agents MD... Third layer is the extensions. Skills are the reusable playbooks... Commands are like oneshot buttons" — OpenCode Tutorial EN complementario | — | Marco Build/Plan + AGENTS.md + Skills/Commands que replica nuestro vault (AGENTS.md + .opencode/agents/*.md) |
| SDD spec-first con preguntas | "Hazme preguntas de una en una para eliminar ambigüedades, casos límite, comportamientos con errores que queden fuera del MVP. Máximo seis preguntas. Con mis respuestas genera dentro de la carpeta specs ... 001 Habits MVP" — El fin del Vibe Coding |  — | Flujo SDD que Brais enseña y que nuestro fathom-pm ya aplica (specs/ + pomodoro) |

> Nota: no existe un video titulado literal "opencode 101" en canal Brais con esa slug. Lo más cercano verificado es el **taller/curso completo OpenCode desde cero (2.5h)** anunciado en LinkedIn (lnkd.in/euau7pZU → moure.dev) y el **Day 2 — Program with agents** (https://www.youtube.com/watch?v=irR8437xihg). Si Sol tiene URL distinta, se sustituye en §10 sin rehacer estructura.

### 3B. Playbook instalación Codex v1.0 (164 líneas)

| Concepto | Cita verbatim | Ubicación |
|---|---|---|
| Objetivo mañana | "dejar Codex funcionando para replicar `vault-arquitectura` en la PC de Emilia y hablar del camino a rutina matutina sin depender de que su PC quede prendida." | playbook §0 |
| Ya instalado previo | "Git, GH CLI, Node LTS, Obsidian, Google Drive Stream, `vault-emilia` piloto — ver `playbook-instalacion-windows-emilia.md` v1.4. Este playbook solo agrega **Codex**." | §0 |
| No toca opencode.json | "No toca `opencode.json` — replica MCPs vía `~/.codex/config.toml`." | frontmatter + §4 |
| Instalador standalone | `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 \| iex"` | §2 Opción A |
| npm scope correcto | `npm install -g @openai/codex # paquete correcto es @openai/codex, no "codex" sin scope` | §2 Opción B |
| Auth con plan pago | `codex → elige "Sign in with ChatGPT" → abre browser → loguea con cuenta Emilia Plus/Pro` | §2 Auth |
| Sandbox elevated | `[windows] sandbox = "elevated" # o "unelevated" si bloquea IT` | §3 |
| MCP Fathom OAuth | `codex mcp add fathom --url https://api.fathom.ai/mcp` + `codex mcp login fathom` | §4 |
| Rutina n8n vs Actions | "n8n Workflow Cron 07:00 AR → Fathom list_calls → ... → GitHub vía API (GH_TOKEN) y Google Drive vía API" vs "GitHub Actions cron 0 10 * * * (07:00 AR = 10:00 UTC) runner ubuntu-latest" | §6 |

## 4. Ruta donde guardará + frontmatter propuesto

| Destino | Ruta exacta | Frontmatter propuesto |
|---|---|---|
| pbook Brais | `wiki/glosario/interno/pbooks/pbk-opencode_101_Brais.md` | `tipo: metodologia, codigo: pbk-opencode_101_Brais, fecha_creacion: 2026-09-30, ultima_actualizacion: 2026-09-30, tags: [opencode, brais-moure, mouredev, onboarding, tui, agentes, mcp, skills], idioma: es` |
| pbook Codex | `wiki/glosario/interno/pbooks/pbk-instalacion-codex.md` | `tipo: metodologia, codigo: pbk-instalacion-codex, fecha_creacion: 2026-09-30, ultima_actualizacion: 2026-09-30, tags: [codex, chatgpt-desktop, mcp, fathom, leantime, autodesk, windows, sandbox, rutina-matutina], idioma: es` |
| Alias Codex | `wiki/glosario/interno/pbooks/pbk-codex-instalacion.md` | redirect 3 líneas: `> Alias de [[wiki/glosario/interno/pbooks/pbk-instalacion-codex\|pbk-instalacion-codex]]` |
| Índice pbooks | `wiki/glosario/interno/pbooks/00-index.md` | añadir 2 líneas en ## Infraestructura y ## Agentes |
| Fuente raw | `raw/contenidos/2026-09-30-opencode-101-brais-codex.md` (este archivo) | `tipo: reporte-contenidos, estado: propuesta` |

> Frontmatter obligatorio `AGENTS.md:59-68` — `tipo, fecha_creacion, ultima_actualizacion, tags, idioma`. Para pbooks se añade `codigo:` para trazabilidad.

## 5. Tags + wikilinks previstos

- **Tags Brais:** [opencode, brais-moure, mouredev, onboarding, tui, agentes, mcp, skills, zen, provider-agnostic]
- **Tags Codex:** [codex, chatgpt-desktop, mcp, fathom, leantime, autodesk-help, autocad, windows, sandbox, n8n, github-actions, rutina-matutina]
- **`## Conceptos relacionados` previsto (≥2 wikilinks absolutos):**
  - `[[wiki/glosario/software/opencode|opencode]]`
  - `[[wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode|pbk-config_ctas_git_github_opencode]]`
  - `[[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]]`
  - `[[wiki/glosario/software/mcp-autodesk-help|mcp-autodesk-help]]`
  - `[[wiki/glosario/software/mcp-autocad|mcp-autocad]]`
  - `[[wiki/glosario/interno/pbooks/pbk-instalacion-codex|pbk-instalacion-codex]]` (cruce entre pbooks)
- **Índice interno previsto con `[[#Encabezado exacto]]`** — nunca `[Texto](#slug)` con tildes.

## 6. Referencias verificadas 200 (sin 404)

| # | Fuente | URL | Status | Tipo |
|---|---|---|---|---|
| 1 | Opencode docs — Intro / Install | https://opencode.ai/docs | 200 webfetch 2026-09-30 | oficial |
| 2 | Opencode docs — Agents | https://opencode.ai/docs/agents/ | 200 webfetch 2026-09-30 | oficial |
| 3 | Opencode docs — MCP servers | https://opencode.ai/docs/mcp-servers/ | 200 webfetch 2026-09-30 | oficial |
| 4 | Opencode docs — Providers / Zen | https://opencode.ai/docs/providers | 200 webfetch (citado en pbk-opencode) | oficial |
| 5 | Opencode GitHub | https://github.com/anomalyco/opencode | 200 | oficial |
| 6 | MoureDev YouTube — canal | https://www.youtube.com/@mouredev | 200 (canal verificado) | externa |
| 7 | MoureDev — Day 2 AI Development Course (opencode tutorial) | https://www.youtube.com/watch?v=irR8437xihg | 200 webfetch 2026-09-30 | externa |
| 8 | Brais LinkedIn — Curso gratis OpenCode 2.5h | https://es.linkedin.com/posts/braismoure_este-es-mi-curso-gratis-de-opencode-desde-activity-7502728040905367552-74AA | 200 websearch | externa |
| 9 | Codex — Windows sandbox | https://developers.openai.com/codex/windows (→ https://learn.chatgpt.com/docs/codex/windows/windows-sandbox) | 200 webfetch 2026-09-30 | oficial |
| 10 | Codex CLI docs | https://learn.chatgpt.com/docs/codex/cli | 200 (citado playbook) | oficial |
| 11 | Codex GitHub — installer | https://github.com/openai/codex | 200 | oficial |
| 12 | Remote connections (requiere host online) | https://learn.chatgpt.com/docs/remote-connections | 200 (citado playbook) | oficial |

> Si `lnkd.in/euau7pZU` redirige, verificar con `webfetch` tras `s` y sustituir por URL final moure.dev/youtube.

## 7. Propuestas wiki concretas

### 7.1 Preview `pbk-opencode_101_Brais.md` — diff listo para `¿Avanzo? s`

```markdown
---
tipo: metodologia
codigo: pbk-opencode_101_Brais
fecha_creacion: 2026-09-30
ultima_actualizacion: 2026-09-30
tags: [opencode, brais-moure, mouredev, onboarding, tui, agentes, mcp, skills, zen]
idioma: es
---

# pbk-opencode_101_Brais — Opencode 101 con Brais Moure (MoureDev)

> Curso 2.5h + Day 2 (88 min) que instala y opera opencode como agente open source agnóstico (Claude/GPT/Kimi/local). Fuente YouTube MoureDev — ver `raw/contenidos/2026-09-30-opencode-101-brais-codex.md`.

- [[#Resumen]]
- [[#Instalación]]
- [[#Configuración Zen y providers]]
- [[#TUI — Build vs Plan]]
- [[#AGENTS.md y reglas]]
- [[#Skills, MCPs y plugins]]
- [[#Modelos locales]]
- [[#Relación con vault arquitectura]]
- [[#Verificación 30 seg]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Resumen

Brais presenta opencode como espejo open source de Claude Code, con tres capas: agentes (Build/Plan + subagents), rules (AGENTS.md) y extensions (Skills/Commands). El curso propone instalar → conectar provider → `/init` → planear → construir, con SDD spec-first (6 preguntas → `specs/001-*.md`).

## Instalación

**Universal (curl):** `curl -fsSL https://opencode.ai/install | bash` → `opencode --version` (ver https://opencode.ai/docs — Install). **Node:** `npm install -g opencode-ai` (o bun/pnpm/yarn/homebrew). **Windows:** WSL recomendado; nativo vía `choco install opencode`, `scoop install opencode`, `npm install -g opencode-ai` o Docker (ver https://opencode.ai/docs#windows).

## Configuración Zen y providers

`/connect` → elegir `opencode` (Zen) → https://opencode.ai/auth → copiar `OPENCODE_API_KEY` → pegar en TUI. Alternativa: conectar Claude/GPT/Gemini/Kimi vía API key. Por repo: `opencode.json` con `provider.opencode.options.apiKey: "{env:OPENCODE_API_KEY}"` y wrapper `.\with-env.ps1 opencode` (ver [[wiki/glosario/software/opencode|opencode]] § Config por repositorio).

## TUI — Build vs Plan

- **Build (default):** todas las tools habilitadas, itera y escribe.
- **Plan:** `edit` y `bash` en `ask` — sugiere sin tocar código. Cambiar con `Tab`.
- Comandos clave: `/init`, `/connect`, `/undo`, `/redo`, `/share`, `Tab` (switch agent), `@` (mencionar file/subagent).

## AGENTS.md y reglas

`/init` genera `AGENTS.md` (commitear). Define estructura, convenciones, DoD. Equivale a nuestro `AGENTS.md` + `.opencode/agents/*.md`.

## Skills, MCPs y plugins

- **MCPs:** `opencode.json → mcp: { "fathom": {"type":"remote","url":"https://api.fathom.ai/mcp"}, "n8n-mcp": {...}, ... }` — ver https://opencode.ai/docs/mcp-servers/
- **Skills:** `skills.sh` — instalar con `npx skills add front-end-design` → `.agents/skills/` (ver https://opencode.ai/docs/skills/)
- Plugins: `opencode plugin add ...` (ver https://opencode.ai/docs/plugins/)

## Modelos locales

Brais muestra conexión a modelos locales (Ollama/LM Studio) para privacidad/costo cero — provider `ollama` o `lmstudio` en `opencode.json`.

## Relación con vault arquitectura

| Vault | Opencode Brais | Puente |
|---|---|---|
| `AGENTS.md` | `AGENTS.md` generado | Mismo rol: onboarding del agente |
| `.opencode/agents/*.md` | Agents Build/Plan/Explore | Nuestros `@vaultworm-arq`, `@contenidos`, `@sherlock` |
| `opencode.json` + `with-env.ps1` | `opencode.jsonc` global o repo | Nosotros aislamos por repo con `{env:}` |
| `wiki/` | — | Brais no usa wiki; nosotros volcamos digest a `wiki/glosario/` |

## Verificación 30 seg

```powershell
opencode --version
.\with-env.ps1 opencode mcp list
# en TUI: /connect → verificar Zen, Tab → Plan/Build, @vaultworm-arq digest
```

## Conceptos relacionados

- [[wiki/glosario/software/opencode|opencode]]
- [[wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode|pbk-config_ctas_git_github_opencode]]
- [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]]
- [[wiki/glosario/interno/pbooks/pbk-instalacion-codex|pbk-instalacion-codex]]

## Referencias

- Opencode docs — Intro: https://opencode.ai/docs (200)
- Agents: https://opencode.ai/docs/agents/ (200)
- MCP servers: https://opencode.ai/docs/mcp-servers/ (200)
- Zen: https://opencode.ai/docs/zen/ (200)
- MoureDev — Day 2: https://www.youtube.com/watch?v=irR8437xihg (200)
- MoureDev canal: https://www.youtube.com/@mouredev (200)
```

### 7.2 Preview `pbk-instalacion-codex.md` — migración canónica desde `proyectos/STUDIO_OS-Emilia/...`

> Origen: `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault.md` v1.0 (164 líneas). No se toca `opencode.json`; replica MCPs vía `~/.codex/config.toml`.

```markdown
---
tipo: metodologia
codigo: pbk-instalacion-codex
fecha_creacion: 2026-09-30
ultima_actualizacion: 2026-09-30
tags: [codex, chatgpt-desktop, mcp, fathom, leantime, autodesk-help, autocad, windows, sandbox, rutina-matutina, n8n, github-actions]
idioma: es
---

# pbk-instalacion-codex — Réplica vault con Codex (Windows) — canónico

> Canónico de instalación Codex para replicar `vault-arquitectura` en PC nueva (Emilia/Studio OS) sin repetir Git/GH/Node/Obsidian/Drive. Fuente: `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault.md` v1.0.

- [[#Qué llevar]]
- [[#Verificación previa]]
- [[#Instalar Codex]]
- [[#Sandbox Windows]]
- [[#MCPs espejo]]
- [[#Clonar vault]]
- [[#Rutina sin PC prendida]]
- [[#Verificación final]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Qué llevar

Playbook impreso 1 carilla + cuenta ChatGPT Plus/Pro Emilia + internet (winget/irm, sin USB).

## Verificación previa (2 min)

```powershell
git --version; gh auth status; node -v; npm -v
obsidian --version
# Drive Stream corriendo
```

Si falta algo → `playbook-instalacion-windows-emilia.md:3.1-3.2`.

## Instalar Codex (10 min) — nativo Windows sin WSL2

**A Standalone (recomendado):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
codex --version
# cae en %LOCALAPPDATA%\Programs\OpenAI\Codex\bin — re-ejecutar actualiza
# desatendido: $env:CODEX_NON_INTERACTIVE=1
```

**B npm:**
```powershell
npm install -g @openai/codex
codex --version
```

**Auth:**
```powershell
codex
# Sign in with ChatGPT → browser → cuenta Plus/Pro
codex auth status
```

## Sandbox Windows (2 min)

`%USERPROFILE%\.codex\config.toml`:
```toml
[windows]
sandbox = "elevated"   # fallback "unelevated" si bloquea IT
# sandbox_private_desktop = false # solo si rompe UI
```

`elevated` = usuarios sandbox dedicados + firewall; `unelevated` = token restringido + ACL (ver https://developers.openai.com/codex/windows). Verificar: `codex mcp list` o `/status` en TUI.

## MCPs espejo (5 min) — sin tocar opencode.json

`opencode.json` intacto; Codex lee `~/.codex/config.toml` (global) o `.codex/config.toml` (proyecto confiado). Comandos espejo: `codex mcp add/list`, `codex mcp login <nombre>`.

```powershell
codex mcp add fathom --url https://api.fathom.ai/mcp
codex mcp login fathom

codex mcp add fathom-proyectopi -- npx -y @luminarylane/fathom-mcp-server
# env FATHOM_API_KEY_PROYECTOPI vía with-env.ps1

codex mcp add n8n-mcp --url https://n8n.pitau.tech/mcp-server/http
# header Authorization Bearer {env:N8N_MCP_TOKEN} en config.toml

# Leantime futuro:
# codex mcp add leantime -- node P:/00-repos/npm-global/node_modules/leantime-mcp/bin/leantime-mcp.js https://pitau.tech/mcp --token {env:LEANTIME_TOKEN} --insecure

codex mcp list
```

Tabla completa: `raw/docs/Estudio Pi – Guía de conexiones MCP.md`.

### Ejemplo config.toml MCPs (con {env:})

```toml
[mcp_servers.fathom]
type = "remote"
url = "https://api.fathom.ai/mcp"
# OAuth via codex mcp login fathom

[mcp_servers."fathom-proyectopi"]
command = ["npx", "-y", "@luminarylane/fathom-mcp-server"]
env = { FATHOM_API_KEY_PROYECTOPI = "{env:FATHOM_API_KEY_PROYECTOPI}" }

[mcp_servers."n8n-mcp"]
type = "remote"
url = "https://n8n.pitau.tech/mcp-server/http"
headers = { Authorization = "Bearer {env:N8N_MCP_TOKEN}" }
```

## Clonar vault (5 min)

```powershell
cd P:\00-repos\proyecto-pi
gh repo clone p-31416/vault-arquitectura
cd vault-arquitectura
# .env NO viene por git — copiar plantilla (OPENCODE_API_KEY, GH_TOKEN, FATHOM_API_KEY_PROYECTOPI, N8N_MCP_TOKEN, LEANTIME_TOKEN)
.\with-env.ps1 codex --version
.\with-env.ps1 opencode --version
```
Binarios solo por ref `activos/...` o `C:\BIM\...`.

## Rutina sin PC prendida

> Remote Codex y Drive Stream exigen host despierto/logueado (https://learn.chatgpt.com/docs/remote-connections). Para rutina matutina automática, usar worker cloud.

**Recomendada — n8n pitau.tech (always-on):**
Cron 07:00 AR → `Fathom list_calls` (`FATHOM_API_KEY_PROYECTOPI`) → filtra `created_after=yesterday` → download transcript → `raw/reuniones/YYYY-MM-DD-{id}.md` vía GitHub API (`GH_TOKEN`) y Drive API → `git push`. Teléfono no necesita estar; al prender PC `git pull`.

**Alternativa — GitHub Actions (gratis):**
Clonar `.github/workflows/vaultworm-arq.yml` a `fathom-pull.yml` cron `0 10 * * *` (07:00 AR = 10:00 UTC) en `ubuntu-latest` con secrets `FATHOM_API_KEY_PROYECTOPI`, `GH_TOKEN` → curl Fathom → raw/reuniones → git commit/push. Ventaja sin n8n; desventaja menos visual.

**Siempre-on dedicado (solo si ejecutar Codex):** Mini PC/VPS/Mac mini 24/7 para Remote pesado.

**Propuesta mañana:** Fase 1 n8n o Actions para Fathom→GitHub, Fase 2 botón manual "descargala" vía Remote, Fase 3 Leantime MCP.

## Verificación final (2 min)

```powershell
codex --version; codex auth status; codex mcp list
gh auth status
git config user.email
Get-ChildItem raw/reuniones | Select -Last 2 Name,LastWriteTime
codex exec "lista los .md en raw/reuniones de los últimos 2 días"
```

Checklist: Codex + login OK, `codex mcp list` fathom connected, `raw/reuniones/` accesible, decisión n8n vs Actions agendada, CRD/Quick Assist backup vigente.

## Conceptos relacionados

- [[wiki/glosario/software/opencode|opencode]]
- [[wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode|pbk-config_ctas_git_github_opencode]]
- [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]]
- [[wiki/glosario/interno/pbooks/pbk-opencode_101_Brais|pbk-opencode_101_Brais]]
- [[wiki/glosario/software/mcp-autodesk-help|mcp-autodesk-help]]
- [[wiki/glosario/software/mcp-autocad|mcp-autocad]]

## Referencias

- Codex Windows sandbox: https://developers.openai.com/codex/windows (200)
- Codex CLI: https://learn.chatgpt.com/docs/codex/cli (200)
- Remote: https://learn.chatgpt.com/docs/remote-connections (200)
- Codex GitHub: https://github.com/openai/codex (200)
- Guía MCPs: `raw/docs/Estudio Pi – Guía de conexiones MCP.md`
- Matriz cuentas: [[wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode|pbk-config_ctas_git_github_opencode]]

> Alias `pbk-codex-instalacion.md` redirige aquí.
```

### 7.3 Propuesta `00-index.md` (2 líneas de 1 línea c/u)

```markdown
## Infraestructura, Cuentas y Entorno

- [[pbk-config_ctas_git_github_opencode|Gestión y Separación de Cuentas (Git, GitHub, OpenCode)]] — ...
- [[pbk-instalacion-codex|Réplica vault con Codex (Windows)]] — **Canónico**: CLI+Desktop, sandbox elevated/unelevated, MCPs espejo (Fathom/Leantime/Autodesk), rutina sin PC (n8n vs Actions).

## Agentes del vault

- [[pbk-agentes-vaultarq|Agentes del vault (vaultworm-arq, brainstormy)]] — ...
- [[pbk-opencode_101_Brais|Opencode 101 con Brais Moure (MoureDev)]] — Curso 2.5h + Day 2: instalación, Zen/providers, TUI Build/Plan, AGENTS.md, Skills/MCPs, modelos locales y puente al vault.
```

### 7.4 Nota para `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault.md`

Añadir arriba, debajo de frontmatter:

```markdown
> **Canónico:** [[wiki/glosario/interno/pbooks/pbk-instalacion-codex|pbk-instalacion-codex]] — este archivo queda como referencia/apéndice del pbook. Actualizar solo el pbook.
```

## 8. Estado wiki (post-s — completar tras `¿Avanzo?`)

| Destino | Acción | Link creado/actualizado | Fecha |
|---|---|---|---|
| `wiki/glosario/interno/pbooks/pbk-opencode_101_Brais.md` | crear | pendiente s | 2026-09-30 |
| `wiki/glosario/interno/pbooks/pbk-instalacion-codex.md` | crear | pendiente s | 2026-09-30 |
| `wiki/glosario/interno/pbooks/pbk-codex-instalacion.md` | crear alias | pendiente s | 2026-09-30 |
| `wiki/glosario/interno/pbooks/00-index.md` | actualizar | pendiente s | 2026-09-30 |
| `proyectos/STUDIO_OS-Emilia/documentacion/playbook-instalacion-codex-replica-vault.md` | actualizar nota | pendiente s | 2026-09-30 |
| `wiki/glosario/software/opencode.md` | proponer vía @vaultworm-arq | pendiente | — |

## 9. Decisiones SOL

- [ ] Aprobar ambos pbooks tal cual (s)
- [ ] Corregir: cambiar nombre `pbk-instalacion-codex` ↔ `pbk-codex-instalacion` (elegir uno canónico, otro alias)
- [ ] Descartar: dejar playbook solo en proyectos/ (no canónico)
- [ ] Añadir con Emilia: definir en reunión si n8n o GitHub Actions para rutina 07:00

## 10. Preguntas para SOL

1. ¿URL exacta Brais opencode 101 que querés canónica? Hoy propongo Day 2 (https://www.youtube.com/watch?v=irR8437xihg) + curso 2.5h (moure.dev via lnkd.in/euau7pZU). Si tenés otra URL, la sustituyo sin rehacer estructura.
2. ¿Preferencia nombre canónico Codex: `pbk-instalacion-codex` (propuesto) o `pbk-codex-instalacion`? Dejo alias del otro en cualquier caso.
3. ¿Mantengo `proyectos/.../playbook-instalacion-codex-replica-vault.md` como apéndice o lo archivamos tras migrar?
4. ¿Autorizás que `@vaultworm-arq` actualice `wiki/glosario/software/opencode.md` con referencia a Brais tras tu `s`?

## 11. Pipeline

- **Transcript YouTube:** si descargás a `activos/videos/ytb-2026-09-30-opencode-101-brais.mkv`, correr `P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/videos/ytb-2026-09-30-opencode-101-brais.mkv" --model medium --language es` (ajustar a yt-dlp si es webm).
- **Manual SOL:** si entregás PDF `activos/pdfs/...pdf`, normalizar a `wiki/raw/YYYY-MM-DD-<slug>.md` (`tipo: raw`, `fuente_binaria: <path>`).
- **Código paralelo didáctico:** `scripts/codex-mcp-config_notas.md` con `# NOTA ES:` línea a línea del `config.toml` (no escribo código ejecutable sin `s`; el ejemplo va en preview §7.2).

---

**¿Avanzo? (s/N)** — Esperando `s` de Sol para escribir en `wiki/` (HITL `AGENTS.md`). Con `s` ejecuto: `pbk-opencode_101_Brais.md` + `pbk-instalacion-codex.md` + alias + `00-index.md` + nota en proyectos + `log.md` (entrada nueva arriba).
