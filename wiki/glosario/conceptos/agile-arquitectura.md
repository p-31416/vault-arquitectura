---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, agile, scrum, sprints, arquitectura]
---

# Agile para arquitectura

> Scrum/Kanban adaptados al estudio: sprints de diseño de 1–2 semanas, backlog de entregables, demo con comitente. Ritmo sin perder incumbencia profesional ni valor legal del plano.

- [Definición](#definición)
- [Scrum mínimo viable](#scrum-mínimo-viable)
- [Adaptación a fases de obra](#adaptación-a-fases-de-obra)
- [Sprints en Leantime](#sprints-en-leantime)
- [Límites y advertencias](#límites-y-advertencias)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Definición

Agile (Manifiesto 2001): **individuos e interacciones sobre procesos; producto funcionando sobre documentación exhaustiva; colaboración con el cliente sobre negociación contractual; respuesta al cambio sobre plan rígido**. En arquitectura el "producto funcionando" = **entregable revisable cada sprint** (lámina, modelo, render, cómputo), no software.

## Scrum mínimo viable

| Elemento | Software | Estudio de arquitectura |
|----------|----------|------------------------|
| Sprint | 2 semanas código | 1–2 semanas, un recorte de alcance loco→posible (ej. "anteproyecto ala norte") |
| Backlog | user stories | entregables del vault (`proyectos/<x>/entregables/`) priorizados por valor/riesgo |
| Planning | lunes sprint | lunes: qué entra según capacidad real (WIP de [[wiki/glosario/conceptos/kanban|kanban]]) |
| Daily | 15 min standup | 15 min: qué terminé / qué me bloquea (bloqueo = restricción LPS) |
| Review/demo | demo software | **demo con comitente**: mostrar, no contar (plano + render + cómputo) |
| Retrospectiva | qué mejorar | ver [[wiki/glosario/conceptos/retrospectivas|retrospectivas]] + [[wiki/glosario/conceptos/kaizen|kaizen]] |

Roles livianos: **Product Owner** = Sol (prioriza, habla con comitente) · **Equipo** = dibujantes/BIM/ingenieros · **Facilitador** = quien cuida el tablero (rotativo, no un "Scrum Master" full-time en estudio chico).

## Adaptación a fases de obra

- **Concurso/anteproyecto:** sprint 1 semana, mucha divergencia, demo = láminas concepto.
- **Documentación/legajo:** sprint 2 semanas, pull planning (ver [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]), demo = set de planos con DoD legal (sello, escalas, rótulos).
- **Obra:** el sprint se subordina al **plan semanal LPS** — Agile pone el ritmo, LPS pone las promesas confiables.
- Regla de oro: **ningún sprint entrega un plano "casi"** — sale con DoD o no sale (valor jurídico del plano en ARG).

## Sprints en Leantime

Leantime trae **Sprint Management** nativo: se crean sprints con fecha, se asignan To-Dos, se cierra con retrospectiva integrada. Detalle operativo en [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] §3.

## Límites y advertencias

- Agile no reemplaza normativa (código edificación, incumbencia Ley 24.335): el cambio bienvenido **dentro** del marco legal.
- Evitar "Sprint theater": si cada demo se pospone, el problema es capacidad/WIP, no el método.
- En equipo de 2–3, Scrum completo sobra: usar **sprints + kanban + retro** y listo.

## Conceptos relacionados

- [[wiki/glosario/conceptos/kanban|kanban]]
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]
- [[wiki/glosario/conceptos/retrospectivas|retrospectivas]]
- [[wiki/glosario/conceptos/okr-goals|okr-goals]]

## Referencias

- Manifiesto Agile (2001, 17 firmantes): https://agilemanifesto.org/ (verificado 2026-09-09 — 200)
- Scrum.org — What is Scrum: https://www.scrum.org/resources/what-scrum-module (verificado 2026-09-09 — 200)
- Leantime — Sprint Management + Retrospectives: https://leantime.io/ (verificado 2026-09-09 — 200) y https://github.com/Leantime/leantime (verificado 2026-09-09 — feature list)
