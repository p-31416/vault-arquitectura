---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/reading_gaudi_s_great_book_of_nature/READING GAUDÍ’S GREAT BOOK OF NATURE.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\READING GAUDÍ’S GREAT BOOK OF NATURE.pdf
titulo: READING GAUDÍ’S GREAT BOOK OF NATURE
titulo_provisional: si
autor: Mark Pantano
idioma: en
paginas: 33
palabras: 8707
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — READING GAUDÍ’S GREAT BOOK OF NATURE

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/reading_gaudi_s_great_book_of_nature/READING GAUDÍ’S GREAT BOOK OF NATURE.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\READING GAUDÍ’S GREAT BOOK OF NATURE.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-reading_gaudi_s_great_book_of_nature-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | Microsoft Word - Gaudi Project Final Paper Revision II |
| Autor | Mark Pantano |
| Creator / Producer | PScript5.dll Version 5.2.2 / Acrobat Distiller 9.3.0 (Windows) |
| CreationDate / ModDate | D:20130427231201-04'00' |
| Páginas | 33 |
| Palabras (texto extraíble) | 8707 |
| Caracteres | ~94026 |
| Idioma (heurística) | en |
| Peso PDF | 2811021 bytes (2.68 MB) |
| Cobertura de texto | 31/33 páginas (94%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-reading_gaudi_s_great_book_of_nature-transcripcion\|2026-10-20-reading_gaudi_s_great_book_of_nature-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

| # | Página del PDF | Pie detectado |
|---|---|---|
| 1 | p. 6 | Fig. 2. Palau Guell, El Raval suburbs, asked Gaudí to design infrastructure for |
| 2 | p. 7 | Fig. 5. Casa Milá, Eixample around two major interior courtyards where Gaudí introduced an |
| 3 | p. 8 | Fig. 6. Crypt, Santa Coloma de Cervelló catenary structure using a hanging funicular |
| 4 | p. 11 | Fig. 9. Catalan Vault Construction expansive spaces, and causing brick to become a delica |
| 5 | p. 12 | Fig. 10. Modernista Townhouse in the Eixample Catalonia. For the first time, many |
| 6 | p. 14 | Fig. 11. Augustus Pugin. Contrasts |
| 7 | p. 22 | Fig. 12. Collegi de les Teresianes, Sant Gervasi (fig. 12). Confronted with a limited budget |
| 8 | p. 25 | Fig. 14. Gaudí’s Funicular Model |

> Total: 8 pies. Para ver la imagen: abrir el PDF y la página indicada. Las imágenes **no se extraen** (decisión B): la wiki referencia el PDF.

## Candidatos a verificación exterior (sherlock)

- Sin DOI/ISBN detectables: la referencia completa la resuelve @sherlock (fuera).

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\READING GAUDÍ’S GREAT BOOK OF NATURE.pdf`; copia de trabajo en `activos/fuentes/reading_gaudi_s_great_book_of_nature/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
