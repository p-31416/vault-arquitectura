# Resumen — Flujo Agente de Voz (OS-Studio)

> Workflow `OS-Studio — Agent Voz TEST (revision)` (`Gpd6NHB4HQdU7ary`) · Subflujo del Router (sin trigger propio) · Perfil Sol activo, perfil Emilia diseñado · Doc operativo, 2026-10-16

## Qué hace

Atiende texto y voz en lenguaje natural (rioplatense) para agenda: agendar, modificar, cancelar, listar, sincronizar Fathom. Un Agent (OpenRouter) con tools a subflujos + memoria Postgres por chat + debounce Redis anti-fragmento (12 s).

## Cadena

```
Voz Agent Trigger (subflujo, entra `update` del Router)
→ Detectar Entrada (audio/texto/callback, allowlist Sol)
→ Tipos Entrada → voz: Descargar → Transcribir (Gemini) → ...
→ Normalizar → Redis batch → Es último? → Arma Lote → Limpia
→ Agente Voz TEST (+ memoria + tools Agenda/Fathom)
→ Responder Telegram (mismo chat)
```

Reglas del sistema: buscar_contacto primero, validar slots con tools, confirmación con Ref antes de escribir, fail-closed (si falla el cancel, NO crea la nueva — verificado 2026-10-15).

## Credenciales que usa

OpenRouter · Postgres (memoria) · Redis (loteo) · Gemini (STT) · Cal.com (por perfil) · Sheets clientes.

## Tiempo que ahorra

| Tarea | Manual | Auto (medido) | Ahorro |
|---|---|---|---|
| Agendar (abrir Cal.com, cargar, invitar) | ~6 min | ~25–40 s (exec 3723/3726) | ~5 min c/u |
| Cancelar+reagendar con confirmación | ~10 min | ~35 s | ~9 min c/u |
| Revisar agenda ("qué tengo mañana") | ~3 min | ~25 s | ~2,5 min c/u |

Ejemplo: 10 gestiones/sem → ~1 h/sem ≈ 4 h/mes. Regla Cal.com (incidente 2026-10-15): mover/cancelar siempre desde bot o Cal.com, nunca desde Google Calendar (huérfana el uid y rebota).

## Pendiente (perfil Emilia)

Ver `documentacion/onboarding-emilia-perfiles.md`: 1 agente N perfiles — falta `chat_id` de Emilia (reunión), switch de cred por perfil, reconectar Google.
