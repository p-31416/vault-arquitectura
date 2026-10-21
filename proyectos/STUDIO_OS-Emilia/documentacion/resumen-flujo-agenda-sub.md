# Resumen — Flujo Agenda Sub TEST (OS-Studio)

> Workflow `OS-Studio — Agenda Sub TEST` (`ygdjqRfXpxKMFWEN`) · Activo TEST · 12 nodos · Verificado 2026-10-16 vía MCP · Doc operativo v1 (2026-10-16). Patrón: `LidIA_V5.0-SWF_Agenda` (`w8iMJ01WGCSxvSMg`).

## Qué hace

Ejecutor de toda la operatoria Cal.com. Lo invoca el Agent Voz con el pedido en lenguaje natural (`query` con ficha completa); nunca atiende usuarios directo.

## Cadena

```
Agenda TEST Trigger (query) → Agente Agenda TEST (OpenRouter openai/gpt-5.6-luna + memoria por ejecución)
├─ consultar_disponibilidad (GET /v2/slots — SIEMPRE antes de agendar)
├─ obtener_reuniones (GET /v2/bookings eventTypeId 7467793 — Ref + listados)
├─ agendar_online (POST booking videollamada) · agendar_presencial (POST booking con dirección)
├─ actualizar_reunion (POST /bookings/<uid>/reschedule — solo horario)
├─ cancelar_reunion (POST /bookings/<uid>/cancel)
└─ leer_calendario (Google Calendar proyectopi.31416@gmail.com — incluye manuales)
```

Evento `7467793` (`Reunión Semanal`, duraciones 30/60/180, Meet por defecto, Lun-Vie 9-17). Horario AR; Google con `-03:00` se copia tal cual. Revisión de agenda: une bookings + calendario, deduce duplicados fecha+título, solo `accepted` cuenta. Cambio de duración = cancelar + reagendar. Ficha incompleta (sin email) = no agenda.

## Cómo contribuye

Opera Cal.com con invitación por email, mueve/cancela con Ref, lista próximas/semana/cliente. Regla de oro que sostiene: mover/cancelar desde bot o Cal.com, nunca desde Google (huérfana el uid).

## Credenciales que usa

Cal.com Bearer `ppi_calcom-Bearer Auth` (`60SFxvMa6AaqmWWi`, `cal-api-version: 2024-08-13`, slots `2024-09-04`) · Google Calendar · (Emilia M4: `ppi-EmiliaOS_Cal.com` + evento `7109200` 60 min Meet).

## Tiempo que ahorra

Con el Voz: 1 mensaje vs 15 min manual → ~14 min × 8/mes ≈ **2 h/mes**.

## Cotización

Incluido en el módulo agente (USD 50 de referencia). Evento 60 min con Meet se configura con Emilia en la reunión de cierre.
