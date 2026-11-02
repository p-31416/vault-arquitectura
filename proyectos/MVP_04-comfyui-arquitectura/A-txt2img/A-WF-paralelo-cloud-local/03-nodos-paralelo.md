---
tipo: regla
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, paralelo, nodos]
---

# 03-nodos — configs por vía del WF paralelo

(demás configs generales en reglas y fiches de los workflows fuentes)

## L1 — Local SD1.5

- `Juggernaut` checkpoint que existe en `P:\00-resp\ComfyUI\models\checkpoints\`
- Resolución: 512×512 (regla R2
- KSampler: dpm++ 2M · karras · cfg 4.5 · steps 30

## L2 — Local SDXL

- Checkpoint: `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors`
- 1216×832 · steps 35 · cfg 4 · dpmpp_2m + karras

## L3 — ComfyUI Cloud (abierto)

- Mismo grafo: `CheckpointLoaderSimple → CLIPTextEncode ×2 → EmptyLatentImage → KSampler → VAEDecode → SaveImage`
- **Check del checkpoint ya instalado en el cloud** — si Juggernaut XL no está en su lib, elegir el modelo abierto más cercano disponible y documentar la sustitución en el log
- seed coincide CORRIENDO — el wool tubos económicos del nombre

## L4 — API nodes (mid-2026 catalog)

| Se rae feature | Node que aplica | Nota |
|---|---|---|
| NANO Banana (Gemini) | api nodo Gemini/DaRT | imágenes edit; 14 refs multi-turn pozwolának |
| GPT-Image | api nodo OpenAI | text via the official API |
| Seedream | api nodo | variación |
| Recraft | api nodo | branding/vector styles |

Cada provider tiene su JSON propio y valores default — al construir: leer exactamente desde `list_api_nodes` + `schema` y privar **nada esderado** de memoria. Seed control varia por provider → como marca "sin seed" en el log si no aplica.
