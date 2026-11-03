---
tipo: guia
proyecto: concurso-gaudi-nexus
titulo: Pod ComfyUI unificado — montar, pagar, instalar, decidir y automatizar
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
estado: vigente
tags: [concurso, gaudi-nexus, comfyui, runpod, pod, flux, costos, n8n]
idioma: es
---

# Pod ComfyUI unificado — montar, pagar, instalar, decidir y automatizar

> Unifica en un solo archivo (pedido Sol 2026-11-02) los 5 documentos `pod-`/`comfy-vs`/`n8n-ciclo` de `WF-Comfy-YT`: conceptos + instalación paso a paso + costo Flux + comparativa Comfy Cloud + ciclo n8n. Esos 5 quedan superseded — no editarlos, solo este.
> Puerta: [[proyectos/concurso-gaudi-nexus/workflows/00-index|workflows/00-index]] · LoRA que corre acá: [[proyectos/concurso-gaudi-nexus/lora-estudio-plan|lora-estudio-plan]].

## 1. Conceptos (ex 00-pod-runpod-comfyui)

Video base: DorianAI "How to Connect n8n to ComfyUI on Runpod" (35 min, 2025-06-16): `https://www.youtube.com/watch?v=RgrEAge_5Kk` — guardado por Sol con playlist ítem 19 para unirlo a n8n: `https://www.youtube.com/watch?v=RgrEAge_5Kk&list=PLmQpFKkkTXQFj2NLaW8H1wjwQYGCbdZnc&index=19`. Pasos con timestamps originales: cuenta (05:18) + pod con disco permanente (06:00) + ComfyUI puerto 8188 (11:38) + modelos imagen (14:10) + modelos API/LoRAs (18:58) + n8n VPS (23:58) + advertencia ARM (32:00). Script autor (Google Doc): `https://docs.google.com/document/d/110wJjV7_SbBlvRaRzkZThvUt7a9J-yH_7Fh2QIm0WTs/edit?usp=sharing`. No usar ARM.

Actualización 2026: precio $0.15/h ya no existe (4090 on-demand ≈ $0.74/h, comunidad $0.34/h); cuenta pide $10 mín. Usar **template oficial** (`runpod/comfyui`, Blackwell Edition solo 5090/B200): `https://docs.runpod.io/tutorials/pods/comfyui`. Storage: container se recrea, volume sobrevive stop pero se cobra parado y se borra con terminate, **network volume es lo único permanente** (`/workspace`). Running ≠ listo: secuencia `404 → 502 → 200`, primer boot hasta 30 min. URL: `https://[POD_ID]-8188.proxy.runpod.net`. ComfyUI 0.26.2+, torch 2.10+cu128, Python 3.12. Atajo estudio: despliegue MCP con dead-man switch. Comfy Cloud solo si no hay LoRA propio.

## 2. Instalación paso a paso desde cualquier PC (ex 00-pod-instalar)

Resultado: URL ComfyUI en navegador, modelos persistentes, PC libre. Requisitos: cuenta runpod.io + saldo 1 h.

1. console.runpod.io → Deploy → GPU **A5000 community $0.16/h** (klein 9B entra) o 4090 $0.34/h con prisa → template oficial ComfyUI → container 30 GB + **volume 100 GB** → Deploy On-Demand.
2. Esperar 200 (no re-desplegar).
3. Connect → HTTP 8188 → bookmark URL (privada, no compartir).
4. Modelos una vez al volume: Manager → Model Manager o terminal a `ComfyUI/models/<carpeta>/` → refresh R.
5. Custom nodes: Manager → Install → reiniciar desde Manager.
6. Workflows: arrastrar `.json`/PNG → encolar → descargar → **exportar JSON a PC antes del stop**.
7. Stop entre sesiones; terminate solo con todo exportado.

Fallas: Bad Gateway = boot en curso; sin stock = otra GPU/región; modelo no aparece = R + carpeta; nodo no aparece = reinicio; disco parado factura = terminate si pausa larga.

## 3. Pod Flux al menor costo (ex 00-pod-flux-economico)

| Modelo | VRAM | GPU barata | $/h community |
|---|---|---|---|
| klein 9B + LoRA | ~24 GB | A5000 24 GB | **0.16** |
| klein 9B con prisa | ~24 GB | 4090 | 0.34 |
| klein 9B holgura | ~24 GB | A6000 48 GB | 0.33 |
| klein 4B | ~13 GB | 4080/5080 16 GB | 0.19–0.34 |

Secure ×2.5 (4090 $0.89): solo cliente final. Receta: A5000 on-demand (spot solo batch) + template oficial + volume 100 GB (modelos Flux ~50 GB una vez) → trabajar → stop / terminate al cerrar sprint. Ojo: volume parado $0.20/GB/mes (100 GB ≈ $20/mes parado); pausas largas → network storage $0.07/GB o borrar. Sesión 13 min ≈ **$0.035** + disco; tarde 10 sesiones ≈ $0.40. Cuando no usar pod: endpoints por request (dev $0.02/MP), serverless, y todo SDXL/SD1.5 en RX 570 $0. Entrenar klein 4B ai-toolkit ≈ $0.50–0.70/corrida vs Civitai on-site 500 Buzz (dataset en su storage 30 días): concurso → pod.

## 4. Comfy $20 vs RunPod (ex 00-comfy-vs-runpod)

| | Comfy Standard $20 | RunPod A5000 |
|---|---|---|
| Precio | $20 fijos (4200 créditos ≈ 5.7 h) | $0.16/h por segundo |
| GPU | PRO 6000 96 GB | A5000 24 GB (alcanza klein 9B) |
| Custom nodes | solo comunes | cualquiera |
| LoRA propio | no (Creator $35+ solo Civitai/HF) | cualquiera (rhino-to-image local incluido) |
| Concurrencia/tiempo | 1 API, 30 min/corrida | sin límite |
| Créditos | vencen | no hay |

Costo estudio: 10 sesiones ≈ $20 vs **$0.35** pod; 40 sesiones ≈ $27 vs **$1.50**. Recomendación: **Fase G klein 9B + LoRA va en pod sí o sí**; Comfy $20 solo complemento (partner nodes, batch estándar, nodos fijos sin suscripción). Mes sin Flux = no pagar fijo.

## 5. n8n VPS mayordomo start→run→stop (ex 00-n8n-ciclo-pod)

Sin esto el ahorro se pierde en pods olvidados. Arquitectura todo HTTP: n8n VPS → Runpod API v2 (start/stop) → proxy ComfyUI (`/prompt`, `/history`, `/view`, `/system_stats`) → Telegram Send aviso. Key en credenciales n8n, nunca en grafo. API v2 vigente (v1 se retira 15-11-2026).

| Paso | Método + URL | Body |
|---|---|---|
| Arrancar/parar | `POST https://api.runpod.io/v2/pods/{ID}/action` | `{"action":"start"}` / `"stop"` |
| Terminar | `DELETE https://api.runpod.io/v2/pods/{ID}` | — |
| ¿Listo? | `GET https://[ID]-8188.proxy.runpod.net/system_stats` | 200 = listo |
| Encolar | `POST .../prompt` | `{"prompt":{grafo API},"client_id":"..."}` |
| Estado | `GET .../history/{PROMPT_ID}` | outputs = listo |
| Descargar | `GET .../view?filename=...&subfolder=...&type=output` | binario |

Nodos n8n: Trigger manual/schedule → HTTP start → loop Wait 30 s + system_stats (tope ~15) → HTTP prompt (guardar prompt_id) → loop history (tope ~5 min klein) → view + Telegram → **HTTP stop siempre incluso en error**. Probar a mano (curl/test) antes de conectar. Ciclo 13 min ≈ $0.035; pod olvidado un día ≈ $3.80.

## Checklist operativo único

1. Network volume 100–200 GB en región con GPU → deploy template oficial + volume + 1 GPU on-demand.
2. Esperar 200 → instalar checkpoint + LoRAs **en volumen** una vez → verificar `/system_stats`.
3. Probar workflows, exportar cada JSON a local.
4. n8n start→run→stop con alerta si sigue corriendo.
5. Stop entre sesiones; terminate al cerrar sprint con respaldo.

## 6. Flux cuantizado en hardware local RX 570 8 GB (veredicto 2026-11-02)

Respuesta corta: **existe (GGUF Q4 ~6.8 GB) pero NO es viable en la RX 570 por DirectML**.

- Qué existe (verificado multi-fuente 2026): FLUX.1-dev Q4_K_S (~6.8 GB) y FLUX.2 klein 4B Q4 (~2.6 GB, Apache 2.0, 4 pasos) vía `city96/ComfyUI-GGUF` + T5 cuantizado + `--lowvram`. En NVIDIA 8 GB (3060/4060) corre lento pero corre.
- Por qué acá no: el loader GGUF tiene soporte débil en ROCm/DirectML frente a CUDA (fuente 2026-05 verificada); en AMD el camino fiable es SDXL. Además el nodo `ComfyUI-GGUF` **no está instalado** en `P:\00-repos\ComfyUI\custom_nodes` (solo IC-Light + IPAdapter) y no hay ningún `.gguf` en checkpoints (solo Juggernaut v9, RealVisXL v5.0 + Lightning, inpainting SD1.5).
- En 8 GB el error típico es cargar el T5 fp16 (~9 GB) en vez del GGUF cuantizado; y con CPU i5-4460 el offload sería impracticable.
- Decisión: Flux (sea fp8, GGUF o klein 9B) va en **pod** (§3); local queda SDXL (Lightning para iterar, RealVis/Juggernaut para final). Si algún día se prueba GGUF local, el candidato es klein 4B Q4 (~2.6 GB) + instalar el nodo + T5 GGUF, como experimento, no como vía de producción.

## Referencias verificadas

- Tutorial oficial pods (verificado 2026-11-02): `https://docs.runpod.io/tutorials/pods/comfyui`
- Precios Runpod (verificado 2026-11-02): `https://www.runpod.io/pricing`
- Precios Comfy (verificado 2026-11-02): `https://comfy.org/pricing/`
- Volumes: `https://docs.runpod.io/storage/network-volumes` · Manage pods: `https://docs.runpod.io/pods/manage-pods` · Migración v2: `https://docs.runpod.io/api-reference-v2/migrate-from-v1`
- klein VRAM/límites BFL: `https://help.bfl.ai/articles/7592221790-how-do-i-generate-quickly-with-flux-2-klein`
- Video origen: `https://www.youtube.com/watch?v=RgrEAge_5Kk`

---
*Más nuevo → más arriba. Log: 2026-11-02 unificación 5→1 desde pedido Sol. Supersede: `WF-Comfy-YT/00-pod-runpod-comfyui`, `00-pod-flux-economico`, `00-pod-instalar-comfy-paso-a-paso`, `00-comfy-vs-runpod`, `00-n8n-ciclo-pod`.*
