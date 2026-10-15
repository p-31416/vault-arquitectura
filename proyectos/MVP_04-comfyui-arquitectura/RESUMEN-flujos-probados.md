---
tipo: indice
mvp: 04
fecha_creacion: 2026-10-14
ultima_actualizacion: 2026-10-14
tags: [mvp_04, resumen, corridas, salidas, baseline]
---

# RESUMEN — flujos probados e imágenes obtenidas (por flujo y por corrida)

> Foto del estado antes de la serie nueva n_07. Todo lo listado queda como lección aprendida, no se modifica. Detalle completo en cada `02-WF-log` de su carpeta.

## n_01 txt2img — A-WF-estadio (Realmix SD1.5 + Juggernaut SDXL) — 5 imágenes

| Corrida | Fecha | Modelo / params | Tiempo | Imagen | Lectura |
|---|---|---|---|---|---|
| n_01-A-01 | 2026-07-17 | Realmix, euler, 30 steps, cfg 7, seed 42, 768×512 | 114s | `A-WF-estadio/salidas/n_01-A-01.png` | Baseline. 21/35: sunset y césped OK, luz plana, bordes blandos |
| n_01-A-02 | 2026-07-18 | idem seed 42 | 88s | `n_01-A-02.png` | Repetibilidad: archivo distinto (731 vs 741 KB), variación estocástica normal |
| n_01-B-01 | 2026-07-18 | prompt nocturno floodlights (seed sin registrar) | ~88s | `n_01-B-01.png` | Atmósfera responde; seed perdida → no replicable |
| n_01-C-01 | 2026-07-24 | seed 43 | 88s | `n_01-C-01.png` | Variabilidad entre seeds confirmada |
| n_01-D-01 | 2026-07-24 | Juggernaut XL, dpmpp_2m/karras, 35 steps, cfg 4, 1216×832, --lowvram --cpu-vae | 562s | `n_01-D-01.png` | 1ª SDXL OK en RX 570; 6× más lenta que SD1.5 |

## n_01 txt2img — WF-vivienda (SDXL) — 0 imágenes

- 3 baselines A-01/A-02/A-03 planificados en log, **sin ejecutar** (`salidas/` vacía). Primer hueco a cerrar si se retoma SDXL.

## n_02 img2img — log-WF-croquis — 1 imagen

| Corrida | Fecha | Params | Tiempo | Imagen | Lectura |
|---|---|---|---|---|---|
| n_02-A-01 | 2026-07-18 | croquis001.jpg, denoise 0.7, prompt base | ~74s | `log-WF-croquis/salidas/n_02-A-01.png` | Baseline croquis→render OK gracias a ImageScale |
| (fallo previo) | 2026-07-18 | croquis 1600×1350 directo a VAE | OOM | — | **Nace la regla R1**: ImageScale 512 siempre |

## n_03 ControlNet — WF01-croquis-estadio — 7 imágenes

- `outputs-salidas/`: `n_03-v1.0.0_01/02/03` (Canny baseline), `n_03-v1.0.1_01`, `n_03-v1.0.2_01` (prompts tuneados), `n_03-v1.1a_01/02` (scribble).
- Dual Canny+Depth v1.1b validado en config (Canny 0.3 + Depth 1.0, Canny nativo + DA3 Small).

## n_06 moodboard — 10 imágenes

| WF | Corridas | Tiempo | Imágenes | Lectura |
|---|---|---|---|---|
| v1 Canny local | B-01 seed 42, Canny 0.31/0.59, CN 0.85, denoise 1.0 | 134s | `n_06-B-01.png` | Interior rústico guiado por croquis; IPAdapter ausente → fallback VAEEncode |
| v2 batch | B-02a/B-02b denoise 0.6 seed 100, B-03 denoise 0.75 seed 200 | 221s | `n_06-B-02a/b.png`, `n_06-B-03.png` | **Deriva a villa toscana** (prompt tuscan + batch híbrido + denoise alto) |
| v3 escalera | B-04 seed 300, CN 0.85, denoise 0.75 | 89s | `n_06-B-04.png` | Comedor piedra fiel a croquis2 |
| v4 parque | B-05 seed 400 txt2img directo | 77s | `n_06-B-05.png` | Parque OK; pajarera de hierro no aparece (falla prompt) |
| v5 fachada | OOM `ec4c64a7` (3 ramas 768px) → v5.1 secuencial C-01/C-02/C-03, CN 0.90, denoise 0.40 | 108/103/89s | `n_06-C-01/02/03.png` | **Lección: 1 rama/corrida**; C-01 puente+madera fiel |

## demo-manana (serie puente) — 0 imágenes (JSON listos, sin correr)

- `demo-manana/`: 01 txt2img casa hormigón · 02 img2img golden hour (denoise 0.65) · 03 stack 2 LoRAs. Hoy se corrigieron los `lora_name` a los archivos reales.

## Totales

- **23 imágenes** en `salidas/` (5 + 0 + 1 + 7 + 10). Modelos usados: Realmix (mayoría), Juggernaut (1). Tiempos SD1.5 típicos 77-221s; SDXL 562s.
- Huecos: WF-vivienda sin correr, evaluaciones /35 casi todas pendientes de inspección visual, upscalers e IPAdapter ausentes.
