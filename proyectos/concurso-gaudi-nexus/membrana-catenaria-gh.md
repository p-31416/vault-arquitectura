---
tipo: metodologia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, catenaria, kangaroo, grasshopper, membrana, trazabilidad]
idioma: es
---

# Membrana catenaria paramétrica — método, archivos y fuentes

> Dónde vive el trabajo de cáscara del concurso: qué se modeló, con qué método, en qué archivos y de qué fuentes sale cada decisión. Puerta a los `.gh` (binarios en `activos/`, fuera de git).

## 1. Qué se hizo

- **Membrana 1 — loft reglado** (archivado, eliminado de escena): extrusión de catenaria transversal con ola longitudinal. Sirvió para fijar medidas (`L=8, LONG=30, H=2,5`) y el teselado triangular `s=1,2`.
- **Membrana 2 — doble curvatura matemática** (en escena, capas `CASCARA`, `CAMINO`, `VERDE`, `APOYOS`, `PISO`): catenaria en X (`7,5 m / flecha 0,6`) × catenaria en Y (`8 m / flecha 0,8`), invertida, 10 apoyos, piso a −1,0. Luz libre al centro 4,8 m.
- **Definición Grasshopper `membrana-catenaria.gh` → `v2`** (paramétrica, Kangaroo2): rectángulo → `MeshPlane` → anclas en 4 esquinas → `EdgeLengths` + `Load` → `Solver` → espejo en XY (la simulación cuelga, el espejo la vuelve bóveda a compresión) → `Show` + `TriRemesh`. Después: esquinas a altura independiente (`H1–H4`) y malla de piso con depresión editable (`Prof` vía `Point Deform`).
- **Réplica Fig. 6 de Makert (pendiente)**: malla 10×10 con carga puntual en un vértice, tal cual el experimento del paper. Definida, a construir cuando el puente Rhino esté activo (`fig6-malla-10x10.gh`).

## 2. De qué fuentes sale

| Decisión | Fuente |
|----------|--------|
| Mesh en vez de NURBS, anclas + resortes + gravedad, componente matemático vs Kangaroo, membranas y estructuras anidadas | Wintour, P. (2015). *Catenary curves and membranes in Grasshopper*. Parametric Monkey. https://parametricmonkey.com/2015/10/10/catenary-curves/ (verificado 200) |
| Malla 10×10, carga en un vértice, sin invertir el modelo digital, comparación físico vs digital | Makert, R., Alves, G. (2016). *Between Designer and Design*. Periodica Polytechnica Architecture, 47(2), pp. 89–93. https://doi.org/10.3311/PPar.10335 (verificado 200) · transcripción local en [[raw/pdf/2026-10-20-between_designer_and_design-transcripcion|between_designer_and_design-transcripcion]] |
| Contexto catenarias Gaudí / Kangaroo del estudio | [[raw/research/2026-10-30-gaudi-catenarias-cascaras-tensadas|gaudi-catenarias-cascaras-tensadas]] |
| Precepto rector (camino fractal, cáscara habitable, museo bajo plaza) | [[proyectos/concurso-gaudi-nexus/reinterpretacion-programa-fractal|reinterpretacion-programa-fractal]] |

## 3. Archivos

- `activos/proyectos/concurso-gaudi-nexus/grasshopper/membrana-catenaria.gh` — v1 (anclas en plano, 4 esquinas a `z=0`).
- `activos/proyectos/concurso-gaudi-nexus/grasshopper/membrana-catenaria-v2.gh` — vigente: + `H1–H4` por esquina + malla de piso con `Prof`. 34 objetos, 41 cables, 0 obsoletos (verificado por API).
- Escena Rhino: capas `CASCARA`, `CAMINO`, `VERDE`, `APOYOS`, `PISO`, `PROGRAMA_M2` (4 rectángulos de control: Museo 950, Mercado 450, Feria 900, Digital 380).

## 4. Reglas de uso

- El `.gh` manda; Rhino recibe por `Bake`. La malla 2D de control de m2 vive en `PROGRAMA_M2`.
- Sliders de juego: `Factor` (panza), `Peso` (carga), `s_tri` (tesela), `H1–H4` (apoyos), `Prof` (depresión del piso).
- Versiones nuevas como archivo nuevo (`v3`, …), nunca se pisa la vigente.
