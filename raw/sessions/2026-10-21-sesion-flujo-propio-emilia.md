---
tipo: log
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [n8n, emilia, os-studio, cal-com, sesion-2026-10-21, agente-voz, arquitectura]
---

# Sesión 2026-10-21 (madrugada) — Emilia con su propio flujo: agente de voz + subagente de agendamiento

## Qué se hizo

Sol decidió que **Emilia tenga su propio flujo completo** (no un flujo compartido con un dispatcher de Cal.com). Se rehízo la parte de n8n y se dejó todo probado.

### Arquitectura final

```
Telegram → OS-Emilia — Telegram Router (único trigger)
              └─→ OS-Studio — Voz Dispatcher        (decide por chat_id)
                    ├─ 8459099332 → OS-Studio — Agent Voz TEST (Sol)   → OS-Studio — Agenda Sub TEST
                    └─ resto      → OS-Studio — Agent Voz Emilia (nuevo) → OS-Studio — Agenda Sub Emilia
```

**Workflows nuevos de hoy:**
- `OS-Studio — Agent Voz Emilia` (`Fa2AlIDqUntSWMrw`, 23 nodos): copia del agente de voz con identidad propia — allowlist de su chat, claves Redis `studio_os_emilia_<chat_id>`, memoria Postgres `studio_os_emilia`, `Tool Agenda Emilia` apuntando a su Agenda Sub, tool de Fathom con `source: telegram-voz-emilia`.
- `OS-Studio — Voz Dispatcher` (`Msh31moofBKBwZId`, 5 nodos): extrae el `chat_id` y llama al flujo que corresponde.

**Workflows modificados:**
- `OS-Emilia — Telegram Router` (`YWpuV5p0vCDTbIHz`): su nodo `Run Voz Agent` ahora apunta al Voz Dispatcher (1 cambio de parámetro). La regla 2 del switch `Route Telegram Command` sigue siendo la que decide "el chat de Emilia entra al flujo" (placeholder `999999999`).
- `OS-Studio — Agent Voz TEST` (`Gpd6NHB4HQdU7ary`): volvió a su forma final: `Tool Agenda` directo a su Agenda Sub (sin dispatcher ni marcador `[chat:ID]`), allowlist solo suya, claves Redis `studio_os_test_8459099332` (para que `Limpiar Memoria TEST` siga funcionando).

**Archivado:** `OS-Studio — Agenda Dispatcher` (el intermedio de la arquitectura anterior).

### Pruebas

- Voz Dispatcher con el chat de Emilia → `Run Voz Emilia` → la cadena completa respondió con **su** Cal.com ✓
- Voz Dispatcher con el chat de Sol → `Run Voz Sol` → **Telegram real entregado** (`message_id 277`, `chat 8459099332`, desde `@emiliaospi_bot`) ✓
- El `Detector` de Emilia ahora compara el chat id **como texto** (`String(chatId) !== String(PERMITIDO)`): el `pinData` del MCP stringifica los valores y con comparación numérica la allowlist rechazaba ✓

## Lecciones técnicas (21/10)

1. **El SDK de n8n (`create_workflow_from_code`) es la única vía fiel** para clonar un workflow: el MCP `addNode`/`updateNodeParameters` **stringifica** booleanos y aplana colecciones. Pero el SDK tiene un **límite de payload**: con ~16 KB la llamada agota el tiempo del MCP (timeout) → hay que recortar el código (sin `position`, sin `id` de asignación, sin `cachedResult*`).
2. **Los `subnodes` van dentro de `config`**, no al nivel del nodo. Si van fuera, el agente se crea sin modelo ni tools (el aviso es *"Required field subnodes is missing"*).
3. **Los `id` de las asignaciones de un nodo Set son obligatorios** (el SDK avisa `SET_INVALID_ASSIGNMENT`).
4. El SDK **tolera** que un mismo nodo sea destino de varias ramas de un switch (se probó con un workflow de prueba).
5. **El Code node no debe comerse el item de entrada**: si devuelve un objeto nuevo sin conservar el dato original, lo que sigue (`$json.update`) queda vacío y el flujo destino falla con *"Key parameter is empty"*. La solución: devolver `{chatId, update: u}`.
6. **Un `executeWorkflow` necesita su `workflowInputs.schema`**: no se puede crear ese nodo por MCP (la colección se aplana), pero sí por SDK.
7. `restore_workflow_version` **puede fallar**: las versiones viejas se purgan por retención ("It may have been pruned by workflow history retention"). Para deshacer cambios hay que parchear el workflow, no volver a una versión.
8. La tabla de memoria `studio_os_emilia` la crea el nodo de Postgres en la primera ejecución (no hubo que crearla a mano).

## Archivos del vault

- `proyectos/STUDIO_OS-Emilia/documentacion/que-le-pedimos-a-emilia-2026-10-21.md` (nuevo) — los 3 datos a pedirle + 7 preguntas de confirmación + guion de prueba en vivo + qué NO hay que decidir.
- `proyectos/STUDIO_OS-Emilia/documentacion/plan-minimo-sesion-2026-10-21.md` — arquitectura final (§1.2) y los 2 lugares del `chat_id` (§2.1).
- `log.md` (entrada del 21/10).

## Pendientes para la sesión del 21/10

1. `chat_id` real de Emilia → 2 reemplazos (`999999999`): Router `rightValue` + `Detectar Entrada Emilia` `PERMITIDO`. Después, **publicar** las 2 versiones.
2. Dirección del estudio → Cal.com ET `7563141` (location). El bot no manda dirección: la hereda del event type.
3. Que comparta su calendario con `proyectopi.31416@gmail.com` → `leer_calendario` deja de dar error.
4. Opcional en la UI de Cal.com: duraciones 120/180 y el schedule 24/7 del ET libre.
