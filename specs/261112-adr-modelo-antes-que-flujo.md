# ADR-2026-11-12-modelo-antes-que-flujo: El modelo se decide primero, el flujo después

**Fecha**: 2026-11-12
**Estado**: aceptada
**Deciden**: SOL
**Proyecto**: estudio (concurso gaudi-nexus como caso piloto)

## Contexto

Durante noviembre 2026 se probaron Pollinations (flux, klein, kontext, sana, mai), Cloudflare Workers AI, ComfyUI local (SDXL/SD1.5 + ControlNet) y las vías cloud/pod/serverless. La conclusión del mes: las capacidades dependen del modelo (lo nativo absorbe nodos: edición por sectores, multi-referencia, 4K), el hardware define costo y privacidad, y Comfy aporta la precisión quirúrgica. Decidir el flujo sin decidir el modelo es construir al revés.

## Decisión

Usamos el orden **modelo → hardware → flujo**: primero se elige el modelo por capacidad y licencia, después dónde corre por costo y privacidad, y Comfy solo donde haga falta precisión que el modelo no da nativa.

## Alternativas

### Alternativa 1: Flujo primero (Comfy + nodos, modelo el que entre)
- Pros: control total desde el día uno, reproducible en local.
- Contras: se pagan pasos que el modelo moderno ya trae nativos; se elige hardware antes de saber qué necesita el modelo.
- Por qué no: lleva a nodos custom atados a checkpoints viejos y a sorpresas de VRAM.

### Alternativa 2: Todo en cloud (Comfy Cloud / APIs cerradas)
- Pros: cero setup, modelos frontera.
- Contras: sin nodos custom, sin entrenar LoRA, suscripción permanente, privacidad distinta (grafo y referencias en cuentas de terceros).
- Por qué no: el concurso exige LoRA propio/entrenado y el estudio exige control de datos; el free tier (5 corridas) no sostiene producción.

## Consecuencias

### Positivas

- Tres carriles claros: explorar con klein 4B (Apache 2.0, libre), entregar a cliente con FLUX.3 Image Klein (mejor calidad open, imágenes comerciales bajo $5M/año), volumen con Z-Image-Turbo; LoRA propio sobre klein 4B en pod.
- Cada prueba fija un par (modelo, hardware) con costo medido: pod ≈ $0.44/2 h en 3090, Cloudflare ~170 schnell/día gratis, API por ejecución.
- Qwen-Image-2.1 (mejor calidad cruda) queda en observación por licencia NC.

### Negativas

- klein 4B GGUF Q4 en la RX 570 local está sin confirmar (DirectML + GGUF no probado): la exploración barata depende de API/pod hasta medirlo.
- FLUX.3 Image Klein no admite LoRA comercial sin licencia BFL: el LoRA comercial vive en klein 4B.

### Riesgos + mitigación

- Que el modelo elegido cambie de licencia: re-chequear licencia al desplegar (el repo manda).
- Que el goteo gratis no alcance: recarga x402 desde $0.01 o cuota Cloudflare como respaldo diario.

## Camino (qué sigue)

1. Explorar tipos de flujo con klein 4B (API/pod; probar GGUF Q4 local y medir).
2. Replicar en grande con FLUX.3 Image Klein.
3. Entrenar LoRA propio sobre klein 4B en pod (ai-toolkit).
4. Geometría fina en Comfy local/pod (ControlNet, inpaint, LoRA propio).
5. Producción repetible en serverless/API; conversacional en el agente pi imágenes (n8n).

## Adenda 2026-11-13 — qué flujos Comfy se justifican (veredicto)

Batería W mediante: estación/hora/material global no justifican Comfy (klein cloud, sin Canny). Comfy se reserva a: geometría no negociable (ControlNet + denoise bajo), identidad repetible (checkpoint + seed + LoRA propio), privacidad de concurso, upscale print, inpaint/outpaint con máscara. Pod con klein solo para el grafo combinado klein-local + ControlNet + LoRA. Regla: exploración/estación/hora/mood/croquis → nube (agente); lo demás → Comfy.

## Trazabilidad

- spec: [[specs/261103-spec-ajuste-pollinations-flux|spec-ajuste-pollinations-flux]] | wiki: [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] · [[wiki/glosario/software/cloudflare-workers-ai|cloudflare-workers-ai]] · [[wiki/glosario/interno/pbooks/pbk-pi-imagenes|pbk-pi-imagenes]] | activos: [activos/proyectos/concurso-gaudi-nexus/pollinations-tests]
