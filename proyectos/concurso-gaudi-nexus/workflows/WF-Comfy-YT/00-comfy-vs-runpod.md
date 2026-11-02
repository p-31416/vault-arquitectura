---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, runpod, comfy-cloud, costos, decision]
idioma: es
---

# 00 — Comfy $20 vs RunPod: guía paso a paso y costo final

> Responde a la pregunta del estudio: ¿pago los $20 de Comfy o armo pod en Runpod? Datos oficiales al 02-11-2026: https://comfy.org/pricing/ y https://www.runpod.io/pricing. Matiz a tu hipótesis: en Comfy Cloud **sí** funcionan los custom nodes más usados; lo que no entra es tu nodo raro/propio ni (en Standard) tu LoRA.

## 1. Tabla comparativa

| | Comfy Standard $20/mes | RunPod community (A5000) |
|---|---|---|
| Precio | $20 fijos (o $16 con año) | $0,16/h, por segundo, sin mínimo mensual |
| GPU incluida | RTX PRO 6000 96 GB | RTX A5000 24 GB (suficiente para klein 9B) |
| Horas por $20 | **≈ 5,7 h** (4.200 créditos ÷ 736,39/h) | **≈ 125 h** |
| Custom nodes | solo los más usados | cualquiera, incluidos los tuyos |
| LoRA/modelo propio | **no** (solo Creator $35+ y solo desde Civitai/HF) | cualquiera (el `rhino-to-image` local incluido) |
| n8n por API | 1 workflow concurrente | sin límite (tu key, tu pod) |
| Tiempo máx. por corrida | 30 min | el que pagues |
| Créditos no usados | vencen cada mes | no hay créditos: pagás lo usado |
| Uso comercial | incluido | incluido |
| Setup | cero | 10 min la primera vez |

## 2. Paso a paso A — Comfy Standard ($20)

1. Cuenta en https://comfy.org → probar gratis (5 runs en GPU real, sin tarjeta para el trial).
2. Standard mensual; los 4.200 créditos caen cada ciclo (no se acumulan: lo no usado se pierde).
3. Subir tu workflow o usar un template; verificar que tus custom nodes estén entre los soportados antes de asumir nada.
4. Encolar; solo el tiempo activo de GPU descuenta créditos (armar el grafo no cuesta).
5. Si te quedás corto: top-up (dura 1 año) o subir a Creator ($35, recién ahí entra LoRA propio desde Civitai/HF).

Límites que duelen: 30 min por corrida, 1 concurrente por API, 100 en cola.

## 3. Paso a paso B — RunPod mínimo (resumen)

Detalle completo en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-flux-economico|00 — Pod Flux económico]]:

1. A5000 community + template oficial ComfyUI + volume disk 100 GB.
2. Modelos una vez; trabajar; **stop** entre sesiones; terminate al cerrar el sprint.
3. n8n en el VPS con ciclo start→run→stop (el pod solo factura minutos reales).

## 4. Costo final por escenario del estudio (estimado)

Sesión tipo Flux: boot 3 min + 10 min de trabajo ≈ 13 min.

| Escenario mensual | Comfy Standard | RunPod A5000 $0,16/h |
|---|---|---|
| 10 sesiones Flux (≈ 2 h GPU) | $20 (sobran créditos, se pierden) | **≈ $0,35** |
| 40 sesiones concurso (≈ 9 h GPU) | $20 + top-up (~$7) ≈ **$27** | **≈ $1,50** |
| Solo partner ocasional (Nano Banana) | $20 o pay-as-you-go con créditos | n/a (API, no pod) |

La hora vale ~$3,50 en Comfy contra $0,16–0,34 en Runpod: ~20× por sesión. El $20 fijo solo cierra si usás las 5,7 h todos los meses en workflows estándar.

## 5. Recomendación para el estudio

1. **Fase G (klein 9B + LoRA `rhino-to-image`) va en pod sí o sí**: el LoRA es un archivo local y Comfy ni siquiera en Creator lo aceptaría (solo Civitai/HF). No hay decisión acá.
2. **Comfy $20 como complemento**, no como base: partner nodes (Nano Banana), batch estándar sin setup, Comfy Cloud nodes (Flux 2 T2I y otros 7 fijos) que corren **sin suscripción**, solo con créditos, para pruebas sin LoRA.
3. **Si un mes no tocás Flux**, no pagues el fijo: RunPod cobra $0 parado (pod terminado y todo exportado) y Comfy vende top-ups sueltos que duran un año.
4. Todo lo SDXL/SD1.5 sigue en la RX 570 a $0; el pod es solo para lo que no entra en 8 GB.

## Referencias

- Precios Comfy (verificado 2026-11-02): https://comfy.org/pricing/
- Precios Runpod (verificado 2026-11-02): https://www.runpod.io/pricing
- Pod barato + n8n mayordomo: [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-flux-economico|00 — Pod Flux económico]]
- Pod general: [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-runpod-comfyui|00 — ComfyUI en un pod]]
