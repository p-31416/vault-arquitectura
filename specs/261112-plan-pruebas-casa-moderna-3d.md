---
tipo: plan
proyecto: concurso-gaudi-nexus
titulo: Plan pruebas casa moderna simple a 3D a urbano Gaudi
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
estado: borrador-activo
tags: [plan, pruebas, casa-moderna, 3d, rhino, urbano, gaudi, sdxl, gratis]
idioma: es
---

# Plan pruebas — casa moderna simple → cambios → 3D → urbano Gaudí

> Integra sin duplicar: [[specs/261030-plan-continuacion-pruebas|campaña 261030 fases A–I]] · [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz concurso]] · [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-index|WF-Comfy-YT YT-01–04]] · [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/10-prompts-prueba-nexus|P-01–P-10]] · [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/11-diez-formas-sagrada-familia|F-01–F-10]] · [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/30-backlog-futuras-pruebas|backlog 30]] · [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/20-reporte-corridas-YT|reporte 20]] · [[proyectos/concurso-gaudi-nexus/workflows/WF-curso/01-index-sdxl-vista|sdxl-vista 7 WF]] · [[specs/261112-diagnostico-controlnet-inpaint-upscale|diagnóstico nodos]] · [[specs/261112-veredicto-comfy-vs-openhiggsfield|veredicto Comfy]] · [[specs/261112-plan-lamina-1000x700|plan lámina A1]] · [[MUSE.md#L4027|MUSE.md]].
> Videos YT: índice curado en [[wiki/fuentes/00-index-yt|00-index-yt]] (71 videos, creador/duración/tags/estado) + pipeline en `raw/yt/00-index`; transcripciones curso en `raw/yt/transcripts/`. No hay sheet de videos en el vault — la lista viva es 00-index-yt.

## 0. Mejor modelo local (veredicto)

RX 570 8GB DirectML, flags nuevos (sin `--disable-dynamic-vram`, con `--reserve-vram 1.0`):

| Uso | Modelo | Por qué |
|---|---|---|
| Iterar rápido | RealVisXL Lightning 4-6 pasos CFG 1-2 | 80-400s por imagen, misma familia que final |
| Calidad final | RealVisXL V5.0 30-35 pasos CFG 3-4 / Juggernaut Ragnarok | BakedVAE (carpeta vae vacía), ✅ comercial con matices |
| Retador | Juggernaut Ragnarok vs v9 | compara anatomía/manos en misma seed |
| Inpaint liviano | sd-v1-5-inpainting-fp16 | 2GB, ideal RX 570 |
| Relight | IC-Light `iclight_sd15_fc` (en disco) | cambia sol sin regenerar |

Regla estudio: láminas solo filas ✅ (ver `modelos-recomendados`); ArchitectureRealmix solo tests internos (⛔ comercial). SD1.5 queda fuera por tu decisión — todo este plan es SDXL.

## 1. Base casa moderna simple (F0)

Parte de [[proyectos/MVP_04-comfyui-arquitectura/A-txt2img/WF-vivienda/01-index|WF-vivienda]]: `workflow_txt2img_vivienda_sdxl.json`, Juggernaut v9, 1216×832, dpmpp_2m/karras 35 steps cfg 4, prompt casa hormigón+vidrio 24mm tilt-shift. 1 corrida seed 42 = keeper base `casa-base.png`. Si tarda >12min, baja a 1024x640 Lightning para iterar y reserva 1216x832 al final.

## 2. Cambios sobre la casa (F1, una variable por corrida)

| Prueba |Workflow | Cambio | Denoise/params | Qué mirar | Registro |
|---|---|---|---|---|---|
| T-camara izq | YT-03 `workflow_YT-03-vista-nueva.json` | prompt `new viewpoint 15° left, eye-level` | 0.65, seed 7 | misma obra, sombras coherentes | reporte 20 |
| T-camara low | mismo | `low angle looking up` | 0.6 | verticales a plomo | reporte 20 |
| T-aerea | mismo | `elevated three-quarter` | 0.7 | cubierta creíble | reporte 20 |
| T-noche | mismo | `same viewpoint, night warm interior` | 0.55 | conserva encuadre | reporte 20 |
| T-luz dia/tarde | IC-Light fc (backlog L1/L2) | `morning soft / golden hour / night` | strength fc | solo cambia luz | backlog 30 L1 |
| T-luz lora | backlog L3 | CinelightX/Chiaroscuro 0.3-0.6 | sobre Juggernaut | dirección de luz | backlog 30 L3 |
| T-muebles | YT-01 inpaint / YT-03-alt | máscara zona + `add linen sofa, keep walls` | 0.8 solo máscara | bordes coherentes | YT-01 T1–T5 |
| T-material | WF_v5 fachada | prompt hormigón↔madera | 0.4-0.6 | conserva geometría | WF_v5 C01–C03 |
| T-perspectiva | F-03/F-04 | depth 0.85-1.0 / canny 0.7+depth 0.5 | 0.35-0.45 | lock geométrico | F-03/F-04 |

Escalera denoise si pierde identidad: 0.5 → 0.65 → 0.8. Variante modelo: repetir T-camara con RealVisXL v5.0.

## 3. Desde 3D (F2)

1. YT-04 `workflow_YT-04-rhino-vivo.json`: captura viewport Rhino (`scripts/rhino-mcp-cli.py shot`) + canny → corrida T1. Requiere `s` si falta base SD1.5 — sustituir checkpoint a inpainting o Juggernaut según ficha §7.
2. WF-03 rhino→imagen (SDXL, denoise 0.65) + upscale ESRGAN (ver diagnóstico §4, no LatentUpscale).
3. Negro = aberturas: planos negros en Rhino → prompt los convierte en loggias (técnica módulo 3 [00:40:11]).

## 4. Urbano Gaudí (F3)

Con la casa validada, sube a plaza con P-01–P-10 + F-01–F-10 + matriz WF-01–07:
P-01 captura+trazo, P-02 rhino→foto, P-04 inpaint plaza, P-05 puestos, P-07 mirador zoom, P-08 cocina, F-01 foto real+inpaint (más fiel), F-03 depth lock, F-08 doble sampler, F-09 upscale con máscara Sagrada. Final A1 según plan lámina.

## 5. Orden de ejecución $0

Semana 1 local: F0 → T-camara (4) → T-luz (2) → T-muebles (2) → T-material (1). Semana 2: F2 3D → F3 P-01/P-04/F-01. Pod solo si SDXL no rinde (F6–F8 backlog, Flux klein 4B). Pollinations free solo borrador.

## 6. Gates

- G0: F0 keeper `casa-base.png` aprobado por Sol.
- G1: 1 keeper por familia (cámara/luz/muebles/material) en reporte 20.
- G2: 1 captura Rhino → render YT-04 OK.
- G3: P-01 + F-01 keeper plaza → entra a lámina A1.

## 7. Registro

Cada corrida: fila en reporte 20 (probamos/config/miniatura/sucedió/veredicto/solución/costo) + `gx-{L}-{NN}.png` en `salidas/` + seed/prompt/modelo. Lo nuevo de YT/Sherlock suma a matriz, no duplica (backlog 30 §3–4).
