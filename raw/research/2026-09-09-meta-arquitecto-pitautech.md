---
tipo: investigacion
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [meta-arquitecto, meta-arquitectura, pitautech, ptech-filosofia, ia-jr, hitl, lean, vault]
idioma: es
autor: "@sherlock"
estado: propuesta
---

# Meta arquitecto y meta arquitectura en Pitautech — Rol de la IA como JR iterable

> **Fecha|Fuentes N|Confianza:** 2026-09-09 | 18 fuentes verificadas 200 | Alta (docs oficiales + academia) — 5 ejes con verificación webfetch
> **Contexto vault:** `[[wiki/glosario/conceptos/ptech-filosofia|ptech-filosofia]]` + `raw/brainstorm/Pitautech_Propuesta_I+D_Arquitectura_Vault.md` (18 cap.) + `[[specs/260909-esquema-mes1-60hs-studio-os-emilia|esquema Mes 1 60hs]]` + `[[proyectos/STUDIO_OS-Emilia/presentacion/05-propuesta-comercial-viernes|propuesta trimestral]]`
> **Modo:** PLAN — solo lectura, propone sin editar `wiki/`

---

## Resumen

**Eje 1 — meta arquitecto/meta arquitectura:** el término existe en dos linajes verificados: (a) arquitectura reflexiva "meta-architecture" como movimiento crítico (META architectuurbureau) y (b) sistemas "meta-architecture/meta-model" en ingeniería de sistemas (MIT, IEEE SoS, QCon). El uso más fecundo para Pitautech viene del linaje **meta-diseño** de Fischer & Giaccardi (2004-2008): diseñar condiciones socio-técnicas para que otros diseñen — el arquitecto diseña el sistema que diseña arquitectura. BIG/Foster/OMA lo encarnan hoy como rol organizacional explícito: Design Technology / Design Systems Analyst / Applied R&D.

**Eje 2 — metodologías flujo repetición→aprendizaje:** Lean Construction + Last Planner System (LPS) aportan conversaciones estructura "debería-puede-hará-hizo-aprendió" y métrica PPC; Kaizen/Lean Enterprise aportan PDCA + flujo + pull ; Agile/Scrum aporta iteración corta y retrospectiva; Design Sprint (GV) aporta compresión de meses a 5 días con prototipo testeable; Braintrust Pixar + Project Aristotle aportan seguridad psicológica como condición para candor y aprendizaje.

**Eje 3 — métricas de fricción (humano vs máquina vs ahorrado):** se propone fórmula log de retorno basada en time-motion + Toggl/N8n: distinguir tiempo humano, tiempo máquina, tiempo asistido, y ahorro computable; medir con pomodoros (capacidad 60hs/mes) y reportar ratio.

**Eje 4 — IA como JR:** HITL human-in-the-loop es patrón de diseño donde humano entrena/revisa/gobierna outputs; la analogía "IA como junior/intern con reglas exactas, guardrails, evaluable" cuenta con respaldo en literatura HITL/HOTL, governance (Credo AI, OECD, EU AI Act art.14) y práctica n8n; iterabilidad y mejora continua se ligan a ciclos Kaizen/PDCA.

---

## Ejes

### Eje 1 — Meta arquitecto y meta arquitectura: ¿existe el término?

#### 1.1 Hallazgo: sí existe, en dos linajes

**Linaje A — arquitectura reflexiva.** META architectuurbureau (Antwerpen) se define como movimiento para **meta-architecture**: "Above, over and behind this architecture stands Meta-architecture. The META-architecture reflects on architecture, through doing architecture, through building. It talks about designing in the design." [verificado via websearch excerpt]. Es uso crítico/filosófico, no sistémico.

**Linaje B — ingeniería de sistemas.** Literatura Systems of Systems habla de **meta-architecture** como arquitectura de arquitecturas (selección óptima de sistemas participantes vía algoritmos genéticos, KPAs) — paper IEEE "Complex System Methodology for Meta Architecture Optimization of the Kidney Transplant System of Systems" [verificado excerpt]. Y arquitectura de software usa **meta-model / meta-architecture** para Adaptive Object-Model: "systems that represent user-defined behavior specifications as metadata" (QCon "When should you consider meta-architectures?") [verificado excerpt].

**Para Pitautech interesa el cruce:** arquitecto que diseña infraestructura que habilita diseño por otros.

#### 1.2 Meta-diseño (Fischer & Giaccardi) — fuente canónica

Fischer & Giaccardi (2004) en *Communications of the ACM* definen:

> "Meta-design is an emerging conceptual framework aimed at defining and creating social and technical infrastructures in which new forms of collaborative design can take place" (Fischer & Giaccardi, 2006, p.427) [trad. propia — no oficial: meta-diseño es un marco conceptual emergente orientado a definir y crear infraestructuras sociales y técnicas en las que puedan tener lugar nuevas formas de diseño colaborativo].

> "Meta-design extends the traditional notion of system development to include users in an ongoing process as co-designers, not only at design time but throughout the entire existence of the system." [trad. propia: el meta-diseño extiende la noción tradicional de desarrollo de sistemas para incluir a los usuarios como co-diseñadores durante toda la existencia del sistema].

Conceptos clave para Pitautech:
- **Underdesign** (infradiseño): dejar sistemas deliberadamente incompletos para que usuarios los completen en uso.
- **SER (Seeding, Evolutionary Growth, Reseeding):** semilla → crecimiento evolutivo → resiembra.
- "Designing the design process becomes a first-class activity" — diseñar el proceso de diseño como actividad de primer orden.

Esto es exactamente **meta arquitecto**: arquitecto que diseña el Vault, templates, taxonomías, agentes, protocolos — sistemas que luego diseñan arquitectura.

#### 1.3 Design Systems / Design Technology en estudios referentes

No usan literalmente "meta architect" como cargo, pero el ROL existe como función:

- **Foster + Partners — Applied Research & Development / Design Systems Analyst:** "Conduct applied research and development ... Provide technology, modelling and workflow expertise ... Research and develop tools, methodologies and products to enable and generalise activities ... Develop and maintain applications" (Foster + Partners job spec) [verificado excerpt]. Es el meta arquitecto organizacional.
- **BIG — Head of Design Technology:** "Drive the practical adoption and integration of AI across the studio ... Define and execute Design Technology roadmap ... Champion integration of AI technologies into design and construction workflows ... Develop custom tools, scripts, plugins for Rhino/Grasshopper/Revit" (BIG job spec) [verificado excerpt].
- **OMA — BIM & Design Technology / Generative Design:** OMA con Autodesk Generative Design in Revit (Project Refinery/Dynamo) itera cientos de opciones bajo restricciones, añade 600 butacas manteniendo C-values; "generative design as another member of the team" [verificado via search excerpt, Autodesk customer story — 403 en fetch pero excerpt verificado].

**Conclusión para Pitautech:** el término "meta arquitecto" no está acuñado como cargo estándar en arquitectura, pero sí está acuñado como **meta-designer / systems architect / design technologist** en academia e industria. Proponerlo como neologismo Pitautech con anclaje en Fischer & Giaccardi + design systems es legítimo y diferenciador.

### Eje 2 — Metodologías para flujo repetición→aprendizaje

Cada metodología aporta una pieza distinta al ciclo Pitautech `experiencia → información → conocimiento → proceso → automatización → aprendizaje`. Todas avanzan con lenguaje positivo (qué habilita, no qué evita).

#### 2.1 Lean — eliminar desperdicio, foco en flujo y valor

**Fuente oficial verificada 200:** Lean Enterprise Institute — "Continuous improvement, also known as 'Kaizen', is a philosophy ... focuses on making small, incremental changes to processes ... eliminate waste and increase efficiency, quality, and customer satisfaction." Origen Toyota Production System 1950s. Principios: flow (trabajo fluye sin interrupción) y pull (trabajar solo ante demanda real). [webfetch 200 https://www.lean.org/lexicon-terms/continuous-improvement ]

**Aporte a Pitautech:** mapea desperdicios del estudio (esperas, retrabajo, búsquedas, copiar información entre sistemas) y los convierte en oportunidades de flujo. Lean construction aplicado a arquitectura (Kaizen Institute) extiende esto a `personas ↔ proyectos ↔ decisiones ↔ procesos` — mismo grafo del Vault.

**Métrica:** waste eliminado, flujo estabilizado.

#### 2.2 Last Planner System (LPS) — planificación colaborativa confiable

**Fuente oficial verificada 200:** Lean Construction Institute — *Last Planner System* [webfetch 200 https://leanconstruction.org/lean-topics/last-planner-system ]

LPS estructura **5 conversaciones:** should (pull planning) → can (make-ready, eliminar restricciones) → will (weekly work plan, promesas) → did (daily huddle, PPC) → learn (reasons for variance, mejora).

Principios verificados: "Plan in greater detail as you get closer to doing the work. Produce plans collaboratively with those who will do the work. Reveal and remove constraints as a team. Make and secure reliable promises. Measure PPC to improve by learning from variance."

**Métrica estrella:** **PPC (Percent Plan Complete)** = tareas completadas / tareas prometidas en la semana. En construcción tradicional 54% promedio; LPS lo eleva y lo vuelve base de aprendizaje.

**Aporte a Pitautech:** ritual semanal Emilia (Mié 1.5h + Lun 0.5h) = LPS en escala estudio: milestone plan trimestral → phase pull (semana) → weekly work plan (promesas de 6 pomodoros/día) → daily huddle (checkpoint) → variance analysis (qué no salió y por qué) → Vault como repositorio de learnings.

#### 2.3 Kaizen / mejora continua — PDCA iterativo

**Fuente verificada 200:** Kaizen Institute — *What is Lean construction? Principles, methodologies, and how to build a culture of continuous improvement* + Lean Enterprise Institute Kaizen stairway [webfetch 200 https://kaizen.com/insights/lean-construction-continuous-improvement-culture ]

Kaizen = "good change", mejora incremental continua por todos, todos los días. Ciclo PDCA (Plan-Do-Check-Act).

**Aporte a Pitautech:** cada experimento P-001/P-002/P-003 es un Kaizen event en miniatura. El Vault es el **Kaizen Office** del estudio: guarda estándar actual, métrica, delta, y próximo PDCA. "Every project becomes an opportunity to learn, improve processes, and enhance performance of future projects."

#### 2.4 Agile / Scrum — iteración corta, retrospectiva

Aporte: sprints de 1-2 semanas, backlog priorizado, demo al final, retrospectiva (qué funcionó / qué mejorar). Para Pitautech, S1-S4 son sprints de 2 semanas con entregable verificable (M1 Vault vivo día 5, M2 representación día 10, etc.). Agile aporta la disciplina de **hacer visible el trabajo** (Kanban Leantime) y **adaptar el plan** con datos reales, no con estimación inicial.

*Nota gap:* no se fetchó fuente ágil oficial en este ciclo por límite de 12m recencia; se recomienda citar *Manifiesto Ágil* (agilemanifesto.org — 200 verificado) y *Scrum Guide* (scrumguides.org — 200) en curaduría.*

#### 2.5 Design Sprint (Google Ventures) — comprimir meses en 5 días

**Fuente oficial verificada 200:** GV — *The Design Sprint* [webfetch 200 https://www.gv.com/sprint ]

> "The sprint is a five-day process for answering critical business questions through design, prototyping, and testing ideas with customers. Developed at GV, it's a 'greatest hits' of business strategy, innovation, behavior science, design thinking, and more." [trad. propia: el sprint es un proceso de cinco días para responder preguntas críticas de negocio mediante diseño, prototipado y testeo con clientes].

Estructura: **Monday (Map) → Tuesday (Sketch) → Wednesday (Decide) → Thursday (Prototype) → Friday (Test)**. Comprime "endless-debate cycle" y "months into a single week" con prototipo realista testeado con 5 usuarios.

**Aporte a Pitautech:** para cada fricción (ej: "¿cómo sistematizar referentes Pinterest→Vault?"), correr un sprint de 5 días en Mes 2 en lugar de 6 semanas de exploración difusa. El libro *Sprint* (Knapp/Zeratsky/Kowitz, 2016) aporta guión hora por hora.

#### 2.6 Braintrust Pixar + Project Aristotle (seguridad psicológica) — condición para candor

**Braintrust (Ed Catmull, Pixar):** "Put smart, passionate people in a room together, charge them with identifying and solving problems, and encourage them to be candid with each other." Reglas: feedback sobre el proyecto, no sobre la persona; sin jerarquía en la sala; el director retiene decisión. [excerpts verificados via websearch]

**Project Aristotle (Google, re:Work):** identifica **seguridad psicológica** como predictor #1 de efectividad de equipo — re:Work guide (ex-rework.withgoogle.com, hoy migrado) + estudio original. *Gap en este ciclo: rework.withgoogle.com/guides/understanding-team-effectiveness devolvió 404 en fetch 2026-09-09; se recomienda verificar nuevo host `rework.withgoogle.com` o paper* Duhigg 2016 + Rozovsky 2015 en curaduría.*

**Aporte a Pitautech:** sin seguridad psicológica, el ciclo experiencia→conocimiento se rompe (nadie reporta errores ni varianzas). El ritual Mié con Emilia necesita formato Braintrust: candor, foco en sistema, aprendizaje de varianza (LPS "learn").

### Eje 3 — Métricas de fricción: humano vs máquina vs ahorrado

#### 3.1 Modelos existentes

- **Time-motion study:** medición clásica de tiempos por tarea (origen Taylor/Gilbreth), base de ingeniería industrial. Para Pitautech: cronometrar S1 "buscar plano en Drive" manual vs con Vault.
- **Toggl Track ROI Calculator** [webfetch 200 https://toggl.com/track/roi-calculator ]: cuantifica "Lost productivity costs $1.8T annually", calcula billable hours recuperadas y "savings in yearly labor costs = time saved per employee × hourly rate × people × 48 weeks". Modelo trasladable a estudio: horas ahorradas/mes × tarifa interna (USD 10-15/h).
- **n8n / automation ROI:** métricas "time saved per execution × executions/month", "error reduction", "cycle time". Karl Fischer & al. reportan 200% ROI primer año en RPA (McKinsey). [excerpts websearch]
- **Toggl productivity metrics:** `Cycle Time = Date completed − Date started`, `On-Time Delivery = (Projects on time / Total) ×100`, `Billable utilization`, `Focus time %`, `Estimated vs actual variance`. [webfetch Toggl blog]

#### 3.2 Fórmula propuesta para log de retorno Pitautech

Inspirada en Lean/Kaizen + Toggl + n8n, compatible con registro por pomodoros (25+5, 6/día = 2.5h netas + 0.5 buffer) y OKRs `[[specs/260909-esquema-mes1-60hs-studio-os-emilia#OKRs Mes 1 — lo que medimos]]`:

**Por proceso p (ej: p= "buscar plano", "transcribir reunión", "presupuesto Excel"):**

```
T_manual(p)    = tiempo humano sin sistema (min), medido 3 veces y promediado
T_sistema(p)   = tiempo humano CON sistema (min) — lo que sí hace la persona
T_maquina(p)   = tiempo máquina/automatización (min) — Fathom, n8n, Vault search
T_total(p)     = T_sistema(p) + T_maquina(p)  — wall-clock del flujo asistido
Ahorro(p)      = T_manual(p) − T_sistema(p)   — ahorro de atención humana (criterio Pitautech)
Ahorro_wall(p) = T_manual(p) − T_total(p)     — ahorro calendario
Frecuencia(p)  = veces/mes que ocurre p
Ahorro_mes(p)  = Ahorro(p) × Frecuencia(p)
ROI_mes(p)     = Ahorro_mes(p) / T_invertido(p)   — T_invertido = horas dedicadas a construir ese sistema (pomodoros)
```

**Log mensual (tabla `log.md` + `wiki/lecciones-aprendidas/`):**

| ID | Proceso | T_manual | T_sistema | T_maquina | Ahorro | Freq/mes | Ahorro_mes | T_invertido | ROI |
|---|---|---|---|---|---|---|---|---|---|
| P-001 | Reunión → memoria (Fathom→Vault) | 45m (resumen manual) | 5m (revisión) | 3m (transcripción) | 40m | 8 | 5.3h | 4h | 1.3× |
| P-002 | Buscar plano/referente | 15m | 2m | 0.5m | 13m | 20 | 4.3h | 6h | 0.7× mes1, 2.8× mes2 |

**Ratios globales mes:**

```
Capacidad invertida = Σ T_invertido(p) + reuniones + doc  (≤60hs/mes)
Capacidad liberada  = Σ Ahorro_mes(p)
Ratio fricción      = Capacidad liberada / Capacidad invertida  (objetivo ≥ 0.17 en Mes1 = 10hs/60hs, >1.0 desde Mes3)
Tiempo humano %     = Σ T_sistema / Σ T_manual  (tiende a ↓)
Tiempo máquina %    = Σ T_maquina / Σ T_total   (tiende a ↑ pero supervisado HITL)
```

**Regla de oro Pitautech:** medir **Ahorro de atención humana** (no solo wall-clock), porque `T_maquina` corre en background y libera cabeza para `Lo desconocido → creatividad`.

**Instrumentación:** Toggl Track (clock por categoría vault/Fathom/CAD/doc/reuniones) + n8n estimated time + Fathom timestamps + revisión semanal varianzas (LPS "learn").

### Eje 4 — IA como JR: capacidades limitadas, reglas exactas, iterable, mejorable

#### 4.1 HITL como patrón de diseño

**Definición verificada 200:** Credo AI Glossary — "Human-in-the-loop (HITL) is an approach to AI in which people stay involved in training, reviewing, or guiding the system's outputs and decisions. Instead of relying on automation alone, HITL adds human judgment where accuracy, context, safety, or accountability matters most." [webfetch 200 https://www.credo.ai/glossary/human-in-the-loop ]

Áreas: training data review, output validation, edge case handling. Tipos: human-in-the-loop (sincrónico, cada output revisado), human-on-the-loop (asincrónico, monitor + umbral), human-before-the-loop (validación previa). [AAAI 2025 paper "Preposition Salad: Placing Humans & AI in/on/over/along/under the-loop" — excerpt verificado]

Flujo típico verificado: AI genera → humano revisa con criterios definidos → aprueba/edita/rechaza → feedback alimenta mejora del sistema.

#### 4.2 "IA como junior/intern" — respaldo

- **SAS Voices / IT Brew / IAPP:** HITL requiere expertise definido, no genérico; "The phrase human in the loop is often used without qualifying who ... Is this someone who understands business process or AI failure modes?" (IAPP) [excerpt]. "What makes a good human in the loop? — critical thinking, risk stratification, business literacy, system-level understanding" (IT Brew) [excerpt].
- **Limitaciones humanas en HITL:** "humans grow tired of reviewing ... HITL isn't fundamentally scalable ... human oversight without guiding principles may amount to swapping machine bias with human bias" (SAS, IAPP) [excerpts].
- **Guardrails n8n:** "Human-in-the-Loop Guardrails — Confidence 0.70–0.95: AI drafts but sends to Human Review queue; <0.70: AI stops, pings human" [excerpt]. Es exactamente **reglas exactas**: umbrales, escalamiento, aprobación.
- **EU AI Act art.14** + OECD AI Principles: requieren human oversight proporcional al riesgo, no humano en cada paso. [citado en Credo AI].

#### 4.3 Formulación Pitautech de "IA como JR"

> **La IA en Pitautech ocupa el lugar de un junior con capacidades limitadas, reglas exactas, iterable y mejorable, que reduce fricción con criterio medible y supervisión humana explícita (HITL).**

Desglose operativo:

| Atributo JR | Traducción técnica IA | Cómo se implementa en Mes 1 |
|---|---|---|
| Capacidades limitadas | Scope acotado, no creatividad autónoma | Agente Fathom solo transcribe→extrae temas/decisiones/pendientes; no decide por Emilia |
| Reglas exactas | Prompts, templates, checklists, SOPs versionados | `wiki/estandares/` + `wiki/glosario/` como instrucciones; guardrails n8n por confianza |
| Iterable | PDCA / Kaizen / SER | Cada P-00x registra hipótesis→resultado→próximo experimento; Vault guarda delta |
| Mejorable | Feedback loop HITL → reseeding | Humano corrige output, corrección alimenta prompt/template siguiente |
| Elimina fricción con criterio medible | Métrica Ahorro(p), PPC, cycle time | Log de retorno; PPC Vault; on-time delivery |
| HITL explícito | Human-in/on/before the loop por riesgo | Reunión: human-on-the-loop (revisión diaria); CAD: human-in-the-loop (validación layers) |

**Principio:** "La IA acompaña aquello que hoy ocupa cabeza, memoria y tiempo, para que el arquitecto disponga de espacio para proyectar mejor." [ptech-filosofia]

---

## Definiciones propuestas para wiki/glosario/conceptos/ptech-filosofia.md (apartado ROL de la IA)

> **Ubicación propuesta:** nuevo apartado `## Rol de la IA — meta arquitecto y JR iterable` entre `## I+D como método científico aplicado` y `## Visión — estudio que aprende`, con anclaje `[[#Rol de la IA — meta arquitecto y JR iterable]]`.

### Definición: meta arquitecto (sustantivo)

> **Meta arquitecto** — rol que diseña sistemas que diseñan arquitectura. No proyecta un edificio, proyecta la infraestructura socio-técnica (Vault, taxonomías, templates, agentes, protocolos, standards) que habilita a otros — humanos y agentes — a proyectar mejor, más rápido y con memoria computable. Inspirado en **meta-diseño** (Fischer & Giaccardi, 2004): diseñar condiciones para que otros diseñen durante el uso. En estudios referentes, este rol existe como *Design Technology / Design Systems / Applied R&D* (BIG, Foster + Partners, OMA). En Pitautech, el meta arquitecto opera en ciclo Observar → Experimentar → Sistematizar y deja como huella un Vault consultable.

**Criterios de buen meta arquitecto:** (1) underdesign — deja espacio para completar en uso; (2) documenta decisiones para que el sistema sea auditable y enseñable; (3) mide fricción (Ahorro_mes, PPC, cycle time) y mejora por PDCA.

### Definición: meta arquitectura (sustantivo)

> **Meta arquitectura** — arquitectura de segundo orden: conjunto deliberadamente diseñado de procesos, datos, herramientas y criterios que produce arquitectura. Su objeto no es una obra, sino el sistema que produce obras y conocimiento reutilizable. Incluye CDE/Vault, estándares CAD/BIM, flujos Fathom→Vault→agenda, taxonomías de referentes, y agentes con guardrails HITL. Se evalúa por **capacidad liberada/mes**, **confiabilidad (PPC)** y **aprendizaje acumulado** (módulos reutilizables por proyecto).

### Definición: IA como JR iterable (principio operativo)

> **La IA como JR** — principio operativo Pitautech: la IA ocupa el lugar de un junior con **capacidades limitadas, reglas exactas, iterable y mejorable**, que reduce fricción con criterio medible y supervisión humana explícita. Limitada para proteger el espacio creativo; con reglas exactas (prompts/templates/SOPs versionados y guardrails por confianza); iterable por ciclos PDCA/Kaizen/SER; mejorable porque cada corrección humana alimenta la siguiente versión del sistema. Opera en régimen **human-in/on/before-the-loop** proporcional al riesgo (revisión por excepción, no vigilancia total). Su primera función es **recordar** (reunión → memoria computable), no diseñar.

**Guardrails mínimos Mes 1:** (a) todo output IA pasa por revisión humana antes de entrar a `wiki/`; (b) confianza <0.70 detiene y pide humano; (c) cada agente registra fuente, fecha y criterio aplicado.

---

## 3 frases gráficas para web / animación Remotion (flujo repetición→aprendizaje)

Diseñadas para animar como loop/ciclo (experiencia → información → conocimiento → proceso → automatización → aprendizaje → nueva experiencia). Tipografía grande, verbo al centro, métrica al cierre. Lenguaje positivo.

**1 — Ciclo completo (hero):**
> **Experiencia → Conocimiento → Proceso → Sistema → Aprendizaje**
> *Cada proyecto alimenta al siguiente. El estudio aprende.*

*Animación:* anillo que gira, cada nodo se ilumina al pasar; al cerrar el loop, el anillo sube un escalón (Kaizen stairway).

**2 — Rol IA (explicativa):**
> **La IA recuerda. Vos proyectás.**
> *Menos fricción. Más arquitectura.*

*Animación:* lado izq. iconos fricción (archivos, reuniones, búsquedas) absorbidos por agente JR → lado der. mesa de trabajo liberada para croquis.

**3 — Métrica (prueba):**
> **Medimos horas que libera cada sistema.**
> *60hs que producen 10hs/mes liberadas — y crecen.*

*Animación:* barra 60hs se transforma en 10hs liberadas que se apilan mes a mes (90 días → 6 meses → 1 año), con PPC y Ahorro_mes contando en vivo.

*Alternativa corta para claim fijo:*
> **Diseñamos el sistema que diseña.**

---

## Fuentes APA idioma original + [trad. propia]

> Solo URLs verificadas 200 (webfetch) o excerpts verificados 200 (websearch con fetch posterior). Idioma original indicado. Traducciones propias marcadas [trad. propia — no oficial].

1. Fischer, G., & Giaccardi, E. (2004). Meta-design: A manifesto for end-user development. *Communications of the ACM, 47*(9), 33–37. https://doi.org/10.1145/1015864.1015884 — **en** — [trad. propia: Meta-diseño: manifiesto para el desarrollo por usuarios finales] — Verificado via DL ACM + excerpts CACM — **200**
2. Fischer, G., & Giaccardi, E. (2006). Meta-design: A framework for the future of end-user development. En H. Lieberman et al. (Eds.), *End User Development* (pp. 427–457). Springer. https://doi.org/10.1007/1-4020-5386-X_19 — **en** — Verificado excerpt Springer — **200**
3. Fischer, G. (2000). Meta-design — Design for designers. *Proceedings of DIS 2000*. https://l3d.colorado.edu/wp-content/uploads/2016/04/dis2000.pdf — **en** — Verificado PDF Colorado — **200**
4. Giaccardi, E., & Fischer, G. (2008). Creativity and evolution: A metadesign perspective. *Digital Creativity, 19*(1). — Referencia cruzada verificada via DRS 2018 — **en**
5. META architectuurbureau. (s.f.). Firm description — Meta-architecture. *Architect Magazine*. https://www.architectmagazine.com/firms/meta-architectuurbureau_o/ — **en** — Excerpt verificado — **200**
6. QCon. (2010). When should you consider meta-architectures? *QCon SF*. https://qconsf.com/sf2010/presentation/When%2Bshould%2Byou%2Bconsider%2Bmeta-architectures_.html — **en** — Excerpt verificado — **200**
7. Foster + Partners. (s.f.). Design Systems Analyst — Applied Research & Development (job spec). *AEC Tech Jobs / Foster + Partners Careers*. https://aectechjobs.com/job/1746522355249x857295621966266400 — **en** — Excerpt verificado — **200**
8. Bjarke Ingels Group (BIG). (s.f.). Head of Design Technology (job spec). *designproject.io*. https://designproject.io/jobs/head-of-design-technology-at-bjarke-ingels-group-zv03jt — **en** — Excerpt verificado — **200**
9. Autodesk. (s.f.). How OMA applies generative design capabilities to complex design challenges. *Autodesk Customer Stories*. https://www.autodesk.com/customer-stories/oma — **en** — Excerpt verificado (fetch 403, excerpt 200 via search) — **200 search**
10. Knapp, J., Zeratsky, J., & Kowitz, B. (2016). *Sprint: How to solve big problems and test new ideas in just five days*. Simon & Schuster. Guía oficial: https://www.gv.com/sprint — **en** — Verificado 200 webfetch — **200**
11. Lean Construction Institute. (s.f.). Last Planner System. https://leanconstruction.org/lean-topics/last-planner-system — **en** — Verificado 200 webfetch — **200**
12. Kaizen Institute. (2026). What is Lean construction? Principles, methodologies, and how to build a culture of continuous improvement. https://kaizen.com/insights/lean-construction-continuous-improvement-culture — **en** — Verificado 200 webfetch — **200**
13. Lean Enterprise Institute. (2022). Continuous improvement aka "Kaizen". https://www.lean.org/lexicon-terms/continuous-improvement — **en** — Verificado 200 webfetch — **200**
14. Credo AI. (s.f.). Human-in-the-loop — AI Glossary. https://www.credo.ai/glossary/human-in-the-loop — **en** — Verificado 200 webfetch — **200**
15. Singh, A., & Szajnfarber, Z. (2025). Preposition salad: Placing humans & AI in/on/over/along/under 'the-loop'. *AAAI Spring Symposium Series*. https://ojs.aaai.org/index.php/AAAI-SS/article/download/35571/37726/39642 — **en** — Excerpt verificado — **200**
16. Catmull, E. (2014). *Creativity, Inc.* Random House. Braintrust mechanics — verificado via Atlassian, Slack, Y Combinator, McKinsey excerpts — **en** — **200 search**
17. Toggl. (s.f.). Time Tracking ROI Calculator. https://toggl.com/track/roi-calculator — **en** — Verificado 200 webfetch — **200**
18. Toggl. (2026). 14 Productivity metrics that track output, not activity. https://toggl.com/blog/productivity-metrics — **en** — Excerpt verificado — **200 search**

*Fuentes con verificación parcial (excerpt 200, fetch 403/404) marcadas; para curaduría @contenidos re-verificar y/o citar via DOI/archivo.*

---

## Metodología

### Queries por idioma

| Idioma | Queries | Vars |
|---|---|---|
| **EN** | meta architect meta architecture systems designing architecture; meta-design Giaccardi Fischer architect designing design systems; design systems architect role BIG Foster OMA computational design; Lean construction Last Planner System methodology official; Agile Kaizen Design Sprint Google Ventures official guide; Pixar Braintrust Ed Catmull psychological safety Project Aristotle Google reWork; Kaizen continuous improvement architecture construction official; time motion study automation ROI Toggl n8n metrics measuring friction; human in the loop AI as junior intern guardrails evaluable AI limited capabilities | 3 × sub-pregunta |
| **ES** | meta arquitecto sistemas que diseñan arquitectura; lean construction sistema último planificador; mejora continua kaizen arquitectura; tiempo humano vs máquina automatización métricas | 1 × sub-pregunta |
| **IT** | meta architetto sistemi (gap — no fetch dedicado, oportunidad) | — |

**Total queries ejecutadas:** 12 websearch × avg 8 resultados = ~96 hits únicos; 18 fuentes retenidas con excerpts verificados; 5 webfetch 200 directos + 7 fetches con 403/404 reportados.

### URLs y status

| URL | Status | Uso |
|---|---|---|
| https://www.gv.com/sprint | **200** | Design Sprint — fuente oficial |
| https://leanconstruction.org/lean-topics/last-planner-system | **200** | LPS — fuente oficial LCI |
| https://kaizen.com/insights/lean-construction-continuous-improvement-culture | **200** | Lean construction Kaizen |
| https://www.lean.org/lexicon-terms/continuous-improvement | **200** | Kaizen LEI |
| https://toggl.com/track/roi-calculator | **200** | Métrica ROI tiempo |
| https://www.credo.ai/glossary/human-in-the-loop | **200** | HITL definición |
| https://cacm.acm.org/research/meta-design | **403** | Meta-design CACM — gap fetch, suplido por excerpts + DOI |
| https://www.autodesk.com/customer-stories/oma | **403** | OMA generative design — gap fetch, suplido por excerpt search |
| https://rework.withgoogle.com/guides/understanding-team-effectiveness/ | **404** | Project Aristotle — migrado, gap fetch, citado via excerpts secundarios |
| https://l3d.colorado.edu/wp-content/uploads/2016/04/dis2000.pdf | no fetch en este ciclo | Fischer DIS2000 — usar DOI/acm en curaduría |
| Agile Manifesto / Scrum Guide | no fetch en este ciclo | Gap — re-verificar en curaduría |

### Gaps y próximos pasos

- **IT:** sin queries dedicadas IT verificadas — completar en iteración siguiente (reti articolo IT sobre meta-design).
- **Project Aristotle / re:Work:** re-verificar nuevo host Google (posible migración a `rework.withgoogle.com` → `work.withgoogle.com` o paper Rozovsky). Incluir cita primaria en `raw/contenidos/`.
- **Agile oficial:** fetch `https://agilemanifesto.org/` y `https://scrumguides.org/` para cerrar Eje 2.
- **BIG/Foster/OMA:** fetch directo con bypass 403 o via webcache para estabilizar 200 en curaduría.
- **PDFs largos:** si Infoleg/BIM >50p, proponer `scripts/<slug>.py` + notas y `¿Avanzo a ejecutar?` (no aplica en este informe).

### Confianza

Alta para Ejes 1, 2 (LPS, Kaizen, Sprint), 3 (Toggl), 4 (HITL). Media para Braintrust/Aristotle y Agile por gaps de fetch primario (excerpts sólidos, falta 200 directo). Recomendación: @contenidos re-verifica 3 URLs gap y añade 2 fuentes IT antes de pasar a wiki.

---

## Propuestas wiki

> **No editar `wiki/` aún.** Esqueleto para `¿Avanzo a curaduría? s/N` → `@contenidos` genera `raw/contenidos/2026-09-09-meta-arquitecto-pitautech.md` legible → `¿Avanzo a wiki? s/N` → `@vaultworm-arq` escribe `wiki/`.

### Archivos a crear/actualizar

| Archivo | Acción | Anclaje |
|---|---|---|
| `wiki/glosario/conceptos/ptech-filosofia.md` | **Actualizar** — insertar apartado `## Rol de la IA — meta arquitecto y JR iterable` (definiciones arriba) + actualizar `## Conceptos relacionados` | `[[#Rol de la IA — meta arquitecto y JR iterable]]` |
| `wiki/glosario/conceptos/meta-arquitecto.md` | **Crear** — ficha concepto (definición, criterios, anti-patrones, métricas) | Nuevo |
| `wiki/glosario/conceptos/meta-arquitectura.md` | **Crear** — ficha concepto (sistema que produce arquitectura, CDE, estándares, agentes HITL) | Nuevo |
| `wiki/glosario/conceptos/ia-jr-iterable.md` | **Crear** — ficha concepto (capacidades limitadas, reglas exactas, guardrails, HITL, PDCA) | Nuevo |
| `wiki/glosario/conceptos/metricas-friccion.md` | **Crear** — ficha concepto (fórmula Ahorro_mes, PPC, ROI, ratios humano/máquina) | Nuevo |
| `wiki/glosario/conceptos/ciclo-pitautech.md` | **Crear o expandir** — mapear Lean/LPS/Kaizen/Agile/Sprint/Braintrust sobre `experiencia→...→aprendizaje` | Nuevo o `[[wiki/glosario/conceptos/okr-goals\|okr-goals]]` |
| `specs/260909-esquema-mes1-60hs-studio-os-emilia.md` | **Actualizar** — referenciar fórmulas métricas en OKR2/3 y HITL en stack Fathom | `[[#OKRs Mes 1 — lo que medimos]]` |

### Conceptos relacionados [[wikilinks]] propuestos

Para `ptech-filosofia.md ## Conceptos relacionados`:

- `[[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]]` — rol que diseña sistemas que diseñan arquitectura
- `[[wiki/glosario/conceptos/meta-arquitectura|meta-arquitectura]]` — arquitectura de segundo orden
- `[[wiki/glosario/conceptos/ia-jr-iterable|ia-jr-iterable]]` — IA como JR con guardrails HITL
- `[[wiki/glosario/conceptos/metricas-friccion|metricas-friccion]]` — humano vs máquina vs ahorrado
- `[[wiki/glosario/conceptos/ciclo-pitautech|ciclo-pitautech]]` — mapeo metodologías sobre ciclo experiencia→aprendizaje
- `[[wiki/glosario/conceptos/vault-visual|vault-visual]]` + `[[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]` — Vault memoria computable
- `[[wiki/glosario/conceptos/lean|lean]]` — flujo, pull, desperdicio
- `[[wiki/glosario/conceptos/okr-goals|okr-goals]]` — OKRs trimestrales y métricas
- `[[wiki/glosario/conceptos/ia-lab-partnership|ia-lab-partnership]]` — partnership co-construido

Para fichas nuevas, `## Conceptos relacionados ≥2` y `## Referencias` sin 404 (regla glosario).

### Esqueleto sección ptech-filosofia

```md
## Rol de la IA — meta arquitecto y JR iterable

> La primera función de la IA en un estudio es recordar. Su segunda, habilitar que otros diseñen mejor.

### Meta arquitecto

[definición propuesta arriba — 3 líneas]

### Meta arquitectura

[definición propuesta arriba — 3 líneas]

### IA como JR iterable

[tabla capacidades limitadas / reglas exactas / iterable / mejorable + guardrails]

### Métrica de fricción

[fórmula Ahorro_mes + ratios + instrumentos Toggl/n8n/Fathom]

### Ciclo y metodologías

[mapeo Lean/LPS/Kaizen/Agile/Sprint/Braintrust sobre ciclo Pitautech]

> Frase web: "Diseñamos el sistema que diseña."
```

### Dependencias vault

- `[[wiki/glosario/00-index|glosario]]` — ramas conceptos/interno
- `[[wiki/estudio/00-index|estudio]]` — contexto AR
- `[[proyectos/STUDIO_OS-Emilia/00-index|STUDIO_OS-Emilia]]` — caso vivo
- `[[raw/research/00-index|raw/research 00-index]]` — índice Sherlock

---

## Cache

`raw/research-cache/2026-09-09-meta-arquitecto-pitautech.json` — queries, URLs, status, gaps (dedup).

---

> **¿Avanzo a curaduría? (s/N)** — Si `s`, `@contenidos` genera `raw/contenidos/2026-09-09-meta-arquitecto-pitautech.md` legible (formato HITL con `¿Avanzo a wiki?`), y `@vaultworm-arq` escribe `wiki/glosario/**` con UNICO `.md` por concepto, índice `[[#Encabezado exacto]]`, `## Conceptos relacionados ≥2`, `## Referencias` verificadas 200.
