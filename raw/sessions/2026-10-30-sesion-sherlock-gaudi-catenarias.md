---
tipo: log
fecha: 2026-10-30
tags: [sesion, sherlock, contenidos, gaudi, catenaria, cascaras, tensadas, escala-urbana]
---

# Sesión 2026-10-30 — Sherlock: Gaudí catenarias, cáscaras y tensadas + documento entregable

## Qué se hizo

1. **@sherlock investiga** (pedido SOL): estructuras inspiradas en Gaudí — impacto/uso de catenarias en hormigón (cáscaras, estructuras tensadas) + aplicación a escala urbana (farolas, asientos, juegos de parque, stands de feria, construcciones pequeñas, edificios).
   - Informe: `raw/research/2026-10-30-gaudi-catenarias-cascaras-tensadas.md` — 58 fuentes (4 fetch 200 + 52 snippets verificados + 2 descartadas: Detail 410, Ingenia 403). Confianza Alta histórico/estructural, Media escala urbana.
   - Crudos por fuente: `gaudi-historico`, `candela-cascaras`, `dieste`, `otto-tensadas`, `sagrada-digital`, `escala-urbana` + cache `raw/research-cache/2026-10-30-gaudi-catenarias-cascaras-tensadas.json`. Índice `raw/research/00-index.md` actualizado.
2. **@contenidos documenta** (pedido SOL: "necesito un documento"): entregable legible `raw/contenidos/2026-10-30-gaudi-catenarias-cascaras-tensadas.md` — prosa desarrollada, 70 citas numeradas, Referencias (repos oficiales por autor), Otros links de interés, Registro HITL. Estado `pendiente-ok`.
3. **Fix citas clicable (feedback SOL ×4 rondas)**: SOL no veía los números como links. Primer intento footnotes `[^NN]` — @contenidos convirtió 196 citas + 70 def (correcto en sintaxis) pero **el plugin core Footnotes está roto en este vault** (mismo hallazgo de la sesión 2026-09-28 en el maestro AutoCAD). Solución re-aplicada: **block references de Obsidian** `[[#^fNN|NN]]` + ancla `^fNN` al pie de cada definición → 196 wikilinks + 70 anclas, verificado, **SOL confirma "listo perfecto solucionado"**. Lección reforzada: en este vault las citas referenciadas al pie SIEMPRE van como block refs, directa la solución.
2. **@contenidos documenta** (pedido SOL: "necesito un documento"): generó entregable legible `raw/contenidos/2026-10-30-gaudi-catenarias-cascaras-tensadas.md` con frontmatter, índice nativo, prosa desarrollada, **70 citas numeradas** (5 ✅ fetch / 64 ⚠️ snippet / 2 ⛔ marcadas), Referencias (repos oficiales por autor: Gaudí Museum, UNESCO, freiotto.com, MoMA, IL Stuttgart, BRG/ETH), Otros links de interés (tutoriales Kangaroo/GH, workflow digital SF, MARS Pavilion, MPavilion, Shellstar) y Registro HITL.
3. Estado `estado: pendiente-ok` — la ficha queda SIN mover a `wiki/fuentes/` (SOL dijo "ok, terminamos por hoy": no es `s` para el paso).

## Hallazgos clave (para consumo futuro)

- **Una idea, dos materiales**: maqueta polifunicular de Gaudí (cuerdas + perdigones, Sagrada Família / Cripta Güell) = mismo algoritmo que Kangaroo/Grasshopper hoy. Papers que reproducen a Isler digitalmente; tutoriales que replican la catenaria en Rhino.
- **Cáscaras**: Candela (hypars 4 cm, regla luz/espesor 400-1000), Dieste (bóvedas gausas, directriz catenaria, vínculo Cripta Güell), Isler (telas colgadas congeladas). Contraejemplo Kresge/Saarinen (forma sin ingeniero → deflectó).
- **Tensadas**: Frei Otto (películas jabón = membranas, redes invertidas = gridshells), Múnich 72 (74.000 m² cable-net, 50.000 h modelos físicos). Otto dirigió reconstrucción de la maqueta de Gaudí (Stuttgart 1982).
- **Sagrada 2026**: torre de Jesús 172,5 m cargada a centenario; Arup piedra pretensada + Rhino/GH + impresión 3D de maquetas.
- **Escala urbana**: Gaudí empezó con farolas (Plaça Reial 1879, primer encargo público); hoy: MPavilion, canopies de juegos (Oryahovo, Yangón), kiosco hormigón plegado 50 mm (Varna), MARS Pavilion (catenaria invertida robótica que cita a Gaudí), Shellstar (stand feria w/ Kangaroo).

## Archivos modificados

- `raw/research/2026-10-30-gaudi-catenarias-cascaras-tensadas.md` (+ 6 crudos por fuente)
- `raw/research-cache/2026-10-30-gaudi-catenarias-cascaras-tensadas.json` (quedó vacío según @contenidos)
- `raw/research/00-index.md`
- `raw/contenidos/2026-10-30-gaudi-catenarias-cascaras-tensadas.md` (entregable, pendiente-ok)
- Nada en `wiki/` ni `raw/sessions/` previos.

## Pendiente próximo día

- Decisión SOL: mover ficha a `wiki/fuentes/` + 8 fichas wiki propuestas a @vaultworm-arq (catenaria-funicular, form-finding, cáscaras, tensadas, Gaudí-urbano + referentes Candela/Dieste/Otto).
- Gaps: pasada IT pendiente; corpus débil asientos urbanos contemporáneos; cache de research vacío.

## Análisis cerebro-digital (Karpathy)

- **Topics**: catenaria-funicular · form-finding · cascaras-hormigon · estructuras-tensadas · escala-urbana · maqueta-digital · HITL-pendiente-ok
- **Entidades**: Gaudí · Candela · Dieste · Otto · Isler · Saarinen · Arup · Kangaroo · Grasshopper · Sagrada Família · MPavilion · MARS Pavilion · Shellstar · Plaça Reial · Múnich 72
- **Hechos**: 58 fuentes sherlock → 70 citas en entregable · Otto reconstruyó maqueta Gaudí 1982 · Gaudí primer encargo público = farolas 1879 · regla Candela luz/espesor 400-1000 · torre Jesús 172,5 m cierre 2026
