---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, kanban, flujo, leantime, mejora-continua]
---

# Kanban

> Método de gestión visual del flujo de trabajo: visualizar, limitar WIP, gestionar flujo. En el vault se usa vía tableros Leantime (Kanban/Table/List) por proyecto.

- [[#Definición]]
- [[#Principios y prácticas]]
- [[#Métricas de flujo]]
- [[#Kanban en estudio de arquitectura]]
- [[#Kanban → Leantime]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Definición

Kanban (David J. Anderson, 2010, raíces en Toyota/Lean) **no es una metodología con roles prescriptos**: es un método de gestión que se aplica **sobre el proceso que ya existe**. Tres cambios mínimos: hacer visible el trabajo invisible, limitar el trabajo en curso (WIP) y medir el flujo para mejorar evolutivamente.

Lema operativo: **"Stop starting, start finishing"** — terminar lo empezado vale más que empezar lo nuevo.

## Principios y prácticas

**Principios de cambio:** empezar con lo que se hace ahora; acordar mejora evolutiva (no big-bang); fomentar liderazgo en todos los niveles.

**Principios de servicio:** entender necesidades del cliente; gestionar el trabajo y dejar que las personas se auto-organicen; revisar la red de servicios regularmente.

**6 prácticas generales:**

| # | Práctica | Traducción al estudio |
|---|----------|----------------------|
| 1 | Visualizar | Tablero por proyecto: columnas = fases reales (briefing → concepto → DD → legajo → obra) |
| 2 | Limitar WIP | Máx. 2–3 planos/entregables "en curso" por dibujante; 1 render en curso por máquina |
| 3 | Gestionar flujo | Medir lead time plano→aprobado; detectar cuellos (ej. espera comitente) |
| 4 | Hacer políticas explícitas | Definition of Done por columna (ej. "plano sale de Revisión solo con sello + PDF en activos/") |
| 5 | Feedback loops | Daily 15 min + weekly review del tablero |
| 6 | Mejora colaborativa | Experimentos safe-to-fail (ej. "esta semana probamos WIP=2 en legajo") |

**STATIK** (Systems Thinking Approach to Introducing Kanban): pasos para diseñar el tablero — identificar insatisfacciones → analizar demanda → analizar capacidad → modelar workflow → clases de servicio (urgente/normal) → diseñar tablero.

## Métricas de flujo

- **Lead time:** compromiso → entrega (días por entregable).
- **Throughput:** entregables/semana.
- **WIP:** cantidad en curso (si sube, el lead time sube — ley de Little).
- **CFD (Cumulative Flow Diagram):** bandas por columna; banda que se ensancha = cuello de botella.
- **PPC** cuando se combina con Last Planner (ver [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]).

## Kanban en estudio de arquitectura

Columnas sugeridas (mapean fases del vault):

`Backlog → Briefing → Concepto → Desarrollo → Revisión interna → Corrección comitente → Aprobado → Obra/Entrega`

Clases de servicio: `estándar` / `urgente` (habilitación con fecha legal) / `bloqueado` (falta dato externo — se marca, no se esconde).

WIP inicial recomendado: dibujante 2, revisión Sol/Emilia 3, renders 1 por GPU.

## Kanban → Leantime

Leantime implementa Kanban como una vista de To-Dos (Kanban/Table/List/Calendario/Gantt). Ver [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]] §2 para el mapeo columna↔estado Leantime, subtasks y dependencias.

## Conceptos relacionados

- [[wiki/glosario/conceptos/lean|lean]]
- [[wiki/glosario/conceptos/last-planner-system|last-planner-system]]
- [[wiki/glosario/conceptos/agile-arquitectura|agile-arquitectura]]
- [[wiki/glosario/conceptos/kaizen|kaizen]]

## Referencias

- Kanban University — Official Guide to the Kanban Method: https://kanban.university/kanban-guide/ (verificado 2026-09-09 — 200, incluye principios, prácticas, STATIK, métricas)
- Anderson, D. J. (2010) *Kanban: Successful Evolutionary Change for Your Technology Business* — Blue Hole Press
- EPA Lean — JIT/Kanban: https://www.epa.gov/lean/lean-thinking-and-methods-jitkanban (verificado 2026-09-09 — familia Lean con Kanban)
- Leantime — vistas Kanban/Table/List: https://leantime.io/ (verificado 2026-09-09 — 200)
