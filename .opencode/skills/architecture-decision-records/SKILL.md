---
name: architecture-decision-records
description: "Actas de decisión ADR (formato Nygard) para el estudio. Se activa con ADR, registra esta decisión, elegimos X vs Y, por qué elegimos X. Decisiones de concurso, DD, obra, BIM (CAD→BIM), ComfyUI, stack vault. Vive en specs/ y lecciones-aprendidas, no en docs/adr/."
---

# Architecture Decision Records — estudio de arquitectura

> Portado de `vault-lidia` y adaptado: allá `docs/adr/NNNN-*.md`; acá las decisiones viven donde el estudio las usa: `specs/YYMMDD-<tema>.md` (SPEC/PLAN/TASKS/MILESTONES-OKRs) + `wiki/lecciones-aprendidas/` para cerradas + referencia en `log.md`. Formato ADR liviano de Michael Nygard.

## When to Activate

- Usuario dice `ADR`, `registra esta decisión`, `acta de decisión`
- Se elige entre alternativas con trade-off: sistema constructivo, material, partido, BIM vs CAD, checkpoint SD1.5 vs SDXL, DirectML patch, pass-through a Leantime
- Pregunta `¿por qué elegimos X?` (leer ADRs existentes en `specs/`)

## ADR Format (en specs/)

```markdown
# ADR-YYYY-MM-DD-<slug>: [Decisión]

**Fecha**: YYYY-MM-DD
**Estado**: propuesta | aceptada | deprecada | superada por ADR-YYYY-MM-DD-<otro>
**Deciden**: [SOL, equipo, cliente]
**Proyecto**: [proyectos/<cliente>-<proyecto>-<ciudad>/ o estudio]

## Contexto
[2-5 líneas: problema, restricciones normativa/costo/plazo, fuerzas]

## Decisión
[1-3 líneas en presente: "Usamos X"]

## Alternativas
### Alternativa 1: [Nombre]
- Pros / Contras / Por qué no
### Alternativa 2: [Nombre]
- Pros / Contras / Por qué no

## Consecuencias
### Positivas / Negativas / Riesgos + mitigación
## Trazabilidad
- spec: [[specs/YYMMDD-<tema>]] | wiki: [[wiki/...]] | activos: [activos/...] | lección: [[wiki/lecciones-aprendidas/...]]
```

## Workflow

1. **Detectar** (explícito: "vamos con X", "trade-off vale porque..."; implícito: se compara y se concluye → sugerir ADR, no auto-crear sin `s`)
2. **Numerar** por fecha-slug (no secuencial global: `ADR-2026-09-09-directml-rx570`)
3. **Borrador → revisión SOL** → solo con `s` se escribe en `specs/` y se enlaza desde proyecto/wiki/`log.md`
4. **Leer**: ante `¿por qué X?` buscar en `specs/*` + `wiki/lecciones-aprendidas/*` y citar Contexto+Decisión
5. **Ciclo**: `propuesta → aceptada → [deprecada | superada]`, siempre linkeando reemplazo

## Qué merece ADR (estudio)
| Categoría | Ejemplos |
|---|---|
| Partido/sistema | Estructura H°A° vs acero, fachada ventilada vs EIFS, fundación |
| Normativa | Interpretación código CABA/municipal, Ley 24.335 incumbencia, PH |
| BIM/CAD | Plantilla, layers, familias, CAD→BIM, `C:\BIM\` vs `activos/bims/` |
| Visualización | ComfyUI checkpoint, ControlNet, RX570 flags, patch VRAM WMI |
| Vault/IT | Agente reuniones vs vaultworm-arq, Fathom→specs→Leantime, n8n omitido |
| Proceso | Concurso→entrega, Last Planner, Kaizen semanal |

No: nombres de variables, formato menor, decisiones triviales.

## Origen
Portado de `P:\00-repos\pitau-tech\vault-lidia\.opencode\skills\architecture-decision-records\SKILL.md` — adaptado de `docs/adr/` dev a `specs/` + `lecciones-aprendidas` del estudio.
