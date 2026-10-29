---
tipo: software
software: n8n
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-10-22
tags: [glosario, software, n8n, webhook, telegram, automatizacion, vps, monitoreo]
idioma: es
---

# n8n

> Automatización fair-code self-hosted en el VPS Contabo — **activo con 10 workflows en producción** (verificado 2026-10-22).

- [[Estado actual]]
- [[Arquitectura]]
- [[Workflows]]
- [[Monitoreo y alertas]]
- [[Conceptos relacionados]]
- [[Referencias]]

## Estado actual

**Activo desde 2026-09-24** en el VPS Contabo (`n8n.pitau.tech`). Instancia única compartida por vault-arquitectura y vault-lidia.

| Dato | Valor |
|------|-------|
| URL | `https://n8n.pitau.tech` |
| Instalación | Docker Swarm (servicio `pitautech_n8n`) en EasyPanel |
| Imagen | `n8nio/n8n:latest` |
| MCP | `https://n8n.pitau.tech/mcp-server/http` (Bearer `N8N_MCP_TOKEN`) |
| Credenciales | Gmail OAuth2, Telegram `emiliaospi_bot`, Fathom, Google Drive/Docs/Sheets, Cal.com, OpenRouter, Redis, Postgres, Gemini |

## Arquitectura

- **1 trigger de Telegram por token** (regla de oro — un segundo trigger le roba el webhook al Router)
- Los sub-flujos (agente de voz, agenda) se invocan vía `ExecuteWorkflowTrigger`, no con trigger propio
- **Workflows nuevos solo usan Telegram `sendMessage`** (output) para alertas — nunca `Telegram Trigger` (input) para no interferir
- Postgres y Redis corren como contenedores separados en el VPS

## Workflows

Mapa completo nodo por nodo: [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura-n8n-os-emilia]]

| Workflow | ID | Trigger |
|----------|-----|---------|
| Fathom Core | `UeDkqVZSeLnae5cF` | Schedule 07:00 |
| Telegram Router | `YWpuV5p0vCDTbIHz` | Telegram Trigger |
| Voz Dispatcher | `Msh31moofBKBwZId` | ExecuteWorkflowTrigger |
| Agent Voz TEST | `Gpd6NHB4HQdU7ary` | ExecuteWorkflowTrigger |
| Agent Voz Emilia | `Fa2AlIDqUntSWMrw` | ExecuteWorkflowTrigger |
| Agenda Sub TEST | `ygdjqRfXpxKMFWEN` | ExecuteWorkflowTrigger |
| Agenda Sub Emilia | `2JogeOoT3Wjq2ncH` | ExecuteWorkflowTrigger |
| SET_01 Cuadro carpinterías | `VIQmMEZ9tkDBfKjd` | Webhook |
| Limpiar Memoria TEST | `uOonS1LWzowvwyns` | Manual (inactivo) |

## Monitoreo y alertas

- **Workflow salud VPS** (schedule 5 min): chequea HTTP de n8n y Leantime → Telegram a Sol si falla
- **Workflow ingest Contabo** (Gmail trigger): filtra mails de seguridad Contabo → Telegram + log Sheets
- **UptimeRobot** (externo): monitorea `n8n.pitau.tech` cada 5 min, alerta por Telegram cuando el host cae — complementa al workflow que corre en el propio VPS
- Ver: [[wiki/glosario/interno/pbooks/pbk-vps-acceso-monitoreo|pbk-vps-acceso-monitoreo]]

## Conceptos relacionados

- [[wiki/glosario/software/telegram|telegram]]
- [[wiki/glosario/software/leantime|leantime]]
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]

## Referencias

- Documentación oficial: https://docs.n8n.io/ (verificado 2026-10-22 — 200)
- Nodo Telegram: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/
- MCP server: https://docs.n8n.io/advanced-ai/mcp/ (verificado 2026-10-22 — 200)
- Arquitectura detallada: [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia]]
