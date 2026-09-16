---
tipo: reunion
proyecto: STUDIO_OS-Emilia
fecha: 2026-09-09
fecha_reuniones: 2026-08-28
duracion_total: ~230 min (4 sesiones: 59 + 59 + 59 + 52)
formato: online (Google Meet + Fathom)
objetivo: "Análisis simultáneo de las 4 reuniones del 28/08 (presentación onepager) para mapear necesidades y objetivos antes de la PROPUESTA COMERCIAL del viernes."
tags: [reunion, analisis, necesidades, objetivos, propuesta-comercial, studio-os, fathom]
estado: analisis-previo-propuesta
---

# Análisis 4 reuniones 28/08 — Mapeo de necesidades previo a propuesta del viernes

> Las 4 sesiones del 28/08 forman UN arco: tesis (open-source vs plataformas) → infraestructura → dolores administrativos → proyecto gancho + cierre comercial. El onepager de 6 áreas se presentó de forma oral/fragmentada; precio USD 600, 2hs/semana titular y alcance fase 1 **no quedaron cerrados** — eso es lo que el viernes debe cerrar.

**Fuentes (transcripts completos):**
- [[raw/reuniones/2026-08-28-802902095]] — Tesis open-source + Adapt1 (59 min)
- [[raw/reuniones/2026-08-28-802992698]] — Infra/PCs + Magenta + deriva academia (59 min)
- [[raw/reuniones/2026-08-28-803065252]] — Dashboard/admin/honorarios, piloto Magenta (59 min)
- [[raw/reuniones/2026-08-28-803125998]] — Vinícola Gema masterplan + plan 30 días + valores (52 min)
- Marco presentado: [[proyectos/STUDIO_OS-Emilia/reuniones/2026-08-28-plan-exploracion-onepager-v02-con-pitautech-pre-voseo]]

## 1. Objetivos — acordados vs abiertos

### Acordados (base de la propuesta)
| # | Objetivo | Dueño | Fuente |
|---|---|---|---|
| O1 | Plan 30 días IA (casa = retrospectivo, vinícola = en vivo) | Sol, entrega lunes | 803125998 [51:35] |
| O2 | Vinícola Gema/Magenta como caso piloto (F1 casa + restaurante/eventos → F2 villa → F3 establo) | Emília | 803065252 [57:14], 803125998 [15:44] |
| O3 | Infra local-first por privacidad/PI + copia nube (no nube obligatoria) | Ambas | 803065252 [02:12], 803125998 [44:10] |
| O4 | Trabajo por fases por áreas, no todo junto | Ambas | 803065252 [56:20] |
| O5 | Registrar decisiones (ADR) revisables y reversibles | Sol | 803065252 [02:12] |
| O6 | Grupo WhatsApp equipo ("Vinícola Brasil", sin cliente) + Fathom instalado siempre | Ambas | 803125998 |

### Abiertos (cerrar SÍ o SÍ el viernes)
| # | Tema | Estado |
|---|---|---|
| A1 | **Valores: cuánto, cuándo, cómo se cobra** (pedido explícito Emília [45:26]) | Sin responder |
| A2 | Alcance fase 1 + qué NO entra (base vs nice-to-have) | Sin delimitar |
| A3 | Proyecto piloto único: ¿Magenta, casa masterplan o Casa Schomer? | Sin elegir |
| A4 | 2hs/semana titular + rol socias/equipo (10 personas, 2 sin PC) | Sin compromiso |
| A5 | Veredicto Adapt1 (trial 30 días corriendo): cancelar vs convivir | Sin fecha fin trial |
| A6 | Dónde viven archivos + quién mantiene (Dropbox sí/no, backup, accesos) | Sin definir |
| A7 | Regla de cobro de cambios (Juego de la Oca → cláusula) | Sin escribir |

## 2. Mapeo de necesidades (clusters)

### N1. Propiedad del dato / no-dependencia (tesis central, aceptada)
"No podés contratar una herramienta que te resuelva un problema pero no te solucione el global" [16:16]. Miedo a costos escalados ("300 USD/mes", "miles de dólares") y a quedar cautiva (Adapt1 trial, "todo lo que desarrollé, perdés"). → Propuesta: open-source + dato propio + métricas propias como principio no negociable.

### N2. Presupuestos / honorarios / cobro (dolor dominante operativo)
Excel manual, 2hs discutiendo números con socias, miedo a errar ("si erran por 10 mil dólares, ¿de quién es la culpa?"), cambios Pinterest no cobrados, volatilidad AR, "no sabemos comunicar el servicio". Pide: Excel → contrato automático, bloques A40 con data real, metodología propia (no Clarín/CPAU). → Quick-win candidato fase 1.

### N3. Dashboard / gestión (pedido literal)
"Un dashboard donde miro y sé dónde está cada cosa" + "qué me toca hacer hoy, objetivo de la semana/mes" + informe de obra auto (foto → IA → cliente) + portal cliente con login. → Núcleo del sistema a proponer.

### N4. Renders con estilo propio (dolor visible)
Todo el equipo usa ChatGPT y "todo sale igual, tono anaranjado fin de día". Pide fine-tuning con materialidad propia + velocidad (probar un material = una tarde, no 3 días) + entrega profesional (no WhatsApp suelto) + evitar copyright. → Piloto fine-tuning como win rápido.

### N5. Archivo / backup / memoria (pedido literal)
"Un backup donde organice mi proceso creativo", transcripción ES/PT guardada por proyecto, metodología de archivo, miedo a perder fuentes ("no me acuerdo dónde encontré"), documentar el camino + lo que NO funciona (negativos). → Cerebro digital como respuesta directa.

### N6. Titular no-técnica (restricción de diseño)
"Como no soy programadora, quiero entender la lógica". Sobrecarga técnica la saca ("me saca", "parate/frenate", Sol habla 70-80%). Pregunta clave sin resolver: "¿dónde entra el humano en el flujo de la IA?". → Todo entregable debe tener puerta no-técnica (portal, sí/no, canvas) y la propuesta debe dosificar técnica.

### N7. Equipo y adopción (riesgo)
10 personas, 2 sin PC; juniors que no saben elegir; estudio adaptado a la herramienta del pasante; "los chicos" deben alimentar sin fricción. → Plan debe incluir adopción (referente JR, permisos, capacitación) o no se usa.

### N8. Infraestructura (decisión pendiente)
PC Emília al límite (22 GB, Descargas 20 GB), inversión hardware de Quique subutilizada ("no usan ni el 10%"), VPS USD 7/mes vs suscripciones como ancla positiva. Pendiente: local vs VPS/Contabo vs nube, limpieza PC presencial. → Incluir auditoría hardware + decisión infra en fase 1.

## 3. Señales comerciales para el viernes

- **Sensibilidad precio alta, sin cifra declarada.** Anclas positivas: VPS 7 USD, "10 dólares sale la mitad que Cloud/ChatGPT". Referencias de valor: baño USD 40k, casa ~USD 1.000/m2. Presentar valores con forma/cuándo/cuánto (pedido explícito) y faseo que baje el ticket de entrada.
- **Timing caliente pero disperso.** Trial Adapt1 corriendo (ventana corta), proyectos vivos (Magenta, casa BR, Casa Schomer que drena), pero cliente vinícola lento (presupuesto pausado 1-4 meses hasta relevamiento terreno). Vender velocidad en lo controlable (plan 30 días, quick-wins) sin prometer lo que depende de terceros.
- **Decisores:** Emília (titular, interlocutora) + socias (números) + Quique (hardware, ausente) + cliente vinícola/Leticia (terceros). La propuesta debe dar material para que Emília venda hacia adentro (socias) y hacia el cliente.
- **Riesgos a mitigar en la propuesta:** dispersión academia vs STUDIO OS (separar explícitamente), sobrecarga técnica (dosificar), alcance infinito ("no podemos abordar todo" → fase 1 acotada + NO explícito), cliente que cambia todo (cláusula cobro cambios como feature, no como queja).

## 4. Estructura sugerida propuesta viernes

1. Recuento en sus palabras (qué escuchamos: N1–N8) → 2. Propuesta fase 1 acotada (piloto único + quick-wins N2/N4) → 3. Valores con forma/cuándo/cuánto + qué NO entra → 4. Compromisos (2hs/semana, referente, accesos) → 5. Cronograma 30 días + hitos → 6. Cierre con fecha de arranque.
