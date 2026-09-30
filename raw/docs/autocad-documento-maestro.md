---
tipo: documento
proyecto: estudio-pi
software: [autocad, mcp]
fecha_creacion: 2026-09-27
ultima_actualizacion: 2026-09-27
tags: [autocad, documento-maestro, cursos, mcp, standards, SETs, estudio-pi]
idioma: es
---

# Estudio Pi · AutoCAD: documento maestro

Cursos, comandos, normativa, SETs de estándar y agente IA (MCP).
Versión 1.0 · 27/09/2026 · Base: AutoCAD 2027 (versión de prueba), comandos en inglés.

> Este documento centraliza cinco archivos raw de `raw/docs/`:
> 1. "Fuentes oficiales y comandos (EN)"
> 2. "Ecosistema de cursos AutoCAD"
> 3. "Guía de conexiones MCP"
> 4. "Kit temático SETs de estándar CAD"
> 5. "Estudio Pi – AutoCAD documento maestro" (este)
>
> Cada dato lleva una nota numerada `[^n]` que enlaza a la lista de fuentes del final, y desde cada fuente se puede volver al texto donde se usó.

---

## Índice

- [[#1. Situación actual y decisiones clave]]
- [[#2. Fuentes oficiales de Autodesk (priorizadas)]]
- [[#3. Ecosistema de cursos]]
- [[#4. SETs de estándar CAD (Kit Estudio Pi)]]
- [[#5. C1: AutoCAD Base (8 clases), comandos por clase]]
- [[#6. C2: AutoCAD 2D Avanzado + Paramétrico (alineado al ACP)]]
- [[#7. Extensiones: instalación eléctrica y sanitaria]]
- [[#8. C3: Gestión y presentación municipal (con tu socia gestora)]]
- [[#9. C4: AutoCAD 3D, impresión 3D y CNC]]
- [[#10. Agente IA: panorama de conexiones MCP]]
- [[#11. Configuración de Claude Code, Codex y OpenCode]]
- [[#12. Plan de trabajo con AutoCAD 2027 (versión de prueba)]]
- [[#13. Licencias: prueba, educación y uso comercial]]
- [[#14. Próximos pasos]]
- [[#15. Fuentes]]

---

## 1. Situación actual y decisiones clave

- Tenés instalada la versión de prueba de AutoCAD 2027. La prueba dura 15 días, vence sola y no se puede extender. Después, las opciones son una suscripción mensual (desactivando la renovación automática) o tokens Flex [[#^f64|64]]. El precio de lista es de USD 2.095 por año o USD 260 por mes [[#^f67|67]].
- AutoCAD 2027 incorpora Autodesk Assistant con IA. Puede verificar el dibujo contra un archivo de estándar, seleccionar objetos a partir de una instrucción en lenguaje natural y responder consultas sobre capas y uso de bloques. Estas funciones están en tech preview y Autodesk advierte que los resultados pueden no ser exactos [[#^f24|24]] [[#^f21|21]].

---

## 2. Fuentes oficiales de Autodesk (priorizadas)

### A. Referencia de comandos (la fuente "madre")

| Recurso | Para qué sirve | URL |
|---|---|---|
| Command Reference AutoCAD 2026 (A–Z) | Lista alfabética completa y oficial de todos los comandos | https://help.autodesk.com/view/ACD/2026/ENU/?page=commands |
| Command Reference AutoCAD 2027 (A–Z) | Versión más reciente de la misma lista | https://help.autodesk.com/view/ACD/2027/ENU/?page=commands&q=* |
| Commands for Working With 3D Models | Grupo oficial de comandos 3D (3DMOVE, 3DORBIT, BOX, EXTRUDE...) | https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-6548456A-28BD-40CB-89BA-F19F5800C0ED |
| New Commands and System Variables (2027) | Qué comandos/variables son nuevos en la versión | https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-B93A458E-1A7F-4090-A8CF-87A31C24E404 |
| Updated Commands and System Variables (2026) | Qué cambió respecto a versiones anteriores | https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/CIV3D/2014/ENU/filesACD/GUID-4FEBA606-95E0-4DC4-A116-257ED86DCD58-htm.html |

### B. Atajos, alias y teclas

| Recurso | Para qué sirve | URL |
|---|---|---|
| AutoCAD Keyboard Shortcuts Guide (web) | Página oficial de atajos, con link al PDF | https://www.autodesk.com/shortcuts/autocad |
| AutoCAD Shortcuts Guide (PDF imprimible, con stickers de teclado) | Material ideal para entregar a alumnos | https://damassets.autodesk.net/content/dam/autodesk/www/shortcuts/autocad/AutoCAD-Shortcuts-Guide-Autodesk.pdf |
| AutoCAD LT 2025 Shortcuts Guide (PDF) | Misma lógica, versión LT | https://damassets.autodesk.com/content/dam/autodesk/www/pdfs/autocad-lt-2025-shortcut-guide-en.pdf |
| AutoCAD for Mac 2025 Shortcuts (PDF) | Para alumnos con Mac | https://damassets.autodesk.net/content/dam/autodesk/www/pdfs/autocad-for-mac-2025-keyboard-shortcuts-guide-en.pdf |
| Shortcut Keys Reference (Ctrl/F-keys) | Tabla oficial de teclas F1–F12, Ctrl+... | https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/CIV3D/2014/ENU/filesACD/GUID-B6A9C126-230D-47F5-8973-464BC80E3736-htm.html |
| About Creating Command Aliases (acad.pgp) | Cómo personalizar alias | https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/CIV3D/2014/ENU/filesACD/GUID-FE9AE544-F537-4D3B-8F75-B76484513787-htm.html |
| Command Aliases, Shortcut Keys and AutoCorrect | Explicación de alias vs. teclas vs. autocorrección | https://help.autodesk.com/view/ACD/2025/ENU/?guid=GUID-D2B4BF16-B1F7-4EF2-89AF-88ACE85FAD73 |
| Blog: Essential Keyboard Shortcuts | Tabla Acción / Comando / Alias / Uso | https://www.autodesk.com/blogs/autocad/work-faster-in-autocad-essential-keyboard-shortcuts-and-commands/ |

### C. Aprendizaje oficial (estructura de curso)

| Recurso | Uso sugerido | URL |
|---|---|---|
| AutoCAD Foundations (2026) | Serie oficial para empezar a trabajar solo: base del curso inicial | https://help.autodesk.com/view/ACD/2026/ENU/?contextId=ACD_FOUNDATIONS_LANDING |
| The Hitchhiker's Guide to AutoCAD | Recorrido por los comandos esenciales | https://help.autodesk.com/view/ACDLT/2026/ENU/?contextId=HITCHHIKERSGUIDETOAUTOCADBASICS |
| Get started with AutoCAD (13 ítems) | Colección on-demand | https://app.learn-one.autodesk.com/learn/ondemand/collection/get-started-with-autocad |
| On-demand Learning catalog / Quick Start Guide | Tutoriales cortos | https://www.autodesk.com/learn/catalog/autocad/product/AutoCAD |
| AutoCAD tutorials for beginners | Hub de tutoriales | https://www.autodesk.com/solutions/aec/autocad-tutorials |

### D. Certificación (para el curso intermedio/avanzado)

| Recurso | Uso | URL |
|---|---|---|
| ACP AutoCAD Exam Objectives (dic. 2025) | Temario oficial nivel profesional: sirve para validar el programa avanzado | https://damassets.autodesk.net/content/dam/autodesk/www/campaigns/emea/docs/AutoCAD-ACP-Exam-Objectives_Dec2025.pdf |
| ACP Exam Guide | Habilidades previas esperadas | https://damassets.autodesk.net/content/dam/autodesk/www/training-and-certification/docs/autocad-acp-exam-guide-beta.pdf |

### E. Novedades / IA (conecta con tu perfil de consultor IA)

- What's New in AutoCAD 2027 (Autodesk Assistant con conteo de objetos, análisis según la selección, Connected References): https://help.autodesk.com/view/ACD/2027/ENU/?contextId=WHATS_NEW_2027_ACD
- Blog AutoCAD 2027 (guía con IA, limpieza automática de geometría, Forma Data Management): https://www.autodesk.com/blogs/autocad/autocad-2027/
- Release Notes 2026 (incluye ayuda offline): https://help.autodesk.com/view/ACD/2026/ENU/?guid=AUTOCAD_2026_RELEASE_NOTES

---

## 3. Ecosistema de cursos

### 3.1 Mapa de cursos

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

### 3.2 Principios de diseño del kit

1. **Núcleo + SETs.** SET-GEN lleva lo común (carátula, estilos, CTB y capas generales). Cada SET temático suma solo lo propio de su tema. Un plano municipal, por ejemplo, combina SET-GEN + SET-ARQ + SET-MUN.
2. **Una sola nomenclatura interna y varias salidas.** El estudio trabaja en castellano y exporta a NCS, ISO o AEC (UK) con LAYTRANS y un DWS de mapeo por estándar [[#^f82|82]] [[#^f105|105]].
3. **Campos fijos y separador `-`**, en el orden SET/disciplina - elemento - subelemento - estado. El estado se alinea con NCS e ISO: N nuevo o a construir, E existente, D a demoler [[#^f68|68]] [[#^f71|71]].
4. **Todo va PorCapa.** Color, tipo de línea y grosor se definen en la capa, y el CTB traduce color a grosor según la serie ISO [[#^f76|76]] [[#^f87|87]].
5. **Anotación anotativa**, con escalas por SET: 1:100 municipal [[#^f94|94]] y 1:50 para replanteo [[#^f78|78]].
6. **Estados de capa (.las)** para cambiar de vista rápido, por ejemplo "Municipal", "Replanteo" o "Estructura". Se importan desde el administrador de estados de capa [[#^f83|83]] [[#^f85|85]].
7. **Bloques inteligentes** (dinámicos y con atributos) para el cómputo con extracción de datos [[#^f91|91]] [[#^f92|92]] [[#^f93|93]].
8. **Distribución centralizada.** Las paletas de herramientas pueden apuntar a una carpeta de red. En AutoCAD 2027 también pueden venir de un proyecto en Forma Data Management ("Connected Support Files"), y las ubicaciones de confianza aceptan `\..` para incluir subcarpetas [[#^f84|84]] [[#^f89|89]] [[#^f90|90]].
9. **Checklist legible por humanos y por el agente IA.** Cada SET incluye un `checklist.md` que el agente usa para auditar planos. En 2027, además, el Autodesk Assistant puede verificar contra el DWS [[#^f104|104]].

---

## 4. SETs de estándar CAD (Kit Estudio Pi)

### 4.1 Comparativa de nomenclatura de capas

| Estándar | Estructura | Ejemplo | Estado / fase | Fuente |
|---|---|---|---|---|
| NCS (EE. UU.): AIA CAD Layer Guidelines | Disciplina (1–2 caracteres) - Grupo mayor (4) - Grupo menor 1 (4) - Grupo menor 2 (4) - Estado (1). Obligatorios: disciplina y grupo mayor | `AI-WALL-FULL-DIMS-N` | Campo de estado (N = nuevo; E = existente; D = a demoler) | [[#^f68\|68]] [[#^f70\|70]] |
| ISO 13567 (internacional) | Campos de largo fijo, sin separador: agente (2) + elemento (6) + presentación (2) obligatorios. Opcionales: estado, sector, fase, proyección, escala, paquete, usuario | Presentación: `E-` gráfico, `T-` texto, `H-` sombreado, `D-` cotas, `G-` grilla | N nuevo, E existente, R a remover, T temporario | [[#^f71\|71]] [[#^f72\|72]] |
| AEC (UK) sobre BS 1192 / Uniclass 2015 | Rol - Clasificación Uniclass - Presentación - Descripción - Vista (opcional). Máximo 64 caracteres; descripción en CamelCase y singular | Rol: `A` arquitectura, `E` eléctrica, `EL` iluminación, `G` topografía | Por descripción o por vista | [[#^f73\|73]] [[#^f74\|74]] |
| NCS: compatibilidad con ISO | Mantener el mismo formato y largo en todo el proyecto. `ANNO` no se permite si se busca conformidad con ISO 13567 | — | — | [[#^f68\|68]] |

### 4.2 Designadores de disciplina

Nivel 1 del NCS: G General, V Relevamiento/cartografía, B Geotecnia, C Civil, L Paisajismo, S Estructura, A Arquitectura, I Interiores, Q Equipamiento, F Incendio, P Sanitaria (plomería), D Procesos, M Mecánica (termomecánica), E Eléctrica, W Energía distribuida, T Telecomunicaciones, R Recursos, X Otras, Z Contratista / planos de taller [[#^f68|68]] [[#^f69|69]].
El nivel 2 agrega un modificador. En arquitectura: AD demolición, AE elementos, AF terminaciones, AG gráfica, AI interiores, AS sitio, y AJ/AK definibles por el usuario [[#^f68|68]].

### 4.3 Identificación de láminas y archivos

- NCS/UDS: `A-101` (nivel 1) o `AD-101` (nivel 2). Estructura: disciplina + tipo de lámina (1 dígito) + número secuencial (2 dígitos), con sufijo opcional del usuario [[#^f69|69]].
- ISO 19650: `Proyecto-Originador-Volumen-Nivel-Tipo-Rol-Número`, por ejemplo `PRJ-ORG-ZZ-00-DR-A-0001`. Estado (S0, S1, S2, A1) y revisión (P01, C01) se manejan aparte, como metadatos [[#^f75|75]].

### 4.4 Grosores de línea

- ISO 128-2: serie 0,13 · 0,18 · 0,25 · 0,35 · 0,5 · 0,7 · 1 · 1,4 · 2 mm (razón 1:√2). La relación entre línea extra gruesa, gruesa y fina es 4:2:1, y la separación mínima entre líneas paralelas es de 0,7 mm [[#^f76|76]].
- NCS: ocho grosores entre 0,18 y 2,00 mm. Las líneas visibles suelen ser de 0,35 mm y las ocultas de 0,25 mm [[#^f70|70]].
- En Argentina, IRAM 4502-23 ("Líneas de dibujo para construcciones"), IRAM 4504 (formatos y plegado), IRAM 4505 (escalas), IRAM 4508 (rótulo) e IRAM 4513 (cotas) forman parte del Manual de Normas IRAM de Dibujo Tecnológico [[#^f77|77]]. No tuve acceso al texto de esas normas: conviene validar la tabla de grosores del SET con tu manual.

### 4.5 Qué incluye un "estándar CAD" según Autodesk

Objetos con nombre (capas, estilos de texto, estilos de cota, tipos de línea), bloques de carátula y de detalle, criterios de anotación, criterios de layouts y conjuntos de planos, y la convención de propiedades (PorCapa, PorBloque o explícitas) [[#^f81|81]]. El DWS verifica capas, estilos de texto, tipos de línea, estilos de cota y de directriz múltiple. El Batch Standards Checker genera un informe sin modificar los dibujos y guarda su configuración en un archivo `.chx` [[#^f82|82]] [[#^f83|83]].

### 4.6 SET-GEN: núcleo común

- **Capas:** `G-CART` (carátula), `G-MARC` (marco), `G-TEXT`, `G-COTA`, `G-REFE` (referencias de corte y detalle), `G-VPRT` (ventanas, no imprimible), `G-AUXI` (construcción, no imprimible). Equivalen a los grupos de presentación de ISO 13567 (B, V, D, J, U) [[#^f71|71]] y al ejemplo `G-ANNO-TTLB` del NCS [[#^f70|70]].
- **Estilos:** texto EP-2,5 y EP-3,5 anotativos; cotas EP-ARQ; directriz EP; tabla EP.
- **Láminas:** formatos y plegado según IRAM 4504 y rótulo según IRAM 4508 [[#^f77|77]]. Identificación `A-101` al estilo UDS [[#^f69|69]].
- **Archivos:** `EP-OBRA-ORIG-ZONA-NIVEL-TIPO-DISC-NNNN`, adaptación de ISO 19650 [[#^f75|75]].

### 4.7 Anatomía de un SET (plantilla común)

| Componente | Archivo | Contenido |
|---|---|---|
| Plantilla | `SET-XXX.dwt` | Unidades, capas, estilos, layouts, configuraciones de página, DWS asociado |
| Estándar | `SET-XXX.dws` | Capas, estilos de texto, cota y directriz, tipos de línea; mapeos de LAYTRANS [[#^f82\|82]] |
| Estados de capa | `SET-XXX.las` | Vistas temáticas [[#^f85\|85]] |
| Estilo de trazado | `EP-ISO.ctb` (común) | Color → grosor de la serie ISO 128 [[#^f76\|76]] [[#^f87\|87]] |
| Tipos de línea y sombreados | `EP.lin` / `EP.pat` | LM, eje medianero, proyección, existente, a demoler |
| Biblioteca de bloques | `SET-XXX_bloques.dwg` | Dinámicos y con atributos |
| Paleta de herramientas | `SET-XXX.xtp` | Bloques, sombreados, cotas y comandos [[#^f84\|84]] |
| Conjunto de planos | `SET-XXX.dst` | Láminas, numeración y carátula con campos [[#^f86\|86]] |
| Extracción de datos | `SET-XXX.dxe` | Configuración de cómputo reutilizable [[#^f92\|92]] |
| Checklist | `SET-XXX_checklist.md` | Controles mínimos (para humanos y para el agente IA) |
| Guía | `SET-XXX_guia.md` | Norma base, escalas, ejemplos, videos |

### 4.8 SETs temáticos

#### SET-LEV: Relevamiento y topografía (disciplina V)
- **Propósito:** estado actual del terreno y de lo construido; base para el resto de los SETs.
- **Capas:** `V-TERR` (límites y medidas del terreno), `V-EDIF-E` (construcciones existentes), `V-ARBO` (árboles), `V-NIVE` (niveles y puntos), `V-SERV` (servicios existentes), `V-VECI` (linderos).
- **Bloques:** punto de nivel con atributos (número, cota) y árbol con diámetro.
- **Salidas:** plano de relevamiento, que sirve de base para SET-MUN (existente y a demoler).
- **Estado:** conceptual. Falta una fuente local de contenidos mínimos. Se toma el designador V del NCS [[#^f68|68]].

#### SET-REP: Replanteo
- **Base:** apuntes de cátedra de la UNaM y de la UNLP [[#^f78|78]] [[#^f79|79]].
- **Contenido mínimo:** medidas perimetrales y ángulos de la parcela, distancia sobre la LM a la ochava más cercana, al menos dos ejes de replanteo, fundaciones acotadas, cotas parciales y acumuladas, espesores de muros y columnas, niveles en plantas altas [[#^f79|79]]. En muros curvos: radio, centro y coordenadas de inicio y fin [[#^f78|78]].
- **Escala convencional:** 1:50. Tolerancias: 10 mm con replanteo manual y 5 mm con instrumental [[#^f78|78]].
- **Capas:** `R-EJES` (ejes de replanteo), `R-EJAX` (auxiliares), `R-COTP` (parciales), `R-COTA` (acumuladas), `R-PTOS` (puntos con coordenadas), `R-NIVE`, `R-FUND` (fundación, en referencia a SET-EST).
- **Bloques:** marca de eje (letra o número), punto de replanteo con atributos (ID, X, Y, Z) y cota de nivel.
- **Cómputo:** cuadro de coordenadas generado automáticamente a partir de los bloques con extracción de datos [[#^f103|103]] [[#^f94|94]].

#### SET-ARQ: Arquitectura
- **Capas por elemento y estado:** `A-MURO-N/E/D`, `A-TABI`, `A-ABER` (aberturas), `A-SOLA` (solados), `A-CIEL`, `A-ESCA`, `A-EQUI` (equipamiento), `A-LOCA` (rótulos de locales), `A-SOMB` (sombreados). Estado N/E/D alineado con NCS e ISO [[#^f68|68]] [[#^f72|72]].
- **Bloques:** puertas y ventanas dinámicas con atributos de código, rótulo de local con campo de área, escalera paramétrica.
- **Láminas:** A-1xx plantas, A-2xx vistas, A-3xx cortes, A-5xx detalles.

#### SET-MUN: Presentación municipal (se combina con SET-ARQ)
- **Base:** guía del CAPBA 1 (1:100) [[#^f96|96]]. En CABA, template y protocolos CAD del GCBA [[#^f97|97]].
- **Capas:** `M-SILUET`, `M-BALA`, `M-LMUN`, `M-EMED`, `M-FOSF`, `M-DEMO`, `M-CONS`.
- **Bloques:** carátula por jurisdicción con atributos y campos, tabla de balance, croquis de ubicación.

#### SET-EST: Estructuras (disciplina S)
- **Base:** INPRES-CIRSOC 103, art. 1.3.4.1.b [[#^f81|81]]. Planos de encofrado, detalles de hormigón armado, estructuras metálicas según IRAM 4518 e IRAM ISO 2553 [[#^f78|78]].
- **Capas:** `S-EJES`, `S-FUND`, `S-COLU`, `S-VIGA`, `S-LOSA`, `S-TABI`, `S-ARMA`, `S-ESTR`, `S-META`, `S-UNIO`, `S-NIVE`, `S-DESI`.
- **Alcance del curso:** representación y documentación, sin cálculo. El cálculo lo firma el ingeniero.

#### SET-ELE: Instalación eléctrica (disciplina E)
- **Base:** AEA 90364-7-771 y su anexo de símbolos usuales [[#^f98|98]].
- **Capas:** `E-ILUM`, `E-TOMA`, `E-COMA`, `E-TABL`, `E-CANA`, `E-CIRC`, `E-TEXT`.

#### SET-SAN: Instalación sanitaria (disciplina P)
- **Base:** requisitos de AySA para planos sanitarios en CABA [[#^f97|97]].
- **Capas:** `P-AFRI`, `P-ACAL`, `P-CLOA`, `P-PLUV`, `P-ARTE`, `P-CAMA`, `P-TANQ`.
- **Pendiente:** simbología local, a partir de manuales.

#### SET-FAB: Fabricación (CNC e impresión 3D)
- **Capas por operación:** `F-CORT`, `F-GRAB`, `F-PLEG`, `F-MARC`. Salida: DXF 2D para CNC y STL para impresión 3D.

#### SETs futuros (fuera de alcance por ahora)
SET-INC (incendio, F), SET-TER (termomecánica, M), SET-GAS, SET-INT (interiorismo, I), SET-PAI (paisajismo, L). Los designadores ya existen en el NCS [[#^f68|68]].

### 4.9 Matriz: qué SET usa cada tipo de plano

| Plano | GEN | LEV | REP | ARQ | MUN | EST | ELE | SAN | FAB |
|---|---|---|---|---|---|---|---|---|---|
| Relevamiento | ● | ● | | | | | | | |
| Municipal (permiso) | ● | ○ | | ● | ● | | | | |
| Obra / replanteo | ● | | ● | ● | | ○ | | | |
| Estructura | ● | | ○ | | | ● | | | |
| Eléctrica | ● | | | ○ | | | ● | | |
| Sanitaria | ● | | | ○ | ○ | | | ● | |
| Maqueta CNC / 3D | ● | | | ○ | | | | | ● |

● obligatorio · ○ como referencia (xref o capas bloqueadas)

### 4.10 Equivalencias de nomenclatura (ejemplos)

| Estudio Pi | NCS (formato) | ISO 13567 (lógica) | AEC (UK) (lógica) |
|---|---|---|---|
| `A-MURO-N` | `A-WALL-N` [[#^f68\|68]] | Agente A + elemento + presentación E + estado N [[#^f71\|71]] | A + código Uniclass de muro + presentación + `Wall` [[#^f73\|73]] |
| `A-MURO-D` | `AD-WALL` [[#^f70\|70]] | Estado R (a remover) [[#^f71\|71]] | Descripción con estado |
| `G-CART` | `G-ANNO-TTLB` [[#^f70\|70]] | Presentación B / V (espacio papel) [[#^f71\|71]] | Z (general) [[#^f73\|73]] |
| `R-EJES` | Designador del usuario (AJ/AK) [[#^f68\|68]] | Presentación G (grilla) [[#^f71\|71]] | — |

### 4.11 Flujo de verificación

1. El dibujo nace de `SET-XXX.dwt`, que ya tiene el DWS asociado [[#^f82|82]].
2. Durante el trabajo, las notificaciones de CHECKSTANDARDS avisan las violaciones [[#^f82|82]] [[#^f88|88]].
3. Antes de entregar, se corre el Batch Standards Checker sobre todo el juego (informe `.chx`) [[#^f82|82]].
4. Para un cliente con otro estándar, se usa LAYTRANS con el DWS de mapeo [[#^f105|105]].
5. El agente IA recorre `SET-XXX_checklist.md`. En AutoCAD 2027, el Assistant verifica contra el estándar (función en tech preview) [[#^f104|104]].

---

## 5. C1: AutoCAD Base (8 clases), comandos por clase

> Stub — crear sección dedicada cuando se documente cada comando. Ver `raw/docs/` para el contenido completo de la fuente original.

---

## 6. C2: AutoCAD 2D Avanzado + Paramétrico (alineado al ACP)

### 6.1 Alineación con el ACP (Autodesk Certified Professional)

Fuente: [ACP AutoCAD Exam Objectives, dic. 2025](https://damassets.autodesk.net/content/dam/autodesk/www/campaigns/emea/docs/AutoCAD-ACP-Exam-Objectives_Dec2025.pdf). El examen es de opción múltiple, sin software, y Autodesk recomienda unas 400 h mínimas de uso (1.200 h ideales).

| Dominio ACP | Peso | Dónde lo cubrís en C2 |
|---|---|---|
| Application and drawing management (capas, UCS, propiedades, MEASUREGEOM, COUNT, AUDIT/RECOVER/PURGE) | 22 % | Módulos 1 y 7 |
| Design annotation and detailing (estilos, tablas, escalas anotativas) | 20 % | Módulo 2 |
| Author and edit drawing content (bloques, atributos, ATTSYNC, WBLOCK, Blocks palette, sombreados, matrices asociativas, pinzamientos) | 29 % | Módulos 3, 4 y 5 |
| Configure and manage design output (layouts, viewports, plot) | 16 % | Módulo 6 |
| Collaboration (xrefs, compartir, comparar) | 13 % | Módulo 7 |

Consejo: usá "alineado a los objetivos del ACP" y no "preparación oficial", para no dar a entender que es un curso autorizado.

### 6.2 Módulos propuestos (8 clases × 2 h, mismo formato que C1)

| Clase | Tema | Comandos / funciones clave | Fuente oficial |
|---|---|---|---|
| 1 | Plantilla DWT del estudio: unidades, capas por norma, estilos de texto/cota, tipos de línea (LM, eje medianero), layouts con carátula | NEW, LAYER, STYLE, DIMSTYLE, MLEADERSTYLE, TABLESTYLE, SCALELISTEDIT | Command Reference |
| 2 | Anotación anotativa: escalas 1:50 / 1:100 / 1:200 en un mismo dibujo; tablas y campos (FIELD) | ANNOTATIVE, CANNOSCALE, TABLE, FIELD | ACP 2.1–2.3 |
| 3 | Bloques dinámicos I: estirables (puertas, ventanas, mesadas) | BEDIT, parámetro Linear + acción Stretch | Create a Stretchable Dynamic Block |
| 4 | Bloques dinámicos II: varias posiciones (Visibility States), Flip, Rotate, Lookup, Array | BVSTATE, BVHIDE/BVSHOW, BPARAMETER, BACTION | About Creating Dynamic Blocks |
| 5 | Bloques con atributos para cómputo: carátula inteligente, rótulos de locales, aberturas con código | ATTDEF, BATTMAN, ATTSYNC, DATAEXTRACTION, COUNT | About Extracting Data from Block Attributes |
| 6 | Paramétrico: restricciones geométricas y dimensionales, tabla de parámetros | GEOMCONSTRAINT, DIMCONSTRAINT, PARAMETERS, AUTOCONSTRAIN, BCPARAMETER | Command Reference |
| 7 | Estándares (DWS) y salud del dibujo: verificar el estándar, traducir capas de terceros, auditar | STANDARDS, CHECKSTANDARDS, LAYTRANS, AUDIT, PURGE, OVERKILL | CAD Standards (Tuesday Tips) |
| 8 | Salida y colaboración: juegos de planos, xrefs, PDF, eTransmit + intro al agente IA | SHEETSET, XREF, EXPORTPDF, PUBLISH, ETRANSMIT, DWGCOMPARE | ACP 4 y 5 |

---

## 7. Extensiones: instalación eléctrica y sanitaria

> Stub — contenido derivado de C2-E y C2-S. Ver `raw/docs/Estudio Pi – Ecosistema de cursos AutoCAD.md`.

---

## 8. C3: Gestión y presentación municipal (con tu socia gestora)

> Stub — crear sección dedicada cuando se documente. Ver `raw/docs/`.

---

## 9. C4: AutoCAD 3D, impresión 3D y CNC

> Stub — contenido derivado de la fuente original. Ver `raw/docs/`.

---

## 10. Agente IA: panorama de conexiones MCP

### 10.1 Resumen: qué se puede conectar hoy

| Servidor                     | Qué hace                                                          | Tipo               | Lo mantiene             | Claude Code                  | Codex | OpenCode |
| ---------------------------- | ----------------------------------------------------------------- | ------------------ | ----------------------- | ---------------------------- | ----- | -------- |
| Autodesk Product Help        | Busca en la ayuda oficial (110+ productos, varios idiomas)        | Remoto (HTTP)      | Autodesk (oficial)      | Sí                           | Sí    | Sí       |
| AutoCAD and Civil 3D MCP     | Lee y analiza el dibujo abierto                                   | Interno de AutoCAD | Autodesk (oficial)      | No (solo Autodesk Assistant) | No    | No       |
| autocad-mcp (puran-water)    | Dibuja en AutoCAD LT 2024+ vía AutoLISP, o genera DXF sin AutoCAD | Local (stdio)      | Comunidad               | Sí                           | Sí    | Sí       |
| autocad-mcp (limuzi013)      | Controla AutoCAD 2026 completo vía COM                            | Local (stdio)      | Comunidad               | Sí                           | Sí    | Sí       |
| Revit Public MCP             | Lectura/escritura del modelo Revit 2027.2                         | Local (stdio)      | Autodesk (tech preview) | Sí                           | Sí    | Sí       |
| Fusion MCP / Fusion Data MCP | Modelado en vivo / datos en la nube                               | Local / Remoto     | Autodesk                | Sí                           | Sí    | Sí       |

Los tres clientes hablan el mismo protocolo, así que cualquier servidor stdio o HTTP funciona en los tres. Solo cambia el formato de la configuración. Los servidores que no son de Autodesk no aparecen documentados para estos tres clientes, pero la configuración es estándar.

---

## 11. Configuración de Claude Code, Codex y OpenCode

### 11.1 Resumen: configuración por cliente

| | Claude Code | Codex | OpenCode |
|---|---|---|---|
| Archivo de config | `~/.claude.json` o `.mcp.json` en la raíz del proyecto | `~/.codex/config.toml` (global) o `.codex/config.toml` (proyecto) | `opencode.json` / `opencode.jsonc`, bajo la clave `mcp` |
| Agregar remoto (HTTP) | `claude mcp add --transport http <nombre> <url>` | `codex mcp add <nombre> --url <url>` | `"type": "remote", "url": "..."` |
| Agregar local (stdio) | `claude mcp add --transport stdio <nombre> -- <comando> [args]` | `codex mcp add <nombre> -- <comando>` | `"type": "local", "command": ["...", "..."]` |
| Login OAuth | `/mcp` o `claude mcp login <nombre>` | `codex mcp login <nombre>` | `opencode mcp auth <nombre>` |
| Ver servidores | `/mcp` | `codex mcp list` | `opencode mcp list` |
| Diagnóstico | `/mcp` | `codex mcp --help` | `opencode mcp debug <nombre>` |
| Timeouts | — | `startup_timeout_sec` (10 s), `tool_timeout_sec` (60 s) | `timeout` en ms (5000 por defecto) |
| Limitar herramientas | permisos de Claude Code | `enabled_tools`, `disabled_tools`, `default_tools_approval_mode` | `tools` global o por agente |

Fuentes: [Claude Code – MCP](https://code.claude.com/docs/en/mcp) · [Codex – MCP](https://developers.openai.com/codex/mcp) · [OpenCode – MCP servers](https://opencode.ai/docs/mcp-servers/)

Detalles que suelen fallar:
- En Claude Code, el `--` separa las opciones de Claude del comando del servidor. Sin el `--`, Claude interpreta como propios flags del servidor como `--port`. Si en un JSON ponés `url` sin `type`, Claude Code toma la entrada como stdio y la saltea.
- En los archivos de configuración de Windows, las barras de las rutas van dobles en JSON (`C:\\ruta`). En TOML conviene usar comillas simples (`'C:\ruta'`) para que las barras no se interpreten.

### 11.2 Autodesk Product Help (conectarlo primero)
Endpoint: `https://developer.api.autodesk.com/knowledge/public/v1/mcp`. La documentación oficial lo marca como público y sin autenticación [[#^f50|50]]. Algunos directorios mencionan OAuth [[#^f52|52]]: si el cliente pide login, se abre el navegador. Herramientas: `get_available_products` y `search_help_content`.

```bash
# Claude Code
claude mcp add --transport http --scope user autodesk-help https://developer.api.autodesk.com/knowledge/public/v1/mcp
# Codex
codex mcp add autodesk-help --url https://developer.api.autodesk.com/knowledge/public/v1/mcp
```
```json
// OpenCode (opencode.json)
{ "$schema": "https://opencode.ai/config.json",
  "mcp": { "autodesk-help": { "type": "remote",
    "url": "https://developer.api.autodesk.com/knowledge/public/v1/mcp", "enabled": true } } }
```
Prueba: "Buscá en la ayuda de AutoCAD 2027, en es_ES, cómo crear un bloque dinámico con estados de visibilidad".

### 11.3 puran-water (AutoLISP o DXF sin AutoCAD) [[#^f57|57]]
- Backends: File IPC (Windows 10/11, AutoCAD LT 2024+, Python 3.10+ nativo) o ezdxf (sin AutoCAD, cualquier sistema operativo). Variable `AUTOCAD_MCP_BACKEND`: `auto`, `file_ipc` o `ezdxf`.
- Instalación: `git clone https://github.com/puran-water/autocad-mcp.git`, después `cd autocad-mcp` y `uv sync`. En AutoCAD: `APPLOAD` → `lisp-code/mcp_dispatch.lsp`.

### 11.4 limuzi013 (COM, AutoCAD completo) [[#^f56|56]]
- Requiere Windows, AutoCAD completo abierto con un dibujo activo y Python 3.10+. Solo guarda archivos dentro de `ACAD_MCP_OUTPUT_ROOT`. No incluye sombreados, impresión, xrefs ni sólidos 3D.
- Instalación: `git clone https://github.com/limuzi013/autocad-mcp.git`, crear el entorno con `py -3 -m venv .venv` e instalar con `.venv\Scripts\python.exe -m pip install .`.

### 11.5 Revit y Fusion (para más adelante)
- Revit Public MCP: solo funciona con Revit 2027.2 más el add-on. Hay tres variantes (Read, Write y Experimental) y el ejecutable es `Autodesk.RevitMcpServer.Stdio.exe` [[#^f54|54]].
- Fusion MCP: es local y se activa en Preferences > General > API. Fusion Data MCP es remoto y usa OAuth [[#^f55|55]].

### 11.6 Qué cliente elegir
- Claude Code: el más simple para empezar, se configura con un comando y tiene el panel `/mcp` [[#^f59|59]].
- Codex: el que da más control, con listas de herramientas permitidas o bloqueadas y aprobación antes de cada acción. Comparte la configuración con la app de escritorio y la extensión del IDE [[#^f60|60]].
- OpenCode: open source, funciona con distintos modelos (sirve para comparar costos) y tiene `opencode mcp debug` para diagnosticar [[#^f61|61]].

### 11.7 Seguridad
1. Trabajá sobre copias del DWG y con una carpeta de salida dedicada.
2. Activá la aprobación manual, sobre todo con servidores que ejecutan LISP.
3. Revisá el código de los MCP comunitarios antes de instalarlos.
4. Nunca guardes claves en `.mcp.json` ni en `.codex/config.toml` si vas a compartir esos archivos.

---

## 12. Plan de trabajo con AutoCAD 2027 (versión de prueba)

Compatibilidad de los conectores comunitarios con 2027:
- limuzi013 se verificó con AutoCAD 2026 y su biblioteca `acax25enu.tlb`. Busca automáticamente la `acax*.tlb` más nueva instalada [[#^f56|56]], y AutoCAD 2027 usa `acax26enu.tlb` [[#^f65|65]]. Es probable que funcione, pero no está verificado: probalo en un dibujo de prueba.
- puran-water está documentado para AutoCAD LT 2024+ [[#^f57|57]]. AutoCAD completo también ejecuta AutoLISP, pero el repositorio no lo documenta, así que también hay que probarlo.
- Si AutoCAD bloquea la carga del archivo LISP, agregá la carpeta del conector a TRUSTEDPATHS. Con SECURELOAD en 1 o 2, AutoCAD solo carga código desde ubicaciones de confianza [[#^f65|65]].

Plan sugerido para los 15 días:
| Días | Objetivo |
|---|---|
| 1–2 | Conectar Product Help MCP en Claude Code. Explorar Autodesk Assistant (consultas del dibujo, selección por instrucción) |
| 3–5 | Armar el Kit Estudio Pi v1: DWT + DWS + primeros bloques dinámicos (puerta, ventana, rótulo de local, carátula) |
| 6–7 | Probar la verificación de estándares con el Assistant 2027 contra tu DWS [[#^f24\|24]] |
| 8–10 | Instalar y probar un MCP comunitario (COM o LISP) sobre copias del kit |
| 11–12 | Probar el modo ezdxf: el agente genera DXF sin AutoCAD, para seguir trabajando cuando venza la prueba |
| 13–15 | Grabar demos y capturas para el material de C2 y del módulo de IA |

---

## 13. Licencias: prueba, educación y uso comercial

- Prueba: 15 días, no se puede extender [[#^f64|64]].
- Plan Education: gratis por un año, solo para fines educativos, para alumnos y docentes de instituciones acreditadas [[#^f62|62]]. Los participantes de centros de capacitación y programas de recapacitación no califican, y tampoco pueden usar la prueba de 30 días para capacitarse [[#^f63|63]].
- Qué implica para Estudio Pi: la cuenta de estudiante no sirve para trabajos de consultoría pagos, y tus alumnos de cursos privados no pueden usarla salvo que sean estudiantes de una institución acreditada. Conviene definir la política de licencias del curso: licencia propia de cada alumno, AutoCAD LT, o un convenio con una institución.

---

## 14. Próximos pasos

1. Pasame tus manuales para armar la tabla EN↔ES y la simbología eléctrica y sanitaria.
2. Definir con tu socia la jurisdicción piloto para C3 (CABA o un municipio de PBA).
3. Seguir el plan de 15 días de la sección 12.
4. Diseñar el agente: prompts, checklist municipal y flujo de cómputo.
5. Elegir el municipio piloto para SET-MUN.
6. Construir primero SET-GEN + SET-ARQ + SET-REP, que se usan en el curso 2D Avanzado, aprovechando la prueba de AutoCAD 2027.
7. Definir las políticas de LT: los alumnos con LT no tienen DWS [[#^f16|16]], así que su control se hace con el checklist y el agente IA.
8. Validar con tu manual IRAM la tabla de grosores y tipos de línea (IRAM 4502-23) antes de cerrar el CTB [[#^f11|11]].

---

## 15. Fuentes

[^1]: Autodesk, AutoCAD 2026 Help: Command Reference. https://help.autodesk.com/view/ACD/2026/ENU/?page=commands ^f1
[^2]: Autodesk, AutoCAD 2027 Help: Command Reference. https://help.autodesk.com/view/ACD/2027/ENU/?page=commands&q=* ^f2
[^3]: Autodesk, Commands for Working With 3D Models (2026). https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-6548456A-28BD-40CB-89BA-F19F5800C0ED ^f3
[^4]: Autodesk, New AutoCAD Commands and System Variables Reference (2027). https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-B93A458E-1A7F-4090-A8CF-87A31C24E404 ^f4
[^5]: Autodesk, Updated Commands and System Variables Reference (2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/CIV3D/2014/ENU/filesACD/GUID-4FEBA606-95E0-4DC4-A116-257ED86DCD58-htm.html ^f5
[^6]: Autodesk, AutoCAD Keyboard Commands & Shortcuts Guide. https://www.autodesk.com/shortcuts/autocad ^f6
[^7]: Autodesk, AutoCAD Shortcuts Guide (PDF). https://damassets.autodesk.net/content/dam/autodesk/www/shortcuts/autocad/AutoCAD-Shortcuts-Guide-Autodesk.pdf ^f7
[^8]: Autodesk, AutoCAD LT 2025 Shortcuts Guide (PDF). https://damassets.autodesk.com/content/dam/autodesk/www/pdfs/autocad-lt-2025-shortcut-guide-en.pdf ^f8
[^9]: Autodesk, AutoCAD for Mac 2025 Keyboard Shortcuts Guide (PDF). https://damassets.autodesk.net/content/dam/autodesk/www/pdfs/autocad-for-mac-2025-keyboard-shortcuts-guide-en.pdf ^f9
[^10]: Autodesk, Shortcut Keys Reference (AutoCAD 2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/CIV3D/2014/ENU/filesACD/GUID-B6A9C126-230D-47F5-8973-464BC80E3736-htm.html ^f10
[^11]: Autodesk, About Creating Command Aliases (2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/CIV3D/2014/ENU/filesACD/GUID-FE9AE544-F537-4D3B-8F75-B76484513787-htm.html ^f11
[^12]: Autodesk, Have You Tried: Command Aliases, Shortcut Keys, and AutoCorrect. https://help.autodesk.com/view/ACD/2025/ENU/?guid=GUID-D2B4BF16-B1F7-4EF2-89AF-88ACE85FAD73 ^f12
[^13]: Autodesk Blog, Work Faster in AutoCAD: Essential Keyboard Shortcuts and Commands. https://www.autodesk.com/blogs/autocad/work-faster-in-autocad-essential-keyboard-shortcuts-and-commands/ ^f13
[^14]: Autodesk, Welcome to AutoCAD Foundations (2026). https://help.autodesk.com/view/ACD/2026/ENU/?contextId=ACD_FOUNDATIONS_LANDING ^f14
[^15]: Autodesk, The Hitchhiker's Guide to AutoCAD. https://help.autodesk.com/view/ACDLT/2026/ENU/?contextId=HITCHHIKERSGUIDETOAUTOCADBASICS ^f15
[^16]: Autodesk Learn, Get started with AutoCAD. https://app.learn-one.autodesk.com/learn/ondemand/collection/get-started-with-autocad ^f16
[^17]: Autodesk, On-demand Learning: AutoCAD. https://www.autodesk.com/learn/catalog/autocad/product/AutoCAD ^f17
[^18]: Autodesk, AutoCAD tutorials for beginners & students. https://www.autodesk.com/solutions/aec/autocad-tutorials ^f18
[^19]: Autodesk, Autodesk Certified Professional in AutoCAD: Exam Objectives (dic. 2025). https://damassets.autodesk.net/content/dam/autodesk/www/campaigns/emea/docs/AutoCAD-ACP-Exam-Objectives_Dec2025.pdf ^f19
[^20]: Autodesk, Exam Guide: Autodesk Certified Professional in AutoCAD. https://damassets.autodesk.net/content/dam/autodesk/www/training-and-certification/docs/autocad-acp-exam-guide-beta.pdf ^f20
[^21]: Autodesk, What's New or Changed in AutoCAD 2027. https://help.autodesk.com/view/ACD/2027/ENU/?contextId=WHATS_NEW_2027_ACD ^f21
[^22]: Autodesk Blog, AutoCAD 2027: Redefining How You Create, Collaborate, and Deliver. https://www.autodesk.com/blogs/autocad/autocad-2027/ ^f22
[^23]: Autodesk, AutoCAD 2026 Release Notes. https://help.autodesk.com/view/ACD/2026/ENU/?guid=AUTOCAD_2026_RELEASE_NOTES ^f23
[^24]: Autodesk, AutoCAD 2027: Autodesk Assistant. https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-99E2D8F7-D4D9-4B3A-9E57-7B73D6BB12AD ^f24
[^25]: Autodesk Blog, AutoCAD 2027.1 Now Available. https://www.autodesk.com/blogs/autocad/autocad-2027-1/ ^f25
[^26]: Autodesk, AutoCAD 2026 Ayuda: Comandos para el inicio de dibujo (ESP). https://help.autodesk.com/cloudhelp/2026/ESP/AutoCAD-Core/files/GUID-18FAFA58-DB9E-41BF-B130-4ECB7016E4E2.htm ^f26
[^27]: Autodesk, About Foreign Language Support (AutoLISP), AutoCAD 2027. https://help.autodesk.com/view/ACD/2027/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-D156B6ED-B1B4-42CB-BE1D-CA251BFC08C3-htm.html ^f27
[^28]: CAD Forum, Interactive dictionary of AutoCAD commands (ES). https://www.cadforum.cz/en/command.asp?lan=ES ^f28
[^29]: Autodesk, Create a Stretchable Dynamic Block (2026). https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-4005A6BB-388A-4EC7-BF17-555F1E6C137C ^f29
[^30]: Autodesk, About Creating Dynamic Blocks. https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-LT/files/GUID-DF133028-1A0C-4739-859F-83D967041B91.htm ^f30
[^31]: Autodesk, Block Editor (visibility states). https://help.autodesk.com/view/ACDLT/2026/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-B69D58AD-7920-4198-AB2A-0E24B944F6CD-htm.html ^f31
[^32]: Autodesk, About Extracting Data from Block Attributes. https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-BA68DD22-A3CD-4538-90A9-6101C33BC963.htm ^f32
[^33]: Autodesk, About Data Extraction. https://help.autodesk.com/view/ACD/2025/ENU/?guid=GUID-B0D32260-45E3-4643-B574-7F6C31579B68 ^f33
[^34]: Autodesk Blog, Managing Your CAD Standards: Tuesday Tips With Frank. https://www.autodesk.com/blogs/autocad/cad-standards-tuesday-tips-with-frank/ ^f34
[^35]: Autodesk, CAD Standards Settings Dialog Box (2027). https://help.autodesk.com/cloudhelp/2027/ENU/AutoCAD-Core/files/GUID-E03CA0C6-C1EF-4C83-A0C7-B1EC9C484CD2.htm ^f35
[^36]: CAPBA Distrito 1, Guía base para dibujo de plano municipal. https://capbauno.org/wp-content/uploads/2023/04/GUIA-ELEMENTOS.pdf ^f36
[^37]: Municipalidad de Vicente López, Modelo de plano municipal. https://www.vicentelopez.gov.ar/contenido/archivos/2024-06-26-945-archivo.pdf ^f37
[^38]: Municipalidad de Zárate, Especificaciones para la presentación de planos 2024. https://zarate.gob.ar/wp-content/uploads/2024/03/ESPECIFICACIONES-PARA-LA-PRESENTACION-DE-PLANOS-2024.pdf ^f38
[^39]: AEA, Reglamentación AEA 90364-7-771 (Anexo 771-K: símbolos usuales). https://aea.org.ar/wp-content/uploads/2017/10/90364-7-771-2.pdf ^f39
[^40]: AEA, Reglamentaciones impresas. https://aea.org.ar/reglamentaciones/impresas/ ^f40
[^41]: AySA, Requisitos para solicitar planos sanitarios. https://aysa.com.ar/media-library/usuarios/tramites_online/Requisitos-planos-sanitarios_2024_V2.pdf ^f41
[^42]: GCBA, Armado de Planos. https://buenosaires.gob.ar/gcaba_historico/armado-de-planos ^f42
[^43]: GCBA, Instructivos de trámites. https://buenosaires.gob.ar/gcaba_historico/guia-de-tramites/instructivos-de-tramites ^f43
[^44]: CPIC, Normas (Disposición 118/DGROC/20). https://cpic.org.ar/normas/ ^f44
[^45]: GCBA, Reglamentos Técnicos del Código de Edificación. https://buenosaires.gob.ar/gcaba_historico/codigo-urbanistico-y-de-edificacion/reglamentos-tecnicos-del-codigo-de-edificacion ^f45
[^46]: Autodesk, About Printing 3D Models. https://help.autodesk.com/view/ACDLT/2026/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-16D8B210-E4FC-4E89-9905-B5F9C9569E39-htm.html ^f46
[^47]: Autodesk, Create STL File Dialog Box. https://help.autodesk.com/view/ACDLT/2026/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-4B5C0F42-2B82-49F0-946E-C1E22C8D7336-htm.html ^f47
[^48]: Autodesk University, Modeling Basics for 3D Printing Using AutoCAD. https://static.au-uw2-prd.autodesk.com/handout_6549_AC6549_Modeling_Basics_for_3D_Printing_Using_AutoCAD.pdf ^f48
[^49]: Autodesk, AutoCAD and Civil 3D MCP Server. https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_AutoCADCivil3DMcp_autodesk_autocad_civil_3d_mcp_html ^f49
[^50]: Autodesk, Autodesk Product Help MCP Server (documentación). https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_KnowledgeMcp_autodesk_product_help_mcp_server_html ^f50
[^51]: ADSK News, Autodesk launches Product Help MCP Server (09/04/2026). https://adsknews.autodesk.com/en/news/product-help-mcp-server/ ^f51
[^52]: MCP Servers, Autodesk Product Help: Setup Guide. https://mcpservers.org/remote-mcp-servers/autodesk-product-help ^f52
[^53]: Autodesk Platform Services, Building agentic AI: what's new (DevCon 2026). https://aps.autodesk.com/blog/building-agentic-ai-whats-new-autodesk-platform-services ^f53
[^54]: Autodesk, Setting Up Revit Public MCP Server. https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_RevitMcp_setting_up_revit_mcp_server_html ^f54
[^55]: Autodesk, Autodesk Fusion MCPs Overview. https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW ^f55
[^56]: Glama, autocad-mcp (COM, AutoCAD 2026). https://glama.ai/mcp/servers/Slacker-LLC/autocad-mcp/tree ^f56
[^57]: GitHub, puran-water/autocad-mcp. https://github.com/puran-water/autocad-mcp ^f57
[^58]: GitHub, BarryMcAdams/AutoCAD_MCP. https://github.com/BarryMcAdams/AutoCAD_MCP ^f58
[^59]: Anthropic, Claude Code: Connect to tools via MCP. https://code.claude.com/docs/en/mcp ^f59
[^60]: OpenAI, Codex: Model Context Protocol. https://developers.openai.com/codex/mcp ^f60
[^61]: OpenCode, MCP servers. https://opencode.ai/docs/mcp-servers/ ^f61
[^62]: Autodesk Education, All products (plan educativo). https://www.autodesk.com/education/edu-software/overview ^f62
[^63]: Autodesk, Students and Educators: Plan Eligibility. https://www.autodesk.com/support/account/education/students-educators/eligibility ^f63
[^64]: Autodesk, AutoCAD Free Trial. https://www.autodesk.com/products/autocad/free-trial ^f64
[^65]: Autodesk, AutoCAD 2027 Help: compatibilidad VBA y ActiveX (FRA). https://help.autodesk.com/cloudhelp/2027/FRA/AutoCAD-Customization/files/GUID-927E71C2-E515-438E-9D7A-246D97BEF93F.htm ^f65
[^66]: Autodesk Developer Blog, AutoCAD 2027 interoperabilidad para personalización. https://blog.autodesk.io/autocad-2027-interoperability-for-customization/ ^f66
[^67]: Autodesk, AutoCAD 2027 overview (precios). https://www.autodesk.com/products/autocad/overview ^f67

[^68]: NCS v6, AIA CAD Layer Guidelines: Layer Name Format. https://www.nationalcadstandard.org/ncs6/pdfs/ncs6_clg_lnf.pdf ^f68
[^69]: NCS v6, Uniform Drawing System, Module 1: Sheet Identification. https://www.nationalcadstandard.org/ncs6/pdfs/ncs6_uds1.pdf ^f69
[^70]: NCS v6, Frequently Asked Questions. https://www.nationalcadstandard.org/ncs6/faqs.php ^f70
[^71]: Wikipedia, ISO 13567. https://en.wikipedia.org/wiki/ISO_13567 ^f71
[^72]: iTeh Standards, ISO 13567-2:2017. https://standards.iteh.ai/catalog/standards/iso/392fa47f-9e0d-461c-a83f-97654fcb878d/iso-13567-2-2017 ^f72
[^73]: AEC (UK), Protocol for Layer Naming v4.1. https://aecuk.wordpress.com/wp-content/uploads/2018/06/aecukprotocolforlayernaming-v4-1.pdf ^f73
[^74]: NBS, Uniclass 2015: Download. https://uniclass.thenbs.com/download ^f74
[^75]: BI3M, ISO 19650: Naming and Information Structure. https://www.bi3m.com/knowledge/bim-and-digital-engineering-insights/iso-19650/naming-and-information-structure ^f75
[^76]: iTeh Standards, ISO 128-2:2020: Basic conventions for lines. https://standards.iteh.ai/catalog/standards/iso/a0c6a7e3-b7fa-4ea2-8d4b-6858cf97df24/iso-128-2-2020 ^f76
[^77]: UCP Biblioteca, Manual de Normas IRAM de Dibujo Tecnológico (2017). https://koha.ucp.edu.ar/cgi-bin/koha/opac-ISBDdetail.pl?biblionumber=48049 ^f77
[^78]: UNaM FIO, Construcción de Edificios: Replanteo. https://aulavirtual.fio.unam.edu.ar/pluginfile.php/323422/mod_resource/content/1/REPLANTEO.pdf ^f78
[^79]: UNLP FAU, Producción de Obras I: TP 7 Plano de Replanteo y de Obra (2023). https://blogs.ead.unlp.edu.ar/produccion/files/2016/09/TP-7-Replanteo-2023.pdf ^f79
[^80]: INPRES, CIRSOC 103 Parte I: Adenda (art. 1.3.4.1.b). http://contenidos.inpres.gob.ar/docs/Reglamentos/INPRES-CIRSOC-103_Parte_I-ADENDA.pdf ^f80
[^81]: Autodesk, About Creating and Managing CAD Standards. https://help.autodesk.com/view/OARX/2026/ENU/?guid=GUID-9985B23D-C42D-431D-B766-D1E5FE3ECC07 ^f81
[^82]: Civil Survey Solutions (YouTube), Webinar: AutoCAD CAD Standards. https://www.youtube.com/watch?v=HJbDNOC8GBQ ^f82
[^83]: Autodesk University, Handout CES463392 (CAD Standards Manager). https://static.au-uw2-prd.autodesk.com/Class_Handout_CES463392_Samuel_Lucido.pdf ^f83
[^84]: Autodesk, About Creating Tool Palettes (AutoCAD 2027). https://help.autodesk.com/cloudhelp/2027/ENU/AutoCAD-Core/files/GUID-6B20D7DF-447A-4A8D-8FF1-8339CF54FFBD.htm ^f84
[^85]: Autodesk, Layer States Manager (AutoCAD 2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/ACDLT/2014/ENU/files/GUID-3E0F662B-226F-4A27-B5BB-D15252CC994C-htm.html ^f85
[^86]: Autodesk, About Sheet Sets (AutoCAD 2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/ACDLT/2014/ENU/files/GUID-34D889BC-19AD-4CD1-ADB1-F359D9B515FB-htm.html ^f86
[^87]: Autodesk, About Plot Style Tables (AutoCAD 2026). https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-2FD01085-DDD8-49D2-A910-E63EA45A7FED.htm ^f87
[^88]: Autodesk, CAD Standards Settings Dialog Box (AutoCAD 2027). https://help.autodesk.com/cloudhelp/2027/ENU/AutoCAD-Core/files/GUID-E03CA0C6-C1EF-4C83-A0C7-B1EC9C484CD2.htm ^f88
[^89]: Autodesk, To Set Up an Autodesk Project to Use Connected Support Files (2027). https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-2EDD58B6-ACB8-40EE-93B7-6333B345857E ^f89
[^90]: Autodesk, What's New or Changed in AutoCAD 2027. https://help.autodesk.com/view/ACD/2027/ENU/?contextId=WHATS_NEW_2027_ACD ^f90
[^91]: Autodesk, Create a Stretchable Dynamic Block (2026). https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-4005A6BB-388A-4EC7-BF17-555F1E6C137C ^f91
[^92]: Autodesk, About Data Extraction. https://help.autodesk.com/view/ACD/2025/ENU/?guid=GUID-B0D32260-45E3-4643-B574-7F6C31579B68 ^f92
[^93]: Autodesk, About Extracting Data from Block Attributes. https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-BA68DD22-A3CD-4538-90A9-6101C33BC963.htm ^f93
[^94]: CAPBA Distrito 1, Guía base para dibujo de plano municipal. https://capbauno.org/wp-content/uploads/2023/04/GUIA-ELEMENTOS.pdf ^f94
[^95]: GCBA, Armado de Planos. https://buenosaires.gob.ar/gcaba_historico/armado-de-planos ^f95
[^96]: AEA, Reglamentación AEA 90364-7-771. https://aea.org.ar/wp-content/uploads/2017/10/90364-7-771-2.pdf ^f96
[^97]: AySA, Requisitos para solicitar planos sanitarios. https://aysa.com.ar/media-library/usuarios/tramites_online/Requisitos-planos-sanitarios_2024_V2.pdf ^f97
[^98]: arqMANES (YouTube), Plantilla (Template) AutoCAD: arquitectura. https://www.youtube.com/watch?v=iRpwMM1Ik1g ^f98
[^99]: ModelPro Academy (YouTube), AutoCAD: Templates & Layer Standards. https://www.youtube.com/watch?v=MAYwYopn3HI ^f99
[^100]: CAD Intentions (YouTube), 7 Ways to Automate Your AutoCAD Template. https://www.youtube.com/watch?v=fg-Z27l8bJ4 ^f100
[^101]: Javi Lapina (YouTube), Cuadro replanteo o coordenadas desde bloques en AutoCAD. https://www.youtube.com/watch?v=mDH4DV50x74 ^f101
[^102]: Cursos Fernando Montaño (YouTube), Replanteo. https://www.youtube.com/watch?v=D4m8JQ8BPXc ^f102
[^103]: Autodesk Blog, Managing Your CAD Standards: Tuesday Tips With Frank. https://www.autodesk.com/blogs/autocad/cad-standards-tuesday-tips-with-frank/ ^f103
[^104]: Autodesk, AutoCAD 2027: Autodesk Assistant. https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-99E2D8F7-D4D9-4B3A-9E57-7B73D6BB12AD ^f104
[^105]: Wiley (extracto de libro), Establishing the Foundation for Drawing Standards (Layer Translator y DWS). https://catalogimages.wiley.com/images/db/pdf/9781118798881.excerpt.pdf ^f105
