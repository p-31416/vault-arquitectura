# NOTA ES: demo mañana — qué hace cada archivo (línea a línea)

Paralelo didáctico de `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/WF/demo-manana/`.
Sin código Python: son 3 JSON ComfyUI en formato API (nodo = cajón, cable = dato).

## 01 — workflow_demo_01_txt2img.json
- Nodo 1 `CheckpointLoaderSimple`: carga el cerebro `architecturerealmix_v11.safetensors` (SD1.5, 2 GB, corre holgado en RX 570).
- Nodos 2/3 `CLIPTextEncode`: traducen tu prompt (+) y tu negativo (−) al idioma interno del modelo.
- Nodo 4 `EmptyLatentImage`: lienzo vacío 768×512 (una sola imagen).
- Nodo 5 `KSampler`: cocina la imagen (euler, 30 pasos, cfg 7, seed 42, denoise 1 = inventa todo).
- Nodos 6/7 `VAEDecode` + `SaveImage`: revelan el lienzo a PNG y lo guardan como `demo01_txt2img.png`.

## 02 — workflow_demo_02_img2img.json
- Igual cerebro y prompts, más 3 nodos nuevos:
- Nodo 4 `LoadImage`: lee `demo01_txt2img.png` (la salida del acto 1).
- Nodo 5 `ImageScale`: la aplana a 512×512 lanczos (regla R1: evita OOM con fotos heterogéneas).
- Nodo 6 `VAEEncode`: la convierte a lienzo interno para retocarla.
- Nodo 7 `KSampler` con denoise 0.65: 0 = calco, 1 = ignora el original; 0.65 = misma casa, nueva luz/material.
- Cambiar seed 42 → 12345 da variante comparable.

## 03 — workflow_demo_03_estilo_marker.json
- Suma nodos 8/9 `LoraLoader` en serie entre el checkpoint y el sampler:
- Nodo 8: LoRA `architectural-design-sketches-with-markers` fuerza 0.6 (estilo marker, trigger `marker painting, handsketch`).
- Nodo 9: LoRA `architecture-sketch-style` fuerza 0.5 (trazo lineal, trigger `linear`).
- Los prompts 2/3 ahora apuntan al clip del nodo 9 (el estilo tiñe el texto).
- Requiere los 2 `.safetensors` en `C:\Users\Solch16\ComfyUI\models\loras\`; sin ellos ComfyUI avisa qué falta.

## Cómo correrlo vos (yo no ejecuto nada)
1. `C:\Users\Solch16\ComfyUI\corre_comfyui.bat` (doble-click) → `http://127.0.0.1:8188`.
2. Arrastrar cada JSON en orden 01 → 02 → 03, botón Queue Prompt.
3. Si el acto 3 pide LoRAs: descargar de Civitai 34384 y 32757 a `models/loras/` y reintentar.
