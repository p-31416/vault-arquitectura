---
tipo: plan-tecnico
fecha_creacion: 2026-07-02
tags: [plan, tecnico, calculadora, honorarios]
---

# Plan Técnico — Calculadora de Honorarios

Estructura y decisiones de implementación del MVP generado desde Google AI Studio.

## Arquitectura

```
[FeeCalculator.tsx] ← slider + resultados
        |
        v
[App.tsx] ← estado global (squareMeters, marketData)
        |
        ├── [Dashboard.tsx] ← market data + charts
        └── [Budget.tsx] ← presupuesto final + PDF
```

### Flujo de datos

1. `App.tsx` monta y llama `getArgentinianMarketData()` → `marketData` (mock con delay 1.2s)
2. `App.tsx` computa `feeData = calculateFee(squareMeters)` via `useMemo`
3. `FeeCalculator` recibe `squareMeters`, `onSquareMetersChange`, `feeData`
4. `Dashboard` recibe `feeData`, `marketData`, `loading`
5. `Budget` recibe `feeData`, `marketData`, `loading`, `squareMeters`

### Lógica de cálculo (`utils/feeCalculator.ts`)

**USD**: Pendiente lineal sobre total fee
- totalFeeAtMin(50m²) = 50 × 25 = 1250 USD
- totalFeeAtMax(300m²) = 300 × 7.78 ≈ 2333 USD
- slope = (2333 - 1250) / (300 - 50) ≈ 4.33
- Para cualquier sqm: `totalFee = slope × sqm + intercept`
- `pricePerSqm = totalFee / sqm`

**Oro**: Piecewise linear sobre total fee
- 4 puntos de control definidos en `GOLD_TOTAL_FEE_POINTS`
- Interpolación lineal entre puntos adyacentes
- `goldPricePerSqm = totalGoldFee / sqm`

### Mock API (`services/marketApi.ts`)

- `getArgentinianMarketData()` → Promise con timeout de 1.2s
- Genera historial sintético de 30 días con volatilidad controlada
- Valores hardcodeados base: Dólar Blue 1440 ARS, Oro 250000 ARS/gr

## Decisiones técnicas

| Decisión | Alternativa | Elegida | Motivo |
|----------|------------|---------|--------|
| Charts | Recharts / Chart.js | SVG nativo | Sin dependencias extra, control total |
| PDF | Print-to-PDF browser | jsPDF | Formato más profesional y portable |
| Estado | Redux / Zustand | useState + useMemo | Suficiente para la complejidad actual |
| API mercado | Real (dolarsi, bluelytics) | Mock data | MVP sin backend; mock reemplazable 1:1 |
| Persistencia | backend / IndexedDB | localStorage | Simple, sin servidor |

## Próximos pasos técnicos

1. Conectar API real de Dólar Blue (ej. `https://api.bluelytics.com.ar/v2/latest`)
2. Conectar API real de oro (ej. cotización del Banco Central o datos abiertos)
3. Agregar factor de ajuste por tipo de gestión y complejidad
4. Migrar a la estructura final dentro del vault si la app evoluciona
5. Agregar tests con Vitest
