---
tipo: proyecto
cliente: Casa Uruguay
proyecto: Casa frente al mar (Arraigada) — reconstrucción 3D en Rhino 8
ciudad: Manantiales
pais: Uruguay
fase: investigacion
area_m2: 140
fecha_inicio: 2026-10-26
fecha_estimada_entrega: s/d
equipo: [modelado_3d: Sol, modelado_3d_rhino: agente]
estado: activo
tags: [mvp_05, rhino8, casa_uruguay, arraigada, madera, pdf, escala, axonometria, autocad]
idioma: es
---

# 02-CASA-URUGUAY — Reconstruction 3D en Rhino 8 desde el PDF

> Proyecto gemelo de `3D-casa_uruguay.dwg` (AutoCAD LT 2027). La fuente del 2D es la publicación de la casa; en Rhino se reconstruye el 3D con **sólidos** para poder cortar y laminar.
> **Corrección (27/10):** el corte de AIZ **salió bien** — la hoja a 1:50 quedó hecha y renderizada. Lo que quedó pendiente fue el **relleno por material** (3 de 7 capas con Section Style) y una geometría abierta. La regla que queda: cada material con su Section Style desde el arranque.

---

## 1. Fuentes

| Archivo | Ubicación | Qué es |
|---|---|---|
| `Casa frente al mar - Diego Arraigada_…pdf` | `G:\Mi unidad\E#E.EDU\mora\` | 6 págs A3 vertical. **Pág. 5** = planta baja + planta alta (con escala gráfica 0·1·2·5) + detalles. **Pág. 6** = vista NE + cortes D-D, E-E, F-F, G-G con cotas (+250, +263, +285, +295, +300 cm). **Pág. 2** = implantation. 11 imágenes, 4 fuentes |
| `3D-casa_uruguay.dwg` | `G:\Mi unidad\E#E.EDU\mora\` | El AutoCAD en el que se modela en paralelo |
| **`CAD-UY-xa-RHINO_02.dwg`** | `G:\Mi unidad\E#E.EDU\mora\` | **5,3 MB** · el AutoCAD con las entidades 3D ya avanzadas + el corte 2D de inicio. En **metros**. Importado en Rhino el 27/10 |
| **`3D-casa_uruguay_02.3dm`** | `G:\Mi unidad\E#E.EDU\mora\` | **Archivo de trabajo desde el 27/10** (0,8 MB): el 3D importado del DWG, donde se construye el corte y la hoja |
| `3D-casa_uruguay.3dm` | `G:\Mi unidad\E#E.EDU\mora\` | El Rhino del 26/10 con el PDF de Arraigada importado y calibrado (35 MB) |
| `primer intento madera.pdf` | `G:\Mi unidad\E#E.EDU\mora\` | 1 pág A2, 100 % vector, sin texto: un **corte** de casa de madera (referencia de sistema constructivo) |
| `ref/` | `G:\Mi unidad\E#E.EDU\mora\ref\` | Precedentes: Arraigada, Gago House (Pezo von Ellrichshausen) |

**Datos de la casa (ficha de la publicación):** Manantiales, Uruguay · 2011 · 140 m² · Diego Arraigada + colaboradores · construcción 2012/2013 · estructura de pino y eucalipto · exterior en chapa de fibras vegetales.

---

## 2. Estado verificado del archivo Rhino (2026-10-26)

| Dato | Valor |
|---|---|
| Documento | `G:\Mi unidad\E#E.EDU\mora\3D-casa_uruguay.3dm` (35 MB) |
| Unidades | **metros** (modelo); layout en mm |
| Objetos | 100.557 → 96.136 polylines + 3.001 hatches + 845 nurbs + 559 polylines + 1 brep + 1 extrusión |
| Capas con contenido | `3D-EST-MAD` 62.934 · `Default` 37.610 · `Layer 01` 1 |
| Capas creadas para el proyecto | 13 de material + 4 de referencia (ver §4) |
| Vistas | `Parallel`, `Top`, `Front`, `Left` |
| Páginas de layout | 0 (la hoja A3 se arma en la fase de corte) |
| Contenido | págs. 2, 5 y 6 del PDF importadas (emplazamiento, plantas, detalles y cortes) |

### 2.1 Calibración: verificada y correcta

La **escala gráfica** de cada planta mide **exactamente 5,000000 m** en el archivo importado:

| Barra | Extensión en X | Largo |
|---|---|---|
| PLANTA 1 | 13,281836 → 18,281836 | **5,000000 m** |
| PLANTA 2 | 13,281836 → 18,281836 | **5,000000 m** |

Las dos barras comparten el mismo span en X y los ticks interiores caen a 1,000 m y 2,000 m de la marca 0, que es exactamente el patrón `0·1·2·5` publicado. **El import está a escala real: no hace falta reescalar.**

Contraste visual: el ala de la casa mide aproximadamente el doble que la barra (≈10 m) y las dos alas más la terraza suman los 140 m² de la ficha.

### 2.2 Archivo de trabajo `3D-casa_uruguay_02.3dm` (2026-10-27)

| Dato | Valor |
|---|---|
| Documento | `G:\Mi unidad\E#E.EDU\mora\3D-casa_uruguay_02.3dm` |
| Origen | `File > Import` de `CAD-UY-xa-RHINO_02.dwg` (5,3 MB) |
| Unidades | el DWG está en **metros** → entra 1:1, sin conversión (escala verificada) |
| Contenido | entidades 3D de base + el corte 2D de inicio (según el usuario) |
| En curso | el **plano de corte** 3D → ver §9 de la guía de comandos |

**Bitácora del día:** §12 de [[proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/01-comandos-rhino-8|01-comandos-rhino-8]] — import ✅, escala ✅, verificación del contenido ⏳, plano de corte ⏳, capas + Section Style ⏳.

---

## 3. Procedimiento (para repetirlo)

### 3.1 Importar el PDF

1. `Import` → el PDF → **PDF Select Page**: `5,6` (la pág. 2 se importa si se quiere el emplazamiento).
2. **PDF Import Options**: Scale = *Fit to default screen* · **line weights OFF** (bug de Rhino 8: las curvas importadas aparecen muy gruesas) · fills = *Hatches* · **Load Text ON** (para leer rótulos y cotas).
3. Ajustar la escala con la escala gráfica: medir la barra (0 → 5) y `Scale1D` hasta 5,000 m. En este archivo ya quedó hecha.

### 3.2 Capas de material

Una capa por material, con **Section Style** propio → los cortes salen con hatch por material:

| Capa | Patrón | Color | Rotación | Escala |
|---|---|---|---|---|
| `EST-MAD` | Hatch1 (líneas) | 140 · 95 · 60 | 0° | 1,0 |
| `MAD-MARCO_PINO` | Hatch2 | 105 · 72 · 43 | 0° | 1,0 |
| `04-BAST-2.6` | Hatch1 | 160 · 160 · 160 | 0° | 1,0 |
| `05-AISL-LANAVID` | Hatch3 | 235 · 215 · 120 | 0° | 1,0 |
| `CARP-MET` | sólido | 70 · 70 · 70 | 0° | 1,0 |
| `CARP-VID` | sólido | 170 · 200 · 210 | 0° | 1,0 |
| `01-PLACA YESO` | sólido | 235 · 235 · 235 | 0° | 1,0 |
| `02-FENOLICO` | sólido | 90 · 60 · 40 | 0° | 1,0 |
| `03-FILM_POL` | sólido | 215 · 215 · 215 | 0° | 1,0 |
| `06 TYVEK` | sólido | 240 · 240 · 235 | 0° | 1,0 |
| `07-CALV-2.2` | sólido | 150 · 150 · 150 | 0° | 1,0 |
| `08-CHAPA-NEGRO` | sólido | 30 · 30 · 30 | 0° | 1,0 |
| `09-ZING-CHAPA_GALV` | sólido | 180 · 185 · 190 | 0° | 1,0 |

Referencias: `REF-PDF-P5`, `REF-PDF-P6`, `REF-TXT`, `00-EJES`.

---

## 4. Pendientes

| # | Tarea | Estado |
|---|---|---|
| 1 | Unidades en metros y capas con Section Style (archivo del 26/10) | ✅ |
| 2 | PDF importado y calibrado con la escala gráfica | ✅ |
| 3 | Importar `CAD-UY-xa-RHINO_02.dwg` en `3D-casa_uruguay_02.3dm` | ✅ 27/10 |
| 4 | Verificar qué entró (`What`, `SelClosedPolysrf`, `SelMesh`, `Layer`) | ⏳ |
| 5 | Recrear las 13 capas de material + Section Style en el archivo nuevo | ⏳ |
| 6 | Plano de corte 3D (`PlanoDelimitador` + `VerSeccionesDeCorte`) | ⏳ en curso |
| 7 | Separar el PDF importado en `REF-PDF-P5` / `REF-PDF-P6` | Pendiente |
| 8 | Redibujar la planta en las capas de material | Pendiente |
| 9 | Extruir a **sólidos** (`ExtrudeCrv` con tapa), alturas desde la pág. 6 | Pendiente |
| 10 | Hoja A3 a 1:50 con corte 3D y pie de página (reusando la vista de la hoja AIZ) | Pendiente |

---

## 5. Documentos del proyecto

| Documento | Qué resuelve |
|---|---|
| [[proyectos/MVP_05-rhino-mcp/02-CASA-URUGUAY/01-comandos-rhino-8\|01-comandos-rhino-8]] | Guía de comandos Rhino 8 del proyecto: **§9 el corte 3D** (plano delimitador: insertar, prender, apagar, configurar, y la familia `SeccionesDeCorte` → `VerSeccionesDeCorte` → `ExtraerSeccionesDeCorte` → `DibujosDeCorte`), **§12 bitácora viva** de `3D-casa_uruguay_02.3dm`, importar PDF y DWG, `Box` para parantes, `ExtrudeCrv`, `Offset` + `PlanarSrf` para dar espesor, **chapa sinusoidal** (alto de onda 0,036 m) paso a paso, **zinguerías** con `Sweep1`, `PushPull` / `MoveFace` / `Gumball`, cheatsheet y errores frecuentes |

---

## 6. Relaciones

- Procedimiento de cortes, hatch y hoja: [[proyectos/MVP_05-rhino-mcp/01-AIZ/01-playbook-cortes-rhino-8|01-playbook-cortes-rhino-8]]
- Operación del puente MCP: [[proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp|pbook-rhino-mcp]]
- Axonométrica militar 30/60: [[scripts/axonometria-militar-rhino_notas|axonometria-militar-rhino_notas]]
