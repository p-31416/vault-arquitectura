---
tipo: software
software: n8n
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, software, n8n, webhook, telegram, automatizacion]
idioma: es
---

# n8n

> Automatización fair-code con nodos — integración futura `Telegram Trigger` + `Webhook` para el vault (no activo hoy).

- [Webhook y Telegram Trigger](#webhook-y-telegram-trigger)
- [setWebhook y polling](#setwebhook-y-polling)
- [Integración futuro vaultworm-arq](#integración-futuro-vaultworm-arq)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Webhook y Telegram Trigger

n8n conecta apps sin código custom: trigger (`Telegram Trigger`, `Webhook`, `Schedule`) → acciones (nodos `Telegram`: sendMessage, sendDocument, sendPhoto…). El nodo Telegram soporta chat/callback/file/message (get, send, edit, pin, delete). Credencial: token del bot (igual que en [[wiki/glosario/software/telegram|telegram]]).

## setWebhook y polling

Telegram entrega updates por **webhook** (requiere HTTPS público → `setWebhook?url=...`) o **polling** (`getUpdates`, 0 config, ideal local). Futuro del vault: `getUpdates` → ruta `/vaultworm` → issue/commit → `@vaultworm-arq avanza`.

## Integración futuro vaultworm-arq

Estado: **no activo**. El camino elegido para ejecución online es GitHub Actions (ver `specs/260909-github-actions-agentes-online.md`), no n8n. El plan de túnel local (`sjanaX01/n8n-Telegram-Bot-Webhook` + `ngrok`) quedó descartado como infra efímera (decisión SOL 2026-09-09). n8n queda como integración futura si el vault necesita workflows multi-app (Telegram + Sheets + Drive). Nota API: un solo `Telegram Trigger` activo por bot a la vez (limitación Telegram).

## Conceptos relacionados

- [[wiki/glosario/software/telegram|telegram]]
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]

## Referencias

- Nodo Telegram (oficial): https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/ (verificado 2026-09-08 — 200)
- Integración Webhook + Telegram (acciones soportadas, triggers): https://n8n.io/integrations/webhook/and/telegram/ (verificado 2026-09-09 — 200)
