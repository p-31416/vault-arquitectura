---
tipo: metodologia
mvp: 02
set: SET_01-REP
fecha_creacion: 2026-10-15
ultima_actualizacion: 2026-10-21
tags: [mvp_02, SET_01, playbook, autocad, full, replanteo, comandos, autocad-lt]
idioma: es
estado: vigente-lt-2027
---

# PB-02 — Replanteo desde 0 (variante LT 2027 vigente, Full EN como alternativa)

> **Actualizado 21/10/2026.** La máquina del estudio tiene **AutoCAD LT 2027** (`C:\Program Files\Autodesk\AutoCAD LT 2027`), no el Full 2027. Todo el flujo de este playbook es válido en LT; lo que cambia está marcado como **⚠ LT**. Comandos con prefijo `_` (p. ej. `_COMANDO`) corren en inglés en cualquier UI.
> **Regla:** comando `_COMANDO` corre EN en cualquier UI. Tabla EN primero / ES segundo.
> **Lo que LT no trae:** COM/ActiveX externo, `DATAEXTRACTION` / `ATTIN` / `ATTOUT`. **Lo que sí trae:** AutoLISP (`APPLOAD`, desde LT 2024 en Windows), `TABLA` con vínculo de datos (exige Excel instalado), `STANDARDS`, palettes y DesignCenter.
> Fuentes oficiales: [LT 2027 — LISP en LT](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Unable-to-load-lisp-in-AutoCAD-LT.html) · [LT 2027 — Tool Palettes](https://help.autodesk.com/view/ACDLT/2027/ENU/?guid=GUID-6668905A-3FAD-4EED-82A2-5D6177AD4280) · [LT 2027 — DesignCenter](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-insert-blocks-using-DesignCenter-for-AutoCAD-LT.html).

## 0. Comandos madre (ficha oficial + atajo)

| EN / ES (atajo) | Descripción oficial (1 línea Help) | Ref verificada |
|---|---|---|
| `UNITS` / `UNIDADES` (`UN`) | Sets length/angle format, precision, insertion scale | [Convert units (-DWGUNITS)](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Convert-imperial-unit-drawing-to-metric-units.html) |
| `-DWGUNITS` (solo línea) | Sets drawing units + match INSUNITS without rescaling when answered No/Yes | misma + [Blocks scaled when inserted](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Blocks-xrefs-or-raster-images-are-scaled-when-inserted.html) |
| `SCALELISTEDIT` / `EDITLISTAESCALAS` | Adds/edits drawing scale list; Paper vs Drawing units | [Custom scale paper vs drawing](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-scale-does-not-scale-viewports-as-expected-in-AutoCAD.html) · [Incorrect 1:100 viewport](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Incorrect-scale-when-setting-up-viewport-plot-scale-in-AutoCAD.html) |
| `LAYER` / `CAPA` (`LA`) | Manages layers: name, color ACI, linetype, lock/freeze | spec §2 + [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/REP-ARAOZ-capas-bloques\|medición §1]] |
| `STYLE` / `ESTILO` (`ST`) | Creates text styles (font, height, annotative) | audit URLs 2026-09-27 vigentes (spec §8) |
| `DIMSTYLE` / `ESTILOCOTA` (`D`) | Creates dimension styles (arrows `_ArchTick`/`_Open90`, offsets) | spec §4.2 (`COTAS-ARQ-50`, `REPLANTEO 150`) |
| `DIMLINEAR` / `COTLINEAL` (`DLI`) + `DIMCONTINUE` / `COTCONTINUA` + `DIMBASELINE` / `COTLINEABASE` | Linear + continued + baseline chains (parciales + acumuladas) | spec §3.2 |
| `BLOCK` / `BLOQUE` (`B`) + `INSERT` / `INSERTAR` (`I`) + `ATTDEF` / `DEFATRIB` | Defines/inserts blocks + attributes `TIPO/ANCHO/MURO/NPT` | [BOM via ATTDEF + DATAEXTRACTION](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Creating-a-Bill-of-Materials-BOM-in-AutoCAD-and-AutoCAD-LT.html) |
| `BATTMAN` / `ADMINATRIB` + `ATTSYNC` / `SINCRATR` | Manages + syncs attribute definitions to existing inserts | [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/bloques-personalizados|bloques-personalizados §5]] |
| `BEDIT` / `EDITARBLOQUE` + `FIELD` / `CAMPO` | Edits block + links viewport Custom scale to `ESCALA` | [Field trap Move Up + REGEN](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-viewport-scale-is-not-being-displayed-for-Field-in-AutoCAD.html) |
| `MVIEW` / `VENTANAS` + `LAYOUT` + `PAGESETUP` / `ADMINPAGINAS` | Creates viewport + layout + paper setup `DWG To PDF.pc3` A1 841x594 landscape 1:1 | [Plot layout 1:1](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Plotting-a-layout-in-paperspace-results-in-the-the-drawing-not-plotting-to-scale-in-AutoCAD.html) |
| `DATAEXTRACTION` / `EXTRACDAT` | Extracts block attributes to table/CSV (cómputos auto-actualizables) | [BOM](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Creating-a-Bill-of-Materials-BOM-in-AutoCAD-and-AutoCAD-LT.html) |
| `CHECKSTANDARDS` / `VERIFICANORMAS` | Audits drawing vs DWS, Fix/Next hasta Checking Complete | [About Checking](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-F8B47FBB-1276-4D74-BA89-0440CB4E4866) · [To Audit](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-3E786E2E-7F6A-4D89-8B2B-F749F1AC2B85) |
| `AUDIT` / `AUDITORIA` + `PURGE` / `LIMPIA` + `REGEN` / `REGENERAR` | Repairs + removes unused + regenerates | spec §5 |
| `PLOT` / `TRAZAR` (`Ctrl+P`) + `EXPORTPDF` | Plots Layout 1:1 with `monochrome.ctb` (vigente; `EP-ISO` en backlog multi-escala) | [Plot 1:1](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Plotting-a-layout-in-paperspace-results-in-the-the-drawing-not-plotting-to-scale-in-AutoCAD.html) · [How to Plot B/W](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-Plot-in-Grayscale-or-Black-and-White-from-AutoCAD-Products.html) |
| `APPLOAD` / `CARGARAPL` + `XREF` / `REFEXTERN` (`XR`) | Loads LSP (Full + LT 2024+ Win; `Unknown Command` en LT 2023- y LT Mac) + attaches `ARQ-ARAOZ` on `0-REF` | spec §4.1 + §7 · [LISP en LT](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Unable-to-load-lisp-in-AutoCAD-LT.html) |
| `TOOLPALETTES` + `ADCENTER` / `DESIGNCENTER` + `BLOCKSPALETTE` | Palettes con bloques (sí en LT): Tool Palettes + DesignCenter + Blocks palette Current/Recent/Favorites/Libraries | [Tool Palettes LT 2027](https://help.autodesk.com/view/ACDLT/2027/ENU/?guid=GUID-6668905A-3FAD-4EED-82A2-5D6177AD4280) · [DesignCenter LT](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-insert-blocks-using-DesignCenter-for-AutoCAD-LT.html) · [Blocks palette](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-E3413A03-8EEF-44D5-B5C7-8B345A9257FE) |

Edición base: `LINE`/`LINEA` (`L`), `OFFSET`/`DESFASE` (`O`), `RECTANG` (`REC`), `MOVE`/`DESPLAZA` (`M`), `COPY`/`COPIA` (`CO`), `TRIM`/`RECORTA` (`TR`), `EXTEND`/`ALARGA` (`EX`), `MTEXT`/`TEXTOM` (`T`).

## 1. Setup desde 0 (15 min)

1. Nuevo desde `acadiso.dwt` (`QNEW`). Guarda como `SET_01-REP.dwt` en `activos/.../SET_01-REP/` (NO en git, espejo Drive).
2. `-DWGUNITS` → 6 Meters → Decimal → Precision 4 → Scale on insert Yes → Match INSUNITS Yes → Scale existing No. Verifica `UNITS` decimal + Insertion Meters.
3. `SCALELISTEDIT` → Delete all → cerrar/reabrir DWG (regenera ajustada a metros) → Add `1:50 (m)` Paper 1 / Drawing 0.05. Aplica por nombre, nunca factor crudo.
4. `LAYER` → 29 propias §2 spec (tabla completa en spec; acá resumen operativo): `REP-EJES` 81 DASHDOTX2 bloq · `REP-COTAS` 41 · `A-COTA-1-50` 250 · `A-EJES` 90 DASHDOT bloq · `A-EJES-VACIOS` 113 · `E-EJES` 10 cong · `E-COL-EJES` 254 bloq · `IE-EJEX` 32 cong+bloq · `A-MURO-MAMP` 24 · `A-MURO-MED` 11 bloq · `E-COL` 5 · `E-TAB` 166 · `A-TERRENO` 163 cong · `A-CARP-02` 251 · `SIMB-CARP` 33 · `SIMB-MURO` 251 · NPT 251 · fondo `A-EQUIP-` 8 / `A-SOLADOS` 250 / `CONDUCTOS` 3 · base `0`/`0-REF`/`Defpoints` · paper `ROT-HOJA` 5 / `ROT-TXT` 174 / `ROT-VP` 130 Plot No.
5. `STYLE` → 9 medidos (`cotas-50` h 0.16, `COTAS`, `style2`, `Standard`, `MBA25`, `ROMANS`, `ROT` mm). `DIMSTYLE` → `COTAS-ARQ-50` tick `_ArchTick` + `REPLANTEO 150` `_Open90`.
6. `LAYOUT` New → renombra `REP-PTipo-A1` → `PAGESETUP` → `DWG To PDF.pc3` → ISO full bleed A1 841x594 landscape → Plot area Layout → Plot scale 1:1 → `MVIEW` 1 ventana → clic dentro → `ZOOM 20 XP` → verifica `1:50 (m)` → Display Locked Yes.
7. `PAGESETUP` → Plot style table `monochrome.ctb` (vigente, viene con todo AutoCAD) → guarda en ruta tablas (`OPTIONS` → Files). Prueba plot: todo negro, mide 20 mm por cada metro en viewport 1:50.
8. `SAVEAS` DWT + `SAVEAS` DWS (`SET-REP.dws` misma base). Asocia vía Configure Standards.
9. **LT 2024+ Win (vigente en el estudio):** `APPLOAD` → `lisp/SET_01-REP.lsp` → `SET-REPLANTEO` en dibujo limpio → verifica 29 capas ([LISP en LT](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Unable-to-load-lisp-in-AutoCAD-LT.html)). Con `SECURELOAD = 1` y `TRUSTEDPATHS` vacío, AutoCAD pide confirmar la ruta de búsqueda al cargar: agregar la carpeta a *Ubicaciones de confianza* o contestar Sí/Continuar. LT 2023- / LT Mac (`Unknown Command`): setup manual pasos 2-8, el DWT ya trae todo.
10. **⚠ LT — límites del entorno:** sin COM/ActiveX externo → el MCP `autocad` del vault no llega al LT y la automatización del CAD va por AutoLISP. Instalación real: `C:\Program Files\Autodesk\AutoCAD LT 2027`. El AutoCAD 2027 full (instalador en `P:\autocad\AutoCAD.2027_English_64bit`) devuelve la vía COM y el `STANDARDS`/`CHECKSTANDARDS` en pantalla.

## 1.5 Bloques en memoria + palettes (LT sí)

Memoria = definiciones dentro del DWT/plano (pestaña Current Drawing de Blocks palette). Organización vigente:

* DWT SET_01 trae en memoria solo lo general + replanteo (13): (a) Vanos dinámicos 2: `VENTANA BAJA SIMPLE`, `PUERTA BATIENTE` en `A-CARP-02` · (b) Tags/niveles 5: `SIMB-MURO`, `SIMBOLO DE EJE`, `SIMBOLO NIVEL PISO CORTE`, `C40.20`, `Tabela_Esquadrias` · (c) Carátula 1: `G-CART-MEPA` en `ROT-*` + 4 puntas de cota. Cada `INSERT` fija capa de inserción + punto (vanos al centro, tags horizontales) según [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/bloques-personalizados|bloques-personalizados]].
* **Bloque nuevo (fuera del DWT por ahora):** `SIMB-LOC_ID` — rectángulo 0.30 × 0.30 m + `N_LOC` visible (número) + `TXT_LOC` invisible (nombre). Se crea e inserta con `lisp/SET-01-SIMB-LOC-ID.lsp` (comando `SIMB-LOC_ID`, control `LOC-ID-CHECK`, diagnóstico `LOC-ID-DIAG`). **Estado 21/10:** bloque definido y probado en LT, con **0 ejemplares** en REP-ARAOZ → los 28 locales siguen numerados a mano sobre los rótulos legacy `*U482`.
* Generales vs disciplina: `GEN-` (niveles corte/vista/planta, ejes, norte, escala gráfica) viven en DWT SET_01; `SAN-`, `ELE-`, etc. (artefactos, bocas, tableros) viven en bibliotecas por disciplina (`SET_XX-YYY_bloques.dwg`), fuera de memoria SET_01 — entran vía Libraries/DesignCenter solo cuando el SET los pide. Así la memoria avanza liviana y cada disciplina avanza con su madre.
* Nivel dinámico que mide (**a construir**): un solo bloque `GEN-NIVEL` con visibilidades Corte/Vista/Planta + `Block Table` que alinea atributo `NPT` con visibilidad ([attribute + visibility via Block Table](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Connecting-attribute-values-to-visibility-states-for-dynamic-blocks-in-AutoCAD.html)). En corte suma grip linear/stretch para altura gráfica + `NPT` editable (semi-auto; el cómputo sale por LSP en LT, ver §3); evita anidados con visibilidades y `COPY` con portapapeles dentro de `BEDIT` ([avoid duplicates](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Dynamic-block-entities-are-duplicated-after-modifications-are-made-using-the-Block-Editor-in-AutoCAD.html)).
* Palettes LT: `TOOLPALETTES` → New Palette `SET_01-REP` → arrastra desde DesignCenter (`ADCENTER` → dibujo madre → Blocks) o desde `SET_01-REP_bloques.dwg`; por herramienta fija Description (tooltip) + Layer por defecto (crea la capa si falta) + escala/ángulo según [Tool Palettes LT](https://help.autodesk.com/view/ACDLT/2027/ENU/?guid=GUID-6668905A-3FAD-4EED-82A2-5D6177AD4280). Separa con texto/separadores en grupos GEN / REP / disciplina. Comparte vía Drive: exporta `.xtp` + apunta Support Path a `W03-CAD/SET_01-REP/` ([share palettes](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-share-tool-palettes-containing-custom-blocks.html)).
* Blocks palette como alternativa sin palettes: Libraries tab → Browse a `SET_01-REP_bloques.dwg` (biblioteca) o Current/Recent/Favorites en el plano ([Blocks palette](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-E3413A03-8EEF-44D5-B5C7-8B345A9257FE) · [symbol libraries](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-create-and-organize-symbol-libraries-in-AutoCAD.html)). Si un nombre ya existe en el plano, manda la definición local: actualiza con re-`INSERT`/`-INSERT`, nunca con `EXPLODE`.

## 2. Dibujo (12 pasos, solo set + básicos)

Plantilla lista arriba. Xref fondo `XREF ATTACH ARQ-ARAOZ` en `0-REF` si aplica.

1. Terreno `LINE` en `A-TERRENO` (referencia congelada, avanza intacta).
2. Ejes `LINE` en `REP-EJES` + `INSERT SIMBOLO DE EJE` en extremos (≥2 principales, nunca sobre LM/divisorios ni huecos escalera).
3. Muros `OFFSET` desde ejes según espesor en `A-MURO-MAMP` (medianeros `A-MURO-MED` bloqueada: avisa antes de tocarla).
4. Columnas/tabiques `RECTANG` en `E-COL` / `E-TAB` + tag `C40.20`, acotados a ejes.
5. Vanos `INSERT VENTANA BAJA SIMPLE` / `PUERTA BATIENTE` al centro del vano en `A-CARP-02`. Estira con grips azules, avanza con bloques intactos.
6. Atributos `TIPO`/`ANCHO` al insertar (`V01`, `2.30`). Puertas suman `ALFEIZAR/ALTURA`.
7. Tags `INSERT SIMB-MURO` + `SIMBOLO NIVEL PISO CORTE` horizontales (rotación 0).
8. Cotas `DIMLINEAR` estilo `REPLANTEO 150` cadena parciales + segunda cadena acumuladas en `REP-COTAS`, por fuera de locales. Estructura desde ejes, mampostería a filos, vanos a ejes.
9. Textos `MTEXT` estilo `cotas-50` para locales. NPT por piso.
10. `ATTSYNC` + `REGEN` si un atributo avanza oculto.
11. `CHECKSTANDARDS` vs `SET-REP.dws` → Fix/Next → `AUDIT` → `PURGE`.
12. Layout `REP-PTipo-A1` → `PLOT` PDF 1:1 + viewport 1:50 bloqueado. `FIELD` en `ESCALA` apunta a viewport 358 (Move Up si duplica, `REGEN`).

## 3. Cómputos

**⚠ LT 2027 (vigente en la máquina del estudio):** `DATAEXTRACTION` **no existe** (*Unknown command*; el help oficial de AutoCAD LT dice *"AutoCAD LT doesn't support data extraction commands"*). Las vías reales son:

| Vía | Qué | Estado |
|---|---|---|
| `ATTEXT` + `LIST` | Extrae valores de atributos a un archivo de texto con plantilla | alternativa oficial en LT |
| LSP que dibuja la tabla dentro del DWG | lee el CSV y dibuja la tabla (patrón de `SET-01-CUADRO-NIVELES.lsp`, capa `A-CUADRO-NIVELES`) | **usada en REP-ARAOZ** |
| `TABLA` + vínculo de datos (`DATALINK` → `-TABLE` → `ACTUALVINCUDAT`) | tabla viva ligada al CSV | ⚠ exige Excel instalado + proveedor ACE/OLE DB (sin Excel, el preview queda vacío) |
| `DATAEXTRACTION` → CSV → Sheet | el flujo original | solo en **Full**; en pausa desde el 20/10 |

Columnas del cuadro de carpinterías en [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/cuadro-carpinterias|cuadro-carpinterias]].

**Medición del plano real (REP-ARAOZ):** 28 locales numerados `01`…`28` (rótulos legacy `*U482`, numeración puesta a mano) → planilla en [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/planilla-locales|planilla-locales]]; niveles del proyecto (14 filas × 3 columnas) → [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/planilla-niveles|planilla-niveles]].

## 4. Reglas madre

- Bloques avanzan intactos (conservan atributos y cómputos).
- Cotas escritas mandan sobre medición en pantalla.
- Capa bloqueada = pedir permiso (`REP-EJES`, `A-MURO-MED`, `E-COL-EJES`).
- Cota que difiere de acumulada = avisa, avanza con registro.
- Todo vano incluye código; si falta, consulta, avanza con código asignado.

Lectura previa JR: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/guia-jr-replanteo|guia-jr-replanteo §§3-4]] + glosario (eje, parcial/acumulada, vano, filo, NPT, medianero, wipeout).
