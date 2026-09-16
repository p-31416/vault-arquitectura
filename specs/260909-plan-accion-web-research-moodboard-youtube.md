---
tipo: plan
proyecto: web-research-moodboard-youtube
cliente: interno
fase: concepto
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [plan, sherlock, moodboard, youtube, autocad, comfyui, vault-visual, contenidos, hitl]
idioma: es
estado: plan
---

# Plan de acción — Investigación web + Moodboard + YouTube (AutoCAD / ComfyUI) — @sherlock

> Unifica 3 pedidos en 1 ejecución trazable: (1) agente GENERAL `@sherlock` para cualquier tema (humano/redes/legado/papers/software SIEMPRE al manual oficial, bilingüe ES/EN+IT con fuentes en idioma original), (2) moodboard `n_06-moodboard` Recraft+GPT, (3) transcript YouTube `cTdHYiD28F4` vía `@contenidos`. Define herramienta, flujo terminal y gates HITL con código paralelo didáctico sin violar `AGENTS.md` ni glosario.

## 0. Resumen en 1 línea

Crear `@sherlock` (websearch+webfetch, temp 0.2, `bash: deny`) generalista bilingüe con HITL `¿Avanzo?` + código `scripts/<slug>.py` + `scripts/<slug>_notas.md` (`# NOTA ES` línea a línea), cerrar gaps AutoCAD/ComfyUI como piloto 1A/1B, normalizar `n_06-moodboard` y desbloquear `YouTube → vault` vía Vía A OBS default + Fase 2 `yt-dlp` solo con tu `s`.

## 1. Objetivo

- **Investigador GENERAL @sherlock (no solo técnico):** tema libre — humano/redes/legado/papers/software SIEMPRE al manual/docs oficial primero (heredado dev), bilingüe ES/EN+IT trayendo **fuentes bibliográficas en idioma original + `[trad. propia]`** con APA + `idioma_original`. Piloto: 9 stubs AutoCAD (`autocad.md:150-174` + `OFFSET/FILLET/BLOCK/DXF 90/70/42`) + 6 nodos ComfyUI (`comfyui.md:538` KSampler/CheckpointLoaderSimple/CLIPTextEncode/EmptyLatentImage/VAEDecode/SaveImage) + 2 stubs legales Ley 24.335/CPAU — con `websearch 2-3 vars × sub-pregunta × idioma → 15-30 fuentes → webfetch 3-5 deep 200 → raw/research/ → ¿Avanzo? → @vaultworm-arq → wiki/glosario` (contract `deep-research/SKILL.md:16-59` + `pbk-sherlock.md` + `wiki/glosario/00-index.md:27-30`). Ver `AGENTS.md` HITL + `pbk-sherlock.md:Backlog`.
- **Moodboard operativo:** normalizar `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/Advertising1 - Moodboard Creation.json:1-968` (Recraft `RecraftCreateStyleNode:392`+`RecraftStyleV3InfiniteStyleLibrary:395` + GPT `OpenAIGPTImageNodeV2:430`/`BatchImagesNode:409`) a estructura `reglas-workflows-comfy.md:76-116` y variante local SDXL, y definir `wiki/glosario/conceptos/moodboard.md` como entrada `vault-visual.md:19-28`.
- **YouTube → vault:** habilitar `https://www.youtube.com/watch?v=cTdHYiD28F4` (`ComfyUI Moodboard Workflow: Generate On-Brand Ad Images`) → `wiki/raw/ytb-...md` → propuestas `wiki/estudio/`+`wiki/glosario/software/recraft|gpt-image` respetando `contenidos.md:28` Fase1→Fase2 con gate `¿Avanzo?`. Vía A OBS default sin riesgo clones; Vía B `yt-dlp` solo con tu `s` (`AGENTS.md` HITL + `pbk-sherlock.md`). Todo código en `scripts/<slug>.py` + `scripts/<slug>_notas.md` con `# NOTA ES`.

## 2. Por qué un agente nuevo y no reusar `@explore`/`@vaultworm-arq`

| Agente actual | Limite | Evidencia |
|---|---|---|
| `@explore` (built-in opencode) | Solo `grep/glob/read` local, 0 web | No existe `.opencode/agents/explore.md`; `pbk-agentes-vaultarq.md:51-55` no lo lista |
| `@vaultworm-arq` / `@brainstormy` / `@contenidos` / `@fathom-pm` | Solo `webfetch: allow`, falta `websearch: allow`; MCPs 0 | `vaultworm-arq.md:13`, `contenidos.md:13` permiso; `opencode.json:10-25` solo `comfyui`+`fathom` |
| `deep-research` SKILL | Contract perfecto pero hereda permisos del caller → hoy solo corre vía primary | `deep-research/SKILL.md:8,30-52` exige `websearch` y `webfetch` |
| **Gap** | Sin `websearch` delegado, sin extract PDF/YouTube, sin cache/dedup, YouTube `webfetch` devuelve shell vacío (probado) | Auditoría 2026-09-09 |

**Decisión:** crear `@sherlock` (`.opencode/agents/sherlock.md` temp 0.2 criterio) con `websearch: allow` + `webfetch: allow` + `read/grep/glob/edit/task/skill: allow, bash: deny`, reusando workflow `deep-research` + reglas `AGENTS.md:97` no-404 + `wiki/glosario/00-index.md:27-31` (UNICO `.md` por tool, `## Conceptos relacionados ≥2`, `## Referencias` 1 oficial +1 externa 200) + HITL obligatorio `AGENTS.md` (código paralelo `scripts/<slug>.py` + `scripts/<slug>_notas.md` con `# NOTA ES`). Playbook canónico `wiki/glosario/interno/pbooks/pbk-sherlock.md` (qué hace, dónde vive el código, backlog futuro). Ver `pbk-agentes-vaultarq.md`.

Opcional Fase 2: añadir 1 MCP `tavily` o `exa` en `opencode.json` solo con tu `¿Avanzo con MCP <nombre>? s/N` + fallback nativo, para re-rank + `site:gob.ar` + `recencia 12m` + extracción PDF (normativa AR vive en PDF Infoleg).

## 3. Arquitectura de archivos (destino)

```
.opencode/agents/sherlock.md                           # agente GENERAL bilingüe HITL (este plan)
wiki/glosario/interno/pbooks/pbk-sherlock.md           # playbook + backlog futuro
opencode.json                                           # + MCP tavily/exa solo con tu s (fallback nativo)
scripts/transcribir_youtube.py + scripts/transcribir_youtube_notas.md  # Fase 2 (clon transcribir_ghl.py:66-93, didáctico)
specs/260909-plan-accion-web-research-moodboard-youtube.md  # ← este plan
raw/research/<fecha>-<slug>.md + raw/research-cache/<fecha>-<slug>.json  # informe + cache queries
proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/
  ├── 00-README.md | 01-index.md | 02-WF-log-n_06.md | 03-nodos-n_06.md | 04-backlog.md
  ├── salidas/  (n_06-A-01.png, referenciadas como [activos/...])
  ├── Advertising1 - Moodboard Creation.json (original API, 968L)
  └── workflow_moodboard_sdxl_local.json (variante local ImageScale 512 R1)
activos/videos/ytb-2026-09-09-moodboard-recraft-gptimage.{mkv,mp3}  # gitignored
wiki/raw/2026-09-09-ytb-moodboard-recraft-gptimage.md    # raw verbatim + fuente_url
wiki/estudio/metodologia-moodboard-recraft-gptimage.md   # 2 métodos, style_id 02f005e2-..., costos API
wiki/glosario/conceptos/moodboard.md                    # nuevo, vía @vaultworm-arq
wiki/glosario/software/recraft.md | gpt-image.md        # UNICO .md por tool
wiki/glosario/software/autocad.md  (+ secciones LINE/LAYER/HATCH/ssget/command/entmod/CLAYER/CELTYPE/LUNITS)
wiki/glosario/software/comfyui.md  (+ 6 nodos KSampler/CheckpointLoaderSimple/...)
wiki/legal/plano-como-documento-legal.md | wiki/practica-profesional/incumbencia-ley-24335.md (relleno)
wiki/glosario/interno/standares/tecnico/tec-capas-autocad.md (A-MURO...)
```

Binarios NUNCA a git (`AGENTS.md:7`, `.gitignore:2` `/activos/`); `.md` solo `[activos/...]` o `` `C:\BIM\...` `` (`AGENTS.md:47-54`).

## 4. Plan por fases (con gates `¿Avanzo?`)

### Fase 0 — Agente (1-2h, sin riesgo, hacer primero) — DONE 2026-09-09

- [x] Crear `.opencode/agents/sherlock.md` (plantilla `vaultworm-arq.md:1-14` + `websearch: allow`, temp 0.2, `bash: deny`, HITL código paralelo `scripts/<slug>.py` + `scripts/<slug>_notas.md` con `# NOTA ES`) + `wiki/glosario/interno/pbooks/pbk-sherlock.md` + `AGENTS.md:99` principio HITL
- [x] Registrar en `wiki/glosario/interno/pbooks/pbk-agentes-vaultarq.md:24-32` tabla + `wiki/glosario/software/opencode.md` §Agentes
- [ ] (Opcional) Añadir MCP `tavily` remoto en `opencode.json:10-25` solo con tu `s` (`¿Avanzo con MCP tavily? s/N`), fallback a `websearch/webfetch` nativo
- Gate: `¿Avanzo a Fase 1?`

### Fase 1 — Investigación web piloto (2 sprints paralelizables, `¿Avanzo?` por sprint)

**1A AutoCAD (websearch `site:help.autodesk.com` + Infoleg)**

- `websearch` 2-3 vars × 8 sub-preguntas (LINE/LAYER/HATCH/ssget/command/entmod/CLAYER/CELTYPE/LUNITS + OFFSET/FILLET/BLOCK/INSERT/DXF LWPOLYLINE `90/70/42` crítico `proyectos/MVP_01-dibujo_ia/01-spec-mvp_01.md:61-72`) → 20-30 fuentes priorizando `help.autodesk.com/view/ACD/2026/ENU/GUID-` (reemplaza 9 `?query=` `autocad.md:188` riesgo 404) + `webfetch` 3-5 deep verificado 200
- Legal: `infoleg.gob.ar Ley 24.335 + 25.506 firma digital` + `CPAU Código Edificación CABA/DGROC` → rellenar 2 stubs + crear `tec-capas-autocad.md` (A-MURO/A-PTA-)

**1B ComfyUI (webfetch `docs.comfy.org/built-in-nodes/<PascalCase>` `AGENTS.md:97`)**

- `KSampler/CheckpointLoaderSimple/CLIPTextEncode/EmptyLatentImage/VAEDecode/SaveImage` → completar `comfyui.md:538` 6 fichas
- DirectML: `ComfyUI AMD GPUs GitHub + pytorch-directml + city96/ComfyUI-GGUF + Fannovel16/comfyui_controlnet_aux` + RunPod pricing/TOS (`runpod.io` RTX 3090 0.22 USD/h) → actualizar `pbk-comfyui.md:58-63`, `pbk-troubleshooting-reconexion.md`, `modelos-recomendados.md`
- Salida por sprint: `raw/research/<fecha>-<slug>.md` Informe `Fecha|Fuentes|Confianza` + `wiki/glosario/**` UNICO `.md` + `## Conceptos relacionados ≥2` + `## Referencias` 1 oficial +1 externa 200 → gate `¿Avanzo?` antes de escribir (dueño glosario `@vaultworm-arq` `pbk-agentes-vaultarq.md:33-38`)

### Fase 2 — YouTube + Moodboard (2 vías, elegir una)

**Vía A — Bypass OBS inmediato (0 código, 10min, cumple `contenidos.md:28` Fase1)**

```bash
# 1. OBS: Captura pantalla + Captura audio salida → reproducir https://www.youtube.com/watch?v=cTdHYiD28F4 → guardar
#    P:\00-repos\proyecto-pi\vault-arquitectura\activos\videos\ytb-2026-09-09-moodboard-recraft-gptimage.mkv
# 2. Transcribir (video en inglés → --language en):
P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/videos/ytb-2026-09-09-moodboard-recraft-gptimage.mkv" --model medium --language en
# → .mp3 + .txt + .srt + wiki/raw/YYYY-MM-DD-ghl-ytb-....md (frontmatter tipo:raw fuente_binaria: activos/videos/...)
```

`@contenidos` lee `wiki/raw/*.md` + `n_06/*.json` + `vault-visual.md:19-28` + `cerebro-digital-karpathy.md:15-20` → propone (sin escribir hasta `s`):

- `wiki/estudio/metodologia-moodboard-recraft-gptimage.md` (Método 1 `RecraftTextToImageNode:401` style_id `02f005e2-...` + Método 2 `OpenAIGPTImageNodeV2:430` `gpt-image-2` `1024x1024` `quality medium` + Nota `411: Style ID` + `426: Quick Intro`)
- `wiki/glosario/conceptos/moodboard.md` (vía `@vaultworm-arq`) + update `vault-visual.md:30-34` caso `n_06` (piloto Casa → 20-30 referentes con ficha `specs/260907-vault_cerebro.md:131`)
- `wiki/glosario/software/recraft.md` + `gpt-image.md` + normalización `n_06/00-README/01-index/03-nodos/04-backlog/salidas/` + variante local `workflow_moodboard_sdxl_local.json` con `ImageScale 512` (`reglas-workflows-comfy.md:15-32`)

**Vía B — Fase 2 nativa (para todos los próximos YouTubes, con desbloqueos)**

- [ ] `scripts/transcribir_youtube.py` (clon `transcribir_ghl.py:31-44 FFMPEG_CANDIDATES + 66-93 WhisperModel cpu int8 + 95-139 write_raw` + pre-step `yt-dlp --write-auto-sub --sub-lang en,es --skip-download` fallback `yt-dlp -x --audio-format mp3 -o activos/videos/ytb-%(title)s.%(ext)s`)
- [ ] `P:\Anaconda\envs\comfyenv\python.exe -m pip install yt-dlp` (faster-whisper ya en `comfyenv` `transcribir_ghl.py:68-72`)
- [ ] Actualizar `.opencode/agents/contenidos.md:28` → `FASE 2 habilitada: YouTube vía yt-dlp` + `SKILL.md:20` + convención `ytb-YYYY-MM-DD-<slug>.mkv` (`contenidos.md:24`, `obs.md:34`)
- Flujo desde entonces: `pegás link → @contenidos valida webfetch → indica comando transcribir_youtube.py → vos ejecutás → wiki/raw/ytb-...md` (frontmatter `fuente_url: https://www.youtube.com/watch?v=cTdHYiD28F4` + `fuente_binaria: activos/videos/ytb-...mp3` + nota `uso interno, no redistribuir`)

`webfetch` YouTube seguirá vacío (JS shell) — no usar para transcript.

## 5. Checklist terminal paso a paso (cuando ejecutes conmigo)

```powershell
# 0. Ver estado actual (solo lectura, hoy permitido):
Get-ChildItem proyectos\MVP_04-comfyui-arquitectura\n_06-moodboard
Get-Content proyectos\MVP_04-comfyui-arquitectura\n_06-moodboard\"Advertising1 - Moodboard Creation.json" | Select-Object -First 20
Get-Content .opencode\agents\contenidos.md  # verificar Fase 1 gate
# webfetch https://www.youtube.com/watch?v=cTdHYiD28F4  # shell vacío esperado

# 1. Crear agente (Fase 0):
#   copiar .opencode/agents/vaultworm-arq.md → .opencode/agents/web-researcher.md + añadir websearch: allow
#   editar wiki/glosario/interno/pbooks/pbk-agentes-vaultarq.md + wiki/glosario/software/opencode.md

# 2. Vía A inmediata (sin código):
#   OBS grabar → activos/videos/ytb-2026-09-09-moodboard-recraft-gptimage.mkv
P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/videos/ytb-2026-09-09-moodboard-recraft-gptimage.mkv" --model medium --language en
Get-Content wiki/raw/*ytb*.md

# 2. Vía B nativa (desbloqueo):
P:\Anaconda\envs\comfyenv\python.exe -m pip install yt-dlp youtube-transcript-api
# crear scripts/transcribir_youtube.py (yt-dlp + faster-whisper) → luego:
P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_youtube.py "https://www.youtube.com/watch?v=cTdHYiD28F4" --lang en

# 3. Ingest @contenidos (propone, no escribe sin ¿Avanzo?):
#   @contenidos lee wiki/raw/ytb-*.md + lee n_06/*.json → propone wiki/estudio + conceptos/moodboard (vía @vaultworm-arq) + recraft/gpt-image + normaliza n_06
```

## 6. Criterios de salida / DoD

- `@sherlock` existe + registrado + `websearch: allow` verificable; 1 informe `raw/research/*` bilingüe `ES/EN+IT` con `Metodología: queries por idioma + URLs + status 200 + Bibliografía APA idioma original` sin 404 (`AGENTS.md:97`, `AGENTS.md` HITL).
- AutoCAD: `autocad.md` sin stubs vacíos + URLs `help.autodesk.com/GUID` verificadas + 2 stubs legales con >300 palabras + `tec-capas-autocad.md`.
- ComfyUI: `comfyui.md:538` 6 nodos documentados + `pbk-comfyui.md` flags DirectML/GGUF actualizados + alternativa comercial a `Remacri CC-BY-NC` documentada.
- YouTube: `wiki/raw/ytb-...md` con transcript verbatim + `fuente_binaria` + `fuente_url` + `wiki/estudio/metodologia-moodboard...` + `conceptos/moodboard.md` con `## Conceptos relacionados ≥2` + `## Referencias` 1 oficial +1 externa 200; Vía A OBS default sin `yt-dlp` salvo tu `s`.
- `n_06-moodboard` normalizado `00-README/01-index/02-WF-log/03-nodos/04-backlog/salidas/` + variante local con `ImageScale 512`; selects y salidas referenciadas como `[activos/...]` nunca embebidas; código `scripts/transcribir_youtube.py` + `scripts/transcribir_youtube_notas.md` solo con tu `s` y `# NOTA ES`.
- Índices `wiki/00-index.md`, `wiki/glosario/00-index.md`, `proyectos/MVP_04-comfyui-arquitectura/00-index.md`, `log.md` (entrada nueva arriba `AGENTS.md:81`) actualizados.

## 7. Riesgos y mitigaciones

| Riesgo | Mitigación | Ref |
|---|---|---|
| `webfetch` YouTube sin `yt-dlp` alucina transcript | Usar solo `yt-dlp` auto-sub o `faster-whisper` local; `webfetch` no es fuente | `contenidos.md:39` Nunca inventes |
| Escribir `wiki/glosario/**` directo sin `@vaultworm-arq` | `@contenidos` propone, `@vaultworm-arq` escribe | `pbk-agentes-vaultarq.md:33-38`, `contenidos.md:34` |
| `Remacri CC-BY-NC` en entrega cliente | Documentar alternativa `RealESRGAN_x4plus` BSD | `comfyui.md:392`, `pbk-comfyui.md:161` |
| 20-30 imágenes Pinterest → repo gigante | `/activos/` gitignored, solo refs | `AGENTS.md:7`, `.gitignore:2` |
| Fase 2 sin gate contamina backlog | Respetar `¿Avanzo?` por fase | `contenidos.md:27` |

## 8. Próximos pasos inmediatos

1. Fase 0 DONE — revisar `@sherlock` + `pbk-sherlock.md` conmigo en terminal → ¿Avanzo a Fase 1?
2. Si `s`: piloto `@sherlock` 1A AutoCAD o 1B ComfyUI a elección (como `raw/research/` bilingüe con gate) + Vía A YouTube `cTdHYiD28F4` vía OBS (10min, `AGENTS.md` HITL) en paralelo.
3. Luego Vía B `scripts/transcribir_youtube.py` + `scripts/transcribir_youtube_notas.md` (`# NOTA ES`) solo con tu `s` para dejar YouTube nativo permanente sin riesgo clones.

## Referencias

- `AGENTS.md:7,42-55,97,99,111-113` — binarios en `activos/`, patrón `[activos/...]`, verificar enlaces, HITL código paralelo
- `wiki/glosario/00-index.md:22-30` — 5 reglas calidad glosario
- `wiki/glosario/interno/pbooks/pbk-agentes-vaultarq.md:51-55` + `pbk-sherlock.md` — tabla agentes + dueño glosario + backlog futuro @sherlock
- `.opencode/agents/sherlock.md` — agente GENERAL bilingüe doc-oficial-primero HITL + `pbk-sherlock.md:Backlog`
- `.opencode/agents/contenidos.md:22-28` + `SKILL.md:11-20` — trigger y gate Fase1→Fase2 (PDF/video academia vs investigación general → @sherlock)
- `proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy.md:15-32,76-116` — R1 `512` + estructura WF
- `wiki/glosario/conceptos/vault-visual.md:19-28` + `cerebro-digital-karpathy.md:15-20` — brain visual
- `scripts/transcribir_ghl.py:24-29,66-93,95-139,146-151` + `wiki/glosario/software/obs.md:31-34` — pipeline transcripción (base para `transcribir_youtube.py` + `*_notas.md` didáctico)
- `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/Advertising1 - Moodboard Creation.json:1-968` — flujo Recraft+GPT
- `wiki/glosario/software/autocad.md:150-174,185-188` + `wiki/glosario/software/comfyui.md:538-551` — gaps piloto @sherlock
- `specs/260907-ghl-extraccion-automatica.md` + `specs/260907-vault_cerebro.md` — templates
