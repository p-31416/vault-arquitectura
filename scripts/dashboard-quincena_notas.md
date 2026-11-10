# dashboard-quincena.py — notas

## Qué resuelve

`specs/261102-dashboard-resumen-15d.md` es el reporte en markdown para Obsidian.
Faltaba la vista visual: un HTML que se abre con doble clic con KPIs, línea
de tiempo por día y reporte de sesiones del período, como los tableros del
curso y del concurso.

## Cómo se corre

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\dashboard-quincena.py
```

Opciones:

- `--desde AAAA-MM-DD` inicio del período (default `2026-10-18`)
- `--hasta AAAA-MM-DD` fin del período (default `2026-11-02`)
- `--out` carpeta del sitio (default `activos/web/quincena`)

Salida:

```
activos/web/quincena/index.html   ← HTML+CSS+JS en un archivo (abre con doble clic)
activos/web/quincena/datos.json   ← los datos, reutilizables
```

## De dónde salen los datos (sin hardcodear)

| Fuente | Qué aporta |
|---|---|
| `raw/sessions/YYYY-MM-DD-*.md` | fecha (prefijo del nombre), título (primer `# `), tags (frontmatter), bullets (sección "Qué se hizo", máx. 6) |
| `log.md` | entradas `## AAAA-MM-DD` del período con sus primeros bullets |
| `git log --since/--until` | commits del período (si git falla, lista vacía) |
| `specs/*.md` por fecha de modificación | specs nuevos con su título |
| `scripts/*.py` por fecha de modificación | scripts nuevos |
| `activos/proyectos/concurso-gaudi-nexus/` | conteo de renders en disco |
| `PENDIENTES` en el script | lista editable del siguiente ciclo |

## Decisiones

**El rango se filtra por texto.** Las fechas ISO `AAAA-MM-DD` comparan bien
como cadenas, así que `desde <= nombre[:10] <= hasta` alcanza sin parsear.

**Un solo pase de escape.** Todo texto del vault se pasa por `html.escape`
antes de volcar el JSON; además los `<`/`>` del JSON embebido van como
`\u003c`/`\u003e` para que nunca cierren el `<script>`.

**Días con y sin actividad.** La línea de tiempo recorre todos los días del
rango: muestra huecos además de avances, que es lo que pide un reporte.

**Sin dependencias.** Solo stdlib (`argparse`, `datetime`, `html`, `json`,
`os`, `re`, `subprocess`). Funciona con `file://`.

## Solapas y temas

- **SESSIONS**: línea de tiempo por día + tabla de sesiones (vista original).
- **TEMAS**: Rhino 3D + massing · ComfyUI + concurso · AutoCAD 2D · Hermes +
  Sistema Operativo · Otros. Cada tarjeta trae descripción breve (dónde vive
  en el vault), rutas, las sesiones del tema y sus plans.
- La clasificación vive en `TEMAS` + `_REGLAS_TEMA` + `clasificar()` arriba
  del script: una sesión cae en un solo tema, por tags + título, con claves
  cortas como palabra completa (`pi`, `cad`, `tim`, `wf`, `flow`, `whisk`),
  sin tildes para comparar y lista editable de programas.
- **Historia completa**: el mismo script genera `activos/web/historia/` con
  `--desde 2026-06-28` (123 sesiones, cero "otros") → `presentacion/dashboard-historia.html`.
- El buscador filtra ambas vistas.

## Para regenerar con otro período

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\dashboard-quincena.py --desde 2026-11-03 --hasta 2026-11-17
```

## Límite conocido

Los bullets de sesión se recortan a 220 caracteres y 6 por sesión: el tablero
es un mapa, el detalle vive en cada `raw/sessions/*.md`.
