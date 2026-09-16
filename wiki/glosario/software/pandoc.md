---
tipo: software
software: pandoc
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [glosario, software, pandoc, pdf, digest]
idioma: es
---

# pandoc

> Conversor universal de documentos — pipeline digest `.md` → PDF para envío por Telegram.

- [Instalación](#instalación)
- [md → pdf](#md--pdf)
- [pdf-engine](#pdf-engine)
- [Uso en digest vaultworm-arq](#uso-en-digest-vaultworm-arq)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Instalación

Windows (canónico estudio): `winget install --source winged --exact --id JohnMacFarlane.Pandoc` o `choco install pandoc` (+ `choco install miktex` para PDF vía LaTeX). Alternativas: instalador MSI en GitHub releases, Docker `pandoc/latex`, o `conda install -c conda-forge pandoc`.

## md → pdf

```bash
pandoc digest.md -o digest.pdf
pandoc digest.md -o digest.pdf --pdf-engine=xelatex -V geometry:margin=2cm
```

## pdf-engine

Por defecto usa LaTeX (MiKTeX/BasicTeX/TinyTeX). Con `--pdf-engine` se elige otro motor: `xelatex` (Unicode/fuentes), `weasyprint` (HTML/CSS, liviano), `typst` (moderno, rápido). Para digest con emojis/tablas: `xelatex` o `weasyprint`.

## Uso en digest vaultworm-arq

Flujo aprobado: `raw/vaultworm-arq/digest-*.md` → `pandoc digest.md -o digest.pdf` → `curl api.telegram.org/bot$TOKEN/sendDocument`. Ver [[wiki/glosario/software/telegram|telegram]] (envío) y `specs/260909-github-actions-agentes-online.md` (ejecución online).

## Conceptos relacionados

- [[wiki/glosario/software/telegram|telegram]]
- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]

## Referencias

- Manual oficial: https://pandoc.org/MANUAL.html (verificado 2026-09-08 — 200)
- Instalación (Windows winget/choco, pdf-engine): https://pandoc.org/installing.html (verificado 2026-09-09 — 200)
