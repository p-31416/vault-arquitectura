---
tipo: log
fecha_creacion: 2026-10-16
ultima_actualizacion: 2026-10-16
tags: [sesion, mvp_02, SET_01, playbooks, adr]
idioma: es
---

# 2026-10-16 — Sesión SET_01 playbooks + ADR único

## Qué se hizo

- Auditoría spec/ft SET_01 sin editarlos: DoD 6 cumple + 3 parcial + 1 diferido (CTB/TEMPLATE/LISP parciales, glosario diferido).
- Propuesta inicial 8 ADRs → consolidada por pedido SOL en registro único `proyectos/MVP_02-autocad-standards/03-adr-SET_01.md` (ADR-A unidades/escala, B capas/rótulo, C bloques/memoria/palettes, D Full+LT/Drive/monochrome). 4 `specs/261015-adr-*.md` creados y luego eliminados para cero duplicados.
- 2 playbooks MD borrador para lectura (PDFs en pausa):
  - `SET_01-REP_Replanteo/playbooks/PB-01-SET-informe.md` — informe Emilia: kit Drive, DoD, horas/payback, mapa anti-duplicados.
  - `SET_01-REP_Replanteo/playbooks/PB-02-replanteo-desde-0.md` — setup 0 → PDF Full EN base + variante LT vigente, tabla EN/ES + atajo + descripción oficial + URL Help verificada.
- Kit ajustado por SOL: DWT único con 13 bloques en memoria (sin oposición) + `bloques.dwg` como madre; CTB vigente `monochrome.ctb` (preinstalado, `EP-ISO` a backlog multi-escala); LSP `SET-REPLANTEO` crea 29 capas + fija variables, idempotente.
- Bloques en memoria organizados: generales + replanteo en DWT (vanos/tags/carátula, 3 grupos) vs disciplina (`SAN-`, `ELE-`) en bibliotecas propias; nivel `GEN-NIVEL` dinámico Corte/Vista/Planta con `Block Table` + grip altura; palettes LT verificadas (sí incluidas en LT 2027).
- Refs `autodesk-help` (ACD/ACDLT 2027, `en_US`): `-DWGUNITS`, `INSUNITS`, `SCALELISTEDIT`, `CHECKSTANDARDS`, `DATAEXTRACTION`, `FIELD` trap, `PLOT` 1:1, `monochrome.ctb`, Tool Palettes LT, DesignCenter LT, Blocks palette, symbol libraries, LISP en LT, dynamic visibility.

## Archivos modificados

- Nuevo: `proyectos/MVP_02-autocad-standards/03-adr-SET_01.md`
- Nuevo: `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/playbooks/PB-01-SET-informe.md`
- Nuevo: `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/playbooks/PB-02-replanteo-desde-0.md`
- Eliminados: `specs/261015-adr-a-unidades-escala-metros.md`, `261015-adr-b-capas-rotulo.md`, `261015-adr-c-bloques-computos-field.md`, `261015-adr-d-entorno-drive.md`
- Intactos (auditoría): `SET_01-REP_Replanteo/01-spec-SET_01.md`, `02-ft-SET_01.md`

## Pendiente siguiente ciclo

- SOL lee PB-01 + PB-02 en MD; con `s`: paso a PDF para Drive `W03-CAD/SET_01-REP/`.
- Confirmar LT año + Win/Mac para paso LISP exacto (LT 2024+ Win sí, LT 2023-/Mac manual).
- Prototipo `GEN-NIVEL` dinámico en Full; variante LT documentada.
- Tras evaluar SET_01: pase a `wiki/estandares/` + `wiki/glosario/software/autocad` + mkdocs online.

## Cerebro-digital

### Topics
- SET_01-REP replanteo 1:50 metros + viewport 20 XP + `monochrome.ctb` vigente
- DWT único con bloques en memoria vs biblioteca madre + palettes LT
- ADRs únicos por SET + playbooks MD → PDF → wiki

### Entidades
- Emilia (informe mañana, Drive `W03-CAD/SET_01-REP/`, LT vigente)
- `REP-ARAOZ.dwg` (49 capas, 13 bloques, 304 cotas, 208 inserts, `$INSUNITS 6`)
- Comandos: `-DWGUNITS`, `SCALELISTEDIT`, `LAYER`, `STYLE`, `DIMSTYLE`, `BLOCK/INSERT/ATTDEF/BATTMAN/ATTSYNC`, `TOOLPALETTES/ADCENTER/BLOCKSPALETTE`, `DATAEXTRACTION`, `CHECKSTANDARDS`, `PLOT`, `APPLOAD`

### Hechos
- DoD SET_01: 6/10 cumple, 3 parcial (CTB/TEMPLATE/LISP), 1 diferido (glosario)
- `monochrome.ctb` grafica todo negro y viene preinstalado (Help ACD 2027)
- LT 2027 incluye Tool Palettes + DesignCenter + Blocks palette; LISP solo LT 2024+ Win
- 14 h invertidas, ahorro ~12-15 h por plano, payback primer plano
