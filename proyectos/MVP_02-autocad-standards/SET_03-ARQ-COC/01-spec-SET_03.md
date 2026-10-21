---
tipo: spec
mvp: 02
nivel: SET_03-ARQ
set_numero: "03"
set_disciplina: ARQ
set_nombre: Cocina
version: 0.1-base-dxf-real
fecha_creacion: 2026-10-16
ultima_actualizacion: 2026-10-16
tags: [mvp_02, SET, SET_03, cocina, autocad-lt, dxf, planta-1_50, vista-1_20, anotativas, xref]
idioma: es
base_empirica: D:\Users\Solch\Desktop\AUTOCAD\TRABAJOS-AUTOCAD\NATACHA SERANTES\2026-COCINA_TAGLE\COCINA20261016.dxf
---

# SET_03-ARQ-COC — Cocina interiorismo 1:50 + 1:20 v0.1

> **SET** = Set de herramientas, Standards, Capas, Puntas
> Estructura: hereda `../01-spec-mvp_02.md` (10 items). Detalle abajo con dato real DXF, sin inferencia.
> Base empírica: `COCINA20261016.dxf` (844KB, AC1027, 99371 líneas) leído 2026-10-16. Binarios fuera de git, solo ruta.
> Contexto: sigue a SET_01-REP (terreno) y SET_02-GEST (municipio). SET_03 resuelve interiorismo cocina ejecutiva.

## 0. DoD SET_03

- [ ] **1. SETEO** → §1 (metros `INSUNITS=6`, `LIMMAX` 420x297, escalas 1:50 planta + 1:20 vistas)
- [ ] **2. LAYERS** → §2 (24 reales: `A-MURO, A-SOLADOS, A-CARPINTERIA, A-EQUIPAMIENTO, A-COTAS, A-VISTA-0..4, rotulo`, etc.)
- [ ] **3. CTB** → §3 (`monochrome.ctb` municipal + color presentación)
- [ ] **4. TEXTSTYLES** → §4 (6 reales → 1 `ARQ-2.5-Anno`)
- [ ] **5. DIMSTYLES** → §5 (8 reales → 2 `ARQ-50` + `ARQ-20`)
- [ ] **6. BLOQUES** → §6 (equipos 1x c/u + `_ArchTick` 78x)
- [ ] **7. DINÁMICOS** → §6.2 (`cocina-600` stretch, pileta visibilidad, puerta flip) — especificados, no implementados
- [ ] **8. TEMPLATE** → `activos/proyectos/mvp_02-autocad-standards/SET_03-ARQ-COC/SET_03-COC.dwt` (NO en git)
- [ ] **9. AUTOLISP** → `lisp/SET_03-COC.lsp` cmd `SET-03-COC`
- [ ] **10. GLOSARIO** → diferido a [[wiki/glosario/software/autocad|AutoCAD]] + [[wiki/estudio/instructivo-cocina-tagle|instructivo-cocina-tagle]]

## 1. SETEO

| Variable | Valor real | Decisión SET_03 |
|---|---|---|
| `INSUNITS` | 6 metros | mantener |
| `LUNITS/LUPREC` | 2 / 4 decimal | bajar a 2 decimales en DWT |
| `MEASUREMENT` | 1 métrico | mantener |
| `LIMMIN/MAX` | 0,0 / 420,297 | A3 apaisado semilla |
| `TEXTSIZE` | 0.05 | 0.05m = 2.5mm papel en 1:20, 1mm en 1:50 → justifica 2 dimstyles |
| `DIMSCALE` | 1.0 | pasar a anotativo |
| `CLAYER` | `A-VISTA-4` | mantener prefijo `A-VISTA-` por vista |
| `LTSCALE` | 0.01 | revisar en DWT con `PSLTSCALE=1` |

Escalas: `SCALELISTEDIT` solo 1:50 / 1:20 / 1:10 / 1:5. Viewports lock Yes (`0.02`=1:50, `0.05`=1:20).

## 2. LAYERS (24 reales)

`0, A-CARPINTERIA, A-CARPINTERIA2, A-CARPINTERIA-DET, A-COTAS, A-COTAS-Equip, A-EJES, A-EQUIPAMIENTO, A-HATCH-SOLADO, A-MURO, A-PROYECCIONES, A-SOLADOS, A-TEXTO, A-VISTA-0..4, A-VISTA-HATCH, Defpoints, DEMOLICION, H-MURO, POLILINEAS, rotulo`

Regla: `A-` modelo, `rotulo` paper, `VPORT` NoPlot por crear, `DEMOLICION` con DASHED, purgar `POLILINEAS`/`Defpoints` residual.

## 3. CTB

`monochrome.ctb` para entrega + color presentación. Lineweight manda lectura.

## 4. TEXTSTYLES (6 → 1)

Reales: `Standard, Romans, COTAS, Annotative, 1.20, X-TEXTO COTAS VARIAS` → unificar en `ARQ-2.5-Anno` (Arial/Romans, anotativo, 2.5mm papel).

## 5. DIMSTYLES (8 → 2)

Reales: `Annotative, ARQUITECTURA, COTAS-100, DETALLE, ISO-25, Standard, X-25-COTA DETALLES, X-25-COTA PLANTAS`
Destino: `ARQ-50` planta replanteo + `ARQ-20` vistas detalle, tick `_ArchTick`, texto 2.5mm papel. Anotativa solo si misma cota sale en ambas escalas.

## 6. BLOQUES

### 6.1 Biblioteca fija (INSERT 148)

- `78x _ArchTick` (ok, ticks cota)
- Equipos 1x: `MICRO FR, Microwave / Microondas-02, cocina-domec-55-58, HO-ELEC, licuadora, tostador, 411-87 VF, mesa120x70, LUXOR MINI SI55A`
- Anónimos `A$C...` x2 + `*U25/26` → `PURGE`, convertir grupos a bloque

### 6.2 Dinámicos (especificados)

- `COC-BM-600`: bajo mesada stretch 450-1200 + visibilidad con/sin pileta + flip
- `COC-PU-BAT`: puerta lookup 0/45/90, capa `0` → explota a `A-CARPINTERIA`

## 7. HATCH + COTAS + TEXTO

- Hatch 26: `SOLID 19x, _USER 4x, AR-B816C 3x` → sumar cerámico/solado con nombre en `A-HATCH-SOLADO`
- Cotas 38 + textos 81 (`MTEXT 75 + TEXT 6`) → pasar a estilos §4-5

## 8. SHEETS

- `*Paper_Space` x3 = Model + 2 hojas, `VIEWPORT` x8, `rotulo` en paper
- Layouts: `COC-Planta-A3` 1 viewport 1:50 lock + `COC-Vistas-A3` 2 viewports 1:20 lock
- Rótulo con Fields `CurrentSheetNumber/Title/PlotDate`, DST `COCINA-TAGLE.dst`

## 9. XREF

Planta base como xref overlay en archivo vistas. `VISRETAIN=1`, path relativo, `XDWGFADECTL=50`.
Oficial: https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-53030EDD-1D1D-40C4-922E-9B964A048ED9

## 10. Próximos

1. Validar 24 capas + 2 dimstyles con equipo
2. Construir 2 dinámicos §6.2
3. Crear DWT + DWS + DST piloto
4. Plano piloto: 1 planta 1:50 + 2 vistas 1:20 + publish PDF
