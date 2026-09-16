---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, retrospectiva, rituales, mejora-continua]
---

# Retrospectivas breves

> Ritual de cierre de sprint: qué funcionó, qué no, 1 experimento para el próximo. 30 min máximo. Sin retrospectiva, el sprint es solo un calendario.

- [Definición](#definición)
- [Formato 30 min](#formato-30-min)
- [Reglas](#reglas)
- [Retro en Leantime + vault](#retro-en-leantime--vault)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Definición

Práctica Scrum (último evento del sprint): el equipo inspecciona **su proceso** (no el producto) y acuerda **una** mejora accionable. En el vault se fusiona con el Nivel 5 de [[wiki/glosario/conceptos/last-planner-system|last-planner-system]] (Learn) y el ritual "Victoria + Mejora".

## Formato 30 min

| Min | Bloque | Técnica |
|-----|--------|---------|
| 0–5 | Check-in | Una palabra: ¿cómo llega cada uno? |
| 5–12 | Datos | PPC del sprint, throughput, lead time (sin opiniones todavía) |
| 12–20 | Plus/Delta | Qué estuvo bien / qué puede estar mejor (notas 1 min en silencio, luego agrupar) |
| 20–27 | 5 porqués | Solo sobre el delta de mayor impacto; causa sistema, no persona |
| 27–30 | 1 experimento | Formato: "Creemos que ___, lo probamos ___ durante ___ y medimos ___" → entra al próximo sprint como task `kaizen` |

## Reglas

- **Blameless:** se habla del sistema (plantilla, WIP, info que faltó), nunca de quién.
- **Una sola mejora:** tres mejoras = ninguna. WIP también aplica a las mejoras.
- **Timebox estricto:** 30 min con timer; lo no tratado va al backlog.
- **Participa quien ejecuta:** dibujantes/BIM primero, dirección escucha.
- Frecuencia: cada cierre de sprint (1–2 sem) + versión mensual de 60 min con comitente interno (Sol+Emilia) para OKRs.

## Retro en Leantime + vault

Leantime trae módulo **Retrospectives** nativo: se crea la retro del sprint, se cargan plus/delta y sale con action items que son tasks del próximo sprint. Salida obligatoria al vault: nota `raw/sessions/YYYY-MM-DD-retro-sprint-N.md` con PPC + experimento + responsable, y las 3 victorias a `log.md` (entradas nuevas arriba).

## Conceptos relacionados

- [[wiki/glosario/conceptos/kaizen|kaizen]]
- [[wiki/glosario/conceptos/agile-arquitectura|agile-arquitectura]]
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]
- [[wiki/glosario/conceptos/okr-goals|okr-goals]]

## Referencias

- Scrum.org — What is a Sprint Retrospective: https://www.scrum.org/resources/what-is-a-sprint-retrospective (verificado 2026-09-09 — 200)
- Atlassian — Sprint retrospectives (formato + ideas): https://www.atlassian.com/agile/scrum/retrospectives (verificado 2026-09-09 — 200)
- Leantime — Retrospectives module: https://leantime.io/ (verificado 2026-09-09 — 200) y https://github.com/Leantime/leantime (verificado 2026-09-09 — feature list)
