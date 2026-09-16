---
tipo: readme
fecha_creacion: 2026-07-02
tags: [readme, calculadora, honorarios, mvp]
---

# MVP_03 — CalHon Gest — Honorarios de Gestiones

> **CalHon-Gest** — Calculadora web para estimar honorarios de **gestión municipal** (tramitación TAD GCBA) de proyectos residenciales, con cotización en USD y gramos de oro, datos de mercado actualizados (Dólar Blue, oro) y exportación a PDF. Ver también [[proyectos/MVP_03b-calhon-pdo/readme-mvp_03b|MVP_03b — CalHon PyDO]] para Proyecto y Dirección de Obra.

## Stack

| Capa | Tecnología |
|------|-----------|
| Frontend | React 19 + TypeScript |
| Build | Vite 6 |
| Charts | SVG nativo (React) |
| Market data | Mock API (simula Dólar Blue + oro) |
| PDF export | jsPDF |
| Origen | Generado en Google AI Studio (Gemini) |

## Archivos del proyecto

| Archivo | Propósito |
|---------|-----------|
| `readme-mvp_03.md` | **← Este archivo — puerta de entrada** |
| `00-filo-mvp_03.md` | Manifiesto: por qué una calculadora de honorarios |
| `01-spec-mvp_03.md` | Especificaciones: qué calcula, rangos, fórmulas |
| `02-ft-mvp_03.md` | Plan técnico: estructura del código, decisiones |
| `03-log-mvp_03.md` | Bitácora de desarrollo |

## Repositorio

El código fuente vive en: [github.com/p-31416/arch_fee_gest](https://github.com/p-31416/arch_fee_gest)

```
git clone https://github.com/p-31416/arch_fee_gest.git
cd arch_fee_gest
npm install
# Crear .env.local con GEMINI_API_KEY
npm run dev
```

## Estado

- ✅ App funcional generada desde AI Studio
- ⏳ Pendiente: integrar datos reales de mercado, validar curva de honorarios con la práctica real del estudio
