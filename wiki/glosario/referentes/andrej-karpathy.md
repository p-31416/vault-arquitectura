---
tipo: referente
referente: andrej-karpathy
fecha_creacion: 2026-09-07
ultima_actualizacion: 2026-09-09
tags: [referente, ia, cerebro-digital, software-2-0, educacion-abierta, glosario]
idioma: es
origen: https://karpathy.ai/
---

# Andrej Karpathy

> Investigador y educador central del deep learning moderno (ex-director IA Tesla, cofundador OpenAI, fundador Eureka Labs, equipo pretraining Anthropic desde 2026): combina papers visión+lenguaje, pedagogía abierta masiva y marcos Software 2.0 / Software 3.0 que inspiran el cerebro digital del vault.

- [[#Resumen]]
- [[#Trayectoria]]
- [[#Papers clave]]
- [[#Docencia abierta]]
- [[#Ideas-fuerza]]
- [[#Oportunidades de ampliación]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## Resumen

Andrej Karpathy (Bratislava 1986, eslovaco-canadiense) articula investigación, construcción de producto y docencia abierta: cofundador de OpenAI (2015-2017, 2023-2024), Director de AI en Tesla Autopilot Vision (2017-2022), creador de CS231n Stanford y de la serie Zero to Hero, fundador de Eureka Labs (2024, escuela AI-native) e integrante del equipo pretraining de Anthropic (Claude) desde 2026-05-19. Su legado une tesis y papers de conexión imagen-lenguaje con conceptos Software 2.0 / vibe coding / Software 3.0 y pedagogía masiva en YouTube, GitHub y blogs. Síntesis de `raw/research/2026-09-09-karpathy-legado.md` (22 fuentes, confianza Alta).

## Trayectoria

Formación con referentes fundacionales: BSc Toronto (cs + física, con Hinton), MSc UBC (con van de Panne), PhD Stanford 2011-2015 con Fei-Fei Li (Stanford Vision Lab), más internships Google Brain 2011 / Google Research 2013 / DeepMind 2015. Su sitio personal resume: Director de AI en Tesla con equipo de visión Autopilot y nueva etapa OpenAI en midtraining y synthetic data generation. La página Stanford confirma timeline Tesla / OpenAI / PhD y lista talks (ScaledML 2020, Autonomy Day 2019, Software 2.0 stack 2018). El movimiento 2026 hacia Anthropic queda registrado en prensa internacional para audiencia hispana e inglesa.

Aporta al estudio un modelo de trayectoria que integra academia, industria y educación: investigar, construir a escala y enseñar en abierto.

## Papers clave

Tesis PhD *Connecting Images and Natural Language* (2016): paradigma end-to-end para image-sentence matching, captioning y region-annotation. Extensiones aplicadas:

- *Deep Visual-Semantic Alignments for Generating Image Descriptions* CVPR 2015 Oral (Karpathy & Fei-Fei): CNN por regiones + Bi-RNN + embedding multimodal.
- *DenseCap: Fully Convolutional Localization Networks for Dense Captioning* CVPR 2016 Oral (Johnson, Karpathy, Fei-Fei).
- *Large-Scale Video Classification with CNNs* CVPR 2014 Oral: dataset Sports-1M (1.1M videos, 487 clases).
- *PixelCNN++* ICLR 2017, *World of Bits* ICML 2017, *Visualizing and Understanding Recurrent Networks* ICLR 2016 Workshop.
- *ImageNet Large Scale Visual Recognition Challenge* IJCV 2015 (coautor, experimentos human accuracy): base de su mote "reference human for ImageNet".
- Fundacionales previos: *Deep Fragment Embeddings* NIPS 2014, *Grounded Compositional Semantics* TACL 2013, *Emergence of Object-Selective Features* NIPS 2012.

Relevancia para el vault: el linaje visión+lenguaje sustenta el loop vault-visual (imagen + texto consultable) y el etiquetado asistido de activos.

## Docencia abierta

CS231n: primera materia deep learning Stanford, con notas, slides y syllabus abiertos y comunidad r/cs231n; videos 2016 con amplia audiencia global. *Neural Networks: Zero to Hero*: curso desde backprop (micrograd) hasta GPT desde cero en código; syllabus verificado con micrograd, makemore, MLP, BatchNorm, Backprop Ninja, WaveNet, GPT y Tokenizer; repo `karpathy/nn-zero-to-hero` abierto. GitHub `karpathy`: nanoGPT, nanochat, llm.c, llama2.c, micrograd, arxiv-sanity; pet projects ConvNetJS, char-rnn, neuraltalk2, arxiv-sanity.com. Blogs (GitHub, Medium, Bear) con piezas guía: *Unreasonable Effectiveness of RNNs* (2015), *A Recipe for Training Neural Networks* (2019), *Software 2.0* (2017). YouTube `@AndrejKarpathy` en doble track técnico / general más talks State of GPT Build 2023 y Tesla AI Day 2021. TIME100 AI 2024 destaca su impacto como educador.

Patrón reutilizable: enseñar construyendo desde cero en código, con syllabus público y repos reproducibles.

## Ideas-fuerza

*Software 2.0* (2017): código escrito por optimización (pesos neuronales) junto al Software 1.0 escrito por humanos. Eureka Labs (16-jul-2024): escuela AI-native con simbiosis teacher + AI Teaching Assistant y primer producto LLM101n undergraduate. Ciclo 2025-2026: Software 3.0, context engineering y agentes como evolución natural del stack programable en lenguaje. Su gist `llm-wiki` (abr 2026) propone mantener un vault markdown local con un agente que ingiere `raw/`, escribe `wiki/` interlinkeada y avanza lint, con context windows largos.

Para el estudio, Software 2.0 enmarca ComfyUI / DirectML y el vault computable; el patrón llm-wiki inspira directamente la técnica cerebro-digital (`AGENTS.md`): `raw/sessions/` hacia `wiki/glosario/`.

## Oportunidades de ampliación

El research 2026-09-09 deja ciclos fértiles: corpus italiano con cobertura primaria limitada (oportunidad de sumar fuente IT en siguiente pasada); cifras de seguidores en X / YouTube quedan para verificación futura con fuente primaria; síntesis 2025-2026 sobre Software 3.0 avanza con cruce adicional; DOI Crossref / Semantic Scholar queda como backlog de precisión bibliográfica. Todo ello enriquece futuras actualizaciones sin frenar el uso actual.

## Conceptos relacionados

- [[wiki/glosario/conceptos/cerebro-digital-karpathy|cerebro-digital-karpathy]]
- [[wiki/glosario/conceptos/vault-visual|vault-visual]]
- [[wiki/glosario/conceptos/sdd-spec_driven_development|sdd-spec_driven_development]]
- [[wiki/glosario/referentes/big-bjarke-ingels-group|big-bjarke-ingels-group]]
- [[wiki/glosario/referentes/template|template]]

## Referencias

- Karpathy, A. (2016). *Connecting Images and Natural Language* [Conectando imágenes y lenguaje natural] (Tesis doctoral, Stanford). https://cs.stanford.edu/people/karpathy/main.pdf (idioma original: en) [trad. propia]
- Karpathy, A., & Fei-Fei, L. (2015). *Deep Visual-Semantic Alignments for Generating Image Descriptions* [Alineamientos visual-semánticos profundos para generar descripciones de imágenes]. CVPR 2015 (Oral). (en) [trad. propia]
- Johnson, J., Karpathy, A., & Fei-Fei, L. (2016). *DenseCap: Fully Convolutional Localization Networks for Dense Captioning* [DenseCap: redes de localización totalmente convolucionales para dense captioning]. CVPR 2016. (en) [trad. propia]
- Karpathy, A., et al. (2014). *Large-Scale Video Classification with Convolutional Neural Networks* [Clasificación de video a gran escala con CNN]. CVPR 2014. (en) [trad. propia]
- Karpathy, A. (s.f.). Sitio personal oficial: https://karpathy.ai/ (verificado 2026-09-09 — 200, idioma: en)
- Karpathy, A. (s.f.). *Neural Networks: Zero to Hero*: https://karpathy.ai/zero-to-hero.html (verificado 2026-09-09 — 200, idioma: en) [trad. propia del título: Redes neuronales de cero a héroe]
- Stanford Computer Science. (s.f.). Sitio académico: https://cs.stanford.edu/people/karpathy (idioma: en)
- Karpathy, A. (2017, 11 nov.). *Software 2.0* [Software 2.0]. Medium. https://karpathy.medium.com/software-2-0-a64152b37c35 (en)
- Pillay, T. (2024, 5 sep.). *Andrej Karpathy*. TIME100 AI. https://time.com/7012851/andrej-karpathy (en)
- Capoot, A., & Kolodny, L. (2026, 19 may.). *Anthropic hires OpenAI cofounder Andrej Karpathy* [Anthropic contrata al cofundador de OpenAI Andrej Karpathy]. CNBC. (en)
- Millán, S. (2026, 19 may.). *Andrej Karpathy, miembro del equipo fundador de OpenAI, se une a su rival Anthropic*. El País. (idioma original: es)
- Bellan, R. (2024, 16 jul.). *After Tesla and OpenAI, Karpathy's startup aims to apply AI assistants to education* [Tras Tesla y OpenAI, la startup de Karpathy avanza con asistentes IA en educación]. TechCrunch. (en) [trad. propia]
- Gist oficial `llm-wiki` (patrón cerebro digital): https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (verificado 2026-09-07 — 200)
- Resumen arquitectura second brain (Codersera): https://codersera.com/blog/karpathy-llm-knowledge-base-second-brain (verificado 2026-09-07 — 200)
- Second Brain paso a paso (Ask Glitch): https://www.askglitch.com/blog/build-a-second-brain (verificado 2026-09-07 — 200)
- Insumo vault: [[raw/research/2026-09-09-karpathy-legado|research 2026-09-09 Karpathy]] (22 fuentes, confianza Alta)
