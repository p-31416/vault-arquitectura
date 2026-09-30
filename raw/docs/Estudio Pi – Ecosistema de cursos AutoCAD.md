# Estudio Pi: ecosistema de cursos AutoCAD + agente IA
Investigación fase 2 · 27/09/2026 · Base: AutoCAD 2026/2027 (inglés), normativa AMBA

---

## 0. Mapa de cursos

| # | Curso | Estado | Deriva en |
|---|---|---|---|
| C1 | AutoCAD Base (8 × 2 h) | Ya lo dictás | C2, C4 |
| C2 | AutoCAD 2D Avanzado + Paramétrico (alineado a objetivos ACP, sin ser oficial) | Nuevo | Ext. Eléctrica, Ext. Sanitaria, C3 |
| C2-E | Extensión Instalación Eléctrica (bloques + cómputo) | Nuevo | — |
| C2-S | Extensión Instalación Sanitaria (bloques + cómputo) | Nuevo | — |
| C3 | Gestión y Presentación Municipal (con tu socia gestora) | Nuevo | — |
| C4 | AutoCAD 3D Básico → Impresión 3D / Corte CNC | Ya lo dictaste | Alianzas CNC / impresora 3D |
| IA | Agente personal CAD (transversal: aparece en C2, C3 y C4) | En diseño | Consultoría IA para estudios |

Idea central: todos los cursos comparten el mismo "Kit Estudio Pi" (plantilla DWT + archivo de estándar DWS + biblioteca de bloques). C1 lo usa, C2 lo construye, C3 lo aplica al trámite municipal y el agente IA lo controla.

---

## 1. C2: AutoCAD 2D Avanzado + Paramétrico

### 1.1 Alineación con el ACP (Autodesk Certified Professional)
Fuente: [ACP AutoCAD Exam Objectives, dic. 2025](https://damassets.autodesk.net/content/dam/autodesk/www/campaigns/emea/docs/AutoCAD-ACP-Exam-Objectives_Dec2025.pdf). El examen es de opción múltiple, sin software, y Autodesk recomienda unas 400 h mínimas de uso (1.200 h ideales).

| Dominio ACP | Peso | Dónde lo cubrís en C2 |
|---|---|---|
| Application and drawing management (capas, UCS, propiedades, MEASUREGEOM, COUNT, AUDIT/RECOVER/PURGE) | 22 % | Módulos 1 y 7 |
| Design annotation and detailing (estilos, tablas, escalas anotativas) | 20 % | Módulo 2 |
| Author and edit drawing content (bloques, atributos, ATTSYNC, WBLOCK, Blocks palette, sombreados, matrices asociativas, pinzamientos) | 29 % | Módulos 3, 4 y 5 |
| Configure and manage design output (layouts, viewports, plot) | 16 % | Módulo 6 |
| Collaboration (xrefs, compartir, comparar) | 13 % | Módulo 7 |

Consejo: usá "alineado a los objetivos del ACP" y no "preparación oficial", para no dar a entender que es un curso autorizado.

### 1.2 Módulos propuestos (8 clases × 2 h, mismo formato que C1)

| Clase | Tema | Comandos / funciones clave | Fuente oficial |
|---|---|---|---|
| 1 | Plantilla DWT del estudio: unidades, capas por norma, estilos de texto/cota, tipos de línea (LM, eje medianero), layouts con carátula | NEW (desde DWT), LAYER, STYLE, DIMSTYLE, MLEADERSTYLE, TABLESTYLE, SCALELISTEDIT | [Command Reference](https://help.autodesk.com/view/ACD/2026/ENU/?page=commands) |
| 2 | Anotación anotativa: escalas 1:50 / 1:100 / 1:200 en un mismo dibujo; tablas y campos (FIELD) | ANNOTATIVE, CANNOSCALE, TABLE, FIELD | ACP 2.1–2.3 |
| 3 | Bloques dinámicos I: estirables (puertas, ventanas, mesadas) | BEDIT, parámetro Linear + acción Stretch | [Create a Stretchable Dynamic Block](https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-4005A6BB-388A-4EC7-BF17-555F1E6C137C) |
| 4 | Bloques dinámicos II: varias posiciones (Visibility States), Flip, Rotate, Lookup, Array | BVSTATE, BVHIDE/BVSHOW, BPARAMETER, BACTION | [About Creating Dynamic Blocks](https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-LT/files/GUID-DF133028-1A0C-4739-859F-83D967041B91.htm) · [Block Editor](https://help.autodesk.com/view/ACDLT/2026/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-B69D58AD-7920-4198-AB2A-0E24B944F6CD-htm.html) |
| 5 | Bloques con atributos para cómputo: carátula inteligente, rótulos de locales (nombre, número, superficie), aberturas con código | ATTDEF, BATTMAN, ATTSYNC, DATAEXTRACTION → tabla / Excel, COUNT | [About Extracting Data from Block Attributes](https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-BA68DD22-A3CD-4538-90A9-6101C33BC963.htm) · [About Data Extraction](https://help.autodesk.com/view/ACD/2025/ENU/?guid=GUID-B0D32260-45E3-4643-B574-7F6C31579B68) |
| 6 | Paramétrico: restricciones geométricas y dimensionales, tabla de parámetros, bloques restringidos | GEOMCONSTRAINT, DIMCONSTRAINT, PARAMETERS, AUTOCONSTRAIN, BCPARAMETER | Command Reference |
| 7 | Estándares (DWS) y salud del dibujo: verificar el estándar, traducir capas de terceros, auditar | STANDARDS, CHECKSTANDARDS, LAYTRANS, AUDIT, PURGE, OVERKILL | [CAD Standards (Tuesday Tips)](https://www.autodesk.com/blogs/autocad/cad-standards-tuesday-tips-with-frank/) · [CAD Standards Settings 2027](https://help.autodesk.com/cloudhelp/2027/ENU/AutoCAD-Core/files/GUID-E03CA0C6-C1EF-4C83-A0C7-B1EC9C484CD2.htm) |
| 8 | Salida y colaboración: juegos de planos, xrefs, PDF, eTransmit + intro al agente IA | SHEETSET, XREF, EXPORTPDF, PUBLISH, ETRANSMIT, DWGCOMPARE | ACP 4 y 5 |

### 1.3 Biblioteca de bloques mínima para un plano municipal
Qué suele pedir un plano municipal según la [Guía base para dibujo de plano municipal del CAPBA Distrito 1](https://capbauno.org/wp-content/uploads/2023/04/GUIA-ELEMENTOS.pdf): plantas y cortes a 1:100, un corte transversal y otro longitudinal, una vista por cada frente, cotas parciales y totales, espesores de muro, destino y numeración de los locales, Línea Municipal con ochavas, ejes medianeros, niveles de piso, referencias de corte, pozo absorbente o bomba con distancias, y una carátula con balance de superficies, profesionales, datos catastrales, croquis de ubicación y zonificación. Otros modelos de referencia: el [plano municipal de Vicente López](https://www.vicentelopez.gov.ar/contenido/archivos/2024-06-26-945-archivo.pdf) y las [especificaciones de Zárate](https://zarate.gob.ar/wp-content/uploads/2024/03/ESPECIFICACIONES-PARA-LA-PRESENTACION-DE-PLANOS-2024.pdf), que piden siluetas a 1:200 y planillas de balance.

| Bloque | Tipo | Parámetros / atributos |
|---|---|---|
| Carátula municipal (por jurisdicción) | Atributos + campos | Titular, destino, partida, nomenclatura catastral, profesionales, matrículas, superficies |
| Balance de superficies / siluetas | Tabla con campos | Sup. terreno, cubierta, semicubierta, a construir, existente, a demoler, FOS, FOT |
| Puerta (abrir, corrediza, vaivén) | Visibility + Stretch + Flip | Código, ancho, tipo (para planilla de aberturas) |
| Ventana / paño fijo | Stretch + Visibility | Código, ancho × alto, tipo |
| Rótulo de local | Atributos + campo de área | N.º de local, destino, superficie |
| Artefactos sanitarios (inodoro, bidet, lavatorio, ducha, bañera, pileta de cocina, lavarropas) | Visibility | Código, para cómputo |
| Escalera | Array + Stretch | Cantidad de escalones, huella, contrahuella |
| Cota de nivel (planta y corte) | Atributo | Nivel ±0.00 |
| Flecha de corte / referencia de vista | Atributos | Letra, hoja |
| Norte, croquis de ubicación | Estático / atributo | Calles, distancia a la esquina |
| Pozo absorbente / cámara séptica / bomba | Atributos | Distancias a EM y LM |
| Tipos de línea: LM, eje medianero, proyección | Linetype | — |
| Sombreados: existente / a construir / a demoler | Hatch por capa | Varía según municipio (confirmar con tu socia) |

---

## 2. Extensiones de C2

### C2-E: Instalación eléctrica
- Norma base: Reglamentación AEA 90364, en particular la [parte 7-771 (viviendas, oficinas y locales)](https://aea.org.ar/wp-content/uploads/2017/10/90364-7-771-2.pdf), cuyo Anexo 771-K trae los "Símbolos usuales". Catálogo de ediciones vigentes: [AEA – Reglamentaciones](https://aea.org.ar/reglamentaciones/impresas/).
- Bloques con atributos: boca de iluminación, tomacorriente, interruptor, tablero principal / seccional, caja de paso. Atributos: circuito, tipo de circuito, potencia, altura.
- Cómputo: DATAEXTRACTION → cantidad de bocas por circuito y tablero → planilla de materiales / presupuesto.

### C2-S: Instalación sanitaria
- En CABA, los planos sanitarios pasan por AySA. Ver [requisitos de planos sanitarios de AySA](https://aysa.com.ar/media-library/usuarios/tramites_online/Requisitos-planos-sanitarios_2024_V2.pdf).
- Bloques: artefactos, piletas de patio, bocas de acceso, cámaras de inspección, tanque de reserva / bombeo, llaves de paso, montantes (agua fría / agua caliente / cloaca / pluvial, con colores y tipos de línea por capa).
- Cómputo: cantidad de artefactos y accesorios; metros de cañería con MEASUREGEOM o polilíneas por capa + extracción de datos.
- Pendiente: conseguir la simbología normativa local que usa tu socia o tus manuales (no encontré una ficha pública de simbología de AySA equivalente al anexo de la AEA).

---

## 3. C3: Gestión y presentación municipal (con tu socia gestora)

### CABA (recursos oficiales)
- La página [Armado de Planos del GCBA](https://buenosaires.gob.ar/gcaba_historico/armado-de-planos) tiene el template y la carátula reglamentaria para planos de obra e instalaciones, cómo publicar planos en PDF y los "Protocolos CAD" (una botonera para AutoCAD, su template y videos explicativos). Es el material ideal para una clase práctica.
- Los [instructivos de trámites](https://buenosaires.gob.ar/gcaba_historico/guia-de-tramites/instructivos-de-tramites) explican cómo llenar las carátulas, traen ejemplos de cómputo y planillas de superficies para calcular la plusvalía, y el acceso a TAD.
- La Disposición 118/DGROC/20 aprueba los modelos de documentación oficial para registrar planos de obra, de instalaciones y de prehorizontalidad ([resumen en CPIC](https://cpic.org.ar/normas/)).
- [Reglamentos Técnicos del Código de Edificación](https://buenosaires.gob.ar/gcaba_historico/codigo-urbanistico-y-de-edificacion/reglamentos-tecnicos-del-codigo-de-edificacion).

### Provincia de Buenos Aires
- Cada municipio tiene su propio modelo. Conviene armar un módulo por jurisdicción, empezando por donde trabaja más tu socia. Referencias: la guía del CAPBA 1 y los modelos de Vicente López y Zárate citados arriba.

### Estructura sugerida (4–6 clases)
1. Circuito del trámite y roles (profesional / gestor), documentación previa.
2. Carátula y template reglamentario en AutoCAD (usando la botonera de CABA).
3. Balance de superficies, siluetas, FOS/FOT con campos y tablas.
4. Publicación PDF / firma / carga en TAD (CABA) o mesa de entradas (PBA).
5. Observaciones típicas y cómo evitarlas (checklist → luego lo automatiza el agente IA).
6. Caso práctico completo.

---

## 4. C4: AutoCAD 3D Básico → Impresión 3D y corte CNC

| Salida | Flujo en AutoCAD | Fuente |
|---|---|---|
| Impresión 3D | Sólidos cerrados (sin huecos, sin caras sueltas) → 3DPRINT o STLOUT → STL → slicer | [About Printing 3D Models](https://help.autodesk.com/view/ACDLT/2026/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-16D8B210-E4FC-4E89-9905-B5F9C9569E39-htm.html) · [Create STL File](https://help.autodesk.com/view/ACDLT/2026/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-4B5C0F42-2B82-49F0-946E-C1E22C8D7336-htm.html) · [AU: Modeling Basics for 3D Printing](https://static.au-uw2-prd.autodesk.com/handout_6549_AC6549_Modeling_Basics_for_3D_Printing_Using_AutoCAD.pdf) |
| Corte CNC / láser (maquetas, placas) | 2D en mm, polilíneas cerradas (JOIN, PEDIT), limpieza (OVERKILL), una capa por operación (corte / grabado / marcado) → DXF (SAVEAS DXF). Desde 3D: FLATSHOT o SECTIONPLANE para sacar perfiles | Command Reference |

Propuesta de producto con tus contactos: un taller de "maqueta de arquitectura digital a física", con piezas planas cortadas por CNC más detalles impresos en 3D. Antes de armarlo, pediles a cada uno el formato que acepta su máquina (DXF, versión, capas y colores), para enseñar exactamente ese flujo.

---

## 5. El agente IA personal: conexiones posibles

### 5.1 Qué existe hoy (sept. 2026)

| Pieza | Qué hace | Clientes | Estado / límites |
|---|---|---|---|
| Autodesk Assistant (dentro de AutoCAD 2027) | Chat con IA, chequeo de estándares contra un archivo de estándar, selección por lenguaje natural, consultas del dibujo (capas, uso de bloques) | Solo dentro de AutoCAD | Funciones nuevas en tech preview; Autodesk advierte que los resultados pueden no ser exactos ([Autodesk Assistant 2027](https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-99E2D8F7-D4D9-4B3A-9E57-7B73D6BB12AD)) |
| AutoCAD and Civil 3D MCP Server (oficial) | Consulta el dibujo abierto: objetos, capas, estilos, estadísticas, chequeo contra la plantilla | Documentado solo para Autodesk Assistant; corre local, en Windows | En AutoCAD es de lectura y análisis; la escritura está solo en Civil 3D ([Autodesk MCP docs](https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_AutoCADCivil3DMcp_autodesk_autocad_civil_3d_mcp_html)) |
| Autodesk Product Help MCP (oficial, gratis) | Busca en la documentación oficial de más de 110 productos; es de solo lectura | Cualquier cliente MCP (Claude Code, Codex, Cursor, VS Code) | Remoto, Streamable HTTP, OAuth. Endpoint `https://developer.api.autodesk.com/knowledge/public/v1/mcp` ([ADSK News](https://adsknews.autodesk.com/en/news/product-help-mcp-server/) · [setup](https://mcpservers.org/remote-mcp-servers/autodesk-product-help)) |
| Otros MCP oficiales de Autodesk | Fusion, Fusion Data y Revit en tech preview; Fusion Automation en beta privada | Agentes externos | Útiles para cuando pases a BIM (Revit) o a fabricación (Fusion) ([APS DevCon 2026](https://aps.autodesk.com/blog/building-agentic-ai-whats-new-autodesk-platform-services)) |
| MCP comunitarios para AutoCAD (control del dibujo) | Dibujar líneas, polilíneas, texto y cotas; insertar bloques; manejar capas; capturas de pantalla | Claude Code, Claude Desktop, Codex (con config documentada) | Ej. [autocad-mcp (COM, AutoCAD 2026 completo, no LT)](https://glama.ai/mcp/servers/Slacker-LLC/autocad-mcp/tree), sin comando libre por seguridad; [autocad-mcp para LT vía AutoLISP](https://github.com/hvkshetry/autocad-mcp); [AutoCAD_MCP](https://github.com/BarryMcAdams/AutoCAD_MCP). No son oficiales: probalos antes en archivos de prueba |

### 5.2 Arquitectura propuesta ("Agente Estudio Pi")
```
Agente (Claude Code / Codex / OpenCode)
 ├─ Conocimiento
 │   ├─ Autodesk Product Help MCP  → responde "cómo se hace" con la doc oficial
 │   └─ Tus manuales + wiki (Obsidian/Markdown) → normativa local, convenciones del estudio
 ├─ Dibujo (local, Windows, AutoCAD abierto)
 │   └─ MCP comunitario vía COM/AutoLISP → insertar bloques del kit, crear capas, cotas
 ├─ Control de calidad
 │   ├─ DWS + CHECKSTANDARDS / Autodesk Assistant → ¿el plano cumple el estándar?
 │   └─ Checklist municipal (C3) en Markdown → el agente revisa que no falte nada
 └─ Cómputo
     └─ DATAEXTRACTION → CSV/Excel → el agente arma la planilla de materiales / presupuesto
```
Conectar el Product Help MCP en Claude Code es un solo comando:
`claude mcp add autodesk-product-help --transport http https://developer.api.autodesk.com/knowledge/public/v1/mcp`
En Codex y OpenCode se agrega como servidor MCP remoto por HTTP en su archivo de configuración.

Ruta de aprendizaje sugerida para vos: (1) conectar Product Help MCP; (2) probar un MCP comunitario en una PC de prueba con AutoCAD completo; (3) sumar tu kit DWT/DWS/bloques como "contexto" del agente; (4) recién después, empaquetarlo como servicio de consultoría.

### 5.3 Ojo con la cuenta de estudiante
- El plan Education de Autodesk da acceso gratis por un año, solo para fines educativos ([Autodesk Education](https://www.autodesk.com/education/edu-software/overview)).
- Es solo para alumnos y docentes de instituciones educativas acreditadas. Los alumnos de centros de capacitación y programas de recapacitación no califican, y tampoco pueden usar la prueba de 30 días para capacitarse ([Elegibilidad](https://www.autodesk.com/support/account/education/students-educators/eligibility)).
- Qué implica para vos: sirve para aprender y hacer prototipos, pero no para trabajos de consultoría pagos. Además, tus alumnos de cursos privados no pueden usarla salvo que sean estudiantes universitarios. Conviene definir la política de licencias del curso: licencia propia del alumno, AutoCAD LT o que la institución donde dictás tenga convenio.

---

## 6. Próximos pasos
1. Pasame tus manuales → armo la tabla de comandos EN ↔ ES y la simbología eléctrica y sanitaria.
2. Definir con tu socia la jurisdicción piloto para C3 (¿CABA o qué municipio de PBA?).
3. Construir el Kit Estudio Pi v1: DWT + DWS + 15 bloques del punto 1.3.
4. Prueba técnica del agente: Product Help MCP + 1 MCP de AutoCAD sobre el kit.
