---
tipo: concepto
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-10
tags: [hitl, human-in-the-loop, ia-jr, guardrails, gobernanza, pitautech]
idioma: es
---

# HITL — Human-in-the-loop

> La IA como JR con capacidades limitadas, reglas exactas, iterable y mejorable — con supervisión humana explícita y proporcional al riesgo.

Patrón de diseño donde personas permanecen involucradas en entrenar, revisar y guiar salidas y decisiones del sistema IA, en momentos clave del flujo.

- [[#Definición]]
- [[#Modalidades — in / on / before the loop]]
- [[#Guardrails por confianza — cómo opera Pitautech]]
- [[#IA como JR iterable — capacidades limitadas + reglas exactas]]
- [[#Anti-patrones y límites]]
- [[#Conceptos relacionados]]
- [[#Referencias]]
- [[#Fuentes bibliográficas — APA idioma original + [trad. propia]]]

## Definición

**Human-in-the-loop (HITL):** enfoque de IA donde personas permanecen involucradas en entrenar, revisar o guiar salidas y decisiones del sistema. En lugar de automatizar todo, HITL suma juicio humano donde precisión, contexto, seguridad o responsabilidad resultan críticas (Credo AI, 2026 — verificado 200).

Áreas típicas:

- **Revisión de datos de entrenamiento:** etiquetado, corrección y mejora de calidad antes/durante entrenamiento.
- **Validación de salidas:** revisión de outputs generados para confirmar precisión, seguridad, relevancia o alineación con uso previsto.
- **Manejo de casos borde:** intervención humana ante situaciones poco claras, inusuales o de alto riesgo.

> HITL traduce principios de gobernanza en controles operativos: define dónde el juicio humano aporta valor y cómo se revisan decisiones.

## Modalidades — in / on / before the loop

| Modalidad | Cómo participa la persona | Cuándo aplica en Pitautech |
|---|---|---|
| **Human-in-the-loop** (sincrónico) | Cada salida pasa por revisión humana antes de avanzar | CAD: validación de layers/bloques; `wiki/` antes de publicar (regla Mes 1: todo output IA pasa por revisión humana) |
| **Human-on-the-loop** (asincrónico, supervisión) | Sistema corre autónomo; persona monitorea umbrales y excepciones | Reuniones: Fathom transcribe → Vault → persona revisa excepciones y varianzas diarias (LPS learn) |
| **Human-before-the-loop** (validación previa) | Persona valida prompts/templates/SOPs antes de ejecutar | Agentes: prompts y templates versionados en `wiki/estandares/` validados antes de activar flujo |
| **Human-over / under / along** | Variantes de autoridad y encuadre (AAAI 2025 Preposition Salad) | Gobernanza: la autoridad de revisión avanza con nivel de riesgo (EU AI Act art.14) |

Principio: diseñar supervisión **proporcional al riesgo y adecuada al caso de uso** (Credo AI, OECD AI Principles, EU AI Act).

## Guardrails por confianza — cómo opera Pitautech

Flujo HITL típico: IA genera → humano revisa con criterios definidos → aprueba/edita/rechaza/escala → feedback alimenta mejora del sistema.

Guardrails mínimos Mes 1 (ver [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]]):

1. **Trazabilidad:** cada agente registra fuente, fecha y criterio aplicado.
2. **Umbral 0.70:** confianza <0.70 detiene y solicita humano; 0.70–0.95 envía a cola de revisión humana (guardrail n8n).
3. **Aprobación previa a `wiki/`:** ningún output IA entra a `wiki/` sin revisión humana.
4. **Feedback loop:** cada corrección humana alimenta siguiente versión de prompt/template (SER → reseeding).

Instrumentación: Toggl/clock + n8n estimated time + timestamps Fathom + PPC para medir confiabilidad. Ver [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-métricas-fricción]].

## IA como JR iterable — capacidades limitadas + reglas exactas

> La IA en Pitautech ocupa el lugar de un junior con **capacidades limitadas, reglas exactas, iterable y mejorable**, que reduce fricción con criterio medible y supervisión humana explícita (HITL).

| Atributo JR | Traducción técnica IA | Implementación Mes 1 |
|---|---|---|
| Capacidades limitadas | Scope acotado, sin creatividad autónoma | Agente Fathom solo transcribe→extrae temas/decisiones/pendientes; no decide por Emilia |
| Reglas exactas | Prompts, templates, checklists, SOPs versionados | `wiki/estandares/` + `wiki/glosario/` como instrucciones; guardrails por confianza |
| Iterable | PDCA / Kaizen / SER | Cada P-00x registra hipótesis→resultado→próximo experimento; Vault guarda delta |
| Mejorable | Feedback loop HITL → reseeding | Humano corrige output, corrección alimenta prompt/template siguiente |
| Reduce fricción con criterio medible | Métrica Ahorro(p), PPC, cycle time | Log de retorno; PPC Vault; on-time delivery |
| HITL explícito | Human-in/on/before por riesgo | Reunión: human-on-the-loop; CAD: human-in-the-loop |

Primera función: **recordar** (reunión → memoria computable), no diseñar. La creatividad permanece como territorio del arquitecto; la IA acompaña como copiloto de investigación, comparación y simulación.

## Anti-patrones y límites

- **Vigilancia total sin criterio:** poner humano en cada paso genera fatiga de revisión y sesgo humano reemplaza sesgo máquina (IAPP, SAS Voices).
- **HITL sin expertise definido:** "quién revisa" importa tanto como "dónde revisa" — requiere pensamiento crítico, estratificación de riesgo y alfabetización de negocio/sistema (IT Brew, IAPP).
- **HITL como etiqueta vacía:** sin principios guía, la supervisión no escala ni aporta control real (OECD, EU AI Act art.14).

> Avanza con la pregunta correcta: dónde ocurre la revisión, qué autoridad posee quien revisa y cómo esa supervisión afecta resultados.

## Conceptos relacionados

- [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]] — rol que diseña sistemas que habilita HITL
- [[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]] — filosofía Pitautech: primera función recordar
- [[wiki/glosario/interno/standares/ptech-metricas-friccion|ptech-metricas-friccion]] — métricas Ahorro_mes, humano vs máquina
- [[wiki/glosario/conceptos/kaizen|kaizen]] — PDCA que itera el loop HITL
- [[wiki/glosario/conceptos/seguridad-psicologica-aristotle|seguridad-psicologica-aristotle]] — condición para reportar varianzas y mejorar el loop
- [[wiki/glosario/conceptos/braintrust-pixar|braintrust-pixar]] — candor que nutre el feedback loop

## Referencias

- Credo AI — Human-in-the-loop glossary: https://www.credo.ai/glossary/human-in-the-loop — 200 — definición HITL + training/output/edge + oversight proporcional
- Singh, A. & Szajnfarber, Z. (2025). Preposition Salad: Placing humans & AI in/on/over/along/under 'the-loop'. *AAAI Spring Symposium*: https://ojs.aaai.org/index.php/AAAI-SS/article/download/35571/37726/39642 — 200 — taxonomía in/on/before/over/under/along
- OECD AI Principles — https://www.oecd.org/en/topics/artificial-intelligence.html — 200 — principios IA centrada en humanos citados en Credo
- EU AI Act art.14 — supervisión humana para sistemas de alto riesgo — citado vía Credo AI — 200
- Kaizen Institute — What is Lean construction: https://kaizen.com/insights/lean-construction-continuous-improvement-culture — 200 — Kaizen que itera HITL
- Lean Enterprise Institute — Continuous improvement: https://www.lean.org/lexicon-terms/continuous-improvement — 200 — mejora continua como base del loop
- `raw/research/2026-09-09-meta-arquitecto-pitautech.md` §Eje 4 — síntesis HITL + guardrails + tabla JR

## Fuentes bibliográficas — APA idioma original + [trad. propia]

- Fischer, G., & Giaccardi, E. (2004). Meta-design: A framework for the future of end-user development. *Communications of the ACM*. https://doi.org/10.1145/1015864.1015884 — **en** — [trad. propia]
- Singh, A., & Szajnfarber, Z. (2025). Preposition salad: Placing humans & AI in/on/over/along/under 'the-loop'. *AAAI Spring Symposium Series*. https://ojs.aaai.org/index.php/AAAI-SS/article/download/35571/37726/39642 — **en** — [trad. propia: Ensalada de preposiciones: ubicar humanos y IA en/sobre/bajo/a lo largo de 'the-loop'] — taxonomía modalidades HITL
- Credo AI. (s.f.). Human-in-the-loop — AI Glossary. https://www.credo.ai/glossary/human-in-the-loop — **en** — [trad. propia: Humano en el loop] — definición operativa HITL verificada 200
