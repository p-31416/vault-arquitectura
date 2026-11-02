---
tipo: indice
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [dashboard, resumen-15-dias, studio-os, pi, concurso-gaudi, rhino, comfyui]
idioma: es
proyecto: Proyecto Pi
cliente: Estudio (línea propia)
estado: vigente
---

# Dashboard resumen — 15 días (2026-10-18 → 2026-11-02)

> Puerta de lectura rápida del período. Detalle diario completo en [[log|log]] y cierres por sesión en `raw/sessions/`.
> Set PI vigente en [[00-index|00-index]] § Specs y diagramas nov-2026.

Más nuevo → más arriba.

## Lectura en 1 minuto

- **Studio OS + PI como sistema único**: tabula rasa de Sol → [[specs/261101-tabula-rasa-arquitecto-futuro-pi-os|tabula rasa + PI OS]] → [[specs/261102-plan-maestro-pi-por-temas|plan maestro T1-T9]] → [[specs/261102-system-overview-pi|system overview]] → [[diagramas/pi-system-ingenieria|ingeniería C4 + despliegue + secuencia]] → [[specs/261101-guion-visual-pi-remotion|guion visual + video]] alineado, con **holoarquitecto** como rol que dirige y **un Hermes por estudio**.
- **Concurso Gaudí Nexus**: 7 flujos del curso AI×Gaudí fichados, [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro de workflows adaptados]], matriz txt2img con seed fijo, galería web de 100 renders, 17 LoRAs locales validadas, massing Sagrada + CABA desde fuentes abiertas, [[specs/261102-plan-24h-croquis-lora-laminas|plan 24 h croquis → LoRA → láminas]].
- **Rhino + CAD**: corte A3 1:50 construido y verificado, guía de Section Styles por material, Casa Uruguay con 17 capas y diagnóstico de hatches, scripts de inspección y configuración listos para corrida en Rhino.
- **Infra + Emilia**: VPS verificado y PHP parcheado, Router Emilia con extracción Jina reparada mediante API key, 15 h registradas en Leantime, ruta Telegram → imagen vía Pollinations diseñada para el día siguiente.

## KPIs del período

| Métrica | Valor |
|---|---|
| Sincs a `master` | 4 (21/10, 28/10, 29/10, 30/10) |
| Sesiones registradas en `raw/sessions/` | 39 dentro del rango |
| Specs nuevos del período | 8 (7 PI + plan Gaudí + matriz + filosofía Hermes) |
| Scripts nuevos / ampliados | 30+ (Rhino, ComfyUI, massing OSM/GCBA, dashboards, Leantime, transcripción) |
| LoRAs locales validadas | 17 (9 SD1.5 + 7 SDXL + 1 FLUX curso), con catálogo y WF de calibración |
| Renders trazables en galería | 100 (matriz 14/14 OK en bloque SD1.5 + baseline SDXL) |
| Workflows curso AI×Gaudí | 7 fichas + plan maestro + carpeta [[proyectos/concurso-gaudi-nexus/index|concurso]] |
| Horas Leantime cargadas | 15 h (19–21/10) + 33 cards + 85 subtasks del plan 16/10 |
| Enlaces oficiales verificados | 200+ con chequeo HTTP (guías Rhino, VISION/ESTRUCTURA/REQUISITOS, GUIA-LECTURA) |

## Línea de tiempo por día

| Día | Avance principal |
|---|---|
| 2026-11-02 | Set PI unificado con cross-links + ruta Telegram → Pollinations (flux/sana/turbo/kontext) + índice maestro al 02/11 |
| 2026-11-01 | Tabula rasa Pi + arquitectura PI OS para MVP 2 personas · empresa sintética + meta-arquitecto · guion Remotion alineado · massing CABA con Tejido Urbano GCBA (3020 volúmenes Obelisco) · RealVisXL instalado + baseline R-01 + WF fractal hires + dashboard concurso + plan 24 h · fix Jina Router con API key |
| 2026-10-30 | Filosofía Hermes + grafo 3D · Studio OS con guía de lectura + nombre y dirección Hermes · catenarias Gaudí (research) · dashboard curso + massing earth2rhino3d |
| 2026-10-29 | IMPLEMENTACION-HERMES (SQLite FTS5, Docker, memoria 2200 caracteres) · matriz txt2img + galería web + tabla nodos pago → open source |
| 2026-10-28 | Studio OS delineado: VISION + ESTRUCTURA + REQUISITOS + 8 ADRs + auditoría RunPod + kit F0 · 7 workflows Gaudí + plan maestro + concurso creado · LoRAs locales 17/17 + WF calibración |
| 2026-10-27 | Casa Uruguay: 3D importado + Section Styles + lámina + viewport 1:30 + causa raíz hatch scaling + scripts inspección/configuración |
| 2026-10-26 | Casa Uruguay arrancada desde PDF Arraigada: escala verificada + 17 capas + guía comandos + fix ProgID AutoCAD 26 |
| 2026-10-25 | Corte 3D AIZ en hoja A3 1:50 + playbook unificado |
| 2026-10-22 | VPS: CVE PHP parcheado + SSH verificado + runbook · ruta modelado casa Rhino + reajuste a reunión 09:00 |
| 2026-10-21 | Emilia con flujo propio (voz + agenda + dispatcher) · corpus AI×Gaudí como proyecto compartido · dashboard como puerta · dashboard AutoCAD v2 LT 2027 · propuesta SET_04-URB Barcelona · VPS caído y recuperado |
| 2026-10-20 | LoRA rhino-to-image analizado + research FLUX.2 klein + WF rhino-to-image · Corpus Miro/Archademy + transcripciones Mux 6/7 · 15 h Leantime · Cal.com Emilia + agenda n8n probada end-to-end |
| 2026-10-19 | Planes 16/10 cargados a Leantime (33 cards + 85 subtasks) · guion agente agenda Emilia |
| 2026-10-18 | Ventana de base: Takeout YT + preparación corpus (enlaza con tanda 19–21/10) |

## Por sistema

### 1. PI + Studio OS (núcleo del período)

- [[specs/261101-tabula-rasa-arquitecto-futuro-pi-os|Tabula rasa + PI OS]]: voz primigenia de Sol, Hermes agente único, contrato con `file_ref`, gobernanza A-D, ComfyUI por API, Rhino Hops, FreeCAD+IfcOpenShell, Unreal futuro.
- [[specs/261102-plan-maestro-pi-por-temas|Plan maestro T1-T9]]: reunión→doc, reparto agentes, MCPs, matriz open/pago/cloud/local, L0-L4 con ControlNet, licencias por jurisdicción, firma local Llama, loop moodboard→LoRA, evolución diaria + lámina Gaudí con catenarias.
- [[specs/261102-system-overview-pi|System overview]]: entry points (Telegram/CLI/webhook/cron/API) → Hermes → storage + backends, mapeado a N2 Windows, M20 y nube GPU.
- [[diagramas/pi-system-ingenieria|Ingeniería]]: L2 contenedores con puertos, L3 componentes, despliegue N1-N4 por Tailscale, secuencia sobre-de-tarea, ER, casos C-01 a C-13, máquina de estados, BPMN, journeys, stakeholders.
- [[specs/261101-guion-visual-pi-remotion|Guion visual]]: holoarquitecto, empresa sintética, storyboard 86 s, trazabilidad VISION/ESTRUCTURA/REQUISITOS.
- [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] + ESTRUCTURA + REQUISITOS + [[proyectos/MVP_07-studio-os-sistema/GUIA-LECTURA|GUIA-LECTURA]] con recorridos por tema y preguntas de Emilia.

### 2. Concurso Gaudí Nexus

- 7 fichas en `proyectos/concurso-gaudi-nexus/flujos/` + [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan maestro]] con hitos M-C1 a M-C7, entrega 16/12.
- Matriz txt2img (20 filas, prompt fijo, seed 42) + galería web (`scripts/galeria-renders.py`) + [[specs/261029-matriz-txt2img-galeria-y-publicacion|doc maestro]].
- Catálogo [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]] + WF calibración + 14/14 OK bloque SD1.5.
- Massing: earth2rhino3d (OSM/CADMapper) para Sagrada + Tejido Urbano GCBA para CABA (EPSG:4326, 3020 volúmenes Obelisco, builder Rhino listo).
- Research catenarias/cáscaras/tensadas + reinterpretación programa fractal + [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz de pruebas concurso]] + `scripts/dashboard-concurso.py`.
- [[specs/261102-plan-24h-croquis-lora-laminas|Plan 24 h]] + research modelos imagen n8n Telegram (24 motores, costos y licencias al 01/11).

### 3. Rhino + AutoCAD

- AIZ: hoja A3 1:50 verificada (1 m = 20 mm en papel), playbook unificado.
- Casa Uruguay: import DWG/PDF a escala real, 17 capas con Section Style, lámina aparte, viewport 1:30, checklist 7 puntos para hatch en detalle, fórmula `Pattern Scale` y causa raíz `Model space hatch scaling`.
- Scripts: `inspeccionar-seccion-rhino.py`, `configurar-corte-hatch-rhino.py`, `cortes-plaza-rhino.py`, massing Sagrada/CABA, cheercheet ampliado, URLs verificadas.

### 4. Infra, Emilia, gestión

- VPS Contabo: LEANTIME 3.12.0 + PHP 8.3.36, 12 servicios Swarm, runbook + pbks monitoreo/alertas, backup 3-2-1 documentado.
- n8n Emilia: voz propia + agenda propia + dispatcher por `chat_id`, Cal.com 3 event types, extracción Jina reparada (500 RPM por key, ack con aviso de completado manual).
- Leantime: 33 cards + 85 subtasks + 15 h, RPC documentado con ajuste de fecha.
- Telegram → imagen: Pollinations como vía operativa (clásico anónimo + key `sk_` con grants Pollen), pipe de 3 nodos listo para armar.

## Trabajo en working tree, listo para próximo commit

- Diagramas PI (`arquitectura-pi-os`, `pi-bpmn`, `pi-casos`, `pi-er`, `pi-journeys`, `pi-maquina`, `pi-stakeholders`, `pi-system-ingenieria-*`).
- Specs 261101–261102 (tabula rasa, plan maestro, overview, guion, plan 24 h, doc ChatGPT, plan continuación).
- Scripts massing CABA, cortes plaza, dashboards concurso/curso, auditoría presentación PI.
- Research Gaudí catenarias + massing CABA + modelos imagen Telegram.
- Sesiones 30/10–02/11 con cierres completos.

## Oportunidades del siguiente ciclo

1. Localizar el dashboard solo-imágenes del concurso y enlazarlo desde [[proyectos/concurso-gaudi-nexus/index|concurso]].
2. Crear key Pollinations `sk_` y correr primera imagen por navegador, luego pipe n8n de 3 nodos.
3. Correr builder massing CABA dentro de Rhino 8 mediante `_RunPythonScript` directo.
4. Cerrar tanda de calibración LoRAs (32 renders, arranque con SD1.5 strength 0,8).
5. Activar RunPod para FLUX.2 klein 9B + LoRA rhino-to-image y tanda fractal hires v2 con refiner 0,55 + tiles + ESRGAN.
6. Completar filas Fuentes-Inbox con título pendiente y publicar set PI (commit + push).

## Trazabilidad

- Fuente diaria: [[log|log]] (entradas 2026-10-19 → 2026-11-02).
- Sesiones: `raw/sessions/2026-10-19-*` → `raw/sessions/2026-11-02-sesion-telegram-pollinations.md`.
- Specs noviembre: [[specs/261101-tabula-rasa-arquitecto-futuro-pi-os|tabula rasa]] · [[specs/261102-plan-maestro-pi-por-temas|plan maestro]] · [[specs/261102-system-overview-pi|overview]] · [[specs/261101-guion-visual-pi-remotion|guion]] · [[specs/261102-plan-24h-croquis-lora-laminas|plan 24 h]] · [[specs/261101-doc-chatgpt-diseno-pi-os|doc ChatGPT]] · [[specs/261030-plan-continuacion-pruebas|plan continuación]].
- ComfyUI: [[proyectos/MVP_04-comfyui-arquitectura/readme-mvp_04|MVP_04]] · [[wiki/glosario/software/lora-locales-comfyui|lora-locales]] · [[wiki/glosario/software/proveedores-modelos-ia|proveedores modelos]].
- Studio OS: [[proyectos/MVP_07-studio-os-sistema/VISION|VISION]] · [[proyectos/MVP_07-studio-os-sistema/GUIA-LECTURA|GUIA-LECTURA]].
