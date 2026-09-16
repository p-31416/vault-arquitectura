---
tipo: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, concepto, 5s, archivos, orden, lean]
---

# 5S para archivos (digital + físico)

> Seiri–Seiton–Seiso–Seiketsu–Shitsuke aplicadas al vault: carpetas, nomenclatura, limpieza, estándar y disciplina. Primera herramienta Lean que se implementa — antes que cualquier otra.

- [Definición](#definición)
- [Las 5S](#las-5s)
- [5S digital en el vault](#5s-digital-en-el-vault)
- [5S física (oficina/obra)](#5s-física-oficinaobra)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Definición

5S = sistema para **reducir desperdicio manteniendo el lugar ordenado con señales visuales**. Típicamente la **primera** técnica Lean que adopta una organización, base para TPM, JIT, Six Sigma. Es cíclica: ordenar → limpiar → estandarizar → sostener → volver a ordenar.

## Las 5S

| S | Japonés | Idea | Técnica |
|---|---------|------|---------|
| 1 | **Seiri** (clasificar) | Quedarse solo con lo necesario | **Red tagging**: etiquetar lo dudoso, mover a zona de cuarentena, decidir (archivar/tirar/reasignar). Recupera espacio. |
| 2 | **Seiton** (ordenar) | Un lugar para cada cosa, cada cosa en su lugar | Pintar pisos, rotular, kits con "justo lo necesario", ubicaciones etiquetadas por color. |
| 3 | **Seiso** (limpiar) | Limpiar + inspeccionar | Limpieza diaria asignada; en ambiente limpio se detectan fallas (filtraciones, errores) temprano. |
| 4 | **Seiketsu** (estandarizar) | Mantener las 3 primeras | Responsables + rutinas integradas al trabajo + checklists + tableros visuales. **Prevención**: que no se vuelva a acumular. |
| 5 | **Shitsuke** (sostener) | Hacerlo hábito | La más difícil: cartelería, rondas, revisiones, auditorías hasta que sea "como se hacen las cosas". Sin esta S, las otras colapsan. |

## 5S digital en el vault

Mapeo directo a reglas del vault (ver `AGENTS.md`):

| S | Aplicación vault |
|---|-----------------|
| Seiri | `activos/` fuera de git; borrar duplicados; cuarentena `temp/` con fecha de vencimiento 30 días |
| Seiton | Estructura fija `proyectos/<cliente>-<proyecto>-<ciudad>/` + snake_case + `00-README → 04-backlog` en WFs ComfyUI; `[[wikilinks]]` como "rótulos" |
| Seiso | Lint trimestral (índice vs páginas, huérfanas, links rotos a activos) — workflow `Lint` del vault |
| Seiketsu | `AGENTS.md` + templates de proyecto + frontmatter obligatorio = estándar escrito y visible |
| Shitsuke | Ritual semanal 15 min + cierre de sesión en `raw/sessions/` obligatorio; auditoría 5S mensual de 30 min |

Checklist Seiton digital (DoD de carpeta nueva): ¿tiene `index.md` con frontmatter? ¿nombres en snake_case? ¿binarios solo como referencia de ruta? ¿entrada en `index.md` padre con resumen 1 línea?

## 5S física (oficina/obra)

- Mesa/plotter: red tag a muestras y rollos viejos; kits por fase (concurso / legajo / obra).
- Obra: libro de obra convive con foto-regla (misma toma, misma hora) que alimenta `raw/`; tablero físico espejo del Kanban Leantime para capataces sin celular.
- Beneficio medido típico: menos m² para archivo, menos compras duplicadas (se encuentra antes de pedir), menos accidentes por obstáculos.

## Conceptos relacionados

- [[wiki/glosario/conceptos/lean|lean]]
- [[wiki/glosario/conceptos/kaizen|kaizen]]
- [[wiki/glosario/conceptos/kanban|kanban]]

## Referencias

- US EPA — Lean Thinking and Methods 5S (pilares, red tagging, implementación): https://www.epa.gov/lean/lean-thinking-and-methods-5s (verificado 2026-09-09 — 200)
- Productivity Press: Hirano, *5 Pillars of the Visual Workplace* (1995); *5S for Operators* (1996) — vía bibliografía EPA
- Lean Construction Institute: https://www.leanconstruction.org/ (verificado 2026-09-09 — 200)
