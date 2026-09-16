---
tipo: metodologia
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-07
tags: [telegram, bot, vault, ingest, raw, automatizacion, studio-os]
origen: analisis telegram con Emilia — supergrupo foro + bot volcado a raw/telegram/
estado: plan
---

# Plan — Bot Telegram → Vault (raw/telegram/)

> **Objetivo:** Toda conversación con Emilia (diseño, obra, admin) queda en el vault sin copiar/pegar. Vos hablás en Telegram, el bot vuelca a `raw/telegram/` por día y tema, y un job marca tareas pendientes y qué interactuamos.

## 0. Resumen en 1 línea

Supergrupo Foro `Studio OS — Emilia` (4 topics) + `@StudioOSBot` (privacy off) → webhook/polling → `raw/telegram/YYYY-MM-DD.md` (separado por `## #topic`) → job nocturno extrae `→ [ ]` tareas → `proyectos/STUDIO_OS-Emilia/reuniones/` + `wiki/`.

## 1. Por qué Telegram Foro y no Canal/Grupo simple

| Opción | Temas? | Uso para Emilia |
|---|---|---|
| **Canal** | No | Solo broadcast admin → no sirve para conversar obra/diseño |
| **Grupo normal** | No | 1 chat único, se mezclan obra + diseño + admin |
| **Supergrupo Foro (Topics)** | **Sí** | 1 grupo, 4 pestañas: `General`, `Diseño`, `Obra Balcarce`, `Admin`. Cada mensaje trae `message_thread_id` → separación automática |

**Decisión:** Supergrupo Foro. Un grupo, 4 topics. Si crece → añadir topic por obra (`Obra Palermo`, `Obra Caballito`) sin crear grupos nuevos.

## 2. Arquitectura (100% libre, sin licencia)

```
[Telegram — Supergrupo Foro Studio OS - Emilia]
   ├─ topic 1 General (thread_id 1)
   ├─ topic 2 Diseño
   ├─ topic 3 Obra Balcarce
   └─ topic 4 Admin
         │  Bot API (getUpdates polling o webhook)
         ↓
[Bot @StudioOSBot — python-telegram-bot, privacy disabled]
   token en .env TELEGRAM_BOT_TOKEN= (gitignored, .gitignore:22)
   host: tu PC (comfyenv) via polling (0 config) ó webhook via Tailscale/Cloudflare Tunnel
         │
         ├─→ Guarda binarios: foto/documento → activos/proyectos/emilia-<obra>/fotos/YYYY-MM-DD-HHMM.jpg
         └─→ Append raw: raw/telegram/YYYY-MM-DD.md  (1 archivo/día, por tema)
               │
               └─→ Job nocturno 22:00 (scripts/telegram-ingest.py + Ollama qwen2.5:7b local)
                     ├─ Extrae tareas → - [ ] Revisar fisura PB (de #obra-balcarce 09:12)
                     ├─ Clasifica tema → ya viene del thread_id
                     └─ Propone: proyectos/STUDIO_OS-Emilia/reuniones/YYYY-MM-DD-<tema>.md + wiki/...
```

**Polling vs Webhook:**
- **Polling (recomendado inicio):** `bot.run_polling()` — 0 config red, el bot pregunta a Telegram cada 2s. Funciona detrás de NAT, sin abrir puerto. Suficiente para 2-4 personas.
- **Webhook:** `https://tu-tailscale.ts.net/telegram/webhook` — instantáneo, necesita Tailscale/Cloudflare Tunnel ya previsto en `04-plan-studio-os.md`. Migrar cuando quieras latencia <1s.

## 3. Estructura raw/telegram/ (evidencia, no se edita)

**1 archivo por día (recomendado para estudio chico):**

```markdown
raw/telegram/2026-09-07.md
---
tipo: raw
fuente: telegram
chat: Studio OS - Emilia (Supergrupo Foro, 4 topics)
chat_id: -1001234567890
fecha: 2026-09-07
topics: [general, diseno, obra-balcarce, admin]
---

## 09:12 — #obra-balcarce — Emilia Pimenta
Se fisuró el revoque en PB, ver detalle
→ media: [activos/proyectos/emilia-balcarce/fotos/2026-09-07-0912-fisura.jpg]

## 09:15 — #obra-balcarce — SOL
¿Tenés foto del encuentro losa-muro?

## 14:30 — #diseno — SOL
Te paso 2 variantes ComfyUI del croquis PB
→ media: [activos/proyectos/emilia-balcarce/renders/2026-09-07-variantes.zip]

## 16:00 — #admin — Emilia
Pendiente honorarios etapa 1 — ¿facturamos 50%?
→ tarea: [ ] Definir facturación etapa 1

---
_Append-only. Cada mensaje nuevo hace append con timestamp y topic._
```

**Alternativa 1 archivo por tema/día:** `raw/telegram/2026-09-07/obra-balcarce.md` — misma data, más archivos. Cambiable con flag `SPLIT_BY_TOPIC=1`.

**Frontmatter obligatorio:** `tipo: raw`, `fuente: telegram`, `chat`, `fecha`, `topics`. Binarios nunca en `raw/`, solo refs a `activos/` (regla `AGENTS.md: Prioridad máxima`).

## 4. Qué guarda el bot (raw) y qué extrae el job (procesado)

| Capa | Qué hace | Dónde | Cuándo |
|---|---|---|---|
| **Raw (bot)** | Append verbatim + timestamp + topic + media ref | `raw/telegram/YYYY-MM-DD.md` | En cada mensaje (segundos) |
| **Tareas (job)** | Detecta `TODO|pendiente|revisar|facturar|fisura` + LLM local → `→ tarea: [ ] ...` inline + propone `proyectos/.../reuniones/YYYY-MM-DD-<tema>.md` | Mismo raw (inline) + nuevo .md en `proyectos/` | 22:00 o `/resumen` |
| **Temas (job)** | Ya separado por `## #topic` — no hay que clasificar con IA | — | — |
| **Interacción (job)** | Cuenta `quién habló / qué respondió / fotos / archivos` → tabla al pie del día | Pie de `raw/telegram/YYYY-MM-DD.md` o `proyectos/.../reuniones/` | 22:00 |

**Ejemplo tareas extraídas:**
```markdown
## Tareas detectadas (auto 2026-09-07 22:00)
- [ ] Revisar fisura PB — origen: #obra-balcarce 09:12 Emilia — foto: activos/.../2026-09-07-0912.jpg
- [ ] Facturar 50% etapa 1 — origen: #admin 16:00 Emilia
→ Crear: [[proyectos/STUDIO_OS-Emilia/reuniones/2026-09-07-obra-balcarce]]
```

## 5. Comandos del bot (opcional, útil)

- `/resumen` — dispara job inmediato para ese día (no esperar 22:00)
- `/tareas` — lista tareas pendientes del día/semana
- `/vault` — link a `raw/telegram/YYYY-MM-DD.md` del día

Todos funcionan por topic: si escribís `/resumen` en `#obra-balcarce`, solo resume ese topic.

## 6. Seguridad y privacidad

- Token en `.env` `TELEGRAM_BOT_TOKEN=123456:ABC...` — gitignored, nunca en `raw/` ni `wiki/`
- Bot en `privacy disabled` (BotFather → `/setprivacy` → Disable) para leer todos los topics, no solo comandos
- `raw/telegram/` es evidencia interna — no redistribuir, igual que `wiki/raw/` de GHL
- Fotos sensibles (planos legales) → `activos/` con ref, no se suben a nube Telegram más allá de lo que ya hace Telegram (cifrado en tránsito, no E2E en grupos)

## 7. Implementación paso a paso (HOY, 45 min)

### 7.1 Telegram (5 min, vos)
1. Crear Supergrupo `Studio OS — Emilia` → `⋮ → Convertir en foro` → Crear topics: `General`, `Diseño`, `Obra Balcarce`, `Admin`
2. Invitar a Emilia + junior
3. `@BotFather` → `/newbot` → nombre `StudioOSBot` → copiar token → pegar en `P:\00-repos\proyecto-pi\vault-arquitectura\.env` como `TELEGRAM_BOT_TOKEN=...`
4. `/setprivacy` → Disable (para que lea topics)

### 7.2 Bot base (15 min, yo)
- `scripts/telegram-bot/bot.py` — `python-telegram-bot` polling, append a `raw/telegram/YYYY-MM-DD.md`, guarda media a `activos/`
- `scripts/telegram-bot/requirements.txt` — `python-telegram-bot==21.*`
- `scripts/telegram-bot/.env.example` — plantilla

### 7.3 Prueba (5 min)
- Escribir en `#obra-balcarce` una foto + "fisura PB" → verificar `raw/telegram/2026-09-07.md` aparece con `## 09:12 — #obra-balcarce` + ref a `activos/...jpg`

### 7.4 Job tareas (20 min, siguiente iteración)
- `scripts/telegram-ingest.py` — lee `raw/telegram/YYYY-MM-DD.md` → regex + Ollama `qwen2.5:7b` (local, libre) → append `→ tarea: [ ]` + propone `proyectos/STUDIO_OS-Emilia/reuniones/YYYY-MM-DD-<tema>.md`
- Cron: `22:00` o manual `/resumen`

## 8. Costos y licencias

- Telegram Bot API: $0, sin límite, sin licencia
- `python-telegram-bot`: GPL/MIT, $0
- Ollama + qwen2.5: MIT, local, $0 (opcional, si querés extracción IA; si no, solo regex)
- Polling: $0, sin dominio ni servidor

## 9. Qué NO hacer

- No usar Canal para conversar — no tiene topics
- No copiar binarios a `raw/` — solo refs a `activos/` (regla `AGENTS.md`)
- No editar `raw/telegram/*.md` a mano — append-only. Lo procesado va a `proyectos/` y `wiki/`
- No guardar token en `wiki/` ni `raw/` — solo `.env`

## 10. Próximo paso

¿Avanzamos con `scripts/telegram-bot/bot.py` (polling) + `raw/telegram/` + `wiki/glosario/interno/pbooks/pbk-telegram-ingest.md`? Con eso probás hoy mismo con Emilia en `#obra-balcarce`.

---
*Referencias vault:* [[proyectos/STUDIO_OS-Emilia/00-index]] · [[proyectos/STUDIO_OS-Emilia/04-plan-studio-os]] · [[wiki/glosario/software/obs|obs]] · [[AGENTS.md]] · [[wiki/glosario/interno/00-index]]
