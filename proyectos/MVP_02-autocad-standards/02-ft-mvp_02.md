---
tipo: road-map
mvp: 02
fecha_creacion: 2026-06-30
ultima_actualizacion: 2026-06-30
tags: [mvp_02, ft, roadmap]
---

# MVP_02 — Plan técnico global

## Roadmap

| Nivel | Tema | Depende de | Estado |
|-------|------|-----------|--------|
| n_01 | Layers y nomenclatura | — | 🔜 Pendiente |
| n_02 | Plot styles (CTB) y grosores | n_01 | 🔜 Pendiente |
| n_03 | Text styles y dimension styles | n_01 | 🔜 Pendiente |
| n_04 | Templates DWT | n_01–n_03 | 🔜 Pendiente |
| n_05 | Bloques estándar | n_01 | 🔜 Pendiente |
| n_06 | Naming de planos y presentación | n_01–n_04 | 🔜 Pendiente |

## Decisiones globales

Las decisiones que afectan a todo el MVP se registran acá. Las específicas de cada nivel van en `02-ft-n_XX.md`.

### ADR-001 — Estructura de niveles
**Contexto**: los estándares AutoCAD abarcan muchos temas. Necesitamos una progresión lógica.
**Decisión**: niveles secuenciales donde cada uno depende del anterior. Layers primero porque todo lo demás (CTB, dims, templates) referencia layers.

### ADR-002 — Formato de registro de decisiones
**Contexto**: cada nivel implica decisiones (color X, grosor Y). Sin registro, se pierde el por qué.
**Decisión**: usar ADR embebidos en `02-ft-n_XX.md`. Formato: `ADR-NN — Título` con Contexto, Decisión, Consecuencias.

## Glosario asociado

Cada comando AutoCAD usado en los `.lsp` se documenta en:
[[wiki/glosario/software/autocad|wiki/glosario/software/autocad]]

Ej: `entmake.md`, `command.md`
