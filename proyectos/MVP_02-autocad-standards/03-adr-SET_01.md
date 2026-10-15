---
tipo: metodologia
mvp: 02
set: SET_01-REP
fecha_creacion: 2026-10-15
ultima_actualizacion: 2026-10-15
tags: [adr, mvp_02, SET_01, decisiones]
idioma: es
estado: propuesta-para-lectura
---

# 03-adr-SET_01 — Decisiones SET_01-REP (único)

> Registro único de decisiones del SET_01. Spec/ft quedan intactos como auditoría. Tras aprobación avanzan hacia `wiki/estandares/` + `wiki/glosario/software/autocad` + `log.md`. Playbooks en `SET_01-REP_Replanteo/playbooks/` avanzan hacia wiki una vez definidos.

## ADR-A — Unidades en metros + escala 1:50 (m) 20 XP

**Fecha**: 2026-10-15 · **Estado**: propuesta · **Deciden**: SOL + equipo

Contexto: modelo `REP-ARAOZ.dwg` medido `$INSUNITS 6` metros, `$MEASUREMENT 1` métrico. Papel A1 en mm. Lista default mm/mm de `acadiso.dwt` deja viewports con factor incorrecto en modelo en metros.

Decisión: modelo en metros (`-DWGUNITS` 6, `LUNITS` 2 decimal, igualar `INSUNITS`, geometría existente intacta) + custom `1:50 (m)` Paper 1 / Drawing 0.05 + viewport `ZOOM 20 XP` aplicado por nombre, vista bloqueada.

Alternativas: modelo en mm (lista default directa, pide conversión constante en obra) / tipear factor crudo (dropdown muestra número, `FIELD` incluye duplicado). Ambas quedan para siguiente ciclo.

Consecuencias: inserciones escalan auto por `INSUNITSDEFSOURCE/TARGET`; viewport estable + `FIELD` legible. Riesgos: reset `SCALELISTEDIT` + cerrar/reabrir documentado en PB-02; `PurgeAECData` resetea a 4 → verifica `UNITS` tras purga.

Trazabilidad: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/01-spec-SET_01|01-spec §4.2 + §4.6]] · [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/REP-ARAOZ-capas-bloques|medición §1]] · `playbooks/PB-02` pasos 1-2.
Refs: [How to change units (-DWGUNITS)](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Convert-imperial-unit-drawing-to-metric-units.html) · [Blocks scaled when inserted](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Blocks-xrefs-or-raster-images-are-scaled-when-inserted.html) · [Incorrect scale 1:100 viewport](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Incorrect-scale-when-setting-up-viewport-plot-scale-in-AutoCAD.html) · [Custom scale paper vs drawing](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-scale-does-not-scale-viewports-as-expected-in-AutoCAD.html)

## ADR-B — Nombres del archivo canónicos + ROT- paper-only

**Fecha**: 2026-10-15 · **Estado**: propuesta · **Deciden**: SOL + equipo

Contexto: 29 propias + 20 xref `ARQ-ARAOZ|` medidas 2026-10-13. Kit propone `R-/A-/S-/G-`; archivo avanza con `REP-EJES`, `A-MURO-MAMP`, `SIMB-MURO`, `ROT-HOJA/TXT/VP` paper mm.

Decisión: nombres del archivo como canónicos v2.2; Kit como equivalencia. `ROT-` separada de modelo (paper mm, Plot No), layout `REP-PTipo-A1` full bleed A1 apaisado.

Alternativas: renombrar a Kit (49 renombres + riesgo 208 inserts/304 cotas) / rótulo en modelo (mezcla mm con metros). Quedan para siguiente ciclo.

Consecuencias: cero retrabajo, auditoría §2.6 cerrada; CTB limpio. Riesgo: doble nomenclatura → tabla equivalencia §2 spec.

Trazabilidad: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/01-spec-SET_01|01-spec §2 + §2.6 + §4.7 + §10]] · PB-02 pasos 3+6.

## ADR-C — Bloques en memoria organizados + palettes LT + DATAEXTRACTION + FIELD escala

**Fecha**: 2026-10-15 · **Estado**: propuesta · **Deciden**: SOL + equipo

Contexto: 13 bloques, 208 inserts: 2 dinámicos con `WIPEOUT` (20 vent + 22 puertas) + tags 89/20/29/26. Atributos `TIPO/ANCHO/ALFEIZAR/ALTURA/MURO/NPT`. Carátula `G-CART-MEPA` con `ESCALA`. Uso vigente en LT (verifica palettes).

Decisión: DWT único con 13 definiciones en memoria organizadas en generales + replanteo (vanos/tags/carátula) + `SET_01-REP_bloques.dwg` como madre + disciplina (`SAN-`, `ELE-`) en bibliotecas propias fuera de memoria SET_01 + paleta `SET_01-REP` (`TOOLPALETTES` + `ADCENTER`, con layer/descripción por herramienta) + Blocks palette Libraries como alternativa; nivel `GEN-NIVEL` dinámico con visibilidades Corte/Vista/Planta + `Block Table` (atributo `NPT` alineado) + grip de altura en corte; bloques intactos (`BEDIT`, `ATTSYNC`, tag horizontal), cómputos `DATAEXTRACTION` a CSV, `ESCALA` como `FIELD` al Custom scale viewport 358.

Alternativas: explotar (pierde atributos/dinámicos/cómputos) / cómputo manual + escala tipeada (planilla desincronizada) / solo DWG sin DWT (doble paso `INSERT` por plano). Quedan para siguiente ciclo.

Consecuencias: `NUEVO` y dibuja; ahorro mayor (~10 h + ~2 h); rótulo auto-actualiza con `REGEN`. LT incluye palettes (solo excluye luces/cámaras/materiales). Riesgos: trap lista duplicada → Move Up + `REGEN`; nombre duplicado manda definición local → re-`INSERT`; palettes migran con Plot No → recrea desde DesignCenter.

Trazabilidad: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/01-spec-SET_01|01-spec §3.3 + §10.2.1]] · [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/bloques-personalizados|bloques]] · [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/cuadro-carpinterias|cuadro]] · PB-02 §1.5 + pasos 5+8+10.
Refs: [BOM via ATTDEF + DATAEXTRACTION](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Creating-a-Bill-of-Materials-BOM-in-AutoCAD-and-AutoCAD-LT.html) · [Field trap](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-viewport-scale-is-not-being-displayed-for-Field-in-AutoCAD.html) · [Tool Palettes LT 2027](https://help.autodesk.com/view/ACDLT/2027/ENU/?guid=GUID-6668905A-3FAD-4EED-82A2-5D6177AD4280) · [DesignCenter LT](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-insert-blocks-using-DesignCenter-for-AutoCAD-LT.html) · [Blocks palette](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-E3413A03-8EEF-44D5-B5C7-8B345A9257FE) · [symbol libraries](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-create-and-organize-symbol-libraries-in-AutoCAD.html)

## ADR-D — Full EN canónico + LT vigente + kit en Drive con DWS + monochrome

**Fecha**: 2026-10-15 · **Estado**: propuesta · **Deciden**: SOL + equipo

Contexto: base Full inglés; uso vigente LT. Equipo necesita `FIELD`, `CHECKSTANDARDS` batch, full bleed A1. LISP avanza en Full + LT 2024+ Win; LT 2023- y LT Mac devuelven `Unknown Command`. CTB vigente `monochrome.ctb` (viene con todo AutoCAD). Binarios fuera de git hacia `activos/` + Drive `W03-CAD/SET_01-REP/`.

Decisión: playbook Full EN (`_COMANDO`, tabla EN/ES + atajo) con variante LT documentada, kit `DWT (con bloques) + DWS + bloques.dwg madre + LSP + paleta .xtp` en Drive, plot con `monochrome.ctb`, verificación `CHECKSTANDARDS`+`AUDIT`+`PURGE` antes de `PLOT`. `EP-ISO.ctb` en backlog multi-escala.

Alternativas: solo LT ES (dispersa variantes) / binarios en git (rompe regla vault) / EP-ISO hoy (pide instalación y prueba por escala). Quedan para siguiente ciclo.

Consecuencias: un playbook canónico + notas LT; `DWS` + `STANDARDSVIOLATION` alertan al crear violación. Riesgos: `Missing Standards File` → ruta fija + re-asociar; plot fuera escala → `PAGESETUP` Layout 1:1.

Trazabilidad: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/01-spec-SET_01|01-spec §4.3-§6]] · [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/02-ft-SET_01|02-ft §1+§8+§9]] · PB-01 kit + PB-02 setup + §1.5.
Refs: [About Checking](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-F8B47FBB-1276-4D74-BA89-0440CB4E4866) · [To Audit](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-3E786E2E-7F6A-4D89-8B2B-F749F1AC2B85) · [Plot 1:1](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Plotting-a-layout-in-paperspace-results-in-the-the-drawing-not-plotting-to-scale-in-AutoCAD.html) · [LISP en LT](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Unable-to-load-lisp-in-AutoCAD-LT.html)
