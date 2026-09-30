---
tipo: metodologia
codigo: pbk-codex_101_Brais
fecha_creacion: 2026-09-30
ultima_actualizacion: 2026-09-30
tags: [codex, brais-moure, mouredev, codex-cli, chatgpt-desktop, gpt-5-6, mcp, agents-md, skills, onboarding]
idioma: es
---

# pbk-codex_101_Brais — Codex 101 con Brais Moure (MoureDev) — Codex CLI + GPT-5.6

> Curso gratis Codex desde cero por Brais Moure (MoureDev) — editor agéntico oficial de OpenAI con GPT-5.6 (Sol, Terra y Luna). Fuente: https://www.youtube.com/watch?v=af1KAQCD7mk — ver `raw/contenidos/2026-09-30-codex-101-brais.md`. Corrige reporte previo que asumía opencode.

- [[#Resumen]]
- [[#Instalación]]
- [[#Auth — Sign in with ChatGPT]]
- [[#CLI vs Desktop vs IDE vs Cloud]]
- [[#AGENTS.md y reglas]]
- [[#MCPs]]
- [[#Skills y plugins]]
- [[#Modelos GPT-5.6 — Sol Terra Luna]]
- [[#Relación con vault arquitectura]]
- [[#Verificación 30 seg]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Resumen

Brais presenta Codex como agente de código local de OpenAI que inspecciona, edita y ejecuta tu repo desde terminal/IDE/Desktop. El curso cubre instalación (install.sh / install.ps1 / npm / brew), autenticación con cuenta ChatGPT Plus/Pro, creación de `AGENTS.md`, uso de MCPs y skills, y construcción de proyectos reales con GPT-5.6.

## Instalación

**Universal Mac/Linux:** `curl -fsSL https://chatgpt.com/codex/install.sh | sh` → `codex --version` (https://github.com/openai/codex).
**Windows:** `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"` → `codex --version` (cae en `%LOCALAPPDATA%\Programs\OpenAI\Codex\bin`).
**npm:** `npm install -g @openai/codex` — paquete scopeado correcto es `@openai/codex`, no `codex` sin scope.
**Homebrew:** `brew install --cask codex`.

> Ver Brais Codex 101 para demo en vivo de install.ps1 + Sign in with ChatGPT: https://www.youtube.com/watch?v=af1KAQCD7mk

## Auth — Sign in with ChatGPT

```powershell
codex
# elige "Sign in with ChatGPT" → abre browser → loguea con cuenta Plus/Pro/Business/Edu/Enterprise
codex auth status
```

Recomendado por OpenAI para usar tu plan ChatGPT. Alternativa API key requiere setup adicional (https://developers.openai.com/codex/auth).

## CLI vs Desktop vs IDE vs Cloud

| Superficie | Cuándo usar | Comando / ruta |
|---|---|---|
| CLI | Trabajo en terminal, scripts, CI (`codex exec`) | `codex` en repo |
| IDE extension | VS Code / Cursor / Windsurf junto al código | instalar desde https://developers.openai.com/codex/ide |
| Desktop app | Proyectos + tareas largas + archivos locales | `codex app` o https://chatgpt.com/codex?app-landing-page=true |
| Cloud/Web | Trabajo remoto sin instalación | https://chatgpt.com/codex (Codex Web) |

Todo comparte `AGENTS.md` y MCPs.

## AGENTS.md y reglas

`/init` o `codex init` genera `AGENTS.md` en raíz — commitear. Define estructura, convenciones, DoD. Equivale a nuestro `AGENTS.md` + `.opencode/agents/*.md`. Brais lo muestra como segunda capa (agents → rules → extensions).

## MCPs

`codex mcp add/list/login` — espejo de `opencode.json` pero en `~/.codex/config.toml` (global) o `.codex/config.toml` (proyecto confiado).

```powershell
codex mcp add fathom --url https://api.fathom.ai/mcp
codex mcp login fathom
codex mcp add autocad -- P:/00-repos/proyecto-pi/tools/autocad-mcp/.venv/Scripts/autocad-mcp.exe
codex mcp list
```

Ver `raw/docs/Estudio Pi – Guía de conexiones MCP.md` para tabla completa (Fathom, n8n, Leantime, Autodesk).

## Skills y plugins

"Package repeatable instructions as skills, then add plugins to connect Codex to your team's tools" — https://developers.openai.com/codex/cli

- Skills: playbooks reutilizables (ver https://developers.openai.com/codex/skills-and-plugins)
- Plugins: `codex plugin add ...` + MCP servers

## Modelos GPT-5.6 — Sol Terra Luna

Brais trabaja con GPT-5.6 en tres variantes: **Sol, Terra y Luna** (nombradas en LinkedIn 2026-09-06). Selección con `/model` en TUI o `codex --model gpt-5.6-sol`. GPT-5.6 Sol luce como frontier model con modo Ultra (budget extendido, consumo mayor).

## Relación con vault arquitectura

| Vault | Codex Brais | Puente |
|---|---|---|
| `AGENTS.md` | `AGENTS.md` generado | Mismo onboarding de agente |
| `.opencode/agents/*.md` | Skills + subagents Codex | Nuestros `@vaultworm-arq`, `@contenidos`, `@sherlock` mapean a skills/subagents |
| `opencode.json` + `with-env.ps1` | `~/.codex/config.toml` + `{env:}` | Nosotros aislamos por repo; Codex por global/proyecto confiado |
| `wiki/` + `raw/` | — | Brais no usa wiki; nosotros volcamos a `wiki/glosario/` + `raw/reuniones/` |

## Verificación 30 seg

```powershell
codex --version; codex auth status; codex mcp list
# en TUI: /model → Sol/Terra/Luna, /status, /permissions
```

## Conceptos relacionados

- [[wiki/glosario/software/codex|codex]]
- [[wiki/glosario/interno/pbooks/pbk-instalacion-codex|pbk-instalacion-codex]]
- [[wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode|pbk-config_ctas_git_github_opencode]]
- [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]]
- [[wiki/glosario/software/mcp-autodesk-help|mcp-autodesk-help]]
- [[wiki/glosario/software/mcp-autocad|mcp-autocad]]

## Referencias

- Brais Moure — Codex + GPT-5.6: https://www.youtube.com/watch?v=af1KAQCD7mk (200)
- Brais LinkedIn Codex desde cero: https://es.linkedin.com/posts/braismoure_este-es-mi-curso-gratis-de-codex-desde-cero-activity-7502365507103203328-POAX (200)
- Codex GitHub: https://github.com/openai/codex (200)
- Codex CLI docs: https://developers.openai.com/codex/cli (200)
- Codex Quickstart: https://developers.openai.com/codex/quickstart (200)
- Codex IDE: https://developers.openai.com/codex/ide (200)
- MoureDev canal: https://www.youtube.com/@mouredev (200)
