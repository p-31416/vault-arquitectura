---
tipo: proyecto
proyecto: concurso-gaudi-nexus
titulo: Programa punto a punto — superficies, aforos y plaza
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
estado: borrador-activo
tags: [concurso, gaudi-nexus, programa, superficies, aforos, plaza]
idioma: es
---

# Programa punto a punto — superficies, aforos y plaza

> Fuente: `G:\Mi unidad\OS-Emilia\AIxGaudi\GxAI_BRIEFING_ES.pdf` § programa. Aforos y superficies **orientativos**, solo para dimensionar escala. Edificio total **1500–2000 m²**. Detalle briefing en [[proyectos/concurso-gaudi-nexus/02-briefing-punto-a-punto|02-briefing-punto-a-punto]]. Reinterpretación fractal vigente en [[proyectos/concurso-gaudi-nexus/reinterpretacion-programa-fractal|reinterpretacion-programa-fractal]].
> Estado: borrador activo para iterar con Emilia.

## 0. Tabla madre (triple hipótesis Sol + % plaza)

| Pieza | % | m² sobre 1500 | m² sobre 1750 | m² sobre 2000 | Aforo orientativo | Criterio que la mira |
|-------|---|---------------|---------------|---------------|-------------------|----------------------|
| A Mercado + vecinal | 45% | 675 | 787.5 | 900 | 100 + 50 | 5.1 uso barrio |
| B Interpretación + mirador | 25% | 375 | 437.5 | 500 | 50 + 25 | 5.1 control recorridos |
| C Encuentro cocina | 15% | 225 | 262.5 | 300 | 2×20 | 5.1 convergencia |
| D Admin + logística + aseos | 15% | 225 | 262.5 | 300 | 8 puestos | 5.5 + 5.1 servicio |
| E Plaza completa | — | manzana 113.3 m + chaflanes 20 m (~12.000–12.400 m² est.) | idem | idem | abierto | 5.2 integración |
| **Total construido** | 100% | **1500** | **1750** | **2000** | **~265 interior + plaza** | 100 pts |

> % sobre plaza (estimación para Rhino, a verificar con massing `earth2rhino3d`): 1500 ≈ 12.1–12.5% / 1750 ≈ 14.1–14.6% / 2000 ≈ 16.1–16.7% de la manzana. Base cálculo: 113.3² = 12.837 m² menos 4 recortes chaflán (400–800 m² según se mida chaflán 20 m como cateto o hipotenusa).

## 1. A — Mercado y zona vecinal (45% = 675 / 787.5 / 900 m²)

| Sub-pieza | Qué pide | m² (1500 / 1750 / 2000) | Implicancia diseño |
|-----------|----------|------------------|-------------------|
| Zona mercado 20 puestos frescos proximidad | 100 pax | ~450–500 / ~525–575 / ~600–650 estimado | 20 puestos × ~10–12 m² + circulación 35%. Luz natural + ventilación olores (5.5). Acceso diario directo calle, sin pasar por turista |
| Zona vecinal flexible (reuniones, talleres jóvenes, clases adultos, conciertos/teatro barrio) | 50 pax interior + ≥100 exterior | ~175–225 / ~210–260 / ~250–300 interior + exterior poroso | Cáscaras catenaria invertida con condición acústica (música) + techo verde. Secuencia descubierto → semicubierto → cubierto. Interior 50 pax a 1.8–2.2 m²/pax; exterior por lo menos el doble de gente para dimensionar explanada |

> Sol dixit 2026-11-02: "Esa área que tiene 50 personas. Podemos decir que tiene que haber 50 personas adentro. Y que afuera tiene que haber por lo menos el doble. Entonces. Para poder dimensionar esa zona vecinal de reuniones y talleres. Porque estamos pensando, no sé, ahí veíamos que hacían música. Entonces que tenga un lugar que con estas que sean como estas cáscaras que tengan alguna cuestión acústica y que sean todas cáscaras de catenaria invertida y techo verde. [...] tres espacios. Descubierto. Semicubierto. y cubierto."

Puntos de control: accesibilidad diaria, comodidad compra, altura libre ≥3.5 m mercado, muelle logístico separado público. Cáscaras testeadas en WF-03 corte acústico.

## 2. B — Centro interpretación + mirador (25% = 375 / 437.5 / 500 m²)

| Sub-pieza | Qué pide | m² (1500 / 1750 / 2000) | Implicancia diseño |
|-----------|----------|------------------|-------------------|
| Expositivo Gaudí–IA (maquetas colgantes → IA paramétrica) | 50 pax bajo centro interpretación | ~250–275 / ~290–320 / ~330–370 estimado | Va abajo del centro interpretación, ganando "otra dimensión" al bajar 1 m. Brief autoriza no dar bola a lo de abajo = oportunidad enterrar. Penumbra + focos, narrativa cuerdas → nodos ComfyUI |
| Mirador templo — refutación Sol: no punto, recorrido | 25 pax simultáneos en recorrido | ~100–125 / ~115–145 / ~130–170 + recorrido | Varias zonas, no única: una de lejos para admirar obra completa + una de cerca para apreciar material = zoom fractal (Eames Powers of Ten / encuadres). Marcado por teselado triangular que se achica y agranda por módulos. Crudo Pasión + tensado |

> Sol dixit 2026-11-02: "Para mí el mirador no es un punto. Porque justamente, si no Gaudí hubiese puesto una sola visual, y él tiene muchas visuales. Que justamente está el documento ese de las diagonales que quería Gaudí. Entonces, para mí, el mirador es un recorrido. [...] podría estar marcado por estos teselados triangulares [...] fractales. Porque además también se tienen que ir haciendo más chiquitos y más grandes. Justamente por módulos."
> "Centro de interpretación [...] como otra de esas cáscaras. [...] se entra bajando unos niveles. Un metro. [...] empieza a tener como otra dimensión. Total, dijeron que no le demos bola a lo de abajo."
> "El espacio expositivo [...] es lo que va a estar abajo de ese centro de interpretación."
> "Una de lejos para poder admirar toda la obra. Y una de cerca para apreciar el material. Entonces, eso es un zoom. [...] como los fractales [...] de sus encuadres. O en el [...] video [...] del zoom escala. [...] varios encuadres que hagan honor a la obra de Gaudí. [...] lo mío, crudo."

Puntos de control: flujo turista gestionado (5.1), soporta grupo 25 + guía en estaciones, barandilla/óculo a altura ojos + dron para doble lectura. Documento diagonales Gaudí como cita en A1.

## 3. C — Punto encuentro (15% = 225 / 262.5 / 300 m²)

| Sub-pieza | Qué pide | m² (1500 / 1750 / 2000) | Implicancia diseño |
|-----------|----------|------------------|-------------------|
| Taller cocina 2 cocinas completas independientes, 20 pax c/u | 40 pax cocinando + público | 225 / 262.5 / 300 | 2×~50–60 m² cocina + 120–180 m² degustación/compartir según hipótesis. Puede resolverse como otro lugarcito cerrado con bóvedas, más chico que vecinal. Extracción reforzada, acústica, vista a mercado |

> Sol dixit 2026-11-02: "Quiero que calcules cuánto es el 45, el 25, el 15 [...] en base al 1500, 1750 y 2000. Área con dos cocinas. [...] podría ser otro más chiquitito de estos lugares cerrados. Con bóvedas."

Punto de control: es la prueba de Nexus. Si cocina queda residual, se pierde criterio convergencia 5.1.

## 4. D — Administración, logística y servicios (15% = 225 / 262.5 / 300 m²)

| Sub-pieza | Qué pide | m² (1500 / 1750 / 2000) | Implicancia diseño |
|-----------|----------|------------------|-------------------|
| Oficina diáfana vidrio 8 puestos | 8 | ~80–100 en las 3 hipótesis | Lugar cerrado de vidrio, moderno y abierto, con equipamiento teselado que encastra. Ubicación en intersección en T entre recorrido mercado y recorrido adoración Sagrada Familia |
| Logística: almacén, mantenimiento, instalaciones | — | resto D ~80–120 | Donde queden lugares / intersticios. Flujo sucio separado, cuartos UTA/filtrado olores/ruido |
| Aseos públicos todo aforo | ~265 + plaza | ~40–60 | Acceso desde plaza sin entrar a salas |

> Sol dixit 2026-11-02: "La oficina va a ser un lugar cerrado de vidrio. Donde haya unos trabajando. [...] con también unos equipamientos con forma de teselado que encastren unos con otros. Y trabajan ahí de una manera muy moderna y abierta. Y ese va a ser el espacio diáfano. Que justamente tiene que estar en la intersección entre lo que es la parte del recorrido que forma una T con la plaza del mercado y el recorrido de la adoración a la sagrada familia."
> "Zona de logística. Bueno, eso después lo vemos. Donde nos quedan lugares."

## 5. E — Entorno urbano (plaza completa) + puente Gaudí y sutura parques

- No objeto aislado. Reconfiguración total manzana Cerdà con libertad: niveles, elevar para vistas, hundir parcial (museo bajo cáscara según precepto fractal).
- Lengua mirador-recorrido que retoma el puente planteado por Gaudí: pasa por la fachada acceso que él planteó, cruza y llega hasta fachada Nacimiento. Une las tres fachadas sin invadir: solo piso lo más fino posible con patrón.
- Sutura de los dos parques / lados con pieza no invasiva: estereoestructura ramificada biomímica, escultórica, vidrio, que pasa desapercibida.
- Debe unificar plaza + edificio (5.2), alinear trama Cerdà/Eixample + escala residencial, preservar dominio visual Pasión.
- Verde + SUDS + solado drenante + accesibilidad 1–2% como parámetros generación (ver [[proyectos/concurso-gaudi-nexus/reinterpretacion-programa-fractal|reinterpretacion-programa-fractal]] §6).

> Sol dixit 2026-11-02: "Ahí quiero algo que tenemos que hacer con el puente que había planteado Gaudí. [...] una de estas lenguas de recorrido mirador pase por la fachada [...] que había planteado Gaudí como acceso. Y que te haga un cruce y que llegue hasta la fachada del nacimiento."
> "Deberás proponer reconfiguración de toda la plaza [...] justamente unir esas tres fachadas con algo que no sea invasivo, que sea solo un piso lo más fino posible. Que tenga algún patrón [...] y que después [...] conecte estos dos parques. [...] puede ser [...] tipo [...] estereoestructura [...] ramificada. Que ahí representás como la biomímica. Y que pueda ser [...] una pieza escultórica que pase desapercibida con vidrio."

## 6. Cruce programa × principios Gaudí (P1-P10)

- A mercado: P3 ventilación pasiva olores, P6 jerarquía cargas luces amplias, P9 material común + trencadís.
- B expositivo: P5 geometría reglada catenarias, P4 forma = fuerzas.
- C cocina: P10 ergonomía 2 cocinas 20 pax, P7 biosincronización (residuo → compost verde plaza).
- D logística: P8 adaptarse terreno, enterrar sin excavar agresivo.
- E plaza: P2 biomimética funcionamiento, P8 material zona, P3 sol/viento.

## 7. Estrategia Sol — dictado 2026-11-02 (precepto rector reinterpretación)

> Todo lo de esta sección es cita directa de Sol, transcripta como precepto de diseño. Se conserva su voz para trazabilidad en lámina A1.

### 7.1 Reinterpretar para distinguirse

> "Yo me caractericé toda mi vida por reinterpretar el programa a mi antojo. ¿Y por qué? Porque eso también te da una distinción frente a todos [los] proyectos que están haciendo exactamente el mismo programa."
> "El texto del briefing dice que está a libre interpretación del participante."
> "Es un proyecto totalmente volado, que es un experimento social para ver cómo los arquitectos usan la IA."

Implicancia: usar libertad volumétrica §2.2 + superficies orientativas como cobertura contractual para mover % sin romper bases. La distinción se juega en piso + puestos + vecinal escalonado, no en m².

### 7.2 Superficies orientativas = margen

> "Los aforos y superficies son orientativos. ¿Qué quiere decir? Que si te pasás un poco o es un poco menos para la idea, está bien."

Decisión: dimensionar en Rhino triple hipótesis 1500 / 1750 / 2000 y elegir la que sostenga la idea, manteniendo proporciones A 45 / B 25 / C 15 / D 15 como tablita rápida (§0).

### 7.3 Corazón social a escala feriante, con vértices

> "El nuevo corazón social del barrio. Entonces [...] mercado, el tipo de mercado de feriantes. [...] tiene que tener una escala. No puede ser algo totalmente fuera de escala, porque justamente es para la parte social del barrio. Entonces, yo por social entiendo que tiene que tener vértices. [...] para que en esos vértices del camino funcione. [...] como lo queremos poner en el sentido de circulación del barrio, en el único sentido que no va a haber una conexión directa, es a la sagrada familia, justamente porque Gaudí decía que no quería vistas ortogonales."

Reglas que fija:
- Escala feriante doméstica, no monumental.
- Vértices = nodos de encuentro sobre el camino, en sentido circulación barrial.
- Sin eje ortogonal directo a Sagrada Familia (precepto Gaudí según Sol). El templo se conquista en escorzo / mirador, no en eje.

### 7.4 Piso fractal triangular trencadís contemporáneo

> "En ese paseo, yo veo [...] un piso que sean como mosaico fractales. Me imaginaba piezas triangulares, que a su vez esas piezas triangulares están divididas en tres partes y cada una de ellas tiene diferente color, como para honrar el trencadís tradicional de Barcelona, y la parte manual, pero como se traduciría, eso fue en determinado tiempo y espacio."

Especificación:
- Tesela base triangular, subdividida en 3 subtriángulos de distinto color (homenaje manual trencadís traducido a tiempo presente).
- Tres colores simbolizan las tres fachadas: Nacimiento / Pasión / Gloria.
- Multi-escala: triangulitos a diferente escala para que el piso crezca, tenga movimiento y mapee flujos — "siendo cuadrados no tendrían" ese movimiento.
- Teselado que arma vértices donde circulan y se agrupan puestos de distintas maneras.

### 7.5 Mano de obra y materiales: pieza que deja crecer pasto

> "La mano de obra y los materiales [...] tendría que ser una pieza, qué sé yo, biodegradable, que permita que crezca pasto por dentro y que no sea tan invasivo para el crecimiento del pasto, como pasa con hoy, que es un liso llano sin pasto, y que esas piezas además [...] impresas con una impresora de cemento, de materiales reciclables, [...] o [...] biodegradables."

Especificación:
- Pieza permeable/biodegradable o cemento reciclado impreso 3D, con alveolo que deja crecer pasto.
- Contraste con estado actual: "liso llano sin pasto".
- Junta ancha drenante + sustrato (enlace con SUDS §5 y techo verde museo).

### 7.6 Triángulo como estructura → techo puestos tensados austeros

> "Además, el triángulo también es una pieza fundamental de la estructura. Entonces, estructuralmente eso también se tendría que trasladar a lo que era ese techo que pensábamos para los puestos."
> "Quiero que conserve algo de lo crudo de la fachada de la pasión. Porque está en la fachada de la pasión. [...] Entonces quiero que combine eso con [...] una estructura tensada que quizás en ese momento no hubiese podido existir. Y que eso te arme [...] el puesto con un solo apoyo y que [...] puedan funcionar de a una o de a varias al mismo tiempo, como estructuras tensadas de los feriantes, [...] con materiales de última generación. [...] que sean muy austeros, que sean muy despojados. Puede ser que haya, no sé, tres tipos, entonces que vaya [...] representando [...] las diferentes fachadas."

Especificación:
- Puesto = mástil único + membrana tensada triangular (hormigón crudo tipo Pasión + textil técnico última generación).
- Módulo autónomo (de a uno) o agregable (de a varios) según configuración feria día pico / día vecino / montaje.
- 3 tipos de puesto = 3 fachadas. Austeridad y despojo como lenguaje.
- Tensión imposible en época Gaudí como guiño temporal: lo que él habría hecho con nuestros medios.

### 7.7 Zona vecinal: cerrado + abierto + semicubierto, bajando 1 m con techo verde

> "Zona vecinal [...] área flexible [...] reservada para vecinos. Bueno, ahí tiene que ser algo que te permita. [...] un espacio más cerrado que tenga a su vez un espacio abierto. [...] tengo un espacio semicubierto. Y [...] que vaya bajando el nivel. Entonces, cuando llego al último nivel, que bajé un metro, ahí ya es la parte techada. Y que arriba de esa parte techada esa cubierta tiene techo verde, por ejemplo. Ese es el tipo de interpretación que yo quiero."

Secuencia: abierto → semicubierto → cerrado, descendiendo hasta -1.00 m techado, con cubierta verde transitable como remate. Conecta con museo bajo cáscara y doble circulación arriba/abajo.

### 7.8 Pendiente metadata imágenes briefing

> "Hay unas imágenes que nos dan en el briefing, que creo que se podrían utilizar. Quisiera analizar si tienen metadata o algo así."

Ver §9 abajo: propuesta de script sin ejecutar hasta `s` de Sol.

## 8. Conceptos relacionados

- [[proyectos/concurso-gaudi-nexus/02-briefing-punto-a-punto|02-briefing-punto-a-punto]]
- [[proyectos/concurso-gaudi-nexus/reinterpretacion-programa-fractal|reinterpretacion-programa-fractal]]
- [[proyectos/concurso-gaudi-nexus/criterio/criterio-jurado|criterio-jurado]]
- [[proyectos/concurso-gaudi-nexus/index|concurso-gaudi-nexus]]

## 9. Metadata imágenes briefing — propuesta pendiente de `s`

Para responder "¿tienen metadata?" sin romper HITL: propongo `scripts/gx-briefing-metadata.py` (runnable) + `scripts/gx-briefing-metadata_notas.md` didáctico línea a línea, que extrae imágenes del PDF `G:\Mi unidad\OS-Emilia\AIxGaudi\GxAI_BRIEFING_ES.pdf`, lista EXIF/XMP, y vuelca a `raw/research/` sin copiar binarios al vault. Comando propuesto para que ejecutes vos: `P:\Anaconda\envs\comfyenv\python.exe scripts/gx-briefing-metadata.py`. Sin tu `s` no lo escribo ni lo corro.

---
*Más nuevo → más arriba. Log: 2026-11-02 segundo dictado Sol (vecinal 50+100 cáscaras acústicas, centro interpretación cáscara -1 m, mirador recorrido zoom lejos/cerca, cocina bóvedas, oficina vidrio en T, logística intersticial, puente Gaudí + sutura parques vidrio). 2026-11-02 integración dictado Sol §7 + propuesta metadata §9. 2026-11-02 creación ficha.*
