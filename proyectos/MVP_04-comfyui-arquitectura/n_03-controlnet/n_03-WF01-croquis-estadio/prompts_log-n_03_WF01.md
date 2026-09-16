---
tipo: log
workflow: workflow_controlnet_canny.json
nivel: n_03-controlnet
fecha_creacion: 2026-07-18
ultima_actualizacion: 2026-07-19 22:00
tags: [log, controlnet, canny, scribble, depth, comfyui, estadio]
---

# Log de Prompts — n_03 ControlNet (Canny / Scribble / Dual)

Cada entrada documenta una corrida completa del workflow con todos los parámetros y resultado.

Más nuevo → más arriba.

## Parámetros base (referencia) — Canny baseline v1.0.x

| Parámetro | Valor |
|-----------|-------|
| checkpoint | architecturerealmix_v11.safetensors |
| controlnet | control_v11p_sd15_canny.safetensors |
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| resolución | 512×512 |
| canny_low | 0.31 |
| canny_high | 0.59 |
| strength | 0.7 |
| guidance_end | 0.7 |

## Log

### `v1.1a_02` | 2026-07-19 22:00 | ✅

**Input:** croquis001.jpg
**Workflow:** v1.1a.0 — Scribble ControlNet (sin preprocesador)
**Cambio:** Segunda corrida con Scribble. Mismos parámetros que v1.1a_01.

| Parámetro | Valor |
|-----------|-------|
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |
| seed | — |
| strength | 0.7 |
| guidance_end | 0.7 |
| checkpoint | architecturerealmix_v11.safetensors |
| controlnet | control_v11p_sd15_scribble.safetensors |

**Prompt positivo:**
```
architecturerealmix style, soccer stadium, football stadium architecture, grandstands, stadium bowl, pitch, sports venue, modern building, architectural photography, photorealistic, 8K, highly detailed, dramatic lighting
```

**Prompt negativo:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, office building, residential, empty interior
```

**Output:** `n_03-v1.1a_02.png`

![v1.1a_02](outputs-salidas/n_03-v1.1a_02.png)

**Evaluación:** ❌ El resultado no sigue el croquis. **El croquis es una vista desde el interior del estadio**, pero el prompt describe estadio exterior (grandstands, stadium bowl, pitch). Hay un desajuste fundamental entre el input visual y la instrucción textual. El Scribble intenta guiar la forma, pero el prompt domina el contenido generando una vista exterior genérica.

**Diagnóstico:** El prompt necesita reorientarse a interior del estadio (tribunas vistas desde adentro, cielo abierto, estructura de techo/cobertura si la hay, butacas, pasillos). Alternativamente, la strength del Scribble podría necesitar subirse para que la composición del interior del croquis pese más que el prompt exterior.

**Acción → [[backlog-n_03_WF01]]:**
- ~~Reescribir prompt para vista interior del estadio~~ ✅ → v1.1a.1
- ~~Evaluar subir strength a 0.85-1.0 para forzar la composición del croquis~~ ✅ → v1.1a.1 (0.85)
- Considerar reducir guidance_end para dar más peso al Scribble en pasos tempranos

**Fix aplicado:** → [[workflow_log-n_03_WF01#v1.1a.2 — Scribble Max + Prompt Simplificado 2026-07-19 22:30|v1.1a.2]] — strength 1.0, prompt sin "stadium", negativo reforzado. **Lección:** SD 1.5 asocia "stadium" con exterior por sesgo del training. Para forzar interior, eliminar la palabra "stadium" y describir los elementos visuales directamente.

---

### `v1.1a_01` | 2026-07-19 17:30 | ✅

**Input:** croquis001.jpg
**Workflow:** v1.1a.0 — Scribble ControlNet (sin preprocesador)
**Cambio:** Primer test con ControlNet Scribble. El croquis se alimenta directo al modelo (sin Canny ni otro preprocesador de bordes). La tesis es que el croquis arquitectónico es inherentemente un scribble.

| Parámetro | Valor |
|-----------|-------|
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |
| seed | 42 |
| strength | 0.7 |
| guidance_end | 0.7 |
| tiempo | ~90s |
| checkpoint | architecturerealmix_v11.safetensors |
| controlnet | control_v11p_sd15_scribble.safetensors |

**Prompt positivo:**
```
architecturerealmix style, soccer stadium, football stadium architecture, grandstands, stadium bowl, pitch, sports venue, modern building, architectural photography, photorealistic, 8K, highly detailed, dramatic lighting
```

**Prompt negativo:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, office building, residential, empty interior
```

**Nodos cacheados:** 1, 2, 3, 4, 6, 8 — solo 5, 7, 9, 10, 11 descodificaron (ControlNetLoader nuevo, ControlNetApplyAdvanced con imagen Scribble).

![v1.1a_01](outputs-salidas/n_03-v1.1a_01.png)

**Evaluación:** Pendiente — revisar si el scribble guía la forma sin forzar bordes lineales rotos.

**Referencias:** [[workflow_log-n_03_WF01#v1.1 — Bifurcación: Scribble (v1.1a) ± Dual Canny+Depth (v1.1b) 2026-07-19 21:00\|v1.1 changelog]] — [[index-n_03_WF01]]

---

### `v1.0.2_01` | 2026-07-19 15:00 | ✅

**Input:** croquis001.jpg
**Workflow:** v1.0.2 — stadium prompt + ControlNet revertido
**Cambio:** Mismos prompts de estadio, pero Canny thresholds y ControlNet strength/end vuelven a valores estables (donde las líneas no se cortaban).

| Parámetro | Valor |
|-----------|-------|
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |
| seed | 42 |
| canny_low | 0.31 |
| canny_high | 0.59 |
| strength | 0.7 |
| guidance_end | 0.7 |
| tiempo | ~88s |
| checkpoint | architecturerealmix_v11.safetensors |
| controlnet | control_v11p_sd15_canny.safetensors |

**Prompt positivo:**
```
architecturerealmix style, soccer stadium, football stadium architecture, grandstands, stadium bowl, pitch, sports venue, modern building, architectural photography, photorealistic, 8K, highly detailed, dramatic lighting
```

**Prompt negativo:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, office building, residential, empty interior
```

**Nodos cacheados:** 1, 2, 3, 4, 5, 6, 7, 12 — solo 8, 9, 10, 11 descodificaron.

![v1.0.2_01](outputs-salidas/n_03-v1.0.2_01.png)

**Evaluación:** Pendiente — verificar que las líneas cortadas desaparecieron manteniendo el tema de estadio.

**Referencias:** [[workflow_log-n_03_WF01#v1.0.2 — Stadium Prompt, ControlNet Tuned 2026-07-19 14:00\|v1.0.2 changelog]] — [[nodos-n_03_WF01]] — [[index-n_03_WF01]]

---

### `v1.0.1_01` | 2026-07-19 14:00 | ✅

**Input:** croquis001.jpg
**Workflow:** v1.0.1 — stadium prompt + stronger ControlNet
**Cambio:** Primer render con prompt de estadio y ControlNet ajustado. 

| Parámetro | Valor |
|-----------|-------|
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |
| seed | 42 |
| canny_low | 0.20 |
| canny_high | 0.45 |
| strength | 0.85 |
| guidance_end | 1.0 |
| tiempo | ~97s |
| checkpoint | architecturerealmix_v11.safetensors |
| controlnet | control_v11p_sd15_canny.safetensors |

**Prompt positivo:**
```
architecturerealmix style, soccer stadium, football stadium architecture, grandstands, stadium bowl, pitch, sports venue, modern building, architectural photography, photorealistic, 8K, highly detailed, dramatic lighting
```

**Prompt negativo:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch, office building, residential, empty interior
```

**Nodos no cacheados:** 3 (Canny nuevos thresholds), 5-6 (nuevos prompts), 8 (nuevos strength/end), 9-10-11 (sampling + decode)

![v1.0.1_01](outputs-salidas/n_03-v1.0.1_01.png)

**Evaluación:** El tema de estadio mejoró, pero strength 0.85 + end 1.0 forzó líneas cortadas del Canny. → v1.0.2.

**Referencias:** [[workflow_log-n_03_WF01#v1.0.1 — Stadium Prompt + Stronger ControlNet 2026-07-19 11:30\|v1.0.1 changelog]] — [[nodos-n_03_WF01]] — [[index-n_03_WF01]]

---

### `v1.0.0_03` | 2026-07-19 12:30 | ✅

**Input:** croquis001.jpg
**Cambio:** Re-queue manual desde UI de ComfyUI — seed aleatorio, mismos parámetros. Verifica que el fix Canny se mantiene estable tras reinicio.

| Parámetro | Valor |
|-----------|-------|
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |
| seed | random |
| canny_low | 0.31 |
| canny_high | 0.59 |
| strength | 0.7 |
| guidance_end | 0.7 |
| tiempo | ~92s |
| checkpoint | architecturerealmix_v11.safetensors |
| controlnet | control_v11p_sd15_canny.safetensors |

**Prompt positivo:**
```
architecturerealmix style, modern building, architectural photography, photorealistic, 8K, highly detailed, dramatic lighting
```

**Prompt negativo:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch
```

**Nodos cacheados:** 1, 2, 3, 4, 5, 6, 7, 8, 12 — solo KSampler descodificó (seed fresco).

![v1.0.0_03](outputs-salidas/n_03-v1.0.0_03.png)

---

### `v1.0.0_02` | 2026-07-19 11:00 | ✅

**Input:** croquis001.jpg
**Cambio:** Canny nativo de ComfyUI — se corrigió bug de kornia + DirectML (`F.pad` invertía ejes). Ahora el nodo Canny ejecuta en CPU para evitar el bug.

| Parámetro | Valor |
|-----------|-------|
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |
| seed | 42 |
| canny_low | 0.31 |
| canny_high | 0.59 |
| strength | 0.7 |
| guidance_end | 0.7 |
| tiempo | ~97s |
| checkpoint | architecturerealmix_v11.safetensors |
| controlnet | control_v11p_sd15_canny.safetensors |

**Prompt positivo:**
```
architecturerealmix style, modern building, architectural photography, photorealistic, 8K, highly detailed, dramatic lighting
```

**Prompt negativo:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch
```

**Fix aplicado:** `comfy_extras/nodes_canny.py` — detecta device DirectML y ejecuta kornia en CPU donde `F.pad` funciona correctamente.

![v1.0.0_02](outputs-salidas/n_03-v1.0.0_02.png)

**Evaluación:** Pendiente — comparar con v1.0.0_01.

---

### `v1.0.0_01` | 2026-07-19 10:00 | ✅

**Input:** croquis001.jpg (croquis arquitectónico, original 1600×1315, reescalado a 512×512)
**Cambio:** Baseline — primera corrida con ControlNet Canny sobre croquis.

| Parámetro | Valor |
|-----------|-------|
| steps | 30 |
| cfg | 7 |
| sampler | euler |
| scheduler | normal |
| res | 512×512 |
| seed | 42 |
| canny_low | 0.31 |
| canny_high | 0.59 |
| strength | 0.7 |
| guidance_end | 0.7 |
| tiempo | ~111s |
| checkpoint | architecturerealmix_v11.safetensors |
| controlnet | control_v11p_sd15_canny.safetensors |

**Prompt positivo:**
```
architecturerealmix style, modern building, architectural photography, photorealistic, 8K, highly detailed, dramatic lighting
```

**Prompt negativo:**
```
low quality, blurry, distorted, ugly, bad architecture, cartoon, sketch
```

**Nota técnica:** El nodo Canny nativo de ComfyUI (kornia) falló con imágenes reescaladas por ImageScale. Se generó el edge map externamente (script Python con kornia 0.8.1) y se usó `generate_with_controlnet` con el mapa preprocesado.

![v1.0.0_01](outputs-salidas/n_03-v1.0.0_01.png)

**Evaluación:** Pendiente — revisar fidelidad de bordes vs resultado.

**Sugerencias → [[backlog-n_03_WF01]]:**
- Repetir con strength 0.5 vs 0.85
- Probar MLSD para edificios rectos
- Probar depth map (MiDaS) en vez de Canny
