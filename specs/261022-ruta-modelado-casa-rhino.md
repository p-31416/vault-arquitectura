---
tipo: plan
proyecto: Modelado vivienda Rhino 8
cliente: Estudio (línea propia)
fecha_creacion: 2026-10-22
ultima_actualizacion: 2026-10-22
estado: activo
tags: [rhino8, pushpull, dwg, bloques, make2d, layout, entrega, vivienda, creadores]
idioma: es
---

# Ruta — Modelado de casa en Rhino 8 y entrega A3

> Reunión de entrega: **mañana 2026-10-23, 09:00**. Caso: casa de tres niveles (planta baja, entrepiso, primer piso, segundo piso barra-terraza; sin planta de servicio) desde un plano 2D de AutoCAD LT.
> Restricción: **AutoCAD LT no modela en 3D**. LT se usa sólo para verificar, limpiar y exportar el 2D; todo el 3D se hace en Rhino.
> Documento de trabajo: [[raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores|reporte de flujo y creadores]] · Investigación: [[raw/research/2026-10-22-modelar-casa-rhino|informe madre]].

---

## 1. Objetivo

Llegar al PDF A3 con cuatro plantas, un corte (dos si entra) y el modelo `.3dm` guardado, usando la ruta **DWG → sólidos**, bloques para la base CAD y el mobiliario, `Make2D` + `Layout` para la lámina. La práctica de las técnicas queda integrada al trabajo real: se aprende Rhino resolviendo la entrega.

## 2. Alcance

**Dentro**

- Insertar el DWG como bloque en capa `CAD-BASE` (bloqueada y oculta al proyectar).
- Modelar PB, entrepiso, 1° piso y 2° piso barra-terraza, con muros, losas, aberturas, cubierta y escalera.
- Bloques de cocina y baño.
- Cuatro plantas 1:50, un corte (dos si entra), rótulo y PDF vectorial A3.
- Mapa de creadores y los 8 candidatos, como insumo de aprendizaje post-entrega.

**Fuera**

- Planta de servicio.
- Renders, recorridos y maqueta.
- Grasshopper completo: sólo escalera o piezas repetidas si el reloj lo permite.
- Curaduría wiki (va después, con su propio `s`).

## 3. Entregables

| # | Entregable | Formato | Criterio |
|---|---|---|---|
| 1 | Modelo 3D | `casa-<cliente>-v01.3dm` | Sólidos cerrados, capas nombradas |
| 2 | Lámina | `casa-<cliente>-A3.pdf` | A3 420×297, vectorial, cuatro plantas + 1 corte (2 si entra) |
| 3 | Base CAD | Bloque `CAD-BASE` | Vinculado al DWG, lock + hide |
| 4 | Biblioteca | Bloques `MOB-COCINA`, `MOB-BANO-*` | Punto base contra muro |
| 5 | Documento | `raw/reports/2026-10-22-rhino-flujo-entrega-y-creadores.md` | Publicado |
| 6 | Ruta | este archivo | Aprobada |

## 4. Ruta de trabajo (6 módulos, ~15.5 h)

| Módulo | Horas | Contenido | Entregable interno |
|---|---|---|---|
| 0. Setup | 0.5 | Unidades, tolerancia, capas, template | `.3dm` vacío con capas |
| 1. PushPull | 2 | Sólido base, caras, `SplitFace`, `Inset` | Volumen de prueba |
| 2. Casa ES (Diego Pascual) | 3 | Serie 1/4–4/4: extruir, booleanas, bloques, secciones | Casa de práctica 8×12 |
| 3. DWG → 3D | 2 | `Insert` como bloque, `Join`, `ExtrudeSrf`, `BooleanUnion` | Base CAD vinculada |
| 4. Cubierta y escalera | 2 | `Loft`/`Sweep1`, `ArrayLinear`, paso libre | Escalera y cubierta |
| 5. 3D → planos | 4 | `Make2D`, `Layout`, `Detail`, `Dim`, `Hatch`, PDF | A3 de práctica |
| 6. Cierre | 2 | Correcciones, rótulo, checklist, export | PDF final |

Los módulos 1–2 se cursan **antes** de tocar la entrega (hoy); 3–6 se ejecutan sobre el DWG real. Si el reloj aprieta, el módulo 2 se reduce a los capítulos de booleanas y bloques.

## 5. Plan de la entrega (dos jornadas)

| Bloque | Ventana | Contenido | Corte |
|---|---|---|---|
| A | hoy 18:30–21:30 | Setup, limpieza en LT, `Insert` DWG, escala, ejes, muros PB | Ejes propios si el DWG está sucio |
| B | hoy 21:30–00:00 | Entrepiso, 1° piso, aberturas | Vanos sólo en fachada principal |
| C | hoy 00:00–01:30 | 2° barra-terraza, cubierta, escalera simple | Cubierta como losa inclinada |
| D | hoy 01:30–03:00 | `Make2D` 4 plantas, `Layout` A3, 1 corte, **PDF v1** | Sin mobiliario si el reloj aprieta |
| E | mañana 06:30–08:30 | Correcciones, 2° corte si entra, re-export, backup | PDF cerrado a las 08:30 |

**Regla:** el PDF v1 se exporta **esta noche**. Mañana sólo se corrige y se re-exporta; a las 08:30 el archivo está cerrado y copiado a Drive/USB.

### 5.1 Restricción AutoCAD LT

- LT sirve para `AUDIT`, `PURGE`, `WBLOCK` del área del plano y verificación de unidades con `DIST`; no para extruir, boolear ni generar sólidos.
- Si el DWG tiene xrefs, pedir una copia con las xrefs bindeadas o hacer `WBLOCK` de la planta completa.
- Si las plantas vienen superpuestas en Z=0, separarlas por capa/nivel en Rhino (`SelLayer` + `Move` en Z).
- En Rhino, insertar el DWG como bloque (`CAD-BASE`), duplicar la instancia, explotar **sólo la copia** en `CAD-WORK` y trabajar sobre esas curvas. La base original queda intacta, bloqueada y oculta.

## 6. Secuencia técnica

1. **Setup** — metros, tolerancia 0.001, capas `00-EJES`, `CAD-BASE`, `A-MUROS`, `A-ABERTURAS`, `A-LOSAS`, `A-CUBIERTA`, `A-ESCALERA`, `A-MOBILIARIO`, `A-ANOTACION`, `A-CORTES`, `LAYOUT`.
2. **DWG** — `Insert` → *Insert as: Block instance* → *Embedded and linked* → capa `CAD-BASE` → verificar escala con `Distance` → `Lock` + `Hide`. Duplicar la instancia, `Explode` sólo la copia en `CAD-WORK`, `Join`/`CloseCrv` y usar esas curvas para offset y extrusión.
3. **Muros y losas** — `Offset`, `CloseCrv`, `ExtrudeSrf` (Solid=Yes), `BooleanUnion`; retoques con `PushPull`.
4. **Aberturas** — sólidos de corte + `BooleanDifference`; ajustes con `PushPull` + `Inset`.
5. **Cubierta y barra** — `Loft` o `Sweep1`, `OffsetSrf`, alero por extensión de bordes.
6. **Bloques** — `Block` con punto base contra muro, `BlockEdit`, `BlockManager`, `Copy` por ambiente.
7. **Escalera** — `Sweep1` para zanca + `ArrayLinear` para peldaños; GH sólo si hay margen.
8. **Make2D** — vista Top paralela, `First angle`, hidden lines, `Clipping plane intersections`, `Register with previous`; `CAD-BASE` oculta; `Intersect` donde falte línea.
9. **Lámina** — `Layout` A3 horizontal, `Detail` 1:50, `Dim`, `Text`, `Hatch`, rótulo.
10. **PDF** — `Print` → Rhino PDF → página del layout → vectorial.

## 7. Creadores y candidatos

**Seguir (4):** McNeel *PushPull for Architects* (EN), Diego Pascual *Modelar casa 1/4–4/4* (ES), Tom Budd *Planos de Arquitectura + espacio papel* (ES), SMlab UGR como índice.

**Ver (5):** Kyle Houchens *House with Push Pull* (EN), Hakan Architecture *Floor Plan from 2D* + escaleras (ES), Flavio Bevilacqua *Le Corbusier 1/3–3/3* (ES), Gediminas *Dynamic Sections* (EN), David Copete *Parametric Floor Plan* (ES).

**Referencia:** Ruben Borup (Azuma), McNeel Discourse (Layouts), `rhinomcp` (Food4Rhino), Andrew Friedenberg (geometric workflows), Arturo Tedeschi (GH + ChatGPT).

**Ya en el vault (16 canales):** Rhino 3D oficial (13 videos), How to Rhino (5), Gediminas (3), David Copete (3), Urban Decoders (3), ArchiTech Network (3), McNeel Europe (1), Algorithmix (1), Tedeschi (1), The Different Design (1), Nate's Studio Desk (1), Friedenberg (2), Arkpe (1), ThinkParametric (1), Philipp Galvan (1), PlanFinder/McNeel Europe (1).

## 8. Criterios de aceptación

- [ ] Cuatro plantas y **al menos un corte** (dos si el reloj lo permite).
- [ ] PDF cerrado y copiado antes de las 08:30.
- [ ] Escala 1:50 verificada contra una cota del DWG.
- [ ] `CAD-BASE` en bloque, oculta en la lámina.
- [ ] Sólidos cerrados (`ShowEdges`) y sin caras duplicadas.
- [ ] Escalera con paso libre verificado por corte.
- [ ] Bloques de cocina y baño insertados y nombrados.
- [ ] PDF vectorial A3 con rótulo completo.
- [ ] `.3dm` y `.pdf` en la carpeta del proyecto.

## 9. Riesgos

| Riesgo | Mitigación |
|---|---|
| AutoCAD LT sin 3D | LT sólo limpia y exporta 2D; extrusión, booleanas y cubierta en Rhino |
| Plantas superpuestas en Z=0 | Separar por capa/nivel con `SelLayer` + `Move` en Z |
| Xrefs sin bindear | `WBLOCK` del área o pedir copia con xrefs bindeadas |
| Unidades del DWG | `DIST` contra cota conocida en LT; escalar la instancia en Rhino |
| Make2D sucio | Ocultar `CAD-BASE`, proyectar por nivel y vista guardada |
| Bloques desincronizados | `BlockEdit`, nunca `Explode` + copiar |
| GH consume tiempo | GH sólo escalera |

## 10. Dependencias y próximos pasos

- **@contenidos** formatea el stub `raw/contenidos/sherlock-modelar-casa-rhino.md` con los 8 candidatos y el mapa de creadores, y prepara la página de `wiki/fuentes` para su gate HITL.
- **Fase 2** (post-entrega): transcribir Diego Pascual y Tom Budd con `scripts/transcribir_youtube.py` para verificar duraciones y extraer comandos.
- **@vaultworm-arq**: ampliar `wiki/glosario/software/rhino` (PushPull, 3D→planos, ecosistema) y crear `modelado-vivienda-rhino` y `planos-como-documento-legal`, con `s` propio.
- Verificar la guía oficial PushPull contra el DWG real y anotar diferencias de flujo.

---

**Estado:** activo. Aprobado por SOL el 2026-10-22 (`SI`).
