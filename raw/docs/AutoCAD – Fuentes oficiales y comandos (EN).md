# AutoCAD (Autodesk): fuentes oficiales + mapa de comandos en inglés
Fase 1 de la investigación para Estudio Pi · Base: AutoCAD 2026/2027 (Windows) · Fecha: 27/09/2026

> Alcance: solo AutoCAD de Autodesk, comandos en INGLÉS (nombre global + alias por defecto del archivo acad.pgp). La versión en español (nombres y alias locales) queda para la fase 2.

---

## 1. Fuentes oficiales de Autodesk (priorizadas)

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

### F. Puente a la fase 2 (español)
- La ayuda oficial existe en español (idioma ESP), p. ej.: https://help.autodesk.com/cloudhelp/2026/ESP/AutoCAD-Core/files/GUID-18FAFA58-DB9E-41BF-B130-4ECB7016E4E2.htm
- Truco clave: en la versión en español, anteponer guion bajo ejecuta el comando inglés (`_LINE`, `_OFFSET`). Esto está documentado para AutoLISP: https://help.autodesk.com/view/ACD/2027/ENU/?caas=caas/documentation/ACD/2014/ENU/files/GUID-D156B6ED-B1B4-42CB-BE1D-CA251BFC08C3-htm.html
- Diccionario EN↔ES (no oficial, útil para cruzar datos): https://www.cadforum.cz/en/command.asp?lan=ES

---

## 2. Comandos esenciales por clase (curso de 8 clases × 2 h)
Alias = valor por defecto del acad.pgp en inglés. Verificar siempre contra la Command Reference.

### Clase 1: Interfaz, archivos y navegación
| Comando | Alias | Función |
|---|---|---|
| NEW / QNEW | Ctrl+N | Nuevo dibujo (plantilla) |
| OPEN | Ctrl+O | Abrir |
| QSAVE / SAVEAS | Ctrl+S / Ctrl+Shift+S | Guardar |
| UNITS | UN | Unidades |
| ZOOM | Z | Zoom (E = Extents, W = Window) |
| PAN | P | Desplazar |
| REGEN | RE | Regenerar |
| OPTIONS | OP | Opciones |
| U / UNDO / REDO | Ctrl+Z / Ctrl+Y | Deshacer / rehacer |

### Clase 2: Dibujo básico y precisión
| Comando | Alias | Función |
|---|---|---|
| LINE | L | Línea |
| CIRCLE | C | Círculo |
| ARC | A | Arco |
| RECTANG | REC | Rectángulo |
| POLYGON | POL | Polígono |
| PLINE | PL | Polilínea |
| OSNAP | OS / F3 | Referencias a objetos |
| ORTHO | F8 | Modo ortogonal |
| POLAR | F10 | Rastreo polar |
| Dynamic Input | F12 | Entrada dinámica |
| GRID / SNAP | F7 / F9 | Rejilla / forzcursor |

### Clase 3: Edición I
| Comando | Alias | Función |
|---|---|---|
| MOVE | M | Mover |
| COPY | CO / CP | Copiar |
| ROTATE | RO | Rotar |
| SCALE | SC | Escalar |
| MIRROR | MI | Simetría |
| OFFSET | O | Desfase (paralelas) |
| ERASE | E | Borrar |
| STRETCH | S | Estirar |

### Clase 4: Edición II
| Comando | Alias | Función |
|---|---|---|
| TRIM | TR | Recortar |
| EXTEND | EX | Alargar |
| FILLET | F | Empalme |
| CHAMFER | CHA | Chaflán |
| EXPLODE | X | Descomponer |
| JOIN | J | Unir |
| BREAK | BR | Partir |
| ARRAY (RECT/POLAR/PATH) | AR | Matrices |
| PEDIT | PE | Editar polilínea |
| MATCHPROP | MA | Igualar propiedades |

### Clase 5: Capas y propiedades
| Comando | Alias | Función |
|---|---|---|
| LAYER | LA | Administrador de capas |
| PROPERTIES | PR / Ctrl+1 | Propiedades |
| LINETYPE | LT | Tipos de línea |
| LTSCALE | LTS | Escala de tipo de línea |
| LAYISO / LAYUNISO | — | Aislar capas |
| LAYOFF / LAYFRZ | — | Apagar / inutilizar capa |
| QSELECT | — | Selección rápida |

### Clase 6: Bloques, sombreados y referencias
| Comando | Alias | Función |
|---|---|---|
| BLOCK | B | Crear bloque |
| INSERT | I | Insertar (paleta Blocks) |
| WBLOCK | W | Bloque a archivo |
| BEDIT | BE | Editor de bloques |
| ATTDEF | ATT | Definir atributo |
| HATCH | H | Sombreado |
| XREF / ATTACH | XR | Referencias externas |
| PURGE | PU | Limpiar |

### Clase 7: Texto, cotas y anotación
| Comando | Alias | Función |
|---|---|---|
| MTEXT | MT / T | Texto de líneas múltiples |
| TEXT | DT | Texto de una línea |
| STYLE | ST | Estilo de texto |
| DIM | — | Acotación inteligente |
| DIMLINEAR / DIMALIGNED | DLI / DAL | Cotas lineal / alineada |
| DIMSTYLE | D | Estilo de cota |
| MLEADER | MLD | Directriz múltiple |
| TABLE | TB | Tablas |
| DIST / MEASUREGEOM | DI / MEA | Medir |
| AREA | AA | Áreas |

### Clase 8: Presentación e impresión
| Comando | Alias | Función |
|---|---|---|
| LAYOUT | LO | Presentaciones |
| MVIEW | MV | Ventanas gráficas |
| PAGESETUP | — | Configurar página |
| PLOT | Ctrl+P | Trazar / imprimir |
| EXPORTPDF | — | Exportar a PDF |
| ANNOSCALE (var.) | — | Escalas anotativas |

---

## 3. Curso intermedio/avanzado (puente a BIM y 3D)
| Área | Comandos clave (alias) |
|---|---|
| Bloques dinámicos y atributos | BEDIT (BE), BPARAMETER (PARAM), BACTION (AC), ATTEDIT (ATE), BATTMAN, ATTEXTRACT / DATAEXTRACTION (DX) |
| Estándares y plantillas | DWT, STANDARDS, LAYTRANS, CUI, acad.pgp (ALIASEDIT, de Express Tools) |
| Productividad | GROUP (G), DESIGNCENTER (ADC / Ctrl+2), TOOLPALETTES (TP / Ctrl+3), SHEETSET (SSM / Ctrl+4), FIELD, COUNT |
| Paramétrico (antesala del modelado paramétrico) | GEOMCONSTRAINT (GCON), DIMCONSTRAINT (DCON), PARAMETERS (PAR), AUTOCONSTRAIN |
| Referencias y colaboración | XREF, REFEDIT, DWGCOMPARE, TRACE, SHARE, IMAGEATTACH, PDFATTACH / PDFIMPORT |
| 3D: sólidos | BOX, CYLINDER (CYL), SPHERE, EXTRUDE (EXT), REVOLVE (REV), SWEEP, LOFT, PRESSPULL, UNION (UNI), SUBTRACT (SU), INTERSECT (IN), SLICE (SL), SOLIDEDIT, FILLETEDGE |
| 3D: navegación y vistas | UCS, VIEW (V), 3DORBIT (3DO), VISUALSTYLES (VSM), 3DMOVE, 3DROTATE, 3DALIGN, VIEWBASE (vistas 2D desde el 3D) |
| Render/visualización | RENDER (RR), MATERIALS (MAT), LIGHT |
| Automatización | ACTRECORD (grabador de acciones), SCRIPT (SCR), AutoLISP (APPLOAD / AP), Autodesk Assistant (2027) |

---

## 4. Próximos pasos sugeridos
1. Fase 2: tabla EN ↔ ES con alias locales (desde la ayuda ESP + tus manuales).
2. Descargar el PDF oficial de atajos y armar tu propia versión de "Guía rápida Estudio Pi" (A4 con los comandos de las 8 clases).
3. Cruzar el programa avanzado con los objetivos del ACP (dic. 2025) para ofrecer un curso "alineado a certificación".
4. Módulo final de IA: Autodesk Assistant (2027) + automatización con LISP/scripts.

Nota: los alias listados son los valores por defecto habituales del acad.pgp en inglés. Pueden variar según la versión o la personalización, así que conviene validarlos en la Command Reference oficial o con ALIASEDIT.
