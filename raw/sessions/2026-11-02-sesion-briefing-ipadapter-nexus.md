---
tipo: log
titulo: Sesión 2026-11-02 — briefing GxAI punto a punto + IPAdapter calco-estilo
fecha: 2026-11-02
tags: [sesion, concurso, gaudi-nexus, briefing, programa, ipadapter, pod, lora]
---

# Sesión 2026-11-02 — briefing punto a punto + set Comfy + IPAdapter

## Qué se hizo

1. **Briefing GxAI punto a punto**: leído `GxAI_BRIEFING_ES.pdf` local + URLs oficiales verificadas 200 (archademy.ai, briefings EN/ES, fundación). Creadas `02-briefing-punto-a-punto.md` (12 bloques) y `03-programa-punto-a-punto.md` (tabla triple 1500/1750/2000 + % plaza), enlazadas en `index.md`.
2. **Dos dictados Sol integrados citados**: reinterpretación libre del programa, piso triangular trencadís 3 colores, puestos tensados 1 apoyo 3 tipos, vecinal 50+100 con cáscaras -1 m techo verde, centro interpretación -1 m, mirador recorrido zoom lejos/cerca, oficina vidrio en T, puente-lengua Gaudí hasta Nacimiento + sutura parques. `reinterpretacion-programa-fractal.md` actualizada en consecuencia.
3. **Set Comfy en WF-Comfy-YT**: `10-prompts-prueba-nexus` (P-01..P-10 visión/estructura/requisitos/modelo), `11-diez-formas-sagrada-familia` (F-01..F-10), `20-reporte-corridas-YT` (hoja viva + 2 veredictos descartar), ficha `YT-02` (video LoRA SDXL pocas imágenes, pendiente ver).
4. **Pod unificado**: 5 archivos `pod-`/`comfy-vs`/`n8n-ciclo` fusionados en `workflows/00-pod-comfyui-unificado.md` (+ link playlist ítem 19 n8n, + §6 veredicto flux cuantizado: existe GGUF pero NO viable en RX 570 DirectML) y **borrados** tras verificar conservación. Referencias actualizadas (`00-index`, `00-conclusiones`).
5. **Precedentes LoRA**: `lora-precedentes-estudios.md` (Nire Haus Non-Commercial, mnml.ai con JSON+fanunnel, Arch Soul Apache 2.0), linkeado desde `lora-estudio-plan` §6.4.
6. **IPAdapter calco→estilo**: carpeta nueva con JSON v2 (16 nodos, 512 max, CN canny + strong style, prompt edificio sunscreen/hormigón/verde) + ficha. Descargados y verificados byte-exacto: `ip-adapter-plus_sdxl_vit-h` (847 MB) y `control_sdxl_canny_fp16` (2.5 GB). R4 OK. Corridas: gx-A-01 deforme/pálida (descartar), gx-B-01 croquis-sobre-croquis (descartar), gx-B-01v2 foto+estilo con detalle derretido (descartar). Próxima propuesta: gx-B-03 (denoise 0.3, style 0.5, CN 0.8), sin correr.
7. **Discrepancias detectadas** (no resueltas): `architecturerealmix` figura instalado pero no está en checkpoints/; SD1.5 era el único adapter hasta hoy.

## Archivos modificados

`02-briefing-punto-a-punto.md` · `03-programa-punto-a-punto.md` · `reinterpretacion-programa-fractal.md` · `proyectos/concurso-gaudi-nexus/index.md` · `10-prompts-prueba-nexus.md` · `11-diez-formas-sagrada-familia.md` · `20-reporte-corridas-YT.md` · `WF-Comfy-YT/00-index.md` · `YT-02-lora-sdxl-pocas-imagenes.md` · `00-pod-comfyui-unificado.md` (nuevo) · 5 pod- viejos (borrados) · `workflows/00-index.md` · `00-conclusiones.md` · `lora-precedentes-estudios.md` (nuevo) · `lora-estudio-plan.md` · `ipadapter-calco-estilo/` (JSON + ficha + salidas/, nuevo).

## Cerebro-digital

- **Topics**: programa-orientativo como cobertura para reinterpretar; piso triangular trencadís; mirador-recorrido vs punto; IPAdapter como puente calco→estilo y dataset futuro del LoRA; 512 max como política local; GGUF inviable en DirectML.
- **Entidades**: Sol (preceptos diseño), Emilia (iteración), Fundació Antoni Gaudí, Archademy, Nire Haus, mnml.ai, DorianAI (video n8n ítem 19), ALEXOTANO (regularización LoRA).
- **Hechos**: entrega 16/12 23:59 PDT A1 ≤15 MB + A4 opcional; programa 1500-2000 orientativo 45/25/15/15; premios 10k USD; klein 4B Apache vs 9B/dev Non-Commercial; A5000 $0.16/h; RX 570 solo SDXL; CN canny SDXL 2.5 GB en disco; gx-B-03 pendiente.
