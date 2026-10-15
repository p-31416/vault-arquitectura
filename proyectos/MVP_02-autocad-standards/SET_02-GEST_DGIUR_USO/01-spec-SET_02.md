---
tipo: spec
mvp: 02
nivel: SET_02-GEST
set_numero: "02"
set_disciplina: GEST
set_nombre: DGIUR_Uso
version: 0.2-referencia-oficial
fecha_creacion: 2026-10-05
ultima_actualizacion: 2026-10-05
tags: [mvp_02, SET, SET_02, dgiur, dgpp, actividad_economica, anexo_III, uso_de_suelo, plano_municipal, 1_100, monochrome, simbologia, bloques_dinamicos]
documento_referencia: PLANO_USOAnexoIII.pdf
documento_referencia_titulo: Anexo III - Formularios de Presentacion de Solicitud de Actividad Economica
documento_referencia_organo: DGHP
documento_referencia_expediente: IF-2025-11263770-GCABA-DGHP
documento_referencia_fecha: 2025-03-13
documento_referencia_paginas: 21
discrepancia_organo: true
base_empirica: MODELO PLANO DE USO.dwg
---

# SET_02-GEST_DGIUR_USO — Plano de Uso para Trámite Municipal v0.2

> **SET** = Set de herramientas, Standards, Capas, Puntas
> **Estructura**: importa `../01-spec-mvp_02.md` (genérica, 10 items) y detalla abajo según necesidad de SET_02.
> **Alcance**: transcrito del documento oficial de referencia (§8.1). Lo que ese documento no fija queda anotado como pendiente, sin inferencia.
> **Base empírica**: auditoría del DWG `G:\Mi unidad\G#GESTIONES\TEMPLATES\MODELO PLANO DE USO.dwg` leída vía MCP `autocad_*` el 2026-10-05 (73 capas, 314 bloques, 2 layouts, `INSUNITS=6` metros). Ver §2.6.
> **Contexto**: sigue a SET_01-REP_Replanteo. SET_01 fija el sistema de referencia del terreno; SET_02 lo traduce al documento que el municipio lee.

## 0. "DoD" SET_02 (hereda orden de `../01-spec-mvp_02.md`)

- [ ] **1. SETEO** → §4.2 (metros `INSUNITS=6`, escala única 1:100, viewport CustomScale 10). CÓMO en `02-ft-SET_02.md` §1.
- [ ] **2. LAYERS** → §2 (25 capas: `A-` 15, `SIMB-` 3, `PL-` 1, `ROT-` 2, `SUP-` 4). Prefijos por función.
- [ ] **3. CTB** → §4.4 (`monochrome.ctb` estándar de AutoCAD). Obligación del documento oficial: *"líneas de color negro con fondo blanco"* (§1.1).
- [ ] **4. TEXTSTYLES** → §4.2. Pendiente de definir (SET_01 usa `EP-2.5` / `EP-3.5`).
- [ ] **5. DIMSTYLES** → §4.2. Pendiente de definir (SET_01 usa `EP-ARQ`).
- [ ] **6. BLOQUES — biblioteca fija** → §6.7 (dos bloques de carátula `GCBA-CRTL-PLANO_USO` y `GCBA-CRTL-PLANO_UNICO`).
- [ ] **7. BLOQUES DINÁMICOS / ATRIBUTOS** → §6 (4 bloques: `A-CARP-PU-088`, `SIMB-NIV-NPT`, `SIMB-LOC-01`, `SIMB-CORTE-01`). **Documentados, no implementados** — decisión 2026-10-05.
- [ ] **8. TEMPLATE** → `activos/proyectos/mvp_02-autocad-standards/SET_02-GEST_DGIUR_USO/SET_02-GEST.dwt` (NO en git). CÓMO en `02-ft-SET_02.md` §8.
- [ ] **9. AUTOLISP** → §7 (comando `SET-02-GEST`). Archivo en `lisp/`, pendiente.
- [ ] **10. GLOSARIO** → diferido (wiki tras evaluar SET_02).

---

## 1. ALCANCE

> Todo este capítulo es transcripción del ítem **6) CONTENIDO DEL PLANO DE USO** del Anexo III (§8.1). Las comillas marcan texto oficial.

### 1.1 Presentación

> *"Deberá presentarse en líneas de color negro con fondo blanco y contendrá:"*

De esa obligación se derivan dos reglas de ploteo:

- **Negro sobre blanco**: el color no se usa para distinguir elementos en la lámina. El ACI de cada capa sirve para trabajar en pantalla; la salida es monocroma.
- **Valor de línea correspondiente**: el grosor de trazo no es decorativo, es información. El lineweight de cada capa se define en §2 y se respeta en el plot.

### 1.2 Contendrá (7 ítems)

> - *"La/s planta/s."*
> - *"El corte de la unidad que se desea autorizar."*
> - *"Planilla de iluminación y ventilación de los locales."*
> - *"La ubicación de dicha unidad dentro de la totalidad del inmueble y de la parcela."*
> - *"Sus accesos desde la vía pública."*
> - *"En caso de contar con superficie para la que no se solicite autorización de actividad económica ésta deberá rayarse a 45°."*
> - *"Valor de línea correspondiente."*

### 1.3 Se individualizarán (12 ítems)

> - *"La parte a usar."*
> - *"Patios, aire y luz y/o áreas descubiertas que se pretenden autorizar."*
> - *"Accesos desde Línea Oficial, con su correspondiente domicilio."*
> - *"Medida de los destinos, de las áreas semicubiertas y descubiertas y de los medios de salida."*
> - *"Alturas libres."*
> - *"Línea Oficial (L.O.) y Líneas Divisorias de Parcela (L.D.P.)."*
> - *"Ventilaciones."*
> - *"Identificación y uso y destino de cada local."*
> - *"Salidas exigidas."*
> - *"Puertas, con su sentido de apertura y barrido."*
> - *"Ubicación de los servicios de salubridad con sus correspondientes artefactos sanitarios."*
> - *"Cotas de niveles de piso terminado de cada planta, respecto del nivel de piso en vereda sobre la L.O. frente al acceso principal."*

### 1.4 Según el caso (5 ítems)

> *"Sin perjuicio de ello, y en caso de corresponder, las áreas intervinientes podrán requerir corte/s complementario/s, balance de superficies, detalle de local, planilla de artefactos sanitarios, silueta de superficie destinada al público, entre otros."*

### 1.5 Carátula (6 datos)

> *"La carátula se confeccionará de acuerdo al modelo definido en el presente Anexo y contendrá los siguientes datos:"*

> - *"Rubro o descripción, Ciudadano Responsable, Domicilio, Plantas a autorizar, UF (de corresponder) y datos catastrales de la parcela."*
> - *"Croquis de ubicación, indicando medidas de la parcela y ancho de calle."*
> - *"Mixtura de Usos del Suelo y/o Área Especial Individualizada."*
> - *"Superficies, discriminándose cubierta, semicubierta, descubierta y total."*
> - *"Cantidad de personas que trabajan por turno."*
> - *"Nombre del Profesional Responsable, Título o Profesión y N° de matrícula."*

El modelo de carátula (ítem 9 del Anexo) agrega además: **Hoja Adicional de Firmas**, **Informe gráfico**, **Número**, **Fecha** y **Referencia**.

> **Lo que el documento oficial NO fija**: ni escala, ni formato de archivo. La verificación del 2026-10-05 sobre el texto extraído del PDF arrojó **0 coincidencias** de `escala`, `1:100`, `DWF`, `DWG`, `PDF` y `formato`. La escala 1:100 y el plotter `DWF-CABA.pc3` son decisiones del estudio (§4.2, §4.4), noDel documento.

---

## 2. CAPAS — Prefijos por función

> **Regla MVP_02 para SET_02**: cinco prefijos, cada uno con una función.
>
> | Prefijo | Función | Espacio |
> |---------|---------|---------|
> | `A-` | Arquitectura: lo que se dibuja | Modelo |
> | `SUP-` | Superficies: polilíneas de cómputo y rayados | Modelo |
> | `SIMB-` | Simbología: marcas y rótulos del plano | Modelo |
> | `PL-` | Planillas y cuadros | Modelo |
> | `ROT-` | Carátula | **Paper** |
>
> El rótulo va a `ROT-` porque vive en paper space: es la única familia con `Plot = No` por diseño (junto con `A-MURO-EXIST`).

### 2.1 Arquitectura — `A-` (15 capas)

| Layer | Color | Linetype | Lineweight | Plot | Descripción |
|-------|-------|----------|-----------|------|-------------|
| `A-MURO` | 7 | CONTINUOUS | 0.50 | Sí | Muros |
| `A-MURO-EXIST` | 5 | CONTINUOUS | 0.35 | **No** | Superposición de muros existentes. Auxiliar de trabajo: no se imprime |
| `A-CARP-01` | 2 | CONTINUOUS | **0.15** | Sí | Carpintería línea fina (bastidor, herraje leve) |
| `A-CARP-02` | 2 | CONTINUOUS | **0.05** | Sí | Carpintería línea gruesa (hoja, perfil principal) |
| `A-COTAS` | 7 | CONTINUOUS | 0.25 | Sí | Cotas de locales |
| `A-COTAS-2` | 7 | CONTINUOUS | 0.35 | Sí | Cotas de terreno y linderos |
| `A-SOLADOS` | 250 | CONTINUOUS | 0.25 | Sí | Cambios de piso, escaleras |
| `A-HERR` | 6 | CONTINUOUS | **0.00** | Sí | Herrería: barandas, pasamanos, antepechos |
| `A-PROY-01` | 6 | DASHED | 0.25 | Sí | Proyecciones: interlineado tipo 1 |
| `A-PROY-02` | 6 | DASHDOT | 0.25 | Sí | Proyecciones: interlineado tipo 2 |
| `A-EJES` | 3 | **DASHDOT** | 0.35 | Sí | Ejes municipales |
| `A-EQUIP` | **251** | CONTINUOUS | 0.25 | Sí | Equipamiento necesario para la habilitación, incluidos servicios de salubridad y artefactos sanitarios |
| `A-VISTA-01` | 254 | CONTINUOUS | 0.25 | Sí | Vistas / cortes: tipo 1 |
| `A-VISTA-02` | 252 | CONTINUOUS | 0.25 | Sí | Vistas / cortes: tipo 2 |
| `A-VISTA-03` | 251 | CONTINUOUS | 0.25 | Sí | Vistas / cortes: tipo 3 |

> **Por qué `A-HERR` con lineweight 0.00**: la herrería es el trazo más delgado del plano de uso. Va con el valor más bajo de la serie ISO 128-2 para que se lea sin competir con los muros.
>
> **Por qué dos capas de proyección**: los dos interlineados (`DASHED` y `DASHDOT`) sirven para diferenciar proyección de medianera contra proyección de cierre. Separarlas permite apagarlas por separado al superponer.
>
> **Por qué tres capas de vista**: cada vista o corte va en su propia capa para poder congelar las que no entran en la lámina vigente sin tocar las demás.

### 2.2 Superficies — `SUP-` (4 capas)

> Las polilíneas de superficie se dibujan separadas del rayado: una cosa es **medir** m² y otra es **autorizar**. Son dos operaciones distintas y por eso dos familias de capas.

| Layer | Color | Contenido | Plot |
|-------|-------|-----------|------|
| `SUP-AUT` | 34 | **Rayado 135°** — superficie habilitada/autorizada (puede ser distinta de la existente) | Sí |
| `SUP-SEMI` | 44 | Polilínea de superficie **semicubierta**, por tipo | Sí |
| `SUP-DESC` | 140 | Polilínea de superficie **descubierta**, por tipo | Sí |
| `SUP-NVO` | 1 | Polilínea de **superficie nueva** | Sí |

> El rayado 45° (superficie para la que no se solicita autorización) se dibuja dentro de la polilínea de superficie correspondiente, sin capa propia. La distinción se verifica por el ángulo del patrón y se referencia en el campo de notas (§3.1).
>
> **`SUP-AUT` concentra el hatch**: al ir el rayado en la misma capa que la superficie autorizada, un filtro por capa devuelve exactamente lo autorizado, sin filtrar la geometría a mano.

### 2.3 Simbología — `SIMB-` (3 capas)

| Layer | Color | Linetype | Lineweight | Plot | Descripción |
|-------|-------|----------|-----------|------|-------------|
| `SIMB-NIV` | 31 | CONTINUOUS | 0.25 | Sí | Símbolo de nivel terminado (NPT) |
| `SIMB-LOC` | 3 | CONTINUOUS | 0.25 | Sí | Símbolo de local: texto + número |
| `SIMB-CORTE` | 1 | CONTINUOUS | 0.35 | Sí | Marca de corte: posición planta + posición corte |

### 2.4 Planillas — `PL-` (1 capa)

| Layer | Color | Linetype | Lineweight | Plot | Descripción |
|-------|-------|----------|-----------|------|-------------|
| `PL-LOC` | 7 | CONTINUOUS | 0.25 | Sí | Planillas de locales y de iluminación y ventilación |

### 2.5 Carátula — `ROT-` (paper-only, 2 capas)

| Layer | Color | Linetype | Plot | Descripción |
|-------|-------|----------|------|-------------|
| `ROT-HOJA` | 5 | Continuous | **No** | Recuadro exterior del rótulo |
| `ROT-TXT` | 7 | Continuous | **No** | Textos fijos del rótulo (no atributos) |

### 2.6 Total

**15 (`A-`) + 4 (`SUP-`) + 3 (`SIMB-`) + 1 (`PL-`) + 2 (`ROT-`) = 25 capas.**

Contraste con el modelo auditado: 73 capas → 25. La reducción viene de fusionar duplicados (4 capas de cotas → 2, 4 de texto → 1, 4 de solado → 1) y de enviar a `A-MURO-EXIST` (no imprimible) todo lo que es superposición de existentes.

### 2.7 Auditoría del DWG modelo

Resumen de la auditoría del 2026-10-05 sobre `MODELO PLANO DE USO.dwg`. Tabla completa de las 73 capas en `docs/auditoria-capas-modelo-uso.md`.

| Hallazgo | Capas involucradas | Acción |
|----------|--------------------|--------|
| Cotas duplicadas ×4 | `A-COTAS`, `ANN-COTAS-`, `ANN-COTAS-Y-TEXTOS`, `C_COTAS_NIVELES` | Quedan `A-COTAS` (locales) y `A-COTAS-2` (terreno) |
| Texto duplicado ×4 | `A-TXT`, `A-TEXTO`, `B_TEXTO`, `TEXTO` | Se unifican en `SIMB-LOC` y `A-COTAS` según destino |
| Niveles duplicado ×2 | `A-TXT-NIV`, `A-TXT-NIVEL` | Se unifican en `SIMB-NIV` |
| Solado duplicado ×4 | `A-SOLADO`, `A-SOLADOS`, `A-HATCH-SOLADO`, `Z-CORREC-SOL` | Se unifican en `A-SOLADOS` |
| Equipamiento ×3 | `A-EQUIPAMIENTO`, `ARQ-EQUIPAMIENTO MOVIL`, `MUEBLES` | Se unifican en `A-EQUIP` |
| Ejes ×2 | `A-EJES` (DASHDOT), `EJES` (TRAZO_Y_PUNTO) | Se unifican en `A-EJES` |
| Estados de superficie sin codificar | `SUP-EXIST`, `SUP-MURO_NVO`, `SUP-MURO_NEGRO`, `SUP-DEM` | `SUP-EXIST` → `SUP-NVO` si es nueva, si no a `A-MURO-EXIST`; `SUP-MURO_NVO` y `SUP-MURO_NEGRO` → `A-MURO`; `SUP-DEM` → `A-PROY-01` |
| Calco de PDF (basura) | `PDF_*` (4), `PDF3_*` (7), `PDF_RECUADRO` | Congelar o purgar. Son rastros de calco, nunca imprimen |
| Sin prefijo de función | `MURO`, `MUROS`, `DET`, `metra`, `POLILINEAS`, `CORRECCIONES`, `INCENDIO`, `INCENDIO-TEXTO` | Redirigir a la capa que corresponde o purgar |
| Sin calificar | `PLUSVALIA`, `PLUSVALIA 2` | Fuera del SET: la plusvalía se calcula sobre el Cuadro de Usos y la Ley Tarifaria, no se dibuja. Ver `docs/normativa-dgiur.md` |
| Ruido de bloque | ~280 definiciones `*D###` + `A$C...` anónimas | `PURGE` |
| Layout sin estandarizar | `Presentación1` (vacía, `Microsoft Print to PDF`) | Renombrar a `USO-PTipo-A1`, plotter según §4.4 |

---

## 3. STANDARS — Reglas

### 3.1 Rayados

Los tres estados que define el Anexo, y cómo se dibujan:

| Estado oficial | Rayado | Dónde |
|----------------|--------|-------|
| Superficie habilitada / autorizada | **135°** | Hatch en `SUP-AUT` |
| Superficie para la que **no** se solicita autorización | **45°** | Hatch en la polilínea de superficie correspondiente, sin capa propia |
| Superficie a ampliar / disminuir / redistribuir | **sin rayado** | Sin hatch. Queda superficie limpia |

- Si se combinan dos o más situaciones, la superficie a ampliar **sin ninguna clase de rayado** y las restantes se identifican con un rayado distinto a los anteriores
- Cada estado se referencia en el **campo de notas** de la carátula
- La clave de lectura es la que acabo de escribir: 135° autorizada · 45° no solicitada · sin rayado a modificar

### 3.2 Línea Oficial y Linderos

- **Línea Oficial (L.O.)** y **Líneas Divisorias de Parcela (L.D.P.)** se individualizan siempre
- Los linderos se acotan contra la L.O., nunca contra el muro
- El croquis de ubicación lleva las medidas de la parcela y el ancho de calle (§1.5)

### 3.3 Salidas

- **Salidas exigidas** y **medios de salida** van marcados individualmente
- Su medida se acota en `A-COTAS`
- La dimensión de los destinos, de las áreas semicubiertas y descubiertas, y de los medios de salida va en el mismo juego de cotas

### 3.4 Servicios de salubridad

- La **ubicación de los servicios de salubridad** con sus correspondientes **artefactos sanitarios** se dibuja en `A-EQUIP`
- Cuando el caso lo requiera, se agrega la **planilla de artefactos sanitarios** (§1.4) como anexo

### 3.5 Planilla de iluminación y ventilación

- **Obligatoria** (it. 3 de §1.2). Pasa de "carga manual pendiente" a contenido exigido
- Una fila por local
- Hoy se carga a mano; después se referencia a un bloque común con el índice como parámetro, de modo que cambiar el índice de un local se aplique a todos los de su tipo

### 3.6 Balance de superficies

- Cuando el caso lo requiera, el **balance de superficies** se dibuja junto a la planta, no como anexo suelto

### 3.7 Alturas

- **Alturas libres** individualizadas por local
- Las **cotas de niveles de piso terminado de cada planta** se miden contra el **nivel de piso en vereda sobre la L.O. frente al acceso principal**: ese es el cero único del plano
- Los niveles se marcan con `SIMB-NIV` en su posición real dentro del corte

### 3.8 Locales

- Cada local lleva su marca `SIMB-LOC`: texto + número
- El número es un **POS correlativo** (§6.3): `PB01`, `P102`, `P203`
- El bloque mide el **área del local automáticamente** — el área que aparece en `PL-LOC` es la misma que la del símbolo
- La suma de las áreas de los locales debe dar la superficie declarada
- Cada local lleva **uso y destino** identificados (§1.3, it. 8)

### 3.9 Carpintería y herrería

- Las puertas van como **bloques**, todos en capa `0` (patrón AutoCAD), y se explotan a `A-CARP-01` / `A-CARP-02` según el grosor de trazo
- El barrido de cada puerta va en línea punteada
- La puerta tipo es `A-CARP-PU-088`: hoja 0.80 para vano 0.88
- Se puede **flipar** para cambiar entre mano derecha y mano izquierda, y el cambio se refleja en la planilla de carpinterías
- La herrería (barandas, pasamanos) va en `A-HERR` con lineweight 0.00

### 3.10 Equipamiento

- Todo el equipamiento necesario para la habilitación va en `A-EQUIP` (ACI 251)
- Se dibuja a la escala del plano, no como símbolo genérico

### 3.11 Estados N/E/D

- N = nuevo, E = existente, D = a demoler (alineado NCS + ISO 13567)
- En el plano de uso: lo existente va a `A-MURO-EXIST` como superposición no imprimible; lo nuevo va a `A-MURO` y su superficie a `SUP-NVO`
- Ej: `A-MURO`, `A-MURO-EXIST`

---

## 4. HERRAMIENTAS — Comandos → Capas

### 4.1 Comandos por categoría

| Función | Comandos | Capas |
|---------|----------|-------|
| Capas | `LAYER`, `LAYISO`, `LAYFRZ`, `QSELECT` | Todas `A-`/`SUP-`/`SIMB-`/`PL-`/`ROT-` |
| Dimensión | `DIM`, `DLI`, `DAL`, `DIMSTYLE`, `DIMCONTINUE` | `A-COTAS`, `A-COTAS-2` |
| Texto | `MTEXT`, `TEXT`, `STYLE` | `SIMB-LOC`, `SIMB-NIV`, `PL-LOC` |
| Edición | `MOVE`, `COPY`, `OFFSET`, `TRIM`, `EXTEND`, `ARRAY` | Todas |
| Bloques | `BLOCK`, `INSERT`, `BEDIT`, `BATTMAN`, `ATTSYNC`, `MIRROR` (flip) | `0` → `A-CARP-01`/`-02`, `SIMB-*` |
| Bloques dinámicos | `BEDIT` → pestaña Parámetros | §6 (4 bloques) |
| Rayados | `HATCH`, `SOLIDEDIT`, `HATCHEDIT` | `SUP-AUT` (135°), 45° sin capa propia |
| Áreas | `AREA`, `LIST`, `MASSPROP` | `SUP-SEMI`, `SUP-DESC`, `SUP-NVO` |
| Datos | `DATAEXTRACTION` | `SIMB-LOC` → `PL-LOC` |
| Plot | `PLOT`, `PUBLISH` | Todas (CTB `monochrome.ctb`) |
| Estándares | `CHECKSTANDARDS`, `LAYTRANS`, `AUDIT`, `PURGE` | Todas |
| Sombra | `HATCH`, `SOLIDEDIT` | `A-SOLADOS` |

### 4.2 SETEO — Setup base (`acadiso.dwt` → `SET_02-GEST.dwt`)

Base: `acadiso.dwt`. Este § define el QUÉ; el CÓMO paso a paso está en `02-ft-SET_02.md` §1.

**Unidades — metros, 2 decimales:**

| Variable | Valor | Significado |
|----------|-------|-------------|
| `LUNITS` | 2 | Decimal (1 unidad = 1 m, formato 0.00) |
| `LUPREC` | 2 | Precisión 2 decimales |
| `INSUNITS` | 6 | Metros |
| `MEASUREMENT` | 1 | Métrico |
| `-DWGUNITS` | 6, sin reescalar geometría | Fija metros e iguala INSUNITS |

Fuentes: [Convert imperial unit drawing to metric units (-DWGUNITS)](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Convert-imperial-unit-drawing-to-metric-units.html) · [About Block Units and Insertion Scale](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-6C46049D-8636-442D-8BAC-CF4FD515FDC0)

**Escala — 1:100 única:**

Los planos municipales van a una sola escala, así que la lista de escalas del SET_02 tiene **una sola entrada**.

| Entrada | Paper | Drawing | Factor | Uso |
|---------|-------|---------|--------|-----|
| `1:100` | 1 (=1 mm) | 0.1 (=0.1 m) | **10** | Todos los viewports del plano de uso |

El modelo se dibuja en metros y el papel en milímetros. Para 1:100, 1 m de modelo sale a 10 mm en papel → **CustomScale del viewport = 1000 / denominador = 1000 / 100 = 10**, que es `ZOOM 10 XP`. La barra de estado del viewport debe mostrar **1:100**.

> La barra de status tiene que coincidir con la escala que declara la carátula. Si la escala vive solo en el rótulo y el viewport muestra otra cosa, la lámina miente.

Fuentes: [Custom scale does not scale viewports as expected](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-scale-does-not-scale-viewports-as-expected-in-AutoCAD.html) · [Viewport Scale doc](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-3B8EA357-0906-41D2-B2B0-8EAEA4CA2CF8)

**Estilos — pendientes de definir.** SET_01 usa `EP-2.5` / `EP-3.5` (texto anotativo) y `EP-ARQ` (cotas). Para SET_02 hay que decidir si se heredan esos nombres o se definen nuevos (`USO-2.5`, `USO-3.5`, `USO-COTAS`) que dejen explícito que el plano municipal tiene su propio juego. **Decisión pendiente (2026-10-05).**

### 4.3 DWS (`SET_02-GEST.dws`)

Verifica capas, estilos texto/cota/directriz, tipos de línea. Comando: `CHECKSTANDARDS`.

### 4.4 CTB y plotter

**CTB: `monochrome.ctb`** (estándar de AutoCAD).

La razón es normativa, no estética. El Anexo III exige *"líneas de color negro con fondo blanco"* (§1.1). El color de capa cumple otra función: distinguir en pantalla mientras se dibuja. Con `monochrome.ctb` todo sale negro y lo que gobierna la lectura de la lámina es el **lineweight** de cada capa, definido en §2.

> **Por qué no `CABA-MILLERCO.ctb`**: ese CTB del estudio mapea por color, y con 25 capas el resultado son 25 tonos distintos sobre la lámina. Es útil para revisión interna; no cumple lo que pide el trámite.
>
> **Consecuencia de diseño**: como el CTB es monocromo, la separación por color en pantalla es la única herramienta de lectura durante el dibujo. Por eso las 25 capas tienen color y lineweight bien diferenciados en §2.

**Plotter**: `DWF-CABA.pc3` con su `.pmp`, en `CONFIGURACION/PLOTTERS/PC3/` y `PMP/` (`G:\Mi unidad\G#GESTIONES\TEMPLATES\BOTONERA-APP\APP-PARA-AUTOCAD\`). Es el plotter que ya trae el estudio.

> El Anexo III no fija formato de archivo (§1.5). El DWF es decisión del estudio, tomándolo de la configuración que ya existe.

### 4.5 Equivalencias internacionales

| SET_02 | NCS | ISO 13567 | AEC UK |
|--------|-----|-----------|--------|
| `A-MURO` | A-WALL-FULL-N | A-G25---E-N | A-MU-... |
| `A-MURO-EXIST` | A-WALL-FULL-E | A-G25---E-E | A-MU-...-E |
| `A-EJES` | AJ-EJES* | A-...-G- | A-EJ-... |
| `A-COTAS` | AJ-COTA* | A-...-D- | A-CO-... |
| `A-SOLADOS` | A-FLOR-FIN | A-FLOR-... | A-FL-... |
| `A-EQUIP` | A-FURN-EQPM | A-...-F- | A-FU-... |
| `SIMB-NIV` | A-ANNO-LEVL | A-...-L- | A-LV-... |
| `SIMB-LOC` | A-ANNO-IDEN | A-...-I- | A-ID-... |
| `SIMB-CORTE` | A-ANNO-SECT | A-...-S- | A-SC-... |
| `PL-LOC` | A-ANNO-TABL | A-...-T- | A-TB-... |
| `ROT-HOJA` | G-ANNO-TTLB | A-...-B- | G-TT-... |

> *R en NCS = "Resource". SET_02 exporta a NCS mapeando `A-` a AJ/AK (definible por el usuario) y `SIMB-`/`PL-` a `A-ANNO-*`, que ya existe en NCS. Guardar el mapeo en DWS vía `LAYTRANS`.
>
> **Nota**: `SIMB-` y `PL-` no son designadores NCS. En la exportación se traducen a `A-ANNO-*`; internamente el estudio usa `SIMB-` y `PL-` porque son más cortos y más claros en pantalla.

### 4.6 Sombra

Los rayados van en la capa de la superficie que corresponden (§3.1). `A-SOLADOS` lleva el cambio de piso y las escaleras, con su propio hatch cuando corresponda.

### 4.7 Plot de la lámina

| Parámetro | Valor |
|---|---|
| CTB | `monochrome.ctb` |
| Plotter | `DWF-CABA.pc3` |
| Fondo | Blanco (sin `Background` en el plot) |

### 4.8 LAYOUT — `USO-PTipo-A1`

| Parámetro | Valor |
|---|---|
| Nombre | `USO-PTipo-A1` |
| Formato | ISO A1 841×594 mm, apaisado |
| Plotter | `DWF-CABA.pc3` |
| CTB | `monochrome.ctb` |
| Escala de trazado | 1:1 (1 mm = 1 unidad) |
| **Viewports** | **Arranca con uno**, CustomScale 10 → 1:100, display locked |
| Hoja | El área del plano, **separada de la carátula** |
| Planillas | Bloques sobre la hoja, no viewports |
| Carátula | Bloque `GCBA-CRTL-*` en `ROT-HOJA` / `ROT-TXT` |

**Un solo layout con varios viewports.** La presentación se arma en una única hoja: cada dibujo es un viewport, y todos a 1:100.

1. **Empieza con un viewport** para la planta principal, a CustomScale 10. Verificar que la barra de estado muestre `1:100`.
2. Los viewports siguientes se abren **uno por corte o por dibujo** según haga falta, siempre a 1:100 y siempre con display locked.
3. El corte transversal de la unidad va en su propio viewport, no superpuesto a la planta.
4. El croquis de ubicación y el balance de superficies, cuando correspondan, van en viewports propios.

> **Hoja separada de carátula**: la carátula es un bloque (`GCBA-CRTL-*`) y no se integra al marco de la hoja. Se cambia, se actualiza y se versiona por separado, y la hoja conserva su geometría.

Creación del layout vía `-LAYOUT New` → `PAGESETUP` con el plotter `DWF-CABA.pc3`.

> **Regla del estudio MVP_02**: el nombre del layout codifica `<SET>-PTipo-<formato>`. Otros tamaños si hacen falta: `USO-PTipo-A0`, `USO-PTipo-A3`.

---

## 5. PUNTAS

- `LAYFRZ` (no `LAYOFF`) para apagar `A-MURO-EXIST` mientras se dibuja lo nuevo: así el existente queda a la vista sin imprimir
- `AREA` sobre la polilínea de `SUP-SEMI`, `SUP-DESC` y `SUP-NVO` para el balance de superficies
- Explotar los bloques de puerta con `EXPLODE` solo al final; hasta entonces se mantienen dinámicos para el flip mano d/i
- `MIRROR` horizontal sobre `A-CARP-PU-088` cambia mano derecha / izquierda
- `DIMCONTINUE` para las cotas acumuladas de parcela, `DIMBASELINE` para las cotas parciales de local
- `DATAEXTRACTION` de `SIMB-LOC` → `PL-LOC`: la planilla de locales se actualiza sola
- Congelar las capas `PDF_*` antes de plotear: son rastros de calco y ensucian la lámina
- `AUDIT` + `PURGE` antes de entregar: en el modelo auditado hay ~280 bloques `*D###` anónimos
- El rótulo se arma con `ROT-HOJA` / `ROT-TXT` en paper, nunca en modelo

---

## 6. BLOQUES — Especificación

> **Estado 2026-10-05**: los 4 bloques dinámicos están **especificados, no implementados**. Se documentan en `docs/bloques-dinamicos.md` para construirlos en AutoCAD.
>
> Regla general: los bloques de carpintería y herrería se crean en **capa `0`** (patrón AutoCAD) y se explotan a la capa que corresponda después.

### 6.1 `A-CARP-PU-088` — Puerta tipo

> Requisito oficial que lo origina (§1.3, it. 10): *"Puertas, con su sentido de apertura y barrido."*

| Parámetro / atributo | Valor |
|----------------------|-------|
| Tipo | Dinámico, con acción *flip* |
| Vano | 0.88 m |
| Hoja | 0.80 m |
| Capas de explotación | `A-CARP-01` (trazo 0.15), `A-CARP-02` (trazo 0.05) |
| Color | 2 (amarillo), ambos trazos |
| Barrido | Línea **punteada** (DASHED) |
| Mano | Derecha por defecto; `MIRROR` horizontal → izquierda |
| Salida | Planilla de carpinterías vía `BATTMAN` + `DATAEXTRACTION` |
| Capa de bloque | `0` |

**Uso**: se inserta un bloque por vano. El flip cambia mano sin redibujar. La planilla se arma con `BATTMAN` sobre el bloque, de modo que al reflipar el bloque el dato de mano se actualiza solo.

### 6.2 `SIMB-NIV-NPT` — Símbolo de nivel terminado

> Requisito oficial que lo origina (§1.3, it. 12): *"Cotas de niveles de piso terminado de cada planta, respecto del nivel de piso en vereda sobre la L.O. frente al acceso principal."*
>
> Y también (§1.3, it. 5): *"Alturas libres."*

| Parámetro / atributo | Valor |
|----------------------|-------|
| Tipo | Dinámico |
| Texto fijo | Triángulo + línea de nivel |
| **Altura real** | **Atributo dinámico: lee la altura real del corte** |
| Cero | Nivel de vereda sobre la L.O. frente al acceso principal (§3.7) |
| Capa | `SIMB-NIV` |

**Por qué dinámico**: hoy el nivel se carga a mano y eso admite el error. Un bloque con altura real obliga a que la cota del corte sea la fuente única: si cambia la altura, cambia el símbolo. El cero del plano es uno solo —la vereda en la L.O. frente al acceso principal—, así que el símbolo no puede tener un origen propio distinto.

### 6.3 `SIMB-LOC-01` — Símbolo de local

> Requisito oficial que lo origina (§1.3, it. 8): *"Identificación y uso y destino de cada local."*

| Parámetro / atributo | Valor |
|----------------------|-------|
| Tipo | Dinámico |
| Contenido | Texto descriptivo + número de local |
| **POS** | **Correlativo (ver abajo)** |
| **Área** | **Se mide automáticamente** |
| Iluminación / ventilación | Hoy manual; después referenciable a bloque (§3.5) |
| Capa | `SIMB-LOC` |

**POS correlativo.** El número tiene dos componentes: la última unidad es correlativa 1, 2, 3… y la parte anterior es el piso, que se agrega por tramos de 100.

| Piso | Tramo | POS resultante | Ejemplos |
|------|-------|----------------|----------|
| Planta baja | +000 | `PB00n` | `PB01`, `PB02`, `PB03` |
| Primer piso | +100 | `P1nn` | `P102`, `P103`, `P204` |
| Segundo piso | +200 | `P2nn` | `P203` |
| En adelante | +100 por piso | `P3nn`, `P4nn`… | `P301`, `P402` |

> O sea: el **2** de `PB01` es correlativo del piso; el **0** es el piso en centenas; y el 1 final es el número de local. Cuando cambia el piso, el correlativo arranca de nuevo (1, 2, 3) pero el piso suma 100.
>
> Esto permite que `DATAEXTRACTION` ordene la planilla por piso: el orden natural del número ya coincide con el orden constructivo.

**Área.** El bloque mide el área del local automáticamente. La superficie que aparece en `PL-LOC` es la misma que la del símbolo — misma fuente de verdad. La suma de los locales debe dar la superficie declarada.

**Iluminación y ventilación.** Ver §3.5: hoy se cargan a mano; cuando se definan, van como referencia a un bloque común, de modo que cambiar el índice se aplique a todos los locales de una vez.

### 6.4 `SIMB-CORTE-01` — Marca de corte

> Requisito oficial que lo origina (§1.2, it. 2): *"El corte de la unidad que se desea autorizar."*

| Parámetro / atributo | Valor |
|----------------------|-------|
| Tipo | Dinámico |
| Contenido | Letra + posición en planta + posición en corte |
| Criterio | Igual que `SIMB-NIV-NPT`: la posición del corte se lee de la cota real |
| Capa | `SIMB-CORTE` |

Misma lógica que el nivel: posición en planta y posición en corte salen de la cota real del corte, no de un texto suelto.

### 6.5 Bloque de herrería

Barandas y pasamanos. Bloque en capa `0`, se explota a `A-HERR` con lineweight 0.00. Sin bloque dinámico por ahora.

### 6.6 Bloque de croquis de ubicación

> Requisito oficial que lo origina (§1.5): *"Croquis de ubicación, indicando medidas de la parcela y ancho de calle."*

Sin bloque dinámico: se dibuja en su propio viewport (§4.8) con las medidas en `A-COTAS-2`.

### 6.7 Carátula — `GCBA-CRTL-*`

> **Prefijo `GCBA-CRTL-`.** El `G-` de SET_01 §10.2 (`G-CART-MEPA`) fue un error de nomenclatura: `G-` nunca debió ser prefijo. SET_02 usa el prefijo correcto. SET_01 queda para revisión aparte.

Dos bloques fijos:

| Bloque | Uso |
|--------|-----|
| `GCBA-CRTL-PLANO_USO` | Carátula del plano de uso de actividad económica |
| `GCBA-CRTL-PLANO_UNICO` | Carátula de la presentación en plano único |

Van en `ROT-HOJA` (recuadro) y `ROT-TXT` (textos fijos), en paper space. **Separados de la hoja** (§4.8): cambiar la carátula no toca la geometría del plano.

**Campos del bloque**, tomados de §1.5 y del modelo del Anexo:

| Campo | Origen |
|-------|--------|
| Rubro o descripción | §1.5, dato 1 |
| Ciudadano Responsable | §1.5, dato 1 |
| Domicilio | §1.5, dato 1 |
| Plantas a autorizar | §1.5, dato 1 |
| UF (de corresponder) | §1.5, dato 1 |
| Datos catastrales de la parcela | §1.5, dato 1 |
| Mixtura de Usos del Suelo y/o Área Especial Individualizada | §1.5, dato 3 |
| Superficie cubierta | §1.5, dato 4 |
| Superficie semicubierta | §1.5, dato 4 |
| Superficie descubierta | §1.5, dato 4 |
| Superficie total | §1.5, dato 4 |
| Cantidad de personas que trabajan por turno | §1.5, dato 5 |
| Nombre del Profesional Responsable | §1.5, dato 6 |
| Título o Profesión | §1.5, dato 6 |
| N° de matrícula | §1.5, dato 6 |
| Hoja Adicional de Firmas | Modelo de carátula, ítem 9 del Anexo |
| Informe gráfico | Modelo de carátula, ítem 9 del Anexo |
| Número | Modelo de carátula, ítem 9 del Anexo |
| Fecha | Modelo de carátula, ítem 9 del Anexo |
| Referencia | Modelo de carátula, ítem 9 del Anexo |
| **Croquis de ubicación** | §1.5, dato 2 — medidas de parcela y ancho de calle |
| **Campo de notas** | §3.1 — referenciando cada estado de rayado |

> **El croquis va en la carátula**, no es un viewport aparte: el Anexo lo pide entre los datos de la carátula. Por eso no lleva bloque propio en §6.6 más allá de dibujarse dentro del área de carátula.

### 6.8 Bloques preexistentes que se preservan

El modelo auditado tiene bloques de carátula que ya funcionan y conviene mirar antes de construir los nuevos: `CARATULA-CABA-2023` (147 entidades), `CARATULA_SIMB_RT2023` (103), `CARATULA_SIMB_IS_RT2023` (103), `CARATULA-CABA-2020-SIMB` (13), `CARATULA-CROQUIS-` (7). Se contrastan contra `GCBA-CRTL-*` antes de decidir si se reconstruyen o se versionan.

---

## 7. AutoLISP — `SET_02-GEST.lsp`

```lisp
; SET_02-GEST.lsp — borrador v0.2 (25 capas, prefijo por funcion)
; Ejecutar: SET-02-GEST

(defun c:SET-02-GEST (/)
  (vl-load-com)
  (SET-GEST-CAPAS)
  (SET-GEST-VARIABLES)
  (princ "\nSET_02-GEST_DGIUR_USO v0.2 aplicado (25 capas).")
  (princ)
)

(defun SET-GEST-CAPAS (/
  ; (mk "nombre" color linetype lineweight plot-no)
  ; A- arquitectura (15)
  (mk "A-MURO"         7   "CONTINUOUS" 0.50 nil)
  (mk "A-MURO-EXIST"   5   "CONTINUOUS" 0.35 t)
  (mk "A-CARP-01"      2   "CONTINUOUS" 0.15 nil)
  (mk "A-CARP-02"      2   "CONTINUOUS" 0.05 nil)
  (mk "A-COTAS"        7   "CONTINUOUS" 0.25 nil)
  (mk "A-COTAS-2"      7   "CONTINUOUS" 0.35 nil)
  (mk "A-SOLADOS"    250   "CONTINUOUS" 0.25 nil)
  (mk "A-HERR"         6   "CONTINUOUS" 0.00 nil)
  (mk "A-PROY-01"      6   "DASHED"     0.25 nil)
  (mk "A-PROY-02"      6   "DASHDOT"    0.25 nil)
  (mk "A-EJES"         3   "DASHDOT"    0.35 nil)
  (mk "A-EQUIP"      251   "CONTINUOUS" 0.25 nil)
  (mk "A-VISTA-01"   254   "CONTINUOUS" 0.25 nil)
  (mk "A-VISTA-02"   252   "CONTINUOUS" 0.25 nil)
  (mk "A-VISTA-03"   251   "CONTINUOUS" 0.25 nil)
  ; SUP- superficies (4)
  (mk "SUP-AUT"      34   "CONTINUOUS" 0.25 nil)
  (mk "SUP-SEMI"     44   "CONTINUOUS" 0.25 nil)
  (mk "SUP-DESC"    140   "CONTINUOUS" 0.25 nil)
  (mk "SUP-NVO"       1   "CONTINUOUS" 0.25 nil)
  ; SIMB- simbologia (3)
  (mk "SIMB-NIV"     31   "CONTINUOUS" 0.25 nil)
  (mk "SIMB-LOC"      3   "CONTINUOUS" 0.25 nil)
  (mk "SIMB-CORTE"    1   "CONTINUOUS" 0.35 nil)
  ; PL- planillas (1)
  (mk "PL-LOC"        7   "CONTINUOUS" 0.25 nil)
  ; ROT- caratula (2, paper)
  (mk "ROT-HOJA"      5   "CONTINUOUS" 0.00 t)
  (mk "ROT-TXT"       7   "CONTINUOUS" 0.00 t)
  (princ)
)

(defun SET-GEST-VARIABLES (/
  (setvar "LUNITS" 2)
  (setvar "LUPREC" 2)
  (setvar "MEASUREMENT" 1)
  (setvar "INSUNITS" 6)
  (setvar "OSMODE" 511)
  (princ)
)
```

> `mk` es placeholder: falta implementar con la API de layers (como en SET_01 §7). El `Plot = No` de `A-MURO-EXIST`, `ROT-HOJA` y `ROT-TXT` se marca con `(vl-catch-all-apply 'vla-put-Plot (list lay :vlax-true))`.
>
> Los colores ACI se conservan para lectura en pantalla; el ploteo a negro lo resuelve `monochrome.ctb` (§4.4).

---

## 8. Fuentes

### 8.1 Documento de referencia oficial — fuente primaria

| Campo | Valor |
|-------|-------|
| Archivo | `G:\Mi unidad\G#GESTIONES\TEMPLATES\PLANO_USOAnexoIII.pdf` |
| Título | Anexo III — Formularios de Presentación de Solicitud de Actividad Económica |
| Órgano emisor | **DGHP** (Dirección General de Habilitaciones y Permisos) |
| Expediente | `IF-2025-11263770-GCABA-DGHP` |
| Fecha | 13 de marzo de 2025 |
| Extensión | 21 páginas |
| Firma | Carla Borgognoni, Director General |

**Ítems que gobiernan este spec**: el 6 (Contenido del Plano de Uso de Actividad Económica) y el 7 (Plano de Uso de Redistribución / Ampliación / Disminución). El 9 define el modelo de carátula.

> El texto del PDF se extrajo el 2026-10-05 descomprimiendo los content streams y reconstruyendo los operadores `Tm` + `TJ` con separación de columnas. Las listas del §6 del Anexo se verificaron item por item contra las coordenadas para confirmar que no había intercalación entre columnas.

### 8.2 Marco normativo de referencia secundaria

| Norma | Qué regula |
|-------|------------|
| **Ley 6099** (texto consolidado por Ley 6764, mod. Ley 6776) | Código Urbanístico de CABA. Título 3: Normas de uso del suelo. §3.3: Cuadro de Usos del Suelo |
| **Decreto 99/GCABA/2019** | Reglamentación del Código Urbanístico |
| **Decreto 475/20** | Secretaría de Desarrollo Urbano como autoridad de aplicación de la Ley 6099 |
| **Decreto 334/24** | Responsabilidades primarias de la DGIUR |
| **Disposición 970/DGIUR/23** | Procedimientos de las consultas de interpretación urbanística (deroga la 448/23) |
| **Disposición 1317/DGIUR/25** | Autorización simplificada para localización de usos en inmuebles catalogados |
| **Ley 6062** | Derecho para el Desarrollo Urbano y el Hábitat Sustentable (plusvalía), incorporada al Código Fiscal |
| **Decreto 105/19** | Procedimiento de cálculo de la base imponible de la plusvalía |
| **Ley 2930** | Plan Urbano Ambiental (ley marco) |
| **Ley 6466** | Fondo para el Desarrollo Urbano Sustentable (FODUS) |

Detalle completo y URLs en `docs/normativa-dgiur.md`.

### 8.3 Autodesk (heredadas de SET_01, vigentes)

- [Convert imperial unit drawing to metric units (-DWGUNITS)](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Convert-imperial-unit-drawing-to-metric-units.html)
- [Custom scale does not scale viewports as expected](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-scale-does-not-scale-viewports-as-expected-in-AutoCAD.html)
- [About Block Units and Insertion Scale](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-6C46049D-8636-442D-8BAC-CF4FD515FDC0)
- [Viewport Scale doc](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-3B8EA357-0906-41D2-B2B0-8EAEA4CA2CF8)

### 8.4 Kit temático del estudio

`raw/docs/Estudio Pi – Kit temático  SETs de estándar CAD.md` — el §5 define la lista de SETs temáticos. SET_02-GEST es un SET **de gestión**, no temático: se agrega al conjunto porque el plano de uso es un documento que el estudio produce, pero no proviene de un SET temático del Kit. Conviene registrarlo en el Kit cuando se actualice.

---

## 9. Próximos pasos

1. [ ] Validar las 25 capas con el equipo
2. [ ] Confirmar que `monochrome.ctb` está disponible en el entorno AutoCAD del estudio
3. [ ] Definir los estilos de texto y cota de SET_02 (¿heredar `EP-*` de SET_01 o definir `USO-*`?)
4. [ ] Implementar los 4 bloques dinámicos desde `docs/bloques-dinamicos.md`
5. [ ] Construir `GCBA-CRTL-PLANO_USO` y `GCBA-CRTL-PLANO_UNICO` mapeando los 21 campos de §6.7
6. [ ] Comparar `GCBA-CRTL-*` contra los bloques preexistentes del modelo (§6.8) y decidir si se versionan o se reconstruyen
7. [ ] Verificar que `DWF-CABA.pc3` esté disponible en el entorno AutoCAD
8. [ ] Crear `SET_02-GEST.dwt` + `SET_02-GEST.dws`
9. [ ] Completar AutoLISP (implementar `mk` con la API de layers)
10. [ ] Plano piloto: presentación completa de una gestión real, un layout con sus viewports a 1:100
11. [ ] @sherlock investiga el marco normativo completo → @vaultworm-arq procesa → wiki

---

## 10. MARCO NORMATIVO — Qué pide el trámite

### 10.1 El Anexo III, ítem por ítem

Todo el contenido exigible está transcrito en §1. La estructura del Anexo es:

| Ítem | Nombre |
|------|--------|
| 1 | Declaración responsable exprés |
| 2 | Solicitud de autorización de actividad económica |
| 3 | Anexo técnico — actividad económica de tipo declaración responsable **sin plano** |
| 4 | Anexo técnico — actividad económica de tipo declaración responsable **con plano y licencia** |
| 5 | Manifestación de transmisión / Declaración responsable de actualización de datos |
| **6** | **Contenido del plano de uso de actividad económica** |
| **7** | **Plano de uso de redistribución / ampliación / disminución de actividad económica** |
| 8 | Anexo técnico de ampliación / disminución de rubro y/o superficie |
| **9** | **Carátula de plano** |

Los ítems que gobiernan el dibujo son **6**, **7** y **9**.

### 10.2 Discrepancia de nombre — DGIUR vs DGHP

El nombre del SET es `SET_02-GEST_DGIUR_USO`, y sin embargo el documento de referencia es del **DGHP**, no de la DGIUR. La diferencia:

| | DGIUR | DGHP |
|---|--------|------|
| Sigla | Dirección General de Interpretación Urbanística | Dirección General de Habilitaciones y Permisos |
| Qué hace | Interpreta el Código Urbanístico: si el uso está permitido y en qué cantidad | Habilita la actividad económica sobre una unidad de uso yahlabilitada |
| Trámites | Consulta de Usos, Consulta Obligatoria General, Certificado Urbanístico | Solicitud de autorización de actividad económica, con o sin plano |
| Documento | CUR (Ley 6099) y sus disposiciones | Anexo III de formularios de actividad económica |

**Decisión 2026-10-05**: se mantiene el nombre `SET_02-GEST_DGIUR_USO` por decisión del estudio, y se deja asentada la discrepancia. La consecuencia práctica es que **el contenido normativo citado en este spec es del Anexo III del DGHP**. Si el SET llega a cubrir también los trámites de DGIUR, hacen falta los checklists de cada uno por separado, porque cambian el formato de entrega y el juego de escalas.

> **Corrección registrada**: la primera hipótesis del análisis fue "Ley 257". El marco real de uso del suelo en CABA es el **Código Urbanístico, Ley 6099**.

### 10.3 Lo que el documento oficial no fija

Verificado el 2026-10-05 sobre el texto extraído del PDF. **0 coincidencias** de:

| Término buscado | Coincidencias |
|-----------------|---------------|
| `escala` | 0 |
| `1:100` | 0 |
| `DWF` | 0 |
| `dwg` | 0 |
| `PDF` | 0 |
| `formato` | 0 |

Presentes sí: `negro` (1), `rayado` (3), `Línea Oficial` (2), `campo`/`notas` (2).

**Conclusión**: el Anexo III fija **qué** hay que dibujar, **cómo se lee** (negro sobre blanco, con valor de línea) y **cómo se rayan** las superficies. No fija **a qué escala** se dibuja ni **en qué formato** se entrega. La escala 1:100 y el DWF son decisiones del estudio (§4.2, §4.4), y quedan anotadas como tales.

---

> *El Anexo III no dice a qué escala. Lo que sí dice es que la línea tiene que valer algo: negro sobre blanco, con su grosor. Un plano municipal se lee por el peso del trazo antes que por el color.*