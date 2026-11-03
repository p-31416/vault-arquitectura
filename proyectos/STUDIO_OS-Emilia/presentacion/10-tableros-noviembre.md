---
tipo: proyecto
cliente: Emilia Pimenta
proyecto: Studio OS
ciudad: Argentina
pais: AR
fase: briefing
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
estado: presentacion
tags: [dashboard, tableros, presentacion, studio-os, quincena, concurso, referentes]
---

# Tableros noviembre — qué se hizo y qué se ve

> Tres tableros autocontenidos (abren con doble clic, sin servidor) con el trabajo 18/10 → 02/11. Para revisión con Emilia en pantalla.

## 1. Reporte de la quincena (SESSIONS + TEMAS)

[dashboard-quincena.html](dashboard-quincena.html) — 164 KB, sin imágenes externas.

- **KPIs**: 40 sesiones · 12 días con actividad · 16 specs · 58 scripts · 15 renders · 5 commits.
- **Solapa SESSIONS**: línea de tiempo por día con tags y bullets + tabla de sesiones.
- **Solapa TEMAS**: Rhino 3D + massing (7) · ComfyUI + concurso (9) · AutoCAD 2D (4) · Hermes + Sistema Operativo (20), cada tarjeta con descripción, rutas del vault, sesiones y plans.
- Buscador por palabra + tablas de specs, scripts, commits y pendientes.
- Detalle de cada sesión en `raw/sessions/`. Reporte largo en [[specs/261102-dashboard-resumen-15d|resumen 15 días]].
- Se regenera con `P:\Anaconda\envs\comfyenv\python.exe scripts\dashboard-quincena.py`.

## 2. Corridas del concurso (polaroid con tiempos)

[dashboard-concurso.html](dashboard-concurso.html) — 8 imágenes en miniatura embebida.

- 4 corridas 01/11 (baseline + hires ×3, Juggernaut/RealVisXL/Lightning) + 4 WF-01 de hoy (comparativa de checkpoint, prompting en español, receta del autor), con modelo y segundos medidos.
- Clic para agrandar, flechas para pasar. La versión full-res para revisión fina vive en `activos/web/concurso/`.
- Matriz completa en [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz del concurso]].
- Se regenera con `P:\Anaconda\envs\comfyenv\python.exe scripts\dashboard-concurso.py --embebido proyectos\STUDIO_OS-Emilia\presentacion\dashboard-concurso.html`.

## 3. Referentes AI×Gaudí (pinterest del concurso)

[dashboard-referentes-aixgaudi.html](dashboard-referentes-aixgaudi.html) — mosaico navegable por tags.

- Inventario de referentes del curso con filtros por tema y material en la URL (cada vista es un link compartible).
- Fuente: `raw/referentes/aixgaudi/` + `scripts/referentes_dashboard.py --slug aixgaudi`.
- Se regenera con `P:\Anaconda\envs\comfyenv\python.exe scripts\referentes_dashboard.py --slug aixgaudi` y se copia el `index.html` resultante a esta carpeta.

## Cómo mostrarlos

Doble clic en cada `.html` (Chrome/Edge). Funcionan sin internet salvo las fuentes del sistema. Para actualizar: correr el comando de cada tablero y commitear el HTML resultante.
