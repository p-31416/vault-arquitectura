---
tipo: log
fecha_creacion: 2026-07-02
tags: [log, calculadora, honorarios, iteraciones]
---

# Bitácora — Calculadora de Honorarios

## 2026-07-02 — MVP creado desde Google AI Studio

- App generada con AI Studio (Gemini) a partir de prompt de Sol
- Repo exportado a `github.com/p-31416/arch_fee_gest` (público)
- Documentación del MVP creada en el vault
- La app tiene mock data para mercado; pendiente reemplazar con APIs reales
- Curvas de honorarios USD y Oro definidas; falta validar con práctica real del estudio
- Componentes: FeeCalculator, Dashboard, Budget, SavedBudgets, charts SVG
- Pendiente: tests, responsive, factor de complejidad

## 2026-07-02 — Migración a APIs reales + CPAU medición

- **marketApi.ts**: reemplazado mock por Bluelytics API (dólar blue + oficial)
- **gold-api.com**: integrado para spot internacional USD/oz → ARS/gramo
- **Ajuste local %**: campo editable en Dashboard para calibrar precio retail del oro
- **Historial real**: snapshots diarios en localStorage, sin mock. Chart siempre visible
- **CPAU medición**: fórmula Cuadro 8 "muy compartimentada" implementada
- **Types extendidos**: `MediciónResult`, `ServiceOptions`, `gold24k`, `services` en SavedBudget
- **Dashboard**: 3 cards (Blue, Oficial, Oro), chart con 3 líneas dinámicas
- **FeeCalculator**: slider + input manual, checkboxes servicios, desglose CPAU
- **Budget**: desglose por servicio, total con/sin medición, PDF completo
- **Auto-refresh**: mercado cada 1 hora, snapshot diario en localStorage
- **vite.config**: simplificado (sin host 0.0.0.0, sin importmap AI Studio)
- Build exitoso, sin errores de compilación
