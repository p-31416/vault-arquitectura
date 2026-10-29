---
tipo: backlog
workflow: WF-loras-locales
nivel: n_01-txt2img
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [backlog, lora, calibracion, rx570]
---

# 04-backlog — WF-loras-locales

Pendientes, ideas y decisiones abiertas de la calibración de LoRAs.

---

## Para la próxima sesión

- [ ] **Lanzar la tanda completa** (32 renders): `scripts/calibrar-loras-comfyui.py` con ComfyUI arriba.
- [ ] **Empezar por SD 1.5 strength 0,8** (9 renders, ~20 min) para tener lectura rápida antes de la tanda larga.
- [ ] **Registrar cada corrida** en `02-WF-log-WFloraslocales.md` (seed, strength, segundos, veredicto).
- [ ] **Decidir keepers**: con los renders a la vista, quedarse con 4–6 LoRAs y documentarlos en [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]] como "recomendados para el estudio".
- [ ] **Medir el techo SDXL**: los LoRAs de 870 MB (rank 128) definen si el techo de 900 MB se sostiene o baja.

## Decisiones abiertas

| Decisión | Estado | Nota |
|---|---|---|
| Techo SDXL 900 MB | Hipótesis | Pendiente de medir con los renders de rank 128 |
| Instalar LCM-LoRA / Hyper-SD | Documentado, sin instalar | La aceleración baja el render de ~132 s a ~25–30 s. Ver [[wiki/glosario/software/lora-locales-comfyui#Aceleración: candidatos para instalar\|§ Aceleración]] |
| `CIVITAI_API_TOKEN` | No definido en el entorno | Con el token se bajan los 5 LoRAs que piden login (incluye *Building Info Concepts Sheets*, sin sustituto) |
| Alternativa a CivitAI para LoRAs | Parcial | El mirror de HF del brutalista de JJ es la **variante FLUX** (no local) |
| Preprocesadores MiDaS/DPT | Ausentes | Requiere instalar `comfyui_controlnet_aux`; Depth Anything V3 ya es nativo en el core 0.28 |

## Ideas

- **Canny para los LoRAs de croquis.** `archisketch-v1`, `markerhandsketch-V1` y `landscape_architecture_sketch` piden ControlNet Canny (el propio CivitAI lo dice: *"need to pair with controlnet for finer controls"*, canny weight 0,8, CFG 7). Probar esos tres en un WF aparte con `ImageScale 512×512` (regla R1) en vez de txt2img puro.
- **Renders "de proyecto"**: con un LoRA de LoRAs + Canny sobre una planta real, el LoRA deja de ser estilo y pasa a ser material.
- **Contraste LoRA vs checkpoint**: Juggernaut XL ya es fotorrealista; los LoRAs SDXL como `ArcvizXL_V01` pueden sumar o estilar de más. Comparar contra `n_01-D-01.png` (baseline SDXL) para ver si aportan.
- **Perfil de VRAM por LoRA**: guardar el tiempo de render por LoRA en `PLANS/calibracion-loras.json` → tabla de costo/beneficio para elegir.

## Referencias

- [[wiki/glosario/software/lora-locales-comfyui|lora-locales-comfyui]]
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-loras-locales/00-README|00-README]]
- [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/A-WF-estadio/00-README|WF-estadio]] (baseline)
