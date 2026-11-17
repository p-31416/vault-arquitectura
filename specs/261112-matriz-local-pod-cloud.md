---
tipo: plan
proyecto: concurso-gaudi-nexus
titulo: Matriz local vs pod abierto vs Cloud — veredicto por caso
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
estado: borrador-activo
tags: [plan, matriz, local, pod, cloud, veredicto, gratis]
idioma: es
---

# Matriz local / pod abierto / Cloud — qué va dónde y qué gana

> Lee primero el veredicto (§1), después el caso que te toque (§2). Detalle técnico en [[specs/261112-diagnostico-controlnet-inpaint-upscale|diagnóstico]] y costos en [[specs/261112-veredicto-comfy-vs-openhiggsfield|veredicto Comfy]].

## 1. Veredicto en una página

| Caso | Local $0 | Pod abierto | Cloud | Gana |
|---|---|---|---|---|
| F1 txt2img casa base | ✅ RealVis/Juggernaut | ✅ más calidad | ✅ rápido | **Local** (iterar gratis) |
| F2 img2img 3D→render | ✅ SDXL denoise | ✅ Flux klein+LoRA curso | ✅ Nano Banana ref | **Local** prueba, **pod** final |
| F3 viewpoint ±15° | ✅ YT-03 SDXL | ✅ Qwen multi-ángulo 96 poses | ⚠️ solo 2D | **Local** giros chicos, **pod** giro real |
| F4 inpaint/muebles | ✅ inpainting-fp16 | ✅ Qwen-Edit preciso | ✅ Nano Banana quirúrgico | **Local** (cero costo por intento) |
| F5 relight/sol | ✅ IC-Light en disco | ✅ Flux relight | ⚠️ genérico | **Local** |
| F6 sketch→render | ⚠️ canny simple sí, dual no (9.4GB>8GB) | ✅ dual + Qwen | ✅ Nano Banana sketch | **Pod** (dual), **local** simple |
| F7 upscale | ⚠️ por mitades ESRGAN | ✅ full + tiles | ✅ Topaz/Magnific 1-click | **Local** por partes, **Cloud** si hay crédito free |
| F8 imagen↔3D | ⚠️ solo preparación | ✅ Hunyuan3D/Tripo pack | ✅ Tripo API 1-click | **Pod** (abierto, sin pagar por malla) |
| F9 imagen→video | ❌ excede 8GB | ✅ LTX/Wan | ✅ Seedance/Veo API | **Pod** (LTX $0.3/h) salvo Seedance puntual |
| F10 loop Telegram | ✅ n8n + LAN free | ✅ wake-on-demand | ❌ innecesario | **Local** |
| Biblioteca estilos | ✅ crece con keepers | ✅ LoRA propio 4B $1 | ❌ no entrena | **Pod** entrena, **local** aplica |
| Lámina A1 texto/vector | ✅ HTML + fonts propias | — | ✅ Recraft/Ideogram API | **Local** final, **Cloud/API** solo benchmark |
| Entrenar LoRA | ❌ sin CUDA | ✅ ai-toolkit klein 4B ~$1 | ❌ no entrena | **Pod** (única vía) |

Regla de oro: **local itera, pod produce pesado, Cloud solo lo irremplazable propietario** (Nano Banana grounding, Seedance, Tripo API 1-click). Cloud Standard $20 no importa tu LoRA ni entrena; Creator $35 importa desde HF/CivitAI.

## 2. Caso por caso (las tres vías)

### F1 — txt2img casa base
- Local: RealVisXL v5 1216x832 30-35 pasos / Lightning 512 4-6 pasos. $0, 80s-10min.
- Pod: mismo + Flux klein 9B 4 pasos (~8s/imagen). $0.22-0.34/h.
- Cloud: 900+ modelos, Nano Banana Pro, GPT Image. Suscripción + créditos partner.
- Gana **local**: iterar 20 prompts gratis no tiene rival.

### F2 — img2img 3D→render / material
- Local: SDXL denoise 0.4/0.6/0.8, AR-VAE baked. Fiel hasta 0.65.
- Pod: Flux klein 9B + LoRA rhino-to-image 0.8 (geometría clavada + material curso).
- Cloud: Nano Banana 2 con 2-14 refs + image search grounding (mejor "conoce Sagrada").
- Gana **local para probar, pod para final Gaudí, Cloud 1 test grounding**.

### F3 — viewpoint
- Local: YT-03 SDXL ±15°, low-angle, aérea leve. $0.
- Pod: Qwen-Edit + CameraAngleSelector 96 poses + LoRA multi-ángulo.
- Cloud: sin giro 3D real (solo re-encuadre 2D).
- Gana **local chicos / pod real**. Cloud no compite acá.

### F4 — inpaint / muebles / loggia
- Local: `sd-v1-5-inpainting-fp16` + SetLatentNoiseMask + CropStitch. Cada reintento $0.
- Pod: Qwen-Image-Edit bordes quirúrgicos.
- Cloud: Nano Banana inpaint (módulo 3 curso) + GPT Image edit 16 refs.
- Gana **local**: inpaint vive de iterar 10 veces la máscara.

### F5 — relight / sol
- Local: IC-Light fc/fbc + LoRA direccionales backlog L3. $0.
- Pod: Flux relight consistente.
- Cloud: filtros genéricos, sin control paramétrico.
- Gana **local**.

### F6 — sketch→render ControlNet
- Local: canny SD1.5/SDXL simple sí. Dual canny+depth SDXL = 9.4GB > 8GB → OOM. Sin `control_aux` (no hed/lineart).
- Pod: dual Union + Qwen + GGUF.
- Cloud: Nano Banana sketch + GPT Image.
- Gana **pod para dual, local para simple**. Si Cloud tiene tu sketch, 1 test Nano Banana vale.

### F7 — upscale
- Local: RealESRGAN + 2º denoise 0.2-0.35 por mitades (full 2K OOM). `n_09-upscale` armado.
- Pod: full + tiles + UltimateSDUpscale instalable.
- Cloud: Topaz/Magnific 1-click (28-50 créditos 2K-4K).
- Gana **local por partes**; Cloud solo con créditos free sobrantes.

### F8 — imagen↔3D
- Local: preparación (maqueta blanca, normal, AO/DA3) sí; malla no.
- Pod: Hunyuan3D/Tripo vía 3D-Pack abierto + 24GB. Sin costo por malla.
- Cloud: Tripo 3.1 API 1-click (~105 cr) — propietario, pagas por malla.
- Gana **pod**. Cloud solo si una malla urgente justifica el crédito.

### F9 — imagen→video
- Local: no viable 8GB.
- Pod: LTX i2v (JSON existe) ~$1/h total clip 15s.
- Cloud: Seedance 2.0 (320cr 720p/7s, 1600cr 4K), Veo, Wan API.
- Gana **pod LTX** salvo que pidas Seedance puntual (F-10 pod vs Cloud comparan).

### F10 — loop Telegram + viewport vivo
- Local: n8n + ComfyUI LAN + `capture_rhino_viewport` (puente MCP). $0.
- Pod: mismo + wake-on-demand API.
- Cloud: innecesario (el loop es orquestación, no modelo).
- Gana **local** (+ pod wake solo al generar pesado).

### Biblioteca de estilos / LoRA propio
- Local: crece con keepers; aplica LoRA 4B/9B livianos.
- Pod: entrena klein 4B Apache 2.0 rank16 ~$0.50-1/corrida (ai-toolkit). Única vía (Cloud no entrena, local sin CUDA).
- Cloud: Creator importa LoRA publicado en HF/CivitAI; no entrena.
- Gana **pod entrena, local aplica**.

### Lámina A1 (texto + vector + composición)
- Local: HTML espejo + fonts propias + SVG Inkscape. 100% gratis y editable.
- Pod: no aplica.
- Cloud/API: Recraft vector + Ideogram bounding-box + GPT Sunburst texto largo (benchmarks pagos).
- Gana **local final**; API solo 3-5 pruebas techo.

## 3. Cuándo Cloud sí es obligatorio (lista cerrada)

1. Grounding con image search real (Nano Banana 2.1/3.1) para "conocer Sagrada".
2. Seedance/Veo video fotorreal 1-click sin operar pod.
3. Tripo API 1-click para una malla urgente.
4. Topaz/Magnific upscale 1-click con créditos free.
Fuera de eso, local+pod cubren todo sin suscripción.

## 5. Doctrina de infraestructura del estudio (acordada 2026-11-12)

1. **Local prueba lo mínimo viable.** Todo flujo nuevo se prueba primero en la PC con lo que haya (RX 570, SDXL, Lightning) hasta demostrar que el grafo funciona. Local no es para producir pesado: es el banco de pruebas.
2. **Pod = tu local con músculo.** El pod corre exactamente los mismos workflows, modelos y LoRAs que correrían en una buena máquina propia. Por eso todo flujo que va a pod entra **ya probado en local** (aunque sea en versión liviana): al pod no se sube a experimentar, se sube a producir.
3. **Portabilidad obligatoria.** Modelos, LoRAs y JSON validados viven versionados en el vault y corren igual en pod y en infraestructura propia si la hubiera. Nada atado a una máquina.
4. **Video y tandas pesadas no bloquean al dibujante.** La PC de trabajo es del dibujante (par arquitecto + sintético en vivo). Lo pesado corre de noche / en idle, o en pod. Regla: si ocupa la máquina en horario de dibujo, va a pod.
5. **Concurrencia y entrega → pod.** Dos personas o fecha de entrega con volumen: pod con el stack ya probado, se enciende, produce el lote, se apaga. El pod es elastico, no una segunda oficina.
6. **Cloud = última opción, solo lo imposible local.** Lo que ningún hardware propio ni pod abierto resuelve (lista §3: grounding real, Seedance/Veo 1-click, Tripo API urgente, Topaz con free). Multi-PC con una sola credencial Cloud suena cómodo pero: Standard $20 no importa LoRAs propios (+$10 Creator para importarlos, y solo vía HF/CivitAI, sin upload directo), no entrena nada, 1 concurrente y 30 min por trabajo. Para el dibujante que itera 20 veces, el costo por fricción supera al de un pod por horas.
7. **Ventaja del pod, con límite.** Control total (nodos, LoRAs, entrenamiento klein 4B ~$1) a $0.22-0.39/h, sin suscripción. Límite: cada hora idle es plata quemada — auto-stop 5 min, volúmenes efímeros, tandas nocturnas. Presupuesto concurso completo medido: $5-6, no $20-35/mes.

## 6. Plan de lectura y ejecución

1. Lee veredicto §1, ubica tu caso en §2.
2. Prueba local según [[specs/261112-plan-pruebas-casa-moderna-3d|plan casa-moderna]] F0→F1→F2.
3. Pod solo con gate de gasto (F6 dual, F8 malla, F9 clip, LoRA).
4. Cloud solo lista §3 con tope de créditos.
5. Registra en reporte 20 + matriz + lámina.
