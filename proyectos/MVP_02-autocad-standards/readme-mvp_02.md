---
tipo: readme
mvp: 02
fecha_creacion: 2026-06-30
ultima_actualizacion: 2026-06-30
tags: [readme, mvp_02, guia, reglas]
---

# MVP_02 — Estándares y Reglas de Diseño en AutoCAD

Puerta de entrada al MVP de estándares AutoCAD. Si llegás a esta carpeta por primera vez, empezá acá.

## Qué es esto

Un **framework de documentación de estándares AutoCAD** para el estudio. Captura, organiza y versiona:

- **Decisiones de diseño** (por qué layer X se llama así, por qué usamos color 7 para muros)
- **Reglas técnicas** (nomenclatura de layers, CTB, tipos de línea, grosores)
- **Defaults opinados** (dimension styles, text styles, plot settings)
- **AutoLISP asociado** (comandos que aplican estos estándares automáticamente)

Todo sale de la práctica real del estudio y queda documentado con **registro de decisiones** (ADR = Architecture Decision Record).

## Documentos: qué pregunta responde cada uno

| Archivo | Pregunta | Contenido |
|---------|----------|-----------|
| `00-filo` | **¿POR QUÉ?** | Filosofía, principios, propósito del estándar |
| `01-spec` | **¿QUÉ?** | Catálogo universal: capas, bloques, estilos. Cada item con nombre, color, linetype, lineweight |
| `02-ft` | **¿CÓMO?** | Metodología: comandos, pasos, AutoLISP |
| `03-log` | **¿CUÁNDO?** | Bitácora de decisiones e iteraciones |
| `SET-{tipo}` | **¿AQUÍ Y AHORA?** | Aplicación concreta del spec+ft a un tipo de plano. Norma: `SET_0x-XXX_Descripcion.md` (ej: `SET_01-REP_Replanteo.md`, `SET_02-EST_Estructura.md`). Numerados por orden de aparición. |

## Flujo de conocimiento iterativo

> **Regla de agentes**: `@sherlock` escribe en `raw/` (solo BUSCA: `raw/research/` + `raw/sessions/` + `raw/reports/`; NUNCA toca `wiki/`). `@vaultworm-arq` analiza los crudos de `raw/` y escribe en `wiki/` (solo con `s` explícita). `@contenidos` genera versión legible intermedia en `raw/contenidos/`.

```
@sherlock investiga → raw/research/*.md (+ raw/sessions/, raw/reports/)
      ↓
@vaultworm-arq analiza crudos raw/ → digest → propone wiki entries + links
      ↓
@sherlock investiga más (referencias del digest) → nuevo raw/research/
      ↓
@vaultworm-arq re-analiza → digest actualizado
      ↓
...hasta convergencia → `s` → wiki/ canonizado
      ↓
Manuales de uso + lecturas sugeridas
```

- **`raw/docs/`**: crudos de Perplexia y otras fuentes → procesados por @sherlock → `raw/sessions/`
- **`raw/sessions/`**: sesiones de trabajo con registro verbatim
- **`raw/vaultworm-arq/`**: digest de análisis
- **`raw/brainstorm/`**: sesiones de brainstorming

## Crudos de referencia

- `docs/` contiene archivos crudos de Perplexia sobre AutoCAD, cursos, MCP, licencias → fuente primaria para sherlock

## Cómo está organizado

```
MVP_02-autocad-standards/
│
├── readme-mvp_02.md          â† Este archivo. Puerta de entrada.
├── 00-filo-mvp_02.md         â† Manifiesto (visión, principios, por qué)
├── 01-spec-mvp_02.md         â† Spec viva (acuerdo macro + historial)
├── 02-ft-mvp_02.md           â† Plan técnico global (roadmap, decisiones)
├── 03-log-mvp_02.md          â† Transiciones entre niveles
│
├── n_01-layers/              â† Nivel 1 — Layers y nomenclatura
├── n_02-plot/                â† Nivel 2 — Plot styles (CTB) y grosores
├── n_03-text-dims/           â† Nivel 3 — Text styles y dimension styles
├── n_04-templates/           â† Nivel 4 — Templates (DWT) y config inicial
└── n_XX-.../                 â† Próximos niveles
```

Cada nivel `n_XX-*/` sigue el mismo esquema de MVP_01:

| Archivo | Rol |
|---------|------|
| `01-spec-n_XX.md` | Acuerdo macro del nivel |
| `02-ft-n_XX.md` | Plan técnico paso a paso |
| `03-log-n_XX.md` | Bitácora de fallos e iteraciones |
| `lisp-{nombre}.lsp` | AutoLISP que aplica el estándar |

## Vinculación con el vault

- **Glosario de comandos**: cada comando AutoCAD usado en los `.lsp` se documenta en [[wiki/glosario/software/autocad|wiki/glosario/software/autocad]]
- **Wiki destino**: los estándares consolidados se reflejan en `wiki/estandares/tecnico/`
- **Activos**: DWT, CTB, PAT y demás binarios en `activos/proyectos/mvp_02-autocad-standards/`

## Reglas

1. **Spec es la guía**: se escribe antes de implementar cualquier regla.
2. **Toda decisión se registra**: cada nivel tiene ADR en `02-ft-` o `03-log-`.
3. **Un estándar no documentado no existe**: si no está acá, no es oficial.
4. **AutoLISP aplica el estándar**, no lo reemplaza. El `.md` explica qué hace y por qué.
5. **Sync automático**: cuando un nivel se consolida, pasa a `wiki/`.
6. **Norma SET**: `SET_0x-XXX_Descripcion.md` donde `0x` = orden de aparición (01, 02...), `XXX` = disciplina (REP, EST, ARQ, ELE, SAN, MUN, GEN), `Descripcion` = nombre corto. Foco actual: `SET_01-REP_Replanteo.md` únicamente.
