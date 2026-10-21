---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg/Gaudí’s La Pedrera, sustainable masonry building from the beginning of the 20th century.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudí’s La Pedrera, sustainable masonry building from the beginning of the 20th century.pdf
titulo: Gaudí’s La Pedrera, sustainable masonry building from the beginning of the 20th century
titulo_provisional: si
autor: A.A. Balkema Uitgevers B.V.
idioma: en
paginas: 8
palabras: 3882
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — Gaudí’s La Pedrera, sustainable masonry building from the beginning of the 20th century

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg/Gaudí’s La Pedrera, sustainable masonry building from the beginning of the 20th century.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudí’s La Pedrera, sustainable masonry building from the beginning of the 20th century.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | Title of paper |
| Autor | A.A. Balkema Uitgevers B.V. |
| Creator / Producer | Microsoft® Word 2016 / Microsoft® Word 2016 |
| CreationDate / ModDate | D:20210602132046+02'00' |
| Páginas | 8 |
| Palabras (texto extraíble) | 3882 |
| Caracteres | ~38824 |
| Idioma (heurística) | en |
| Peso PDF | 931767 bytes (0.89 MB) |
| Cobertura de texto | 8/8 páginas (100%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg-transcripcion\|2026-10-20-gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

| # | Página del PDF | Pie detectado |
|---|---|---|
| 1 | p. 2 | Figure 1. Sagrada Familia Schools. |
| 2 | p. 3 | Figure 3. La Pedrera’s brick masonry arcs. |
| 3 | p. 4 | Figure 5. La Pedrera’s main beams and pillars structure. tice to use materials located less than |
| 4 | p. 5 | Figure 7. La Pedrera’s façade great openings. |
| 5 | p. 6 | Figure 10. Great patios for lighting and air circulation in La |
| 6 | p. 6 | Figure 9. Metal structure with spider beams in the shape of bi- |

> Total: 6 pies. Para ver la imagen: abrir el PDF y la página indicada. Las imágenes **no se extraen** (decisión B): la wiki referencia el PDF.

## Candidatos a verificación exterior (sherlock)

- Sin DOI/ISBN detectables: la referencia completa la resuelve @sherlock (fuera).

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudí’s La Pedrera, sustainable masonry building from the beginning of the 20th century.pdf`; copia de trabajo en `activos/fuentes/gaudi_s_la_pedrera_sustainable_masonry_building_from_the_beg/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
