---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/bio_insipred_design_approach_analysis/Bio Insipred Design Approach Analysis.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Bio Insipred Design Approach Analysis.pdf
titulo: Bio-Inspired Design Approach Analysis: A Case Study of Antoni Gaudi and Santiago Calatrava
autor: Marzieh Imani
idioma: en
paginas: 7
palabras: 3626
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — Bio-Inspired Design Approach Analysis: A Case Study of Antoni Gaudi and Santiago Calatrava

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/bio_insipred_design_approach_analysis/Bio Insipred Design Approach Analysis.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Bio Insipred Design Approach Analysis.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-bio_insipred_design_approach_analysis-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | Bio-Inspired Design Approach Analysis: A Case Study of Antoni Gaudi and Santiago Calatrava |
| Autor | Marzieh Imani |
| Creator / Producer | WASET Zend Publishing System / Acrobat Distiller 11.0 (Windows) |
| CreationDate / ModDate | D:20170816161157+03'00' |
| Páginas | 7 |
| Palabras (texto extraíble) | 3626 |
| Caracteres | ~83577 |
| Idioma (heurística) | en |
| Peso PDF | 226546 bytes (0.22 MB) |
| Cobertura de texto | 7/7 páginas (100%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-bio_insipred_design_approach_analysis-transcripcion\|2026-10-20-bio_insipred_design_approach_analysis-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

- Sin pies de figura detectados en el texto (puede ser un PDF con figuras vectoriales sin rótulo).

## Candidatos a verificación exterior (sherlock)

- Sin DOI/ISBN detectables: la referencia completa la resuelve @sherlock (fuera).

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Bio Insipred Design Approach Analysis.pdf`; copia de trabajo en `activos/fuentes/bio_insipred_design_approach_analysis/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
