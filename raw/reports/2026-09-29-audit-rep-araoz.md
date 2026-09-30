---
tipo: report
proyecto: estudio-pi
software: [autocad, mcp-autocad, com]
fecha_creacion: 2026-09-29
ultima_actualizacion: 2026-09-30
tags: [audit, dwg, SET_01, REP, capa, layout, unidades, bloques, entidades, com]
---

# Auditoría `REP-ARAOZ.copia-trabajo.dwg` vs SET_01-REP — 2026-09-29

> Fuente: lectura en vivo vía **COM directo con `pywin32`** (script `scripts/audita-dwg-com.py`) y **MCP `autocad`** para status/drawing info. Copia de trabajo: `activos/caddy-salidas/REP-ARAOZ.copia-trabajo.dwg` (original intacto).
> Datos completos en `raw/reports/audit-REP-ARAOZ.copia-trabajo.json` (2677 líneas) y `.md` (198 líneas).

---

## 1. Datos del archivo y unidades

| Campo | Valor |
|---|---|
| AutoCAD | **26.0s (LMS Tech) — 2027 TRIAL (NON COMMERCIAL)** |
| Archivo activo | `REP-ARAOZ.copia-trabajo.dwg` |
| Path | `P:\00-repos\proyecto-pi\vault-arquitectura\activos\caddy-salidas\REP-ARAOZ.copia-trabajo.dwg` |
| `INSUNITS` | **6 — metres** |
| Contrato MCP | millimetres (sin `unit_warning`) |
| `EXTMIN` | `[-90.72, -10.86, 0]` |
| `EXTMAX` | `[590.42, 834.0, 0]` |
| Área cubierta | ~681 × 845 m (planta urbana del estudio) |
| Screenshot | `activos/caddy-salidas/REP-ARAOZ.copia-trabajo.screenshot.png` (1376×754) |

**Lectura:** unidades consistentes. AutoCAD en metros, MCP en mm, sin `unit_warning`. El servidor convierte mm→drawing unit con `INSUNITS=6` (1000 mm = 1 m). OK para SET_01.

---

## 2. Layouts

| Layout | Tipo | Tab | Activo |
|---|---|---|---|
| `Model` | model space | 0 | — |
| `REP-PTipo-A1` | paper space | 1 | **activo** |

`REP-PTipo-A1` coincide con `REP-A1` esperado del spec (papel A1 full-bleed con `DWG To PDF.pc3`). Diferencia de nombre: `REP-PTipo-A1` vs `REP-A1` esperado — alinear.

---

## 3. Capas — cruce con spec SET_01 §2 (22 esperadas)

### 3.1 Resumen

- **Total en DWG:** 54 (incluye `0`, `Defpoints`, `*U4`, capas `ARQ-ARAOZ|*` y otras).
- **Coinciden con spec SET_01:** **0 / 22**.
- **Faltan del spec:** 22 (todas las del Kit).
- **Sobrantes del spec:** 54 (no hay match exacto).

### 3.2 Inventario de capas (54)

| # | Capa | Color ACI | Linetype | On | Frozen | Locked |
|---|---|---|---|---|---|---|
| 1 | `0` | 7 | Continuous | ✓ | — | — |
| 2 | `ROT-HOJA` | 5 | Continuous | ✓ | — | — |
| 3 | `ROT-TXT` | 174 | Continuous | ✓ | — | — |
| 4 | `ROT-VP` | 130 | Continuous | ✓ | — | — |
| 5 | `A-TERRENO` | 163 | Continuous | ✓ | ✓ | — |
| 6 | `REP-EJES` | 81 | DASHDOTX2 | ✓ | — | ✓ |
| 7 | `A-EJES` | 90 | DASHDOT | ✓ | — | ✓ |
| 8 | `REP-COTAS` | 41 | Continuous | ✓ | — | — |
| 9 | `Defpoints` | 7 | Continuous | ✓ | — | — |
| 10 | `SIMB-CARP` | 33 | Continuous | ✓ | — | — |
| 11 | `A-COTA-1-50` | 250 | Continuous | ✓ | — | — |
| 12 | `E-EJES` | 10 | Continuous | ✓ | — | ✓ |
| 13 | `A-MURO-MED` | 11 | Continuous | ✓ | — | ✓ |
| 14 | `0-REF` | 7 | Continuous | ✓ | ✓ | ✓ |
| 15 | `A-MURO-MAMP` | 24 | Continuous | ✓ | — | — |
| 16 | `A-SOLADOS` | 250 | Continuous | ✓ | — | — |
| 17 | `A-CARP-02` | 251 | Continuous | ✓ | — | — |
| 18 | `E-COL` | 5 | Continuous | ✓ | — | — |
| 19 | `E-COL-H` | 251 | Continuous | ✓ | — | ✓ |
| 20 | `CONDUCTOS` | 3 | Continuous | ✓ | — | — |
| 21 | `E-COL-EJES` | 254 | Continuous | ✓ | — | ✓ |
| 22 | `AR-CUADRO DE VANO` | 1 | Continuous | ✓ | — | — |
| 23 | `ARQ-ARAOZ\|TEXTO` | 7 | Continuous | ✓ | ✓ | — |
| 24 | `ARQ-ARAOZ\|A-TERRENO` | 163 | Continuous | ✓ | ✓ | — |
| 25 | `ARQ-ARAOZ\|NUMLOC` | 3 | Continuous | ✓ | ✓ | — |
| 26 | `ARQ-ARAOZ\|FLECHA` | 8 | Continuous | ✓ | — | — |
| 27 | `ARQ-ARAOZ\|ESCALERA` | 4 | Continuous | ✓ | — | — |
| 28 | `ARQ-ARAOZ\|CARP` | 2 | Continuous | ✓ | — | — |
| 29 | `ARQ-ARAOZ\|COTAS` | 3 | Continuous | ✓ | — | — |
| 30 | `ARQ-ARAOZ\|PROYECCIONES` | 9 | `ARQ-ARAOZ\|DASHED` | ✓ | ✓ | — |
| 31 | `ARQ-ARAOZ\|MUROS` | 7 | Continuous | ✓ | — | — |
| 32 | `ARQ-ARAOZ\|MUROS-VISTA` | 4 | Continuous | ✓ | — | — |
| 33 | `ARQ-ARAOZ\|HATCHMUROS` | 1 | Continuous | ✓ | ✓ | — |
| 34 | `ARQ-ARAOZ\|CONDUCTOS` | 3 | Continuous | ✓ | — | — |
| 35 | `ARQ-ARAOZ\|INCENDIO` | 5 | Continuous | ✓ | — | — |
| 36 | `ARQ-ARAOZ\|ASCENSOR` | 2 | Continuous | ✓ | — | — |
| 37 | `ARQ-ARAOZ\|BASICO` | 1 | Continuous | ✓ | — | — |
| 38 | `ARQ-ARAOZ\|VANOS` | 1 | Continuous | ✓ | — | — |
| 39 | `ARQ-ARAOZ\|REP-EJES` | 254 | `ARQ-ARAOZ\|DASHDOTX2` | ✓ | ✓ | — |
| 40 | `ARQ-ARAOZ\|EJES` | 2 | `ARQ-ARAOZ\|DASHDOT` | ✓ | — | — |
| 41 | `ARQ-ARAOZ\|ESTRUCTURA` | 6 | Continuous | ✓ | — | — |
| 42 | `ARQ-ARAOZ\|000-cotas estructrua` | 5 | Continuous | ✓ | — | — |
| 43 | `ANOTAÇÃO` | 33 | Continuous | ✓ | — | — |
| 44 | `ESQUADRIAS` | 250 | Continuous | ✓ | — | — |
| 45 | `SIMB-MURO` | 251 | Continuous | ✓ | — | — |
| 46 | `A-LETRA-GENERAL` | 154 | Continuous | ✓ | — | — |
| 47 | `A-LETRA-DETALLES` | 154 | Continuous | ✓ | — | — |
| 48 | `A-SIMBOLO-NPT-PLANTA` | 251 | Continuous | ✓ | — | — |
| 49 | `A-EQUIP-` | 8 | Continuous | ✓ | — | — |
| 50 | `IE-EJEX` | 32 | DASHDOT | ✓ | ✓ | ✓ |
| 51 | `A-EJES-VACIOS` | 113 | DASHDOT | ✓ | — | ✓ |
| 52 | `E-TAB` | 166 | Continuous | ✓ | — | — |
| 53 | `E-TAB-H` | 251 | Continuous | ✓ | — | ✓ |
| 54 | `E-COL-TXT` | 250 | Continuous | ✓ | — | ✓ |

### 3.3 Diagnóstico de nomenclatura

**Lo que se llegó a hacer (práctica razonable del estudio):**
- Sub-capas por subcategoría: `A-MURO-MED` (mampostería existente?), `A-MURO-MAMP` (mampostería), `A-CARP-02`, `A-COTA-1-50` (escala 1:50 en el nombre), `A-LETRA-GENERAL` vs `A-LETRA-DETALLES`, `A-SIMBOLO-NPT-PLANTA`.
- Bloque `ARQ-ARAOZ|*` con sub-capas separadas por disciplina funcional (carpintería, ejes, muros, vanos, escaleras, incendio, ascensor, conductos).
- Uso inteligente de `Frozen` para capas de referencia (`A-TERRENO`, `0-REF`, `IE-EJEX`, `ARQ-ARAOZ|TEXTO`).
- `Locked` para ejes (`REP-EJES`, `A-EJES`, `E-EJES`, `A-MURO-MED`, `E-COL-H`, `E-COL-EJES`, `IE-EJEX`, `A-EJES-VACIOS`, `E-TAB-H`, `E-COL-TXT`) — buena práctica para evitar modificaciones accidentales en capas de referencia.

**Gaps contra SET_01:**
1. **Nomenclatura divergente del Kit:** prefijos `REP-` (replanteo real), `A-` (arquitectura), `E-` (estructura), `ROT-` (rotulado), `SIMB-` (simbología), `IE-` (instituto/ingeniería?). El spec pide `R-`, `A-`, `S-`, `G-`, `V-`, `M-`, `P-`, `E-`, `F-` con semántica clara.
2. **Sin sufijo de estado NCS** (`-N` / `-E` / `-D`): la diferenciación `A-MURO-MED` vs `A-MURO-MAMP` parece estado (existente / a demoler) pero no sigue el patrón canónico.
3. **Nombres con espacios y glifos no ASCII:** `AR-CUADRO DE VANO`, `ANOTAÇÃO`, `A-EQUIP-` (guion final), `ARQ-ARAOZ|000-cotas estructrua` (typo + espacio). Incompatible con export a NCS/ISO 13567 y con herramientas de automatización.
4. **Linetypes personalizados no estándar:** `ARQ-ARAOZ|DASHED` y `ARQ-ARAOZ|DASHDOTX2` están definidos como capas de un estudio anterior — no forman parte del Kit.
5. **`S-` (estructura) usado como `E-`:** las capas `E-EJES`, `E-COL`, `E-TAB`, `E-COL-H`, `E-TAB-H` deberían ser `S-EJES`, `S-COLU`, `S-VIGA` según el Kit.

### 3.4 Áreas de mejora (capas)

| Mejora | Comando / acción | Soporte |
|---|---|---|
| Migrar nomenclatura al Kit | `LAYTRANS` con `LayMap.dwg` (mappings `REP-EJES→R-EJES`, `REP-COTAS→R-COTA`, `A-MURO-MED→A-MURO`, `E-EJES→S-EJES`, etc.) | `mcp-autocad` (`acet-laytrans`) |
| Renombrar a ASCII sin espacios | LISP `RENAME-LAYER` o `acet-laytrans` con opción 1 | MCP + ayuda oficial |
| Crear las 22 del spec si faltan | `LISP SET-01-REP` (idempotente) | LISP a crear |
| Asignar DWS de validación | `EP-REP.dws` + `CHECKSTANDARDS` | DWT a crear |

---

## 4. Bloques definidos (top 20)

| Bloque | Entities | Nota |
|---|---|---|
| `_Dot` | 2 | punto |
| `M2_COTA` | 3 | símbolo de cota manual |
| `_Open90` | 3 | ángulo 90° |
| `Tabela_Esquadrias` | 10 | **tabla de carpinterías** (pre-armada, candidata a `DATAEXTRACTION`) |
| `*U4` | 30 | anónimos (AutoCAD) |
| `*D5`, `*D8`–`*D18` | 9–10 c/u | anónimos dimensionales |
| `_ArchTick` | 1 | tick de arquitectura |
| **`SIMBOLO DE EJE`** | 9 | **marca de eje (con espacio, renombrar)** |
| `C40.20` | 6 | columna 40×20 |
| **`PUERTA BATIENTE`** | 46 | **puerta batiente (con espacio, renombrar)** |

**Total de bloques:** 367 (muchos anónimos `*U*` y `*D*`).

**Diagnóstico:**
- Hay 2 bloques con nombre semántico útil (`SIMBOLO DE EJE`, `PUERTA BATIENTE`) pero con **espacios en el nombre** — incompatibles con atributos estándar y con la práctica del Kit.
- Bloques anónimos (`*U*`, `*D*`) sugieren uso intenso del Mechanical/Architectural Desktop o de operaciones `BURST` que dejan basura. Limpieza con `PURGE` recomendada.
- `C40.20` (columna 40×20 cm) es un bloque dimensional explícito — útil para `DATAEXTRACTION`.
- `Tabela_Esquadrias` es una tabla pre-armada (no se pudo leer contenido en este escaneo).

**Áreas de mejora:**
- Renombrar `SIMBOLO DE EJE → R-EJE-MARCA`, `PUERTA BATIENTE → R-PUERTA`.
- Bloque dinámico `R-PTO-ATTR` con atributos `ID/X/Y/Z` para extracción de coordenadas.
- Bloque dinámico `R-ABER-DYN` con Visibility States (0.60 / 0.70 / 0.80 / 0.90 / 1.00 m).
- `PURGE` agresivo antes de empaquetar DWT.

---

## 5. Entidades en model space (1311 leídas + 47 con race COM)

| Tipo | Cantidad |
|---|---|
| `LINE` | 619 |
| `DIM` | 291 |
| `INSERT` | 197 |
| `TEXT` | 83 |
| `POLYLINE` | 60 |
| `MTEXT` | 26 |
| `HATCH` | 23 |
| `CIRCLE` | 14 |
| `AcDb2LineAngularDimension` | 3 |

**Lectura:** el plano es geométricamente rico. 619 líneas + 60 polilíneas + 23 hachurados dibujan una planta completa. 291 cotas (DIM) es muy alto — coherente con un plano de replanteo. 197 inserts (referencias a bloques) implica mucho uso de simbología pre-armada.

---

## 6. Entidades por capa (top 20)

| Capa | Total | Rol inferido |
|---|---|---|
| `A-MURO-MAMP` | **271** | mampostería nueva (la mayor parte del dibujo) |
| `0` | **254** | geometría suelta en capa default (no migrada) |
| `REP-COTAS` | **152** | cotas de replanteo |
| `A-COTA-1-50` | **135** | cotas anotadas a 1:50 |
| `SIMB-MURO` | **122** | simbología de muros |
| `A-EQUIP-` | **67** | equipamiento (¿mobiliario?) |
| `A-SIMBOLO-NPT-PLANTA` | **55** | NPT en planta |
| `A-CARP-02` | **52** | carpintería |
| `E-EJES` | **30** | ejes estructurales |
| `Defpoints` | **27** | puntos de definición (AutoCAD) |
| `A-MURO-MED` | **25** | muros existentes |
| `CONDUCTOS` | **25** | conductos |
| `E-COL` | **22** | columnas |
| `IE-EJEX` | **14** | ejes preliminares (frozen) |
| `A-EJES` | **13** | ejes arquitectónicos |
| `REP-EJES` | **12** | ejes de replanteo (locked) |
| `A-SOLADOS` | **11** | solados |
| `A-EJES-VACIOS` | **10** | ejes de vacíos |
| `E-TAB-H` | `E-TAB-H` | 8 | tabiques (hormigón?) |
| `E-TAB` | 6 | tabiques |

**Hallazgo clave:** **254 entidades viven en la capa `0`** — eso es geometría suelta que no se migró a una capa con nombre. Buena candidata para `set_entity_layer` vía MCP `autocad`.

---

## 7. Textos representativos (TEXT)

- **Ejes (A-EJES, REP-EJES):** `'L.O'`, `'E.D.P'`, `'E.R.1'`, `'E.R.2'` — nomenclatura de ejes con prefijos `L.O` (línea oficial?), `E.D.P`, `E.R.1/2`.
- **NPT (A-SIMBOLO-NPT-PLANTA):** `'NPT+7.634'` — nivel de piso terminado +7.634 m.
- **Equipamiento (A-EQUIP-):** `'1'` — contador.

**Lectura:** los textos son técnicos, con mezcla de convenciones (algunos `+` decimal, otros con punto).

---

## 8. Inserts representativos (INSERT)

- `E-COL` × `C40.20` en múltiples posiciones → columnas de 40×20 cm insertadas como bloque dimensional.
- `E-EJES` con `*U233`, `*U234`, `*U235`, `*U282` → marcas de ejes en grilla.
- `A-CARP-02` con `*U39`, `*U38`, `*U161` → carpinterías (probable puerta).
- `0-REF` con `ARQ-ARAOZ` → **xref externa** `ARQ-ARAOZ` anclada al origen — el proyecto viene de un DWG externo referenciado.

**Hallazgo crítico:** `0-REF` referencia un DWG externo `ARQ-ARAOZ` (probablemente el original del arquitecto que hacía las plantas). **Las capas `ARQ-ARAOZ|*` que aparecen son las de ese xref**, no del DWG actual.

---

## 9. Áreas de mejora (consolidado)

### 9.1 Nomenclatura de capas
- Migrar al Kit SET_01 con `acet-laytrans` (mapeo) + LISP `RENAME-LAYER` (ASCII sin espacios).
- Eliminar las 22 capas del Kit que faltan (crearlas via `SET-01-REP`).
- Documentar las 21 capas custom como **extensiones** del SET_01 (sub-capas) en el spec.

### 9.2 Bloques
- Renombrar `SIMBOLO DE EJE → R-EJE-MARCA`, `PUERTA BATIENTE → R-PUERTA`.
- Crear `R-PTO-ATTR` (con atributos ID/X/Y/Z) y `R-ABER-DYN` (dinámico con Visibility States).
- `PURGE` agresivo antes de empaquetar la DWT.

### 9.3 Layouts
- Renombrar `REP-PTipo-A1 → REP-A1` (alinear con spec).

### 9.4 Geometría suelta
- 254 entidades en capa `0` → migrar con `set_entity_layer` o `LAYER` manual.
- `xdata` revisar si aplica (no leído en este escaneo).

### 9.5 Documentación
- Capa `AR-CUADRO DE VANO` (espacio) → `AR-CUADRO-DE-VANO` o migrar al Kit.
- Capa `ARQ-ARAOZ|000-cotas estructrua` (typo) → corregir o eliminar.
- Capa `ANOTAÇÃO` (portugués) → traducir o eliminar.

---

## 10. Automatización propuesta

### 10.1 AutoLISP

- **`SET-01-REP`** — crea las 22 capas del spec con color/linetype/lineweight correctos. Idempotente.
- **`AUDIT-LAYERS`** — compara dibujo activo contra `EP-REP.dws` y reporta delta.
- **`RENAME-LAYER`** — convierte espacios y glifos a ASCII.
- **`PURGE-ANON`** — limpia bloques `*U*` / `*D*` con confirmación.
- **`MK-R-PTO`** — inserta `R-PTO-ATTR` con prompts ID/X/Y/Z.
- **`R-ABER-DYN`** — bloque dinámico de puerta con Visibility States (0.60 / 0.70 / 0.80 / 0.90 / 1.00 m).

### 10.2 Botonera (paleta `.cuix`)

Botones en la paleta del estudio: `SET-01-REP`, `AUDIT-LAYERS`, `MK-R-PTO`, `R-EJE-MARCA`, `ZOOM 1000/50 XP`, `LAYTRANS-FROM-EP-REP`.

### 10.3 DWS + DWT

- **`EP-REP.dwt`** con `INSUNITS=6`, escalas 1:25/1:50/1:100/1:200/1:1.25, layout `REP-A1` A1 apaisado con viewport a 1:50 Display Locked.
- **`EP-REP.dws`** con las 22 capas, `EP-2.5`/`EP-3.5`, `EP-ARQ`, mapeos `LAYTRANS`.
- Verificación: `CHECKSTANDARDS` y Batch Standards Checker (`.chx`).

### 10.4 Extracción de datos

- `DATAEXTRACTION` desde `R-PTO-ATTR` → CSV/XLS de coordenadas de replanteo.
- `EATTEXT` / `ATTEXT` (CDF/CSV) alternativa sin UI.
- `Tabela_Esquadrias` (existente) → pipeline de planillas de carpintería.

### 10.5 MCP `autocad`

- `list_layers` (validado), `query_entities(layer=R-EJES)` (requiere scan acotado).
- `set_entity_layer` para migrar las 254 entidades de capa `0` a capas del Kit.
- `capture_screenshot` para feedback visual al humano.
- `autodesk-help_search_help_content` con `product_code=ACD, release_code=2027, locale=es_ES` para citas oficiales (`LAYTRANS`, `CHECKSTANDARDS`, bloques dinámicos).

---

## 11. Próximos pasos (siguiente ciclo)

1. **Migrar la geometría de `0` a su capa correcta** con `set_entity_layer` MCP (254 entidades — auditar primero cuáles van a dónde).
2. **Definir `EP-REP.dws`** con las 22 capas del Kit.
3. **Construir `SET-01-REP.lsp`** y aplicarlo en una copia limpia para verificar idempotencia.
4. **Definir el playbook `pbk-set-replanteo`** (wiki) con las fichas Jr por función.
5. **Capturar screenshot del layout activo `REP-PTipo-A1`** para comparar con un render esperado del spec.
6. **Generar reporte comparativo de las 22 capas** una vez migrada la nomenclatura.

---

## 12. Archivos generados

| Archivo | Tamaño | Propósito |
|---|---|---|
| `scripts/audita-dwg-com.py` | ~5 KB | Script COM con notas didácticas |
| `scripts/audita-dwg-com_notas.md` | ~2 KB | Notas línea por línea |
| `scripts/audita-dwg.py` | ~9 KB | Script ezdxf (alternativa offline) |
| `scripts/audita-dwg_notas.md` | ~5 KB | Notas ezdxf |
| `raw/reports/audit-REP-ARAOZ.copia-trabajo.json` | 45 KB | Dump completo (machine-readable) |
| `raw/reports/audit-REP-ARAOZ.copia-trabajo.md` | 7.5 KB | Reporte tabular por capas/tipos |
| `raw/reports/2026-09-29-audit-rep-araoz.md` | este archivo | Análisis consolidado + delta vs spec |
| `activos/caddy-salidas/REP-ARAOZ.copia-trabajo.dwg` | 553 KB | Copia de trabajo |
| `activos/caddy-salidas/REP-ARAOZ.copia-trabajo.screenshot.png` | ~70 KB | Screenshot del layout activo |
