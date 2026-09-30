# Estudio Pi · AutoCAD: documento maestro
Cursos, comandos, normativa y agente IA (MCP)
Versión 1.0 · 27/09/2026 · Base: AutoCAD 2027 (versión de prueba), comandos en inglés

> Este documento une y reemplaza a los tres anteriores: "Fuentes oficiales y comandos (EN)", "Ecosistema de cursos + agente IA" y "Guía de conexiones MCP". Cada dato lleva una nota numerada [^n] que enlaza a la lista de fuentes del final, y desde cada fuente se puede volver al texto donde se usó.

---

## Índice
1. Situación actual y decisiones clave
2. Fuentes oficiales de Autodesk
3. Ecosistema de cursos
4. C1: AutoCAD Base (8 clases), comandos por clase
5. C2: AutoCAD 2D Avanzado + Paramétrico (alineado al ACP)
6. Extensiones: instalación eléctrica y sanitaria
7. C3: Gestión y presentación municipal
8. C4: AutoCAD 3D, impresión 3D y CNC
9. Agente IA: panorama de conexiones MCP
10. Configuración de Claude Code, Codex y OpenCode
11. Plan de trabajo con AutoCAD 2027 (versión de prueba)
12. Licencias: prueba, educación y uso comercial
13. Próximos pasos
14. Fuentes

---

## 1. Situación actual y decisiones clave

- Tenés instalada la versión de prueba de AutoCAD 2027. La prueba dura 15 días, vence sola y no se puede extender. Después, las opciones son una suscripción mensual (desactivando la renovación automática) o tokens Flex [^64]. El precio de lista es de USD 2.095 por año o USD 260 por mes [^67].
- AutoCAD 2027 incorpora Autodesk Assistant con IA. Puede verificar el dibujo contra un archivo de estándar, seleccionar objetos a partir de una instrucción en lenguaje natural y responder consultas sobre capas y uso de bloques. Estas funciones están en tech preview y Autodesk advierte que los resultados pueden no ser exactos [^24] [^21].
- AutoCAD 2027 no es compatible a nivel binario con 2026: los complementos compilados para 2026 hay que adaptarlos. Su biblioteca COM es `acax26enu.tlb` (versión 26.0) [^65] [^66]. Esto afecta a los conectores MCP de la comunidad probados en 2026 (ver sección 11).
- Conclusión: aprovechá los 15 días para probar lo que solo existe en 2027 (Assistant, verificación de estándares, conectores MCP) y armá el kit de plantillas y bloques. Para después de la prueba, dejá preparado un flujo que no dependa de la licencia (generación de DXF sin AutoCAD, sección 9).

---

## 2. Fuentes oficiales de Autodesk

### 2.1 Referencia de comandos
| Recurso | Uso |
|---|---|
| Command Reference 2026 (A–Z) [^1] | Lista oficial completa de comandos |
| Command Reference 2027 (A–Z) [^2] | Versión vigente, la que tenés instalada |
| Comandos para modelos 3D [^3] | 3DMOVE, 3DORBIT, BOX, CONVTOSOLID, etc. |
| Comandos y variables nuevos en 2027 [^4] | Qué cambió en la versión |
| Comandos y variables actualizados en 2026 [^5] | Cambios de la versión anterior |

### 2.2 Atajos y alias
| Recurso | Uso |
|---|---|
| Guía de atajos (web) [^6] | Página oficial con enlace al PDF |
| Guía de atajos (PDF imprimible con stickers) [^7] | Material para entregar a los alumnos |
| Guía de atajos LT 2025 [^8] / Mac 2025 [^9] | Variantes por producto y sistema |
| Referencia de teclas (F1–F12, Ctrl) [^10] | Tabla oficial |
| Crear alias (acad.pgp) [^11] | Personalizar atajos |
| Alias, teclas y AutoCorrect [^12] | Diferencias entre los tres mecanismos |
| Blog: atajos esenciales [^13] | Tabla de acción, comando, alias y uso |

### 2.3 Aprendizaje oficial
| Recurso | Uso |
|---|---|
| AutoCAD Foundations [^14] | Serie oficial para empezar a trabajar de forma independiente |
| The Hitchhiker's Guide to AutoCAD [^15] | Recorrido por los comandos esenciales |
| Get started with AutoCAD (13 ítems) [^16] | Colección on demand |
| Catálogo on demand / Quick Start [^17] | Tutoriales cortos |
| Tutoriales para principiantes [^18] | Hub de tutoriales |

### 2.4 Certificación, novedades y español
- Objetivos del examen ACP (dic. 2025) [^19] y guía del examen [^20].
- Novedades 2027 [^21], blog de AutoCAD 2027 [^22], notas de la versión 2026 [^23] y AutoCAD 2027.1 con un Assistant más contextual [^25].
- Ayuda oficial en español (ESP) [^26]. En la versión en español, anteponer un guion bajo ejecuta el comando en inglés (`_LINE`, `_OFFSET`) [^27]. Diccionario EN↔ES no oficial para cruzar datos [^28].

---

## 3. Ecosistema de cursos

| # | Curso | Estado | Deriva en |
|---|---|---|---|
| C1 | AutoCAD Base (8 × 2 h) | Lo dictás hoy | C2, C4 |
| C2 | AutoCAD 2D Avanzado + Paramétrico (alineado a los objetivos del ACP, sin ser oficial) | Nuevo | Extensiones eléctrica y sanitaria, C3 |
| C2-E | Extensión: instalación eléctrica | Nuevo | — |
| C2-S | Extensión: instalación sanitaria | Nuevo | — |
| C3 | Gestión y presentación municipal (con tu socia gestora) | Nuevo | — |
| C4 | AutoCAD 3D básico → impresión 3D y corte CNC | Ya lo dictaste | Alianzas con CNC e impresora 3D |
| IA | Agente personal CAD (transversal) | En diseño | Consultoría IA para estudios |
| Futuro | BIM (Revit), modelado 3D/Rhino, paramétrico, IA | Después | — |

Idea central: todos los cursos comparten el mismo "Kit Estudio Pi", formado por una plantilla DWT, un archivo de estándar DWS y una biblioteca de bloques. C1 lo usa, C2 lo construye, C3 lo aplica al trámite municipal y el agente IA lo controla.

---

## 4. C1: AutoCAD Base, comandos por clase
Alias: son los valores por defecto habituales del acad.pgp en inglés. Conviene validarlos contra la Command Reference 2027 [^2] o con ALIASEDIT, porque pueden variar según la versión o la personalización. Las teclas de función siguen la referencia oficial [^10].

**Clase 1: interfaz, archivos y navegación.** NEW/QNEW (Ctrl+N), OPEN (Ctrl+O), QSAVE/SAVEAS (Ctrl+S / Ctrl+Shift+S), UNITS (UN), ZOOM (Z; E = extensión, W = ventana), PAN (P), REGEN (RE), OPTIONS (OP), U/UNDO/REDO (Ctrl+Z / Ctrl+Y).

**Clase 2: dibujo y precisión.** LINE (L), CIRCLE (C), ARC (A), RECTANG (REC), POLYGON (POL), PLINE (PL), OSNAP (OS / F3), ORTHO (F8), POLAR (F10), Dynamic Input (F12), GRID/SNAP (F7/F9).

**Clase 3: edición I.** MOVE (M), COPY (CO/CP), ROTATE (RO), SCALE (SC), MIRROR (MI), OFFSET (O), ERASE (E), STRETCH (S).

**Clase 4: edición II.** TRIM (TR), EXTEND (EX), FILLET (F), CHAMFER (CHA), EXPLODE (X), JOIN (J), BREAK (BR), ARRAY (AR), PEDIT (PE), MATCHPROP (MA).

**Clase 5: capas y propiedades.** LAYER (LA), PROPERTIES (PR / Ctrl+1), LINETYPE (LT), LTSCALE (LTS), LAYISO/LAYUNISO, LAYOFF/LAYFRZ, QSELECT.

**Clase 6: bloques, sombreados y referencias.** BLOCK (B), INSERT (I), WBLOCK (W), BEDIT (BE), ATTDEF (ATT), HATCH (H), XREF/ATTACH (XR), PURGE (PU).

**Clase 7: texto, cotas y medición.** MTEXT (MT/T), TEXT (DT), STYLE (ST), DIM, DIMLINEAR (DLI), DIMALIGNED (DAL), DIMSTYLE (D), MLEADER (MLD), TABLE (TB), DIST (DI), MEASUREGEOM (MEA), AREA (AA).

**Clase 8: presentación e impresión.** LAYOUT (LO), MVIEW (MV), PAGESETUP, PLOT (Ctrl+P), EXPORTPDF, escalas anotativas (ANNOSCALE).

---

## 5. C2: AutoCAD 2D Avanzado + Paramétrico

### 5.1 Alineación con el ACP
El examen es de opción múltiple y se hace sin el software. Autodesk recomienda al menos 400 horas de uso (1.200 horas ideales) [^19].

| Dominio ACP | Peso | Módulo de C2 |
|---|---|---|
| Gestión de la aplicación y del dibujo: capas, UCS, propiedades, MEASUREGEOM, COUNT, AUDIT/RECOVER/PURGE | 22 % | Clases 1 y 7 |
| Anotación y detalle: estilos, tablas, escalas anotativas | 20 % | Clase 2 |
| Creación y edición de contenido: bloques, atributos, ATTSYNC, WBLOCK, paleta Blocks, sombreados, matrices asociativas, pinzamientos | 29 % | Clases 3, 4 y 5 |
| Configuración de la salida: layouts, ventanas gráficas, impresión | 16 % | Clase 8 |
| Colaboración: xrefs, compartir, comparar | 13 % | Clase 8 |

Recomendación: comunicarlo como "alineado a los objetivos del ACP" y no como "preparación oficial".

### 5.2 Programa (8 × 2 h)
| Clase | Tema | Comandos clave | Fuente |
|---|---|---|---|
| 1 | Plantilla DWT del estudio: unidades, capas por norma, estilos, tipos de línea (LM, eje medianero), layouts con carátula | LAYER, STYLE, DIMSTYLE, MLEADERSTYLE, TABLESTYLE, SCALELISTEDIT | [^2] |
| 2 | Anotación anotativa (1:50, 1:100 y 1:200 en un mismo dibujo), tablas y campos | ANNOTATIVE, CANNOSCALE, TABLE, FIELD | [^19] |
| 3 | Bloques dinámicos I: estirables (puertas, ventanas, mesadas) | BEDIT, parámetro Linear + acción Stretch | [^29] |
| 4 | Bloques dinámicos II: varias posiciones (estados de visibilidad), Flip, Rotate, Lookup, Array | BVSTATE, BVHIDE/BVSHOW, BPARAMETER, BACTION | [^30] [^31] |
| 5 | Atributos para cómputo: carátula inteligente, rótulos de locales, aberturas codificadas | ATTDEF, BATTMAN, ATTSYNC, DATAEXTRACTION → tabla o Excel, COUNT | [^32] [^33] |
| 6 | Paramétrico: restricciones geométricas y dimensionales, parámetros, bloques restringidos | GEOMCONSTRAINT, DIMCONSTRAINT, PARAMETERS, AUTOCONSTRAIN, BCPARAMETER | [^2] |
| 7 | Estándares (DWS) y salud del dibujo | STANDARDS, CHECKSTANDARDS, LAYTRANS, AUDIT, PURGE, OVERKILL | [^34] [^35] |
| 8 | Salida y colaboración + introducción al agente IA | SHEETSET, XREF, EXPORTPDF, PUBLISH, ETRANSMIT, DWGCOMPARE | [^19] |

En AutoCAD 2027, el Autodesk Assistant puede verificar el dibujo contra el archivo de estándar [^24]. Encaja directo en la clase 7.

### 5.3 Biblioteca mínima para un plano municipal
Según la guía base del CAPBA Distrito 1, un plano municipal lleva: plantas y cortes a 1:100 (uno transversal y uno longitudinal), una vista por cada frente, cotas parciales y totales, espesores de muro, destino y numeración de los locales, Línea Municipal con ochavas, ejes medianeros, niveles de piso, referencias de corte, pozo absorbente o bomba con sus distancias, y una carátula con balance de superficies, profesionales, datos catastrales, croquis de ubicación y zonificación [^36]. Hay otros modelos de referencia en Vicente López [^37] y Zárate, que piden siluetas a 1:200 y planillas de balance [^38].

| Bloque | Tipo | Parámetros / atributos |
|---|---|---|
| Carátula municipal (una por jurisdicción) | Atributos + campos | Titular, destino, partida, nomenclatura, profesionales, matrículas, superficies |
| Balance de superficies / siluetas | Tabla con campos | Terreno, cubierta, semicubierta, a construir, existente, a demoler, FOS, FOT |
| Puerta (de abrir, corrediza, vaivén) | Visibilidad + Stretch + Flip | Código, ancho, tipo |
| Ventana / paño fijo | Stretch + visibilidad | Código, ancho × alto, tipo |
| Rótulo de local | Atributos + campo de área | Número, destino, superficie |
| Artefactos sanitarios | Visibilidad | Código para cómputo |
| Escalera | Array + Stretch | Escalones, huella, contrahuella |
| Cota de nivel, flecha de corte, norte | Atributos | Nivel, letra, hoja |
| Pozo absorbente / cámara séptica / bomba | Atributos | Distancias a EM y LM |
| Tipos de línea: LM, eje medianero, proyección | Linetype | — |
| Sombreados: existente / a construir / a demoler | Hatch por capa | Depende del municipio (confirmar con tu socia) |

---

## 6. Extensiones de C2

### C2-E: Instalación eléctrica
- Norma base: Reglamentación AEA 90364, parte 7-771 (viviendas, oficinas y locales). Su Anexo 771-K trae los "Símbolos usuales" [^39]. Catálogo de ediciones vigentes: [^40].
- Bloques con atributos: boca de iluminación, tomacorriente, interruptor, tablero principal o seccional, caja de paso. Atributos: circuito, tipo, potencia, altura.
- Cómputo con DATAEXTRACTION [^33]: bocas por circuito y por tablero → planilla de materiales.

### C2-S: Instalación sanitaria
- En CABA, los planos sanitarios pasan por AySA [^41].
- Bloques: artefactos, piletas de patio, bocas de acceso, cámaras, tanque de reserva o bombeo, llaves de paso, montantes (capas separadas para agua fría, agua caliente, cloaca y pluvial).
- Cómputo: cantidad de artefactos y accesorios, y metros de cañería con MEASUREGEOM o polilíneas por capa más extracción de datos.
- Pendiente: la simbología normativa local, a partir de tus manuales o del material de tu socia. No encontré una ficha pública de AySA equivalente al anexo de la AEA.

---

## 7. C3: Gestión y presentación municipal

### CABA
- Página "Armado de Planos" del GCBA: template y carátula reglamentaria para planos de obra e instalaciones, instrucciones para publicar en PDF y "Protocolos CAD", con una botonera para AutoCAD, su template y videos explicativos [^42].
- Instructivos de trámites: llenado de carátulas, ejemplos de cómputo y planillas de superficies para calcular la plusvalía, y acceso a TAD [^43].
- La Disposición 118/DGROC/20 aprueba los modelos de documentación oficial para registrar planos de obra, de instalaciones y de prehorizontalidad [^44].
- Reglamentos Técnicos del Código de Edificación [^45].

### Provincia de Buenos Aires
Cada municipio tiene su propio modelo. Conviene armar un módulo por jurisdicción, tomando como referencia la guía del CAPBA 1 [^36] y los modelos de Vicente López [^37] y Zárate [^38].

### Estructura sugerida (4 a 6 clases)
1. Circuito del trámite y roles (profesional y gestor), documentación previa.
2. Carátula y template reglamentario en AutoCAD, con la botonera de CABA [^42].
3. Balance de superficies, siluetas y FOS/FOT con campos y tablas.
4. PDF, firma y carga en TAD (CABA) o en mesa de entradas (PBA).
5. Observaciones típicas y checklist (que después automatiza el agente IA).
6. Caso práctico completo.

---

## 8. C4: AutoCAD 3D, impresión 3D y CNC

| Salida | Flujo | Fuente |
|---|---|---|
| Impresión 3D | Sólidos cerrados, sin huecos → 3DPRINT o STLOUT → STL → slicer | [^46] [^47] [^48] |
| Corte CNC o láser | 2D en mm, polilíneas cerradas (JOIN, PEDIT), limpieza con OVERKILL, una capa por operación → DXF. Desde el 3D, usar FLATSHOT o SECTIONPLANE | [^1] [^3] |
| Futuro: Fusion | MCP de Fusion para modelar con IA y Fusion Data para gestionar datos | [^55] |

Propuesta con tus contactos: un taller de "maqueta digital a física", con placas cortadas por CNC y detalles impresos en 3D. Antes de armarlo, pediles el formato exacto que acepta cada máquina: tipo de DXF, versión, capas y colores.

---

## 9. Agente IA: panorama de conexiones MCP

### 9.1 Qué existe hoy
| Servidor | Qué hace | Tipo | Lo mantiene | Clientes |
|---|---|---|---|---|
| Autodesk Assistant (AutoCAD 2027) | Chat con IA, verificación de estándares, selección por instrucción, consultas del dibujo | Integrado | Autodesk | Solo dentro de AutoCAD [^24] |
| AutoCAD and Civil 3D MCP | Lee y analiza el dibujo abierto: objetos, capas, estilos, estadísticas, cumplimiento de la plantilla | Local, dentro de AutoCAD (Windows) | Autodesk | Documentado solo para Autodesk Assistant. En AutoCAD es de lectura y análisis; la escritura solo está en Civil 3D [^49] |
| Autodesk Product Help MCP | Busca en la ayuda oficial (más de 110 productos, varios idiomas), solo lectura, gratis | Remoto, Streamable HTTP | Autodesk | Cualquier cliente MCP [^50] [^51] [^52] |
| Fusion, Fusion Data y Revit MCP | Modelado y datos en Fusion; consulta y edición de modelos Revit | Local o remoto | Autodesk (tech preview o beta) | Clientes MCP [^53] [^54] [^55] |
| autocad-mcp (limuzi013) | Controla AutoCAD 2026 completo vía COM: capas, geometría 2D, cotas, bloques, captura de pantalla. No tiene comando libre | Local, stdio | Comunidad | Claude Code, Claude Desktop, Codex [^56] |
| autocad-mcp (puran-water) | AutoCAD LT 2024+ vía AutoLISP, o genera DXF con ezdxf sin tener AutoCAD | Local, stdio | Comunidad | Cualquier cliente stdio [^57] |
| AutoCAD_MCP (BarryMcAdams) | Automatización 2D/3D para AutoCAD 2025 | Local | Comunidad | [^58] |

### 9.2 Arquitectura propuesta: "Agente Estudio Pi"
```
Agente (Claude Code / Codex / OpenCode)
 ├─ Conocimiento
 │   ├─ Autodesk Product Help MCP → "cómo se hace", con la ayuda oficial
 │   └─ Tus manuales + wiki (Obsidian/Markdown) → normativa local y convenciones del estudio
 ├─ Dibujo (local, Windows)
 │   ├─ Con AutoCAD abierto: MCP comunitario (COM o AutoLISP)
 │   └─ Sin AutoCAD: generación de DXF con ezdxf
 ├─ Control de calidad
 │   ├─ DWS + CHECKSTANDARDS / Autodesk Assistant 2027
 │   └─ Checklist municipal (C3) en Markdown
 └─ Cómputo
     └─ DATAEXTRACTION → CSV/Excel → planilla de materiales y presupuesto
```

---

## 10. Configuración de Claude Code, Codex y OpenCode

Los tres clientes usan el mismo protocolo (MCP), así que cualquier servidor stdio o HTTP funciona en los tres. Solo cambia el formato de la configuración.

### 10.1 Comparativa
| | Claude Code [^59] | Codex [^60] | OpenCode [^61] |
|---|---|---|---|
| Archivo | `~/.claude.json` (local/usuario) o `.mcp.json` en el proyecto | `~/.codex/config.toml` o `.codex/config.toml` (proyecto de confianza) | `opencode.json` / `.jsonc`, clave `mcp` |
| Servidor remoto | `claude mcp add --transport http <nombre> <url>` | `codex mcp add <nombre> --url <url>` | `"type": "remote", "url": "..."` |
| Servidor local | `claude mcp add --transport stdio <nombre> -- <comando>` | `codex mcp add <nombre> -- <comando>` | `"type": "local", "command": [...]` |
| Login OAuth | `/mcp` o `claude mcp login <nombre>` | `codex mcp login <nombre>` | `opencode mcp auth <nombre>` |
| Listar / diagnosticar | `/mcp` | `codex mcp list` | `opencode mcp list`, `opencode mcp debug` |
| Timeouts | — | `startup_timeout_sec` (10 s), `tool_timeout_sec` (60 s) | `timeout` en ms (5.000) |
| Control de herramientas | Permisos del cliente | `enabled_tools`, `disabled_tools`, `default_tools_approval_mode` | `tools` global o por agente |

Detalles que suelen fallar:
- En Claude Code, el `--` separa las opciones del cliente del comando del servidor. Un JSON con `url` pero sin `type` se toma como stdio y se ignora [^59].
- En Windows, las rutas van con barras dobles en JSON (`C:\\ruta`). En TOML conviene usar comillas simples (`'C:\ruta'`) [^56].

### 10.2 Autodesk Product Help (conectarlo primero)
Endpoint: `https://developer.api.autodesk.com/knowledge/public/v1/mcp`. La documentación oficial lo marca como público y sin autenticación [^50]. Algunos directorios mencionan OAuth [^52]: si el cliente pide login, se abre el navegador. Herramientas: `get_available_products` y `search_help_content`.

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

### 10.3 puran-water (AutoLISP o DXF sin AutoCAD) [^57]
- Backends: File IPC (Windows 10/11, AutoCAD LT 2024+, Python 3.10+ nativo) o ezdxf (sin AutoCAD, cualquier sistema operativo). Variable `AUTOCAD_MCP_BACKEND`: `auto`, `file_ipc` o `ezdxf`.
- Instalación: `git clone https://github.com/puran-water/autocad-mcp.git`, después `cd autocad-mcp` y `uv sync`. En AutoCAD: `APPLOAD` → `lisp-code/mcp_dispatch.lsp`.
- Permite ejecutar AutoLISP libre: trabajá sobre copias y con aprobación manual.

```bash
claude mcp add --transport stdio --env AUTOCAD_MCP_BACKEND=auto autocad-lisp -- C:\ruta\autocad-mcp\.venv\Scripts\python.exe -m autocad_mcp
```
```toml
# Codex
[mcp_servers.autocad-lisp]
command = 'C:\ruta\autocad-mcp\.venv\Scripts\python.exe'
args = ["-m", "autocad_mcp"]
startup_timeout_sec = 20
default_tools_approval_mode = "prompt"
[mcp_servers.autocad-lisp.env]
AUTOCAD_MCP_BACKEND = "auto"
```
```json
// OpenCode
"autocad-lisp": { "type": "local",
  "command": ["C:\\ruta\\autocad-mcp\\.venv\\Scripts\\python.exe", "-m", "autocad_mcp"],
  "environment": { "AUTOCAD_MCP_BACKEND": "auto" }, "timeout": 20000 }
```

### 10.4 limuzi013 (COM, AutoCAD completo) [^56]
- Requiere Windows, AutoCAD completo abierto con un dibujo activo y Python 3.10+. Solo guarda archivos dentro de `ACAD_MCP_OUTPUT_ROOT`. No incluye sombreados, impresión, xrefs ni sólidos 3D.
- Instalación: `git clone https://github.com/limuzi013/autocad-mcp.git`, crear el entorno con `py -3 -m venv .venv` e instalar con `.venv\Scripts\python.exe -m pip install .`.

```toml
# Codex
[mcp_servers.autocad-com]
command = 'C:\ruta\.venv\Scripts\autocad-mcp.exe'
[mcp_servers.autocad-com.env]
ACAD_MCP_OUTPUT_ROOT = 'C:\EstudioPi\salidas'
```
```bash
claude mcp add --transport stdio --env ACAD_MCP_OUTPUT_ROOT=C:\EstudioPi\salidas autocad-com -- C:\ruta\.venv\Scripts\autocad-mcp.exe
```
Prueba: con AutoCAD abierto, pedile al agente que llame a `autocad_status`.

### 10.5 Revit y Fusion (para más adelante)
- Revit Public MCP: solo funciona con Revit 2027.2 más el add-on. Hay tres variantes (Read, Write y Experimental) y el ejecutable es `Autodesk.RevitMcpServer.Stdio.exe` [^54].
- Fusion MCP: es local y se activa en Preferences > General > API. Fusion Data MCP es remoto y usa OAuth [^55].

### 10.6 Qué cliente elegir
- Claude Code: el más simple para empezar, se configura con un comando y tiene el panel `/mcp` [^59].
- Codex: el que da más control, con listas de herramientas permitidas o bloqueadas y aprobación antes de cada acción. Comparte la configuración con la app de escritorio y la extensión del IDE [^60].
- OpenCode: open source, funciona con distintos modelos (sirve para comparar costos) y tiene `opencode mcp debug` para diagnosticar [^61].

### 10.7 Seguridad
1. Trabajá sobre copias del DWG y con una carpeta de salida dedicada.
2. Activá la aprobación manual, sobre todo con servidores que ejecutan LISP.
3. Revisá el código de los MCP comunitarios antes de instalarlos.
4. Nunca guardes claves en `.mcp.json` ni en `.codex/config.toml` si vas a compartir esos archivos.

---

## 11. Plan de trabajo con AutoCAD 2027 (versión de prueba)

Compatibilidad de los conectores comunitarios con 2027:
- limuzi013 se verificó con AutoCAD 2026 y su biblioteca `acax25enu.tlb`. Busca automáticamente la `acax*.tlb` más nueva instalada [^56], y AutoCAD 2027 usa `acax26enu.tlb` [^65]. Es probable que funcione, pero no está verificado: probalo en un dibujo de prueba.
- puran-water está documentado para AutoCAD LT 2024+ [^57]. AutoCAD completo también ejecuta AutoLISP, pero el repositorio no lo documenta, así que también hay que probarlo.
- Si AutoCAD bloquea la carga del archivo LISP, agregá la carpeta del conector a TRUSTEDPATHS. Con SECURELOAD en 1 o 2, AutoCAD solo carga código desde ubicaciones de confianza [^65].

Plan sugerido para los 15 días:
| Días | Objetivo |
|---|---|
| 1–2 | Conectar Product Help MCP en Claude Code. Explorar Autodesk Assistant (consultas del dibujo, selección por instrucción) |
| 3–5 | Armar el Kit Estudio Pi v1: DWT + DWS + primeros bloques dinámicos (puerta, ventana, rótulo de local, carátula) |
| 6–7 | Probar la verificación de estándares con el Assistant 2027 contra tu DWS [^24] |
| 8–10 | Instalar y probar un MCP comunitario (COM o LISP) sobre copias del kit |
| 11–12 | Probar el modo ezdxf: el agente genera DXF sin AutoCAD, para seguir trabajando cuando venza la prueba |
| 13–15 | Grabar demos y capturas para el material de C2 y del módulo de IA |

---

## 12. Licencias: prueba, educación y uso comercial
- Prueba: 15 días, no se puede extender [^64].
- Plan Education: gratis por un año, solo para fines educativos, para alumnos y docentes de instituciones acreditadas [^62]. Los participantes de centros de capacitación y programas de recapacitación no califican, y tampoco pueden usar la prueba de 30 días para capacitarse [^63].
- Qué implica para Estudio Pi: la cuenta de estudiante no sirve para trabajos de consultoría pagos, y tus alumnos de cursos privados no pueden usarla salvo que sean estudiantes de una institución acreditada. Conviene definir la política de licencias del curso: licencia propia de cada alumno, AutoCAD LT, o un convenio con una institución.

---

## 13. Próximos pasos
1. Pasame tus manuales para armar la tabla EN↔ES y la simbología eléctrica y sanitaria.
2. Definir con tu socia la jurisdicción piloto para C3 (CABA o un municipio de PBA).
3. Seguir el plan de 15 días de la sección 11.
4. Diseñar el agente: prompts, checklist municipal y flujo de cómputo.

---

## 14. Fuentes

[^1]: Autodesk, AutoCAD 2026 Help: Command Reference. https://help.autodesk.com/view/ACD/2026/ENU/?page=commands
[^2]: Autodesk, AutoCAD 2027 Help: Command Reference. https://help.autodesk.com/view/ACD/2027/ENU/?page=commands&q=*
[^3]: Autodesk, Commands for Working With 3D Models (2026). https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-6548456A-28BD-40CB-89BA-F19F5800C0ED
[^4]: Autodesk, New AutoCAD Commands and System Variables Reference (2027). https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-B93A458E-1A7F-4090-A8CF-87A31C24E404
[^5]: Autodesk, Updated Commands and System Variables Reference (2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/CIV3D/2014/ENU/filesACD/GUID-4FEBA606-95E0-4DC4-A116-257ED86DCD58-htm.html
[^6]: Autodesk, AutoCAD Keyboard Commands & Shortcuts Guide. https://www.autodesk.com/shortcuts/autocad
[^7]: Autodesk, AutoCAD Shortcuts Guide (PDF). https://damassets.autodesk.net/content/dam/autodesk/www/shortcuts/autocad/AutoCAD-Shortcuts-Guide-Autodesk.pdf
[^8]: Autodesk, AutoCAD LT 2025 Shortcuts Guide (PDF). https://damassets.autodesk.com/content/dam/autodesk/www/pdfs/autocad-lt-2025-shortcut-guide-en.pdf
[^9]: Autodesk, AutoCAD for Mac 2025 Keyboard Shortcuts Guide (PDF). https://damassets.autodesk.net/content/dam/autodesk/www/pdfs/autocad-for-mac-2025-keyboard-shortcuts-guide-en.pdf
[^10]: Autodesk, Shortcut Keys Reference (AutoCAD 2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/CIV3D/2014/ENU/filesACD/GUID-B6A9C126-230D-47F5-8973-464BC80E3736-htm.html
[^11]: Autodesk, About Creating Command Aliases (2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/CIV3D/2014/ENU/filesACD/GUID-FE9AE544-F537-4D3B-8F75-B76484513787-htm.html
[^12]: Autodesk, Have You Tried: Command Aliases, Shortcut Keys, and AutoCorrect. https://help.autodesk.com/view/ACD/2025/ENU/?guid=GUID-D2B4BF16-B1F7-4EF2-89AF-88ACE85FAD73
[^13]: Autodesk Blog, Work Faster in AutoCAD: Essential Keyboard Shortcuts and Commands. https://www.autodesk.com/blogs/autocad/work-faster-in-autocad-essential-keyboard-shortcuts-and-commands/
[^14]: Autodesk, Welcome to AutoCAD Foundations (2026). https://help.autodesk.com/view/ACD/2026/ENU/?contextId=ACD_FOUNDATIONS_LANDING
[^15]: Autodesk, The Hitchhiker's Guide to AutoCAD. https://help.autodesk.com/view/ACDLT/2026/ENU/?contextId=HITCHHIKERSGUIDETOAUTOCADBASICS
[^16]: Autodesk Learn, Get started with AutoCAD. https://app.learn-one.autodesk.com/learn/ondemand/collection/get-started-with-autocad
[^17]: Autodesk, On-demand Learning: AutoCAD. https://www.autodesk.com/learn/catalog/autocad/product/AutoCAD
[^18]: Autodesk, AutoCAD tutorials for beginners & students. https://www.autodesk.com/solutions/aec/autocad-tutorials
[^19]: Autodesk, Autodesk Certified Professional in AutoCAD: Exam Objectives (dic. 2025). https://damassets.autodesk.net/content/dam/autodesk/www/campaigns/emea/docs/AutoCAD-ACP-Exam-Objectives_Dec2025.pdf
[^20]: Autodesk, Exam Guide: Autodesk Certified Professional in AutoCAD. https://damassets.autodesk.net/content/dam/autodesk/www/training-and-certification/docs/autocad-acp-exam-guide-beta.pdf
[^21]: Autodesk, What's New or Changed in AutoCAD 2027. https://help.autodesk.com/view/ACD/2027/ENU/?contextId=WHATS_NEW_2027_ACD
[^22]: Autodesk Blog, AutoCAD 2027: Redefining How You Create, Collaborate, and Deliver. https://www.autodesk.com/blogs/autocad/autocad-2027/
[^23]: Autodesk, AutoCAD 2026 Release Notes. https://help.autodesk.com/view/ACD/2026/ENU/?guid=AUTOCAD_2026_RELEASE_NOTES
[^24]: Autodesk, AutoCAD 2027: Autodesk Assistant. https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-99E2D8F7-D4D9-4B3A-9E57-7B73D6BB12AD
[^25]: Autodesk Blog, AutoCAD 2027.1 Now Available. https://www.autodesk.com/blogs/autocad/autocad-2027-1/
[^26]: Autodesk, AutoCAD 2026 Ayuda: Comandos para el inicio de dibujos (ESP). https://help.autodesk.com/cloudhelp/2026/ESP/AutoCAD-Core/files/GUID-18FAFA58-DB9E-41BF-B130-4ECB7016E4E2.htm
[^27]: Autodesk, About Foreign Language Support (AutoLISP), AutoCAD 2027. https://help.autodesk.com/view/ACD/2027/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-D156B6ED-B1B4-42CB-BE1D-CA251BFC08C3-htm.html
[^28]: CAD Forum, Interactive dictionary of AutoCAD commands (ES). https://www.cadforum.cz/en/command.asp?lan=ES
[^29]: Autodesk, Create a Stretchable Dynamic Block (2026). https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-4005A6BB-388A-4EC7-BF17-555F1E6C137C
[^30]: Autodesk, About Creating Dynamic Blocks. https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-LT/files/GUID-DF133028-1A0C-4739-859F-83D967041B91.htm
[^31]: Autodesk, Block Editor (visibility states). https://help.autodesk.com/view/ACDLT/2026/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-B69D58AD-7920-4198-AB2A-0E24B944F6CD-htm.html
[^32]: Autodesk, About Extracting Data from Block Attributes. https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-BA68DD22-A3CD-4538-90A9-6101C33BC963.htm
[^33]: Autodesk, About Data Extraction. https://help.autodesk.com/view/ACD/2025/ENU/?guid=GUID-B0D32260-45E3-4643-B574-7F6C31579B68
[^34]: Autodesk Blog, Managing Your CAD Standards: Tuesday Tips With Frank. https://www.autodesk.com/blogs/autocad/cad-standards-tuesday-tips-with-frank/
[^35]: Autodesk, CAD Standards Settings Dialog Box (2027). https://help.autodesk.com/cloudhelp/2027/ENU/AutoCAD-Core/files/GUID-E03CA0C6-C1EF-4C83-A0C7-B1EC9C484CD2.htm
[^36]: CAPBA Distrito 1, Guía base para dibujo de plano municipal. https://capbauno.org/wp-content/uploads/2023/04/GUIA-ELEMENTOS.pdf
[^37]: Municipalidad de Vicente López, Modelo de plano municipal. https://www.vicentelopez.gov.ar/contenido/archivos/2024-06-26-945-archivo.pdf
[^38]: Municipalidad de Zárate, Especificaciones para la presentación de planos 2024. https://zarate.gob.ar/wp-content/uploads/2024/03/ESPECIFICACIONES-PARA-LA-PRESENTACION-DE-PLANOS-2024.pdf
[^39]: AEA, Reglamentación AEA 90364-7-771 (Anexo 771-K: símbolos usuales). https://aea.org.ar/wp-content/uploads/2017/10/90364-7-771-2.pdf
[^40]: AEA, Reglamentaciones impresas. https://aea.org.ar/reglamentaciones/impresas/
[^41]: AySA, Requisitos para solicitar planos sanitarios. https://aysa.com.ar/media-library/usuarios/tramites_online/Requisitos-planos-sanitarios_2024_V2.pdf
[^42]: GCBA, Armado de Planos. https://buenosaires.gob.ar/gcaba_historico/armado-de-planos
[^43]: GCBA, Instructivos de trámites. https://buenosaires.gob.ar/gcaba_historico/guia-de-tramites/instructivos-de-tramites
[^44]: CPIC, Normas (Disposición 118/DGROC/20). https://cpic.org.ar/normas/
[^45]: GCBA, Reglamentos Técnicos del Código de Edificación. https://buenosaires.gob.ar/gcaba_historico/codigo-urbanistico-y-de-edificacion/reglamentos-tecnicos-del-codigo-de-edificacion
[^46]: Autodesk, About Printing 3D Models. https://help.autodesk.com/view/ACDLT/2026/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-16D8B210-E4FC-4E89-9905-B5F9C9569E39-htm.html
[^47]: Autodesk, Create STL File Dialog Box. https://help.autodesk.com/view/ACDLT/2026/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-4B5C0F42-2B82-49F0-946E-C1E22C8D7336-htm.html
[^48]: Autodesk University, Modeling Basics for 3D Printing Using AutoCAD. https://static.au-uw2-prd.autodesk.com/handout_6549_AC6549_Modeling_Basics_for_3D_Printing_Using_AutoCAD.pdf
[^49]: Autodesk, AutoCAD and Civil 3D MCP Server. https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_AutoCADCivil3DMcp_autodesk_autocad_civil_3d_mcp_html
[^50]: Autodesk, Autodesk Product Help MCP Server (documentación). https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_KnowledgeMcp_autodesk_product_help_mcp_server_html
[^51]: ADSK News, Autodesk launches Product Help MCP Server (09/04/2026). https://adsknews.autodesk.com/en/news/product-help-mcp-server/
[^52]: MCP Servers, Autodesk Product Help: Setup Guide. https://mcpservers.org/remote-mcp-servers/autodesk-product-help
[^53]: Autodesk Platform Services, Building agentic AI: what's new (DevCon 2026). https://aps.autodesk.com/blog/building-agentic-ai-whats-new-autodesk-platform-services
[^54]: Autodesk, Setting Up Revit Public MCP Server. https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_RevitMcp_setting_up_revit_mcp_server_html
[^55]: Autodesk, Autodesk Fusion MCPs Overview. https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW
[^56]: Glama, autocad-mcp (COM, AutoCAD 2026). https://glama.ai/mcp/servers/Slacker-LLC/autocad-mcp/tree
[^57]: GitHub, puran-water/autocad-mcp. https://github.com/puran-water/autocad-mcp
[^58]: GitHub, BarryMcAdams/AutoCAD_MCP. https://github.com/BarryMcAdams/AutoCAD_MCP
[^59]: Anthropic, Claude Code: Connect to tools via MCP. https://code.claude.com/docs/en/mcp
[^60]: OpenAI, Codex: Model Context Protocol. https://developers.openai.com/codex/mcp
[^61]: OpenCode, MCP servers. https://opencode.ai/docs/mcp-servers/
[^62]: Autodesk Education, All products (plan educativo). https://www.autodesk.com/education/edu-software/overview
[^63]: Autodesk, Students and Educators: Plan Eligibility. https://www.autodesk.com/support/account/education/students-educators/eligibility
[^64]: Autodesk, AutoCAD Free Trial. https://www.autodesk.com/products/autocad/free-trial
[^65]: Autodesk, AutoCAD 2027 Help: compatibilidad VBA y ActiveX (FRA). https://help.autodesk.com/cloudhelp/2027/FRA/AutoCAD-Customization/files/GUID-927E71C2-E515-438E-9D7A-246D97BEF93F.htm
[^66]: Autodesk Developer Blog, AutoCAD 2027 interoperabilidad para personalización. https://blog.autodesk.io/autocad-2027-interoperability-for-customization/
[^67]: Autodesk, AutoCAD 2027 overview (precios). https://www.autodesk.com/products/autocad/overview
