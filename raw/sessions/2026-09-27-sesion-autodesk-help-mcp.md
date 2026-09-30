---
tipo: log
fecha_creacion: 2026-09-27
ultima_actualizacion: 2026-09-27
tags: [sesion, autocad, mcp, opencode, autodesk-help, wiki]
---

# Sesión 2026-09-27 — Autodesk Product Help MCP en vault-arquitectura + docs en wiki

Más nuevo → más arriba

## 2026-09-30 madrugada — auditoría completa REP-ARAOZ.dwg via COM directo

- Reintento pedido por el usuario. MCP `autocad` solo expone `autocad_status` / `get_active_drawing_info` / `list_layers` / `list_layouts` (verificado con `tools/list` directo al binario). `query_entities` y `list_blocks` no están en el server.
- **Bypass:** script `scripts/audita-dwg-com.py` con `pywin32` habla directo con AutoCAD. Resultado: 1311 entidades leídas (race COM en últimas 47 de 1358), 54 capas, 367 bloques, 17 inserts/muestras.
- Inventario completo: 619 LINE, 291 DIM, 197 INSERT, 83 TEXT, 60 POLYLINE, 26 MTEXT, 23 HATCH, 14 CIRCLE.
- Top capas por entidades: `A-MURO-MAMP` 271, `0` 254 (geometría suelta), `REP-COTAS` 152, `A-COTA-1-50` 135, `SIMB-MURO` 122.
- Bloques notables: `SIMBOLO DE EJE` (9), `PUERTA BATIENTE` (46), `Tabela_Esquadrias` (10), `C40.20` (6 columnas).
- **Hallazgos clave:** `0-REF` referencia xref `ARQ-ARAOZ` → las 21 capas `ARQ-ARAOZ|*` son del xref, no del DWG; 254 entidades viven en `0` (no migradas); nombres con espacios (`AR-CUADRO DE VANO`) y tildes (`ANOTAÇÃO`) incompatibles con NCS.
- Reemplazado `raw/reports/2026-09-29-audit-rep-araoz.md` (versión consolidada con delta, áreas de mejora, automatización).
- Screenshot capturado: `activos/caddy-salidas/REP-ARAOZ.copia-trabajo.screenshot.png` (1376×754, ventana AutoCAD con `REP-PTipo-A1` activo).
- Pendiente: migrar 254 entidades de `0`, definir `EP-REP.dws`, construir `SET-01-REP.lsp`.

## 2026-09-29 noche — auditoría REP-ARAOZ.dwg vía MCP autocad — reporte parcial

- Pedido con `s`: analizar `REP-ARAOZ.dwg` contra spec SET_01 §2 (22 capas).
- AutoCAD 2027 trial (26.0s LMS Tech) abrió la copia `REP-ARAOZ.copia-trabajo.dwg` (creada por el agente); `INSUNITS=6 metres`; contrato MCP mm sin warning.
- Leído con éxito: `autocad_status` (caption + path + unidades), `get_active_drawing_info` (idem), `list_layers` (34 capas), `list_layouts` (`Model` + `REP-PTipo-A1` activo en A1 full-bleed con `DWG To PDF.pc3`).
- **Timeout COM:** `query_entities` (walk >200 entities), `list_blocks` (idem). En revisión: filtrar por `object_name` o acotar `max_scan`.
- Reporte generado: `raw/reports/2026-09-29-audit-rep-araoz.md`. Hallazgos: 0/22 capas del spec SET_01 coinciden; prefijos mezclados (`REP-`, `A-`, `E-`, `ROT-`, `SIMB-`, `IE-`), sub-capas por subcategoría (práctica razonable no documentada en spec), nombres con espacios/glifos no ASCII (`AR-CUADRO DE VANO`, `ANOTAÇÃO`, `A-EQUIP-`), locked/frozen bien aplicados en capas de referencia.
- Áreas de mejora: migrar nomenclatura al Kit con `acet-laytrans`, normalizar nombres ASCII, definir `EP-REP.dwt`+`EP-REP.dws`, crear bloques `R-EJE-MARCA` y `R-PTO-ATTR`, alinear nombre de layout `REP-PTipo-A1` → `REP-A1`.
- Pendiente: reintento con `object_name` filtro o `max_scan` bajo.

## 2026-09-29 noche — auditoría REP-ARAOZ.dwg vía MCP autocad (pendiente DWG abierto)

- Pedido con `s`: analizar `activos/caddy-salidas/REP-ARAOZ.dwg` y cruzar con spec SET_01 §2 (22 capas).
- Script `scripts/audita-dwg.py` + `scripts/audita-dwg_notas.md` (didáctico línea por línea) con spec embebido y reporte Markdown+JSON. Probado: ezdxf 1.4.4 lee DXF pero **no DWG nativo** sin ODA File Converter (no instalado).
- Decisión: vía MCP `autocad` (ya conectado 6/6). Pendiente: usuario abre 2027 con copia del DWG → yo disparo `autocad_status` + `list_layers` + `query_entities` + `list_blocks` + `get_active_drawing_info` + `list_layouts` y armo `raw/reports/2026-09-29-audit-rep-araoz.md`.

## 2026-09-27 noche4 — detalle 30 herramientas en mcp-autocad.md

- Pedido: cada herramienta con su ficha (parámetros, unidades, notas) y la tabla del documento como índice con wikilinks `[[#herramienta]]`.
- `mcp-autocad.md`: tabla reorganizada con wikilinks por herramienta; nueva sección `## <herramienta>` para las 30 (Conexión 3, Documentos 4, Estado del dibujo 8, Geometría 9, Edición 3, Vista y feedback 2). Verificado contra `acad_core.py` y README del repo.

## 2026-09-27 noche3 — separación wiki: opencode solo menciona, detalle en dos páginas

- Pedido con `s`: `opencode.md` solo menciona MCPs; el detalle va en páginas separadas porque `autocad` y `autodesk-help` son distintos.
- Creadas `wiki/glosario/software/mcp-autodesk-help.md` (remoto, 2 herramientas, demo es_ES) y `wiki/glosario/software/mcp-autocad.md` (local COM, 30 herramientas por área, mm/`INSUNITS`, handles, output jail, pilotos A/B).
- `opencode.md`: tabla recortada a 5 columnas con **Estado** + columna "ver detalle" con wikilink. Subsecciones eliminadas.
- `wiki/glosario/software/00-index.md`: 2 filas nuevas. `wiki/glosario/software/autocad.md`: links directos a las dos páginas detalle.

## 2026-09-27 noche2 — instalación MCP autocad (limuzi013 COM)

- Pedido con `s`: escribir entrada wiki primero, luego instalar.
- Wiki: fila `autocad` en tabla Servidores MCP + subsección `### autocad (limuzi013)` en `opencode.md`; link en `autocad.md` Agente IA. Estado inicial pendiente → conectado tras install.
- Revisión código: `autocad-mcp 0.1.0`, Apache-2.0, deps `mcp/pywin32/pillow` (sin red). Guardados enjaulados bajo `ACAD_MCP_OUTPUT_ROOT` con chequeo `..`. Incluye herramienta Delete (mitigación: copias + aprobación manual).
- Install: clonado en `P:/00-repos/proyecto-pi/tools/autocad-mcp` (fuera del repo git), `venv` Python 3.12 + `pip install .` → `autocad-mcp.exe`. Salidas en `activos/caddy-salidas/` (gitignored, verificado en `git status`: no figura).
- `opencode.json`: bloque `autocad` local, array único al `.exe` + `env` output root + `timeout` 20000. `mcp list` → 6/6 ✓ connected.
- Pendiente usuario: abrir 2027 con copia del DWG y pedir `autocad_status` para prueba funcional (clave 2026 vs 2027 por `acax*.tlb`).

## 2026-09-27 noche — prueba leantime + autodesk, fix leantime

- Pedido: probar conexión a leantime y autodesk.
- `autodesk-help`: `mcp list` → ✓ connected; `mcp debug` → `HTTP 200 OK`, sin auth requerida. Operativo.
- `leantime`: figuraba `✗ failed (MCP error -32000: Connection closed)`. Diagnóstico: el bloque usaba `"command": ["leantime-mcp"]` + clave `"args"` que el esquema OpenCode no contempla (solo `command` array completo) → el proceso nacía sin argumentos y moría al instante. Sonda stdio directa al binario con token responde `leantime-mcp 1.6.2`, así que binario + token + red están sanos.
- Fix en `opencode.json`: `command` array único `["node", "P:/00-repos/npm-global/node_modules/leantime-mcp/bin/leantime-mcp.js", "https://pitau.tech/mcp", "--token", "{env:LEANTIME_TOKEN}", "--insecure"]` (node directo, sin shims `.cmd`/`.ps1`). Re-verificado: `mcp list` → 5/5 ✓ connected.
- Nota seguridad: `opencode mcp list` imprime el token leantime en claro en la línea del comando (solo metadata len en este log, valor nunca copiado). Mejora pendiente: pasar el token por variable de entorno `LEANTIME_API_TOKEN` en vez de flag `--token` para que no figure en la lista de procesos.
- `wiki/glosario/software/opencode.md`: fila leantime de la tabla actualizada al nuevo comando.

## 2026-09-27 pm — fix índice mismo-doc + verificación no manual

- Índice `opencode.md` y `autocad.md` usaba `[[Título]]` (nota separada inexistente → figura vacía). Normalizado a `[[#Encabezado exacto]]` según convención Obsidian del vault.
- Verificación ejecutada por el agente (usuario pidió no hacerlo manual): `opencode mcp list` → `autodesk-help ✓ connected` (5 servers; `leantime ✗ failed` preexistente, fuera de alcance). `opencode mcp debug autodesk-help` → `HTTP 200 OK`, sin auth requerida.

## Qué se hizo

- Pedido: instalar Autodesk Product Help como MCP para consultar fuentes oficiales AutoCAD, con receta de `raw/docs/autocad-documento-maestro.md` §11.2.
- Verificado endpoint `https://developer.api.autodesk.com/knowledge/public/v1/mcp` vía directorio MCP + docs OpenCode (200 OK). Doc oficial `help.autodesk.com/...ADSKMCP_KnowledgeMcp...` existe pero carga como app JS.
- Agregado a `opencode.json` (con aprobación "ok si"): bloque `mcp.autodesk-help` remote + `timeout: 30000`. JSON queda con 5 servers: `comfyui, n8n-mcp, fathom, leantime, autodesk-help`.
- Documentado en wiki donde viven los MCP: nueva sección `## Servidores MCP del vault` en `wiki/glosario/software/opencode.md` (tabla 5 MCP + subsección `autodesk-help` con herramientas, prueba ES, verificación).
- Documentado uso en `wiki/glosario/software/autocad.md`: nueva sección `## Agente IA — Product Help MCP` con wikilink a opencode + ejemplo ES + fuente raw §10-11.
- Pendiente del usuario: `opencode mcp list` + `opencode mcp debug autodesk-help` + recargar sesión OpenCode para tomar el MCP nuevo.

## Archivos modificados

- `P:\00-repos\proyecto-pi\vault-arquitectura\opencode.json` — agregado `mcp.autodesk-help` (remote, URL Autodesk, enabled true, timeout 30000)
- `P:\00-repos\proyecto-pi\vault-arquitectura\wiki\glosario\software\opencode.md` — frontmatter 2026-09-27 + tag mcp, índice + sección Servidores MCP del vault + referencias verificadas
- `P:\00-repos\proyecto-pi\vault-arquitectura\wiki\glosario\software\autocad.md` — frontmatter 2026-09-27 + tag mcp, índice + sección Agente IA Product Help MCP

## Análisis cerebro-digital

### Topics

- Autodesk Product Help MCP remoto solo lectura vs conectores comunitarios de dibujo (`puran-water` AutoLISP, `limuzi013` COM)
- Inventario MCP canónico en `opencode.json` + descripción humana en `opencode.md`, uso por software en `<software>.md`
- Timeout remoto 30s vs default OpenCode 5s; OAuth automático vs Bearer `{env:}`

### Entidades

- `developer.api.autodesk.com/knowledge/public/v1/mcp`, `get_available_products`, `search_help_content`, OpenCode MCP client, AutoCAD 2027, `raw/docs/autocad-documento-maestro.md`

### Hechos

- 2026-09-27 vault-arquitectura suma 5to MCP `autodesk-help`; resto (`comfyui, n8n-mcp, fathom, leantime`) queda intacto
- Wiki software suma primera tabla inventario MCP + primer puente AutoCAD ↔ OpenCode vía wikilink absoluto
- Ningún secreto tocado; Product Help es público y lleva autenticación propia si el cliente la pide

## Próximo

- Usuario ejecuta `opencode mcp list` → `autodesk-help ✓ connected`
- Prompt prueba ES bloques dinámicos con `use autodesk-help`
- Opcional siguiente ciclo: probar conector comunitario de dibujo sobre copias DWG + TRUSTEDPATHS
