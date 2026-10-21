---
tipo: software
software: comfy-cloud-vs-runpod
categoria: decision
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [glosario, software, comfyui, comfy-cloud, runpod, privacidad, licencias, costo, gaudi, concurso]
---

# Comfy Cloud vs RunPod vs local — dónde renderizar (y qué se puede)

> Comparación de las tres rutas para producir imagen con IA desde el estudio, con los límites y los precios verificados el 2026-10-21. La decisión que se discute con Emilia es de infraestructura, no de estética: **dónde corre el GPU, qué datos salen de la máquina y qué se puede entrenar**.

- [[#La pregunta en una línea]]
- [[#El cuadro]]
- [[#Qué puede y qué no puede cada una]]
- [[#Privacidad: qué sale de la máquina y qué queda]]
- [[#Entrenar un LoRA]]
- [[#Qué sirve específicamente para el concurso]]
- [[#Veredicto y costos]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

## La pregunta en una línea

El concurso exige **un modelo de IA entrenado con material de la Fundació Antoni Gaudí** y una lámina A1 protegida. Eso descarta de entrada la mitad de las opciones: **en Comfy Cloud Standard no se pueden importar modelos propios, y en Comfy Cloud no se entrena nada**. La ruta del concurso es **ComfyUI propio + GPU alquilada (RunPod)**; Comfy Cloud sirve para **aprender y prototipar** (con el Free Tier, sin costo).

## El cuadro

| | **Local + RunPod** (escritorio) | **Comfy Cloud $20** (Standard) | **Comfy Cloud gratis** (Free tier) |
|---|---|---|---|
| **Dónde corre el GPU** | Tu ComfyUI en la PC de estudio; el GPU (24 GB) en un pod de RunPod | GPUs de Comfy: Blackwell RTX 6000 Pro, **96 GB VRAM** + 180 GB RAM | Las mismas GPUs |
| **Modelos** | Los tuyos, bajados a mano (el stack FLUX.2 son 18 GB) | **900+ preinstalados** | Los mismos |
| **Tu LoRA (el del curso, o el propio)** | ✅ Sí, sin límites | ❌ **No**: importar modelos propios es solo en Creator/Pro/Team, y **el upload directo de archivos grandes no existe todavía** (está "en la hoja de ruta") | ❌ igual |
| **Entrenar un LoRA** | ✅ En el pod (klein 4B: 12 GB VRAM) | ❌ **Comfy Cloud no entrena**: no permite instalar nodos propios, y los nodos de entrenamiento no están en la lista aprobada | ❌ |
| **Nodos personalizados** | Todos los que instales | Solo la lista aprobada (~90 % de los workflows locales) | Solo la lista aprobada |
| **Límite por trabajo** | El que pongas (tú controlás) | **30 minutos** por workflow · 1 concurrente | 30 min · 400 créditos/mes |
| **Privacidad: el grafo y los archivos** | En tu disco | En tu cuenta de Comfy (retención: "el tiempo necesario para operar, analizar y mejorar el servicio") | ídem |
| **Privacidad: prompts e imágenes** | Van al pod (disco efímero cifrado; al terminar el pod, **no queda rastro**) | Quedan en la cuenta de Comfy; si usás **Partner Nodes**, además se reenvían al proveedor (Nano Banana, etc.) con sus propias políticas | ídem |
| **El Agent** | El chat vive en tu máquina, **pero el mensaje + el workflow van al servicio online de Comfy** | Ídem + el chat se guarda en la nube | ídem |
| **Costo** | **$0,22/h** (3090 Community) · $0,34/h (4090) · $0,35/h (A40 48 GB) | $20/mes · 50.400 créditos/año | $0 · 400 créditos/mes ≈ **25 min de GPU** |
| **Veredicto** | **La ruta del concurso y del trabajo de cliente** | Producción de imagen sin LoRA propio, con fricción de plataforma | **Pruebas gratis de los workflows oficiales del curso** |

## Qué puede y qué no puede cada una

### Comfy Cloud Standard ($20)

- ✅ 900+ modelos preinstalados (FLUX.2, Wan, LTX, Qwen…), 30 min por workflow, 1 concurrente, cola de 100, 50.400 créditos/año, solo GPU activa se cobra (armar el grafo es gratis).
- ❌ **Importar tu propio LoRA o checkpoint** (solo Creator $35, Pro $80, Team).
- ❌ **Subir un `.safetensors` propio**: no existe todavía; se importa desde CivitAI o Hugging Face.
- ❌ Nodos personalizados fuera de la lista aprobada (ni instalar ni subir).
- ❌ Entrenar.

> **Consecuencia directa:** el LoRA del curso (bajado de `thomasnelissen.ai`) **no se puede usar en Comfy Cloud Standard**. Se podría si estuviera publicado en CivitAI o Hugging Face (importación desde ahí), pero el curso lo reparte desde su web.

### Comfy Cloud Creator ($35)

- ✅ Todo lo de Standard + **importar tus propios modelos y LoRAs desde CivitAI o Hugging Face** + 3 workflows concurrentes + 88.800 créditos/año.
- ⚠️ El LoRA propio habría que **publicarlo en un repo de Hugging Face** para poder importarlo: el upload directo de archivo no existe.
- ❌ Sigue sin poder **entrenar** ni instalar nodos propios.

### Comfy Cloud Free (0 USD)

- ✅ 400 créditos/mes (≈25 min de GPU a 0,266 cr/s), mismos modelos y nodos, sin tarjeta.
- ✅ **Alcanza para la calibración**: probar los workflows oficiales del curso (RHINO-TO-IMAGE, IMAGE-EDIT, SPECTRUM) y ver si el grafo corre tal cual.
- ❌ Los créditos **no se acumulan**: renuevan cada mes.

### RunPod + ComfyUI propio

- ✅ GPU 24 GB (3090 $0,22/h) o 48 GB (A40 $0,35/h): entra FLUX.2 klein 9B fp8 con el text encoder a la RAM del pod (125 GB).
- ✅ **Control total**: cualquier nodo, cualquier modelo, cualquier LoRA, y **entrenamiento** (ai-toolkit / kohya).
- ✅ **Trazabilidad y privacidad**: el grafo, los prompts y las referencias salen de la PC solo hacia tu pod; el disco del contenedor está cifrado y **al terminar el pod no queda nada**. Los volúmenes se pueden cifrar y borrar a mano.
- ⚠️ El pod es de un tercero: mientras corre, ve lo que corre en él. Se mitiga apagándolo/terminándolo y no dejando volúmenes persistentes.
- ⚠️ Setup: hay que bajar 18 GB de stack y subir los archivos.

### La PC de estudio (8 GB VRAM, DirectML)

- ✅ Cero costo, todo local, control total, ideal para **iterar** con SD1.5/SDXL (ya hay 52 renders) y para **klein 4B GGUF Q4** (5,7 GB + text encoder a RAM).
- ❌ FLUX.2 klein **9B no entra** (9,4 GB de pesos en 8 GB de VRAM) y con DirectML sobre un i5 de 2013 cada imagen lleva minutos.
- ❌ Entrenar un LoRA (klein 4B pide 12 GB).

## Privacidad: qué sale de la máquina y qué queda

| Dato | Local + pod | Comfy Cloud |
|---|---|---|
| Archivos de workflow y modelos | En tu disco | En tu cuenta de Comfy (retención por el tiempo necesario para operar/analizar/mejorar) |
| Prompts e imágenes de referencia | Al pod; disco cifrado; al terminar el pod, borrado | En la cuenta de Comfy; y a un tercero si usás Partner Nodes (medios borrados a las 24 h, pero el prompt y las imágenes los procesa el proveedor) |
| Datos para entrenar modelos | Comfy declara que no usa tus entradas ni salidas para entrenar; RunPod: "vos controlás tus datos" | Ídem (Comfy: "no usamos tus entradas ni salidas para entrenar modelos generativos") |
| Telemetría | En Desktop: opt-in y **no** procesa workflows, prompts, salidas ni pesos; las rutas y los secretos se redactan solos | Mismo criterio, más el uso del servicio (Agent, partners) |
| El Agent | El historial vive en tu máquina, pero el mensaje y el workflow elegido se procesan en el servicio online de Comfy | El historial se guarda en la nube |

**Reglas que el estudio se puede dar hoy (costo cero):**

1. Para material del concurso, **no usar el Comfy Agent**: pasar el workflow por el chat online es mandar el grafo del concurso a un servicio externo.
2. En el pod: **usar el disco del contenedor** (no Network Volume) para material sensible, y **terminar el pod** al terminar → no queda rastro ni costo de storage.
3. Si se usa Comfy Cloud para material del concurso, subir **solo imágenes derivadas**, nunca los `.dwg` originales ni las fotos de material con licencia de la Fundació.
4. En los prompts: no escribir datos de cliente (nombres, superficies, dirección). El prompt viaja a los dos lados.

## Entrenar un LoRA

- **Comfy Cloud no entrena**: no hay nodos de entrenamiento en la lista aprobada y no se pueden instalar. El plan Creator ($35) **no** habilita entrenamiento: solo habilita *importar* un LoRA ya entrenado.
- **Dónde se entrena**: pod con GPU (klein 4B pide 12 GB → 4090 $0,34/h; 2-3 h ≈ **$1**; 9B pediría 24 GB y unos $2-3) o una máquina propia con ≥12 GB.
- **El flujo completo en un pod**: bajar el modelo base (klein 4B, Apache 2.0) + el dataset propio → entrenar con `ai-toolkit` (o kohya) → el `.safetensors` sale en `models/loras` → usar en el mismo pod o en local.
- **Para poder usarlo después en Comfy Cloud**: hay que publicarlo en un repo de Hugging Face (importable desde Creator+) **o** seguir usándolo en local/pod (que es lo razonable: el LoRA propio es material de trabajo del estudio).

## Qué sirve específicamente para el concurso

Los requisitos técnicos del concurso (verificados en el plan `261019-plan-concurso-gaudi-nexus-ia`):

| Requisito del concurso | Con la ruta local + pod | Con Comfy Cloud $20 |
|---|---|---|
| Texto → imagen | ✅ | ✅ |
| Edición de imágenes con IA | ✅ | ✅ |
| Video de IA para presentación | ✅ (LTX/Kling/Seedance en el pod; los Partner Nodes solo en Cloud) | ✅ (más fácil: Nano Banana Pro, Seedance ya están) |
| Reconstrucción 3D desde imágenes IA | ✅ (nodos de imagen→3D) | ⚠️ si el nodo está en la lista aprobada |
| **Modelo IA entrenado con material de la Fundació** | ✅ **el LoRA del curso** (ya lo tenemos) o **el propio** (se entrena en el pod) | ❌ **no se puede importar** el LoRA del curso (no está en CivitAI/HF) ni el propio sin publicarlo en HF |
| Entrega protegida (JPG/PNG de resolución limitada, nunca PDF con cotas) | ✅ (se controla en el pod y en la composición) | ✅ |

**Y lo que cada ruta habilita después del concurso:**

- El LoRA del curso es **FLUX Non-Commercial** (klein 9B): sirve para el concurso, **no para un cliente**.
- El LoRA **propio**, entrenado sobre **klein 4B (Apache 2.0)** con fotos y croquis del estudio, sí habilita trabajo de cliente. Y ese entrenamiento **exige un pod** (o una máquina de 12 GB+): no hay forma de hacerlo en Comfy Cloud.
- Dónde se aplica después ese LoRA propio: en **local** (klein 4B GGUF, 8 GB) o en **pod**. Comfy Cloud Creator sirve solo si el LoRA se publica en Hugging Face.

## Veredicto y costos

| Ruta | Para qué | Costo del mes |
|---|---|---|
| **Local 8 GB** | Iterar (SD1.5/SDXL ya andando) · preprocesado desde Rhino · la parte del flujo que no necesita 9B | $0 |
| **Comfy Cloud Free** | Probar los workflows oficiales del curso y ver si corren tal cual | $0 |
| **RunPod 3090 $0,22/h** | Producción 9B + **entrenamiento del LoRA propio** + render de la lámina | **$1-2** |
| **Comfy Cloud $20** | Producción de imagen sin LoRA propio, o cuando conviene no tocar la PC | $20 |
| **Comfy Cloud Creator $35** | Solo si el LoRA propio estuviera publicado en HF y quisiéramos iterarlo en la nube | $35 |

**Costo del concurso completo: $1-2** (RunPod puntual) frente a $20-35/mes de suscripción permanente. Para una línea de trabajo que el 16/12 cierra, lo razonable es **pagar por uso, no por suscripción**.

## Conceptos relacionados

- [[wiki/glosario/software/comfyui|comfyui]] — nodos, modelos y flujos del estudio
- [[wiki/glosario/software/flux2-klein-9b|flux2-klein-9b]] — el modelo del concurso y su stack
- [[wiki/glosario/software/lora-rhino-to-image-gaudi|lora-rhino-to-image-gaudi]] — el LoRA del curso
- [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] — playbook operativo
- [[wiki/glosario/conceptos/payback|payback]] — costo de la nube vs tiempo de iteración
- [[proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image|WF-rhino-to-image]] — el flujo del concurso

## Referencias

- [Comfy Cloud — Pricing (planes, créditos, límites, API)](https://comfy.org/pricing/) (verificado 2026-10-21 — 200)
- [Comfy — Data & Storage on Cloud (privacidad por defecto)](https://support.comfy.org/articles/6342729551-data-storage-on-cloud) (verificado 2026-10-21 — 200)
- [Comfy — Data retention (qué se guarda y cuánto)](https://docs.comfy.org/support/data-retention) (verificado 2026-10-21 — 200)
- [Comfy — Partner Node Data Retention (24 h y reenvío a terceros)](https://docs.comfy.org/tutorials/partner-nodes/data-retention) (verificado 2026-10-21 — 200)
- [Comfy — Custom nodes on Cloud (no se pueden instalar)](https://support.comfy.org/articles/6791455062-custom-nodes-on-cloud) (verificado 2026-10-21 — 200)
- [Comfy — Comfy Agent: datos y privacidad (local y cloud)](https://docs.comfy.org/agent-tools/in-app-agent-data-privacy) (verificado 2026-10-21 — 200)
- [Comfy — Desktop Privacy Policy (telemetría opt-in; no procesa prompts ni salidas)](https://comfy.org/privacy/desktop/) (verificado 2026-10-21 — 200)
- [Comfy — Enterprise MSA (cláusula "No AI Training" y metadatos derivados)](https://comfy.org/enterprise-msa/) (verificado 2026-10-21 — 200)
- [RunPod — Pricing (3090 $0,22/h, 4090 $0,34/h, A40 $0,35/h)](https://www.runpod.io/pricing) (verificado 2026-10-21 — 200)
- [RunPod — Pods: stop / terminate y qué se borra](https://docs.runpod.io/pods/manage-pods) (verificado 2026-10-21 — 200)
- [RunPod — Storage types (disco efímero vs volumen)](https://docs.runpod.io/pods/storage/types) (verificado 2026-10-21 — 200)
- [RunPod — Keeping data secure on cloud GPUs](https://www.runpod.io/articles/guides/keep-data-secure-cloud-gpus) (verificado 2026-10-21 — 200)
- [RunPod — Privacy Policy](https://www.runpod.io/legal/privacy-policy) (verificado 2026-10-21 — 200)
- [Comfy Cloud vs alternativas: límites reales (upload directo inexistente, nodos, precios)](https://www.earngenix.com/blog/what-is-comfy-cloud) (verificado 2026-10-21 — 200)
