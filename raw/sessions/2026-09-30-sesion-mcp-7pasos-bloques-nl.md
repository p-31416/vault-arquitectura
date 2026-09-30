---
tipo: log
sesion: 2026-09-30-sesion-mcp-7pasos-bloques-nl
fecha: 2026-09-30
participantes: [usuario, Muse Spark]
duracion_min: 180
tags: [sesion, mcp, n02, bloques, lenguaje-natural, ia-cad-test]
---

# Sesión 2026-09-30 — MCP 7 pasos + bloques por lenguaje natural — cierre positivo

## Qué se hizo

Sesión de dibujo por lenguaje natural vía LLM + MCP `autocad` sobre `activos/caddy-salidas/ia-cad-test.dwg` (metros, contrato MCP mm). Se desglosó el plano en 7 reglas infinitesimales y se ejecutaron por MCP con verificación por paso. Estado final positivo: **inserta bloques por lenguaje natural** queda verificado.

**Geometría ejecutada:**
- Interior 4×4: polilínea `2F1` `A-AREA` azul (0,0)-(4,4) + duplicada `573` `A-MURO` blanca superpuesta (A-AREA Plot No como Defpoints)
- Exterior: `2F2` `A-MURO` (-0.15,-0.15)-(4.15,4.15) offset 0.15 m
- Vano 98 para puerta 90: jambas blancas `2F3` x1500 y `2F5` x2480 (movida +100 mm de 2380) distancia 980 mm en `A-MURO`
- Puerta: bloque `PUERTA BATIENTE` `574` en [1.5,-0.15] exterior (corregida -15 cm de [1.5,0]) + hoja roja `718` [1.5,-0.15]→[1.5,0.75] 900 mm `A-CARP` (reemplaza `2FD` 800 mm)
- Ventanas Y: 2× `VENTANA BAJA SIMPLE` en paredes Y medio y=2.0: oeste `719` [0.212,2.0] y este `724` [3.787,2.0] (simétrica, rot 90°) `A-CARP` con atributos visibles mock `ALFEIZAR 0.90` `ALTO 1.20` `TIPO DVH Mock` `ANCHO 1.50` activados vía `HandleToObject` + `GetAttributes` + `Visible=True`
- MText: `72F` eliminado (gigante en 2000 m), nuevo `744` `AcDbMText` `A-AREA` en [2,2,0] `AttachmentPoint 5 (MC)` `Height 0.15` `width 2.5` `Text LOCAL 4x4\n16.00 m2` medio-centro dentro de interior
- Equipamiento: `table-5.dwg` (52 ents) insertado `782` en [2,2,0] `A-MOB` centro geométrico (reemplaza placeholder `2F6` 0.80×0.80 eliminado); cocina Y: mesada `785` [0,2500]-[600,4000] 0.60×1.50, bacha `786` [150,3000]-[450,3500] 0.50×0.30, heladera `787` [600,3400]-[1200,4000] 0.60×0.60 todas `A-MOB`

**Herramientas MCP usadas:** `autocad_draw_polyline`, `autocad_draw_line`, `autocad_copy_entity`, `autocad_set_entity_layer`, `autocad_move_entity`, `autocad_erase_entity`, `autocad_insert_block`, `autocad_draw_text`, `autocad_create_layer`, `autocad_query_entities`, `autocad_zoom_extents`, `autocad_save_active_drawing`, `autocad_status`, `list_blocks`, `autocad_list_layers` + `win32com` para `AddMText` MC, `HandleToObject` atributos y `InsertBlock` DWG.

## Archivos modificados

- `proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/00-filo-n_02.md` — creado, luego correcciones menores de encoding
- `proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/01-spec-n_02.md` — hipótesis en positivo, 7 pasos con vano 98, capas A-AREA no imprimible, MText MC + Field, bloques ventana/puerta, trazabilidad 30/09 + refs Help
- `proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/02-ft-n_02.md` — protocolo paso a paso dummies con URLs verificadas Help 2026 (OFFSET, COPY, MTEXT MC, FIELD, Blocks)
- `proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/03-log-n_02.md` — 7 fichas + 5 correcciones (puerta exterior, vano 98, hoja 90, ventanas Y, texto gigante, table-5, cocina) con handles y VD, estado final positivo
- `proyectos/MVP_01-dibujo_ia/readme-mvp_01.md` — árbol actualizado con `n_02-mcp_test_local`
- `activos/caddy-salidas/ia-cad-test.dwg` — 87.610 bytes 30/09 00:39, 11 entidades nuevas verificadas
- `activos/caddy-salidas/table-5.dwg` — origen bloque 782 (existente, leído)

## Análisis cerebro-digital

### Topics
- Dibujo asistido por lenguaje natural vía LLM+MCP, descomposición en reglas infinitesimales, capas A- arquitectura, vano para carpintería, MText MC y Fields, atributos de bloque

### Entidades
- `ia-cad-test.dwg` (4×4 local), `table-5` (52 ents), `PUERTA BATIENTE` (46), `VENTANA BAJA SIMPLE` (14), `A-MURO`/`A-AREA`/`A-CARP`/`A-MOB`, `2F1`/`573`/`2F2`/`2F3`/`2F5`/`718`/`719`/`724`/`744`/`782`/`785`/`786`/`787`/`574`

### Hechos
- Vano ajustado 88→98 para hoja 90; puerta movida -15 cm a polilínea exterior; texto MText MC corregido de (2000,2000) mm-gigante a (2,2) m; ventana derecha simetrizada a 3.787; table-5 insertado en centro 2,2 con placeholder eliminado; cocina Y con mesada 60, bacha 50×30 y heladera 60×60

### Hipótesis verificada
- Positivo: el flujo por lenguaje natural incluye inserción de bloques por indicación en lenguaje natural y queda verificado (puerta, 2 ventanas, table-5 por MCP). Próximo ciclo: Field de área linkeado a `2F1` (16.00 m²) y nuevos bloques por NL desde este DWG base en `activos/caddy-salidas/ia-cad-test.dwg`.

## Próximos pasos

- Field `Area` de `2F1` linkeado en MText `744` con `Insert Field → Object → Area` y `FIELDEVAL`
- Bloques adicionales por NL (heladera real si existe en librería, artefactos cocina)
- Captura con ventana AutoCAD al frente para evidencia visual
- Retomar desde DWG base `ia-cad-test.dwg` sin recrear geometría

## Referencias verificadas (sin 404)

- https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-C0E4246D-C420-42BD-A6FC-8B1852EFD005 — OFFSET
- https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-1CF9287F-06E8-4D03-8377-2E130862FE02 — COPY
- https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-F94BE932-DA31-437E-9610-27F46ACD5711 — MTEXT MC
- https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-18389CD1-2F81-4185-A459-F59AE311D637 — Area + Field
- https://help.autodesk.com/view/OARX/2026/ENU/?guid=GUID-2D31D8C1-9BEC-48CF-8B73-E2AD38A08D74 — Area Property
- https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-F613CBDA-5899-4419-9C23-2E0F6C76BB99 — Field Object
- https://help.autodesk.com/view/ACD/2026/ENU/?guid=ACD_FOUNDATIONS_MAIN11 — Blocks
