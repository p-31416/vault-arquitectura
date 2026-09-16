# FEATURES — Inventario de funcionalidades

Lista de lo que la app **hace hoy**. No explica decisiones (eso está en [`ADRs.md`](ADRs.md)) ni el historial (en [`CHANGELOG.md`](CHANGELOG.md)). Ver [`0-INDEX.md`](0-INDEX.md).

**Estados:** `Funcional` · `En desarrollo` · `Pendiente`

**Orden:** de la funcionalidad más reciente (arriba) a la más antigua (abajo).

## Índice

- [Identidad y formato del PDF (logo, Estudio Pi)](#identidad-y-formato-del-pdf-logo-estudio-pi)
- [Presupuesto en dos versiones (estudio y cliente)](#presupuesto-en-dos-versiones-estudio-y-cliente)
- [Vista previa del PDF y guardado en carpeta](#vista-previa-del-pdf-y-guardado-en-carpeta)
- [Exportación a PDF](#exportacion-a-pdf)
- [Modal de datos de obra](#modal-de-datos-de-obra)
- [Persistencia de la tipología elegida](#persistencia-de-la-tipologia-elegida)
- [Presupuesto Clarín discriminado por rubros](#presupuesto-clarin-discriminado-por-rubros)
- [Subdivisión por etapas y presupuesto parcial](#subdivision-por-etapas-y-presupuesto-parcial)
- [Adicional de remodelación](#adicional-de-remodelacion)
- [Estimación del monto de obra](#estimacion-del-monto-de-obra)
- [Cálculo de honorarios CPAU](#calculo-de-honorarios-cpau)

---

## Identidad y formato del PDF (logo, Estudio Pi)

- **Estado:** ✓ Funcional
- Encabezado con banda de color: logo (`public/logo.png`, redimensionado a 180 px) + nombre del estudio ("Estudio Pi") y fecha.
- Título de obra (nombre del cliente/obra) al inicio, con cliente y dirección como detalle.
- Título "PRESUPUESTO POR …" que lista las etapas seleccionadas con "Usar" (p. ej. *Croquis preliminares, Anteproyecto y Dirección de obra*).
- Formato con separadores, bandas de totales, tabla con cabecera destacada y cajas de color (paleta de la app). Ver [ADR 0007](ADRs.md#adr-0007--identidad-y-formato-del-pdf).
- Archivos: `src/lib/presupuesto.ts`, `public/logo.png`.

## Presupuesto en dos versiones (estudio y cliente)

- **Estado:** ✓ Funcional
- Al generar se crean dos PDFs: **estudio** (`Presupuesto-Estudio-*.pdf`, detalle completo: M, honorario, rango, tabla por etapas y nota del arancel) y **cliente** (`Presupuesto-*.pdf`, sin M/K/fórmula: solo honorarios por etapas, total y modalidad de pago).
- La vista previa tiene pestañas para alternar entre versiones, cada una con su botón de guardado. Ver [ADR 0008](ADRs.md#adr-0008--dos-versiones-de-presupuesto).
- Archivos: `src/lib/presupuesto.ts`, `src/components/PresupuestoPreview.tsx`, `src/App.tsx`.

## Vista previa del PDF y guardado en carpeta

- **Estado:** ✓ Funcional
- Vista previa en modal con `<iframe>` (data URL) y pestañas Estudio/Cliente antes de guardar, y guardado automático en `P:\devs\CalHon\presupuestos\` vía dev server. Ver [ADR 0006](ADRs.md#adr-0006--vista-previa-del-pdf-y-guardado-en-carpeta) y [ADR 0009](ADRs.md#adr-0009--vista-previa-con-data-urls-y-logo-redimensionado).
- Archivos: `plugins/savePresupuesto.ts`, `src/components/PresupuestoPreview.tsx`, `src/lib/presupuesto.ts`.

## Exportación a PDF

- **Estado:** ✓ Funcional
- Generación en cliente con `jsPDF` (A4, mm) del documento sin `save()`, a partir del cual se derivan las dos versiones del presupuesto. Ver [ADR 0005](ADRs.md#adr-0005--exportacion-a-pdf-con-jspdf).
- Archivo: `src/lib/presupuesto.ts`.

## Modal de datos de obra

- **Estado:** ✓ Funcional
- Ingreso de nombre de obra, dirección y apellido del cliente que se incorporan al PDF.
- Archivo: `src/components/PresupuestoModal.tsx`.

## Persistencia de la tipología elegida

- **Estado:** ✓ Funcional
- Guarda la tipología en `localStorage` y la restaura al reabrir la app.

## Presupuesto Clarín discriminado por rubros

- **Estado:** ✓ Funcional
- Solo disponible en el Modelo 11 (reciclaje): 18 rubros con porcentajes aplicados al `M` considerado, con marcar/desmarcar todos.
- Archivo: `src/data/clarin.ts`.

## Subdivisión por etapas y presupuesto parcial

- **Estado:** ✓ Funcional
- Cinco etapas del Cuadro 6 con parciales/acumulados, selección y presupuesto de etapa con definiciones del arancel. Ver [ADR 0004](ADRs.md#adr-0004--subdivision-por-etapas-art-314).

## Adicional de remodelación

- **Estado:** ✓ Funcional
- Toggle manual y auto-activación en tipologías de reciclaje; +40 % solo sobre honorarios. Ver [ADR 0003](ADRs.md#adr-0003--adicional-de-remodelacion-art-318).

## Estimación del monto de obra

- **Estado:** ✓ Funcional
- `M = precio/m² × superficie` por tipología Clarín ARQ, editable manualmente. Ver [ADR 0002](ADRs.md#adr-0002--estimacion-del-monto-de-obra-tipologias-clarin-arq).
- Archivos: `src/data/clarin.ts`, `src/lib/honorarios.ts`.

## Cálculo de honorarios CPAU

- **Estado:** ✓ Funcional
- Fórmula `coefM × M + coefK × K` con rangos A/B/C/D y grupos 1/2/3. Ver [ADR 0001](ADRs.md#adr-0001--calculo-de-honorarios-cpau).
- Archivos: `src/lib/honorarios.ts`, `src/data/cpau.ts`.
