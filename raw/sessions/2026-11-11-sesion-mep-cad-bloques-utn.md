---
tipo: log
fecha: 2026-11-11
tags: [sesion, mep-abierto, freecad, cad-bloques, utn-computos, electrica, sanitaria]
---

# 2026-11-11 — Sesión MEP abierto + CAD bloques UTN

## Qué se hizo

- Investigación @sherlock FreeCAD como opción FLOSS/OpenBIM para eléctrica + sanitaria: `raw/research/2026-11-10-freecad-mep-floss.md` + cache.
- Investigación mejor opción MEP abierta con normas AR AEA/IRAM/AySA/ENARGAS + librería AR 12 piezas: `raw/research/2026-11-10-mep-abierto-normas-ar.md`.
- Relevamiento marcas con bloques CAD + BIM mínimo sin licencias (ABB/Siemens/Schneider/Legrand/FV/Ferrum/Roca/Tigre/Saladillo vs gap IMSA/Cambre/Jeluz/Kalop/Prysmian): `raw/research/2026-11-10-marcas-bloques-cad-bim.md`.
- Revisión curso UTN `D:\Users\Solch\Desktop\ESTUDIO.AR\CAPACITACION PROFESIONAL\UTN-ComputosYPresupuestos` (M1 suelos/H°A°/metálica, M2 mampostería/carpinterías/terminaciones, M3 agua/cloacal/pluvial/gas/incendio/eléctrica, M4 costos/venta + catálogos).
- Decisión SOL: hacerlo en CAD con bloques con atributos (no BIM full aún).
- Documento único creado: `raw/contenidos/2026-11-11-utn-computos-bloques-atributos.md` con todo extraíble + esquema ATTDEF `CODIGO-RUBRO-ITEM_UTN-UN-MARCA-NORMA_AR-MEDIDA` para DATAEXTRACTION a XLS UTN.
- Índice `raw/research/00-index.md` actualizado (ultima_actualizacion 2026-11-11).

## Archivos modificados

- `raw/research/2026-11-10-freecad-mep-floss.md` (nuevo vía sherlock)
- `raw/research-cache/2026-11-10-freecad-mep-floss.json` (nuevo)
- `raw/research/2026-11-10-mep-abierto-normas-ar.md` (nuevo)
- `raw/research-cache/2026-11-10-mep-abierto-normas-ar.json` (nuevo)
- `raw/research/2026-11-10-marcas-bloques-cad-bim.md` (nuevo)
- `raw/research-cache/2026-11-10-marcas-bloques-cad-bim.json` (nuevo)
- `raw/contenidos/2026-11-11-utn-computos-bloques-atributos.md` (nuevo)
- `raw/research/00-index.md` (filas nuevas arriba)
- `raw/contenidos/sherlock-mep-abierto-normas-ar.md` (stub)
- `raw/contenidos/sherlock-marcas-bloques-cad-bim.md` (stub)

## Cerebro-digital

- topics: [mep-abierto, freecad-bim, cables-workbench, bonsai-ifc, bloques-atributos-cad, computos-utn, electrica-aea, sanitaria-aysa, libreria-mep-ar]
- entidades: [FreeCAD-1.1.4, Cables-0.4.1, Bonsai-0.9.1, QET, ABB-library, Siemens-PartCommunity, FV-Bimetica, TigreBIM, Duratop-DWG, UTN-850, AZCONA-TP]
- hechos: [stack ganador FreeCAD+Cables+QET+Bonsai+QCAD; ninguna marca da DWG con atributos; Tigre único con cómputo; IMSA/Cambre/Jeluz/Kalop/Prysmian gap; piloto propuesto cloacal+eléctrica con DATAEXTRACTION; pendiente plano AZCONA]
- pendiente: [seguir sobre plano AIZ-/AZCONA: levantar bloques existentes, normalizar ATTDEF, correr DATAEXTRACTION a planillas 17a + 20]

Más nuevo → más arriba
