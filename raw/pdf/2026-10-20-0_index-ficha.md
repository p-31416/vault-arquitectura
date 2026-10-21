---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/0_index/0. INDEX.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\0. INDEX.pdf
titulo: 0. INDEX
titulo_provisional: si
autor: Gaudí
idioma: en
paginas: 7
palabras: 913
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — 0. INDEX

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/0_index/0. INDEX.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\0. INDEX.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-0_index-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | Microsoft Word - MASTERCLASS GAUDI BIOMIMESIS BIBLIOGRAPHY |
| Autor | Gaudí |
| Creator / Producer | Microsoft® Word 2019 / Microsoft® Word 2019 |
| CreationDate / ModDate | D:20260529152440+02'00' |
| Páginas | 7 |
| Palabras (texto extraíble) | 913 |
| Caracteres | ~12877 |
| Idioma (heurística) | en |
| Peso PDF | 126460 bytes (0.12 MB) |
| Cobertura de texto | 7/7 páginas (100%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-0_index-transcripcion\|2026-10-20-0_index-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

- Sin pies de figura detectados en el texto (puede ser un PDF con figuras vectoriales sin rótulo).

## Candidatos a verificación exterior (sherlock)

- ISBN detectados (verificar): `324-339-2006`

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\0. INDEX.pdf`; copia de trabajo en `activos/fuentes/0_index/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
