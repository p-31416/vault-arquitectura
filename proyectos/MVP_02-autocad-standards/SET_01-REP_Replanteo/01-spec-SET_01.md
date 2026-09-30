---
tipo: spec
mvp: 02
nivel: SET_01-REP
set_numero: "01"
set_disciplina: REP
set_nombre: Replanteo
version: 2.1-unificado
fecha_creacion: 2026-09-27
ultima_actualizacion: 2026-09-27
tags: [mvp_02, SET, SET_01, replanteo, n_01, capas, standares, v2, unificado]
referencia_arquilogia: true
url_audit: raw/reports/2026-09-27-url-audit.md
reemplaza_a: SET-replanteo-spec.md (v1, eliminado 2026-09-27) + SET-replanteo-2.md (renombrado)
---

# SET_01-REP — Plano de Replanteo Arquitectónico v2.1 (Unificado)

> **SET** = Set de herramientas, Standards, Capas, Puntas
> **Estructura**: importa `../../01-spec-mvp_02.md` (genérica, 10 items) y detalla abajo según necesidad SET_01.
> **Plano tipo**: Replanteo arquitectónico (ejes, fundaciones, cotas, niveles)
> **Nomenclatura**: Prefijos Kit (R-/A-/S-/G-) — NO DR-*
> **Contexto**: MVP concreto — primer SET desarrollado, fija precedente.
> **Referencia**: `raw/reports/2026-09-27-url-audit.md` — 36/38 URLs vigentes
> **Referencia**: Kit temático `raw/docs/Estudio Pi – Kit temático  SETs de estándar CAD.md` §§6-7

## 0. "DoD" SET_01 (hereda orden de `01-spec-mvp_02.md`)

- [x] **1. SETEO** → §4.2 (base acadiso.dwt, metros INSUNITS 6, escala 1:50(m)=20xp, layout A1). CÓMO en `02-ft-SET_01.md` §1.
- [ ] **2. LAYERS** → §2 (22 capas R-/G-/A-/S- con prefijo, tipo, valor, AUX). Pendiente paso a paso.
- [ ] **3. CTB** → §4.4 (EP-ISO.ctb; fallback `monochrome.ctb`). Doc `docs/ctb.md` pendiente.
- [ ] **4. TEXTSTYLES** → §4.2 (`EP-2.5`, `EP-3.5` anotativos). Pendiente paso a paso.
- [ ] **5. DIMSTYLES** → §4.2 (`EP-ARQ`). Pendiente paso a paso.
- [ ] **6. BLOQUES** → marca eje, punto, nivel. Doc `docs/bloques.md` pendiente.
- [ ] **7. DINÁMICOS/ATRIBUTOS** → R-PTO-ATTR ID,X,Y,Z → `DATAEXTRACTION`. Pendiente paso a paso.
- [ ] **8. TEMPLATE** → `activos/.../SET_01-REP.dwt` (NO en git). Doc `docs/template-dwt.md` pendiente; CÓMO en `02-ft-SET_01.md` §8.
- [ ] **9. AUTOLISP** → §7 (comando `SET-01-REP`). Archivo `lisp/` pendiente (se reconstruye tras 1–8).
- [ ] **10. GLOSARIO** → diferido (wiki tras evaluar SET_01)

---

## 1. Alcance

Un plano de replanteo establece el **sistema de referencia** desde el cual todo el proyecto se mide. Contenido mínimo (Kit §6 SET-REP):

- Medidas perimetrales y ángulos de la parcela
- Distancia sobre LM a ochava y a eje de calle
- ≥2 ejes de replanteo (+ auxiliares). NO coinciden con LM ni divisorios, NO cruzan escaleras/dobles alturas
- Fundaciones (bases, troncos, columnas, pilotes) acotadas desde sus ejes hasta ejes de replanteo
- Cotas parciales y acumuladas, espesores por lados exteriores, niveles en plantas altas
- En muros curvos: radio, centro, coordenadas inicio/fin
- **Escala**: 1:50. **Tolerancias**: 10mm manual, 5mm instrumental

---

## 2. CAPAS — Nomenclatura Kit

### 2.1 SET-REP (núcleo replanteo)

| Layer | Color | Linetype | Lineweight (ISO 128-2) | Descripción |
|-------|-------|----------|------------------------|-------------|
| `R-EJES` | Green (3) | CONTINUOUS | 0.50 | Ejes de replanteo principales |
| `R-EJAX` | Green (3) | CONTINUOUS | 0.35 | Ejes auxiliares |
| `R-COTP` | White (7) | CONTINUOUS | 0.35 | Cotas parciales |
| `R-COTA` | White (7) | CONTINUOUS | 0.50 | Cotas acumuladas |
| `R-PTOS` | Yellow (2) | CONTINUOUS | 0.25 | Puntos con coordenadas (ID, X, Y, Z) |
| `R-NIVE` | Green (3) | CONTINUOUS | 0.35 | Niveles |
| `R-FUND` | Red (1) | CONTINUOUS | 0.50 | Fundación (ref. SET-EST) |

### 2.2 SET-GEN (plantilla, siempre presente)

| Layer | Color | Linetype | Lineweight | Descripción |
|-------|-------|----------|------------|-------------|
| `G-CART` | Gray (8) | CONTINUOUS | 0.10 | Carátula |
| `G-MARC` | Gray (8) | CONTINUOUS | 0.10 | Marco |
| `G-TEXT` | White (7) | CONTINUOUS | 0.25 | Textos generales |
| `G-COTA` | White (7) | CONTINUOUS | 0.25 | Cotas generales (no replanteo) |
| `G-REFE` | Cyan (4) | CONTINUOUS | 0.25 | Referencias corte/detalle |
| `G-VPRT` | Gray (8) | CONTINUOUS | 0.10 | Viewports (no imprimible) |
| `G-AUXI` | Gray (8) | CONTINUOUS | 0.10 | Construcción (no imprimible) |

### 2.3 SET-ARQ (referencia, xref o frozen)

Solo las necesarias como fondo para replantear:

| Layer | Color | Linetype | Lineweight | Descripción |
|-------|-------|----------|------------|-------------|
| `A-MURO-N` | Magenta (6) | CONTINUOUS | 0.50 | Muros nuevos (ref.) |
| `A-TABI` | Magenta (6) | CONTINUOUS | 0.35 | Tabiques (ref.) |
| `A-ABER` | Yellow (2) | CONTINUOUS | 0.25 | Aberturas (ref. vanos a ejes) |
| `A-LOCA` | Blue (5) | CONTINUOUS | 0.25 | Rótulos locales (ref.) |

### 2.4 SET-EST (referencia, xref)

| Layer | Color | Linetype | Lineweight | Descripción |
|-------|-------|----------|------------|-------------|
| `S-FUND` | Red (1) | CONTINUOUS | 0.50 | Fundaciones (detalle en SET-EST) |
| `S-COLU` | Red (1) | CONTINUOUS | 0.50 | Columnas (acotadas a ejes R-) |
| `S-VIGA` | Red (1) | CONTINUOUS | 0.35 | Vigas (ref.) |
| `S-EJES` | Green (3) | CONTINUOUS | 0.35 | Ejes estructurales (xref R-EJES) |

> **Total**: 7 (REP) + 7 (GEN) + 4 (ARQ ref) + 4 (EST ref) = **22 capas** (vs 80+ DR-* anteriores).

### 2.5 SET-ROT (paper-only, layout `REP-PTipo-A1`)

Capas exclusivas del espacio papel. NO imprimibles en `EP-ISO.ctb` (Plot = No).

| Layer | Color ACI | Linetype | Descripción |
|-------|-----------|----------|-------------|
| `ROT-HOJA` | Blue (5) | Continuous | Recuadro exterior del rótulo A-434 / IRAM 4508 |
| `ROT-TXT` | Indexed custom (174) | Continuous | Textos fijos del rótulo (no atributos) en paper space mm |
| `ROT-VP` | Indexed custom (130) | Continuous | Viewports del layout A1 (no plot si quedó basura en `0`) |

> Convención interna MVP_02 — prefijo `ROT-` (rotulación) es **categoría distinta** de `R-/G-/A-/S-` (modelo). Están separadas porque las capas paper-only no salen en el CTB y no entran al modelo en metros.

### 2.6 Auditoría de capas en DWG activo (placeholder)

Auditoría aplicada al DWG `G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg` con `INSUNITS=6`. Estado actual leído vía `autocad_list_layers` (2026-09-28):

| Capa real en DWG | Spec §2 match | Estado | Acción documentada |
|---|---|---|---|
| `0` | (default AutoCAD) | ✓ | Mantener |
| `ROT-HOJA` | §2.5 SET-ROT | ✓ | Mantener; ACI 5 blue |
| `ROT-TXT` | §2.5 SET-ROT | ✓ | Mantener; ACI 174 custom (a normalizar a ACI 7 white si se uniforma con G-TEXT) |
| `ROT-VP` | §2.5 SET-ROT | ✓ | Mantener; ACI 130 custom (mismo criterio) |
| `A-TERRENO` | §2.3 SET-ARQ (genérico `A-*`) | ✓ | Mantener |
| `REP-EJES` | §2.1 SET-REP `R-EJES` | ✗ prefijo diverge | Pendiente renombre `-LAYER Rename REP-EJES R-EJES`. Linetype actual `DASHDOTX2` (eje punteado 2×) es apropiado. |
| `INCENDIO` | n/a — sin prefijo de disciplina | ✗ | Pendiente renombre `-LAYER Rename INCENDIO A-INCEN` y agregar a §2.3 SET-ARQ |

> Las capas que no respetan el formato Kit quedan marcadas para renombre y luego se re-auditan. **Las que sigan sin encajar tras renombre, se borran** (regla del estudio MVP_02).

---

## 3. STANDARDS — Reglas

### 3.1 Ejes (R-EJES, R-EJAX)

- ≥2 ejes principales (R-EJES), auxiliares en R-EJAX
- NO coinciden con LM ni divisorios
- NO cruzan huecos escalera / dobles alturas
- Marca de eje: bloque con letra/número

### 3.2 Cotas (R-COTP, R-COTA)

- **Parciales** (R-COTP): entre dos puntos intermedios
- **Acumuladas** (R-COTA): desde eje 0 hasta punto final
- Estructura acotada **desde ejes R-** (nunca desde muro)
- Mampostería a filos, vanos a ejes

### 3.3 Puntos (R-PTOS)

- Bloque con atributos: ID, X, Y, Z
- Cuadro de coordenadas vía `DATAEXTRACTION` (auto-actualiza si se mueven)

### 3.4 Niveles (R-NIVE)

- Cotas NPT por piso
- Símbolo de nivel estándar

### 3.5 Fundaciones (R-FUND → S-FUND)

- En R-FUND: silueta + acotado a ejes R-
- Detalle constructivo en SET-EST (S-FUND, S-COLU, S-ARMA)

### 3.6 Estados N/E/D

- N = nuevo, E = existente, D = a demoler (alineado NCS + ISO 13567)
- Ej: `A-MURO-N`, `A-MURO-E`, `A-MURO-D`

---

## 4. HERRAMIENTAS — Comandos → Capas

### 4.1 Comandos por categoría

| Función | Comandos | Capas |
|---------|----------|-------|
| Capas | `LAYER`, `LAYISO`, `LAYFRZ`, `QSELECT` | Todas R-/A-/S-/G- |
| Dimensión | `DIM`, `DLI`, `DAL`, `DIMSTYLE`, `DIMCONTINUE`, `DIMBASELINE` | R-COTP, R-COTA |
| Texto | `MTEXT`, `TEXT`, `STYLE` | G-TEXT, A-LOCA |
| Edición | `MOVE`, `COPY`, `OFFSET`, `TRIM`, `EXTEND`, `ARRAY` | Todas |
| Bloques | `BLOCK`, `INSERT`, `ATTDEF`, `BATTMAN`, `ATTSYNC` | R-PTOS, R-EJES (marcas) |
| Xref | `XREF`, `ATTACH` | A-*, S-* (como ref.) |
| Plot | `PLOT`, `EXPORTPDF`, `PUBLISH` | Todas (CTB EP-ISO) |
| Estándares | `CHECKSTANDARDS`, `LAYTRANS`, `AUDIT`, `PURGE` | Todas |
| Datos | `DATAEXTRACTION` | R-PTOS → cuadro coordenadas |

### 4.2 SETEO — Setup base (`acadiso.dwt` → `SET_01-REP.dwt`)

Base: `acadiso.dwt` (plantilla ISO métrica original de AutoCAD). Este § define el QUÉ; el CÓMO paso a paso está en `02-ft-SET_01.md` §1.

**Unidades — metros, 2 decimales:**

| Variable | Valor | Significado |
|----------|-------|-------------|
| `LUNITS` | 2 | Decimal (1 unidad = 1 m, formato 0.00) |
| `LUPREC` | 2 | Precisión 2 decimales |
| `INSUNITS` | 6 | Metros (escala de inserción de bloques/xrefs) |
| `MEASUREMENT` | 1 | Métrico (sombreados y tipos de línea) |
| `-DWGUNITS` | 6, sin reescalar geometría | Fija metros e iguala INSUNITS sin cambiar tamaños existentes |

Fuentes: [How to change units (-DWGUNITS)](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Convert-imperial-unit-drawing-to-metric-units.html) · [About Block Units and Insertion Scale](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-6C46049D-8636-442D-8BAC-CF4FD515FDC0) · [Objects scaled when inserted (INSUNITSDEFSOURCE/TARGET)](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Blocks-xrefs-or-raster-images-are-scaled-when-inserted.html)

**Escalas — 1:50 con modelo en metros:**

El modelo se dibuja en metros y el papel en milímetros. Para 1:50, 1 m de modelo sale a 20 mm en papel → factor de viewport **20** = `ZOOM 1000/50 XP`. El "1:50" de la lista standard (factor 0.02) supone mm/mm y NO sirve con modelo en metros: hay que agregar entrada custom.

| Entrada | Paper | Drawing | Factor | Uso |
|---------|-------|---------|--------|-----|
| `1:50 (m)` | 1 (=1 mm) | 0.05 (=0.05 m) | 20 | Viewport replanteo |

Crear vía `SCALELISTEDIT` → Add. Fuentes: [Incorrect scale 1:100 viewport](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Incorrect-scale-when-setting-up-viewport-plot-scale-in-AutoCAD.html) · [Custom scale paper vs drawing units](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-scale-does-not-scale-viewports-as-expected-in-AutoCAD.html) · [Viewport Scale doc](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-3B8EA357-0906-41D2-B2B0-8EAEA4CA2CF8)

**Layout A1:**

| Parámetro | Valor |
|-----------|-------|
| Nombre | `REP-A1` |
| Formato | ISO A1 841×594 mm, apaisado (IRAM 4504) |
| Impresora | `DWG To PDF.pc3` (full bleed para tamaño exacto) |
| Escala de trazado | 1:1 (1 mm = 1 unidad) |
| Viewport | 1 ventana + escala `1:50 (m)` + bloqueada (display locked) |
| Rótulo | Lo dibuja el usuario después (bloque `G-CART`, ver research A-434) |

1. Capas: las 22 de §2 con color/linetype/weight
2. Styles: `EP-2.5`, `EP-3.5` (anotativos); cotas `EP-ARQ`; tabla `EP`

### 4.3 DWS (`SET-REP.dws`)

Verifica capas, estilos texto/cota/directriz, tipos línea. Comando: `CHECKSTANDARDS`.

### 4.4 CTB (`EP-ISO.ctb`, común)

Color → grosor serie ISO 128-2 (0.13–2mm):
- Green (3) → 0.50 (ejes)
- White (7) → 0.35/0.50 (cotas/texto)
- Red (1) → 0.50 (estructura/fund)
- Yellow (2) → 0.25 (puntos)
- Magenta (6) → 0.50 (muros ref.)
- Gray (8) → 0.10 (plantilla, no plot)

### 4.5 Equivalencias internacionales

| Kit (Estudio Pi) | NCS | ISO 13567 | AEC UK |
|------------------|-----|-----------|--------|
| R-EJES | AJ-EJES* | A-...-G- | A-EJ-... |
| R-COTA | AJ-COTA* | A-...-D- | A-CO-... |
| A-MURO-N | A-WALL-FULL-N | A-G25---E-N | A-MU-... |
| S-FUND | S-FUND-... | S-...-E- | S-FD-... |
| G-CART | G-ANNO-TTLB | A-...-B- | G-TT-... |

> *R en NCS = "Resource". Para exportar NCS, mapear SET-REP a AJ/AK (definible usuario). Guardar mapeo en DWS vía `LAYTRANS`.

### 4.6 SETEO ScaleList — modelo en metros

**Principio** (confirmado contra help oficial 2026-09-28): con `INSUNITS=6` (metros), las default scales de acadiso.dwt se ajustan automáticamente **al cerrar y reabrir el DWG**. El factor **CustomScale del viewport = 1000 / denominador_escala** (no 1/denominador).

| Display en lista | CustomScale aplicado | Fórmula `ZOOM n XP` |
|---|---|---|
| `1:5` | 200 | `ZOOM 200 XP` |
| `1:10` | 100 | `ZOOM 100 XP` |
| `1:20` | 50 | `ZOOM 50 XP` |
| `1:50` | 20 | `ZOOM 20 XP` (default Replanteo SET_01-REP) |
| `1:75` | 13.333 | `ZOOM 13.3333 XP` |
| `1:100` | 10 | `ZOOM 10 XP` (Plantas generales) |
| `1:200` | 5 | `ZOOM 5 XP` (Masterplan) |
| `1:500` | 2 | `ZOOM 2 XP` (Urbano / lote) |
| `1:1000` | 1 | `ZOOM 1 XP` (Paisajismo) |

**Procedimiento canónico** (ver `02-ft-SET_01.md` §4.6 para paso a paso con UI):
1. `SCALELISTEDIT` → Ctrl+A → Delete.
2. Cerrar el DWG → Reabrir. **AutoCAD regenera las default ajustadas a metros** (help: *"After you close and reopen the drawing the scale definition revert to correct values again"*).
3. Si no se auto-ajusta, `OPTIONS → User Preferences → Default Scale List…` → Edit cada escala con Paper=1, DrawingUnits = denom/1000.
4. En el viewport, **aplicar la escala por nombre desde la lista, NUNCA tipear el factor crudo** (regla: "If an equal value is available in the scale list, it will be represented in the properties palette"). Si el dropdown muestra "20" en vez de "1:50", la escala no está en la lista.

Fuentes oficiales: [Resetting the scales list](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Resetting-the-scales-list-leads-to-wrong-scale-definitions-that-are-corrected-after-reopening-the-DWG.html) · [Incorrect scale 1:100 viewport](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Incorrect-scale-when-setting-up-viewport-plot-scale-in-AutoCAD.html) · [CustomScale Property ActiveX](https://help.autodesk.com/view/OARX/2027/ENU/?guid=GUID-B2267102-5970-49A4-AA7E-A9D0362D2CF6) · [Viewport Scale doc](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-3B8EA357-0906-41D2-B2B0-8EAEA4CA2CF8) · [Custom viewport scale field trap](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-viewport-scale-is-not-being-displayed-for-Field-in-AutoCAD.html).

### 4.7 LAYOUT — `REP-PTipo-A1` (full bleed A1)

Layout activo del proyecto `REP-ARAOZ.dwg`. El nombre se mantiene como vos lo creaste (`REP-PTipo-A1`) y queda registrado acá.

| Parámetro | Valor verificado |
|---|---|
| Nombre | `REP-PTipo-A1` |
| Plotter | `DWG To PDF.pc3` |
| Paper | `ISO_full_bleed_A1_(594.00_x_841.00_MM)` = 841×594 mm **apaisado (landscape)** |
| Plot area | Layout |
| Plot scale | 1:1 (1 mm = 1 unidad) |
| Viewports | handle `358` (principal, escala 1:50) + handle `3E4` (chico, escala 1:200 en duda) |
| Display locked | Pendiente confirmar por viewport (BLOCK → "Yes") |
| Layout2 huérfano | Eliminado 2026-09-27 ✓ |

**Creación del layout** vía `-LAYOUT New` (help: *"Layout names must be unique… Up to 255 layouts can be created"*) → `PAGESETUP` con full bleed. Si el `Plotter Configuration` no muestra "full bleed A1" como opción, modificar `DWG To PDF.pc3` → Device and Document Settings → Modify Standard Paper Sizes → ISO A1 → margins = 0 (help: [Full bleed PDF](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-print-pdf-in-full-layout-in-AutoCAD.html)).

> **Regla del estudio MVP_02**: el nombre del layout codifica `<SET>-PTipo-<formato>` donde `PTipo` identifica el tipo de lámina (en este caso A1). Otros tamaños: `REP-PTipo-A0`, `REP-PTipo-A2`, `REP-PTipo-A3`, etc.

---

## 5. PUNTAS

- `OSNAP` Endpoint/Intersection/Center/Node para ejes
- `DIMCONTINUE` para acumuladas, `DIMBASELINE` para parciales
- `DATAEXTRACTION` de R-PTOS → cuadro coordenadas auto-actualizable
- `LAYFRZ` (no `LAYOFF`) para capas de ejes
- `AUDIT` + `PURGE` antes de plotear
- LT sin DWS → control con plantilla + checklist + agente IA

---

## 6. Orden de trabajo

1. Setup DWT con 22 capas
2. Ejes R-EJES/R-EJAX
3. Terreno: medidas perimetrales, ángulos, LM/ochava
4. Fundaciones R-FUND/S-FUND acotadas a ejes
5. Cotas R-COTP/R-COTA
6. Puntos R-PTOS + cuadro coordenadas
7. Niveles R-NIVE
8. Revisión: `CHECKSTANDARDS`, `AUDIT`, `PURGE`
9. Presentación 1:50, plot PDF

---

## 7. AutoLISP — `SET-Replanteo.lsp`

```lisp
; SET-Replanteo.lsp — v2.1 (Kit naming: R-/A-/S-/G-)
; Ejecutar: SET-REPLANTEO

(defun c:SET-REPLANTEO (/ )
  (vl-load-com)
  (SET-REP-CAPAS)
  (SET-REP-STYLES)
  (SET-REP-VARIABLES)
  (princ "\nSET-Replanteo v2.1 aplicado (22 capas Kit).")
  (princ)
)

(defun SET-REP-CAPAS (/ mk)
  (defun mk (n c lt w)
    ; crear capa n con color c, linetype lt, weight w
    ; (implementar con Layer API)
    (princ (strcat "\n" n))
  )
  ; SET-REP (7)
  (mk "R-EJES" 3 "CONTINUOUS" 0.50)
  (mk "R-EJAX" 3 "CONTINUOUS" 0.35)
  (mk "R-COTP" 7 "CONTINUOUS" 0.35)
  (mk "R-COTA" 7 "CONTINUOUS" 0.50)
  (mk "R-PTOS" 2 "CONTINUOUS" 0.25)
  (mk "R-NIVE" 3 "CONTINUOUS" 0.35)
  (mk "R-FUND" 1 "CONTINUOUS" 0.50)
  ; SET-GEN (7)
  (mk "G-CART" 8 "CONTINUOUS" 0.10)
  (mk "G-MARC" 8 "CONTINUOUS" 0.10)
  (mk "G-TEXT" 7 "CONTINUOUS" 0.25)
  (mk "G-COTA" 7 "CONTINUOUS" 0.25)
  (mk "G-REFE" 4 "CONTINUOUS" 0.25)
  (mk "G-VPRT" 8 "CONTINUOUS" 0.10)
  (mk "G-AUXI" 8 "CONTINUOUS" 0.10)
  ; SET-ARQ ref (4)
  (mk "A-MURO-N" 6 "CONTINUOUS" 0.50)
  (mk "A-TABI" 6 "CONTINUOUS" 0.35)
  (mk "A-ABER" 2 "CONTINUOUS" 0.25)
  (mk "A-LOCA" 5 "CONTINUOUS" 0.25)
  ; SET-EST ref (4)
  (mk "S-FUND" 1 "CONTINUOUS" 0.50)
  (mk "S-COLU" 1 "CONTINUOUS" 0.50)
  (mk "S-VIGA" 1 "CONTINUOUS" 0.35)
  (mk "S-EJES" 3 "CONTINUOUS" 0.35)
  (princ)
)

(defun SET-REP-STYLES (/ )
  ; EP-2.5, EP-3.5, EP-ARQ, EP (tabla)
  (princ)
)

(defun SET-REP-VARIABLES (/ )
  (setvar "LUNITS" 2)
  (setvar "LUPREC" 2)
  (setvar "MEASUREMENT" 1)
  (setvar "INSUNITS" 6)
  (setvar "OSMODE" 511)
  (princ)
)
```

---

## 8. Fuentes (36 vigentes)

Ver `raw/reports/2026-09-27-url-audit.md`. Descartadas (403): Autodesk Blog CAD Standards, UNLP TP7 Replanteo.

Claves: NCS [^1][^2][^3], ISO 13567 [^5][^6], AEC UK [^7], Uniclass [^8], ISO 19650 [^9], ISO 128-2 [^10], IRAM [^11], UNaM [^12], CIRSOC [^14], Autodesk Help [^15][^17-^28], CAPBA [^29], GCBA [^30], AEA [^31], AySA [^32], YouTube [^33-^37], Assistant 2027 [^39], Wiley [^40].

---

## 9. Próximos pasos

1. [ ] Validar 22 capas con equipo
2. [ ] Crear `SET-REP.dwt` + `SET-REP.dws` + `EP-ISO.ctb`
3. [ ] Completar AutoLISP (funciones mk con Layer API real)
4. [ ] Plano piloto 1:50
5. [ ] @sherlock investiga 36 fuentes → @vaultworm-arq procesa → wiki

> *El replanteo es donde todo comienza — es la primera marca en el terreno.*

---

## 10. RÓTULO / BLOQUE CARÁTULA (placeholder §10.1, §10.2, §10.2.1)

Documentación del rótulo A-434 / IRAM trazado en `REP-PTipo-A1` y del futuro bloque `G-CART-MEPA` con FIELD para escala del viewport.

### 10.1 Rótulo (entidades pre-bloque) — *[placeholder]*

Estado actual leído del DWG activo `G:\Mi unidad\OS-Emilia\W03-CAD\REP-ARAOZ.dwg` (2026-09-28):

- 4 polilíneas en `ROT-HOJA` (subrecuadros / subdivisiones del marco A-434)
- 8 líneas en `ROT-HOJA` (guías internas, ejes de carátula)
- 9 `AcDbText` en `ROT-TXT` (textos fijos)
- 7 `AcDbAttributeDefinition` en `ROT-TXT` (atributos del bloque futuro; **tags aún sin identificar** — pendiente que pegues el listado)

**Norma**: 5 campos "se recomienda" de A-434 (designación de obra, identificación del comitente, designación+lámina+número+escala(s), dirección+teléfono del estudio, fechas de terminación/revisión/aprobación). Ver [[raw/research/2026-09-27-A434-rotulado-resumen|A-434 rotulado]] (research vault 2026-09-27) + [[raw/research/2026-09-27-mepa-rotulos|MEPA rótulos]].

**IRAM 4508** (rótulo ángulo inferior derecho de zona de ejecución): 175×51 mm según fuente docente UNL. **Lámina oficial IRAM no verificada** (norma paga). Si se adopta, citar como "según fuente docente, pendiente verificación con lámina oficial IRAM".

**Sublay PDF de referencia** (NO imprimir): `G:\Mi unidad\OS-Emilia\W03-CAD\REPLANTEO-ref\ROTULO_MEPA_A-434.pdf`. PDF binario sin capa de texto por `webfetch` (gap conocido). Trazar sobre la sublay con nueva layer propuesta `ROT-PDF-REF` (Plot = No).

### 10.2 Bloque `G-CART-MEPA` — *[placeholder]*

Conversión de las entidades de §10.1 en un bloque reutilizable:

1. `BLOCK` → Block name: **`G-CART-MEPA`** → Insertion point: esquina inferior derecha del rótulo (convención IRAM 4508).
2. Select objects: window crossing el recuadro completo + textos fijos + los 7 ATTDEFs.
3. Verificar con `autocad_list_blocks` (debería aparecer con `entity_count > 0`).
4. (futuro) `WBLOCK` para guardar en path canónico: `activos/proyectos/mvp_02-autocad-standards/SET_01-REP/SET_01-REP_bloques.dwg` (gitignored, NO en git).

### 10.2.1 Atributo ESCALA = FIELD — *[placeholder]*

Vínculo FIELD viewport → atributo `ESCALA` del bloque `G-CART-MEPA`. Procedimiento oficial:

1. Identificar el ATTDEF de tag `ESCALA` (entre los 7 actuales). Pegar el listado Tag+Default en sesión cuando esté disponible.
2. `BEDIT` sobre `G-CART-MEPA` → doble-click sobre el ATTDEF `ESCALA` → botón **`Insert Field`** junto a "Default value".
3. Field category → `Objects` → Object type → `Viewport`.
4. Click sobre el viewport handle `358` (principal, escala 1:50). Property → **`Custom scale`**. Format → `1:X` o `X/Y`.
5. `REGEN` para que el FIELD se actualice.

Fuentes oficiales: [How to use custom scale of viewport in title block](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-use-the-custom-scale-of-layout-viewports-in-the-title-block.html) · [Custom viewport scale field trap](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-viewport-scale-is-not-being-displayed-for-Field-in-AutoCAD.html).

**Trap a evitar**: si la lista de escalas tiene dos entradas con mismo factor numérico y formateo distinto (ej. `1:50` mm-default + `1:50` m-custom), **mover arriba** la que querés en `SCALELISTEDIT`, sino el FIELD muestra la que esté primera.

**Catch-up necesario**: para armar esta sección, falta decisión del estudio sobre cuál de los 7 ATTDEFs será `ESCALA`. Hoy los tags no son legibles vía MCP autocad_* (`object_name` solo expone el tipo, no las propiedades). Opción A: pegar el listado (Tag + Default) en sesión. Opción B: dejar que sherlock abra el DWG con un sub-agente. La Opción A es más rápida.

---

## 11. PRÓXIMOS PASOS inmediatos (2026-09-28) — operativos MVP_02

1. [ ] (UI) Aplicar paso 1: `UN` → Decimal, Precision 0.0000, Insertion Scale Meters.
2. [ ] (UI) Aplicar paso 2: `SCALELISTEDIT` → Delete all → cerrar/reabrir → verificar default con factor 1000/denom.
3. [ ] (UI) Aplicar paso 3: confirmar `REP-PTipo-A1` paper 841×594 apaisado, full bleed, plotter `DWG To PDF.pc3`.
4. [ ] (UI) Aplicar paso 4: validar geometría del rótulo actual vs `ROTULO_MEPA_A-434.pdf` (sublay).
5. [ ] (UI) Aplicar paso 5: `BLOCK G-CART-MEPA` con los 7 ATTDEFs.
6. [ ] (UI) Aplicar paso 6: FIELD en el ATTDEF `ESCALA` apuntando al viewport `358` (1:50).
7. [ ] (UI) Aplicar paso 7: renombres `REP-EJES → R-EJES`, `INCENDIO → A-INCEN`.
8. [ ] (Build) Editar §4.2 cuando aplique UI paso 1 (sustituir LUPREC=2 → LUPREC=4 confirmado).
9. [ ] (Build) Editar §10.1 cuando pegues los 7 tags + reorganizar §10.2 al cerrar paso 5.
10. [ ] (Build) Editar §2.6 tabla al cerrar paso 7 (sacar filas "Pendiente renombre" o marcar "Hecho").
11. [ ] (HITL) Definir a qué MVP pertenece la URL `www.ar.weber/detalles-constructivos/muros-interiores` (MVP_02 / MVP_03 / glosario). Hoy agendada en `raw/research/2026-09-28-weber-detalles-muros.md`.
