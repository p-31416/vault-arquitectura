---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, marco-creativo, google, pixar, pitau-tech, estudio-arquitectura]
idioma: es
---

# Marco creativo Google + Pixar (base pitau-tech y estudios)

> Síntesis operativa: 5 pilares combinados de Google (sprint, OKR, seguridad psicológica, 20%) y Pixar (braintrust, dailies, ugly babies) como sistema de trabajo para pitau-tech y cualquier estudio de arquitectura argentino.

- [[#Tesis]]
- [[#Los 5 pilares]]
- [[#Cómo se combinan (sistema, no lista)]]
- [[#Traducción a estudio de arquitectura ARG]]
- [[#Plan de adopción en 4 semanas]]
- [[#Antipatrones (qué NO copiar)]]
- [[#Conceptos relacionados]]
- [[#Referentes]]
- [[#Referencias]]

## Tesis

Google aporta el **sistema de ejecución** (decidir rápido, medir lo que importa, equipos seguros, tiempo para explorar) y Pixar el **sistema de calidad creativa** (crítica franca sin jerarquía, iteración diaria, protección de lo nuevo). Ninguno funciona sin el otro: un sprint sin seguridad psicológica produce obediencia, y un braintrust sin OKR produce charla infinita. Para pitau-tech —que vende modernización a estudios que hoy trabajan en papel, WhatsApp y obra presencial— este marco es doble: **cómo trabajamos nosotros** y **qué instalamos en el cliente**.

## Los 5 pilares

| # | Pilar | Origen | Idea en 1 línea | Ficha |
|---|-------|--------|-----------------|-------|
| 1 | Sprint semanal | Google Ventures | 1 semana: entender → bocetar → decidir → prototipar → validar con el usuario real | [[wiki/glosario/conceptos/design-sprint|design-sprint]] |
| 2 | Braintrust + dailies | Pixar | Crítica franca entre pares sin autoridad + revisión diaria del avance; se critica el proyecto, no la persona | [[wiki/glosario/conceptos/braintrust-pixar|braintrust-pixar]] |
| 3 | Seguridad psicológica | Google (Aristotle) | Sin miedo a reportar errores no hay calidad; el talento pesa menos que la dinámica | [[wiki/glosario/conceptos/seguridad-psicologica-aristotle|seguridad-psicologica-aristotle]] |
| 4 | OKR trimestrales | Intel → Google (Doerr) | 3–5 objetivos que importan + resultados medibles; contrato social visible, no atado al sueldo | [[wiki/glosario/conceptos/okr-goals|okr-goals]] |
| 5 | Tiempo de exploración | Google 20% / Pixar riesgo | Horas protegidas para lo nuevo (detalle experimental, flujo IA, familia Revit); el mensaje es "así somos" | [[wiki/glosario/conceptos/seguridad-psicologica-aristotle|seguridad-psicologica-aristotle]] §Work Rules |

## Cómo se combinan (sistema, no lista)

```
OKR trimestral (adónde vamos)
 └─→ Sprint semanal (cómo decidimos rápido qué vale la pena)
       └─→ Dailies (avance visible todos los días)
             └─→ Braintrust semanal (crítica franca que salva el proyecto)
                   └─→ Todo sobre Seguridad psicológica (sin esto, lo anterior es teatro)
                         └─→ 20% exploración (de acá sale el próximo trimestre)
```

- El **sprint** genera el prototipo; el **braintrust** lo rompe a tiempo; los **dailies** evitan que el error llegue a obra; el **OKR** dice si importaba; la **seguridad** permite decir "está mal"; el **20%** inventa lo siguiente.
- Rituales mínimos del sistema: daily 15 min + braintrust 1 h/semana + planning OKR trimestral + [[wiki/glosario/conceptos/retrospectivas|retrospectiva]] 30 min + postmortem por proyecto cerrado.
- Todo ya existe en el vault como piezas sueltas ([[wiki/glosario/conceptos/lean|lean]], [[wiki/glosario/conceptos/kanban|kanban]], [[wiki/glosario/conceptos/agile-arquitectura|agile-arquitectura]], [[wiki/glosario/conceptos/last-planner-system|last-planner-system]], [[wiki/glosario/conceptos/kaizen|kaizen]]): este marco es la **capa creativa** que les faltaba.

## Traducción a estudio de arquitectura ARG

| Realidad actual | Práctica del marco | Efecto |
|-----------------|-------------------|--------|
| Libro de obra en papel, fotos sueltas de celular | Dailies + reporte sin culpa (seguridad psicológica) | El error se caza el día 1, no en la certificación |
| Detalle dibujado in situ, apurado | Ugly baby: el detalle experimental se protege 2 semanas solo con revisión interna | Innovación constructiva sin riesgo de obra |
| Plano = documento legal (Ley 24.335, incumbencia) | Braintrust pre-firma: toda lámina legal pasa por crítica de pares antes del sello | El sello respalda algo ya roto y rehecho |
| Cada municipio, su código | Sprint de 1 semana para conquista normativa (prototipo = anteproyecto + memoria de encuadre) | Se valida con el comitente antes de dibujar el legajo entero |
| Equipo remoto distribuido | Dailies async + braintrust por videollamada con turnos parejos | La distancia deja de ser excusa de calidad |
| Renders "por si acaso" | Pull lean + validación viernes (sprint): no se produce lo que nadie pidió | Menos sobreproducción, más margen |

## Plan de adopción en 4 semanas

1. **Semana 1 — Seguridad primero:** anunciar regla "el que avisa un error propio es reconocido"; primera revisión de láminas con palabra de junior primero.
2. **Semana 2 — Dailies + braintrust piloto:** un solo proyecto, 15 min diarios + 1 h de braintrust viernes. Medir: errores cazados antes de plot.
3. **Semana 3 — Primer sprint:** un anteproyecto o un flujo interno en formato lunes→viernes. Validar con comitente real el viernes.
4. **Semana 4 — OKR del trimestre + 20%:** 3 objetivos del estudio en [[wiki/glosario/conceptos/okr-goals|okr-goals]] + medio día mensual de exploración con demo.

## Antipatrones (qué NO copiar)

- **Sprint sin decider real:** si el que decide no está en la sala, la semana es teatro.
- **Braintrust con jefes:** si tu jefe está en la sala y tiene poder sobre tu sueldo, no hay candor — sacar a los reportes directos de la ecuación.
- **OKR atado a bonus:** en cuanto el objetivo paga, la gente lo baja para cobrarlo (sandbagging).
- **20% sin demo:** tiempo libre sin muestra obligatoria se vuelve ocio invisible; con demo se vuelve I+D.
- **Copiar la forma, no el fondo:** la sala con post-its no es el método; el método es decidir rápido, criticar sin miedo y proteger lo nuevo.

## Conceptos relacionados

- [[wiki/glosario/conceptos/design-sprint|design-sprint]]
- [[wiki/glosario/conceptos/braintrust-pixar|braintrust-pixar]]
- [[wiki/glosario/conceptos/seguridad-psicologica-aristotle|seguridad-psicologica-aristotle]]
- [[wiki/glosario/conceptos/okr-goals|okr-goals]]
- [[wiki/glosario/conceptos/design-thinking|design-thinking]]
- [[wiki/glosario/conceptos/lean|lean]]

## Referentes

- [[wiki/glosario/referentes/google|google]] — sistema de ejecución
- [[wiki/glosario/referentes/pixar-animation-studios|pixar-animation-studios]] — sistema de calidad creativa
- [[wiki/glosario/referentes/ed-catmull|ed-catmull]] — filosofía "gente buena > buena idea"
- [[wiki/glosario/referentes/jake-knapp|jake-knapp]] — método sprint

## Referencias

- Catmull: la idea inicial vale poco, el equipo que itera vale todo: https://hbr.org/2008/09/how-pixar-fosters-collective-creativity (verificado 2026-09-09 — 200)
- Google: pensar en grande y coordinar con OKR (playbook oficial): https://www.whatmatters.com/resources/google-okr-playbook (verificado 2026-09-09 — 200)
- La seguridad psicológica como factor #1 de equipo: https://www.nytimes.com/2016/02/28/magazine/what-google-learned-from-its-quest-to-build-the-perfect-team.html (verificado 2026-09-09 — puede tener paywall)
- Sprints reales (Slack, Blue Bottle, robots, medicina): https://www.gv.com/sprint (verificado 2026-09-09 — 200)
