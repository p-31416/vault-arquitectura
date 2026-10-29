---
fecha: 2026-10-22
tema: Modelar una casa simple en Rhino 8 (flujo completo, 3D → planos)
slug: modelar-casa-rhino
idiomas: [es, en, it]
fuentes_n: 11
fuentes_citadas_n: 24
confianza: alta (oficial McNeel + índice académico UGR) · media en duraciones no verificadas
estado: crudo
investigador: sherlock
destino: raw/contenidos/sherlock-modelar-casa-rhino.md
wiki_probable: wiki/glosario/software/rhino.md + wiki/glosario/conceptos/modelado-vivienda-rhino.md
---

# Modelar una casa simple en Rhino 8

Fecha: 2026-10-22 · Zona: `-03:00 America/Argentina/Buenos_Aires`
Objetivo declarado: aprender/decidir el flujo mínimo para modelar una vivienda unifamiliar simple desde cero en Rhino 8 y llevarla a planos.

## Resumen

Rhino 8 cambia el flujo de modelado arquitectónico con **PushPull**: en lugar de extruir curvas una por una, se trabaja sobre sólidos cerrados y se empuja/corta caras. McNeel publicó una guía oficial específica — *PushPull for Architects | Modeling a House* — que modela una casa completa (muros con espesor, aberturas, cubierta, planta baja, puerta de entrada) sobre un archivo de partida `PP-Architecture-Start.3dm`. Ese es el camino más corto y el único respaldado por documentación oficial.

Para quien viene de AutoCAD, el eje alternativo es **DWG → curvas → superficies → sólidos** (importar plano 2D, unir curvas, `ExtrudeCrv`/`ExtrudeSrf`, `BooleanUnion` para cerrar juntas), que es el flujo que enseñan How to Rhino en inglés y Hakan Architecture / Diego Pascual en español.

El tercer tramo — **3D a planos** — se resuelve con `Make2D` + `Layout` (espacio papel). En el estudio esto es crítico y no opcional: los planos son documentos legales (Ley 24.335). Hay dos recursos en español dedicados exclusivamente a esto: Tom Budd (Planos de Arquitectura 1/4–4/4 + Páginas de diseño) y el thread oficial de Layouts, que apunta al *Level 1 Training Guide* de Rhino 8.

El índice de tutoriales en español más completo y curado que apareció es el de la **Universidad de Granada (SMlab)**: reúne ~20 autores con series completas de vivienda (Diego Pascual 4 partes, Hakan 2 partes, Flavio Bevilacqua 3 partes sobre Le Corbusier, Ruben Borup 4 partes sobre Azuma House). Es la mejor puerta de entrada en castellano y no está en el vault.

Vacíos claros: **cubierta inclinada** paso a paso y **escalera** en vivienda de una planta aparecen sólo como fragmentos; **geolocalización** (EarthAnchorPoint) y **import DWG con cotas** tienen videos sueltos sin serie; **italiano** no produjo material específico de vivienda (gap declarado).

## Ejes

### a) Tres rutas según punto de partida

| Ruta | Perfil | Secuencia | Respaldo |
|---|---|---|---|
| **A. PushPull (Rhino 8 nativo)** | Empieza de cero, sin DWG | sólido base → caras → `PushPull`/`SplitFace`/`Inset` → aberturas → cubierta | Oficial McNeel (`rhino3d.com/en/docs/guides/push-pull/push-pull-for-architects/`) + video Kyle Houchens |
| **B. DWG → sólidos** | Viene de AutoCAD, ya tiene plano | import DWG → `Join`/`CloseCrv` → `ExtrudeCrv`/`ExtrudeSrf` → `BooleanUnion` → detalles | How to Rhino (EN), Hakan + Diego Pascual (ES) |
| **C. Caso de estudio (aprender viendo)** | Quiere referencia formal | imagen/ráster o plano → modelar volumen → detalle | Ruben Borup (Azuma House 1/4–4/4), Flavio Bevilacqua (Le Corbusier 1/3–3/3), Instituto de Arquitectura (Maison Cook) |

Ruta A es la recomendada para el objetivo declarado ("casa simple desde cero"). Ruta B es la que sirve cuando el estudio ya tiene el DWG del cliente.

### b) Comandos por recurso (mapa de trabajo)

| Recurso | Comando(s) Rhino 8 | Dónde se explica |
|---|---|---|
| Muros con espesor | `PushPull` sobre cara, o `OffsetSrf` + `ExtrudeSrf`; `SplitFace` para dividir | Guía oficial PushPull; How to Rhino (extrusión de superficies evita costuras) |
| Losa / entrepiso | `ExtrudeCrv` con `Solid=Yes`, o `PlanarSrf` + `ExtrudeSrf` | docs `extrudecrv` (citado, no fetcheado) |
| Aberturas (vanos) | `PushPull` con `Inset`, o `BooleanDifference` con sólido de corte | Guía oficial; Diego Pascual "Operaciones booleanas" |
| Carpintería repetida | `Block` / `BlockEdit` / `BlockManager` | Diego Pascual "Bloques"; Master Bath Reno (usa blocks) |
| Cubierta | `Loft` / `Sweep` / `OffsetSrf` + `ExtrudeSrf`; overhang duplicando y extendiendo bordes | How to Rhino (roofs por offset de superficie de piso); SubD Roof (oficial) |
| Escalera | `Sweep1`/`Sweep2` para zanca, `ArrayLinear`, o modelado por peldaños | Hakan "Escaleras" (playlist); Daniel Flores "escalera helicoidal" |
| Terreno / contexto | `EarthAnchorPoint` + import de ubicación; `Drape` sobre malla | How to Rhino "Import ANY location"; Hakan "Plano de situación desde CAD" |
| Redondeo de aristas | `FilletEdge` / `ChamferEdge` | Diego Pascual "Empalmes y chaflanes" |
| Alinear / mover preciso | `SetPt`, `Move`, `Copy`, `Rotate`, `Oriented` | Diego Pascual "Mover, copiar, simetría" |
| Planos 2D | `Make2D` (View/CPlane, Third angle, Register with previous) | docs `make2d` (fetcheado 200) |
| Láminas / escala / rótulo | `Layout`, `Detail`, `Dim`, `Hatch`, line weights | Tom Budd "Planos de Arquitectura 1/4–4/4" + "Páginas de diseño (espacio papel)"; thread oficial Layouts |
| Cortes | `ClippingPlane`, `Section` | Diego Pascual "Secciones virtuales"; Gediminas "Dynamic Sections" |

### c) Vacíos detectados (declarados, no inventados)

- **Cubierta inclinada paso a paso**: aparece como "there are many techniques" en How to Rhino, sin secuencia cerrada. Candidato: `SubD Roof` de la lista oficial.
- **Escalera en vivienda de una planta**: sólo playlists genéricas de escaleras (Hakan), sin serie específica de casa.
- **Geolocalización para Argentina**: los videos usan el importador de ubicación de Rhino; no se encontró material que trate datum/coordenadas locales argentinas (Gauss-Krüger POSGAR 2007).
- **Import DWG con cotas y capas**: tratado de pasada; ningún recurso verificado cubre mapeo de capas CAD → capas Rhino con estándar de oficina.
- **Italiano**: sin material específico de vivienda. Gap explícito (`datos insuficientes IT`); los resultados fueron genéricos o de producto.
- **RhinoMCP**: existe y es gratis (Apache 2.0, 7.836 descargas), permite crear/modificar objetos, inspeccionar documento, ejecutar scripts y manejar capas por socket. No hay tutorial verificado que lo aplique a modelar una vivienda.

## Candidatos

Ordenados por utilidad para el objetivo (casa simple → planos). `[NUEVO]` = no está en los 47 videos `rhino` del Takeout.

1. **PushPull for Architects | Modeling a House** — McNeel (oficial, texto + archivo `.3dm`) — s/d — https://www.rhino3d.com/en/docs/guides/push-pull/push-pull-for-architects/ — **inicial** — única guía oficial que modela una casa completa en Rhino 8; trae archivo de partida — `[NUEVO]`
2. **Modelar casa en Rhino (1/4 → 4/4)** — Diego Pascual (ES) — 4 partes, duración no verificada — https://www.youtube.com/watch?v=ZYcY-cB-DRA · `WbFTIiR11ac` · `Gys-DojDmF8` · `t4eqDYKEHi0` — **inicial** — la única serie en castellano que modela una casa de punta a punta con comandos nombrados en español — `[NUEVO]`
3. **Planos de Arquitectura – Rhino 2D (1/4 → 4/4) + Páginas de diseño (espacio-papel)** — Tom Budd (ES) — 5 videos — https://www.youtube.com/watch?v=NuK0SX93J4E (`W4jEyci5iJs`, `T9FUGLikg2U`, `4A2pM4gSSBI`, `CdnD4dJ3MTI`) — **intermedio** — cubre exactamente el tramo legal del estudio: de modelo a lámina con peso de línea y espacio papel — `[NUEVO]`
4. **Rhino Architecture – Modeling a House from CAD drawings** — How to Rhino / Dusan Cvetkovic (EN) — video + artículo — https://www.youtube.com/watch?v=aqotuhPejiA · https://howtorhino.com/rhino-grasshopper-tutorials/house-from-cad-drawings/ — **intermedio** — el puente DWG→3D con el detalle de "extruir superficies en vez de curvas para evitar costuras" — `[NUEVO]`
5. **Rhino 8 – building a house with Push Pull (new!)** — Kyle Houchens / McNeel (EN) — s/d — https://www.youtube.com/watch?v=pwAqZH9b85E — **inicial** — demostración en vivo del flujo PushPull sobre una casa; complementa la guía escrita — `[NUEVO]`
6. **Rhino Floor Plan Modeling From 2d Drawing** — Hakan Architecture (ES) — https://www.youtube.com/watch?v=rUb-mPL6KQw — **intermedio** — caso de vivienda: primero planimetría 2D (`rMhDc8AOEZc`), después 3D; secuencia didáctica completa — `[NUEVO]`
7. **Modelización de vivienda (Le Corbusier) partiendo de su 2D en AutoCAD (1/3 → 3/3)** — Flavio Bevilacqua (ES) — 3 partes — https://www.youtube.com/watch?v=Bq6pQ0ZBjb0 · `hj1Ikix73dQ` · `60KG6DKAQ7w` — **intermedio** — referencia formal clásica con el flujo CAD→Rhino ya resuelto — `[NUEVO]`
8. **Layouts – learning resources** — McNeel Discourse (EN) — hilo curado — https://discourse.mcneel.com/t/layouts-learning-resources/176929 — **avanzado** — apunta al *Level 1 Training Guide* oficial y a un tutorial de layouts de Agata Kycia — `[NUEVO]`

### Contexto ya cubierto por el vault (no re-bajar)

Los 47 videos `rhino` del Takeout ya tienen la **oficial Rhino Studio Series** completa: `How to Get Started with Rhino` (9:06, `RFPG6BmpyFs`), `Top 10 Setup Tricks` (5:34, `qUhbXIF1DDw`), `Drafting Site Plans & Context | S1 E2` (13:32, `PlWRlBdxKcA`), `Drafting Floor Plans | S1 E3` (17:40, `gf1rkK-Uq1A`), `How to Think in 3D | S2 E1` (17:57, `sozaV2SFWDI`), `3D Massing Iterations | S2 E3` (20:55, `Fu1JUMR_oLY`), `Beyond the 3D Box | S2 E4` (20:00, `3DigELY2Zus`), más los cortos de estándar de dibujo (`qsMZlvavM3k`, `ZQZPhtbp00s`, `jUFQQX7-cPw`). **Los candidatos 1-8 no los duplican**: ninguno de los 47 es una serie "casa completa" ni cubre espacio papel en español.

## Fuentes

Verificadas con `webfetch` (status 200):

1. Robert McNeel & Associates. (2026). *PushPull for Architects | Modeling a House*. Rhino 8 Documentation. https://www.rhino3d.com/en/docs/guides/push-pull/push-pull-for-architects/ — `idioma_original: en` [trad. propia — no oficial] — **200**
2. Robert McNeel & Associates. (2026). *Make2D | Rhino 8*. https://docs.mcneel.com/rhino/8/help/en-us/commands/make2d.htm — `idioma_original: en` [trad. propia — no oficial] — **200**
3. McNeel Discourse. (2025). *Rhino for Architectural Modeling – Learning Resources*. https://discourse.mcneel.com/t/rhino-for-architectural-modeling-learning-resources/162144 — `idioma_original: en` [trad. propia — no oficial] — **200**
4. McNeel Discourse. (2026). *Layouts – Learning Resources*. https://discourse.mcneel.com/t/layouts-learning-resources/176929 — `idioma_original: en` [trad. propia — no oficial] — **200**
5. Cvetkovic, D. (2023, 20 de octubre). *House from CAD Drawings: The Ultimate Rhino Modeling Tutorial*. How to Rhino. https://howtorhino.com/rhino-grasshopper-tutorials/house-from-cad-drawings/ — `idioma_original: en` [trad. propia — no oficial] — **200**
6. Cvetkovic, D. (2023). *Rhino Architecture – Modeling a House from CAD drawings* [Video]. YouTube. https://www.youtube.com/watch?v=aqotuhPejiA — `idioma_original: en` — **200** (título confirmado; duración no expuesta)
7. SMlab, Universidad de Granada. (s.f.). *Tutoriales de RHINOCEROS*. https://blogs.ugr.es/smlab/miscelanea-miscellany/tutoriales-rhinoceros/ — `idioma_original: es` — **200**
8. Houchens, K. (2025). *Rhino 8 – building a house with Push Pull (new!)* [Video]. YouTube. https://www.youtube.com/watch?v=pwAqZH9b85E — `idioma_original: en` — **200** (título confirmado; duración no expuesta)
9. Pascual, D. (s.f.). *Modelar casa en Rhino (1/4)* [Video]. YouTube. https://www.youtube.com/watch?v=ZYcY-cB-DRA — `idioma_original: es` — **200** (título confirmado)
10. Hakan Architecture. (s.f.). *Rhino Floor Plan Modeling From 2d Drawing* [Video]. YouTube. https://www.youtube.com/watch?v=rUb-mPL6KQw — `idioma_original: es` — **200** (título confirmado)
11. ccc159. (2025). *rhinomcp* [Software]. Food4Rhino. https://www.food4rhino.com/en/app/rhinomcp — `idioma_original: en` [trad. propia — no oficial] — **200**

Citadas sin fetch propio (aparecen en las anteriores; nivel 1 sin verificar status):

12. Robert McNeel & Associates. *ExtrudeCrv | Rhino 8*. https://docs.mcneel.com/rhino/8/help/en-us/commands/extrudecrv.htm
13. Robert McNeel & Associates. *Level 1 Training Guide – Printing and Layouts*. https://docs.mcneel.com/rhino/8/training-level1/en-us/
14. McNeel. *PushPull Townhouse* [Video]. https://vimeo.com/903927402
15. McNeel. *ADU Guest House Design* [Video]. https://vimeo.com/showcase/7805155/video/569544780
16. McNeel. *Master Bath Reno* [Video]. https://vimeo.com/showcase/10775985?video=1067888384
17. McNeel. *PushPull Vanity* [Video]. https://vimeo.com/925550624
18. McNeel. *Park Building* [Video]. https://vimeo.com/showcase/7805155/video/808444230
19. Budd, T. (s.f.). *Planos de Arquitectura – Rhino 2D (1/4)* [Video]. https://www.youtube.com/watch?v=NuK0SX93J4E
20. Bevilacqua, F. (s.f.). *Modelización de vivienda (Le Corbusier) 1/3* [Video]. https://www.youtube.com/watch?v=Bq6pQ0ZBjb0
21. Borup, R. (s.f.). *Modelado de Azuma House (Tadao Ando) 1/4* [Video]. https://www.youtube.com/watch?v=6LP19pKH3DE
22. Parra, D. (s.f.). *Rhinoceros – Introducción* [Lista de videos]. YouTube. https://www.youtube.com/@bydavidparra
23. VisualARQ. (s.f.). *Video tutorial – Villa Savoye*. https://www.visualarq.com/es/tutorial/video-tutorial/
24. De Costas, A. (s.f.). *Curso Rhino* [Lista de reproducción]. YouTube. https://www.youtube.com/playlist?list=PL_7UEOgbqi2SjLq1Q0oQ_RLkrNy12zFi1

## Metodología

### Queries ejecutadas

**EN**
- `Rhino 8 model a house tutorial step by step architecture`
- `Rhino 8 PushPull architecture house modeling official`
- `Rhino 8 commands ExtrudeCrv BooleanUnion Make2D layout architectural model`
- `How to Rhino model house from CAD drawings`
- `rhino architecture modeling house beginner tutorial youtube`

**ES**
- `tutorial Rhino 8 modelar casa paso a paso arquitectura`
- `Rhino modelar vivienda desde plano AutoCAD español`
- `Rhino 8 planos Make2D espacio papel tutorial español`
- `tutoriales Rhinoceros arquitectura índice universidad`

**IT**
- `tutorial Rhino 8 modellare una casa architettura`
- `Rhino modellazione casa da pianta italiano`

### URLs consultadas y status

| URL | Status | Uso |
|---|---|---|
| rhino3d.com/en/docs/guides/push-pull/push-pull-for-architects/ | 200 | fuente principal ruta A |
| docs.mcneel.com/rhino/8/help/en-us/commands/make2d.htm | 200 | Make2D |
| discourse.mcneel.com/t/rhino-for-architectural-modeling-learning-resources/162144 | 200 | índice oficial videos |
| discourse.mcneel.com/t/layouts-learning-resources/176929 | 200 | layouts |
| howtorhino.com/rhino-grasshopper-tutorials/house-from-cad-drawings/ | 200 | ruta B + artículo |
| blogs.ugr.es/smlab/miscelanea-miscellany/tutoriales-rhinoceros/ | 200 | índice ES (hallazgo clave) |
| food4rhino.com/en/app/rhinomcp | 200 | RhinoMCP |
| youtube.com/watch?v=pwAqZH9b85E | 200 (shell) | título confirmado |
| youtube.com/watch?v=aqotuhPejiA | 200 (shell) | título confirmado |
| youtube.com/watch?v=ZYcY-cB-DRA | 200 (shell) | título confirmado |
| youtube.com/watch?v=rUb-mPL6KQw | 200 (shell) | título confirmado |
| docs.mcneel.com/.../extrudecrv.htm | sin fetch | citado desde búsqueda |

### Duplicados contra el vault

`grep "| rhino"` sobre `raw/yt/videos-y-canales-guardados.md` → 47 videos. **Ninguno** de los 8 candidatos coincide: el vault tiene la Rhino Studio Series oficial (masa, site plans, floor plans, elevations, setup) y piezas de How to Rhino sobre ubicación/plugins/Grasshopper, pero **no** tiene ninguna serie "casa completa" ni espacio papel en español. Único solapamiento temático: Gediminas `Carve Building Envelope` (38:02) toca volumetría de edificio, no vivienda.

### Gaps

- Duraciones de videos nuevos: YouTube no expone metadata a `webfetch` (devuelve sólo el shell). Requiere `yt-dlp --dump-json` o transcripción en Fase 2.
- Italiano: `datos insuficientes IT` (búsquedas devolvieron resultados genéricos).
- Cubierta inclinada y escalera: sin serie dedicada verificada (ver Eje c).
- Ninguna fuente argentina: no se halló tutorial local con normativa/estándar de dibujo AR.

## Propuestas wiki

- Actualizar `[[wiki/glosario/software/rhino]]`: agregar sección **Rhino 8 / PushPull** (qué reemplaza del flujo extruir-curvas, comandos `PushPull`, `SplitFace`, `Inset`) y **3D→planos** (`Make2D` + `Layout`), con referencias 1 y 2. El stub actual no menciona PushPull.
- Crear `[[wiki/glosario/conceptos/modelado-vivienda-rhino]]`: flujo canónico de 7 pasos (unidades y capas → sólido base → muros → aberturas → cubierta → escalera → `Make2D` → `Layout`), con tabla de comandos y enlace a las 3 rutas (A/B/C). Conceptos relacionados: `[[wiki/glosario/software/rhino]]`, `[[wiki/glosario/conceptos/bim-metodologia]]`, `[[wiki/glosario/software/autocad]]`.
- Crear `[[wiki/glosario/conceptos/planos-como-documento-legal]]` (o ampliar el existente): el tramo `Make2D`+`Layout` como requisito registral, no como salida gráfica opcional — Ley 24.335.
- Registrar `rhinomcp` como ficha de software/herramienta en `[[wiki/glosario/software/rhino]]` §Ecosistema, con la salvedad de que no hay tutorial verificado de uso arquitectónico.
- Hub: `[[raw/research/2026-10-22-modelar-casa-rhino]]` → este informe; índice de video-tutoriales ES de la UGR como fuente de candidatos Nivel 2 (nunca Nivel 3 sin `s` por fuente).

---

**Estado:** crudo verificado. Sin formatear, sin template, sin tocar `wiki/`.
