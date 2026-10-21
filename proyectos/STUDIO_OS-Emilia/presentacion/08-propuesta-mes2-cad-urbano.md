---
tipo: presentacion
cliente: Emilia Pimenta
proyecto: Studio OS
ciudad: Argentina
pais: AR
fase: propuesta
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
estado: propuesta
tags: [propuesta, mes2, autocad, set_04, urb, rhino, comfyui, concurso, gaudi-nexus]
idioma: es
---

# Propuesta Mes 2 (CAD) — del replanteo a la escala urbana

> **Nota corta:** el trabajo de CAD del Mes 2 propone **una sola arista** — llevar el mismo sistema de SET_01 (capas, DWT/DWS, LISP, bloques con atributos, cómputos) a la **escala urbana**, trabajando sobre el **plano 2D de Barcelona** del concurso. Ese plano 2D alimenta el **3D en Rhino** (MCP ya instalado) y de ahí las imágenes con **ComfyUI** (LoRA `rhino-to-image` ya analizado). Es decir: **CAD → Rhino → ComfyUI**, con la misma lógica de capas y bloques en el primer eslabón.
> Dashboard donde vive: `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-autocad.html` (§11).
> Medición de hoy: `raw/reports/barcelona-2d.audit.md` (+ `.json`).

---

## 1. La idea en una frase

SET_01 demostró que el sistema funciona a escala de replanteo (un edificio, 28 locales, 42 carpinterías, 12-15 h de ahorro por plano). El **Mes 2 propone el mismo sistema a escala urbana** —40 km de ciudad en el `Barcelona-2D.dwg`— porque ahí es donde el concurso lo necesita, y porque el caso urbano **estresa** cada pieza del sistema: capas, escalas, bloques, rótulos y cómputos.

Es el "un tipo de plano bien usado en CAD" que quedó como compromiso del Mes 1, aplicado al archivo que ya tenemos.

---

## 2. Lo medido hoy (no supuesto)

Método ODA File Converter → DXF → ezdxf 1.4.4, DWG intacto, igual que la auditoría de REP-ARAOZ.

| Dato | `Barcelona-2D.dwg` | `REP-ARAOZ.dwg` (replanteo) |
|---|---|---|
| Tamaño | 27,9 MB (DXF 176 MB) | ~2 MB |
| **Capas** | **96** | 29 propias + 21 de fondo |
| **Entidades** | **162.396** | ~1.360 |
| Bloques definidos | 46 (38 con nombre + 8 anónimos) | 14 |
| INSERTs | 1.344 | 203 |
| TEXT / MTEXT | 34.574 / 547 | 83 / 26 |
| HATCH | 43.032 | 23 |
| Extensión | **40,4 × 38,7 km** (X 409.693→450.137 m · Y 4.560.549→4.599.261 m) | un edificio de 9 pisos |
| Layouts | 1 (`Layout1`) | 2 (`REP-PTipo-A1-H` + replanteo) |
| Unidades | `$INSUNITS` 6 (m) · `$MEASUREMENT` 0 (imperial) | `$INSUNITS` 6 (m) |
| Capas del SET_01 presentes | **0 de 22** | 22 de 22 |

**Reparto real de las 162.396 entidades:** 75.228 polilíneas + 43.032 hatches + 34.574 textos + 7.213 líneas + 1.344 inserts + 547 mtexts + 316 sólidos + 99 círculos + 42 puntos + 1 spline.

**Las capas que importan para el concurso** (nombres reales, en catalán): `Estacions Metro` (492 inserts) · `Mercats Municipales` → `Mercats Municipals` · `Monuments` · `Corbes de nivell` · `Línies de Projectes` · `Parterres (Carrers i Places)` · `Zona Verd Públic` · `Cobertes Edificis` · `Numeració postal Districte 1..10` · `Túnels - Rondes - Vies ferries - Escales`.

**Los 38 bloques con nombre** (el catálogo heredado): `metro` · `ffcc` · `renfe` · `tramvi` · `funicu` · `taxi` · `torre1` `torre2` · `mariti` · `aeropo` · `ascens` · `hospi` · `seu` · `escala` · `blau` · `ptoalt` · `telefe` · `l1`…`l11` · `t1`…`t6`.

> **Conclusión de la medición:** la escala urbana es **120× más densa** que el replanteo y usa una taxonomía **temática y funcional** (qué cosa es: manzanas, parterres, equipamientos, red viaria), no de dibujo (muros, cotas, vanos). El sistema del SET se replica: cambian las **capas** y la **escala**; la mecánica (DWT/DWS + LISP + bloques con atributos + cómputos) se mantiene.

---

## 3. Qué cambia y qué no a escala urbana

| Pieza | SET_01 (replanteo) | SET_04 (urbano, propuesta) |
|---|---|---|
| Taxonomía de capas | de dibujo (`A-MURO`, `A-CARP-02`, `REP-COTAS`) | **temática + de propuesta** (`URB-*` base heredada, `PRO-*` lo que diseñamos) |
| Escala de trabajo | 1:50 con escala custom `1:50 (m)` | 1:500 / 1:1000 / 1:5000 (plaza, barrio, ciudad) |
| Soporte del fondo | xref `ARQ-ARAOZ` | xref de la cartografía (el 2D va de fondo, no en el DWG de trabajo) |
| Bloques | 13 + `SIMB-LOC_ID` (número visible, nombre invisible) | 38 heredados **renombrados con prefijo** + bloques de la propuesta |
| Cómputo | cuadro de carpinterías y de locales (atributos) | **cuadro urbano**: m² de plaza, equipamientos por tipo, cobertura verde, arbolado |
| LISP | 4 LSP (twist, locales, giros, tabla de niveles) | 4 LSP nuevos, **derivados** de los que ya funcionan |
| DWT / DWS | `SET_01-REP.dwt` + `SET-REP.dws` | `SET_04-URB.dwt` + `SET-URB.dws` (mismo generador ya automatizado) |

---

## 4. La propuesta concreta: `SET_04-URB`

### 4.1 Capas (propuesta de juego, ~26 propias)

| Familia | Capas | Origen |
|---|---|---|
| `URB-` (base, heredada del 2D) | `URB-EDIFICI` · `URB-PARTERRE` · `URB-VIA` · `URB-EQUIP` · `URB-VERD` · `URB-MOBILIARI` · `URB-PLAZA` | mapeo de las 96 capas catalanas a una taxonomía del estudio (el 2D entra como xref de fondo) |
| `PRO-` (la propuesta) | `PRO-MERCAT` · `PRO-CULTURA` · `PRO-ESPACIO-PUBLICO` · `PRO-VEGETACION` · `PRO-MOBILIARIO` · `PRO-PAVIMENTO` · `PRO-ARBOLADO` | lo que dibujamos |
| `REF-` (referencia, no se imprime) | `REF-CARTO` · `REF-3D` · `REF-COTES-URB` | referencias |

> El 2D con 96 capas **no se renombra a mano**: se deja como xref de fondo y el juego de trabajo se construye encima. Eso evita 96 capas huérfanas y mantiene el DWT liviano.

### 4.2 DWT / DWS

- `SET_04-URB.dwt`: metros (`INSUNITS 6`), escalas custom `1:500 (m)` / `1:1000 (m)` / `1:5000 (m)`, layout `URB-A1` (A1 apaisado) + viewport de la plaza a 1:500, xref de la cartografía en `REF-CARTO`, y el juego de capas `URB-`/`PRO-` con los bloques de la propuesta en memoria.
- `SET-URB.dws`: la norma que AutoCAD hace cumplir sola (misma mecánica que `SET-REP.dws` + `CHECKSTANDARDS`).
- **Se reutiliza el generador que ya existe**: `scripts/genera-template-set01.py` (verificado ida/vuelta con ODA+ezdxf) → el costo de crear el template urbano es bajo.

### 4.3 LISP (4, todos derivados de los que ya funcionan)

| LSP | Qué hace | Se deriva de |
|---|---|---|
| `SET-04-URB.lsp` (`SET-URB`) | crea las ~26 capas propias + variables + verifica | `SET-01-REP.lsp` (`SET-REPLANTEO`) |
| `SET-04-RESUMEN-URB.lsp` (`RESUMEN-URB`) | **el cuadro urbano**: m² por capa, cantidad de equipamientos por tipo, cobertura verde, arbolado → tabla dentro del DWG + CSV | `SET-01-CUADRO-NIVELES.lsp` (lee CSV, dibuja tabla) |
| `SET-04-VISTAS.lsp` (`VISTAS-URB`) | genera las ventanas de trabajo por escala (plaza 1:500 / barrio 1:1000 / ciudad 1:5000) en el layout | `SET-01-HORIZ.lsp` (twist/viewport) |
| `SET-04-PLACA.lsp` (`PLAZA-PLACA`) | recorta y prepara el polígono de la plaza de la Sagrada Família + su entorno inmediato (el objeto del concurso) | `SET-01-SIMB-LOC-ID.lsp` (interactivo, con control) |

### 4.4 Bloques

| Bloque | Qué es | Estado |
|---|---|---|
| 38 heredados (`metro`, `ffcc`, `renfe`, `tramvi`, `funicu`, `taxi`, `torre1/2`, `mariti`, `aeropo`, `ascens`, `hospi`, `seu`, `escala`, `blau`, `ptoalt`, `telefe`, `l1`–`l11`, `t1`–`t6`) | se renombran con prefijo (`URB-METRO`, `URB-FFCC`, …) y se documentan en la tabla de bloques | heredar + renombrar |
| `PRO-MERCAT` | volumetría del mercado de proximidad (el programa del concurso) | crear |
| `PRO-CULTURA` | centro de cultura digital | crear |
| `PRO-ESPACIO-PUBLICO` | plaza / espacio de convivencia | crear |
| `PRO-MOBILIARIO` | **mobiliario urbano** — el objeto del **premio especial** del concurso ("mejor mobiliario u objeto arquitectónico") | crear, con atributos (`MATERIAL`, `CANT`, `COSTO`) → entra al cuadro urbano |
| `PRO-ARBOL` | arbolado con atributo de especie | crear |

> **Por qué el bloque de mobiliario importa:** el concurso premia específicamente el mobiliario. Un bloque con atributos (material, cantidad, costo) es exactamente lo que el sistema de SET_01 produce: la idea de premio del concurso y la del cuaderno de standards son la misma cosa.

---

## 5. La cadena: CAD → Rhino → ComfyUI

```
Barcelona-2D.dwg (cartografía de fondo, 40 km)
        │  ← AutoCAD: xref + capas PRO- + bloque de propuesta + vista de la plaza
        ▼
   SET_04-URB.dwg  (plano urbano de trabajo: plaza, mercado, cultura, mobiliario)
        │  ← export DXF / vista
        ▼
   Rhino 8 + MCP  (volumetría: MCPConnect, capas, GH)   ← MCP YA INSTALADO
        │  ← 3 pasadas desde la misma cámara (geo_shaded, geo_lines, + foto de material)
        ▼
   ComfyUI: FLUX.2 klein 9B + LoRA rhino-to-image (arcilla → hiperreal)
        │
        ▼
   Lámina A1 del concurso (JPG/PNG de resolución limitada — entrega protegida)
```

**Lo que ya está listo en cada eslabón:**

| Eslabón | Estado | Dónde |
|---|---|---|
| CAD | SET_01 completo (DWT/DWS + 4 LSP + bloques + cómputos) | `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/` |
| Rhino | MCP instalado y documentado (`MCPConnect`, `get_scene_summary`, capas, GH) | `proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp.md` + `scripts/rhino-mcp-cli.py` |
| ComfyUI | LoRA `rhino-to-image` analizado (rank 16, FLUX.2 klein 9B); workflow JSON construido y validado contra el código local | `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/` |

**Lo que falta en cada eslabón:**

- **CAD**: el `SET_04-URB` (capas, DWT/DWS, LISP, bloques) → es lo que propone este documento.
- **Rhino**: 3 capturas desde la misma cámara + foto de material (precondición del flujo). El MCP no reemplaza la exportación: hay que capturar en Rhino.
- **ComfyUI**: stack de 18,3 GB en RunPod (3090, $0,22/h), LoRA copiado a `models/loras/`, trigger word a confirmar con el instructor, y las 3 pasadas de calibración A/B/C/D.

---

## 6. Cómo visualizar la escala urbana con ComfyUI (el análisis)

Es la pregunta abierta del planteo. La respuesta corta: **la escala urbana no es un problema de LoRA, es un problema de control de líneas**. Y ahí la arquitectura de modelos que ya tenemos en el vault separa bien los casos:

| Qué se quiere | Herramienta correcta | Por qué | Estado en el vault |
|---|---|---|---|
| **Plano ilustrado / planta coloreada** de la plaza | **SDXL + ControlNet** (canny / depth / scribble) sobre el DXF exportado a PNG | la fidelidad del trazo la da el ControlNet; el LoRA no controla líneas | controlnet-canny/depth/scribble + Juggernaut-XL v9 ya instalados; `n_03` validó canny 0.3 + depth 1.0 |
| **Axonométrica / vista aérea de la propuesta** | **FLUX.2 klein 9B + LoRA `rhino-to-image`** (3 pasos: capturar → arcilla → hiperreal) | el LoRA da materialidad y el "sello propio"; la geometría entra por `ReferenceLatent` | workflow JSON validado; falta stack + LoRA + capturas |
| **Croquis → render** (volumen rápido de coherencia) | **SD1.5 img2img** (denoise 0.6-0.75, ImageScale 512) | rápido en la RX 570 (77-221 s) | probado en `n_02` y `n_06` (23 imágenes) |
| **Serie / consistencia** entre láminas | **controlnet-canny + IPAdapter** + seeds fijas | para que planta, axonométrica y vista aérea se lean como el mismo proyecto | IPAdapter ausente (pendiente en backlog) |

**Límite técnico que define la frontera:** FLUX.2 **klein** 9B **no tiene ControlNet nativo** (solo `ReferenceLatent`), así que para el plano que exige fidelidad de trazo el modelo correcto es **SDXL + ControlNet** (o FLUX.2 dev + ControlNet Union). El LoRA del curso entra donde aporta: **materialidad y estilo**, no geometría. Regla del curso que ya está copiada al vault: *"the clay is the base for the edit LoRA: keep it clean, monochrome, edge-legible, camera + footprint 1:1"* → en escala urbana, la **arcilla monocolor legible de bordes** es el paso intermedio ideal para leer la volumetría de la plaza antes de texturizar.

**Orden de trabajo que se propone** (de lo rápido a lo caro):

1. **Croquis / axonometría rápida** (SD1.5 img2img, local, minutos) → para decidir forma.
2. **Plano ilustrado** (SDXL + ControlNet sobre el DXF, local o pod) → para decidir el dibujo de la lámina.
3. **Volumetría en Rhino + arcilla** (MCP + 3 capturas) → para decidir la materialidad.
4. **Hiperreal / vista aérea** (klein 9B + LoRA, pod 3090) → para la lámina final.

**Sobre la vista aérea en concreto:** es el paso 3-4. La aerial no se genera "directo": sale de la geometría (Rhino) con cámara alta y el LoRA de materialidad. Intentar generarla solo desde texto es lo que produce el "look IA notoria" que la reunión del 16/10 dejó como criterio a descartar.

---

## 7. Cómo se conecta con el concurso

| Dato del concurso | Dónde lo produce esta cadena |
|---|---|
| **"Mercado de Proximidad y Centro de Cultura Digital"** | bloques `PRO-MERCAT` y `PRO-CULTURA` en SET_04 + volumetría en Rhino |
| **Reconfiguración del entorno urbano circundante de la Plaza de la Sagrada Família** | `PRO-ESPACIO-PUBLICO` + `SET-04-PLACA.lsp` (el recorte de la plaza) + vista aérea final |
| **Premio especial al mejor mobiliario u objeto arquitectónico** | bloque `PRO-MOBILIARIO` con atributos → es a la vez el objeto que se premia y la pieza que entra al cuadro urbano |
| **Lógica constructiva paramétrica de Gaudí** | la arcilla monocolor (paso 2 del flujo del curso) es exactamente el lenguaje de representación paramétrica: forma legible, sin textura, para discutir geometría |
| **Entrega 16/12/2026** (lámina A1, JPG/PNG limitado) | el DWT `URB-A1` + viewport 1:500 + el flujo de exportación protegida ya definido en el plan del concurso (F3) |

---

## 8. Primeros pasos (propuesta de orden, a validar)

| # | Paso | Pieza | Tamaño |
|---|---|---|---|
| 1 | Decidir el **recorte de trabajo**: ¿plaza (1:500), barrio (1:1000) o ciudad (1:5000)? | decisión de estudio | 1 pomodoro |
| 2 | Auditar el **2D** como base: 96 capas → mapeo a `URB-*` | `scripts/audita-dwg.py` (ya anda) + tabla de mapeo | 2 pomodoros |
| 3 | Crear `SET_04-URB.dwt` + `SET-URB.dws` | reutilizando `scripts/genera-template-set01.py` | 2 pomodoros |
| 4 | `SET-04-URB.lsp` (crea las 26 capas) | derivados de `SET-REPLANTEO` | 1 pomodoro |
| 5 | Bloques de la propuesta (6) + renombrar los 38 heredados | tabla de bloques al estilo de `bloques-personalizados.md` | 3 pomodoros |
| 6 | `RESUMEN-URB.lsp` (el cuadro urbano) | sobre el patrón de `CUADRO-NIVELES` | 2 pomodoros |
| 7 | Puente a Rhino: exportar DXF + abrir en Rhino 8 + `MCPConnect` | `scripts/rhino-mcp-cli.py` | 1 pomodoro |
| 8 | 3 capturas desde la misma cámara + foto de material | precondición del WF | 1 pomodoro |
| 9 | Primera corrida klein 9B + LoRA en el pod (3090, $0,22/h) | calibración A/B/C/D | 2 pomodoros |

**Criterio de cierre de la arista:** *un tipo de plano bien usado a escala urbana* → la plaza de la Sagrada Família resuelta en `SET_04-URB` (planta + axonométrica + vista aérea) con la cadena CAD → Rhino → ComfyUI corriendo de punta a punta y documentada para el que venga después.

---

## 9. Archivos y fuentes

| Qué | Dónde |
|---|---|
| Medición del 2D (reporte + JSON) | `raw/reports/barcelona-2d.audit.md` · `raw/reports/barcelona-2d.audit.json` |
| Plan del concurso (bases, hitos, entregables) | `specs/261019-plan-concurso-gaudi-nexus-ia.md` |
| Rhino MCP (playbook + scripts) | `proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp.md` · `scripts/rhino-mcp-cli.py` |
| ComfyUI: flujo Rhino→imagen | `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/00-README.md` |
| LoRA del curso (ficha técnica y licencia) | `wiki/glosario/software/lora-rhino-to-image-gaudi.md` |
| Sistema de SET_01 que se replica | `proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/` · `wiki/glosario/interno/pbooks/pbk-set01-rep.md` |
| Dashboard | `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-autocad.html` |
