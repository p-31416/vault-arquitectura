---
tipo: software
software: mcp-autocad
fecha_creacion: 2026-09-27
ultima_actualizacion: 2026-09-27
tags: [glosario, software, mcp, autocad, com, limuzi013, opencode]
---

# MCP autocad (limuzi013)

> Servidor MCP local que controla una sesión AutoCAD completa abierta vía COM. Lee y edita el dibujo activo; solo guarda dentro de una carpeta dedicada.

- [[#Resumen]]
- [[#Requisitos]]
- [[#Instalación]]
- [[#Configuración]]
- [[#Unidades y ángulos]]
- [[#Handles — cómo referenciar entidades]]
- [[#Índice de herramientas]]
- [[#Conexión]]
- [[#Documentos]]
- [[#Estado del dibujo]]
- [[#Geometría]]
- [[#Edición]]
- [[#Vista y feedback]]
- [[#Carpetas de salida (output jail)]]
- [[#Límites conocidos]]
- [[#Pilotos del estudio]]
- [[#Estado y verificación]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Resumen

`autocad-mcp` (autor: limuzi013, Apache-2.0, `autocad-mcp 0.1.0`) se conecta a una instancia de AutoCAD **ya abierta** en Windows y expone 30 herramientas con scope definido — no es un endpoint libre para ejecutar comandos AutoCAD. Toda llamada COM va serializada (la automatización es single-threaded). Es la vía principal para que el agente audite o dibuje sobre DWGs reales durante MVP_01/MVP_02.

## Requisitos

- Windows con **AutoCAD completo** (no LT) instalado.
- AutoCAD abierto con un dibujo activo antes de llamar cualquier herramienta.
- Python 3.10+.

## Instalación

Repo: `https://github.com/limuzi013/autocad-mcp`. En este vault vive fuera del git en `P:/00-repos/proyecto-pi/tools/autocad-mcp` y se instala en un venv dedicado:

```powershell
git clone https://github.com/limuzi013/autocad-mcp.git "P:\00-repos\proyecto-pi\tools\autocad-mcp"
py -3 -m venv "P:\00-repos\proyecto-pi\tools\autocad-mcp\.venv"
& "P:\00-repos\proyecto-pi\tools\autocad-mcp\.venv\Scripts\python.exe" -m pip install "P:\00-repos\proyecto-pi\tools\autocad-mcp"
```

Resultado: `autocad-mcp.exe` en el venv. Ese `.exe` es el que invoca OpenCode.

## Configuración

Bloque en `opencode.json`:

```json
"autocad": {
  "type": "local",
  "command": ["P:/00-repos/proyecto-pi/tools/autocad-mcp/.venv/Scripts/autocad-mcp.exe"],
  "env": { "ACAD_MCP_OUTPUT_ROOT": "P:/00-repos/proyecto-pi/vault-arquitectura/activos/caddy-salidas" },
  "enabled": true,
  "timeout": 20000
}
```

Nota Windows: en JSON usar barra `/` o escapar `\\`. El servidor rechaza paths fuera del output root (chequeo anti-`..`).

## Unidades y ángulos

- **Coordenadas y geometría** entran y salen en **milímetros** (compatible con la práctica del estudio).
- El servidor lee `INSUNITS` y convierte a la unidad del dibujo (con `INSUNITS=metres`, 1000 mm = 1 unidad). Los dibujos sin unidad pasan tal cual y se marcan en `get_active_drawing_info`.
- **Ángulos**: grados sexagesimales medidos CCW desde +X. Internamente ActiveX espera radianes — la conversión la hace el server.
- **Valores unitless** (`scale` de inserción, ratio de elipse) NO se convierten: la escala 1 = tamaño real del bloque, independientemente de `INSUNITS`.

## Handles — cómo referenciar entidades

`query_entities` devuelve **handles AutoCAD estables** (no son selection sets volátiles). Para apuntar a una entidad concreta después: `set_entity_layer`, `erase_entity`, `move_entity`, `copy_entity`. Sin handles no hay forma estable de referirse a un objeto entre llamadas.

`query_entities` corta en `max_scan` (default 5000) y reporta:
- `total_in_space`: total de entidades en el espacio.
- `scanned`: cuántas examinó realmente.
- `truncated`: true si paró antes del final.
- `stopped_by`: `"limit"`, `"max_scan"` o null.

## Índice de herramientas

| Área | Herramienta |
|---|---|
| Conexión | [[#autocad_status]] · [[#list_open_drawings]] · [[#get_active_drawing_info]] |
| Documentos | [[#create_new_drawing]] · [[#open_drawing]] · [[#save_active_drawing]] · [[#save_drawing_as]] |
| Estado del dibujo | [[#list_layers]] · [[#create_layer]] · [[#set_current_layer]] · [[#set_layer_properties]] · [[#list_blocks]] · [[#list_layouts]] · [[#query_entities]] · [[#set_entity_layer]] |
| Geometría | [[#draw_line]] · [[#draw_circle]] · [[#draw_arc]] · [[#draw_ellipse]] · [[#draw_polyline]] · [[#draw_point]] · [[#draw_text]] · [[#insert_block]] · [[#add_linear_dimension]] |
| Edición | [[#erase_entity]] · [[#move_entity]] · [[#copy_entity]] |
| Vista y feedback | [[#zoom_extents]] · [[#capture_screenshot]] |

---

## Conexión

### autocad_status

Verifica la conexión con la sesión AutoCAD abierta y reporta el dibujo activo.

- **Sin parámetros.**
- **Uso:** primera llamada tras cambios de sesión; diagnóstico rápido.

### list_open_drawings

Lista todos los DWGs abiertos en la sesión.

- **Sin parámetros.**
- **Uso:** saber qué dibujo atender antes de operar.

### get_active_drawing_info

Devuelve metadata y unidades del dibujo activo (incluye `INSUNITS`).

- **Sin parámetros.**
- **Uso:** confirmar unidad de dibujo (mm vs unitless) antes de insertar geometría — clave para que la conversión mm→drawing unit aplique bien.

---

## Documentos

### create_new_drawing

Crea y activa un dibujo nuevo en blanco. Usa template métrico local por defecto.

- `template_path` (opcional): ruta absoluta a un `.dwt` existente.
- **Uso:** abrir sesión de auditoría sobre un DWG limpio.

### open_drawing

Abre un `.dwg` o `.dxf` existente.

- `path`: ruta absoluta local al archivo.
- **Uso:** cargar el DWG que vas a auditar. Recordá: trabajá sobre copia.

### save_active_drawing

Guarda el dibujo activo en su ruta actual.

- **Sin parámetros.** In-place, undoable en AutoCAD.
- **Uso:** punto de guardado intermedio (mejor que `save_drawing_as`).

### save_drawing_as

Guarda el dibujo activo bajo el output root (output jail).

- `path`: ruta `.dwg`/`.dxf` **relativa** a `ACAD_MCP_OUTPUT_ROOT` (anti-`..` enforced).
- `allow_overwrite` (default false): permite pisar archivos existentes.
- **Uso:** única vía para escribir DWGs. Verificá `allow_overwrite` antes de aprobar.

---

## Estado del dibujo

### list_layers

Lista todas las layers con color ACI, lock, freeze y visibilidad.

- **Sin parámetros.**
- **Uso:** piloto A — auditar nombres existentes contra el spec SET_01.

### create_layer

Crea una layer o devuelve la existente con el mismo nombre.

- `name` (requerido): nombre de la layer.
- `color_aci` (opcional, 1–255): color AutoCAD Color Index.
- `make_current` (opcional): la deja como layer activa.
- **Uso:** materializar specs de capa desde cero.

### set_current_layer

Hace current una layer existente.

- `name`: nombre de layer existente.
- **Uso:** asegurar que la próxima geometría va a la capa correcta.

### set_layer_properties

Cambia color, lock, freeze o visibilidad de una layer existente. Al menos una propiedad requerida.

- `name`: layer existente.
- `color_aci` (1–255): color ACI.
- `locked`: visible pero no editable.
- `frozen`: oculta y no regenera (más fuerte que off).
- `visible`: false apaga la layer pero la deja thawed.
- **Uso:** correcciones masivas por lote (ej: apagar `G-AUXI` antes de plot).

### list_blocks

Lista definiciones de bloque en el dibujo activo.

- **Sin parámetros.**
- **Uso:** verificar qué bloques están definidos antes de `insert_block`.

### list_layouts

Lista los layouts: tab Model + paper-space, con dispositivo de plot y tamaño de papel.

- **Sin parámetros.**
- **Uso:** inventario de láminas para auditoría de presentación.

### query_entities

Lista entidades en model o paper space; devuelve handles estables.

- `space` (`model`/`paper`, default `model`).
- `limit` (1–1000, default 200): tope de entidades reportadas.
- `object_name` (opcional): nombre COM exacto (ej `AcDbLine`).
- `layer` (opcional): nombre exacto de layer.
- `max_scan` (1–200000, default 5000): corte de seguridad si el escaneo se vuelve caro.
- **Devuelve:** `total_in_space`, `scanned`, `truncated`, `stopped_by`.
- **Uso:** piloto A — barrer `R-EJES` y exportar a reporte de auditoría.

### set_entity_layer

Mueve una entidad (por handle) a otra layer existente.

- `handle`: handle devuelto por `query_entities` o una herramienta de dibujo.
- `layer`: nombre de layer existente.
- **Uso:** normalizar capas antes de validar contra spec.

---

## Geometría

### draw_line

Dibuja una línea recta.

- `start_mm`, `end_mm`: puntos en mm (`[x,y]` o `[x,y,z]`).
- `layer`, `space` (opcionales).
- **Uso:** ejes, líneas auxiliares.

### draw_circle

Dibuja un círculo.

- `center_mm`: centro en mm.
- `radius_mm` (>0): radio en mm.
- `layer`, `space` (opcionales).
- **Uso:** shafts,柱子, pre-armado.

### draw_arc

Dibuja un arco CCW desde `start_angle_deg` hasta `end_angle_deg`.

- `center_mm`: centro en mm.
- `radius_mm` (>0): radio en mm.
- `start_angle_deg`, `end_angle_deg`: grados CCW desde +X.
- `layer`, `space` (opcionales).
- **Uso:** trazas curvas, encuentros.

### draw_ellipse

Dibuja una elipse completa con semi-ejes en mm.

- `center_mm`: centro en mm.
- `major_axis_mm` (>0): semi-eje mayor.
- `minor_axis_mm` (>0, ≤ major): semi-eje menor.
- `rotation_deg` (default 0): rotación CCW del eje mayor desde +X.
- **Uso:** mesas elípticas, vanos especiales.

### draw_polyline

Polilínea 2D ligera (LWPOLYLINE).

- `vertices_mm`: array de puntos mm (≥2).
- `closed` (default false): cierra al primer vértice.
- `layer`, `space` (opcionales).
- **Uso:** muros, contornos, losas — la base del dibujo arquitectónico (preferir `PLINE` siempre).

### draw_point

Punto singular. Render depende de `PDMODE`/`PDSIZE` del dibujo (default: un solo píxel).

- `point_mm`: coordenada mm.
- `Uso:** replanteo, puntos de nivel (atributos complementarios mejor — ver `insert_block` con `R-PTO-ATTR`).

### draw_text

Texto de una línea.

- `text` (requerido): cadena.
- `insertion_point_mm`: punto mm.
- `height_mm` (>0): altura en mm.
- `layer`, `space` (opcionales).
- **Uso:** rótulos, ejes (mejor con `insert_block` + atributo para `DATAEXTRACTION`).

### insert_block

Inserta una referencia a un bloque ya definido en el dibujo (`list_blocks` para nombres).

- `block_name` (requerido): nombre del bloque existente.
- `insertion_point_mm`: punto mm.
- `scale` (default 1, unitless): 1 = tamaño real del bloque, sin importar `INSUNITS`.
- `rotation_deg` (default 0): rotación CCW sobre el punto de inserción.
- `layer`, `space` (opcionales).
- **Uso:** puertas, ventanas, marcas de eje (`R-EJE-MARCA`), puntos con atributos.

### add_linear_dimension

Cota lineal entre dos puntos.

- `start_mm`, `end_mm`: puntos en mm.
- `dimension_line_point_mm`: ubicación de la línea de cota (offset).
- `orientation`: `aligned` (default), `horizontal`, `vertical`, `rotated`.
- `rotation_deg` (solo con `rotated`): ángulo de medición.
- `layer`, `space` (opcionales).
- **Devuelve:** valor medido en mm.
- **Uso:** acotar replanteo, validar contra spec (`EP-ARQ`).

---

## Edición

### erase_entity

Borra una entidad por handle. Edit normal AutoCAD (undoable desde AutoCAD; este servidor no puede revertirla).

- `handle` (requerido).
- **Uso:** limpieza selectiva. Mitigación: copias del DWG + aprobación manual.

### move_entity

Mueve una entidad por el vector `from_mm → to_mm`.

- `handle`, `from_mm`, `to_mm`.
- Para mover por desplazamiento, pasar `from_mm=[0,0]` y `to_mm=desplazamiento`.
- **Uso:** recolocar después de auditoría.

### copy_entity

Copia una entidad (queda en el mismo space; con `displacement_mm` se ubica offset).

- `handle` (requerido).
- `displacement_mm` (opcional): offset aplicado a la copia.
- **Uso:** replicar bloques para variaciones.

---

## Vista y feedback

### zoom_extents

Hace zoom para encuadrar todo el contenido visible del dibujo activo.

- **Sin parámetros.**
- **Uso:** antes de `capture_screenshot` para devolver una vista completa al usuario.

### capture_screenshot

Captura la ventana de AutoCAD y devuelve la imagen como adjunto MCP.

- `width_px` (200–2400, default 1400): ancho de la captura (downscaling).
- **Devuelve:** nota si la ventana estaba minimizada/oculta.
- **Uso:** feedback visual para el humano — útil cuando una operación tiene resultado ambiguo.

---

## Carpetas de salida (output jail)

`ACAD_MCP_OUTPUT_ROOT` define el directorio permitido para `save_drawing_as`. Todo path relativo se resuelve contra esa raíz y se rechaza si sale fuera (chequeo anti-`..`).

**Reglas del estudio:**
- Carpeta dedicada: `activos/caddy-salidas/` (gitignored).
- Guardar **siempre sobre copias** del DWG original, nunca sobre la copia maestra.
- Aprobación manual antes de cada `save_drawing_as` o `erase_entity`.

## Límites conocidos

- No incluye **sombreados, impresión, xrefs ni sólidos 3D**.
- Requiere AutoCAD completo (no LT).
- Single-thread: las llamadas se serializan automáticamente.
- Compatible declarado con **AutoCAD 2026** vía `acax25enu.tlb`. En este vault corre contra **2027** (`acax26enu.tlb`): funciona hasta que la API rompa compatibilidad entre versiones de type library.

## Pilotos del estudio

- **Caso A — auditoría R-EJES:** `list_layers` + `query_entities(layer="R-EJES")` → comparar contra spec SET_01 (Green 3, CONTINUOUS, 0.50) y reportar delta. Cruzar con `mcp-autodesk-help` para citas oficiales de `STANDARDS`/`CHECKSTANDARDS`.
- **Caso B — tabla XP métrica:** verificar que `SCALELISTEDIT` tiene 1:25 / 1:50 / 1:100 / 1:200 / 1:1.25. Procedimiento documentado en la guía raw MCP §3.3.

## Estado y verificación

- ✅ instalado y conectado (`mcp list` 6/6, 2026-09-27).
- ⚠️ pendiente prueba funcional con AutoCAD 2027 abierto: requiere `autocad_status` con dibujo activo (validación `acax26enu.tlb`).
- `opencode mcp debug autocad` — solo para servidores remotos; este es local, usar `mcp list`.

---

## Conceptos relacionados

- [[wiki/glosario/software/opencode|opencode]]
- [[wiki/glosario/software/mcp-autodesk-help|mcp-autodesk-help]]
- [[wiki/glosario/software/autocad|autocad]]
- [[proyectos/MVP_02-autocad-standards/readme-mvp_02|MVP_02 — Estándares AutoCAD]]

## Referencias

- Repo oficial: https://github.com/limuzi013/autocad-mcp (Apache-2.0)
- README del repo (firmas, unidades, herramientas): https://github.com/limuzi013/autocad-mcp/blob/main/README.md (verificado 2026-09-27)
- Guía raw del vault MCP: `raw/docs/Estudio Pi – Guía de conexiones MCP.md` §3.3
- OpenCode MCP servers: https://opencode.ai/docs/mcp-servers/ (verificado 2026-09-27 — 200)
