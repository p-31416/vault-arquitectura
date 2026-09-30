# PLAN DE IMPLEMENTACIÓN — MVP_02 Estándares AutoCAD

> Versión 1.0 · 2026-09-27
> Escalable · Comandos en inglés · Nomenclatura en español

---

## 0. Estructura de carpetas (organización final)

```
MVP_02-autocad-standards/
├── README-mvp_02.md                    # Puerta de entrada. Explica qué es cada doc
├── 00-filo-mvp_02.md                   # FILO → ¿POR QUÉ? (Done)
├── 01-spec-mvp_02.md                   # SPEC → ¿QUÉ?
├── 02-ft-mvp_02.md                     # FT → ¿CÓMO?
├── 03-log-mvp_02.md                    # LOG → ¿CUÁNDO?
│
├── docs/                               # Crudos de Perplexia → FUENTES RAW
│   ├── Estudio_Pi_AutoCAD_doc_maestro.md
│   ├── [crudo_2].md
│   ├── [crudo_3].md
│   └── [crudo_4].md
│
├── n_01-layers/                        # Nivel 1: Layers
│   ├── 01-spec-n_01.md                 # Catálogo universal de capas
│   ├── 02-ft-n_01.md                   # Cómo crear layers (comandos + steps)
│   ├── 03-log-n_01.md                  # Bitácora de n_01
│   └── SET/                            # Aplicaciones específicas
│       ├── SET_01-REP_Replanteo/       # SET 01 (carpeta: spec + lisp + docs)
│       └── lisp-replanteo.lsp          # AutoLISP para replanteo
│
├── n_02-plot/                          # Nivel 2: Plot styles
│   ├── 01-spec-n_02.md                 # Monochrome + CTB por escala
│   ├── 02-ft-n_02.md
│   └── 03-log-n_02.md
│
├── n_03-text-dims/                     # Nivel 3: Text & Dimension styles
│   ├── 01-spec-n_03.md                 # Estilos de texto + dimensión
│   └── ...
│
├── n_04-templates/                     # Nivel 4: DWT templates
│   └── ...
│
├── n_05-blocks/                        # Nivel 5: Bloques estándar
│   └── ...
│
├── n_06-naming/                        # Nivel 6: Naming de planos
│   └── ...
│
├── raw/sessions/                       # Sesiones de trabajo (vaultworm-arq)
├── raw/docs/                           # Crudos procesables
├── raw/brainstorm/                     # Sesiones de brainstorming
└── raw/vaultworm-arq/                  # Digest de vaultworm-arq
```

---

## 1. Definición de cada documento

| Doc | Pregunta | Contenido | DoD (Definition of Done) |
|-----|----------|-----------|--------------------------|
| **00-filo** | ¿POR QUÉ? | Filosofía, principios, propósito del estándar | Manifiesto con ≥7 principios escritos en positivo. Referencia a wiki/glosario |
| **01-spec** | ¿QUÉ? | Catálogo universal: capas, bloques, estilos. Cada item con nombre, color, linetype, lineweight, descripción | Catálogo con ≥1 capas documentadas. Cada layer tiene prefijo (A-/E-/DR-/SIMB-), color ACI, linetype, lineweight |
| **02-ft** | ¿CÓMO? | Metodología de implementación. Comandos, pasos, AutoLISP | Documento con workflow paso a paso. Al menos 1 comando por cada función listada. Propuesta de LISP |
| **03-log** | ¿CUÁNDO? | Bitácora de decisiones, iteraciones, cambios | Cada sesión documentada con fecha, evento, y qué se cambió |
| **README** | ¿QUÉ ES CADA UNO? | Explica FILO/SPEC/FT/LOG con ejemplos | README con tabla de 4 docs + qué contiene cada uno |
| **SET** | ¿AQUÍ Y AHORA? | Aplicación concreta del spec+ft a un tipo de plano | SET con capas aplicadas, orden de trabajo, monochrome configurado |

---

## 2. CHECKLIST DE IMPLEMENTACIÓN — Paso a paso

### FASE 0: Preparación

| # | Tarea | Responsable | DoD |
|---|-------|-------------|-----|
| 0.1 | Crear `raw/docs/` | ✅ Hecho | Carpeta existe con 4 crudos de Perplexia |
| 0.2 | Verificar que hay 4 archivos en `raw/docs/` | sherlock | `ls raw/docs/` → 4 archivos |
| 0.3 | Verificar `00-filo-mvp_02.md` está actualizado | vaultworm-arq | Frontmatter OK, principios positivos, sin negaciones |
| 0.4 | Verificar `02-ft-mvp_02.md` tiene ADR-003 (SET) | sherlock | ADR-003 con SET-replanteo |
| 0.5 | Verificar `03-log-mvp_02.md` tiene entrada SET | sherlock | Entrada SET + vaultworm-arq en bitácora |

### FASE 1: sherlock → Raw de fuentes (iterativo)

| # | Tarea | Agente | DoD |
|---|-------|--------|-----|
| 1.1 | sherlock investiga cada crudo de `raw/docs/` | @sherlock | Cada crudo tiene nota de fuente + procesado |
| 1.2 | sherlock identifica topics, entidades, referentes en cada crudo | @sherlock | Lista de topics por crudo |
| 1.3 | sherlock genera `.md` de raw por cada fuente | @sherlock | `raw/sessions/YYYY-MM-DD-[tema].md` |
| 1.4 | vaultworm-arq analiza cada `.md` de raw | @vaultworm-arq | `raw/vaultworm-arq/digest-YYYY-MM-DD.md` |
| 1.5 | vaultworm-arq propone entradas wiki + links verificados | @vaultworm-arq | Tabla de propuestas (topics → destino wiki) |
| 1.6 | sherlock investiga las referencias web propuestas | @sherlock | Nuevas fuentes verificadas (sin 404) |
| 1.7 | vaultworm-arq re-analiza → digest actualizado | @vaultworm-arq | Digest actualizado con nuevas fuentes |
| 1.8 | Repetir 1.6-1.7 hasta convergencia | Ambos | Todas las fuentes verificadas, todos los topics catalogados |

**DoD de la iteración:**
- Todos los crudos procesados → `raw/sessions/`
- Todos los topics tienen ≥1 fuente verificada
- Todas las entidades tienen `[[wikilinks]]`
- Al menos 1 wildcard por sesión
- Referentes con URLs verificadas (webfetch confirmado)

### FASE 2: SPEC — Catálogo universal de capas

| # | Tarea | Agente | DoD |
|---|-------|--------|-----|
| 2.1 | sherlock define sistema de prefijos | @sherlock | `A-`, `E-`, `DR-`, `REP-`, `SIMB-` documentados |
| 2.2 | sherlock investiga layer naming internacional (AIA/ISO 13567) | @sherlock | Referencias web verificadas |
| 2.3 | sherlock compila catálogo de capas para SET-replanteo | @sherlock | Lista completa: capa, color, linetype, lineweight, descripción |
| 2.4 | sherlock define bloques con atributos | @sherlock | `SIMB-MURO`, `SIMB-P.V`, `E-COL-TXT` — atributos listados |
| 2.5 | vaultworm-arq analiza catálogo de capas | @vaultworm-arq | Propuestas de categorías + wiki links |
| 2.6 | sherlock investiga bloques annotative en AutoCAD | @sherlock | Documentación oficial de Autodesk verificada |
| 2.7 | Definir DIMSTYLE: text height, annotative vs no | @sherlock | Reglas documentadas |
| 2.8 | Definir STYLE de texto para model space | @sherlock | Height ≠ 0 para model, height = tamaño papel para paper |
| 2.9 | sherlock investiga annotative scaling con viewports | @sherlock | Autodesk doc sobre annotative objects |
| 2.10 | vaultworm-arq propone entradas wiki para capas/bloques | @vaultworm-arq | `wiki/glosario/conceptos/` entries |

**DoD del SPEC:**
- Cada layer: `nombre (español)`, `color ACI (número)`, `linetype (inglés)`, `lineweight (mm)`, `descripción`
- Cada bloque: nombre, tipo (dynamic/static), atributos listados, annotative Yes/No
- Cada dimstyle: height, annotative status, scales aplicadas
- Cada textstyle: height, annotative status, font

### FASE 3: FT — Metodología + Setup + LISP

| # | Tarea | Agente | DoD |
|---|-------|--------|-----|
| 3.1 | sherlock documenta setup de DWT | @sherlock | Paso a paso: UNITS, LIMITS, GRID, SNAP, OSNAP |
| 3.2 | sherlock documenta configuración de UNITS | @sherlock | Metric, precision 0.0000, architecture units |
| 3.3 | sherlock documenta DIMSTYLE setup | @sherlock | Annotative Yes, height, offset, arrow, color, scales |
| 3.4 | sherlock documenta STYLE setup | @sherlock | Fonts, heights, annotative status |
| 3.5 | sherlock documenta MLEADERSTYLE setup | @sherlock | Para "ver detalle plano xx" |
| 3.6 | sherlock documenta TABLESTYLE setup | @sherlock | Para Cuadro de Niveles |
| 3.7 | sherlock documenta SCALELISTEDIT | @sherlock | 1:50, 1:100, 1:200, 1:25, 1:1.25 |
| 3.8 | sherlock documenta PAGESETUP + PLOT + monochrome | @sherlock | Configuración de plot sin CTB (monochrome) |
| 3.9 | sherlock investiga annotative dimensions en viewports | @sherlock | Cómo funciona cuando hay múltiples escalas en un mismo dibujo |
| 3.10 | vaultworm-arq analiza FT documentado | @vaultworm-arq | Propuestas de refinamiento |
| 3.11 | sherlock escribe SET-Replanteo.lsp | @sherlock | Funciones: SET-CAPAS, SET-STYLES, SET-DIMSTYLE, SET-VARIABLES |
| 3.12 | vaultworm-arq verifica LISP | @vaultworm-arq | Sintaxis, comandos, nomenclatura |
| 3.13 | sherlock prueba LISP sobre un plano piloto | @sherlock | LISP funciona, aplica todas las capas |

**DoD del FT:**
- Cada setup tiene comandos en inglés + explicación en español
- Cada paso tiene un resultado verificable
- LISP con funciones nombradas en español (SET-CAPAS, SET-STYLES)
- Cada comando con su sintaxis completa

### FASE 4: Monochrome + Viewports + Escalas

| # | Tarea | Agente | DoD |
|---|-------|--------|-----|
| 4.1 | Definir monochrome plot sin CTB | @sherlock | Layer lineweights → monochrome |
| 4.2 | Definir viewports múltiples (1:50 general, 1:25 local, 1:1.25 detalle) | @sherlock | Viewport configurado con SCALELIST |
| 4.3 | Definir cotas acumuladas vs totales | @sherlock | Capas `REP-COTAS-ACU`, `REP-COTAS-TOT` |
| 4.4 | Definir cotas fijas (1:25 para detalles) | @sherlock | Cotas con height fijo, no annotative |
| 4.5 | Definir cotas annotative (model space) | @sherlock | Cotas con Annotative Yes, escalas 1:50, 1:100, 1:200 |
| 4.6 | Definir diferencia entre cota annotative y no annotative | @sherlock | Regla documentada en spec |
| 4.7 | sherlock investiga cuando SÍ usar annotative vs no | @sherlock | Casos de uso específicos para cada tipo de plano |

**DoD del monochrome/viewport:**
- Monochrome: todos los lineweights asignados a capas, no a objects
- Viewports: al menos 2 escalas por plano de replanteo
- Cotas: clasificadas en annotative (viewport-dependente) y fijas (un plano, una escala)
- Regla escrita: "Usa annotative cuando el mismo objeto aparece a distintas escalas en el mismo dibujo"

### FASE 5: Bloques con Atributos + Computación

| # | Tarea | Agente | DoD |
|---|-------|--------|-----|
| 5.1 | sherlock define `SIMB-MURO` como bloque | @sherlock | Rectangle + atributo con nombre (M02, M03...) |
| 5.2 | sherlock define `SIMB-P.V` como bloque | @sherlock | Símbolo de puerta/ventana + atributo |
| 5.3 | sherlock define `E-COL-TXT` como bloque annotative | @sherlock | Rectangle + atributo con medidas x/y (auto-poblado) |
| 5.4 | sherlock define `E-VIGA` como bloque | @sherlock | Línea con interlineado + atributos |
| 5.5 | sherlock investiga DATAEXTRACTION de atributos | @sherlock | Cómo extraer a CSV/Excel |
| 5.6 | vaultworm-arq analiza propuesta de bloques | @vaultworm-arq | Entradas wiki para block types |
| 5.7 | sherlock investiga ATTDEF + BATTMAN + ATTSYNC | @sherlock | Documentación oficial de Autodesk |
| 5.8 | sherlock escribe LISP para crear bloques con atributos | @sherlock | Función `CREA-BLOQUE-ATRIB` |

**DoD de bloques:**
- Cada bloque: geometría + atributo(s) con nombre, tipo, y valor por defecto
- Cada bloque anotative = Yes si escala con viewport
- Cada bloque estático = No si es un símbolo fijo
- DATAEXTRACTION documentado: `DATAEXTRACTION → tabla o Excel`
- Atributos computables = listos para `COUNT`, `DATAEXTRACTION`, `SUM`

### FASE 6: Wiki canonización (futuro, post-convergencia)

| # | Tarea | Agente | DoD |
|---|-------|--------|-----|
| 6.1 | vaultworm-arq genera propuesta wiki final | @vaultworm-arq | Todas las entradas listadas con wikilinks |
| 6.2 | SOL marca aprobar/corregir/descartar | Usuario | Cada entrada marcada |
| 6.3 | vaultworm-arq escribe en wiki/fuentes/ | @vaultworm-arq | Entradas con frontmatter + wikilinks |
| 6.4 | vaultworm-arq actualiza `wiki/glosario/00-index.md` | @vaultworm-arq | Índice actualizado |
| 6.5 | Manuales de uso creados | @sherlock | Lecturas sugeridas + flujos de trabajo |
| 6.6 | README actualizado con referencia a wiki | sherlock | Link a wiki/fuentes/ |

**DoD del wiki:**
- Cada entrada con `tipo: concepto|referente|entidad|software`
- Cada entrada con `## Conceptos relacionados` (≥2 wikilinks)
- Cada entrada con `## Referencias` (≥1 fuente verificada)
- Cada entrada con índice interno `[[#Encabezado exacto]]`
- Sin entradas para personas internas (p-31416, Emilia, Sol)

---

## 3. Workflow sherlock → vaultworm-arq (documentado)

```
┌─────────────────────────────────────────────────┐
│  CICLO ITERATIVO DE CONOCIMIENTO                 │
├─────────────────────────────────────────────────┤
│                                                  │
│  1. @sherlock investiga                          │
│     • Fuentes web, docs, crudos                  │
│     • Genera raw .md                             │
│     • Guarda en raw/sessions/ o raw/docs/        │
│     • Nota: "Fuente X, verificada el DD/MM/AAAA" │
│                                                  │
│  2. @vaultworm-arq analiza                       │
│     • Lee raw/sessions/*.md                      │
│     • Extrae: topics, entidades, referentes       │
│     • Genera digest-YYYY-MM-DD.md               │
│     • Propone: entradas wiki + links             │
│     • Pregunta: "¿Avanzo?"                       │
│                                                  │
│  3. @sherlock investiga más                      │
│     • Toma las referencias del digest            │
│     • Busca, verifica, profundiza                │
│     • Inyecta nuevo raw .md                      │
│                                                  │
│  4. @vaultworm-arq re-analiza                    │
│     • Actualiza digest                          │
│     • Refina propuestas                         │
│     • Agrega/elimina/actualiza entradas         │
│                                                  │
│  ... N iteraciones hasta convergencia            │
│                                                  │
│  5. CONVERGENCIA                                 │
│     • SOL marca: ✅ aprobar / ✏️ corregir / ❌ descartar │
│     • @vaultworm-arq escribe en wiki/fuentes/    │
│     • wiki/glosario/00-index.md actualizado      │
│                                                  │
│  6. POST-CONVERGENCIA                            │
│     • Manuales de uso (@sherlock)                │
│     • Lecturas sugeridas (catálogo de libros)    │
│     • SET-Replanteo.lsp probado                  │
│     • DWT + DWS creados                          │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Reglas del ciclo:**
1. Cada raw `.md` lleva nota de fuente con URL verificada
2. Cada digest tiene máximo 1 iteración por día
3. Cada iteración genera UN digest unificado
4. Nunca se escribe en `wiki/` sin aprobación de SOL
5. Nunca se inventa URL — siempre webfetch verificado
6. Timezone `-03:00 America/Argentina/Buenos_Aires`

---

## 4. DoD — Definition of Done — Nivel global

| Nivel | DoD | Verificación |
|-------|-----|--------------|
| **00-filo** | ≥7 principios en positivo, sin negaciones | `grep -i "no " 00-filo-mvp_02.md` → 0 matches |
| **01-spec** | Catálogo completo con todos los campos por capa | Cada capa: nombre+color+linetype+lineweight+descripción |
| **02-ft** | Cada comando en inglés con explicación en español | Cada step tiene comando + resultado verificable |
| **03-log** | Cada sesión documentada | Fecha + evento + qué cambió |
| **README** | Tabla de 4 docs + ejemplos | README con sección "Qué es cada uno" |
| **SET-replanteo** | Capas + orden de trabajo + LISP | SET con ≥30 capas, LISP con ≥4 funciones |
| **DWT** | Template con todas las capas + estilos | DWT abierto en AutoCAD → capas visibles |
| **DWS** | Archivo de verificación | `CHECKSTANDARDS` pasa sin errores |
| **Bloques** | Cada bloque con atributos listados | `BATTMAN` muestra todos los atributos |
| **Wiki** | Cada entrada con 2 wikilinks + 1 fuente | `[[wikilinks]]` y `## Referencias` presentes |
| **Monochrome** | Todos los lineweights asignados | Ningún object on layer 0 |

---

## 5. Reglas de escalabilidad

| Regla | Detalle |
|-------|---------|
| **Comandos en inglés** | `LAYER`, `STYLE`, `DIMSTYLE`, `BLOCK`, `ATTDEF`, `DATAEXTRACTION`, `MLEADER`, `PAGESETUP`, `PLOT` |
| **Nomenclatura en español** | `A-MURO-MED`, `E-COL-TXT`, `SIMB-P.V`, `REP-EJES`, `A-LC-NOM` |
| **Prefijos universales** | `A-` arquitectura, `E-` estructura, `DR-`/`REP-` replanteo, `SIMB-` simbología |
| **Una función por layer** | Cada layer tiene un solo propósito |
| **Color que se asemeje** | Marrón para madera, verde para planta, etc. |
| **Color 7 para muro terminado** | Siempre white para bordes visibles (imprime en negro en monochrome) |
| **Monochrome primero** | CTB por escala viene después |
| **Metric system** | Siempre metros, precision 0.0000 en UNITS, 0.00 en dimensiones |
| **Annotative para viewports** | Solo cuando el mismo objeto aparece a múltiples escalas en un mismo dibujo |
| **Height ≠ 0 en model space** | Siempre definir text height en mm reales |
| **Blocks para cómputo** | Todo bloque con atributo debe ser computable (COUNT, DATAEXTRACTION) |

---

## 6. Checklist rápido — estado actual

| # | Tarea | Estado |
|---|-------|--------|
| ☐ | `raw/docs/` con 4 archivos de Perplexia | Pendiente (carpeta creada) |
| ☐ | sherlock investiga crudos → raw sessions | Pendiente |
| ☐ | vaultworm-arq analiza → digest | Pendiente |
| ☐ | Catálogo universal de capas completado | En progreso (SET-replanteo ~60 capas) |
| ☐ | DIMSTYLE con annotative definido | Pendiente |
| ☐ | STYLE de texto con height definido | Pendiente |
| ☐ | Bloques con atributos (`SIMB-MURO`, `E-COL-TXT`) | Pendiente |
| ☐ | DATAEXTRACTION documentado | Pendiente |
| ☐ | Monochrome plot configurado | Pendiente |
| ☐ | Viewports múltiples (1:50, 1:25, 1:1.25) | Pendiente |
| ☐ | SET-Replanteo.lsp funcional | Pendiente |
| ☐ | DWT con todas las capas + estilos | Pendiente |
| ☐ | DWS de verificación | Pendiente |
| ☐ | Wiki/fuentes/ canonizado | Pendiente |
| ☐ | Manuales de uso | Pendiente |
| ☐ | README actualizado con explicación FILO/SPEC/FT/LOG | Pendiente |

---

> *El estándar es un organismo vivo: crece, se adapta, incorpora lo que la práctica le regala.*
