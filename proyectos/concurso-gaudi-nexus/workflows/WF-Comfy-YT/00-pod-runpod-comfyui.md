---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, runpod, pod, infraestructura]
idioma: es
---

# 00 — ComfyUI en un pod (Runpod): guía + notas de mejora 2026

> Documento fundacional de [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-index|WF-Comfy-YT]]: antes de probar flujos de YouTube con GPU seria (Flux klein, WAN, LTX), el pod tiene que existir, persistir y apagarse sin tirar plata. Sigue al video y lo actualiza a noviembre 2026.

## 1. Video de referencia

- Título: "How to Connect n8n to ComfyUI on Runpod | $0.15 for 24GB VRAM | Step-By-Step Tutorial"
- Canal: DorianAI · 2025-06-16 · 35 min · https://www.youtube.com/watch?v=RgrEAge_5Kk (ítem 19 de la playlist)
- Objetivo del video: ComfyUI auto-hospedado en Runpod + conectado a n8n para automatizaciones. Incluye NocoDB en un VPS (no necesario para el estudio).
- Script del autor (Google Doc): https://docs.google.com/document/d/110wJjV7_SbBlvRaRzkZThvUt7a9J-yH_7Fh2QIm0WTs/edit?usp=sharing

## 2. Pasos del video (junio 2025)

| # | Paso (timestamps) | Qué hace |
|---|---|---|
| 1 | Cuenta en Runpod (05:18) | registro + créditos |
| 2 | Pod con almacenamiento permanente (06:00) | GPU 24 GB + volumen para que los modelos sobrevivan |
| 3 | Correr ComfyUI (11:38) | levantar el servicio web en el puerto 8188 |
| 4 | Descargar modelos de imagen (14:10) | checkpoints al pod |
| 5 | Modelos por API + LoRAs (18:58) | nodos partner y LoRAs |
| 6 | Conectar n8n del VPS (23:58) | automatización R3 en la nube |
| 7 | Advertencia ARM (32:00) | no usar arquitectura ARM (error de NCA Toolkit) |

## 3. Notas de mejora — qué cambió en un año

### 3.1 Precio: el $0,15 ya no es la referencia

El título promete $0,15/h por 24 GB: era tarifa spot/comunitaria de 2025. Hoy el rango real es:

- RTX 4090 on-demand ≈ $0,74/h (verificado ago-2026); el estudio presupuesta ≈ $0,39/h según disponibilidad.
- La cuenta pide mínimo $10 en créditos para arrancar.
- Regla de oro que el video insinúa y hoy es mandamiento: **stop al terminar** (el pod parado con volume disk sigue cobrando disco; terminado sin network volume borra todo). Bajar los workflows a local antes de terminar.

### 3.2 No armar el pod a mano: usar el template oficial

El video construye el entorno paso a paso; hoy existen **templates oficiales** que traen ComfyUI + Manager auto-arrancando:

- GPUs estándar (RTX 4090, L40, A100): template **ComfyUI** (`runpod/comfyui`).
- GPUs Blackwell (RTX 5090, B200): template **ComfyUI Blackwell Edition** (CUDA 13; la imagen estándar no es compatible).
- Tutorial oficial vigente: https://docs.runpod.io/tutorials/pods/comfyui

### 3.3 Storage: tres capas, una sola que sobrevive al terminate

- **Container disk**: se recrea en cada boot (60–90 s); lo de afuera de `/workspace` se pierde.
- **Volume disk**: sobrevive a stop/restart, se cobra parado, **se borra con terminate**.
- **Network volume**: lo único permanente entre pods; montado en `/workspace`; atado a un datacenter (el pod debe desplegarse en la misma región) y solo en Secure Cloud. Modelos, LoRAs y workflows van acá.
- Layout del template oficial bajo `/workspace`: instalación + `ComfyUI/models/*`. Todo lo que cueste descargar vive en el volumen.

### 3.4 Readiness: Running no es listo

Secuencia normal de un pod nuevo: `404 → 502 → 200`. Primer boot hasta ~30 min (imagen fría o con volumen: ~4 min; imagen cacheada sin volumen: ~20 s). No reiniciar porque "no abre": esperar y refrescar. ComfyUI expone en `https://[POD_ID]-8188.proxy.runpod.net`.

### 3.5 Versiones 2026

ComfyUI 0.26.2+, torch 2.10+cu128, Python 3.12 (template CUDA 12.8); template CUDA 13 solo para Blackwell. Si un workflow del 2025 falla con nodos viejos, actualizar el template antes de tocar el grafo.

### 3.6 El atajo del estudio: desplegar con la herramienta propia

El MCP trae despliegue en un paso con el template comfyui-mcp (panel + Manager preinstalados):

- Crear/conectar/vigilar el pod sin consola, con **dead-man switch** (el pod se apaga solo si se pierde el contacto: fin del "me olvidé el pod prendido").
- `watch`/`troubleshoot` para saber por qué un pod no responde antes de reintentar a ciegas.
- `use_local` para volver a la RX 570 cuando el trabajo vuelve a ser SDXL.

Ver comandos en el research de modelos y precios del estudio.

### 3.7 Alternativa sin pod: Comfy Cloud

Si el flujo usa nodos partner + LoRAs propios, Comfy Cloud (planes Creator/Pro/Team) importa LoRAs propios; el plan básico no. Para Flux klein + `rhino-to-image` el pod sigue siendo el camino (Fase G del plan).

### 3.8 n8n: en este estudio corre en el VPS

El paso 6 del video conecta n8n corriendo en un VPS, que es exactamente el setup del estudio. El detalle fino y el ciclo start→run→stop están en [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-flux-economico|00 — Pod Flux económico]] §4.

### 3.9 ARM: la advertencia sigue vigente

Plantillas x86_64 siempre; ARM da el mismo error de toolkits que en el video.

## 4. Checklist operativo (10 min, una vez aprendido)

1. Crear network volume (100–200 GB) en una región con GPU disponible.
2. Deploy con template oficial según GPU (estándar o Blackwell) + volumen + 1× GPU on-demand.
3. Esperar `200` en el proxy del puerto 8188.
4. Instalar checkpoint + LoRAs **en el volumen** (una sola vez).
5. Probar workflows; exportar cada JSON que funcione a local.
6. Stop al terminar; terminate solo con todo ya respaldado.

## Referencias

- Video: https://www.youtube.com/watch?v=RgrEAge_5Kk
- Tutorial oficial Runpod (verificado 2026-11-02): https://docs.runpod.io/tutorials/pods/comfyui
- Volumes: https://docs.runpod.io/storage/network-volumes · Manage pods: https://docs.runpod.io/pods/manage-pods
- Plan de campaña del estudio: [[specs/261030-plan-continuacion-pruebas|plan de continuación]] (Fase G: Flux klein en pod)
- Costos y n8n: [[raw/research/2026-11-01-modelos-imagen-n8n-telegram|research 2026-11-01]]
