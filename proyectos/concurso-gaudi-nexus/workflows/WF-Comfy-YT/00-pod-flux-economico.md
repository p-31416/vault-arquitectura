---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, runpod, pod, flux, costos]
idioma: es
---

# 00 — Pod Flux al menor costo posible (con n8n en el VPS)

> Complemento de [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-runpod-comfyui|00 — ComfyUI en un pod]]. Ese documento explica cómo montar el pod; este explica cómo pagarlo menos corriendo Flux (klein 9B + LoRA del curso, o FLUX.1 dev). Precios oficiales Runpod al 28-10-2026: https://www.runpod.io/pricing. Regla de oro: **el minuto de GPU manda; el disco parado también factura**.

## 1. Qué GPU mínima pide cada Flux

| Modelo | VRAM (fuente) | GPU más barata que lo contiene | Precio community/h |
|---|---|---|---|
| FLUX.2 klein 9B (+ LoRA `rhino-to-image`) | ~24 GB (BFL) | RTX A5000 24 GB | **$0,16** |
| FLUX.2 klein 9B, con prisa | ~24 GB (BFL) | RTX 4090 24 GB | $0,34 |
| FLUX.2 klein 9B, con holgura | ~24 GB (BFL) | RTX A6000 48 GB | $0,33 |
| FLUX.1 dev (fp8, práctica estándar) | 24 GB | RTX A5000 24 GB | **$0,16** |
| FLUX.2 klein 4B (sin LoRA: otra arquitectura) | ~13 GB (BFL) | RTX 4080/5080 16 GB | ~$0,19–0,34 |

Secure Cloud multiplica ×2,5 aprox (4090: $0,89). Community alcanza para este trabajo; Secure queda para cliente final o volumen de red.

## 2. Receta barata (una vez, después es repetir)

1. **GPU**: RTX A5000 community on-demand ($0,16/h). Si no hay stock, 4090 community ($0,34/h). Spot solo para batch: te pueden reclamar la máquina a mitad de corrida.
2. **Template**: oficial ComfyUI estándar (Blackwell solo si la GPU es 5090/B200).
3. **Discos**: container 30 GB + **volume disk 100 GB** (modelos + LoRA + salidas). Los modelos se descargan **una sola vez** al volume disk.
4. **Modelos** (ver §5 de [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]]): base fp8 + text encoder + VAE + LoRA. Reservar ~50 GB para el set Flux.
5. **Ciclo de vida**: trabajar → **stop** (no terminate) entre sesiones del mismo sprint; **terminate** al cerrar el sprint con todo exportado. Ojo al truco de la lista oficial: el volume disk parado sale $0,20/GB/mes (más que corriendo); 100 GB parados un mes ≈ $20. Para pausas largas, pasar a network storage ($0,07/GB/mes) o borrar.

## 3. Costo por sesión (estimado, A5000 community)

Boot 3 min + trabajo 10 min ≈ 13 min × $0,16/h ≈ **$0,035 por sesión** más centavos de disco. Una tarde de 10 sesiones ronda los $0,40. La cuenta pide saldo para cubrir 1 h al desplegar; la facturación real es por segundo y el egress es gratis.

## 4. n8n en el VPS como mayordomo del pod

n8n corre en el VPS del estudio (no en local). El ahorro real sale de que **n8n prenda y apague el pod solo**:

```
n8n (VPS) → Runpod API: arrancar pod → poll proxy hasta 200 (/system_stats)
  → POST /prompt con el JSON del WF → poll /history → GET /view (salida)
  → guardar + avisar por Telegram → stop del pod
```

Endpoints ComfyUI usados: `/prompt`, `/history`, `/view`, `/system_stats`. La API key de Runpod vive en las credenciales de n8n, nunca en el grafo. Con este ciclo el pod solo factura los minutos de trabajo real; el resto del día vale $0 de GPU.

## 5. Cuándo no usar pod

- Edición puntual sin LoRA propio: endpoints públicos por request (FLUX.1 dev $0,02/MP · Kontext dev $0,025 · Nano Banana Edit $0,038).
- Ráfagas esporádicas: serverless (workers 24 GB ≈ $1,34/h solo mientras ejecutan).
- Todo lo SDXL/SD1.5: la RX 570 local, costo $0.

## 6. Checklist del sprint Flux

1. Volume + modelos una vez; verificar con `/system_stats` (VRAM libre antes de encolar).
2. Exportar cada JSON que funcione a local antes del stop.
3. n8n con ciclo start→run→stop; alerta si el pod sigue corriendo pasada la ventana.
4. Terminate al cerrar el sprint; la próxima sesión re-despliega sobre lo exportado.

## Referencias

- Precios oficiales (verificado 2026-11-02): https://www.runpod.io/pricing
- Tutorial oficial pods: https://docs.runpod.io/tutorials/pods/comfyui
- klein 4B/9B VRAM y límites (BFL): https://help.bfl.ai/articles/7592221790-how-do-i-generate-quickly-with-flux-2-klein
- Piezas Flux del estudio: [[proyectos/concurso-gaudi-nexus/WF-curso/00-modelos-sdxl-a-probar|00-modelos-sdxl-a-probar]] §5
- Costos y n8n: [[raw/research/2026-11-01-modelos-imagen-n8n-telegram|research 2026-11-01]]
