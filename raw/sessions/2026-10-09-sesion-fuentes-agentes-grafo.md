---
tipo: log
fecha: 2026-10-09
slug: sesion-fuentes-agentes-grafo
tags: [sesion, youtube, ingesta, agentes, grafo, comfyui]
---

# Sesión 2026-10-09 — Fuentes, agentes y grafo (piloto ComfyUI video 1 completo)

## Qué se hizo

1. **Paso 1 ejemplo completo (video 1 ComfyUI `RAMs89SS6cM`)**: script `transcribir_youtube.py` + notas → transcript vía subtítulos manuales EN (sin Whisper) → `.md` envoltorio para Obsidian → prefijo fecha ISO (opción A) → `@contenidos` fichó (formato spec §13) → OK → movido a `wiki/fuentes/comfyui-for_architects-architutors.md`, borrado de raw, hub en ✅.
2. **Modelo de agentes fijado (flujo v3 adelgazado)**: Sherlock SOLO exterior (transcript por fuente + stub `pendiente-formato`, o reporte links; sin wiki) → Contenidos FORMATEA (único acceso `wiki/fuentes`, OK→mueve+borra) → Vaultworm 1/semana (barre fuentes, alimenta glosario/estudio) → Vistas (Obsidian+web+VR). Grabado en los 3 `.opencode/agents/*.md` + spec ingesta v5 §12.
3. **Specs**: `261009-spec-ingesta-fuentes.md` (v1→v5: ecuación, ficha biblioteca, image-first, trazabilidad, ejemplo, convenciones) + `261009-spec-vista-grafica-yt.md` (notas atómicas + grafo).
4. **Convenciones**: `wiki/fuentes/` = `{tema_ppal}-{tema_secundario}-{canal}` (`_` intra, `-` inter, software = tema); tags sin `:` (fix `workflow-img2img`); hub renombrado a `00-index-yt.md` (primero).
5. **Gráfico para Emilia**: `diagramas/agentes-fuentes.{png,excalidraw.md,mmd}` v4 (FUENTES + 4 bandas), verificado en PNG. Traspiés: conversor mermaid solapa títulos (reconstruido a mano), regex sin `_` en patch (restaurado del editable, 51/51).
6. **Instalado**: yt-dlp 2026.08.19 + faster-whisper 1.2.1 en comfyenv.

## Archivos creados / modificados

Creados: `scripts/transcribir_youtube.py(+_notas.md)`, `raw/yt/transcripts/2026-10-09_RAMs89SS6cM.en.{md,srt,txt,origen.json}`, `specs/261009-*` (2), `wiki/fuentes/comfyui-for_architects-architutors.md`, `diagramas/agentes-fuentes.*` (3).
Modificados: `raw/yt/index-state.json`, `scripts/{yt_build_index,00-index}.md`, `.opencode/agents/{sherlock,contenidos,vaultworm-arq}.md`, `wiki/fuentes/00-index-yt.md` (renombre+regen), `log.md` (12 entradas).

## Pendiente (próxima sesión)

- `s` #3: `@vaultworm-arq` conecta video 1 a glosario/estudio + primera página-galería local
- Video 2 del lote ComfyUI (de a 1) · Piloto revista (Tesseract + PyMuPDF) · 3 links IG ejemplo
- Disparar Agente 1 (ingesta) + Agente 2 (vista-grafo) con los specs como brief
- Reunión con Emilia (llevar PNG + specs + convenciones)

## Análisis cerebro-digital (Karpathy)

- **Topics**: ingest-fuentes, handoff-agentes, ficha-bibliografica, image-first, transcripts-yt, nomenclatura-fuentes, vista-grafo, canvas-imagenes, vaultworm-semanal
- **Entidades**: architutors, flux-kontext, comfyui-cloud, youtube-data-api, tesseract (pendiente), pymupdf (pendiente)
- **Hechos**: protocolo mover-borrar estrenado y verificado; RAW=fecha / wiki=tema; `:` inválido en tags Obsidian; mermaid→canvas solapa títulos (construir a mano); export escena sin tab devuelve parcial (restaurar del .excalidraw.md); Sherlock nunca wiki / Contenidos solo fuentes / Vaultworm resto semanal
