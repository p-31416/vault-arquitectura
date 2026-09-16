# Esquema de pagos — Presupuesto cliente

Regla general (versión cliente): **el número de pagos = etapas seleccionadas + 1**. Los pagos se calculan sobre el monto de las etapas incluidas (`montoEtapas`).

## Regla general

| Etapas seleccionadas | Cant. de pagos | Desglose |
|---|---|---|
| 1 | 2 | 60% adelanto · 40% contra entrega de la documentación |
| 2 | 3 | 40% encargo (antes de la 1.ª etapa) · 30% en la reunión intermedia (análisis de variantes) · 30% contra entrega de la documentación |
| 3 | 4 | 25% c/u |
| 4 | 5 | 20% c/u |
| 5 | 6 | 16,7% c/u |

## Cómo se etiquetan los pagos (3 o más etapas)

- **Pago 1:** `Encargo (antes de {primera etapa})`.
- **Pagos intermedios:** `Antes de {etapa N}` (uno por etapa restante).
- **Pago final:** `Contra entrega de la documentación`.

Ejemplo con 3 etapas (*Croquis preliminares, Croquis avanzados, Anteproyecto*):

1. Encargo (antes de Croquis preliminares) — 25%
2. Antes de Croquis avanzados — 25%
3. Antes de Anteproyecto — 25%
4. Contra entrega de la documentación — 25%

## Notas

- El monto de cada pago = `montoEtapas × pct`, redondeado a pesos.
- Si no hay etapas seleccionadas (caso "Etapa completa"), se usa el esquema de 1 etapa (60/40).
- Este esquema aplica a la sección **Modalidad de pago** del PDF. La línea de tiempo en **NOTAS** muestra los montos por etapa (honorario parcial) y los hitos de reunión/entrega.
