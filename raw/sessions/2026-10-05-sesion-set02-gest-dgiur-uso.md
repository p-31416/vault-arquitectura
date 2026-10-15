---
tipo: log
fecha_creacion: 2026-10-05
ultima_actualizacion: 2026-10-05
tags: [sesion, mvp_02, SET_02, autocad, dgpp, dgiur, anexo_III, actividad_economica, rayados, caratula, bloques_dinamicos, norma, auditoria_dwg]
---

# Sesión 2026-10-05 — SET_02-GEST_DGIUR_USO: creación y corrección contra Anexo III oficial

Más nuevo → más arriba

## Resumen ejecutivo

Se creó `SET_02-GEST_DGIUR_USO` en MVP_02 a partir de la auditoría del DWG `MODELO PLANO DE USO.dwg`. A mitad de camino el usuario imposed la regla **"leé el documento oficial antes de definir el ALCANCE, no inventes"**, lo que revealed que el marco legal estaba mal y forzó una reescritura completa del spec contra el **Anexo III de la DGHP**.

**El hallazgo que importa**: el documento oficial es del **DGHP** (Habilitaciones y Permisos), no de la **DGIUR** (Interpretación Urbanística). Son dos organismos distintos, con trámites distintos. El nombre del SET se mantiene `SET_02-GEST_DGIUR_USO` por decisión del estudio, con la discrepancia asentada en §10.2.

## Estado al cierre

`01-spec-SET_02.md` **escrito y aprobado** (753 líneas, v0.2-referencia-oficial). Otros archivos del SET **no existen todavía**.

```
proyectos/MVP_02-autocad-standards/SET_02-GEST_DGIUR_USO/
└── 01-spec-SET_02.md      ← ÚNICO archivo existente
```

## De dónde retomamos

### 1. Archivos que faltan (aprobados en el plan, nunca escritos)

| Archivo | Contenido previsto | Origen |
|---|---|---|
| `README.md` | Índice del SET, estado de archivos, binarios fuera de git | Patrón de `SET_01-REP_Replanteo/README.md` |
| `02-ft-SET_02.md` | CÓMO paso a paso, 10 secciones espejando §0 del spec. Mismo formato que `SET_01-REP_Replanteo/02-ft-SET_01.md` | Hereda SET_01 |
| `docs/auditoria-capas-modelo-uso.md` | Tabla de las **73 capas** del DWG modelo con destino y acción. El spec §2.7 tiene el resumen; el doc tiene el detalle completo | Datos ya recogidos vía MCP |
| `docs/bloques-dinamicos.md` | Los 4 bloques dinámicos con parámetros y atributos, listos para construir en AutoCAD | §6.1–§6.4 del spec |
| `docs/normativa-dgiur.md` | Ley 6099 + Decretos + Disposiciones + URLs verificadas. Nota: el nombre del archivo quedó "dgiur" pero el contenido es mixto CU/DGIUR/DGHP | §8.2 del spec |
| `lisp/` (vacío) | Placeholder para `SET_02-GEST.lsp` | Item 9 del DoD |

### 2. Entradas de índice (no escritas)

- `proyectos/MVP_02-autocad-standards/03-log-mvp_02.md` — nueva entrada, **más nueva arriba**
- `proyectos/MVP_02-autocad-standards/readme-mvp_02.md` — alta de SET_02

### 3. Cerrar sesión formalmente (AGENTS.md pide esto)

- `raw/sessions/2026-10-06-sesion-set02-dgiur-uso.md` cuando se retome

## Decisiones tomadas (no re-preguntar)

| Decisión | Valor | Fecha |
|----------|-------|-------|
| Nombre del SET | `SET_02-GEST_DGIUR_USO` (guiones bajos) | 2026-10-05 |
| Organismo real del documento | **DGHP**, no DGIUR. Discrepancia asentada, nombre se mantiene | 2026-10-05 |
| Prefijos de capa | **5 por función**: `A-` arquitectura · `SUP-` superficies · `SIMB-` simbología · `PL-` planillas · `ROT-` carátula | 2026-10-05 |
| Total de capas | **25** (15+4+3+1+2), contra 73 del modelo | 2026-10-05 |
| CTB | **`monochrome.ctb`** estándar, NO `CABA-MILLERCO.ctb`. Razón: el Anexo exige "líneas de color negro con fondo blanco" | 2026-10-05 |
| Escala | **1:100 única**, viewport CustomScale **10** (= 1000/100, modelo en metros). Barra de status debe mostrar 1:100 | 2026-10-05 |
| Layout | **Uno solo** (`USO-PTipo-A1`), arranca con **un viewport**, los siguientes uno por corte, todos 1:100 | 2026-10-05 |
| Hoja / carátula | **Separadas**. Carátula es bloque aparte, no integrada al marco | 2026-10-05 |
| Bloques de carátula | `GCBA-CRTL-PLANO_USO` y `GCBA-CRTL-PLANO_UNICO` | 2026-10-05 |
| Prefijo `G-` | **Nunca debió usarse** (error de SET_01 §10.2 `G-CART-MEPA`). SET_02 usa `GCBA-CRTL-`. SET_01 queda para revisión aparte | 2026-10-05 |
| Bloques dinámicos | **Documentados, NO implementados** | 2026-10-05 |
| Rayado 45° | Sin capa propia; se dibuja en la polilínea de superficie, se verifica por ángulo + campo de notas | 2026-10-05 |
| Superficie "sin rayado" | Sin capa. Queda superficie limpia, referenciada en campo de notas | 2026-10-05 |

## Cómo se leyó el PDF oficial

El modelo **no puede leer PDFs**. El texto se extrajo con PowerShell + .NET, en memoria, sin escribir archivos:

1. Leer bytes, decodificar Latin1 para ubicar los offsets
2. Localizar cada `stream`, saltear el header zlib (2 bytes), descomprimir con `DeflateStream`
3. Quedarse con los content streams que contienen `BT`
4. En cada bloque `BT...ET`: capturar `Tm` (coordenadas x,y) + concatenar los strings de `(...)`
5. **Separar por coordenada X** para no intercalar las dos columnas del documento

Ese último paso importó: la primera extracción mezclaba las listas del §6 y daba la impresión de que había 12 ítems en "contendrá" cuando son 7, y 7 en "se individualizarán" cuando son 12. Las coordenadas confirmaron el orden real.

**Scripts reutilizables**: si hay que leer otro PDF, el procedimiento sirve tal cual. No hay `pypdf`, `PyPDF2` ni `fitz` en `P:\Anaconda\envs\comfyenv\python.exe`.

## Correcciones hechas sobre mi propio trabajo

| Error | Corrección |
|-------|-----------|
| Hipotesis "Ley 257" como norma de uso del suelo | Es el **Código Urbanístico, Ley 6099** (consolidado 6764, mod. 6776). Queda asentado en §8.1 y §10.2 |
| §1 Alcance inventado | Reemplazado por transcripción literal de los ítems 6, 7 y 9 del Anexo III |
| Mapeo CTB por color ACI | Eliminado. `monochrome.ctb` mapea todo a negro; lo que lee la lámina es el lineweight |
| §10 mezclaba DGIUR + `.dwf` + 1:100 sin fuente propia | §10 reescrito en 3 partes, con lo que el documento **no** fixes explicitado |
| ACI 5 en `A-HERR` y `ROT-HOJA` | Error mío: `A-HERR` es ACI 6. El conflicto real era ACI 251 entre `A-EQUIP` y `A-VISTA-03`, y ya no aplica con CTB monocromo |
| Conteo de ítems invertido en §1.2/§1.3 | Corregido contra las coordenadas del PDF |
| Croquis de ubicación en viewport propio (§4.8 paso 4) | Contradicho: el Anexo lo pide entre los datos de la carátula. Va en el bloque de carátula, anotado en §6.7 |
| Caracteres corruptos (CJK) colados en la escritura | 5 casos, detectados con regex de rangos Unicode y corregidos. Verificado 0 al cierre |

## Hallazgos de la auditoría del DWG

`MODELO PLANO DE USO.dwg` (73 capas, 314 bloques, 2 layouts, `INSUNITS=6`):

- **Duplicaciones**: 4 capas de cotas, 4 de texto, 4 de solado, 3 de equipamiento, 2 de ejes
- **Sin calificar**: `MURO`, `MUROS`, `DET`, `metra`, `POLILINEAS`, `CORRECCIONES`, `INCENDIO`, `PLUSVALIA`, `PLUSVALIA 2`
- **Basura de calco**: 11 capas `PDF_*` / `PDF3_*` (`PDF3_0.15`, `PDF_RECUADRO`, etc.)
- **Ruido**: ~280 bloques `*D###` y `A$C...` anónimos → `PURGE`
- **Layout**: solo `Presentación1`, vacía, `Microsoft Print to PDF`, sin papel definido
- **Lo que sí está bien y se preserva**: `A-VISTA-0..4` + `A-VISTA-HATCH` (sombreado por nivel), `IE-*` (8) y `IS-*` (3) con prefijo disciplina, bloques de carátula `CARATULA-CABA-2023` / `CARATULA_SIMB_RT2023` / `CARATULA_SIMB_IS_RT2023`

**Detalle completo de las 73 capas**: NO está escrito en ningún archivo todavía. Vive solo en el historial de esta sesión y en la conversación. Hay que reconstruirlo para `docs/auditoria-capas-modelo-uso.md` releyendo con `autocad_list_layers` sobre el DWG (que sigue abierto en AutoCAD 2027, sesión `saved: false`).

## Carpeta de trabajo

`G:\Mi unidad\G#GESTIONES\TEMPLATES\`
- `MODELO PLANO DE USO.dwg` — abierto en AutoCAD 2027, **sin guardar**
- `PLANO_USOAnexoIII.pdf` — documento oficial de referencia (3.2 MB, 21 págs)
- `template-caratula-2023.dwg (1)\Template Carátula 2023 (4).dwg` — carátula suelta
- `BOTONERA-APP/APP-PARA-AUTOCAD/CONFIGURACION/` — `CTB/CABA-MILLERCO.ctb`, `PLOTTERS/PC3/DWF-CABA.pc3`, `.pmp`
- `BOTONERA-TEMPLATE/.../BMO/PROYECTO/SISTEMAS/` — nomenclatura de entrega `ARQ-P00-`, `EST-S01-`, etc., con carpeta `SUPERADOS/`

> **Nota**: el DWG tiene `saved: false`. Si se cierra AutoCAD pidiendo guardar, revisar antes.

## Análisis cerebro-digital

### Topics

- El alcance de un SET municipal no se inventa: se transcribe del formulario oficial que la Ciudad define
- La capa, el color y el grosor dejan de ser lo mismo cuando el trámite impone "negro sobre blanco": el color pasa a ser herramienta de trabajo en pantalla, el grosor pasa a ser información
- Tres rayados obligatorios (135° autorizada / 45° no solicitada / sin rayado a modificar) son un sistema de lectura, no un detalle gráfico
- Prefijar por función (`A-`/`SUP-`/`SIMB-`/`PL-`/`ROT-`) evita la ambigüedad de un prefijo único que termina mezclando arquitectura con rotulación
- Un nombre de SET puede no coincidir con el organismo que lo regula: conviene asentar la discrepancia en el spec en vez de forzar el nombre o inventar la fuente

### Entidades

- `SET_02-GEST_DGIUR_USO` (nuevo, MVP_02)
- `DGHP` / `DGIUR` — dos organismos, dos trámites
- `PLANO_USOAnexoIII.pdf` · `IF-2025-11263770-GCABA-DGHP` · Carla Borgognoni · 13/03/2025
- `MODELO PLANO DE USO.dwg` — 73 capas, 314 bloques
- `GCBA-CRTL-PLANO_USO`, `GCBA-CRTL-PLANO_UNICO` (bloques nuevos)
- `A-CARP-PU-088`, `SIMB-NIV-NPT`, `SIMB-LOC-01`, `SIMB-CORTE-01` (dinámicos, documentados)
- `monochrome.ctb`, `DWF-CABA.pc3`, `CABA-MILLERCO.ctb`
- Código Urbanístico Ley 6099 · Decreto 99/19 · DI 970/DGIUR/23 · DI 1317/DGIUR/25 · Ley 6062

### Hechos

- El Anexo III **no fija escala ni formato**: 0 coincidencias de `escala`, `1:100`, `DWF`, `DWG`, `PDF`, `formato` en el texto extraído
- La escala 1:100 y el DWF son decisiones del estudio, registradas como tales en el spec
- Un layout, un viewport inicial, CustomScale 10, todos los viewports a 1:100
- 25 capas contra 73 del modelo: 48 eliminadas por fusión de duplicados
- Los 4 bloques dinámicos quedaron especificados pero no implementados, por decisión explícita
- El texto oficial fue verificado ítem por ítem contra coordenadas de columna antes de transcribirlo

## Lo primero al retomar

1. Releer `01-spec-SET_02.md` §0 y §9 para ver el estado real
2. Preguntar si seguimos con `README.md` + `02-ft-SET_02.md` (los dos de menor riesgo) o con `docs/`
3. Para `docs/auditoria-capas-modelo-uso.md`: reconectar AutoCAD y releer `autocad_list_layers`, porque el detalle de las 73 capas no quedó en ningún archivo
4. Cerrar con entrada en `03-log-mvp_02.md` (más nueva arriba) y alta en `readme-mvp_02.md`
5. Recordar el aviso HITL: cada tanda de escritura necesita `s` explícito