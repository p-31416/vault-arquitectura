---
tipo: spec
mvp: 02
fecha_creacion: 2026-06-30
ultima_actualizacion: 2026-09-27
tags: [mvp_02, spec, generico, DoD]
---

# MVP_02 — Spec (genérica)

> **Acuerdo macro**: Documentar y estandarizar las reglas de dibujo AutoCAD del estudio, con registro de decisiones (ADR) y herramientas AutoLISP que apliquen dichas reglas automáticamente.
>
> Este spec es **genérico**: define la estructura y el orden que todo SET (`SET_0x-XXX_Descripcion/`) debe seguir. El detalle vive en cada carpeta SET. El primer SET desarrollado (SET_01-REP) fija el precedente; los siguientes lo heredan y ajustan.

## Criterios de éxito ("DoD")

> **"DoD"** = *Definition of Done* (término de disciplinas ágiles/software). Criterio verificable que marca un item como completado.
>
> Orden obligatorio para todo SET:

- [ ] **1. SETEO — Unidades, escalas, layout.** `UNITS`, `INSUNITS`, `MEASURE`, lista de escalas (`SCALELISTEDIT`), layout modelo por copiar (viewport + carátula + escala gráfica). Detalle en `SET_0x/.../docs/template-dwt.md`. → SET_01: `SET_01-REP_Replanteo/docs/template-dwt.md` (metros, 1:50)
- [ ] **2. LAYERS — Nomenclatura + propiedades.** NOMBRES con prefijos (`R-/A-/S-/E-/P-/G-/M-/V-/F-` según Kit), TIPO de línea, VALOR de línea (serie ISO 128-2), capa AUX no imprimible (`G-AUXI`, `G-VPRT`). Detalle en `SET_0x/.../SET_0x-XXX.md` §2. → SET_01: 22 capas (7 REP + 7 GEN + 4 ARQ + 4 EST)
- [ ] **3. CTB — Plot style (opcional).** Asociado a los layers. Layers siempre **color index** salvo indicación (ej: hatches con colores verdaderos R,G,B). Si no se genera CTB propio, usar `monochrome.ctb` (standard AutoCAD). Detalle en `SET_0x/.../docs/ctb.md`. → SET_01: `EP-ISO.ctb` (común), `docs/ctb.md`
- [ ] **4. TEXTSTYLES.** Nombres, fuentes, alturas (anotativos). Detalle en spec del SET. → SET_01: `EP-2.5`, `EP-3.5`
- [ ] **5. DIMENSION STYLES.** Nombre, fuente, tamaño, offsets, flechas, color. Detalle en spec del SET. → SET_01: `EP-ARQ`
- [ ] **6. BLOQUES.** Biblioteca (`.dwg`), nombres, capas. Detalle en spec del SET. → SET_01: marca eje, punto PTOS, cota nivel
- [ ] **7. BLOQUES DINÁMICOS / CON ATRIBUTOS (si aplica).** Parámetros, atributos, cómputo vía `DATAEXTRACTION`/`ATTEXT` (recuento, planillas, extracción). Detalle en spec del SET. → SET_01: R-PTOS (ID,X,Y,Z) → cuadro coordenadas
- [ ] **8. TEMPLATE (.dwt).** Creación a partir de 1–7. Ruta en `activos/` (NO en git). Detalle en `SET_0x/.../docs/template-dwt.md`. → SET_01: `activos/.../SET_01-REP/SET_01-REP.dwt`
- [ ] **9. AUTOLISP (si aplica).** `.lsp` en `SET_0x/.../lisp/` que aplica 1–8. Detalle en spec §AutoLISP. → SET_01: `lisp/SET_01-REP.lsp`, comando `SET-01-REP`
- [ ] **10. GLOSARIO DEL SET.** Términos propios → `wiki/estandares/acad/...`, referenciando conceptos base en `wiki/glosario/software/autocad`. → SET_01: pendiente (replanteo, NPT, LM, ochava, ejes)

## Historial de cambios

| Fecha | Cambio |
|-------|--------|
| 2026-06-30 | Spec inicial |
| 2026-09-27 | Manifiesto reescrito (sesión @brainstormy). Frase: "El dibujo es un documento y también un lenguaje". |
| 2026-09-27 | Reescritura genérica v2: estructura 10 items ordenados (seteo → layers → CTB → textos → cotas → bloques → dinámicos → template → lisp → glosario). "DoD" entre comillas con referencia wiki futura. Detalle delegado a SET_01-REP. |
