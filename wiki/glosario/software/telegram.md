---
tipo: software
software: telegram
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, software, telegram, bot, digest]
idioma: es
---

# telegram

> Bot API para envío del digest (PDF) + feedback loop con Emilia — `vaultworm_arqbot`.

- [BotFather y token](#botfather-y-token)
- [sendDocument](#senddocument)
- [vaultworm_arqbot — flujo digest](#vaultworm_arqbot--flujo-digest)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## BotFather y token

Crear el bot con `@BotFather` → `/newbot` → token `123456:ABC...`. El token es secreto total: vive en `.env` (`TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` placeholders) y se inyecta vía `{env:TELEGRAM_BOT_TOKEN}` — nunca hardcodear. Quien tiene el token controla el bot.

## sendDocument

```bash
curl -F document=@digest.pdf \
     -F chat_id="$TELEGRAM_CHAT_ID" \
     -F caption="vaultworm-arq digest $(date +%F)" \
     "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendDocument"
```

Límite 50 MB por archivo, `multipart/form-data`. Soporta `reply_markup` con inline keyboard (✅ aprobar / ✏️ corregir / ❌ descartar) para el feedback loop del digest.

## vaultworm_arqbot — flujo digest

Bot del grupo con Emilia: recibe el PDF del digest (`pandoc` → `sendDocument`), Junta ✅/✏️/❌, y la respuesta decide si `@vaultworm-arq avanza` escribe en `wiki/`. Plan completo bot → vault en `specs/260907-telegram-vault.md`. Ejecución online (PC apagada): ver `specs/260909-github-actions-agentes-online.md`. Túnel local n8n/ngrok descartado como infra efímera (decisión SOL 2026-09-09).

## Conceptos relacionados

- [[wiki/glosario/software/pandoc|pandoc]]
- [[wiki/glosario/software/n8n|n8n]]
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]

## Referencias

- Bot API `sendDocument`: https://core.telegram.org/bots/api#senddocument (verificado 2026-09-08 — 200)
- Intro bots para devs (BotFather, token, privacy): https://core.telegram.org/bots (verificado 2026-09-09 — 200)
