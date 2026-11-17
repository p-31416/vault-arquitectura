---
tipo: plan
proyecto: concurso-gaudi-nexus
titulo: Veredicto Comfy vs Open Higgsfield — pod en rafagas gana
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
estado: borrador-activo
tags: [concurso, comfyui, open-higgsfield, runpod, costos, veredicto, gratis]
idioma: es
---

# Veredicto Comfy vs Open Higgsfield

> Relacionado: [[specs/261028-plan-workflows-adaptados-curso-ai-gaudi|plan workflows]] · [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] · [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz pruebas]] · [[specs/261112-plan-lamina-1000x700|plan lamina A1]].

## 1. Veredicto en una linea

Gana Comfy en rafagas $0-6. Pod prendido 16hs pierde. Open Higgsfield solo sirve como benchmark puntual.

## 2. Costos verificados

| Ruta | Costo | Nota |
|---|---|---|
| Local RX 570 | $0 + luz | RealVisXL Lightning 4-6 pasos, SD1.5, ControlNet |
| RunPod 3090 Community | $0.22/h | 64hs on = $14/mes idle |
| RunPod 4090 | $0.34/h | 64hs on = $22/mes idle |
| Matriz concurso 59 corridas | ~5.5hs GPU = $5-6 total | no mensual, por concurso |
| Open Generative AI (MuAPI) | imagen $0.01-0.15, clip 5s 720p ~$1.7, 1080p ~$3-4 | programa $0, generacion paga siempre |
| Open Higgsfield API | USD por generacion | saldo separado de suscripcion |
| Comfy Cloud Standard / Creator | $20 / $35 mes | no importa LoRA propio en Standard, no entrena |
| Comfy Cloud Free | $0, 400cr ~25min GPU | calibracion oficial del curso |
| Pollinations keyed | flux 0 Pollen, kontext ~200, nanobanana ~50 | borrador $0 |
| Kaggle | ~30hs/sem T4x2 | tandas pesadas $0 |

## 3. Por que pod on 16hs sale caro

Pagas silla aunque Telegram este idle. 16hs/sem x 4 = 64hs con GPU cobrando sin generar. Solucion: separar construccion (local $0) de computo (pod solo en lote 10-20 variantes + auto-stop 5 min).

## 4. Por que Open Higgsfield no es gratis en pod

El pod solo hospeda la pagina. Al generar llama a MuAPI / Higgsfield con tu key. Sin saldo no genera. Excepcion: modo Local sd.cpp solo imagen chica, video cine queda fuera en RX 570.

## 5. Break-even

- <50 img/mes esporadicas: local + Pollinations free gana.
- 50-200 img con inpaint/mascara: pod rafagas gana a Open Higgsfield.
- Pod always-on idle: pierde contra todos.

## 6. Arquitectura recomendada ($0 base)

1. Local valida grafo con proxy chico (512px, Lightning).
2. Bot chico always-on $0 (PC o VPS free) recibe Telegram, guarda foto+mascara+caption.
3. Bot prende pod por API solo al generar, cola via ComfyUI API, devuelve imagen, auto-stop.
4. Open Higgsfield solo 5 renders techo para comparar.

## 7. Gate

- G0: este veredicto aprobado por Sol.
- G1: bot wake-on-demand + 1 lote test 10 img registrado en `02-WF-log` con costo real.
