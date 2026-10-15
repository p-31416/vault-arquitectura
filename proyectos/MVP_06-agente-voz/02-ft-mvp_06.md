---
tipo: plan
mvp: 06
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [plan, mvp_06, agente-voz, n8n, construccion]
---

# 02-ft-mvp_06 — Plan técnico de construcción

> El detalle canónico vive en [[proyectos/MVP_06-agente-voz/01-spec-mvp_06|01-spec-mvp_06]] §4. Este archivo registra el orden de construcción y se expande al ejecutar.

## Orden

1. Infra cuentas Sol: `OS-Sol` + `clientes-sol-test` + fila `sol` en `OS-Bot-Profiles` + tu `eventTypeId` Cal.
2. Workflow `OS-Studio — Agent Voz TEST`: Trigger → Auth → Tipos → STT Gemini → Normalizar → Redis (clon `pw5OHhXNjeXSnD3u`) → Agent free + Postgres + tools Agenda/Fathom TEST → responder.
3. Rama HTTP turbo + modelo pago cableadas pero desactivadas.
4. Prueba 5+5, métricas, umbral 8/10.
5. Swap pago + 2° Cron TEST + costos 7 días.
6. M4 Emilia prod sin tocar Cores.

## Quirk conocido

Nodos `IF` nuevos creados por API no discriminan en esta instancia (todo sale por rama 0); usar `Switch` v3.4 con el patrón del Router. Ver [[proyectos/STUDIO_OS-Emilia/documentacion/arquitectura-n8n-os-emilia|arquitectura-n8n-os-emilia]] §4–5.

## Protocolo de pruebas (TEST, sin romper producción)

0. Previo: en los 3 nodos Telegram del TEST poner la cred `emiliaospi_bot-Telegram account` (n8n autoasignó la genérica). **NO activar el TEST**: le roba el webhook al Router de producción.
1. Subflujo solo (n8n UI → `OS-Studio — Agenda Sub TEST` → Execute Workflow, input `{"query": "..."}`):
   - `qué reuniones tengo esta semana` → lectura real, seguro.
   - `hay lugar mañana de 10 a 11` → slots (requiere eventTypeId real; con 0 falla cerrado = esperado).
2. Escritura real: pasar tu `eventTypeId` → se carga en el system prompt del subflujo → `agendame mañana 10h con <contacto real> <email>` → verificar en `cal.com/bookings` → cancelar ahí mismo.
3. Punta a punta con Telegram (ventana de 5 min, coordinar horario): desactivar Router → activar TEST → mandar 1 texto + 1 voz + 1 callback → volver atrás (activar Router, desactivar TEST).
4. Voz: solo se valida en vivo; el pin de prueba no lleva binario.
5. Fathom sync: no disparar hasta perfil Sol (hoy escribe en carpetas de Emilia).
6. Métricas M2 (8/10): éxito, latencia, WER en nombres, `usage` → anotar en `03-log-mvp_06.md`.
