---
tipo: plan
proyecto: threads-paralelos
cliente: interno
fase: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [plan, threads, sherlock, contenidos, moodboard, vault-visual, hitl]
idioma: es
estado: plan
---

# PLAN — 3 Threads paralelos (2026-09-09) — @sherlock / @contenidos / Moodboard

> Copiá cada bloque `Instrucción para terminal` tal cual en una terminal distinta con `opencode` abierto en `P:\00-repos\proyecto-pi\vault-arquitectura` (`.\with-env.ps1 opencode` si Windows). Cada thread es independiente, respeta `AGENTS.md:98-99` HITL (`¿Avanzo? s/N` + código `scripts/<slug>.py` + `scripts/<slug>_notas.md` `# NOTA ES`).

## Thread 1 — @sherlock solo BUSCA (humano/redes legado, alta prioridad)

### Qué hace

@sherlock BUSCA en internet (redes sociales, YouTube, webs, PDFs, papers — siempre doc oficial primero) bilingüe ES/EN+IT con fuentes APA idioma original + `[trad. propia]`. No procesa a wiki; deja hallazgos brutos en `raw/research/` + `raw/research/00-index.md` y @contenidos los cura.

### Instrucción para terminal 1 — copiar tal cual

```
@sherlock investiga Andrej Karpathy legado redes papers y Bjarke Ingels / BIG legado redes — tema humano doble piloto — bilingüe ES/EN+IT con doc oficial primero — alta prioridad pbk-sherlock.md:73

Objetivo: decidir/aprender — alcance internacional + IT poco — deja raw/research/2026-09-09-karpathy-legado.md y raw/research/2026-09-09-big-bjarke-ingels.md con Fecha|Fuentes N|Confianza + Resumen + Ejes con citas inline + Fuentes APA idioma original + Metodología queries ES/EN/IT + URLs status 200 + gaps + Propuestas esqueleto wiki/glosario + actualiza raw/research/00-index.md con Dependencias vault (wiki/glosario/referentes/andrej-karpathy, wiki/glosario/referentes/big-bjarke-ingels-group, cerebro-digital-karpathy). No toques wiki/ — presenta ¿Avanzo a curaduría? s/N para que @contenidos genere raw/contenidos/. Ver AGENTS.md HITL + pbk-sherlock.md Flujo HITL + wiki/glosario/00-index.md 5 reglas.

OBLIGATORIO en cada informe: anota TIEMPO que llevó la investigación (cronometra desde websearch inicial hasta cierre, ej. Tiempo: 42 min), CANTIDAD DE SITIOS revisados (ej. Sitios: 18 — 7 oficiales docs + 6 papers + 5 prensa), con INDICE numerado por sitio y tabla Fuentes N | Tipo | Idioma | Status 200 | Confianza. Usa deep-research/SKILL.md 15-30 fuentes como criterio y deja Metodología con queries por idioma. Si necesitas código (no esperado aquí), pide ¿Avanzo con código <slug>? s/N y genera scripts/<slug>.py + scripts/<slug>_notas.md # NOTA ES.
```

### DoD Thread 1

- [ ] `raw/research/2026-09-09-karpathy-legado.md` + `raw/research/2026-09-09-big-bjarke-ingels.md` existen, con `websearch 2-3 vars × sub-pregunta × idioma` ≥15 fuentes c/u, `webfetch` 3-5 deep 200, cita oficial primero si aplica, gaps explícitos + **Tiempo:** `HH:MM` + **Sitios:** `N (X oficiales + Y papers + Z prensa)` + **Índice** numerado por sitio + tabla Fuentes N | Tipo | Idioma | Status 200 | Confianza
- [ ] `raw/research-cache/2026-09-09-karpathy.json` + `...-big.json` con queries/URLs/status
- [ ] `raw/research/00-index.md` actualizado con 2 filas + Dependencias wikilinks + columnas Tiempo/Cantidad sitios/Índice
- [ ] `¿Avanzo a curaduría?` presentado, sin write en `wiki/`

---

## Thread 2 — @contenidos PROCESA (reporte legible HITL, también con tu material manual)

### Qué hace

@contenidos PROCESA lo que encuentra @sherlock o lo que vos le entregás manualmente (`activos/videos/...mkv` OBS o `activos/pdfs/...pdf` / `C:\...`). Siempre genera `raw/contenidos/YYYY-MM-DD-<slug>.md` con plantilla `_template.md` (Resumen 5 bullets + Qué parte wiki alimenta + Contenidos extraídos verbatim + Ruta+frontmatter + Tags/wikilinks + Referencias 200) para que revises BEFORE subir. Con tu `s` escribe `wiki/estudio/**` y `pbooks/pbk-*` directo; glosario siempre vía `@vaultworm-arq`.

### Instrucción para terminal 2 — copiar tal cual

**Caso 2 — clase propuestas comerciales academia (tu .mkv):**

```
@contenidos procesa "activos/videos/ghl-2026-09-09-propuestas-comerciales-academia.mkv" — intake video academia capturado con OBS (FASE 1 = OBS + material manual con invocación explícita). Vas a grabar esta clase con OBS → guardar como activos/videos/ghl-2026-09-09-propuestas-comerciales-academia.mkv → si no hay transcript, te indicaré P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/videos/ghl-2026-09-09-propuestas-comerciales-academia.mkv" --model medium --language es (vos lo ejecutás, bash: deny). Luego generá raw/contenidos/2026-09-09-propuestas-comerciales-academia.md con plantilla _template.md (Resumen 5 bullets + Qué parte wiki alimenta tabla Destino exacto Tipo Acción Sección Owner + Contenidos extraídos verbatim con timestamps [00:03:21] + Ruta donde guardará + frontmatter + Tags + wikilinks Conceptos ≥2 + Referencias 1 oficial+1 externa 200). No escribas wiki/ sin ¿Avanzo a wiki? s/N — si s, escribe wiki/estudio/** directo y deriva wiki/glosario/** a @vaultworm-arq. También procesa raw/research/2026-09-09-karpathy-legado.md y big si ya están de Thread 1.
```
> Si ya grabaste, reemplaza el nombre por el real. Si necesitas curar también Thread 1, @contenidos puede hacer ambos en la misma corrida: raw/research/ + tu .mkv.

**Opcional — curar Thread 1 si ya existe:**

```
@contenidos procesa raw/research/2026-09-09-karpathy-legado.md y raw/research/2026-09-09-big-bjarke-ingels.md — genera reporte legible HITL raw/contenidos/2026-09-09-karpathy-legado.md y raw/contenidos/2026-09-09-big-bjarke-ingels.md con misma plantilla.
```

### DoD Thread 2

- [ ] `activos/videos/ghl-2026-09-09-propuestas-comerciales-academia.mkv` grabado con OBS + `raw/contenidos/2026-09-09-propuestas-comerciales-academia.md` con checklist `_template.md` completo (Resumen + Destino wiki + Contenidos extraídos verbatim [00:03:21] + Ruta+frontmatter + Tags + Referencias 200) y `¿Avanzo a wiki? (s/N)` presentado
- [ ] Sin write en `wiki/` sin tu `s`; con `s`, `wiki/estudio/**` creado y glosario derivado a `@vaultworm-arq` con destino exacto `wiki/glosario/software/<tool>.md#Seccion`

---

## Thread 3 — Moodboard + Vault Visual + ComfyUI local L1+L2 (DoD + spec)

### Qué hace

Analizar `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/Advertising1 - Moodboard Creation.json:1-968` (Recraft `392+395+401` + GPT `430` API, no corre sin keys) y generar variante **local L1+L2** en RX570 8GB DirectML (`pbk-comfyui.md:58-63`) + plan de ingesta `activos/referentes/` y simulación vault visual en Obsidian (Dataview/Canvas/Excalidraw) aunque Obsidian no hace visión.

### Instrucción para terminal 3 — copiar tal cual (armar flujo en tu Comfy local vía MCP)

```
Armá el flujo moodboard L1+L2 en mi Comfy local vía MCP comfyui — batch que vos LO ARMES con el MCP local (comfyui-mcp, http://127.0.0.1:8188).

1. Lee proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/Advertising1*json:1-968 + reglas-workflows-comfy.md:15-32 R1 ImageScale 512 + 76-116 estructura WF + pbk-comfyui.md:58-63 Base local DirectML (prohibido CUDA, solo DirectML) + 84-98 pipeline Canny + 100-145 tabla Canny/Depth + wiki/glosario/software/comfyui.md catálogo (ArchitectureRealmix v1.1 2.1GB SD1.5 + ControlNet Canny 689MB + Depth FP16 689MB) y propone variante LOCAL L1 Variation (ImageScale lanczos 512 + Canny 0.31/0.59 + ControlNetLoader control_v11p_sd15_canny + ControlNetApplyAdvanced 0.85/0.80 + CheckpointLoaderSimple architecturerealmix_v11 + KSampler euler_ancestral karras 30 cfg7 + IPAdapterUnifiedLoader weight 0.65 style) y L2 Alteration (Batch mood refs CLIPVision + product Canny 0.12/0.39 + IPAdapter product 0.8 + denoise 0.75, fallback VAEEncode img2img si no IPAdapter). Documenta nodos con docs.comfy.org/built-in-nodes/<PascalCase> AGENTS.md:97.

2. Con el MCP local comfyui (comfyui_comfy_cli/comfyui_create_workflow/comfyui_enqueue_workflow), validá nodos disponibles (comfyui_create_workflow action node_info) y armá el workflow local L1+L2 batch: usa comfyui_create_workflow create + validate + enqueue_workflow, o comfyui_enqueue_workflow run_template si hay pack. Si falta IPAdapter, propone fallback VAEEncode denoise 0.65. Guarda el workflow como proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/WF/WF_v1_local_Canny_IPA/workflow_moodboard_local.json y deja salidas en salidas/n_06-B-01.png con 02-WF-log (seed/cfg/strength). Usa el MCP local — no inventes flujo API Recraft/GPT, es solo DirectML local.

3. Lee wiki/glosario/conceptos/vault-visual.md:19-28 + cerebro-digital-karpathy.md:15-20 + AGENTS.md:7,42-55 .gitignore:2 /activos/ + analiza ingesta 3 destinos: activos/videos/ytb-...mkv, activos/proyectos/<obra>/referentes/YYYY-MM-DD-<origen>-<slug>-NN.jpg, activos/proyectos/<obra>/renders/ + ficha 1:1 .md con frontmatter tipo referente estilo:[toscana,piedra] material curaduria + sin ficha no entra.

4. Lee .obsidian/core-plugins.json canvas + excalidraw-skill y propone simulación vault-visual: Dataview TABLE where curaduria si elemento cocina estilo toscana material piedra + Canvas file nodes + Excalidraw con ![[activos/...]] (Obsidian local sí lee gitignored, Quartz no — servir aparte analisis-despliegue-wiki-quartz.md:411). Si necesitas código (ej. indexar referentes), genera scripts/<slug>.py + scripts/<slug>_notas.md # NOTA ES y pide ¿Avanzo a ejecutar? s/N.

5. Deja specs/2609XX-moodboard-vault-visual-local.md + flujo MCP validado. Presenta ¿Avanzo? s/N — no escribas wiki/ sin s (wiki/glosario/conceptos/moodboard.md vía @vaultworm-arq).
```

### DoD Thread 3

- [ ] Flujo MCP local validado vía `comfyui_create_workflow node_info` + `enqueue_workflow` en `http://127.0.0.1:8188` — workflow `WF/WF_v1_local_Canny_IPA/workflow_moodboard_local.json` creado con nodos `ImageScale 512 lanczos`, `Canny 0.31/0.59` / `0.12/0.39`, `ControlNetApplyAdvanced 0.85/0.80`, `KSampler 30 cfg7` + fallback `VAEEncode` si falta IPAdapter, sin usar API Recraft/GPT, solo DirectML
- [ ] `specs/2609XX-moodboard-vault-visual-local.md` existe con Objetivo + L1+L2 con nodos `docs.comfy.org/built-in-nodes/<PascalCase>` verificados + Arquitectura ingesta 3 destinos + Simulación Obsidian
- [ ] `salidas/n_06-B-01.png` y `02-WF-log` con seed/cfg/strength + ingesta `activos/proyectos/<obra>/referentes/` con ficha `.md` frontmatter buscable + `Canvas` + `Dataview` query funcionando

---

## Reglas transversales a los 3 threads

- `AGENTS.md:98-99` HITL: ningún `write` en `wiki/` ni `bash` sin `s` explícito; todo código en `scripts/<slug>.py` + `scripts/<slug>_notas.md` `# NOTA ES` y comando `P:\Anaconda\envs\comfyenv\python.exe scripts/...` lo ejecutás vos (salvo Thread 3 si pide ¿Avanzo a ejecutar? s).
- `@sherlock` solo BUSCA → `raw/research/` + `raw/research/00-index.md` + `raw/research-cache/*.json` (auto por defecto, backlog `pbk-sherlock.md:78`).
- `@contenidos` PROCESA → `raw/contenidos/_template.md` → `¿Avanzo a wiki?` → `wiki/estudio` directo / `wiki/glosario` vía `@vaultworm-arq` (`pbk-agentes-vaultarq.md:64`).
- `activos/` gitignored `AGENTS.md:7` — `.md` solo `[activos/...]` o `` `C:\BIM\...` ``.
- Cada thread actualiza `log.md` (Más nuevo → más arriba) + `raw/sessions/YYYY-MM-DD-sesion-<slug>.md` al cerrar.

## Referencias

- `.opencode/agents/sherlock.md` + `wiki/glosario/interno/pbooks/pbk-sherlock.md` — investigador GENERAL @sherlock, backlog 11 ítems
- `.opencode/agents/contenidos.md` + `SKILL.md` — curador con intake manual + reporte `raw/contenidos/`
- `.opencode/agents/vaultworm-arq.md` + `pbk-agentes-vaultarq.md` — dueño `wiki/glosario/**`
- `AGENTS.md:7,42-55,97-99,111` — binarios, wikilinks, verificar 200, HITL código paralelo
- `wiki/glosario/00-index.md:26-30` — 5 reglas calidad glosario
- `specs/260909-plan-accion-web-research-moodboard-youtube.md` — plan Fase 0 DONE, Fase 1A/1B + Vía A OBS default, Vía B yt-dlp solo con s
- `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/Advertising1 - Moodboard Creation.json:1-968` — flujo Recraft+GPT API
- `wiki/glosario/conceptos/vault-visual.md:19-28` + `cerebro-digital-karpathy.md:15-20` — brain visual
