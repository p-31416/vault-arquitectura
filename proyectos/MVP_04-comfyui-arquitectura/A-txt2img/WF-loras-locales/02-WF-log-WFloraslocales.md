---
tipo: wf-log
workflow: WF-loras-locales
nivel: n_01-txt2img
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
tags: [wf-log, lora, calibracion, rx570]
---

# 02-WF-log — WF-loras-locales

**Log de todas las corridas de calibración.** Más nuevo → más arriba.
Cada corrida → una entrada aquí + imagen en `salidas/n_01-G-{NN}.png` + fila en `PLANS/calibracion-loras.json`.

> **Estado 2026-10-28:** sin corridas todavía. El script quedó escrito y verificado en `--dry-run`; la tanda arranca cuando ComfyUI esté arriba. Se abortó el primer intento de tanda (job `99eeabec` cancelado) a pedido del estudio: primero documentación, después renders.

---

## Plantilla de entrada

```markdown
## n_01-G-{NN} — {YYYY-MM-DD} — {HH:MM}

**LoRA:** `archivo.safetensors` · base SD 1.5 · rank {r} · {tamaño}
**Trigger:** `{trigger}`
**Strength:** 0,6 | 0,8
**Archivo output:** `salidas/n_01-G-{NN}.png`
**ComfyUI output:** `loras/n_01-G-{NN}_00001_.png`

### Configuración
| Parámetro | Valor |
|-----------|-------|
| Seed | 42 |
| Steps | 30 |
| CFG | 7 (SD1.5) / 4 (SDXL) |
| Sampler | euler_ancestral (SD1.5) / dpmpp_2m (SDXL) |
| Scheduler | karras |
| Resolution | 768×512 (SD1.5) / 1216×832 (SDXL) |
| Checkpoint | architecturerealmix_v11 / Juggernaut-XL_v9 |
| Flags | --directml 0 --force-fp16 --lowvram --cpu-vae |

### Métricas
| Métrica | Valor |
|---------|-------|
| Tiempo generación | ~XXX s |
| Tamaño archivo | XXX KB |
| VRAM peak | (a completar) |

### Observaciones
- [Qué aporta el LoRA sobre el baseline]
- [Artefactos / efectos no deseados]
- [Decisión: mantener / descartar / ajustar fuerza]
```

---

## Registro de corridas

_(sin corridas registradas — la tanda se lanza con `scripts/calibrar-loras-comfyui.py`)_
