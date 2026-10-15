---
tipo: research-sherlock
fecha: 2026-10-15
slug: autocad-cocina-bhindu
fuentes_n: 25
confianza: Alta (oficial Autodesk vía MCP Help API, bodies completos)
idioma: ES/EN
entregado_por: vaultworm-arq-exterior
estado: pendiente-formato
timezone: America/Argentina/Buenos_Aires
fuente_dwg: D:\Users\Solch\Desktop\AUTOCAD\TRABAJOS-AUTOCAD\CONSTANZA SERANTES\Cocina02\COCINA-BHindu.dwg
---

# Links AutoCAD cocina — 2026-10-15

> Fecha: 2026-10-15 | Fuentes N: 25 oficiales + 14 exteriores curadas | Confianza: Alta (Help Autodesk vía API)
> Caso: DWG cocina argentina planta 1:50 + vistas 1:20. Vault guarda solo .md con ref por ruta. Frente 1 MCP: sin sesión AutoCAD activa — inspección directa pendiente.

## Resumen

- Flujo pro cocina: Model 1:1 mm + Layouts 1:1 papel + Viewports 1:50 (0.02) / 1:20 (0.05) + anotativos 2.5 mm papel habilitan planta + vistas desde un único modelo.
- Kit estudio: DWT + DWS + CTB + Sheet Set DST + Fields en rótulo consolida calidad repetible sin retrabajo de seteos.
- Bloques dinámicos muebles (stretch/visibilidad/flip/lookup) + hatches asociativos + cotas anotativas cubren el núcleo de automatización interiorismo.
- Publish PDF multipágina + Page Setups + eTransmit resuelven entrega con trazabilidad + índice automático desde DST.
- Starter LISP 6 rutinas integra todo en comandos de una línea, cargado vía Startup Suite / acaddoc.lsp.

## Ejes con citas inline

### 1. SHEETS — SSM, Layouts, Viewports (lo que nunca se entendió)

- SSM gestiona colecciones de sheets: crea/abre sets, subsets, propiedades, numeración automática, importa layouts, publica a PDF y transmite (Autodesk Help ACD 2026, About Sheet Set Manager for Web) [4].
- Trabajo colaborativo: cada integrante accede al DST + DWT asociados para crear sheets con misma plantilla y page setups estandarizados (Autodesk Help ACD 2026) [4].
- MODEL = taller 1:1 real (mesada 600 fondo, largo 3600); LAYOUT = hoja papel 1:1 (A3 420x297 + rótulo); VIEWPORT = ventana con lupa calibrada (0.02=1:50 planta, 0.05=1:20 vistas, Lock Yes); SHEET = ficha administrativa sobre el Layout (número/título/revisión/subset en DST, rótulo vía Field).
- Viewport con escala incorrecta o lista de escalas sucia rompe plot: dibujar 1:1 en model, layout 1:1 en paper, chequear Custom scale en Properties (Autodesk support, Incorrect scale viewport) [V2].
- Si no se ve contenido en viewport: revisar VP Freeze, color 255 vs White, escala anotativa vs escala viewport, `REGENALL`, `ANNOALLVISIBLE=1` (Autodesk support, Drawing elements do not show within viewport) [V4].

### 2. Anotativos 1:50 / 1:20

- Texto/cota con propiedad anotativa ajusta altura según escala viewport y mantiene 2.5 mm papel en ambos (Autodesk support, Annotation objects change scale) [V3].
- Escala 1:50 mal definida (1 Paper = 0.02 Drawing en vez de 20) rompe texto en layout; corregir con `SCALELISTEDIT` + `ANNOAUTOSCALE=1` (Autodesk support, Wrong annotative text scaling) [V1].
- Hatch dentro de bloque sigue viewport si el hatch es anotativo + escalas agregadas a la lista (Autodesk support, Hatch inside block viewport scale) [V5].

### 3. Bloques dinámicos cocina

- Bloques dinámicos incluyen reglas que controlan apariencia al insertar/editar, solo 2D; Block Editor (BEDIT) + paleta autoría con parámetros/acciones/restricciones (Autodesk Help ACD 2027, About Dynamic Blocks) [D2].
- Un bloque cambia forma/tamaño/configuración en vez de familia estática (ej. mesa redonda 4 sillas vs rectangular 8; análogo mesada 600 vs 900) (Autodesk Help ACD 2027, Dynamic Blocks) [D4].
- Parámetros anidados no se controlan desde padre salvo vía LISP/VBA custom o Field a parámetro (Autodesk support, Controlling nested dynamic blocks) [D5].

### 4. DWT / DWS / Rótulo Fields

- DWT incluidos con title blocks `Tutorial-*`; paths `C:\Program Files\Autodesk\AutoCAD...\Template`; buscar `AutoCAD title block template` para externos (Autodesk support, Title block templates) [T1].
- Fields copiados vía Design Center muestran `######` si pierden contexto; crear DWG nuevo desde DWT resuelve (Autodesk support, Fields Show ######) [T2].
- Conflicto nombre bloque al importar layout reemplaza rótulo; renombrar con `REN` antes de importar (Autodesk support, Title block replaced) [T5].
- CAD Standards centraliza layers, text/dim/linetype/multileader/table/detail/section styles, layouts, sheet set guidelines, ByLayer/ByBlock; tools `BEDIT/WBLOCK/LAYER/STYLE/DIMSTYLE/LINETYPE/MLEADERSTYLE/TABLESTYLE/LAYOUT/SAVEAS-DWT/ADCENTER/LAYTRANS/STANDARDS/Batch Checker` (Autodesk Help OARX 2027, CAD Standards) [T4].

### 5. Publish / Plot + LISP

- Publicar set es más eficiente desde SSM que desde diálogo Publish; flyout Publish to DWF/DWFx/PDF/Plotter; `BACKGROUNDPLOT` off acelera (Autodesk Help ACD 2027, To Publish Sheet Set) [P5].
- `PUBLISHCOLLATE=1` combina en un multipágina; `=0` genera individuales (Autodesk support, Publish creates multiple vs single) [P2].
- Para mono desde SSM: Page Setup con `monochrome.ctb` + Publish Using Page Setup Override (Autodesk support, Publish monochrome) [P3].
- Si solo sale primera hoja: revisar Publish Options, DST corrupto, `BGCOREPUBLISH=0`, PC3 `DWG to PDF` (Autodesk support, Only first sheet published) [P4].
- Lisp startup incompatible con Core Console rompe publish background; aislar `acad.lsp`/`acaddoc.lsp` (Autodesk support, SSM Plot background Lisp) [P1].

## Fuentes APA idioma original

OFICIALES FRENTE 2 (verificadas vía `autodesk-help_search_help_content` 2026-10-15, bodies completos):

- Autodesk. (s.f.). *Sheet Set Manager - DST File Not Found*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Sheet-Set-Manager-DST-File-Not-Found-when-opening-files-in-AutoCAD-2024.html
- Autodesk. (s.f.). *Sheet Set Manager menus and buttons are disabled*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/sheet-set-manager-menus-and-buttons-are-disabled-in-autocad.html
- Autodesk. (2026). *About Sheet Set Manager for Web* (ACD 2026 ENU). https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-1690E514-A7B0-44EB-8EB0-E1C897D78780
- Autodesk. (2025). *Working with Sheet Set Manager for Web* (ACD 2025 ENU). https://help.autodesk.com/view/ACD/2025/ENU/?guid=GUID-45700EEC-B549-4879-9C8C-7C23AB54B112
- Autodesk. (s.f.). *Wrong annotative text scaling in layout*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Wrong-annotative-text-scaling-in-layout-while-working-in-AutoCAD-LT.html
- Autodesk. (s.f.). *Incorrect scale when setting up viewport plot scale like 1:100*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Incorrect-scale-when-setting-up-viewport-plot-scale-in-AutoCAD.html
- Autodesk. (s.f.). *Annotation objects change scale*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Annotation-objects-change-scale-without-making-changes-to-the-annotative-scale.html
- Autodesk. (s.f.). *Drawing elements do not show within a layout viewport*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/drawing-elements-do-not-show-within-a-viewport.html
- Autodesk. (s.f.). *Hatch inside block follows viewport scale*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Is-it-possible-to-use-a-hatch-pattern-inside-a-block-where-the-scale-of-the-hatch-automatically-follows-the-scale-of-the-viewport-in-AutoCAD.html
- Autodesk. (s.f.). *BLOCKREPLACE fails to replace dynamic blocks*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/BLOCKREPLACE-fails-to-replace-dynamic-blocks-in-AutoCAD.html
- Autodesk. (2027). *About Dynamic Blocks* (ACD 2027 ENU). https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-3C2FB982-3AF6-437B-987F-4EDF81EA0662
- Autodesk. (s.f.). *Creating custom Parameters Sets for Dynamic Blocks*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Creating-custom-Parameters-Sets-for-Dynamic-Blocks.html
- Autodesk. (2027). *Dynamic Blocks* (ACD 2027 ENU). https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-2A3D92B8-20E2-47B3-92CE-FB3EB03888C3
- Autodesk. (s.f.). *Controlling parameters of nested dynamic blocks*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Controlling-parameters-of-nested-dynamic-blocks-from-parent-block-in-AutoCAD.html
- Autodesk. (s.f.). *Where to find title block templates*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Where-to-find-title-block-templates.html
- Autodesk. (s.f.). *Fields Show ###### When Importing Layouts*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Fields-Show-When-Importing-Layouts-via-Design-Center-in-AutoCAD-Products.html
- Autodesk. (s.f.). *Title block on imported layout gets replaced*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Title-block-on-an-imported-layout-gets-replaced-by-existing-block-in-AutoCAD.html
- Autodesk. (2027). *About Creating and Managing CAD Standards* (OARX 2027). https://help.autodesk.com/view/OARX/2027/ENU/?guid=GUID-9985B23D-C42D-431D-B766-D1E5FE3ECC07
- Autodesk. (s.f.). *SSM Plot or Publish in background does not plot*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/SSM-Plot-or-Publish-in-background-does-not-plot-in-AutoCAD-Products.html
- Autodesk. (s.f.). *Publish from SSM creates multiple sheets instead of single*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Publish-from-Sheet-Set-Manager-creates-multiple-sheets-instead-of-single.html
- Autodesk. (s.f.). *How to publish all sheets in monochrome*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-publish-all-sheets-in-a-sheet-set-in-monochrome-from-AutoCAD-products.html
- Autodesk. (s.f.). *When Publishing to pdf only first sheet is published*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/When-Publishing-to-pdf-in-AutoCAD-only-first-sheet-of-the-sheetset-is-published.html
- Autodesk. (2027). *To Publish a Sheet Set* (ACD 2027 ENU). https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-1484D4DE-BE0C-4FF6-BDA1-6F020DA3A177

EXTERIORES CURADAS (subagente vaultworm-arq, verificadas vía Help API):

- Autodesk Help. *How to setup Layouts in template*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-setup-Layouts-in-template-drawing-in-AutoCAD.html
- Autodesk Help. *How to use annotative text and dimensions*. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-use-annotative-text-and-dimensions-in-AutoCAD.html
- Autodesk Help. *About Using Annotative Objects*. https://help.autodesk.com/view/ACD/2027/PTB/?guid=GUID-590DE319-FD23-45FE-8430-D3EF4AB989D2
- Autodesk Help. *About Contextual Fields / Using Fields in Text*. https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-D32A29E7-7B98-4ADB-BF32-5CC24DBCC8C3
- Autodesk Help. *To Create Drawing Template / Standards / Batch Checker / LISP load / Publish multiple / eTransmit*. (ver lista completa en stub)

## Metodología queries por idioma + URLs + status + gaps

- `get_available_products` → OK, AutoCAD `ACD` releases 2021-2027 validado.
- EN `AutoCAD sheet set manager sheets layouts DST` → 5 hits OK (SSM Web + DST not found + disabled menus).
- EN `AutoCAD layout viewport scale annotative 1:50` → 5 hits OK (wrong anno scale, incorrect 1:100, anno change, viewport not show, hatch anno block).
- EN `AutoCAD dynamic blocks kitchen furniture` → 5 hits OK (BLOCKREPLACE, About Dynamic 2027, custom param sets, Dynamic overview, nested params).
- EN `AutoCAD DWT template DWS standards fields title block` → 5 hits OK (title templates, Fields ######, CAD Standards OARX, title replaced).
- EN `AutoCAD AutoLISP automate publish plot sheet set` → 5 hits OK (SSM background Lisp, PUBLISHCOLLATE, mono override, only first sheet, To Publish 2027).
- Locale `en_US` (Help ENU completo; `es_ES` con menor cobertura para SSM/BEDIT, se prioriza ENU + traducción propia).
- Webfetch directo a support.autodesk.com → 403 bot-protection (verificado vía API que entrega body, se cita API como fuente).
- Gaps: sin sesión AutoCAD viva → `layers/blocks/layouts/entities/screenshot` pendientes; YouTube interiorismo no incluido (URLs no 100% verificables, queda ciclo 2 con Autodesk University).

## Propuestas wiki (esqueleto, no crear)

- Amplía [[wiki/glosario/software/autocad\|AutoCAD]]: §§ Dinámicos cocina, Anotativos 1:50/1:20, DWT/DWS, SHEETS/SSM, Publish/eTransmit, LISP starter.
- Crea [[wiki/estudio/instructivo-plano-cocina-autocad\|instructivo-plano-cocina-autocad]] + [[wiki/estudio/sheets-autocad-layouts-viewports\|sheets-autocad-layouts-viewports]].
- Dependencias: [[wiki/glosario/software/00-index\|índice software]] · [[raw/contenidos/sherlock-cocina-bhindu-2026-10-15-pendiente-formato\|stub]] · `opencode.json` (MCP autocad).

¿Avanzo a curaduría? (s/N) para @contenidos → reporte legible → @vaultworm-arq escribe wiki/glosario con s.
