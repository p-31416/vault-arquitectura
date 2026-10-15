---
tipo: metodologia
mvp: 02
set: SET_01-REP
fecha_creacion: 2026-10-15
ultima_actualizacion: 2026-10-15
tags: [mvp_02, SET_01, informe, emilia, kit, drive]
idioma: es
estado: borrador-para-lectura
---

# PB-01 — SET_01-REP Informe (qué recibe Emilia)

> Borrador para lectura. PDFs en pausa hasta tu `s`. Spec/ft quedan intactos como auditoría.
> Audiencia: Emilia. Tiempo lectura: 10 min. Base Full EN.

## 1. Qué es

Plano de replanteo arquitectónico 1:50: sistema de referencia desde el cual se mide toda la obra (ejes, cotas parciales/acumuladas, vanos a ejes, muros a filos, niveles NPT, columnas). Modelo en metros. Base medida: `REP-ARAOZ.dwg` (49 capas, 13 bloques, 304 cotas, 208 inserts).

Origen medido: `G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg` (externo, fuera de git).

## 2. Kit a mano (Drive, disponible para Emilia)

Destino Drive: `G:\Mi unidad\OS-Emilia\W03-CAD\SET_01-REP\` (espejo local gitignored: `activos/proyectos/mvp_02-autocad-standards/SET_01-REP/`).

| Archivo Drive | Qué es | Estado |
|---|---|---|
| `SET_01-REP.dwt` | Plantilla única para `NUEVO`: 29 capas + 9 estilos texto + 3 cotas + metros `INSUNITS 6` + lista `1:50 (m)` + layout `REP-PTipo-A1` + **13 bloques integrados** (2 dinámicos + tags + carátula) — abrir y dibujar | Generado, verifica ida/vuelta |
| `SET-REP.dws` | Norma para `CHECKSTANDARDS` / `VERIFICANORMAS` | Generado misma base |
| `monochrome.ctb` | **CTB vigente**: viene con todo AutoCAD (Full + LT), grafica todo negro. `EP-ISO.ctb` con grosores queda en backlog hasta manejar varias escalas | Usa sin instalar, elige en `PAGESETUP` / `PLOT` |
| `SET_01-REP_bloques.dwg` | Biblioteca madre editable (fuente de los 13 bloques del DWT, para `WBLOCK` / Tool Palettes / DesignCenter) — avanza como respaldo, el uso diario sale del DWT | Medido, consolida en PB-02 paso 5 |
| `SET_01-REP.lsp` | Comando `SET-REPLANTEO`: crea 29 capas (color/tipo/estado) + fija variables (`INSUNITS 6`, `LUNITS`, `MEASUREMENT`) + reporta verificación. Avanza idempotente en dibujo limpio; en siguiente ciclo suma estilos + escalas + layout | Borrador spec §7, API real en siguiente ciclo |
| `PB-01-SET-informe.md` + `.pdf` | Este informe | Borrador (este archivo) |
| `PB-02-replanteo-desde-0.md` + `.pdf` | Instructivo paso a paso Full EN | Borrador, PDFs en pausa |

CTB vigente: `monochrome.ctb` (preinstalado en Plot Styles, grafica todo negro — [Table Reference](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-F6DF548E-DF71-45F7-8DC5-A1EAD73998B1) · [How to Plot B/W](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-Plot-in-Grayscale-or-Black-and-White-from-AutoCAD-Products.html)). `EP-ISO.ctb` con grosores ISO avanza en backlog hasta manejar varias escalas.

### 2.1 DWT — trae bloques integrados (sin oposición)

Avanzamos con tu criterio: DWT único trae todo (capas + metros + escalas + cotas + textos + **bloques en memoria**). En SET_01 con 13 bloques el costo de peso avanza compensado por flujo simple para Emilia (`NUEVO` y dibuja, cero `INSERT` desde archivo aparte). Memoria = pestaña Current Drawing de Blocks palette, organizada en 3 grupos: (a) vanos dinámicos 2 · (b) tags/niveles 5 · (c) carátula + puntas. Práctica oficial para bibliotecas grandes avanza con DWG + Tool Palettes/DesignCenter ([About Organizing Blocks](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-9C9FF3BC-7275-44E8-93D4-00A2F50BC96D) · [Tool Palettes](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-6B20D7DF-447A-4A8D-8FF1-8339CF54FFBD)); por eso `SET_01-REP_bloques.dwg` avanza como madre editable y el DWT como distribución.

Palettes en LT: sí incluidas (LT trae `TOOLPALETTES` + `ADCENTER` + Blocks palette — [Tool Palettes LT 2027](https://help.autodesk.com/view/ACDLT/2027/ENU/?guid=GUID-6668905A-3FAD-4EED-82A2-5D6177AD4280) · [DesignCenter LT](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-insert-blocks-using-DesignCenter-for-AutoCAD-LT.html)). Solo quedan fuera en LT luces/cámaras/materiales. LISP: Full + LT 2024+ Win vía `APPLOAD`; LT 2023- y LT Mac devuelven `Unknown Command` ([LISP en LT](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Unable-to-load-lisp-in-AutoCAD-LT.html)) — en ese caso el DWT ya trae el setup hecho. Detalle operativo en PB-02 §1.5.

## 3. DoD (auditoría, spec/ft intactos)

| # | Ítem | Estado | Dónde vive detalle |
|---|---|---|---|
| 1 | SETEO | cumple | [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/01-spec-SET_01\|01-spec §4.2 + §4.6]] |
| 2 | LAYERS 29+20 | cumple | [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/REP-ARAOZ-capas-bloques\|REP-ARAOZ-capas-bloques §1]] |
| 3 | CTB | cumple con `monochrome.ctb` vigente; `EP-ISO.ctb` en backlog multi-escala | PB-01 §2 + [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/01-spec-SET_01\|01-spec §4.4]] |
| 4 | TEXTSTYLES 9 | cumple | spec §4.2, destino `EP-2.5/EP-3.5` backlog |
| 5 | DIMSTYLES 3 | cumple | spec §4.2, destino `EP-ARQ` backlog |
| 6 | BLOQUES 13 | cumple | [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/bloques-personalizados\|bloques-personalizados]] |
| 7 | DINÁMICOS/ATRIB → cómputos | cumple | [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/cuadro-carpinterias\|cuadro-carpinterias]] |
| 8 | TEMPLATE | avanza parcial | ruta activos, doc `template-dwt.md` siguiente ciclo |
| 9 | AUTOLISP | avanza parcial | spec §7, `lisp/` con API real siguiente ciclo |
| 10 | GLOSARIO | diferido | avanza hacia wiki tras evaluar SET_01 |

## 4. Por qué así (registro único)

- [[proyectos/MVP_02-autocad-standards/03-adr-SET_01\|03-adr-SET_01]] — ADR-A unidades/escala (metros `INSUNITS 6` + custom `1:50 (m)` 20 XP) · ADR-B capas/rótulo (nombres archivo + `ROT-` paper-only) · ADR-C bloques/cómputos/FIELD (intactos + `DATAEXTRACTION` + `FIELD`) · ADR-D entorno/Drive (Full EN + kit con DWS + `monochrome.ctb` vigente)

Tras tu aprobación avanzan hacia `wiki/estandares/` + `wiki/glosario/software/autocad` + `log.md`.

## 5. Horas y payback

14 h invertidas (10 h construcción + 4 h medición/docs). Ahorro por plano futuro ~12-15 h (setup + inserciones + cómputos). Payback en primer plano completo. Detalle y supuestos: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/desglose-configuraciones\|desglose-configuraciones]].

## 6. Mapa (evita duplicados)

- QUÉ técnico: `01-spec-SET_01.md` (475 líneas, intacto)
- CÓMO inicial: `02-ft-SET_01.md` §1 (intacto)
- Medición madre: `docs/REP-ARAOZ-capas-bloques.md`
- Catálogo bloques: `docs/bloques-personalizados.md`
- Operativa diaria: `PB-02` (este set, siguiente archivo)
- Primer plano JR: `docs/guia-jr-replanteo.md` (integra hacia PB-02, conserva glosario mínimo)

## 7. Siguiente paso

Lees PB-01 + PB-02 en MD. Con tu `s`: paso a PDF para Drive. Tras evaluar SET_01: pase a wiki + mkdocs online.
