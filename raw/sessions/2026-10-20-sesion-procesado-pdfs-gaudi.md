# 2026-10-20 — Procesado de fuentes PDF de Gaudí (AIxGaudi): diagnóstico + plan para Emilia

tags: [sesion, fuentes, pdf, gaudi, ai-gaudi, sherlock, contenidos, hitl, grafo, spec]

## Gate 0 v2 — ejecutado y validado (3er bloque, 20/10 noche)

> Más nuevo → más arriba: esta sección se agregó después del plan.

- **T1-T3 hechos**: `scripts/pdf_scan_bibliografia.py` v2 (Ghostscript `txtwrite` por página, `pypdf` solo metadata/outline, sin extracción de imágenes, OCR opcional) + `_notas.md` reescrito a v2.
- **Corrida del lote**: **31 PDF → 31 fichas v2 + 31 transcripciones** en `raw/pdf/` (+ la ficha Baudrillard previa = 32 filas en `00-index.md`), **1.062 páginas / ~479.000 palabras**, **116 MB** en `activos/fuentes/` (gitignored). Drive intacto.
- **Casos difíciles cerrados**: tesis UPM cifrada AES (396 p, 79.374 palabras, 97 %); OCR de *Morphogenesis* (Korra, UNM 2017) y *Tomlow* (*Engineering History and Heritage* 164/EH4). Títulos reales recuperados de la metadata donde existían.
- **Incidente "se tildó"**: se percibió colgado porque no imprimía progreso y Ghostscript tarda ~2 s/página. Diagnóstico: **no había proceso huérfano** (los 13 `python` vivos eran MCP servers: notebooklm, autocad, uv); el lote había terminado. Lección registrada en el plan: imprimir progreso por página.
- **Reparación de lo extraído** (`--fix-titulos`, idempotente, sin re-extraer): 8 títulos artefacto (`Microsoft Word - ...`, `Title of paper`, `LearningXDesign_post-review_CE_AS`) sustituidos por el nombre real + `titulo_provisional: si`; **62 wikilinks** pasados a ruta absoluta (`[[raw/pdf/...]]`). Bug encontrado y corregido: en tablas el pipe va escapado (`\|`) y la comparación usaba el texto ya mutado.
- **Duplicado archivado**: el piloto v1 *Gaudi and CAD* (2026-10-19) se movió a `raw/pdf/_v1/` para que @contenidos no procese dos veces el mismo paper.

## Qué se hizo

- **Medición real del corpus** (no supuesto): `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography` tiene **31 PDF = 30 fuentes + `0. INDEX.pdf`**; 1.062 páginas, ~397.000 palabras, ~1.700 imágenes embebidas. Corrección de un error previo: se habían contado 28.
- **Dos casos técnicos resueltos con pruebas, no con teoría:**
  - `Antonio Gaudi Precursor de la Sostenibilidad...pdf` (tesis UPM 2018, Salas Mirat) está **cifrado con AES**: `pypdf` revienta (`cryptography>=3.1` ausente). **Ghostscript 10.08 lo abre y extrae bien** ("UNIVERSIDAD POLITÉCNICA DE MADRID… TESIS DOCTORAL… AÑO 2018").
  - `pypdf` **degrada los acentos** con fonts Type1 sin `fontTools` (`GAUD�`); **Ghostscript `txtwrite` los resuelve** (`GAUDÍ`). Rinde ~0,16 s/página → 1.062 págs en ~3 min.
  - `Morphogenesis.pdf` (29 p) y `Tomlow_J_...pdf` (15 p) son **escaneos puros** (0 palabras) → requieren OCR (tesseract disponible, solo `eng`+`spa`; falta `cat` para el catalán de *El Park Güell*).
- **Piloto ejecutado**: `Gaudi_and_CAD.pdf` → `raw/pdf/2026-10-19-gaudi_and_cad-ficha.md` + copia en `activos/fuentes/gaudi_and_cad/` (4 imágenes extraídas en el piloto, que la decisión B posterior deja sin efecto) + fila en `raw/pdf/00-index.md`. Es el paper **"GAUDÍ AND CAD"** de Jane R. Burry y Mark C. Burry (*ITcon* Vol. 11, 2006, pp. 437-446, itcon.org/2006/32/): superficies regladas de Gaudí llevadas a modelado paramétrico para la Sagrada Família.
- **Decisiones de SOL tomadas y registradas:** A) transcripción completa **versionada** en `raw/pdf/<slug>-transcripcion.md`; B) **cero extracción de imágenes** (la ficha lista figuras con página y remite al PDF); C) binarios copiados a `activos/fuentes/<slug>/`, Drive intacto; D) extractor Ghostscript por página con `pypdf` para metadata/outline.
- **Plan armado** en `specs/261020-plan-procesado-fuentes-pdf-gaudi.md` para revisión el **miércoles 21/10 con Emilia**: SPEC, estado del corpus, pipeline de 4 gates HITL con las incumbencias delimitadas, 15 tasks con pomodoros, 3 piezas de grafo, 7 riesgos y 5 preguntas para Emilia.

## Archivos modificados

- `specs/261020-plan-procesado-fuentes-pdf-gaudi.md` (nuevo) — plan de revisión.
- `diagramas/pipeline-pdfs-gaudi.mmd` (nuevo) — grafo del pipeline (mermaid, se ve en Obsidian).
- `scripts/pdf_scan_bibliografia.py` (nuevo) + `scripts/pdf_scan_bibliografia_notas.md` (nuevo) — extractor Gate 0 v1 (a reescribir con Ghostscript).
- `raw/pdf/00-index.md` (fila nueva del piloto) + `raw/pdf/2026-10-19-gaudi_and_cad-ficha.md` (nuevo).
- `activos/fuentes/gaudi_and_cad/` (nuevo, gitignored): PDF + `img/p003-r25.jpg`, `p003-r26.jpg`, `p003-r27.jpg`, `p004-r35.jpg`.

> **Sesión pausada por SOL: "seguimos mañana" (21/10).** El plan queda para revisión con Emilia el miércoles 22/10; el Gate 0 v2 arranca cuando SOL lo pida.

## Cierre de la jornada (2º bloque) — curso Archademy / AI×Gaudí

- El usuario preguntó por el video de `https://archemony.ai/my-account/my-competitions/214/?tab=course` (pedido #214). **La página exige login**: sin sesión no hay lectura. La biblioteca media pública solo expone **14 videos de promo** (el dron de la Sagrada Família, el video del concurso); los **7 módulos del curso (5h45)** no están ahí — se sirven detrás de la sesión.
- El sitio es **WordPress + WooCommerce** (`wp-json` abierto, sitemap solo con páginas públicas). La home no expone embeds Vimeo/YouTube.
- **Método de descarga acordado**: el usuario copia la URL del media desde `F12 → Network → Media` (o "Copy as cURL") y yo la bajo con `yt-dlp` + `ffmpeg` (ya instalados) a `activos/videos/archademy/<fecha>-<modulo>.mkv`; alternativa con `--cookies-from-browser chrome` (requiere autorización explícita: toca cookies de sesión).
- **Encaje con el pipeline**: los módulos entran por la misma vía que los PDFs → transcript (whisper) → `@contenidos` → `wiki/fuentes/`. Modules 6 (mesa redonda: Jos Tomlow, Gijs Rikken/MVRDV, Arturo Tedeschi, Cas Esbach) y 7 (The Gaudí Workflow con Cas Esbach) son insumo directo del concurso Gaudí Nexus.
- **Pendiente**: bajar Module 5 (20 min, el más corto) como prueba del método antes que el resto.

## Pendiente siguiente ciclo

- ~~**Gate 0 v2**~~ **hecho** (ver bloque de arriba). Queda la revisión de SOL del índice y de 2-3 fichas antes de mover agentes.
- **Gate 1**: @sherlock por lotes L1-L6, un lote por sesión, con `s` entre lotes.
- **Gate 2**: @contenidos ×6 reportes; **Gate 3**: `wiki/fuentes/` con `s` de SOL.
- **T12-T13**: grafo VR (`scripts/grafo-pdfs-gaudi.html`) + `.excalidraw.md`/`.png` + publicar el grafo en la wiki como ejemplo.
- Instalar `cat` (tesseract) si se quiere el catalán de *El Park Güell* sin degradar.

## Cerebro-digital

- **Topics**: pipeline-pdf-gaudi · raw-pdf-espejo-yt · hitl-4-gates · sherlock-lotes-tematicos · contenidos-template-11-secciones · ghostscript-vs-pypdf · ocr-escaneados · fair-use-transcripcion-versionada · grafo-vr-fuentes · corpus-ai-gaudi · concurso-gaudi-nexus-corpus.
- **Entidades**: `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography` (31 PDF) · `raw/pdf/` (fichas + transcripciones) · `activos/fuentes/<slug>/` · `scripts/pdf_scan_bibliografia.py` · `diagramas/pipeline-pdfs-gaudi.mmd` · `specs/261020-plan-procesado-fuentes-pdf-gaudi.md` · thesis UPM Salas Mirat 2018 · Burry & Burry 2006 *ITcon* 11:437-446.
- **Hechos**: el Drive nunca se altera (siempre solo lectura) · 30 fuentes agrupadas en 6 lotes temáticos (8/7/6/3/5/1) · 3 PDF con problema técnico resuelto con Ghostscript · ~36 pomodoros estimados para el ciclo completo · la bibliografía es el corpus natural del modelo del concurso Gaudí Nexus (requisito "lógica constructiva paramétrica de Gaudí").
