# 2026-10-09 — Alta Emilia en Leantime + proyecto O.S_ARQ-Emi

tags: [sesion, emilia, leantime, accesos, proyecto, api, cierre]

## Qué se hizo
- Pedido inicial: crear usuaria `arq.emiliapimentalombardi@gmail.com` vía MCP de Leantime.
- Hallazgo MCP: el remoto responde `initialize` 200 (Laravel MCP 1.0.0) con la API key vigente, pero `tools/list`, `prompts/list` y `resources/list` devuelven catálogo vacío → alta por MCP inviable, queda para siguiente ciclo (revisar plugin MCP Server).
- Corrección intermedia: mis primeras sondas leían `LEANTIME_TOKEN` con off-by-one (`Substring(16)` en vez de `IndexOf('=')+1`) y reportaban 67 chars; el `.env` siempre estuvo íntegro (68, `lt_`). Supersedido por scripts v2/v3.
- Alta de proyecto por API JSON-RPC documentada (`POST /api/jsonrpc`, `x-api-key`): creado **`O.S_ARQ-Emi` id 4**, cliente Pitautech id 1. Primer intento falló con `Parse error` por em-dash en `details`; reintento ASCII → `result: [4]`.
- Flujo de contraseña de Emilia respondido con docs oficiales: invite email con link para generar contraseña; si el SMTP no entrega, el link se copia de su ficha en User Management.
- Verificación de cierre: usuaria Emilia **id 5, status `i` (invitada, pendiente de aceptar)**; usuarios totales 3; proyectos totales 3.

## Archivos modificados
- `scripts/probe-leantime-mcp.ps1` (v1, con off-by-one — superseded)
- `scripts/check-leantime-token-meta.ps1`, `scripts/compare-leantime-tokens.ps1`, `scripts/fix-leantime-token*.ps1` (diagnóstico, sin cambios reales al `.env`)
- `scripts/probe-leantime-mcp-v2.ps1`, `scripts/probe-leantime-mcp-v3.ps1` (sonda canónica: 200 + catálogo vacío)
- `scripts/leantime-crear-proyecto.ps1`, `-v2.ps1`, `-v3.ps1` (alta efectiva en v3)
- `scripts/leantime-verificar-emilia.ps1` (verificación de cierre)
- `.env` intacto (verificado, sin escritura efectiva)

## Pendiente siguiente ciclo
- Rotar token expuesto en `create-user-emilia.ps1:4`.
- Revisar plugin MCP Server (expone 0 tools) para el flujo `Fathom → specs → Leantime`.
- Emilia: aceptar invite, generar contraseña, asignarla a `O.S_ARQ-Emi` con `inherit`.

## Cerebro-digital
- Topics: leantime-mcp-vacio, jsonrpc-addproject, invite-flow-smtp, offbyone-token.
- Entidades: Emilia Pimenta Lombardi (id 5, status i), proyecto O.S_ARQ-Emi (id 4), clientes Pitautech (1) / LidIA (2), endpoint `pitautech-leantime.3nq4ow.easypanel.host`.
- Hechos: MCP sin tools al 2026-10-09; proyecto creado por API; usuaria invitada pendiente de aceptar.
