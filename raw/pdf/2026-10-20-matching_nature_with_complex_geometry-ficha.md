---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/matching_nature_with_complex_geometry/Matching nature with ‘Complex Geometry’.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Matching nature with ‘Complex Geometry’.pdf
titulo: Matching nature with ‘Complex Geometry’
titulo_provisional: si
autor: Alistair Smith
idioma: en
paginas: 10
palabras: 3847
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — Matching nature with ‘Complex Geometry’

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/matching_nature_with_complex_geometry/Matching nature with ‘Complex Geometry’.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Matching nature with ‘Complex Geometry’.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-matching_nature_with_complex_geometry-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | Microsoft Word - DN04 Sections.doc |
| Autor | Alistair Smith |
| Creator / Producer | PScript5.dll Version 5.2 / Acrobat Distiller 5.0.5 (Windows) |
| CreationDate / ModDate | D:20040428100656+01'00' |
| Páginas | 10 |
| Palabras (texto extraíble) | 3847 |
| Caracteres | ~30567 |
| Idioma (heurística) | en |
| Peso PDF | 1091274 bytes (1.04 MB) |
| Cobertura de texto | 10/10 páginas (100%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-matching_nature_with_complex_geometry-transcripcion\|2026-10-20-matching_nature_with_complex_geometry-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

| # | Página del PDF | Pie detectado |
|---|---|---|
| 1 | p. 2 | Figure 1: The five platonic polyhedra, their symbolism air, fire, universe, |
| 2 | p. 3 | Figure 2: Uccello’s stellated polyhedron; portrait of Pacioli with glass, water |
| 3 | p. 5 | Figure 3: The abstract nature of Complex Geometry. |
| 4 | p. 8 | Figure 4: Viollet-le-Duc’s general explanation of a ruled surface; Model of |
| 5 | p. 9 | Figure 1: Kepler, J.: Weltharmonik, München 1990. Figure 2: Borsi, F.: Paolo |

> Total: 5 pies. Para ver la imagen: abrir el PDF y la página indicada. Las imágenes **no se extraen** (decisión B): la wiki referencia el PDF.

## Candidatos a verificación exterior (sherlock)

- ISBN detectados (verificar): `ISBN-1-85312-721-3`

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Matching nature with ‘Complex Geometry’.pdf`; copia de trabajo en `activos/fuentes/matching_nature_with_complex_geometry/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
