---
tipo: log
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [sesion, dashboard, quincena, concurso, referentes, presentacion, wiki, embebido]
idioma: es
---

# 2026-11-02 — Sesión dashboards: quincena SESSIONS/TEMAS + concurso 8 imgs + 3 HTML para Emilia

Más nuevo → más arriba.

## Qué se hizo

1. **Dashboard resumen 15 días** (`specs/261102-dashboard-resumen-15d.md`): KPIs, línea de tiempo 18/10→02/11, 4 sistemas, pendientes. Commiteado en `c1ed826`.
2. **Dashboard concurso con las 4 corridas nuevas**: `gx-WF01_00001..00004` (hoy 11:16–11:57, WF-01 512²) detectadas en output de ComfyUI, metadata leída del PNG, tiempos vivos de `/history` (354/390/334/445 s), copiadas a `activos/.../sdxl-vista/`, 4 entradas en `ITEMS` + `segundos_fijo`. Tablero regenerado con 8 imágenes. Matriz con sección 2026-11-02.
3. **Respaldo de tiempos en dashboard-concurso.py**: `segundos_fijo` por corrida (el `/history` se vacía al reiniciar ComfyUI); notas actualizadas.
4. **Dashboard quincena HTML** (`scripts/dashboard-quincena.py` + notas + fila en `scripts/00-index`): parsea `raw/sessions/`, `log.md`, `git log`, specs/scripts por mtime, conteo de renders → `activos/web/quincena/` con KPIs, línea de tiempo, tablas y buscador.
5. **Solapas SESSIONS/TEMAS**: `TEMAS` + `_REGLAS_TEMA` + `clasificar()` (tags+título, claves cortas como palabra completa, pre-chequeos LoRA/massing). Reparto final: rhino 7 · comfy 9 · autocad 4 · hermes 21 · otros 0. Tres bugs de clasificación corregidos en el camino (3d vs grafo-3D, viewport en AutoCAD, LoRA rhino-to-image en Comfy).
6. **Pregunta de Emilia**: los HTML estaban en `activos/` (gitignored) → publicados autocontenidos en `proyectos/STUDIO_OS-Emilia/presentacion/`: quincena (164 KB tal cual), concurso (`--embebido` nuevo con thumbs base64 520px, 593 KB, 0 refs externas), referentes aixgaudi (2,4 MB). Puerta `10-tableros-noviembre.md`.
7. **Commits**: `c1ed826` (set PI + resumen 15d), `39444ad` (quincena + concurso 8 + reorg WF-curso de Sol), `7c3bcff` (3 dashboards Emilia + puerta). Sin secretos en el diff (verificado por grep).

## Archivos tocados / creados

| Archivo | Qué |
|---|---|
| `specs/261102-dashboard-resumen-15d.md` | nuevo — reporte markdown 15 días |
| `scripts/dashboard-quincena.py` | nuevo — tablero HTML quincena con solapas y temas |
| `scripts/dashboard-quincena_notas.md` | nuevo — didáctica |
| `scripts/dashboard-concurso.py` | `segundos_fijo` + modo `--embebido` (thumbs base64) |
| `scripts/dashboard-concurso_notas.md` | notas de ambos agregados |
| `scripts/00-index.md` | filas de ambos dashboards |
| `proyectos/.../workflows/00-index.md`, `00-matriz-pruebas-concurso.md`, `proyectos/concurso-gaudi-nexus/index.md` | links al tablero concurso + sección corridas 02/11 |
| `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-{quincena,concurso,referentes-aixgaudi}.html` | nuevos — versiones para Emilia |
| `proyectos/STUDIO_OS-Emilia/presentacion/10-tableros-noviembre.md` | nuevo — puerta |
| `activos/web/quincena/`, `activos/web/concurso/`, `activos/.../sdxl-vista/` | generados/copiados (fuera de git) |
| `raw/sessions/2026-11-02-sesion-dashboards-quincena.md` | este cierre |

## Análisis cerebro-digital

- **Topics**: dashboard-quincena, solapas sessions-temas, clasificación por tags, segundos_fijo vs history, modo embebido base64, presentacion para Emilia, wiki vs activos, reorg WF-curso en paralelo.
- **Entidades**: dashboard-quincena.py, dashboard-concurso.py --embebido, referentes_dashboard.py, presentacion/, WF-curso, WF-Comfy-YT, sdxl-vista, ComfyUI /history, PIL 11.3.0.
- **Hechos**: 41 sesiones en rango 18/10→02/11; tablero concurso con 8 imágenes y tiempos (54,3 + 25,4 min GPU); 3 HTML commiteados y visibles en otra compu tras pull; full-res solo local; 3 commits del día; cero secretos commiteados.
