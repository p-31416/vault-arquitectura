# Sesión 2026-09-10 — Moodboard L1–L4 local DirectML (n_06)

## Qué se hizo

1. Propuesta inicial L1 Variation + L2 Alteration desde `Advertising1 - Moodboard Creation.json` (Recraft + GPT-image con costo → réplica local sin costo): R1 ImageScale 512, Canny, ControlNet canny, Realmimix, fallback VAEEncode ante IPAdapter ausente.
2. Spec creado: `specs/260909-moodboard-vault-visual-local.md` (variantes, flujo MCP, ingesta 3 destinos, Dataview/Canvas/Excalidraw, gates HITL).
3. Comfy caído (ECONNREFUSED + `ModuleNotFoundError: sqlalchemy`): el usuario instaló la dependencia y arrancó `corre_comfyui.bat` (venv `comfyenv`). Health OK: ComfyUI 0.28.0, torch 2.4.1+cpu, DirectML, Realmimix + Juggernaut, CN canny/depth/scribble, 0 errores.
4. WF v1 (`WF_v1_local_Canny_IPA`): L1 Canny 0.31/0.59 + CN 0.85, seed 42, input sustituido a `croquis001.jpg` → `n_06-B-01.png` (134s, interior rústico madera).
5. WF v2 (`WF_v2_moodboard_batch`): réplica del referente — ImageBatch 2 refs + variation denoise 0.6 (B-02a villa travertino con pérgola, B-02b casa patio nocturna) + alteration IMG_2305 Canny 0.12/0.39 denoise 0.75 (B-03 atrio vidriado). 221s.
6. WF v3 (`WF_v3_escalera_piedra`): desde `croquis2.jpg` con prompt del usuario (escalera piedra derecha, comedor izquierda, mesa primer plano, barra fondo) → `n_06-B-04.png` (88s, comedor doble altura).
7. WF v4 (`WF_v4_parque_pajareras`): txt2img parque (sin refs en input/) → `n_06-B-05.png` (77s). Hierro ornamental flojo; iteración pendiente (prompt victorian aviary seed 401 o alteration con fotos reales).
8. Los 4 flujos guardados en vault (`workflow_*.json` + 00-README + 02-WF-log + 03/04 donde aplica) y en librería Comfy (`n_06-moodboard-WF_v*.json`, abren en canvas).
9. IPAdapter ausente en el server (`node_info` 0 resultados) → rige fallback VAEEncode en L2.

## Archivos modificados

- `specs/260909-moodboard-vault-visual-local.md` (nuevo)
- `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/WF/WF_v1_local_Canny_IPA/` (workflow_moodboard_local.json, 00-README, 01-index, 02-WF-log, 03-nodos, 04-backlog, salidas/n_06-B-01.png)
- `.../WF_v2_moodboard_batch/` (workflow_moodboard_batch.json, 00-README, 02-WF-log, salidas n_06-B-02a/b.png, n_06-B-03.png)
- `.../WF_v3_escalera_piedra/` (workflow_escalera_piedra.json, 00-README, 02-WF-log, salidas/n_06-B-04.png)
- `.../WF_v4_parque_pajareras/` (00-README, 02-WF-log, salidas/n_06-B-05.png; workflow en librería Comfy)
- ComfyUI user library: `n_06-moodboard-WF_v1_local_Canny_IPA.json`, `n_06-moodboard-WF_v2_batch.json`, `n_06-moodboard-WF_v3_escalera_piedra.json`, `n_06-moodboard-WF_v4_parque_pajareras.json`

## Análisis cerebro digital (Karpathy)

- Topics candidatos: `wiki/glosario/conceptos/moodboard` (pendiente, vía @vaultworm-arq con `s curaduria`); validación MCP `validate` como gate previo a `enqueue`; patrón fallback ante custom node ausente (IPAdapter → VAEEncode).
- Entidades: ComfyUI 0.28.0 DirectML (RX 570), ArchitectureRealmix v1.1, ControlNet canny/depth/scribble, `croquis001/croquis2/croquis3/IMG_2305/estadio_futbol` (inputs), ComfyUI_IPAdapter_plus (pendiente instalar).
- Hechos/decisiones: DirectML SD1.5 30 steps ≈ 80–135s (batch x2 ≈ 221s); Canny 0.31/0.59 + CN 0.85 sostiene layout de croquis; denoise 0.6–0.75 re-estiliza manteniendo composición; `sqlalchemy` requerido por `main.py` (seeder) en esta versión; `mood-product-ref.png` no existía → sustituir por inputs reales tras `validate value_not_in_list`; hierro forjado ornamental necesita prompt reforzado o ref real.
- Infra efímera: prompt_ids de la sesión (4908ac63, ceac85df, e90e858a, 39c9886a); VRAM fantasma 1GB (patch WMI conocido).
