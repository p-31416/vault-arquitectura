---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/la_arquitectura_y_la_naturaleza_compleja/La arquitectura y la naturaleza compleja.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\La arquitectura y la naturaleza compleja.pdf
titulo: La arquitectura y la naturaleza compleja
titulo_provisional: si
autor: acd Grillo
idioma: es
paginas: 218
palabras: 77466
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — La arquitectura y la naturaleza compleja

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/la_arquitectura_y_la_naturaleza_compleja/La arquitectura y la naturaleza compleja.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\La arquitectura y la naturaleza compleja.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-la_arquitectura_y_la_naturaleza_compleja-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | Microsoft Word - Tesis con imágenes _NG MT_.doc |
| Autor | acd Grillo |
| Creator / Producer | PScript5.dll Version 5.2 / Acrobat Distiller 6.0 (Windows) |
| CreationDate / ModDate | D:20061121152434-02'00' |
| Páginas | 218 |
| Palabras (texto extraíble) | 77466 |
| Caracteres | ~703087 |
| Idioma (heurística) | es |
| Peso PDF | 3355100 bytes (3.2 MB) |
| Cobertura de texto | 210/218 páginas (96%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-la_arquitectura_y_la_naturaleza_compleja-transcripcion\|2026-10-20-la_arquitectura_y_la_naturaleza_compleja-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

- Sin pies de figura detectados en el texto (puede ser un PDF con figuras vectoriales sin rótulo).

## Candidatos a verificación exterior (sherlock)

- ISBN detectados (verificar): `ISBN-:-2-87009-114-1`, `ISBN:-0-226-79118-1`, `ISBN:-0-262-53130-5`, `ISBN:-0-471-49193-4`, `ISBN:-0-471-49541-7`, `ISBN:-0-471-97686-5`, `ISBN:-0-471-97687-3`, `ISBN:-0-471-97739-X`

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\La arquitectura y la naturaleza compleja.pdf`; copia de trabajo en `activos/fuentes/la_arquitectura_y_la_naturaleza_compleja/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
