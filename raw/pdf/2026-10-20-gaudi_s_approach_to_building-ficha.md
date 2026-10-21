---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/gaudi_s_approach_to_building/Gaudí_s approach to building.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudí_s approach to building.pdf
titulo: gaudi s approach to building
autor: 
idioma: en
paginas: 10
palabras: 4978
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — gaudi s approach to building

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/gaudi_s_approach_to_building/Gaudí_s approach to building.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudí_s approach to building.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-gaudi_s_approach_to_building-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | gaudi s approach to building |
| Autor | — (lo resuelve @sherlock por fuera) |
| Creator / Producer | I.R.I.S. / I.R.I.S. Autoformatting < PDF v0.2.1 > |
| CreationDate / ModDate | D:20070628122558Z |
| Páginas | 10 |
| Palabras (texto extraíble) | 4978 |
| Caracteres | ~107192 |
| Idioma (heurística) | en |
| Peso PDF | 1084911 bytes (1.03 MB) |
| Cobertura de texto | 10/10 páginas (100%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-gaudi_s_approach_to_building-transcripcion\|2026-10-20-gaudi_s_approach_to_building-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

| # | Página del PDF | Pie detectado |
|---|---|---|
| 1 | p. 3 | Figure 1 |
| 2 | p. 4 | Figure 3 |
| 3 | p. 4 | Figure 2 Figure 4 |
| 4 | p. 5 | Figure 5 |
| 5 | p. 5 | Figure 7 |
| 6 | p. 5 | Figure 6 |
| 7 | p. 6 | Figure 8. |
| 8 | p. 6 | Figure 9 |
| 9 | p. 6 | Figure 8 |
| 10 | p. 7 | Figure 10 that was rea |
| 11 | p. 8 | Figure 12 |
| 12 | p. 9 | Figure 14 |
| 13 | p. 9 | Figure 13 works |

> Total: 13 pies. Para ver la imagen: abrir el PDF y la página indicada. Las imágenes **no se extraen** (decisión B): la wiki referencia el PDF.

## Candidatos a verificación exterior (sherlock)

- Sin DOI/ISBN detectables: la referencia completa la resuelve @sherlock (fuera).

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudí_s approach to building.pdf`; copia de trabajo en `activos/fuentes/gaudi_s_approach_to_building/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
