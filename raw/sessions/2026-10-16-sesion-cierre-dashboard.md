---
tipo: log
fecha_creacion: 2026-10-16
ultima_actualizacion: 2026-10-16
tags: [sesion, dashboard, n8n-mcp, leantime, autocad, cierre]
---

# Sesión 2026-10-16 — dashboard visual + n8n MCP + Leantime visible

## Qué se hizo

- Dashboard Mes 1 con sistema visual propuesta-oscuro (header sticky, pills, hero, cards, pie, barras, details). AutoCAD migrada al mismo sistema + stepper W1-W4 + flow hipótesis→Mes 2.
- Página reporte AutoCAD: extracción plano (29 propias, 13 bloques, 208 INSERTs), SET_01, cuadro real, ventana 6 pasos, minutos por operación (~7.5hs), evolución SVG, recursos + DWS test (LT no trae STANDARDS: probar en full).
- Wiki `pbk-set01-rep.md` elevado (puerta única + links duros + migración Drive).
- n8n MCP por HTTP: Router 17 (13+4, sin agendar/cancel, +Voz+Jina) · Voz 26 (24+2, Gemini/Redis/Postgres/OpenRouter) · Agenda 12 (11+1, 6 tools Cal.com) · Limpiar 6 (4+2, inactivo) · SET_01 12 · Fathom cron 07:00 success diario.
- Leantime: proyecto pasado a `open` (era restricted e invisible); cliente/descripción restaurados tras wipe accidental (regla: editProject manda objeto completo).
- 65hs en Timesheets (12 entradas, 64.5hs): firma `logTime` + `getAll`; fecha 16/10 no persiste (quedó 15/10).

## Pendiente mañana

- GOAL 3 en UI · factura C 600 · reunión cierre · CAD demo + dry run · revisar dashboards Comfy/Estudio OS (estilo) · Mes 2 W1 (DWT/DWS + plano terminado).

## Análisis cerebro-digital

**Topics:** dashboard-visual-oscuro, n8n-mcp-http, conteo-nodos-sticky, leantime-restricted-open, timesheets-logtime, dws-lt-inexistente.
**Entidades:** O.S_ARQ-Emi id 4, Router YWpuV5p0vCDTbIHz, Voz Gpd6NHB4HQdU7ary, Agenda ygdjqRfXpxKMFWEN, Fathom UeDkqVZSeLnae5cF, SET_01 VIQmMEZ9tkDBfKjd.
**Hechos:** UI cuenta nodos+stickies; API Fathom sin campo duración; LT no crea DWS (fuente oficial); editProject reemplaza values.
