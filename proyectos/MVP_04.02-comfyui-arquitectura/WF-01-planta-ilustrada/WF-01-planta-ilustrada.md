---
tipo: proyecto
mvp: 04.02
wf: WF-01-planta-ilustrada
cliente:
proyecto:
ciudad:
pais:
fase: concepto
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [mvp_04.02, comfyui, controlnet, canny, planta-ilustrada, inmobiliaria]
estado: activo
---

# WF-01 — Planta técnica → planta ilustrada

> De una planta en PNG (negro sobre blanco) a un dibujo a color estilo marketing inmobiliario: misma distribución de ambientes, muebles sugeridos, sombras suaves. NO es un render perspectivo fotorreal (eso es otro WF, próximo ciclo).

- [[#1. Ficha]]
- [[#2. Modelo sugerido]]
- [[#3. Grafo]]
- [[#4. Prompts]]
- [[#5. Corridas]]
- [[#6. Evaluación]]
- [[#7. Backlog del WF]]

## 1. Ficha

| Campo | Valor |
|---|---|
| Objetivo | Planta ilustrada a color desde planta técnica PNG |
| Input | `inputs/planta-01.png` (negro sobre blanco, sin cotas chicas ni textos) |
| Output esperado | PNG a color, top-down, con muebles y sombras, líneas de la planta respetadas |
| Output NO esperado | Render perspectivo 3D, textos/cotas legibles (se agregan en post-producción) |
| Workflow base | `workflow_planta_canny_v1.json` (copiado de `n_03-WF01` Canny `BAK_v1.0.2`, sin modificar el original) |
| Hardware | Esta PC: RX 570 8GB DirectML. Sin RunPod |

## 2. Modelo sugerido

| Rol | Sugerido | Por qué |
|---|---|---|
| Checkpoint | `architecturerealmix_v11.safetensors` (SD1.5, ya instalado) | Tuneado para arquitectura, liviano en RX 570 (~60-90 s/img), ecosistema ControlNet SD1.5 completo |
| ControlNet | `control_v11p_sd15_canny.safetensors` (ya instalado), strength **0.9** / end **0.8** | Obliga al modelo a respetar tus líneas exactas; sin modelo Lineart instalado, Canny lo cubre si el PNG es limpio |
| KSampler | steps 30, cfg 7, sampler `euler`, scheduler `normal`, 512×512, denoise 1.0 (es ControlNet, no img2img) | Baseline validado en `n_03-WF01` |
| Alternativa | Scribble (`control_v11p_sd15_scribble.safetensors`, strength 0.6-0.7) si Canny sale muy rígido; Juggernaut XL queda para WF-02 entrega (SDXL en RX 570 es ~3-4× más lento, no para iterar) | Ver [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados\|modelos-recomendados]] |

## 3. Grafo

```
CheckpointLoaderSimple ──model──┐
    ├──clip─────────────────────┤
    └──vae──────────────────┐   │
                            │   │
LoadImage ──► ImageScale ──► Canny ──┐
(planta-01)   (512,lanczos) (30/100) │
                                     │
ControlNetLoader ──cn────────────────┤
(canny 689MB)                        │
                                     │
CLIPTextEncode (pos) ────────────────┤
CLIPTextEncode (neg) ────────────────┤
                                     ▼       ▼
ControlNetApplyAdvanced (0.9 / 0.0-0.8) ──► KSampler ──► VAEDecode ──► SaveImage
```

| Nodo | Clase | Parámetros propios de este WF |
|---|---|---|
| CheckpointLoader | `CheckpointLoaderSimple` | `architecturerealmix_v11.safetensors` |
| LoadImage | `LoadImage` | `inputs/planta-01.png` |
| ImageScale | `ImageScale` | 512×512, `lanczos`, crop center (regla obligatoria [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy\|reglas-workflows-comfy]] R1) |
| Canny | `CannyEdgeDetector` | low 30 / high 100 (normalizados 0-0.99) |
| ControlNetLoader | `ControlNetLoader` | `control_v11p_sd15_canny.safetensors` |
| ControlNetApply | `ControlNetApplyAdvanced` | strength 0.9, start 0.0, end 0.8 |
| CLIP pos/neg | `CLIPTextEncode` | ver §4 |
| KSampler | `KSampler` | steps 30, cfg 7, euler, normal, seed variable, denoise 1.0 |

Nodos genéricos (qué hace cada uno): [[wiki/glosario/software/comfyui|comfyui]].

## 4. Prompts

**Positivo base — versión ES (activa en el JSON):**

```
plano de planta arquitectonica ilustrado, vista en planta desde arriba,
a color, distribucion de muebles, sombras suaves, estilo folleto
inmobiliario, lineas limpias, alto detalle, ilustracion inmobiliaria
profesional
```

**Negativo base — versión ES (activa en el JSON):**

```
vista en perspectiva, render 3d, borroso, baja calidad, distorsionado,
marca de agua, texto, firma, caricatura, feo, deformado
```

**Variante EN (para test A/B contra ES — el modelo SD1.5 fue entrenado mayormente en inglés y suele rendir mejor):**

```
illustrated architectural floor plan, top-down view, colored,
furniture layout, soft shadows, marketing brochure style,
clean lines, high detail, professional real estate illustration
```

**Negativo EN:**

```
perspective view, 3d render, blurry, low quality, distorted,
watermark, text, signature, cartoon, ugly, deformed
```

**Variantes de estilo (sumar al positivo):** B1 = `piso de madera calida, ambientes acogedores` · B2 = `minimalista monocromo con un color de acento` · B3 = `estilo acuarela, trazo a mano alzada`.

## 5. Corridas

> Más nuevo → más arriba. Formato: fecha · seed · cambio vs anterior · archivo · tiempo · calidad /5 · nota.

| Fecha | Seed | Cambio | Archivo | Tiempo | Calidad | Nota |
|---|---|---|---|---|---|---|
| 2026-10-08 | 42 | pulido CON Canny: img2img F-03 + Canny 0.9/end 1.0 + denoise 0.25 | `salidas/n_01-F-05.png` | 141 s | _pendiente evaluación SOL_ | prompt_id `058aa972` — SIN DELIRIO: conserva F-03 + texturas/sombras sutiles |
| 2026-10-08 | 42 | pulido SIN Canny: img2img F-03 denoise 0.35 | `salidas/n_01-F-04.png` | 103 s | 2/5 — FALLIDA | prompt_id `38e7aa76` — DELIRIO: movió el baño, cambió muebles terraza, vació planta baja. Lección: 2ª pasada siempre CON Canny |
| 2026-10-08 | 42 | fix formas: latent+scale 512×832 (aspecto real), Canny 0.25/0.55, end 1.0, prompt EN + pista ambientes | `salidas/n_01-F-03.png` | 134 s | _pendiente evaluación SOL_ | prompt_id `c369f7f7` — MEJORA CLARA: baño/escalera/terraza reconocibles, "TERRAZA" casi legible |
| 2026-10-08 | 42 | test A/B idioma: prompt EN, mismo seed que F-01 | `salidas/n_01-F-02.png` | 102 s | _pendiente evaluación SOL_ | prompt_id `ea43aeac` — misma planta, muebles más definidos (comedor), texto deformado ("DERIGEA") |
| 2026-10-08 | 42 | baseline ES vía MCP (prompt español, Canny 0.9/end 0.8) | `salidas/n_01-F-01.png` | 193 s | _pendiente evaluación SOL_ | prompt_id `510e7a1f` — respeta líneas, look inmobiliario, texto deformado ("MENCTA") como esperado |
| _(pendiente)_ | | | | | | Esperando `inputs/planta-01.png` |

## 6. Evaluación

**Evaluación SOL 2026-10-08:** ningún resultado convence para entrega. F-05 es la mejor de las 5 pero el techo SD1.5 + Canny no alcanza el fotorrealismo buscado. **Decisión: WF-01 en pausa.** Se pasa a WF-02 inpainting (dibujar ventanas sobre renders) y WF-03 upscale. Revisit de planta ilustrada con SDXL o FLUX cuando haya hardware/RunPod.

## 7. Backlog del WF

- [ ] 3 corridas baseline letra F (`n_01-F-01/02/03.png`)
- [ ] Comparar Canny 0.9 vs 0.7 (fidelidad vs libertad)
- [ ] Variante Scribble si Canny sale rígido
- [ ] WF-02 (entrega): mismo input en Juggernaut XL SDXL
- [ ] Post-producción: re-agregar cotas/textos en Illustrator sobre el PNG ilustrado
- [ ] WF-02 (nuevo): Inpainting para dibujar ventanas — estilo video "ComfyUI For Architecture - Simple SDXL Inpainting Workflow" (https://www.youtube.com/watch?v=px8POauudLY). Probar primero con inpainting SD1.5 en esta PC (más liviano); SDXL inpainting solo si entra en 8 GB con `--lowvram`
- [ ] WF-03 (nuevo): Upscale entrega — upscaler 4x liviano (`4x_foolhardy_Remacri` o ClearReality, ~100 MB, la RX 570 lo banca) + Hires Fix (2º KSampler mismo costo que una corrida). Duda PC: solo el Hires, no el upscaler
