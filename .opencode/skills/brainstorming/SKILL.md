---
name: brainstorming
description: "Facilita sesiones divergentes/convergentes con 8 frameworks (Design Thinking, Double Diamond, SCAMPER, Six Hats, Reverse, Brainwriting 6-3-5/Crazy 8s, JTBD, TRIZ lite) + pensamiento lateral. Se activa con @brainstormy, brainstorm, idear, scamper, sombreros, doble diamante, sesión creativa."
---

# Brainstorming — Skill de facilitación creativa

> Caja de herramientas divergente/convergente para el estudio. Diverge sin juzgar (temp alta) → converge con matriz Impacto×Esfuerzo + JTBD → propuesta accionable + pensamiento lateral.

Adaptado de `vault-lidia` al contexto **estudio de arquitectura argentino** (concursos, obra, BIM, ComfyUI, normativa CABA/municipal).

## When to Activate

- Usuario dice `@brainstormy`, `brainstorm`, `brainstorming`, `idear`, `sesión creativa`, `lluvia de ideas`
- Menciona `scamper`, `sombreros`, `seis sombreros`, `doble diamante`, `design thinking`, `pensamiento lateral`, `reverse`, `crazy 8`, `jtbd`, `triz`
- Pide "ideas para concurso", "concepto para vivienda", "desbloquear proyecto", "re-pensar workflow", "estrategia estudio"
- Encargo sin ficha en `proyectos/00-index.md` o briefing ambiguo

## Core Rules

- **Diverge antes de converger.** Prohibido juzgar en divergencia.
- **1 idea = 1 sticky/línea** (`ID-01: verbo + outcome verificable`).
- **Timebox 25'** (1 pomodoro). Grande → 2 pomodoros (Discover+Define / Develop+Deliver).
- **Cantidad > calidad en divergencia; calidad > cantidad en convergencia.**
- **Siempre cierra con matriz + Top 3 + pregunta de avance.** No dejar lista sin priorizar.
- **Criterios estudio:** viabilidad constructiva, normativa (CABA/municipal), costo material/obra, sustentabilidad, impacto habitante/cliente, tiempo, esfuerzo equipo, coherencia con identidad del estudio.
- **Pensamiento lateral obligatorio**: al menos 20% de ideas wildcards / analogías cruzadas / provocaciones.

## Framework Router

| Señal | Framework | Detalle |
|-------|-----------|---------|
| Problema mal definido / nuevo encargo o concurso | Design Thinking 5 fases → HMW | `design-thinking.md` |
| Estructurar sesión | Double Diamond (Discover-Define / Develop-Deliver) | `double-diamond.md` |
| Mejorar algo existente (obra, workflow, servicio del estudio) | SCAMPER 7×3 | `scamper.md` |
| Evaluar riesgos / decidir entre opciones | Six Thinking Hats (6 rondas 3' c/u) | `six-thinking-hats.md` |
| Equipo bloqueado / "ya probamos todo" | Reverse Brainstorming (causar fracaso → invertir) | `reverse-brainstorming.md` |
| Rápido silencioso / bocetar | Brainwriting 6-3-5 / Crazy 8s (8 en 8') | `brainwriting-635-crazy8s.md` |
| Reframe desde habitante/cliente | JTBD (Job Statement + 4 fuerzas) | `jtbd-jobs-to-be-done.md` |
| Contradicción técnica (luz vs privacidad, costo vs calidad) | TRIZ lite (3 principios) | `triz-lite.md` |

Default sin señal → **Double Diamond**.

## Pensamiento lateral — técnicas

Usar al menos 1 por sesión divergente:

- **Analogía cruzada**: "¿cómo lo resolvería un bosque / una app / una cocina profesional?"
- **Inversión**: formular el objetivo inverso y luego invertir las causas.
- **Provocación (Po)**: premisa absurda → explorar consecuencias (ej. "Po: el edificio no tiene puertas").
- **Palabra aleatoria**: forzar conexión entre estímulo random y el problema.
- **Reframe escalar**: 10× más grande / 10× más barato / sin gravedad / para 2050.

## Workflow — 6 pasos

### 1) Intake (3')
- Leer `wiki/00-index.md` + `proyectos/00-index.md` + `AGENTS.md` + contexto relevante (`lecciones-aprendidas`, `estudio`, `estandares` si aplica).
- Preguntar (1 por vez): ¿Divergir o converger? ¿Cuántas ideas? ¿Criterios? (viabilidad, normativa, costo, sustentabilidad, impacto, esfuerzo).
- Crear `raw/brainstorm/b-YYYY_MM_DD-N.md` crudo con prompt + contexto.

### 2) Seleccionar framework
- Router arriba. Si duda → Double Diamond.

### 3) Divergencia (12' — estilo 0.85)
- Generar N ideas brutas sin filtro, 1 por línea, prohibido "no se puede".
- Técnicas según framework: HMW / SCAMPER 7×3 / Crazy 8 / Reverse causas.
- Incluir ≥20% wildcards / pensamiento lateral.

### 4) Convergencia (7' — estilo 0.2)
- Dot voting 3 votos/persona.
- Matriz Impacto×Esfuerzo 2×2 (Cuadrante 1 = quick win bajo esfuerzo/alto impacto).
- JTBD por Top 3: *Cuando [situación], quiero [motivación], para [outcome]*.

### 5) Synthesize
- Top 3 + Wildcards (idea loca pero barata/viable).
- Mapear a `proyectos/<cliente>-<proyecto>/` o entrada `wiki/` candidata.

### 6) Output + Avance

Entregar:
```markdown
## Ideas brutas (N)
- ID-01 ...
## Priorizadas (Impacto×Esfuerzo)
| Idea | Impacto | Esfuerzo | Cuadrante |
## Top 3 con JTBD
1. Cuando ..., quiero ..., para ... — Idea X
## Wildcards (pensamiento lateral)
- ...
## Próximos pasos → propuesta candidata
- proyectos/<cliente>-<proyecto>/00-index.md borrador o wiki/estudio/...
```

Preguntar **siempre**:
```
¿Avanzo a ficha de proyecto / entrada wiki? (s/N) — Si S, creo la ficha con frontmatter completo y actualizo el índice.
```
- Si `s` → crear ficha/borrador mínimo + actualizar `proyectos/00-index.md` o `wiki/00-index.md`.
- Si `N` → deja crudo + borrador sin crear.

Si surge teoría/entidad nueva relevante → crear/actualizar `wiki/glosario/conceptos|entidades/*.md` con `## Referencias oficiales` + `[[wikilinks]]` (condicional). Si no → no tocar glosario.

## Output Contract

- `## Ideas brutas (N)` ≥ 8 (ideal 12-20)
- `## Priorizadas` matriz completa
- `## Top 3 con JTBD` con Job Statement
- `## Wildcards` ≥1 (pensamiento lateral)
- `## Próximos pasos` con propuesta candidata
- `raw/brainstorm/b-YYYY_MM_DD-N.md` creado

## Banned Patterns

- Lista de 20 ideas sin matriz ni Top 3.
- "Lluvia libre sin framework".
- Ideas sin criterio (viabilidad/normativa/costo).
- Cerrar sin pregunta de avance.
- Crear glosario sin `## Referencias oficiales`.

## References

- `wiki/glosario/conceptos/design-thinking.md`
- `wiki/glosario/conceptos/double-diamond.md`
- `wiki/glosario/conceptos/scamper.md`
- `wiki/glosario/conceptos/six-thinking-hats.md`
- `wiki/glosario/conceptos/reverse-brainstorming.md`
- `wiki/glosario/conceptos/brainwriting-635-crazy8s.md`
- `wiki/glosario/conceptos/jtbd-jobs-to-be-done.md`
- `wiki/glosario/conceptos/triz-lite.md`
- `AGENTS.md` — schema del vault

## Origen

Portado de `P:\00-repos\vault-lidia\.opencode\skills\brainstorming\SKILL.md` y `.opencode/agents/brainstormy.md` — adaptado de LidIA real estate a estudio de arquitectura (criterios, ejemplos, handoff, y referencias).
