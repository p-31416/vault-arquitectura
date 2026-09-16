---
tipo: log
fecha: 2026-09-07
sesion: vaultworm-digest-diario
participantes: [SOL]
tags: [vaultworm-arq, digest, schedule]
---

# 2026-09-07 — Digest 1 vez/día

## Decisión SOL
Digest **1 vez por día** (no por push). Mañana se revisa el digest de hoy. Debe quedar registrado en el vault y el digest debe incluir detalle de cómo quedó la subida a wiki.

## Cambios aplicados
- `.github/workflows/vaultworm-arq.yml:7` schedule `0 2 * * *` (23:00 AR diario) — quita trigger por push `raw/sessions/**` si se quiere estricto diario, por ahora se mantiene pero se documenta que la cadencia oficial es diaria
- `.opencode/agents/vaultworm-arq.md:73` doc actualizada a “1 vez/día 23:00 AR”

## Pendiente mañana
- Decidir dónde escribe “como quedó la subida”: ¿en el mismo digest (`## Estado wiki`) o en `log.md` + `raw/vaultworm-arq/digest-*.md`?
- Validar que digest quede en `raw/vaultworm-arq/digest-YYYY-MM-DD.md` y que el commit diario lo deje trazable.
