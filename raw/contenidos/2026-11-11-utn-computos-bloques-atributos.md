---
tipo: reporte-contenidos
fecha_creacion: 2026-11-11
ultima_actualizacion: 2026-11-11
tags: [utn, computos, presupuestos, bloques-atributos, cad, mamposteria, terminaciones, sanitaria, electrica]
idioma: es
fecha: 2026-11-11
fuente_binaria: D:\Users\Solch\Desktop\ESTUDIO.AR\CAPACITACION PROFESIONAL\UTN-ComputosYPresupuestos
estado: propuesta
---

# UTN Cómputos y Presupuestos — Todo extraíble para CAD con bloques con atributos — 2026-11-11

> Inventario completo de planillas + bases CAD del curso para armar librería `activos/libreria-mep-ar/01_dwg-atributos/` y cómputo global mampostería, terminaciones, sanitarias, agua, eléctrica.

## 0. Gate HITL

> `¿Avanzo a wiki? (s/N)` — Sin `s` no hay `write` en `wiki/`.

## 1. Resumen (qué podés extraer)

- Mampostería + estructura + contrapisos + revoques desde M1/M2 con planillas base y DWG.
- Terminaciones locales + revestimientos + terminaciones ext desde M2-U3/U4 con CSV + XLS listos para DATAEXTRACTION.
- Agua + cloacal + pluvial + gas + incendio + eléctrica desde M3 con 7 planillas oficiales + 30+ bloques Duratop + bases CAD.
- Costos + presupuesto venta desde M4 para cerrar precio: MO, gremios/equipos, base costos, presupuesto edificio.
- Atributo único para todo bloque: `CODIGO - RUBRO - ITEM - UN - MARCA - NORMA_AR - MEDIDA`.

## 2. Inventario por módulo — planilla + base CAD + bloques

### M1 Movimiento suelos + H°A° + Metálica/Madera

| Módulo | Planilla extraíble | Base CAD | Bloques / datos para atributos |
|---|---|---|---|
| M1-U2 Suelos | `01 Planilla de movimiento de suelos.xls`, `02 Computo excavaciones superficiales.xls` | `TP02-AZCONA.dwg` | Perfiles excavación, volúmenes m3. ATT: `SUE-EXC - m3 - cota - tipo suelo` |
| M1-U3 H°A° | `planillas base/` + `Ejemplo memoria e-learning.pdf` | `M1U3-Plano_Est_HºAº-AZCONA.dwg` | Bases, columnas, vigas, losas, escalera. ATT: `E-HA-VIGA - m3/m2/kg - H21/fe` |
| M1-U4 Metálica/Madera | `Ejercicio_Cómputo-Caminadora-Incompleto.xls`, `Planillas/`, `TABLAS ACINDAR.pdf` | `Estructura_CAMINADORA.dwg` | Perfiles IPN/UPN/chapa. ATT: `E-MET-PERFIL - kg/ml - Acindar` |

### M2 Mampostería + Carpinterías + Terminaciones (cómputo global)

| Módulo | Planilla extraíble | Base CAD | Bloques / datos |
|---|---|---|---|
| M2-U2 Mampostería | `DATOS-CAD.xls`, `U2M2-*.dwg` (estructura, carpinterías) | `U2M2-TP06-Mamposteria_AZCONA` + `U2M2-CARPINTERIAS.dwg` | Muros m2/m3 por espesor, vanos descuento. ATT: `MAMP-LAD-18 - m2 - hueco 18x19x33` |
| M2-U1 Carpinterías | `CARP01-05.dxe`, `planos/` | `M2-U1-Azcona.dwg` | Puertas/ventanas/rejas. ATT: `CARP-P1 - u - 0.90x2.10 chapa` |
| M2-U3 Terminaciones int | `12 Planilla Revestimientos.xls`, `13 Planilla Terminaciones Locales.xls/.csv`, `04-U2M3-contrapisos.csv`, `COMP-GEOM.dwg` | `04-U2M3-TP07_Terminaciones-AZCONA.dwg`, `PLANOS/` | Contrapiso, carpeta, cerámico, revoque, cielorraso, pintura por local. ATT: `TERM-REV-CER - m2 - 20x20` + `bloque con atributos_LUIS.txt` ya trae ejemplo |
| M2-U4 Terminaciones ext | `TERM-EXT/`, `CHAPAS/` | `M2U4-TP08-Estructura_Caminadora-AZCONA.dwg` | Revestimiento ext, chapas, aislaciones. ATT: `TERM-EXT-CHAPA - m2 - calibre` |

### M3 Instalaciones — agua + sanitaria + gas + eléctrica (foco estudio)

| Módulo | Planilla extraíble | Base CAD | Bloques con atributos a crear |
|---|---|---|---|
| M3U1 Agua | `15 Planilla cómputo Instalacion Agua.xls`, `16 Planilla Nucleos Sanitarios.xls` | `M3U1-BASE-CAD.dwg`, `M3U1-BASE-CAD02.dwg`, `Bano_y_cocina_portero.dwg` | Tubo-H/M, codo, tee, tee-red, LLP, tapa, tubo-H fotos JPG = piezas. ATT: `AG-CAÑO-20 - ml - AcquaSystem - IRAM` / `AG-CODO-90-20 - u` |
| M3U2 Cloacal/Pluvial | `17a Cloacal.xls`, `17b Pluvial.xls`, `ENTREGA_TP/01-U3M2-TP010-Planillas.xls`, `cloacal.csv/.dxe` | `M3U2-BASE-CAD02.dwg`, `bloques_autocad_DESAGUES_DURATOP/` 24 DWG (TUBO-M-H-40/50/60/110, CODO-M-H-40/50/63/110, CODO90, EMPALME-63-50, PPA-63x40 + 7 en 3D) | Duratop directo. ATT: `CLO-CODO-110 - u - Saladillo - AySA Ø110` / `CLO-TUBO-63 - ml - pendiente 1:50` / `CLO-PPA - u` |
| M3U3 Gas/Incendio | `BASE_TP/18 Gas.xls`, `19 Incendio.xls`, `01-U3M3-TP011-Planillas.xls` | `M3U3-BASE-CAD.dwg`, `BASE_TP/Plano instalación gas.dxf` | Sigas, llaves, artefactos, extintores. ATT: `GAS-CAÑO-25 - ml - Sigas - NAG200` / `INC-EXT-5KG - u` |
| M3U4 Eléctrica | `20 Planilla Instalacion Electrica.xls`, `ENTREGA_TP/01-U3M4-TP12-Planillas.xls` | `M3U4-BASE-CAD.dwg`, `PLANO_INST_ELECTRICA.dwg` | Tomas, llaves, tableros, cañería, cables. ATT: `EL-TOMA-10A - u - Cambre IRAM2071 AEA90364` / `EL-CAÑO-3/4 - ml` / `EL-CABLE-2.5 - ml IRAM2178` |

Catálogos para medidas: `CATALOGOS INSTALACIONES/` (Acqua_System_completo.pdf, awaduct.pdf, duratop-*.pdf, Manual-Tecnico-DESAGUE.pdf, Sigas_Thermofusion_13.pdf, IPS-GAS-MANUAL.pdf).

### M4 Costos + Venta (cierra presupuesto)

| Módulo | Planilla extraíble | Uso |
|---|---|---|
| M4U1 MO | `22 Costo Mano Obra.xlsx`, `01-Planillas_CostoMO_Zonas.xlsx` | Costo hora por zona UOCRA |
| M4U2 Gremios/Equipos | `23 Gasto automóvil.xls`, `24 Gasto equipo.xls`, `01-Planillas_AMAROK/HILUX.xls` | Ayuda gremios + equipos |
| M4U3 Base costos | `01-M4U3-Planillas.xls`, `BASE_INEFICIENTE.xls` | Análisis precios unitarios |
| M4U4 Venta | `Base_Costos.xls`, `Presupuesto_Edificio.xls`, `01-M4U4-Base_Costos.xls`, `TP7 Cómputo.pdf + Tabla Dinámica.pdf`, `funciones.xls` | Presupuesto venta final con tablas dinámicas |

## 3. Esquema atributos único para DATAEXTRACTION

Bloque = `NOMBRE = CODIGO`. ATTDEF:

```
CODIGO (ej EL-TOMA-10A)
RUBRO (Mampostería / Terminaciones / Agua / Cloacal / Pluvial / Gas / Eléctrica)
ITEM_UTN (texto exacto planilla UTN para vincular)
UN (u/ml/m2/m3/kg/gl)
MARCA (Cambre / FV / Duratop / AcquaSystem / etc)
NORMA_AR (AEA90364 / IRAM2071 / IRAM2178 / AySA / NAG200)
MEDIDA (Ø40 / 110mm / 2.5mm2 / 20x20 / etc)
```

Flujo CAD: `ATTDEF` en base DWG → `DATAEXTRACTION` → `.csv/.dxe` → pega en `*.xls` UTN → cómputo + presupuesto.

Ya tenés ejemplos andando: `M2-U3/bloque con atributos_LUIS.txt`, `04-U2M3-contrapisos.csv`, `M3U2/cloacal.csv/.dxe`, `M2-U1/CARP01-05.dxe`.

## 4. Qué parte de la wiki alimenta

| # | Destino | Acción |
|---|---|---|
| 1 | `wiki/glosario/software/autocad` | actualizar § bloques con atributos + DATAEXTRACTION |
| 2 | `wiki/glosario/conceptos/computo-presupuesto-utn` | crear — índice planillas M1-M4 |
| 3 | `wiki/glosario/software/freecad` | enlazar alternativa open (ver raw/research freecad-mep) |
| 4 | `activos/libreria-mep-ar/01_dwg-atributos/` | crear librería física DWG |

## 5. Referencias locales verificadas

- `D:\Users\Solch\Desktop\ESTUDIO.AR\CAPACITACION PROFESIONAL\UTN-ComputosYPresupuestos\Programa Experto Universitario en Cómputos y Presupuestos.pdf`
- `M3_U1_-_INST_DE_AGUA.pdf`, `M3_U2_-_Desagues_Cloacales.pdf`, `M3_U2_-_Desagues_Pluviales.pdf`, `M3_U4_Instalacion_electrica.pdf`
- `BIBLIOGRAFIA/Chandias - Cómputos y Presupuestos (CD)`, `Quadri - Instalaciones Sanitarias.pdf`, `Quadri-instalaciones-electricas-en-edificios.pdf`

## 6. Próximo paso

1. Elijo piloto: M3U2 cloacal (tenés 24 bloques Duratop + planilla 17a) + M3U4 eléctrica (plano + planilla 20).
2. Normalizo esos 2 a ATTDEF estándar y corro DATAEXTRACTION → XLS.
3. Replico a agua + mampostería + terminaciones.

¿Avanzo a normalizar piloto cloacal+eléctrica? `s/N`
