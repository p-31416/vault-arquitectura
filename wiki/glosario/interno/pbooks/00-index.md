---
tipo: indice
seccion: playbooks-internos
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-10-30
tags: [playbooks, infra, comfyui, tim, git, github, opencode, setup, vps, ssh, monitoreo, contabo]
---

# Playbooks Internos del Estudio

Colección de guías operativas y procedimientos técnicos para el día a día del estudio.

## Infraestructura, VPS y Cuentas

- [[pbk-vps-acceso-monitoreo|Acceso SSH y monitoreo del VPS]] — **Canónico**: SSH `contabo`, 3 capas de monitoreo (UptimeRobot + n8n + manual), portabilidad a otros VPS/usuarios.
- [[pbk-alertas-contabo|Alertas de seguridad de Contabo]] — **Canónico**: flujo de respuesta a mails de Contabo (kernel CVE, PHP RCE, outage), verificación y registro.
- [[pbk-config_ctas_git_github_opencode|Gestión y Separación de Cuentas (Git, GitHub, OpenCode)]] — Matriz de identidades, rutas de credenciales, archivos de configuración, verificación en 30 seg y conexión/desconexión de proveedores IA.
- [[pbk-instalacion-codex|Réplica vault con Codex (Windows)]] — **Canónico**: CLI+Desktop, sandbox elevated/unelevated, MCPs espejo (Fathom/Leantime/Autodesk/AutoCAD), rutina sin PC (n8n vs Actions). Ref Brais Codex 101.
- [[pbk-opencode-linux|Vault con OpenCode en Linux (terminal)]] — **2026-11-02**: install v2, auth Console (ex-Zen) con otra cuenta, clon del vault, modo plan solo-lectura, qué viaja y qué queda en la PC principal.

## PM y gestión del estudio

- [[pbk-pm_vault|PM + Lean + Agile en el vault (Leantime)]] — **Canónico**: Goals/Milestones/Sprints, Kanban+LPS diario, rituales, convenciones, MCP Leantime.

## Agentes del vault

- [[pbk-agentes-vaultarq|Agentes del vault (vaultworm-arq, brainstormy)]] — Qué son, qué hacen, cómo están configurados, triggers, invocación y cómo agregar uno nuevo.
- [[pbk-codex_101_Brais|Codex 101 con Brais Moure (MoureDev)]] — **2026-09-30**: Curso Codex + GPT-5.6 (Sol/Terra/Luna): instalación, auth ChatGPT, CLI vs Desktop/IDE/Cloud, AGENTS.md, MCPs, skills y puente al vault. Fuente https://www.youtube.com/watch?v=af1KAQCD7mk

## ComfyUI y Generación IA

- [[pbk-comfyui|ComfyUI para el estudio]] — **Canónico UNICO**: mapa de flujos (txt2img/img2img/Canny/Depth/Upscale/Video/RunPod), RX 570 vs RunPod, prompt-packs, DoD.
- [[pbk-comfy-agent|Playbook del agente @tim]] — **2026-10-30**: manual de invocación, checklist pre-`s` de 4 puntos, recetario por 6 tipologías, constantes de fotografía (Baan · IQ4 · 6 hex · stock) y ciclo con la bitácora `04-bitacora-corridas`.
- [[pbk-troubleshooting-reconexion|Troubleshooting & Reconexión MCP]] — Checklist completa: ComfyUI caído, cola atascada, MCP desconectado, modelos no aparecen, VRAM full, reconexión paso a paso, escalación.

---

## En preparación

- Setup inicial (Desktop App vs Manual vs Cloud)
- Gestión de modelos (licencias, descarga, versionado)
- Pipeline trabajo: prompt → render → upscale → entrega
- Entrenamiento LoRA personaje/estilo
- RunPod: deploy, connect, train, download