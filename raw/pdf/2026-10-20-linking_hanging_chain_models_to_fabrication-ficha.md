---
tipo: raw
fecha: 2026-10-20
fuente_binaria: activos/fuentes/linking_hanging_chain_models_to_fabrication/Linking Hanging Chain Models to Fabrication.pdf
fuente_original: G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Linking Hanging Chain Models to Fabrication.pdf
titulo: Linking Hanging Chain Models to Fabrication
titulo_provisional: si
autor: akilian
idioma: en
paginas: 17
palabras: 5775
metodo_extraccion: ghostscript-txtwrite
tags: [pdf, raw, gaudi, bibliografia-ai, ficha-extraccion, fair-use]
licencia_texto_completo: no (copyright, solo extractos breves)
estado: texto-extraible
---

# RAW ficha — Linking Hanging Chain Models to Fabrication

> Ficha de extracción (metadata + índice + stats + figuras) del PDF de Drive. Binario local: [activos/fuentes/linking_hanging_chain_models_to_fabrication/Linking Hanging Chain Models to Fabrication.pdf]. Origen (solo lectura): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Linking Hanging Chain Models to Fabrication.pdf`.
> El PDF de origen **no se modifica**. Texto completo: [[raw/pdf/2026-10-20-linking_hanging_chain_models_to_fabrication-transcripcion|transcripción completa]] (raw, uso interno). En la wiki solo entran extractos breves con atribución (fair use).

## Metadata extraída

| Campo | Valor |
|---|---|
| Título | Microsoft Word - PDF-finalversion.doc |
| Autor | akilian |
| Creator / Producer | PScript5.dll Version 5.2 / Acrobat Distiller 5.0 (Windows) |
| CreationDate / ModDate | D:20040817155517-04'00' |
| Páginas | 17 |
| Palabras (texto extraíble) | 5775 |
| Caracteres | ~47665 |
| Idioma (heurística) | en |
| Peso PDF | 1105215 bytes (1.05 MB) |
| Cobertura de texto | 17/17 páginas (100%) |
| Método de extracción | ghostscript-txtwrite |
| Estado | Texto extraíble (sin OCR) |
| Transcripción | [[raw/pdf/2026-10-20-linking_hanging_chain_models_to_fabrication-transcripcion\|2026-10-20-linking_hanging_chain_models_to_fabrication-transcripcion]] |

## Índice extraído (marcadores del PDF)

- Sin marcadores/outline en el PDF (documento lineal o escaneado).

## Figuras detectadas (referencia al PDF, sin extraer)

| # | Página del PDF | Pie detectado |
|---|---|---|
| 1 | p. 1 | Figure 1. Overview of the tool, showing mesh and string models as well as flattened |
| 2 | p. 4 | Figure 2. Catenary equation and family of catenary curve plots (Weisstein 1999) |
| 3 | p. 5 | Figure 3. Calculation of a catenary curve between uneven supports (Cella 1999) |
| 4 | p. 7 | Figure 4. Hanging chains with varying subdivisions of particles (left). The hanging |
| 5 | p. 7 | Figure 5. Different linear translation strategies programmatically linked to the form |
| 6 | p. 8 | Figure 6. Joint studies from a previous project for intersections of members of |
| 7 | p. 9 | Figure 7. Simple instability test through varying gravity and tracing the position of |
| 8 | p. 10 | Figure 8. Physical hanging model test. (left) Paper tubes constructed on the basis of |
| 9 | p. 10 | Figure 9. Roof example design using a wireframe based form finding approach with |
| 10 | p. 11 | Figure 10. Two stage design: (a) constructing the mesh in a frozen state, (b) starting |
| 11 | p. 12 | Figure 11. Load paths emerge through form finding (load proportional to the area |
| 12 | p. 13 | Figure 12. Variations on possible meshes for a dome with a square footprint |
| 13 | p. 13 | Figure 13. Details of different mesh patterns for a square footprint |
| 14 | p. 15 | Figure 14. C++ implementation of an implicit solver, the outcome of the workshop, |

> Total: 14 pies. Para ver la imagen: abrir el PDF y la página indicada. Las imágenes **no se extraen** (decisión B): la wiki referencia el PDF.

## Candidatos a verificación exterior (sherlock)

- Sin DOI/ISBN detectables: la referencia completa la resuelve @sherlock (fuera).

## Qué sí / qué no guarda esta ficha

- Sí: metadata, índice, stats, cobertura, figuras con página, candidatos DOI/ISBN, rutas de origen y binario, enlace a la transcripción.
- No: imágenes (no se extraen), ni el binario en git (vive en `activos/`, gitignored).

## Metodología

- Texto con **Ghostscript `txtwrite` página por página** (acentos correctos; abre también el PDF cifrado AES). `pypdf` queda para metadata, outline y control.
- PDF de origen abierto en solo lectura desde `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Linking Hanging Chain Models to Fabrication.pdf`; copia de trabajo en `activos/fuentes/linking_hanging_chain_models_to_fabrication/`.
- OCR (tesseract) solo cuando la cobertura de texto < 40 % (PDF escaneado).
- Flujo siguiente: @sherlock (exterior) → @contenidos (reporte legible) → `wiki/fuentes` con `s` de SOL.
