---
tipo: concepto
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-07
tags: [sdd, spec-driven-development, spec-kit, spec, plan, opencode]
idioma: es
---

# SDD — Spec-Driven Development

> Define qué construir antes de construirlo. El spec se vuelve ejecutable y genera la implementación, en lugar de guiarla y luego descartarse.

## Índice interactivo

- [[#1. Cómo se aplica al vault-arquitectura]]
- [[#2. Qué es SDD]]
- [[#3. Qué es un Spec]]
- [[#4. Qué es un Plan]]
- [[#5. Qué son Tasks y Implement]]
- [[#6. Constitución, Clarify, Analyze y Checklist]]
- [[#7. Flujo híbrido para este vault — Spec Kit + template liviano via opencode]]
- [[#8. Convenciones de archivos en este vault]]
- [[#9. Conexiones con otros conceptos del wiki]]
- [[#10. Referencias oficiales]]

---

## 1. Cómo se aplica al vault-arquitectura

> Esta sección es la puerta de entrada. Todo lo que sigue se lee a través de este lente.

**Regla de oro — SPEC FIRST, siempre preguntar antes de crear código:**

```
spec  →  plan  →  tasks  →  implement  →  converge
  ✓       ✓       ✓           ↻ hasta converger
```

Para cada entrega en `vault-arquitectura`:

| Fase | Dónde vive | Gate | Quién aprueba |
|------|------------|------|---------------|
| **Spec** | `specs/YYMMDD-{tema}_spec.md` | Describe *qué* y *por qué*, sin stack | Sol — `✓ spec` |
| **Plan** | `specs/YYMMDD-{tema}_plan.md` | Describe *cómo*, con stack y arquitectura | Sol — `✓ plan` |
| **Tasks** | `specs/YYMMDD-{tema}_tasks.md` | Checklist por pomodoros / hitos | — |
| **Implement** | `proyectos/{fecha}-{proyecto}/` + `.github/workflows/` + `wiki/` | Ejecuta tasks, respeta spec/plan | opencode + Sol |
| **Converge** | validación contra spec/plan/tasks | Repite implement hasta converger | — |

**Reglas del vault:**

- **Planes nunca duplicados:** todo plan/spec vive **solo** en `/specs/` con nombre `YYMMDD-{tema_snake}.md` (ej: `260907-vault_cerbero.md`). En `proyectos/{fecha}-{proyecto}/` solo van `workflows/`, `apps/`, `documentacion/`, `agentes/` y se linkea con `[[specs/260907-vault_cerebro]]`.
- **Preguntar antes de crear código:** antes de cualquier `.github/workflows/*.yml`, `scripts/` o `.lsp`, debe existir un spec aprobado.
- **Opencode como motor:** todo el flujo se ejecuta desde **opencode en terminal** (`P:\00-repos\proyecto-pi\vault-arquitectura`) con `specify` + comandos `/speckit.*` (o `$speckit-*` en modo skills). La transición futura a VPS mantiene el mismo prompt y solo cambia el disparador a `cron` local.
- **Caso actual:** `260907-brain_emilia` — su spec es `[[specs/260907-vault_cerebro]]`. El workflow `.github/workflows/opencode-vault.yml` creado previamente fue **retirado por anticiparse al spec** y se recrea solo tras `✓ spec` + `✓ plan`.

---

## 2. Qué es SDD

**Spec-Driven Development** invierte la jerarquía clásica: durante décadas el código fue rey y el spec era andamiaje descartable. En SDD el **spec se vuelve ejecutable** y genera implementación de forma directa.

- Desarrollo guiado por **intención**: el spec define el *qué* antes del *cómo*.
- Creación rica de specs con guardarraíles y principios del proyecto.
- Refinamiento en múltiples pasos, en lugar de generación one-shot desde un prompt.
- Apoyo en capacidades avanzadas de modelos de IA para interpretar el spec.

En este vault, SDD es el puente entre la **capacidad de mejora diaria** y la **ejecución técnica**: cada repetición de un proceso se vuelve una oportunidad de refinar el spec.

---

## 3. Qué es un Spec

Un **spec** describe *qué* se quiere construir y *por qué*, sin prescribir stack tecnológico.

**Contenido mínimo (template liviano del vault):**

- Contexto y objetivo verificable
- Alcance / no-alcance
- Criterios de aceptación (given/when/then o checklist)
- Ejemplos de uso y casos borde
- Riesgos y dependencias

**En Spec Kit:** se crea con `/speckit.specify` (o `speckit-specify` en modo skills). Enfocado en historias de usuario y requisitos.

> Ver también: [[wiki/glosario/conceptos/sdd-spec_driven_development#4. Qué es un Plan|Plan]] — el spec alimenta al plan, nunca lo reemplaza.

---

## 4. Qué es un Plan

Un **plan** describe *cómo* se va a construir lo especificado, con decisiones técnicas explícitas.

**Contenido mínimo:**

- Stack y arquitectura elegida (ej: OpenCode + OpenAI cuenta Emilia via OpenCode Zen free tier, Fathom MCP, cowork schedule / GitHub Actions)
- Diagramas de flujo y decisiones (ADRs livianos)
- Alternativas evaluadas y trade-offs
- Estimación por pomodoros / hitos

**En Spec Kit:** se crea con `/speckit.plan` (o `speckit-plan`). Se nutre del spec y de la constitución del proyecto.

> Ver también: [[wiki/glosario/conceptos/sdd-spec_driven_development#3. Qué es un Spec|Spec]] y [[wiki/glosario/conceptos/sdd-spec_driven_development#5. Qué son Tasks y Implement|Tasks]]

---

## 5. Qué son Tasks y Implement

- **Tasks** (`/speckit.tasks`): descompone el plan en checklist accionable y ordenado. Cada task es una unidad ejecutable y verificable. En el vault equivale a `specs/YYMMDD-{tema}_tasks.md`.
- **Implement** (`/speckit.implement`): ejecuta los tasks y construye la feature según el plan. Itera hasta que `/speckit.converge` reporte **Converged**.

Ciclo brownfield recomendado para este vault (proyecto ya existente): mantener actualizaciones de tooling separadas de la evolución de artefactos en `specs/`.

---

## 6. Constitución, Clarify, Analyze y Checklist

Comandos que elevan la calidad antes y después del plan:

| Comando | Cuándo | Qué hace |
|---------|--------|----------|
| `/speckit.constitution` | Una vez por proyecto | Define principios rectores (calidad, testing, UX, performance) que guían todo lo siguiente |
| `/speckit.clarify` | Antes de `/speckit.plan` (recomendado) | Aclara áreas sub-especificadas (antes `/quizme`) |
| `/speckit.analyze` | Después de `/speckit.tasks`, antes de implement | Análisis de consistencia y cobertura cruzada entre spec/plan/tasks |
| `/speckit.checklist` | Opcional | Genera checklists de calidad que validan completitud y claridad (como tests para el spec) |
| `/speckit.converge` | Después de implement | Evalúa código contra spec/plan/tasks y anexa trabajo restante como nuevos tasks |

---

## 7. Flujo híbrido para este vault — Spec Kit + template liviano via opencode

> **Respuesta a "¿se pueden hacer las dos cosas?" — Sí, y así se hace aquí, siempre desde opencode.**

**Opción A — Spec Kit oficial (recomendado para trazabilidad completa):**

```powershell
# requiere uv (https://docs.astral.sh/uv/)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.12.11
specify init . --here --force --integration opencode
# o: specify init 260907-brain_emilia --integration opencode
```

Dentro de opencode en terminal, en `P:\00-repos\proyecto-pi\vault-arquitectura`:

```
/speckit.constitution  # principios del vault
/speckit.specify       # describe qué (genera spec en specs/)
/speckit.clarify       # aclara dudas
/speckit.plan          # describe cómo
/speckit.tasks         # descompone en checklist
/speckit.implement     # ejecuta
/speckit.converge      # verifica hasta converger
```

**Opción B — Template liviano del vault (sin CLI, compatible con todo):**

```
specs/YYMMDD-{tema}_spec.md   → qué/por qué
specs/YYMMDD-{tema}_plan.md   → cómo
specs/YYMMDD-{tema}_tasks.md  → checklist
proyectos/{fecha}-{proyecto}/ → implementación
```

**Híbrido adoptado en `vault-arquitectura`:** se usa **Spec Kit via opencode** como orquestador, pero los artefactos viven con la convención liviana `specs/YYMMDD-{tema}_*.md` y se linkean con `[[wikilinks]]`. Si Spec Kit no está instalado, el flujo liviano sigue funcionando sin bloqueo. Las dos vías convergen en el mismo `/specs/` como fuente única.

---

## 8. Convenciones de archivos en este vault

```
specs/
├── 260907-vault_cerbero.md          # plan existente (pre-SDD, se migrará a spec+plan)
├── 260907-github_actions_cerbero_spec.md   # ← próximo spec SPEC FIRST
├── 260907-github_actions_cerbero_plan.md   # ← solo tras ✓ spec
└── 260907-github_actions_cerbero_tasks.md  # ← solo tras ✓ plan

proyectos/260907-brain_emilia/
├── index.md                # ficha con frontmatter + link [[specs/260907-vault_cerebro]]
├── documentacion/
├── workflows/              # workflows documentados (no planes)
├── apps/
├── agentes/                # docu de agentes implementados
└── reuniones/              # notas raw → wiki/fuentes
```

> Ver [[proyectos/prefijos-documentacion|Prefijos de documentación]] para `filo-`, `fram-`, `spec-`, `ft-`, `log-`.

---

## 9. Conexiones con otros conceptos del wiki

- **Cerebro digital:** [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]] — SDD aporta la capa *spec-first* al flujo raw → entidades → wiki. El spec es la memoria intencional antes del código.
- **Diseño y exploración:** *design-thinking*, *double-diamond* (pendientes) — SDD complementa el divergir/converger con artefactos verificables.
- **Herramientas:** [[wiki/glosario/software/opencode|opencode]] — motor que ejecuta el flujo SDD; [[wiki/glosario/software/git|git]] + `github-cli` para versionado de specs/plans; `specs/` como CDE liviano (ver [[wiki/glosario/conceptos/bim-metodologia|bim-metodologia]] para CDE).
- **Proyecto vivo:** [[proyectos/260907-brain_emilia/00-index|260907-brain_emilia]] ↔ [[specs/260907-vault_cerebro|260907-vault_cerbero]] — ejemplo vivo de SDD en este vault.
- **Entidad espejo (eliminada 2026-09-09):** existió `wiki/glosario/entidades/sdd-spec_driven_development.md` como registry; se eliminó por duplicada — SDD es concepto, el registry vivía en una línea y duplicaba mantenimiento.

---

## 10. Referencias oficiales

- GitHub Spec Kit — Toolkit Spec-Driven Development: https://github.com/github/spec-kit — spec ejecutable que genera implementación, con flujo `specify → plan → tasks → implement → converge`, CLI `specify` y soporte para 30+ agentes incluyendo **opencode**. Ver `spec-driven.md` para metodología completa y `README.md` para quickstart.
- Spec Kit — Supported AI Coding Agent Integrations: https://github.github.io/spec-kit/reference/integrations.html — lista de integraciones (incluye opencode, claude, copilot).
- Spec Kit — Quickstart y CLI Reference: https://github.github.io/spec-kit/ (ver también `docs/install/uv.md` y `src/specify_cli`).
- Spec-Driven Development — Filosofía core: especificaciones como fuente de verdad, refinamiento multi-paso y convergencia (ver `spec-driven.md` en el repo).
- Este vault — `AGENTS.md` y `proyectos/prefijos-documentacion.md` para convenciones locales de `specs/` y `proyectos/`.

> Verificación: enlaces a `github.com/github/spec-kit` y `github.github.io/spec-kit` verificados vía `webfetch` el 2026-09-07 (repo público, 133k stars, release 1.0.0).
