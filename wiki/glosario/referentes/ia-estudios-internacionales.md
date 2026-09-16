---
tipo: referente
fecha_creacion: 2026-06-28
ultima_actualizacion: 2026-09-07
tags: [ia, estudios-internacionales, referente, investigacion]
origen: wiki/glosario/referentes/ia-estudios-internacionales.md → wiki/glosario/referentes/ (global)
estudios: [zha-hadid, big-bjarke-ingels, mvrdv, foster-partners]
---

# IA en estudios de arquitectura internacionales

## Panorama general

La adopción de IA en arquitectura pasó de experimental a estándar entre 2024 y 2026. Según encuestas del sector:

- **64%** de los profesionales ya experimentaron con herramientas de IA (Chaos/Architizer, 2025)
- **74%** planea aumentar su uso en los próximos 12 meses
- **46%** ya usa IA en algún punto de su flujo visual
- Tareas de renderizado que tomaban 4-8 horas ahora se hacen en menos de 10 minutos

El patrón común entre los grandes estudios no es reemplazar arquitectos, sino **amplificar el proceso creativo**: la IA genera cientos de variaciones, el humano selecciona y refina.

---

## Zaha Hadid Architects (ZHA)

**Ubicación:** Londres | **Fundación:** 1979 | **Equipo:** ~500 personas

ZHA es el estudio más avanzado en integración de IA a nivel global. La firma viene de una tradición de adopción temprana de tecnología: CAD en los 80, diseño paramétrico en los 90, y ahora IA generativa como estándar.

### Cómo usan IA

| Aplicación | Herramientas | Descripción |
|------------|-------------|-------------|
| Ideación conceptual | DALL-E, Midjourney, Stable Diffusion | La mayoría de los proyectos comienzan con prompts de texto que generan imágenes en el lenguaje formal característico de ZHA. El equipo selecciona ~10-15% de las salidas para avanzar a modelado 3D. |
| Optimización de planta | ML interno (CODE research group) | Algoritmos entrenados con datos históricos optimizan layouts de plantas según programa, circulación y eficiencia espacial. |
| Análisis de luz, visibilidad, movimiento | Simulación + ML | Evaluación de miles de variaciones en minutos para informar decisiones de diseño basadas en evidencia. |
| Base de datos de imágenes | NVIDIA NIM + LoRA + Stable Diffusion | ZHA mantiene un archivo interno de diseño con décadas de proyectos. Usan LLMs para etiquetar, buscar y reentrenar modelos de estilo propios. |
| Renderizado y visualización | NVIDIA Omniverse + RTX | Pipeline completo de IA acelerado por GPU, con modelos entrenados localmente para proteger IP del cliente. |

### Unidades internas

- **ZHAI (Zaha Hadid Analytics and Insights)** — unidad dedicada a desarrollar aplicaciones de IA para la práctica arquitectónica
- **CODE (Computational Design Research Group)** — co-fundado por Shajay Bhooshan, aplica ML a optimización de diseño desde antes de que "IA" fuera mainstream
- Colaboración con **NVIDIA** para infraestructura de workstations con hasta 4x RTX 6000 Ada Generation

> *"La mayoría de los proyectos pasan por este proceso [IA generativa]. Animamos a todos los que trabajan en concursos e ideación temprana a ver qué aparece y tener un repertorio más amplio."* — Patrik Schumacher, Principal de ZHA (2023)

**Fuentes:**
- [How Zaha Hadid Architects Uses AI to Design Buildings — Innovation Library](https://innovationlibrary.com/articles/how-zaha-hadid-architects-uses-ai-to-design-buildings)
- [AI in practice at Zaha Hadid Architects — Allplan](https://www.allplan.com/blog/ai-in-practice-at-zaha-hadid-architects)
- [ZHA + NVIDIA Case Study](https://www.nvidia.com/en-us/case-studies/zaha-hadid-architects-with-omniverse-and-usd/)
- [ZHA developing "most" projects using AI images — Dezeen](https://www.dezeen.com/2023/04/26/zaha-hadid-architects-patrik-schumacher-ai-dalle-midjourney/)

---

## BIG — Bjarke Ingels Group

**Ubicación:** Copenhague, NY, Londres, Barcelona, LA, Oslo, Zúrich | **Fundación:** 2005 | **Equipo:** ~700 personas

BIG usa IA como extensión de su filosofía de diseño basada en diagramas. Su enfoque combina métodos analógicos (diagramas dibujados a mano) con simulación digital paramétrica y herramientas de IA generativa.

### Cómo usan IA

| Aplicación | Herramientas | Descripción |
|------------|-------------|-------------|
| Renderizado y visualización | D5 Render integrado con BIM | Visualizaciones inmersivas con calidad fotográfica en fracciones del tiempo tradicional. Acelera iteraciones de diseño y presentaciones a clientes. |
| Generative design | Herramientas paramétricas + ML | Algoritmos que exploran múltiples configuraciones para optimizar forma, programa y eficiencia. |
| Simulación ambiental | Ladybug Tools + CFD | Análisis climático, luz natural, acústica y dinámica de fluidos computacional para validar decisiones de sostenibilidad. |
| Evaluación de ciclo de vida | LCA computacional | Herramientas propias para medir huella de carbono desde etapas tempranas del diseño. |
| Real-time rendering | D5 Render + workflows BIM | Colaboración multi-arquitecto en proyectos globales con visualización en tiempo real. |

### Proyectos destacados

- **Terminus AI City (Chongqing, China)** — Masterplan de campus tecnológico que integra big data y robótica, diseñado con herramientas de IA
- **Google Bay View** — Simulaciones data-driven para optimizar sistemas pasivos de climatización
- **CODEX + ICON** — Catálogo de viviendas 3D-printed diseñadas algorítmicamente, combinando IA generativa con fabricación aditiva

BIG también co-organizó la competencia "Exploring the Impact and Opportunities of AI at BIG Architects" con IE School of Architecture and Design.

**Fuentes:**
- [Architectural Firm in 2025: BIG — RTF](https://www.re-thinkingthefuture.com/know-your-architects/a14433-architectural-firm-in-2025-big-bjarke-ingles/)
- [Grokipedia — BIG](https://grokipedia.com/page/Bjarke_Ingels_Group)
- [Conversation with Bjarke Ingels on AI — Archinect](https://archinect.com/features/article/150420098/a-conversation-with-bjarke-ingels-on-ai-3d-printing-and-the-future-of-the-architectural-profession)

---

## MVRDV

**Ubicación:** Róterdam | **Fundación:** 1993 | **Equipo:** ~300 personas

MVRDV integra IA a través de su unidad de investigación interna **MVRDV NEXT**, que experimenta con modelos generativos entrenados con el archivo propio del estudio.

### Cómo usan IA

| Aplicación | Herramientas | Descripción |
|------------|-------------|-------------|
| Concept sketches | Midjourney, Stable Diffusion | Generación de imágenes para exploración conceptual temprana |
| Modelos personalizados | Modelos propios entrenados con archivo MVRDV | Entrenan modelos con su propio archivo de proyectos para mantener identidad visual |
| Carbon tracking | CarbonSpace (herramienta propia) | Medición y reducción de carbono embebido desde el primer boceto. Usado en el IPAI Campus. |
| Simulación urbana | Herramientas internas | Análisis de flujos peatonales, densidad, impacto urbano |

### Proyecto destacado

- **IPAI Campus (Heilbronn, Alemania)** — Campus de 30 hectáreas para el Innovation Park Artificial Intelligence. MVRDV usó CarbonSpace para rastrear y reducir carbono embebido. Emplearon análisis ambientales para optimizar microclima, materiales (madera, bio-basados) y eficiencia energética.

> *"MVRDV ve la IA como un aliado creativo, pero insiste en que la tecnología debe apoyar, no reemplazar, la imaginación humana."* — MVRDV NEXT

**Fuentes:**
- [Architectural Firm in 2025: MVRDV — RTF](https://www.re-thinkingthefuture.com/know-your-architects/a14440-architectural-firm-in-2025-mvrdv)
- [MVRDV breaks ground on IPAI Campus — ArchDaily](https://www.archdaily.com/1035412/mvrdv-breaks-ground-on-the-innovation-park-artificial-intelligence-campus-in-heilbronn-germany)
- [How Top Firms See AI Shaping Architecture's Workflows — ArchDaily](https://www.archdaily.com/1036357/how-top-firms-see-ai-shaping-architectures-workflows)

---

## Foster + Partners

**Ubicación:** Londres | **Fundación:** 1967 | **Equipo:** ~1,500 personas

Foster + Partners aborda la IA desde la investigación aplicada con equipos internos dedicados, usando su vasto archivo de décadas de proyectos como base de datos de entrenamiento.

### Cómo usan IA

| Aplicación | Herramientas | Descripción |
|------------|-------------|-------------|
| Investigación aplicada | Applied R+D team | Equipo multidisciplinario de arquitectos, ingenieros y programadores que desarrollan herramientas propias de IA |
| Machine Learning | Modelos entrenados con archivo Foster | +600,000 archivos digitalizados del archivo del estudio. Usan ML para clasificar, buscar y extraer patrones de diseño. |
| Simulación de fachadas adaptativas | Algoritmos de ML + materiales | Fachadas termo-activas que se deforman pasivamente con la temperatura, optimizadas con ML |
| Building Physics | Specialist Modelling Group | Modelado de luz natural, aire, sonido, confort térmico. Simulación generativa automatizada. |
| Fabricación avanzada | IA + impresión 3D | Investigación colaborativa con universidades, incluyendo impresión 3D extraterrestre (hábitats lunares/martes) |

Foster mantiene tres equipos de investigación permanentes:
- **Applied R+D** — desarrollo de herramientas propias de IA
- **Specialist Modelling Group** — geometría compleja, física de edificios, innovación
- **Materials Research Centre** — investigación de materiales sostenibles

**Fuentes:**
- [Towards AI in Architecture — Foster + Partners Journal](https://www.fosterandpartners.com/insights/plus-journal/towards-artificial-intelligence-in-architecture-how-machine-learning-can-change-the-way-we-approach-design)
- [Technology and Research at Foster + Partners](https://www.fosterandpartners.com/expertise/technology-and-research)
- [Top Architecture Firms Leading AI Innovation — Archinect](https://archinect.com/c4ablog/top-architecture-firms-leading-the-future-of-ai-innovation-in-design)

---

## Otros estudios notables

| Estudio | Enfoque IA | Particularidad |
|---------|-----------|----------------|
| **UNStudio** | Investigación en IA para sostenibilidad, diseño paramétrico + ML | 7 oficinas en 4 continentes, integran IA con consulting |
| **Gensler** | Herramientas de IA para análisis de datos urbanos, modelos predictivos de comportamiento | Mayor estudio del mundo por volumen, IA aplicada a data-driven design |
| **Coop Himmelb(l)au** | Diseño paramétrico avanzado, exploración formal algorítmica | Pioneros en deconstructivismo digital, ahora con herramientas de IA |
| **AI SpaceFactory** | IA + impresión 3D para hábitats extraterrestres | Ganadores del NASA 3D-Printed Habitat Challenge |
| **LWK + Partners** | Investigación con AIRI Lab en datasets, fine-tuning, AIGC | Colaboración activa con laboratorios de IA para arquitectura |

---

## Patrones comunes de uso

En todos los estudios se repiten estos casos de uso:

1. **Ideación generativa temprana** — Midjourney, DALL-E, Stable Diffusion para explorar conceptos antes de modelar. El humano selecciona, la IA genera.
2. **Renderizado acelerado** — Reducción de 4-8h a <10 min por imagen. D5 Render, Lumion AI, NVIDIA Omniverse.
3. **Simulación y optimización** — ML para evaluar miles de variantes de luz, energía, estructura, costo.
4. **Carbon footprint tracking** — Herramientas de IA para medir y reducir carbono embebido desde fase conceptual.
5. **Archivos como datasets** — El propio archivo de proyectos del estudio se convierte en dato de entrenamiento para modelos propios.
6. **Infraestructura local** — Workstations con GPUs NVIDIA para entrenar y correr modelos localmente, sin enviar datos a la nube (protección IP del cliente).

### Herramientas más mencionadas

| Herramienta | Tipo | Usada por |
|-------------|------|-----------|
| Midjourney | Generación de imágenes | ZHA, MVRDV, Gensler |
| Stable Diffusion | Generación open-source | ZHA, MVRDV |
| DALL-E | Generación de imágenes | ZHA |
| D5 Render | Renderizado en tiempo real | BIG |
| NVIDIA Omniverse | Simulación + colaboración | ZHA |
| Rhino.Inside + Grasshopper | Paramétrico + IA | ZHA, BIG, Foster |
| Autodesk Forma | Análisis urbano generativo | Gensler, Foster |
| Ladybug Tools | Simulación ambiental | BIG |
| CarbonSpace | Carbon tracking | MVRDV |

---

## Recursos multimedia

### YouTube

- [The B1M — How AI is Changing Architecture](https://youtube.com/@TheB1M)
- [ZHA + NVIDIA — AI-Accelerated Architecture Pipeline](https://www.nvidia.com/en-us/case-studies/zaha-hadid-architects-with-omniverse-and-usd/)
- [ArchDaily — How Top Firms See AI Shaping Architecture](https://www.archdaily.com/1036357/how-top-firms-see-ai-shaping-architectures-workflows)

### Podcasts

| Podcast | Episodios relevantes |
|---------|---------------------|
| Future Construct | Múltiples episodios sobre IA en AEC |
| The BIM Podcast | Discusiones sobre IA generativa en diseño |

### Thought leaders en IA + Arquitectura

| Nombre | Estudio / Rol | Redes |
|--------|--------------|-------|
| [[wiki/glosario/referentes/patrik-schumacher|Patrik Schumacher]] | Principal, ZHA | [[wiki/glosario/referentes/patrik-schumacher|ficha]] |
| [[wiki/glosario/referentes/ulrich-blum|Ulrich Blum]] | Senior Associate, ZHA / Prof. Münster | [[wiki/glosario/referentes/ulrich-blum|ficha]] |
| [[wiki/glosario/referentes/shajay-bhooshan|Shajay Bhooshan]] | CODE Research Group, ZHA | [[wiki/glosario/referentes/shajay-bhooshan|ficha]] |
| [[wiki/glosario/referentes/nils-peter-fischer|Nils-Peter Fischer]] | Director, ZHA | [[wiki/glosario/referentes/nils-peter-fischer|ficha]] |
| [[wiki/glosario/referentes/bjarke-ingels|Bjarke Ingels]] | Fundador, BIG | [[wiki/glosario/referentes/bjarke-ingels|ficha]] |
| [[wiki/glosario/referentes/jacob-van-rijs|Jacob van Rijs]] | Fundador, MVRDV | [[wiki/glosario/referentes/jacob-van-rijs|ficha]] |
| [[wiki/glosario/referentes/fredy-fortich|Fredy Fortich]] | Arquitecto, MVRDV | [[wiki/glosario/referentes/fredy-fortich|ficha]] |
| [[wiki/glosario/referentes/ben-van-berkel|Ben van Berkel]] | Fundador, UNStudio | [[wiki/glosario/referentes/ben-van-berkel|ficha]] |
| [[wiki/glosario/referentes/carlos-banon|Carlos Bañón]] | Formas.AI | [[wiki/glosario/referentes/carlos-banon|ficha]] |

---

## Referencias

- [ArchDaily — How Top Firms See AI Shaping Architecture's Workflows (2025)](https://www.archdaily.com/1036357/how-top-firms-see-ai-shaping-architectures-workflows)
- [Innovation Library — How ZHA Uses AI to Design Buildings (2025)](https://innovationlibrary.com/articles/how-zaha-hadid-architects-uses-ai-to-design-buildings)
- [Allplan — AI in Practice at ZHA (2026)](https://www.allplan.com/blog/ai-in-practice-at-zaha-hadid-architects)
- [NVIDIA — ZHA Customer Story](https://www.nvidia.com/en-us/case-studies/zaha-hadid-architects-with-omniverse-and-usd/)
- [RTF — Architectural Firm in 2025: BIG](https://www.re-thinkingthefuture.com/know-your-architects/a14433-architectural-firm-in-2025-big-bjarke-ingles/)
- [RTF — Architectural Firm in 2025: MVRDV](https://www.re-thinkingthefuture.com/know-your-architects/a14440-architectural-firm-in-2025-mvrdv)
- [Foster + Partners — Towards AI in Architecture](https://www.fosterandpartners.com/insights/plus-journal/towards-artificial-intelligence-in-architecture-how-machine-learning-can-change-the-way-we-approach-design)
- [Foster + Partners — Technology and Research](https://www.fosterandpartners.com/expertise/technology-and-research)
- [Archinect — Top Architecture Firms Leading AI Innovation](https://archinect.com/c4ablog/top-architecture-firms-leading-the-future-of-ai-innovation-in-design)
- [Cadd Centre — How Top Firms Are Using Generative AI in 2025](https://caddcentre.com/blog/how-top-architecture-firms-are-using-generative-ai-today-and-into-2025/)
- [Illustrarch — Top AI Tools Transforming Architectural Design in 2026](https://illustrarch.com/artificial-intelligence/75112-ai-architectural-design-tools.html)
- [ArchDaily — What Architects Expect From AI Tools in 2026](https://www.archdaily.com/1040024/what-architects-expect-from-ai-tools-in-2026)
