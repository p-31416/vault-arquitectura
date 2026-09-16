# Sesión 2026-09-09 — PM/Lean + ComfyUI extensivo + plan semanal vault-cerebro

## Qué se hizo

- Investigación mejora continua (Lean, Kanban, Agile-arq, LPS, Kaizen/PDCA, 5S, retros, PM, OKR, Leantime) + ComfyUI (Canny/Depth/img2img/video/RunPod) con fuentes verificadas (LCI, Kanban University, Agile Manifesto, EPA-5S, Procore, Leantime.io/GitHub, docs.comfy.org, RunPod, arxiv ControlNet).
- 9 fichas en `wiki/glosario/conceptos/` (8 nuevas + `lean.md` ampliado), cada una con índice interno, ≥2 wikilinks, referencias verificadas.
- 2 playbooks: `pbk-pm_vault` (operativa Leantime en el vault) y `pbk-comfyui-arquitectura` (canónico ComfyUI).
- `specs/260907-vault_cerebro.md`: cuadro maestro Semanas 0–4 + checklist instalación (Antigravity, OpenCode, Fathom, MCPs, ComfyUI, Emilia local/RunPod).
- Script `scripts/inventario-hardware.ps1` (primero de todo: correr en Semana 0 en ambas PCs).
- Actualizados índices (conceptos, pbooks, scripts) + `log.md` (entrada nueva arriba).

## Archivos modificados/creados

- `scripts/inventario-hardware.ps1` (nuevo) + `scripts/00-index.md`
- `wiki/glosario/conceptos/kanban.md`, `agile-arquitectura.md`, `last-planner-system.md`, `kaizen.md`, `retrospectivas.md`, `cinco-s-5s-archivos.md`, `pm-project-management.md`, `okr-goals.md` (nuevos); `lean.md`, `00-index.md`
- `wiki/glosario/interno/pbooks/pbk-pm_vault.md`, `pbk-comfyui-arquitectura.md` (nuevos); `00-index.md`
- `specs/260907-vault_cerebro.md`, `log.md`, este archivo

## Análisis cerebro digital (Karpathy)

- **Topics candidatos a software:** `leantime` (operativa Tasks/Sprints/Milestones/Goals como herramienta), `antigravity` (IDE), `fathom` (transcripción Meet) — evaluar fichas `wiki/glosario/software/leantime.md` etc. en próxima sesión.
- **Entidades:** Emilia (usuaria early-bird, PC por relevar aptitud ComfyUI), Sol (gestora), 2 estudios early bird, VPS Leantime, PC Sol/RX 570, RunPod (proveedor cloud GPU).
- **Hechos/decisiones reutilizables:** regla aptitud (RAM≥16+VRAM≥6=local SD1.5; iGPU=RunPod); orden instalación estricto (inventario→OpenCode→Antigravity→Fathom→GH→Leantime→ComfyUI); OKRs propuestos O1/O2/O3; DoD renders `n_XX-{A–F}`; CC-BY-NC nunca a cliente. **Efímero:** rate-limit 429 del buscador durante la sesión (reintentado con éxito parcial); URL re:Work Google muerta (se usó Atlassian/whatmatters en su lugar).
