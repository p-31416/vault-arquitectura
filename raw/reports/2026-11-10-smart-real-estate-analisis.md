# Análisis — Smart Real Estate mkt, scrapping, leads, agenda
Fecha: 2026-11-10
Workflow: `ZRDZCTdQR2lqRT75` — https://n8n.pitau.tech/workflow/ZRDZCTdQR2lqRT75
Estado: inactivo (deprecado), 132 nodos (94 funcionales + 38 stickies), 0 triggers activos
Origen: creado 2026-03-21, última edición 2026-04-05

> Objetivo: rescatar ideas y patrones útiles para re-implementar en stack actual (LidIA V5.0, OS-Emilia, OS-Studio). Este documento es borrador para leer, ajustar y seguir.

---

## 1. Diagnóstico general

No es 1 flujo, es **mega-pegado de 6-7 plantillas community** de n8n.io en un mismo canvas, desconectadas entre sí. Por eso `triggerCount: 0` y ~70 entradas en `connections`.

Valor alto como banco de ideas. Valor bajo como código ejecutable directo. Recomendación: desguazar, no revivir tal cual.

---

## 2. Inventario por bloques

### 2.1 Triggers / Entradas — 11 puntos

- `When clicking Execute workflow` (manualTrigger v1) — test scraping immobiliare
- `On form submission` (formTrigger v2.2) — lead scoring simple
- `0. Form Trigger Property Tour Request` (formTrigger v1) — Full Name, Email, Phone, Interested Property ID
- `Webhook chatbot-webhook` (webhook v2) — chat general
- `Webhook1` (webhook v1) — chat leads GPT-4o-mini
- `Receive Lead Data from VAPI` (webhook v2, path 60d5fdeb...) — voz → CRM
- `4. Webhook Schedule Confirmation` (webhook v1, path calendly-tour-confirm)
- `Schedule Trigger` (schedule v1.2, diario) — Telegram listings
- `Schedule Trigger1` (schedule v1, diario) — Market Radar
- `Gmail Trigger` (gmailTrigger v1.2, everyHour) — appointment automation
- `Watch Real Estate Offer Sheet` (googleSheetsTrigger v1, everyMinute) — dispara campaña marketing

### 2.2 Bloque A — Scraping Immobiliare.it — 13 nodos

`Set params (set v3.4) → Generate Urls (code js: baseUrl+max_pages+page_format) → Split Out → Loop Over Items (splitInBatches v3) → Scrape listings (scrapegraphAi v1) → Extract individual URL (informationExtractor v1.2 + Gemini Chat Model) → Wait (pacing) → Aggregate → Unified (code flatMap) → Split Out1 → Limit → Loop Over Items1 → Extract data (scrapegraphAi JSON schema: title, price, area, bedrooms, bathrooms, floor, rooms, balcony, terrace, cellar, heating, AC, image URLs) → Update sheets (googleSheets v4.7 appendOrUpdate, dedup por URL)`

Stickies: STEP1 Config Params, STEP2/3 Extract Urls, STEP4 detalle, How it works 2 fases + Setup ScrapeGraphAI+Gemini+Sheets.

### 2.3 Bloque B — Lead scoring simple — 6 nodos

`On form submission → OpenAI Chat Model (gpt-4o-mini) + Information Extractor → If (v2.2) → Edit Fields (set) → Gmail send (v2.1) + Airtable create (v2.1, YOUR_TABLE_ID)`

### 2.4 Bloque C — Telegram listings scheduler — 6 nodos

`Schedule → ScrapegraphAI → Code formatForTelegram (typo year_bult) → Telegram send (v1.2) + If1, Code1, Merge, Gmail1`

Stickies: Trigger, Telegram config @BotFather.

### 2.5 Bloque D — Chatbot inmobiliario avanzado SG — 30 nodos [el más valioso]

`Webhook chatbot-webhook → Code2 urlRegex extrae links → If2 link? → rama link: Postgres SELECT * FROM new_properties WHERE propertyguru_url=$1 OR 99.co_url=$1 → Get Property Media (SELECT storage_path, property_id FROM property_media) → construct_image_url (code baseUrl supabase + storage_path) → Merge combine → LLM conversation (agent v1.9) / Format Results AI (agent v1.9 + gpt-4o-mini/gpt-4) → Format Response (set) → Send Formatted Response (respondToWebhook) + Parse Data (code: normaliza personal{name,phone,email}+property{type,locations,budget,timeline,citizenship}, limpia locations, parsea budget regex, ready=name+phone+email) → Save Personal Info (postgres INSERT user_info) → Query Properties (SELECT * WHERE Property Type ILIKE, Nearest MRT ILIKE, Rental Price<=bigint LIMIT 5) + PostgreSQL Memory (memoryPostgresChat) + SerpAPI (toolSerpApi) + AI Agent + Human agent (gmailTool) + Ready Check (if v1) + agenda Gmail Trigger → AI Agent → get_Calendar/update_Calendar/Google Calendar/create (googleCalendarTool v1.3 getAll/create/update/delete) + OpenAI Chat Models`

Stickies: Chatbot Description completa (entry, link detection, content filter, sequential collection Name→Phone→Email, Type→Location→Budget→Timeline), Format response, Flow/Engine/CRM/Follow Up, AI Agent Leads Processor (problema/solución/scope).

### 2.6 Bloque E — Market Radar pain-points — 9 nodos

`Schedule Trigger1 → Apify Scraper (httpRequest v1 https://api.apify.com/v2/acts/apify~google-search-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN) → Extract Summary (code join organicResults title—description) → Extract Pain Points (agent + gpt-4o-mini) → Read Yesterday Pain Points (airtable v1) → Compare Pain Points (code diff today vs yesterday) → Telegram Notifier + Store to Airtable`

Stickies: Market Radar Problem/Solution/Scope, Flow/Engine/Sinyal/Database/Get yesterday.

### 2.7 Bloque F — Tour scheduling Calendly — 9 nodos

`0. Form Trigger → 1. Extract Prospect Data (function v1 formData Full Name...) → 2. Generate Scheduling Link (function v1 calendlyBaseLink YOUR_CALENDLY_BASE_LINK + ?name&email&a1) → 3. Send Scheduling Link Gmail (v1) → 4. Webhook calendly-tour-confirm → 5. Add Event to Agent Calendar (googleCalendar v1.3) → 6. Send Confirmation Slack (v1) → 7. Wait → 8. Send Tour Reminder (gmail v1)`

Stickies: Tour Scheduling doc 11 pasos setup, Property Tour Request & Scheduling / Confirmation & Reminders.

### 2.8 Bloque G — Marketing voz + email Llama/VAPI — 11 nodos

`Watch Offer Sheet (Sheet1) → Get Client Contact List (Sheet2) → Llama 3.2 Promo Content Model (lmChatOllama llama3.2-16000:latest) + Generate Promo Content (agent v2) → Delay to Sync Data (wait) → Create Personalized Email Template (code map Emial [typo], join allEmails + promo output) → Email Promo to Clients (gmail) + Trigger Voice Campaign via VAPI (httpRequest v4.2 POST api.vapi.ai/call) → Receive Lead Data from VAPI → Delay for Lead Parsing (wait) → Save Lead to CRM Sheet (googleSheets v4.5 appendOrUpdate) → Send Acknowledgement to VAPI (respondToWebhook v1.2) + AI Agent1 (agent v2 + OpenAI Chat Model5 + memoryBufferWindow)`

Stickies: Triggers offer Sheet, VAPI lead, CRM Sheet, Delay, Email template, Promo, Marketing Llama/VAPI link 6630.

### 2.9 Credenciales y variables

- Reales: `gmailOAuth2 (Gmail account) | postgres (Postgres account)` — 15 usos aprox.
- Placeholders sin credencial: `YOUR_APIFY_TOKEN, YOUR_TABLE_ID, YOUR_CALENDLY_BASE_LINK, YOUR_AGENT_CALENDAR_ID, YOUR_TIMEZONE, YOUR_AWS_SECRET_KEY_HERE (en Code supabase), YOUR_GMAIL_CREDENTIAL_ID, YOUR_GOOGLE_CALENDAR_CREDENTIAL_ID, Slack sin ID`.
- Parámetros: `Set params url, max_pages, page_format_value | Generate Urls baseUrl&pag=i | Sheets documentId+sheetName | Postgres queries user_info/new_properties/property_media | Webhook paths chatbot-webhook, calendly-tour-confirm | VAPI api.vapi.ai/call | Apify google-search-scraper | Telegram chat/channel | Airtable base/table`.

---

## 3. Ideas reutilizables por bloque

- **Scraping:** patrón `Code genera URLs → SplitOut → SplitInBatches → Wait` para Idealista / Zonaprop / Argenprop. Schema InformationExtractor como contrato.
- **Leads chatbot:** `Parse Data` robusto + `ready flag` + `urlRegex` + `SELECT ILIKE + regexp_replace budget` + `Merge media` + `content filter primero` + `nunca repreguntar dato dado`. Copiar a OS-Emilia con memoria Postgres.
- **Agenda:** tools Calendar como tools del agente + Gmail Trigger como inbox → patrón handoff `Human agent gmailTool`. Ideal para LidIA secretaria.
- **Radar:** `Summary → Pain Points → Compare Yesterday` como mini-memoria de mercado → OS-Studio observatorio con Telegram.
- **VAPI:** `SheetsTrigger oferta → POST /call → webhook lead → ack` como plantilla voz para campañas.
- **Formato Telegram:** `formatForTelegram` con safe defaults como base WhatsApp/Telegram OS.

---

## 4. Riesgos / Deprecaciones

- `function v1` x2 (tour) — deprecado desde 2022, migrar a `Code v2`.
- `scrapegraphAi v1 community` — coste, latencia, vendor lock → Firecrawl / Apify + Extract o `httpRequest + InformationExtractor`.
- `lmChatOllama llama3.2-16000:latest` — tag inexistente → `llama3.1:8b / qwen2.5` local OS-Studio.
- `gpt-4` en formateo — caro, alcanza `gpt-4o-mini`.
- `manualTrigger v1, webhook v1, gmail v1, telegram v1, airtable v1, postgres v2.6, agent v1.9 mezclado con v2` — actualizar a latest al reimportar.
- `executionOrder v1` obsoleto → `v1.1` o default.
- Placeholders `YOUR_...` + token en URL + supabase secret en Code + typos `Emial, year_bult` — rompe en prod, pasar secretos a env.
- Polling `everyMinute Sheets + everyHour Gmail` — costoso, usar webhooks nativos.
- `Limit+Aggregate+Unified` sin errores/reintentos, `Wait` fijo frágil.
- 132 nodos en 1 workflow inactivo imposible de debuggear/versionar.

---

## 5. Propuesta re-implementación

1. **Desguazar en 4 sub-workflows + 1 orquestador:** `RE-scrape, RE-marketing-voz, RE-leads-chat, RE-agenda`. Importar por separado, activar solo necesarios en LidIA V5.0. Stickies → docs.
2. **Stack actual:** Postgres `new_properties+property_media+user_info` como CRM único en vez de Sheets/Airtable; `Ollama qwen2.5 + OpenAI gpt-4o-mini` vía gateway; `Firecrawl/Apify`; `Telegram/WhatsApp` vía Bot API OS-Emilia; `Google Calendar MCP + Gmail OAuth2`.
3. **Endurecer:** migrar `function→Code`, latest typeVersion, secretos a `.env`, fix typos, `If error + Retry + dedup URL`, `memoryPostgresChat sessionId=phone/email`, content filter como guardrail.
4. **Conectar a OS:** exponer `Webhook chatbot-webhook + calendly-tour-confirm + VAPI-lead` como tools MCP `lidia.leads.search, lidia.agenda.create, lidia.marketing.blast`; radar diario → canal OS-Studio.
5. **Pilotar 1 rama:** empezar por `D chatbot SG` — la más completa y rentable — test con 5 propiedades reales, luego tour scheduling y por último scraping.

---

## 6. Pendiente de revisión conjunta [editar acá]

- [ ] ¿Qué bloque pilotamos primero? Propuesta: D chatbot SG.
- [ ] ¿CRM único Postgres o mantenemos Sheets/Airtable en transición?
- [ ] ¿Scraping con Firecrawl o Apify?
- [ ] ¿Voz VAPI sí / no para primera versión?
- [ ] Próximo paso: desguace en sub-workflows + estimación.

---
*Fuente: JSON full workflow ZRDZCTdQR2lqRT75 leído vía MCP 2026-11-10. Credenciales solo tipos/nombres, sin secretos.*
