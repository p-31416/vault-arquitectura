---
tipo: glosario
fecha_creacion: 2026-06-30
tags: [prefijos, nomenclatura, documentacion, convenciones]
---

# Prefijos de documentación — filo, fram, spec, ft, log

Guía de los prefijos usados para nombrar archivos de documentación técnica en proyectos internos. Cada prefijo responde a una pregunta distinta.

| Prefijo | Pregunta | Rol | Contenido típico |
|---------|----------|-----|-------------------|
| `readme-` | **¿Cómo navego?** | Puerta de entrada | Guía del proyecto, organización, reglas. Sin número por ser el primer archivo a leer. |
| `00-filo-` | **¿Por qué?** | Manifiesto | Visión, principios rectores, qué aporta al estudio. Solo global. |
| `01-spec-` | **¿Qué logramos?** | Acuerdo macro | Alcance concreto: qué entra/sale, criterio de éxito. **Se crea primero.** |
| `02-ft-` | **¿Cómo se hace?** | Plan técnico | Paso a paso para lograr spec. |
| `03-log-` | **¿Qué falló?** | Bitácora | Fallos, iteraciones, bugs, correcciones. |
| `lisp-` | **¿El código?** | Script | Archivo `.lsp` de AutoLISP. Sin número, es el resultado. |

## Jerarquía conceptual

```
readme- →  ¿Cómo navego?     (puerta de entrada, léase primero)
00-filo →  ¿Por qué?         (manifiesto, inmutable en esencia)
01-spec →  ¿Qué logramos?    (acuerdo macro del nivel, se crea 1ro)
02-ft   →  ¿Cómo se hace?    (plan técnico, paso a paso)
03-log  →  ¿Qué falló?       (bitácora de iteraciones y bugs)
lisp-   →  ¿El código?       (script AutoLISP ejecutable)
```

## Cómo se relacionan

1. **`readme-`** es la puerta de entrada. Explica organización y reglas.
2. **`00-filo-`** define la visión general. Solo global.
3. **`01-spec-`** define los objetivos. Guía contra la que se verifica el desarrollo.
4. **`02-ft-`** define los pasos técnicos para implementar lo que spec definió.
5. **`03-log-`** registra los fallos e iteraciones.
6. **`lisp-`** contiene el código ejecutable.

> El desarrollo nunca debe alejarse de `01-spec-`. Si hay desvío, se actualiza spec primero y luego 02-ft.

## Ejemplos en MVP_01-dibujo_ia

| Archivo | Prefijo | Respuesta |
|---------|---------|-----------|
| `readme-mvp_01.md` | readme- | Puerta de entrada del MVP |
| `00-filo-mvp_01.md` | 00-filo- | Manifiesto (por qué, principios) |
| `01-spec-mvp_01.md` | 01-spec- | Spec viva del framework |
| `02-ft-mvp_01.md` | 02-ft- | Roadmap de niveles, decisiones técnicas |
| `03-log-mvp_01.md` | 03-log- | Transiciones entre niveles |
| `n_01-local/01-spec-n_01.md` | 01-spec- | Objetivos del nivel 1 (local con muros concéntricos) |
| `n_01-local/02-ft-n_01.md` | 02-ft- | Algoritmo paso a paso del nivel 1 |
| `n_01-local/lisp-local.lsp` | lisp- | Script AutoLISP comando LOC |
