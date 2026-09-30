---
tipo: log
fase: concepto
fecha_creacion: 2026-09-30
ultima_actualizacion: 2026-09-30
tags: [mvp_04, n_06, log, fachada, hamad]
---

# 02-WF-log — WF_v5_fachada_hormigon_madera — Más nuevo → más arriba

## 2026-09-30 01:05 — WF_v5 falló OOM `ec4c64a7` → WF_v5.1 secuencial

- **Fallo:** `ec4c64a7-066e-4264-8b54-d09779457d6d` (27 nodos, 3 ramas paralelas `768x512/512x768`) → `VAEDecode 92 — RuntimeError: Could not allocate tensor 201MB` (507s, `privateuseone` RX570 8GB). 3× `768x512` + 3 `VAEDecode` simultáneos saturan VRAM (--directml 0 sin --lowvram).
- **Fix WF_v5.1:** vuelve a `R1 512x512 lanczos center` (seguro 8GB) y 1 rama por corrida: 3 workflows separados `workflow_fachada_hormigon_madera_C0{1,2,3}.json` con mismos prompts Hamad (`exposed concrete + dark oiled wood slats` / `cantilevered wood volume` / `brutalist concrete prism`), `Canny 0.31/0.59 CN 0.90 denoise 0.40` seeds 42/77/123 → `n_06-C-01/02/03` secuenciales. Alternativa `768x512` queda para `--lowvram` futuro.
- **Encolados:** `ed6c2b8a` (C-01), `a3f7d9c1` (C-02), `b81e4f2a` (C-03) — actualizados abajo al terminar.
- **Estado:** re-encolado secuencial 01:05, monitoreo queue.

## 2026-09-30 — WF_v5 armado (corrección post WF_v2_batch 351ff3db)

- **Origen fallo:** `WF_v2_batch` `n_06-B-02_00003/00004` y `n_06-B-03_00002` (376s, success) derivaron a villa suburbana vidrio/piedra y muro piedra vs inputs Hamad hormigón visto + madera oscura, volumen elevado, puente, bosque pinos. Causa: prompt `tuscan/cypress/travertine` + `ImageBatch` híbrido + `denoise 0.6/0.75` + `ImageScale 512x512` recorta voladizo.
- **Workflow nuevo:** `workflow_fachada_hormigon_madera.json` (27 nodos) — 1 ref = 1 rama, sin batch. `ImageScale 768x512 (01,03) / 512x768 (02)` lanczos center; `Canny 0.31/0.59`, `ControlNet canny 0.90/0.0-0.85`, `VAEEncode → KSampler 30 steps euler_ancestral/karras cfg7 denoise 0.40 seeds 42/77/123` → `n_06-C-01/02/03`. Prompts alineados Hamad (ver `03-nodos-WFv5.md`), negativo bloquea tuscan.
- **Validación:** pendiente `comfyui_create_workflow validate` + `node_info`.
- **Próximo:** encolar vía MCP → `P:\00-repos\ComfyUI\output\n_06-C-0*.png` → copiar a `salidas/` y comparar fidelidad vs `01/02/03hamad.JPG`. Lograr C-01 puente, C-02 voladizo, C-03 prisma horizontal.

## 2026-09-30 — Contexto heredado WF_v2_batch

- Ver `WF_v2_moodboard_batch/02-WF-log-WFv2_moodboard_batch.md` y `WF_v1_local_Canny_IPA/02-WF-log-WFv1_local_Canny_IPA.md` para corridas base. WF_v5 reutiliza R1 ImageScale y stack Canny+CN validado en WF_v1 (seed 42, 134s, success).
