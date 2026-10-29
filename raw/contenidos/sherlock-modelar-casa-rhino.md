---
tipo: raw
estado: pendiente-formato
fuente_binaria:
fecha_creacion: 2026-10-22
ultima_actualizacion: 2026-10-22
tags: [rhino8, modelado-3d, pushpull, vivienda, make2d, layouts, planos, arquitectura, tutoriales, rhinomcp]
idioma: es
canal: web-research + youtube
nivel: inicial-intermedio
timezone: America/Argentina/Buenos_Aires
---

# Stub — Modelar una casa simple en Rhino 8 — investigación 2026-10-22

> Objetivo: flujo mínimo y verificado para modelar una vivienda unifamiliar simple desde cero en Rhino 8 y llevarla a planos.
> Informe madre: [[raw/research/2026-10-22-modelar-casa-rhino|2026-10-22-modelar-casa-rhino]]
> Cache: `raw/research-cache/2026-10-22-modelar-casa-rhino.json`
> Sin binario propio: el material es web + video (Fase 2 de transcripción decide si baja algún `.3dm` de la guía oficial).

## Resumen (5 bullets, lenguaje en positivo)

- Rhino 8 consolida **PushPull** como flujo nativo: se modela sobre sólidos cerrados y se empujan o cortan caras, con guía oficial que arma una casa completa.
- La ruta **DWG → curvas → superficies → sólidos** sigue vigente para quien ya tiene el plano del cliente, y es la que cubren los tutoriales en español.
- El cierre del ciclo **3D → planos** se resuelve con `Make2D` + `Layout`, requisito registral en el estudio (Ley 24.335) y no una salida gráfica opcional.
- El índice de la **Universidad de Granada (SMlab)** reúne la mejor puerta de entrada en castellano: series completas de vivienda por autor.
- **RhinoMCP** (gratuito, Apache 2.0) abre la puerta a modelado asistido por agente sobre objetos, capas y scripts, con tutorial arquitectónico todavía pendiente.

## 0. Gate HITL

> `¿Avanzo a curaduría? (s/N)` — SOL marca: ✅ aprobar / ✏️ corregir / ❌ descartar / 💡 añadir.
> Sin `s` no hay `write` en `wiki/` (AGENTS.md HITL).

## 1. Diagnóstico de fuentes

- Oficial McNeel: 4 documentos verificados 200 (guía PushPull, `Make2D`, thread de modelado arquitectónico, thread de Layouts).
- Académico/curado: índice UGR SMlab (200) con ~20 autores y series completas de vivienda.
- Referencia de industria: How to Rhino, artículo + video (200) sobre DWG→3D.
- Video YouTube: 4 URLs con **título confirmado** por fetch, **duración no expuesta** (requiere `yt-dlp` en Fase 2).
- Software: Food4Rhino `rhinomcp` (200), 7.836 descargas, Apache 2.0.
- Gap declarado: italiano sin material específico de vivienda; sin fuente argentina con estándar de dibujo local.

## 2. Hallazgos crudos

- Ruta A (PushPull): sólido base → `PushPull` en caras → `SplitFace` para subdividir → `Inset` para retranquear antes de un vano → cubierta → planta baja → puerta. Archivo de partida `PP-Architecture-Start.3dm`.
- Ruta B (DWG): import por drag&drop → `Join` / `CloseCrv` → extraer superficies de hatches (explode → join → extrude) → `ExtrudeSrf` (superficies, no curvas sueltas: evita costuras) → `BooleanUnion` para cerrar juntas → `Block` para carpintería → `Sweep` para molduras → cubierta por offset y extensión de bordes.
- Ruta C (caso de estudio): Azuma House (Borup, 4 partes), Le Corbusier (Bevilacqua, 3 partes), Maison Cook (Instituto de Arquitectura), Villa Rotonda (How to Rhino).
- `Make2D`: opciones View/CPlane, Third angle / First angle projection, Register with previous — permite actualizar la proyección sin perder capas.
- `Layout`: el thread oficial deriva al *Level 1 Training Guide* (§ Printing and Layouts) y a un tutorial de layouts de Agata Kycia en el blog de Rhino.
- Español, planos: Tom Budd cubre pesos de línea, tramas, planos 1/4–4/4 y "Páginas de diseño (espacio-papel)" — el tramo completo modelo→lámina en castellano.
- Español, casa: Diego Pascual 4/4 con comandos nombrados en español (extruir, booleanas, empalmes, bloques, secciones virtuales); Hakan separa planimetría 2D (`rMhDc8AOEZc`) de modelización 3D (`rUb-mPL6KQw`).
- Geolocalización: How to Rhino tiene import de ubicación (corto `zCUZ1SP0vkc` + largo `YtlK4046VRQ`), ya en el vault; falta el paso a datum/coordenadas locales.
- RhinoMCP: comunicación bidireccional por socket, crear/modificar/borrar objetos, inspeccionar documento, ejecutar scripts Python de Rhino (experimental), seleccionar por filtros, gestionar capas.

## 3. Topics → glosario/software|conceptos

| # | Topic | Por qué | Destino |
|---|---|---|---|
| T1 | PushPull en Rhino 8 | Reemplaza el flujo extruir-curva por edición directa sobre sólido | [[wiki/glosario/software/rhino\|rhino]] § PushPull |
| T2 | `Make2D` + `Layout` | Tramo legal: de modelo a plano registrable | [[wiki/glosario/software/rhino\|rhino]] § 3D→planos |
| T3 | Flujo de 7 pasos de vivienda | Secuencia replicable para el equipo | concepto `modelado-vivienda-rhino` (nueva) |
| T4 | DWG→sólidos | Puente desde AutoCAD, insumo real del estudio | [[wiki/glosario/software/autocad\|autocad]] § interoperabilidad |
| T5 | Planos como documento legal | Justifica invertir en el tramo 2D | concepto `planos-como-documento-legal` (nueva) |
| T6 | RhinoMCP | Modelado asistido por agente | [[wiki/glosario/software/rhino\|rhino]] § ecosistema |
| T7 | Índice UGR de tutoriales ES | Fuente de candidatos Nivel 2 reusable | este stub § 11 |

## 4. Entidades

| # | Entidad | Tipo | Nota |
|---|---|---|---|
| E1 | Vivienda unifamiliar simple | tipología | Caso base del flujo |
| E2 | Sólido cerrado / polisuperficie | geometría | Unidad de trabajo de PushPull |
| E3 | Cara / borde / vértice SubD | subobjeto | Edición directa |
| E4 | `Make2D` | comando | Proyección 2D del modelo 3D |
| E5 | `Layout` / `Detail` | presentación | Lámina y ventana de detalle |
| E6 | Bloque | objeto | Carpintería reutilizable |
| E7 | `EarthAnchorPoint` | referencia | Geolocalización del sitio |
| E8 | RhinoMCP | herramienta | Puente agente ↔ Rhino |

## 5. Referentes

| # | Referente | Aporte |
|---|---|---|
| R1 | McNeel / Robert McNeel & Associates | Documentación oficial Rhino 8: PushPull, Make2D, Layouts |
| R2 | Universidad de Granada — SMlab | Curaduría del mejor índice de tutoriales ES |
| R3 | Dusan Cvetkovic — How to Rhino | Flujo DWG→3D documentado con criterio |
| R4 | Diego Pascual · Tom Budd · Hakan Architecture | Series ES: casa y planos |

## 6. Qué parte de la wiki alimenta

| # | Destino wiki | Tipo | Acción | Sección | Prioridad | Owner |
|---|---|---|---|---|---|---|
| 1 | [[wiki/glosario/software/rhino\|rhino]] | software | actualizar | PushPull + 3D→planos + ecosistema RhinoMCP | alta | vía @vaultworm-arq con `s` |
| 2 | `wiki/glosario/conceptos/modelado-vivienda-rhino` | concepto | crear | Flujo de 7 pasos + tabla de comandos + 3 rutas | alta | @contenidos con `s` |
| 3 | `wiki/glosario/conceptos/planos-como-documento-legal` | concepto | crear | Ley 24.335 aplicada al tramo Make2D/Layout | media | @contenidos con `s` |

> Integra antes de duplicar: `wiki/glosario/software/rhino.md` existe como stub (NURBS, Make2D para ControlNet, Grasshopper). Las secciones nuevas avanzan sobre esa base sin repetirla.

## 7. Propuestas wiki esqueleto

- P1 — Ampliar [[wiki/glosario/software/rhino|rhino]] con `## Rhino 8 / PushPull`, `## 3D → planos (Make2D + Layout)`, `## Ecosistema (RhinoMCP)`, `## Aprendizaje (rutas ES/EN)`.
- P2 — Crear `wiki/glosario/conceptos/modelado-vivienda-rhino.md` (`tipo: conceptos`): unidades y capas → sólido base → muros → aberturas → cubierta → escalera → `Make2D` → `Layout`, con tabla comando-por-recurso.
- P3 — Crear `wiki/glosario/conceptos/planos-como-documento-legal.md`: por qué el tramo 2D es requisito registral y cómo se verifica (escala, rótulo, cotas).

## 8. Estado wiki

| Destino | Acción | Link | Fecha |
|---|---|---|---|
| — | pendiente `¿Avanzo? s` | — | 2026-10-22 |

## 9. Decisiones SOL

- [ ] Aprobar / [ ] Corregir / [ ] Descartar por propuesta

## 10. Preguntas para SOL

- ¿Arrancamos por la **ruta A (PushPull, oficial)** o por la **ruta B (DWG del cliente)** según el próximo trabajo real del estudio?
- ¿Bajamos el `.3dm` de la guía oficial (`PP-Architecture-Start.3dm`) como activo del vault para práctica interna?
- ¿Qué serie ES entra a Fase 2 de transcripción: Diego Pascual (casa 4/4) o Tom Budd (planos 5 videos)?
- ¿Sumamos RhinoMCP a la evaluación de stack o queda como nota de ecosistema hasta tener tutorial arquitectónico?
- ¿Necesitamos una ficha propia de estándar de dibujo Rhino AR (capas, pesos, rótulo) o reusamos el estándar AutoCAD ya documentado?

## 11. Referencias verificadas

Ver detalle completo en [[raw/research/2026-10-22-modelar-casa-rhino|informe madre]] — 11 fuentes con `webfetch` 200 + 13 citadas. Sin 404. Duraciones de YouTube no expuestas al fetch: se confirman en Fase 2 con `yt-dlp`.
