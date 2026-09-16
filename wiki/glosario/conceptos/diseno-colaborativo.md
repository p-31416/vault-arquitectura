---
tipo: concepto
fecha_creacion: 2026-09-10
ultima_actualizacion: 2026-09-10
tags: [diseno-colaborativo, co-design, meta-design, underdesign, braintrust, ser]
idioma: es
---

# Diseño colaborativo — co-diseño y underdesign

> Diseñar condiciones para que otros diseñen — meta-diseño como infraestructura socio-técnica donde usuarios avanzan hacia co-diseñadores durante toda la vida del sistema.

Desprendido de [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]]: práctica que habilita que el Vault, los standards y los agentes se completen en uso con quienes proyectan.

- [[#Definición]]
- [[#Principios — underdesign + SER]]
- [[#Braintrust + seguridad psicológica — condición para candor]]
- [[#Adaptación a estudios de arquitectura — rituales Pitautech]]
- [[#Conceptos relacionados]]
- [[#Referencias]]
- [[#Fuentes bibliográficas — APA idioma original + [trad. propia]]]

## Definición

**Diseño colaborativo / co-design:** proceso donde quienes usarán el sistema participan como co-diseñadores durante toda su existencia, no solo en el diseño inicial (Fischer & Giaccardi, 2006).

En Pitautech, el estudio avanza hacia sistema socio-técnico donde:

- arquitectos, dibujantes, comitentes y agentes aportan decisiones que quedan trazables en el Vault;
- cada proyecto deja aprendizajes que vuelven como estándares, templates y taxonomías;
- la infraestructura queda deliberadamente abierta para completar en uso (underdesign).

Se diferencia de "participación" genérica: aquí el co-diseño produce artefactos reutilizables (ficha `wiki/estandares/`, taxonomía, agente), no solo opiniones.

## Principios — underdesign + SER

**Underdesign (infradiseño):** dejar sistemas deliberadamente incompletos para que usuarios los completen en uso. Avanza con confianza: el estándar propone 80% y el proyecto completa 20% contextual, que luego vuelve al estándar si resulta valiosa.

**SER — Seeding, Evolutionary Growth, Reseeding:**

| Fase | Qué pasa | En el Vault |
|---|---|---|
| **Seeding** (siembra) | Se instala semilla mínima viable | Vault inicial + 1 agente Fathom + DWT base + taxonomía 20–30 referentes |
| **Evolutionary Growth** (crecimiento evolutivo) | Usuarios usan, adaptan y extienden en proyectos reales | Nayara, Studio OS: nuevos layers, variantes de lámina, prompts ajustados por correcciones HITL |
| **Reseeding** (resiembra) | Se consolida lo aprendido en nueva versión del sistema | Fichas `wiki/estandares/` actualizadas + roadmap Mes 2 + templates versionados |

> El diseño colaborativo avanza cuando la semilla habilita crecimiento y la resiembra captura aprendizaje.

## Braintrust + seguridad psicológica — condición para candor

Sin candor no hay co-diseño. Dos condiciones lo habilitan:

- **[[wiki/glosario/conceptos/braintrust-pixar|Braintrust Pixar]] (Ed Catmull):** pares que ya pasaron por eso, sin autoridad en la sala; feedback sobre proyecto, nunca sobre persona; el presentador decide cómo incorporar.
- **[[wiki/glosario/conceptos/seguridad-psicologica-aristotle|Seguridad psicológica]] (Project Aristotle):** predictor #1 de efectividad de equipo; sin ella nadie reporta varianzas ni propone mejoras.

En Pitautech, el ritual **Mié 1.5h + Lun 0.5h** avanza hacia Braintrust en escala estudio: el que traba presenta, el grupo critica el proyecto, se registra varianza (LPS learn) y queda en Vault.

Técnicas que nutren el co-diseño:

- **Dailies:** 15 min diarios, cada uno muestra avance; corrección temprana cuando cuesta minutos.
- **Plussing:** al criticar, siempre agregar dirección de mejora; el trabajo ajeno es punto de partida.
- **Ugly babies:** toda idea nace vulnerable; se protege 2 semanas de crítica externa mientras muta con prototipos.

## Adaptación a estudios de arquitectura — rituales Pitautech

| Ritual | Formato | Producto colaborativo |
|---|---|---|
| **Vault vivo (S1)** | Obsidian + Fathom + Leantime instalados, guía wiki enseñable | 1 reunión transcripta <24hs, junior opera solo en S4 |
| **Referentes curados (S2)** | 20–30 referentes ArchDaily/revistas/web con ficha qué tomar/dejar | Carpeta curada + sistema representación v0 aplicado a Nayara |
| **Estándares CAD (S3)** | DWT/layers/bloques/rótulos + Lisp con IA validado sobre objeto de estudio | Estándares operativos + 4 fichas `wiki/estandares/` |
| **Cierre + roadmap (S4)** | Clase 2h + retro + acta + métricas Ahorro_mes | Doc Mes 1 completa + roadmap Mes 2 con precio anclado a horas liberadas |

> El diseño colaborativo avanza cuando cada ritual produce artefacto enseñable que el siguiente proyecto reutiliza y mejora. Ver [[wiki/glosario/interno/standares/ptech-filosofia#I+D como método científico aplicado|I+D método]] + [[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral]].

## Conceptos relacionados

- [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]] — rol que diseña el sistema que habilita co-diseño
- [[wiki/glosario/conceptos/braintrust-pixar|braintrust-pixar]] — candor sin jerarquía + dailies + plussing
- [[wiki/glosario/conceptos/seguridad-psicologica-aristotle|seguridad-psicologica-aristotle]] — condición para co-diseño
- [[wiki/glosario/conceptos/kaizen|kaizen]] — PDCA que itera el co-diseño
- [[wiki/glosario/conceptos/hitl-human-in-the-loop|hitl-human-in-the-loop]] — supervisión que habilita iteración con criterio
- [[wiki/glosario/conceptos/design-sprint|design-sprint]] — sprint 5 días para prototipar co-diseño rápido
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]] — Vault como memoria que crece con co-diseño

## Referencias

- Fischer, G., & Giaccardi, E. (2004). Meta-design: A framework for the future of end-user development. https://doi.org/10.1145/1015864.1015884 — 200 — underdesign + SER
- Fischer, G., & Giaccardi, E. (2006). Meta-design ... *End User Development* (pp. 427–457). Springer. https://doi.org/10.1007/1-4020-5386-X_19 — 200 — definición co-diseño continuo
- Fischer, G. (2000). Meta-design — Design for designers. DIS 2000. https://l3d.colorado.edu/wp-content/uploads/2016/04/dis2000.pdf — 200 — Designing the design process becomes a first-class activity
- Catmull, E. (2014). *Creativity, Inc.* + HBR How Pixar Fosters Collective Creativity: https://hbr.org/2008/09/how-pixar-fosters-collective-creativity — 200 — Braintrust
- Atlassian — Braintrust culture: https://www.atlassian.com/blog/productivity/braintrusts-build-a-candid-think-tank-culture-at-work — 200 — mecánica replicable Braintrust
- re:Work / Project Aristotle — seguridad psicológica (ex rework.withgoogle.com, migrado; citado vía HBR/Duhigg + excerpts verificados 200 vía search) — condición para candor
- GV — Design Sprint: https://www.gv.com/sprint — 200 — base para sprints colaborativos
- `raw/research/2026-09-09-meta-arquitecto-pitautech.md` §Eje 2.6 — Braintrust + Aristotle como condición

## Fuentes bibliográficas — APA idioma original + [trad. propia]

- Fischer, G., & Giaccardi, E. (2004). Meta-design: A manifesto for end-user development. *Communications of the ACM, 47*(9), 33–37. https://doi.org/10.1145/1015864.1015884 — **en** — [trad. propia]
- Fischer, G., & Giaccardi, E. (2006). Meta-design: A framework for the future of end-user development. En H. Lieberman et al. (Eds.), *End User Development* (pp. 427–457). Springer. https://doi.org/10.1007/1-4020-5386-X_19 — **en** — [trad. propia]
- Catmull, E. (2014). *Creativity, Inc.: Overcoming the unseen forces that stand in the way of true inspiration*. Random House — **en** — [trad. propia: Creatividad, S.A.]
