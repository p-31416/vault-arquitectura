---
tipo: guia
proyecto: concurso-gaudi-nexus
modulo: 6
slug: round-table
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, wf-curso, wf-06, curso-ai-gaudi, jurado, detalle]
idioma: es
estado: pendiente-transcripcion
---

# WF-06 — Round Table jurado + detalle constructivo 1024²

> Unifica [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-06-round-table\|flujo-06]] (transcripción pendiente) + [[proyectos/concurso-gaudi-nexus/WF-curso/WF-06_sdxl\|WF-06_sdxl]] (interpreta el criterio en imagen).

## 1. Ver en Miro + video

| Fuente | Link |
|--------|------|
| Miro frame round table | pendiente link Sol |
| Video módulo 6 (mesa Cas Esbach, sin subtítulos, ~538 MB mp4) | pendiente link Sol |
| Audio + transcripción faster-whisper | `activos/curso-ai-gaudi/videos/mux-round-table.mp4` → `raw/yt/transcripts/*mux-round-table*` (procedimiento en [[proyectos/concurso-gaudi-nexus/WF-curso/flujo-06-round-table\|flujo-06]]) |

## 2. Flujo del curso (resumen)

Mesa con **Cas Esbach** (SCAD, ex-BIG/MVRF, jurado): lógica constructiva sobre apariencia. Tesis: transferencia conceptual (lógica) por encima de transferencia estilística; reducir Gaudí a un LoRA deja algo afuera. Insumo del **checklist de cierre de los 7 WF** en [[proyectos/concurso-gaudi-nexus/criterio/criterio-jurado\|criterio-jurado]].

## 3. WF SDXL vista

JSON: `workflow_WF-06_sdxl.json` (misma carpeta WF-curso/, original en `workflows/sdxl-vista/`) · txt2img 1024² · seed 6 · prefijo `gx-WF06`. El módulo 6 no genera imagen; este flujo la interpreta.

+ `close-up constructive detail, branching fractal column joint, stone and steel connection, tectonic logic over appearance, raking light, architectural photography, 8k uhd, masterpiece` · − casa + `decorative only`. Alternativa RealVisXL (más nítido) y ControlNet Union SDXL para clavar la junta.

## 4. Cómo lo adaptamos

Transcribir módulo 6 en local (faster-whisper) → checklist 5-7 puntos → copiar a `04-backlog` de cada WF como aceptación. Detalle: una junta por corrida.

## 5. Checks jurado

Pregunta que responde la imagen: *¿cómo se construye?* — junta continua, espesor creíble, pieza metálica diseñada, sombra rasante que describe la forma. Falla: junta derretida / material sin borde.
