---
name: contenidos
description: "Curaduría de contenidos (OBS + PDF/video manual) → reporte raw/contenidos/ legible HITL → wiki/estudio + glosario vía @vaultworm-arq. Se activa con @contenidos. @sherlock solo BUSCA."
---

# Skill contenidos — espejo del agente

> Espejo operativo de `.opencode/agents/contenidos.md`. El agente es la definición viva; este skill es el trigger `@contenidos` + checklist rápida.

## Trigger

`@contenidos`, `@contenidos lee <tema>`, `contenidos procesa <video>`

## Checklist

1. Localizar binario en `activos/videos/<prefijo>-YYYY-MM-DD-<slug>.mkv` o `path manual SOL` (`activos/pdfs/...pdf`); verificar `wiki/raw/*.md` + transcript o normalizar PDF a raw
2. Leer transcript/texto → extraer conceptos, terminología, patrones reutilizables
3. Proponer: a) `wiki/estudio/`, b) glosario (vía `@vaultworm-arq`), c) `pbk-*` si es operativo; multi-tema → N propuestas
4. Generar **siempre** `raw/contenidos/YYYY-MM-DD-<slug>.md` reporte legible (Resumen + Destino wiki + Contenidos extraídos + Ruta+frontmatter + Tags + Referencias 200) — es lo que SOL revisa
5. Reporte → `¿Avanzo a wiki? (s/N)` → si `s`, escribe `wiki/estudio/**` y `pbooks/pbk-*` directo; glosario solo propone a `@vaultworm-arq`
6. FASE 1 = OBS + material manual con invocación explícita (`@contenidos procesa <path>`); búsqueda web PDF/YouTube es de `@sherlock`

## Output contract

- `raw/contenidos/YYYY-MM-DD-<slug>.md` reporte legible HITL (ver `_template.md`) — Resumen + Qué parte wiki + Contenidos extraídos verbatim + Ruta+frontmatter + Tags/wikilinks + Referencias 200 + Gate `¿Avanzo?`
- Propuesta con destino exacto por concepto + Pbook candidato si aplica
- Nota de uso interno en salidas de academia

## Origen

`.opencode/agents/contenidos.md` + `specs/260909-agente-reuniones-fathom-specs.md` (Track C) + `specs/260907-ghl-extraccion-automatica.md`.
