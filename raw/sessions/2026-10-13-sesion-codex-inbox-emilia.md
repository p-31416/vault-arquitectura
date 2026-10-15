---
tipo: log
fecha: 2026-10-13
tags: [sesion, youtube, codex, mouredev, emilia, inbox, telegram, n8n, spec]
---

# Sesión 2026-10-13 — Transcript Codex MoureDev + inbox Fuentes Emilia

## Qué se hizo

1. **Transcript video MoureDev** `af1KAQCD7mk` ("Codex + GPT-5.6") → `raw/yt/transcripts/2026-10-13_af1KAQCD7mk.es.*` (4 archivos, fuente `auto-sub`, 9352 cues).
2. **Fix `scripts/transcribir_youtube.py`** (2 bugs): clave `writeautomaticsubs` → `writeautomaticsub` (singular, la plural se ignora en silencio); intentos por idioma (un 429 en `en` no descarta el `es`).
3. **Análisis Codex para Emilia** (no-técnica, Plus): veredicto — Codex IDE directo no; Plus como puerta (Work, tareas, plugins) + equipo técnico en Codex, sí.
4. **Share ChatGPT "Evaluación gráfica"** recuperado vía lector (r.jina.ai): 2 mensajes Emilia (prompt eficiente + comparativa 10-15 plantas, 6 atributos).
5. **Plan colaboración Emilia** (7 micro-pantallas, terminal sin scroll) → aprobado.
6. **Spec** `specs/261013-plan-fuentes-emilia-inbox.md` (sheet, clasificador, rutina 07:00, puentes GPT, cortes).
7. **Rama inbox en Router** `YWpuV5p0vCDTbIHz` (14 nodos): Route Fuentes Group → Has Link → Append Sheet → Ack. Sin IA. Placeholders: `FUENTES_CHAT_ID=0`, `documentId` dummy (publish lo exige).
8. **Debug grupo os.emi-fuentes**: grupo mudo (ni links ni /help llegan); privado OK tras republicar Router (mi edición había tumbado el webhook — mea culpa, republicado y verificado exec 3644). Pendiente: obtener `chat_id` real del grupo + crear Sheet.

## Archivos modificados

- `scripts/transcribir_youtube.py` (fix singular + loop por idioma)
- `specs/261013-plan-fuentes-emilia-inbox.md` (nuevo, +§9 rama inbox)
- n8n Router `YWpuV5p0vCDTbIHz` (v Activa `a2a511f2`; ramas inbox + republicación)
- `raw/yt/transcripts/2026-10-13_af1KAQCD7mk.es.{md,srt,txt,origen.json}` (nuevo)

## Pendiente retomar

1. Grupo os.emi-fuentes mudo: verificar privacy BotFather OFF + bot admin + que sea grupo real; mandar link → leer `chat_id` → setear regla.
2. Crear Sheet "Fuentes-Inbox" (encabezado A1:I1 entregado) → pegar `documentId` real.
3. Rutina 07:00 + digest (corte 1 pendiente).
4. Doc oficial Drive en ChatGPT verificado 200: `help.openai.com/en/articles/10929079`.

## Cerebro-digital

- Topics: transcript-autosub-yt, codex-plus-no-tecnicos, inbox-fuentes, router-n8n-schedued-vs-webhook, group-privacy-telegram.
- Entidades: MoureDev/Codex GPT-5.6, emiliaospi_bot, grupo os.emi-fuentes, Sheet Fuentes-Inbox, Router YWpuV5p0vCDTbIHz.
- Hechos: `writeautomaticsub` singular es la clave real (no `writesubtitles`); publish n8n valida `documentId` no-vacío; update vía API puede tumbar webhook (republicar); descripción BotFather ≠ respuesta del bot (confusión usuario).
