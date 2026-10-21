---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/la_arquitectura_escultorica_de_antonio_gaudi/LA ARQUITECTURA ESCULTORICA DE ANTONIO GAUDI.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\LA ARQUITECTURA ESCULTORICA DE ANTONIO GAUDI.pdf
titulo: La arquitectura escultórica de Antonio Gaudí
autor: Bassegoda Nonell_ Juan
idioma: es
paginas: 6
palabras: 2777
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — La arquitectura escultórica de Antonio Gaudí

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/la_arquitectura_escultorica_de_antonio_gaudi/LA ARQUITECTURA ESCULTORICA DE ANTONIO GAUDI.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\LA ARQUITECTURA ESCULTORICA DE ANTONIO GAUDI.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-la_arquitectura_escultorica_de_antonio_gaudi-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título |  La arquitectura escultórica de Antonio Gaudí |
| Autor | Bassegoda Nonell_ Juan |
| Creator / Producer | Oce-Technologies / Adobe Acrobat 8.1 Paper Capture Plug-in |
| CreationDate / ModDate | D:20080609135249+02'00' |
| Páginas | 6 |
| Palabras (texto extraíble) | 2777 |
| Caracteres | ~28241 |
| Idioma (heurística) | es |
| Peso PDF | 2334325 bytes (2.23 MB) |
| Cobertura de texto | 6/6 páginas (100%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-la_arquitectura_escultorica_de_antonio_gaudi-transcripcion\|2026-10-20-la_arquitectura_escultorica_de_antonio_gaudi-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

| # | Página del PDF | Pie detectado |
|---|---|---|
| 1 | p. 2 | Fig. 2.- Plantade La,Sagrada |
| 2 | p. 3 | Fig. 3.- Pabellón escuelas de La |
| 3 | p. 4 | Fig. 4.- Casa Milá - Azotea |
| 4 | p. 5 | Fig. 5.- Cripta de la Capilla de la |
| 5 | p. 6 | Fig. 6.- A. Gaudf, casa Batlló |

> Total: 5 pies. Para ver la imagen: abrir el PDF y la página indicada. Las imágenes **no se extraen** (decisión B): la wiki referencia el PDF.

## Candidatos a verificación exterior (sherlock)

- Sin DOI/ISBN detectables: la referencia completa la resuelve @sherlock (fuera).

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\LA ARQUITECTURA ESCULTORICA DE ANTONIO GAUDI.pdf`; copia de trabajo en `activos/fuentes/la_arquitectura_escultorica_de_antonio_gaudi/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
