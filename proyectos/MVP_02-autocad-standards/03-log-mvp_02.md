---
tipo: log
mvp: 02
fecha_creacion: 2026-06-30
ultima_actualizacion: 2026-09-27
tags: [mvp_02, log]
---

# MVP_02 — Bitácora global

| Fecha | Evento |
|-------|--------|
| 2026-06-30 | Creación del MVP. Pendiente de definir n_01-layers. |
| 2026-09-27 | Sesión de brainstorming @brainstormy para reescribir la filosofía (`00-filo-mvp_02.md`). Divergencia con 20 ideas + wildcards, convergencia con matriz Impacto×Esfuerzo y Top 3 JTBD. Manifiesto reescrito con enfoque filosófico: "El dibujo es un documento y también un lenguaje". |
| 2026-09-27 | Creación del SET — Plano de Replanteo Arquitectónico (`SET-replanteo-spec.md`). Catálogo de capas DR-* completo (~60 capas), standards, comandos, tips, propuesta de AutoLISP `SET-Replanteo.lsp`. Análisis vaultworm-arq del documento maestro como referencia para Arquilogia. ADR-003: SET como MVP concreto del n_01. |
| 2026-09-27 | Plan de implementación creado (`PLAN-implementacion-MVP_02.md`). DoD para cada parte. Workflow sherlock → vaultworm-arq documentado. `raw/docs/` creada para crudos de Perplexia. README actualizado con explicación FILO/SPEC/FT/LOG y flujo iterativo. Prefijos definidos: A-/E-/DR-/REP-/SIMB-. Monochrome como mínimo, CTB por escala después. Metric system, commands in English, naming in Spanish. |
| 2026-09-27 | Fase 1 — Carga de 5 crudos Perplexia en `raw/docs/`. @sherlock falló por tier gratuito → ejecución manual: se leyeron los 5 archivos y se generó `raw/sessions/2026-09-27-mvp_02-fuentes.md` con topics, entidades, hechos y 12 propuestas wiki para vaultworm-arq. Se generó digest en `raw/vaultworm-arq/digest-2026-09-27-mvp_02-fuentes.md`. |
| 2026-09-27 | URL audit manual (sherlock falla por tier): `curl.exe` chequeó 38 URLs del Kit temático → 36 OK (200), 2 descartadas 403 (Autodesk Blog, UNLP TP7). Reporte en `raw/reports/2026-09-27-url-audit.md`. |
| 2026-09-27 | Unificación SET: eliminado `SET-replanteo-spec.md` v1 (DR-* 80+ capas). Creada carpeta `SET_01-REP_Replanteo/` con spec v2.1 (R-/A-/S-/G-, 22 capas), `lisp/SET_01-REP.lsp`, `docs/` (rotulo, template-dwt, ctb, dws, activos). Binarios NO en git → `activos/` (gitignored). Norma SET: `SET_0x-XXX_Descripcion/`. |
| 2026-09-27 | Spec genérica v2 (`01-spec-mvp_02.md`): 10 items ordenados (seteo → layers → CTB → textos → cotas → bloques → dinámicos → template → lisp → glosario). "DoD" entre comillas (sin ref. wiki — descartado por vaultworm-arq por falta de respaldo). CTB opcional (fallback `monochrome.ctb`), layers color index salvo hatches RGB, AUX no imprimible. SET_01 detalla §0 "DoD" importando estructura global. |
| 2026-09-27 | SET_01 cerrado 9/10 DoD: lisp v2.2 con `entmake` real + `G-VPRT/G-AUXI` no imprimibles; creado `docs/bloques.md` (R-PTO-ATTR → DATAEXTRACTION). Glosario diferido. Propuesta wiki en `raw/vaultworm-arq/propuesta-wiki-2026-09-27.md` (14 entradas, 10 referentes; corregidos AEA=Electrotécnica, aysa.com.ar). Wiki NO creada — diferida hasta evaluar SET_01. |
| 2026-09-27 | Sherlock A-434: extracción factual en `raw/research/2026-09-27-A434-rotulado-resumen.md` (definición tripartita, 5 campos "se recomienda", 8 contenidos áreas libres, ficha 2a ed. 2010 ISBN 978-987-9210-21-5; PDF binario sin mm extraíbles). `docs/rotulo.md` actualizado con citas literales + tabla 11 atributos (5 A-434 + 6 SET_01 ext.). |
| 2026-09-27 | Research GCBA muros de sherlock ELIMINADO (reemplazado por fuente local). PDF RT GCBA `3.3 Soluciones admitidas.pdf` (G:, 030301 v3 + 030303 v1) leído: tabla eT LH/LC/BH/HCCA/tabiques en `docs/muros-espesores.md`. Índice research limpio (fila GCBA muros borrada). |
| 2026-09-27 | `docs/muros-espesores.md` ELIMINADO (el usuario edita espesores manualmente). README linkea carpeta externa `G:\Mi unidad\OS-Emilia\W03-CAD` (Drive montado, verificado: REP-ARAOZ.dwg, ARQ-ARAOZ.dwg). Regla: .md referencia binarios por ruta, sin duplicar; lectura directa por filesystem. |
| 2026-09-27 | Reestructura SET_01 con nomenclatura MVP: `SET_01-REP_Replanteo.md` → `01-spec-SET_01.md`; creado `02-ft-SET_01.md` (esqueleto 10 items para completado manual con MCPs). AutoCAD 2027 TRIAL conectado vía MCP (Drawing4.dwg, mm). Paso a paso desde acá. |
| 2026-09-28 | SETEO (item 1) — spec §4.2 + ft §1 escritos: `-DWGUNITS` 6 (m), `LUNITS=2`, `INSUNITS=6`, `MEASUREMENT=1`, escala custom `1:50 (m)` paper 1/drawing 0.05 (=factor 20 = `ZOOM 1000/50 XP`), layout A1 841×594 apaisado `DWG To PDF.pc3`, viewport display locked. Citas Autodesk oficiales (units, scale, viewport, paper size). Docs/lisp pendientes (se crean al ejecutar cada paso). |
| 2026-09-28 | **Plan mode cerrado.** Sistema pasó a build mode activo. URL `https://www.ar.weber/detalles-constructivos/muros-interiores` agendada en `raw/research/2026-09-28-weber-detalles-muros.md` con estado 403 (no verificada) + 3 URLs alternativas 200 OK del mismo dominio + 2 fuentes oficiales secundarias (Bahía Blanca, UNAM). Índice research actualizado con nueva fila prepend. **Spec anotado progresivamente**: §2.5 SET-ROT paper-only + §2.6 Auditoría de capas (placeholder con tabla de renombres) + §4.6 SETEO ScaleList (tabla CustomScale = 1000/denom para 1:5–1:1000) + §4.7 LAYOUT (REP-PTipo-A1 + full bleed) + §10 Rótulo/Bloque (10.1, 10.2, 10.2.1 con FIELD syntax) + §11 Próximos pasos operativos 1–11. User instructed: "ve anotando en el 01-spec" — cada edit chico viene después de aplicar UI cada paso. |
