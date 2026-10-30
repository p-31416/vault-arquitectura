---
name: comfy-prompting
description: "Prompts y flujos de ComfyUI por modelo: SD 1.5, SDXL, FLUX.1, FLUX.2 y video (LTX-2.3, Kling 3.0, Seedance 2.0), con léxico de cine y fotografía. Se activa con prompt para comfy, flujo para sdxl, prompt flux, json flux2, video con ltx. Entrega prompt en el dialecto del modelo + cadena de nodos con parámetros."
---

# comfy-prompting — el dialecto cambia con el modelo

> La misma idea se escribe distinto según el modelo. Este skill es el router: identifica el modelo, abre su playbook y devuelve **prompt + flujo**. El léxico de cine y fotografía es común a todos; lo que cambia es el empaquetado.

## Cuándo se activa

- `@tim prompt …`, `prompt para comfy`, `prompt para sdxl`, `prompt para flux`
- `flujo para <modelo>`, `workflow json`, `nodos para …`
- `json flux2`, `structured prompt`
- `video con ltx`, `kling`, `seedance`, `recorrido`

## Los tres dialectos

| Dialecto | Modelos | Regla mental |
|---|---|---|
| **Keyword** | SD 1.5 · SDXL | Lista de descriptores separados por coma, lo importante primero, con pesos y **negativo obligatorio** |
| **Prosa** | FLUX.1 · FLUX.2 | Frase descriptiva, sin pesos ni tags de calidad, **sin negativo** |
| **JSON** | FLUX.2 | Objeto de claves fijas, seis hex, cámara anidada. Control quirúrgico por bloque |

## Router

| Si el modelo es… | Abrí | Y recordá |
|---|---|---|
| SD 1.5 | `references/sd15-sdxl.md` | 512² nativo · cfg 7–8 · ControlNet disponible · LoRA ≤250 MB |
| SDXL | `references/sd15-sdxl.md` | 1024² · cfg 3–4 · Union solo en RunPod |
| FLUX.1 | `references/flux1.md` | 1024² · cfg 1 (dev) o 4 steps (schnell) · sin negativo |
| FLUX.2 | `references/flux2.md` | klein no hace upsampling · JSON opcional · hasta 4 referencias |
| LTX-2.3 · Kling 3.0 · Seedance 2.0 | `references/video.md` | movimiento, cámara y tiempo son parte del prompt |
| Cualquiera | `references/lexico-cine-foto.md` | encuadre, lente, luz, material, stock |
| Cualquiera | `references/workflows-por-modelo.md` | cadena de nodos y parámetros |

## Contrato de salida

Toda respuesta entrega, en este orden:

1. **Modelo declarado** y por qué ese (una línea).
2. **Prompt** en bloque copiable. SD 1.5/SDXL agregan **negativo** en bloque aparte.
3. **Flujo**: cadena de nodos `A → B → C` con los valores propios del modelo.
4. **Parámetros**: resolución, steps, cfg, sampler, scheduler, seed, strength del LoRA.
5. **Racional**: una o dos líneas de qué hace el prompt y por qué.
6. **Siguiente paso**: qué cambiar primero.

Si SOL pide el archivo, el `workflow_<nombre>.json` va en API format dentro del WF y se valida con `comfyui_validate_workflow` antes de entregarlo.

## Reglas que no se negocian

1. Un LoRA vive sobre su modelo base. Nunca se mezcla.
2. Negativo solo en SD 1.5 y SDXL.
3. JSON solo en FLUX.2.
4. En FLUX.2 klein el prompt se escribe completo: no hay upsampling que lo complete.
5. Escalado por modelo: 512×512 en SD 1.5, megapíxeles en FLUX.2.
6. Sin CUDA: la estación es AMD RX 570 por DirectML.
7. Solo modelos que existen en `models/`; se confirman con `comfyui_list_local_models`.
8. Una variable por corrida.

## Fuentes verificadas

- FLUX.2 overview — https://docs.bfl.ai/flux_2/flux2_overview
- FLUX.2 [pro]/[max] prompting — https://docs.bfl.ai/guides/prompting_guide_flux2
- FLUX unified technical (aspect ratios, negativos, upsampling) — https://docs.us.bfl.ai/guides/prompting_unified_technical
- FLUX.2 [klein] generación rápida — https://help.bfl.ai/articles/7592221790-how-do-i-generate-quickly-with-flux-2-klein
- Prompting summary de la familia FLUX — https://docs.bfl.ai/guides/prompting_summary
- LTX-2.3 prompt guide — https://ltx.io/model/model-blog/ltx-2-3-prompt-guide
- Kling 3.0 user guide — https://kling.ai/quickstart/klingai-video-3-model-user-guide
- Seedance 2.0 guide — https://seedance2.ai/guide
- SD 1.5 prompt guide — https://stable-diffusion-art.com/prompt-guide/
- Vocabulario SDXL (encuadres, lentes, luz, color) — https://gist.github.com/lukecav/39431632378a63a7bc3860106943a96a
