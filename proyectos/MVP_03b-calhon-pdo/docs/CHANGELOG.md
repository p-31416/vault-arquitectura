# CHANGELOG — Historial de cambios

Registro cronológico de cambios visibles. **Los más nuevos van arriba.** Cada entrada lleva fecha y hora (`YYYY-MM-DD HH:mm`). No documenta decisiones (eso está en [`ADRs.md`](ADRs.md)) ni features (en [`FEATURES.md`](FEATURES.md)). Ver [`0-INDEX.md`](0-INDEX.md).

**Tipos de cambio:** `Agregado` · `Cambiado` · `Corregido` · `Eliminado`

## Índice

- [2026-08-08 10:43 — Identidad del PDF y dos versiones](#2026-08-08-1043--identidad-del-pdf-y-dos-versiones)
- [2026-08-08 08:49 — Vista previa del PDF y guardado en carpeta](#2026-08-08-0849--vista-previa-del-pdf-y-guardado-en-carpeta)
- [2026-08-08 08:36 — Línea base y documentación](#2026-08-08-0836--linea-base-y-documentacion)

---

## 2026-08-08 10:43 — Identidad del PDF y dos versiones

**Agregado**

- Identidad en el PDF: logo (`public/logo.png`, redimensionado a 180 px), nombre "Estudio Pi", título de obra al inicio y título "PRESUPUESTO POR …" con las etapas seleccionadas con "Usar".
- Dos versiones de presupuesto al generar: **estudio** (`Presupuesto-Estudio-*.pdf`) y **cliente** (`Presupuesto-*.pdf`, sin M/K/fórmula/tabla/nota del arancel).
- Pestañas en la vista previa para alternar entre versiones, cada una con su guardado en carpeta.

**Cambiado**

- `src/lib/presupuesto.ts`: rediseño del layout (bandas, separadores, tabla destacada, cajas de color) y parámetro `version: 'estudio' | 'cliente'` que ramifica el contenido.
- Nombres de archivo: `Presupuesto-Estudio-AAAA-MM-DD.pdf` (estudio) y `Presupuesto-AAAA-MM-DD.pdf` (cliente).

**Corregido**

- Vista previa gris: el `<iframe>` ahora usa data URL en lugar de blob URL, con `key` por versión para recarga limpia.
- Tamaño del PDF: el logo se redimensiona a 180 px antes de embeber (de ~760 KB a ~106 KB).

---

## 2026-08-08 08:49 — Vista previa del PDF y guardado en carpeta

**Agregado**

- Vista previa del presupuesto en un modal con `<iframe>` antes de guardarlo (componente `PresupuestoPreview`).
- Guardado automático del PDF en `P:\devs\CalHon\presupuestos\` vía `POST /api/presupuesto` del dev server (plugin de Vite `plugins/savePresupuesto.ts`).
- Nombres de archivo únicos `Presupuesto-Honorarios-AAAA-MM-DD[_n].pdf`.

**Cambiado**

- `src/lib/presupuesto.ts`: se extrajo `buildPresupuestoPDF()` (devuelve el documento) y el helper `nombreArchivoPresupuesto()`; el flujo ahora pasa por vista previa en lugar de descarga directa.
- Carpeta del proyecto renombrada de `cal-hon/` a `app-cal_hon/`.
- Índice de documentación renombrado a `docs/0-INDEX.md` (para que aparezca primero).

## 2026-08-08 08:36 — Línea base y documentación

**Agregado**

- Documentación inicial del repo: `docs/0-INDEX.md`, `docs/ADRs.md`, `docs/FEATURES.md` y este archivo.
- Registro de las decisiones de diseño ya tomadas (ADRs 0001–0005) y de la feature planificada de vista previa + guardado en carpeta (ADR 0006).

**Línea base del estado actual de la app** (features ya funcionales a esta fecha):

- Cálculo de honorarios CPAU con rangos A/B/C/D y grupos 1/2/3.
- Estimación del monto de obra por tipologías Clarín ARQ, editable manualmente.
- Adicional de remodelación (+40 % sobre honorarios).
- Subdivisión por etapas (Cuadro 6) con presupuesto parcial seleccionable.
- Presupuesto Clarín discriminado por rubros (Modelo 11, reciclaje).
- Modal de datos de obra (nombre, dirección, cliente).
- Exportación a PDF con `jsPDF` (descarga directa).
- Persistencia de la tipología elegida en `localStorage`.
