---
tipo: flujo
mvp: 08
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [mvp_08, F0, prompt, casa-moderna, buenos-aires, sdxl]
idioma: es
---

# F0 — prompt casa base (Buenos Aires, hormigón visto)

> JSON canónico: `workflow_F0b-casa-base_realvis.json` — RealVisXL V5.0 estándar (`realvisxlV50_v50Bakedvae.safetensors`), 1216x832, 32 steps, cfg 4, seed 42 (ya trae este prompt + títulos 🔵/🔴). Keeper verificada 2026-11-12: [activos/proyectos/MVP_08-casa-moderna/flujos/salidas/casa-F0b-v01-T3-steps40-keeper.png].
> Archivado: `workflow_F0-casa-base_lightning.json` → `_archivados/` (Lightning 512 salía blanda/deformada).
> Convención fija del estudio: **positivo en azul, negativo en rojo**. En el canvas: clic derecho en el nodo → Color → azul/rojo (una vez; el título 🔵/🔴 ya viene en el JSON).

## Positivo (🔵 — lo único que cambia entre pruebas de estilo)

```text
photorealistic, raw photo, 8k uhd, architectural photography,
modern single-family house in Buenos Aires, Argentina,
urban context between neighboring party walls,
board-formed exposed concrete facade,
black steel window frames,
secondary materials of dark timber slats and blackened iron details,
flat roof, small front patio with native plants,
late afternoon warm light, long soft shadows,
eye-level street view, 24mm tilt-shift lens,
sharp focus, highly detailed
```

Bloques (ubicación → entorno → materiales → luz → cámara), en ese orden. Para variar material/hora se toca solo su bloque.

## Negativo (🔴 — fijo del estudio, no se toca)

```text
blurry, low quality, distorted, deformed, ugly,
suburban detached villa, countryside, forest, beach,
cartoon, illustration, painting, drawing,
watermark, text, signature, logo,
oversaturated, overexposed, underexposed, grain, noise,
people, cars
```

## KSampler — valores normales (RealVis canónico)

| Param | Normal | Rango que se puede tocar | Efecto |
|---|---|---|---|
| seed | 42 fija | 42 / 77 / aleatoria | 42 = repetible; cambiar = otra casa |
| steps | 32 | 24–40 | +steps = más detalle, +tiempo lineal |
| cfg | 4 | 3–5 | +cfg = más obediencia al prompt, riesgo de quemado |
| sampler | dpmpp_2m | dpmpp_2m / dpmpp_sde | sde = más textura, más lento |
| scheduler | karras | karras / normal / simple | karras = default probado |
| denoise | 1.0 | solo txt2img (F0 siempre 1.0) | en img2img manda (F1–F4) |
| tamaño | 1216×832 | fijo local | apaisada calle completa |

## Cómo funciona el seed (leer antes de tocar nada)

El seed es el número del sorteo inicial de ruido: **mismo seed + mismo prompt + mismo modelo + mismos params = misma imagen** (repetible, por eso la T1 es la referencia). Cambiar steps o cfg con el mismo seed NO cambia la casa: cambia solo el render de ese mismo ruido (más detalle / más obediencia). Cambiar el seed (T2) es otra casa del mismo estilo.

- T1 (seed 42) vs T2 (seed 77): **distinta casa**, mismo estilo → se elige la mejor.
- T1 (seed 42, steps 32) vs T3 (seed 42, steps 40): **misma casa**, más detalle fino → se comparan lado a lado.
- T1 vs T4 (seed 42, cfg 5): misma casa, prompt más obedecido (si quema blancos, se vuelve a 4).

## 5 pruebas mínimas F0 (una variable por prueba, seed 42 salvo T2)

| # | Cambio | Esperado | Salida |
|---|---|---|---|
| T1 | base tal cual (seed 42) | base referencia | [activos/proyectos/MVP_08-casa-moderna/flujos/salidas/casa-F0b-v01-T1-seed42.png] |
| T2 | seed aleatorio 1104876903174892 | otra casa, mismo estilo | [activos/proyectos/MVP_08-casa-moderna/flujos/salidas/casa-F0b-v01-T2-seed1104876903174892.png] |
| T3 | steps 40, seed 42 | ✅ KEEPER Sol 2026-11-12 | [activos/proyectos/MVP_08-casa-moderna/flujos/salidas/casa-F0b-v01-T3-steps40-keeper.png] |
| T4 | cfg 5, seed 42 | quemó listones (rojizo) | [activos/proyectos/MVP_08-casa-moderna/flujos/salidas/casa-F0b-v01-T4-cfg5.png] |
| T5 | 832×1216 vertical, seed 42 | otra casa (cambia el ruido) | [activos/proyectos/MVP_08-casa-moderna/flujos/salidas/casa-F0b-v01-T5-vertical.png] |

Keeper T3 → alimenta F1–F4. Registrar en dashboard casa + reporte 20.
