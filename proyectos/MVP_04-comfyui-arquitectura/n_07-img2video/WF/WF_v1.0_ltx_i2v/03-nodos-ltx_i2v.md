---
tipo: regla
mvp: 04
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
tags: [mvp_04, img2video, nodos, configs]
---

# 03-nodos — configs propias de WF_ltx_i2v

De lo genérico foraltar (reglas comúnes en [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]]).

## Escalado del start frame (aplica R2 — la imagen de entrada manda la resolución del modelo)

| Nodo | Widget | Valor | Motivo |
|---|---|---|---|
| `ImageScale` | width/height | 768 / 512 | Resolución típica VAE LTX 2.3; múltiplo de 32 |
| | upscale_method | `bilinear` | foto/render (no controlnet) |
| | crop | `center` | recorte controlado si el input no respeta 3:2 |

**Transferencia:** a 768×512 hace match del blanco de resolución `resolution: 768x512` (rounded a 32) del canvas de inicio — es lo que la entrada MCP espera para LTX.

## Timing

| Parámetro | Valor |
|---|---|
| `frame_rate` / `fps` | 25 |
| `length` | 97 (8n+1 ≈ 4 s) |
| `steps` | 8 (distilled) |
| `cfg` | 1.0 (distilled, CFG off) |
| `max_shift / base_shift` | 2.05 / 0.95 |
| `strength (i2v)` | **pendiente primera corrida** — start conservador 0.6; 1.0 congela el clip |

## Seed

- `RandomNoise.noise_seed` con valor fijo para las corridas de **baseline A** (3 idénticas)
- Baseline B en adelante: seed aleatoria

## Salidas

- Nomenclatura `n_07-{LETRA}-{NN}.mp4` (misma tabla de letras que el estándar de MVP_04)
- `filename_prefix` actual: `n_07-img2video/ltx-2.3`
