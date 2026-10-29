---
tipo: proyecto
cliente: Estudio (interno)
proyecto: 01-AIZ — cortes AutoCAD → Rhino
ciudad: —
pais: Argentina
fase: experimento
area_m2: s/d
fecha_inicio: 2026-10-25
fecha_estimada_entrega: s/d
equipo: [investigacion: Sol, modelado: s/d]
estado: activo
tags: [mvp_05, rhino8, autocad, aiz, cortes, dwg, make2d, layout, comparativa]
idioma: es
---

# 01-AIZ — Cortes en Rhino desde un modelo de AutoCAD

> Experimento 1 del MVP_05. Pregunta central: **¿un modelo 3D hecho en AutoCAD sirve para producir cortes en Rhino, o conviene remodelar?**
>
> El caso AIZ es un referente: el 3D nace de un PDF vectorizado, se modela a mano en AutoCAD y hoy se pasa a Rhino como planta 2D. Acá probamos el paso siguiente: usar ese 3D para cortar.

---

## 1. Pregunta y alcance

**Pregunta:** ¿se pueden hacer cortes generales y cortes constructivos en Rhino a partir del modelo 3D de AutoCAD de AIZ?

**Alcance de esta fase:**

- Importar el DWG 3D de AIZ en Rhino.
- Producir un corte general a 1:50 y un corte-detalle a 1:10 o 1:20.
- Comparar el resultado con el mismo corte hecho en AutoCAD.
- Medir ventajas, fricciones y tiempos.

**Fuera de esta fase:** modelado completo de la casa, renders, instalaciones, cálculo estructural y lámina final de entrega.

---

## 2. Material de partida

| Insumo | Formato | Ubicación |
|---|---|---|
| Modelo AIZ en AutoCAD | `.dwg` 3D | `activos/mvp_05-rhino-mcp/01-AIZ/` |
| PDF vectorizado de origen | `.pdf` | `activos/mvp_05-rhino-mcp/01-AIZ/` |
| Plantas 2D de referencia | `.dwg` / `.pdf` | `activos/mvp_05-rhino-mcp/01-AIZ/` |
| Protocolo, corte, hatch y hoja A3 1:50 | `.md` | [[proyectos/MVP_05-rhino-mcp/01-AIZ/01-playbook-cortes-rhino-8\|01-playbook-cortes-rhino-8]] |

> Los binarios viven en `activos/` (gitignored). En el vault solo se referencian por ruta.

---

## 3. Hipótesis

1. **Sí, si el DWG tiene sólidos 3D cerrados.** Rhino importa los sólidos ACIS de AutoCAD como polysuperficies cerradas y puede cortarlos con `ClippingPlane`, `ClippingSections` y `Make2D`.
2. **El corte general 1:50 sale rápido.** A esa escala, un modelo de masa con espesores de conjunto alcanza para leer espacios, alturas y encuentros.
3. **El corte constructivo 1:10 exige capas separadas.** Si el modelo de AutoCAD es un sólido único por muro, el hatch por material se resuelve partiendo el sólido o remodelando un testigo en Rhino.
4. **La ventaja grande de Rhino está en la sección dinámica y en la lámina.** `Section Style` por capa, `Make2D` con líneas ocultas y `Layout` con detalles a distinta escala en una sola hoja.

---

## 4. Protocolo

Todo el trabajo con Rhino 8 vive en **un solo documento**: [[proyectos/MVP_05-rhino-mcp/01-AIZ/01-playbook-cortes-rhino-8|01-playbook-cortes-rhino-8]]. Reúne el protocolo de preparación desde AutoCAD, el manual de corte 3D con hatch por material y el plan de la hoja A3 a 1:50, con el estado verificado del archivo y las lecciones de API.

Resumen:

1. **Preparar el DWG** — copia limpia, `AUDIT`, `PURGE`, xrefs bindeadas, unidades verificadas.
2. **Importar a Rhino** — template en metros, control de escala, conteo de sólidos y mallas.
3. **Corte de masa** — un plano delimitador y `ClippingSections` para ver el alcance real.
4. **Corte constructivo** — capas por material, `Section Style` y hatch; testigo si hace falta.
5. **Lámina** — `Make2D`, `Layout` A3, detalles 1:50 y 1:10, PDF vectorial.
6. **Comparación** — el mismo corte en AutoCAD con `SECTIONPLANE`, `SECTION` y `FLATSHOT`.

---

## 5. Criterio de decisión (go / partial / no-go)

| Resultado | Condición | Decisión |
|---|---|---|
| **GO** | ≥80 % del área del corte proviene de sólidos cerrados; los hatches funcionan; la limpieza lleva ≤30 min | Usar el DWG de AutoCAD como base y cortar en Rhino |
| **PARTIAL** | El modelo sirve como masa, pero las capas no están separadas | Usar AutoCAD para 1:50 y modelar el testigo 1:10 en Rhino |
| **NO-GO** | El DWG trae mallas o superficies abiertas; el corte no cierra | Remodelar en Rhino desde el PDF vectorizado |

---

## 6. Rhino vs AutoCAD para cortes

| Criterio | AutoCAD | Rhino 8 | Lectura |
|---|---|---|---|
| Corte dinámico | `SECTIONPLANE` | `ClippingPlane` + `ClippingSections` | Ambos; Rhino suma estilos |
| Hatch por material | Manual, después de generar la sección | `Section Style` por capa u objeto | **Rhino** |
| Líneas ocultas | `FLATSHOT` | `Make2D` | **Rhino** |
| Varios detalles a escalas distintas | Layouts con viewports | `Layout` + `Detail` | **Rhino** |
| Edición del modelo | Sólidos ACIS nativos | Breps importados | Empate |
| Precisión y booleanas | Sólidos ACIS | NURBS y polysuperficies | **Rhino** |
| Dibujo 2D puro | Nativo y rápido | Correcto, con más pasos | **AutoCAD** |
| Interoperabilidad | DWG nativo | Importa y exporta DWG | **AutoCAD** |
| Curva de aprendizaje | Conocida por el estudio | Nueva | **AutoCAD** |
| PDF vectorial | `EXPORTPDF` / `PLOT` | `Print` → Rhino PDF | Empate |

**Conclusión provisoria:** AutoCAD sigue siendo el lugar del modelo 3D base y del dibujo 2D; Rhino aporta el corte dinámico, el hatch por material y la lámina. La prueba define si el modelo de AIZ alcanza o si hay que remodelar el testigo.

---

## 7. Entregables de la fase

| # | Entregable | Formato | Criterio |
|---|---|---|---|
| 1 | DWG limpio de AIZ | `.dwg` | Sin xrefs sueltas, unidades verificadas |
| 2 | Modelo importado | `.3dm` | Sólidos cerrados, capas mapeadas |
| 3 | Corte general A-A | En lámina | 1:50, legible |
| 4 | Corte-detalle D-1 | En lámina | 1:10 o 1:20, con hatch por material |
| 5 | Lámina de prueba | `.pdf` A3 | Vectorial, rótulo mínimo |
| 6 | Planilla comparativa | En este índice o anexo | Tiempos, fricciones, veredicto |

---

## 8. Riesgos

| Riesgo | Mitigación |
|---|---|
| El DWG trae mallas en lugar de sólidos | Verificar con `SelMesh` y `What` antes de cortar |
| El modelo está en milímetros | Verificar con `Units` y `Distance` contra una cota conocida |
| Un solo sólido por muro | Partir con `BooleanSplit` o modelar el testigo en Rhino |
| Xrefs sin bindear | `XREF` → Bind, o `WBLOCK` del área |
| El hatch no aparece | Cada capa debe ser un sólido cerrado y tener `Section Style` asignado |
| El PDF sale con escala incorrecta | Medir una cota de 1,00 m impresa en el PDF |

---

## 9. Próximo paso

1. Dejar el DWG de AIZ en `activos/mvp_05-rhino-mcp/01-AIZ/`.
2. Confirmar si el modelo es de masa o tiene capas por material.
3. Ejecutar el protocolo con el puente MCP abierto y aprobación paso a paso.
4. Registrar tiempos y veredicto en este documento.

> **Estado:** puente MCP operativo (script relanzado dentro de Rhino 8, puerto 9876 escuchando). Archivo `set-ej_corte.3dm` inspeccionado y medido: 159 mallas, 7 capas de material, clipping plane `A-A` en X = 575 sin Custom Depth, viewports `axo3060`/`Top`/`Front`/`Right` en paralelo. **Hoja A3 a 1:50 construida y verificada** (1,00 m = 20,0 mm medidos): detalle, corte y pie de hoja en [[proyectos/MVP_05-rhino-mcp/01-AIZ/01-playbook-cortes-rhino-8|01-playbook-cortes-rhino-8]], parte 5. Quedan pendientes: los hatches de las 4 capas sin estilo, el Custom Depth, la malla abierta y la impresión del PDF.
