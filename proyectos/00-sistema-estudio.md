---
tipo: metodologia
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [sistema, estudio, vault, autocad, comfyui, seguridad, agentes]
---

# Sistema del estudio — una persona, máquina + agente, en 3 meses

> Documento a nivel vault: aplica a todos los proyectos. Lo que se construye en este trimestre es el sistema que permite que **una persona** opere revisión de planos, planillas y renders con partes automatizadas, iterando en local y con el agente corriendo pruebas sistematizadas sobre procesos ya mapeados. Al cerrar, el sistema queda en funcionamiento y seguro.

## 1. AutoCAD: lo medido y lo que sigue

Logros ya en funcionamiento ([[proyectos/MVP_02-autocad-standards/01-spec-mvp_02|MVP_02]]):

- **Cuadro de carpinterías** extraído de atributos (20 ventanas + 22 puertas) a CSV y planilla en Sheets vía webhook: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/cuadro-carpinterias|cuadro-carpinterias]]
- **Planilla de locales** (28 locales) y **planilla de niveles** dibujada por LSP desde CSV: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/planilla-locales|planilla-locales]] · [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/planilla-niveles|planilla-niveles]]
- **Ahorro por plano futuro: ~12-15 h**, payback en el primer plano completo: [[proyectos/MVP_02-autocad-standards/SET_01-REP_Replanteo/docs/desglose-configuraciones|desglose-configuraciones]]

Lo que sigue: puertas, ventanas y metros lineales resueltos en AutoCAD; IFC/BIM después, cuando el cómputo 2D quede cerrado.

## 2. El sistema se alimenta de información

Cada plano, detalle de baño, detalle de cocina o planilla que entra al vault vuelve como capacidad: el sistema recopila y extrapola a otros niveles en vez de quedarse en el caso puntual. La planilla de carpinterías de hoy es la planilla de cualquier rubro de mañana.

## 3. Comfy: sello personal sobre procesos mapeados

Comfy rinde cuando recibe el sello del estudio, y el sello se construye mapeando procesos —que es lo que hace [[proyectos/concurso-gaudi-nexus/workflows/00-conclusiones|00-conclusiones]]—: sketch→render, render→sketch, animación, cada uno con su camino correcto (qué checkpoint + qué LoRA + qué venue). Una vez mapeado, el camino se repite y se mide.

## 4. Costo: punto único humano + agente

Una cuenta Cloud por persona escala el mantenimiento (el orden que maneja el estudio: ~USD 120/mes); en cambio un **punto único** al que se conectan el humano y el agente mantiene el costo fijo y la base compartida. Venues y números: [[proyectos/concurso-gaudi-nexus/workflows/00-conclusiones|00-conclusiones]] §6 · [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]].

## 5. Agente: pruebas sistematizadas, revisión humana

Con la base mapeada, el agente repite exactamente el mismo flujo (un plano de tal tipo, una serie de seeds, una variable por corrida) y extrapolation queda registrada en la matriz. Toda corrida pide revisión: HITL es el gate, nunca el trámite.

## 6. Seguridad: local itera, el pod se borra, la nube se audita

Regla madre: **el material con propiedad intelectual no sale a nubes cuyo uso de datos no esté auditado**. Se itera en la máquina; el pod se usa y se borra sin dejar rastro; cada servicio nuevo pasa por la auditoría antes de recibir material sensible. Fundamento: [[wiki/estudio/decision-arquitectura-ia-privacidad|decision-arquitectura-ia-privacidad]] · [[raw/research/2026-10-28-runpod-auditoria-pi|auditoría RunPod]] · [[proyectos/concurso-gaudi-nexus/lora-estudio-plan|lora-estudio-plan]] §6 (bordes legales del dataset).

## 7. Cuenta pendiente: marca de agua + envío automático

Las imágenes con derecho de autor viven en la nube propia, con el sistema propio. Cuando una imagen o PDF sale hacia un mail, sale con **marca de agua en la calidad que pide el destino**, puesta automáticamente: el pedido en lenguaje natural ("mandame el proyecto tal") dispara marca + adjunto + envío sin pasos manuales.

Flujo listo (imágenes): [[proyectos/MVP_04-comfyui-arquitectura/n_08-marca-agua/WF-marca-agua/00-README|WF-marca-agua]] — overlay de PNG con transparencia, posición y opacidad regulables. El PDF va por script/n8n (Comfy no lee PDF): ver backlog del flujo.

## 8. Cierre del trimestre

Sistema en funcionamiento: una persona revisa planos, saca planillas y produce renders con partes automatizadas; el agente prueba sobre lo mapeado; todo corre en superficies auditadas. Eso es lo que estos tres meses dejan instalado.
