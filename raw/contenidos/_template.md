---
tipo: reporte-contenidos
fecha: YYYY-MM-DD
fuente_binaria: activos/videos/<prefijo>-YYYY-MM-DD-<slug>.mkv  # o activos/pdfs/...pdf / manual SOL
transcript: activos/videos/<...>.txt | wiki/raw/YYYY-MM-DD-<slug>.md
duracion: ~XX min | paginas: N
idioma: es
tags: [tag1, tag2]
estado: propuesta  # propuesta → aprobado → en-wiki → descartado
---

# Reporte contenidos — <slug> — YYYY-MM-DD

> 1 línea: qué se procesó y por qué importa al estudio.

## 0. Gate HITL

> `¿Avanzo a wiki/? (s/N)` — SOL marca: ✅ aprobar / ✏️ corregir / ❌ descartar / 💡 añadir con Emilia
> Sin `s` no hay `write` en `wiki/` (`AGENTS.md` HITL).

## 1. Resumen (5 bullets, lenguaje positivo)

- ...

## 2. Qué parte de la wiki alimenta

| # | Destino wiki (ruta absoluta sin ext) | Tipo | Acción | Sección destino | Prioridad | Owner escribe |
|---|---|---|---|---|---|---|
| 1 | [[wiki/estudio/entrega-servicio-ia\|entrega-servicio-ia]] | metodologia | crear | ## Proceso | alta | @contenidos con s |
| 2 | [[wiki/glosario/software/gohighlevel\|gohighlevel]] | software | actualizar | ## Pipeline GHL | media | vía @vaultworm-arq con s |
| 3 | [[wiki/glosario/conceptos/cerebro-digital-karpathy\|cerebro-digital-karpathy]] | concepto | enlazar | — | baja | vía @vaultworm-arq con s |
| 4 | [[wiki/glosario/interno/pbooks/pbk-entrega-ia\|pbk-entrega-ia]] | pbook | crear | — | alta | @contenidos con s |

## 3. Contenidos extraídos (sin inventar, con cita verbatim)

| Concepto / terminología | Cita verbatim (transcript/fuente) | Minutaje / página | Interpretación curada |
|---|---|---|---|
| GHL workflow | "..." | 12:34 | ... |

## 4. Ruta donde guardará + frontmatter propuesto

| Destino | Ruta exacta | Frontmatter propuesto |
|---|---|---|
| wiki/estudio | `wiki/estudio/entrega-servicio-ia.md` | `tipo: metodologia, fecha_creacion: YYYY-MM-DD, tags: [ghl, entrega, ia], idioma: es` |
| glosario software | `wiki/glosario/software/gohighlevel.md#Pipeline` | `UNICO .md por tool — nueva sección ## Pipeline` |

> Frontmatter obligatorio `AGENTS.md:59-68` — `tipo, fecha_creacion, ultima_actualizacion, tags, idioma`.

## 5. Tags + wikilinks previstos

- Tags: [...]
- `## Conceptos relacionados` previsto con ≥2 [[wikilinks]] absolutos (`wiki/glosario/00-index.md:27`)
- Índice interno previsto con `[[#Encabezado exacto]]` — nunca `[Texto](#slug)` con tildes

## 6. Referencias verificadas 200 (sin 404)

| # | Fuente | URL | Status | Tipo |
|---|---|---|---|---|
| 1 | Docs oficial GoHighLevel | https://... | 200 webfetch | oficial |
| 2 | Paper / externa | https://... | 200 webfetch | externa |

> `AGENTS.md:Verificar enlaces` + `wiki/glosario/00-index.md:28` — ≥1 oficial +1 externa 200. Si no verificable, mover a Preguntas.

## 7. Propuestas wiki concretas

- Crear/actualizar `[[wiki/estudio/...]]` — 1 línea qué aporta
- Glosario vía @vaultworm-arq `[[wiki/glosario/software/...#Sección]]`

## 8. Estado wiki (post-s — completar tras `¿Avanzo?`)

| Destino | Acción | Link creado/actualizado | Fecha |
|---|---|---|---|
| ... | crear | [[wiki/estudio/...]] | YYYY-MM-DD |

## 9. Decisiones SOL

- [ ] Aprobar / [ ] Corregir / [ ] Descartar por propuesta
- ...

## 10. Preguntas para SOL

- Qué falta, qué descartar, qué priorizar con Emilia

## 11. Pipeline

- Comando transcript: `P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/videos/..." --model medium --language es`
- O manual SOL: `C:\...\manual.pdf` → `wiki/raw/YYYY-MM-DD-<slug>.md` (`tipo: raw`, `fuente_binaria: <path>`)
