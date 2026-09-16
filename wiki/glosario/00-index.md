---
tipo: indice
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-10
tags: [glosario, indice]
---

# Glosario

Conocimiento permanente del estudio — términos normalizados para reuso en wiki, proyectos y prompts.

| Carpeta    | Contenido                                                                                                                                          | Ruta                                |                        |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ---------------------- |
| Software   | Comandos/funciones por herramienta — UNICO `.md` por tool con índice interno                                                                       | [[wiki/glosario/software/00-index   | glosario/software/]]   |
| Entidades  | Personas, clientes, proyectos, herramientas y modelos internos (p-31416, Emilia…)                                                                  | [[wiki/glosario/entidades/00-index  | glosario/entidades/]]  |
| Referentes | Personas y estudios/organizaciones externas que inspiran la práctica (Karpathy, BIG, Foster, ZHA, MVRDV…) + `ia-estudios-internacionales` (global) | [[wiki/glosario/referentes/00-index | glosario/referentes/]] |
| Conceptos  | Teorías y frameworks transversales + metodologías externas (cerebro-digital Karpathy, bim-metodologia/ISO 19650, lean…)                            | [[wiki/glosario/conceptos/00-index  | glosario/conceptos/]]  |
| Interno    | Propio del estudio: standares (tec-/ops-) y playbooks (pbk-*)                                                                                      | [[wiki/glosario/interno/00-index    | glosario/interno/]]    |

> `wiki/glosario/software/` documenta *qué hace cada comando* por herramienta; `wiki/glosario/conceptos/` documenta metodologías externas (bim-metodologia…); `wiki/glosario/interno/` guarda lo propio (standares/pbooks).

## Reglas de calidad (canónico — movidas de `AGENTS.md` 2026-09-10)

Toda entrada `wiki/glosario/**` (software/entidades/referentes/conceptos):

1. **Ruta correcta** — `software/<software>.md` (UNICO .md por herramienta, índice interno, sin carpetas), `conceptos/<concepto>.md`, `referentes/<slug>.md`, `entidades/<slug>.md`, con frontmatter `tipo` correspondiente. Nuevo comando = sección `##` en el `.md` de su herramienta.
2. **Conceptos relacionados** (obligatorio) — `## Conceptos relacionados` con ≥2 `[[wikilinks]]` (la entrada no queda aislada).
3. **Búsqueda web para ampliar** (obligatorio) — `## Referencias` con ≥1 fuente externa verificada además de la oficial (sin 404).
4. **Referentes** (cuando aplica) — persona/estudio con peso disciplinar → crear/actualizar `referentes/<slug>.md` y enlazar.
5. **Índice interno** — cada `.md` único lleva índice `[[#Encabezado exacto]]` al inicio. `00-index.md` por carpeta es obligatorio.

## Contenido actual

- `software/`: 21 herramientas en `.md` único (ver [[wiki/glosario/software/00-index|índice software]])
- `conceptos/`: metodologías (kanban, lean, kaizen, agile-arquitectura, last-planner-system, okr-goals, bim-metodologia…)
- `referentes/`: 20 entradas (personas + estudios; ver índice)
- `entidades/`: registry (solo `00-index.md` + criterios en el índice)
- `interno/`: `standares/` (canónico de estándares) + `pbooks/` (`pbk-*` operativos)
