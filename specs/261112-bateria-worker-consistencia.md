---
tipo: spec
fecha_creacion: 2026-11-12
ultima_actualizacion: 2026-11-12
tags: [spec, plan, bateria, worker, klein-4b, consistencia, cloudflare]
idioma: es
---

# Batería worker: consistencia sobre la misma imagen (klein-4b)

> Responde: ¿se puede cambiar ángulo, temporada, clima y materiales específicos sobre MI imagen sin perder la original? Base única real: `cf-schnell-cascara-01.jpg` (render propio, no placeholder). Refs <512px (límite Workers AI) — se achican antes de enviar.

## Mapeo Comfy → worker

| Flujo Comfy (vault) | Equivalente worker | Test |
|---|---|---|
| n_02 img2img croquis→render | klein edit con instrucción | W1–W4 |
| n_03 ControlNet (respeta geometría) | klein conserva+cambia | W1–W4 (¿aguanta sin CN?) |
| A-txt2img RealVis/Juggernaut | schnell txt2img | Ya hecho (bases) |
| WF-loras / rhino-to-image | Sin equivalente (requiere pesos) | Pod/local, fuera de esta batería |
| n_09 upscale | Sin equivalente en worker | Fuera |

## Batería (misma base, 1 variable por test)

| ID | Cambio | Prompt edit (EN) | Qué valida |
|---|---|---|---|
| W1 | Temporada → invierno | Same plaza and shell, winter: snow on vaults and paving, bare trees, cold overcast light | Estación sin mover geometría |
| W2 | Clima/hora → noche | Same view at night: warm interior light glowing through glass, dark blue sky, street lamps on | Hora sin mover cámara |
| W3 | Material → madera | Same shell geometry rebuilt in glulam timber ribs with wood grain, warm tones | Material específico |
| W4 | Ángulo → aérea (límite) | Same pavilion seen from high aerial view, plaza context | LÍMITE: ¿mantiene el edificio? |
| W5 | Multi-ref + material | Base + 2ª ref material: apply material of image 1 to shell | Transferencia multi-ref |
| W6 | Seed reproducible | Mismo prompt + seed 42, dos corridas → comparar bytes | Reproducibilidad |
| W7 | Guidance alta vs baja | Mismo edit, guidance 8 vs 1.5 | Sensibilidad del control |

Criterio: W1–W3 deben conservar geometría y cámara; W4 documenta el límite (se espera deriva); W5–W7 calibran la herramienta.

## Ejecución 2026-11-12 (base `cf-schnell-cascara-01-512.jpg`)

| ID | Archivo | Estado |
|---|---|---|
| W1 invierno | `cf-w-1-invierno.jpg` (693 KB) | ✅ generado |
| W2 noche | `cf-w-2-noche.jpg` (647 KB) | ✅ generado |
| W3 madera | `cf-w-3-madera.jpg` (694 KB) | ✅ generado |
| W4 aérea | `cf-w-4-aerea.jpg` (839 KB) | ✅ generado (revisar deriva) |
| W5 multi-ref | `cf-w-5-multiref.jpg` (545 KB) | ✅ generado |
| W6 seed 42 ×2 | `cf-w-6a-seed42.jpg` / `cf-w-6b-seed42.jpg` | Bytes distintos → comparar a ojo |
| W7 guidance 8 / 1.5 | `cf-w-7-guid-8.jpg` / `cf-w-7-guid-1_5.jpg` | ✅ generados (vano este) |

## Serie casa BA entre medianeras (base `cf-casa-base.jpg`, 792 KB)

Base txt2img: casa hormigón + medianeros vecinos + calle angosta. Edits misma imagen:

| ID | Archivo | Cambio |
|---|---|---|
| H1 noche | `cf-casa-h-1-noche.jpg` | Luz cálida interior, cielo azul noche |
| H2 lluvia | `cf-casa-h-2-lluvia.jpg` | Mañana nublada, asfalto mojado |
| H3 aérea | `cf-casa-h-3-aerea.jpg` | Vista alta: techo, calle, medianeros |
| H4 vano | `cf-casa-h-4-vano.jpg` | Portón vidriado planta baja, resto idéntico |

Hallazgo seed: con seed 42 fija, dos corridas dan bytes distintos — en destilados la seed no fija la imagen; la consistencia se logra con imagen de referencia, no con seed.

## SK croquis → fotorrealista (proxy bordes)

Proxy `cf-croquis-proxy-512.jpg` (bordes extraídos de la casa) → `cf-croquis-a-render-01.jpg` (696 KB) con instrucción sketch→render. Proxy válido para calibrar; la prueba real requiere croquis a mano del usuario (línea suelta ≠ bordes perfectos).

## Veredicto 2026-11-13 — qué flujos Comfy se justifican en arquitectura

La batería W demuestra que cambio de estación/hora/material global **ya no justifica ningún flujo Comfy**: klein-4b en la nube lo resuelve sin Canny, sin pod, por centavos (equivale al min 17:05 del video Ep39 de FLUX 3 Klein: seasons = tarea resuelta por el modelo).

**Sí justifican Comfy** (lo que el cloud no da por no-determinista): fidelidad geométrica cuando el plano manda (klein inventa: inodoro wall-hung, deriva en aérea W4, seed 42 no reproducible); identidad repetible del proyecto (mismo checkpoint + seed + LoRA = mismo edificio en 10 vistas); LoRA propio del estudio; privacidad de concurso; upscale a print A1; inpaint/outpaint con máscara dibujada.

**No justifican Comfy**: exploración, estación, hora, mood, material global, croquis→render → nube (agente).

**Pod con klein, ¿para qué?** Solo para el grafo combinado: klein-local + ControlNet + LoRA (potencia generativa con control geométrico, sin cuota, en batch). Replicar W1/W2 en pod = pagar GPU por lo que la nube regala.

**Regla**: exploración/estación/hora/mood/croquis → nube; geometría no negociable, identidad, print, privacidad → Comfy.
