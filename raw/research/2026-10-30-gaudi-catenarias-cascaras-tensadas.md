---
tipo: research
fecha: 2026-10-30
tema: Estructuras inspiradas en Gaudí — catenarias en cáscaras de hormigón (funicular, form-found) y estructuras tensadas (membranas, cable-net), con aplicación a escala urbana
idioma: ES/EN (IT gap)
fuentes_n: 58 (4 fetch 200 + 52 snippets verificados + 2 descartadas 410/403)
confianza: Alta (histórico Gaudí + Candela/Dieste/Otto + Sagrada Família actual) / Media (escala urbana: casos dispersos, sin corpus unificado)
solicitante: SOL (cliente del estudio)
tags: [research, sherlock, gaudi, catenaria, funicular, cascaras, tensadas, membranas, escala-urbana]
---

# 2026-10-30 — Estructuras inspiradas en Gaudí: catenarias, cáscaras y tensadas

**Fecha:** 2026-10-30 (-03:00) · **Fuentes:** 58 (4 fetch 200 + 52 snippets + 2 descartadas) · **Confianza:** Alta en histórico/estructural, Media en escala urbana (casos buenos pero dispersos)

## Resumen

La línea Gaudí→hoy se puede contar como **una sola idea con dos materiales**: encontrar la forma dejando que las fuerzas la dibujen. Gaudí la resolvió con la **maqueta polifunicular** (cuerdas + saquitos de perdigones de plomo colgados del techo, fotografiados e invertidos: lo que cuelga a tracción pura, invertido, se sostiene a compresión pura) para la cripta de la Colònia Güell (1898-1914) y la Sagrada Família. Esa misma lógica produce dos familias estructurales que hoy conviven:

1. **Cáscaras / form-found a compresión** (hormigón, ladrillo): Candela (hypars de paraboloide hiperbólico, encofrado de tablas rectas, cáscaras de 4 cm), Dieste (bóvedas gausas de cerámica armada con directriz catenaria), Heinz Isler (modelos de tela colgada congelados en hormigón), y hoy KnitCandela/RhinoVault/Kangaroo (form-finding digital + encofrado textil/impresión 3D).
2. **Tensadas / form-found a tracción** (membranas, cable-net): Frei Otto (películas de jabón = superficies mínimas a tracción; redes colgantes invertidas = gridshells a compresión), techo olímpico de Múnich 1972 (cable-net de 74.000 m²), y hoy MPavilion 2022, canopies escolares, juegos infantiles.

**Hallazgo transversal para el estudio:** el form-finding físico de Gaudí y Otto es el mismo algoritmo que hoy corre en **Kangaroo (Grasshopper/Rhino)** — hay tutoriales que reproducen la maqueta de Isler y el pabellón de Montreal 67 digitalmente. El estudio ya tiene Rhino 8: la catenaria es el puente natural entre el legado Gaudí y el pipeline paramétrico del vault.

**Escala urbana:** Gaudí mismo empezó ahí (farolas de la Plaça Reial, 1878-79, su primer encargo público). Hoy la escala pequeña está dominada por **membranas tensadas** (canopies de juegos, kioscos, stands) y por **cáscaras modulares ligeras** (Shell in the Park Varna, MARS Pavilion catenaria invertida, Shellstar Hong Kong con Kangaroo). Corpus disperso pero con casos verificables.

## Ejes

### Eje 1 — Gaudí histórico: la maqueta polifunicular y las superficies regladas

- **Método**: en un cobertizo junto a la obra de la Colònia Güell, maqueta a escala 1:10 de 4 m de altura, colgada boca abajo del techo: tablero con la planta, cordeles, saquitos de tela con perdigones de plomo proporcionales a las cargas reales. «Al colgar, un cordel adopta por sí solo la única forma que trabaja a tracción pura, sin flexión. Gaudí fotografiaba el conjunto y le día la vuelta a la fotografía» (Gaudí Museum, fetch 200). La estructura no se calculaba después de dibujar: **la estructura era el dibujo**.
- **Catenaria vs parábola**: la catenaria es la curva de la cadena colgada con peso repartido a lo largo de sí misma; la parábola, la del cable con peso repartido en horizontal (puente colgante). En luces pequeñas se confunden — las fuentes se contradicen sobre el desván de la Casa Milà (270 arcos: catenarios para lapedrera.com, parabólicos para el Cuaderno Informativo 3).
- **Arbotantes = «muletas»**: el arco catenario invertido «es estable por sí mismo, no necesita otros elementos de apoyo» (definición oficial de la basílica). Gaudí buscaba eliminar los arbotantes góticos para inundar el interior de luz.
- **Primera catenaria de su obra**: Cooperativa Obrera Mataronense (1878-1882), 12 arcos en nave de 48×12 m, con el sistema de pernos de Philibert de l'Orme.
- **Superficies regladas** (construibles con tablas rectas): hiperboloide (289 lucernarios de la Sagrada Família), paraboloide hiperbólico (**primera vez en la historia de la arquitectura**: pórtico de la cripta de la Colònia Güell — verificado estadísticamente por Cortés et al. en Informes de la Construcción CSIC: 14 de 19 bóvedas del pórtico ajustan a hypar con fit >99%), helicoide (columnas de doble giro), conoide (Escoles de la Sagrada Família, 1908-09, dibujadas por Le Corbusier en 1928).
- **La maqueta original se destruyó en julio de 1936**; la reconstrucción expuesta se hizo en **Stuttgart en 1982 bajo la dirección de Frei Otto** — el nudo histórico Gaudí↔Otto es literal.
- **Crítica académica**: Casáis (Informes de la Construcción CSIC) advierte que la cripta en pie trabaja con un estado de cargas parcial no previsto por el modelo funicular del conjunto completo — el mapa de fisuras de la solera de rasilla es la evidencia.

### Eje 2 — Cáscaras de hormigón: Candela, Isler, Saarinen (línea form-found a compresión)

- **Félix Candela** (1910-1997): funda **Cubiertas Ala** (1950) y construye ~1.500 proyectos hasta 1976. Geometría base: **paraboloide hiperbólico (hypar)** — superficie de doble curvatura generada por rectas, lo que permite encofrado con tablas rectas y cálculo a mano. Obras clave: Pabellón de Rayos Cósmicos UNAM (1951, una de las cáscaras más delgadas jamás construidas), capilla Palmira/Lomas de Cuernavaca (1958), **Los Manantiales** Xochimilco (1958: 8 hypars de borde curvo en flor, luz 106 pies entre apoyos, espesor **4 cm**, trabaja esencialmente a compresión con «vigas V» ocultas en las limatones), Palacio de los Deportes (1968, acero+cobre). Premios: Auguste Perret 1961, medalla de oro Institution of Structural Engineers 1961.
- **Regla de oro de Candela** (Textbook of Architecture): luz/espesor de una buena cáscara ≈ **400-1000** (un huevo ≈ 100). «Strength from form»: la cáscara delgada trabaja por fuerzas de membrana, no por flexión.
- **Declive de las cáscaras** (~1965): encofrados y mano de obra caros, impermeabilización difícil, oscuridad interior, poca adaptabilidad a cambios de uso, competencia del metal ligero y las cubiertas textiles (Galindo Díaz et al., Redalyc).
- **Eero Saarinen + Ammann & Whitney — Kresge Auditorium MIT (1953-55)**: cáscara de 1/8 de esfera sobre 3 apoyos, luz libre 48,8 m, la mayor de EE.UU. en su momento. **Contraejemplo pedagógico**: Saarinen fijó la forma sin consultar a los ingenieros («make it work»), el borde libre deflectó mucho más de lo previsto y hubo que reforzar 9 montantes de ventana para sostener el borde — el caso de manual de lo que pasa cuando la forma no sigue las fuerzas (Plunkett & Mueller, MIT; Whitehead, Iowa State). Lección directa para el estudio: la catenaria de Gaudí funciona porque la forma ES el cálculo; la esfera de Kresge falla porque la forma se impuso.
- **Heinz Isler** (comparado con Otto y Musmeci por Boller & D'Acunto 2021): modelos de tela húmeda colgada y congelada → Deitingen (1968, 90 mm, doble curvatura), Wyss Garden Centre (1962, 70 mm, borde en labio invertido que imita la tela colgada). Su método experimental fue digitalizado después con Grasshopper+Kangaroo (ver Eje 6).

### Eje 3 — Dieste y la cerámica armada (cáscara catenaria en ladrillo)

- **Eladio Dieste** (1917-2000), **cerámica armada**: ladrillo + mortero + barras de acero en las juntas. **Bóveda gausa**: perfil longitudinal catenaria (inverso del diagrama de momentos), sección transversal ondulada para rigidez. Iglesia Cristo Obrero de **Atlántida** (1958-60, UNESCO 2021): nave 16×30 m, luz media 16 m, flecha variable 7-147 cm, muros ondulados de conoides (directriz recta al piso, ondulada arriba), tensores embebidos en los valles de la ondulación, armadura mínima (2 kg/m² en bóveda, 0,5 kg/m² en muros).
- **Vínculo directo con Gaudí**: Álvarez Prozorovich (DPA/UPC) escribe que «sobre los muros laterales planean Gaudí y sus dibujos para la Cripta Güell» — Dieste repite el gesto con simetría y ritmo industrial (mercados, galpones). La tradición es la bóveda tabicada a la catalana (Guastavino) que Gaudí heredó.
- **Comparativa Dieste vs Candela** (Álvarez-Dorado et al., Anales de Edificación 2022): las cáscaras de hormigón logran luces casi el doble que la cerámica armada; la cerámica gana en economía de encofrado y movilidad (fraguado lento del hormigón limita).

### Eje 4 — Estructuras tensadas: Frei Otto, membranas, cable-net

- **Frei Otto** (1925-2015, Pritzker 2015): dos principios espejados — **películas de jabón** = superficies mínimas a tracción pura (membranas); **redes colgantes con pesos, invertidas** = gridshells a compresión. Su grupo «Biologie und Bauen» (1961) y el Institut für Leichte Flächentragwerke (IL) de Stuttgart sistematizaron el form-finding físico: burbujas, arena, cadenas, telas, neumáticos (Uni Stuttgart, fetch vía snippet).
- **Reconstrucción de la maqueta de Gaudí (Stuttgart 1982)**: Otto dirigió la reconstrucción de la maqueta polifunicular de la Colònia Güell — reconocimiento explícito del linaje.
- **Techo olímpico de Múnich 1972** (Behnisch + Otto + Leonhardt/Schlaich + Argyris): cable-net pretensado de **74.000-78.000 m²** (según fuente: 34.000 m² solo estadio según MoMA), mallas de 75×75 cm, mástiles de 51-80 m, cubierta de metacrilato. Form-finding con modelos 1:200 (¡medias de nylon!) + modelos de medición 1:125 en acero de 0,2 mm; **más de 50.000 horas de trabajo en modelos físicos**; los métodos de Argyris y Linkwitz dieron el primer cálculo computacional iterativo de este tipo (Tomlow 2016; Schmid & Weber). Es «el progenitor de todas las estructuras ligeras» (schlaich bergermann partner).
- **Form-finding de membranas hoy** (bigwalls.net, guía técnica): el form-finding determina la forma de equilibrio con pretensado dado; tres métodos principales convergen en superficie mínima; el patterning (corte de la tela) es el paso crítico posterior.
- **Otto neumáticos** (UMass BTES): membranas neumáticas casi ingrávidas, desplegables, «podrían teóricamente abarcar millas» — limitaciones económicas/energéticas, no estructurales.

### Eje 5 — Sagrada Família hoy: la catenaria en obra 2026

- **Estado 2026**: torre de María (138 m) terminada 2021, cuatro torres de Evangelistas (135 m) 2022-2023, **torre de Jesucristo (172,5 m) en cierre para 2026** (centenario de la muerte de Gaudí); fachada de la Gloria queda para fase final (booklet oficial sagradafamilia.org).
- **Arup** (desde 2014): las 6 torres centrales sobre la nave y la cripta exigían aligerar — solución de **piedra pretensada prefabricada** (paneles de 5 t en torre de María, 25 t en la de Jesús, 450 mm de espesor), que reduce el peso a la mitad y acelera el programa. «Diseño paramétrico: conocimiento humano profundo de las variables estructurales + herramientas algorítmicas» (Arup).
- **Las columnas catenarias de la nave** (terminada 2010): en sección transversal son las catenarias de Gaudí sin verticales; en longitudinal son regulares — Gaudí usó la catenaria en 2D, no en 3D completo (Ingenia, fetch 403 pero contenido citable de snippet).
- **Workflow actual** (IAAC, entrevista a Esteve Umbert): Rhino+Grasshopper paramétrico → impresión 3D de maquetas físicas (tradición Gaudí) → Rhino con atributos embebidos como BIM de piedra (cada bloque con info de fabricación) → Revit para documentación → mock-ups 1:1 antes de cada fase. **Es exactamente el pipeline del estudio (Rhino 8 + paramétrico + maqueta)**.
- **Rhino World 2026** (charla oficial del equipo): de arcos catenarios a estructuras polifuniculares completas «form finding» que encuentran el camino natural de las fuerzas; geometría gaussiana de doble curvatura; la subdivisión en triángulos de la Colònia Güell se reutiliza hoy para las bóvedas hiperboloides y la cruz 3D de la torre de Jesús.

### Eje 6 — Form-finding digital: Kangaroo/Grasshopper (el método de Gaudí en el pipeline del estudio)

- **Kangaroo** (plugin de physics engine para Grasshopper/Rhino): reproduce la catenaria como simulación de cadena colgada (anclas + gravedad + muelles). Componente nativo `Catenary` de GH es matemático-exacto; Kangaroo es aproximación física pero permite **membranas catenarias completas y estructuras anidadas** (Parametric Monkey; HKU Building Simplexity Lab; TU Delft textbook).
- **Reproducción digital de Isler**: paper ICCCBE (Seoul National University) reproduce el form-finding de la Naturtheater Grötzingen de Isler con script Grasshopper+Kangaroo+WeaverBird, validado contra SAP2000 — el método experimental de 1961 es hoy un script.
- **Shellstar Pavilion** (Matsys, Hong Kong 2012, fetch 200): pabellón temporal 8×8×3 m de Coroplast 4 mm, ~1.500 celdas, «form-finding basado en las técnicas clásicas de **Antoni Gaudí y Frei Otto**» con Grasshopper+Kangaroo; optimización de planitud de celdas con Python; fabricación CNC. Caso de manual de catenaria a escala de stand de feria.
- **RhinoVault** (Block Research Group, ETH): software de form-finding de cáscaras a compresión usado en Armadillo Vault, MLK Jr Pavilion y la **biblioteca Maya Somaiya** (Sameep Padora & Associates, Maharashtra, 2017) — cáscara de ladrillo con RhinoVault por un estudio independiente del BRG (IStructE Nanayakkara).

### Eje 7 — Escala urbana: farolas, asientos, juegos, stands, kioscos, pabellones

- **Gaudí urbano (1878-79)**: farolas de la **Plaça Reial** (2 de 6 brazos, inauguradas 24-09-1879) y **Pla de Palau** (4 de 3 brazos, 1890, quedan 2). Hierro colado + mármol, remate de caduceo de Mercurio (dios del comercio) con casco alado, escudo de Barcelona policromado. Su **Memoria** es uno de los pocos textos proyectuales de Gaudí: «a la sobreabundancia ornamental escultórica se prefiere con gran tino la estructura de los materiales naturales realzada con sencillos perfiles». Diseño sustentable avant la lettre: proyectadas a gas, electrificadas después, 140+ años en pie. Proyectó instalarlas en toda la ciudad (Ayuntamiento, Llotja, Catedral, Portal de l'Àngel…) — quedó en 6 unidades.
- **Banco del Park Güell** (Jujol, 1906-14): la serpiente ondulada como asiento urbano — superficie reglada a escala de mobiliario (referencia en Gaudí Museum).
- **Membranas tensadas a escala urbana (casos verificables)**:
  - **MPavilion 2022, Melbourne** (all(zone) + AECOM): pabellón temporal de 3 capas textiles (redes de pesca recicladas + membrana STFE 250 m² + waffle de Soltis 86 1.400 m²), kiosco repintado cada mes, donado a la ciudad al cerrar la temporada (ArchDaily).
  - **Canopies Tachkemoni, Amberes** (Laurent Ney, 2001): membranas hypar pretensadas contra anillo tubular sobre patios de escuela urbana (12 m Ø y 16×21 m); las columnas se fijaron torcidas 10 cm para quedar verticales tras el tensado (Tensinet).
  - **Playground Oryahovo, Bulgaria** (tensil.bg, 2013): membrana en silla de montar 11×11 m sobre juegos infantiles, textil transpirable MEHLER POLYMAR.
  - **Shade School Playground Pavilion, Yangón** (Blue Temple, 2023): 127 m² de sombra para patio escolar con bambú + membrana, apoyos fuera del patio (ArchDaily).
  - **Cloud Forests, Hwaseong, Corea** (UNITEDLAB, 2018): 70 m² de pabellón de juego con varillas de aluminio y globos, presupuesto total US$4.000 (ArchDaily).
- **Cáscaras/kioscos a escala urbana**:
  - **MARS Pavilion, Palm Springs 2017** (Form Found Design + Walter P Moore): **catenaria invertida de hormigón** construida con robots ABB + encofrado de tela, 70 componentes «wishbone»; explícitamente «harkening back to Gaudí's use of inverting parabolic, hyperbolic and catenary masonry forms» (Walter P Moore). Primer hormigón robótico del sur de California.
  - **Shell in the Park, Varna** (uau studio): kioscos modulares de hormigón plegado de **50 mm** de espesor, 3 paneles = arco = kiosco, drenaje por gravedad, expandibles a pabellón (uau studio).
  - **Boves Kiosk** (3osi): pabellón universal de hormigón impreso 3D 7,1×4,2×3,8 m para retail/información en parques.
  - **GAUDI'S CAT, Barcelona** (IAAC 2024): pabellón estudiantil de arcos catenarios en madera impresa 3D + tela — la catenaria como lenguaje de pabellón efímero (IAAC blog).
  - **Catenary Symphonies** (Barberio/Fabbri, 2024): pabellón estereotómico impreso 3D en eco-hormigón con residuos de piedra, «modelos funiculares de curvas catenarias + resistencia de cáscaras, geometría sometida únicamente a compresión» (LinkedIn, snippet).
  - **Ideas City Pavilion NYC 2015** (BRG): cáscara de doble curvatura de 20 m² con 442 bloques de tetra-pack reciclado CNC (IStructE).
- **Stands de feria**: el Shellstar (Eje 6) es el caso directo; los neumáticos de Otto y el pabellón de Montreal 67 (Gutbrod+Otto) son los ancestros tipológicos del stand tensado.

## Fuentes (APA, idioma original)

**Histórico Gaudí (ES):**
- Gaudí Museum. (s.f.). *El método Gaudí: geometría y naturaleza*. https://gaudi.museum/descubre-gaudi/antoni-gaudi/metodo-gaudi/ [200 ✓]
- Consorci de la Colònia Güell. (s.f.). *La Cripta Gaudí*. https://www.lacoloniaguell.cat/es/la-cripta-gaudi [200 ✓]
- Wikipedia. (2026). *Maqueta funicular de la cripta de la colonia Güell*. https://es.wikipedia.org/wiki/Maqueta_funicular_de_la_cripta_de_la_colonia_G%C3%BCell [snippet]
- Casáis Balagué, A. (s.f.). *Gaudí y el misterio de la encarnación (las incógnitas de la cripta de la colonia Güell)*. Informes de la Construcción, CSIC. https://informesdelaconstruccion.revistas.csic.es/index.php/informesdelaconstruccion/article/download/1434/1593 [snippet PDF]
- Cortés, A., et al. (s.f.). *Geometric determination of the hyperbolic paraboloids of the vaults in the entrance porch to the Crypt of Colònia Güell by Antoni Gaudí* [EN]. Informes de la Construcción, CSIC. https://informesdelaconstruccion.revistas.csic.es/index.php/informesdelaconstruccion/article/download/5958/7149 [snippet PDF]
- Fundación Antonio Gaudí. (s.f.). *Las farolas de Gaudí en Barcelona*. https://fundacionantoniogaudi.org/las-farolas-de-gaudi-en-barcelona/ [snippet]
- Wikipedia. (2026). *Farolas de la plaza Real (Barcelona)*. https://es.wikipedia.org/wiki/Farolas_de_la_plaza_real_(Barcelona) [snippet]
- Ajuntament de Barcelona, Art Públic. (s.f.). *Farolas de la plaza Real*. http://w10.bcn.cat/APPS/gmocataleg_monum/FitxaMonumentAc.do?codiMonumIntern=1383&idioma=ES [snippet]
- Sama García, A. (s.f.). *«Historia versus natura»: arquitectura y literatura en la obra de Gaudí. Los candelabros de Barcelona*. Dialnet. https://dialnet.unirioja.es/servlet/articulo?codigo=1987030 [snippet]
- Casa Batlló. (s.f.). *Streetlights for Plaza Real and Pla de Palau* [EN]. https://www.casabatllo.es/en/antoni-gaudi/lights-plaza-real-pla-palau/ [snippet]
- Junta Constructora del Temple. (2026). *Sagrada Família — booklet oficial* [ES]. https://sagradafamilia.org/documents/20142/1693659/SF_Booklet_04_20260227_digital_AF.pdf [snippet PDF]

**Candela (EN/ES):**
- Pimenta, A. (2018). *Félix Candela's Concrete Shells Through Photographs, Architectural Models and Plans*. ArchDaily. https://www.archdaily.com/888082/felix-candelas-concrete-shells-through-photographs-architectural-models-and-plans [200 ✓]
- Miller, M. (2014). *AD Classics: Los Manantiales / Felix Candela*. ArchDaily. https://www.archdaily.com/496202/ad-classics-los-manantiales-felix-candela [snippet]
- Watkins, K. (2020). *Spotlight: Félix Candela*. ArchDaily. https://www.archdaily.com/591415/spotlight-felix-candela [snippet]
- del Cueto, J. I., & Eisenschmidt, A. (2018). *Félix Candela's Concrete Shells: An Engineered Architecture for Mexico and Chicago* [brochure]. Gallery 400, UIC. https://gallery400.uic.edu/wp-content/uploads/2020/04/CS_brochure_final.pdf [snippet PDF]
- Paton, C. (s.f.). *Félix Candela, The hyperbolic paraboloid (1958)*. The Textbook of Architecture. https://textbookofarchitecture.com/source/candela [snippet]
- Galindo Díaz, J., Salazar Marulanda, C., & Escobar García, D. (2018). *El legado de Félix Candela en Colombia a través de seis proyectos inéditos*. Arquitetura Revista, 14(1), 17-28. https://www.redalyc.org/journal/1936/193656124002/193656124002.pdf [snippet PDF]
- Álvarez-Dorado, M., Fernández-Vega, D., & Morón-Fernández, C. (2022). *Estudio comparativo de estructuras ligeras en la arquitectura moderna: Eladio Dieste vs Félix Candela*. Anales de Edificación, 8(1). https://polired.upm.es/index.php/anales_de_edificacion/article/view/5015 [snippet]

**Dieste (ES/EN):**
- UNESCO World Heritage Centre. (2021). *The work of engineer Eladio Dieste: Church of Atlántida*. https://whc.unesco.org/en/list/1612/ [snippet]
- Adell Argilés, J. M. (1992). *Las bóvedas de la Atlántida*. Informes de la Construcción, 44(421). https://doi.org/10.3989/ic.1992.v44.i421.1316 [snippet]
- Más-Guindal Lafarga, A. J., & Adell, J. M. (2005). *Eladio Dieste y la cerámica estructural en Uruguay*. Informes de la Construcción, 57(496). https://doi.org/10.3989/ic.2005.v57.i496.459 [snippet]
- Álvarez Prozorovich, F. V. (1999). *Iglesia de Atlántida*. DPA (UPC). http://raco.cat/index.php/DPA/article/view/259797 [snippet]
- Corres Melachos, F., et al. (2023). *The architectural geometry of the Church of Cristo Obrero y Nuestra Señora de Lourdes*. ISPRS Archives. https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1059-2023 [snippet]

**Saarinen/Kresge (EN):**
- Plunkett, J. W., & Mueller, C. T. (2015). *Thin Concrete Shells at MIT: Kresge Auditorium and the 1954 Conference*. http://digitalstructures.mit.edu/files/2015-08/plunkett-mueller.pdf [snippet PDF]
- Whitehead, R. P. (2018). *Portentous and Predictable: Eero Saarinen, Ammann & Whitney, and the Failures of Kresge Auditorium (1950-1955)*. Iowa State University. https://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=1143&context=arch_conf [snippet PDF]
- MIT List Visual Arts Center. (s.f.). *Kresge Auditorium, 1955*. https://listart.mit.edu/art-artists/kresge-auditorium-1955 [snippet]

**Otto / tensadas (EN/DE):**
- Songel Gonzalez, J. M. (2022). *Tents: a paradigm of lightness and sustainability in vernacular architecture and in Frei Otto's work*. Journal of Cultural Heritage Management and Sustainable Development, 12(2), 171-191. https://doi.org/10.1108/JCHMSD-05-2021-0097 [snippet PDF]
- Boller, G., & D'Acunto, P. (2021). *Structural design via form finding: Comparing Frei Otto, Heinz Isler and Sergio Musmeci*. https://doi.org/10.1201/9781003173434-168 [snippet]
- Songel González, J. M. (2023). *Frei Otto: Light Structures Inspired by Nature*. https://doi.org/10.1007/978-3-031-33144-2_3 [snippet]
- Goldsmith, N. (2016). *The physical modeling legacy of Frei Otto*. International Journal of Space Structures. https://ftlstudio.com/wp-content/uploads/2016/05/International-Journal-of-Space-Structures-2016-Goldsmith-0266351116642071.pdf [snippet PDF]
- Universität Stuttgart. (s.f.). *Stuttgart Incentives — Institute for Lightweight Structures*. https://www.uni-stuttgart.de/universitaet/profil/historie/impulse/imp/alles.php_id_6_lang_en.html [snippet]
- Tomlow, J. (2016). *Designing and constructing the Olympic roof (Munich 1972)*. International Journal of Space Structures. https://doi.org/10.1177/0266351116642078 [snippet]
- schlaich bergermann partner. (s.f.). *Roof for Munich Olympic Stadium 1972*. https://www.sbp.de/en/project/roof-for-munich-olympic-stadium-1972/ [snippet]
- Olympiapark München. (s.f.). *Tent Roof*. https://olympiapark.muenchen.de/en/olympiapark/zeltdach.html [snippet]
- Glaeser, L. (1972). *The work of Frei Otto* [catálogo MoMA]. https://www.moma.org/documents/moma_catalogue_2757_300299029.pdf [snippet PDF]
- Hollyday, J. (s.f.). *Form Finding for Anticlastic Membrane Structures*. https://bigwalls.net/download/membrane.pdf [snippet PDF]
- BTES UMass. (s.f.). *Otto's Pneumatic Experiments*. https://openpublishing.library.umass.edu/btes/article/516/galley/466/download/ [snippet PDF]

**Sagrada Família actual (EN/ES):**
- Arup. (s.f.). *Sagrada Familia*. https://www.arup.com/en-us/projects/sagrada-familia/ [snippet]
- Royal Academy of Engineering / Ferguson, H. (s.f.). *Completing the Sagrada Família*. Ingenia. https://www.ingenia.org.uk/articles/completing-the-sagrada-familia/ [403 fetch — contenido citado de snippet]
- Henriques, M. (2026). *The ancient engineering marvels of the world's tallest church*. BBC Future. https://www.bbc.com/future/article/20260608-sagrada-famlia-the-ancient-engineering-marvels-of-the-worlds-tallest-church [snippet]
- McFarland, P. (2026). *Spain's Sagrada Familia: Contemporary Construction Methods Speed Iconic Basilica to Completion*. ENR. https://www.enr.com/articles/62506-spains-sagrada-familia-contemporary-construction-methods-speed-iconic-basilica-to-completion [snippet]
- Sánchez Domínguez, M. (2026). *BIM in Ongoing Heritage Construction: The case of the Sagrada Família*. IAAC Blog. https://blog.iaac.net/bim-in-ongoing-heritage-construction-the-case-of-the-sagrada-familia-a-conversation-with-esteve-umbert/ [snippet]
- Lorente, B. (2026). *The central towers at the Sagrada Familia*. Rhino World 2026. https://rhino3d.world/talk/talk-sagrada-familia/ [snippet]
- Makert, R., & Alves, G. M. (2017). *Between Designer and Design: Parametric Design and Prototyping Considerations on Gaudí's Sagrada Familia*. Periodica Polytechnica Architecture. https://doi.org/10.3311/ppar.10335 [snippet]

**Form-finding digital (EN):**
- Wintour, P. (2015). *Catenary curves and membranes in Grasshopper*. Parametric Monkey. https://parametricmonkey.com/2015/10/10/catenary-curves/ [snippet]
- Building Simplexity Lab, HKU. (2022). *Catenary Lines (Kangaroo 2)*. https://bsl.hku.hk/tutorials/physics-simulation-structural-analysis/kangaroo-2/catenary-lines/ [snippet]
- TU Delft. (s.f.). *Generative Form Finding with Kangaroo Physics* [open textbook]. https://interactivetextbooks.tudelft.nl/rhino-grasshopper/Grasshopper_Rhino_course/2_Knowledge_base/Generative_Design/Generative_Form_Finding/!index.html [snippet]
- Kang, T., & Kim, D. (2016). *Design Programming of Catenary Shell Using Grasshopper Script*. ICCCBE 2016. http://www.see.eng.osaka-u.ac.jp/seeit/icccbe2016/Proceedings/Full_Papers/011-050.pdf [snippet PDF]
- Leung, N. (2018). *The Nature of Gridshell Form Finding*. WeWantToLearn.net. https://wewanttolearn.net/2018/03/13/the-nature-of-gridshell-form-finding/ [snippet]
- Nanayakkara, K. I. (2018). *Shell Structures from Catalan to Mapungubwe* [premio PaiLin Li]. IStructE. https://www.istructe.org/IStructE/media/Public/PaiLinLiAward-2018-Candidate-Report-KIUNanayakkara.pdf [snippet PDF]
- Kudless, A. (2012). *Shellstar Pavilion*. Matsys. https://www.matsys.design/shellstar-pavilion [200 ✓]
- Popescu, M., Rippmann, M., Liew, A., Van Mele, T., & Block, P. (2019). *Concrete shell made of steel cables and knitted formwork (KnitCandela)*. DETAIL. https://www.detail.de/de_de/concrete-shell-made-of-steel-cables-and-knitted-formwork [410 — descartada como fetch; contenido de snippet archivado en crudo]

**Escala urbana (EN):**
- Walter P Moore. (s.f.). *MARS Pavilion*. https://www.walterpmoore.com/projects/mars-pavilion [snippet]
- uau studio. (s.f.). *Shell in the Park*. https://www.uau-studio.com/project/shell-in-the-park [snippet]
- 3osi. (s.f.). *Boves Kiosk 1*. https://3osi.com/projects/boves-kiosk-1/ [snippet]
- Veselova, S., & Vohra, G. (2024). *GAUDI'S CAT*. IAAC Blog. https://blog.iaac.net/gaidis-ca/ [snippet]
- Barberio, M. (2024). *Catenary Symphonies* [post]. LinkedIn. https://www.linkedin.com/posts/mauriziobarberio_catenary-symphonies-is-a-project-for-a-3d-printed-activity-7176930130710183936-PyZy [snippet]
- Cano, P. (2022). *The 9th Edition of the MPavilion, Designed by Bangkok-Based Studio All(zone), Opens in Melbourne*. ArchDaily. https://www.archdaily.com/993571/the-9th-mpavilion-designed-bangkok-based-studio-all-zone-opens-in-melbourne-australia [snippet]
- Tensinet. (s.f.). *Tachkemoni canopies*. https://tensinet.com/index.php/projects-database/projects/4754 [snippet]
- Tensil.bg. (2013). *Saddle-Shaped Membrane Canopy Playground in Oryahovo*. https://tensil.bg/en/projects/membranes/membrane-playground/ [snippet]
- Abdel, H. (2024). *Shade School Playground Pavilion / Blue Temple*. ArchDaily. https://www.archdaily.com/1019040/shade-school-playground-pavilion-blue-temple [snippet]
- Abdel, H. (2021). *Cloud Forests Pavilion for Children's Play / UNITEDLAB Associates*. ArchDaily. https://www.archdaily.com/966076/cloud-forests-pavilion-for-childrens-play-unitedlab-associates [snippet]
- Pereira, M. (2018). *Cáscaras de hormigón: principios de diseño y ejemplos construidos* [ES]. ArchDaily en Español. https://www.archdaily.com/es/895405/cascaras-de-hormigon-principios-de-diseno-y-ejemplos-construidos [snippet]
- Serna, I. (2018). *Del hueso a la piel* [ES]. Arquitectura Viva. https://arquitecturaviva.com/articulos/del-hueso-a-la-piel [snippet]
- Pino, F. G. (2016). *Centro Multiusos en Mannheim. Frei Otto. Doblando la malla hasta hacer una concha* [ES]. https://doi.org/10.24192/2386-7027(2016)(v5)(06) [snippet]

## Metodología

**Queries (ES/EN; IT gap — tema con corpus casi nulo en italiano, reportado):**
1. `Gaudí maquete funicular Colònia Güell cripta catenaria estructura` (ES) → 8 resultados, 6 útiles
2. `Félix Candela concrete shells hyperbolic paraboloid architecture ArchDaily` (EN) → 8, todos útiles
3. `Frei Otto tensile membrane structures form finding architecture` (EN) → 8, todos útiles
4. `Gaudí farolas Plaça Reial diseño urbano mobiliario` (ES) → 8, 6 útiles
5. `Eladio Dieste ladrillo armado cascarón gausa iglesia Atlántida` (ES) → 8, todos útiles
6. `Eero Saarinen Kresge Auditorium cable suspended roof Ammann Whitney` (EN) → 8, 6 útiles
7. `tensile membrane canopy pavilion kiosk playground shade structure ArchDaily` (EN) → 8, 6 útiles
8. `Sagrada Família construcción 2026 torres catenaria parametric design` (ES/EN) → 8, todos útiles
9. `"Arquitectura Viva" OR "Detail" cáscaras hormigón estructuras ligeras tensadas revista` (ES) → 8, 5 útiles
10. `Frei Otto Munich 1972 Olympic Stadium cable net roof tensile structure` (EN) → 8, todos útiles
11. `catenary shell pavilion contemporary small scale concrete Gaudí inspired kiosk` (EN) → 8, 6 útiles
12. `Kangaroo Grasshopper form finding catenary shell Rhino tutorial architecture` (EN) → 8, todos útiles

**Fetch verificación:**
| URL | Status |
|---|---|
| gaudi.museum/descubre-gaudi/antoni-gaudi/metodo-gaudi/ | 200 ✓ |
| lacoloniaguell.cat/es/la-cripta-gaudi | 200 ✓ |
| archdaily.com/888082 (Candela shells) | 200 ✓ |
| matsys.design/shellstar-pavilion | 200 ✓ |
| detail.de/de_de/concrete-shell-made-of-steel-cables-and-knitted-formwork | **410** — descartada como fetch (recurso eliminado); contenido de snippet archivado en crudo |
| ingenia.org.uk/articles/completing-the-sagrada-familia/ | **403** — descartada como fetch; contenido de snippet citado con marca |

**Gaps:**
- **IT**: sin búsqueda dedicada en italiano; el corpus italiano (Barberio/Fabbri catenary pavilions, Nervi) quedó cubierto solo por snippets en EN. Candidato a segunda pasada si SOL lo pide.
- **Arquitectura Viva**: solo 1 artículo directo (Serna 2018); la revista tiene paywall parcial. Detail: el artículo KnitCandela dio 410; hay copia del contenido en el crudo.
- **Asientos urbanos catenarios contemporáneos**: corpus débil (solo banco Park Güell como histórico); oportunidad de segunda pasada con `site:archdaily.com bench shell` o similar.
- **Normativa AR**: fuera de alcance de esta búsqueda (estructuras tensadas en CABA: no buscado).

## Propuestas wiki (esqueleto — solo si SOL aprueba curaduría)

1. **`wiki/glosario/conceptos/catenaria-funicular.md`** (nueva): catenaria vs parábola, maqueta polifunicular, tracción→compresión invertida, Gaudí→Otto→Kangaroo. Relacionadas: `bim-metodologia`, `form-finding` (nueva).
2. **`wiki/glosario/conceptos/form-finding.md`** (nueva): físico (Gaudí, Otto, Isler) → digital (Kangaroo, RhinoVault, Karamba). Relacionadas: `rhino`, `catenaria-funicular`.
3. **`wiki/glosario/referentes/felix-candela.md`** (nueva): hypar, Cubiertas Ala, Los Manantiales, regla luz/espesor 400-1000, KnitCandela como homenaje.
4. **`wiki/glosario/referentes/eladio-dieste.md`** (nueva): cerámica armada, bóveda gausa, Atlántida UNESCO, vínculo Gaudí/bóveda catalana. Relevancia AR directa (ladrillo, economía).
5. **`wiki/glosario/referentes/frei-otto.md`** (nueva): superficies mínimas, cable-net Múnich 72, reconstrucción maqueta Gaudí 1982, Pritzker 2015.
6. **`wiki/glosario/conceptos/estructuras-tensadas.md`** (nueva): membranas, cable-net, neumáticos, patterning, casos urbanos (MPavilion, canopies escolares).
7. **`wiki/glosario/conceptos/cascaras-hormigon.md`** (nueva): cáscara/membrana, regla de espesor, Kresge como contraejemplo, Maya Somaiya/RhinoVault como presente.
8. **`wiki/glosario/conceptos/gaudi-escala-urbana.md`** (nueva): farolas Plaça Reial/Pla de Palau, banco Park Güell, lección de mobiliario como primer encargo público.

## Candidatos (nivel 2 — esperan elección de SOL)

| Fuente | Por qué importa | Acceso |
|---|---|---|
| Tomlow 2016, *Designing and constructing the Olympic roof* (DOI 10.1177/0266351116642078) | Relato completo del proceso Múnich 72 con modelos físicos | DOI, probablemente paywall |
| Plunkett & Mueller 2015, *Thin Concrete Shells at MIT* (PDF MIT) | Kresge + conferencia 1954 con Candela presente | PDF abierto ✓ |
| Nanayakkara 2018, *Shell Structures from Catalan to Mapungubwe* (IStructE PDF) | Panorámica bóveda catalana→RhinoVault con dibujos | PDF abierto ✓ |
| Songel 2022, *Tents* (Emerald DOI) | Otto y vernacular, ligereza/sostenibilidad | DOI paywall, PDF UPV abierto ✓ |
| Galindo Díaz 2018, *Candela en Colombia* (Redalyc PDF) | Candela en América Latina, declive de las cáscaras | PDF abierto ✓ |
| Libro Burry et al. 2008 sobre Sagrada Família digital | Referencia canónica del workflow paramétrico SF | Libro — buscar acceso |
| KnitCandela (DETAIL 2019) | Encofrado textil + cable net, tributo a Candela | 410 — buscar copia alternativa (ETH Block Research Group) |

---

**¿Avanzo a curaduría? (s/N)** — si `s`, `@contenidos` genera el reporte legible en `raw/contenidos/` y luego `¿Avanzo a wiki?` para `@vaultworm-arq`.
