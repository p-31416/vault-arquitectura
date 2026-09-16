# Sesión 2026-09-09 — Reparación encoding + links de índices

## Qué se hizo

- **Mojibake UTF-8/cp1252:** 35 `.md` reparados (`├──`, `—`, `→`, tildes restaurados). Causa: archivos guardados con UTF-8 leído como Windows-1252 y re-guardado. Script `C:\Users\Solch16\AppData\Local\Temp\opencode\fix_mojibake.py` (ftfy-lite: solo repara ventanas que decodifican a UTF-8 válido, texto correcto intacto). `log.md` (78 líneas con mojibake) excluido por regla de inmutabilidad — pendiente decisión Sol.
- **Links índices:** auditoría 297 links → 111 rotos + 8 `../` → **0 rotos, 0 `../`**. Script `fix_links.py`: relativos→absolutos desde raíz, barras residuales, renombres (MVP_03-calculadora→calhon-gest, template→template_arq, playbooks→pbooks/pbk-*), typo `vault_cerbero`→`cerebro` (solo docs vivos, no log/raw).
- **21 stubs creados:** 8 comandos AutoCAD, 6 nodos ComfyUI base, 6 índices software (revit/rhino/grasshopper/twinmotion/unreal/impresion-3d), `MVP_04/00-index.md`.
- **1 rename:** `output_log-n_03-WF01.md` → `output_log-n_03_WF01.md` (convención familia + link existente).
- Regla adoptada: todo wikilink path-like = ruta absoluta desde raíz sin extensión (`[[wiki/...]]`, `[[proyectos/...]]`, `[[specs/...]]`); `[[../]]` prohibido (Obsidian no lo resuelve); carpetas no se enlazan (texto plano o link a su índice).

## Ronda 2 — rotos restantes resueltos (pedido Sol)

- `[[../tests/README]]` → `n_02-img2img/tests/README` con alias aclaratorio.
- Minuta Balcarce + transcript GHL creados como andamios ⏳ con origen.
- Final: 298 links en índices → 0 rotos, 0 `../`. Solo placeholders intencionales.
- Pendiente único: `log.md` (mojibake 78 líneas + links viejos `cerbero`/pre-renombre) — inmutable, requiere decisión explícita.

## Pendientes / decisiones para Sol (ronda 1)

1. `log.md`: 78 líneas con mojibake — ¿reparo mecánico (no cambia contenido) o se deja por inmutabilidad?
2. `[[../tests/README]]` en `n_03-WF01-croquis-estadio/backlog-n_03_WF01.md`: no existe tests en n_03 — ¿apuntar a `n_02-img2img/tests/README` o quitar?
3. Faltan por crear (pipeline, no stubs): `wiki/raw/2026-09-07-ghl-6-etapas-transcripcion.md` y `proyectos/STUDIO_OS-Emilia/reuniones/2026-09-07-obra-balcarce.md` (los specs los referencian).
4. Intencionales sin tocar: `[[...]]` en 2 análisis, `[[otro-referente]]` en template, typo `cerbero` en log/raw (verbatim).

## Análisis cerebro digital (Karpathy)

- **Topics candidatos a software:** ninguno nuevo (los 6 nodos ComfyUI ya tienen ficha; comandos AutoCAD son stubs).
- **Entidades:** — (sesión técnica, sin nuevas).
- **Hechos/decisiones:** regla de links absolutos (arriba) → proponer como estándar en `AGENTS.md` (convención wikilinks); scripts de reparación quedan en Temp opencode, no en el vault.
