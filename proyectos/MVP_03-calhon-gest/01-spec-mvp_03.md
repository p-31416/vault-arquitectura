---
tipo: especificaciones
fecha_creacion: 2026-07-02
ultima_actualizacion: 2026-07-02
tags: [especificaciones, calculadora, honorarios, residencial, vivo]
---

# Especificaciones — Calculadora de Honorarios

Documento VIVO. Refleja el estado actual del MVP.

## ⚠️ Corrección de scope

La app generada en AI Studio es genérica. La versión real del estudio debe reemplazar por completo la lógica de cálculo. Lo que sigue es la especificación **real del estudio**.

## Alcance del negocio

**Esta calculadora es exclusivamente para GESTIONES RESIDENCIALES.** No aplica a:
- Habilitaciones comerciales
- Proyectos de gran escala
- Obras de infraestructura
- Regularizaciones dominicales

### Servicios ofrecidos

El estudio ofrece estos **items facturables**, cada uno opcional según el proyecto:

| Item | Tipo | Fórmula / Base | Descripción |
|------|------|----------------|-------------|
| **TRAMITACIÓN y GESTIÓN** | Base | Curva USD propia del estudio (decreciente por m², total creciente) | Procesamiento y seguimiento municipal. Incluye: adaptar planos a normativa municipal, armar carátulas, cuadros, detalles mínimos, carga y seguimiento en **TAD GCBA** |
| **MEDICIÓN / REPLANTEO** | Adicional | CPAU Cuadro 8 — muy compartimentada | Medición de construcción existente para replanteo |
| **DIGITALIZACIÓN ANTECEDENTE ARQ** | Adicional | ⏳ Pendiente de definir | Digitalización de antecedentes arquitectónicos |
| **PROYECTO POR OTRO PROFESIONAL** (adaptación a norma) | Adicional | A definir | Cuando el anteproyecto viene de arquitecto externo: corrección de errores, omisiones, y adaptación a normativa municipal. Se cobra aparte de la gestión. |

### Servicios NO incluidos

- ❌ Proyecto arquitectónico desde cero
- ❌ Anteproyecto original
- ❌ Croquis
- ❌ Cálculo de instalaciones (el arquitecto del proyecto las envía)
- ❌ Dirección de obra

### Flujo de trabajo

1. El **arquitecto del proyecto** envía: planos de arquitectura + instalaciones
2. El **estudio** (nosotros) recibe, revisa, adapta a normativa municipal (cubre **adaptación de anteproyecto externo** si aplica)
3. Si no hay planos → se hace **medición/replanteo** in situ
4. Se digitalizan antecedentes (**digitalización** si aplica)
5. Se arman planos municipales: carátulas, cuadros, detalles
6. Se presenta y sigue en **TAD GCBA** hasta aprobación

### Referencia CPAU — Medición / Replanteo (Cuadro 8)

**K = 623.849.763,77** (ICC Mayo 2026 — se actualiza mensualmente)

| Tipo | Fórmula |
|------|---------|
| Medición solo superficie (sin planos) | `0.000006 × K × S` |
| Poco compartimentada | `0.000010 × K × S` |
| **Muy compartimentada** (usamos esta) | |
| └ hasta 50 m² | `0.000004 × K × S + 0.0003 × K` |
| └ **51 a 500 m²** | **`0.000006 × K × S + 0.0003 × K`** |
| └ 501 a 2.500 m² | `0.000003 × K × S + 0.0018 × K` |
| └ más de 2.500 m² | `0.0000015 × K × S + 0.00555 × K` |

> Ejemplo 100 m²: 0.000006 × 623.849.763,77 × 100 + 0.0003 × 623.849.763,77 = $374.309,86 + $187.154,93 = **$561.464,79**

### Honorario base — Tramitación y Gestión

Es la **curva USD propia del estudio** (la generada en AI Studio y validada por Sol). Ver `constants.ts` para los puntos de control. Se expresa en USD (conversión a ARS vía Dólar Blue) y decrece por m² mientras el total crece.

## Scope funcional (MVP)

### Inputs

| Parámetro | Tipo | Rango / Opciones | Descripción |
|-----------|------|-------------------|-------------|
| Superficie (m²) | number | 50 — 300 | Metros cuadrados del proyecto |
| Incluye medición/replanteo | boolean | sí / no | Adicional CPAU |
| Incluye digitalización | boolean | sí / no | Adicional por m² |
| Incluye adaptación anteproyecto externo | boolean | sí / no | Adicional |

### Outputs

| Output | Unidad | Nota |
|--------|--------|------|
| Tramitación y gestión | ARS (y USD ref.) | Curva propia del estudio |
| Medición / Replanteo | ARS | Fórmula CPAU Cuadro 8 |
| Digitalización antecedente ARQ | ARS | Por m² |
| Adaptación anteproyecto externo | ARS | A definir |
| **Total estimado** | ARS | Suma de items seleccionados |
| Desglose en PDF | Documento | Exportable |

### Dashboard de mercado

| Indicador | Fuente actual | Prioridad |
|-----------|---------------|-----------|
| Dólar Blue (venta) | Mock → API real | Alta |
| Dólar Blue (compra) | Mock → API real | Media |
| Oro (precio por gramo) | Mock → API real | Media |
| CPC/ICC (CPAU) | Tabla manual → scraping | Alta |

### Presupuesto

- Nombre de gestión (input libre)
- Tipo de gestión (obra nueva / ampliación / regularización)
- Fecha y superficie cotizada
- Desglose: base + adicionales
- Exportación a PDF

### Persistencia

- Presupuestos guardados en localStorage
- Exportable a PDF para enviar al cliente

## Stack técnico

| Capa | Tecnología |
|------|-----------|
| UI | React 19 + TypeScript |
| Bundler | Vite 6 |
| Charts | SVG inline (sin librerías externas) |
| PDF | jsPDF (vía CDN o npm) |
| Datos mercado | Mock → API real (bluelytics / datos.gob.ar) |
| Persistencia | localStorage |

## Archivos del código (generado por AI Studio)

```
├── App.tsx                  ← Orquestador, tabs, layout
├── FeeCalculator.tsx        ← Slider + resultados USD/Oro
├── Dashboard.tsx            ← Market data + charts históricos
├── Budget.tsx               ← Presupuesto final + PDF export
├── constants.ts             ← MIN_SQM, MAX_SQM, curvas
├── types.ts                 ← Interfaces
├── utils/feeCalculator.ts   ← Lógica de cálculo
├── services/marketApi.ts    ← Mock de API de mercado
└── components/              ← Charts, header, saved budgets
```

> ⚠️ Esta estructura es el **punto de partida**. La lógica de cálculo debe reescribirse completamente para reflejar los valores reales del estudio.

## Fórmulas implementadas

### Honorario base — Tramitación y Gestión (curva USD)

**Tipo de función:** lineal en el total, hiperbólica decreciente en el precio por m².

**Ecuación general:**

```
Total_USD(S) = m · S + b       [función lineal]
Precio_m2_USD(S) = m + b/S    [función racional decreciente]
```

**Parámetros fijos del estudio (definidos en constants.ts):**

| Parámetro | Símbolo | Valor | Unidad |
|-----------|---------|-------|--------|
| Superficie mínima | S₁ | 50 | m² |
| Superficie máxima | S₂ | 300 | m² |
| Precio en S₁ | P₁ | 25,00 | USD/m² |
| Precio en S₂ | P₂ | 70/9 ≈ 7,78 | USD/m² |

**Cálculo de coeficientes (se resuelve una vez en `feeCalculator.ts`):**

```
Total₁ = S₁ · P₁ = 50 × 25 = 1.250 USD
Total₂ = S₂ · P₂ = 300 × 70/9 ≈ 2.333,33 USD

m = (Total₂ − Total₁) / (S₂ − S₁)
  = (2.333,33 − 1.250) / (300 − 50)
  = 4,3333...    [adimensional]

b = Total₁ − m · S₁
  = 1.250 − 4,3333 × 50
  = 1.033,33...  [USD]
```

**Fórmula final evaluada en runtime:**

```
Total_USD(S) = 4,3333 × S + 1.033,33          [USD]
Precio_m2_USD(S) = 4,3333 + 1.033,33/S       [USD/m²]
```

**Rango de valores (50-300 m²):**

| S (m²) | Precio USD/m² | Total USD |
|--------|---------------|-----------|
| 50     | 25,00         | 1.250     |
| 100    | 14,67         | 1.467     |
| 200    | 9,50          | 1.900     |
| 300    | 7,78          | 2.333     |

**Conversión a ARS:** `Total_ARS = Total_USD(S) × Dólar_Blue_venta`

Para un nuevo par de puntos (ej. habilitaciones comerciales), se cambian P₁ y P₂ en `constants.ts` y la fórmula se recalcula automáticamente.

### Honorario base — Curva Oro (referencia)

**Tipo de función:** lineal por segmentos (piecewise linear) en el total de gramos.

**Ecuación general (para cada segmento i):**

```
Total_oro(S) = m_i · S + b_i       [función lineal por segmento]
Precio_m2_oro(S) = m_i + b_i/S    [función racional por segmento]
```

**Puntos de control definidos por el estudio:**

| Punto | S (m²) | Total_oro (gr) | Precio (gr/m²) |
|-------|--------|---------------|----------------|
| A     | 50     | 9,50          | 0,1900         |
| B     | 100    | 11,00         | 0,1100         |
| C     | 200    | 14,00         | 0,0700         |
| D     | 300    | 16,50         | 0,0550         |

**Segmentos resultantes:**

| Segmento | Pendiente m_i | Ordenada b_i | Fórmula Total_oro(S) |
|----------|--------------|-------------|---------------------|
| 50-100   | 0,030        | 8,000       | 0,030·S + 8,000    |
| 100-200  | 0,030        | 8,000       | 0,030·S + 8,000    |
| 200-300  | 0,025        | 9,000       | 0,025·S + 9,000    |

Notar que los segmentos 50-100 y 100-200 tienen la misma pendiente (la recta es continua).

**Conversión a ARS:** `Total_ARS = Total_oro(S) × Precio_oro_ARS_gr`

Donde `Precio_oro_ARS_gr = (gold_API_USD/oz ÷ 31,1035) × Dólar_Oficial × (1 + ajuste_local%)`

### Medición / Replanteo — CPAU Cuadro 8

**Siempre se usa la categoría "MUY COMPARTIMENTADA"** para gestiones residenciales.

**K = 623.849.763,77** (ICC Mayo 2026 — actualizar mensualmente según CPAU)

| Rango | Fórmula |
|-------|---------|
| hasta 50 m² | `0,000004 × K × S + 0,0003 × K` |
| **51 a 500 m²** (rango típico residencial) | **`0,000006 × K × S + 0,0003 × K`** |
| 501 a 2.500 m² | `0,000003 × K × S + 0,0018 × K` |
| más de 2.500 m² | `0,0000015 × K × S + 0,00555 × K` |

**Ejemplo 100 m²:**
```
0,000006 × 623.849.763,77 × 100 + 0,0003 × 623.849.763,77
= $374.309,86 + $187.154,93
= $561.464,79
```

### Datos de mercado (auto-refresh cada 1h)

| Indicador | Fuente | Conversión |
|-----------|--------|-----------|
| Dólar Blue | `api.bluelytics.com.ar/v2/latest` → `blue.value_sell/buy` | Directo ARS |
| Dólar Oficial | `api.bluelytics.com.ar/v2/latest` → `oficial.value_sell/buy` | Directo ARS |
| Oro 24K spot | `api.gold-api.com/price/XAU` → `price` (USD/oz) | `USD/oz ÷ 31,1035 × Dólar_Oficial × (1 + ajuste_local%)` |
| Ajuste local | Configurable en UI (default 10%) | Calibración a precio retail argentino |

### Historial de precios (persistencia)

- Los 3 indicadores se guardan como **snapshot diario** en `localStorage`
- Sin datos mock — solo datos reales desde el primer día de uso
- El chart se renderiza siempre, los puntos se hacen más pequeños a medida que crece el historial
- Después de ~30 días: historial completo 100% real

## Pendientes conocidos

## Estado actual (02-Jul-2026)

### ✅ Implementado
- Curva USD propia del estudio para honorario base (tramitación y gestión)
- Fórmula CPAU Cuadro 8 "muy compartimentada" para medición/replanteo
- Slider + input manual de m² (rango 50-300)
- Checkbox para medición/replanteo (funcional)
- Checkboxes digitalización y adaptación proyecto externo (placeholder)
- Dólar Blue vía API Bluelytics (real, auto-refresh 1h)
- Dólar Oficial vía API Bluelytics (real, auto-refresh 1h)
- Oro 24K: spot internacional gold-api.com + ajuste local % configurable
- Historial de precios con snapshots diarios en localStorage (sin mock)
- Dashboard con 3 cards y chart de 3 líneas
- Presupuesto con desglose por servicio
- Exportación a PDF con todos los items
- Persistencia en localStorage

### Pendientes
- [ ] **Digitalización antecedente ARQ**: valor por m² pendiente de definir por Sol
- [ ] **Adaptación proyecto externo**: criterio/cálculo pendiente de definir por Sol
- [ ] Agregar selector de tipo de gestión (obra nueva / ampliación / regularización)
- [ ] Mejorar estilos responsive
- [ ] Agregar tests unitarios de la lógica de cálculo
