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
