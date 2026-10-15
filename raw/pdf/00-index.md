---
tipo: indice
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [indice, pdf, raw, fuentes, hitl]
---

# raw/pdf — Crudo de PDFs y fichas de extracción

> Espejo de [[raw/yt/00-index|raw/yt]] para documentos. Cada PDF deja una ficha con metadata, índice, stats e inventario de imágenes, más referencia al binario. El texto completo solo se guarda si la licencia lo habilita (propio, libre, open-access). Libros con copyright: solo ficha + extractos breves fair use + binario en `/activos/` (gitignored).

## Estructura

```
raw/pdf/
├── 00-index.md                        ← este archivo
└── YYYY-MM-DD-<slug>-ficha.md         ← una ficha por PDF (metadata + TOC + stats + imágenes)
```

## Reglas

- Binario original → `activos/fuentes/<slug>/` (gitignored, no entra a git). El `.md` solo referencia ruta.
- Imágenes útiles → `activos/fuentes/<slug>/img/pXX-nombre.jpg` + pie + página en la ficha.
- Texto completo verbatim solo si licencia habilita. Si no, extractos breves en el §12 del reporte de `raw/contenidos/` (sin capa cache adicional).
- Reporte legible siempre en `raw/contenidos/` vía @contenidos. A `wiki/fuentes` solo con tu `s`.

## Fichas

| Fecha | PDF | Páginas | Palabras | Imágenes | Ficha | Binario | Estado |
|---|---|---|---|---|---|---|---|
| 2026-10-13 | Baudrillard 1994 Simulacra and Simulation (Glaser/Michigan) | 108 | 57294 | 1 (portada) | [[raw/pdf/2026-10-13-baudrillard-1994-ficha\|2026-10-13-baudrillard-1994-ficha]] | `activos/fuentes/baudrillard-1994/Jean_baudrillard-simulacra-and-simulation.pdf` | propuesta |
