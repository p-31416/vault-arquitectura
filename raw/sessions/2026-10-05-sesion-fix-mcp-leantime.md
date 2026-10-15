---
tipo: log
fecha_creacion: 2026-10-05
ultima_actualizacion: 2026-10-05
tags: [sesion, leantime, mcp, opencode, easypanel, vps, fix, emilia]
---

# Sesión 2026-10-05 — Fix MCP Leantime (`remote` + `x-api-key`, URL EasyPanel real)

## Qué se hizo

- **Diagnóstico** del MCP `leantime` caído (`MCP error -32000: Connection closed`). Dos causas encadenadas: (1) el binario `leantime-mcp` ya no estaba instalado en `npm-global/node_modules` y el paquete está deprecado oficialmente; (2) la URL de la config `https://pitau.tech/mcp` es el **panel de EasyPanel** (cert autofirmado `CN=Easypanel`, sin SAN) y no el MCP de Leantime.
- **Verificación técnica**: cert de `pitautech-leantime.3nq4ow.easypanel.host` = Let's Encrypt `YE2` (válido); `/mcp` → 401; probe JSON-RPC `initialize` con `x-api-key` → 200 con respuesta MCP válida; `Authorization: Bearer` → `Invalid API Key` (es API key `lt_`, no PAT).
- **Fix en `opencode.json`**: `type: local` (binario + `--token --insecure`) → `type: remote` + `url` del subdominio de la app + `headers: {"x-api-key": "{env:LEANTIME_TOKEN}"}` + `timeout: 30000`.
- **Verificación final**: `opencode mcp list` → 7 servers, `✓ leantime connected` (6/7 OK; `fathom-proyectopi` sigue en rojo, fuera de alcance).
- **Wiki (con `s` explícito de Sol)**: creada `wiki/glosario/software/leantime.md`; actualizadas fila Leantime en `wiki/glosario/software/00-index.md` y fila MCP en `wiki/glosario/software/opencode.md`; entrada nueva en `log.md`.

## Segunda parte — MCP `fathom-proyectopi` (`env` → `environment`)

- **Síntoma:** mismo `MCP error -32000: Connection closed`, causa opuesta.
- **Diagnóstico:** el paquete `@luminarylane/fathom-mcp-server` v1.0.1 (node >=22.14, tenemos 24.15) funciona standalone. Corriendo `npx -y @luminarylane/fathom-mcp-server` sin la variable, su stderr dice textualmente `FATHOM_API_KEY env var is required` y sale con código 1 → de ahí el "Connection closed".
- **Causa raíz:** en opencode la clave es **`environment`**, no `env` (docs oficiales: opciones del MCP local). Con `env` la variable se ignora en silencio.
- **Fix:** `environment: { "FATHOM_API_KEY": "{env:FATHOM_API_KEY_PROYECTOPI}" }` + `timeout: 30000`. El `.env` de la raíz del vault tiene `FATHOM_API_KEY_PROYECTOPI` (len 92), y `LEANTIME_TOKEN` además está en scope User de Windows.
- **Bugs silenciosos del mismo tipo:** `comfyui` y `autocad` también usaban `env`. `COMFYUI_URL` coincidía con el default (8188) y nadie lo notó; `ACAD_MCP_OUTPUT_ROOT` sí importaba (las salidas CAD no iban a `activos/caddy-salidas`). Corregidos ambos.
- **Verificación:** `opencode mcp list` → **7/7 ✓ connected**.
- **Herramientas del MCP:** `fathom_list_meetings`, `fathom_get_summary`, `fathom_get_transcript`, `fathom_search_meetings`.
- **Wiki:** sección [[#Trampas MCP verificadas]] nueva en `wiki/glosario/software/opencode.md` + fila `fathom-proyectopi` en la tabla MCP + heading `## Conceptos relacionados` duplicado corregido + segunda entrada en `log.md`.

## Archivos modificados

- `opencode.json` (bloques `leantime`, `fathom-proyectopi`, `comfyui`, `autocad`)
- `wiki/glosario/software/leantime.md` (nuevo)
- `wiki/glosario/software/00-index.md`
- `wiki/glosario/software/opencode.md`
- `log.md` (dos entradas: Leantime + fathom-proyectopi)
- `raw/sessions/2026-10-05-sesion-fix-mcp-leantime.md` (esta nota)

## Análisis cerebro-digital

**Topics**
- Leantime como gestor de proyectos self-hosted y su capa MCP (Streamable HTTP nativo desde 3.10.3).
- Topología de despliegue en EasyPanel: dominio raíz del panel vs subdominio por app, y su impacto en clientes MCP `type: remote`.
- Migración de MCPs locales (puente npm) a MCPs remotos (HTTP + headers), incluyendo higiene de secretos.
- Diferencia de credenciales en Leantime: API key `lt_` (`x-api-key`) vs Personal Access Token (`Authorization: Bearer`).
- Claves de configuración de MCP local en opencode (`environment` vs `env`) y por qué el síntoma genérico `Connection closed` oculta la causa real.

**Entidades**
- Leantime (`pitautech-leantime.3nq4ow.easypanel.host`), EasyPanel (`panel.pitau.tech`), VPS Pitautech, plugin MCP Server de Leantime.
- `opencode.json` (capa MCP del vault), `LEANTIME_TOKEN` (`lt_…`, 68 chars, valor nunca impreso), paquete `leantime-mcp` 1.6.5 (deprecado).
- MCPs del vault: comfyui, n8n-mcp, fathom, fathom-proyectopi (reparado), leantime (reparado), autodesk-help, autocad.
- `@luminarylane/fathom-mcp-server` v1.0.1 (MCP SENSE, 4 tools, node >=22.14), `FATHOM_API_KEY_PROYECTOPI` (`.env` raíz del vault, len 92), `ACAD_MCP_OUTPUT_ROOT`, docs opencode.ai/docs/mcp-servers.
- Docs de referencia: docs.leantime.io (MCP), marketplace.leantime.io (plugin), github.com/leantime/leantime-mcp.

**Hechos**
1. `https://pitau.tech` = panel EasyPanel con certificado autofirmado; cada app vive en `https://<servicio>.<id>.easypanel.host` con Let's Encrypt válido.
2. `https://pitautech-leantime.3nq4ow.easypanel.host/mcp` responde 401 sin credencial y 200 con `x-api-key` válida.
3. `leantime-mcp` (npm) está deprecado: Leantime 3.10.3+ expone MCP por Streamable HTTP y los clientes se conectan directo.
4. Pasar la API key como `Authorization: Bearer` produce `Invalid API Key`; el prefijo `lt_` identifica el tipo de credencial.
5. Los MCP remotos evitan exponer el token en la lista de comandos (`opencode mcp list`) — el bridge local lo imprimía en claro.
6. "404 / connection closed" en un MCP del VPS es el síntoma de apuntar al dominio raíz del panel en lugar del subdominio de la app.
7. **En opencode la clave es `environment`, no `env`**, para variables de un MCP local; con `env` la variable se ignora en silencio y el error que se ve (`Connection closed`) no dice nada de la causa real.
8. **El error de opencode es genérico y engañoso**: 4 fallas distintas (binario inexistente, URL de panel, variable ignorada, timeout) se reportan igual. El mensaje vero aparece al correr el comando a mano y leer stderr.
9. `opencode mcp debug <servidor>` solo sirve para MCP remotos (OAuth) — con locales responde "not a remote server".
10. Una variable ignorada puede no romper nada visible si coincide con el default del servidor (`COMFYUI_URL`) — el daño aparece tarde y en otro lado (`ACAD_MCP_OUTPUT_ROOT`).

**Pendientes**
- Reiniciar la sesión OpenCode para que las herramientas de Leantime + fathom-proyectopi queden cargadas.
- Prueba funcional de `@fathom-pm` con una reunión real de la cuenta proyectopi (4 tools disponibles, sin probar contra la API real).
- `ACAD_MCP_OUTPUT_ROOT`: confirmar que las salidas CAD ahora caen en `activos/caddy-salidas`.
- Revisar si algún otro archivo del vault usa `env:` en bloques MCP (búsqueda puntual recomendada).
- Emilia necesita su propia credencial de Leantime en el PC de ella (mismo patrón `x-api-key` + `LEANTIME_TOKEN` local) — ver `specs/260929-alta-emilia-leantime.md`.
