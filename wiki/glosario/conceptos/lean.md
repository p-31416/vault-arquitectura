---
tipo: concepto
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, lean, lean-construction, desperdicio, valor]
---

# Lean (construcción + estudio)

> Maximizar valor, minimizar desperdicio, flujo pull y perfección continua. Raíz de todo lo demás: Kanban, LPS, Kaizen y 5S son Lean aplicado.

- [Definición](#definición)
- [5 principios](#5-principios)
- [8 desperdicios en el estudio](#8-desperdicios-en-el-estudio)
- [Lean Construction (diferencia con fábrica)](#lean-construction-diferencia-con-fábrica)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Definición

Lean (Toyota → Womack & Jones → Lean Construction Institute): sistema para **entregar más valor con menos desperdicio**, con flujo continuo tirado por la demanda (pull) y mejora perpetua. En construcción lo adapta el LCI: no se copian herramientas de fábrica, se adoptan principios (los proyectos son únicos, el trabajo es temporal y multi-actor).

## 5 principios

1. **Valor** — definido por el cliente (comitente/municipio/usuario), no por el estudio. Pregunta: ¿paga o exige esto alguien?
2. **Flujo de valor** — mapear todos los pasos del entregable y marcar los que no agregan valor.
3. **Flujo continuo** — que el trabajo avance sin colas ni lotes gigantes (ver [[wiki/glosario/conceptos/kanban|kanban]]).
4. **Pull** — producir cuando el siguiente lo pide (el comitente pide demo → se produce demo; no renders "por si acaso").
5. **Perfección** — mejora sin fin vía [[wiki/glosario/conceptos/kaizen|kaizen]] + [[wiki/glosario/conceptos/retrospectivas|retrospectivas]].

## 8 desperdicios en el estudio

| Desperdicio | Ejemplo estudio | Antídoto vault |
|-------------|----------------|----------------|
| Defectos/retrabajo | Plano v7 por error de cota | DoD + revisión interna Kanban |
| Sobreproducción | 12 renders que nadie pidió | Pull: demo agenda qué se produce |
| Espera | Dibujante parado por falta dwg base | Make-ready LPS, restricción visible |
| Talento no usado | Dibujante senior haciendo rótulos | Estandarizar + Lisp/AutoLISP |
| Transporte | Archivos por WhatsApp/mail/USB | Vault único + `activos/` |
| Inventario | 400 GB de "final_FINAL2" | 5S digital, Seiri con red tagging |
| Movimiento | Buscar archivos 20 min/día | Nomenclatura + índice (Seiton) |
| Sobre-proceso | Memoria de 40 páginas que nadie lee | Plantillas + prompt-packs |

## Lean Construction (diferencia con fábrica)

Obra ≠ línea de montaje: producto único, sitio temporal, decenas de contratistas. Por eso Lean Construction (Ballard, Howell, Koskela) pone el foco en **confiabilidad del flujo** (LPS, PPC) y **aprendizaje entre proyectos** (el vault es exactamente eso: memoria organizacional). La "fábrica" del estudio es el **proceso de proyecto**, y su producto es el legajo + la obra.

## Conceptos relacionados

- [[wiki/glosario/conceptos/kanban|kanban]]
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]
- [[wiki/glosario/conceptos/kaizen|kaizen]]
- [[wiki/glosario/conceptos/cinco-s-5s-archivos|cinco-s-5s-archivos]]
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]

## Referencias

- Lean Construction Institute: https://www.leanconstruction.org/ (verificado 2026-09-09 — 200)
- LCI — PDCA in Lean: https://leanconstruction.org/lean-topics/pdca/ (verificado 2026-09-09 — mejora continua en diseño/construcción)
- US EPA — Lean Thinking & Methods (5S, JIT/Kanban, Kaizen): https://www.epa.gov/lean (verificado 2026-09-09 — 200)
- Womack & Jones (2003) *Lean Thinking* — Free Press
