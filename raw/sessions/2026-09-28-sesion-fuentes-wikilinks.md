---
fecha: 2026-09-28
herramientas: [opencode]
---

# Sesión 2026-09-28 — Fuentes con wikilinks en autocad-documento-maestro

## Qué se hizo

1. **Diagnóstico del reclamo**: en `raw/docs/autocad-documento-maestro.md` los `[^n]` aparecían como links pero caían en fuentes equivocadas. Causa raíz: el consolidado unió 5 archivos con numeración `[^n]` propia; el contenido copiado del Kit (`### 3.2 Principios de diseño del kit` + `## 4 SETs`) conservaba numeración Kit (`[^1]`–`[^40]`) que colisionaba con la del master (`[^1]`–`[^67]`). Caso testigo: `[^39]` junto a "Autodesk Assistant" saltaba a la def `[^39]` = reglamentación AEA; la fuente verdadera es `[^104]`.
2. **Hallazgo de entorno**: el plugin central de footnotes estaba en `"footnotes": false` en `.obsidian/core-plugins.json`; la usuaria lo activó (quedó `true`) pero ni un archivo mínimo de prueba renderizaba navegación ni el panel "Notas al pie" listaba nada. Decisión: no depender del plugin.
3. **Reemplazo de notación** (aprobado por la usuaria): cuerpo `[^64]` → `[[#^f64|64]]` (en tablas `\|` escapado) + ancla `^fN` al final de cada una de las 105 definiciones en `## 15. Fuentes`. Motor de links de Obsidian, el mismo del Índice.
4. **Mapeo validado por URL** en `scripts/convert-fuentes-wikilinks.py` (con `# NOTA ES:` línea a línea): cada ref del Kit se cotejó contra el Kit original por URL exacta; aborta sin escribir si algo no cuadra. El primer intento (`n→n+67`) abortó correctamente al detectar corrimientos (ej: Kit `[^5]`=Wikipedia vs `[^72]`=iTeh). La v2 deriva el destino buscando la URL entre las 105 definiciones y coteja que las frases de la sección 4 existan en el cuerpo del Kit.
5. **Correcciones aplicadas por el script**: `39→104` (Assistant), `40→105` (Wiley), desfases `5→71`, `10→72`, `12→78`, `13→79`, `16→82`, `21→87`, `24→89`, `25→90`, `26→91`, `27→92`, `28→93`, `29→94`, entre otros. Reporte final: 103 refs convertidas, 105 anclas, cero `[^n]` sueltos en cuerpo, cero alias sin ancla, índice intacto.
6. **Ajuste manual**: línea 199 (frase fusionada que el guarda omitió): niveles→`79` (UNLP, Kit `[^13]` verificado en Kit línea 101), muros curvos→`78` (UNaM, Kit `[^12]` verificado en Kit línea 102).
7. **Verificación semántica manual**: tablas 4.1 (NCS→68/70, ISO→71/72, AEC→73/74) y 4.10 + §3.2 completa contra definiciones del Kit original. Todo cierra.
8. **Limpieza**: borrado `raw/docs/__test-footnotes.md` (test mínimo, cumplió su rol).

## Archivos modificados
- `raw/docs/autocad-documento-maestro.md` — conversión de notación + destinos corregidos (único archivo de contenido tocado).
- `scripts/convert-fuentes-wikilinks.py` — NUEVO, runnable con NOTA ES, autovalidante (aborta sin escribir ante mismatch).
- `scripts/check-footnotes.py`, `scripts/renumber-footnotes.py` — apoyo de un solo uso (renumber dejó deuda: línea 63 con bug de ordenamiento; solo afecta su propio reporte, no el documento).
- `raw/docs/__test-footnotes.md` — creado y luego borrado.
- `.obsidian/core-plugins.json` — cambio por UI de la usuaria (`footnotes: true`).
- `raw/sessions/2026-09-27-sesion-fix-indices-wiki.md` — apéndice con esta continuación.
- `raw/sessions/2026-09-28-sesion-fuentes-wikilinks.md` — este archivo.

## Análisis cerebro-digital
- **Topics**: Obsidian block-references (`[[#^id|alias]]`) como sustituto robusto de footnotes; validación de mapeos por URL exacta en consolidaciones; tablas markdown + escapes `\|` en wikilinks; guardas de frase para no tocar contenido ajeno.
- **Entidades**: documento maestro AutoCAD (550 líneas, 105 fuentes), Kit temático SETs (40 fuentes propias), Assistant 2027 (`^f104`), Wiley Layer Translator (`^f105`), CAPBA/GCBA/AEA/AySA (municipal).
- **Hechos**: el plugin footnotes no responde en este vault aun activado; la numeración colisionada producía destinos cruzados silenciosos; la conversión a wikilinks fue verificada occurrence por occurrence y confirmada funcional por la usuaria en Vista de Lectura.
