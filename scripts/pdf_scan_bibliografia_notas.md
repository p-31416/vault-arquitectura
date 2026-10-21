# pdf_scan_bibliografia — notas v2 (leer antes de ejecutar)

## Qué hace

Escanea **PDFs de bibliografía** (carpeta `G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography`) y deja
**una ficha + una transcripción por PDF** en `raw/pdf/`, con:

- metadata (título, autor, creator/producer, fechas, peso)
- stats (páginas, palabras, caracteres, cobertura de texto, idioma por heurística)
- índice/marcadores (outline) del PDF con página
- conteo y listado de figuras (solo como referencia: **el binario no se copia ni se recorta**)
- transcripción **completa, página por página**, versionada en `raw/pdf/<slug>-transcripcion.md`

Y actualiza la tabla de `raw/pdf/00-index.md` (10 columnas) con una fila por PDF.

## Garantías

- **El PDF de origen NO se modifica**: se abre en solo lectura con Ghostscript.
- **El binario nunca entra a git**: la copia vive en `activos/fuentes/<slug>/` (`.gitignore` → `/activos/`).
- **Imágenes: cero extracción**. La ficha lista cada figura con su página y remite al PDF
  (`activos/fuentes/<slug>/<archivo>.pdf`, pág. N). Si un día se necesitan, se regeneran con un
  pase aparte a 150 dpi, sin tocar este pipeline.
- **OCR automático solo si hace falta** (`--ocr`): páginas sin capa de texto → tesseract.

## Por qué Ghostscript y no pypdf

| | pypdf | Ghostscript `txtwrite` |
|---|---|---|
| Acentos en fuentes Type1 | degrada (`GAUD�`) sin `fontTools` | correcto (`GAUDÍ`) |
| PDF cifrado AES (tesis UPM) | `DependencyError: cryptography` | abre y transcribe |
| Texto por página | sí | sí (una invocación por página) |

Por eso: **Ghostscript pagina a pagina** para el texto, y `pypdf` **solo** para metadata
(fechas, autor, producer) y outline. Costo: ~2 s/página → los 31 PDF tardan ~8-10 min.

## Comandos

```powershell
# Piloto: un PDF
P:\Anaconda\envs\comfyenv\python.exe scripts/pdf_scan_bibliografia.py --src "G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography\Gaudi_and_CAD.pdf"

# Lote: toda la carpeta
P:\Anaconda\envs\comfyenv\python.exe scripts/pdf_scan_bibliografia.py --dir "G:\Mi unidad\OS-Emilia\AIxGaudi\Bibliography" --all

# Lote con OCR (los 2 escaneados: Morphogenesis y Tomlow)
P:\Anaconda\envs\comfyenv\python.exe scripts/pdf_scan_bibliografia.py --dir "..." --all --ocr --ocr-lang eng

# Reparar títulos artefacto y wikilinks de lo ya extraído (no re-extrae texto)
P:\Anaconda\envs\comfyenv\python.exe scripts/pdf_scan_bibliografia.py --fix-titulos

# Sin copiar el binario (solo ficha, para probar en otra máquina)
P:\Anaconda\envs\comfyenv\python.exe scripts/pdf_scan_bibliografia.py --src "..." --no-copy
```

Opciones: `--raiz <vault>` (default: carpeta del repo), `--ocr`, `--ocr-lang eng|spa`,
`--no-copy`, `--fix-titulos`.

## Dependencias

- `pypdf 6.20.1` + `Pillow` en `C:\Users\Solch16\AppData\Local\Temp\opencode\pdflibs`
  (el script lo agrega al `sys.path`; **no se instala nada en `comfyenv`**).
- Ghostscript: `C:\Users\Solch16\scoop\shims\gswin64c.exe` (10.08).
- OCR: `tesseract` en PATH. Idiomas instalados: `eng`, `spa`. **Falta `cat`** → el catalán de
  *El Park Güell* queda aproximado (anotado en su ficha).

## Dónde queda cada cosa

| Ruta | Qué es |
|---|---|
| `raw/pdf/YYYY-MM-DD-<slug>-ficha.md` | ficha de extracción (entra a git) |
| `raw/pdf/YYYY-MM-DD-<slug>-transcripcion.md` | texto completo con `## [p. N]` (entra a git) |
| `raw/pdf/00-index.md` | índice con tabla de 10 columnas |
| `raw/pdf/_v1/` | fichas piloto superadas (no se rehidratan) |
| `activos/fuentes/<slug>/<archivo>.pdf` | copia de trabajo (gitignored) |
| `G:\...\Bibliography\*.pdf` | origen, solo lectura |

## Dónde sigue el flujo (HITL)

```
G:\...\Bibliography\*.pdf   (solo lectura)
        │
        ▼  [Gate 0] scripts/pdf_scan_bibliografia.py  → raw/pdf/*-ficha.md + *-transcripcion.md   ← ¿Avanzo? s
        │
        ▼  [Gate 1] @sherlock (exterior: edición oficial, DOI, papers derivados) → raw/research/  ← ¿Avanzo a curaduría? s
        │
        ▼  [Gate 2] @contenidos (template + desarrollo) → raw/contenidos/      ← ¿Avanzo a wiki? s
        │
        ▼  [Gate 3] @contenidos con `s` → wiki/fuentes/<slug>.md (+ borra raw)
        │
        ▼  [Gate 4] @vaultworm-arq → glosario / estudio
```

## Notas de implementación (para leer el código)

1. `slugify()` quita acentos y deja `[a-z0-9_]` → nombres de archivo portables.
2. `titulo_de_documento()` usa el `/Title` del PDF **salvo** que sea artefacto de edición:
   `Microsoft Word - ...`, `Title of paper`, `Chapter_00.indd`, `.doc/.indd`, o un nombre sin
   espacios con `_` (`LearningXDesign_post-review_CE_AS`). En ese caso toma el nombre real del
   archivo y marca `titulo_provisional: si` (el título definitivo lo trae @sherlock en Gate 1).
3. `gs_texto_pagina()` = una invocación de `gswin64c -sDEVICE=txtwrite -dFirstPage=N -dLastPage=N`
   por página. Así se aísla una página problemática sin tirar el PDF completo.
4. `gs_ocr_pagina()` renderiza a PNG 200 dpi y le pasa el PNG a `tesseract ... stdout`.
5. `escanear_pdf()` calcula cobertura = páginas con texto / total; < 40 % ⇒ escaneo.
6. `leer_outline()` aplana la jerarquía con `get_destination_page_number()`.
7. `escribir_transcripcion()` antepone frontmatter propio y un marcador `## [p. N]` por página.
8. `actualizar_indice()` rehidrata la tabla **desde las fichas** (idempotente): borra las filas
   entre los separadores y las reconstruye ordenadas por título.
9. `fix_titulos()` repara en lote títulos artefacto y wikilinks relativos → absolutos
   (`[[raw/pdf/...]]`). **Ojo**: en tablas Markdown el pipe va escapado (`\|`), por eso usa
   reemplazo literal y no regex.
10. La copia del binario no sobreescribe: si ya existe, lo dice y conserva.

## Estado de la corrida (2026-10-20)

| Métrica | Valor |
|---|---|
| PDF procesados | 31 (30 fuentes + `0. INDEX`) |
| Fichas en `raw/pdf/` | 32 (31 + Baudrillard, piloto previo) |
| Transcripciones | 31 |
| Páginas | 1.062 |
| Palabras | ~479.000 |
| Binarios copiados | 31 carpetas, ~116 MB (gitignored) |
| OCR | 2 PDF (`Morphogenesis` 29 p, `Tomlow` 15 p) |
| Tesis cifrada AES | 396 p, 79.374 palabras, 97 % (Ghostscript) |
| Títulos provisionales | 7 (los resuelve @sherlock) |

## Referencias internas

- `raw/pdf/00-index.md` — índice de fichas
- `specs/261020-plan-procesado-fuentes-pdf-gaudi.md` — plan y gates
- `diagramas/pipeline-pdfs-gaudi.mmd` — grafo del pipeline
- [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]] — incumbencias de los agentes
