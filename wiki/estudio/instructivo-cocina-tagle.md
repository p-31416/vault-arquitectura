---
tipo: metodologia
fecha_creacion: 2026-10-16
ultima_actualizacion: 2026-10-16
tags: [autocad, cocina, sheets, anotativas, xref, instructivo]
idioma: es
---

# Instructivo cocina Tagle — de DXF real a set de planos

> Fuente real leída: `D:\Users\Solch\Desktop\AUTOCAD\TRABAJOS-AUTOCAD\NATACHA SERANTES\2026-COCINA_TAGLE\COCINA20261016.dxf` (844KB, AC1027, 99371 líneas). Solo lectura, sin modificar DWG.

## 1. Estado real

- Uds metros (`INSUNITS=6`), decimal prec 4, `LIMMAX` 420x297 (A3)
- Capa actual `A-VISTA-4`, texto 0.05, `DIMSCALE` 1.0
- 24 capas: `A-MURO, A-SOLADOS, A-CARPINTERIA, A-EQUIPAMIENTO, A-COTAS, A-VISTA-0 al 4, A-HATCH-SOLADO, rotulo`, etc.
- Bloques: `mesa120x70, MICRO FR, Microwave, HO-ELEC, LUXOR MINI SI55A`
- Entidades: `LINE 1796, LWPOLYLINE 179, INSERT 148, MTEXT 75, DIMENSION 38, HATCH 26, VIEWPORT 8, TEXT 6`
- Lectura: muchas LINE sueltas = oportunidad de bloques + estándar. Ver [[wiki/glosario/software/autocad|AutoCAD]].

## 2. Sheets (Model vs Layout vs Viewport vs Sheet)

- `*Paper_Space` x3 = Model + 2 hojas paper
- `VIEWPORT` x8 en total, capa `rotulo` en paper
- Regla: Model 1:1 m > Layout A3 1:1 > Viewport lupa (`0.02`=1:50 planta, `0.05`=1:20 vista, Lock Yes) > Sheet = ficha DST con número/título
- En LT verificar escala con `PROPIEDADES` del viewport + `REGENALL`

## 3. Cotas anotativas: ¿cuándo sí?

- Dato real: `DIMTXT 0.05m` = 1mm papel en 1:50, 2.5mm en 1:20
- Tu criterio vale: 1:50 acota muros/replanteo general, 1:20 acota mueble/frentes/detalle. Objetos distintos.
- Usar anotativa solo cuando la misma cota aparece en ambas escalas. Si no, dos estilos fijos rinden más y evitan ruido:
  - `ARQ-50` para planta, `ARQ-20` para vistas, ambos 2.5mm papel
- Chequeos: `ANNOAUTOSCALE=1`, `ANNOALLVISIBLE=1`, `SCALELISTEDIT` limpia 1:50/1:20

## 4. Bloques, hatches, capas

- Pasar LINE repetidas a bloques dinámicos: bajo mesada stretch 450-1200 + visibilidad con/sin pileta + flip
- Hatches en `A-HATCH-SOLADO` asociativo, capa propia
- Capas base: `A-MURO, I-FURN, I-EQPM, A-DIMS, A-TEXT, VPORT` (NoPlot)

## 5. DWT / DWS / Publish

- DWT `ESTUDIO-ARQ-Metric-m.dwt`: UNITS m, capas, estilos, layouts semilla A101/A201, Page Setup `A3-PDF-1a1`
- DWS `ESTUDIO-ARQ.dws` + `STANDARDS` para chequear
- Publish desde Sheet Set a PDF multipágina + `ETRANSMIT`

## 6. Xref (referencia externa)

- Para armar cocina sin copiar: planta base como xref overlay en archivo de vistas/detalles
- Si se mueve el xref, `XREF` > repath relativo, `VISRETAIN=1`, `XDWGFADECTL=50`
- Oficial Autodesk (verificado vía MCP Help 2026-10-16):
  - Attach External Reference Dialog Box: https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-53030EDD-1D1D-40C4-922E-9B964A048ED9
  - Xref management strategies: https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/External-Reference-xref-management-strategies-in-AutoCAD.html

## 7. Paso a paso LT

1. Abrir DXF, `AUDIT` + guardar DWG
2. Fijar `INSUNITS=6`, capa por función
3. Bloquear mobiliario repetido en bloque
4. Acotar: `ARQ-50` en planta, `ARQ-20` en vistas
5. Layouts: 1 viewport planta 1:50 lock, 2 viewports vistas 1:20 lock
6. Rótulo en paper + publish PDF
