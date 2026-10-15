---
tipo: indice
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [indice, yt, takeout, raw, hitl]
---

# raw/yt — Curación de YouTube y Marcadores

> Pipeline de curación continua de contenido del estudio: YouTube (canales, suscripciones, Watch Later, listas) + Chrome (marcadores sincronizados). Procesa fuentes externas y produce reportes HITL en `raw/contenidos/` y wiki en `wiki/glosario/`. La metodología detallada vive en [[wiki/glosario/interno/metodologia-curacion-youtube|metodologia-curacion-youtube]].

## Estructura

```
raw/yt/
├── 00-index.md                          ← este archivo
├── _template-briefing.md                ← formato del briefing semanal
├── videos-y-canales-guardados.md        ← DOCUMENTO UNICO (lo que tenes que leer)
├── takeout/                             ← (opcional) zip de Takeout extraido aca
├── _preview-2026-10-08/                 ← previews en revision (mover o borrar)
└── briefings/                           ← historial de briefings semanales
    └── YYYY-MM-DD-briefing-yt-semanal.md
```

## Dónde leer

| Quiero ver | Abro |
|---|---|
| **TODO: videos + canales + marcadores** | [[raw/yt/videos-y-canales-guardados|videos-y-canales-guardados]] ← **empezá por acá** |
| **Creadores (suscriptos + solo-WL)** | [[raw/yt/creadores|creadores]] ← 151 canales con veredicto WL |
| Los 44 canales del rubro (curados) | [[wiki/glosario/interno/canales-youtube|canales-youtube]] |
| Los marcadores del navegador (detalle) | [[wiki/glosario/interno/bookmarks-web\|bookmarks-web]] |
| Cómo hacer la API key de YouTube | [[wiki/glosario/interno/youtube-data-api-key\|youtube-data-api-key]] |
| Cómo funciona el sistema | [[wiki/glosario/interno/metodologia-curacion-youtube|metodologia-curacion-youtube]] |
| El formato del briefing semanal | [[raw/yt/_template-briefing\|_template-briefing]] |

## Anatomía del documento único

`videos-y-canales-guardados.md` tiene 4 partes, en este orden:

| Parte | Contenido | Para qué |
|---|---|---|
| **Resumen** | Métricas + top 20 tags de tus videos | Ver de un vistazo de qué tenés material |
| **Parte A** | Los 709 videos agrupados por tus 16 carpetas, con título, canal, duración, fecha, tags y link | Decidir qué ver y qué procesar con `@contenidos` |
| **Parte B** | 113 canales fuera de scope, con link + "Parece ser" + columnas vacías | Tu veredicto: sumar / descartar |
| **Parte C** | 44 canales en scope, resumen por categoría | Referencia |
| **Parte D** | 434 marcadores de Chrome en 36 carpetas | Ordenar páginas útiles |

**Cómo se calculan los tags**: se aplican contra el título del video con límites de
palabra (para que `ar` no matchee dentro de `generar`) y stemming de plurales
(`floor plan` matchea `floor plans`). Si el título no matchea, se usa el nombre de
tu carpeta. Solo queda `sin-clasificar` lo que no tiene tema claro.

**Cómo se calcula la columna Cat**: cada tag pertenece a una de 7 categorías
amplias (`software-arq`, `ia-imagen`, `ia-video-audio`, `ia-agentes-code`,
`construccion`, `diseno-arq`, `gestion`). Sirve para filtrar grueso sin perderse
entre ~40 tags. Detalle en `scripts/yt_takeout_parser_notas.md`.

## Regenerar después de un Takeout nuevo

```
$env:PYTHONIOENCODING="utf-8"
P:\Anaconda\envs\comfyenv\python.exe scripts\yt_takeout_parser.py
```

Lee `scripts/yt_takeout_parser_notas.md` para entender qué hace y cómo ajustar
las keywords de clasificación.

## Cómo se procesa (flujo resumido)

```
Takeout / fuente externa
    ↓
inspección estructura
    ↓
parser categoriza (HITL aprueba)
    ↓
raw/yt/cola-procesamiento.md (videos pendientes)
    ↓
HITL dispara @contenidos por video prioritario
    ↓
raw/contenidos/YYYY-MM-DD-<slug>.md (legible)
    ↓
HITL aprueba → @vaultworm-arq integra a wiki/glosario/**
```

Detalle en [[wiki/glosario/interno/metodologia-curacion-youtube|metodologia-curacion-youtube]].

## Cómo hacer un Takeout nuevo (cuando quieras actualizar)

1. Andá a **https://takeout.google.com**
2. **Desmarcar todo** → tildar solo:
   - ✅ **YouTube and YouTube Music** (exporta suscripciones, playlists, watch later, historial, comentarios, etc.)
   - ✅ **Chrome** → Bookmarks (marcadores sincronizados)
3. Formato de exportación: **JSON** (mejor para parsear)
4. Periodicidad: **cada 3-6 meses** (o cuando lo pidas)
5. Cuando llegue el mail con el link, descargar zip y extraer SOLO las carpetas `YouTube y YouTube Music/` y `Chrome/` en `raw/yt/takeout/`
6. Avisarme con *"listo el takeout"* y arranco el pipeline

## Reglas HITL

- ❌ No se ejecuta `@contenidos` ni `@vaultworm-arq` sin `s` explícito
- ❌ No se sobreescribe `cola-procesamiento.md` (solo se append-ea)
- ✅ Todo cambio en `wiki/glosario/**` requiere `s` separado
- ✅ Categorización se valida por bloques (no todo de una)

## Origen

Sesión 2026-10-08 — definida por el estudio para gestionar la saturación de información de YouTube y Chrome. Decisiones:
- Tipo briefing: híbrido (resumen + detalle)
- Frecuencia: semanal lunes 8 AM
- Destino: vault + Telegram/email (cuando esté en Nivel 2)
- Idiomas: EN + ES mezclado
