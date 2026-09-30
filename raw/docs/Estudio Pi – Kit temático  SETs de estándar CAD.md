# Kit Estudio Pi temático: SETs de estándar CAD
Informe conceptual basado en el análisis de fuentes
Versión 1.0 · 27/09/2026 · Base: AutoCAD 2027

> Objetivo: definir qué debe contener cada SET temático del Kit Estudio Pi (SET-ARQ, SET-REP, SET-EST, etc.) y cómo diseñarlo para que se adapte a distintos estándares: el propio del estudio, el NCS de EE. UU., ISO 13567, AEC (UK) / ISO 19650 y las normas locales (IRAM, municipios, AEA, AySA, CIRSOC). Las notas [^n] llevan a la lista de fuentes del final.

---

## 1. Resumen
- Ningún estándar internacional está pensado para la práctica argentina, pero todos comparten la misma lógica. La capa se nombra con campos fijos, como disciplina + elemento + presentación + estado [^1] [^5] [^7], y las láminas se identifican con disciplina + tipo + número [^2] [^9].
- Propuesta: un núcleo común (SET-GEN) más SETs temáticos que se suman según el tipo de plano. Cada SET es un paquete de archivos (DWT, DWS, LAS, CTB, bloques, paleta y checklist) y no un solo archivo.
- Para servir a distintos estándares: el estudio trabaja con su nomenclatura en castellano y mantiene tablas de equivalencia (Layer Translator guardado en DWS) hacia NCS, ISO 13567 o AEC (UK). El Layer Translator permite guardar esos mapeos de capas en un DWS para reutilizarlos con cada cliente [^16] [^40].
- Advertencia para los cursos: el verificador de estándares (DWS) no está en AutoCAD LT [^16]. En LT, el control se hace con plantilla, estados de capa y el checklist, o con el agente IA.

---

## 2. Qué dicen los estándares analizados

### 2.1 Comparativa de nomenclatura de capas
| Estándar | Estructura | Ejemplo | Estado / fase | Fuente |
|---|---|---|---|---|
| NCS (EE. UU.): AIA CAD Layer Guidelines | Disciplina (1–2 caracteres) - Grupo mayor (4) - Grupo menor 1 (4) - Grupo menor 2 (4) - Estado (1). Obligatorios: disciplina y grupo mayor | `AI-WALL-FULL-DIMS-N` | Campo de estado (N = nuevo; E = existente; D = a demoler, según los ejemplos `X-CLNG-E` y `X-FLOR-D`) | [^1] [^3] |
| ISO 13567 (internacional) | Campos de largo fijo, sin separador: agente (2) + elemento (6) + presentación (2) obligatorios. Opcionales: estado, sector, fase, proyección, escala, paquete, usuario | Presentación: `E-` gráfico, `T-` texto, `H-` sombreado, `D-` cotas, `G-` grilla | N nuevo, E existente, R a remover, T temporario | [^5] [^6] |
| AEC (UK) sobre BS 1192 / Uniclass 2015 | Rol - Clasificación Uniclass - Presentación - Descripción - Vista (opcional). Máximo 64 caracteres; descripción en CamelCase y singular | Rol: `A` arquitectura, `E` eléctrica, `EL` iluminación, `G` topografía | Por descripción o por vista | [^7] [^8] |
| NCS: compatibilidad con ISO | Mantener el mismo formato y largo en todo el proyecto. `ANNO` no se permite si se busca conformidad con ISO 13567 | — | — | [^1] |

### 2.2 Designadores de disciplina (útiles para nombrar SETs y láminas)
Nivel 1 del NCS: G General, V Relevamiento/cartografía, B Geotecnia, C Civil, L Paisajismo, S Estructura, A Arquitectura, I Interiores, Q Equipamiento, F Incendio, P Sanitaria (plomería), D Procesos, M Mecánica (termomecánica), E Eléctrica, W Energía distribuida, T Telecomunicaciones, R Recursos, X Otras, Z Contratista / planos de taller [^1] [^2].
El nivel 2 agrega un modificador. En arquitectura: AD demolición, AE elementos, AF terminaciones, AG gráfica, AI interiores, AS sitio, y AJ/AK definibles por el usuario [^1].

### 2.3 Identificación de láminas y archivos
- NCS/UDS: `A-101` (nivel 1) o `AD-101` (nivel 2). Estructura: disciplina + tipo de lámina (1 dígito) + número secuencial (2 dígitos), con sufijo opcional del usuario [^2].
- ISO 19650: `Proyecto-Originador-Volumen-Nivel-Tipo-Rol-Número`, por ejemplo `PRJ-ORG-ZZ-00-DR-A-0001`. Estado (S0, S1, S2, A1) y revisión (P01, C01) se manejan aparte, como metadatos [^9].

### 2.4 Grosores de línea
- ISO 128-2: serie 0,13 · 0,18 · 0,25 · 0,35 · 0,5 · 0,7 · 1 · 1,4 · 2 mm (razón 1:√2). La relación entre línea extra gruesa, gruesa y fina es 4:2:1, y la separación mínima entre líneas paralelas es de 0,7 mm [^10].
- NCS: ocho grosores entre 0,18 y 2,00 mm. Las líneas visibles suelen ser de 0,35 mm y las ocultas de 0,25 mm [^3].
- En Argentina, IRAM 4502-23 ("Líneas de dibujo para construcciones"), IRAM 4504 (formatos y plegado), IRAM 4505 (escalas), IRAM 4508 (rótulo) e IRAM 4513 (cotas) forman parte del Manual de Normas IRAM de Dibujo Tecnológico [^11]. No tuve acceso al texto de esas normas: conviene validar la tabla de grosores del SET con tu manual.

### 2.5 Qué incluye un "estándar CAD" según Autodesk
Objetos con nombre (capas, estilos de texto, estilos de cota, tipos de línea), bloques de carátula y de detalle, criterios de anotación, criterios de layouts y conjuntos de planos, y la convención de propiedades (PorCapa, PorBloque o explícitas) [^15]. El DWS verifica capas, estilos de texto, tipos de línea, estilos de cota y de directriz múltiple. El Batch Standards Checker genera un informe sin modificar los dibujos y guarda su configuración en un archivo `.chx` [^16] [^17].

---

## 3. Principios de diseño del kit

1. **Núcleo + SETs.** SET-GEN lleva lo común (carátula, estilos, CTB y capas generales). Cada SET temático suma solo lo propio de su tema. Un plano municipal, por ejemplo, combina SET-GEN + SET-ARQ + SET-MUN.
2. **Una sola nomenclatura interna y varias salidas.** El estudio trabaja en castellano y exporta a NCS, ISO o AEC (UK) con LAYTRANS y un DWS de mapeo por estándar [^16] [^40].
3. **Campos fijos y separador `-`**, en el orden SET/disciplina - elemento - subelemento - estado. El estado se alinea con NCS e ISO: N nuevo o a construir, E existente, D a demoler [^1] [^5].
4. **Todo va PorCapa.** Color, tipo de línea y grosor se definen en la capa, y el CTB traduce color a grosor según la serie ISO [^10] [^21].
5. **Anotación anotativa**, con escalas por SET: 1:100 municipal [^29] y 1:50 para replanteo [^12].
6. **Estados de capa (.las)** para cambiar de vista rápido, por ejemplo "Municipal", "Replanteo" o "Estructura". Se importan desde el administrador de estados de capa [^17] [^19].
7. **Bloques inteligentes** (dinámicos y con atributos) para el cómputo con extracción de datos [^26] [^27] [^28].
8. **Distribución centralizada.** Las paletas de herramientas pueden apuntar a una carpeta de red. En AutoCAD 2027 también pueden venir de un proyecto en Forma Data Management ("Connected Support Files"), y las ubicaciones de confianza aceptan `\..` para incluir subcarpetas [^18] [^24] [^25].
9. **Checklist legible por humanos y por el agente IA.** Cada SET incluye un `checklist.md` que el agente usa para auditar planos. En 2027, además, el Autodesk Assistant puede verificar contra el DWS [^39].

---

## 4. Anatomía de un SET (plantilla común)

| Componente | Archivo | Contenido |
|---|---|---|
| Plantilla | `SET-XXX.dwt` | Unidades, capas, estilos, layouts, configuraciones de página, DWS asociado |
| Estándar | `SET-XXX.dws` | Capas, estilos de texto, cota y directriz, tipos de línea; mapeos de LAYTRANS [^16] |
| Estados de capa | `SET-XXX.las` | Vistas temáticas [^19] |
| Estilo de trazado | `EP-ISO.ctb` (común) | Color → grosor de la serie ISO 128 [^10] [^21] |
| Tipos de línea y sombreados | `EP.lin` / `EP.pat` | LM, eje medianero, proyección, existente, a demoler |
| Biblioteca de bloques | `SET-XXX_bloques.dwg` | Dinámicos y con atributos |
| Paleta de herramientas | `SET-XXX.xtp` | Bloques, sombreados, cotas y comandos [^18] |
| Conjunto de planos | `SET-XXX.dst` | Láminas, numeración y carátula con campos [^20] |
| Extracción de datos | `SET-XXX.dxe` | Configuración de cómputo reutilizable [^27] |
| Checklist | `SET-XXX_checklist.md` | Controles mínimos (para humanos y para el agente IA) |
| Guía | `SET-XXX_guia.md` | Norma base, escalas, ejemplos, videos |

---

## 5. SET-GEN: núcleo común
- **Capas:** `G-CART` (carátula), `G-MARC` (marco), `G-TEXT`, `G-COTA`, `G-REFE` (referencias de corte y detalle), `G-VPRT` (ventanas, no imprimible), `G-AUXI` (construcción, no imprimible). Equivalen a los grupos de presentación de ISO 13567 (B, V, D, J, U) [^5] y al ejemplo `G-ANNO-TTLB` del NCS [^3].
- **Estilos:** texto EP-2,5 y EP-3,5 anotativos; cotas EP-ARQ; directriz EP; tabla EP.
- **Láminas:** formatos y plegado según IRAM 4504 y rótulo según IRAM 4508 [^11]. Identificación `A-101` al estilo UDS [^2].
- **Archivos:** `EP-OBRA-ORIG-ZONA-NIVEL-TIPO-DISC-NNNN`, adaptación de ISO 19650 [^9].

---

## 6. SETs temáticos

### SET-LEV: Relevamiento y topografía (disciplina V)
- **Propósito:** estado actual del terreno y de lo construido; base para el resto de los SETs.
- **Capas:** `V-TERR` (límites y medidas del terreno), `V-EDIF-E` (construcciones existentes), `V-ARBO` (árboles), `V-NIVE` (niveles y puntos), `V-SERV` (servicios existentes), `V-VECI` (linderos).
- **Bloques:** punto de nivel con atributos (número, cota) y árbol con diámetro.
- **Salidas:** plano de relevamiento, que sirve de base para SET-MUN (existente y a demoler).
- **Estado:** conceptual. Falta una fuente local de contenidos mínimos. Se toma el designador V del NCS [^1].

### SET-REP: Replanteo
- **Base:** apuntes de cátedra de la UNaM y de la UNLP [^12] [^13].
- **Contenido mínimo:**
  - Medidas perimetrales y ángulos de la parcela.
  - Distancia sobre la LM a la ochava más cercana y al eje de calle.
  - Al menos dos ejes de replanteo, más auxiliares si hace falta. No deben coincidir con la LM ni con los ejes divisorios, ni cruzar huecos de escalera o dobles alturas.
  - Fundaciones (bases, troncos, columnas, pilotes) acotadas desde sus ejes hasta los ejes de replanteo.
  - Cotas parciales y acumuladas, espesores de muros y columnas por sus lados exteriores, niveles en plantas altas [^13].
  - En muros curvos: radio, centro y coordenadas de inicio y fin [^12].
- **Escala convencional:** 1:50. Tolerancias: 10 mm con replanteo manual y 5 mm con instrumental [^12].
- **Capas:** `R-EJES` (ejes de replanteo), `R-EJAX` (auxiliares), `R-COTP` (parciales), `R-COTA` (acumuladas), `R-PTOS` (puntos con coordenadas), `R-NIVE`, `R-FUND` (fundación, en referencia a SET-EST).
- **Bloques:** marca de eje (letra o número), punto de replanteo con atributos (ID, X, Y, Z) y cota de nivel.
- **Cómputo:** cuadro de coordenadas generado automáticamente a partir de los bloques con extracción de datos, que se actualiza si se mueven [^36] [^27].
- **Nota de nomenclatura:** R en el NCS es "Resource" [^1]. Si hay que exportar al NCS, conviene mapear SET-REP a un designador definible por el usuario (AJ/AK) [^1].

### SET-ARQ: Arquitectura
- **Capas por elemento y estado:** `A-MURO-N/E/D`, `A-TABI`, `A-ABER` (aberturas), `A-SOLA` (solados), `A-CIEL`, `A-ESCA`, `A-EQUI` (equipamiento), `A-LOCA` (rótulos de locales), `A-SOMB` (sombreados). Estado N/E/D alineado con NCS e ISO [^1] [^5]. Equivalencia NCS de referencia: WALL, DOOR, FLOR, CLNG, EQPM [^3].
- **Bloques:** puertas y ventanas dinámicas (estirables, con estados de visibilidad y Flip) con atributos de código, ancho y tipo [^26]; rótulo de local con campo de área; escalera paramétrica.
- **Cómputo:** planilla de aberturas y de locales con superficies [^27] [^28].
- **Láminas:** A-1xx plantas, A-2xx vistas, A-3xx cortes, A-5xx detalles. El UDS define un dígito de tipo de lámina [^2].

### SET-MUN: Presentación municipal (se combina con SET-ARQ)
- **Base:** guía del CAPBA 1 (1:100, cortes, vistas, LM, ochavas, ejes medianeros, balance de superficies, carátula) [^29]. En CABA, el template, la carátula y los protocolos CAD del GCBA [^30].
- **Capas:** `M-SILU` (siluetas), `M-BALA` (balance), `M-LMUN`, `M-EMED`, `M-FOSF` (FOS/FOT), `M-DEMO` y `M-CONS` si el municipio pide colores por estado.
- **Bloques:** carátula por jurisdicción (atributos y campos), tabla de balance, croquis de ubicación.
- **Checklist:** el del municipio piloto, a definir con tu socia.

### SET-EST: Estructuras (disciplina S)
- **Base:** INPRES-CIRSOC 103, art. 1.3.4.1.b [^14].
  - Planos de encofrado: plantas, cortes y detalles de todos los elementos, con dimensiones, niveles y etapas de hormigonado si las hay.
  - Planos de detalle de hormigón armado: secciones, ubicación y separación de armaduras, recubrimientos, empalmes, anclajes, ganchos, estribos (en sección y en vista longitudinal) y despiece.
  - Estructuras metálicas: secciones, uniones (tipo, designación y dimensiones), medios de unión, ejecución en taller o en obra, electrodos, bulones y piezas auxiliares.
  - Escalas adecuadas para la obra [^14].
  - Representación de estructuras metálicas según IRAM 4518, y soldaduras según IRAM ISO 2553 [^11].
- **Capas:** `S-EJES` (compartida con R-EJES por xref), `S-FUND`, `S-COLU`, `S-VIGA`, `S-LOSA`, `S-TABI` (tabiques de HºAº), `S-ARMA` (armaduras), `S-ESTR` (estribos), `S-META`, `S-UNIO`, `S-NIVE`, `S-DESI` (designación V101, C1, L1).
- **Bloques:** marca de columna, viga y losa con atributos (código, sección, hormigón); barra con atributos (posición, diámetro, largo, cantidad) para la planilla de armaduras; marca de soldadura.
- **Cómputo:** planilla de armaduras y de hormigón por elemento con extracción de datos [^27].
- **Alcance del curso:** representación y documentación, sin cálculo. El cálculo lo firma el ingeniero.

### SET-ELE: Instalación eléctrica (disciplina E)
- **Base:** AEA 90364-7-771, con su anexo de símbolos usuales [^31].
- **Capas:** `E-ILUM`, `E-TOMA`, `E-COMA` (comandos), `E-TABL`, `E-CANA` (cañerías), `E-CIRC` (circuitos), `E-TEXT`.
- **Bloques:** boca, toma, llave, tablero y caja, con atributos de circuito, tipo, potencia y altura.
- **Cómputo:** bocas por circuito y por tablero [^27].

### SET-SAN: Instalación sanitaria (disciplina P)
- **Base:** requisitos de AySA para planos sanitarios en CABA [^32].
- **Capas:** `P-AFRI` (agua fría), `P-ACAL` (agua caliente), `P-CLOA`, `P-PLUV`, `P-ARTE` (artefactos), `P-CAMA` (cámaras y bocas de acceso), `P-TANQ`.
- **Bloques:** artefactos, PPA, BA, CI, llaves y tanque, con código para el cómputo.
- **Pendiente:** simbología local, a partir de tus manuales o del material de tu socia.

### SET-FAB: Fabricación (CNC e impresión 3D)
- **Capas por operación:** `F-CORT` (corte pasante), `F-GRAB` (grabado), `F-PLEG` (plegado), `F-MARC`. Una capa por operación y polilíneas cerradas.
- **Salida:** DXF 2D para CNC y STL para impresión. El formato exacto se acuerda con cada proveedor.

### Futuros (fuera de alcance por ahora)
SET-INC (incendio, F), SET-TER (termomecánica, M), SET-GAS, SET-INT (interiorismo, I), SET-PAI (paisajismo, L). Los designadores ya existen en el NCS [^1].

---

## 7. Matriz: qué SET usa cada tipo de plano
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

---

## 8. Equivalencias de nomenclatura (ejemplos)
| Estudio Pi | NCS (formato) | ISO 13567 (lógica) | AEC (UK) (lógica) |
|---|---|---|---|
| `A-MURO-N` | `A-WALL-N` [^1] | Agente A + elemento + presentación E + estado N [^5] | A + código Uniclass de muro + presentación + `Wall` [^7] |
| `A-MURO-D` | `AD-WALL` [^3] | Estado R (a remover) [^5] | Descripción con estado |
| `G-CART` | `G-ANNO-TTLB` [^3] | Presentación B / V (espacio papel) [^5] | Z (general) [^7] |
| `R-EJES` | Designador del usuario (AJ/AK) [^1] | Presentación G (grilla) [^5] | — |

Los códigos exactos de los grupos mayores del NCS y los de Uniclass hay que tomarlos del documento completo de cada estándar antes de armar los DWS de mapeo [^1] [^8].

---

## 9. Flujo de verificación
1. El dibujo nace de `SET-XXX.dwt`, que ya tiene el DWS asociado [^16].
2. Durante el trabajo, las notificaciones de CHECKSTANDARDS avisan las violaciones [^16] [^22].
3. Antes de entregar, se corre el Batch Standards Checker sobre todo el juego (informe `.chx`) [^16].
4. Para un cliente con otro estándar, se usa LAYTRANS con el DWS de mapeo [^40].
5. El agente IA recorre `SET-XXX_checklist.md`. En AutoCAD 2027, el Assistant verifica contra el estándar (función en tech preview) [^39].

---

## 10. Videos de referencia
| Video | Canal | Qué aporta |
|---|---|---|
| Plantilla (Template) AutoCAD: arquitectura [^33] | arqMANES | DWT paso a paso en español: capas, filtros, bloques, estilos, escalas anotativas, layouts |
| AutoCAD: Templates & Layer Standards [^34] | ModelPro Academy | Convenciones AIA/NCS e ISO, color y grosor para trazado |
| 7 Ways to Automate Your AutoCAD Template [^35] | CAD Intentions | DesignCenter, plantillas por disciplina, carátulas con atributos y campos |
| Webinar: AutoCAD CAD Standards [^16] | Civil Survey Solutions | DWS, LAYTRANS, verificación por lotes |
| Cuadro de replanteo o coordenadas desde bloques [^36] | Javi Lapina | Extracción de datos para el cuadro de coordenadas |
| Replanteo [^37] | Cursos Fernando Montaño | Pasar a obra curvas y puntos, cotas de replanteo |
| Managing Your CAD Standards (blog) [^38] | Autodesk | Configuración del verificador de estándares |

---

## 11. Próximos pasos
1. Validar con tu manual IRAM la tabla de grosores y tipos de línea (IRAM 4502-23) antes de cerrar el CTB [^11].
2. Elegir el municipio piloto para SET-MUN.
3. Construir primero SET-GEN + SET-ARQ + SET-REP, que se usan en el curso 2D Avanzado, aprovechando la prueba de AutoCAD 2027.
4. Definir las políticas de LT: los alumnos con LT no tienen DWS [^16], así que su control se hace con el checklist y el agente IA.

---

## Fuentes

[^1]: NCS v6, AIA CAD Layer Guidelines: Layer Name Format. https://www.nationalcadstandard.org/ncs6/pdfs/ncs6_clg_lnf.pdf
[^2]: NCS v6, Uniform Drawing System, Module 1: Sheet Identification. https://www.nationalcadstandard.org/ncs6/pdfs/ncs6_uds1.pdf
[^3]: NCS v6, Frequently Asked Questions. https://www.nationalcadstandard.org/ncs6/faqs.php
[^5]: Wikipedia, ISO 13567. https://en.wikipedia.org/wiki/ISO_13567
[^6]: iTeh Standards, ISO 13567-2:2017. https://standards.iteh.ai/catalog/standards/iso/392fa47f-9e0d-461c-a83f-97654fcb878d/iso-13567-2-2017
[^7]: AEC (UK), Protocol for Layer Naming v4.1. https://aecuk.wordpress.com/wp-content/uploads/2018/06/aecukprotocolforlayernaming-v4-1.pdf
[^8]: NBS, Uniclass 2015: Download. https://uniclass.thenbs.com/download
[^9]: BI3M, ISO 19650: Naming and Information Structure. https://www.bi3m.com/knowledge/bim-and-digital-engineering-insights/iso-19650/naming-and-information-structure
[^10]: iTeh Standards, ISO 128-2:2020: Basic conventions for lines. https://standards.iteh.ai/catalog/standards/iso/a0c6a7e3-b7fa-4ea2-8d4b-6858cf97df24/iso-128-2-2020
[^11]: UCP Biblioteca, Manual de Normas IRAM de Dibujo Tecnológico (2017), índice de normas. https://koha.ucp.edu.ar/cgi-bin/koha/opac-ISBDdetail.pl?biblionumber=48049
[^12]: UNaM FIO, Construcción de Edificios: Replanteo. https://aulavirtual.fio.unam.edu.ar/pluginfile.php/323422/mod_resource/content/1/REPLANTEO.pdf
[^13]: UNLP FAU, Producción de Obras I: TP 7 Plano de Replanteo y de Obra (2023). https://blogs.ead.unlp.edu.ar/produccion/files/2016/09/TP-7-Replanteo-2023.pdf
[^14]: INPRES, CIRSOC 103 Parte I: Adenda (art. 1.3.4.1.b). http://contenidos.inpres.gob.ar/docs/Reglamentos/INPRES-CIRSOC-103_Parte_I-ADENDA.pdf
[^15]: Autodesk, About Creating and Managing CAD Standards. https://help.autodesk.com/view/OARX/2026/ENU/?guid=GUID-9985B23D-C42D-431D-B766-D1E5FE3ECC07
[^16]: Civil Survey Solutions (YouTube), Webinar: AutoCAD CAD Standards. https://www.youtube.com/watch?v=HJbDNOC8GBQ
[^17]: Autodesk University, Handout CES463392 (CAD Standards Manager). https://static.au-uw2-prd.autodesk.com/Class_Handout_CES463392_Samuel_Lucido.pdf
[^18]: Autodesk, About Creating Tool Palettes (AutoCAD 2027). https://help.autodesk.com/cloudhelp/2027/ENU/AutoCAD-Core/files/GUID-6B20D7DF-447A-4A8D-8FF1-8339CF54FFBD.htm
[^19]: Autodesk, Layer States Manager (AutoCAD 2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/ACDLT/2014/ENU/files/GUID-3E0F662B-226F-4A27-B5BB-D15252CC994C-htm.html
[^20]: Autodesk, About Sheet Sets (AutoCAD 2026). https://help.autodesk.com/view/ACD/2026/ENU/?caas=caas/documentation/ACDLT/2014/ENU/files/GUID-34D889BC-19AD-4CD1-ADB1-F359D9B515FB-htm.html
[^21]: Autodesk, About Plot Style Tables (AutoCAD 2026). https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-2FD01085-DDD8-49D2-A910-E63EA45A7FED.htm
[^22]: Autodesk, CAD Standards Settings Dialog Box (AutoCAD 2027). https://help.autodesk.com/cloudhelp/2027/ENU/AutoCAD-Core/files/GUID-E03CA0C6-C1EF-4C83-A0C7-B1EC9C484CD2.htm
[^24]: Autodesk, To Set Up an Autodesk Project to Use Connected Support Files (2027). https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-2EDD58B6-ACB8-40EE-93B7-6333B345857E
[^25]: Autodesk, What's New or Changed in AutoCAD 2027. https://help.autodesk.com/view/ACD/2027/ENU/?contextId=WHATS_NEW_2027_ACD
[^26]: Autodesk, Create a Stretchable Dynamic Block (2026). https://help.autodesk.com/view/ACD/2026/ENU/?guid=GUID-4005A6BB-388A-4EC7-BF17-555F1E6C137C
[^27]: Autodesk, About Data Extraction. https://help.autodesk.com/view/ACD/2025/ENU/?guid=GUID-B0D32260-45E3-4643-B574-7F6C31579B68
[^28]: Autodesk, About Extracting Data from Block Attributes. https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Core/files/GUID-BA68DD22-A3CD-4538-90A9-6101C33BC963.htm
[^29]: CAPBA Distrito 1, Guía base para dibujo de plano municipal. https://capbauno.org/wp-content/uploads/2023/04/GUIA-ELEMENTOS.pdf
[^30]: GCBA, Armado de Planos. https://buenosaires.gob.ar/gcaba_historico/armado-de-planos
[^31]: AEA, Reglamentación AEA 90364-7-771. https://aea.org.ar/wp-content/uploads/2017/10/90364-7-771-2.pdf
[^32]: AySA, Requisitos para solicitar planos sanitarios. https://aysa.com.ar/media-library/usuarios/tramites_online/Requisitos-planos-sanitarios_2024_V2.pdf
[^33]: arqMANES (YouTube), Plantilla (Template) AutoCAD: arquitectura. https://www.youtube.com/watch?v=iRpwMM1Ik1g
[^34]: ModelPro Academy (YouTube), AutoCAD: Templates & Layer Standards. https://www.youtube.com/watch?v=MAYwYopn3HI
[^35]: CAD Intentions (YouTube), 7 Ways to Automate Your AutoCAD Template. https://www.youtube.com/watch?v=fg-Z27l8bJ4
[^36]: Javi Lapina (YouTube), Cuadro replanteo o coordenadas desde bloques en AutoCAD. https://www.youtube.com/watch?v=mDH4DV50x74
[^37]: Cursos Fernando Montaño (YouTube), Replanteo. https://www.youtube.com/watch?v=D4m8JQ8BPXc
[^38]: Autodesk Blog, Managing Your CAD Standards: Tuesday Tips With Frank. https://www.autodesk.com/blogs/autocad/cad-standards-tuesday-tips-with-frank/
[^39]: Autodesk, AutoCAD 2027: Autodesk Assistant. https://help.autodesk.com/view/ACD/2027/ENU/?guid=GUID-99E2D8F7-D4D9-4B3A-9E57-7B73D6BB12AD
[^40]: Wiley (extracto de libro), Establishing the Foundation for Drawing Standards (Layer Translator y DWS). https://catalogimages.wiley.com/images/db/pdf/9781118798881.excerpt.pdf
