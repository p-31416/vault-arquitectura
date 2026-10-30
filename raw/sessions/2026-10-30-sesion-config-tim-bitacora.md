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

## Archivos (nuevos con `+`, modificados con `~`)

+ `proyectos/MVP_04-comfyui-arquitectura/prompt-coach/02-prompt-coach-extendido.md`
+ `proyectos/MVP_04-comfyui-arquitectura/prompt-coach/03-flux2-prompt-refiner.md`
+ `proyectos/MVP_04-comfyui-arquitectura/prompt-coach/04-bitacora-corridas.md`
~ `.opencode/agents/tim.md`
~ `proyectos/MVP_04-comfyui-arquitectura/setup_comfy_mcp.md`

## Pendiente próxima sesión

1. **Playbook `wiki/glosario/interno/pbooks/pbk-comfy-agent.md`** (requiere s): manual de invocación + recetario por las 6 tipologías, con constantes de fotografia (Baan · IQ4 · 6 hex · stock), enlazado a la bitácora `04-bitacora-corridas.md`.
2. Registrar `@tim` en `pbk-agentes-vaultarq.md` (tabla + comparativa).
3. Fix mismo paquete en `pbk-troubleshooting-reconexion.md:139` (wiki → requiere s).
4. Primera corrida real de `@tim` (pabellón en Barcelona, 4 modelos) para estrenar checklist y bitácora.

## Análisis cerebro-digital

**Topics:** configuracion-agentes-opencode · permisos-por-ruta · patron-permisos-ultimo-match · comfy-mcp-tools · bitacora-corridas · checkpoints-locales · checklist-pre-corrida · delegacion-subagentes · prompt-coach-miro · paquete-npm-404
**Entidades:** `@tim` (`.opencode/agents/tim.md`) · `comfyui-mcp` (npm artokun, `@comfyorg/comfyui-mcp` 404) · `architecturerealmix_v11` · `Juggernaut-XL_v9_RunDiffusionPhoto_v2` · `sd-v1-5-inpainting-fp16` · `04-bitacora-corridas.md` · `prompt-coach/03-flux2-prompt-refiner.md` · docs.bfl.ai (guía `prompting_guide_flux2_klein` 404 → vigentes `prompting_guide_flux2` · `flux_2/flux2_overview`)
**Hechos:** la config de opencode carga al inicio y ahí quedan definitivos los permisos por agente (el prompt acompaña, no sustituye); a Tim queda definida una plancha local RX 570 con 3 checkpoints fijos, y lo grande (FLUX/video) sale como prompt + flujo listo con el aviso `requiere RunPod/Cloud`; el MCP de ComfyUI expone tools que NO se llaman `run_workflow` (el nombre del doc de setup era incorrecto); del curso quedó integrado el patrón "¿modelo o inpaint?" como primera pregunta y las constantes BFL (Baan · IQ4 · 6 hex · stock · referente real).
