---
tipo: log
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [sesion, glosario, links, design-thinking, sprint, sdd]
---

# Sesión 2026-09-09 — Fixes glosario (lote usuario)

## Qué se hizo

- jake-knapp: coautores Zeratsky/Kowitz/Margolis/Burka + bibliografía Sprint/Make Time/Click con ISBN y fichas.
- design-thinking: de stub a ficha completa (origen, 5 modos, 7 mindsets, giro 2016, traducción arquitectura).
- SDD: eliminada duplicación entidad (queda solo concepto).
- ben-van-berkel: sección The New Understanding (2011) con fuentes League/Cooper.
- carlos-banon: sección NXT BLD 2026 con abstract completo desde fetch.
- Migración de índices a `[[#Encabezado exacto]]` en 12 archivos (causa raíz de links rotos en Obsidian).
- Auditorías por script: 0 links absolutos rotos en glosario; índices referentes/software verificados; 12 URLs externas 200.

## Archivos modificados

- `wiki/glosario/referentes/jake-knapp.md`, `ben-van-berkel.md`, `carlos-banon.md`, `bjarke-ingels.md`, `fredy-fortich.md`
- `wiki/glosario/conceptos/design-thinking.md`, `sdd-spec_driven_development.md`, `kanban.md`, `design-sprint.md`, `braintrust-pixar.md`, `seguridad-psicologica-aristotle.md`, `marco-creativo-google-pixar.md`
- `wiki/glosario/entidades/00-index.md` (delist SDD) + entidad eliminada
- `log.md`

## Análisis cerebro digital (Karpathy)

- **Topics candidatos a `wiki/glosario/software/`**: ninguno nuevo (todo era `conceptos`/`referentes`).
- **Entidades**: Margolis y Burka mencionados sin ficha (quedan como mención hasta que el vault los nombre); Yiping Goh (co-fundadora FORMAS.AI); Stan Allen (moderador League); Carissa Carter (giro d.school 2016).
- **Hechos/decisiones**: regla "índices nativos `[[#...]]`, nunca slugs" confirmada como causa raíz (AGENTS.md ya la predecía); auditar con script antes de afirmar "está roto"; SDD = concepto, no entidad; link Stanford viejo 404 confirmado.
