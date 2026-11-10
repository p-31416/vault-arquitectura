---
tipo: research
fecha_creacion: 2026-11-10
ultima_actualizacion: 2026-11-10
tags: [sherlock, marcas, bloques-cad, bim, electrica, sanitaria, argentina, floss]
idioma: es
---

# Marcas CAD con atributos + BIM mínimo sin licencias (AR eléctrica + sanitaria) — 2026-11-10

Fecha|Fuentes N|Confianza
---|---|---
2026-11-10 America/Argentina/Buenos_Aires|31 (14 fetch 200 + 17 excerpts)|Alta (portales globales oficiales) / Media (FV/Ferrum/Tigre/Saladillo con form) / Baja (IMSA/Cambre/Jeluz/Kalop/Aquarella sin portal)

## Resumen

- Usuario quiere por marca: CAD en bloques DWG/DXF con atributos + BIM mínimo (IFC/RVT/RFA) usable sin pagar licencias (sin Revit/AutoCAD pagos, usable en FreeCAD/Bonsai/QCAD/LibreCAD).
- Hallazgo central: las 5 globales eléctricas/sanitarias SÍ dan gratis (Schneider, ABB, Siemens, Legrand/Bticino, Roca). Las 4 sanitarias AR SÍ dan gratis (FV, Ferrum, Tigre/IPS, Saladillo). Las 5 eléctricas AR (Prysmian, IMSA, Cambre, Jeluz, Kalop) + Aquarella/Rotobras NO dan BIM/CAD oficial: solo catálogo PDF/ficha.
- Ninguna marca da DWG con atributos listo (MARCA/CODIGO/DN/VOLTAJE). Solo TigreBIM plugin (código+descripción+cuantificación auto + dirección de flujo y elevación) y MEPcontent EMCS / Siemens VDI 3805 dan datos de cálculo. Todo lo demás es geometría + dimensiones/IP/IK/material.
- Licencia común: gratis para usar en proyecto (especificar/insertar), prohibida la redistribución como librería propia. No se puede republicar RFA ajeno como CC BY-SA. La librería AR propia debe ser redibujada (trazar sobre STEP/IFC/DXF como referencia, símbolos AEA/IRAM/AySA propios).
- Vía sin licencias: IFC + STEP + DXF/DWG abren en FreeCAD/Bonsai/QCAD. RFA/RVT solo abre en Revit (pago/viewer). Por eso el ranking usable-FLOSS es: Bimetica (FV, IFC+DWG) > TigreBIM catálogos (DWG+RFA) > Saladillo (form, presumible RFA) > BIMobject/Bim&Co/MEPcontent filtrando IFC/DWG > TraceParts STEP/DWG (solo industria) > Bibliocad comunitario (solo referencia, licencia riesgosa).

## Ejes

### 1. Eléctricas globales: todo gratis con registro gratis

**Schneider Electric — portal oficial doble.** `BIM Library` (modelos Revit de media/baja tensión: switchboards, transformers, metering, panelboards) + `CAD Drawings Download Center` (+2000 DWG 2D) + `LayoutFAST for BIM` (plugin Revit que inserta desde la nube). Requiere login mySchneider (gratis). Formatos: RFA/RVT + DWG 2D. Licencia: uso en proyecto, no redistribución. Calidad: tableros con datos eléctricos (potencia, protecciones), aparataje chico solo geometría. Alternativa sin login: NBS Source (`source.thenbs.com` perfil Schneider, RFA free). Status: `se.com/ww/.../building-information-modelling` dio 403 a webfetch (anti-bot Cloudflare) pero existe y es citado por NBS + `se.com/us/.../cad-drawings` (excerpt 200). No es 404.

**ABB — el mejor combo abierto.** `library.abb.com/share?q=bim` lista PUBLIC sin login: `ABB-BIM-*.rfa` (0.5–66 MB, ej. S200 MCB, ReliaHome Load Centers, TLE UPS), partes IFC separadas (`...IFC` 2–5 MB), combos `BIM Files (.rfa_.ifc_.dwg)` en ZIP (ej. free@home Zenit `9AKK108470A7653` RFA+DWG+IFC 1.76 MB), DWG sueltos (`D13 15 DWG files` ZIP 9 MB) y EPLAN EDZ (`9AAC204436_EPLAN`). Registro opcional (algunos docs solo registrados). Formatos: RFA + IFC + DWG + EDZ + STP. Licencia: PUBLIC = uso libre en proyecto (cada ficha dice `Revit BIM model. Family may be copied or loaded into project`). Calidad: tableros/UPS con datos, mecanismos solo geometría + dimensiones. Verificado: fetch 200 (contenido JS mínimo pero URL viva, excerpts con IDs de documento).

**Siemens — dos vías, la buena es CADENAS.** Vía A: `siemens-bt.partcommunity.com/3d-cad-models` (portal CADENAS, 8500 productos building automation + fire safety, hasta 100 formatos: AutoCAD >=V14, Revit 2017–2021, STEP, IFC vía 3Dfindit, BMP/GIF 2D). Registro gratis en PartCommunity. Vía B: `siemens.com/.../bim-data` (SIMARIS: tableros ALPHA DIN/NF, switchgears, busbars, transformadores SINAMICS G150 — descarga RFA directa o configura en SIMARIS Project gratis y exporta IFC). Calidad: la única con norma de datos declarada (ISO 16757 / VDI 3805, características VDI para cálculo hidrónico/eléctrico). Licencia: uso en proyecto. Verificado 200.

**Legrand/Bticino — BIMobject + e-catalogue directo con IFC/STEP.** Página oficial deriva a `bimobject.com` (familias: armoires/coffrets, Cablofil, boîtes de sol, Céliane/Mosaic/Plexo/dooxie, Green'up). Cada ficha e-catalogue trae además `CAD & Design specs / BIM`: ej. Batibox 080041 con `BIM-LEGRAND-MOSAIC-2026-ENGLISH.rvt` 143 MB + `3D_LG-080041.stp` marcado IFC 17 MB. Formatos: RVT + RFA (vía BIMobject) + IFC + STP. Registro BIMobject gratis. Datos: IP/IK/agrements, dimensiones, colores, clasificación IFC/Uniclass, región de comercialización. Sin conectores MEP de cálculo (aparataje = terminal). Verificado 200.

### 2. Eléctricas AR: sin portal (gap que justifica librería propia)

**Prysmian (ex-Pirelli) — sin BIM/CAD.** Solo catálogos PDF, `CableApp` (app de selección, no bloques), DirectIndustry/Scribd con shortform. Sin RFA/DWG/IFC oficial. En BIMobject categoría `Electric cables` hay cables genéricos pero ningún perfil Prysmian AR.

**IMSA / Cambre / Jeluz / Kalop — sin BIM/CAD.** Verificados: `cambre.com.ar` 200 (solo Productos/Profesionales/Dónde comprar, sin Descargas BIM), `kalop.com.ar` 200 (Descargas = Catálogo, Fichas Técnicas, Certificados, Banco de imágenes — sin RFA/DWG), `jeluz.net` (sección Descargas = material comercial, sin bloques; excerpts tienda), IMSA sin sitio con biblioteca (solo tiendas que venden IMSA). Ninguno publica DWG con atributos ni RFA. Gap explícito.

Consecuencia: para AEA/IRAM (tomas, llaves, tableros, caños) hay que dibujar librería propia: símbolos 2D DWG con ATTRIBUTES (MARCA/CODIGO/TENSION/CORRIENTE/NORMA) + sólidos IFC mínimos (IfcDistributionElement) en FreeCAD. Referencia dimensional: fichas PDF de cada marca.

### 3. Sanitarias: las 4 AR sí dan (desigual)

**FV Grifería — doble fuente, la mejor AR.** A) `portafoliofv.com/descargasfv` (Bibliotecas BIM-FV: filtro por GRIFERIA/SANITARIOS + Archivo REVIT, descarga RFA directa, gratis). B) `bimetica.com/bim/es/fv-s-a-/666` (56 objetos, estándar GDO-BIM, categorías Fontanería 9 + Terminales Sanitarias 47: grifería Epuyén/Puelo/Dominic/Arizona + Ofitt L codos/te/uniones/llaves). Registro gratis Bimetica requerido para descargar. Formatos declarados: IFC, Revit, Archicad, Autocad, SketchUp. Calidad: dimensiones/material/acabado/instalación + LEED/Watersense en algunos; sin conectores de cálculo (grifería = terminal). Verificados 200 ambos.

**Ferrum — RFA+CAD por producto.** Cada ficha (`ferrum.com/bidet-andina-...`) lista `Guía de instalación + Bloques Revit + Bloques CAD`. Líneas con familia: Milena, Marina, Bari, Trento, Varese, Veneto, Espacio, Andina (nota ARQA 2021-01-04). Descarga gratis, cuenta opcional (Mis Proyectos). Formatos: RFA + DWG. Calidad: geometría + dimensiones (porcelana ±6.5%), sin datos de caudal/DN. Respaldo comunitario: `bibliocad.com/es/biblioteca/sanitarios/ferrum` 23 bloques (DWG+RFA, ej. inodoro/lavabo/bidet) — licencia comunitaria, solo referencia. Verificado 200 (página con JS pero contenido visible en excerpt + fetch).

**Roca — catálogo masivo vía BIMobject.** `us.roca.com/professional-area/bim-objects`: 2500 productos, 1.7M descargas, 10 formatos (Revit + Archicad + ...), acuerdo Roca–BIMobject 2014. Descarga por producto (Technical Information) o perfil `bimobject.com/en/product?brand=roca`. Registro BIMobject gratis. Calidad: sanitaria completa (artefactos, grifería, bañeras, muebles) con datos de producto, sin cálculo hidráulico. Verificado 200.

**Tigre/IPS — el único con conectores MEP reales.** `tigre.com.br/es/tigre-bim`: plugin TigreBIM gratis (inserción/edición/cuantificación en Revit + AutoCAD, plantillas, catálogos AutoCAD + Revit, info auto: dirección y elevación de flujo, código/descripción/categoría agrupable). FAQ: gratuito, sin activación (solo versión hidráulica MEP comercial de OFCDesk es paga), compatible Revit/AutoCAD 2014–2024 (no LT). Formatos: RFA + DWG vía catálogos + plugin. Calidad: la única con conectores y cómputo (ideal para Hidro3/Awaduct-like). Ojo: catálogo BR (medidas NBR); verificar DN vs IRAM/AySA antes de usar en AR. Verificado 200.

**Saladillo (Awaduct/Rigid/Terra/Hidro3) — biblioteca con formulario.** `industriassaladillo.com.ar/bim.php`: Biblioteca BIM, formulario (Nombre/Apellido/Celular/Email/Empresa/DNI/País/Provincia/Profesión) → solicitar descarga. Gratis, sin pago, con entrega de datos personales. Formato no visible sin completar (presumible RFA por analogía FV/Ferrum; gap a confirmar con descarga de prueba). Respaldo comunitario: `bibliocad.com` accesorios Awaduct DWG por usuario hblazic (347 KB, 40k vistas, dibujados pieza por pieza) — útil como referencia, no oficial. Verificado 200.

**Aquarella/Rotobras — gap.** Sin portal BIM/CAD hallado en ES/EN. Solo tiendas. Gap explícito.

### 4. Plataformas abiertas sin Revit pago (licencia usable en FreeCAD/Bonsai/QCAD)

| Plataforma | URL verificada | Registro | Formatos que abren sin pagar | Licencia | MEP real |
|---|---|---|---|---|---|
| BIMobject | `bimobject.com` (cat. Electric cables Revit/AutoCAD, excerpts) | gratis | RFA (solo Revit) + IFC/STEP/DWG según fabricante | gratis en proyecto, no redistribuir (EULA 2025-06-24) | medio (IP/IK/dimensiones, IFC/Uniclass) |
| Bim&Co / Onfly | `bimandco.com/bim/en` 200 | gratis | .rfa/.skp/.ifc (Smart Download LOD/LOI a elección) + plugin Revit gratis | gratis en proyecto | medio (datos separados geometría/datos, OPMS) |
| MagiCAD Cloud | `magicad.com/cloud/for-designers` (excerpt; faq con 1M objetos, 290 fabricantes) | gratis (porción descargable; full con compra MagiCAD) | RFA + DXF (AutoCAD DXF abre en QCAD/LibreCAD/FreeCAD) — IFC declarado no descargable para diseño | gratis porción | alto (dimensiones exactas + datos técnicos para cálculo MEP) |
| MEPcontent (Trimble) | `mepcontent.com/en/search/findfiles?keyword=+Cable+trays` 200 | sign-in gratis | .RFA + .DWG + .IFC + .RVT (ej. Legrand Cablofil RFA, Spelsberg WKE DWG+RFA+IFC, Legrand XL3 DWG+RFA+IFC) EMCS compliant | gratis en proyecto | alto (EMCS = apto Stabicad/cálculo) |
| TraceParts | `traceparts.com` 200 | gratis | DWG/DXF/STEP/IGES/STL + REVIT (188M códigos, Schneider Electric es supplier) | gratis diseño | bajo-MEP (industrial/eléctrico, no sanitario domiciliario) |
| Bimetica | `bimetica.com/bim/es/fv-s-a-/666` 200 | gratis (login para descargar) | IFC/Revit/Archicad/Autocad/SketchUp (FV 56 GDO-BIM) | gratis en proyecto | medio (grifería terminal) |
| Bibliocad / bloquesautocad / portalbloques | `bibliocad.com/.../ferrum`, `bloquesautocad.com` (excerpts) | sin registro / premium DWG | DWG 2D/3D + algún RFA comunitario | comunitaria sin licencia clara — NO republicar, solo referencia | nulo (geometría muda, sin atributos) |

Sin hallazgo: `Nacional BIM Library` AR no existe como tal (gap/oportunidad). No hay `docs` con atributos por marca.

### 5. Respuesta a "¿las marcas no tienen bloques?" — tabla pedida

| Marca | CAD con atributos (DWG/DXF) | BIM mínimo (formato) | Licencia / registro | Link verificado + estado |
|---|---|---|---|---|
| Schneider Electric | 2D DWG sí, sin atributos (+2000 planos) | RFA/RVT (tableros, trafos) | gratis proyecto / login mySchneider gratis | `se.com/us/en/work/support/resources-and-tools/cad-drawings` — excerpt 200; `se.com/ww/.../building-information-modelling` — 403 anti-bot (existe, no 404) |
| ABB | DWG sí (ej. D11/D13 ZIP) sin atributos | RFA + IFC + DWG en ZIP (lo mejor) | PUBLIC sin login / uso en proyecto | `library.abb.com/share?q=bim` — 200 |
| Siemens | DWG/DXF sí vía CADENAS (AutoCAD >=V14) | RFA 2017–21 + IFC (vía SIMARIS export) + STEP | gratis / registro PartCommunity gratis | `siemens-bt.partcommunity.com/3d-cad-models` + `siemens.com/.../bim-data` — 200 |
| Legrand/Bticino | no DWG con atributos (solo RFA) | RVT + RFA + IFC + STP | gratis / BIMobject gratis | `legrand.fr/.../telechargez-nos-objets-bim...` — 200 |
| Prysmian Pirelli | NO | NO (solo PDF/CableApp) | — | gap (DirectIndustry/Scribd solo catálogo) |
| IMSA | NO | NO | — | gap (solo tiendas) |
| Cambre | NO | NO | — | `cambre.com.ar` — 200 sin biblioteca |
| Jeluz | NO (Descargas = comercial) | NO | — | `jeluz.net` — excerpt 200 sin bloques |
| Kalop | NO (Descargas = catálogo/fichas/fotos) | NO | — | `kalop.com.ar` — 200 sin RFA/DWG |
| FV | DWG vía Bimetica (Autocad) sin atributos | RFA + IFC (+Archicad/SketchUp) 56 GDO-BIM | gratis / registro gratis | `portafoliofv.com/descargasfv` — 200; `bimetica.com/bim/es/fv-s-a-/666` — 200 |
| Ferrum | DWG sí por producto, sin atributos | RFA por línea | gratis / cuenta opcional | `ferrum.com/bidet-andina-...` — 200 (lista Bloques Revit+CAD) |
| Roca | vía BIMobject (DWG según ficha) | Revit + Archicad (+8) 2500 prod. | gratis / BIMobject gratis | `us.roca.com/professional-area/bim-objects` — 200 |
| IPS/Tigre | DWG sí (catálogos AutoCAD) | RFA + plugin (con datos flujo/elevación/cómputo) | plugin gratis / sin activación | `tigre.com.br/es/tigre-bim` — 200 |
| Saladillo/Awaduct | comunitario DWG (no oficial) | biblioteca con formulario (presumible RFA) | gratis / form con DNI+Email | `industriassaladillo.com.ar/bim.php` — 200 |
| Aquarella/Rotobras | NO | NO | — | gap |

Recomendación dónde armar librería AR sin licencias: `activos/libreria-mep-ar/` con 3 carpetas: `01_dwg-atributos/` (QCAD/LibreCAD: símbolos AEA 90364 + sanitarios AySA redibujados, ATTDEF MARCA/CODIGO/DN/VOLTAJE/NORMA), `02_ifc-minimo/` (FreeCAD/Bonsai: IfcDistributionElement con Pset + conectores solo donde Tigre/MEPcontent den base), `03_ref-fabricante/` (solo links + STEP/IFC descargados como referencia, nunca republicados). Base inicial: FV-Bimetica IFC + Tigre DWG/RFA (pasado a IFC vía FreeCAD) + ABB/Legrand IFC donde haya + redibujo propio IMSA/Cambre/Jeluz/Kalop/Prysmian/Saladillo desde PDF. Licencia propia CC BY-SA solo sobre lo redibujado.

## Fuentes (APA, idioma original + [trad. propia])

- Schneider Electric. (s. f.). *CAD Drawings and BIM Content*. Schneider Electric United States. https://www.se.com/us/en/work/support/resources-and-tools/cad-drawings [trad. propia — no oficial]
- Schneider Electric. (s. f.). *Building Information Modeling library | BIM Library*. Schneider Electric. https://www.se.com/ww/en/work/support/building-information-modelling (403 anti-bot, no 404) [trad. propia]
- ABB. (s. f.). *ABB Library — Building information model (RFA/IFC/DWG/EPLAN)*. https://library.abb.com/share?q=bim [trad. propia]
- Siemens. (s. f.). *Access product data for BIM and CAD applications (8,500 products, ISO 16757/VDI 3805)*. https://www.siemens.com/global/en/products/energy/low-voltage/solution-concepts/building-information-modeling.html [trad. propia]
- Siemens. (s. f.). *BIM/CAD data portal (CADENAS PartCommunity)*. https://siemens-bt.partcommunity.com/3d-cad-models/?cwid=1740 [trad. propia]
- Legrand. (s. f.). *Téléchargez nos objets BIM pour réaliser vos plans 3D* [Descargue nuestros objetos BIM para sus planos 3D]. https://www.legrand.fr/pro/outils/applis-logiciels-et-configurateurs/telechargez-nos-objets-bim-pour-realiser-vos-plans-3d [trad. propia]
- FV S.A. (s. f.). *Bibliotecas BIM-FV (Archivo REVIT)*. Portafolio FV Ecuador. https://portafoliofv.com/descargasfv
- Bimetica. (s. f.). *BIM FV, S.A. (56 resultados, estándar GDO-BIM)*. https://bimetica.com/bim/es/fv-s-a-/666
- Ferrum S.A. (s. f.). *Bidet Andina (3 agujeros) — Bloques Revit + Bloques CAD*. https://ferrum.com/bidet-andina-3-agujeros-and-bi-300-bl-1.html
- ARQA Empresas. (2021-01-04). *Bloques Revit, recursos para los diseños de Ferrum*. https://arqa.com/empresas/novedades/bloques-revit-recursos-para-los-disenos-de-ferrum.html
- Roca. (s. f.). *Download Roca BIM objects (2,500 products, Revit/ArchiCAD via bimobject.com)*. https://www.us.roca.com/professional-area/bim-objects [trad. propia]
- Tigre S.A. (s. f.). *Tigre BIM (plugin AutoCAD/Revit, catálogos, FAQ gratuito)*. https://www.tigre.com.br/es/tigre-bim
- Industrias Saladillo S.A. (s. f.). *Biblioteca BIM (formulario)*. https://www.industriassaladillo.com.ar/bim.php
- MagiCAD Group. (s. f.). *MagiCAD Cloud FAQ (1,000,000 objects, RFA/DXF, free subscription)*. https://www.magicad.com/cloud/for-designers/faq [trad. propia]
- Trimble MEPcontent. (s. f.). *Free Revit families & Autocad BIM content (Legrand, EMCS, DWG/RFA/IFC)*. https://www.mepcontent.com/en/search/findfiles?keyword=%20Cable%20trays [trad. propia]
- BIM&CO. (s. f.). *BIM&CO — the high-quality BIM objects platform (.rfa/.skp/.ifc)*. https://www.bimandco.com/bim/en [trad. propia]
- TraceParts S.A.S. (s. f.). *Free 3D models, CAD files and 2D drawings*. https://www.traceparts.com/ [trad. propia]
- BIMobject. (2025-06-24). *Terms of Service (EULA)*. https://business.bimobject.com/terms-of-service-eula [trad. propia]
- Cambre. (s. f.). *Cambre Argentina (sin biblioteca BIM)*. https://www.cambre.com.ar/
- Kalop. (s. f.). *Kalop — Descargas (catálogo/fichas, sin RFA/DWG)*. https://www.kalop.com.ar/
- Jeluz. (s. f.). *Jeluz Argentina*. https://jeluz.net/

## Metodología (queries por idioma + URLs + status + gaps)

Sub-preguntas: (1) eléctricas globales BIM/CAD oficial; (2) sanitarias AR FV/Ferrum/Roca/Tigre/Saladillo; (3) eléctricas AR sin portal (Prysmian/IMSA/Cambre/Jeluz/Kalop); (4) plataformas abiertas gratis + licencia FLOSS; (5) doc oficial primero.

- ES: `FV griferia Ferrum Roca BIM Revit bloques CAD descarga` → 10 res (portafoliofv, ferrum, bimetica, roca). `Cambre Jeluz Kalop IMSA bloques CAD DWG descarga` → 10 res (sin portal, solo tiendas). `IPS Tigre Saladillo Awaduct BIM Revit bloques CAD sanitarios Argentina` → 10 res (tigre-bim, saladillo/bim.php, bibliocad awaduct).
- EN: `Schneider Electric BIM library Revit download free` → 10 res (se.com + NBS Source). `ABB BIM library Revit RFA download EPLAN` → 10 res (library.abb.com IDs 9AKK...). `Siemens BIM Revit Simaris download CAD blocks` → 10 res (siemens.com + partcommunity). `Legrand Bticino BIMobject Revit DWG download` → 10 res (legrand.fr + ecatalogue RVT/IFC). `BIMobject BimAndCo MagiCAD Cloud free download IFC license FreeCAD` → 10 res. `TraceParts Nacional BIM Library Argentina free CAD BIM` → 10 res. `Prysmian Pirelli BIMobject Revit cables DWG download` → 10 res (sin BIM, solo PDF). `BimAndCo free BIM objects license Revit IFC download` → 8 res.
- IT: gap (sin queries IT pertinentes; marcas AR sin presencia IT).

Status webfetch: 200 Siemens-bim-data, FV-descargas, Tigre-bim, Saladillo-bim, Legrand-bim, Roca-bim, Bimetica-FV, TraceParts, Cambre, Kalop, MEPcontent, Bim&Co, Ferrum-ficha, ABB-library (contenido mínimo JS). 403 `se.com/ww/...` (anti-bot, URL existe vía excerpts + NBS). Vacío `magicad.com/.../faq` en fetch directo (contenido en excerpts websearch, no 404). Total 31 fuentes.

Gaps: formatos exactos Saladillo sin completar form; licencias de redistribución (todas prohíben republicar: verificar EULA BIMobject 2025 + términos ABB/Siemens antes de citar texto legal); IMSA sitio oficial no localizado; Aquarella/Rotobras sin portal; Nacional BIM Library AR inexistente; IT n/a.

## Propuestas wiki (esqueleto, no redactar)

- `libreria-marcas-cad-bim` (nueva): tabla del §5 + dónde poner cada descarga en `activos/fuentes/<marca>/` + regla no republicar.
- `fv-bim` (§ o nueva): portafoliofv + bimetica 56 GDO-BIM + formatos IFC/DWG.
- `ferrum-bim` (§): bloques Revit+CAD por producto + líneas con familia.
- `tigre-bim` (§): plugin gratis + catálogos + conectores flujo/elevación + advertencia NBR vs IRAM.
- `saladillo-bim` (§): biblioteca con form + accesorios Awaduct comunitarios.
- `electrica-global-bim` (nueva o § por marca): Schneider/ABB/Siemens/Legrand con formatos y login.
- `plataformas-bim-abiertas` (nueva): BIMobject/Bim&Co/MagiCAD/MEPcontent/TraceParts/Bimetica con filtros IFC/DXF y licencia proyecto.
- `licencia-bloques-comercial` (§ legal): uso en proyecto sí, redistribución CC BY-SA no; librería propia redibujada.

## Candidatos (Nivel 2 — esperar s de SOL)

- NBS Source perfil Schneider (`source.thenbs.com/.../schneider-electric...`) — hub de RFA free, útil si se adopta Schneider tableros.
- Siemens PartCommunity catálogo Americas (`siemens-bt.partcommunity.com`) — hub 8500 productos, candidato a ficha si se usa Siemens.
- MEPcontent Legrand Cablofil / XL3 (`mepcontent.com/en/bim-files/detail/...`) — candidatos si se especifican bandejas/tableros Legrand.
- Bibliocad Awaduct accesorios DWG (`bibliocad.com/es/biblioteca/aaccesorios-awaduct_240002`) — candidato solo como base de redibujo, con s explícito.
- Sin ficha automática para citas dentro de fichas (Nivel 1: verificadas arriba).

---
*Crudo @sherlock — sin formatear, sin template, no wiki. ¿Avanzo a curaduría? (s/N)*
