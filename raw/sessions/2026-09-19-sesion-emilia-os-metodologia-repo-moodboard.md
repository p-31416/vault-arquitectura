---
tipo: log
fecha: 2026-09-19
proyecto: STUDIO_OS-Emilia
participantes: [Sol]
tags: [sesion, studio-os, metodologia, repo-curado, moodboard, bodega, wikilinks, mkdocs, netlify, drive, glosario]
---

# Sesion 2026-09-19 — Emilia OS metodologia + repo curado + moodboard bodega + wiki publish

## Que se hizo

- Conversacion plan-mode (solo lectura/plan): 7 turnos Sol ↔ asistente sobre como compartir carpeta especifica para Emilia sin exponer vault completo.
- Iteracion 1: propuesta repo espejo via `git subtree split -P proyectos/STUDIO_OS-Emilia` → mirror `p-31416/studio-os-emilia` con sync `subtree push`.
- Iteracion 2: refinamiento a repo curado bidireccional (Sol publica curado → Emilia propone via Codex → Sol integra via inbox/PR). Discutido `wiki/` duplicada y `MVP_04` comfy: alternativa submódulo vs scripts sueltos, tradeoffs Codex con repo chico.
- Iteracion 3: decision de mantener `vault-arquitectura` como canonico unico (no duplicar `wiki/glosario/`). Discutido que `activos/` es gitignored (`.gitignore:2`) y fotos van por Drive (`G:\Mi unidad/...` referencia en .md).
- Iteracion 4: foco moodboard bodega + lenguaje grafico CAD. Relevados `n_06-moodboard/WF/WF_v2_moodboard_batch/00-README.md` (batch local DirectML) y `WF_v1_local_Canny_IPA/00-README.md` (Canny 0.31/0.59 CN 0.85, fallback VAEEncode), `reglas-workflows-comfy.md:15` R1 ImageScale 512 y `reglas-workflows-comfy.md:75` estructura WF (`00-README/01-index/02-WF-log/03-nodos/salidas/n_06-B-NN.png/PLANS/SPECS/workflow_*.json`).
- Iteracion 5: evolucion a wiki publish. Verificado `wiki/estudio/analisis/analisis-despliegue-wiki-quartz.md:229` (MkDocs Material + Netlify Identity recomendado vs Quartz + Cloudflare/Vercel/GitHub Pages). Propuesta portal filtrado para Emilia no tecnica: Drive `00-PROYECTOS/EMILIA-BODEGA/01-INPUT-FOTOS/02-SELECTS/03-MOODBOARDS-EXPORT/` + vault referencia + 2 moodboards (bodega referentes + lenguaje grafico CAD → tabla layers/CTB/hatch).
- Iteracion 6: comparativa Netlify ventajas (auth nativo gratis 1k MAU, 15min setup, preview deploys, cero VPS) vs GitHub Pages (publico) vs Cloudflare Basic Auth/worker custom vs Wiki.js VPS $5-10/mes.
- Iteracion 7: auditoria planes existentes: `specs/260910-plan-trimestral-unificado-studio-os-emilia.md` vigente 2026-09-11 (90d Observar/Experimentar/Sistematizar, 180hs 1.800 USD 4 pagos), `specs/260909-moodboard-vault-visual-local.md` (L1 Variation/L2 Alteration local), `specs/260909-esquema-mes1-60hs-studio-os-emilia.md` (Mes 1 60hs 3h/dia, OKRs, milestones M1-M4), `proyectos/STUDIO_OS-Emilia/04-plan-studio-os.md` borrador 2026-08-27 (arquitectura Drive+Vault+Tunel, AS-IS/TO-BE, sprint 30d) — detectado que analisis despliegue es de 2026-07-24 y falta spec de implementacion Netlify filtrado bodega.
- Iteracion 8: pedido de metodologia trabajo Emilia OS (Mes 1 + implementacion). Relevados `ptech-filosofia.md` (capacidad no horas, JR iterable, I+D metodo), `pbooks/00-index.md` (pbk-pm_vault, pbk-comfyui canónicos). Propuesto documento unico `pbk-emilia-os-metodologia` 7 capitulos. Sol aclara: todavia no puede ser pbook, hay que hablarlo y diseñarlo — queda como spec borrador co-diseño en `specs/` con HITL.
- Cierre: paso a build mode, documentacion de sesion presente.

## Archivos modificados

- Ninguno modificado en vault (sesion plan-mode solo lectura/analisis). Solo este `raw/sessions/2026-09-19-sesion-emilia-os-metodologia-repo-moodboard.md` creado en cierre (obligatorio `AGENTS.md`).

## Archivos consultados (lectura)

- `wiki/glosario/interno/standares/oficina/estructura-carpetas.md`, `proyectos/STUDIO_OS-Emilia/00-index.md`, `proyectos/STUDIO_OS-Emilia/04-plan-studio-os.md`, `wiki/glosario/00-index.md`, `proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04.md`, `wiki/00-index.md`, `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/*`, `reglas-workflows-comfy.md`, `proyectos/template_arq/00-index.md`, `proyectos/STUDIO_OS-Emilia/documentacion/checklist-tecnico-emilia-A4.md`, `activos/`, `wiki/estudio/analisis/analisis-despliegue-wiki-quartz.md`, `opencode.json`, `specs/260909-moodboard-vault-visual-local.md`, `specs/260910-plan-trimestral-unificado-studio-os-emilia.md`, `specs/260909-esquema-mes1-60hs-studio-os-emilia.md`, `wiki/glosario/interno/standares/ptech-filosofia.md`, `wiki/glosario/interno/pbooks/00-index.md`, `proyectos/STUDIO_OS-Emilia/presentacion/05-propuesta-comercial-viernes.md`, `plan.md`, `specs/`, `log.md` y globs `**/mkdocs*` `**/quartz*`.

## Pendientes

- [ ] Definir si bodega es `STUDIO_OS-Emilia/casos/bodega-moodboard/` (caso estudio metodologia) o `proyectos/emilia-bodega-mendoza/` (obra real) — impacta template_arq.
- [ ] Acordar indice de metodologia Emilia OS (7 capitulos propuesto) y audiencia: interna operativa vs externa narrativa.
- [ ] Validar portal filtrado: MkDocs Material + Netlify Identity (subset bodega+estandares) vs wiki completa privada 5 personas; hosting Netlify vs Cloudflare/Vercel; dominio.
- [ ] Diseñar spec borrador `specs/260919-plan-metodologia-emilia-os-BORRADOR.md` (no pbook) via 2 sesiones: descubrimiento (dolores, PI local, 2-3 cambios/mes) + ideacion `@brainstormy` → crudo `raw/brainstorm/` → borrador iterativo.
- [ ] Crear estructura Drive `00-PROYECTOS/EMILIA-BODEGA/01-INPUT-FOTOS/02-SELECTS/03-MOODBOARDS-EXPORT/` y adaptar `WF_v2_moodboard_batch` a `workflow_bodega_batch.json` (3 LoadImage Drive + ImageScale 512 lanczos, sin Recraft/GPT pago).
- [ ] Actualizar `260910-plan-trimestral-unificado` §9 demo para apuntar a moodboard bodega Drive + portal, sin duplicar `wiki/glosario/` (wiki-curated read-only si hace falta, Emilia propone en `propuestas/glosario/`).

## Analisis cerebro-digital

**Topics:** Emilia OS metodologia, repo curado vs mirror, vault canonico unico, glosario duplicacion, MVP_04 comfy DirectML, n_06 moodboard L1 Variation L2 Alteration, ImageScale 512 R1, estructura WF 00-README/salidas/n_06-B-NN, Drive CDE fotos, bodega referentes, lenguaje grafico CAD (layers/CTB/hatch), wiki publish MkDocs Material vs Quartz, Netlify Identity auth privado 1k gratis, Cloudflare Workers Basic Auth, plan trimestral 90d 180hs, Mes 1 60hs 3h/dia sprints M1-M4, ptech-filosofia capacidad no horas JR iterable, plan-mode vs build-mode, HITL s.

**Entidades:** Sol (consultora/architecta, vault-arquitectura), Emilia Pimenta (cliente, estudio 2-4, no tecnica), vault-arquitectura (canonico, `p-31416/vault-arquitectura.git`), studio-os-emilia (repo curado futuro), p-31416 (GitHub org), Obsidian (CDE), Google Drive (CDE binarios, `G:\Mi unidad\`), Fathom (Meet→raw/reuniones/), Leantime (VPS Kanban futuro), ComfyUI (`P:\00-repos\ComfyUI` DirectML RX 570 8GB, `--directml 0 --force-fp16`), `ArchitectureRealmix v11` + `Juggernaut XL v9` + `control_v11p_sd15_canny`, Netlify / Cloudflare Pages / Vercel / GitHub Pages / Quartz / MkDocs Material / Wiki.js / Outline, Nayara Alvares Campos Brasil (objeto Mes 1), bodega (caso moodboard), RunPod (entidad futuro escalado), OpenCode Zen + Antigravity + Codex.

**Hechos:** Vault unico sigue en `P:\00-repos\proyecto-pi\vault-arquitectura`; `/activos/` gitignored `.gitignore:2`; `wiki/glosario/00-index.md:22` reglas calidad (2 wikilinks + busqueda web); `reglas-workflows-comfy.md:75` estructura canonica WF; `analisis-despliegue-wiki-quartz.md:102` tabla auth y `l.305` mkdocs.yml base; `260910` vigente 2026-09-11 4 pagos 300/600/600/300 = 1.800 USD, payback mes7 36hs/mes 396hs/año 2.08x; `260909-esquema` 20 dias habiles S1 Vault 15h / S2 Representacion 15h / S3 CAD 15h / S4 Cierre 15h; `04-plan-studio-os.md` borrador 2026-08-27 con Discord vs WhatsApp, Tailscale vs Cloudflare; sesion 2026-09-19 7 turnos plan-mode sin writes, cierre 2026-09-19 build-mode permitido writes, unico archivo creado es esta sesion.

**Conceptos relacionados:** [[wiki/glosario/interno/standares/ptech-filosofia|ptech-filosofia]], [[wiki/glosario/conceptos/vault-visual|vault-visual]], [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]], [[wiki/glosario/conceptos/hitl-human-in-the-loop|hitl-human-in-the-loop]], [[wiki/glosario/conceptos/meta-arquitecto|meta-arquitecto]], [[wiki/glosario/conceptos/okr-goals|okr-goals]], [[wiki/glosario/conceptos/payback|payback]], [[wiki/glosario/interno/standares/oficina/estructura-carpetas|estructura-carpetas]], [[wiki/glosario/software/comfyui|comfyui]], [[wiki/glosario/software/git|git]], [[proyectos/STUDIO_OS-Emilia/00-index|STUDIO OS Emilia]], [[specs/260910-plan-trimestral-unificado-studio-os-emilia|plan trimestral unificado]], [[proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/WF/WF_v2_moodboard_batch/00-README|WF_v2_moodboard_batch]]
