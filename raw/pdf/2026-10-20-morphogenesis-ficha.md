---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/morphogenesis/Morphogenesis.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Morphogenesis.pdf
titulo: morphogenesis
autor: 
autor_origen: pendiente
idioma: en
paginas: 29
palabras: 6079
metodo_extraccion: ocr-tesseract
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: requiere-ocr
---

# RAW ficha — morphogenesis

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/morphogenesis/Morphogenesis.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Morphogenesis.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-morphogenesis-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | morphogenesis |
| Autor | — (sin metadata y sin patrón en la portada; lo resuelve @sherlock) |
| Creator / Producer | pdf-lib (https://github.com/Hopding/pdf-lib) / pdf-lib (https://github.com/Hopding/pdf-lib) |
| CreationDate / ModDate | D:20260603093948Z |
| Páginas | 29 |
| Palabras (texto extraíble) | 6079 |
| Caracteres | ~44542 |
| Idioma (heurística) | en |
| Peso PDF | 6491737 bytes (6.19 MB) |
| Cobertura de texto | 0/29 páginas (0%) |
| Método de extracción | ocr-tesseract |
| Estado | ESCANEADO — transcrito por OCR |
| Transcripción | [[raw/pdf/2026-10-20-morphogenesis-transcripcion\|2026-10-20-morphogenesis-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Índice de secciones (detectado en el texto)

| Página | Sección detectada |
|---|---|
| p. 6 | 1.0  ABSTRACT... as a ‘ - sts savareueeaas sessetveessersateree O4- |
| p. 6 | 3.0  MORPHOGENESIS |
| p. 6 | 3.1  Antoni Gaudi. |
| p. 6 | 3.2  Frei Otto wee |
| p. 6 | 4.0  STEP BY STEP MORPHOGENETIC DESIGN |
| p. 6 | 4.1  Evolution of surface |
| p. 6 | 4.2  Morphogenesis and material ecology |
| p. 6 | 4.3  Morphogenetic patterns as facade |
| p. 6 | 5.2  Differentiation & Integration ... |
| p. 6 | 5.3  Advanced Siniulation ..........06 |
| p. 6 | 6  TOWARDS A MORPHO-ECOLOGICAL APPROACH FOR DESIGN . |
| p. 6 | 6.1  Performance ....... |
| p. 6 | 6.2  Form generation . |
| p. 6 | 7.1  Hygroskin - Meteorosensitive pavilion |
| p. 6 | 7.2  Summary .. |
| p. 6 | 7.3  Project concept: meteorosensitive architecture .. 19 |
| p. 6 | 7.4  Bionumetic principle: materially-ngrained responsiveness .... wane |
| p. 8 | 2  INTRODUCTION: |
| p. 8 | 3  MORPHOGENESIS: |
| p. 9 | 3.1  ANTONI GAUDI |
| p. 9 | 3.2  FREI OTTO |
| p. 11 | 4.1  EVOLUTION OF SURFACE |
| p. 12 | 4.2  MORPHOGENESIS AND MATERIAL ECOLOGY |
| p. 13 | 4.3  MORPHOGENETIC PATTERNS AS FACADE |
| p. 17 | 14  5. COMPUTATIONAL DESIGN |
| p. 17 | 5.1  COMPUTATIONAL MORPHOGENESIS |
| p. 18 | 5.2  DIFFERENTIATION & INTEGRATION |
| p. 18 | 5.3  ADVANCED SIMULATION |
| p. 19 | 6  TOWARDS A MORPHO-ECOLOGICAL APPROACH FOR DESIGN |
| p. 20 | 6.1  PERFORMANCE: |
| p. 20 | 6.2  FORM-GENERATION: |
| p. 21 | 18  7, CASE STUDY OF ICD PAVILION, UNIVERSITY OF STUTTGART |
| p. 21 | 7.1  HYGROSKIN - METEOROSENSITIVE PAVILION |
| p. 21 | 7.2  SUMMARY |
| p. 22 | 7.3  PROJECT CONCEPT: METEOROSENSITIVE ARCHITECTURE |
| p. 23 | 7.4  BIOMIMETIC PRINCIPLE: MATERIALLY-INGRAINED RESPONSIVENESS |
| p. 25 | 22  8, SUMMARY |
| p. 26 | 23  9. ANNOTATED BIBLIOGRAPHY: |
| p. 28 | 25  ARCH 624 | ARCHITECTURAL THEORY CHAITANYA KORRA |

> El PDF no trae marcadores: estas secciones se detectaron por numeración y mayúsculas en el texto. Puede faltar alguna.

## Figuras detectadas (referencia al PDF, sin extraer)

> Cuenta **pies de figura** (`FIG. 3`, `Figure 12`, `Figura 4`, `Plate 2`, `Lám. 5`) encontrados en el texto. No son imágenes: sirven para saber en qué página ir a mirar. 0 = el PDF no trae rótulos o es un escaneo.

- Sin pies de figura detectados en el texto (puede ser un PDF con figuras vectoriales sin rótulo).

## Candidatos a verificación exterior (sherlock)

- Sin DOI/ISBN detectables: la referencia completa la resuelve @sherlock (fuera).

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Morphogenesis.pdf`; copia de trabajo en `activos/fuentes/morphogenesis/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
