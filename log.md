---
tipo: log
fecha_creacion: 2026-06-28
ultima_actualizacion: 2026-09-07
tags: [log, historico]
---

# Log de operaciones

Más nuevo → más arriba

## 2026-09-10 — AGENTS.md slim 393→125 (9 pasos)

- P1 Contexto AR → `wiki/estudio/00-index.md` (sección primera, íntegro); AGENTS 2 líneas.
- P2 Árbol regenerado desde disco → `standares/oficina/estructura-carpetas.md` (template ideal); AGENTS puntero.
- P3 Frontmatter mergeado a `template_arq` (+`ultima_actualizacion`); campo `oficina:` eliminado del spec y de Principios.
- P4 Glosario partido: reglas de calidad → `wiki/glosario/00-index.md`; conducta → `vaultworm-arq.md`; árbol regenerado; AGENTS 2 líneas.
- P5 Ingest/Query/Lint → `pbk-agentes-vaultarq.md` (tasks las corre otro agente, sin duplicar).
- P6 Bloque BIM borrado (rutas sobreviven en `revit.md`/`bim-familias.md`).
- P7 ComfyUI duplicado verbatim borrado (28 líneas ×2 → 2 líneas puntero a `pbk-comfyui`).
- P8 Estructura WF → `reglas-workflows-comfy.md` (sección aparte, sin renombres históricos); Scripts → puntero.
- P9 Estándares unificados en `interno/standares/` (movidas `oficina/`+`tecnico/`, 14 refs retargeteadas, `wiki/estandares/00-index` redirige); 7 refs `AGENTS.md:NNN` vivas → anchors (resto en log/raw intocables); auditoría 268 links → 0 rotos.
- **AFECTA:** `AGENTS.md` (393→125), `wiki/estudio/00-index.md`, `estructura-carpetas.md`, `template_arq/00-index.md`, `glosario/00-index.md`, `vaultworm-arq.md`, `pbk-agentes-vaultarq.md`, `reglas-workflows-comfy.md`, `interno/standares/*`, 7 archivos refs, `log.md`.

## 2026-09-09 — Propuesta viernes: Caso Fundador #01 + HTML + 2 conceptos

- Sesión `@brainstormy` (36 ideas + Top 3 + wildcards, crudo `raw/brainstorm/b-2026_09_09-1.md`): referentes (ZHA A+I, Foster ARD, Hypar, EvolveLAB, Lumera/Elevated/AI50), modelo IA Lab Partnership, portfolio como subsidio, bundle early bird + academia, puesta en escena viernes.
- Propuesta: `proyectos/STUDIO_OS-Emilia/presentacion/04-propuesta-viernes-lab-partnership.md` (Caso #01, sprint 56 hs, 600 fundador, trimestre) + `propuesta-viernes-caso-fundador.html` (scroll + hoja A4 firmable) + esquema `03-propuesta-viernes-esquema.md` desarrollado (desglose hs, tabla mercado, ritmo 2×7h).
- Conceptos nuevos: `wiki/glosario/conceptos/vault-visual.md` + `ia-lab-partnership.md` (+ filas en `conceptos/00-index.md`); entregables en `proyectos/STUDIO_OS-Emilia/00-index.md`.
- Decisiones SOL: piloto Casa masterplan, Drive + mail dedicado, Adapt1 descartado, 15 hs→14 hs/sem (56 hs sprint), ancla mercado 2.500 → fundador 600.
- **AFECTA:** `presentacion/04-propuesta-viernes-lab-partnership.md`, `presentacion/propuesta-viernes-caso-fundador.html`, `presentacion/03-propuesta-viernes-esquema.md`, `wiki/glosario/conceptos/{vault-visual,ia-lab-partnership}.md`, `conceptos/00-index.md`, `proyectos/STUDIO_OS-Emilia/00-index.md`, `log.md`.

## 2026-09-09 — Fathom conectado + 4 reuniones Emilia analizadas (previo propuesta viernes)

- MCP oficial Fathom (`https://api.fathom.ai/mcp`, OAuth) declarado en `opencode.json` y autenticado con cuenta pitau.tech (`mcp list` → connected). Cambio futuro a proyectopi: `logout` + re-auth.
- Descargados transcript + summary + action items de 4 calls 28/08 a `raw/reuniones/2026-08-28-<callid>.md` (~52-59 min c/u): 802902095 (tesis open-source/Adapt1), 802992698 (infra/PCs/Magenta), 803065252 (dashboard/honorarios/piloto Magenta), 803125998 (Vinícola Gema/plan 30 días/valores).
- Análisis simultáneo (4 subagentes en paralelo) → `proyectos/STUDIO_OS-Emilia/reuniones/2026-09-09-analisis-4-reuniones-previo-propuesta.md`: objetivos acordados O1-O6 vs abiertos A1-A7 (valores, alcance F1, piloto único, 2hs/semana, Adapt1, archivos, cobro cambios), mapa N1-N8, señales comerciales y estructura sugerida propuesta viernes.
- Agentes `@fathom-pm` + `@contenidos` creados (`.opencode/agents/`, skills espejo) y registrados en `pbk-agentes-vaultarq.md` + `opencode.md`; `specs/260909-agente-reuniones-fathom-specs.md` en dos tracks; skills importados: deep-research, architecture-decision-records, article-writing, brand-voice, excalidraw-skill.
- **AFECTA:** `opencode.json`, `raw/reuniones/*`, `proyectos/STUDIO_OS-Emilia/reuniones/2026-09-09-analisis-4-reuniones-previo-propuesta.md`, `.opencode/agents/fathom-pm.md`, `.opencode/agents/contenidos.md`, `.opencode/skills/{fathom-pm,contenidos,deep-research,architecture-decision-records,article-writing,brand-voice,excalidraw-skill}/*`, `specs/260909-agente-reuniones-fathom-specs.md`, `pbk-agentes-vaultarq.md`, `opencode.md`, `log.md`.

## 2026-09-09 — Glosario: coautores sprint, design-thinking, dedup SDD, charlas Bañón/Berkel, migración a anchors nativos

- **jake-knapp:** nueva `## El equipo del sprint` (Zeratsky: empezar-por-el-final; Kowitz: story-centered design; Margolis: entrevista 5 actos; Burka: sentido startup) + `## Bibliografía` (*Sprint* S&S 2016 ISBN 9781501121746, *Make Time* Crown 2018 ISBN 9780525572435, *Click*) + fichas S&S/Google Books en Referencias.
- **design-thinking:** reescrito completo (era stub de 5 líneas): origen IDEO+d.school, tabla 5 modos con trampas, 7 mindsets, giro 2016 proceso→habilidades (Carter), traducción a arquitectura. Link viejo Stanford `me113/d.school.html` confirmado 404 → reemplazado por `me113/d_thinking.html`.
- **SDD dedup:** eliminado `wiki/glosario/entidades/sdd-spec_driven_development.md` (SDD es concepto); nota en `entidades/00-index.md` + `conceptos/sdd` §9.
- **ben-van-berkel:** nueva `## The New Understanding (2011)` (Current Work League 1-feb-2011, Cooper Union, modera Stan Allen; tesis post-crisis + 4 tópicos; entrevista Wessner 2-feb) + 3 links archleague/cooper.
- **carlos-banon:** nueva `## NXT BLD 2026` (tesis 3 capas + agency-led workflows + "Form follows you", demo con Yiping Goh) desde fetch de nxtbld.com.
- **Anchors nativos:** índices `[texto](#slug)` → `[[#Encabezado exacto]]` en sdd, kanban, design-thinking, jake-knapp, design-sprint, braintrust-pixar, seguridad-psicologica, marco-creativo, bjarke-ingels, ben-van-berkel, carlos-banon, fredy-fortich; cross-file `[[...#slug]]` → `[[...#Encabezado exacto]]` en sdd. Causa raíz de "links que no andan" en Obsidian.
- **Auditorías:** script scopado `wiki/glosario/**` → 0 absolutos rotos (solo placeholder intencional en template); índices referentes/software verificados fila por fila (todos resuelven); externas verificadas 200 (taschen ×2, kanban.university, epa jitkanban, spec-kit, unstudio, big.dk/people, nxtbld, mvrdv fortich).
- **AFECTA:** `wiki/glosario/referentes/jake-knapp.md`, `ben-van-berkel.md`, `carlos-banon.md`, `bjarke-ingels.md`, `fredy-fortich.md`; `wiki/glosario/conceptos/design-thinking.md`, `sdd-spec_driven_development.md`, `kanban.md`, `design-sprint.md`, `braintrust-pixar.md`, `seguridad-psicologica-aristotle.md`, `marco-creativo-google-pixar.md`; `wiki/glosario/entidades/00-index.md`; `log.md`; `raw/sessions/2026-09-09-sesion-glosario-fixes.md`.

## 2026-09-09 — Marco creativo Google + Pixar (base pitau-tech)

- **Conceptos (4):** nuevas `wiki/glosario/conceptos/design-sprint.md` (GV 5 días + adaptación a anteproyecto), `braintrust-pixar.md` (braintrust + dailies + plussing + ugly babies + braintrust semanal del estudio), `seguridad-psicologica-aristotle.md` (Aristotle + Work Rules + 20% time + libro de obra sin culpa), `marco-creativo-google-pixar.md` (síntesis 5 pilares + traducción a estudio ARG + plan 4 semanas + antipatrones).
- **Referentes (4):** nuevos `wiki/glosario/referentes/google.md` (org, con Bock/Doerr/Edmondson/Buchheit como menciones sin ficha), `pixar-animation-studios.md` (org), `ed-catmull.md` y `jake-knapp.md` (personas). Índices `conceptos/00-index.md` y `referentes/00-index.md` actualizados.
- **Fuentes verificadas:** gv.com/sprint, whatmatters.com (OKR Playbook), hbr.org R0809D, atlassian.com (braintrust), nytimes Aristotle, wikipedia side_project_time, books.google Work Rules, design.google, techcrunch sprint, forbes ugly-babies, mckinsey Catmull, d3.harvard kaizen — todas 200. NO citar: rework.withgoogle.com (404, URL vieja de Aristotle).
- **AFECTA:** `wiki/glosario/conceptos/*`, `wiki/glosario/referentes/*`, índices, `log.md`.

## 2026-09-09 — software/ a UNICO .md (fin carpetas legado)

- Migrados a archivo único navegable: `ffmpeg.md`, `obs.md`, `gohighlevel.md` (6 etapas como secciones) + 6 stubs (`revit, rhino, grasshopper, twinmotion, unreal-engine, impresion-3d`). `autocad.md/comfyui.md/faster-whisper.md` ya cubrían su legado (verificado, sin pérdida).
- Eliminadas 10 carpetas: `faster-whisper ffmpeg gohighlevel obs grasshopper impresion-3d revit rhino twinmotion unreal-engine`.
- Retargets: `opencode.md` → `pbk-config_ctas_git_github_opencode` (nombre truncado roto por renombre); filas `00-index` a singles; `template.md` reescrito a patrón single-file; `AGENTS.md` sin excepción legado.
- Auditoría: 267 links índices → 0 rotos, 0 `../` (restan solo ejemplos en código y placeholders intencionales).
- **AFECTA:** `wiki/glosario/software/*`, `AGENTS.md`, `specs/260907-telegram-vault.md`, `log.md`.

## 2026-09-09 — Regla links agendada en AGENTS.md

- `AGENTS.md` (Nombrado + Glosario regla 6): convención de links obligatoria — entre archivos `[[ruta/desde/raíz|alias]]` sin extensión ni `../`; índice interno `[[#Encabezado exacto]]` (nunca `[texto](#slug)` por tildes); carpetas no se enlazan; excepción portable GitHub `[texto](#slug-ascii)`.
- Motivo: índice de `pbk-config_ctas_git_github_opencode` con slugs a mano no saltaba en Obsidian.
- **AFECTA:** `AGENTS.md`, `log.md`.

## 2026-09-09 — Fix anchors índice pbk-config_ctas (Obsidian)

- Problema: índice superior `[texto](#slug)` no saltaba en Obsidian (2 de 8 anchors con tildes: `verificación`, `conexión`).
- Fix: índice convertido a links nativos Obsidian `[[#Encabezado]]` (resuelven por texto del header, inmunes a slugificación). Wikilinks y URLs externas ya verificados OK.
- Nota: `[[#...]]` no renderiza en GitHub web; se prioriza Obsidian (lector declarado). Si un índice debe ser portable, usar `[texto](#slug-ascii-sin-tildes)`.
- **AFECTA:** `wiki/glosario/interno/pbooks/pbk-config_ctas_git_github_opencode.md`, `log.md`.

## 2026-09-09 — Links rotos restantes resueltos

- `backlog-n_03_WF01.md`: `[[../tests/README]]` → `[[n_02-img2img/tests/README|tests n_02 (referencia)]]` (no existe tests en n_03; se enlaza metodología de tests más cercana con alias explícito).
- Creadas 2 páginas que los specs referenciaban: `proyectos/STUDIO_OS-Emilia/reuniones/2026-09-07-obra-balcarce.md` (andamio minuta Telegram) y `wiki/raw/2026-09-07-ghl-6-etapas-transcripcion.md` (andamio transcript GHL, crea `wiki/raw/`).
- Auditoría final: 298 links en índices → 0 rotos, 0 `../`. Restan solo placeholders intencionales (`[[...]]` en 2 análisis, `otro-referente` en template).
- **AFECTA:** `backlog-n_03_WF01.md`, 2 archivos nuevos, `log.md`.

## 2026-09-09 — Reparación encoding + links de índices

- **Mojibake:** 35 `.md` con `â"œâ"€â"€` reparados a UTF-8 real (`├──`, `—`, `→`, tildes). Causa: UTF-8 leído como cp1252 y re-guardado. `log.md` excluido (inmutable, 78 líneas con mojibake — pendiente decisión).
- **Links:** 297 links de índices auditados → 111 rotos + 8 `[[../]]` → 0. Regla: rutas absolutas desde raíz (`[[wiki/...]]`), sin `../`, sin barras residuales, carpetas como texto o link a su índice.
- **Stubs:** 21 (8 comandos AutoCAD, 6 nodos ComfyUI, 6 índices software, `MVP_04/00-index.md`). **Rename:** `output_log-n_03-WF01.md` → `output_log-n_03_WF01.md`.
- **Pendiente:** `[[../tests/README]]` en backlog n_03 (sin destino), 2 páginas de pipeline por crear (transcript GHL, minuta Balcarce).
- **AFECTA:** 35 `.md` reparados + ~40 con links reescritos + 21 nuevos + `raw/sessions/2026-09-09-sesion-fix-encoding-links.md`, `log.md`.

## 2026-09-09 — PM + ComfyUI + plan semanal (spec vault-cerebro)

- **Mejora continua (9 fichas):** nuevas `wiki/glosario/conceptos/kanban.md`, `agile-arquitectura.md`, `last-planner-system.md`, `kaizen.md`, `retrospectivas.md`, `cinco-s-5s-archivos.md`, `pm-project-management.md`, `okr-goals.md`; `lean.md` ampliado (8 desperdicios del estudio). Índice `conceptos/00-index.md` actualizado.
- **Playbooks:** nuevo `pbk-pm_vault.md` (Leantime: tasks/subtasks/sprints/milestones/GOALS-OKR, Kanban+LPS diario, rituales, MCP futuro) y `pbk-comfyui-arquitectura.md` (canónico: txt2img/img2img/Canny/Depth/otros CN/dual/upscale/video LTX/RunPod/prompt-packs/DoD). Índice `pbooks/00-index.md` actualizado.
- **Spec:** `specs/260907-vault_cerebro.md` suma cuadro maestro Semanas 0–4 + checklist instalación (inventario → OpenCode → Antigravity → Fathom → GH Actions → Leantime → ComfyUI Sol/Emilia) + links a fichas nuevas.
- **Script:** nuevo `scripts/inventario-hardware.ps1` (CPU/RAM/GPU-VRAM real/monitores/discos/red/software/ComfyUI/CAD; salida .md+.json a `raw/sessions/`). Índice `scripts/00-index.md` actualizado.
- **AFECTA:** `wiki/glosario/conceptos/*`, `wiki/glosario/interno/pbooks/*`, `specs/260907-vault_cerebro.md`, `scripts/*`, `log.md`.

## 2026-09-08 — Playbook: Separación y Gestión de Cuentas (Git, GitHub, OpenCode)

- **Nuevo Playbook:** Creado `wiki/glosario/interno/pbooks/pbk-cuentas-git-github-opencode.md` documentando la arquitectura de cuentas segregadas (`proyectopi.31416@gmail.com` vs `pitau.tech@gmail.com`).
- **Detalle de capas:**
  1. Git: Directiva `includeIf` en `.gitconfig`, config condicional y `.git/config` local.
  2. GitHub CLI: Prioridad de `GH_TOKEN` en `.env` vs `hosts.yml`.
  3. OpenCode: Perfiles aislados (`P:\00-repos\.opencode-profiles\proyecto-pi\` vs `pitau\`), rutas de `auth.json`, logs de ejecución y protocolo para uso temporal cruzado (conectar/desconectar con `opencode auth logout`).
- **Índice:** Actualizado `wiki/glosario/interno/pbooks/00-index.md` con categoría *Infraestructura, Cuentas y Entorno*.
- **AFECTA:** `wiki/glosario/interno/pbooks/pbk-cuentas-git-github-opencode.md`, `wiki/glosario/interno/pbooks/00-index.md`, `log.md`.

## 2026-09-08 — CalHon recuperado: MVP_03 Gest + MVP_03b PyDO

- **Recuperado:** `P:\devs\CalHon\` (CalHon — Honorarios CPAU, K=640M ICC junio 2026, Cuadro 5+6 + Clarín ARQ) migrado al vault como **MVP_03b-calhon-pdo** — `proyectos/MVP_03b-calhon-pdo/` con `codigo/` (Vite 8 + React 19 + jsPDF), `docs/` (ADRs/FEATURES/CHANGELOG/PAGOS), `readme-mvp_03b.md`. Origen `P:\devs\CalHon\` queda como respaldo.
- **Renombrado:** `proyectos/MVP_03-calculadora-honorarios` → `proyectos/MVP_03-calhon-gest` (CalHon Gest — honorarios gestiones TAD, curva USD/Oro + CPAU Cuadro 8). `readme-mvp_03.md` actualizado con cross-link a MVP_03b.
- **Índice:** `proyectos/00-index.md:18` ahora lista ambos: `MVP_03-calhon-gest` (gestiones) y `MVP_03b-calhon-pdo` (PyDO + monto de obra).
- **Puertos:** PyDO → `http://localhost:5173` (CalHon — Honorarios CPAU), Gest → `http://localhost:5174` (Calculadora de Honorarios). Verificados 200 OK.
- **AFECTA:** `proyectos/MVP_03-calhon-gest/`, `proyectos/MVP_03b-calhon-pdo/`, `proyectos/00-index.md`, `P:\devs\CalHon\` (origen)

## 2026-09-07 — Sesión cierre: glosario 4 ramas + vaultworm-arq + Telegram

- **Regla glosario:** `AGENTS.md:157` reescrita a 4 ramas `wiki/glosario/software|entidades|referentes|conceptos` â€” toda entrada `wiki/glosario/**` exige `## Conceptos relacionados` â‰¥2 wikilinks + `## Referencias` con bÃºsqueda web verificada + referente en `wiki/glosario/referentes/` si aplica. Estructura actualizada.
- **Referentes:** `wiki/glosario/referentes/00-index.md`, `template.md`, `andrej-karpathy.md` (gist Karpathy + 3 fuentes 200)
- **Renombre:** `bookworm` â†’ `vaultworm-arq` en `raw/vaultworm-arq/`, `.opencode/agents/vaultworm-arq.md` (`@vaultworm-arq`), `.github/workflows/vaultworm-arq.yml`, `.obsidian/workspace.json`
- **Agente:** `.opencode/agents/vaultworm-arq.md` (temp 0.3, rawâ†’digest iterativo) + `raw/vaultworm-arq/digest-2026-09-07.md` (5 topics, entidades, referentes) + workflow push `raw/sessions/**` / lunes 09:00 AR
- **Telegram:** `.env:14` `TELEGRAM_BOT_TOKEN`/`CHAT_ID` para `vaultworm_arqbot` (grupo con Emilia) â€” plan: digest.mdâ†’PDF via pandoc + `sendDocument` + inline âœ…/âœï¸/âŒ, feedback via n8n `getUpdates` â†’ issue/commit
- **SesiÃ³n:** `raw/sessions/2026-09-07-sesion-glosario-vaultworm-arq-telegram.md`
- **AFECTA:** `AGENTS.md`, `wiki/glosario/{00-index,software,conceptos,referentes}/`, `wiki/software/index.md`, `.opencode/agents/vaultworm-arq.md`, `.github/workflows/vaultworm-arq.yml`, `raw/vaultworm-arq/`, `.env`

## 2026-09-07 â€” UnificaciÃ³n wiki/software â†’ wiki/glosario (elimina carpeta)

- **Eliminada:** `wiki/software/` completa (19 archivos). Todo relocalizado sin pÃ©rdida.
- **Conceptos (externo):** `wiki/software/bim-metodologia.md` â†’ `wiki/glosario/conceptos/bim-metodologia.md` (tipo: concepto, origen externo, ISO 19650/LOD/CDE). Propio irÃ¡ a `wiki/glosario/interno/standares/` (tec-/ops-)
- **Referentes (externo):** `wiki/software/ia-arquitectura-estudios-internacionales.md` â†’ `wiki/glosario/referentes/ia-estudios-internacionales.md` (global) + `zha-hadid-architects.md`, `big-bjarke-ingels-group.md`, `mvrdv.md`, `foster-partners.md` (individuales)
- **Software (comandos):** `wiki/software/comfyui/nodos/*` + `modelos/*` â†’ `wiki/glosario/software/comfyui/nodos/*` + `modelos/*` (unificado, arquitectura-realmix conservado). `wiki/software/glosario/{ffmpeg,faster-whisper,obs,gohighlevel}` â†’ `wiki/glosario/software/{...}` (correcciÃ³n ruta duplicada)
- **Interno (propio):** creado `wiki/glosario/interno/` con `standares/00-index.md` (tec-/ops- vacÃ­o, a definir) y `pbooks/00-index.md` + `pbk-comfyui-controlnet.md`, `pbk-comfyui-flujos-index.md`, `pbk-troubleshooting-reconexion.md` (ex- `wiki/software/comfyui/flujos/` y `playbooks/`)
- **Actualizados:** `AGENTS.md` (estructura vault, glosario 5 ramas, esquema interno, workflows), `00-index.md`, `wiki/00-index.md`, `wiki/glosario/00-index.md`, `wiki/glosario/referentes/00-index.md`, `wiki/glosario/conceptos/00-index.md`, `wiki/glosario/software/00-index.md`, `wiki/glosario/software/comfyui/00-index.md`, + bulk fix 30 archivos con `wiki/software/*` â†’ `wiki/glosario/*`
- **VacÃ­a ahora:** `wiki/estandares/` queda para espejo operativo, canÃ³nica es `wiki/glosario/interno/standares/`
- **AFECTA:** 19 moves + 4 creates + 30 bulk fixes, `AGENTS.md`, Ã­ndices

## 2026-09-07 â€” SesiÃ³n GHL transcripciÃ³n â†’ vault automÃ¡tico + cierre

- **SesiÃ³n documentada:** `raw/sessions/2026-09-07-sesion-ghl-transcripcion-vault.md` â€” objetivo: transcribir academia GHL (sin descarga) para alimentar vault sin desperdiciar conocimiento, aplicado a diagnÃ³stico Emilia (ciclo 6 etapas: relevamiento â†’ producciÃ³n)
- **Plan ingest:** `specs/260907-ghl-ingest-6-etapas.md` (captura sin descarga â†’ transcripciÃ³n â†’ raw â†’ vault)
- **Plan automÃ¡tico:** `specs/260907-ghl-extraccion-automatica.md` â€” pipeline `OBS mkv â†’ ffmpeg â†’ faster-whisper (CPU) â†’ wiki/raw/*.md` en 1 comando, resto automÃ¡tico. 100% libre (MIT/Apache, 0 licencia)
- **Script:** `scripts/transcribir_ghl.py` â€” `OBS mkv â†’ ffmpeg extrae mp3 â†’ faster-whisper medium/es/int8 â†’ .txt/.srt + wiki/raw/*.md` con autodetecciÃ³n ffmpeg y reutilizaciÃ³n audio
- **Glosario registrado:** `wiki/glosario/software/ffmpeg/ffmpeg-extract-audio.md`, `wiki/glosario/software/faster-whisper/transcribe.md`, `wiki/glosario/software/obs/captura-pantalla-audio.md`, `wiki/glosario/software/gohighlevel/index.md` (Ã­ndice 6 etapas), + Ã­ndices ffmpeg/faster-whisper/obs
- **PrÃ³ximo paso:** usuario graba primer video con OBS â†’ corre `P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_ghl.py "activos/.../captura.mkv"` â†’ pega `wiki/raw/*.md` â†’ se ejecuta ingest completo (metodologÃ­a + 6 entradas glosario GHL + servicios Pitau Tech + 07-propuesta-diagnostico)
- **AFECTA:** `raw/sessions/2026-09-07-sesion-ghl-transcripcion-vault.md`, `specs/260907-ghl-extraccion-automatica.md`, `scripts/transcribir_ghl.py`, 6 entradas glosario, `proyectos/STUDIO_OS-Emilia/documentacion/`

## 2026-09-07 â€” CorrecciÃ³n Vault Cerebro (ortografÃ­a) + Plan detallado por semanas

- **CorrecciÃ³n:** `vault-cerbero` â†’ `vault-cerebro` en `specs/260907-vault_cerebro.md`, `proyectos/00-index.md` y `proyectos/260907-brain_emilia/00-index.md` + tags normalizados `[vault, cerebro, opencode, fathom, autocad, comfyui, early-bird, academia]`
- **Plan reescrito (240 lÃ­neas, UTF-8):** objetivo para quien reciÃ©n comienza a organizarse (mapeo de procesos + identificaciÃ³n de beneficio IA), uso de IA para scripts Lisp/AutoLISP aunque el estÃ¡ndar no use IA, definiciÃ³n de Cerebro Digital Karpathy aplicado al vault, lean/PM y tÃ©cnicas PM a investigar, MCP Leantime en VPS (pendiente usuario Emilia + URL/pass)
- **Semanas marcadas por puntos:** Semana 1 (miÃ©rcoles conceptual + instalaciÃ³n OpenCode Zen Sol: zen+go / Emilia: zen+openai + Fathom desde Meet â†’ vault con agente + schedule + docu), Semana 2 (casa en construcciÃ³n + referentes web/Instagram/ArchDaily/Pinterest â†’ modelos de visualizaciÃ³n), Semana 3 (flujo ComfyUI posprocesa AutoCAD â€” prueba simple previa a ofrecer), Semana 4 (documentaciÃ³n + clase)
- **Acentos corregidos:** reescritura UTF-8 de `specs/260907-vault_cerebro.md` y `plan.md`
- **AFECTA:** `specs/260907-vault_cerebro.md`, `plan.md`, `proyectos/00-index.md`, `proyectos/260907-brain_emilia/00-index.md`

## 2026-09-07 â€” Cierre sesiÃ³n Vault Cerbero + Brain Emilia (raw/sessions)

- **SesiÃ³n cerrada:** `raw/sessions/2026-09-07-sesion-vault-cerbero-brain-emilia.md` â€” brainstorm IA estudios internacionales (22 ideas + Atelier AutÃ³mata), principios (lenguaje positivo, creatividad con orden), plan Vault Cerbero (Week 1: OpenCode+OpenAI Emilia+Fathom, Week 2: representaciÃ³n Emiliaâ†’Lora/Canny), specs/260907-vault_cerbero, proyecto 260907-brain_emilia, SDD via opencode, 00-index en 36 carpetas, workflow GitHub Actions retirado por SPEC FIRST
- **AFECTA:** `raw/sessions/2026-09-07-sesion-vault-cerbero-brain-emilia.md`, `specs/260907-vault_cerbero.md`, `wiki/glosario/conceptos/sdd-spec_driven_development.md`

## 2026-09-07 â€” SDD Spec-Driven Development + SPEC FIRST

- **Concepto creado:** `[[wiki/glosario/conceptos/sdd-spec_driven_development|sdd-spec_driven_development]]` â€” con Ã­ndice interactivo, Â§1 CÃ³mo se aplica al vault-arquitectura al principio, flujo hÃ­brido Spec Kit + template liviano via opencode, y conexiones con [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]] y [[wiki/glosario/software/opencode/00-index|opencode]]
- **Entidad creada:** `[[wiki/glosario/entidades/sdd-spec_driven_development|sdd (entidad)]]` â€” registry que enlaza al concepto
- **Workflow retirado:** `.github/workflows/opencode-vault.yml` eliminado por crearse sin spec previo â€” se recrea solo tras `âœ“ spec` + `âœ“ plan` (SPEC FIRST)
- **Flujo hÃ­brido validado:** Spec Kit via opencode (`specify init --integration opencode` + `/speckit.*`) + template liviano `specs/YYMMDD-{tema}_*.md` como fuente Ãºnica. Ambas vÃ­as convergen en `/specs/`.
- **Ãndices actualizados:** `wiki/glosario/conceptos/00-index.md`, `wiki/glosario/entidades/00-index.md`
- **AFECTA:** `wiki/glosario/conceptos/sdd-spec_driven_development.md`, `wiki/glosario/entidades/sdd-spec_driven_development.md`, `.github/workflows/opencode-vault.yml` (retirado)

## 2026-09-07 â€” Proyecto 260907-brain_emilia + Vault Cerbero

- **Proyecto creado:** `proyectos/260907-brain_emilia/00-index.md` â€” Vault Cerbero vinculado a `[[specs/260907-vault_cerbero]]` (Plan Vault Cerbero)
- **Spec:** `specs/260907-vault_cerbero.md` â€” Week 1 Vault + OpenCode + OpenAI (cuenta Emilia) + Fathom MCP + schedule cowork, Week 2 representaciÃ³n con Emilia â†’ Lora + Canny, Semanas 3â€“4 Kit AutoCAD documentado. ConvenciÃ³n `YYMMDD-{tema_snake}` activa.
- **Estructura:** `proyectos/260907-brain_emilia/{documentacion,workflows,apps,agentes,reuniones}/` â€” planes solo en `/specs/`, proyecto solo con workflows/apps/docu agentes, linkeado via wikilinks
- **Ãndice actualizado:** `proyectos/00-index.md` â€” entrada 260907-brain_emilia
- **AFECTA:** `specs/260907-vault_cerbero.md`, `proyectos/260907-brain_emilia/00-index.md`, `proyectos/00-index.md`

## 2026-09-07 â€” Plan ingest GHL 6 etapas â†’ vault Pitau Tech (para diagnÃ³stico Emilia)

- **Plan creado:** `specs/260907-ghl-ingest-6-etapas.md` â€” pipeline completo: captura sin descarga (GHL bloquea) â†’ transcripciÃ³n â†’ raw â†’ vault â†’ glosario â†’ servicios Pitau Tech
- **Problema resuelto:** GHL academia no permite descarga directa. Soluciones documentadas: A) ExtensiÃ³n GoHighLevel Downloader (HLS nativo + Wistia/Vimeo/Loom â†’ MP4) [github.com/serpapps/gohighlevel-downloader](https://github.com/serpapps/gohighlevel-downloader) / [Chrome Web Store](https://chromewebstore.google.com/detail/downloader-for-gohighlevel/lcnajelpdoefgoilcihnpkofabpafjgd), B) OBS Studio / Win+Alt+R, C) Audacity WASAPI loopback (solo audio, ideal para vault)
- **TranscripciÃ³n:** `faster-whisper` local CPU (medium) o TurboScribe/WhisperAI en nube â€” sin subir binarios sensibles a wiki (solo refs a `activos/reuniones/ghl-academia/`)
- **Destino vault:** `wiki/raw/` (verbatim) â†’ `wiki/estudio/metodologia-ciclo-6-etapas.md` + `wiki/estudio/servicios-pitau-tech-arquitectura.md` + 6 entradas `wiki/glosario/software/gohighlevel/` + `proyectos/STUDIO_OS-Emilia/documentacion/07-propuesta-diagnostico-emilia-6-etapas.md` (HOY)
- **Mapeo 6 etapas â†’ diagnÃ³stico Emilia:** 1.relevamiento=DiagnÃ³stico Studio OS, 2.analisis=Blueprint TO-BE, 3.implementaciÃ³n=Build mini-prototipo, 4.pruebas=QA interno, 5.entrenamiento=capacitaciÃ³n 30min, 6.producciÃ³n=Go-live + Go/No-Go Fase 2. Sprint 30d USD 600 = etapas 1+2 completas
- **Directorios creados:** `wiki/raw/`, `wiki/glosario/software/gohighlevel/`, `proyectos/STUDIO_OS-Emilia/documentacion/`
- **PrÃ³ximo paso:** usuario pega transcript/audio â†’ se ejecutan Â§5-Â§7 del plan en una vuelta
- **AFECTA:** `specs/260907-ghl-ingest-6-etapas.md`, `wiki/raw/`, `wiki/glosario/software/gohighlevel/`

## 2026-07-28 â€” MigraciÃ³n glosario: proyectos â†’ wiki

- **Movido:** `proyectos/glosario/` â†’ `wiki/glosario/software/` (conocimiento permanente)
- **Eliminado staging:** el glosario ya no tiene fase de staging. Se escribe directamente en la wiki
- **Skill eliminada:** `glosario-sync` ya no es necesaria
- **Actualizados:** todos los wikilinks de `proyectos/glosario/` â†’ `wiki/glosario/software/`
- **AFECTA:** `AGENTS.md`, `index.md`, `proyectos/00-index.md`, `wiki/software/00-index.md`, `proyectos/MVP_02-autocad-standards/*`

## 2026-07-24 â€” Corrida txt2img estadio seed=43 (n_01-C-01)

- **Workflow ejecutado:** `workflow_txt2img_estadio.json` desde API ComfyUI
- **Seed:** 43 (vs seed=42 de baselines A-01/A-02)
- **Output:** `estadio_futbol_00009_.png` â†’ copiado a `proyectos/MVP_04-comfyui-arquitectura/n_01-txt2img/log-WF-estadio/salidas/n_01-C-01.png`
- **DocumentaciÃ³n actualizada:** `prompts-log.md`, `index.md`, `log.md`

## 2026-07-24 â€” Corrida SDXL txt2img estadio seed=42 (n_01-D-01) â€” MIGRACIÃ“N SDXL

- **Workflow ejecutado:** `workflow_txt2img_estadio_sdxl.json` (Juggernaut XL v9)
- **Modelo:** `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` (7.11 GB, SDXL)
- **Seed:** 42 (mismo seed que baseline SD 1.5 A-01/A-02 para comparativa directa)
- **Config SDXL:** steps=35, cfg=4, sampler=dpmpp_2m, scheduler=karras, res=1216Ã—832
- **Flags AMD 8GB:** `--lowvram --cpu-vae --directml 0 --force-fp16 --disable-cuda-malloc`
- **Tiempo:** 561.86s (~9.3 min) en LOW_VRAM mode
- **Output:** `estadio_sdxl_juggernaut_00001_.png` â†’ copiado a `proyectos/MVP_04-comfyui-arquitectura/n_01-txt2img/WF-estadio/salidas/n_01-D-01.png`
- **DocumentaciÃ³n actualizada:** `01-index.md`, `02-WF-log-WFestadio.md`, `PLANS/comparativa-sd15-vs-sdxl.md`, `log.md`
- **Comparativa SD 1.5 vs SDXL:** Primer punto de datos (seed 42) completado para decisiÃ³n migraciÃ³n

## 2026-07-24 â€” Lanzamiento de ComfyUI

- **Servidor ComfyUI iniciado**: Lanzamiento del backend de generaciÃ³n de imÃ¡genes local con GPU AMD RX 570 de 8GB optimizado mediante DirectML y FP16 (`corre_comfyui.bat`) para su uso en el vault.

## 2026-07-19 â€” n_03-controlnet v1.1x: scribble test + DA3 bug + bug log & output log

- **v1.1a.1 interior prompt**: v1.1a_02 revelÃ³ que el prompt exterior (`grandstands, stadium bowl, pitch`) ignoraba la composiciÃ³n del croquis (vista interior del estadio). Fix: prompt reorientado a interior (`stadium interior view, looking up from the pitch, rows of empty seats, steel roof structure overhead`) + strength 0.85 + end 0.85. Backup `BAK_v1.1a.0__scribble.json` creado. Documentado en [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/workflow_log-n_03_WF01|workflow_log-n_03_WF01]]
- **v1.1a scribble test**: Primera corrida `n_03-v1.1a-scribble-01` con ControlNet Scribble directo sobre croquis (~90s)
- **B-002 DA3Inference**: Bug `missing required positional argument: 'mode'` detectado en v1.1b Dual Canny+Depth. SoluciÃ³n: seleccionar `mono` en el widget mode del nodo DA3Inference. Documentado en [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/bug_log-WF_v1.1b_dual|bug_log-WF_v1.1b_dual]]
- **bug_log-WF_v1.1x.md dividido**: Ahora hay bug_log separado por workflow: [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/bug_log-WF_v1.1a_scribble|bug_log-WF_v1.1a_scribble]] (v1.1a Scribble) y [[proyectos/MVP_04-comfyui-arquitectura/n_03-controlnet/n_03-WF01-croquis-estadio/bug_log-WF_v1.1b_dual|bug_log-WF_v1.1b_dual]] (v1.1b Dual). El archivo original quedÃ³ como stub de redirecciÃ³n.
- **output_log-n_03-WF01.md creado**: CatÃ¡logo de todos los outputs organizado por versiÃ³n (1.0, 1.1a, 1.1b) con tabla de parÃ¡metros, outputs y evaluaciones. Prefijos internos: 1.0-index, 1.0-outputs, 1.1a-index, 1.1a-outputs, 1.1b-index, 1.1b-outputs
- **index-n_03_WF01.md actualizado**: Nuevos enlaces a output_log y bug_log

## 2026-06-28

- **CreaciÃ³n del vault**: Estructura inicial creada basada en vault-lidia (Pitautech), adaptada para estudio de arquitectura.
- **Archivos creados**: AGENTS.md, .gitignore, index.md, log.md
- **Directorios**: proyectos/, activos/, bims/, wiki/, legal/, finanzas/, hr/, marketing/, scripts/
- **Template de proyecto**: creado en proyectos/template/

## 2026-06-28 â€” SesiÃ³n con Sol

- **Contexto corregido en AGENTS.md**: PasÃ³ de "estudio internacional multi-oficina" a **contexto argentino real**: oficina en Argentina, equipo remoto nacional, planos como documentos legales (incumbencia profesional Ley 24.335), realidad de obra con papel y celular.
- **ReestructuraciÃ³n profunda del vault**: Se eliminaron todas las carpetas sobrantes de la raÃ­z (`bims/`, `legal/`, `finanzas/`, `hr/`, `marketing/`) y se moviÃ³ su contenido al `wiki/`. La raÃ­z ahora tiene solo: `wiki/`, `proyectos/`, `activos/`, `scripts/`.
- **Nuevo wiki**: 8 secciones â€” practica-profesional, legal, finanzas, estandares (con subsecciones tecnico/ y oficina/), software, estudio, clientes, lecciones-aprendidas. TODO el conocimiento del estudio vive dentro de `wiki/`.
- **`wiki/oficina/` renombrada a `wiki/estudio/`** para evitar confusiÃ³n con `wiki/estandares/oficina/`. `estudio/` contiene escala de decisiones, roles, procedimientos, IT, RRHH.
- **Se eliminÃ³ contenido genÃ©rico internacional** (impuestos UK/DK, GDPR, etc.) y se reemplazÃ³ con contenido especÃ­fico argentino (CPAU, Ley 24.335, IVA/IIBB/Ganancias, cÃ³digos municipales).
- **Perfil de Sol confirmado**: Arquitecta argentina y consultora de IA. Busca centralizar, digitalizar y modernizar la operaciÃ³n del estudio.
- **VisiÃ³n â€” captura desde obra**: Pipeline telÃ©fono/tablet â†’ activos/ â†’ transcripciÃ³n â†’ .md estructurado. Digitalizar el libro de obra en tiempo real.
- **Objetivo de producto**: El vault diseÃ±ado para ser replicable en otros estudios (3ros interesados). Se documentarÃ¡ la metodologÃ­a en `wiki/estudio/metodologia-vault.md` como manual del producto.
- **InvestigaciÃ³n BIM**: Se creÃ³ `wiki/estandares/tecnico/bim-metodologia.md` con investigaciÃ³n completa sobre metodologÃ­a BIM internacional: ISO 19650 (incluyendo revisiÃ³n 2026), LOD Specification 2025, CDE, dimensiones BIM, roles, estÃ¡ndares, recursos multimedia (YouTube, podcasts), thought leaders, y referencias oficiales citadas. GenÃ©rico, sin marca.
- **Movido a wiki/software/**: La pÃ¡gina de metodologÃ­a BIM se moviÃ³ de `estandares/tecnico/` a `software/` por ser mÃ¡s afÃ­n a filosofÃ­a/herramienta que a estÃ¡ndar tÃ©cnico. Se agregÃ³ secciÃ³n "FilosofÃ­a y metodologÃ­a" en el Ã­ndice de software.
- **Secciones aÃ±adidas a bim-metodologia.md**: CDE en la prÃ¡ctica (vault como CDE), y BIM accesible para Argentina (alternativas a Revit: BricsCAD, ArchiCAD, FreeCAD, Blender; CDE sin suscripciÃ³n cloud; flujo hÃ­brido CADâ†’BIM recomendado para estudio ARG).
- **InvestigaciÃ³n IA en estudios internacionales**: Se creÃ³ `wiki/software/ia-arquitectura-estudios-internacionales.md` con investigaciÃ³n detallada sobre cÃ³mo ZHA, BIG, MVRDV, Foster + Partners, UNStudio, Gensler y otros integran IA en sus flujos. Incluye herramientas (Midjourney, Stable Diffusion, D5 Render, NVIDIA Omniverse, CarbonSpace), unidades internas de IA, proyectos destacados (Terminus AI City, IPAI Campus, CODE), fuentes citadas, thought leaders y recursos multimedia.
- **Archivo movido**: `decision-arquitectura-trabajo-ia-privacidad.md` â†’ `wiki/estudio/decision-arquitectura-ia-privacidad.md` (estaba suelto en raÃ­z).
- **activos/ vaciado**: Se eliminaron todos los subdirectorios de plantilla dentro de `activos/`. Cada estudio lo completa segÃºn su estructura.
