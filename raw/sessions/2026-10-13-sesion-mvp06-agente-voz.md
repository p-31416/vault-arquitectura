---
tipo: log
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [sesion, mvp_06, n8n, telegram, agente-voz]
---

# Sesión 2026-10-13 — MVP_06 agente de voz: proyecto propio + 2 workflows TEST + pruebas vivas

Más nuevo → más arriba

## Resumen

Se creó el proyecto propio `proyectos/MVP_06-agente-voz/` (fuera de Studio OS Emilia) con spec canónica, manual de uso, matriz de credenciales, referencia detallada del workflow (26 nodos + reglas + guía edición/stickies) y bitácora. En n8n: `OS-Studio — Agent Voz TEST` (`Gpd6NHB4HQdU7ary`) y `OS-Studio — Agenda Sub TEST` (`ygdjqRfXpxKMFWEN`) con patrón conserje/ejecutor. Ciclo completo probado en vivo (alta, modificación, duración, cancelación), loteo Redis OK con 6 fragmentos, y diagnóstico API que fijó horario real Lun-Vie 9-17 sin sábados. Estado al cierre: TEST activo con webhook (Router de Emilia pausado en la práctica), pendiente revertir al terminar pruebas.

## Decisiones

* Proyecto propio MVP_06, no dentro de Studio OS Emilia.
* Sin comandos slash en el camino principal; lenguaje natural voz+texto.
* Contactos en el principal (buscar+agregar en `clientes-contactos` real); subflujo ejecutor puro con ficha completa obligatoria.
* Email siempre obligatorio; videollamada default del evento; presencial con `attendeeDefined` después.
* Un solo eventType `7467793` con duraciones 30/60 (`lengthInMinutes`); dos tools `agendar_online`/`agendar_presencial`.
* Modelos: free falló (razonamiento en voz alta, exec 3570) → flash-lite floor devolvió vacío (exec 3572, blindado con fallback) → `google/gemini-3.7-flash` (verificado: es lo que realmente usa LidIA; el nodo se llama "luna-pro" pero el parámetro es Gemini).
* Fathom queda con Emilia (funciona, no tocar); dedup de re-sync diferido.
* Limpieza: archivados Eval Extractor y Test Pipeline v5.1; WEB y prospección a mano (fuera de MCP); Postgres se conserva.

## Pendientes

* Probar reserva real + cancelar en `cal.com/bookings` con contacto de prueba.
* Probar voz punta a punta; métricas M2 (8/10) en bitácora.
* Credencial Telegram ya fijada a `emiliaospi_bot` por Sol en UI.
* Al terminar pruebas: desactivar TEST + togglear Router off/on + `/help` de verificación.
* Infra: `OS-Sol`, Data Table perfiles, ubicación dirección-libre habilitada en el evento Cal.com.

## Archivos modificados

* `proyectos/MVP_06-agente-voz/{readme,01-spec,02-ft,03-log}.md` + `documentacion/{manual-uso-agente-voz,credenciales-conexiones}.md`
* `specs/261013-agente-voz-telegram-os.md` (superado, apunta al proyecto)
* `proyectos/00-index.md` (registra MVP_06)
* n8n: `Gpd6NHB4HQdU7ary`, `ygdjqRfXpxKMFWEN` (inactivos salvo TEST en prueba)

## Análisis cerebro-digital

### Topics

* Patrón orquestador validado como corte correcto: conserje con contactos vs ejecutor Cal.com.
* Modelos free no sirven para tool-calling en español; a este volumen (<$1/mes cualquiera) decide fiabilidad, no precio.
* Webhook único por bot token: convivencia TEST/producción exige ventanas con toggle.

### Entidades

* `OS-Studio — Agent Voz TEST`, `OS-Studio — Agenda Sub TEST`, `eventTypeId 7467793`, `chat_id 8459099332`, `clientes-contactos`, `Cal.com API Key`, `emiliaospi_bot`.

### Hechos

* Execs: 3567 listar OK, 3568 slots OK con ID real, 3570 falla free, 3572 vacío floor + fix fallback.
* 4 flujos LidIA inactivos tratados (2 archivados, 2 a mano).
