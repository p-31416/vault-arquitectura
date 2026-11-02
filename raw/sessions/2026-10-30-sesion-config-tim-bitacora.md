# 2026-10-30 — Sesión tim: configuración y bitácora del agente @tim

## Qué se hizo

- **Tarde/archivo prompt-coach** (sesión previa, mismos MVP): archivados verbatim los prompts del curso AI x Gaudi de Miro en `proyectos/MVP_04-comfyui-arquitectura/prompt-coach/`: `02-prompt-coach-extendido.md` (6.064 chars, truncado por el export en "What to deliver (Branch A)", falta Branch B inpaint) y `03-flux2-prompt-refiner.md` (6.859 chars, con las tablas "JSON Template" y "Lens Selection Logic" vacías en el export; el estado del export queda marcado en cada archivo).
- **Corrección de `setup_comfy_mcp.md`**: paquete `@comfyorg/comfyui-mcp` (404 en npm) → `comfyui-mcp` (artokun, requiere Node ≥ 22); tools reales (`comfyui_execute_workflow`, `comfyui_get_history`, `comfyui_list_local_models`, `comfyui_validate_workflow`, `comfyui_get_system_stats`, etc.) en el Paso 2 y el Principio AMV; la línea 139 de `wiki/glosario/interno/pbooks/pbk-troubleshooting-reconexion.md` tiene el mismo error del paquete, pendiente de s.
- **Entrevista definición de `@tim`**: SOL definió la config pregunta a pregunta (9 respuestas):
  1. uso del futuro playbook → los dos (invocación + recetario), enlazado a bitácora de corridas;
  2. bitácora → log por WF + índice central (`prompt-coach/04-bitacora-corridas.md`);
  3. tipologías → todas las seis (fachada · interior · masterplan · detalle · contexto urbano · video);
  4. plataforma → solo local RX 570, con aviso `requiere RunPod/Cloud` si el modelo no entra;
  5. checkpoints → fijos por rol (architecturerealmix_v11 · Juggernaut-XL_v9 · sd-v1-5-inpainting-fp16);
  6. pre-corrida → checklist de 4 puntos (archivos en disco · resolución nativa · dialecto · una sola variable);
  7. modo → `subagent` (sin cambios); temperatura → 0.4 (sin cambios);
  8. delegación → `task: allow`, delega a `@sherlock` (referencias/videos/fuentes) y `explore` (rastrear WF), para traer, no para decidir;
  9. permisos → `edit` allow con **`wiki/**` · `activos/**` · `.git/**` en deny**; MCP `comfyui_*` + `rhino_*` allow, resto de MCP en deny (`leantime_*`, `n8n_*`, `fathom_*`, `autocad_*`, `autodesk_*`); ejecuta con `s` (usa `comfyui_execute_workflow` + `comfyui_get_history` para registrar).
- **Editado `.opencode/agents/tim.md`**: frontmatter reescrito con permisos por ruta/patrón (sintaxis schema opencode: dentro de objeto, el último match gana), sección nueva "Delegación", sección nueva "Plancha local (RX 570)" con los 3 checkpoints, sección nueva "Checklist antes del `s`", paso 6 extendido (fila al índice cuando la corrida es repetible) y referencias internas a la bitácora.
- **Creamos `proyectos/MVP_04-comfyui-arquitectura/prompt-coach/04-bitacora-corridas.md`**: índice central de corridas (tipo log, "Más nuevo → más arriba"), formato de fila, sin corridas todavía.
- **Aviso**: los permisos nuevos del frontmatter aplican al reiniciar opencode (la config carga al inicio).

## Minería del tablero Miro (continuación de la misma sesión, con `s` por fase)

- **Inventario**: 219 items, 14 con texto sustantivo (500–14.072 chars). Fases aprobadas por fase:
- **Fase A** — `02-prompt-coach-extendido.md` completado: continuación del Branch A (6.002 chars: qué entregar, settings sugeridos, variaciones) + Branch B entero (Region-Only Inpaint: mask checks, estructura de 6 pasos con BOUNDARY STITCH, skeleton, failure triage de 9 síntomas, nota de links). Corte restante marcado: 3ª regla de "Hard-won rules" (`- **M`) + párrafo de node settings para inpaint latente. README actualizado.
- **Fase B** — skill nueva `.opencode/skills/seedance-director/` (del curso): `SKILL.md` en ES (contrato JSON EN+ZH, router de arquetipos, reglas del motor, antislop) + `references/fuente-verbatim-01.md` con el sticky original (14.072 chars, verbatim). Cableada en `tim.md` (invocación `@tim seedance <escena>` + referencia) y en [[wiki/glosario/interno/pbooks/pbk-comfy-agent|pbk-comfy-agent]] §6.
- **Fase C** — VARIANTE B de Gaudí ya estaba archivada (2026-10-20, verificado). Faltaban las dos de CREATIVITY 9/10 → `n_05-rhino-mcp/WF-rhino-to-image/`: `prompt-rhino-to-image-creativity-json-short.md` (3.713, compacta) + `prompt-rhino-to-image-creativity-json-full.md` (6.000, con template JSON y Rules & Constants), ambas con análisis y verbatim, registradas en el README del WF. Son el modo convergente: massing + foto estética → JSON único, re-skin de la Image 2 sobre la Image 1.
- **Fase D** — `raw/prompts/2026-10-30-img2-3d-modulo5.md`: los 3 prompts IMG-2-3D del módulo 5 (maquette hormigón 794 · hiperreal→viewport Rhino 791 · holdable object 3.049), verbatim con análisis.
- **Verbatim por PowerShell** (append de los data.title del JSON): evita retipeado y mojibake; los cuerpos quedan como línea larga tal como llegó el export.

## Aporte a la matriz de pruebas (cierre de sesión)

- SOL pidió pruebas con un modelo SDXL local, uno por uno, sobre los flujos documentados del concurso; y decidió el formato de doc: **un único doc por WF** (sección NT arriba / TK abajo) + JSON dual (API + `_ui`) — evaluados los 2 archivos y descartados por multiplicación.
- Escribido `proyectos/concurso-gaudi-nexus/workflows/00-aporte-matriz-pruebas.md`: decisiones cerradas (estructura, naming, carpetas), receta SDXL validada (WF-04 2.0.0: Juggernaut · dpmpp_2m/karras · 35 steps · cfg 4 · 1216×832 · 651 s), rangos de parámetros con evidencia literal, protocolo de revisión manual y mapeo flujos→WF. Otro agente construye la matriz concreta sobre esta base.
- Estado del re-detición: ya existe `WF-04-serie-txt2img` 2.0.0 validado (no se duplican: se extiende); `comfy-prompting` skill confirmada como creada el 29/10; pendientes: WF-02/03/07 del concurso + descarga SSD-1B + corrida emplazamiento E1.

## LoRA de estilo del concurso (@tim, con `s` de SOL)

- Delegación real a `@tim` (subagente) para investigar el entrenamiento de un LoRA de estilo visual propio del concurso, publicable ("que sea nuestro"). Informe completo en el mensaje + documento en el vault.
- Hallazgos clave: klein **4B** es Apache 2.0 (publicable, comercial); klein **9B** es Non-Commercial (un LoRA sobre 9B hereda la restricción) → recomendación LoRA de estilo sobre FLUX.2 klein-base-4B, entrenado en RunPod con ai-toolkit ($0,50–0,70/corrida en 3090 Community; experimento total $3–5), publicado en Civitai + HF (Apache 2.0), trigger propuesto `gaudinexusstyle`, receta rank 16/LR 1e-4/2000 steps (ancla: LoRA del curso, rank 16/F32/176 tensores).
- Dataset ya existe: 80 renders con metadata en `INDICE-RENDERS.md` (más moodboard + capturas Rhino) → objetivo 40 curadas.
- Local RX 570: curación/captioning/validación de inferencia SD1.5/SDXL; el entrenamiento solo en CUDA (ai-toolkit y bitsandbytes 8-bit son CUDA-only, DirectML queda afuera).
- Quedan pendientes de decisión de SOL: trigger, klein 4B vs 9B como fuente del dataset, presupuesto RunPod, y las 4 preguntas legales para @sherlock (outputs del 9B como training data, fotos de Gaudí del moodboard, premio del concurso como uso comercial, precedentes de estudios).

## Archivos (nuevos con `+`, modificados con `~`)

+ `proyectos/MVP_04-comfyui-arquitectura/prompt-coach/02-prompt-coach-extendido.md`
+ `proyectos/MVP_04-comfyui-arquitectura/prompt-coach/03-flux2-prompt-refiner.md`
+ `proyectos/MVP_04-comfyui-arquitectura/prompt-coach/04-bitacora-corridas.md`
+ `wiki/glosario/interno/pbooks/pbk-comfy-agent.md`
~ `.opencode/agents/tim.md`
~ `proyectos/MVP_04-comfyui-arquitectura/setup_comfy_mcp.md`
~ `wiki/glosario/interno/pbooks/pbk-agentes-vaultarq.md` (tabla + sección tim + comparativa)
~ `wiki/glosario/interno/pbooks/00-index.md` (entrada ComfyUI, dedupe pbk-comfyui)
~ `wiki/glosario/software/opencode.md` (fila tim + nota permisos por patrón)
~ `wiki/glosario/interno/pbooks/pbk-troubleshooting-reconexion.md` (paquete fix :139)
+ `.opencode/skills/seedance-director/SKILL.md` + `references/fuente-verbatim-01.md`
+ `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-creativity-json-short.md`
+ `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/prompt-rhino-to-image-creativity-json-full.md`
+ `raw/prompts/2026-10-30-img2-3d-modulo5.md`
+ `proyectos/concurso-gaudi-nexus/lora-estudio-plan.md` (informe LoRA como documento)
+ `proyectos/concurso-gaudi-nexus/workflows/00-aporte-matriz-pruebas.md` (convenciones + receta SDXL para la matriz)
~ `.opencode/agents/tim.md` (invocación seedance + referencia a la skill)
~ `wiki/glosario/interno/pbooks/pbk-comfy-agent.md` (§6 video: skill seedance-director)
~ `proyectos/MVP_04-comfyui-arquitectura/prompt-coach/02-prompt-coach-extendido.md` + `00-README.md` (Branch B completo)
~ `proyectos/MVP_04-comfyui-arquitectura/n_05-rhino-mcp/WF-rhino-to-image/00-README.md` (tabla de prompts +1)

## Pendiente próxima sesión

1. Decisión LoRA de SOL: trigger (`gaudinexusstyle`) · dataset sobre klein 4B (limpio) o 9B (calidad, con verificación de sherlock) · ok del presupuesto RunPod $3–5 → después `¿Avanzo?` E1 (curar 40 → captions → sola corrida RunPod → validar checkpoints).
2. **Matriz de pruebas**: otro agente la arma sobre el aporte (`workflows/00-aporte-matriz-pruebas.md`); cuando esté, corridas uno por uno con revisión manual de SOL (WF-02 primero, luego WF-03, WF-07; SSD-1B para el Union).
3. Primera corrida real de `@tim` (pabellón en Barcelona, 4 modelos) para estrenar checklist y bitácora — pedir `comfyui_get_system_stats` y si ComfyUI está levantado.
4. Minería Miro que sigue: `nano-banana` (2.512 chars, referencia), secciones IMPORTABLE IN COMFY (14), MODULE 2/3/7 (workflows por módulo), RELEVANT WEBSITES / MODELS LINKS / LoRA LINKS (fuentes), UPSCALING 1–4 y MOOD APPLIER APP (53 items).
5. Probar la skill `seedance-director` en una corrida (le reiniciar opencode: nueva skill + permisos).
6. Mandar a @sherlock las 4 preguntas legales del LoRA (`lora-estudio-plan.md` §6).

## Análisis cerebro-digital

**Topics:** configuracion-agentes-opencode · permisos-por-ruta · patron-permisos-ultimo-match · comfy-mcp-tools · bitacora-corridas · checkpoints-locales · checklist-pre-corrida · delegacion-subagentes · prompt-coach-miro · paquete-npm-404
**Entidades:** `@tim` (`.opencode/agents/tim.md`) · `comfyui-mcp` (npm artokun, `@comfyorg/comfyui-mcp` 404) · `architecturerealmix_v11` · `Juggernaut-XL_v9_RunDiffusionPhoto_v2` · `sd-v1-5-inpainting-fp16` · `04-bitacora-corridas.md` · `prompt-coach/03-flux2-prompt-refiner.md` · docs.bfl.ai (guía `prompting_guide_flux2_klein` 404 → vigentes `prompting_guide_flux2` · `flux_2/flux2_overview`)
**Hechos:** la config de opencode carga al inicio y ahí quedan definitivos los permisos por agente (el prompt acompaña, no sustituye); a Tim queda definida una plancha local RX 570 con 3 checkpoints fijos, y lo grande (FLUX/video) sale como prompt + flujo listo con el aviso `requiere RunPod/Cloud`; el MCP de ComfyUI expone tools que NO se llaman `run_workflow` (el nombre del doc de setup era incorrecto); del curso quedó integrado el patrón "¿modelo o inpaint?" como primera pregunta y las constantes BFL (Baan · IQ4 · 6 hex · stock · referente real).
