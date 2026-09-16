---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, kaizen, pdca, mejora-continua]
---

# Kaizen + PDCA

> Kaizen = mejora continua en pasos pequeños con toda la gente. PDCA (Plan-Do-Check-Act, Shewhart/Deming) = motor que la hace sistemática. Ritual del vault: **"Victoria + Mejora" 15 min/semana, 3 victorias en log.md**.

- [Definición](#definición)
- [PDCA paso a paso](#pdca-paso-a-paso)
- [Kaizen en construcción (lo repetible)](#kaizen-en-construcción-lo-repetible)
- [Kaizen diario en el estudio](#kaizen-diario-en-el-estudio)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Definición

**Kaizen** (改善, "cambiar para mejor"): mejoras pequeñas, acumulativas, propuestas por **quienes hacen el trabajo**, no solo por la dirección. **PDCA** es su ciclo operativo: planificar un cambio → probarlo en chico → medir → estandarizar o descartar. Sin proceso estándar previo no hay mejora que se sostenga: primero estándar, después PDCA encima (escalera Kaizen).

## PDCA paso a paso

| Fase | Pregunta | En el vault |
|------|----------|-------------|
| **Plan** | ¿Qué cambio probamos y cómo lo medimos? | A3 de 1 página en `proyectos/<x>/` o issue Leantime: problema, hipótesis, métrica (ej. "bajar búsqueda de archivos de 20→5 min") |
| **Do** | Probar en chico, tiempo acotado | Piloto 1 semana / 1 proyecto (ej. nueva nomenclatura solo en casa en construcción) |
| **Check** | ¿La métrica se movió? | Comparar antes/después con misma vara (tiempos, PPC, retrabajo) |
| **Act** | ¿Estandarizo o revierto? | Si funcionó → ficha en `wiki/estandares/` + anuncio en daily; si no → nota de aprendizaje en `lecciones-aprendidas/` |

El ciclo **nunca termina**: cada estándar nuevo es la base del próximo PDCA.

## Kaizen en construcción (lo repetible)

La objeción clásica ("cada obra es distinta") se resuelve con granularidad: buscar **lo repetible dentro de lo único** — ciclo de losa, colocación de bloques, replanteo, detalle de encuentro. Evidencia: programa 2,5 años en 13 edificios (México, losas postensadas, 200+ estudios de tiempos) que redujo ciclo de losa con PDCA + A3 por iniciativa.

Principios aplicados a obra/estudio:

- **Gemba:** ir donde pasa el trabajo (obra, mesa del dibujante), no teorizar en oficina.
- **Takt time:** ritmo = tiempo disponible / demanda (ej. 1 nivel/semana → cadencia de entrega de planos).
- **One-piece flow + pull:** el material/plano avanza cuando el siguiente lo pide, no en lotes gigantes.
- **Trystorming > brainstorming:** probar rápido en campo en vez de discutir en sala.
- **Estándares medibles:** cada mejora termina en estándar escrito o no existió.
- **Seguridad psicológica:** el que ejecuta propone; el error se analiza como sistema (ver [[wiki/glosario/conceptos/last-planner-system|last-planner-system]] PPC).

## Kaizen diario en el estudio

- **Daily Kaizen:** cada daily cierra con "¿qué traba hoy removemos?" (1 restricción/día).
- **Ritual semanal "Victoria + Mejora" (15 min):** 3 victorias a `log.md` + 1 mejora candidata a PDCA. Es la métrica de éxito del spec vault-cerebro.
- **Tablero Kaizen en Leantime:** idea board / backlog etiqueta `kaizen` → sprint siguiente. Ver [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] §6.

## Conceptos relacionados

- [[wiki/glosario/conceptos/lean|lean]]
- [[wiki/glosario/conceptos/retrospectivas|retrospectivas]]
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]
- [[wiki/glosario/conceptos/cinco-s-5s-archivos|cinco-s-5s-archivos]]

## Referencias

- Lean Construction Institute — PDCA in Lean: https://leanconstruction.org/lean-topics/pdca/ (verificado 2026-09-09 — Plan/Do/Check/Act + escalera Kaizen)
- Procore — Kaizen in Construction: https://www.procore.com/library/kaizen-construction (verificado 2026-09-09 — gemba, takt, trystorming, estándares)
- Kaizen Institute — Excellence in construction (caso Daily Kaizen): https://kaizen.com/insights/construction-excellence-operational-transformation/ (verificado 2026-09-09 — 200)
- IGLC 2025 — PDCA en 13 edificios México (time-motion, A3): https://doi.org/10.24928/2025/0123 (verificado 2026-09-09 — DOI activo)
