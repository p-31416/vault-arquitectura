---
tipo: proyecto
proyecto: STUDIO_OS-Emilia
fecha: 2026-09-09
reunion_propuesta: 2026-09-12
tags: [propuesta, comercial, sprint, studio-os, esquema]
estado: esquema
---

# Propuesta comercial viernes — ESQUEMA (completar juntas)

> Base: [[proyectos/STUDIO_OS-Emilia/reuniones/2026-09-09-analisis-4-reuniones-previo-propuesta]] (O1-O6, A1-A7, N1-N8). Precio fundador USD 600 vs mercado USD 1.500-7.500. Ritmo: 2 jornadas × 7h = 14 hs/sem Sol (8 jornadas, 14 pomodoros/día), 2hs/sem Emília (condición).

## 1. Recuento — qué escuchamos (validado SOL 09/09)
- [x] N1 infraestructura propia: trabajar donde se pueda con infra propia, saber qué modelo se usa, tokens de gasto mensual medidos (API separada proyecto-pi/pitautech). Nada de plataformas IA cautivas.
- [x] N2 presupuestos/honorarios: "si erran por 10 mil dólares, ¿de quién es la culpa?" + 2hs discutiendo con socias + cambios Pinterest sin cobrar.
- [x] N3 dashboard: "miro y sé dónde está cada cosa" + qué toca hoy/objetivo semana-mes + informe de obra auto (foto → IA → cliente).
- [x] N4 renders estilo propio: "todo sale igual, tono anaranjado" + probar un material en una tarde + entrega profesional (no WhatsApp) + sin copyright.
- [x] N5 backup = el vault: organizar proceso creativo + documentar camino y negativos. A ANALIZAR: "vault visual" — imitar el concepto del vault con FOTOS/imágenes (capturas, Pinterest, redes).
- [x] N6 puerta no-técnica: "quiero entender la lógica" + "¿dónde entra el humano?" (dosificar técnica).
- [x] N7 equipo/adopción: 10 personas, 2 sin PC, alimentar sin fricción (referente + permisos).
- [x] N8 infra: PC al límite (22 GB) + "está en mi computadora, eso es privacidad" + VPS USD 7/mes como ancla.

## 2. Propuesta fase 1 — sprint 30 días (definido SOL 09/09)
- [x] Vault compartido: crear vault, instalar herramientas, enseñar a Emília a bajar su información y alimentarlo. Diagnóstico + quick-wins + puesta en marcha de la nueva forma de trabajo.
- [x] Casa en construcción: revisar propuesta + delinear estándares CAD (impacto inmediato; enseñanza a pasantes se obvia, queda documentado).
- [x] UN flujo Comfy (upscale/mejora o render básico) para mostrar ComfyUI. Resto de flujos (img2img, txt2img, upscale, videos — investigar en web) → Fase 2.
- [x] Fathom conectado vía MCP + automatización (objetivo): Fathom → calendar → descarga auto a `/raw` vía GitHub Actions (al subir reunión) + pull al abrir Antigravity; tasks a Leantime (solo las de la semana, sin sobrecargar) — pasar de indicaciones por WhatsApp a tareas anotadas.
- [x] Vault + CAD + Comfy: demo de cómo "representaríamos" + evaluar carga de imágenes de estilos (objetivo Emília con sus clientes).
- [x] Prototipo vault visual en sprint (caso Casa masterplan): fotos/capturas/Pinterest/redes como vault.
- [ ] Plan trimestral (horizonte para que se vea el alcance — el sprint es el Mes 1): Mes 2-3 = quick-wins medidos en hs/$ + automatizaciones (Fathom auto, Leantime semanal) + resto flujos Comfy + calculadora honorarios + presupuestos con rótulo + redes/portfolio. Precio Mes 2-3: a cotizar post-demo con quick-win medido (referencia retainer LatAm USD 3.000-5.000/mes; fundador por debajo).
- [x] Diferenciador: nadie hace esto en estudios de arquitectura (océano azul) — Emília como caso fundador.

## 3. Valores — cuánto/cuándo/cómo (base acordada, falta definir mostrar descuento)
- [x] Precio fundador USD 600 = 56 hs (14/sem × 4, 8 jornadas de 7h) a 15 USD/h → costo 840, descuento ~29%.
- [x] Forma: 50/50 o 100% adelantado. Acreditable a Fase 2 si avanza en 30 días post-demo.
- [x] NO incluye: Fase 2, licencias, academia (negocio separado).
- [x] Ancla mercado — de dónde sale el rango USD 1.500-7.500 (ver tabla abajo: son *auditorías/diagnósticos de IA para PYME*, mismo formato que este sprint: 2-4 semanas, mapa de flujos, roadmap; el nuestro suma prototipo + capacitación, que en mercado es tier "piloto/build" USD 6.900+). PERO ellos venden producto cerrado con casos de éxito; este sprint es piloto co-construido (diagnóstico + quick-wins para demostrar cómo trabajar con IA y automatizar: Fathom auto → vault, WhatsApp → tasks Leantime semanales) → precio fundador USD 600, acreditable. Desde el 2º caso con quick-win medido, precio de mercado.
- [ ] Definir: ¿se muestra mercado 2.500 → fundador 600, o solo precio 600?

### De dónde sale el rango mercado (relevado 09/09/2026, links verificados 200)

| Producto | Precio USD | Qué incluye | Fuente |
|---|---|---|---|
| AI Opportunity Audit 2 sem | 3.500-6.500 | workflow map + lista ROI + roadmap | BetOnAI (rate card 68 consultores) |
| Audit estándar 2 sem / Deep 3-4 sem | 2.500 / 5.000 | 5 oportunidades rankeadas + presentación live; deep suma roadmap 12m | B5 Marketing |
| Audit <10 emp / 10-50 emp | 1.500-3.000 / 2.500-5.000 | inventario tareas, $ por ítem, 1 quick-win funcionando | Prometheus/ConsultKit, O'Donnell ($2.500 flat) |
| Audit mid-market 3 sem (acreditable) | 7.500 | opportunity map + ROI hs/$ + plan 90 días | Sentient Marketer |
| Readiness 2-4 sem | 2.000-8.000 | roadmap priorizado | AI Consulting Network |
| Assessment 1-2 sem / piloto 1 workflow | desde 1.900 / desde 6.900 | 3 workflows + roadmap / 1 workflow en producción | Encelyte (precios públicos) |

Hora consultor IA freelance 2026: AR 15-60, LatAm senior 40-85, global 100-300, boutique 150-350 (BetOnAI, AYAutomate, Upwork vía Ciela). Tu tarifa 15 USD/h = piso argentino: el precio fundador se sostiene como piloto, no como tarifa.

## 4. Compromisos (confirmado SOL 09/09)
- [x] Emília 2hs/sem condición (mié sesión + lun breve; día exacto a definir con ella).
- [x] Accesos: Drive piloto (mail dedicado a crear) + PC (limpieza presencial) + Fathom instalado siempre.
- [x] Ritual: lun check 15-30 min + mié sesión 60-90 min + vie avance async (sin reunión).

## 5. Cronograma 30 días + desglose 56 hs (2 jornadas × 7h/sem, subtasks ≤25 min)

> Ritmo: 2 jornadas de 7h por semana (ritmo pomodoro 25+5 → 14 pomodoros/día, bajo el tope 16). Lun check breve + mié sesión caen dentro de las jornadas.

| Bloque | Hs | Detalle |
|---|---|---|
| Reuniones + rituales | 8 | Lun check 0.5h ×4 (2h) + mié sesión 1.5h ×4 (6h, incluye demo/retro S4) |
| Onboarding Emília | 6 | Enseñar a bajar su info, alimentar el vault, Fathom en su PC, guardar/consultar |
| Vault compartido | 9 | Crear vault + estructura, instalar herramientas, Drive + mail dedicado, Fathom MCP, permisos |
| Casa + estándares CAD | 13 | Revisar propuesta casa en construcción, delinear estándares (layers/bloques/rutinas), documentar (enseñanza a pasantes: solo documento) |
| Comfy 1 flujo | 8 | Upscale/mejora o render básico + prueba con caso Casa + mini-guía de uso |
| Vault visual prototipo | 7 | Diseño ingesta (fotos/capturas/Pinterest/redes) + prototipo estilos Casa masterplan |
| Documentación + cierre | 5 | Roadmap Fase 2, cláusula cobro de cambios, demo integral, retro, acta |
| **Total** | **56** | = 8 jornadas × 7h (14 pomodoros/día) |

- [ ] S1 (14h): vault 7 + onboarding 2 + reuniones 2 + doc 1 + CAD 2 (relevar propuesta casa).
- [ ] S2 (14h): CAD 8 + vault 2 + onboarding 2 + reuniones 2.
- [ ] S3 (14h): CAD 3 + Comfy 7 + vault visual 1 + onboarding 1 + reuniones 2.
- [ ] S4 (14h): vault visual 6 + Comfy 1 + doc/cierre 4 + onboarding 1 + reuniones 2.
- [ ] Trimestre (propuesta viernes): M1 sprint diagnóstico 600 acreditable → M2-M3 implementación + medición (cotizar post-demo). El alcance completo solo se ve en 3 meses.

## 6. Cierre — fecha de arranque + firma (confirmado SOL 09/09)
- [ ] Fecha arranque: ... (definir el viernes)
- [x] Adapt1 descartado (plataforma cautiva) → tesis open-source + infra propia.
- [x] Cláusula cobro de cambios (Juego de la Oca → metodología de servicios a clientes) como entregable del sprint.

## Referencias
- [[proyectos/STUDIO_OS-Emilia/reuniones/2026-09-09-analisis-4-reuniones-previo-propuesta]]
- [[proyectos/STUDIO_OS-Emilia/04-plan-studio-os]]
- [[proyectos/STUDIO_OS-Emilia/reuniones/2026-08-28-plan-exploracion-onepager-v02-con-pitautech-pre-voseo]]
