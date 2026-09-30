---
tipo: especificaciones
nivel: n02
nombre: mcp_test_local
fecha_creacion: 2026-09-29
ultima_actualizacion: 2026-09-29
tags: [especificaciones, hipotesis, mcp, lenguaje-natural, n02]
idioma: es
---

# Especificaciones — Hipótesis operacionalizada

> `01-spec` responde **¿qué logramos?**. Operacionaliza la hipótesis del manifiesto
> y declara por anticipado qué se mide y cómo se califica cada resultado.
>
> Rige para todo el nivel. Si el experimento pide cambiar una regla, primero se actualiza
> este spec.

---

## Hipótesis — formulación en positivo

Lenguaje en positivo: cada enunciado afirma valor creado y posibilidad abierta.
Se evita la negación frontal y se describe lo que la hipótesis incluye, avanza y abre.

|  | Enunciado en positivo |
|---|---|
| **H-base** | El flujo por lenguaje natural vía LLM + MCP incluye potencial para completar un plano de arquitectura mediante reglas descomponibles en pasos métricos pequeños, con verificación que consolida cada avance. |
| **H1 (riqueza)** | El prompt enriquecido con contexto de proyecto (unidad en metros, capas `A-`, espesores) avanza hacia menor error geométrico y menor esfuerzo correctivo en cada paso. |
| **H2 (incremental)** | La concatenación incremental incluye oportunidad de deriva acumulada que queda contenida mediante consolidación geométrica entre pasos. |
| **H3 (trazabilidad)** | El uso de capas `A-` con prefijo arquitectura incluye trazabilidad por disciplina y queda verificable por `query_entities` en cada paso. |

H2 incluye la predicción que matiza la hipótesis original: si la deriva aparece, el framework suma un paso de consolidación; el resultado sigue aportando valor y orienta el siguiente ciclo.

---

## Descomposición en 7 reglas — plano desglosado

El plano se desglosa en reglas infinitesimales para que el LLM reemplace tareas simples. Unidad del archivo: **metros** (factor MCP: 1 m = 1000 mm en la API).

| Paso | Acción | Capa | Medida | Nota |
|---|---|---|---|---|
| 1 | Polilínea cerrada 4×4 m (interior del local, área de medición) | `A-AREA` | 4.00 m × 4.00 m | `A-AREA` queda como capa de medición, superpuesta al muro interior, con Plot en No (como Defpoints) |
| 2 | Polilíneas de muro: interior + exterior (offset 0.15 m) | `A-MURO` | 0.15 m espesor | Dos polilíneas blancas: interior (0,0)-(4,4) y exterior (-0.15,-0.15)-(4.15,4.15); la interior se superpone a `A-AREA` para medición |
| 3 | Líneas perpendiculares laterales del vano (jambas) | `A-MURO` | 0.15 m largo | Blancas, sobre `A-MURO`, marcan el espesor del muro donde se abre el vano |
| 4 | Copia de una jamba a 0.98 m para conformar el vano (puerta 90) | `A-MURO` | 0.98 m vano | Blancas, distancia 980 mm; vano para hoja 0.90 m + marcos |
| 5 | Mesa en centro geométrico | `A-MOB` | 0.80×0.80 m | Centroide (2.00,2.00) m del interior, geometría simple luego bloque |
| 6 | Bloques de carpintería en vanos | `A-CARP` | vano 0.98 m + ventanas | Bloque `PUERTA BATIENTE` (46 ent.) + hoja roja 0.90 m a 90° interior en vano sur; 2× `VENTANA BAJA SIMPLE` (14 ent.) en paredes Y (este/oeste) en y=2000, con atributos visibles ALFEIZAR 0.90 ALTO 1.20 TIPO DVH Mock ANCHO 1.50 |
| 7 | Etiqueta de local como MText + atributo de área | `A-AREA` | centro (2,2) m | MText `MC` (Middle Center) con campo Field linkeado al área de la polilínea `A-AREA` |

Cada paso queda documentado en [[proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/03-log-n_02|03-log-n_02]] con su ficha individual. El log incluye explicación paso a paso apta para dummies y referencia a documentación oficial de Autodesk.

Herramienta en todos los pasos: MCP `autocad` (`autocad_draw_polyline`, `autocad_create_layer`, `autocad_draw_line`, `autocad_copy_entity`, `autocad_insert_block`, `autocad_query_entities`, `autocad_capture_screenshot`, `autocad_set_entity_layer`, `autocad_draw_text`).

Bloques disponibles en `ia-cad-test.dwg`: `PUERTA BATIENTE` (46 ent.) y `VENTANA BAJA SIMPLE` (14 ent.), verificados vía `list_blocks`.

---

## Capas — prefijo A- arquitectura

Todo pertenece a arquitectura (`A-`). Capas creadas vía `autocad_create_layer` antes de dibujar.

| Capa | Uso | Color ACI | Tipo de línea | Espesor | Plot |
|---|---|---|---|---|---|
| `A-MURO` | Muros: 2 polilíneas (interior + exterior) + jambas blancas del vano | 7 (blanco) | Continuous | 0.30 mm | Sí |
| `A-CARP` | Carpinterías: puerta, ventana, hoja roja | 1 (rojo) | Continuous | 0.18 mm | Sí |
| `A-MOB` | Mobiliario: mesa 0.80×0.80 | 3 (verde) | Continuous | 0.13 mm | Sí |
| `A-AREA` | Área de medición: polilínea 4×4 + MText local + campo área | 5 (azul) | Continuous | 0.09 mm | No (como Defpoints) |
| `A-TERRENO` | Entorno existente (histórico del DWG) | — | — | — | — |

`A-AREA` queda con `Plottable = No` (columna Plot desmarcada en Layer Properties, idem `Defpoints`): mide y porta el campo de área, permanece visible en pantalla y queda excluida de la impresión.

---

## Texto y campo de área

- **MText:** objeto multiline con justificación `MC` (Middle Center) en el centro geométrico (2.00,2.00) m del interior. Ancho de caja = 4 m, altura 0.15 m, estilo Standard, capa `A-AREA`. Documentación: `MTEXT` con `Justify MC` — https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-F94BE932-DA31-437E-9610-27F46ACD5711
- **Campo de área:** Field linkeado a la polilínea `A-AREA` (handle 2F1) → Propiedad `Area` → formato `m²` con factor `1e-06` (mm²→m²) y precisión 2 decimales. Inserción vía `Insert Field → Object → Area`. El campo se actualiza con `REGEN` / `FIELDEVAL`. Texto resultante: `LOCAL 4×4 — 16.00 m²` donde `16.00` es campo.
  - Cálculo de área y fields: https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-18389CD1-2F81-4185-A459-F59AE311D637
  - Propiedad Area (ActiveX): https://help.autodesk.com/view/OARX/2026/ENU/?guid=GUID-2D31D8C1-9BEC-48CF-8B73-E2AD38A08D74
  - Insertar field en texto: https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-F613CBDA-5899-4419-9C23-2E0F6C76BB99
- Implementación inicial (geometría simple): `autocad_draw_text` como placeholder centrado; la versión MText MC + field queda para consolidación con ventana restaurada y queda documentada en `02-ft`.

---

## Variables

### Independientes

|  | Valores |
|---|---|
| `VI1` Riqueza de contexto | `C0` NL crudo · `C1` NL + contexto (metros, capas, medidas) · `C2` NL + contexto + vocabulario de dominio |
| `VI2` Tipo de tarea | `T1` primitiva (paso 1) · `T2` compuesta (pasos 2–4 vano) · `T3` incremental (pasos 5–7 equipamiento y bloques) |

### Dependientes

| Métrica | Definición operativa | Unidad |
|---|---|---|
| `VD1` Error posicional | RMSE entre vértices dibujados y referencia nominal | mm |
| `VD2` Completitud | Entidades correctas / esperadas por paso | % |
| `VD3` Adherencia de capa | Entidades en capa esperada / totales del paso | % |
| `VD4` Esfuerzo correctivo | Intervenciones humanas por paso | count |
| `VD5` Reproducibilidad | Desviación entre 3 repeticiones del mismo prompt | % |

### Controladas

AutoCAD 2027 (build fijo) · plantilla métrica en metros · AutoLISP aislado (aisla MCP de `LOC`) · mismo modelo y temperatura del LLM · documento `ia-cad-test.dwg` · orden fijo pasos 1→7.

La referencia es la geometría nominal declarada en la ficha de cada paso, con conversión explícita metros→mm para la API.

---

## Criterios de calificación (régimen laxo, en positivo)

Cada paso se califica en la bitácora con etiqueta en positivo:

| Etiqueta | Lectura en positivo |
|---|---|
| `AVANZA` | El paso incluye mejora apreciable en la dirección predicha |
| `QUEDA PARA SIGUIENTE CICLO` | El paso incluye oportunidad de ajuste y queda para iteración siguiente |
| `APORTA EVIDENCIA MIXTA` | El resultado incluye evidencia mixta y requiere medición adicional |

Guía orientativa:

- **H1**: avanza cuando el error y las correcciones muestran mejora visible entre `C0` y `C1`. Un factor cercano a 2× orienta.
- **H2**: incluye deriva visible cuando el desvío acumulado resulta perceptible tras cuatro pasos incrementales (orden de 1 mm orienta, con unidad en metros = 0.001 m).

Ajustar un criterio después de ver el resultado se anota en el log como `POST-HOC` y queda para el siguiente ciclo de refinamiento.

---

## Serie experimental — mapeo a los 7 pasos

| Exp | Pasos | Qué se prueba | Predicción en positivo |
|---|---|---|---|
| **00** | 1 | Calibración: polilínea 4×4 en `A-AREA` | El instrumento incluye precisión por debajo de 0.1 mm |
| **01** | 1 | NL crudo *Dibujá un rectángulo de 4×4 m* | El paso aporta el dato basal y orienta el contexto siguiente |
| **02** | 2 | Offset 0.15 m en `A-MURO` (2 polilíneas blancas) | El contexto de proyecto avanza hacia el offset correcto |
| **03** | 3–4 | Vano 0.88 m en `A-MURO` (jambas blancas) | El vano incluye topología que queda verificable |
| **04** | 5–6 | Mesa en centroide + puerta `PUERTA BATIENTE` | El equipamiento incluye posicionamiento centrado |
| **05** | 7 | Etiqueta MText MC + campo área + vetana | El bloque local incluye identificación y área linkeada |

---

## Compuerta de verificación

Toda salida de este nivel incluye material de trabajo. El paso a documento registral incluye lectura humana de cotas, capas y posición con planilla firmada. `VD4` mide cuánta verificación acompaña cada salida.

---

## Trazabilidad

| Fecha | Qué cambió | Quién |
|---|---|---|
| 2026-09-29 | Creación. Hipótesis en régimen laxo | asistente |
| 2026-09-29 | Reformulación en positivo + descomposición en 7 pasos + capas A-MURO/A-CARP/A-MOB/A-AREA + unidad metros | asistente |
| 2026-09-29 | Detalles: A-AREA no imprimible, muro con 2 polilíneas blancas, MText MC + Field área, jambas blancas en A-MURO, bloques PUERTA y VENTANA | asistente |

## Referencias

- [[proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/00-filo-n_02|00-filo-n_02]] — problema e hipótesis
- [[proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/02-ft-n_02|02-ft-n_02]] — procedimiento paso a paso dummies
- [[proyectos/MVP_01-dibujo_ia/n_02-mcp_test_local/03-log-n_02|03-log-n_02]] — bitácora por paso
- [[proyectos/MVP_01-dibujo_ia/n_01-local/01-spec-n_01|n_01-local / 01-spec-n_01]]
- Autodesk Help — PLINE, OFFSET, COPY, MTEXT MC, FIELD Area, INSERT (ver 02-ft para URLs)
