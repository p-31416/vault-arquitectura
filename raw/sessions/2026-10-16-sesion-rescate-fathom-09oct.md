---
tipo: log
fecha: 2026-10-16
tags: [sesion, fathom, emilia, import-manual, mes1]
---

# Sesión 2026-10-16 — rescate 3 reuniones 09/10 Fathom Proyecto Pi

## Qué se hizo

- Drive `Reuniones-Internas` confirmado: última reunión 26-9 (6 .md + 6 .gdoc, escritos 08/10).
- API Fathom Proyecto Pi (key `.env`, header `X-Api-Key`, ventana 30 días): 10 reuniones,
  3 con Emilia el 09/10 (~1h c/u, 16:15/17:47/18:48 AR), ausentes en Drive y raw.
- Import manual con `scripts/import_fathom_ppi_manual.py` (+ `_notas.md`):
  `2026-10-09_emilia-proyectopi_191472132/191509492/191524949.md` (557-801 turnos)
  en `raw/reuniones/` + copia Drive + state. Formato idéntico al Fathom Core.

## Análisis (para presentación Mes 1)

- **Emi OS (16:15):** problema errores obra (desagüe baño) → solución Emi OS (prompt ChatGPT
  evalúa planos, referentes Chipperfield/SANAA/OMA) → flujo DWF Design Review iPad Sofi →
  tasks: workflow DWF (Pi), link chat GPT (Emilia), baño PB (Emilia).
- **Sistema conocimiento (17:47):** vault/agentes/n8n/Leantime explicado a Emilia →
  tasks: curso Codex→Drive, libro tipo Ching, Emilia explora Leantime + prueba /agendar,
  cita mié 14/10 13:00.
- **Automatización+Comfy (18:48):** /agendar rígido → agente IA lenguaje natural,
  Comfy + LoRA firma, acuarela vs fotorrealista, proyecto final collage, RAM Emilia, cita mié 1PM.

## Queda

- Google Doc de las 3 (el Core solo genera el de Emilia; carga manual o backfill).
- Pasar tasks a Leantime vía fathom-pm + actualizar dashboard (23 reuniones).
- Conexión Fathom Pi al Core con dedup fecha/título (dual genera 2 recording_id).
