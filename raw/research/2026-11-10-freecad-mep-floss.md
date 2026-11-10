---
tipo: research
fecha_creacion: 2026-11-10
ultima_actualizacion: 2026-11-10
tags: [research, sherlock, freecad, mep, bim, openbim, floss, electrica, sanitaria, ifc, bonsai]
idioma: es
---

# 2026-11-10 — FreeCAD como opción FLOSS/OpenBIM para instalaciones eléctricas y sanitarias (licencia comercial limpia)

> Fecha|Fuentes N|Confianza
> 2026-11-10|22 (6 fetch 200 + 16 excerpts search 200) + 3 bloqueadas Anubis|Alta (freecad.org + GitHub LICENSE + Cables + HVAC + Bonsai oficial) / Media (madurez MEP: issues + foros OSArch) / Media-Baja (cálculos/documentación AR legal: gaps explícitos)

## Resumen

FreeCAD 1.x (1.0 nov-2024, 1.1 24-mar-2026, 1.1.4 28-sep-2026 vigente) SÍ da licencia comercial limpia (LGPL-2.1: correr el programa para vender planos es uso permitido, copyleft solo si redistribuís el código modificado) y SÍ es núcleo FLOSS válido para arquitectura/OpenBIM (BIM Workbench integrado + Native IFC, IFC2x3/IFC4, TechDraw para 2D). Pero hoy NO es "la mejor opción completa" para MEP eléctrica+sanitaria por sí solo: el propio ecosistema lo declara — "MEP layouts — BIM workbench has limited MEP support" — y los issues 2026 confirman que pipes/ducts eran geometría con tag IFC sin ports de conexión expuestos. Lo que sí existe y funciona: Cables Workbench (externo, LGPL-3.0, v0.4.1 27-oct-2026, 110 stars, WireFlex paramétrico + boxes/conectores/dispositivos, compatible BIM/IFC, con videotutoriales) para eléctrica arquitectónica, y para sanitaria/clima un archipiélago — BIM Arch_Pipe/Connector nativo (2 objetos) + Dodo/Quetzal (sucesor de Flamingo) + OSE-Piping + FreeCAD-HVAC de Francisco-Rosa (LGPL-2.1, 12 stars, DuctNetwork + parser + librería JSON, estado "basic usable", routi­ng paramétrico, cálculo de pérdida de carga como objetivo futuro, no hecho). Bonsai (ex-BlenderBIM, sobre IfcOpenShell LGPL-3.0) va por delante en MEP IFC puro: IfcDistributionPort, IfcDistributionSystem/Circuit, ports editables, docs "Model and manage complex distribution systems like HVAC, plumbing, and electrical". OpenStudio es energía (EnergyPlus/Radiance), no autoría MEP geométrica. QCAD/LibreCAD son 2D (GPLv3/GPLv2), sin BIM/MEP 3D. Recomendación: si la condición es "una sola app FLOSS": Bonsai gana en MEP IFC; si la condición es "CAD paramétrico + planos legales + filosofía FLOSS + todo comercial limpio": FreeCAD como base + Cables + HVAC/Quetzal/OSE + Bonsai como verificador/coordinador IFC + QCAD 2D + KiCad para esquemas. Tokenización (solo contexto): los entregables (FCStd/IFC/PDF) son tuyos, no contagian copyleft; tokenizar a futuro no lo bloquea la licencia, lo bloquearía hoy la inmadurez MEP, no lo legal.

## Ejes

### 1. Estado actual FreeCAD 1.x (2026) para MEP

- Versión: 1.0 (19-nov-2024, merge Arch+BIM+NativeIFC en BIM Workbench integrado) → 1.1 (24-mar-2026, release notes: NativeIFC 2D objects, Schedule arrays, Views panel espacial+2D, ignorar grupos std en export IFC default) → 1.1.4 (28-sep-2026, 30+ bugfixes TechDraw/BIM/UI, sin features nuevas, próxima v26.3). Fuente: freecad.org/features.php 200 + blog.freecad.org excerpts.
- BIM Workbench: objetos paramétricos (muro, viga, cubierta, ventana, escalera, pipes, furniture), Site/Building/Level/Space, materiales, schedules a spreadsheet, TechDraw. IFC clásico (convertir) + Native IFC (documento ES el IFC, sin doble conversión, con pérdida evitada). Soporta IFC2x3 (más difundido) e IFC4 (estándar actual), IFC4.3 infra mencionado. Verificado vía mirrors docs (robertmassaioli.github.io/freecad-docs/bim/concepts/ifc-import-export 200 por search, github FreeCAD-documentation mirrors).
- Eléctrica nativa: NO hay workbench eléctrico en core. Lo cubre Cables (externo, Addon Manager): WireFlex (Draft Wire modificado, vértices attachables a cajas/muros/techos, auto-reforma), Cable Profile/Cable/CableConduit, Box/Connector/LightPoint/Electrical Device (v0.3.0), Terminals/SnapLines, Materials multimaterial, Reports + PartsLibrary (v0.4.0), compatibilidad BIM (Arch Component, IFC attrs). Estado declarado alpha ("expect some bugs which can make your model broken"), requiere FreeCAD >=1.0. Releases 2025-2026 activas (v0.3.0 23-oct-2025, v0.4.1 27-oct-2026). Fuente: github.com/sargo-devel/Cables fetch 200.
- Sanitaria/clima nativa: Arch_Pipe + Arch_PipeConnector (2 objetos, reportado 2024 por paullee en OSArch, sin cambio core 2026 salvo issues). Flamingo (Py2/Qt4) → Dodo (Py3/Qt5) → Quetzal (desde 2024): frame+pype (tubes, elbows, flanges, cálculo fricción tubo recto/codo + Kv para otros), tutorials pump-room. OSE-Piping (CSV NPS, codos, sweep elbows, requiere Dodo). FreeCAD-HVAC (Francisco-Rosa, mar-2026, LGPL-2.1): DuctNetwork contenedor + base routing (sketches/líneas) + DuctNetworkParser (topología/conectividad) + DuctSegment/DuctJunction generados + librería JSON + sincronización al editar base. Goals futuros: routing reutilizable para piping, diffusers/VAV/AHU, pressure drop por caudales, sizing (fricción constante/velocidad/static regain), insulation/supports. Estado: "Basic duct creation reasonably in place", base sólida, no validación/cálculo aún. Fuente: github.com/Francisco-Rosa/FreeCAD-HVAC fetch 200.
- IFC/BCF/COBie: IfcOpenShell (motor) parsea IFC2x3 TC1, IFC4 Add2 TC1, IFC4x1, IFC4x3 + BCF + IDS; utilidades ifccobie/ifcfm/ifcclash/ifcdiff. FreeCAD lo consume vía NativeIFC; Bonsai lo expone completo (audit, costing/scheduling 4D/5D, facility/COBie). BCF-client en canal freecad conda verificado por excerpt. COBie en FreeCAD directo: gap (solo vía IfcOpenShell/Bonsai).

### 2. Comparativa FLOSS/OpenBIM real para MEP

| Herramienta | Licencia (verificada) | Modelado MEP | IFC MEP (ports/sistemas) | Cálculo/documentación | Veredicto eléctrica+sanitaria |
|---|---|---|---|---|---|
| FreeCAD 1.1.x + BIM nativo | LGPL-2.1 (LICENSE fetch 200) | Pipes genéricos sin ports (issue #30308) | Tag IFC sin grafo | TechDraw/Schedules, sin cálculo MEP | Base válida, MEP incompleto solo |
| + Cables 0.4.1 | LGPL-3.0 (GitHub fetch) | Cables/conduits/boxes/dispositivos paramétricos, re-route al mover cajas | Compatible BIM/IFC attrs, no red MEP completa | Reports (nuevo), layers extended | Mejor pieza FLOSS para eléctrica arquitectónica |
| + Dodo/Quetzal + OSE-Piping | LGPL-3.0 (Flamingo/Dodo), OSE GPLv3/LGPL-3.0 | Tuberías/frames, fittings CSV | IFC vía BIM genérico | Pérdida carga parcial (fricción+Kv) | Mejor vía open para sanitaria geométrica |
| + FreeCAD-HVAC | LGPL-2.1 (GitHub fetch) | Duct network paramétrico sincronizado | BIM data objetivo, no ports aún | Pressure drop/sizing futuro | Promesa HVAC, hoy básico |
| Bonsai 0.9.x (Blender) | IfcOpenShell LGPL-3.0 (verif.); Bonsai GPL — gap: no fetcheado, no afirmar versión | HVAC/plumbing/electrical declarados en docs + Create Duct + Services/Systems/Ports panel | IfcDistributionPort/SYSTEM/Circuit, connect/disconnect, flow direction, API ifcopenshell.api.system | Drawings/schedules/clash/COBie/FM, costing/scheduling | Hoy más completo en MEP IFC puro; curva Blender |
| OpenStudio (+SketchUp plug-in) | Open source NREL — gap licencia exacta no fetcheada | No autoría MEP geométrica; energía (EnergyPlus/Radiance), gbXML/IFC solo para geometría | No red MEP | Simulación energética, Measures Ruby/Python | Complemento energía, no sustituto |
| QCAD 3.32 / LibreCAD 2.x | QCAD GPLv3 + excepciones (qcad.org excerpts, fetch redirect); LibreCAD GPLv2 (LWN) | 2D genérico, 4800 partes, DXF/DWG | Sin IFC MEP (DXF/DWG 2D) | Planos 2D a escala, impresión | Útil para esquemas/unifilares 2D, no BIM MEP |
| SolveSpace / otros | gap no buscado a fondo | — | — | — | Descartado para MEP edilicio (mecánico pequeño) |

- Síntesis: ningún FLOSS cubre "todo Revit MEP" hoy. FreeCAD gana en CAD paramétrico + TechDraw + ecosistema Python; Bonsai gana en IFC MEP semántico + coordinación. Híbrido open los combina sin piratería.

### 3. Licencias: uso comercial + estudio AR + tokenización (contexto)

- FreeCAD: LGPL-2.1 (archivo LICENSE 504 líneas verificado fetch 200). "FreeCAD can be used freely for any kind of purpose, being private, commercial or institutional" (wiki License, vía excerpts foro + LWN: LGPLv2+). Correr el programa, modelar y vender planos/servicios: permitido, sin pagar, sin registrar. Copyleft solo si modificás la librería y la redistribuís (debés dar fuente). Output (FCStd/STEP/IFC/DXF/PDF) es tuyo, no contagiado. Forums: "You don't need a special license for commercial purposes. Licensing only becomes an issue if you want to sell the software."
- Cables LGPL-3.0, Flamingo/Dodo LGPL-3.0, OSE-Piping GPLv3/LGPL (dual reportado, verificar al instalar), HVAC LGPL-2.1, IfcOpenShell LGPL-3.0 (anaconda excerpt), mep_engineering comunitario GPL-3.0-or-later. Todos permiten uso comercial; GPL exige compartir fuente solo si distribuís el software modificado, no por usarlo para un cliente.
- QCAD: GPLv3 + excepciones que permiten plugins privativos empaquetados (QCAD Professional = GPL core + extensiones privativas). Podés vender tu trabajo hecho con QCAD Community sin comprar Professional; Professional solo agrega DWG propietario y herramientas extra.
- Estudio argentino / Ley 24.335 (planos = instrumento contractual/registral): la licencia FLOSS no impide firmar/vender planos; lo que manda es matrícula, firma, comitente y norma (CABA/CP). FreeCAD TechDraw + Draft Views → Sheets permite producir 2D a escala, pero "regulatory compliance FreeCAD doesn't auto-enforce" (freecad-app.com). Gap explícito: no se verificó exigencia GCBA/CP para instalaciones (eléctrica/sanitaria) ni incumbencias; va a curaduría/legal, no se afirma aquí.
- Tokenización (solo contexto, no se desarrolla): LGPL/GPL no gravan el activo modelado; podés hashear/tokenizar IFC/PDF/FCStd a futuro sin pedir permiso ni pagar royalty al proyecto FreeCAD. Riesgo real no es licencia sino madurez: si el grafo MEP no tiene ports/sistemas, el gemelo tokenizable nace pobre. Recomendación trazabilidad: guardar FCStd + IFC4 + PDF + JSON de quantities con hash, todo con licencias de datos propias (CC BY-SA si publicás).

### 4. Limitaciones conocidas + workarounds open

- Sin ports/conexiones (core): Issue #30308 (pipes/ducts sin MEP connection points: sin start/end, sin snap fittings, sin auto-elbows/tees, sin network graph, sin mapa a IFC connectivity) + #30309 (falta botón "Add IfcDistributionPort" a Part/Assembly/IFC, ej. bomba sin conexiones). Estado: cerrados 05-oct-2026 como completed pero derivados a workbenches externos (HVAC) — no hay core fix verificado. Workaround: Cables Terminals/Attach Wire to Terminal; Bonsai Services>Ports manual + ifcopenshell.api.system.connect_port; dibujar ejes/sketches como ruta y regenerar (HVAC parser).
- Routing/cálculos: sin autorouter, sin dimensionado eléctrico (caída tensión, selectividad), sin cálculo sanitario (pendientes, presiones, Hunter), sin pressure drop en HVAC (objetivo). Workarounds: Spreadsheet + Python (FreeCAD FEM para estructura, no MEP), KiCad (esquemas eléctricos, StepUp ↔ FreeCAD), OpenStudio/EnergyPlus (cargas), EPANET externo (hidráulica, gap a verificar), cálculo manual en planilla adjunta al IFC vía Psets.
- Documentación: TechDraw inmaduro vs Revit (30+ fixes en 1.1.4, aún lejos de ecosistema familias/anotaciones). Workaround: Draft Views → TechDraw pages a escala (guía Migrating from Revit), export IFC temprano y chequear en Revit/Bonsai (round-trip), QCAD para unifilares/detalles 2D.
- Interop Revit/Archicad/AutoCAD MEP: RVT cerrado (sin soporte en FreeCAD), IFC es el puente pero con pérdidas (ej. pipe FreeCAD exporta círculo extruido que Revit facetó cuadrado; familias scriptadas y sheets no viajan). BCF/IDS ayudan a coordinar. Workaround: IFC2x3 para compatibilidad máxima, IFC4 para nativo; pre-cargar IfcTypes; evitar Brep forzado salvo necesidad; federar con Bonsai (mep_engineering bbox clash 93k elementos validado por autor externo, no oficial).
- Curva/comunidad: Cables alpha (puede romper modelo), HVAC 12 stars/40 commits (un autor), Dodo→Quetzal migración (docs desactualizadas), wiki.freecad.org con Anubis anti-bot (bloquea fetch, dificulta verificación). Workaround: fijar versiones (FreeCAD 1.1.4 + Cables 0.4.1 + HVAC main 2026-03), guardar ejemplos, seguir foro/OSArch + Yorik blog + FCB Lounge.

### 5. Recomendación argumentada

- ¿Es FreeCAD hoy la mejor opción OpenBIM FLOSS única para eléctrica+sanitaria? NO como herramienta única productiva si el listón es "Revit MEP sin pagar". SÍ como base estratégica FLOSS si aceptás stack híbrido 100% open y comercial limpio.
- Stack recomendado (todo FLOSS, todo comercial permitido):
  1. FreeCAD 1.1.4 BIM + TechDraw = autoría paramétrica + planos legales 2D.
  2. Cables 0.4.1 = eléctrica arquitectónica (cajas, circuitos, conduits, reports).
  3. Quetzal/Dodo + OSE-Piping + HVAC Francisco-Rosa + Parts Library = sanitaria/HVAC geométrica + duct networks.
  4. Bonsai 0.9.1 + IfcOpenShell = IFC nativo real, ports/systems, clash, COBie, drawings coordinados, auditoría del modelo FreeCAD.
  5. QCAD/LibreCAD + KiCad + Spreadsheet = esquemas unifilares, tableros, cómputos.
  6. OpenStudio solo si necesitás energía.
- Si solo podés elegir una: para MEP IFC puro elegí Bonsai; para CAD paramétrico + oficina + planos + Python + comunidad hispana/estudio, elegí FreeCAD y federá con Bonsai. No piratees: el costo pasa de licencias a horas de aprendizaje/curaduría, que sí son tokenizables como know-how.
- Próximo paso propuesto (no ejecutado): piloto 2 semanas — modelar baño + cocina + tablero en FreeCAD+Cables+OSE, exportar IFC4, abrir en Bonsai, reportar ports/clash/COBie; con `s` pasa a @contenidos para reporte legible.

## Fuentes APA idioma original + [trad. propia]

1. FreeCAD Team. (2026). *FreeCAD: Your own 3D parametric modeler — Features* [FreeCAD: Tu modelador paramétrico 3D — Características]. https://www.freecad.org/features.php — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-10. Declara BIM integrado desde 1.0, IFC, FCStd, Python.
2. FreeCAD Team. (2024-2026). *LICENSE — GNU Lesser General Public License v2.1* [Licencia]. GitHub. https://github.com/FreeCAD/FreeCAD/blob/main/LICENSE — idioma_original: en (legal) [trad. propia]. Verificada 200 el 2026-11-10. 504 líneas, LGPL-2.1.
3. FreeCAD Team. (2026). *Release notes 1.1 — FreeCAD 1.1 released 24 March 2026* [Notas v1.1]. https://wiki.freecad.org/Release_notes_1.1 — idioma_original: en [trad. propia]. Verificada vía search excerpts (wiki con Anubis bloquea fetch directo, gap documentado). Mejoras BIM: NativeIFC 2D, Schedule arrays, Views panel.
4. Prokudin, A. / FreeCAD News. (2026). *FreeCAD 1.1.4 released* [Versión 1.1.4]. https://blog.freecad.org/2026/09/28/freecad-1-1-4-released — idioma_original: en [trad. propia]. Verificada vía search excerpt. 30+ bugfixes, vigente 28-sep-2026.
5. sargo-devel. (2025-2026). *FreeCAD Cables Workbench — External workbench for cables routing* [Workbench Cables]. GitHub. https://github.com/sargo-devel/Cables — idioma_original: en [trad. propia]. Verificada 200 el 2026-11-10. 110 stars, LGPL-3.0, v0.4.1 27-oct-2026, alpha, WireFlex, BIM-compatible, PartsLibrary/Reports.
6. Francisco-Rosa. (2026). *FreeCAD-HVAC — Workbench to design HVAC ducts* [Workbench HVAC]. GitHub. https://github.com/Francisco-Rosa/FreeCAD-HVAC — idioma_original: en [trad. propia]. Verificada 200 el 2026-11-10. 12 stars, LGPL-2.1, DuctNetwork/Parser/Segment/Junction, librería JSON, pressure drop futuro.
7. oddtopus. (2016-2024). *Flamingo / Dodo Workbench* [Andamios y tuberías]. GitHub https://github.com/oddtopus/flamingo + https://github.com/oddtopus/dodo — idioma_original: en [trad. propia]. Verificada vía search excerpts. LGPL-3.0, pype (tubes/elbows/flanges, fricción+Kv), sucesor Quetzal 2024.
8. rkrenzler. (2018-2026). *OSE Piping Workbench* [Tuberías OSE]. GitHub. https://github.com/rkrenzler/ose-piping-workbench — idioma_original: en [trad. propia]. Verificada vía search excerpt. CSV NPS, requiere Dodo.
9. IfcOpenShell / Bonsai. (2026). *Bonsai Studio — native IFC authoring in Blender* [Autoría IFC nativa]. https://bonsaibim.org/studio.html — idioma_original: en [trad. propia]. Verificada 200 el 2026-11-10. MEP systems, drawings, costing/scheduling, COBie/FM, scriptable Python.
10. IfcOpenShell Contributors. (2026). *Introduction to BIM — Bonsai 0.9.1 documentation* [Introducción a BIM]. https://docs.bonsaibim.org/studio/quickstart/introduction_to_bim.html — idioma_original: en [trad. propia]. Verificada 200 el 2026-11-10. Capacidades: "Model and manage complex distribution systems like HVAC, plumbing, and electrical".
11. Isaina et al. (2026). *Issue #30308: BIM pipes/ducts without MEP connection points* [Tuberías sin ports]. GitHub FreeCAD. https://github.com/FreeCAD/FreeCAD/issues/30308 — idioma_original: en [trad. propia]. Verificada vía search excerpt. Abierto 20-may-2026, cerrado 05-oct-2026 derivado a HVAC.
12. Isaina et al. (2026). *Issue #30309: Add IfcDistributionPort tool* [Agregar ports]. GitHub FreeCAD. https://github.com/FreeCAD/FreeCAD/issues/30309 — idioma_original: en [trad. propia]. Verificada vía search excerpt. Derivado a HVAC por semhustej.
13. Isaina et al. (2026). *Feature request: Generic MEP port model for BonsaiBIM — IfcOpenShell #8085* [Modelo genérico de ports]. https://github.com/IfcOpenShell/IfcOpenShell/issues/8085 — idioma_original: en [trad. propia]. Verificada vía search excerpt. Ports/SOURCE-SINK, system.add_system, connect_port.
14. walpa et al. (2025). *I need a IfcDistributionSystem and Circuit doctor — OSArch* [Sistema y circuito]. https://community.osarch.org/discussion/2764/i-need-a-ifcdistributionsystem-and-circuit-doctor-anyone — idioma_original: en [trad. propia]. Verificada vía search excerpt. Dificultad real MEP en Bonsai, circuitos eléctricos.
15. F_Rosa et al. (2024). *HVAC in FreeCAD — OSArch* [Clima en FreeCAD]. https://community.osarch.org/discussion/2459/hvac-in-freecad — idioma_original: en [trad. propia]. Verificada vía search excerpt. Librería paramétrica + spreadsheet + sheet, solo 2 objetos MEP nativos.
16. BIM Tools Hub. (2026). *FreeCAD: modeling software* [Ficha FreeCAD]. https://bimtoolshub.com/freecad — idioma_original: en [trad. propia]. Verificada vía search excerpt. Cita clave: "MEP layouts — BIM workbench has limited MEP support", "Can't replace Revit on large projects".
17. freecad-app.com. (2026). *FreeCAD BIM — Free Open-Source Architecture & IFC Tool* [Guía BIM]. https://freecad-app.com/workbenches/bim — idioma_original: en [trad. propia]. Verificada vía search excerpt. IFC2x3/IFC4, flujo proyecto, límites MEP/cloud/familias.
18. RibbonSoft. (2026). *QCAD — License / QCAD Professional* [Licencia]. https://qcad.org/en/license/ + https://github.com/qcad/qcad — idioma_original: en [trad. propia]. Verificada vía search excerpts (fetch redirige, contenido vía search). GPLv3 + excepciones plugins privativos.
19. NREL / OpenStudio Coalition. (2026). *OpenStudio — whole building energy modeling* [Energía edilicia]. https://openstudio.net/ — idioma_original: en [trad. propia]. Verificada 200 parcial (JS mínimo) + search excerpts. EnergyPlus/Radiance, SketchUp Plug-in, Measures Ruby/Python, BCL. No autoría MEP geométrica.
20. Prokoudine, A. (2023). *A survey of free CAD systems — LWN.net* [Panorama CAD libre]. https://lwn.net/Articles/921676 — idioma_original: en [trad. propia]. Verificada vía search excerpt. FreeCAD LGPLv2+, QCAD GPLv3, LibreCAD fork GPLv2.
21. red1oon. (2025). *mep_engineering — MEP automation for Bonsai/BlenderBIM* [Automatización MEP]. GitHub. https://github.com/red1oon/mep_engineering — idioma_original: en [trad. propia]. Verificada vía search excerpt. GPL-3.0-or-later, routing/clash/cálculos, experimental, depende federation.
22. FCB Lounge. (2026). *The State of the BIM Library in FreeCAD in 2026 — YouTube* [Biblioteca BIM]. https://www.youtube.com/watch?v=dQyLqMLfluw — idioma_original: en [trad. propia]. Verificada vía search excerpt. Calidad variable library, HVAC con library F_Rosa, FreeCAD 1.1RC2.

## Metodología queries por idioma + URLs + status + gaps

- ES: `FreeCAD MEP instalaciones eléctricas sanitarias OpenBIM` → 0 hits directos ES (gap ES explícito, todo técnico en EN). `FreeCAD licencia uso comercial` → foros confirman uso comercial libre.
- EN (4 rondas × 2-3 variaciones):
  - `FreeCAD 1.0 BIM MEP electrical plumbing workbench 2025 2026` → 8 hits, excerpts 200 (Cables wiki, BIM merge 1.0, release 1.0 blog, issue #30308).
  - `FreeCAD IFC4 BCF COBie support 2025 2026` → 8 hits (IfcOpenShell BCF/COBie, NativeIFC tutorial Yorik, BIM update 28, freecad-app BIM límites).
  - `Bonsai BIM MEP electrical plumbing 2025` + `Bonsai BIM MEP distribution systems` → 12 hits (mep_engineering, OSArch release v0.8.3 MEP ports/flow, docs Project0/Project5 MEP, studio.html).
  - `FreeCAD license GPL commercial use 2025`, `FreeCAD 1.1 release 2026`, `FreeCAD Electrical workbench Wiring`, `FreeCAD flamingo Dodo piping HVAC`, `FreeCAD HVAC Francisco-Rosa MEP`, `FreeCAD BIM limitations MEP Revit`, `OpenStudio LibreCAD QCAD IFC MEP` → 30+ hits.
- Fetch: 200 OK — freecad.org/features.php, github.com/sargo-devel/Cables, github.com/Francisco-Rosa/FreeCAD-HVAC, bonsaibim.org/studio.html, docs.bonsaibim.org/introduction_to_bim, openstudio.net (parcial JS), github.com/FreeCAD/FreeCAD/LICENSE (truncado pero LGPL verificado). Bloqueados Anubis anti-bot (no 404, sino challenge JS): wiki.freecad.org/Cables_Workbench, wiki.freecad.org/Release_notes_1.1, wiki.freecad.org/License, forum.freecad.org — se sustituyeron por mirrors GitHub + excerpts search verificados, se reporta como gap de verificación directa.
- Recencia: 12m salvo normativa/licencias vigentes. Todo MEP 2024-2026 vigente; licencias LGPL/GPL vigentes; Ley 24.335 citada por usuario, no fetcheada (gap legal AR).
- Gaps explícitos: `datos insuficientes ES` (sin docs MEP ES oficiales), `datos insuficientes IT` (no buscado IT por irrelevancia normativa AR), sin transcript YouTube completo (captions bloquean fetch), sin verificación matrícula GCBA/CP para instalaciones, sin prueba hands-on (no se ejecutó código/modelo por regla Sherlock).

## Propuestas wiki esqueleto (no escribir sin s)

- `freecad-mep-floss` (nueva): estado 1.1.4, Cables/HVAC/Dodo/OSE, IFC2x3/IFC4, licencia comercial, límites + stack híbrido.
- `cables-workbench-electrica` (nueva/§freecad): WireFlex, boxes/dispositivos, presets STEP, reports, alpha + videotutoriales.
- `hvac-sanitaria-open` (nueva): Arch_Pipe, Dodo/Quetzal pype, OSE CSV, HVAC DuctNetwork/parser, pressure drop futuro.
- `bonsai-mep-ports` (nueva/§bonsai): DistributionPort/System/Circuit, flow SOURCE-SINK, API system.connect_port, COBie/clash.
- `licencia-comercial-floss` (§legal): LGPL/GPL uso comercial, output propio, QCAD excepciones, tokenización como contexto (otro proyecto).
- `planos-documento-legal-ar` (§legal): TechDraw + firma/matrícula + Ley 24.335 (requiere curaduría legal).

## Candidatos (Nivel 1 verificar / Nivel 2 esperar s / Nivel 3 no encadenar)

- Nivel 1 verificado (existe, citado, no ficha): Yorik blog NativeIFC tutorial https://yorik.uncreated.net/?blog%2F2025%2F002-nativeifc-tutorial ; BIM migration guide ; IfcOpenShell docs system https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/system/index.html ; docs.bonsaibim.org Services/Systems.
- Nivel 2 candidatos (accesibles, esperar s de SOL para bajar/transcribir/crear ficha): Cables videotutoriales SargoDevel https://www.youtube.com/@SargoDevelCables ; F_Rosa HVAC library https://github.com/Francisco-Rosa/FreeCAD-library/tree/master/HVAC/Ducts ; FreeCAD-BIM-examples https://github.com/yorikvanhavre/FreeCAD-BIM-examples ; mep_engineering federation demo (Terminal 1/2 93k elementos).
- Nivel 3 citas de citas (solo con s explícito por fuente): EPLAN routing docs, KiCad StepUp, EPANET, normativa GCBA instalaciones — no encadenar por cuenta propia.

## Dependencias vault

- [[wiki/glosario/software/freecad|freecad]] · [[wiki/glosario/conceptos/bim-metodologia|bim-metodologia]] · [[wiki/glosario/software/bonsai-ifcopenshell|bonsai]] (propuesta) · [[proyectos/MVP_02-autocad-standards/00-index|MVP_02]] (planos legales) · [[raw/research/2026-10-15-cad-abierto-mcp-opencode|cad-abierto]] · [[wiki/glosario/software/qcad|qcad]] (propuesta) · tokenización (otro proyecto, solo mención)
