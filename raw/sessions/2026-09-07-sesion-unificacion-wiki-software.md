---
tipo: log
fecha: 2026-09-07
sesion: unificacion-wiki-software
participantes: [SOL, opencode]
tags: [vault, glosario, restructure, wiki-software, bim, referentes, standares, pbooks]
---

# 2026-09-07 — Sesión unificación wiki/software → wiki/glosario

## Objetivo
Eliminar `wiki/software/` (carpeta obsoleta) y relocalizar todo sin pérdida según regla: **externo → glosario** (conceptos/referentes/software), **propio → glosario/interno** (standares/pbooks). Mantener índices y AGENTS.md coherentes. Standares propios quedan vacíos hasta tener definiciones.

## Qué se hizo

### 1. Relevamiento
- `wiki/software/` contenía 19 archivos: `bim-metodologia.md` (262 líneas), `ia-arquitectura-estudios-internacionales.md` (225 líneas), `comfyui/{00-index,modelos/*,nodos/*,flujos/*,playbooks/*}`, y `glosario/{ffmpeg,faster-whisper,obs,gohighlevel}` duplicado (ruta errónea `wiki/software/glosario/` vs canónica `wiki/glosario/software/`).
- Consultas a SOL: confirmar destino `bim-metodologia` (conceptos), partición `ia-estudios` (global + individuales), y destino `comfyui` (unificar a glosario/software + interno/pbooks).

### 2. Corrección ruta duplicada glosario
- `wiki/software/glosario/{ffmpeg,faster-whisper,obs,gohighlevel}` → `wiki/glosario/software/{ffmpeg,faster-whisper,obs,gohighlevel}` (6 archivos, índices incluidos). Directorios creados, copia y verificación.

### 3. Conceptos (externo)
- `wiki/software/bim-metodologia.md` → `wiki/glosario/conceptos/bim-metodologia.md` — frontmatter `tipo: concepto`, `origen: wiki/software/... → wiki/glosario/conceptos/` (externo, ISO 19650/LOD/CDE).

### 4. Referentes (externo)
- `wiki/software/ia-arquitectura-estudios-internacionales.md` → `wiki/glosario/referentes/ia-estudios-internacionales.md` (global, tipo: referente, lista estudios)
- Creados individuales: `zha-hadid-architects.md`, `big-bjarke-ingels-group.md`, `mvrdv.md`, `foster-partners.md` (cada uno con ubicación/fundación/equipo + cómo usan IA + wikilinks a global + referencias).

### 5. Software + Interno (propio)
- `wiki/software/comfyui/nodos/*` + `modelos/*` + `00-index.md` → `wiki/glosario/software/comfyui/nodos/*` + `modelos/*` + `00-index.md` (merge con `architecture-realmix.md` existente). 6 modelos copiados.
- `wiki/software/comfyui/flujos/00-index.md` → `wiki/glosario/interno/pbooks/pbk-comfyui-flujos-index.md`
- `wiki/software/comfyui/flujos/controlnet.md` → `pbk-comfyui-controlnet.md`
- `wiki/software/comfyui/playbooks/00-index.md` → `wiki/glosario/interno/pbooks/00-index.md`
- `wiki/software/comfyui/playbooks/troubleshooting-reconexion.md` → `pbk-troubleshooting-reconexion.md`
- Creado `wiki/glosario/interno/00-index.md` (tabla standares/pbooks) y `wiki/glosario/interno/standares/00-index.md` (vacío, prefijos tec-/ops- a definir).

### 6. Eliminación y actualización índices
- `Remove-Item wiki/software -Recurse` — verificado `Test-Path == False`
- `AGENTS.md`: estructura vault (6 → glosario 5 ramas), glosario (4 → 5 ramas con interno), esquema `glosario/interno`, workflows integración vault (`wiki/software/comfyui/` → `wiki/glosario/software/comfyui/` + `pbooks/`)
- `00-index.md` y `wiki/00-index.md`: `wiki/software` → `wiki/glosario` (software + conceptos + referentes + entidades + interno)
- `wiki/glosario/00-index.md`: actualizado tabla 5 filas + nota
- `wiki/glosario/software/00-index.md`: añadidos ffmpeg, faster-whisper, obs, gohighlevel
- `wiki/glosario/referentes/00-index.md`: añadidos ia-estudios-internacionales + 4 estudios
- `wiki/glosario/conceptos/00-index.md`: añadido bim-metodologia
- `wiki/glosario/software/comfyui/00-index.md`: flujos/playbooks → pbooks
- Bulk fix 30 archivos con `wiki/software/*` → `wiki/glosario/*` via PowerShell (AGENTS.md, log.md, plan.md, proyectos/MVP_*, wiki/estudio/*, etc.). Verificado `Select-String wiki/software == 0` salvo 1 heading intencional + 1 spec ya corregido.

### 7. Log y encoding
- `log.md` restaurado de HEAD (corrupción UTF8 por Set-Content previo) y reescrito limpio con `default.write` (UTF8). Entrada nueva arriba: `2026-09-07 — Unificación wiki/software → wiki/glosario (elimina carpeta)` con detalle moves + bulk fixes.

## Archivos modificados

- **Movidos:** `wiki/software/bim-metodologia.md` → `wiki/glosario/conceptos/bim-metodologia.md`; `wiki/software/ia-...` → `wiki/glosario/referentes/ia-estudios-internacionales.md` + 4 referentes; `wiki/software/comfyui/nodos/*,modelos/*` → `wiki/glosario/software/comfyui/...`; `wiki/software/comfyui/flujos/*,playbooks/*` → `wiki/glosario/interno/pbooks/pbk-*.md`; `wiki/software/glosario/*` → `wiki/glosario/software/*`
- **Creados:** `wiki/glosario/interno/00-index.md`, `wiki/glosario/interno/standares/00-index.md`, `wiki/glosario/interno/pbooks/00-index.md`, `pbk-comfyui-controlnet.md`, `pbk-comfyui-flujos-index.md`, `pbk-troubleshooting-reconexion.md`, `wiki/glosario/referentes/zha-*.md`, `big-*.md`, `mvrdv.md`, `foster-partners.md`
- **Eliminado:** `wiki/software/` (19 archivos)
- **Actualizados:** `AGENTS.md`, `00-index.md`, `wiki/00-index.md`, `wiki/glosario/00-index.md`, `wiki/glosario/software/00-index.md`, `wiki/glosario/referentes/00-index.md`, `wiki/glosario/conceptos/00-index.md`, `wiki/glosario/software/comfyui/00-index.md`, `log.md`, + 30 archivos bulk fix
- **Sesión:** `raw/sessions/2026-09-07-sesion-unificacion-wiki-software.md` (este archivo)

## Análisis cerebro digital (Karpathy — extrapolación)

### Topics candidatos a `wiki/glosario/software/`

- `bim-metodologia` ya movido → `wiki/glosario/conceptos/bim-metodologia.md` — no es comando, es concepto externo (ISO 19650, LOD, CDE). Referentes: Fred Mills, Gavin Crump, etc. ya documentados.
- `ia-estudios-internacionales` → `wiki/glosario/referentes/ia-estudios-internacionales.md` (global) + 4 estudios individuales — patrón para futuros referentes colectivos (ej. `ia-estudios-latam`).
- `comfyui` nodos/modelos → ya en `wiki/glosario/software/comfyui/` — cada nodo nuevo (ej. `was-node-suite`, `rgthree`) va ahí con `comando: NOMBRE, software: comfyui`.
- `ffmpeg-extract-audio`, `faster-whisper/transcribe`, `obs/captura-pantalla-audio` — ya registrados hoy, sirven como template para futuros tools libres (ej. `whisper.cpp`, `yt-dlp`).
- `gohighlevel` → `wiki/glosario/software/gohighlevel/` — cada término nuevo de transcript GHL (workflow, trigger, pipeline, snapshot) va ahí, no a `conceptos/`.

### Topics candidatos a `wiki/glosario/interno/`

- `standares/` vacío — candidatos futuros: `tec-capas-autocad.md`, `tec-naming-planos.md`, `ops-estructura-carpetas.md`, `ops-template-proyecto.md` (prefijos tec-/ops- a definir con SOL).
- `pbooks/` — `pbk-comfyui-controlnet.md` y `pbk-troubleshooting-reconexion.md` ya migrados — próximos: `pbk-transcribir-ghl.md` (pipeline OBS→faster-whisper), `pbk-ingest-raw-vault.md`.

### Entidades

- Personas: SOL (decisión final vaciar standares), p-31416 (cuenta git)
- Herramientas: `ffmpeg` (GPL), `faster-whisper` (MIT), `OBS Studio` (GPL), `GoHighLevel` (propietario, portal/membership)
- Estudios referentes: ZHA, BIG, MVRDV, Foster + Partners (ya como entidades referentes)
- Vault: `wiki/software/` (obsoleta, eliminada), `wiki/glosario/` (5 ramas), `wiki/estandares/` (espejo operativo, canónica en `glosario/interno/standares/`), `AGENTS.md` (schema actualizado)

### Hechos/decisiones reutilizables

- Decisión: **externo → glosario** (conceptos/referentes/software), **propio → glosario/interno** (standares/pbooks). Regla para todos los futuros ingests (ej. próximo curso GHL: términos externos a `conceptos`/`referentes`, SOPs propios a `pbooks/`).
- Decisión: `wiki/software/` ya no existe — cualquier nueva doc de herramienta va directo a `wiki/glosario/software/<tool>/`, no a `wiki/software/`. Si alguien crea `wiki/software/` por hábito, el lint trimestral (AGENTS.md) lo detectará como huérfano.
- Decisión: `wiki/estandares/` queda como espejo operativo, pero canónica es `wiki/glosario/interno/standares/` — evita duplicar. Índices enlazan entre sí.
- Hecho: bulk fix PowerShell `Replace("wiki/software/glosario/", "wiki/glosario/software/")` + 4 patrones corrigió 30 archivos en una pasada — reutilizable para futuras reestructuras.
- Hecho: `log.md` se corrompió por `Set-Content` sin UTF8 — fix: usar `default.write` (UTF8 nativo) para logs con acentos. No usar PowerShell directo para .md con `→`/`—`.
- Pendiente: standares vacíos — SOL creará `tec-*`/`ops-*` a demanda. No inventar estándares sin fuente.

## Referencias

- `AGENTS.md` (estructura vault, glosario 5 ramas)
- `wiki/glosario/00-index.md`, `wiki/glosario/interno/00-index.md`
- `wiki/software/bim-metodologia.md` (origen, ahora en conceptos)
- `wiki/software/ia-arquitectura-estudios-internacionales.md` (origen, ahora en referentes)
