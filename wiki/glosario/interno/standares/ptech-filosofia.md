---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-10
tags: [filosofia, pitautech, vault, investigacion, arquitectura, ptech]
idioma: es
---

# Filosofía Pitautech

> Automatizar la fricción. Conservar el conocimiento. Liberar el pensamiento.

Filosofía operativa de Pitautech — laboratorio I+D aplicado a estudios de arquitectura. Prefijo `ptech-` en `standares/` reserva espacio para futuros documentos propios de Pitautech (hasta que requiera carpeta propia). Ver `[[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]]`.

## Índice

- [[#Idea central — capacidad, no horas]]
- [[#La pregunta que origina la propuesta]]
- [[#Tres modos del conocimiento]]
- [[#La primera función de la IA — recordar]]
- [[#Vault como memoria intelectual computable]]
- [[#Proyecto como unidad de aprendizaje]]
- [[#I+D como método científico aplicado]]
- [[#Rol de la IA — meta arquitecto y JR iterable]]
- [[#Visión — estudio que aprende]]
- [[#Principio rector]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Idea central — capacidad, no horas

Programa de Investigación, Desarrollo e Implementación con **capacidad prevista de 3h/día hábil (60hs/mes)**. La cifra expresa disponibilidad y planificación; el valor está en lo que produce: investigación, hipótesis, experimentos, prototipos, procesos, documentación y conocimiento reutilizable.

> Capacidad, no horas. Investigación que produce sistemas.

## La pregunta que origina la propuesta

La pregunta que origina la propuesta:

> ¿Qué debería hacer una inteligencia artificial para que un arquitecto pueda dedicar más tiempo a pensar arquitectura?

La IA ocupa el lugar de la fricción, con posibilidad de ampliar el espacio creativo.

## Tres modos del conocimiento

### Lo repetible → sistema

Aquello que se repite con criterio estable avanza hacia estándar, template, checklist, automatización, agente, protocolo y validación. Ejemplos: nombres, capas, estructuras, documentación, reuniones, agenda.

### Lo aprendido → memoria

Cada proyecto deja decisiones, soluciones, criterios, referencias, detalles y aprendizajes que vuelven al sistema.

### Lo desconocido → creatividad

La parte que requiere descubrir solución nueva permanece como territorio del arquitecto. La IA acompaña como copiloto instrumento de investigación, comparación, simulación y exploración, con el propósito de proteger y ampliar ese espacio creativo.

## La primera función de la IA — recordar

> La primera función de la IA en un estudio es recordar.

Flujo: reunión → grabación/transcripción → procesamiento → temas/decisiones/pendientes/responsables/fechas/referencias → incorporación al Vault → agenda → próxima reunión. La automatización preserva la conversación arquitectónica.

## Vault como memoria intelectual computable

El Vault avanza hacia memoria intelectual computable del estudio, con capacidad de conectar y recorrer:

personas ↔ proyectos ↔ decisiones ↔ procesos ↔ documentos ↔ referencias ↔ soluciones ↔ aprendizajes

Aspiración: consultable, semánticamente buscable, recorrible, conectado, documentado, auditable, reutilizable y evolutivo.

## Proyecto como unidad de aprendizaje

Cada proyecto opera como experimento real:

proyecto → experiencia → datos → decisiones → conocimiento → proceso → documentación → automatización → aprendizaje → próximo proyecto

Cada proyecto deja huella y alimenta al siguiente. La organización avanza hacia una organización que aprende de sus propios proyectos.

## I+D como método científico aplicado

Ciclo: observación → pregunta → hipótesis → investigación → experimento → resultado → evaluación → protocolo → implementación → aprendizaje. Cada experimento genera conocimiento sobre una forma de trabajar.

Registro por pomodoros como métrica interna de capacidad; los resultados permanecen como unidad de valor.

| ID | Problema | Actividad | Hipótesis | Resultado | Próximo |
|---|---|---|---|---|---|
| P-001 | Reuniones | Transcripción + automatización | La reunión avanza hacia memoria automática | Arquitectura posible | Prototipo |
| P-002 | CAD | Estándares | Parte de la preparación avanza hacia sistema | Oportunidades detectadas | Test |
| P-003 | Referencias | Taxonomía | Estructura común conecta referencias | Taxonomía inicial | Validación |

## Rol de la IA — meta arquitecto y JR iterable

> *Designing the design process becomes a first-class activity* — diseñar el proceso de diseño avanza hacia actividad de primer orden (Fischer & Giaccardi, 2004) [trad. propia]

La IA en Pitautech avanza como **JR con capacidades limitadas, reglas exactas, iterable y mejorable**, que reduce fricción con criterio medible y supervisión humana explícita. Su primera función es **recordar** (reunión → memoria computable); la segunda, habilitar que otros diseñen mejor.

- **Meta arquitecto** — rol que diseña sistemas que diseñan arquitectura (Vault, taxonomías, templates, agentes, protocolos). Ver [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]]: definición unificada meta arquitecto + meta arquitectura + arquitectura de sistemas (systems architect), tabla tradicional vs meta vs con IA, y contexto temporal Fischer 2004 → BIG/Foster 2015–2020 → Karpathy 2022–2023 → MCP 2024–2025.
- **Meta arquitectura** — arquitectura de segundo orden: CDE/Vault + estándares + flujos Fathom→Vault→agenda + agentes con guardrails [[wiki/glosario/conceptos/hitl-human-in-the-loop|HITL]]. Se evalúa con [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-métricas-fricción]] (Ahorro_mes, PPC, ROI).
- **IA como JR iterable** — capacidades limitadas (scope acotado), reglas exactas (prompts/templates/SOPs versionados), iterable por PDCA/Kaizen/SER y mejorable por feedback HITL. Opera en régimen human-in/on/before-the-loop proporcional al riesgo; confianza <0.70 detiene y solicita humano. Ver [[wiki/glosario/conceptos/hitl-human-in-the-loop|hitl-human-in-the-loop]] + [[wiki/glosario/conceptos/diseno-colaborativo|diseño colaborativo]] (underdesign + Braintrust).

> **Traer lo mejor de diferentes disciplinas** — Fischer (meta-design), Karpathy (cerebro digital), MCP (protocolo agentes), Agile Manifesto, Kaizen/Lean, Last Planner, Design Sprint (GV), Pixar Braintrust y seguridad psicológica avanzan como capas del mismo sistema. El contexto temporal (2004 meta-design, 2015–2020 Design Technology en BIG/Foster/OMA, 2022–2023 Karpathy, 2024–2025 MCP) avanza para medir actualidad y elegir qué adoptar hoy. Ver [[wiki/glosario/conceptos/meta-arquitecto#Cross metodológico — Kaizen, Lean, Agile, Last Planner, Design Sprint|meta-arquitecto §Cross metodológico]] + [[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral]].

Implementación: **Leantime** como gestor de proyectos donde viven OKRs, sprints Observar/Experimentar/Sistematizar y tablero Kanban del LPS + Agile del estudio.

## Visión — estudio que aprende

Pitautech proyecta metodología de transformación de estudios:

problema real → investigación → experimento → solución → documentación → conocimiento → módulo reutilizable → nueva implementación → nuevo aprendizaje

Cada proyecto contiene el germen del siguiente sistema.

La pregunta de fondo:

> ¿Cómo producimos arquitectura? ¿Cómo producimos conocimiento mientras producimos arquitectura? ¿Cómo ese conocimiento vuelve al proceso para producir mejor la próxima vez?

Pitautech trabaja sobre el ciclo experiencia → información → conocimiento → proceso → automatización → aprendizaje.

Programa piloto 90 días:

- **Mes 1 OBSERVAR:** ¿Cómo trabaja realmente el estudio? Relevamiento, mapa operativo, fricciones, auditoría, Vault inicial.
- **Mes 2 EXPERIMENTAR:** ¿Qué podemos transformar? Prototipos, agentes, automatizaciones, Vault, taxonomías.
- **Mes 3 SISTEMATIZAR:** ¿Qué aprendimos y qué avanza hacia sistema? Evaluación, protocolos, capacitación, roadmap.

Impacto: 90 días → primeros sistemas, 6 meses → acumulación, 1 año → memoria + procesos + datos + aprendizaje.

## Principio rector

> La inteligencia artificial acompaña aquello que hoy ocupa cabeza, memoria y tiempo, para que el arquitecto disponga de espacio para proyectar mejor.

> La creatividad requiere espacio. Pitautech trabaja para construir ese espacio.

Frases comerciales (versión positiva):

- Diseñamos el sistema de trabajo que hace útiles las herramientas.
- Más arquitectura. Menos fricción.
- Transformar experiencia en conocimiento, conocimiento en procesos y procesos en innovación.
- Construir un estudio que aprenda de cada proyecto.

> Nota de voz: "¿Qué querés trabajando para vos? ¿Alguien que avance más allá de lo establecido o alguien que cumpla a reglamento? Fui ambas y disfruto más este lugar. Busco certeza para construir proyectos realmente aplicables que mejoren el ejercicio de la práctica arquitectónica y explorar hasta dónde podemos llegar."

## Conceptos relacionados

- [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]] — meta arquitecto + meta arquitectura + arquitectura de sistemas (systems architect)
- [[wiki/glosario/conceptos/hitl-human-in-the-loop|hitl-human-in-the-loop]] — HITL, guardrails por confianza, JR iterable
- [[wiki/glosario/conceptos/diseno-colaborativo|diseno-colaborativo]] — co-diseño, underdesign, SER, Braintrust
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]] — raw → entidades → wiki
- [[wiki/glosario/conceptos/vault-visual|vault-visual]] — Vault con fotos/imágenes + curaduría
- [[wiki/glosario/conceptos/ia-lab-partnership|ia-lab-partnership]] — partnership co-construido, caso fundador
- [[wiki/glosario/conceptos/lean|lean]] — eliminar desperdicio / flujo pull
- [[wiki/glosario/conceptos/kaizen|kaizen]] — Kaizen + PDCA, mejora continua
- [[wiki/glosario/conceptos/agile-arquitectura|agile-arquitectura]] — Agile/Scrum sprints
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]] — LPS, PPC, promesas confiables
- [[wiki/glosario/conceptos/design-sprint|design-sprint]] — Design Sprint GV 5 días
- [[wiki/glosario/conceptos/braintrust-pixar|braintrust-pixar]] — candor sin jerarquía
- [[wiki/glosario/conceptos/okr-goals|okr-goals]] — OKRs trimestrales y métricas
- [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-metricas-friccion]] — métricas fricción humano vs máquina

## Referencias

- Fuente interna: `raw/brainstorm/Pitautech_Propuesta_I+D_Arquitectura_Vault.md` (2026-09-09, 18 capítulos) + `raw/research/2026-09-09-meta-arquitecto-pitautech.md` (18 fuentes 200)
- Fischer, G. & Giaccardi, E. (2004). Meta-design — https://doi.org/10.1145/1015864.1015884 — 200 — "Designing the design process becomes a first-class activity" [trad. propia]
- Fischer, G. & Giaccardi, E. (2006). Meta-design framework — https://doi.org/10.1007/1-4020-5386-X_19 — 200
- Andrej Karpathy — Cerebro digital / personal knowledge brain — https://karpathy.github.io/ — 200 — técnica raw → entidades → wiki
- Agile Manifesto — https://agilemanifesto.org/ — 200 — base Agile para sprints del estudio
- Lean Enterprise Institute — Continuous improvement: https://www.lean.org/lexicon-terms/continuous-improvement — 200 — Kaizen + flujo + pull
- Kaizen Institute — What is Lean construction: https://kaizen.com/insights/lean-construction-continuous-improvement-culture — 200 — Lean construction + Kaizen Office
- Lean Construction Institute — Last Planner System: https://leanconstruction.org/lean-topics/last-planner-system — 200 — PPC + 5 conversaciones
- GV — Design Sprint: https://www.gv.com/sprint — 200 — sprint 5 días
- Credo AI — Human-in-the-loop: https://www.credo.ai/glossary/human-in-the-loop — 200 — HITL + guardrails
- BIG — https://www.big.dk/ — 200 — Design Technology; Foster + Partners — https://www.fosterandpartners.com/ — dominio oficial 200 + insights AI
- ISO 19650 — Metodología BIM / CDE — https://www.iso.org/standard/68078.html — 200 — referencia para Vault como CDE
- `[[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]]` · `[[wiki/glosario/conceptos/hitl-human-in-the-loop|hitl]]` · `[[wiki/glosario/conceptos/diseno-colaborativo|diseño colaborativo]]` · `[[specs/260910-plan-trimestral-unificado-studio-os-emilia]]` · `[[specs/260909-esquema-mes1-60hs-studio-os-emilia]]`
