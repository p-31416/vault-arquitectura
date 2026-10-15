# Demo mañana — mock 3 actos (txt2img → img2img → estilo)

Guion 10 min para mostrar lo probado + flujos nuevos.

## Acto 1 — txt2img (idea desde cero)
Archivo: `workflow_demo_01_txt2img.json` (deriva de `A-WF-estadio`, Realmix SD1.5, 768×512, euler, 30 steps, cfg 7, seed 42).
Prompt: casa hormigón minimalista entre árboles. Sale `demo01_txt2img.png` en ~60-90s en RX 570.
Mostrar: cambiar seed 42 → 12345 → 9999 da 3 variantes (letras A del vault).

## Acto 2 — img2img (modificar lo generado)
Archivo: `workflow_demo_02_img2img.json` (deriva de `log-WF-croquis`, respeta R1 ImageScale 512 lanczos).
Tomar `demo01_txt2img.png` como input (`LoadImage`), denoise 0.65, prompt golden hour + madera.
Mostrar en vivo: denoise 0.45 (casi igual) vs 0.75 (reinventa). Guardar `demo02_img2img.png`.

## Acto 3 — estilo marker (lo nuevo)
Archivo: `workflow_demo_03_estilo_marker.json` (nuevo: Realmix + 2 LoRAs apilados).
Nodos 8-9 `LoraLoader`: markers 0.6 + sketch-style 0.5, triggers `marker painting, handsketch, linear`.
Requisito previo: descargar los 2 LoRAs a `models/loras/` (≈27 MB total):
- `architectural-design-sketches-with-markers.safetensors` (Civitai 34384, 9 MB)
- `architecture-sketch-style.safetensors` (Civitai 32757, 18 MB)
Sin ellos el flujo avisa "modelo ausente" — ese error también sirve para mostrar gestión de modelos.

## Orden de arranque (vos en terminal)
1. Doble-click `C:\Users\Solch16\ComfyUI\corre_comfyui.bat` → abrir `http://127.0.0.1:8188`.
2. Arrastrar `workflow_demo_01_txt2img.json` → Queue → mostrar imagen.
3. `stage` la salida como input del acto 2 (o copiar PNG a `input/demo01_txt2img.png`) → Queue acto 2.
4. Acto 3 directo con Queue (si LoRAs instalados).

## Qué decir de modelos
Checkpoint = cerebro (Realmix SD1.5 local, Juggernaut SDXL entrega). LoRA = capa de estilo fina y liviana. ControlNet = respeta geometría (Canny/Depth, ya validados en n_03). Upscale = entrega A3 (Remacri pendiente de descarga).
