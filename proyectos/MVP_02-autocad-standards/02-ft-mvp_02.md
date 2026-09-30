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
| n_01 | Layers y nomenclatura | — | 🔄 En progreso — SET-Replanteo |
| n_02 | Plot styles (CTB) y grosores | n_01 | 🔜 Pendiente |
| n_03 | Text styles y dimension styles | n_01 | 🔜 Pendiente |
| n_04 | Templates DWT | n_01–n_03 | 🔜 Pendiente |
| n_05 | Bloques estándar | n_01 | 🔜 Pendiente |
| n_06 | Naming de planos y presentación | n_01–n_04 | 🔜 Pendiente |
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

### ADR-003 — SET como MVP concreto del n_01
**Contexto**: el roadmap general de niveles es abstracto; falta un plano concreto que demuestre el estándar aplicado.
**Decisión**: el SET — Plano de Replanteo Arquitectónico — es el MVP concreto del n_01. Define capas, standards, comandos, tips y AutoLISP aplicados a un tipo de plano real. Sirve como plantilla para los otros niveles (n_02 a n_06).
**Consecuencias**: el SET demuestra que el manifiesto funciona en la práctica. Cada nivel posterior (n_02 a n_06) sigue el mismo patrón: catálogo + justificación + comandos + tips + AutoLISP.

## Glosario asociado

Cada comando AutoCAD usado en los `.lsp` se documenta en:
[[wiki/glosario/software/autocad|wiki/glosario/software/autocad]]

Ej: `entmake.md`, `command.md`
