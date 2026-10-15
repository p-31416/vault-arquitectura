---
tipo: sesion
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [sesion, yt, takeout, curacion, api, scripts]
---

# 2026-10-08 — Sesión: sistema de curación de YouTube + Chrome

## Qué se hizo

Se diseñó e implementó el sistema de curación de contenido del estudio para resolver
la saturación de información: el estudio tenía 157 canales suscritos y 709 videos
guardados sin ningún orden, y veía menos de la mitad.

**Entrada de datos**: Google Takeout (YouTube + YouTube Music + Chrome), que el
estudio exportó tras recibir las instrucciones de la guía.

## Decisiones HITL del estudio

| Decisión | Valor | Por qué |
|---|---|---|
| Nivel de arranque | Nivel 1 (manual) + Nivel 2 después | Validar el flujo antes de automatizar |
| Datos de entrada | Takeout: YouTube + Chrome | Sin credenciales, todo local |
| Filtrado de canales | Descartar el ruido | 70% de las suscripciones no son del rubro |
| Categorías de canales | 8 categorías de scope | Alineadas con el pedido: arq, software, IA, NFTs, construcción |
| Categorías de videos | Las 16 carpetas del propio estudio | Él ya las tenía hechas, no reimprimir |
| Documento | **Uno solo** con videos + canales + marcadores | Evita saltar entre 6 documentos |
| Doc de review | Tabla de 5 columnas + estado + notas | Que el estudio decida sumar/descartar |
| Briefing (futuro) | Híbrido, semanal lunes 8 AM, vault + Telegram | Formato escaneable en 30s |
| Idiomas de fuentes | EN + ES mezclado | Mayor cobertura técnica en EN, contexto local en ES |

## Flujo technique

```
Takeout (C:\Users\Solch16\Downloads\Takeout)
    ↓
scripts/yt_titles.py          → cache-titulos.json (título+canal+duración)
    ↓                          YouTube Data API v3 · 646/655 · 14 unidades
scripts/yt_takeout_parser.py  → videos-y-canales-guardados.md
    ↓
    ├─ Parte A: 709 videos en 16 carpetas + tags inferidos
    ├─ Parte B: 113 canales fuera de scope (para veredicto del estudio)
    ├─ Parte C: 44 canales en scope
    └─ Parte D: 434 marcadores Chrome en 36 carpetas
```

## Archivos creados

| Archivo | Qué es |
|---|---|
| `raw/yt/videos-y-canales-guardados.md` | **Documento único** (1692 líneas, 197 KB) — el que se lee |
| `raw/yt/00-index.md` | Índice + anatomía del doc + dónde leer |
| `raw/yt/_template-briefing.md` | Formato del briefing semanal (Nivel 2) |
| `raw/yt/cache-titulos.json` | Cache de la API (646 entradas) |
| `scripts/yt_takeout_parser.py` | Parser Takeout → doc único |
| `scripts/yt_takeout_parser_notas.md` | Notas didácticas del parser línea por línea |
| `scripts/yt_titles.py` | Trae título+canal+duración vía API, con cache |
| `wiki/glosario/interno/metodologia-curacion-youtube.md` | Flujo completo y reglas |
| `wiki/glosario/interno/youtube-data-api-key.md` | Guía paso a paso de la API key |

## Bugs resueltos durante la sesión (lecciones)

1. **Encoding del Takeout**: las carpetas traen tilde según el idioma del sistema
   (`listas de reproducción` vs `de reproducción`). Se resolvió con `glob()` por
   patrón en vez de escribir el nombre a mano.

2. **Headers con tilde en CSV**: `csv.DictReader` tiraba `KeyError` porque las
   claves no coincidían con lo escrito a mano. Se resolvió con índices posicionales.

3. **Sufijo `-vídeos`**: el maestro tiene el título de YouTube (`IA/🎨gen_Img`) y el
   archivo tiene `_` en vez de `/` más el sufijo con tilde. Se resolvió con una
   función `_norm()` que normaliza acentos, mayúsculas y sufijo.

4. **Pipes en títulos rompen tablas markdown**: títulos como
   `Beyond the 3D Box with Rhino | S2 E4` partían la tabla en columnas extra.
   Se resolvió escapando como `\|` (296 filas afectadas).

5. **Tags con falsos positivos por substrings**: el tag `ar` matcheaba dentro de
   `generar`/`hacer`, y el 74% de los videos salía con `metaverso`. Se resolvió con
   límites de palabra (`(?<![a-z0-9])...(?![a-z0-9])`).

6. **Contexto de carpeta ignorado**: la mitad de los videos caía en
   `sin-clasificar` porque el título no mencionaba el tema. Se resolvió usando el
   nombre de la carpeta del estudio como contexto y, en último caso, como tag.

## Cerebro digital (topics / entidades / hechos)

### Topics
curación de contenido · vocabulario pasivo · gardeners (mantener el vault podado y
útil) · discovery vs delivery · INFO→ACTION

### Entidades nuevas
- **YouTube Data API v3** — API pública, 10.000 unidades/día, `videos.list` cuesta 1 unidad
- **Google Takeout** — exporta suscripciones, playlists, Watch Later, marcadores
- **RSS de canal** — feed público `youtube.com/feeds/videos.xml?channel_id=` (Nivel 2)
- **n8n CRON** — para automatizar el briefing semanal

### Hechos
- El estudio tiene **157 canales suscritos**; solo **44** son del rubro (28%).
- **709 videos guardados**: 259 en Watch Later + 450 en 15 carpetas temáticas.
- Solo **14 videos** están en Watch Later y también en una carpeta temática (5% de
  solapamiento) → el trabajo de clasificación del estudio está muy fragmentado.
- El etiquetado por substring es **peligroso** en clasificación automática:
  un tag de 2 letras contamina el 74% del corpus.
- La API key de `academia-pi-31416` quedó restringida a YouTube Data API v3 y
  almacenada en `.env` (verificado: `.gitignore:22`, `git check-ignore` la confirma).

## Pendiente para la próxima sesión

1. **Revisión humana de la Parte B**: el estudio completa la columna "Tu veredicto"
   de los 113 canales fuera de scope → se ajustan las keywords del parser.
2. **Procesar videos prioritarios**: con los títulos ya disponibles, elegir 5-10
   videos de Parte A y disparar `@contenidos` sobre ellos.
3. **Nivel 2** (decidir GO/NO-GO): `yt_rss_check.py` + `yt_briefing_gen.py` +
   workflow n8n CRON lunes 8:00 + notificación Telegram.
4. **Limpieza**: `raw/yt/_preview-2026-10-08/` tiene 3 previews superseded por el
   doc único (decidir si se mueven o se descartan).

## Conceptos relacionados

- [[raw/yt/00-index|raw/yt/00-index]] — índice del pipeline
- [[raw/yt/videos-y-canales-guardados|videos-y-canales-guardados]] — el documento único
- [[wiki/glosario/interno/metodologia-curacion-youtube|metodologia-curacion-youtube]]
- [[wiki/glosario/interno/youtube-data-api-key|youtube-data-api-key]]
- [[raw/yt/_template-briefing|_template-briefing]] — formato del briefing semanal
- [[scripts/00-index|scripts/00-index]] — inventario de scripts

---

## Continuacion: tags ampliados + categorias amplias (mismo dia)

El estudio pidio catalogar los 259 Watch Later primero, y cuestiono el bucket de ~150 descartes: la medicion real dio 125 sin-clasificar, y la muestra probo que ~40% de esos eran rescatables (3ds Max, OpenCode, Remotion, floor plans). Conclusion: el diccionario de tags era angosto, no el material descartable.

### Cambios al parser

- 8 tags nuevos: 3dsmax, video-ia, audio-ia, opencode, remotion, dibujo, gestion, whatsapp; +15 keywords en tags existentes (gpt-6, gpt astra, windsurf, copilot, codex, spec-kit, mouredev, quest, vision pro, 3d model, fachada, power bi, notion, leantime).
- Stemming de plurales (`_kw_pat`: singulariza + `s?` opcional). Efecto: floor plans, models, layouts ahora matchean.
- Filtro de fechas (`_es_fecha`): los titulos con fecha adentro ya no generan tags-fecha.
- 7 categorias amplias (`CATEGORIAS_AMPLIAS`) + columna `Cat` en todas las tablas + tabla resumen Por categoria amplia.
- `SLUG_CAT`: mapeo manual de las 16 carpetas a categoria (ej ia-workflowsautom -> ia-agentes-code).

### Efecto medido

- sin-clasificar: 157 -> 131. vibe-coding 9 -> 39. agents 25 -> 41. llm 67 -> 86.
- Por categoria y por fila: ia-agentes-code 196, software-arq 134, ia-imagen 124, diseno-arq 70, construccion 28, ia-video-audio 14, gestion 12, vacio 131.
- Verificacion: 709 filas (259 de 8 col + 450 de 9 col), 113 canales, 0 rotas, 0 mojibake, 40 emojis.

### Pendiente (Fase 1 del plan repriorizado)

1. Generar `raw/yt/triage-watch-later.md` con buckets PROCESAR/REVISAR/DESCARTAR honestos.
2. Veredicto del estudio sobre el descarte real (~50-60, no 150).
3. `raw/yt/catalogo-watch-later.md` con los 259 en estado definitivo + expansion de keywords.
4. Recien despues: homepage `wiki/estudio/noticias/` + edicion piloto.

---

## Revision manual: archivo enfocado (continuacion)

El estudio pregunto como hacer la revision manual sin perderse en el doc de 1710 lineas. Respuesta: un archivo aparte con SOLO lo pendiente.

- Nuevo script `scripts/yt_revision.py`: reusa TAGS/CATS del parser por import (sin duplicar keywords). Genera `raw/yt/revision-manual.md` (300 lineas): Parte 1 = 131 WL sin-clasificar con link clickeable + columna Tu veredicto; Parte 2 = 113 canales fuera con pista + columna Tu veredicto.
- Dos modos de revision: Modo A (editar la tabla en Obsidian y avisar) o Modo B (pasar numeros en el chat).
- Proximo paso tras el veredicto: triage + catalogo final de los 259, despues homepage/ediciones.

---

## Veredictos 1-60 + tags nuevos (continuacion)

El estudio dicto veredictos para los items 1-60 de revision-manual (Parte 1). Distribucion: filosofia 13, otros 22, rescatar 21, descartar 3, proyecto 1. Inferidos por el agente (marcados): 18 y 45 -> otros, 36 -> charlas, 55 -> charlas (TEDx).

### Infraestructura de veredictos

- Nuevo `raw/yt/veredictos.json`: fuente de verdad. El parser (PASO 0b + `aplicar_veredicto()`) lo aplica despues de inferir: un video juzgado no vuelve a sin-clasificar al regenerar.
- Columna veredicto backfilleada en revision-manual para los 60.
- filosofia/personal/otros/proyecto = listados, NO analizados (Cat vacia a proposito). descartar = archivado (sigue en Takeout).

### Tags nuevos y efecto

- 10 tags: magnific, charlas, ai-3d, diagramas, repos, notebook, hardware, arq, filosofia (+keywords en llm/vibe-coding/n8n/nft).
- sin-clasificar 131 -> 62. arq nuevo 118. charlas 20. Verificado 709/709 filas OK, 0 mojibake.
- MAGNIFIC: el video esta en WL #135 (no era el #15 de revision-manual); ya tenia tag upscaling, ahora tiene tag propio.

### Ideas de proyecto detectadas

- davinci-notebook (#14): cuaderno digital tipo Da Vinci con todo. A scafoldear cuando el estudio lo pida.
- repos (#19): extraer links de GitHub de videos (requiere API/transcripts, Nivel 2).

### Pendiente

- Items 61-131 de revision-manual (el estudio sigue desde #61).
- Parte 2 (113 canales): veredicto pendiente.
- Despues: triage + catalogo final 259, homepage/ediciones.

---

## Veredictos 1-60 dictados + tags (continuacion)

El estudio dicto los 60 veredictos de corrido. Distribucion final: filosofia 13, otros 22, rescatar 21, descartar 3, proyecto 1 (+MAGNIFIC WL#135 = 61 en veredictos.json). Columna veredicto backfilleada en revision-manual.

### Decisiones

- filosofia/personal/otros/proyecto/descartado: LISTADOS, no analizados (Cat vacia a proposito).
- charlas: tag + apartado por tag (cruza categorias; los co-tags igual dan Cat). Regla TED: todas las TED/TEDx van en charlas.
- MAGNIFIC: tag propio (soft generacion imagen). El video real es WL#135, no el #15 de revision-manual.
- decentraland: tag propio pedido (sacado de nft).
- davinci-notebook (#14): idea de proyecto registrada, a scafoldear cuando lo pida.
- repos (#19): listar repos interesantes -> Nivel 2 (requiere transcripts).

### Keywords agregadas

- arq: architettura (italiano). llm: ia suelto + gemini bare. vibe-coding: josema. hardware: tecnologia/tecnologico. n8n ya cubria automatica (ARCA).

### Efecto medido

- sin-clasificar 131 -> 51. llm 86 -> 202. Verificado 709/709 filas OK, 113/113 canales OK, 0 mojibake.

### Pendiente

- Items 61-131 (el estudio sigue desde #61). Parte 2 (113 canales). Triage + catalogo final 259. Homepage/ediciones.

---

## Veredictos 61-131 dictados (continuacion)

El estudio dicto del 61 al 131 de corrido. Distribucion de la tanda: rescatar 19, otros 46, descartar 8. Total veredictos.json: 132.

Temas nuevos: gaussian-splatting 61-63 (3D no-IA con repo), video-ia 64/66, charlas 65/83/131, cerebro-digital 67 (llm+notebook), gemma 70, academia 71, herramientas 72, creador 73, notebooklm 75, arq+llm 78, D5 83, Bloomberg/FiloNews 90-91.
Descartes: 68 web, 69 maps, 76 capcut, 77 novedades, 79 Alejavi puntual, 86-88 Xavier/Migue puntuales (keep creators).

Tres conflictos para confirmar (se respeto el dictado): 120 TEDx en bucket personal (vs regla TED->charlas), 121 arq-tech 3D mouse en bucket personal, 110 IA-cuantica en bucket personal 106-111.

Efecto medido: sin-clasificar fuera del top-20 (antes 131). Top: llm 207, arq 119, n8n 90, comfyui 80. Categorias: ia-agentes-code 400, diseno-arq 208, software-arq 160, ia-imagen 133. Verificado 709/709 filas OK, 0 mojibake.

Pendiente: Parte 2 (113 canales). Triage + catalogo final 259. Homepage/ediciones.

---

## Creadores incl. solo-WL (continuacion)

El estudio observo que el planteo de creadores solo con suscriptos (157) dejaba afuera a los creadores descubiertos via Watch Later. Nuevo `scripts/yt_creadores.py` cruza WL (259) con suscripciones: 151 canales distintos, 101 NO suscriptos (Corridor Crew, Kyle Sinko, B:Side, BlessedArch, PixelArtistry, TEDx, DAD, etc.) con veredicto agregado por canal desde veredictos.json.

Salida `raw/yt/creadores.md` (215 lineas): A. 15 suscriptos scope con WL, B. 101 solo-WL con link al video, C. 35 suscriptos fuera con WL. Verificado 50+101 filas OK, 0 mojibake real (los signos de la consola eran render).

Nota: `Psicologia In Depth` y similares se ven con reemplazo en consola PowerShell pero el archivo tiene UTF-8 correcto (verificado por bytes).

---

## Veredictos Parte 2: 47 canales rescatados (continuacion)

El estudio dicto 47 veredictos de canales en dos tandas (39 + 8: bydavidparra, Urban, Ifc Architect, ATELIER, LandSpace, McNeel, ArchiTech, Especialista). Todos rescatar.

Distribucion: arq+IA 14, software arq 16, IA general 5, construccion 4, creadores 3 (TED, Archizoom, DigitalFUTURES), estudios intl. 1 (Schumacher), metaverso 4 (nueva categoria: Spatial, Decentraland, VrPatch, Jacobsen).

Registro en `raw/yt/canales-veredictos.json` (47 IDs conciliados exacto: 0 faltantes, 0 sobrantes). Backfill de las 47 filas en revision-manual Parte 2.

Efecto: scope 44 -> 91, fuera 113 -> 66. creadores.md regenerado (33 scope con WL). Verificado 709/709 filas OK, 0 mojibake.

Bugs corregidos: `tedeschi` capturado por `ted` (fix: keyword en arq+IA, el orden del dict lo prioriza); faltaba `especialista 3d`; `pixeleasel`/`za_lab` con formato exacto; `ifc` auto-incluye a Ifc Architect (correcto).

Pendiente: 66 canales fuera sin veredicto. Triage + catalogo final 259. Homepage/ediciones. Fase B (@contenidos piloto ComfyUI) en espera.

---

## Borrado revision-manual.md (continuacion)

El estudio confirmo que ya reviso todo: se borro `raw/yt/revision-manual.md`. Verificado antes: 132 veredictos de videos + 47 de canales preservados en los JSON (fuente de verdad). El script `yt_revision.py` sigue existiendo y lo regenera si se corre.

---

## Veredictos Parte B creadores 15/16/22/29/80 (continuacion)

El estudio dicto 5 veredictos sobre creadores.md Parte B. Verificacion previa: los 5 ya estaban bien clasificados (15 revit+llm, 16 comfyui+arq+viz, 22 y 29 charlas+arq desde #38/#35, 80 arq+dibujo). Se fijaron igual en veredictos.json para blindarlos (total 135).

Regenerados doc principal + creadores.md (Archi Vlogs/architutors/Rayon pasan a rescatar 1). Verificado sin cambios inesperados.

---

## Indice unico + primer @contenidos (2026-10-09)

Decision del estudio: indice en `wiki/fuentes/index-yt.md` (UN solo archivo, 3 vistas: listado/creador/tag), alcance piloto SOLO comfyui (71 videos). Estado pendiente/procesado via `raw/yt/index-state.json`.

Nuevo `scripts/yt_build_index.py` (filtro por tag, reutiliza parser por import). Generado: 362 lineas, 71 videos, 25 creadores, 17 tags.

Primer @contenidos disparado (video 1: RAMs89SS6cM architutors 10:22): reporte en `raw/contenidos/2026-10-09-comfyui-for-architects-architutors.md` (11,6 KB). Workflow img2img Flux Kontext, tags + workflow:img2img, transcript parcial-via-buscador declarado, alerta VRAM RX570, destino wiki propuesto, gate s/N pendiente. Fila marcada ✅ en las 3 vistas del indice.
