---
tipo: metodologia
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-09
tags: [pitau-tech, ghl, transcripcion, ingest, studio-os, emilia, diagnostico]
origen: GHL Academia - Ciclo 6 etapas (1. relevamiento 2. analisis-diseno 3. implementacion 4. pruebas 5. entrenamiento 6. produccion)
estado: plan
---

# Plan — Ingest GHL 6 etapas → Vault → Servicios Pitau Tech (para diagnóstico Emilia)

> **Objetivo HOY:** definir la propuesta de **diagnóstico** para Emilia (asociada estudio grande) usando el ciclo de 6 etapas de GHL, transcrito sin descarga directa, y alimentar el vault sin desperdigar conocimiento.

## 0. Resumen en 1 línea

Capturar audio de la academia GHL (sin botón de descarga) → transcribir local → guardar **raw** en `wiki/raw/` → procesar en **3 salidas**: a) metodología genérica, b) glosario, c) documento de servicios Pitau Tech para estudios de arquitectura → aplicar a propuesta diagnóstico Emilia.

## 1. Por qué no va a `wiki/software`

`wiki/software` es para herramientas (Revit, ComfyUI). Este conocimiento es **metodología de implementación** — transversala a Pitau Tech. Por eso vive en:
- `wiki/raw/` → evidencia cruda
- `wiki/estudio/` → metodología y servicios
- `wiki/glosario/software/gohighlevel/` → términos puntuales de GHL
- `proyectos/STUDIO_OS-Emilia/` → propuesta cliente

## 2. Arquitectura de archivos (destino final)

```
vault-arquitectura/
├── activos/videos/                        # BINARIOS gitignored, carpeta única por prefijo+fecha (ej. ghl-YYYY-MM-DD-*.mp3)
│   └── ghl-2026-09-07-6-etapas-relevamiento-a-produccion.mp3
│
├── wiki/raw/                                # RAW — transcripción verbatim
│   └── 2026-09-07-ghl-6-etapas-transcripcion.md
│
├── wiki/estudio/                            # PROCESADO — conocimiento permanente
│   ├── metodologia-ciclo-6-etapas.md        # ciclo genérico Pitau Tech (sin marca GHL)
│   └── servicios-pitau-tech-arquitectura.md # cómo aplica cada etapa a estudios ARG
│
├── wiki/glosario/software/gohighlevel/      # GLOSARIO — 6 entradas
│   ├── relevamiento-requerimientos.md
│   ├── analisis-diseno-solucion.md
│   ├── implementacion-tecnica.md
│   ├── pruebas-internas.md
│   ├── entrenamiento-agentes.md
│   └── puesta-produccion.md
│
└── proyectos/STUDIO_OS-Emilia/
    ├── index.md                             # actualizar fase: briefing → diagnostico
    └── documentacion/
        ├── 06-plan-ingest-ghl-6-etapas.md   # â† este plan
        └── 07-propuesta-diagnostico-emilia-6-etapas.md  # propuesta HOY (a crear tras ingest)
```

## 3. Paso 1 — Captura sin descarga (GHL bloquea el download)

GHL no expone botón de descarga en portals/memberships (HLS nativo + embeds Wistia/Vimeo/Loom). Tres opciones, en orden de preferencia:

### 3.1 Opción A — Extensión GoHighLevel Downloader (recomendada, 2 min)
- **Qué es:** extensión Chrome/Edge/Brave que detecta el stream aunque esté bloqueado [github.com/serpapps/gohighlevel-downloader](https://github.com/serpapps/gohighlevel-downloader) — soporta HLS nativo + Wistia/Vimeo/Loom/YouTube embebido, exporta a MP4
- **Instalar:** [Chrome Web Store - Downloader for GoHighLevel](https://chromewebstore.google.com/detail/downloader-for-gohighlevel/lcnajelpdoefgoilcihnpkofabpafjgd) — 3 descargas gratis (OTP email), luego $17/mes. También release GitHub: [github.com/serpapps/gohighlevel-downloader/releases](https://github.com/serpapps/gohighlevel-downloader/releases/latest)
- **Uso:** Abrir lección GHL → dar Play 3s → clic icono extensión → elegir calidad → `Guardar como` → mover a `activos/videos/` con nombre `ghl-YYYY-MM-DD-<slug>.mp4`
- **Si no detecta:** refrescar, dar play de nuevo, reabrir popup. Solo funciona logueado con acceso a la lección.

### 3.2 Opción B — Grabación pantalla (100% gratis, siempre funciona)
- **OBS Studio** [obsproject.com](https://obsproject.com/es) — Fuente `Captura de pantalla` + `Captura de audio de salida` → `Iniciar grabación` → reproducir lección a 1.5x → `Detener` → guarda MP4/MKV local
  - Tip: desactivar aceleración por hardware en Chrome `Configuración > Sistema` para evitar pantalla negra
- **Atajo Windows sin instalar:** `Win+Alt+R` (Xbox Game Bar) graba pantalla+audio a MP4

### 3.3 Opción C — Solo audio (más liviano para transcribir, ideal para vault)
No necesitas video, solo audio. Con **Audacity** (gratis):
`Audacity > Configuración de audio > Anfitrión: WASAPI Windows > Dispositivo: [tu parlante] (loopback)` → REC → reproducir lección → Exportar MP3. Misma calidad para Whisper, 10x menos peso [recorder.easeus.com](https://recorder.easeus.com/es/screen-recording-tips/grabar-audio-de-ordenador.html)

> **Elegí UNA:** A si querés archivo original, C si solo querés alimentar el vault (recomendado para HOY).

## 4. Paso 2 — Transcripción local (sin subir a nube)

### 4.1 Local CPU (recomendado, privado, ilimitado)
Tu RX 570 no necesita CUDA — Whisper corre en CPU:

```bash
P:\Anaconda\envs\comfyenv\python.exe -m pip install faster-whisper
faster-whisper "activos\videos\ghl-2026-09-07-6-etapas.mp3" --language es --model medium --output_dir "activos/videos/"
# genera .txt + .srt con timestamps, diarización básica
```

- Modelo `medium` = buen balance es/co para acento argentino. `large-v3` si querés máxima precisión (más lento).
- Documentación precisión Whisper: [arxiv.org/abs/2212.04356](https://arxiv.org/abs/2212.04356) citado en [meetergo.com/es/blog/transcribir-video](https://meetergo.com/es/blog/transcribir-video)

### 4.2 Nube rápida (si no querés instalar)
- **TurboScribe** [turboscribe.ai](https://turboscribe.ai/es/u/transcribe-audio-and-video-to-text) — arrastrar mp4/mp3, detecta hablantes, 98 idiomas, hasta 10h/archivo, gratis 5min prueba
- **WhisperAI** [whisperai.com](https://whisperai.com/es) — 5min gratis sin tarjeta

Con cualquiera, guardá el `.txt` verbatim.

## 5. Paso 3 — Carga al RAW del wiki

Yo (bibliotecario) creo:

```markdown
wiki/raw/2026-09-07-ghl-6-etapas-transcripcion.md
---
tipo: raw
fecha_creacion: 2026-09-07
tags: [ghl, transcripcion, 6-etapas, raw]
fuente_binaria: activos/videos/ghl-2026-09-07-6-etapas.mp3
idioma: es
duracion: ~XX min
---

# RAW — GHL 6 etapas (verbatim)

> Fuente: academia GHL, lección ciclo implementación. Uso interno, no redistribuir.

[transcript con timestamps 00:00 ...]

---
Notas captura: Opción A/B/C usada, fecha, quién capturó
```

- Este archivo **no se edita** después (evidencia). Se referencia desde los procesados con `fuente: [[wiki/raw/2026-09-07-ghl-6-etapas-transcripcion]]`.

## 6. Paso 4 — Proceso a conocimiento (vault + glosario)

### 6.1 Metodología genérica Pitau Tech
`wiki/estudio/metodologia-ciclo-6-etapas.md`
- Frontmatter `tipo: metodologia`
- Extrae cada etapa: objetivo, input, output, responsable, criterio de salida, anti-patrones
- Sin mencionar GHL en el título (metodología propia), citando fuente en pie

### 6.2 Glosario (6 entradas)
`wiki/glosario/software/gohighlevel/<etapa>.md` — una por etapa, con frontmatter `tipo: metodologia` o `software` según AGENTS.md, ej:

```yaml
---
tipo: metodologia
fecha_creacion: 2026-09-07
tags: [glosario, gohighlevel, relevamiento]
---
# Relevamiento de requerimientos
Definición limpia (2 líneas) + cuándo aplica + salida esperada + link oficial GHL verificado con webfetch
```

- Verificar cada URL no de 404 antes de publicar (regla `AGENTS.md: Verificar enlaces`).

### 6.3 Servicios Pitau Tech para estudios de arquitectura
`wiki/estudio/servicios-pitau-tech-arquitectura.md`
- Mapea cada etapa a la realidad ARG del vault (`AGENTS.md: libro obra papel, fotos celular, planos legales Ley 24.335`)
- Tabla GHL → Pitau Tech → ejemplo arquitectura (ver §7)

## 7. Paso 5 — Aplicación HOY a Emilia (diagnóstico)

El Sprint 30 días USD 600 (`proyectos/STUDIO_OS-Emilia/00-index.md:48` y `04-plan-studio-os.md`) **ya es** la Etapa 1+2 completas. Para la reunión de hoy, generar:

`proyectos/STUDIO_OS-Emilia/documentacion/07-propuesta-diagnostico-emilia-6-etapas.md`

| Etapa GHL | Nombre Pitau Tech para Emilia | Qué se hace en diagnóstico | Entregable que ve Emilia |
|---|---|---|---|
| 1. Relevamiento | **Diagnóstico Studio OS** | 2-3 entrevistas 60-90min + shadowing 1 día. Mapeo 9 ambientes (entrada→memoria) + dolores. Validar cuestionario 03 | Mapa AS-IS + matriz intervención humana (HUMANO/IA/AUTOMATIZACIÓN) |
| 2. Análisis y diseño | **Blueprint TO-BE** | Arquitectura `Drive+Vault+Discord→túnel→ComfyUI 24GB` (ya validada en 04-plan:27). Priorizar por matriz impacto/esfuerzo | Plano del estudio (circulaciones) + roadmap modular 2-3 cambios/mes |
| 3. Implementación técnica | **Build sprint (mini)** | Solo 1 vertical slice en sprint: Discord→ComfyUI con 1 proyecto real Emilia, 3-5 croquis | Prototipo: 8-12 variantes SD1.5/SDXL en Drive/Vault (no implementación completa) |
| 4. Pruebas internas | **QA Pitau Tech** | Validás vos antes de demo. Check licencias OpenRAIL, PI protegida | Checklist QA interno (no entregable cliente) |
| 5. Entrenamiento agentes | **Capacitación equipo** | 30min, 1 comando Discord, junior como librarian. Objeción "no somos técnicos" | Guía 1 página + taller |
| 6. Puesta en producción | **Go-live sprint** | Demo + métricas baseline (tiempo búsqueda, ciclo render, retrabajos) + Go/No-Go Fase 2 | Demo + `07-propuesta` con presupuesto Fase 2 modular, fee sprint acreditable |

**Framing comercial para hoy (no vender diagnóstico):**
> "30 días para entender el estudio, descubrir qué capacidad ya existe dentro de él y dejar un prototipo funcionando. Si avanzamos, el fee se acredita."

- Referenciar `proyectos/STUDIO_OS-Emilia/04-plan-studio-os.md:118-129` (plan operativo sprint) y `Resumen_Propuesta:134-151`.

## 8. Checklist de ejecución (HOY)

- [ ] **Vos:** capturar audio con Opción A o C (§3) → dejar en `activos/videos/ghl-2026-09-07-6-etapas.mp3`
- [ ] **Vos:** transcribir con 4.1 o 4.2 → pegarme el `.txt` verbatim (o el mp3 y lo transcribo yo)
- [ ] **Yo:** crear `wiki/raw/2026-09-07-ghl-6-etapas-transcripcion.md` (raw)
- [ ] **Yo:** crear `wiki/estudio/metodologia-ciclo-6-etapas.md` + 6 entradas glosario + `wiki/estudio/servicios-pitau-tech-arquitectura.md`
- [ ] **Yo:** crear `proyectos/STUDIO_OS-Emilia/documentacion/07-propuesta-diagnostico-emilia-6-etapas.md` (propuesta HOY lista para enviar)
- [ ] **Yo:** actualizar `proyectos/STUDIO_OS-Emilia/00-index.md` (fase: briefing → diagnostico), `wiki/estudio/00-index.md`, `wiki/glosario/software/gohighlevel/00-index.md`, y `log.md` (entrada nueva arriba)
- [ ] **Validación:** links verificados con webfetch, frontmatter completo, wikilinks funcionando

## 9. Qué no hacer

- No copiar binarios al vault (solo referencias a `activos/` — regla `AGENTS.md: Prioridad máxima`)
- No redistribuir contenido pago GHL fuera del vault interno
- No crear `wiki/software/ghl-academia` — ya está definido dónde va cada cosa (§2)

## 10. Próximo paso inmediato

Mandame el transcript (pegado o archivo en `activos/`). Con eso ejecuto §5-§7 en una sola vuelta y te dejo la propuesta de diagnóstico lista para Emilia hoy.

---
*Referencias vault:* [[proyectos/STUDIO_OS-Emilia/00-index]] · [[proyectos/STUDIO_OS-Emilia/04-plan-studio-os]] · [[proyectos/STUDIO_OS-Emilia/Resumen_Propuesta_Emilia_Studio_OS.txt]] · [[wiki/estudio/00-index]] · [[wiki/glosario/software/00-index]] · [[AGENTS.md]]
