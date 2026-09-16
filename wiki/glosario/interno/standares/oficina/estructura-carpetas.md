---
tipo: oficina
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-10
tags: [estandares, estructura-carpetas]
---

# Estructura de carpetas

> Fuente canónica de la estructura del vault (movida de `AGENTS.md` 2026-09-10, regenerada desde disco). Ver [[proyectos/template_arq/00-index|template_arq]] para el ideal de proyecto.

```
vault-arquitectura/
├── AGENTS.md, 00-index.md, log.md  ← boot, catálogo, registro inmutable
├── wiki/                        ← CONOCIMIENTO (ver [[wiki/00-index|wiki/00-index]])
│   ├── glosario/                ← permanente: software (.md único), conceptos, referentes, entidades, interno
│   ├── estandares/              ← redirige a standares propios (canónico)
│   ├── estudio/ clientes/ legal/ finanzas/ practica-profesional/ lecciones-aprendidas/
│   └── raw/                     ← transcripts verbatim por pipeline
├── proyectos/                   ← Un proyecto = una carpeta (ideal: [[proyectos/template_arq/00-index|template_arq]])
│   ├── 00-index.md, prefijos-documentacion.md, nomenclatura-archivos.md
│   └── <cliente>-<proyecto>-<ciudad>/  (ej. MVP_04-comfyui-arquitectura, STUDIO_OS-Emilia)
├── activos/                     ← BINARIOS, fuera de git (proyectos/, documentos/)
├── raw/sessions/ + raw/vaultworm-arq/ + raw/brainstorm/  ← verbatim + digests
├── specs/                       ← planes con fecha (2609xx-*.md)
├── scripts/                     ← automatización (.ps1/.py, ver [[scripts/00-index|scripts/00-index]])
└── .opencode/agents/ + skills/  ← vaultworm-arq, brainstormy, skills
```

## Reglas

- Un proyecto sigue `template_arq` y adapta (cada MVP documenta su desvío).
- Binarios nunca en git: solo referencias por ruta en los `.md`.
- Nueva carpeta top-level = actualizar este árbol + `00-index.md`.
