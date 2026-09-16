---
tipo: sesion
fecha: 2026-09-09
slug: sherlock-contenidos-moodboard-threads
participantes: [SOL, sherlock, contenidos, vaultworm-arq]
tags: [sherlock, contenidos, vaultworm-arq, hitl, moodboard, vault-visual, deep-research, threads]
idioma: es
estado: borrador
---

# Sesión 2026-09-09 — @sherlock / @contenidos / Moodboard + Vault Visual (3 threads)

> 3 hilos paralelos definidos para que puedas abrir 3 terminales con opencode y pegar cada instrucción. Acuerdos HITL + código paralelo didáctico + separación de responsabilidades cerrados.

## Qué se hizo

- Auditoría very-thorough con 3 subagentes `explore`: stack web (websearch/webfetch vs @explore local), gaps AutoCAD (`autocad.md:150-174` 9 stubs + legal Ley 24.335) y ComfyUI (`comfyui.md:538` 6 nodos + DirectML), flujo `n_06-moodboard/Advertising1 - Moodboard Creation.json:1-968` (Recraft 392+395+401 + GPT 430 API vs local L1/L2), vault-visual `vault-visual.md:19-28` + ingesta `activos/` + simulación Obsidian Dataview/Canvas.
- Diseño y cierre de agente GENERAL `@sherlock` (tema libre humano/redes/legado/papers/software SIEMPRE al manual oficial primero) bilingüe ES/EN+IT con fuentes APA idioma original + `[trad. propia]`:
  - Registrado con tus ajustes: solo BUSCA (no procesa), quien PROCESA es `@contenidos` (también con tu PDF/video manual), quien escribe `wiki/glosario/**` es `@vaultworm-arq` (dueño UNICO .md por tool `wiki/glosario/00-index.md:26`). Todo con `¿Avanzo? s/N` + código `scripts/<slug>.py` + `scripts/<slug>_notas.md` `# NOTA ES` para que aprendas Python leyendo (`AGENTS.md:98-99` HITL).
  - Backlog 11 ítems en `pbk-sherlock.md:67-81` revisado 1 a 1 contigo: alta prioridad `persona/redes site:linkedin/archdaily + archive.org` piloto Karpathy + BIG/Bjarke Ingels (doble piloto), docs oficiales como regla preferente (si no hay, gap + otras refs), moodboard L1+L2 con IPAdapter, YouTube Vía A OBS default (GHL siempre OBS) y Vía B `yt-dlp` solo con tu `s` y throttling (riesgo baneo medio si masivo), fuentes originales sin DeepL, cache `raw/research-cache/*.json` auto por defecto, `raw/research/00-index.md` con Tiempo/Cantidad sitios/Índice, MCPs backlog, valija IT.
- Plan en `specs/`:
  - `specs/260909-plan-accion-web-research-moodboard-youtube.md` Fase 0 DONE (@sherlock creado), Fase 1A/1B piloto AutoCAD/ComfyUI, Vía A OBS 10min vs Vía B yt-dlp con tu `s`.
  - `specs/260909-threads-sherlock-contenidos-moodboard.md:1` con fecha hoy, 3 instrucciones copiables por terminal (T1 @sherlock con métricas Tiempo/Sitios/Índice, T2 @contenidos con tu `.mkv` real `ghl-2026-09-09-propuestas-comerciales-academia.mkv`, T3 Moodboard L1+L2 armado con **MCP local comfyui `http://127.0.0.1:8188` solo DirectML**).
- Separación ownership cerrada con 2 auditorías `vaultworm-arq` + `contenidos`: `raw/research/` (@sherlock) → `raw/contenidos/` reporte legible `_template.md` (Resumen + Destino wiki + Contenidos extraídos verbatim + Ruta+frontmatter + Tags + Referencias 200 + Gate) → `wiki/estudio` (@contenidos con s) / `wiki/glosario` (@vaultworm-arq con s). Intake manual `activos/pdfs/...pdf` habilitado en `@contenidos` Fase 1 + material manual.

## Archivos modificados

- `AGENTS.md:98-99` — principio HITL obligatorio código paralelo didáctico `scripts/<slug>.py` + `*_notas.md` `# NOTA ES` + `P:\Anaconda\envs\comfyenv\python.exe ...`
- `.opencode/agents/sherlock.md:1` — nuevo agente GENERAL temp 0.2 `websearch: allow` `bash: deny` solo BUSCA, HITL doble s
- `wiki/glosario/interno/pbooks/pbk-sherlock.md:1` — playbook qué hace, dónde vive código `scripts/<slug>.py`, flujo HITL, piloto, backlog 11 ítems con alta prioridad persona/redes
- `wiki/glosario/interno/pbooks/pbk-agentes-vaultarq.md:31,64` — tabla 5 agentes + comparativa con sherlock + intake `raw/research/`
- `wiki/glosario/software/opencode.md:46` — fila @sherlock
- `specs/260909-plan-accion-web-research-moodboard-youtube.md:1` — renombrado @sherlock, HITL código paralelo, Fase 0 DONE
- `specs/260909-threads-sherlock-contenidos-moodboard.md:1` — 3 threads con instrucciones copiables (T1 Tiempo/Sitios/Índice, T2 tu .mkv, T3 MCP local)
- `.opencode/agents/contenidos.md:24-28` + `.opencode/skills/contenidos/SKILL.md:1,6` — intake manual PDF/video + reporte `raw/contenidos/` HITL, FASE 1 = OBS + manual con invocación explícita
- `raw/contenidos/_template.md:1` — plantilla reporte HITL
- `raw/research/00-index.md:1` — índice búsquedas @sherlock con Tiempo/Sitios/Índice y Dependencias vault
- `raw/contenidos/` + `raw/research/` creados (vacío de informes aún)

## Análisis cerebro-digital (Karpathy)

### Topics → glosario/software|conceptos

| Topic candidato | Por qué | Destino `wiki/glosario/...` |
|---|---|---|
| sherlock websearch/webfetch bilingüe | Investigador GENERAL tema libre doc-oficial-primero ES/EN+IT | `wiki/glosario/software/sherlock.md` o sección en `opencode.md#sherlock` + `wiki/glosario/interno/pbooks/pbk-sherlock.md` (creado) |
| OpenAlex / SerpAPI | Búsqueda académica DOI `cited_by` | `wiki/glosario/software/openalex.md` + `serpapi.md` (pendiente crear, backlog L71) |
| yt-dlp / youtube-transcript-api | YouTube Fase 2 Vía B con throttling, riesgo baneo IP | `wiki/glosario/software/yt-dlp.md` (pendiente, backlog L76) |
| IPAdapter / ControlNet Canny | Moodboard L1+L2 local DirectML 512 `Canny 0.31/0.59` | `wiki/glosario/software/comfyui.md#IPAdapter` (completar) |
| vault-visual / moodboard | Ingesta `activos/referentes/` + ficha + Dataview/Canvas | `wiki/glosario/conceptos/moodboard.md` vía @vaultworm-arq (pendiente) + `vault-visual.md:19-28` |

### Entidades

- SOL — dueño HITL `¿Avanzo? s/N`, ejecuta `P:\Anaconda\envs\comfyenv\python.exe ...`
- @sherlock — investigador GENERAL (solo BUSCA, no procesa)
- @contenidos — curador academia + intake manual PDF/video → reporte `raw/contenidos/` legible
- @vaultworm-arq — dueño `wiki/glosario/**` UNICO .md por tool
- Referentes piloto alta prioridad: `Andrej Karpathy` (`wiki/glosario/referentes/andrej-karpathy.md`) y `Bjarke Ingels / BIG` (`wiki/glosario/referentes/big-bjarke-ingels-group.md`)

### Hechos/decisiones reutilizables

- Decisión: `@sherlock` nunca toca `wiki/` ni procesa fino; `@contenidos` siempre genera `raw/contenidos/` reporte con Resumen + Destino wiki + Contenidos verbatim + Ruta+frontmatter + Tags + Referencias 200 antes de `¿Avanzo a wiki?`
- Decisión: código paralelo didáctico obligatorio `AGENTS.md:99` + doble s (crear→leer→ejecutar con `P:\Anaconda\envs\comfyenv\python.exe` vos ejecutás, `bash: deny` en agentes)
- Decisión: GHL siempre OBS `activos/videos/ghl-...mkv`; YouTube Vía A OBS default 0 riesgo, Vía B `yt-dlp` solo con tu `s`, `youtube-transcript-api` primero sin descarga, `sleep 5s`, `max 10/día`, `pin pypi.org/simple`
- Decisión: `raw/research/00-index.md` con Tiempo que llevó investigación + Cantidad sitios con Índice numerado + Dependencias vault wikilinks
- Hecho: `n_06-moodboard:1-968` es 100% API Recraft+GPT (5 nodos API), brecha local L1 Variation `ImageScale 512 lanczos + Canny 0.31/0.59 + ControlNet 0.85/0.80 + Realmimix 2.1GB + IPAdapter 0.65` y L2 Alteration `Batch CLIPVision + product Canny + denoise 0.75` cabe en RX570 8GB

### Preguntas para SOL

- ¿Cuál piloto arranca T1? Karpathy vs BIG orden, o ambos en paralelo
- ¿Ya tienes `activos/videos/ghl-2026-09-09-propuestas-comerciales-academia.mkv` grabado para T2 o lo grabamos juntos en build?
- ¿Moodboard T3 L1+L2 con IPAdapter lo armamos vía MCP local `http://127.0.0.1:8188` en tu Comfy `P:\00-repos\ComfyUI` ahora o después de T1/T2?
