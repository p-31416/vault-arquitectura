# ADRs — Registro de decisiones de diseño

Cada sección documenta una decisión relevante para CalHon con formato **Contexto → Decisión → Consecuencias**. No es un inventario de features (eso vive en [`FEATURES.md`](FEATURES.md)) ni un historial de cambios (en [`CHANGELOG.md`](CHANGELOG.md)). Ver [`0-INDEX.md`](0-INDEX.md).

**Orden:** de la decisión más reciente (arriba) a la más antigua (abajo). El número de ADR es un identificador estable y no indica orden cronológico.

## Índice

- [ADR 0009 — Vista previa con data URLs y logo redimensionado](#adr-0009--vista-previa-con-data-urls-y-logo-redimensionado)
- [ADR 0008 — Dos versiones de presupuesto (estudio y cliente)](#adr-0008--dos-versiones-de-presupuesto-estudio-y-cliente)
- [ADR 0007 — Identidad y formato del PDF](#adr-0007--identidad-y-formato-del-pdf)
- [ADR 0006 — Vista previa del PDF y guardado en carpeta](#adr-0006--vista-previa-del-pdf-y-guardado-en-carpeta)
- [ADR 0005 — Exportación a PDF con jsPDF](#adr-0005--exportacion-a-pdf-con-jspdf)
- [ADR 0004 — Subdivisión por etapas (Art. 3.14)](#adr-0004--subdivision-por-etapas-art-314)
- [ADR 0003 — Adicional de remodelación (Art. 3.18)](#adr-0003--adicional-de-remodelacion-art-318)
- [ADR 0002 — Estimación del monto de obra (tipologías Clarín ARQ)](#adr-0002--estimacion-del-monto-de-obra-tipologias-clarin-arq)
- [ADR 0001 — Cálculo de honorarios CPAU](#adr-0001--calculo-de-honorarios-cpau)

---

## ADR 0009 — Vista previa con data URLs y logo redimensionado

- **Estado:** Aceptado (implementado)

### Contexto

Tras agregar el logo, la vista previa en el modal quedó gris (el `<iframe>` no renderizaba el PDF). El PDF en sí era válido (se verificó parseándolo con pdfjs-dist), así que el problema estaba en cómo se exponía el documento al navegador.

### Decisión

- La vista previa usa **data URL** (`doc.output('datauristring')`) como `src` del `<iframe>` en lugar de `URL.createObjectURL(blob)`, eliminando el ciclo de vida del blob y su revocación.
- El `<iframe>` recibe una `key` por versión para recargarse limpio al cambiar de pestaña.
- El logo se redimensiona a 180 px vía `<canvas>` al cargarlo, bajando el PDF de ~760 KB a ~106 KB.

### Consecuencias

- Ya no se usan `URL.createObjectURL`/`revokeObjectURL` en la vista previa.
- `PreviewItem.url` contiene el data URL completo del PDF, usado también para guardar el archivo.

---

## ADR 0008 — Dos versiones de presupuesto (estudio y cliente)

- **Estado:** Aceptado (implementado)

### Contexto

El mismo cálculo alimenta dos audiencias distintas: el estudio necesita el detalle completo (M, honorario total, rango, tabla de etapas y nota del arancel) para archivar y controlar, mientras que al cliente solo le corresponden honorarios, desglose de etapas y modalidad de pago. Exponer datos internos (K, fórmula, monto de obra) resta formalidad al documento.

### Decisión

- Al generar el presupuesto se crean **dos PDFs**: versión `estudio` (`Presupuesto-Estudio-*.pdf`) y versión `cliente` (`Presupuesto-*.pdf`).
- La versión **cliente** omite `M`, `K`, rango/fórmula, grupo, adicional de remodelación detallado, tabla de etapas y nota del arancel. Incluye título de obra, "Presupuesto por …", honorarios por etapa, total, modalidad de pago y nota legal de la escala CPAU.
- La vista previa muestra ambas con pestañas y botón de guardado por versión.

### Consecuencias

- `buildPresupuestoPDF()` recibe un parámetro `version: 'estudio' | 'cliente'` que ramifica el contenido.
- Los nombres de archivo distinguen la versión y evitan pisar un documento con el otro en la carpeta de salida.

---

## ADR 0007 — Identidad y formato del PDF

- **Estado:** Aceptado (implementado)

### Contexto

El presupuesto es la cara visible del estudio ante el cliente. El PDF anterior era funcional pero plano: sin logo, sin identidad, con títulos genéricos y sin jerarquía visual.

### Decisión

- Encabezado con banda de color: logo (`public/logo.png`) + nombre del estudio ("Estudio Pi") a la izquierda y fecha a la derecha.
- El nombre de la obra del modal se usa como **título principal**, con cliente y dirección como línea de detalle.
- Título "PRESUPUESTO POR …" construido con los nombres de las etapas seleccionadas con "Usar" (separadas con "y"; "Etapa completa" si no hay selección).
- Jerarquía visual con separadores, bandas de totales, tabla con cabecera destacada y cajas de color (paleta de la app: verde `#0F6E56`).
- El logo se sirve desde `public/logo.png` y se redimensiona a 180 px antes de embeber para que el PDF quede liviano.

### Consecuencias

- Si falta `public/logo.png`, el PDF se genera igual (se omite el logo) y se loguea una advertencia en consola.
- El layout vive en `src/lib/presupuesto.ts` y se dibuja con jsPDF.

---

## ADR 0006 — Vista previa del PDF y guardado en carpeta

- **Estado:** Aceptado (implementado)

### Contexto

El usuario quiere validar el PDF **antes** de descargarlo y que el archivo quede en una carpeta de salida del repo (`P:\devs\CalHon\presupuestos\`), no solo en la carpeta de descargas del navegador. Por seguridad, el navegador no puede escribir en carpetas arbitrarias del disco.

### Decisión

- **Vista previa:** `buildPresupuestoPDF()` devuelve el documento `jsPDF` (sin `save()`); la UI genera un blob y lo muestra en un modal con `<iframe>` antes de descargar.
- **Guardado en carpeta:** plugin de Vite (`plugins/savePresupuesto.ts`) que expone `POST /api/presupuesto` en el dev server; el front envía el PDF (base64) y el servidor lo escribe en `presupuestos\` con nombre único `Presupuesto-Honorarios-AAAA-MM-DD[_n].pdf`.

### Consecuencias

- El guardado depende de que el dev server esté corriendo (entorno local).
- Se descartó la API File System Access del navegador (selector de carpeta manual) por UX y determinismo.
- Implementado en: plugin de Vite, `src/lib/presupuesto.ts`, `src/components/PresupuestoPreview.tsx`, `src/App.tsx` y `src/App.css`.
- *Nota:* el mecanismo de la vista previa evolucionó más adelante — ver [ADR 0009](#adr-0009--vista-previa-con-data-urls-y-logo-redimensionado).

---

## ADR 0005 — Exportación a PDF con jsPDF

- **Estado:** Aceptado

### Contexto

El presupuesto debe entregarse al cliente como documento cerrado. La app no tiene backend.

### Decisión

- Generación del PDF **100 % en el cliente** con `jsPDF` (tamaño A4, mm), dibujando el contenido directamente (sin render HTML).
- En el estado actual, `doc.save()` descarga el archivo directo con nombre `Presupuesto-Honorarios-AAAA-MM-DD.pdf`.

### Consecuencias

- No depende de un servidor, pero tampoco permite escribir en una carpeta arbitraria del disco (ver [ADR 0006](#adr-0006--vista-previa-del-pdf-y-guardado-en-carpeta)).
- El layout vive en `src/lib/presupuesto.ts`.

---

## ADR 0004 — Subdivisión por etapas (Art. 3.14)

- **Estado:** Aceptado

### Contexto

El honorario total debe poder desglosarse en etapas (Cuadro 6 del arancel) para facturar por avance o presupuestar una etapa puntual.

### Decisión

- Cinco etapas con parciales/acumulados del Cuadro 6: Croquis preliminares 7%, Croquis avanzados 8% (15%), Anteproyecto 5% (20%), Anteproyecto avanzado 20% (40%), Documentación 20% (60%), Dirección de obra 40% (100%).
- Cada etapa referencia su artículo y definición del arancel.
- El usuario puede seleccionar etapas y generar un presupuesto parcial (suma de parciales y porcentaje del honorario).

### Consecuencias

- Los parciales se calculan sobre `honorarioTotal` (incluye remodelación si aplica).
- El PDF muestra solo las etapas seleccionadas, con sus parciales, acumulados y definiciones.

---

## ADR 0003 — Adicional de remodelación (Art. 3.18)

- **Estado:** Aceptado

### Contexto

El arancel prevé un adicional cuando la obra es de refacción/remodelación. Debe decidirse sobre qué base se aplica para no duplicar el costo de obra (el `$/m²` de reciclaje ya contempla la obra).

### Decisión

- Adicional `+40%` **solo sobre el honorario base**, nunca sobre el monto de obra.
- `honorarioTotal = honorarioBase × (1 + 0,40)` cuando la obra es remodelación.
- El flag de remodelación se activa automáticamente al elegir una tipología de tipo `reciclaje`, y se puede togglear manualmente.

### Consecuencias

- En el PDF y en la UI se muestra el desglose: base + adicional, para que el comitente vea qué corresponde a remodelación.

---

## ADR 0002 — Estimación del monto de obra (tipologías Clarín ARQ)

- **Estado:** Aceptado

### Contexto

El usuario necesita un `M` razonable sin tener que pedir una cotización de obra. Se dispone de modelos de vivienda publicados por Clarín ARQ (resumen junio 2026) y de un PDF local de kiosco (Modelo 11, reciclaje).

### Decisión

- Estimación por tipología: `M = precio/m² × superficie`, con valores de referencia precargados por modelo (Country, PH Moderno, Vivienda en Altura, Reciclaje casa chorizo).
- `M` también es editable manualmente (se marca `montoManual = true`).
- El Modelo 11 (reciclaje) incluye además un presupuesto discriminado por 18 rubros tomado del PDF local, usado para aplicar porcentajes al `M` considerado.

### Consecuencias

- Las tipologías son datos de referencia de junio 2026 y quedan desactualizadas cuando varían los valores de mercado.
- La tipología elegida se persiste en `localStorage` para la próxima visita.

---

## ADR 0001 — Cálculo de honorarios CPAU

- **Estado:** Aceptado

### Contexto

El honorario profesional por "proyecto y dirección" debe calcularse según el arancel vigente del CPAU. Se dispone del cuadro de coeficientes (Cuadro 5) y del índice `K` = ICC.

### Decisión

- Fórmula: `honorario = coefM × M + coefK × K`, con `M` = monto de obra y `K` = índice del mes.
- Cuatro rangos de monto `A/B/C/D` definidos por múltiplos de `K`: `A ≤ 0,5K`, `B ≤ 5K`, `C ≤ 25K`, `D > 25K`.
- Tres grupos de obra (Art. 3.13): Grupo 1 edificios en general, Grupo 2 efímera/monumentos/funeraria, Grupo 3 paisaje/interiores, cada uno con su tabla de coeficientes.
- `K = 640.069.857,62` (ICC junio 2026) definido en `src/data/cpau.ts`.

### Consecuencias

- El resultado cambia si se actualiza `K` a mano en el código; el usuario no puede editarlo desde la UI.
- En rango A `coefK = 0`, la expresión queda solo `coefM × M`.
