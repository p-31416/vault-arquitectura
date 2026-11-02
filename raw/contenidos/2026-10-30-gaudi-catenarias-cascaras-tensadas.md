---
tipo: raw
fecha_creacion: 2026-10-30
ultima_actualizacion: 2026-10-30
tags: [research, gaudi, catenaria, funicular, cascaras-hormigon, estructuras-tensadas, form-finding, candela, dieste, frei-otto, sagrada-familia, escala-urbana, kangaroo]
idioma: es
fuente: raw/research/2026-10-30-gaudi-catenarias-cascaras-tensadas.md
crudos:
  - raw/research/2026-10-30-gaudi-catenarias-gaudi-historico-crudo.md
  - raw/research/2026-10-30-gaudi-catenarias-candela-cascaras-crudo.md
  - raw/research/2026-10-30-gaudi-catenarias-dieste-crudo.md
  - raw/research/2026-10-30-gaudi-catenarias-otto-tensadas-crudo.md
  - raw/research/2026-10-30-gaudi-catenarias-sagrada-digital-crudo.md
  - raw/research/2026-10-30-gaudi-catenarias-escala-urbana-crudo.md
solicitante: SOL
estado: pendiente-ok
---

# Estructuras inspiradas en Gaudí — catenarias, cáscaras y tensadas

**Fecha:** 2026-10-30 (-03:00) · **Curaduría:** @contenidos desde investigación @sherlock · **Fuentes:** 70 (5 fetch 200 + 64 snippets + 1 descartada 410) · **Confianza:** Alta en histórico/estructural, Media en escala urbana (casos verificables pero dispersos)

## Índice

- [[#Resumen ejecutivo]]
- [[#Catenarias y funiculares: el método Gaudí]]
- [[#Cáscaras de hormigón: Candela, Isler y el contraejemplo Kresge]]
- [[#Dieste y la cerámica armada: la catenaria en ladrillo]]
- [[#Estructuras tensadas: Frei Otto y Múnich 72]]
- [[#Sagrada Família 2026: la catenaria en obra]]
- [[#Form-finding digital: Kangaroo y el pipeline del estudio]]
- [[#Escala urbana: farolas, asientos, juegos, stands, kioscos y pabellones]]
- [[#Fuentes]]
- [[#Referencias (bibliografía y repos oficiales)]]
- [[#Otros links de interés]]
- [[#Registro HITL]]

## Resumen ejecutivo

La línea que va de Gaudí a hoy se puede contar como **una sola idea con dos materiales**: encontrar la forma dejando que las fuerzas la dibujen. Gaudí la resolvió con la **maqueta polifunicular** — cuerdas colgadas del techo con saquitos de perdigones de plomo proporcionales a las cargas reales, fotografiados e invertidos: lo que cuelga a tracción pura, invertido, se sostiene a compresión pura [[#^f1|1]][[#^f2|2]]. Esa misma lógica produce dos familias estructurales que conviven desde hace un siglo:

1. **Cáscaras y form-found a compresión** (hormigón, ladrillo): Candela con sus hypars de encofrado de tablas rectas [[#^f12|12]][[#^f16|16]], Dieste con bóvedas gausas de cerámica armada de directriz catenaria [[#^f23|23]][[#^f24|24]], Heinz Isler con telas húmedas colgadas y congeladas en hormigón [[#^f56|56]], y hoy KnitCandela, RhinoVault y Kangaroo como form-finding digital [[#^f58|58]][[#^f56|56]][[#^f57|57]].
2. **Tensadas y form-found a tracción** (membranas, cable-net): Frei Otto con películas de jabón como superficies mínimas y redes colgantes invertidas como gridshells [[#^f30|30]][[#^f33|33]], el techo olímpico de Múnich 1972 como cable-net de 74.000-78.000 m² [[#^f36|36]][[#^f37|37]], y hoy MPavilion, canopies escolares y juegos infantiles [[#^f64|64]][[#^f65|65]][[#^f66|66]].

El hallazgo transversal para el estudio: el form-finding físico de Gaudí y Otto es el mismo algoritmo que hoy corre en **Kangaroo (Grasshopper/Rhino)** — hay papers y tutoriales que reproducen digitalmente la maqueta de Isler y el pabellón de Montreal 67 [[#^f54|54]][[#^f57|57]]. El estudio ya trabaja con Rhino: la catenaria es el puente natural entre el legado Gaudí y el pipeline paramétrico del vault. Y en escala urbana, Gaudí mismo empezó ahí — las farolas de la Plaça Reial fueron su primer encargo público [[#^f6|6]][[#^f7|7]] — mientras que hoy la escala pequeña está dominada por membranas tensadas y cáscaras modulares ligeras [[#^f59|59]][[#^f60|60]][[#^f64|64]].

## Catenarias y funiculares: el método Gaudí

### La maqueta polifunicular

En un cobertizo junto a la obra de la cripta de la Colònia Güell, Gaudí montó una maqueta a escala 1:10 de cuatro metros de altura, colgada boca abajo del techo: un tablero con la planta del edificio, del que pendían cordeles, y de los cordeles saquitos de tela llenos de perdigones de plomo, proporcionales a las cargas que cada punto tendría que soportar de verdad [[#^f1|1]]. El Consorci de la Colònia Güell describe el procedimiento completo: se colgaban las cuerdas en los puntos correspondientes al cruce de los muros o al nacimiento de las columnas, se forraba la maqueta con papel para obtener las bóvedas y los muros, y se fotografiaba el conjunto; sobre las ampliaciones de la fotografía invertida Gaudí dibujaba directamente sus esbozos [[#^f2|2]]. La cita clave del Gaudí Museum resume el método: «Al colgar, un cordel adopta por sí solo la única forma que trabaja a tracción pura, sin flexión. Gaudí fotografiaba el conjunto y le daba la vuelta a la fotografía. Lo que cuelga hacia abajo, invertido, es exactamente lo que se sostiene hacia arriba, y solo a compresión… La estructura no se calculaba después de dibujar: la estructura era el dibujo» [[#^f1|1]].

La maqueta no la hizo solo: trabajaron en ella Francesc Berenguer, el modelista Joan Bertran, el albañil Agustí Massip, el carpintero Joan Munné y el ingeniero alsaciano Eduard Goetz [[#^f1|1]]. El original se destruyó en julio de 1936; la reconstrucción que hoy se expone se hizo en **Stuttgart en 1982 bajo la dirección de Frei Otto** — el nudo histórico Gaudí↔Otto es literal [[#^f1|1]][[#^f34|34]]. Casáis (CSIC) subraya el carácter pionero: la iglesia de la Colònia Güell fue «el primer edificio relevante generado mediante la utilización —en un modelo tridimensional— de las líneas funiculares como sistema de determinación de formas estables», un conjunto de líneas funiculares «trenzado en las tres dimensiones del espacio» que él denomina «estéreo-funícula» [[#^f4|4]].

### Catenaria vs parábola

La catenaria es la forma que toma una cadena colgada por sus dos extremos con el peso repartido a lo largo de la propia cadena; la parábola es la del cable con peso repartido a lo largo de la horizontal, como en un puente colgante [[#^f1|1]]. En luces pequeñas ambas curvas se confunden, y las fuentes se contradicen en casos concretos: los 270 arcos del desván de la Casa Milà son catenarios según lapedrera.com y parabólicos según el Cuaderno Informativo 3 [[#^f1|1]]. La definición oficial de la basílica añade la propiedad estructural decisiva: el arco catenario «es estable por sí mismo, no necesita otros elementos de apoyo» — Gaudí llamaba a los arbotantes góticos «muletas», y su eliminación era el camino para inundar el interior de luz [[#^f1|1]][[#^f11|11]].

La primera catenaria documentada de su obra está en la Cooperativa Obrera Mataronense (1878-1882): 12 arcos en una nave de 48×12 m, con el sistema de pernos de Philibert de l'Orme [[#^f1|1]]. Le siguen los corredores del Colegio Teresiano (1888-89), los 60 arcos del desván de Casa Batlló, los 270 de Casa Milà (~80 cm de separación) y los parabólicos lobulados de Bellesguard [[#^f1|1]]. Gaudí defendía además que «una columna bien inclinada es más estable que una vertical» (Cuaderno Informativo 4) [[#^f1|1]][[#^f11|11]].

### Superficies regladas: construibles con tablas rectas

La genialidad constructiva de Gaudí está en combinar curvatura estructural con **superficies regladas** — generadas por rectas, lo que permite encofrarlas con tablones de madera rectos [[#^f2|2]]. El repertorio: el **hiperboloide** (289 lucernarios de la Sagrada Família más el gran hiperboloide del ábside a 75 m), el **paraboloide hiperbólico** — cuya introducción en el pórtico de la cripta de la Colònia Güell fue, según el Consorci, «la primera vez en la historia de la arquitectura» [[#^f2|2]], verificación estadística mediante: Cortés et al. (CSIC) confirmaron con ajuste superior al 99% que 14 de las 19 bóvedas del pórtico fueron diseñadas sobre hypars [[#^f5|5]] —, el **helicoide** (columnas de doble giro de la nave) y el **conoide** (Escoles de la Sagrada Família, 1908-09, dibujadas por Le Corbusier en 1928) [[#^f1|1]].

### La cripta en pie: una advertencia técnica

Casáis advierte un punto crítico que el estudio debe retener: la cripta construida trabaja con un **estado de cargas parcial** — solo la nave inferior — que el modelo funicular no previó, porque fue estudiado para el edificio completo. El mapa de fisuras de la solera de rasilla (tres gruesos, 6 cm, ~200 kg/ml) es la evidencia en pie [[#^f4|4]]. Lección: el form-finding es válido para el sistema completo; las construcciones parciales exigen recálculo propio.

## Cáscaras de hormigón: Candela, Isler y el contraejemplo Kresge

### Félix Candela: el hypar industrializado

Félix Candela (1910-1997) funda **Cubiertas Ala** en 1950 con sus hermanos y los arquitectos Fernández Rangel, y entre 1950 y 1976 la empresa acumula **~1.500 proyectos**, más de la mitad construidos [[#^f15|15]]. Su geometría base es el **paraboloide hiperbólico**: superficie de doble curvatura generada por rectas, «lo bastante simple para calcular a mano, cuya doble curvatura hace rígida una cáscara delgada, y cuyas generatrices rectas permiten encofrado con tablas rectas» [[#^f16|16]]. El encofrado de cada cáscara se hacía íntegramente con tablas rectas antes de colocar la armadura y verter el hormigón a mano [[#^f15|15]].

Obras clave: el Pabellón de Rayos Cósmicos de la UNAM (1951, «una de las cáscaras de hormigón más delgadas jamás construidas», la obra que le dio fama nacional) [[#^f15|15]], la capilla de Palmira/Lomas de Cuernavaca (1958), el restaurante **Los Manantiales** en Xochimilco (1958) y el Palacio de los Deportes para los Juegos Olímpicos de 1968 [[#^f12|12]]. Los Manantiales es el caso de manual: array circular de ocho hypars de borde curvo en flor (bóveda de aristas de ocho lados), luz de 106 pies entre apoyos y diámetro máximo de 139 pies, con espesor de **4 cm**; las fuerzas de membrana mayores viajan por las aristas, reforzadas con «vigas V» ocultas de acero, y el resto de la estructura trabaja esencialmente a compresión con armadura mínima [[#^f13|13]]. Recibió en 1961 el premio Auguste Perret (UIA) y la medalla de oro de la Institution of Structural Engineers [[#^f19|19]].

La **regla de oro de Candela** (Textbook of Architecture): luz/espesor de una buena cáscara ≈ **400-1000** (un huevo ≈ 100) [[#^f16|16]]. El principio es «strength from form»: la cáscara delgada trabaja por fuerzas de membrana en su superficie, no por flexión; dándole forma según cargas y apoyos, puede salvar grandes luces con unos centímetros de espesor [[#^f16|16]]. Su evolución tipológica (Galindo Díaz et al.) va desde «cascarones de perfil catenario» (bóveda experimental de San Bartolo, 1949) hasta formas sinusoidales (Residencia Romero, 1951), conoidales (Auditorio de Química UNAM, 1952), plegadas (Agencia Nash, 1952) y cilíndricas (Fábrica Textil La Fama, 1955) [[#^f17|17]].

### El declive de las cáscaras (~1965)

Hacia mediados de los 60 las cáscaras pierden atractivo por factores económicos y prácticos: encarecimiento de encofrados y mano de obra, dificultades de impermeabilización y reparación, oscuridad de los espacios interiores, poca adaptabilidad a cambios de uso, y la competencia de las estructuras metálicas ligeras y la creciente industria de cubiertas textiles [[#^f15|15]][[#^f17|17]]. Es el mismo vacío que las estructuras tensadas de Otto vinieron a llenar.

### Kresge Auditorium: el contraejemplo pedagógico

El Kresge Auditorium del MIT (Eero Saarinen + Ammann & Whitney, 1953-55) es una cáscara de 1/8 de esfera sobre tres apoyos, con luz libre de 48,8 m — la mayor de EE.UU. en su momento — y un peso de solo 1.100 t, proporción de cáscara de huevo [[#^f20|20]][[#^f22|22]]. Es también **el contraejemplo de manual**: Saarinen fijó la forma sin consultar a los ingenieros — el modelo inicial en plastilina se llamaba «the Vulgar Freak» — y el equipo fue simplemente convocado a «make it work» [[#^f21|21]]. Al retirar el encofrado en abril de 1954, los tres arcos de borde de 18" deflectaron mucho más de lo previsto (esperaban 1,5"; siguieron deflectando seis semanas), y la solución fue reforzar nueve montantes de ventana para sostener el borde libre — hecho que se mantuvo oculto hasta septiembre de 1954 [[#^f20|20]][[#^f21|21]].

Plunkett & Mueller formulan la contradicción central de las cáscaras, que vale como criterio de diseño para el estudio: ofrecen «un espectro infinito de posibilidades para nuevas formas estructurales», pero «su éxito depende de una relación precisa y a veces intratable entre geometría y comportamiento estructural; el hecho de que una forma se materialice en hormigón delgado no significa que se comporte como una cáscara eficiente» [[#^f20|20]]. La catenaria de Gaudí funciona porque la forma ES el cálculo; la esfera de Kresge falla porque la forma se impuso. (Contexto: las cáscaras se formalizaron en Alemania en los años 20 con Dischinger y Finsterwalder [[#^f20|20]].)

### Heinz Isler: la tela colgada

Heinz Isler — comparado con Otto y Musmeci por Boller & D'Acunto [[#^f31|31]] — desarrolló el método experimental complementario: **telas húmedas colgadas que se congelan en la forma de equilibrio** y se construyen en hormigón. Casos: Deitingen (1968, dos cáscaras de 31,6×26 m y 90 mm de espesor, forma de tela colgada) y Wyss Garden Centre en Solothurn (1962, 650 m², 70 mm, con borde en labio invertido que «imita los labios levantados observados en los modelos de cadenas y telas colgadas») [[#^f56|56]]. Su método experimental fue digitalizado después con Grasshopper+Kangaroo y validado contra SAP2000 (ver [[#Form-finding digital: Kangaroo y el pipeline del estudio]]) [[#^f54|54]].

## Dieste y la cerámica armada: la catenaria en ladrillo

Eladio Dieste (1917-2000) inventó la **cerámica armada**: ladrillo + mortero + barras de alambre de acero embebidas en las juntas (0,5 kg/m² en muros, 2 kg/m² en bóveda) [[#^f24|24]][[#^f25|25]]. Su pieza tipológica es la **bóveda gausa**: el perfil longitudinal es una catenaria — «el inverso del diagrama de momentos flectores de la cubierta» — de modo que el peso propio no genera tracciones, y la sección transversal ondulada aporta la rigidez que el espesor fino no da [[#^f28|28]]. La forma de las bóvedas «está definida por la curva catenaria resultante de la distribución del peso del cielorraso» (documento de nominación UNESCO) [[#^f23|23]].

La obra cumbre es la **Iglesia Cristo Obrero de Atlántida** (1958-60, UNESCO 2021): nave única de ~16×30 m, luz media de 16 m (máxima 18,80 m), flecha variable entre 7 y 147 cm — «el valle de la onda es casi horizontal» —, muros ondulados formados por una sucesión de conoides de directriz recta al piso y ondulada arriba, y **tensores embebidos en los valles** de la ondulación que absorben el empuje de las bóvedas anclados en las carreras de coronamiento [[#^f23|23]][[#^f24|24]]. Dieste lo describía como «una suerte de pórtico superficial de dos articulaciones» de gran rigidez transversal [[#^f27|27]]. Durante la construcción el techo trabaja como bóveda gausa y luego como cáscara autoportante, con un grueso total de ~18 cm [[#^f24|24]].

El **vínculo con Gaudí es explícito** en la literatura: Álvarez Prozorovich escribe que «sobre los muros laterales planean Gaudí y sus dibujos para la Cripta Güell, pero Dieste trabaja siguiendo una estricta simetría: repite, rítmicamente, seis veces, la sección ondulante anunciada en la fachada y construye una nave, como la de sus edificios para mercados o galpones industriales» [[#^f26|26]]. La tradición de fondo es la **bóveda tabicada a la catalana** (Guastavino) que Gaudí heredó: capas de ladrillos delgados (3 capas de 15-20 mm) donde la primera capa actúa de encofrado de las siguientes, sin encofrado convencional [[#^f56|56]]. Adell Argilés describe Atlántida precisamente como «una depurada ejecución de bóveda tabicada a la catalana» con tablero de triple hoja [[#^f24|24]].

La **comparativa Dieste vs Candela** (Álvarez-Dorado et al., Anales de Edificación 2022) cierra el cuadro: las cáscaras de hormigón logran luces de casi el doble que la cerámica armada y mejor espacialidad diáfana; la cerámica gana en economía de encofrado y movilidad — el fraguado lento del hormigón limita el ritmo de obra [[#^f18|18]][[#^f24|24]]. Para un estudio que trabaja en Argentina, la relevancia es directa: el ladrillo, la economía de medios y la mano de obra local son el terreno natural de la línea Dieste; de hecho, la caracterización de morteros y cerámicos de Atlántida fue hecha por el CIC de la Provincia de Buenos Aires dentro del plan Getty *Keeping It Modern* [[#^f27|27]].

## Estructuras tensadas: Frei Otto y Múnich 72

### Los dos principios espejados de Otto

Frei Otto (1925-2015, Pritzker 2015) definió la construcción ligera (*Leichtbau*) como «una forma de construir con un consumo mínimo de medios materiales, energéticos y económicos» [[#^f30|30]]. Su método se apoya en dos principios espejados: las **películas de jabón** como superficies mínimas a tracción pura (membranas que se autoorganizan dentro de las condiciones de borde hasta el estado de energía mínima) [[#^f32|32]], y las **redes colgantes con pesos, invertidas**, que producen gridshells a compresión [[#^f30|30]][[#^f33|33]]. Su grupo «Biologie und Bauen» (1961) y el Institut für Leichte Flächentragwerke (IL) de Stuttgart sistematizaron el form-finding físico con «materiales que todos conocemos de la infancia: burbujas de jabón, arena, piedras, hilo, tela, cadenas, yeso y film plástico» — máquinas de film de jabón, de camino mínimo, de placa rotatoria e inclinable [[#^f34|34]]. Goldsmith, del equipo del IL, lo resume: «cada tecnología de modelado reflejaba la inteligencia estructural de tecnologías distintas: la superficie mínima del film de jabón para membranas a tracción y la forma catenaria de la cadena colgada para arcos y cáscaras a compresión» [[#^f33|33]]. La influencia biomimética viene de D'Arcy Thompson, *On Growth and Form* [[#^f33|33]].

### Múnich 1972: el cable-net que fundó lo ligero

El techo olímpico de Múnich 1972 (Behnisch + Otto + Leonhardt/Schlaich + Argyris) es «virtualmente el progenitor de todas las estructuras ligeras» [[#^f36|36]]. Datos técnicos: cable-net pretensado de **74.000 m²** según schlaich bergermann (78.000 m² según Olympiapark — discrepancia reportada; solo el estadio son 34.000 m² según el catálogo MoMA), mallas de 75×75 cm, mástiles de 51-80 m, cubierta de metacrilato, cables de borde tipo *locked coil* y nodos de acero colado [[#^f36|36]][[#^f37|37]][[#^f38|38]]. El proceso es tan instructivo como el resultado: form-finding con modelos a escala 1:200 en los que «se usaron medias de nylon para simular la forma de la cubierta tensándolas y levantándolas con palitos de madera», y modelos de medición 1:125 con alambres de acero inoxidable de 0,2 mm (malla de 24 mm, cada 4º cable real); **más de 50.000 horas de trabajo en modelos físicos** [[#^f39|39]]. Cuando los modelos físicos no podían dar datos exactos para los patrones de corte, Argyris y Linkwitz entregaron los primeros métodos computacionales iterativos para calcular longitudes de cable y posiciones de nodos — el nacimiento del cálculo numérico de estructuras tensadas [[#^f35|35]][[#^f36|36]]. El antecedente directo fue el pabellón alemán de Montreal 67 (Gutbrod+Otto), donde se desarrolló el «micrómetro de Montreal» para medir tensiones en modelos; Heinz Isler trabajó la subestructura del estadio [[#^f39|39]].

### Membranas hoy: form-finding y patterning

La guía técnica de Hollyday define el estado del arte operativo: el form-finding «es el proceso de determinar la forma de equilibrio con un pretensado dado, cargas aplicadas y propiedades de membrana»; la mayoría de los programas trabajan sobre mallas triangulares de 3 nodos, ventajosas para el *patterning* posterior (el corte de la tela); los tres métodos principales convergen en la superficie mínima para el pretensado y las condiciones de borde dadas; y la forma final puede apartarse de la superficie de equilibrio para optimizar cargas extremas y montaje en obra [[#^f40|40]]. Los neumáticos de Otto completan el repertorio: membranas casi ingrávidas, desplegables, que «podrían teóricamente abarcar millas» — sus límites son económicos, sociales y energéticos, no estructurales [[#^f41|41]]. Y el puente entre tensadas y cáscaras es la **Multihalle de Mannheim** (1975, Mutschler+Langner+Otto): gridshell de madera nacida de «doblar la malla hasta hacer una concha» — la red colgante invertida vuelta cáscara a compresión [[#^f43|43]].

## Sagrada Família 2026: la catenaria en obra

### Estado de obra

Al 2026: torre de María (138 m) terminada en 2021, las cuatro torres de los Evangelistas (135 m) en 2022-2023, y la **torre de Jesucristo (172,5 m — 23 veces el módulo base de 7,5 m) en cierre para 2026**, centenario de la muerte de Gaudí; la fachada de la Gloria queda para la fase final [[#^f11|11]][[#^f45|45]][[#^f47|47]]. Al coronarse con su cruz de cinco brazos, será la iglesia más alta del mundo y el edificio más alto de Barcelona [[#^f45|45]].

### Piedra pretensada: el aporte de Arup

Desde 2014, con la obra al 60%, Arup aborda el problema estructural central: las seis torres centrales se apoyan sobre la nave y la cripta de Villar, cuyos cimientos no resisten el peso de una torre en mampostería tradicional ni en hormigón armado con revestimiento de piedra. La solución: **piedra pretensada prefabricada** — paneles de 5 t en la torre de María y de 25 t (12 por anillo, 450 mm de espesor) en la de Jesús — que reduce el peso a la mitad y acelera el programa [[#^f44|44]][[#^f45|45]]. La lógica combina la catenaria con el pretensado: la forma del arco mantiene la piedra a compresión con la masa de la propia torre, y los tendones internos añaden más compresión, de modo que con viento fuerte casi no aparece tracción a barlovento [[#^f46|46]]. Arup lo llama «diseño paramétrico: conocimiento humano profundo de las variables estructurales + herramientas algorítmicas que modelan las cientos de variaciones sutiles de geometría» [[#^f44|44]].

### Las columnas catenarias y sus límites

Las columnas de la nave (terminada 2010) son, vistas en sección transversal, las catenarias de Gaudí sin verticales; pero en sección longitudinal son completamente regulares y convencionalmente verticales — Gaudí usó la catenaria en 2D, no en 3D completo, con la excepción de las cuatro columnas verticales del crucero [[#^f45|45]]. Liam Duff (Arup) lo confirma: «usó catenarias para llegar a las formas más eficientes», con columnas ramificadas que se abren como árboles para recibir el peso del techo y las torres [[#^f46|46]].

### El workflow actual: el pipeline del estudio, en versión monumental

El equipo técnico de la Sagrada Família trabaja hoy con un flujo que el estudio reconoce como propio: modelado paramétrico en **Rhino+Grasshopper** → impresión 3D de maquetas físicas (continuando la tradición de Gaudí) → **Rhino con atributos embebidos como BIM de piedra** (cada bloque lleva su información de fabricación y colocación) → Revit para documentación y coordinación → **mock-ups 1:1 antes de cada fase** (cientos de paneles instalados sin problemas, atribuidos a los prototipos) [[#^f48|48]]. En Rhino World 2026, el equipo presentó la línea completa: «de arcos catenarios a estructuras polifuniculares completas "form finding" que encuentran el camino natural de las fuerzas hasta el suelo»; la subdivisión en triángulos de la Colònia Güell se reutiliza hoy para las bóvedas hiperboloides y la cruz 3D de la torre de Jesús (replicada con el método de doble helicoide que Gaudí inventó para las columnas de la nave, desde los modelos de yeso originales); y las herramientas nuevas son estudios solares y CFD para ventilación pasiva [[#^f49|49]]. Makert & Alves lo sintetizan académicamente: Gaudí y Otto usaron el mismo fenómeno — la catenaria como «estado de energía mínima del sistema» — y el material como sistema de cálculo de la forma; pese a trabajar con las últimas herramientas tecnológicas, el método sigue siendo el de Gaudí [[#^f50|50]].

## Form-finding digital: Kangaroo y el pipeline del estudio

**Kangaroo** es un motor de física en vivo para simulación, optimización y form-finding dentro de Grasshopper: opera como sistema de partículas que procesa fuerzas simultáneas sobre puntos [[#^f52|52]]. Para catenarias hay dos caminos: el componente nativo `Catenary` de Grasshopper es matemático-exacto, mientras que Kangaroo da una aproximación física que además permite **membranas catenarias completas y estructuras anidadas** (malla en vez de superficie; si se necesita NURBS, se reconstruye después de la simulación) [[#^f51|51]]. La receta básica de catenaria en Kangaroo 2: líneas subdivididas → anclas fijas → fuerza unary en Z → constraint de longitud con *rest length* original → solver → interpolación de curva; para invertir la curva, el vector de gravedad pasa de (0,0,-1) a (0,0,1) [[#^f51|51]][[#^f52|52]]. El textbook abierto de TU Delft sistematiza el flujo general: preparar geometría (la resolución del mesh define la simulación) → decidir constraints → aplicar Goals → Show → solver → ajustar [[#^f53|53]].

La reproducción digital de Isler ya es un paper: Kang & Kim (ICCCBE 2016) modelan el form-finding del Naturtheater Grötzingen de Isler con script Grasshopper+Kangaroo+WeaverBird — superficie plana → subdivisión → wireframe con riostras → muelles de Kangaroo → gravedad → anclas → simulación de colgado → mesh → DXF → SAP2000 — validando contra análisis previos [[#^f54|54]]. El tutorial de WeWantToLearn da la versión para gridshells: una red anclada por sus esquinas y colgada bajo gravedad simulada genera curvas colgantes que, convertidas en superficie y espejadas, forman una cáscara catenaria que rinde excepcionalmente a compresión «siempre que los bordes estén reforzados y las esquinas arriostradas» [[#^f55|55]].

En el extremo de las cáscaras a compresión está **RhinoVault** (Block Research Group, ETH): software de form-finding de cáscaras usado en el Armadillo Vault, el MLK Jr Pavilion, la bóveda de Valldaura Labs y la **biblioteca Maya Somaiya** (Sameep Padora & Associates, Maharashtra, 2017) — cáscara de ladrillo con bóveda catalana diseñada con RhinoVault por un estudio independiente del BRG, prueba de que la herramienta ya es de dominio público [[#^f56|56]]. El caso de manual a escala de stand de feria es el **Shellstar Pavilion** (Matsys, Hong Kong 2012): pabellón de 8×8×3 m en Coroplast de 4 mm con ~1.500 celdas, «form-finding basado en las técnicas clásicas de Antoni Gaudí y Frei Otto» con Grasshopper+Kangaroo, optimización de planitud de celdas con Python, fabricación CNC y escaneo 3D de la estructura construida [[#^f57|57]]. Y el homenaje directo a Candela es **KnitCandela** (BRG+ZHCODE, 2019): cáscara de ~50 m² con red de cables de acero ultra-ligera y encofrado textil tejido a máquina (55 kg de encofrado para 5 t de hormigón) [[#^f58|58]].

## Escala urbana: farolas, asientos, juegos, stands, kioscos y pabellones

### Gaudí urbano: el mobiliario como primer encargo público

Las **farolas de la Plaça Reial** (1878-79) fueron el primer encargo público de Gaudí: dos farolas de 6 brazos inauguradas el 24-09-1879, en hierro colado y mármol de Santa Cruz, con remate de caduceo de Mercurio (dios del comercio) con casco alado y escudo de Barcelona policromado; presupuesto de 3.605 pesetas, memoria «Candelabro. Apuntes descriptivos del proyecto de candelabros de grupo para plazas y paseos de la ciudad de Barcelona» (junio 1878), equipo con Eudald Puntí, Llorenç Matamala y la Fundición Valls Hermanos [[#^f6|6]][[#^f7|7]]. Le siguen las de **Pla de Palau** (4 de 3 brazos, 1890, quedan 2) y dos en el Paseo Nacional, desaparecidas [[#^f6|6]]. Su **Memoria** es uno de los pocos textos proyectuales de Gaudí: «a la sobreabundancia ornamental escultórica se prefiere con gran tino la estructura de los materiales naturales realzada con sencillos perfiles» [[#^f6|6]]. Diseño sustentable *avant la lettre*: proyectadas a gas, electrificadas después, 140+ años en pie [[#^f6|6]]. Gaudí quiso instalarlas ante el Ayuntamiento, la Llotja, la Aduana, la Catedral, el Portal de l'Àngel y varias plazas — quedó en 6 unidades [[#^f8|8]]. La lectura de Sama García añade la capa simbólica: el candelabro como «metáfora sobre la historia de Cataluña», imagen de «un mítico guerrero que ilumina el porvenir del pueblo catalán» [[#^f10|10]]. En mobiliario, el **banco serpiente del Park Güell** (Jujol, 1906-14) lleva la superficie reglada a escala de asiento urbano [[#^f1|1]].

### Membranas tensadas a escala urbana

El patrón dominante en sombreado urbano contemporáneo es la **membrana tensada**: luz, costo, velocidad y ausencia de columna central. Casos verificables:

- **MPavilion 2022, Melbourne** (all(zone) + AECOM): pabellón temporal de tres capas textiles — redes de pesca recicladas por fuera, membrana STFE de 250 m² (primera vez en Australia, diez veces más liviana que el vidrio) y waffle interior de Soltis 86 de 1.400 m² que se mueve con la brisa; el kiosco se repinta cada temporada y el pabellón se dona a la ciudad al cerrar [[#^f64|64]]. El MPavilion de Murcutt (2019) muestra la versión ligera: cubierta curva con membrana translúcida Serge Ferrari Flexlite 702 S2, 315,9 m², inspirada en el ala de avioneta usada como sombra en Yaxchilán [[#^f69|69]].
- **Canopies Tachkemoni, Amberes** (Laurent Ney + Christiaan Poulissen, 2001): membranas hypar pretensadas contra anillo tubular sobre patios de escuela urbana (círculo de 12 m Ø y elipse de 16×21 m, 263 m²); detalle constructivo memorable: al tensar la membrana, las columnas se desplazaron 10 cm, así que se fijaron torcidas respecto de sus fundaciones para quedar perfectamente verticales una vez tensado el conjunto [[#^f65|65]].
- **Playground Oryahovo, Bulgaria** (tensil.bg, 2013): membrana en silla de montar de 11×11 m sobre juegos infantiles, en textil transpirable MEHLER POLYMAR MESH FR que deja pasar aire y luz [[#^f66|66]].
- **Shade School Playground Pavilion, Yangón** (Blue Temple, 2023): 127 m² de sombra para patio escolar con bambú + membrana, con todas las fundaciones fuera del patio, sobre el pasto [[#^f67|67]].
- **Cloud Forests, Hwaseong, Corea** (UNITEDLAB, 2018): 70 m² de pabellón de juego con varillas de aluminio y globos, presupuesto total de US$4.000 — diseño, instalación y mantenimiento por 6 meses [[#^f68|68]].

### Cáscaras y kioscos a escala urbana

El segundo patrón son las **cáscaras ligeras modulares**, que aportan permanencia, drenaje natural y huella mínima:

- **MARS Pavilion, Palm Springs 2017** (Form Found Design + Walter P Moore): **catenaria invertida de hormigón** construida con robots ABB + encofrado de tela, 70 componentes «wishbone» atornillados; el texto es explícito: «la geometría se invierte para que la cadena "cuelgue" hacia arriba, evocando el uso que Antoni Gaudí hacía de invertir formas parabólicas, hiperbólicas y catenarias en mampostería, notablemente en la Sagrada Familia». Primer hormigón robótico del sur de California, exhibido en la conferencia MARS de Amazon (Machine learning, Automation, Robotics, Space exploration) y luego en el A+D Museum de Los Ángeles [[#^f59|59]].
- **Shell in the Park, Varna** (uau studio): kioscos modulares de hormigón plegado de **50 mm** de espesor en el Jardín del Mar; 3 paneles + 2 conexiones = arco = kiosco, con drenaje por gravedad en los planos inclinados, expandibles a pabellón, en hormigón sostenible Effix Design [[#^f60|60]].
- **Boves Kiosk** (3osi): pabellón universal de hormigón impreso 3D (B25/M350 con fibra), 7,1×4,2×3,8 m, para retail, café, información o servicios en parques y glamping [[#^f61|61]].
- **GAUDI'S CAT, Barcelona** (IAAC 2024): pabellón estudiantil del MAA01 con arcos catenarios en madera impresa 3D («cheapwood») + tela, la catenaria como lenguaje de pabellón efímero barcelonés [[#^f62|62]].
- **Catenary Symphonies** (Barberio/Fallacara, 2024): pabellón estereotómico impreso 3D en eco-hormigón con residuos de procesamiento de piedra, «modelos funiculares de curvas catenarias + resistencia de cáscaras, geometría sometida únicamente a compresión» — línea italiana de estereotomía digital, candidata a segunda pasada [[#^f63|63]].
- **Ideas City Pavilion, NYC 2015** (BRG): cáscara de doble curvatura de 20 m² con 442 bloques de tetra-pack reciclado fresados CNC — pabellón efímero urbano de cáscara [[#^f56|56]].

### Stands de feria

El **Shellstar** es el caso directo de catenaria a escala de stand de feria [[#^f57|57]]; los neumáticos de Otto [[#^f41|41]] y el pabellón de Montreal 67 (Gutbrod+Otto) [[#^f39|39]] son los ancestros tipológicos del stand tensado. La síntesis de la investigación deja tres patrones replicables para el estudio: (1) membranas tensadas para sombreado y eventos — pretensado + patterning + anclajes como claves técnicas; (2) cáscaras ligeras modulares para kioscos permanentes; (3) pabellones efímeros de catenaria como lenguaje de evento.

## Fuentes

Fecha de consulta de todas: **2026-10-30**. Marca de confianza: `✅ fetch 200` = verificada por fetch directo; `⚠️ snippet` = contenido visto en resultados de búsqueda (sin fetch); `⛔` = descartada como fetch (410/403), contenido de snippet citado con marca.

**Gaudí histórico**

[^1]: Gaudí Museum. (s.f.). *El método Gaudí: geometría y naturaleza*. https://gaudi.museum/descubre-gaudi/antoni-gaudi/metodo-gaudi/ — ✅ fetch 200 ^f1
[^2]: Consorci de la Colònia Güell. (s.f.). *La Cripta Gaudí*. https://www.lacoloniaguell.cat/es/la-cripta-gaudi — ✅ fetch 200 ^f2
[^3]: Wikipedia. (2026). *Maqueta funicular de la cripta de la colonia Güell*. https://es.wikipedia.org/wiki/Maqueta_funicular_de_la_cripta_de_la_colonia_G%C3%BCell — ⚠️ snippet ^f3
[^4]: Casáis Balagué, A. (s.f.). *Gaudí y el misterio de la encarnación (las incógnitas de la cripta de la colonia Güell)*. Informes de la Construcción, CSIC. https://informesdelaconstruccion.revistas.csic.es/index.php/informesdelaconstruccion/article/download/1434/1593 — ⚠️ snippet PDF ^f4
[^5]: Cortés, A., et al. (s.f.). *Geometric determination of the hyperbolic paraboloids of the vaults in the entrance porch to the Crypt of Colònia Güell by Antoni Gaudí*. Informes de la Construcción, CSIC. https://informesdelaconstruccion.revistas.csic.es/index.php/informesdelaconstruccion/article/download/5958/7149 — ⚠️ snippet PDF ^f5
[^6]: Fundación Antonio Gaudí. (s.f.). *Las farolas de Gaudí en Barcelona*. https://fundacionantoniogaudi.org/las-farolas-de-gaudi-en-barcelona/ — ⚠️ snippet ^f6
[^7]: Wikipedia. (2026). *Farolas de la plaza Real (Barcelona)*. https://es.wikipedia.org/wiki/Farolas_de_la_plaza_real_(Barcelona) — ⚠️ snippet ^f7
[^8]: Ajuntament de Barcelona, Art Públic. (s.f.). *Farolas de la plaza Real*. http://w10.bcn.cat/APPS/gmocataleg_monum/FitxaMonumentAc.do?codiMonumIntern=1383&idioma=ES — ⚠️ snippet ^f8
[^9]: Casa Batlló. (s.f.). *Streetlights for Plaza Real and Pla de Palau*. https://www.casabatllo.es/en/antoni-gaudi/lights-plaza-real-pla-palau/ — ⚠️ snippet ^f9
[^10]: Sama García, A. (s.f.). *«Historia versus natura»: arquitectura y literatura en la obra de Gaudí. Los candelabros de Barcelona*. Dialnet. https://dialnet.unirioja.es/servlet/articulo?codigo=1987030 — ⚠️ snippet ^f10
[^11]: Junta Constructora del Temple. (2026). *Sagrada Família — booklet oficial*. https://sagradafamilia.org/documents/20142/1693659/SF_Booklet_04_20260227_digital_AF.pdf — ⚠️ snippet PDF ^f11

**Candela**

[^12]: Pimenta, A. (2018). *Félix Candela's Concrete Shells Through Photographs, Architectural Models and Plans*. ArchDaily. https://www.archdaily.com/888082/felix-candelas-concrete-shells-through-photographs-architectural-models-and-plans — ✅ fetch 200 ^f12
[^13]: Miller, M. (2014). *AD Classics: Los Manantiales / Felix Candela*. ArchDaily. https://www.archdaily.com/496202/ad-classics-los-manantiales-felix-candela — ⚠️ snippet ^f13
[^14]: Watkins, K. (2020). *Spotlight: Félix Candela*. ArchDaily. https://www.archdaily.com/591415/spotlight-felix-candela — ⚠️ snippet ^f14
[^15]: del Cueto, J. I., & Eisenschmidt, A. (2018). *Félix Candela's Concrete Shells: An Engineered Architecture for Mexico and Chicago* [brochure]. Gallery 400, UIC. https://gallery400.uic.edu/wp-content/uploads/2020/04/CS_brochure_final.pdf — ⚠️ snippet PDF ^f15
[^16]: Paton, C. (s.f.). *Félix Candela, The hyperbolic paraboloid (1958)*. The Textbook of Architecture. https://textbookofarchitecture.com/source/candela — ⚠️ snippet ^f16
[^17]: Galindo Díaz, J., Salazar Marulanda, C., & Escobar García, D. (2018). *El legado de Félix Candela en Colombia a través de seis proyectos inéditos*. Arquitetura Revista, 14(1), 17-28. https://www.redalyc.org/journal/1936/193656124002/193656124002.pdf — ⚠️ snippet PDF ^f17
[^18]: Álvarez-Dorado, M., Fernández-Vega, D., & Morón-Fernández, C. (2022). *Estudio comparativo de estructuras ligeras en la arquitectura moderna: Eladio Dieste vs Félix Candela*. Anales de Edificación, 8(1). https://polired.upm.es/index.php/anales_de_edificacion/article/view/5015 — ⚠️ snippet ^f18
[^19]: Columbia Wallach Gallery. (s.f.). *Felix Candela: 1910-2010*. https://www.cc.columbia.edu/cu/wallach/exhibitions/Felix-Candela.html — ⚠️ snippet ^f19

**Kresge / Saarinen**

[^20]: Plunkett, J. W., & Mueller, C. T. (2015). *Thin Concrete Shells at MIT: Kresge Auditorium and the 1954 Conference*. http://digitalstructures.mit.edu/files/2015-08/plunkett-mueller.pdf — ⚠️ snippet PDF ^f20
[^21]: Whitehead, R. P. (2018). *Portentous and Predictable: Eero Saarinen, Ammann & Whitney, and the Failures of Kresge Auditorium (1950-1955)*. Iowa State University. https://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=1143&context=arch_conf — ⚠️ snippet PDF ^f21
[^22]: MIT List Visual Arts Center. (s.f.). *Kresge Auditorium, 1955*. https://listart.mit.edu/art-artists/kresge-auditorium-1955 — ⚠️ snippet ^f22

**Dieste**

[^23]: UNESCO World Heritage Centre. (2021). *The work of engineer Eladio Dieste: Church of Atlántida*. https://whc.unesco.org/en/list/1612/ — ⚠️ snippet ^f23
[^24]: Adell Argilés, J. M. (1992). *Las bóvedas de la Atlántida*. Informes de la Construcción, 44(421). https://doi.org/10.3989/ic.1992.v44.i421.1316 — ⚠️ snippet ^f24
[^25]: Más-Guindal Lafarga, A. J., & Adell, J. M. (2005). *Eladio Dieste y la cerámica estructural en Uruguay*. Informes de la Construcción, 57(496). https://doi.org/10.3989/ic.2005.v57.i496.459 — ⚠️ snippet ^f25
[^26]: Álvarez Prozorovich, F. V. (1999). *Iglesia de Atlántida*. DPA (UPC). http://raco.cat/index.php/DPA/article/view/259797 — ⚠️ snippet ^f26
[^27]: CIC GBA. (s.f.). *La Iglesia de Cristo Obrero de Eladio Dieste. Caracterización y evaluación de los morteros y cerámicos*. https://digital.cic.gba.gob.ar/server/api/core/bitstreams/1f996995-29fd-4c13-9606-ecd872cea30d/content — ⚠️ snippet PDF ^f27
[^28]: Fitz, L. (2023). *Os casos das igrejas de Eladio Dieste em Atlántida e Durazno*. UFRGS Propar. https://www.ufrgs.br/propar/wp-content/uploads/2023/11/24-Leonardo-Fitz.pdf — ⚠️ snippet PDF ^f28
[^29]: Corres Melachos, F., et al. (2023). *The architectural geometry of the Church of Cristo Obrero y Nuestra Señora de Lourdes*. ISPRS Archives. https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1059-2023 — ⚠️ snippet ^f29

**Otto / tensadas**

[^30]: Songel Gonzalez, J. M. (2022). *Tents: a paradigm of lightness and sustainability in vernacular architecture and in Frei Otto's work*. JCHMSD, 12(2), 171-191. https://doi.org/10.1108/JCHMSD-05-2021-0097 — ⚠️ snippet PDF ^f30
[^31]: Boller, G., & D'Acunto, P. (2021). *Structural design via form finding: Comparing Frei Otto, Heinz Isler and Sergio Musmeci*. https://doi.org/10.1201/9781003173434-168 — ⚠️ snippet ^f31
[^32]: Songel González, J. M. (2023). *Frei Otto: Light Structures Inspired by Nature*. https://doi.org/10.1007/978-3-031-33144-2_3 — ⚠️ snippet ^f32
[^33]: Goldsmith, N. (2016). *The physical modeling legacy of Frei Otto*. International Journal of Space Structures. https://ftlstudio.com/wp-content/uploads/2016/05/International-Journal-of-Space-Structures-2016-Goldsmith-0266351116642071.pdf — ⚠️ snippet PDF ^f33
[^34]: Universität Stuttgart. (s.f.). *Stuttgart Incentives — Institute for Lightweight Structures*. https://www.uni-stuttgart.de/universitaet/profil/historie/impulse/imp/alles.php_id_6_lang_en.html — ⚠️ snippet ^f34
[^35]: Tomlow, J. (2016). *Designing and constructing the Olympic roof (Munich 1972)*. International Journal of Space Structures. https://doi.org/10.1177/0266351116642078 — ⚠️ snippet ^f35
[^36]: schlaich bergermann partner. (s.f.). *Roof for Munich Olympic Stadium 1972*. https://www.sbp.de/en/project/roof-for-munich-olympic-stadium-1972/ — ⚠️ snippet ^f36
[^37]: Olympiapark München. (s.f.). *Tent Roof*. https://olympiapark.muenchen.de/en/olympiapark/zeltdach.html — ⚠️ snippet ^f37
[^38]: Glaeser, L. (1972). *The work of Frei Otto* [catálogo MoMA]. https://www.moma.org/documents/moma_catalogue_2757_300299029.pdf — ⚠️ snippet PDF ^f38
[^39]: Schmid, V. P., & Weber, B. (s.f.). *The experiments on measurement models for the Munich Olympic site*. https://api.taylorfrancis.com/content/chapters/oa-edit/download?identifierName=doi&identifierValue=10.1201%2F9781003173359-81 — ⚠️ snippet PDF ^f39
[^40]: Hollyday, J. (s.f.). *Form Finding for Anticlastic Membrane Structures*. https://bigwalls.net/download/membrane.pdf — ⚠️ snippet PDF ^f40
[^41]: BTES UMass. (s.f.). *Otto's Pneumatic Experiments*. https://openpublishing.library.umass.edu/btes/article/516/galley/466/download/ — ⚠️ snippet PDF ^f41
[^42]: freiotto.com. (s.f.). *Netzkonstruktionen*. https://freiotto.com/Netzkonstruktionen.html — ⚠️ snippet ^f42
[^43]: Pino, F. G. (2016). *Centro Multiusos en Mannheim. Frei Otto. Doblando la malla hasta hacer una concha*. https://doi.org/10.24192/2386-7027(2016)(v5)(06) — ⚠️ snippet ^f43

**Sagrada Família actual**

[^44]: Arup. (s.f.). *Sagrada Familia*. https://www.arup.com/en-us/projects/sagrada-familia/ — ⚠️ snippet ^f44
[^45]: Ferguson, H. (s.f.). *Completing the Sagrada Família*. Ingenia, Royal Academy of Engineering. https://www.ingenia.org.uk/articles/completing-the-sagrada-familia/ — ⛔ 403 al fetch; contenido citado de snippet ^f45
[^46]: Henriques, M. (2026). *The ancient engineering marvels of the world's tallest church*. BBC Future. https://www.bbc.com/future/article/20260608-sagrada-famlia-the-ancient-engineering-marvels-of-the-worlds-tallest-church — ⚠️ snippet ^f46
[^47]: McFarland, P. (2026). *Spain's Sagrada Familia: Contemporary Construction Methods Speed Iconic Basilica to Completion*. ENR. https://www.enr.com/articles/62506-spains-sagrada-familia-contemporary-construction-methods-speed-iconic-basilica-to-completion — ⚠️ snippet ^f47
[^48]: Sánchez Domínguez, M. (2026). *BIM in Ongoing Heritage Construction: The case of the Sagrada Família* [entrevista a Esteve Umbert]. IAAC Blog. https://blog.iaac.net/bim-in-ongoing-heritage-construction-the-case-of-the-sagrada-familia-a-conversation-with-esteve-umbert/ — ⚠️ snippet ^f48
[^49]: Lorente, B. (2026). *The central towers at the Sagrada Familia*. Rhino World 2026. https://rhino3d.world/talk/talk-sagrada-familia/ — ⚠️ snippet ^f49
[^50]: Makert, R., & Alves, G. M. (2017). *Between Designer and Design: Parametric Design and Prototyping Considerations on Gaudí's Sagrada Familia*. Periodica Polytechnica Architecture. https://doi.org/10.3311/ppar.10335 — ⚠️ snippet ^f50

**Form-finding digital**

[^51]: Wintour, P. (2015). *Catenary curves and membranes in Grasshopper*. Parametric Monkey. https://parametricmonkey.com/2015/10/10/catenary-curves/ — ⚠️ snippet ^f51
[^52]: Building Simplexity Lab, HKU. (2022). *Catenary Lines (Kangaroo 2)*. https://bsl.hku.hk/tutorials/physics-simulation-structural-analysis/kangaroo-2/catenary-lines/ — ⚠️ snippet ^f52
[^53]: TU Delft. (s.f.). *Generative Form Finding with Kangaroo Physics* [open textbook]. https://interactivetextbooks.tudelft.nl/rhino-grasshopper/Grasshopper_Rhino_course/2_Knowledge_base/Generative_Design/Generative_Form_Finding/!index.html — ⚠️ snippet ^f53
[^54]: Kang, T., & Kim, D. (2016). *Design Programming of Catenary Shell Using Grasshopper Script*. ICCCBE 2016. http://www.see.eng.osaka-u.ac.jp/seeit/icccbe2016/Proceedings/Full_Papers/011-050.pdf — ⚠️ snippet PDF ^f54
[^55]: Leung, N. (2018). *The Nature of Gridshell Form Finding*. WeWantToLearn.net. https://wewanttolearn.net/2018/03/13/the-nature-of-gridshell-form-finding/ — ⚠️ snippet ^f55
[^56]: Nanayakkara, K. I. (2018). *Shell Structures from Catalan to Mapungubwe* [premio PaiLin Li]. IStructE. https://www.istructe.org/IStructE/media/Public/PaiLinLiAward-2018-Candidate-Report-KIUNanayakkara.pdf — ⚠️ snippet PDF ^f56
[^57]: Kudless, A. (2012). *Shellstar Pavilion*. Matsys. https://www.matsys.design/shellstar-pavilion — ✅ fetch 200 ^f57
[^58]: Popescu, M., Rippmann, M., Liew, A., Van Mele, T., & Block, P. (2019). *Concrete shell made of steel cables and knitted formwork (KnitCandela)*. DETAIL. https://www.detail.de/de_de/concrete-shell-made-of-steel-cables-and-knitted-formwork — ⛔ 410 al fetch (recurso eliminado); contenido de snippet archivado en el crudo ^f58

**Escala urbana**

[^59]: Walter P Moore. (s.f.). *MARS Pavilion*. https://www.walterpmoore.com/projects/mars-pavilion — ⚠️ snippet ^f59
[^60]: uau studio. (s.f.). *Shell in the Park*. https://www.uau-studio.com/project/shell-in-the-park — ⚠️ snippet ^f60
[^61]: 3osi. (s.f.). *Boves Kiosk 1*. https://3osi.com/projects/boves-kiosk-1/ — ⚠️ snippet ^f61
[^62]: Veselova, S., & Vohra, G. (2024). *GAUDI'S CAT*. IAAC Blog. https://blog.iaac.net/gaidis-ca/ — ⚠️ snippet ^f62
[^63]: Barberio, M. (2024). *Catenary Symphonies* [post]. LinkedIn. https://www.linkedin.com/posts/mauriziobarberio_catenary-symphonies-is-a-project-for-a-3d-printed-activity-7176930130710183936-PyZy — ⚠️ snippet ^f63
[^64]: Cano, P. (2022). *The 9th Edition of the MPavilion, Designed by Bangkok-Based Studio All(zone), Opens in Melbourne*. ArchDaily. https://www.archdaily.com/993571/the-9th-mpavilion-designed-bangkok-based-studio-all-zone-opens-in-melbourne-australia — ⚠️ snippet ^f64
[^65]: Tensinet. (s.f.). *Tachkemoni canopies*. https://tensinet.com/index.php/projects-database/projects/4754 — ⚠️ snippet ^f65
[^66]: Tensil.bg. (2013). *Saddle-Shaped Membrane Canopy Playground in Oryahovo*. https://tensil.bg/en/projects/membranes/membrane-playground/ — ⚠️ snippet ^f66
[^67]: Abdel, H. (2024). *Shade School Playground Pavilion / Blue Temple*. ArchDaily. https://www.archdaily.com/1019040/shade-school-playground-pavilion-blue-temple — ⚠️ snippet ^f67
[^68]: Abdel, H. (2021). *Cloud Forests Pavilion for Children's Play / UNITEDLAB Associates*. ArchDaily. https://www.archdaily.com/966076/cloud-forests-pavilion-for-childrens-play-unitedlab-associates — ⚠️ snippet ^f68
[^69]: OZ.E.TECTURE. (s.f.). *MPavilion (Glenn Murcutt, 2019)*. https://www.ozetecture.org/mpavilion — ⚠️ snippet ^f69
[^70]: Serna, I. (2018). *Del hueso a la piel*. Arquitectura Viva. https://arquitecturaviva.com/articulos/del-hueso-a-la-piel — ⚠️ snippet ^f70

## Referencias (bibliografía y repos oficiales)

Documentación original y repositorios oficiales de los autores y obras tratados. Misma fecha de consulta (2026-10-30) y mismas marcas de confianza.

- **Gaudí**: Gaudí Museum (método, geometría, superficies regladas) — https://gaudi.museum/ ✅ [[#^f1|1]]; Junta Constructora del Temple Expiatori de la Sagrada Família, booklet oficial — https://sagradafamilia.org ⚠️ [[#^f11|11]]; Consorci de la Colònia Güell — https://www.lacoloniaguell.cat ✅ [[#^f2|2]]; Fundación Antonio Gaudí — https://fundacionantoniogaudi.org ⚠️ [[#^f6|6]].
- **Candela**: Gallery 400 (UIC), brochure de la exposición *Félix Candela's Concrete Shells* (del Cueto & Eisenschmidt) — https://gallery400.uic.edu/wp-content/uploads/2020/04/CS_brochure_final.pdf ⚠️ [[#^f15|15]]; Columbia Wallach Gallery, *Felix Candela: 1910-2010* — https://www.cc.columbia.edu/cu/wallach/exhibitions/Felix-Candela.html ⚠️ [[#^f19|19]].
- **Dieste**: UNESCO World Heritage Centre, ficha de inscripción de Cristo Obrero (2021) + documento de nominación (whc.unesco.org/document/189224) — https://whc.unesco.org/en/list/1612/ ⚠️ [[#^f23|23]]; *Informes de la Construcción* (CSIC), artículos de Adell 1992 y Más-Guindal & Adell 2005 (DOIs 10.3989/ic.1992.v44.i421.1316 y 10.3989/ic.2005.v57.i496.459) ⚠️ [[#^f24|24]][[#^f25|25]]; CIC Provincia de Buenos Aires, estudio de morteros y cerámicos (plan Getty *Keeping It Modern*) ⚠️ [[#^f27|27]].
- **Frei Otto**: sitio oficial del legado — https://freiotto.com ⚠️ [[#^f42|42]]; Universität Stuttgart, Institut für Leichte Flächentragwerke (IL) — https://www.uni-stuttgart.de/universitaet/profil/historie/impulse/imp/alles.php_id_6_lang_en.html ⚠️ [[#^f34|34]]; Glaeser, L. (1972), *The work of Frei Otto*, catálogo MoMA — https://www.moma.org/documents/moma_catalogue_2757_300299029.pdf ⚠️ [[#^f38|38]]; schlaich bergermann partner (ingeniería de Múnich 72) — https://www.sbp.de ⚠️ [[#^f36|36]].
- **Cáscaras (teoría clásica)**: Timoshenko, S. & Woinowsky-Krieger, S., *Theory of Plates and Shells* — clásico de referencia citado por la literatura del campo; **sin URL verificada en esta pasada** (candidato a agregar en segunda pasada). Formalización alemana de las cáscaras años 20: Dischinger y Finsterwalder, citados vía [[#^f20|20]].
- **Form-finding digital**: Block Research Group (ETH Zürich) — RhinoVault, Armadillo Vault, KnitCandela, Ideas City Pavilion (referencias vía [[#^f56|56]][[#^f58|58]]); Kangaroo (plugin de Grasshopper) — tutoriales oficiales de HKU Building Simplexity Lab [[#^f52|52]] y TU Delft [[#^f53|53]].
- **Papers clave de acceso abierto**: Plunkett & Mueller 2015 (MIT, Kresge) [[#^f20|20]]; Nanayakkara 2018 (IStructE, bóveda catalana→RhinoVault) [[#^f56|56]]; Galindo Díaz et al. 2018 (Redalyc, Candela en Colombia) [[#^f17|17]]; Kang & Kim 2016 (ICCCBE, Isler digital) [[#^f54|54]].

## Otros links de interés

Extra del material crudo, agrupados por uso potencial. Todos provienen del crudo de @sherlock; se indica confianza.

**Tutoriales Kangaroo/Grasshopper que replican a Gaudí/Isler**

- Parametric Monkey — *Catenary curves and membranes in Grasshopper* (componente nativo vs Kangaroo, membranas catenarias, estructuras anidadas): https://parametricmonkey.com/2015/10/10/catenary-curves/ ⚠️ [[#^f51|51]]
- HKU Building Simplexity Lab — *Catenary Lines (Kangaroo 2)* (receta paso a paso): https://bsl.hku.hk/tutorials/physics-simulation-structural-analysis/kangaroo-2/catenary-lines/ ⚠️ [[#^f52|52]]
- TU Delft — *Generative Form Finding with Kangaroo Physics* (open textbook): https://interactivetextbooks.tudelft.nl/rhino-grasshopper/Grasshopper_Rhino_course/2_Knowledge_base/Generative_Design/Generative_Form_Finding/!index.html ⚠️ [[#^f53|53]]
- Kang & Kim 2016 — script que reproduce el método de Isler (Grasshopper+Kangaroo+WeaverBird→SAP2000): http://www.see.eng.osaka-u.ac.jp/seeit/icccbe2016/Proceedings/Full_Papers/011-050.pdf ⚠️ [[#^f54|54]]
- WeWantToLearn — *The Nature of Gridshell Form Finding* (gridshell colgado+espejado): https://wewanttolearn.net/2018/03/13/the-nature-of-gridshell-form-finding/ ⚠️ [[#^f55|55]]

**Maqueta/workflow digital de la Sagrada Família**

- Rhino World 2026 — charla oficial del equipo sobre las torres centrales (de arcos catenarios a polifuniculares form-finding): https://rhino3d.world/talk/talk-sagrada-familia/ ⚠️ [[#^f49|49]]
- IAAC Blog — entrevista a Esteve Umbert sobre BIM de piedra (Rhino+atributos → Revit → mock-ups 1:1): https://blog.iaac.net/bim-in-ongoing-heritage-construction-the-case-of-the-sagrada-familia-a-conversation-with-esteve-umbert/ ⚠️ [[#^f48|48]]

**Pabellones y casos urbanos**

- MARS Pavilion (catenaria invertida robótica, Palm Springs 2017): https://www.walterpmoore.com/projects/mars-pavilion ⚠️ [[#^f59|59]]
- MPavilion 2022 (all(zone), membranas de 3 capas): https://www.archdaily.com/993571/the-9th-mpavilion-designed-bangkok-based-studio-all-zone-opens-in-melbourne-australia ⚠️ [[#^f64|64]] · MPavilion Murcutt 2019: https://www.ozetecture.org/mpavilion ⚠️ [[#^f69|69]]
- Shellstar Pavilion (Matsys, stand de feria con Kangaroo): https://www.matsys.design/shellstar-pavilion ✅ [[#^f57|57]]
- Shell in the Park (kioscos modulares, Varna): https://www.uau-studio.com/project/shell-in-the-park ⚠️ [[#^f60|60]] · Boves Kiosk (impresión 3D): https://3osi.com/projects/boves-kiosk-1/ ⚠️ [[#^f61|61]]
- GAUDI'S CAT (IAAC, pabellón de catenarias impresas): https://blog.iaac.net/gaidis-ca/ ⚠️ [[#^f62|62]]
- Canopies Tachkemoni (membranas hypar escolares): https://tensinet.com/index.php/projects-database/projects/4754 ⚠️ [[#^f65|65]] · Playground Oryahovo: https://tensil.bg/en/projects/membranes/membrane-playground/ ⚠️ [[#^f66|66]] · Blue Temple Yangón: https://www.archdaily.com/1019040/shade-school-playground-pavilion-blue-temple ⚠️ [[#^f67|67]] · Cloud Forests Corea: https://www.archdaily.com/966076/cloud-forests-pavilion-for-childrens-play-unitedlab-associates ⚠️ [[#^f68|68]]

**Eventos y recursos**

- Detour 2012 (evento donde se montó el Shellstar, Wan Chai, Hong Kong) — vía ficha Matsys [[#^f57|57]]
- Conferencia MIT de cáscaras, junio 1954 (Candela, Tedesko, Philip Johnson presentes) — narrada en [[#^f20|20]]
- Programa MPavilion (pabellón anual donado a la ciudad de Victoria) — vía [[#^f64|64]][[#^f69|69]]
- Premio PaiLin Li de IStructE (reporte Nanayakkara, PDF abierto con dibujos de bóveda catalana→RhinoVault): https://www.istructe.org/IStructE/media/Public/PaiLinLiAward-2018-Candidate-Report-KIUNanayakkara.pdf ⚠️ [[#^f56|56]]
- PDFs abiertos para descarga directa: MIT Kresge [[#^f20|20]], Redalyc Candela-Colombia [[#^f17|17]], Goldsmith IJSS (legado de modelos físicos de Otto) [[#^f33|33]], Hollyday (form-finding de membranas) [[#^f40|40]], CIC GBA (Dieste, morteros) [[#^f27|27]], UFRGS (Dieste, iglesias) [[#^f28|28]].

## Registro HITL

### Qué aprendió SOL (síntesis)

- **Una idea, dos materiales**: el form-finding físico (colgar, fotografiar, invertir) es el mismo algoritmo en Gaudí (1898-1914), Otto (jabón y redes, 1950s-70s) e Isler (telas congeladas, 1960s) — y hoy corre en Kangaroo dentro de Rhino. El estudio ya tiene el pipeline: solo falta conectarlo con la catenaria.
- **La forma ES el cálculo**: la catenaria funciona porque no hay separación entre dibujo y estructura; Kresge falla porque la forma se impuso («make it work») y el borde libre deflectó. Criterio de diseño transferible: toda forma curva del estudio debe justificarse por su línea de empujes.
- **Superficies regladas = constructibilidad**: hiperboloide, hypar y conoide son curvos pero se encofran con tablas rectas — la clave económica de Gaudí y Candela. La regla luz/espesor de Candela (400-1000) da un sanity check instantáneo.
- **Dieste es la línea relevante para Argentina**: ladrillo + mano de obra local + economía de encofrado; Atlántida es UNESCO 2021 y el CIC bonaerense ya estudió sus materiales (Getty). La bóveda gausa es catenaria en ladrillo.
- **Múnich 72 como lección de proceso**: 50.000 horas de modelos físicos + el primer cálculo computacional iterativo (Argyris/Linkwitz) — el híbrido físico-digital es el patrón, no la excepción.
- **La Sagrada Família valida el workflow del estudio**: Rhino+Grasshopper → impresión 3D de maquetas → Rhino con atributos como BIM → Revit → mock-ups 1:1. Es el mismo pipeline a escala monumental, con fecha de cierre 2026 (torre de Jesús, 172,5 m).
- **Escala urbana = puerta de entrada**: el primer encargo público de Gaudí fue mobiliario (farolas, 1878-79); hoy la escala pequeña es de membranas tensadas (MPavilion, canopies escolares) y cáscaras modulares (MARS, Varna) — terreno natural para prototipos del estudio.

### Gaps de investigación

- **Cache vacío**: `raw/research-cache/` no tiene archivos de esta pasada — toda la confianza proviene del fetch directo (5 URLs) vs snippets (64). Las afirmaciones de snippet son citables pero conviene fetch de verificación antes de citarlas en documentos externos.
- **Corpus italiano sin cubrir (IT gap)**: Barberio/Fallacara (Catenary Symphonies, estereotomía digital) y Nervi quedaron solo por snippets en EN/LinkedIn. Candidato a segunda pasada dedicada.
- **Asientos urbanos catenarios contemporáneos**: corpus débil (solo el banco del Park Güell como histórico). Segunda pasada sugerida: `site:archdaily.com bench shell canopy`.
- **KnitCandela (DETAIL 2019) dio 410**: buscar copia alternativa en el sitio del Block Research Group (ETH) o ArchDaily.
- **Ingenia (Sagrada Família) dio 403**: contenido citado de snippet; buscar copia o versión archivada si se cita en externos.
- **Discrepancias abiertas reportadas**: escala de la maqueta (1:10 Gaudí Museum/Consorci vs 1:15 Wikipedia); superficie de Múnich (74.000 m² sbp vs 78.000 m² Olympiapark; 34.000 m² solo estadio MoMA); arcos de Casa Milà (catenarios vs parabólicos según la fuente).
- **Timoshenko** (*Theory of Plates and Shells*): clásico teórico ausente del corpus — agregar en segunda pasada si se desarrolla la ficha de cáscaras.
- **Normativa AR**: estructuras tensadas en CABA/Argentina, fuera del alcance de esta búsqueda.

### Propuesta de 8 fichas wiki (pendiente del `s` de SOL)

| # | Ficha propuesta | Destino | Alcance (1 línea) | Alimentada por |
|---|---|---|---|---|
| 1 | `catenaria-funicular.md` | `wiki/glosario/conceptos/` | Catenaria vs parábola, maqueta polifunicular, tracción→compresión invertida, Gaudí→Otto→Kangaroo | Secciones [[#Catenarias y funiculares: el método Gaudí]] + [[#Form-finding digital: Kangaroo y el pipeline del estudio]] |
| 2 | `form-finding.md` | `wiki/glosario/conceptos/` | Físico (Gaudí, Otto, Isler) → digital (Kangaroo, RhinoVault, patterning) | [[#Form-finding digital: Kangaroo y el pipeline del estudio]] + [[#Estructuras tensadas: Frei Otto y Múnich 72]] |
| 3 | `cascaras-hormigon.md` | `wiki/glosario/conceptos/` | Cáscara/membrana, regla luz/espesor, superficies regladas, Kresge como contraejemplo, Maya Somaiya como presente | [[#Cáscaras de hormigón: Candela, Isler y el contraejemplo Kresge]] |
| 4 | `estructuras-tensadas.md` | `wiki/glosario/conceptos/` | Membranas, cable-net, neumáticos, patterning, casos urbanos (MPavilion, canopies escolares) | [[#Estructuras tensadas: Frei Otto y Múnich 72]] + [[#Escala urbana: farolas, asientos, juegos, stands, kioscos y pabellones]] |
| 5 | `gaudi-escala-urbana.md` | `wiki/glosario/conceptos/` | Farolas Plaça Reial/Pla de Palau, banco Park Güell, el mobiliario como primer encargo público | [[#Escala urbana: farolas, asientos, juegos, stands, kioscos y pabellones]] |
| 6 | `felix-candela.md` | `wiki/glosario/referentes/` | Hypar, Cubiertas Ala, Los Manantiales, regla 400-1000, KnitCandela como homenaje | [[#Cáscaras de hormigón: Candela, Isler y el contraejemplo Kresge]] |
| 7 | `eladio-dieste.md` | `wiki/glosario/referentes/` | Cerámica armada, bóveda gausa, Atlántida UNESCO, vínculo Gaudí/bóveda catalana — relevancia AR directa | [[#Dieste y la cerámica armada: la catenaria en ladrillo]] |
| 8 | `frei-otto.md` | `wiki/glosario/referentes/` | Superficies mínimas, cable-net Múnich 72, reconstrucción de la maqueta de Gaudí (Stuttgart 1982), Pritzker 2015 | [[#Estructuras tensadas: Frei Otto y Múnich 72]] |

Las fichas se crearían vía @vaultworm-arq (dueño de `wiki/glosario/`) con su propio `s`; este documento queda como fuente curada en `wiki/fuentes/` tras el OK de SOL. Relación con la wiki existente: la ficha de form-finding enlazaría con [[wiki/glosario/conceptos/bim-metodologia|BIM metodología]] y el hub [[wiki/glosario/00-index|glosario]].

### Nota de formato

2026-10-30: primera pasada con footnotes `[^NN]`; **no renderizan en este vault** (el plugin core Footnotes está roto — ver [[raw/sessions/2026-09-28-sesion-fuentes-wikilinks|sesión 2026-09-28]]). Solución aplicada (la validada entonces): citas como **block references de Obsidian** `[[#^fNN|NN]]` con ancla `^fNN` al final de cada definición al pie — el clic salta a la fuente y muestra el número. Feedback SOL.

---

**Estado:** pendiente de OK de SOL → al aprobar, @contenidos mueve esta ficha a `wiki/fuentes/gaudi-catenarias-cascaras-tensadas-sherlock.md` (protocolo mover-borrar) y las 8 fichas pasan a @vaultworm-arq.
