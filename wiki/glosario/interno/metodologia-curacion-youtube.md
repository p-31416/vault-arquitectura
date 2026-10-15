---
tipo: metodologia
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [metodologia, yt, contenido, curacion, sherlock, vaultworm]
---

# Metodología de curación de YouTube y Marcadores

> Sistema del estudio para gestionar la saturación de información de YouTube (canales seguidos, suscripciones, Watch Later, listas temáticas) y marcadores de Chrome. Procesa fuentes externas y produce conocimiento permanente en `wiki/glosario/**` vía los agentes `@sherlock`, `@contenidos` y `@vaultworm-arq`. El estado operativo y los archivos del pipeline viven en [[raw/yt/00-index|raw/yt/00-index]].

## Diagrama de flujo

```
[FUENTES EXTERNAS]
├── Google Takeout (YouTube + Chrome)
├── RSS de canales (Nivel 2: sin API key)
├── YouTube Data API v3 (Nivel 3: con API key)
└── INPUT MANUAL: URL o título pegado por el estudio

        ↓

[PASO 1: INGESTA] — scripts/ o manual
├── parser de Takeout (suscripciones.csv → lista de canales)
├── parser de listas (playlists/*.csv → videos con video_id)
├── parser de Marcadores (Marcadores.html → bookmarks)
└── parser de RSS (Nivel 2)

        ↓

[PASO 2: CATEGORIZACIÓN] — HITL
├── sugerencia automática por keywords (nombre canal, título video, URL)
├── propuesta al estudio: "categoría sugerida para X: arq+software"
└── estudio aprueba/recategoriza por bloque

        ↓

[PASO 3: INDEXACIÓN EN VAULT]
├── raw/yt/canales-youtube.md (lista curada de canales)
├── raw/yt/cola-procesamiento.md (videos pendientes)
├── raw/yt/bookmarks-web.md (bookmarks categorizados)
└── raw/yt/briefings/YYYY-MM-DD-briefing-yt-semanal.md (semanal)

        ↓

[PASO 4: PROCESAMIENTO POR VIDEO] — bajo demanda
├── estudio dispara: "@contenidos procesa <video_id o URL>"
├── @contenidos lee el video (Whisper local o YouTube transcript)
├── @contenidos extrae conceptos, terminología, patrones
├── @contenidos escribe raw/contenidos/YYYY-MM-DD-<slug>.md
│
└── HITL: "¿Avanzo a wiki? s/N"

        ↓

[PASO 5: INVESTIGACIÓN PROFUNDA] — bajo demanda
├── estudio dispara: "@sherlock <tema>" o "@deep-research <tema>"
├── @sherlock busca 2-3 variaciones × sub-pregunta (15-30 fuentes)
├── @sherlock verifica cada URL (sin 404)
├── @sherlock escribe raw/research/YYYY-MM-DD-<slug>.md
│
└── HITL: "¿Avanzo a curaduría? s/N" → @contenidos procesa

        ↓

[PASO 6: INTEGRACIÓN A WIKI] — solo @vaultworm-arq
├── @vaultworm-arq toma raw/contenidos/YYYY-MM-DD-<slug>.md
├── @vaultworm-arq identifica destino:
│   ├── concepto nuevo → wiki/glosario/conceptos/**
│   ├── software → wiki/glosario/software/**
│   ├── referente (persona) → wiki/glosario/referentes/**
│   ├── referente (estudio) → wiki/glosario/entidades/**
│   └── metodología operativa → wiki/glosario/interno/**
├── @vaultworm-arq escribe con frontmatter + wikilinks
│
└── HITL final: ya está en wiki (revisión manual cuando quiera)

        ↓

[PASO 7: BRIEFING SEMANAL] — automático en Nivel 2
├── n8n CRON lunes 8:00 ART
├── n8n descarga RSS / Takeout actualizado
├── @sherlock genera raw/yt/briefings/YYYY-MM-DD-briefing-yt-semanal.md
├── n8n manda copia por Telegram/email (bot configurado)
└── estudio revisa cuando toma el café del lunes
```

## Los 3 agentes y sus roles

### `@sherlock` (investigación)
- **Trigger**: "investiga X", "research Y", "qué hay de nuevo sobre Z"
- **Modo**: solo busca, no escribe en wiki
- **Salida**: `raw/research/YYYY-MM-DD-<slug>.md` con fuentes verificadas
- **HITL**: pregunta "¿Avanzo a curaduría? s/N" antes de pasar a `@contenidos`

### `@contenidos` (procesamiento de material)
- **Trigger**: "@contenidos procesa <URL/video_id/tema>", o post-`@sherlock` con `s`
- **Modo**: lee, extrae, resume; escribe reporte legible
- **Salida**: `raw/contenidos/YYYY-MM-DD-<slug>.md` (con Resumen + Contenidos extraídos + Destino wiki propuesto + Tags + Gate)
- **HITL**: pregunta "¿Avanzo a wiki? s/N" antes de pasar a `@vaultworm-arq`

### `@vaultworm-arq` (integración al vault)
- **Trigger**: post-`@contenidos` con `s`, o "@vaultworm-arq digest" para sesión
- **Modo**: lee `raw/contenidos/`, decide destino en `wiki/glosario/**`, escribe con frontmatter + wikilinks
- **Salida**: archivos nuevos en `wiki/glosario/{software,conceptos,referentes,entidades,interno}/**`
- **HITL**: revisa cuando quiera en el vault, propone ajustes

## Reglas del sistema

### 1. Categorías base (provisorias, ajustables HITL)

| Categoría | Keywords típicas | Destino wiki |
|---|---|---|
| `arq+IA` | "comfyui arquitectura", "AI architect", "Stable Diffusion arquitectura" | conceptos/software |
| `software arq` | "Rhino", "Revit", "Grasshopper", "Twinmotion", "Unreal Engine arquitectura", "FreeCAD" | software |
| `estudios intl.` | "BIG", "ZHA", "OMA", "Foster", "Renzo Piano", "MAD architects" | entidades/referentes |
| `IA general` | "LLM", "GPT", "diffusion models", "transformer" | conceptos/software |
| `NFTs/tokens` | "NFT architecture", "tokenización", "blockchain arquitectura" | conceptos |
| `construcción` | "construction tech", "3D print building", "materiales", "BIM" | conceptos/software |
| `creadores` | canales individuales de divulgación arq | referentes |
| `noticias intl.` | "architecture news", "Dezeen", "ArchDaily" | conceptos |
| `mkt/seo` | listas con prefijo `??MKT??` | (categoría del estudio, mantener) |
| `libros` | listas con prefijo `libros` | referentes |

### 2. Niveles de automatización

- **Nivel 1 (actual)**: manual, sin código. Estudio dispara agentes uno a uno.
- **Nivel 2 (próximo)**: n8n CRON + RSS + scripts Python. Briefing semanal automático, parser de Takeout.
- **Nivel 3 (futuro)**: YouTube Data API v3 + yt-dlp + Whisper local. Detección de videos nuevos en tiempo real.

### 3. Convenciones de archivos

- Nombres: `snake-case` con prefijo de fecha `YYYY-MM-DD-`
- Encoding: UTF-8 siempre (parser normaliza los `T��tulo` → `Título` y emojis `??` → emoji real)
- Frontmatter obligatorio en wiki
- Wikilinks formato Obsidian: `[[wiki/glosario/software/git|Git]]` (sin extensión, ruta absoluta desde raíz)

### 4. Calidad (reglas de [[AGENTS|AGENTS.md]] que aplican)

- ✅ Toda afirmación en wiki con fuente verificada (no 404)
- ✅ Citas a manuales oficiales primero, después fuentes externas
- ✅ Lenguaje en positivo
- ❌ No se copia contenido de binarios al vault
- ❌ No se inventan URLs ni cifras

## Estado actual (2026-10-08)

- ✅ Pipeline manual definido
- ✅ 3 archivos del sistema creados ([[raw/yt/00-index|raw/yt/00-index]] · [[raw/yt/_template-briefing|_template-briefing]] · esta página)
- ✅ Takeout recibido en `C:\Users\Solch16\Downloads\Takeout`
- ⏳ Parser de Takeout pendiente (Nivel 2)
- ⏳ n8n CRON pendiente (Nivel 2)
- ⏳ Telegram bot pendiente (Nivel 2)

## Próximos pasos

1. Mini-dry-run del parser con muestra de Takeout (5 canales + 3 bookmarks)
2. HITL aprueba la lógica de categorización
3. Crear `canales-youtube.md` + `bookmarks-web.md` + `cola-procesamiento.md` con datos reales
4. Procesar manualmente los 5-10 videos prioritarios de Watch Later
5. Decisión GO/NO-GO a Nivel 2

## Conceptos relacionados

- [[wiki/glosario/interno/canales-youtube|canales-youtube]] — lista curada de canales
- [[wiki/glosario/interno/bookmarks-web|bookmarks-web]] — marcadores categorizados
- [[raw/yt/00-index|raw/yt/00-index]] — estado operativo del pipeline
- [[raw/yt/_template-briefing|raw/yt/_template-briefing]] — formato del briefing semanal
- [[wiki/glosario/interno/standares/pbk-agentes-vaultarq|pbk-agentes-vaultarq]] — playbook de los 3 agentes
- [[AGENTS|AGENTS.md]] — reglas globales del vault
- [[wiki/glosario/interno/standares/oficina/estructura-carpetas|estructura-carpetas]] — árbol canónico
