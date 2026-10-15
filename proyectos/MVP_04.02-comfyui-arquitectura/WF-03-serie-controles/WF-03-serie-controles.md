---
tipo: proyecto
mvp: 04.02
wf: WF-03-serie-controles
cliente:
proyecto:
ciudad:
pais:
fase: concepto
fecha_creacion: 2026-10-09
ultima_actualizacion: 2026-10-09
tags: [mvp_04.02, comfyui, img2img, scribble, canny, depth, lora, serie]
estado: activo
---

# WF-03 — Serie de controles (5 flujos, 1 imagen)

> Comparar 5 niveles de control sobre la MISMA imagen, del más libre al más dirigido. Spec general: [[proyectos/MVP_04.02-comfyui-arquitectura/WF-03-serie-controles/SPECS/serie-controles-spec|serie-controles-spec]].

- [[#1. Ficha]]
- [[#2. F-A — img2img sin ControlNet (detalle nodo por nodo)]]
- [[#3. Definition of Done de F-A]]
- [[#4. Matriz de pruebas F-A]]
- [[#5. Corridas]]
- [[#6. F-B / F-C / F-D / F-E (resumen y estado)]]
- [[#7. Backlog del WF]]

## 1. Ficha

| Campo | Valor |
|---|---|
| Objetivo | Decidir qué nivel de control usar en cada caso del estudio, comparando 5 flujos sobre 1 imagen |
| Input | `inputs/base-01.png` (casa moderna, 768×512, generada con `workflow_base_txt2img_v1.json`, seed 42) |
| Output esperado | 5 imágenes `salidas/n_03-F-0X.png` comparables entre sí (mismo seed 42) |
| Hardware | Esta PC: RX 570 8GB DirectML. Sin RunPod |

## 2. F-A — img2img sin ControlNet (detalle nodo por nodo)

**Objetivo de F-A:** establecer el piso de la comparación — qué cambia SOLO con prompt, sin ningún control geométrico. Todo lo que F-B..F-E conserven de más, es mérito del control.

**Archivo arrastrable:** `workflow_FA_img2img_v1_ui.json` (validado: 9 nodos, 0 errores).

| # | Nodo | Qué hace (en criollo) | Parámetros en este flujo |
|---|---|---|---|
| 1 | `CheckpointLoaderSimple` | Carga el "cerebro": ArchitectureRealmix SD1.5 | `architecturerealmix_v11.safetensors` |
| 2 | `LoadImage` | Lee tu imagen base del `input` de ComfyUI | `base-01.png` |
| 3 | `CLIPTextEncode` (+) | Traduce tu pedido a idioma-modelo: misma casa al atardecer, ventanas iluminadas | Ver §4 prompts |
| 4 | `CLIPTextEncode` (−) | Lo prohibido: borroso, deformado, gente, autos | Ver §4 prompts |
| 5 | `ImageScale` | Normaliza a 768×512 con lanczos (REGLA R1: nunca mandar tamaño impredecible a VRAM) | `lanczos`, 768×512, `center` |
| 6 | `VAEEncode` | Comprime la imagen a "latente" (el formato interno en que el modelo piensa) | — (solo conexiones) |
| 7 | `KSampler` | El motor: agrega ruido según `denoise` y lo quita guiado por tu prompt. **El mando del flujo** | seed 42, steps 30, cfg 7, euler+normal, **denoise 0.6** |
| 8 | `VAEDecode` | Descomprime el latente a imagen visible | — (solo conexiones) |
| 9 | `SaveImage` | Guarda con prefijo | `WF03-FA` |

**Por qué denoise 0.6:** la doc oficial dice que es LA clave del img2img — *"the smaller the value, the smaller the difference vs the reference"* (https://docs.comfy.org/tutorials/basic/image-to-image.md, verificado 200 el 2026-10-09). 0.6 = re-estilo manteniendo composición (0.3 sería retoque leve, 1.0 ignoraría tu imagen).

## 3. Definition of Done de F-A

F-A se da por **aprobado** si, en al menos 2 de 3 corridas de la matriz:

1. **Composición preservada:** mismos volúmenes, misma posición de aberturas, mismo encuadre que `base-01.png`.
2. **Cambio solicitado visible:** luz de atardecer + ventanas iluminadas (lo que pide el prompt).
3. **Sin invenciones:** ningún volumen, piso ni ambiente nuevo que no exista en la base.
4. **Calidad mínima:** sin caras/firmas/textos deformes dominantes, sin borrosidad general.

Si no pasa: bajar denoise a 0.4 (más fidelidad) antes de culpar al modelo.

## 4. Matriz de pruebas F-A

| Test | Variable | Seed | Versión | Archivo | Para qué |
|---|---|---|---|---|---|
| T1 | denoise 0.6 (baseline) | 42 | `3.0.0.0` | `salidas/n_03-F-A-v3.0.0.0.png` | El DoD se evalúa acá |
| T-prompt | solo prompts (sunset + sol derecha) | 42 | `3.0.0.1` | `salidas/n_03-F-A-v3.0.0.1.png` | ¿El prompt mueve el sol? → No (ver §5) |
| T2 | denoise 0.4 | 42 | `3.0.0.2` | `salidas/n_03-F-A-v3.0.0.2.png` | ¿Cuánta fidelidad se gana? |
| T3 | denoise 0.8 | 42 | `3.0.0.3` | `salidas/n_03-F-A-v3.0.0.3.png` | ¿Cuánta reinterpretación aparece? (+candidato a mover el sol) |

Esquema `X.Y.Z.W`: `W` = cambio mínimo (mismo grafo: prompt, seed, denoise fino) · `Z` = cambio medio (nodo agregado, modelo cambiado, strength, resolución) · `Y` = pipeline (F-A→0, F-B→1, F-C→2, F-D→3, F-E→4) · `X` = familia/enfoque mayor (`3` = WF-03; `4` = enfoque diferente del mismo workflow).

Mismo seed en los 3: la única variable es el denoise. Cada test ≈ 2 min en RX 570.

## 5. Corridas

> Más nuevo → más arriba.

| Fecha | Versión | Test | Seed | Cambio | Archivo | Vista | Tiempo | Calidad | Nota |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-09 | `3.0.0.1` | T-prompt | 42 | solo prompts (sunset + sol derecha, negativo anti-izquierda), mismo grafo | `salidas/n_03-F-A-v3.0.0.1.png` (origen: `WF03-v3.0.0.1_00001_.png`, prompt_id `e0d1a0b5`) | ![3.0.0.1](salidas/n_03-F-A-v3.0.0.1.png) | 190 s | ❌ sol sigue a la izquierda, cielo diurno (no atardecer) · ✅ composición, vegetación e interiores iluminados preservados | `+`: ...sun setting on the right side of the frame, warm golden sunlight coming from the right, long soft shadows falling to the left... lush detailed vegetation and shrubs · `−`: ...sun on the left side, morning light, flat lighting, overcast sky, dull colors. **Diagnóstico:** con denoise 0.6 el prompt no mueve el sol — la luz queda anclada a la base. Siguiente variable: denoise/sampler, no prompt. |
| 2026-10-09 | `3.0.0.0` | T1 | 42 | baseline denoise 0.6, primera corrida de la serie | `salidas/n_03-F-A-v3.0.0.0.png` (origen: `WF03-FA_00001_.png`, prompt_id `81141c83`) | ![3.0.0.0](salidas/n_03-F-A-v3.0.0.0.png) | 208 s | ✅ composición preservada, dusk + ventanas iluminadas visibles | `+`: same modern minimalist house exterior at dusk, warm glowing windows, concrete and wood facade, dramatic evening sky, photorealistic, architectural photography, 8k, highly detailed · `−`: blurry, low quality, distorted, watermark, text, signature, cartoon, illustration, ugly, deformed, people, cars · euler+normal, steps 30, cfg 7, denoise 0.6, lanczos 768×512 |
| _(pendiente)_ | `3.0.0.2` | T2 | 42 | denoise 0.4 | `salidas/n_03-F-A-v3.0.0.2.png` | — | | | |
| 2026-10-09 | `3.0.0.3` | T3 | 42 | denoise 0.8, mismo prompt sunset | `salidas/n_03-F-A-v3.0.0.3.png` (origen: `WF03-v3.0.0.3_00001_.png`, prompt_id `e3c539cf`) | ![3.0.0.3](salidas/n_03-F-A-v3.0.0.3.png) | 145 s | ❌ sigue diurno, sol no definido a la derecha · ❌ se perdió el brillo cálido interior (ventanas apagadas) · ✅ composición y vegetación preservadas | Mismo prompt sunset que `3.0.0.1`. **Diagnóstico:** ni prompt ni denoise mueven el sol en img2img desde una base diurna — la luz global queda anclada a `base-01.png`. F-A no relocaliza el sol; documentado como límite del flujo. |

**Metadata `3.0.0.0` verificada:** el PNG incluye prompt + workflow (UI id `5cc3dfe9-ee19-4d81-9ff2-c59fc9d00baa` = canvas del link). Se abre en ConfUI por arrastre o clic derecho. Copia con metadata intacta (ejecutar en terminal):

```powershell
Copy-Item -LiteralPath "C:\Users\Solch16\AppData\Local\Temp\comfyui-images\WF03-FA_00001_.png" -Destination "P:\00-repos\proyecto-pi\vault-arquitectura\proyectos\MVP_04.02-comfyui-arquitectura\WF-03-serie-controles\salidas\n_03-F-A-v3.0.0.0.png"
```

## 6. F-B / F-C / F-D / F-E (resumen y estado)

| Flujo | Suma | Estado |
|---|---|---|
| F-B Scribble (strength 0.7, sin preprocesador) | Control suelto sobre base F-A | ⏳ pendiente — JSON a armar tras F-A |
| F-C Canny (0.25/0.55, strength 0.9/end 1.0) | Bordes exactos, params validados WF-01 | ⏳ pendiente |
| F-D Depth (dpt_hybrid, 0.75/0.85) | Volumen/sombras — **bloqueado**: falta aux pack (install git+pip+reinicio, decisión SOL: junto a Fase B) | 🔒 bloqueado |
| F-E LoRA A+B (0.6-0.8 sobre F-C) | Estilo Architectural Sketch + detalle — **desbloqueado 2026-10-14**: `markerhandsketch-V1` (9 MB) + `archisketch-v1` (18 MB) en `P:\00-repos\ComfyUI\models\loras\` (cubren rol estilo; B detail-enhancer 1911622 queda descarga opcional) | 🟢 listo para correr |

Detalle completo de cada uno: [[proyectos/MVP_04.02-comfyui-arquitectura/WF-03-serie-controles/SPECS/serie-controles-spec|serie-controles-spec]] §5-§8.

## 7. Backlog del WF

- [ ] T1/T2/T3 de F-A + evaluación DoD (§3)
- [ ] Armar JSONs UI de F-B y F-C
- [ ] Descargar LoRA A+B + F-E (×2)
- [ ] Install aux pack + reinicio + F-D
- [ ] Evaluación final serie: qué flujo para cada caso del estudio
- [ ] F8 (mañana): fijar geometría con ControlNet + aplicar LoRA — Canny 0.9/end 0.85 sobre base + markers 0.8-1.0, denoise 0.4-0.6. Hipótesis: el CN retiene la identidad que el denoise alto pierde (lección 2.1.0 vs 2.1.1). JSON a armar + matriz seed 42
