---
tipo: log
fecha: 2026-09-09
sesion: digest-fichas-pbks-singlefile
participantes: [SOL]
tags: [vaultworm-arq, digest, referentes, pbooks, single-file, backlog]
---

# 2026-09-09 — Digest 09-08 + fichas arquitectos + pbks + single-file

## Qué se hizo

- Analizado `raw/vaultworm-arq/digest-2026-09-08.md` con SOL (6 respuestas: todo sí).
- Creadas 9 fichas en `wiki/glosario/referentes/`: bjarke-ingels, patrik-schumacher, shajay-bhooshan, nils-peter-fischer, ulrich-blum, jacob-van-rijs, ben-van-berkel, carlos-banon, fredy-fortich (bio + redes + biblio, URLs verificadas 200 vía 3 subagentes en paralelo).
- Tabla thought-leaders de `ia-estudios-internacionales.md` linkeada a las 9 fichas; `referentes/00-index.md` +9 filas; `big-bjarke-ingels-group.md` + sección Persona (15 socios → big.dk/people).
- Creado `specs/260909-github-actions-agentes-online.md` (estado backlog) — agentes online sin VPS; explícitamente NO en `n8n.md`.
- Fusionados 3 pbks ComfyUI en UNICO `pbooks/pbk-comfyui.md` (base canónica + diagrama + n_03 + catálogo); borrados los 3 viejos.
- Renombrado `pbk-cuentas-git-github-opencode.md` → `pbk-config_ctas_git.md` (contenido intacto).
- Fase A: creados `software/pandoc.md`, `telegram.md`, `n8n.md`; ampliado `opencode.md` (tabla agentes + Subagents + Permissions); índices software/entidades +3 filas.
- Fase B: migradas carpetas legado `software/autocad/` (12 arch) y `software/comfyui/` (modelos+nodos+raíz) a sus `.md` únicos (URLs stubs absorbidas + sección Nodos pendientes); 37 fixes de links en 17 archivos; carpetas borradas.
- Fase C: creado `pbooks/pbk-agentes-vaultarq.md` (fichas vaultworm-arq + brainstormy, comparativa, cómo agregar agente) + sección en índice pbooks.
- Fase F: digest UNICO/día fijado — agent file (formato Estado wiki + Decisiones SOL) + workflow yml sin trigger push (solo schedule 23:00 AR + dispatch).

## Decisiones SOL (resaltadas)

1. Agregar TODOS los conceptos del digest (4/4).
2. UNICO `.md` por software, completar paso a paso.
3. Agentes registrados en pbook (qué son / qué hacen / cómo configurados).
4. Ficha para TODOS los arquitectos mencionados (9, cada uno en `/referentes/`).
5. GitHub Actions = spec/backlog (agentes online sin VPS), NO en n8n; túnel local descartado como infra efímera.
6. UNICO digest/día unificando sesiones + decisiones resaltadas + links bidireccionales.
7. UN solo pbk de COMFY; cuentas → `pbk-config_ctas_git.md`.

## Archivos modificados

- Nuevos (14): 9 referentes + `pandoc.md`, `telegram.md`, `n8n.md`, `pbk-comfyui.md`, `pbk-agentes-vaultarq.md`, `specs/260909-github-actions-agentes-online.md`, esta sesión.
- Renombrado (1): `pbk-config_ctas_git.md`.
- Borrados (3+2 carpetas): 3 pbks viejos + `software/autocad/` + `software/comfyui/`.
- Editados: `referentes/00-index.md`, `ia-estudios-internacionales.md`, `big-bjarke-ingels-group.md`, `software/00-index.md`, `entidades/00-index.md`, `opencode.md`, `autocad.md`, `comfyui.md`, `pbooks/00-index.md`, `.opencode/agents/vaultworm-arq.md`, `.github/workflows/vaultworm-arq.yml`, `specs/260907-vault_cerebro.md`, `scripts/inventario-hardware.ps1`, `AGENTS.md` (§ComfyUI), `wiki/estudio/adr-001-comfyui-mcp.md`, `wiki/estandares/tecnico/00-index.md`, `wiki/glosario/referentes/zha-hadid-architects.md`, `proyectos/STUDIO_OS-Emilia/04-plan-studio-os.md`, 8 archivos MVP_02/MVP_04/n_03, `software/comfyui/00-index.md` (legado, borrado después).
- No tocados a propósito: `log.md`, raw histórico, digests previos, `.obsidian/`.

## Análisis cerebro digital (Karpathy)

- **Topics candidatos a `wiki/glosario/software/`**: ninguno nuevo — pandoc/telegram/n8n/opencode cubren el lote. Próximo lote probable: `runpod`, `leantime` (mencionados en sesiones 09-09 de otro hilo).
- **Entidades**: pandoc, telegram/vaultworm_arqbot, n8n registradas; vaultworm-arq y brainstormy como agentes (pbook, no entidades).
- **Hechos/decisiones reutilizables**: flujo sesión→raw→digest UNICO/día→`¿Avanzo?`→wiki→Estado wiki (Fase F); patrón single-file `.md` con índice interno como norma; mojibake preexistente en `ia-estudios-internacionales.md` / `big-*.md` (`â€"` por `—`) — normalizar solo líneas tocadas.
- **Infra efímera**: scripts `fix-vault-mojo.py` y `migrate-singlefile.py` en TEMP, ya eliminados; túnel n8n/ngrok descartado.
