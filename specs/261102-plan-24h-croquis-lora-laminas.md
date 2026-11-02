---
tipo: plan
proyecto: Proyecto Pi
cliente: Estudio (línea propia)
fecha_creacion: 2026-11-01
ultima_actualizacion: 2026-11-01
estado: borrador
tags: [plan-24h, concurso, gaudi-nexus, croquis, sagrada-familia, lora, flux, runpod, comfyui, telegram, n8n, openrouter, laminas]
idioma: es
---

# Plan 24 h — croquis en la plaza real → LoRA de estilo → láminas

> Día de ejecución: **lunes 2 de noviembre de 2026**. Arranca 08:00, cierra 24:00.
>
> Origen: decisión del 01/11 de encarar el concurso con tres piezas encadenadas — un croquis insertado en la plaza real de la Sagrada Família, un LoRA de estilo propio y la serie de láminas. Insumo externo: [[raw/research/2026-11-01-modelos-imagen-n8n-telegram|research modelos de imagen + n8n + Telegram]] (24 motores, precios y licencias al 2026-11-01).
>
> Relacionado: [[specs/261019-plan-concurso-gaudi-nexus-ia|plan concurso Gaudí Nexus]] · [[proyectos/concurso-gaudi-nexus/reinterpretacion-programa-fractal|programa fractal]] · [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|modelos recomendados v1.4.0]] · [[raw/sessions/2026-11-01-sesion-ia-generativa-visual|sesión 01/11]].

## 1. Objetivo

Cerrar el día con tres entregables verificables:

1. Un **croquis propio** insertado en una foto real de la plaza, con las torres, el Passeig de Sant Joan y la manzana reconocibles.
2. Un **LoRA de estilo** entrenado y probado sobre esa misma escena.
3. Las **láminas** maquetadas con renders que usan ese LoRA.

Y un canal operativo: **Telegram → agente → modelo**, para pedir variantes desde el teléfono durante todo el día.

## 2. Regla del día

El lugar no lo aporta el modelo — lo aporta la **foto de referencia**. Todos los modelos de la tanda reciben el mismo par: foto panorámica real de la plaza + croquis. Así se compara modelo contra modelo, con el prompt fijo.

Base visual: `activos/proyectos/concurso-gaudi-nexus/earth2rhino3d/ref/sf-plaza-gaudi-panorama.jpg`.

## 3. Materiales de entrada

- [ ] Archivo del LoRA recibido (`.safetensors`) y su metadata leída: `ss_base_model_version` / `modelspec` → confirmar si es Flux.1 (12B) o Flux.2 klein (8B).
- [ ] 2–3 croquis escaneados en alta (planta + volumetría + un detalle).
- [ ] Foto panorámica real de la plaza (referencia fija).
- [ ] Tarjeta y saldo para RunPod (~USD 10).
- [ ] `comfyenv` operativo y ComfyUI local levantado (`http://127.0.0.1:8188`).

## 4. Canales y modelos del día

| Canal | Modelo | Costo unitario | Conocimiento del sitio | Licencia comercial |
|---|---|---|---|---|
| OpenRouter | Nano Banana 2.1 (1K, hasta 14 refs + grounding) | USD 0,0336/img | Alto (referencia + búsqueda de imágenes) | Sí, por API |
| OpenRouter | Seedream 4.5 | USD 0,04/img | Medio | Sí, por API |
| Comfy Cloud | Qwen Image Edit 2509 (preinstalado) | créditos del plan | Medio (edición por referencia) | Sí |
| Comfy Cloud | Nano Banana Pro (Partner Node) | USD 0,134 (1K/2K) · 0,24 (4K) | Alto | Sí, por API |
| RunPod | Flux 8B + LoRA propio | ~USD 0,4–0,7/h (verificar) | Depende de la referencia | Según licencia del modelo base |
| Local (RX 570) | RealVisXL v5.0 / Juggernaut XL | USD 0 | Bajo | Open RAIL++-M / Open RAIL-M |
| Local (RX 570) | SDXL + LoRA SDXL | USD 0 | Bajo | Según licencia del LoRA |
| AI Horde | SDXL (gratis) | USD 0 | Bajo | Verificar por modelo |

Criterio de uso: los gratuitos y locales para **volumen de exploración**; los pagos, solo para las **piezas finales** de lámina.

## 5. Sprints

### Sprint 1 · 08:00–11:00 — Telegram operativo

- [ ] Levantar el túnel público: `cloudflared tunnel --url http://localhost:5678` → URL HTTPS (el webhook de Telegram la exige).
- [ ] n8n: Telegram Trigger → agente que redacta el prompt → HTTP Request a OpenRouter → imagen devuelta al chat.
- [ ] Primer modelo conectado: **Nano Banana 2.1**.
- [ ] Prueba de extremo a extremo desde el teléfono.

**Gate:** si el túnel público se traba, el resto del plan corre igual y el bot se cierra al final del día.

### Sprint 2 · 11:00–14:00 — Croquis dentro de la plaza real

Misma entrada para los tres candidatos:

- [ ] **Nano Banana 2.1** (OpenRouter) — mejor lectura del contexto real.
- [ ] **Qwen Image Edit 2509** (Comfy Cloud) — edición por referencia.
- [ ] **FLUX.1 Kontext** (RunPod, si el pod está arriba) — control fino de geometría.
- [ ] Comparar y elegir **1 keeper**.

**Criterio de aceptación:** torres, Passeig de Sant Joan y manzana reconocibles; la volumetría la manda el croquis; la escena se mantiene creíble.

### Sprint 3 · 14:00–18:00 — RunPod + Flux 8B

- [ ] Cuenta y saldo en RunPod; pod RTX 4090 / A40 con template ComfyUI.
- [ ] Subir el LoRA a `models/loras` y correrlo con el grafo del Sprint 2.
- [ ] Preparar el dataset de estilo: **15–25 imágenes** con captions (qué cambia entre imágenes se describe, el estilo se mantiene fijo).
- [ ] Definir el trigger word del estilo.

**Plan B si RunPod se traba:** Comfy Cloud plan **Creator** (habilita importar LoRA propio) por un mes.

### Sprint 4 · 18:00–22:00 — Entrenar el LoRA de estilo

- [ ] Lanzar el entrenamiento (ai-toolkit en el pod, rank 16–32, ~1–2 h).
- [ ] Mientras entrena: maquetar las láminas (planta, aéreo, eye-level, detalle) sobre el layout del concurso.
- [ ] Al terminar: 4 renders de prueba del LoRA sobre la escena de la plaza.

### Cierre · 22:00–24:00

- [ ] Veredicto escrito: modelo keeper, LoRA v1 y estado de las láminas.
- [ ] Actualizar `02-WF-log` del flujo correspondiente y [[proyectos/concurso-gaudi-nexus/workflows/00-matriz-pruebas-concurso|matriz de pruebas]].
- [ ] Log de sesión en `raw/sessions/`.

## 6. Presupuesto del día

| Rubro | Estimado |
|---|---|
| OpenRouter (exploración + finales) | USD 3–5 |
| RunPod (pod 4–5 h) | USD 8–15 |
| Comfy Cloud (solo si se activa plan Creator) | a confirmar |
| **Total** | **USD 15–25** |

## 7. Riesgos

| Riesgo | Mitigación |
|---|---|
| RunPod es la única pieza nueva de infraestructura | Sprint 2 entrega valor aunque el pod se caiga; el LoRA se entrena otro día |
| El LoRA es Flux 8B y los grafos son Flux.1 | Leer la base antes de encolar; el grafo se arma para la base real |
| Logo/marca de la Sagrada Família en la foto | Usar referencia de calle, encuadre propio |
| Tiers gratuitos sin licencia comercial | Solo exploración; láminas finales con modelos pagos o Open RAIL |
| Falta de dataset de estilo suficiente | 15 imágenes con captions alcanzan para un v1; se amplía en v2 |

## 8. Criterio de éxito del día

El día se considera cerrado si existe: (a) un croquis en la plaza con veredicto de modelo, (b) un LoRA de estilo entrenado con 4 renders de prueba, y (c) el bot de Telegram devolviendo imágenes. Con dos de las tres, el plan avanza igual.

## 9. Pendiente de decisión

- Base real del LoRA recibido (Flux.1 vs Flux.2 klein) y su licencia.
- Si el LoRA viene entrenado (solo aplicar) o si el objetivo es entrenar uno nuevo desde cero.
