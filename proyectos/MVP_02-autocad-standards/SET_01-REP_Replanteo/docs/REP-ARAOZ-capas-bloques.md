---
tipo: metodologia
mvp: 02
set: SET_01-REP
fecha_creacion: 2026-10-13
ultima_actualizacion: 2026-10-13
tags: [mvp_02, SET_01, replanteo, autocad, capas, bloques, ventana, dinamico, wipeout, attsync, dimstyles, textstyles, glosario, paso-a-paso]
archivo_origen: G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg
metodo: ODA-FileConverter-25.12-DWG-a-DXF + ezdxf-1.4.4 (AutoCAD LT sin COM, MCP sin sesion)
estado: v0.5-revision-usuario (tags+atajos+auditoria+backlog+bloques-aparte)
---

# REP-ARAOZ — TODAS las capas y bloques + VENTANA BAJA SIMPLE

> Documento único del plano. Vive en `SET_01/docs/`, wiki intacta.
> Origen: `G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg` (externo, fuera de git).
> Método: el MCP de AutoCAD pide AutoCAD completo abierto (ver [[wiki/glosario/software/mcp-autocad|mcp-autocad]]); con LT de prueba responde sin sesión, así que se convirtió copia a DXF con ODA en `%TEMP%` y se leyó con `ezdxf`. El DWG original queda intacto.
> Lectura: `AC1032`, `$INSUNITS 6` (metros), `$MEASUREMENT 1` (métrico), layout `REP-PTipo-A1`.
> Totales medidos: **49 capas**, **13 bloques nombrados** (+352 anónimos de dinámicos/xref), **208 INSERTs** en model, 304 `DIMENSION`, 83 `TEXT`, 26 `MTEXT`, 23 `HATCH`.

## 1. TODAS las capas (49)

Leyenda estado: `on/fz/lk` = encendida, congelada, bloqueada. Uso = lectura de uso en este plano.

### 1.1 Propias del REP (29)

| Capa | Color | Tipo línea | Estado | Entidades model | Uso en REP-ARAOZ |
|---|---|---|---|---|---|
| `0` | 7 | Continuous | on | 254 | Base general del dibujo |
| `0-REF` | 7 | Continuous | on | 1 | Inserción del xref `ARQ-ARAOZ` |
| `A-CARP-02` | 251 | Continuous | on | 56 | Carpinterías: 20 ventanas + 22 puertas dinámicas |
| `A-COTA-1-50` | 250 | Continuous | on | 142 | Cotas del plano 1:50 + 5 tags `C40.20` |
| `A-EJES` | 90 | DASHDOT | on, lk | 13 | Ejes arquitectónicos |
| `A-EJES-VACIOS` | 113 | DASHDOT | on, lk | 10 | Ejes de vacíos |
| `A-EQUIP-` | 8 | Continuous | on | 67 | Equipamiento de fondo |
| `A-MURO-MAMP` | 24 | Continuous | on | 289 | Muros de mampostería, la masa mayor del plano |
| `A-MURO-MED` | 11 | Continuous | on, lk | 25 | Muros medianeros |
| `A-SIMBOLO-NPT-PLANTA` | 251 | Continuous | on | 55 | 29 tags de nivel de piso terminado |
| `A-SOLADOS` | 250 | Continuous | on | 11 | Solados de fondo |
| `A-TERRENO` | 163 | Continuous | on, fz | 4 | Terreno como referencia (congelada) |
| `AR-CUADRO DE VANO` | 1 | Continuous | on | 0 en model* | Atributos `ALFEIZAR/ALTURA` de puertas |
| `CONDUCTOS` | 3 | Continuous | on | 26 | Conductos de fondo |
| `Defpoints` | 7 | Continuous | on | 27 | Nodos de cotas (no ploteable por definición) |
| `E-COL` | 5 | Continuous | on | 22 | Columnas + 21 tags `C40.20` |
| `E-COL-EJES` | 254 | Continuous | on, lk | 0 en model* | Ejes de columnas |
| `E-COL-H` | 251 | Continuous | on, lk | 0 en model* | Columnas en hatch/proyección |
| `E-EJES` | 10 | Continuous | on, fz | 30 | Ejes estructurales + 20 marcas de eje |
| `E-TAB` | 166 | Continuous | on | 6 | Tabiques estructurales |
| `E-TAB-H` | 251 | Continuous | on, lk | 8 | Tabiques en hatch/proyección |
| `IE-EJEX` | 32 | DASHDOT | on, fz+lk | 14 | Ejes de instalaciones eléctricas |
| `REP-COTAS` | 41 | Continuous | on | 155 | Cotas de replanteo (parciales + acumuladas) |
| `REP-EJES` | 81 | DASHDOTX2 | on, lk | 12 | Ejes de replanteo. Canónico v2.2, se conserva |
| `ROT-HOJA` | 5 | Continuous | on | paper | Recuadro rótulo A-434 / IRAM 4508 |
| `ROT-TXT` | 174 | Continuous | on | paper | Textos fijos del rótulo en mm |
| `ROT-VP` | 130 | Continuous | on | paper | Viewports del layout A1 |
| `SIMB-CARP` | 33 | Continuous | on | 0 en model* | Atributos `TIPO/ANCHO/PUERTA` de carpinterías |
| `SIMB-MURO` | 251 | Continuous | on | 131 | 89 tags de muro `SIMB-MURO` |

`*` = capa con contenido dentro de definiciones de bloque o paper, con conteo model en 0.

### 1.2 Del xref ARQ-ARAOZ (20, prefijo `ARQ-ARAOZ|`)

Llegan con el xref insertado en `0-REF`. Congeladas hoy: `A-TERRENO`, `HATCHMUROS`, `NUMLOC`, `PROYECCIONES`, `REP-EJES`, `TEXTO`.

| Capa xref | Color | Uso |
|---|---|---|
| `ARQ-ARAOZ\|000-cotas estructrua` | 5 | Cotas estructurales del base |
| `ARQ-ARAOZ\|A-TERRENO` | 163 | Terreno del base |
| `ARQ-ARAOZ\|ASCENSOR` | 2 | Ascensor del base |
| `ARQ-ARAOZ\|BASICO` | 1 | Base general |
| `ARQ-ARAOZ\|CARP` | 2 | Carpinterías del base |
| `ARQ-ARAOZ\|CONDUCTOS` | 3 | Conductos del base |
| `ARQ-ARAOZ\|COTAS` | 3 | Cotas del base |
| `ARQ-ARAOZ\|EJES` | 2 | Ejes del base |
| `ARQ-ARAOZ\|ESCALERA` | 4 | Escalera del base |
| `ARQ-ARAOZ\|ESTRUCTURA` | 6 | Estructura del base |
| `ARQ-ARAOZ\|FLECHA` | 8 | Flechas del base |
| `ARQ-ARAOZ\|HATCHMUROS` | 1 | Hatch de muros (fz) |
| `ARQ-ARAOZ\|INCENDIO` | 5 | Incendio del base. Acción §2.6: `A-INCEN` |
| `ARQ-ARAOZ\|MUROS` | 7 | Muros del base |
| `ARQ-ARAOZ\|MUROS-VISTA` | 4 | Muros en vista del base |
| `ARQ-ARAOZ\|NUMLOC` | 3 | Numeración de locales (fz) |
| `ARQ-ARAOZ\|PROYECCIONES` | 9 | Proyecciones (fz) |
| `ARQ-ARAOZ\|REP-EJES` | 254 | Ejes de replanteo del base (fz) |
| `ARQ-ARAOZ\|TEXTO` | 7 | Textos del base (fz) |
| `ARQ-ARAOZ\|VANOS` | 1 | Vanos del base |

## 2. TODOS los bloques

### 2.1 Nombrados (13)

| Bloque | Entidades | Contenido | Ejemplares en model |
|---|---|---|---|
| `VENTANA BAJA SIMPLE` | 12: 1 `WIPEOUT`, 8 `LINE`, 1 `LWPOLYLINE`, 2 `ATTDEF` (`TIPO`, `ANCHO` h=0.06 en `SIMB-CARP`) | Vano simple dinámico, §3 | 16 variantes anónimas `*U`, 20 ejemplares en `A-CARP-02` |
| `PUERTA BATIENTE` | 46: 4 `WIPEOUT`, 31 `LWPOLYLINE`, 1 `ARC`, 5 `CIRCLE`, 5 `ATTDEF` (`ANCHO`, `PUERTA`, `ALFEIZAR`, `ALTURA`, `DESCRIPCION`) | Puerta batiente dinámica con cuadro de vano | 12 variantes anónimas, 22 ejemplares en `A-CARP-02` |
| `SIMB-MURO` | 3 + `ATTDEF MURO` (def `M0`, h=0.10) | Tag de muro | 89 en `SIMB-MURO` |
| `SIMBOLO DE EJE` | 9: 3 `CIRCLE`, 4 `LWPOLYLINE`, 1 `HATCH`, `ATTDEF EJE` (h=0.25) | Marca de eje con número | 20 en `E-EJES` (6 variantes anónimas) |
| `SIMBOLO NIVEL PISO CORTE` | 12 + 3 `ATTDEF` (`NPT` +6.75, `DESCRIPCION`, `Nº`) | Tag NPT | 28 + 1 anónimo en `A-SIMBOLO-NPT-PLANTA` |
| `C40.20` | 6: 2 `LWPOLYLINE`, 2 `HATCH`, 2 `LINE` | Corte columna 40×20 | 26 (21 en `E-COL` + 5 en `A-COTA-1-50`) |
| `ARQ-ARAOZ` | 0 (referencia externa) | Xref del base arquitectónico | 1 en `0-REF` |
| `M2_COTA` | 3 | Símbolo de cota m² | 0 directos (uso en cotas) |
| `Tabela_Esquadrias` | 10: 7 `LINE`, 1 `HATCH`, 2 `MTEXT` | Tabla de carpinterías | paper / detalle |
| `_ArchTick`, `_Dot`, `_DotBlank`, `_Open90` | 1–3 | Puntas de cota y marcadores | uso en `DIMENSION` |

Anónimos restantes (352): variantes de estiramiento de los dinámicos + 260 de combinaciones `INSERT/LINE/MTEXT/POINT` de dimensiones y textos asociativos.

### 2.2 Resumen de INSERTs (208)

| Grupo | Cantidad |
|---|---|
| Ventanas (`VENTANA BAJA SIMPLE`, 16 variantes) | 20 |
| Puertas (`PUERTA BATIENTE`, 12 variantes) | 22 |
| Tags muro `SIMB-MURO` | 89 |
| Tags NPT | 29 |
| Marcas de eje | 20 |
| Cortes columna `C40.20` | 26 |
| Xref + Defpoints | 2 |

## 3. VENTANA BAJA SIMPLE — creación desde cero

Filosofía: simple y esquemático, resuelve el replanteo con el mínimo de entidades y el máximo de reutilización en obra. Medido en el DWG: 1 `WIPEOUT` + 8 `LINE` + 1 `LWPOLYLINE` + `ATTDEF TIPO/ANCHO`.

1. Geometría base en capa `A-ABER` lógica (inserciones en `A-CARP-02`): dos líneas de vano + antepecho bajo, en metros (`INSUNITS 6`).
2. `WIPEOUT` rectangular por debajo del vano. Limpia el hatch y las líneas del muro (`A-MURO-MAMP`) y evita líneas superpuestas que en plot salen gruesas sobre el muro.
3. Parámetros dinámicos: lineal X = largo del vano con `STRETCH` a jambas + `WIPEOUT`; lineal Y = espesor del muro, para que el mismo bloque avance en muro de 15, 20, 30. Las 16 variantes anónimas medidas son los estiramientos aplicados en obra.
4. Punto de inserción al centro del vano. Funciona en todas las escalas y facilita acotar desde ejes `R-` hacia centro y filos (mampostería a filos, vanos a ejes, spec §3.2).
5. Textos anotativos `EP-2.5 / EP-3.5` (ATTDEF h=0.06 hoy), para que la altura avance con el viewport 1:50.

## 4. Atributos — visibles hoy + recomendados en obra

Estado actual: quedan como están (medido: `TIPO` + `ANCHO`, ambos en `SIMB-CARP`).

| Atributo | Estado hoy | Uso |
|---|---|---|
| `TIPO` (tipo de ventana) | Visible | Identifica la ventana en plano y tabla `Tabela_Esquadrias` |
| `ANCHO` (ancho del vano) | Visible | Acota el hueco en replanteo |
| `H_ALFEIZAR / H_COLOCACION` | Oculto, documentado para obra | Altura de antepecho y colocación, simplifica replanteo de alturas en obra |
| `H_VENTANA` | Oculto, documentado para obra | Altura del vano, ídem anterior |

Diseño a futuro ya previsto: esos casilleros avanzan a otro estado de visibilidad dentro del mismo bloque:

- `SIMB-REP`: símbolo mínimo para replanteo.
- `50`: detalle medio 1:50 con cota de vano.
- `100+DETALLE`: a mayor escala, mayor detalle, con los atributos hoy ocultos pasando a visibles, con punto de colocación al centro para que avancen en todas las escalas.

### Texto siempre en sentido del viewport

Pedido: al girar el plano por ajuste, el texto avanza legible en sentido del viewport.

Avance propuesto:

1. Parámetro `Flip` + acción `Flip` sobre textos y atributos.
2. Estilo anotativo con `Match orientation to layout` activo.
3. Alternativa de obra: orientación del atributo bloqueada en horizontal + punto central.

## 5. Edición que funcionó — BEDIT + BATTMAN + ATTSYNC + REGEN

Síntoma 2026-10-13: tras editar el bloque y quitar atributos del original, el tamaño de texto aplicó y los atributos quitados seguían volando, corridos en el aire. Coherente con lo medido: la definición hoy trae solo `TIPO/ANCHO` y los ejemplares pedían sync.

Secuencia que avanzó por línea de comandos:

1. `BEDIT` → `VENTANA BAJA SIMPLE` → quitar ATTDEF + ajustar altura → `Cerrar + Guardar`.
2. `BATTMAN` → `Parámetros` → activar `Aplicar cambios a referencias existentes` → `Eliminar` → `Sincronizar`.
3. `ATTSYNC` → `Nombre` → `VENTANA BAJA SIMPLE` → `Sí`.
4. `REGEN` general.

Detalle: para bloque ya sin atributos, avanza redefinir con `BLOCK` (el administrador pide conservar al menos uno).

Fuentes verificadas `es_AR` (certificación 2026-10-13: todo enlace `help.autodesk.com` en variante `/ESP/` + `/ENU/`; `autodesk.com/support` responde 403 a lectura automática por protección anti-bots, contenido certificado vía índice oficial con cuerpo en español):

- [Acerca de la modificación de definiciones de atributos](https://help.autodesk.com/view/ACD/2027/ESP/?guid=GUID-F351FDBB-2731-40C1-A186-1B1F47779E32) · [English](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-F351FDBB-2731-40C1-A186-1B1F47779E32) (antes enlazado en `/PLK/` polaco, corregido)
- [ATTSYNC (comando) — referencia oficial ESP](https://help.autodesk.com/cloudhelp/2024/ESP/AutoCAD-LT/files/GUID-56B14079-250B-4C99-AB3D-F95BA1C32AB7.htm): confirma nombre ES `SINCRATR` y par `BLOQUE/EDITARBLOQUE`
- [Al desplazar un atributo en el Editor no se mueve en modelo](https://www.autodesk.com/es/support/technical/article/caas/sfdcarticles/sfdcarticles/ESP/Moving-an-attribute-belonging-to-a-dynamic-block-in-AutoCAD-only-moves-the-attribute-grip.html)
- [Cómo restablecer atributos a valores por defecto](https://www.autodesk.com/es/support/technical/article/caas/sfdcarticles/sfdcarticles/ESP/How-to-reset-Block-Attributes-to-default-values-in-AutoCAD.html) (slug corregido al canónico del índice)
- [Referencia de comandos ESP 2026](https://help.autodesk.com/cloudhelp/2026/ESP/AutoCAD-LT/files/GUID-4FEBA606-95E0-4DC4-A116-257ED86DCD58.htm): fuente de nombres ES de §14
- MCP autocad: [[wiki/glosario/software/mcp-autocad|mcp-autocad]] (requiere AutoCAD completo abierto, no LT).

## 6. Pendiente y backlog — ver §16 final

La lista de pendientes vive al final del documento (§16), junto al backlog del mes próximo.

---

## 11. Traducción a DWT + DWS — qué pasa con lo fuera de norma

### Diferencia DWT vs DWS — para qué sirve cada uno

| | DWT (plantilla) | DWS (norma) |
|---|---|---|
| Qué es | Molde de arranque: un DWG maestro que ya trae todo puesto | Regla de control: la lista de lo permitido contra la que se verifica |
| Para qué sirve | Que todo plano nuevo **nazca** bien (capas, estilos, layout, unidades) | Que todo plano dibujado **siga** bien (auditar desvíos) |
| Cuándo actúa | Al inicio (`NUEVO` desde `SET_01-REP.dwt`) | Al control (`VERIFICANORMAS` contra `SET-REP.dws`) |
| Si falta | Cada plano arranca distinto y hay que armarlo a mano | Nadie detecta capas/estilos fuera de norma |
| Binario | `activos/.../SET_01-REP.dwt` (fuera de git) | `activos/.../SET-REP.dws` (fuera de git) |

Dicho corto: el **DWT evita el error al crear**, el **DWS detecta el error al revisar**. El playbook §12 usa el DWT en el paso 1 y el DWS en el paso 10.

### 11.1 DWT (`SET_01-REP.dwt`)

El DWT congela el estándar: arranca de `acadiso.dwt` y guarda unidades metros (`INSUNITS 6`, `LUNITS 2`), las 22 capas §2 con color/linetype/lineweight, estilos `EP-2.5/EP-3.5` + `EP-ARQ` (destino de §7–§8), layout `REP-PTipo-A1` con viewport 1:50 bloqueado y escala custom `1:50 (m)`. Vive en `activos/` (binario, fuera de git). Todo plano nuevo de replanteo nace de ahí: `NUEVO` + elegir la plantilla.

### 11.2 DWS (`SET-REP.dws`) + capa fuera de norma

El DWS es la norma verificable: capas, estilos de texto/cota/directriz y tipos de línea esperados. Comando `VERIFICANORMAS` (`CHECKSTANDARDS`) compara el DWG contra el DWS e informa cada violación.

Qué pasa si se crea una capa fuera de las establecidas (caso real: `INCENDIO`):

1. `VERIFICANORMAS` la marca como "no encontrada en el archivo de normas".
2. Se decide: mapearla a la norma con `TRANSFORMACAPA` (`LAYTRANS`) — `INCENDIO → A-INCEN` — o darla de alta en el spec si el estudio la adopta.
3. Las entidades migran de capa conservando geometría; luego `AUDITORIA` (`AUDIT`) + `LIMPIA` (`PURGE`) y re-verificación hasta cero violaciones.

### 11.3 Cómo se controla y cómo se hace la auditoría (rutina del estudio)

Rutina en cada entrega de plano, en este orden:

1. **Fijar la norma**: `NORMAS` (`STANDARDS`) → asociar `SET-REP.dws` al DWG. Queda guardada la asociación.
2. **Correr la verificación**: `VERIFICANORMAS` → revisa capas, estilos de texto, estilos de cota, estilos de directriz múltiple y tipos de línea. Por cada violación muestra valor actual vs valor norma.
3. **Resolver capa por capa**: lo que coincide se aprueba; lo fuera de norma se mapea con conversor de capas (Herramientas → Conversor de capas) o se incorpora al spec con ADR en `03-log-mvp_02.md`.
4. **Sanear geometría**: `AUDITORIA` (corrige errores de base) → `LIMPIA` (purga capas, bloques `*D` residuales, estilos y tipos sin uso — candidatos §8: `{18b73a54-…}`, `Standard` si queda sin uso).
5. **Re-verificar**: segunda pasada de `VERIFICANORMAS` hasta cero violaciones. Recién ahí el plano avanza a plot.
6. **Evidencia**: el reporte se vuelca como tabla (capas §1 de este doc) y queda versionado en `docs/` junto al DWG auditado.

### 11.4 Manejo de estilos de texto y cotas

- Conviven los medidos (§7–§8) durante la transición; el DWS declara los destino (`EP-*`).
- `VERIFICANORMAS` también marca estilos fuera de norma (`cotas-50`, `COTAS-ARQ-50` → `EP-ARQ`; `ROT` se conserva como estilo de paper).
- Regla: altura fija en estilos de model (`cotas-50` h=0.16), altura 0 en estilos de bloque para que mande cada `ATTDEF`.
- Alta de un estilo nuevo: Formato → Estilo de texto (fuente + altura + ancho) / Formato → Estilo de cota (flecha + texto + escala + decimales) → guardar el DWG → actualizar `SET_01-REP.dwt` y `SET-REP.dws` para que el próximo plano lo herede. Estilo que nace en un plano y no entra al DWT/DWS se purga en la próxima auditoría.

## 12. Playbook principio-fin — plano de replanteo

Comandos en `EN / ES` (tabla completa §14; con guion bajo `_COMANDO` el inglés funciona en versión ES).

1. **Plantilla**: `NUEVO` desde `SET_01-REP.dwt`. Verificar `UNIDADES` (decimal, metros) e `INSUNITS 6`.
2. **Capas**: `CAPA` — crear/confirmar las §1. Congelar xref de fondo (`A-TERRENO`), bloquear `REP-EJES`.
3. **Ejes**: `LINEA` en `REP-EJES` (DASHDOTX2), ≥2 principales → `INSERTAR` `SIMBOLO DE EJE` en cruces.
4. **Muros**: `POLILINEA` cerrada en `A-MURO-MAMP` + hatch `SOMBREA`.
5. **Vanos**: `INSERTAR` `VENTANA BAJA SIMPLE` al centro del vano → estirar a largo/espesor → completar `TIPO/ANCHO`. Ídem `PUERTA BATIENTE` con sus 5 atributos.
6. **Tags**: `INSERTAR` `SIMB-MURO`, `SIMBOLO NIVEL PISO CORTE`, `C40.20` en columnas.
7. **Cotas**: `ACOTA` lineal (`REPLANTEO 150` en `REP-COTAS`, `COTAS-ARQ-50` en `A-COTA-1-50`).
8. **Textos**: `TEXTO` / `TEXTOM` según estilo §8.
9. **Atributos**: `ADMINATRIB` (`BATTMAN`) para revisar → `SINCRATR` (`ATTSYNC`) + `REGENERAR` (`REGEN`).
10. **Normas**: `VERIFICANORMAS` contra `SET-REP.dws` → mapear desvíos → `AUDITORIA` + `LIMPIA`.
11. **Lámina**: layout `REP-PTipo-A1`, viewport 1:50 bloqueado, rótulo `G-CART-MEPA` con `CAMPO` (`FIELD`) de escala al viewport.
12. **Plot**: `TRAZAR` a PDF con `EP-ISO.ctb` (o `monochrome.ctb` como fallback).

## 13. Relación estándares → bloques → atributos → cómputos → escala

- **Estándar** (capas §1 + estilos §7–§8 + DWS §11) fija el lenguaje: cada dato vive en una capa y un estilo conocidos.
- **Bloque** empaqueta geometría repetible (vano, puerta, tag) con punto de inserción al centro y parámetros dinámicos: un solo `VENTANA BAJA SIMPLE` cubre 16 medidas (variantes medidas §2.1).
- **Atributo** convierte el dibujo en base de datos: `TIPO/ANCHO/ALFEIZAR/ALTURA/MURO/NPT` por ejemplar.
- **Cómputos**: `EXTRACDAT` (`DATAEXTRACTION`) vuelca atributos a tabla/CSV — cantidad de ventanas por tipo y ancho, puertas con descripción, muros por tag, NPT por local — sin medir a mano. Cuadro generado: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/cuadro-carpinterias|cuadro-carpinterias]] (V01×6/2.30, V02×10/1.10, PV01×4/1.75, P-1/P-2/P-3). Por eso §4 recomienda conservar `H_ALFEIZAR/H_VENTANA` aunque hoy queden ocultos: alimentan el cómputo de obra.
- **Escala**: el mismo bloque sirve en `SIMB-REP/50/100+DETALLE` (§4) con textos anotativos; el estándar escala porque cada pieza nueva (bloque, atributo, estilo) entra al DWT/DWS una vez y se reutiliza en todos los planos.

## 14. Comandos EN / ES verificados

Fuente ES: referencia oficial cloudhelp `ESP` + índice Autodesk. Regla de oro: `_COMANDO` en inglés funciona en la versión española.

| EN | ES | Atajo | Uso en este playbook |
|---|---|---|---|
| `LINE` | `LINEA` | L | Ejes |
| `PLINE` | `POLILINEA` | PL | Muros, contornos |
| `CIRCLE` | `CIRCULO` | C | Marcas de eje |
| `ARC` | `ARCO` | A | Hojas batientes |
| `TEXT` | `TEXTO` | — | Rótulos una línea |
| `MTEXT` | `TEXTOM` | T | Párrafos, tabla |
| `BLOCK` | `BLOQUE` | B | Crear definición |
| `BEDIT` | `EDITARBLOQUE` | — | Editar definición |
| `INSERT` | `INSERT` | I | Insertar bloque |
| `ATTDEF` | ver cinta Definición de bloque | — | Crear atributo |
| `BATTMAN` | paleta Administrador de atributos | — | Revisar/sincronizar |
| `ATTSYNC` | `SINCRATR` | — | Sincronizar atributos |
| `DIM` | `ACOTA` | — | Acotar |
| `DIMSTYLE` | ver Formato → Estilo de cota | D | Estilos cota |
| `STYLE` | ver Formato → Estilo de texto | ST | Estilos texto |
| `LAYER` | `CAPA` | LA | Capas |
| `REGEN` | `REGEN` | RE | Regenerar vista |
| `REGENALL` | `REGENT` | REA | Regenerar todo |
| `CHECKSTANDARDS` | `VERIFICANORMAS` | — | Verificar vs DWS |
| `STANDARDS` | `NORMAS` | — | Asociar DWS |
| `LAYTRANS` | ver Herramientas → Conversor de capas | — | Mapear capa fuera de norma |
| `AUDIT` | `AUDITORIA` | — | Auditar DWG |
| `PURGE` | `LIMPIA` | PU | Purgar sin uso |
| `DATAEXTRACTION` | `EXTRACDAT` | — | Cómputos a tabla/CSV |
| `HATCH` | `SOMBREA` | H | Hatch muros |
| `TRIM` / `EXTEND` | `RECORTA` / `ALARGA` | TR / EX | Ajustes |
| `ROTATE` | `GIRA` | RO | Girar (símbolo, no tag §15) |
| `OFFSET` | `DESFASE` | O | Paralelas |
| `MIRROR` | `SIMETRIA` | MI | Espejar |
| `SCALE` | `ESCALA` | SC | Escalar |
| `MOVE` / `COPY` | `DESPLAZA` / `COPIA` | M / CO | Reubicar/duplicar |
| `ERASE` | `BORRA` | E | Borrar |
| `PLOT` | `TRAZAR` | — | Imprimir/PDF |
| `ZOOM` / `PAN` | `ZOOM` / `ENCUADRE` | Z / P | Vista |
| `QSELECT` | Selección rápida | — | Filtrar atributos |
| `FIELD` | `CAMPO` | — | Escala viva en rótulo |

> Atajos según pgp de cada idioma (`ALIAS` los lista en tu LT); con `_COMANDO` el inglés funciona en versión ES.

## 15. Tag siempre horizontal — ver doc de bloques

Mudado a [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/bloques-personalizados|bloques-personalizados]] §4 (sector exclusivo de bloques).

---

## 16. Pendiente y backlog (reunión de mañana → mes próximo)

### Pendiente inmediato

- [ ] Releer con MCP (`list_layers / list_blocks / query_entities`) cuando abra AutoCAD completo 2026 (con LT no hay sesión COM).
- [ ] Renombres descartados en v2.2 (mandan nombres del archivo); capas nuevas de instalaciones se evalúan con nombre propio.
- [ ] Desglose de ítems, horas y ahorro: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/desglose-configuraciones|desglose-configuraciones]] (14 h invertidas, ~12–15 h de ahorro por plano).
- [ ] Con aprobado, pase a `wiki/glosario/interno/standares/tecnico/bloques` + `capas-layers` (fuera de esta versión) y split del §12 a playbook aparte ítem por ítem.

### Backlog mes próximo

- [ ] Bloques con varias visibilidades según escala (`SIMB-REP / 50 / 100+DETALLE`) que amplían información a mayor detalle.
- [ ] Cotas dinámicas por escala, documentadas por estado de visibilidad.
- [ ] Capas nuevas: carpinterías adicionales, instalaciones, eléctrica, sanitaria.
- [ ] Estrategia para las ~260 configuraciones anónimas `*D` (INSERT/LINE/MTEXT de cotas): purga, auditoría y criterio de conservación.
- [ ] Catálogo de bloques personalizados con posiciones y escalas (vive en [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/bloques-personalizados|bloques-personalizados]]).

---

## 7. Estilos de cota (3 DIMSTYLEs, 304 cotas medidas)

Uso medido en model: `COTAS-ARQ-50` ×152 + `REPLANTEO 150` ×152.

| Estilo | Flecha | Texto | Extensión / offset | Uso |
|---|---|---|---|---|
| `COTAS-ARQ-50` | tick `_ArchTick`, 0.10 | `COTAS`, color PorCapa, 2 decimales | `exl 0.10 / exo 0.05 / gap 0.10` | Cotas arquitectónicas 1:50 en `A-COTA-1-50` |
| `REPLANTEO 150` | `_Open90`, 0.20 | `cotas-50`, color PorCapa, 2 decimales | `exl 0.0 / exo 0.05 / gap 0.03` | Cotas de replanteo en `REP-COTAS` |
| `Standard` | cerrada default 2.5 | `Standard`, 2 decimales | defaults | Sin uso en model, mantener como fallback |

Acción SET_01: ambos estilos avanzan hacia `EP-ARQ` (spec §4.2) al normalizar el template; conservar puntas `_ArchTick` (arq) y `_Open90` (replanteo) como firmas visuales.

## 8. Estilos de texto (9 STYLEs)

Uso model medido: `TEXT` 83 (`ROT` 27, `cotas-50` 21, `style2` 21, `Standard` 14) + `MTEXT` 26 (`MBA25` 25, `Style-Arial_1` 1). Alturas TEXT en model (m): 0.16 ×21, 0.10 ×21, 0.075 ×16, 0.0179 ×14.

| Estilo | Fuente | Altura base | Uso medido |
|---|---|---|---|
| `cotas-50` | simplex, h fija 0.16, ancho 0.9 | 0.16 | Textos de cotas 1:50 + `ATTDEF MURO` en `SIMB-MURO` |
| `COTAS` | `simplex.shx`, h 0 (por entidad), ancho 0.8 | variable | Texto de cotas dentro de bloques `*D` de DIMENSION + `MTEXT` de cotas |
| `style2` | `simplex.shx`, h 0, ancho 1.0 | 0.10 model / 2.5–4.0 paper | Textos generales + `Nº` de NPT |
| `Standard` | `arial.ttf`, h 0 | 0.0179 model / 1.7–3.5 paper | Textos generales + ATTDEFs de puertas, ejes, NPT en variantes `*U` |
| `MBA25` | `arial.ttf`, h 0.05 | párrafo | `MTEXT` descriptivos + `Tabela_Esquadrias` |
| `ROMANS` | `calibril.ttf`, h 0.06, ancho 0.7 | párrafo | `MTEXT` en paper |
| `ROT` | `calibril.ttf`, h 0.25, ancho 0.8 | 0.075–0.32 model / 4–12 paper | Rótulo: textos fijos + 7 ATTDEFs del bloque carátula |
| `Style-Arial_1` | `arial.ttf`, h 0 | párrafo | 1 `MTEXT` suelto |
| `{18b73a54-…}` | `Simplex.shx` | — | Residual de editor, candidato a `PURGE` |

Acción SET_01: avanzan hacia `EP-2.5 / EP-3.5` anotativos (spec §4.2); `ROT` queda como estilo de paper en mm.

## 9. Glosario de entidades (medido en este plano)

| Entidad | Qué es | Uso en REP-ARAOZ |
|---|---|---|
| `LINE` (639) | Segmento recto | Muros, vanos, ejes |
| `DIMENSION` (304) | Cota asociativa con su bloque `*D` | 152 arq + 152 replanteo |
| `INSERT` (208) | Ejemplar de bloque | §2.2 |
| `TEXT` (83) | Texto de una línea | Rótulos, cotas, ejes |
| `LWPOLYLINE` (61) | Polilínea liviana | Contornos de muros y vanos |
| `MTEXT` (26) | Párrafo multilínea | Descripciones + tabla carpinterías |
| `HATCH` (23) | Sombreado | Muros, marcas de eje |
| `CIRCLE` (14) | Círculo | Marcas de eje, batientes |
| `ARC` (1 en model + en puertas) | Arco | Hojas batientes |
| `WIPEOUT` (solo en bloques) | Máscara que limpia lo de abajo | Limpia el muro bajo vanos y puertas |
| `ATTDEF / ATTRIB` | Definición / valor de atributo | Tags con datos extraíbles (`DATAEXTRACTION`) |
| `POINT` (en bloques `*D`) | Punto de definición | Nodos de cotas asociativas |

## 10. Paso a paso — dibujar el plano desde cero + insertar bloques

Referencia oficial de cada herramienta: [[wiki/glosario/software/mcp-autocad|mcp-autocad]] (§ Conexión, Documentos, Estado del dibujo, Geometría, Edición). El MCP recibe coordenadas en **mm** y convierte según `INSUNITS` (con metros, 1000 mm = 1 unidad); `scale` de bloque es unitless (1 = tamaño real).

0. **Conexión**: `autocad_status` → `list_open_drawings` → `get_active_drawing_info` (confirmar `INSUNITS 6`). Sin sesión (caso LT), avanzar por archivo como en este documento.
1. **Capas**: `create_layer` por cada fila de §1 (nombre + `color_aci`) → `set_current_layer` antes de cada familia → `set_layer_properties` para freeze de `A-TERRENO`, lock de `REP-EJES`, `visible:false` en `G-AUXI` antes del plot.
2. **Terreno**: `draw_polyline` cerrada con medidas perimetrales en `A-TERRENO`.
3. **Ejes**: `draw_line` en `REP-EJES` (≥2 principales + auxiliares) → `insert_block` con `block_name: SIMBOLO DE EJE` en cada cruce, punto en mm del cruce.
4. **Muros**: `draw_polyline` cerradas en `A-MURO-MAMP` (verificado: es la capa con más entidades, 289).
5. **Vanos**: `insert_block` con `block_name: VENTANA BAJA SIMPLE`, `insertion_point_mm` = centro del vano en mm, `scale: 1`, `rotation_deg` según orientación del muro → estirar largo/ancho con grips dinámicos → el `WIPEOUT` limpia el muro solo.
6. **Puertas**: `insert_block` con `block_name: PUERTA BATIENTE`, completar atributos `ANCHO/PUERTA/ALFEIZAR/ALTURA/DESCRIPCION`.
7. **Tags**: `insert_block` `SIMB-MURO` (atributo `MURO`), `SIMBOLO NIVEL PISO CORTE` (atributos `NPT/DESCRIPCION/Nº`), `C40.20` en columnas.
8. **Cotas**: `add_linear_dimension` con `start_mm/end_mm` en mm, `dimension_line_point_mm` con offset, `orientation` (`horizontal/vertical/aligned`), `layer: REP-COTAS` o `A-COTA-1-50`. Devuelve el valor medido en mm para validar contra spec.
9. **Textos**: `draw_text` (`text`, `insertion_point_mm`, `height_mm`, `layer`).
10. **Verificación**: `query_entities` por `layer` (barrer `REP-EJES`, `A-CARP-02`), `list_blocks` para confirmar definiciones, `zoom_extents` + `capture_screenshot` para control visual.
11. **Correcciones**: `set_entity_layer` por handle para normalizar, `move_entity / copy_entity` para reubicar, `erase_entity` para limpieza (undoable en AutoCAD).
12. **Cierre**: `AUDIT + PURGE` en AutoCAD, `save_active_drawing` intermedio, `save_drawing_as` (salida bajo output jail) para entregar.

> Nota de escala MCP: con modelo en metros, pasar puntos en mm (ej. centro de vano en x=12.5 m → `insertion_point_mm: [12500, ...]`).
