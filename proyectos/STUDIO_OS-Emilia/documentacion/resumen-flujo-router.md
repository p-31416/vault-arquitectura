# Resumen — Flujo Router Telegram (OS-Emilia)

> Workflow `OS-Emilia — Telegram Router` (`YWpuV5p0vCDTbIHz`) · Activo · 17 nodos (13+4 stickies) · Verificado 2026-10-16 vía MCP · Doc operativo v2

## Qué hace

Un solo trigger Telegram (`Recibo Mensaje`, bot `emiliaospi_bot`, `message` + `callback_query`) recibe TODO y deriva en 2 niveles: **identidad** (¿quién habla) → **contenido/comando** (¿qué quiere). Regla de oro: **1 trigger por token** (un segundo trigger le roba el webhook — incidente verificado 2026-10-13/14; el Agent Voz vive detrás del Router por ExecuteWorkflow, así conviven).

## Cadena real (16/10)

```
Recibo Mensaje
└─ Route Identidad (String chat.id == 8459099332, Sol)
   ├─ Sol privado → Run Voz Agent (invoca Gpd6NHB4HQdU7ary con update completo)
   └─ resto → Route Fuentes Group (chat.id == -5417177870, grupo Fuentes)
      ├─ link (contains http) → Prepara Fila → Extrae Jina → Parsea Info
      │         → Append Fuentes Sheet2 → Ack "Anotado ✓ <tipo>"
      ├─ texto sin link en grupo → (mudo, no guarda)
      └─ resto → Route Telegram Command → /sync → Run Fathom Sync · /help → Send Help
```

Comandos vigentes: `/sync` (corre el Core con `source: telegram`) y `/help` (*"Hablame en privado con voz o texto para agendar. Links al grupo Fuentes. Comandos: /sync (sincroniza reuniones), /help (esta ayuda)."*). Sin `/agendar`, sin Cancel/Modif: la agenda vive en el agente de voz (antecedente en el sticky Comandos: no borrar).

## Nodos que aportan

- `Prepara Fila` (Set): fecha AR, de (Sol/nombre), link por `entities[0]`, tipo YT/IG/SHARE/LIBRO/WEB, nota.
- `Extrae Jina` (HTTP `GET https://r.jina.ai/<link>`, 30s, retry + sigue en error) + `Parsea Info` (Code: título ≤140, tags ≤8).
- `Append Fuentes Sheet2` (Sheets `18iDrvNUOApNFsEDDQ4rMMo40cw4t0hn3CApLK9iLpvI`, hoja `Fuentes-Inbox`, Estado `pendiente`).

## Credenciales que usa

Telegram `emiliaospi_bot` · Sheets `ppi-EmiliaOS_Google Sheets` (append cola) · las de cada subflujo invocado.

## Tiempo que ahorra

| Tarea | Manual | Auto (medido) | Ahorro |
|---|---|---|---|
| Registrar link (abrir, leer, anotar) | ~4 min | ~10 s (exec 3719/3750) | ~4 min c/u |
| Clasificar + titular | ~3 min | ~9 s (exec 3764, jina) | ~3 min c/u |
| Derivar persona correcta | criterio humano | instantáneo | 0 errores de ruteo |

Método: `(t_manual − t_auto) × N/semana` (contador en Sheet). Ejemplo: 20 links/sem → ~2 h/sem ≈ 8 h/mes.

## Cotización

Módulo inbox + digest: **USD 40** de referencia (propuesta partnership, incluido). Ahorro que entrega: ~8 h/mes + capacidad imposible sin sistema.

## Pendiente

Agregar a Emilia al grupo Fuentes (`-5417177870`) + compartirle el Sheet · mover el Sheet a `OS-Emilia/` · cerrar el resto al `chat_id` de Emilia cuando mande `/start`.

## Límites conocidos

- Expresiones n8n NO aceptan `function/for/var` (solo métodos + ternarios) — cálculo complejo va en nodos Code.
- Editar con el editor UI abierto bloquea la API; publicar es obligatorio (borrador ≠ activo).
- `update_workflow` con regex/backslash en payload falla parse — usar paths o payloads simples.
