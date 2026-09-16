# Índice de documentación — CalHon

Guía breve para no confundir los tres tipos de documento del repo. Cada archivo responde una pregunta distinta.

## ¿Cuál uso?

| Archivo | Pregunta que responde | Cuándo se escribe | Contenido típico |
|---|---|---|---|
| [`ADRs.md`](ADRs.md) | ¿**Por qué** decidimos hacerlo así? | Cuando se toma una decisión de diseño | Contexto → decisión → consecuencias. No cambia. |
| [`FEATURES.md`](FEATURES.md) | ¿**Qué hace** la app hoy? | Cuando se agrega o quita una funcionalidad | Lista de features con estado. |
| [`CHANGELOG.md`](CHANGELOG.md) | ¿**Qué cambió** y **cuándo**? | Al cerrar cada cambio | Historial cronológico con fecha y hora. |
| [`PAGOS.md`](PAGOS.md) | ¿**Cómo** se divide el pago del presupuesto? | Cuando se define el esquema de pagos | Tabla de variantes por cantidad de etapas. |

Analogía: **ADR** es un acta de reunión (decisión + porqué), **FEATURES** es el catálogo del producto y **CHANGELOG** es el diario de cambios.

## Cómo escribirlos

- **Un hecho puede ir en varios lados** con distinto propósito. Ejemplo: *"elegimos jsPDF porque no hay backend"* → decisión (ADR). *"Exporta a PDF"* → feature (FEATURES). *"Se implementó el PDF el 2026-08-08"* → cambio (CHANGELOG).
- **ADR**: una sección nueva por decisión, numerada `0001`, `0002`… Se marca el estado (`Aceptado`, `Superado`).
- **FEATURES**: un item por funcionalidad con estado `✓ Funcional` / `🔧 En desarrollo` / `⏳ Pendiente`. Sin fecha.
- **CHANGELOG**: una entrada por cambio con `YYYY-MM-DD HH:mm` y formato `Agregado | Cambiado | Corregido | Eliminado`. Los más nuevos van arriba.

## Enlaces (compatibles con Obsidian)

- Índice de cada documento: enlaces `[Título](#ancla)` a las secciones, con ancla estilo GitHub (minúsculas, espacios → guiones).
- En Obsidian también funciona el enlace nativo al encabezado: `[[#Título del encabezado|etiqueta]]`.

## Convenciones

- Fechas y horas en `YYYY-MM-DD HH:mm` (24 h), huso local.
- Montos y porcentajes en formato es-AR.
- Fuentes oficiales citadas en los ADR (CPAU, Clarín ARQ, PDFs locales).
