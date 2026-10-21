# Resumen — Flujo Agent Voz TEST (OS-Studio)

> Workflow `OS-Studio — Agent Voz TEST` (`Gpd6NHB4HQdU7ary`) · Activo TEST (perfil Sol `8459099332`) · 26 nodos · Verificado 2026-10-16 vía MCP · Doc operativo v1 (2026-10-16). Canónico de diseño: `proyectos/MVP_06-agente-voz/01-spec-mvp_06.md`.

## Qué hace

Camino principal del estudio: el usuario habla o escribe normal ("agendame mañana 10h con Juan", "cancelá la del jueves", "cambiala a las 17", "qué tengo esta semana", "sincronizá mis reuniones") y el bot resuelve con herramientas reales. Sin comandos con slash.

## Cadena

```
Voz Agent Trigger (lo invoca el Router con update) → Detectar Entrada (kind audio/texto/callback, allowlist Sol)
→ audio: Descargar Voz → Transcribir Voz (Gemini gemini-2.5-flash-lite) · texto: Fijar Texto · callback: Sintetizar /cancel
→ Normalizar W02 {texto, nombre, ID} → Fijar Contexto → Guardar Redis → Esperar Lote 12s
→ Recuperar → Es Ultimo (resto obsoleto) → Armar Lote → Limpiar Lote
→ Agente Voz TEST (OpenRouter openai/gpt-5.6-luna + Memoria Postgres studio_os_test x chat.id)
→ Responder Telegram (mismo chat_id)
```

Tools: `Tool Agenda` (→ Agenda Sub TEST) · `Tool Sincronizar Fathom` (→ Fathom Core, `source: telegram-voz-test`) · `buscar_contacto` + `agregar_contacto` (Sheets `clientes-contactos` `1t9-j_7gJypLOicaJNpwYWLsBy0VDtSmdBJZumW8jtVA`, match insensible a mayúsculas/acentos/parcial).

System prompt: HOY AR, rioplatense 2-3 líneas, ante agendar PRIMERO `buscar_contacto`, nunca propone horario sin validar slots, email obligatorio, resumen + Confirmar antes de escribir, de voz cita lo entendido.

## Cómo contribuye

Absorbe `/agendar`, `/cancel` y `/modif` por comandos: desambigua ("Juan" → candidatos), multi-paso en 1 mensaje, memoria ("cambiala a las 17"), revisión de agenda con filtros, todo con Ref `uid` + auditoría.

## Credenciales que usa

Telegram `emiliaospi_bot` · Gemini STT · OpenRouter · Redis (`studio_os_test_8459099332`) · Postgres (`studio_os_test`) · Sheets `ppi-EmiliaOS_Google Sheets`.

## Tiempo que ahorra

Pedido por voz/texto → 1 mensaje vs 15 min manual (abrir Cal.com + tipear + buscar contacto + invitar). ~14 min × 8/mes ≈ **2 h/mes** + revisión de agenda conversacional.

## Cotización

Módulo agente voz/texto + agenda: **USD 50** de referencia (propuesta partnership, incluido).

## Límites conocidos

- Vive detrás del Router por ExecuteWorkflow: NO crearle un Telegram Trigger propio (le roba el webhook al Router).
- Perfil Sol hasta validar; perfil Emilia (M4): su `chat_id` + cred `ppi-EmiliaOS_Cal.com` + evento `7109200`.
- Callbacks `cancel:<uid>` se sintetizan a `/cancel <uid>` para el agente.
