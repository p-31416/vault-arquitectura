---
tipo: playbook
codigo: pbk-sherlock
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [pbook, sherlock, investigacion, websearch, webfetch, hitl, bilingue, documentacion]
idioma: es
---

# pbk-sherlock — Playbook del investigador GENERAL @sherlock

> Qué hace Sherlock, dónde vive su código y cómo pedirle trabajo. Definición viva en `.opencode/agents/sherlock.md`; este pbook es el índice razonado + backlog futuro.

- [Qué hace](#qué-hace)
- [Dónde vive el código](#dónde-vive-el-código)
- [Cómo está conformado (código)](#cómo-está-conformado-código)
- [Flujo HITL](#flujo-hitl)
- [Bilingüe y doc oficial primero](#bilingüe-y-doc-oficial-primero)
- [Piloto 2026-09-09](#piloto-2026-09-09)
- [Backlog — futuro](#backlog--futuro)
- [Conceptos relacionados](#conceptos-relacionados)
- [Referencias](#referencias)

## Qué hace

**@sherlock** es el investigador GENERAL del vault. Le das un tema libre — humano (redes, legado, papers), software, normativa, referente — y lo investiga en web **siempre yendo al manual/tutorial/documentación oficial primero** (heredado desarrollo software), bilingüe ES/EN+IT trayendo fuentes bibliográficas en idioma original + `[trad. propia]`, y lo procesa al vault **solo con tu `s` HITL**.

No es solo técnico: investiga personas, estudios, obras, papers, incumbencias. Propone `raw/research/YYYY-MM-DD-<slug>.md` con informe citado y **no toca `wiki/` sin tu `s`**; el ingest final de glosario lo hace `@vaultworm-arq` (dueño `wiki/glosario/**`).

## Dónde vive el código

| Capa | Ruta | Qué hay |
|---|---|---|
| **Agente** | `.opencode/agents/sherlock.md` | Frontmatter `description` (drive delegación) + `mode: subagent` + `temperature: 0.2` + `permission: {read,grep,glob,edit: allow; bash: deny; task,skill,websearch,webfetch: allow}` + Misión 5 pasos + Reglas HITL |
| **Playbook** | `wiki/glosario/interno/pbooks/pbk-sherlock.md` | Este archivo — qué hace, flujo, backlog |
| **Código generado** | `scripts/<slug>.py` + `scripts/<slug>_notas.md` o `scripts/<slug>_explicado.py` | Todo código nuevo en **archivo paralelo didáctico** con `# NOTA ES:` línea a línea para que aprendas Python leyendo. `AGENTS.md` HITL obliga: propone comando exacto `P:\Anaconda\envs\comfyenv\python.exe scripts/...` y vos lo ejecutás |
| **Cache** | `raw/research-cache/<fecha>-<slug>.json` | Queries ES/EN/IT + URLs + status 200 para dedup |
| **Salida investigación** | `raw/research/YYYY-MM-DD-<slug>.md` | Informe `Fecha|Fuentes|Confianza` + Metodología + Propuestas wiki con `¿Avanzo?` |
| **Ingest final** | `wiki/glosario/**` (vía `@vaultworm-arq`) + `wiki/estudio/` | UNICO `.md` por tool, `## Conceptos relacionados ≥2`, `## Referencias` 1 oficial+1 externa 200 |

## Cómo está conformado (código)

Frontmatter mínimo + 5 secciones (Misión, Capacidades, Reglas duras, Invocación, Restricciones) igual que `vaultworm-arq.md:1-14`. Temperatura `0.2` criterio (más baja que `vaultworm-arq 0.3` para rigor bibliográfico). Skills downstream: `deep-research` (workflow base `websearch 2-3 vars × sub-pregunta → 15-30 fuentes → webfetch 3-5 deep → informe`), `article-writing`+`brand-voice` (si es memoria), `architecture-decision-records` (si es decisión).

## Flujo HITL

```
Tema libre → @sherlock (websearch/webfetch 15-30 fuentes doc-oficial-primero) → raw/research/<slug>.md (informe + propuestas + Bibliografía APA + gaps)
  → ¿Avanzo? (s/N) SOL → si s: delega glosario a @vaultworm-arq → wiki/glosario/** + índices + log.md (entrada nueva arriba AGENTS.md:81)
```

- Si tenés PDF/video: academia IA (`ghl-`/`ytb-academia`) → `@contenidos` Fase 2 (con tu `s`); investigación general (paper, norma, manual) → `@sherlock` directo. Ante duda pregunta.
- MCP nuevo (`tavily/exa/pdf-extract/youtube-transcript`) solo con `¿Avanzo con MCP <nombre>? s/N` explícito. Default `websearch/webfetch` nativo con fallback.
- Código: propone `¿Avanzo con código <slug>? s/N` → escribe `scripts/<slug>.py` + paralelo anotado → vos ejecutás `P:\Anaconda\envs\comfyenv\python.exe scripts/<slug>.py`.

## Bilingüe y doc oficial primero

- Queries en ES, EN e IT por sub-pregunta; cita APA `Autor (año). Título original [Traducción]. URL (verificado 200, idioma: IT)` — original íntegro + traducción en corchetes, nunca reemplaza.
- Prioridad: (1) oficial/manual/tutorial/docs (`help.autodesk.com/view/ACD/2026/ENU/GUID-`, `docs.comfy.org/built-in-nodes/<PascalCase>`), (2) normativa/académica, (3) estudios/referentes, (4) blogs. Recencia 12m salvo normativa.

## Piloto 2026-09-09

- AutoCAD: 8 sub-preguntas (LINE/LAYER/HATCH/ssget/command/entmod/CLAYER/CELTYPE/LUNITS + OFFSET/FILLET/BLOCK/DXF 90/70/42) + legal Ley 24.335/CPAU → `wiki/glosario/software/autocad.md` + `wiki/legal/plano-como-documento-legal.md` + `tec-capas-autocad.md`.
- ComfyUI: `KSampler/CheckpointLoaderSimple/CLIPTextEncode/EmptyLatentImage/VAEDecode/SaveImage` → `wiki/glosario/software/comfyui.md:538` + DirectML `pbk-comfyui.md` flags.
- Todo vía `specs/260909-plan-accion-web-research-moodboard-youtube.md` Fase 1A/1B con gate por sprint.

## Backlog — futuro (pendientes, requiere tu `s` por ítem)

> Herramientas y ampliaciones que podría tener @sherlock a futuro. No priorizado; cada ítem es un `¿Avanzo?` separado.

- [ ] **Búsqueda académica:** `OpenAlex / Semantic Scholar / Crossref / Google Scholar (via SerpAPI)` — papers, citas, DOI → APA con idioma original; métrica `cited_by`
- [ ] **Normativa AR profunda:** `Infoleg PDF extract + CABA Boletín Oficial` — parse `Ley 24.335 / Código Edificación / CPAU` con `webfetch` PDF + `pypdf/pymupdf` local (MCP `pdf-extract` con tu aprobación)
- [ ] **Detección persona/redes:** `site:linkedin.com / site:instagram.com / site:archdaily.com / site:behance.net` + `websearch` ES/EN/IT + `archive.org` para legado/webs muertas
- [ ] **Docs oficiales allowlist:** `help.autodesk.com/view/ACD/2026/ENU/GUID-`, `docs.comfy.org/built-in-nodes/<PascalCase>`, `help.adobe.com`, `docs.rhino3d.com`, `docs.mcneel.com` — siempre citar oficial 200 antes de blog
- [ ] **Imágenes/moodboard:** `Pinterest/ArchDaily reverse image search` + `vault-visual.md` — curaduría `activos/referentes/` → `ComfyUI ControlNet Canny` para variantes (ya en `n_06`)
- [ ] **YouTube Fase 2 nativa:** `yt-dlp + youtube-transcript-api` → `scripts/transcribir_youtube.py` + `scripts/transcribir_youtube_notas.md` (Vía B, tu `s` HITL, Vía A OBS sigue default sin riesgo clones `specs/260909-plan-accion...:106-112`)
- [ ] **Traducción trazable:** `DeepL API` solo como `[trad. propia]` paralela, nunca reemplaza original IT/EN
- [ ] **Cache/dedup:** `raw/research-cache/<fecha>-<slug>.json` con `queries ES/EN/IT + URLs + status 200 + recencia 12m + site:gob.ar`
- [ ] **MCPs opcionales (1 a la vez, con tu `s`):** `tavily` o `exa` (re-rank + PDF/JS), `brave-search` — fallback a `websearch/webfetch` nativo si falla (`opencode.json:10-25`)
- [ ] **Código paralelo didáctico:** mantener `bash: deny` en `sherlock.md:permission`; todo `P:\Anaconda\envs\comfyenv\python.exe scripts/<slug>.py` lo ejecutás vos, agente solo indica comando exacto (AGENTS.md HITL)
- [ ] **Valija bilingüe IT:** glosario `it-es` de términos jurídicos/técnicos (incumbencia, visado, CCT) para no perder matiz al traducir

## Conceptos relacionados

- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]
- [[wiki/glosario/conceptos/vault-visual|vault-visual]]
- [[wiki/glosario/software/opencode|opencode]]
- [[wiki/glosario/software/autocad|AutoCAD]]
- [[wiki/glosario/software/comfyui|ComfyUI]]

## Referencias

- `.opencode/agents/sherlock.md` — definición viva del agente
- `.opencode/skills/deep-research/SKILL.md` — workflow base websearch/webfetch
- [[wiki/glosario/00-index|Reglas de calidad del glosario]] — 5 reglas + Referencias sin 404
- [[wiki/glosario/interno/pbooks/pbk-agentes-vaultarq|pbk-agentes-vaultarq]] — dueño glosario @vaultworm-arq + cómo agregar agente
- [[AGENTS.md]] — HITL + verificar enlaces
- `specs/260909-plan-accion-web-research-moodboard-youtube.md` — plan Fase 0-2 con Vía A OBS default
- `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/Advertising1 - Moodboard Creation.json:1-968` — flujo Recraft+GPT
