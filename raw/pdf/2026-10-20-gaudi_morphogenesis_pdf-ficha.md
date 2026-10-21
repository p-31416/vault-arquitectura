---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/gaudi_morphogenesis_pdf/Gaudi_Morphogenesis_pdf.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudi_Morphogenesis_pdf.pdf
titulo: gaudi morphogenesis pdf
autor: 
autor_origen: pendiente
idioma: en
paginas: 49
palabras: 16078
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — gaudi morphogenesis pdf

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/gaudi_morphogenesis_pdf/Gaudi_Morphogenesis_pdf.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudi_Morphogenesis_pdf.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-gaudi_morphogenesis_pdf-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | gaudi morphogenesis pdf |
| Autor | — (sin metadata y sin patrón en la portada; lo resuelve @sherlock) |
| Creator / Producer | — / GPL Ghostscript 9.10 |
| CreationDate / ModDate | D:20170305065625-08'00' |
| Páginas | 49 |
| Palabras (texto extraíble) | 16078 |
| Caracteres | ~195701 |
| Idioma (heurística) | en |
| Peso PDF | 1440102 bytes (1.37 MB) |
| Cobertura de texto | 47/49 páginas (96%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-gaudi_morphogenesis_pdf-transcripcion\|2026-10-20-gaudi_morphogenesis_pdf-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

> Cuenta **pies de figura** (`FIG. 3`, `Figure 12`, `Figura 4`, `Plate 2`, `Lám. 5`) encontrados en el texto. No son imágenes: sirven para saber en qué página ir a mirar. 0 = el PDF no trae rótulos o es un escaneo.

- Sin pies de figura detectados en el texto (puede ser un PDF con figuras vectoriales sin rótulo).

## Candidatos a verificación exterior (sherlock)

- ISBN detectados (verificar): `ISBN-84-9803-001-3`, `ISBN-978-84-7782-726-9`

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudi_Morphogenesis_pdf.pdf`; copia de trabajo en `activos/fuentes/gaudi_morphogenesis_pdf/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
