---
tipo: manifiesto
mvp: 02
fecha_creacion: 2026-06-30
ultima_actualizacion: 2026-06-30
tags: [mvp_02, filo, manifiesto]
---

# MVP_02 — Manifiesto: Estándares que funcionan

## Por qué

Cada oficina de arquitectura tiene estándares AutoCAD. En la práctica:

- El layer `A-WALL` de un proyecto no es el mismo `A-WALL` de otro.
- El CTB se copia del proyecto anterior y nadie recuerda por qué el muro se plotea con peso 0.35.
- Un nuevo dibujante pasa dos semanas descubriendo las reglas no escritas.

Este MVP existe para que **cada decisión de estándar tenga un por qué documentado**, sea reproducible y evolucione con el estudio.

## Principios

1. **Opinados pero justificados**: todo default tiene una razón (medida real, práctica de obra, requisito de presentación).
2. **Evolutivos**: los estándares cambian cuando la práctica demuestra que algo se puede mejorar.
3. **AutoLISP como enforcements**: el estándar se aplica con herramientas, no con buena voluntad.
4. **Documentación viva**: los `.md` son la fuente de verdad. Los binarios (DWT, CTB) cuelgan de ellos.
5. **Capa de sync automática al glosario → wiki**: cada comando nuevo documentado en el glosario se refleja en la wiki técnica.

## Scope

**Qué entra**: layer standards, plot styles, text/dim styles, templates, bloques estándar, naming de planos, reglas de presentación.

**Qué NO entra**: flujos de dibujo paramétrico (eso es MVP_01), BIM (wiki/estandares/tecnico/bim-*), gestión de oficina (wiki/estandares/oficina/).
