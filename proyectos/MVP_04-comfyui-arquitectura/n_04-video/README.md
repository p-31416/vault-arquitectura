# Nivel 04: Video — Walkthrough Arquitectónico Animado

## Objetivo (futuro)

Generar animaciones de walkthrough arquitectónico a partir de renders fijos, usando modelos de video como LTX-2.3 y WAN 2.2.

## Pipeline propuesto

```
Render fijo → LTX-2.3 I2V → Walkthrough 480p → Upscale 4x → RIFE interpolación → Video final 1080p
```

## Requerimientos de hardware

| Modelo | VRAM mínima | VRAM recomendada |
|--------|-------------|------------------|
| LTX-2.3 Q4_K_S | 12GB | 24GB |
| WAN 2.2 I2V fp8 | 16GB | 24GB+ |

## Uso arquitectónico

- Walkthrough de espacio interior a partir de render
- Animación de fachada desde diferentes ángulos
- Time-lapse de construcción (futuro)
- Video con audio sincronizado (LTX-2.3)

## Pendiente

- [ ] Hardware adecuado (RunPod o GPU 24GB+)
- [ ] Workflow LTX-2.3 img2vid
- [ ] Workflow WAN 2.2 img2vid
- [ ] Post-procesamiento: upscale 4x + interpolación
