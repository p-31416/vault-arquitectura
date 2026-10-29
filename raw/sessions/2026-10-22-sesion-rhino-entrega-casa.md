---
tipo: log
fecha_creacion: 2026-10-22
ultima_actualizacion: 2026-10-22
tags: [rhino8, modelado-3d, vivienda, dwg, autocad-lt, make2d, layout, entrega, sherlock, contenidos, creadores]
---

# Sesión 2026-10-22 (noche) — Rhino para la entrega de la casa: investigación, ruta y ajuste a reunión 09:00

## Qué se pidió

1. Un documento en los reportes de Sherlock que sintetice la investigación ya hecha, el mapa de creadores/canales a seguir y el cruce con los **47 videos `rhino`** del Takeout de YouTube.
2. Definir el plan de trabajo en Rhino para entregar **una casa de tres niveles** (planta baja, entrepiso, primer piso y segundo piso barra-terraza; sin planta de servicio) a partir de un plano 2D de AutoCAD, con plantas, cortes y lámina A3 en PDF vectorial.
3. Al cierre, dos correcciones de contexto: **la reunión es mañana 2026-10-23 a las 09:00** y **AutoCAD LT no modela en 3D**.

## Qué se hizo

### 1. Investigación y cruce de fuentes

- Se partió del informe madre `raw/research/2026-10-22-modelar-casa-rhino.md` (178 líneas) con **11 fuentes verificadas 200** y 13 citadas: guía oficial McNeel *PushPull for Architects* (con `PP-Architecture-Start.3dm`), docs de `Block`, `Insert`, `Layout`, `Print` y `Make2D`, How to Rhino, índice español de la Universidad de Granada, hilos de Discourse y Food4Rhino/rhinomcp.
- Se cruzaron los **47 videos únicos con tag `rhino`** (31 de la playlist `ARQ/Rhino+Grasshopper` + etiquetados de Watch Later, ya deduplicados) contra los creadores registrados en `raw/yt/creadores.md` y `raw/yt/canales-veredictos.json`.
- Resultado del cruce: **16 canales** en el vault, **0 duplicados** entre los creadores nuevos y los 47 videos. Nuevos aportados por la investigación: Diego Pascual, Tom Budd, Hakan Architecture, Flavio Bevilacqua, Kyle Houchens, Ruben Borup, SMlab UGR y McNeel Discourse.
- **No hay transcripciones de Rhino** en `raw/yt/transcripts/`; las duraciones no se pudieron verificar por fetch (queda para una Fase 2 con `yt-dlp`).

### 2. Reporte entregable

`raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md` (294 líneas, 18.6 KB): síntesis de la investigación, mapa de creadores con veredictos, cruce con los 47 videos, flujo de 10 pasos, cronograma, riesgos, checklist y fuentes.

### 3. Ruta de modelado aprobada y después reajustada

`specs/261022-ruta-modelado-casa-rhino.md` (141 líneas). Aprobada en primera instancia y luego corregida por dos hechos nuevos:

- **Entrega: mañana 09:00**, no 17:00. El PDF v1 se exporta **esta noche**; mañana 06:30–08:30 sólo se corrige, se re-exporta y se copia a Drive/USB. Cierre duro: **08:30**.
- **AutoCAD LT sin 3D.** LT queda para `AUDIT`, `PURGE`, `WBLOCK` y verificación de unidades con `DIST`; toda la extrusión, booleanas, cubierta y escalera se hacen en Rhino.
- Flujo DWG ajustado: `Insert` como **Block instance** en `CAD-BASE` → duplicar la instancia → `Explode` **sólo la copia** en `CAD-WORK` → `Join`/`CloseCrv` → offset y extrusión. La base original queda bloqueada, oculta y removible.
- Si las plantas vienen superpuestas en Z=0: separarlas por capa/nivel con `SelLayer` + `Move` en Z.
- Alcance recortado a **un corte** (dos sólo si entra) y mobiliario mínimo de un bloque por ambiente.

Cronograma vigente:

| Bloque | Ventana | Contenido |
|---|---|---|
| A | hoy 18:30–21:30 | Setup, limpieza en LT, `Insert` DWG, ejes, muros PB |
| B | hoy 21:30–00:00 | Entrepiso, 1° piso, aberturas |
| C | hoy 00:00–01:30 | 2° barra-terraza, cubierta, escalera simple |
| D | hoy 01:30–03:00 | `Make2D` 4 plantas, `Layout` A3, 1 corte, PDF v1 |
| E | mañana 06:30–08:30 | Correcciones, 2° corte si entra, re-export, backup |

### 4. Ficha de contenidos (sin promover)

`@contenidos` generó `raw/contenidos/2026-10-22-modelar-casa-rhino.md` (259 líneas, `estado: propuesta`) con 11 secciones y dos anexos (mapa de 16 creadores; 10 pasos + checklist). Frenó en su gate HITL y **no tocó `wiki/`**.

### 5. Estado de Rhino en la máquina

- **Rhino 8 está instalado**: `C:\Program Files\Rhino 8\System\Rhino.exe`, versión **8.5.24072.13001**.
- El **puente MCP está cerrado**: `rhino_get_rhino_scene_info` devolvió `WinError 10061` (conexión rechazada). Falta correr `rhino_script.py` dentro de Rhino (repo `reer-ide/rhino_mcp`; en Rhino 8: **Tools → RhinoScript → Run**).
- El script no está en el cache local de `uv`; hay que descargarlo del repo o ubicar la copia que usa `uvx`.

## Archivos del vault

- `raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md` (nuevo, 294 líneas)
- `specs/261022-ruta-modelado-casa-rhino.md` (nuevo y reajustado, 141 líneas)
- `raw/research/2026-10-22-modelar-casa-rhino.md` (178 líneas, informe madre)
- `raw/research-cache/2026-10-22-modelar-casa-rhino.json` (cache, gitignored)
- `raw/research/00-index.md` (fila nueva, estado `propuesta`)
- `raw/contenidos/sherlock-modelar-casa-rhino.md` (stub `pendiente-formato`)
- `raw/contenidos/2026-10-22-modelar-casa-rhino.md` (ficha formateada, `estado: propuesta`, sin promover)
- `.gitignore` (bloque nuevo de claves SSH/secretos, sin commit)
- `raw/sessions/2026-10-22-sesion-rhino-entrega-casa.md` (este archivo)
- `log.md` (entrada del 22/10)

Sin commit: los cambios quedan en el working tree.

## Cerebro-digital

**Topics:** modelado de vivienda en Rhino 8 · ruta DWG 2D → sólidos · `PushPull` vs extrusión clásica · 3D → planos (`Make2D` + `Layout`) · bloques para base CAD y mobiliario · restricción AutoCAD LT · entregable A3 en PDF vectorial · creadores y tutoriales de Rhino en español e inglés · puente RhinoMCP.

**Entidades:** `specs/261022-ruta-modelado-casa-rhino.md` · `raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md` · `raw/contenidos/2026-10-22-modelar-casa-rhino.md` · guía McNeel *PushPull for Architects* · `PP-Architecture-Start.3dm` · comandos `Insert`, `Block`, `PushPull`, `Make2D`, `Layout`, `Print` · `reer-rhino-mcp` / `rhino_script.py` · Rhino 8.5.24072 · AutoCAD LT · Diego Pascual, Tom Budd, Hakan Architecture, Flavio Bevilacqua, Kyle Houchens, Ruben Borup, SMlab UGR.

**Hechos verificados:** (1) los 47 videos `rhino` cubren 16 canales y no aportan duplicados frente a los creadores nuevos; (2) no existen transcripciones de Rhino en el vault; (3) `Insert` de Rhino permite insertar un archivo externo como bloque, grupo u objetos individuales, con definición *Embedded*, *Embedded and linked* o *Linked*; (4) `Make2D` trabaja por vista/CPlane y `Print` exporta la página del layout a Rhino PDF vectorial; (5) AutoCAD LT no modela en 3D, así que la única vía es 2D en LT y 3D en Rhino; (6) Rhino 8.5 está instalado pero el socket del MCP rechaza conexiones hasta que se ejecute `rhino_script.py` dentro de Rhino.

## Pendientes

- **Esta noche:** ejecutar los bloques A–D y dejar el PDF v1 exportado.
- **Mañana 06:30–08:30:** corregir, re-exportar y copiar el PDF a Drive/USB antes de las 08:30.
- **Puente Rhino:** descargar `rhino_script.py` a `scripts/` y correrlo en Rhino; después verificar con `get_rhino_scene_info`.
- **Datos faltantes:** ruta y nombre del DWG, nombre del cliente para `casa-<cliente>-v01.3dm`, y estándar de capas Rhino AR.
- **Después de la reunión:** decidir promoción de la ficha a `wiki/fuentes` (`modelar_casa_rhino-dwg_make2d-multifuente.md`) y prioridad P1 (ampliar `wiki/glosario/software/rhino`) vs P2 (página `modelado-vivienda-rhino`).
- **Fase 2:** `yt-dlp` para duraciones y transcripciones; subir `subagent_depth` para encadenar Sherlock → Contenidos.
