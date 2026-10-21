---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/gaudi_und_natur/Gaudi_und_Natur.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudi_und_Natur.pdf
titulo: gaudi und natur
autor: 
idioma: en
paginas: 8
palabras: 4739
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — gaudi und natur

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/gaudi_und_natur/Gaudi_und_Natur.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudi_und_Natur.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-gaudi_und_natur-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | gaudi und natur |
| Autor | — (lo resuelve @sherlock por fuera) |
| Creator / Producer | — / GPL Ghostscript 9.26 |
| CreationDate / ModDate | D:20190809002357-07'00' |
| Páginas | 8 |
| Palabras (texto extraíble) | 4739 |
| Caracteres | ~45493 |
| Idioma (heurística) | en |
| Peso PDF | 3115876 bytes (2.97 MB) |
| Cobertura de texto | 8/8 páginas (100%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-gaudi_und_natur-transcripcion\|2026-10-20-gaudi_und_natur-transcripcion]] |

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
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudi_und_Natur.pdf`; copia de trabajo en `activos/fuentes/gaudi_und_natur/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
