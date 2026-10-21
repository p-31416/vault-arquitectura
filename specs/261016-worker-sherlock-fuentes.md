# Spec — Worker sherlock-fuentes (nube, sin PC)

_Fecha: 2026-10-16 · Estado: aprobado por SOL (micro-pantallas 2026-10-16) · Relacionado: `specs/261013-plan-fuentes-emilia-inbox.md`, `specs/261009-spec-ingesta-fuentes.md`, `.github/workflows/vaultworm-arq.yml` (precedente) · Para evaluar en clase lunes_

## 1. Objetivo

Analizar en la nube (sin PC encendida, sin agentes locales) los links pendientes del Sheet `Fuentes-Inbox` y escribir los crudos en `raw/research/` del repo GitHub, marcando `procesado` + `destino vault`. Gratis.

## 2. Arquitectura

Workflow GitHub Actions `sherlock-fuentes.yml`: `schedule cron 07:30 AR` + `workflow_dispatch` (manual). Pasos: checkout → lee filas `Estado=pendiente` (service account) → por link: fetch (`r.jina.ai`, `yt-dlp` subs) → escribe `raw/research/YYYY-MM-DD-<slug>.md` (cita + tags + propuestas esqueleto) → actualiza Sheet (`procesado`, `Destino vault`) → commit + push.

## 3. Secretos (una vez, GitHub → Settings → Secrets)

- `GOOGLE_SERVICE_ACCOUNT_JSON` (nuevo; compartir el Sheet con esa cuenta como lectora).
- Reusa `GH_TOKEN` / `OPENCODE_API_KEY` si existen (patrón `vaultworm-arq.yml`).

## 4. Costos

Actions free 2000 min/mes; 3 links ≈ 2 min → sobra. `r.jina.ai` gratis con rate-limit; `yt-dlp` sin API key (subs). Sin costo fijo.

## 5. Riesgos y fail-soft

- jina bloquea/rate-limit (IG con login) → fila queda `pendiente` con nota, no rompe el lote.
- Service account revocada (incidente Sheets 2026-10-15) → el run avisa y no escribe parcial.
- Secretos solo en GitHub, nunca en el repo. Binarios nunca a git (solo `.md` + referencias).
- Advertencia real: el `vaultworm-arq.yml` existe pero **nunca se verificó corriendo** — paso 0 obligatorio: dispatch manual + ver commit antes de dar por existente la nube.

## 6. Criterio de done

Link en Sheet → `raw/research/<fecha>-<slug>.md` + `Estado=procesado` + `Destino vault` con ruta, todo vía push, sin PC encendida.

## 7. Duda abierta (lunes)

¿Digest antes o después del worker? Opción A: digest 07:00 con pendientes + worker 07:30 procesa. Opción B: worker primero, digest con resultados. Recomendación: A (Emilia prioriza, worker ejecuta).
