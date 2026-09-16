---
tipo: readme
fecha_creacion: 2026-08-10
ultima_actualizacion: 2026-09-08
tags: [readme, calculadora, honorarios, mvp, cpau, pdo]
---

# MVP_03b — CalHon PyDO — Proyecto y Dirección de Obra

> **CalHon-PyDO** — Calculadora web de **honorarios por Proyecto y Dirección de Obra** según arancel CPAU (Cuadro 5 + Cuadro 6 + Art. 3.18). Calcula **Monto de Obra (M)**, **honorario base** y **por etapas**, con tipologías Clarín ARQ y exportación a PDF en dos versiones (estudio/cliente). Complementa a [[proyectos/MVP_03-calhon-gest/readme-mvp_03|MVP_03 — CalHon Gest]] (gestiones municipales).

## Qué calcula

| Input | Fuente | Output |
|-------|--------|--------|
| `M = precio/m² × superficie` | Tipologías Clarín ARQ (`src/data/clarin.ts`) + edición manual | Monto de obra |
| Grupo 1/2/3 + Rango A/B/C/D | Cuadro 5 CPAU (`src/data/cpau.ts`, `K = 640.069.857,62` ICC junio 2026) | `H = coefM×M + coefK×K` |
| Toggle remodelación | Art. 3.18 (+40% sobre honorarios) | Honorario total |
| Etapas Cuadro 6 | Art. 3.14 (6 etapas: croquis → dirección) | Parcial/acumulado por etapa + presupuesto de etapa |

## Stack

| Capa | Tecnología |
|------|-----------|
| Frontend | React 19 + TypeScript + Vite 8 |
| PDF | jsPDF 4.x (doble versión estudio/cliente) |
| Datos | `src/data/cpau.ts` (K, GRUPOS, ETAPAS), `src/data/clarin.ts` (18 rubros) |
| Lógica | `src/lib/honorarios.ts` (`calcularHonorario`, `estimarMonto`), `src/lib/presupuesto.ts` |
| Persistencia | localStorage (tipología) + `presupuestos/` vía plugin dev server |

## Archivos del proyecto

| Ruta | Propósito |
|------|-----------|
| `readme-mvp_03b.md` | ← Este archivo — puerta de entrada |
| `docs/0-INDEX.md` | Guía de docs (ADR/FEATURES/CHANGELOG/PAGOS) |
| `docs/ADRs.md` | Decisiones de diseño (0001-0009) |
| `docs/FEATURES.md` | Inventario de funcionalidades |
| `docs/CHANGELOG.md` | Historial cronológico |
| `docs/PAGOS.md` | Esquema de pagos por etapas |
| `codigo/` | App Vite (src, plugins, public) |
| `CUADROS-ICC-JUNIO-2026.pdf` | Referencia CPAU escaneada |
| `kiosco.clarin.com_arq.pdf` | Referencia Clarín ARQ |

## Origen

Migrado desde `P:\devs\CalHon\` (2026-08-10 → 2026-09-08) al vault como **MVP_03b**. El original sigue en `P:\devs\CalHon\` como respaldo; el vault es la copia canónica.

```
# Instalación
cd proyectos/MVP_03b-calhon-pdo/codigo
npm install
npm run dev      # → http://localhost:5173  (PyDO)
# Gest sigue en MVP_03-calhon-gest/codigo → :5174
```

## Estado

- ✅ Cálculo CPAU completo (Cuadro 5 + 6) funcional
- ✅ Tipologías Clarín + discriminación por rubros (Modelo 11)
- ✅ Remodelación + etapas + PDF doble versión + vista previa + guardado en `presupuestos/`
- ⏳ Pendiente: actualizar `K` mensual (ICC), validar `PAGOS.md` con contabilidad del estudio
