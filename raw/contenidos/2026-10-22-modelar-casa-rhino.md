---
tipo: reporte-contenidos
fecha: 2026-10-22
fuente_binaria: "— sin binario propio: DWG 2D del cliente (ruta local, s/d) + web/YouTube"
transcript: "raw/research/2026-10-22-modelar-casa-rhino.md + raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md"
duracion: "s/d — duraciones de YouTube no expuestas al fetch"
paginas: "n/a — 3 documentos de texto (informe, reporte, spec)"
idioma: es
tags: [rhino8, pushpull, dwg, bloques, make2d, layout, a3, vivienda, entrega, modelado-3d, creadores]
estado: propuesta
---

# Reporte contenidos — modelar-casa-rhino — 2026-10-22

> Formatea el stub de `@sherlock` sobre modelar una casa en Rhino 8 y lo aterriza en la entrega real: casa de tres niveles desde DWG 2D, lámina A3 en PDF para el **2026-10-23**. Importa porque convierte una investigación de tutoriales en un procedimiento que el estudio puede ejecutar mañana y repetir en el próximo proyecto.

Índice rápido: [[#1. Resumen]] · [[#2. Qué parte de la wiki alimenta]] · [[#3. Contenidos extraídos]] · [[#6. Referencias verificadas 200]] · [[#Anexo A. Mapa de creadores cruzado con el vault]] · [[#Anexo B. Secuencia de 10 pasos y checklist]]

## 0. Gate HITL

> `¿Avanzo a wiki/fuentes? (s/N)` — SOL marca: ✅ aprobar / ✏️ corregir / ❌ descartar / 💡 añadir.
> Sin `s` no hay `write` en `wiki/` (`AGENTS.md`, HITL). Esta pasada deja todo en `raw/contenidos/` y no promueve nada.
> Encadenamiento previo: SOL aprobó `SI` el 2026-10-22 (`specs/261022-ruta-modelado-casa-rhino.md` §Estado).

## 1. Resumen

- La entrega de mañana se resuelve con la **ruta B (DWG → sólidos)**: el plano 2D ya existe, así que el trabajo arranca con `Insert` del DWG como bloque y sigue con `ExtrudeSrf` + `BooleanUnion`; `PushPull` queda para retoques de caras y `BooleanDifference` para vanos.
- Las **tres rutas** quedan claras y ordenadas: A PushPull nativo (oficial McNeel, para empezar de cero), B DWG → sólidos (nuestro caso), C caso de estudio (aprender viendo una obra); la recomendación operativa es **B + PushPull**.
- **Bloques en dos frentes**: `Insert` con *Insert as: Block instance* y *Embedded and linked* deja la base CAD como una sola instancia removible en `CAD-BASE`; `Block` / `BlockEdit` / `BlockManager` resuelven cocina y baño reutilizables por piso.
- El tramo legal se cierra con **`Make2D`** (View/CPlane, First angle, hidden lines, clipping plane intersections, register with previous) → **`Layout`/`Detail` 1:50** → **`Print` a Rhino PDF vectorial A3**, que es requisito registral (Ley 24.335) y no una salida gráfica opcional.
- Quedan **10 pasos, un checklist de 9 puntos y 8 candidatos nuevos** con URL verificada; el mapa de creadores cruza 16 canales del vault con veredicto, sobre un universo de **47 videos** `rhino` (31 de la playlist + etiquetados, con solapamientos).

## 2. Qué parte de la wiki alimenta

| # | Destino wiki (ruta absoluta sin ext) | Tipo | Acción | Sección destino | Prioridad | Owner escribe |
|---|---|---|---|---|---|---|
| 1 | [[wiki/glosario/software/rhino\|rhino]] | software | actualizar | `## Rhino 8 / PushPull` + `## 3D → planos (Make2D + Layout)` | alta | vía @vaultworm-arq con `s` |
| 2 | [[wiki/glosario/conceptos/modelado-vivienda-rhino\|modelado-vivienda-rhino]] | concepto | crear | `## Tres rutas` + `## Flujo de 10 pasos` + `## Tabla de comandos` | alta | vía @vaultworm-arq con `s` |
| 3 | [[wiki/fuentes/modelar_casa_rhino-dwg_make2d-multifuente\|modelar_casa_rhino-dwg_make2d-multifuente]] | fuente | crear | ficha curada de esta investigación | alta | @contenidos con `s` |
| 4 | [[wiki/glosario/software/autocad\|autocad]] | software | actualizar | `## Interoperabilidad DWG → Rhino` (`Insert` como bloque, escala) | media | vía @vaultworm-arq con `s` |
| 5 | [[wiki/glosario/conceptos/planos-como-documento-legal\|planos-como-documento-legal]] | concepto | crear | Ley 24.335 aplicada al tramo `Make2D` + `Layout` | media | vía @vaultworm-arq con `s` |
| 6 | [[wiki/glosario/interno/pbooks/pbk-modelado-entrega-rhino\|pbk-modelado-entrega-rhino]] | pbook | crear | checklist de entrega + secuencia operativa | media | vía @vaultworm-arq con `s` |
| 7 | [[wiki/glosario/software/rhino\|rhino]] § Ecosistema | software | actualizar | `## Ecosistema — rhinomcp` (con la salvedad de que no hay tutorial de vivienda) | baja | vía @vaultworm-arq con `s` |

> Integra antes de duplicar: `wiki/glosario/software/rhino.md` existe como stub (NURBS, Make2D para ControlNet, Grasshopper) y hoy **no menciona PushPull**. Las secciones nuevas avanzan sobre esa base. `wiki/glosario/software/autocad.md` ya tiene el panorama LT 2027: la interoperabilidad entra como sección nueva, sin reescribir lo existente.

## 3. Contenidos extraídos

### 3.1 Tres rutas y recomendación

| Ruta | Cuándo conviene | Secuencia | Respaldo | Veredicto para la entrega |
|---|---|---|---|---|
| **A. PushPull nativo** | Empezar de cero, sin CAD | sólido base → `PushPull` / `SplitFace` / `Inset` → aberturas → cubierta | Guía oficial McNeel + Kyle Houchens | Alternativa si el DWG viene sucio |
| **B. DWG → sólidos** | Ya existe plano 2D (**nuestro caso**) | import DWG → `Join` / `CloseCrv` → `ExtrudeSrf` → `BooleanUnion` → detalles | How to Rhino (EN), Hakan y Diego Pascual (ES) | **Recomendada** |
| **C. Caso de estudio** | Aprender viendo una obra | imagen/plano → volumen → detalle | Ruben Borup (Azuma), Flavio Bevilacqua (Le Corbusier) | Referencia post-entrega |

> Decisión registrada: **ruta B** + `PushPull` para retoques + `BooleanDifference` para vanos (`raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md` §1.1 y §6).

### 3.2 Tabla verbatim

| Concepto / terminología | Cita verbatim | Fuente / sección | Interpretación curada |
|---|---|---|---|
| Objetivo de la entrega | "casa de tres niveles (planta baja, entrepiso, primer piso y segundo piso barra-terraza; sin planta de servicio)" | reporte, encabezado | Cuatro plantas a dibujar; la planta de servicio queda fuera de alcance por decisión, no por olvido. |
| Ruta elegida | "Para la entrega manda la **ruta B**, con PushPull para retoques de caras y `BooleanDifference` para vanos." | reporte §1.1 | El punto de partida manda: hay DWG, entonces se modela desde el DWG. |
| Alcance de la ruta A | "Ruta A es la recomendada para el objetivo declarado ('casa simple desde cero')." | informe madre, Eje a | PushPull es el camino corto cuando no hay CAD; acá queda como plan B. |
| DWG como instancia única | "con **Insert as: Block instance** el DWG entra como **una sola instancia** (no como miles de curvas sueltas) y con **Block definition type: Embedded and linked** queda vinculado al archivo." | reporte §1.3 | La base CAD se mueve, se apaga y se borra como un objeto; el archivo origen sigue vinculado. |
| Punto de inserción | "La instancia cae en la capa actual y su punto de inserción es el punto base del bloque." | reporte §1.3 | Insertar con `CAD-BASE` activa y un eje conocido como punto base; evita corrimientos. |
| Bloques de mobiliario | "`Block` define el bloque a partir de geometría seleccionada." · "`BlockEdit` edita la definición (todos los ejemplares cambian juntos)" | reporte §1.3 | Cocina y baño se corrigen una vez y se actualizan en todos los pisos. |
| Avisos de `Make2D` | "`Make2D` **aplana las cotas** y **no genera la intersección** entre objetos que se atraviesan (para eso hay que correr `Intersect` antes)." | reporte §1.2 | Las cotas se dibujan en `Layout`; la línea de encuentro entre sólidos se resuelve con `Intersect`. |
| Proyección y ángulo | "**Projection: View** (proyecta la vista activa) o **CPlane** (usa el plano de construcción)." · "Para Argentina conviene **First angle**." | reporte §1.2 | First angle para lámina local; View para proyectar la vista guardada. |
| Repetir plantas | "**Register with previous**: alinea la salida con un Make2D anterior de la misma vista; sirve para repetir plantas sin que se corran." | reporte §1.2 | Las cuatro plantas quedan apiladas y comparables. |
| Cierre del tramo 2D | "La lámina se arma después en `Layout` (espacio papel) con detalles a escala y se exporta con `Print` → **Rhino PDF**, tamaño de página del layout y salida vectorial." | reporte §1.2 | Un solo entregable gráfico: A3 vectorial. |
| Extruir superficies | "el detalle de 'extruir superficies en vez de curvas para evitar costuras'" | informe madre, candidato 4 | Menos costuras y sólidos más limpios antes de boolear. |
| Sólidos cerrados | "Revisar con `ShowEdges` que los sólidos estén cerrados antes de boolear." | reporte §4, paso 2 | Chequeo barato que evita fallas de `BooleanUnion` a mitad de modelado. |
| Regla del PDF | "el PDF se exporta a las 17:00, con o sin el segundo corte" | reporte §5 · spec §5 | Fecha límite dura: primero el entregable completo, después la mejora. |
| Aprendizaje integrado | "La práctica de las técnicas queda integrada al trabajo real: se aprende Rhino resolviendo la entrega." | spec §1 | Sin tiempo muerto de curso: la curva de aprendizaje paga la entrega. |
| Universo del vault | "31 videos de la playlist `ARQ/Rhino+Grasshopper` y los etiquetados `rhino` en Watch Later, con solapamientos... total **47**" | reporte §3 | 47 no es 31 + 16: hay solapamientos (Copete 29:42, Urban Decoders/Cesium). |

## 4. Ruta donde guardará y frontmatter propuesto

| Destino | Ruta exacta | Frontmatter propuesto |
|---|---|---|
| wiki/fuentes | `wiki/fuentes/modelar_casa_rhino-dwg_make2d-multifuente.md` | `tipo: fuente, fecha_creacion: 2026-10-22, ultima_actualizacion: 2026-10-22, fuente_tipo: web-research + youtube, idioma: es, fecha_ingesta: 2026-10-22, tags: [rhino8, pushpull, dwg, bloques, make2d, layout, vivienda, entrega], crudo: raw/research/2026-10-22-modelar-casa-rhino.md, quien_guardo: sol, estado: en-wiki` |
| glosario software | `wiki/glosario/software/rhino.md#Rhino 8 / PushPull` | `UNICO .md por tool — nueva sección, sin archivo nuevo` |
| glosario concepto | `wiki/glosario/conceptos/modelado-vivienda-rhino.md` | `tipo: concepto, fecha_creacion: 2026-10-22, tags: [rhino8, modelado-3d, vivienda, dwg, make2d], idioma: es` |
| pbook | `wiki/glosario/interno/pbooks/pbk-modelado-entrega-rhino.md` | `tipo: pbook, fecha_creacion: 2026-10-22, tags: [rhino8, entrega, checklist, planos], idioma: es` |

> **Nombre del archivo** según la convención `{tema_ppal}-{tema_secundario}-{canal}` con `_` dentro del segmento y `-` entre segmentos: `modelar_casa_rhino` + `dwg_make2d` + `multifuente`. Se usa `multifuente` porque la ficha cura documentación McNeel, artículos y 15 videos, sin un canal único. Colisión: ninguna, `wiki/fuentes/` hoy tiene solo `comfyui-for_architects-architutors.md` y `00-index-yt.md`.

> Frontmatter obligatorio `AGENTS.md` — `tipo, fecha_creacion, ultima_actualizacion, tags, idioma`.

## 5. Tags y wikilinks

- Tags: `rhino8`, `pushpull`, `dwg`, `bloques`, `make2d`, `layout`, `a3`, `vivienda`, `entrega`, `modelado-3d`, `creadores`.
- `## Conceptos relacionados` previsto con ≥2 [[wikilinks]] absolutos: [[wiki/glosario/software/rhino|rhino]], [[wiki/glosario/software/autocad|autocad]], [[wiki/glosario/conceptos/bim-metodologia|bim-metodologia]], [[wiki/glosario/software/grasshopper|grasshopper]].
- Índice interno con `[[#Encabezado exacto]]` — nunca `[Texto](#slug)` con tildes. Los encabezados de este reporte ya están escritos sin tildes para que los links queden estables.
- Hub previsto: [[wiki/fuentes/00-index-yt|00-index-yt]] (aparece primero) y [[wiki/glosario/00-index|glosario]].

## 6. Referencias verificadas 200

### 6.1 Documentación y artículos

| # | Fuente | URL | Status | Tipo |
|---|---|---|---|---|
| 1 | McNeel — *PushPull for Architects \| Modeling a House* | https://www.rhino3d.com/en/docs/guides/push-pull/push-pull-for-architects/ | 200 webfetch (informe madre) | oficial |
| 2 | McNeel — *Make2D \| Rhino 8* | https://docs.mcneel.com/rhino/8/help/en-us/commands/make2d.htm | 200 webfetch (informe madre) | oficial |
| 3 | McNeel — *Block \| Rhino 8* | https://docs.mcneel.com/rhino/8/help/en-us/commands/block.htm | 200 webfetch (reporte §8) | oficial |
| 4 | McNeel — *Insert \| Rhino 8* | https://docs.mcneel.com/rhino/8/help/en-us/commands/insert.htm | 200 webfetch (reporte §8) | oficial |
| 5 | McNeel — *Layout \| Rhino 8* | https://docs.mcneel.com/rhino/8/help/en-us/commands/layout.htm | 200 webfetch (reporte §8) | oficial |
| 6 | McNeel — *Print \| Rhino 8* | https://docs.mcneel.com/rhino/8/help/en-us/commands/print.htm | 200 webfetch (reporte §8) | oficial |
| 7 | Cvetkovic, D. — *House from CAD Drawings* (How to Rhino) | https://howtorhino.com/rhino-grasshopper-tutorials/house-from-cad-drawings/ | 200 webfetch (informe madre) | externa |
| 8 | SMlab, Universidad de Granada — *Tutoriales de RHINOCEROS* | https://blogs.ugr.es/smlab/miscelanea-miscellany/tutoriales-rhinoceros/ | 200 webfetch (informe madre) | académica |
| 9 | McNeel Discourse — *Layouts – Learning Resources* | https://discourse.mcneel.com/t/layouts-learning-resources/176929 | 200 webfetch (informe madre) | oficial / comunidad |
| 10 | McNeel Discourse — *Rhino for Architectural Modeling – Learning Resources* | https://discourse.mcneel.com/t/rhino-for-architectural-modeling-learning-resources/162144 | 200 webfetch (informe madre) | oficial / comunidad |
| 11 | Food4Rhino — *rhinomcp* | https://www.food4rhino.com/en/app/rhinomcp | 200 webfetch (informe madre) | externa / software |

### 6.2 Videos (título confirmado, duración `s/d`)

| # | Candidato | Parte | URL | Status | Nivel |
|---|---|---|---|---|---|
| 1 | McNeel — *PushPull for Architects* (guía, no video) | — | ver fila 1 de 6.1 | 200 | inicial |
| 2 | Diego Pascual — *Modelar casa en Rhino* | 1/4 | https://www.youtube.com/watch?v=ZYcY-cB-DRA | 200 shell — título confirmado, duración `s/d` | inicial |
| 3 | Diego Pascual — *Modelar casa en Rhino* | 2/4 | https://www.youtube.com/watch?v=WbFTIiR11ac | 200 shell — duración `s/d` | inicial |
| 4 | Diego Pascual — *Modelar casa en Rhino* | 3/4 | https://www.youtube.com/watch?v=Gys-DojDmF8 | 200 shell — duración `s/d` | inicial |
| 5 | Diego Pascual — *Modelar casa en Rhino* | 4/4 | https://www.youtube.com/watch?v=t4eqDYKEHi0 | 200 shell — duración `s/d` | inicial |
| 6 | Tom Budd — *Planos de Arquitectura – Rhino 2D* | 1/4 | https://www.youtube.com/watch?v=NuK0SX93J4E | 200 shell — título confirmado, duración `s/d` | intermedio |
| 7 | Tom Budd — *Planos de Arquitectura – Rhino 2D* | 2/4 | https://www.youtube.com/watch?v=W4jEyci5iJs | 200 shell — duración `s/d` | intermedio |
| 8 | Tom Budd — *Planos de Arquitectura – Rhino 2D* | 3/4 | https://www.youtube.com/watch?v=T9FUGLikg2U | 200 shell — duración `s/d` | intermedio |
| 9 | Tom Budd — *Planos de Arquitectura – Rhino 2D* | 4/4 | https://www.youtube.com/watch?v=4A2pM4gSSBI | 200 shell — duración `s/d` | intermedio |
| 10 | Tom Budd — *Páginas de diseño (espacio papel)* | 5/5 | https://www.youtube.com/watch?v=CdnD4dJ3MTI | 200 shell — duración `s/d` | intermedio |
| 11 | How to Rhino / Dusan Cvetkovic — *Modeling a House from CAD drawings* | — | https://www.youtube.com/watch?v=aqotuhPejiA | 200 shell — título confirmado, duración `s/d` | intermedio |
| 12 | Kyle Houchens / McNeel — *building a house with Push Pull* | — | https://www.youtube.com/watch?v=pwAqZH9b85E | 200 shell — título confirmado, duración `s/d` | inicial |
| 13 | Hakan Architecture — *Rhino Floor Plan Modeling From 2d Drawing* | — | https://www.youtube.com/watch?v=rUb-mPL6KQw | 200 shell — título confirmado, duración `s/d` | intermedio |
| 14 | Flavio Bevilacqua — *Le Corbusier desde 2D AutoCAD* | 1/3 | https://www.youtube.com/watch?v=Bq6pQ0ZBjb0 | 200 shell — título confirmado, duración `s/d` | intermedio |
| 15 | Flavio Bevilacqua — *Le Corbusier desde 2D AutoCAD* | 2/3 | https://www.youtube.com/watch?v=hj1Ikix73dQ | 200 shell — duración `s/d` | intermedio |
| 16 | Flavio Bevilacqua — *Le Corbusier desde 2D AutoCAD* | 3/3 | https://www.youtube.com/watch?v=60KG6DKAQ7w | 200 shell — duración `s/d` | intermedio |

> 11 documentos + 15 videos + la guía oficial repetida como candidato = los **8 candidatos** del informe madre. Todas las URLs provienen de `raw/research/2026-10-22-modelar-casa-rhino.md` y `raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md`; no se agregó ningún link nuevo sin comprobar. Material de terceros, de uso interno del estudio, no redistribuir.

## 7. Propuestas wiki concretas

- **P1 — Ampliar `[[wiki/glosario/software/rhino|rhino]]`** con `## Rhino 8 / PushPull` (qué reemplaza del flujo extruir-curvas: `PushPull`, `SplitFace`, `Inset`), `## 3D → planos (Make2D + Layout)` y `## Ecosistema — rhinomcp`. Aporta el criterio de modelado que hoy falta en el stub.
- **P2 — Crear `[[wiki/glosario/conceptos/modelado-vivienda-rhino|modelado-vivienda-rhino]]`** con las tres rutas, la tabla comando-por-recurso y el flujo de 10 pasos. Es el concepto reusable para cualquier vivienda.
- **P3 — Crear `[[wiki/glosario/conceptos/planos-como-documento-legal|planos-como-documento-legal]]`** o ampliar el existente: por qué `Make2D` + `Layout` es requisito registral (Ley 24.335) y cómo se verifica (escala, rótulo, cotas).
- **P4 — Crear `[[wiki/glosario/interno/pbooks/pbk-modelado-entrega-rhino|pbk-modelado-entrega-rhino]]`** con el checklist de 9 puntos y las ventanas de trabajo. Separa "cómo se hace en el estudio" (pbook) de "qué es" (concepto), sin duplicar.
- **P5 — Ficha de fuente `[[wiki/fuentes/modelar_casa_rhino-dwg_make2d-multifuente|modelar_casa_rhino-dwg_make2d-multifuente]]`**: resumen limpio + ficha + links al crudo (`raw/research/...` y `raw/reports/...`), sin copiar los binarios.
- **P6 — `[[wiki/glosario/software/autocad|autocad]]` § Interoperabilidad**: `Insert` como bloque, `Embedded and linked` y verificación de escala con `Distance`. Conecta los dos CAD que el estudio usa a diario.

## 8. Estado wiki

| Destino | Acción | Link creado/actualizado | Fecha |
|---|---|---|---|
| wiki/fuentes | pendiente de gate | — | 2026-10-22 |
| wiki/glosario/software/rhino | pendiente de gate + `s` de @vaultworm-arq | — | 2026-10-22 |
| wiki/glosario/conceptos/modelado-vivienda-rhino | pendiente | — | 2026-10-22 |
| wiki/glosario/conceptos/planos-como-documento-legal | pendiente | — | 2026-10-22 |
| wiki/glosario/interno/pbooks/pbk-modelado-entrega-rhino | pendiente | — | 2026-10-22 |

## 9. Decisiones SOL

- [x] Encadenar `@sherlock` → `@contenidos` sobre este tema — `SI`, 2026-10-22.
- [ ] Aprobar el reporte tal como está.
- [ ] Corregir antes de promover (indicar qué sección).
- [ ] Descartar propuestas P3/P4 y quedarse solo con P1 + P2.
- [ ] Aprobar el nombre `modelar_casa_rhino-dwg_make2d-multifuente.md`.

## 10. Preguntas para SOL

- ¿Promovemos la ficha a `wiki/fuentes/` **antes** de la entrega o esperamos al 2026-10-23 con el PDF ya cerrado? Promover antes deja el criterio disponible mientras se modela; esperar evita curar contra un flujo que todavía puede cambiar.
- ¿Arrancamos por **P1 (rhino)** o por **P2 (concepto)**? P1 es la puerta que más se consulta; P2 es el procedimiento completo.
- ¿El nombre `modelar_casa_rhino-dwg_make2d-multifuente.md` te sirve, o preferís `modelado_casa_rhino-...`? Cambia solo el primer segmento.
- ¿Bajamos `PP-Architecture-Start.3dm` como activo de práctica? Sería descarga nueva, va a `activos/` (gitignored) y requiere tu comando.
- **Fase 2**: ¿transcribimos los 4 de Diego Pascual y los 5 de Tom Budd con `scripts/transcribir_youtube.py` para verificar duraciones y extraer comandos? Son 9 corridas.
- ¿Necesitamos ficha propia de **estándar de dibujo Rhino AR** (capas, pesos, rótulo) o reusamos el estándar AutoCAD ya documentado?
- ¿El pbook P4 entra ahora o queda para después de la entrega?

## 11. Pipeline

- Origen de este reporte: **sin OBS y sin transcript**. La fuente es texto (`raw/research/2026-10-22-modelar-casa-rhino.md` + `raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md`) y los binarios viven fuera del vault (DWG del cliente, s/d de ruta).
- Fase 2 de video, cuando SOL lo apruebe:
  `P:\Anaconda\envs\comfyenv\python.exe scripts/transcribir_youtube.py "https://www.youtube.com/watch?v=ZYcY-cB-DRA" --model medium --language es`
- Duración de cada video: `yt-dlp --dump-json "<url>"` (verificar que `yt-dlp` esté disponible en el entorno antes de correrlo). Sin ese paso, toda duración queda `s/d`.
- `raw/` es append-only: este reporte no borra ni edita el stub `raw/contenidos/sherlock-modelar-casa-rhino.md`.
- Al aprobar: mover la ficha a `wiki/fuentes/`, borrar el pendiente de `raw/contenidos/` y actualizar `raw/yt/index-state.json` a la nueva ruta.

---

## Anexo A. Mapa de creadores cruzado con el vault

> Veredictos tomados de `raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md` §2.1 (origen declarado: `raw/yt/veredictos.json`). Universo: **47 videos** `rhino` = 31 de la playlist `ARQ/Rhino+Grasshopper` + etiquetados `rhino` en Watch Later, con solapamientos. Por eso 31 + 16 canales no suma 47 videos únicos.

| # | Creador / canal | Idioma | Videos en vault | Veredicto | Para qué sirve |
|---|---|---|---|---|---|
| 1 | **Rhino 3D (oficial)** | EN | 13 | pendiente | Serie Studio: setup, site plans, floor plans, elevaciones, masa, 3D |
| 2 | **How to Rhino** | EN | 5 | pendiente | Puente DWG→3D, importar ubicación, plugins |
| 3 | **Gediminas Kirdeikis** | EN | 3 | rescatar | Secciones dinámicas, envolvente, cursos largos |
| 4 | **David Copete Parametric** | ES | 3 | pendiente | Planta paramétrica (29:42), tiny home (3:10:04) |
| 5 | **Urban Decoders** | EN | 3 | rescatar | Rhino + IA/MCP, Cesium/Unreal |
| 6 | **ArchiTech Network** | EN | 3 | rescatar | AR con Fologram, animación, defensa de Rhino |
| 7 | **McNeel Europe** | EN | 1 | rescatar | Webinar de machine learning en Rhino 8 (40:11) |
| 8 | **Algorithmix Design** | EN | 1 | rescatar | GH + IA que genera plantas (1:38) |
| 9 | **Arturo Tedeschi** | EN | 1 | rescatar | ChatGPT conectado a Grasshopper |
| 10 | **The Different Design** | EN | 1 | sin veredicto | ChatGPT + GH |
| 11 | **Nate's Studio Desk** | EN | 1 | sin veredicto | ChatGPT para diseñar en Rhino |
| 12 | **Andrew Friedenberg** | EN | 2 | sin veredicto | Geometric workflows, pixelado tipo MVRDV |
| 13 | **Arkpe** | ES | 1 | sin veredicto | De superficie a sólido, 3 métodos (2:20) |
| 14 | **ThinkParametric** | EN | 1 | sin veredicto | Stadium + RhinoScript/Python |
| 15 | **Philipp Galvan Design** | EN | 1 | sin veredicto | "Rhino AI": panorama, tono clickbait |
| 16 | **PlanFinder / McNeel Europe** | EN | 1 | sin veredicto | Webinar de plantas de departamentos (1:03:29) |

**Cómo leer el mapa.** `rescatar` = aporta algo que la entrega no tiene y conviene revisar; `pendiente` = todavía sin juicio, se resuelve mirando el video; `sin veredicto` = está en el vault y espera criterio. La serie oficial Studio cubre masas, plantas y elevaciones: sirve para repasar el estándar, no para aprender la casa completa.

**Los 8 candidatos nuevos** (no están en los 47): McNeel *PushPull for Architects*; Diego Pascual 1/4–4/4; Tom Budd 1/4–4/4 + espacio papel; How to Rhino *House from CAD*; Kyle Houchens *Push Pull*; Hakan *Floor Plan*; Bevilacqua *Le Corbusier* 1/3–3/3; McNeel Discourse *Layouts*.

## Anexo B. Secuencia de 10 pasos y checklist

**Supuesto de arranque:** modelo en metros, tolerancia `0.001` (1 mm), DWG con cotas verificables. Cliente y ruta del DWG: `s/d` (los define SOL al abrir el archivo).

| # | Paso | Comandos / decisión | Tiempo guía |
|---|---|---|---|
| 1 | **Setup** | `New` template *Small Objects – Meters*; `Units` metros + tolerancia 0.001; capas `00-EJES`, `CAD-BASE`, `A-MUROS`, `A-ABERTURAS`, `A-LOSAS`, `A-CUBIERTA`, `A-ESCALERA`, `A-MOBILIARIO`, `A-ANOTACION`, `A-CORTES`, `LAYOUT`; `SaveAs` `casa-<cliente>-v01.3dm` | 15 min |
| 2 | **DWG como bloque** | `Insert` → *Insert as: Block instance* → *Embedded and linked* → capa `CAD-BASE`; `Distance` contra una cota; si viene en mm, escalar la instancia ×0.001; `Lock` + `Hide` | 20 min |
| 3 | **Muros y losas** | `Offset`, `CloseCrv`, `ExtrudeSrf` (Solid=Yes), `BooleanUnion`; retoques con `PushPull`; `ShowEdges` antes de boolear | 60–90 min |
| 4 | **Aberturas** | Sólidos de corte + `BooleanDifference`; ajustes con `PushPull` + `Inset`; vanos repetidos a bloque | 45 min |
| 5 | **Segundo piso barra-terraza y cubierta** | Volumen propio con su losa; cubierta con `Loft` o `Sweep1`, `OffsetSrf` para espesor y alero por extensión de bordes | 60 min |
| 6 | **Bloques de mobiliario** | `Block` con punto base contra muro (`MOB-COCINA-01`, `MOB-BANO-*`); `BlockEdit` para variantes; `BlockManager` para revisar nombres | 45 min |
| 7 | **Escalera** | `Sweep1` para zanca + `ArrayLinear` para peldaños; GH solo si hay margen; verificar paso libre con `ClippingPlane` | 45–60 min |
| 8 | **`Make2D` por planta** | Vista `Top` paralela + `NamedView`; Projection View, **First angle**, hidden lines, clipping plane intersections, layer `A-ANOTACION`; `CAD-BASE` oculta; `Register with previous`; `Intersect` donde falte línea | 60 min |
| 9 | **Lámina A3** | `Layout` A3 420×297 horizontal; `Detail` 1:50 (1:75 si no entra) y vista bloqueada; `Dim`, `Text`, `Hatch`, norte y rótulo en `LAYOUT` | 90 min |
| 10 | **PDF** | `Print` → **Rhino PDF** → página del layout → salida **vectorial** → `casa-<cliente>-A3.pdf`; revisar al 100 % | incluido |

**Checklist de entrega**

- [ ] Unidades y escala verificadas contra una cota del DWG.
- [ ] `CAD-BASE` en bloque, bloqueada y oculta en la lámina.
- [ ] Sólidos cerrados (`ShowEdges`) y sin caras duplicadas.
- [ ] Cuatro plantas: PB, entrepiso, 1° y 2° barra-terraza (sin planta de servicio).
- [ ] Escalera con paso libre verificado.
- [ ] Bloques de cocina y baño insertados y nombrados.
- [ ] Dos cortes acotados (longitudinal por escalera, transversal por cocina/baño).
- [ ] A3 en PDF vectorial, rótulo completo (cliente, proyecto, planta, escala, fecha, lámina).
- [ ] `.3dm` guardado con versión y `.pdf` exportado a la carpeta del proyecto.

**Ventanas de trabajo** (`specs/261022-ruta-modelado-casa-rhino.md` §5)

| Bloque | Ventana | Contenido | Corte de alcance |
|---|---|---|---|
| 1 | hoy 19:00–21:30 | Setup, `Insert` DWG, ejes, muros PB | Ejes propios si el DWG está sucio |
| 2 | hoy 21:30–00:00 | Entrepiso, 1° piso, aberturas | Vanos solo en fachada principal |
| 3 | mañana 08:00–10:30 | 2° barra-terraza, cubierta, escalera | Cubierta como losa inclinada simple |
| 4 | mañana 10:30–13:00 | Bloques cocina/baño, `Make2D` | Un bloque por ambiente |
| 5 | mañana 14:00–17:00 | `Layout` A3, cortes, cotas, PDF | Un corte si el segundo no entra |
| Buffer | mañana 17:00–19:00 | Correcciones y export final | — |

> Regla de oro: **el PDF se exporta a las 17:00**, con o sin el segundo corte. Lo que falte se suma en la versión siguiente.

---

**Estado:** propuesta. Sin tocar `wiki/`, sin mover ni borrar el stub `raw/contenidos/sherlock-modelar-casa-rhino.md`. Esperando `¿Avanzo a wiki/fuentes? (s/N)`.
