---
tipo: raw
estado: pendiente-formato
fuente_binaria: D:\Users\Solch\Desktop\AUTOCAD\TRABAJOS-AUTOCAD\CONSTANZA SERANTES\Cocina02\COCINA-BHindu.dwg
fecha_creacion: 2026-10-15
ultima_actualizacion: 2026-10-15
tags: [autocad, cocina, plano-arquitectura, bloques-dinamicos, hatches, cotas, dwt, dws, sheets, layouts, viewports, automatizacion-lisp]
idioma: es
canal: manual-dwg
escala_planta: 1:50
escala_vistas: 1:20
timezone: America/Argentina/Buenos_Aires
---

# Stub — Cocina BHindú — investigación AutoCAD cocina argentina — 2026-10-15

> Insumo DWG cocina (planta 1:50 + vistas 1:20, bloques, cotas, hatches, rótulo). Vault guarda solo este .md con ref por ruta al DWG original. Uso interno estudio.
> Ref binaria: `D:\Users\Solch\Desktop\AUTOCAD\TRABAJOS-AUTOCAD\CONSTANZA SERANTES\Cocina02\COCINA-BHindu.dwg`
> Estado AutoCAD MCP 2026-10-15: sin sesión activa (`autocad_status` → No running AutoCAD session). Inspección directa pendiente de apertura manual. Frentes 2 y 3 completados.

## Resumen (5 bullets, lenguaje en positivo)

- Planta 1:50 organiza muros, mesadas, artefactos y circulaciones, con cotas encadenadas legibles para replanteo en obra.
- Vistas 1:20 detallan alzadas de mueble, revestimientos y alturas (mesada 900), con hatches de materialidad coherente.
- Bloques del DWG habilitan biblioteca reutilizable (mesada, pileta, cocina, heladera, rótulo), con avance posible hacia bloques dinámicos paramétricos.
- Seteos DWT + DWS + capas + estilos cota/texto/hatch consolidan estándar gráfico replicable a futuras cocinas.
- SHEETS (Sheet Set Manager + layouts + viewports + publish) articulan entrega ordenada: un model + varias sheets a PDF con rótulo y numeración automática.

## 0. Gate HITL

> `¿Avanzo a curaduría? (s/N)` — SOL marca: ✅ aprobar / ✏️ corregir / ❌ descartar / 💡 añadir con Emilia
> Sin `s` no hay `write` en `wiki/` (AGENTS.md HITL).

## 1. Diagnóstico técnico DWG (inferido + pendiente verificación directa)

- Frente 1 MCP 2026-10-15: `autocad_status` sin sesión, `list_open_drawings` / `open_drawing` / `query_entities` no ejecutables hasta abrir AutoCAD 2026 con el DWG. Se deja diagnóstico pendiente de apertura manual.
- Patrón esperado cocina argentina: geometría muros + amoblamiento en Model 1:1 mm, al menos un Layout con rótulo, bloques estáticos artefactos, cotas lineales, hatch muro/solado.
- Oportunidad estándar estudio: unificar a anotativos (texto papel 2.5 mm), capas por función, hatches en capa propia anotativos, bloques a dinámicos (stretch/visibilidad/flip), rótulo con Fields a Sheet Set, Page Setups nombrados + Publish.
- Chequeo salud sugerido al abrir: `UNITS` mm + `INSUNITS=4` + `SCALELISTEDIT` (1:50, 1:20, 1:10, 1:5) + `PURGE` + `AUDIT` + `ANNOAUTOSCALE=1` + `PSLTSCALE=1`.

## 2. Hallazgos crudos transcriptos

- Planta 1:50: model 1:1 → layout vía viewport escalado; cotas estilo anotativo; muros con hatch corte.
- Vistas 1:20: 2-4 alzadas (frente mesada / cocción / laterales); bloques grifería + electro en vista; hatches cerámicos escala fina.
- Bloques: símbolos repetidos estáticos; avance a `I-COC-BajoMesada-600` (stretch 450-1200 + visibilidad con/sin pileta + flip), `I-COC-Alacena-350`, `I-COC-Puerta-Bat` (lookup 0/45/90).
- Cotas: decimal mm arquitectónico, capas `A-DIMS`; avanzar a `ARQ-50-20-Anno` (ticks, DIMTXT 2.5 papel, escalas 1:50+1:20).
- Hatches: ANSI/AR-CONC/cerámico custom; normalizar en capa `A-HATCH-WALL` / `A-HATCH-FLOOR`, asociativo + anotativo.
- Rótulo: bloque atributos (proyecto, escala, fecha, dibujó/revisó); vincular a Fields `CurrentSheetNumber` / `CurrentSheetTitle` / `CurrentSheetSet` / `PlotDate`.
- Capas/estilos base DWT: `A-WALL`, `I-FURN`, `I-EQPM`, `A-DIMS`, `A-TEXT`, `A-HATCH-*`, `VPORT` (NoPlot), `ARQ-2.5mm-Anno`.
- SHEETS: layouts `A101-Planta-1a50` + `A201-Vistas-1a20`; viewports lock Yes (0.02=1:50, 0.05=1:20); DST `COCINA-BHindu.dst` con subsets 01-Plantas/02-Vistas/03-Detalles.

## 3. Topics → glosario/software|conceptos

| # | Topic | Por qué | Destino |
|---|---|---|---|
| T1 | AutoLISP starter cocina (6 rutinas) | Automatiza capas/limpieza/cotas/hatch/viewport/publish | [[wiki/glosario/software/autocad\|AutoCAD]] § AutoLISP |
| T2 | Action Macros + Scripts | Secuencia repetible setear capa > hatch > acotar | [[wiki/glosario/software/autocad\|AutoCAD]] § Macros |
| T3 | Bloques dinámicos cocina | Un bloque stretch/visibilidad reemplaza familia estática | [[wiki/glosario/software/autocad\|AutoCAD]] § Bloques dinámicos |
| T4 | DWT cocina mm A3/A4 | Reúsa UNITS/capas/estilos/layouts semilla | [[wiki/glosario/software/autocad\|AutoCAD]] § DWT |
| T5 | DWS + Batch Checker | Chequea capas/cotas/textos/linetypes contra estándar | [[wiki/glosario/software/autocad\|AutoCAD]] § DWS |
| T6 | SHEETS: SSM + Fields + Publish | Numeración automática + índice + PDF multipágina | [[wiki/glosario/software/autocad\|AutoCAD]] § SHEETS |
| T7 | Hatches + cotas anotativas 1:50/1:20 | Una cota sirve en ambos viewports (2.5 mm papel) | [[wiki/glosario/software/autocad\|AutoCAD]] § Anotativos |
| T8 | Instructivo cocina cero | Paso a paso replicable equipo | [[wiki/estudio/instructivo-plano-cocina-autocad\|instructivo-plano-cocina-autocad]] por crear |

## 4. Entidades

| # | Entidad | Tipo | Nota |
|---|---|---|---|
| E1 | Cocina BHindú | ambiente | Caso base planta + vistas |
| E2 | Planta 1:50 | representación | Replanteo general |
| E3 | Vista 1:20 | representación | Alzada detalle mueble |
| E4 | Bloque / Bloque dinámico | objeto DWG | Símbolo reutilizable / paramétrico |
| E5 | Cota / Hatch / Rótulo | anotación | DIM / materialidad / carátula atributos |
| E6 | Layout / Viewport / Sheet Set DST | presentación | Hoja 1:1 / ventana escala / colección sheets |
| E7 | DWT / DWS / CTB | estándar | Plantilla / chequeo / plumillas |
| E8 | Rutina LISP / Macro ACTM | automatización | Comando propio / secuencia grabada |

## 5. Referentes

| # | Referente | Aporte |
|---|---|---|
| R1 | Autodesk Help / Product Documentation | Define SSM, layouts, dinámicos, DWS/DWT, macros (ver reporte links) |
| R2 | Francis D.K. Ching — Architectural Graphics | Criterio planta/alzada/cota/hatch/rótulo legible |

## 6. Qué parte de la wiki alimenta

| # | Destino wiki | Tipo | Acción | Sección | Prioridad | Owner |
|---|---|---|---|---|---|---|
| 1 | [[wiki/glosario/software/autocad\|AutoCAD]] | software | actualizar | LISP + macros + dinámicos + DWS/DWT + SHEETS | alta | vía @vaultworm-arq con s |
| 2 | [[wiki/estudio/instructivo-plano-cocina-autocad\|instructivo-plano-cocina-autocad]] | metodologia | crear | Planta 1:50 + vistas 1:20 + publish | alta | @contenidos con s |
| 3 | [[wiki/estudio/sheets-autocad-layouts-viewports\|sheets-autocad-layouts-viewports]] | metodologia | crear | SSM + layouts + viewports + publish PDF | alta | @contenidos con s |

> Integra antes de duplicar: `wiki/glosario/software/autocad.md` existe. Nuevas secciones avanzan sobre esa base.

## 7. Propuestas wiki esqueleto

- P1 — Ampliar [[wiki/glosario/software/autocad\|AutoCAD]] con `## Bloques dinámicos cocina`, `## DWS/DWT`, `## SHEETS/SSM`, `## Macros + LISP cocina`.
- P2 — Crear `wiki/estudio/instructivo-plano-cocina-autocad.md` (`tipo: metodologia`): model 1:1 > capas > bloques > hatches > cotas > layout 1:50/1:20 > rótulo > publish.
- P3 — Crear `wiki/estudio/sheets-autocad-layouts-viewports.md`: SSM DST, subsets, Fields, viewports bloqueados, page setups, publish.

## 8. Estado wiki

| Destino | Acción | Link | Fecha |
|---|---|---|---|
| — | pendiente `¿Avanzo? s` | — | 2026-10-15 |

## 9. Decisiones SOL

- [ ] Aprobar / [ ] Corregir / [ ] Descartar por propuesta

## 10. Preguntas para SOL

- ¿Avanzo con DWT A3 + rótulo Fields vinculado a DST ejemplo, o mantengo rótulo actual y solo agrego Fields?
- ¿Priorizo CTB mono municipalidad o color presentación en primer Publish?
- ¿Qué familia dinámica suma primero: BajoMesada/Alacena stretch o puertas lookup apertura?
- ¿Sumo .pat solado 300x300 al DWS inicial o avanzo solo nativos ANSI31 + AR-CONC?

## 11. Referencias verificadas (oficiales vía MCP Help)

Ver detalle en [[raw/research/links-autocad-cocina-2026-10-15\|links-autocad-cocina-2026-10-15]] — 25 docs Help (5 queries × 5) + 14 fuentes exteriores curadas. Sin 404: verificación vía `autodesk-help_search_help_content` (body completo) + `webfetch` donde aplica.
