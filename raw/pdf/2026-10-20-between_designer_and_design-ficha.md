---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/between_designer_and_design/Between Designer and Design.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Between Designer and Design.pdf
titulo: Between Designer and Design: Parametric Design and Prototyping Considerations on Gaudí’s Sagrada Familia
autor: Rodrigo Makert
idioma: en
paginas: 5
palabras: 3154
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — Between Designer and Design: Parametric Design and Prototyping Considerations on Gaudí’s Sagrada Familia

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/between_designer_and_design/Between Designer and Design.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Between Designer and Design.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-between_designer_and_design-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | Between Designer and Design: Parametric Design and Prototyping Considerations on Gaudí’s Sagrada Familia |
| Autor | Rodrigo Makert |
| Creator / Producer | Adobe InDesign CS6 (Windows) / Adobe PDF Library 10.0.1 |
| CreationDate / ModDate | D:20170124160729+01'00' |
| Páginas | 5 |
| Palabras (texto extraíble) | 3154 |
| Caracteres | ~30531 |
| Idioma (heurística) | en |
| Peso PDF | 1012819 bytes (0.97 MB) |
| Cobertura de texto | 5/5 páginas (100%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-between_designer_and_design-transcripcion\|2026-10-20-between_designer_and_design-transcripcion]] |

## Índice extraído (marcadores del PDF)

- **1 Introduction** — p. 1
- **2 Parametric Modelling** — p. 2
- **3 Gaudí, prototyping e digital fabrication** — p. 3
- **4 Catenary: a brief experiment with physical and digital models** — p. 3
- **5 Conclusion** — p. 5
- **References** — p. 5

## Figuras detectadas (referencia al PDF, sin extraer)

| # | Página del PDF | Pie detectado |
|---|---|---|
| 1 | p. 2 | Fig. 1 Gaudí’s hanging model and inverted photographs |
| 2 | p. 4 | Fig. 4 A reproduction of the model designed by Gaudi in Colònia Güell’ |
| 3 | p. 5 | Fig. 6 The same 10x10 mesh created in a digital environment and the code Davis, D. (2013). M |

> Total: 3 pies. Para ver la imagen: abrir el PDF y la página indicada. Las imágenes **no se extraen** (decisión B): la wiki referencia el PDF.

## Candidatos a verificación exterior (sherlock)

- DOI detectados (verificar 200 antes de citar): `10.1002/ad.100`, `10.1002/ad.699`, `10.1002/ad.806`, `10.1007/978-3-7091-0332-6`, `10.11606/T.102.2014.tde-07012015-105828`, `10.3311/PPar.10335`
- ISBN detectados (verificar): `978-3-7091-0332-6`

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Between Designer and Design.pdf`; copia de trabajo en `activos/fuentes/between_designer_and_design/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
