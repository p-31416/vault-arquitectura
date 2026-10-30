---
tipo: flujo-curso
proyecto: concurso-gaudi-nexus
slug: earth2rhino-video-02
video_id: olUmAJBoMJU
titulo_video: "Google Maps to Rhino in 1 MINUTE"
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [earth2rhino, rhino, heron, grasshopper, google-3d-tiles, sitio, sagrada-familia]
idioma: es
generado_por: scripts/transcribir_youtube.py
transcript: raw/yt/transcripts/2026-10-29_olUmAJBoMJU.en.md
---

# Ficha video 02 — Google Maps to Rhino in 1 MINUTE (Heron + Google 3D Tiles)

> Fuente verbatim: `raw/yt/transcripts/2026-10-29_olUmAJBoMJU.en.md` (generado por `scripts/transcribir_youtube.py`, fuente `auto-sub`, 80 líneas). Video: `https://www.youtube.com/watch?v=olUmAJBoMJU`.

## El flujo, paso a paso

| # | Acción | Herramienta (nombre exacto) | Valores que dice el video | Timestamp |
|---|---|---|---|---|
| 1 | Instalar Heron | Rhino → `PackageManager`, buscar `Heron`, instalar última (en la grabación `0.5.0`), reiniciar Rhino | `Heron 0.5.0` | [00:00:14]–[00:00:32] |
| 2 | Abrir Grasshopper y fijar punto ancla | GH → Heron → `Set Earth Anchor Point` + `Toggle True` | punto por nombre/dirección o lat,lon (recomienda lat,lon: la dirección a veces falla) | [00:00:35]–[00:00:57] |
| 3 | Tomar coordenadas | Google Maps → clic derecho → copiar coordenadas → `Panel` GH → `Text Split` por coma → lat a latitude, lon a longitude | separador `,` | [00:01:00]–[00:01:18] |
| 4 | Importar malla 3D | GH → pestaña `GIS API` → `Google 3D Tiles IOI` (IOI = area of interest) | `boundary` = tamaño del área; `LOD 0–20` (arrancar en `13` y subir gradual); `cache folder` default | [00:01:22]–[00:01:49] |
| 5 | Autenticar | Google Cloud → `Map Tiles` → `Enable` → `Credentials` → `Show key` → `Panel` GH → input `API key` | trial gratuito 90 días (link en descripción del video) | [00:01:52]–[00:02:30] |
| 6 | Ejecutar y previsualizar | `Run True` + `Custom Preview` para ver texturas | subir LOD de a poco (más LOD = más tiempo de descarga) | [00:02:33]–[00:02:47] |
| 7 | Pasar a Rhino | `Bake` del preview | malla con textura en escena Rhino | [00:02:49]–[00:02:53] |
| 8 | Post | Render + mejora con Gemini/ChatGPT | crédito a Brian Washburn (autor Heron, vía McNeel Discourse) | [00:02:55]–[00:03:06] |

## Prompts y fórmulas

- Sin prompts. Fórmula operativa: `lat,lon → Split(",") → Anchor + IOI(boundary, LOD 13, API key) → Run → Custom Preview → Bake`.
- Regla del video: arrancar en LOD bajo y subir solo cuando el encuadre conforma.

## Modelos y servicios

| Nombre | Qué es | Costo que dice el video | Timestamp |
|---|---|---|---|
| Heron (Brian Washburn) | Plugin Grasshopper GIS | gratis (PackageManager) | [00:00:14] |
| Google 3D Tiles / Map Tiles API | Tiles 3D con textura de Google Maps | trial 90 días, luego facturación Google Cloud | [00:01:52]–[00:02:10] |
| Rhino 8 + Grasshopper | Destino del bake | no dicho en el video | — |

## Vacíos (no dicho en el video)

1. Sistema de coordenadas del bake (¿WGS84 → metros locales? ¿dónde queda el origen?).
2. Tamaño del área en unidades del `boundary` (metros/grados/tiles).
3. Peso de malla por LOD y limpieza (`ReduceMesh`, `MeshToNURB`).
4. Licencia de uso del material Google en entrega de concurso.

## Cómo lo adaptamos

| Lo que hace el video | Lo que hacemos nosotros | Por qué |
|---|---|---|
| Heron + Google 3D Tiles con API key | Replicar en archivo nuevo `SF-sitio-massing-v01.3dm`, capa `SF-CONTEXTO-GOOGLE`, LOD 13 primero | Es la vía más rápida al massing texturado del entorno Sagrada |
| Trial 90 días | Crear la key con cuenta del estudio y guardar solo referencia (no el secret) en el vault | El secret nunca entra a git (`.env` + `.gitignore`) |
| Bake directo | Medir `BoundingBox` y validar contra manzana Eixample (~133 m) y altura templo 172,5 m antes de densificar | Sin testigo de escala el massing engaña |
| Capa Google como final | Capa Google solo calibración; el massing de entrega se reconstruye en `SF-MASSING-OSM` (sólidos cerrados) | Regla auditada: PI terceros no va a cloud ni a lámina final |

## Checks contra el criterio del jurado

- [ ] Lógica constructiva sobre imitación de estilo.
- [ ] Trazabilidad de fuente + licencia en la ficha.
- [ ] Escala verificada contra testigo real antes del render.
