# Sesión 2026-09-30 — Moodboard fachada hormigón+madera Hamad (WF_v5)

## Qué se hizo

1. **ComfyUI background:** logramos lanzamiento detach con `comfy launch --background` + flags custom RX570 (`--directml 0 --force-fp16 --cache-ram 2 8`). Creamos `P:\00-repos\ComfyUI\corre_comfyui_background.bat` (mismos PARAMS que `corre_comfyui.bat`) y acceso `C:\Users\Solch16\Desktop\ComfyUI RX570 (Background).lnk` (doble click, cierra terminal).
2. **Análisis WF existentes:** `n_06-moodboard/WF/{WF_v1_local_Canny_IPA, WF_v2_moodboard_batch, WF_v3_escalera_piedra, WF_v4_parque_pajareras}` — 3 entran → 2 salen es `WF_v2_batch` (`n_06-moodboard-WF_v2_batch.json`: 3 LoadImage + ImageScale 512 → M1 ImageBatch denoise 0.6 + M2 Canny 0.12/0.39 denoise 0.75). Sticky notes: server 0 nodos Note → alternativa Groups nativos (colores) sin instalar pack.
3. **Corrida WF_v2_batch con 3 Hamad:** inputs `01/02/03hamad.JPG` (hormigón visto + madera oscura, volumen elevado, puente, bosque pinos) → outputs `n_06-B-02_00003/00004` y `n_06-B-03_00002` (376s, `351ff3db`) pero deriva a villa toscana — prompt `tuscan/cypress/travertine` + `ImageBatch` híbrido + `denoise 0.6/0.75` + `512x512 crop` recorta puente.
4. **WF_v5_fachada_hormigon_madera armado:** corrige WF_v2 — prompts Hamad (`exposed concrete + dark oiled wood slats / cantilevered wood volume / brutalist concrete prism`), 1 ref=1 rama sin batch, `768x512/512x768` lanczos, `Canny 0.31/0.59 CN 0.90 denoise 0.40` seeds 42/77/123 → `n_06-C-0*`. Estructura según `reglas-workflows-comfy.md` (00-README,01-index,02-WF-log,03-nodos,04-backlog,salidas/,PLANS/,SPECS/).
5. **Fallo OOM:** `ec4c64a7` (27 nodos, 3 ramas `768x512`) → `VAEDecode 92 — Could not allocate tensor 201MB` (507s, VRAM RX570). Registrado en `02-WF-log-WFv5` y `03-log-mvp_04.md v1.0.2`.
6. **WF_v5.1 fix y corridas secuenciales:** vuelta a `R1 512x512` + 3 workflows separados `workflow_fachada_hormigon_madera_C0{1,2,3}.json` (mismos prompts Hamad, `Canny 0.31/0.59 CN 0.90 denoise 0.40`). Encolados `c3f427ce` (C-01 107.6s success), `fadffd60` (C-02 102.6s success), `2859cae3` (C-03 88.6s success) → `P:\00-repos\ComfyUI\output\n_06-C-0*.png` copiados a `WF_v5/salidas/n_06-C-01/02/03.png` (349/421/486KB). C-01 retiene puente/madera/hormigón (validado visual).
7. **Vault logs actualizados:** `03-log-mvp_04.md` v1.0.2 (tabla eventos + iteración WF_v2→WF_v5), `WF_v5/{00-README,01-index,02-WF-log-WFv5,03-nodos-WFv5,04-backlog}` + librería Comfy `n_06-moodboard-WF_v5*.json` + `n_06-moodboard-WF_v5_C0*.json` en ambos workspaces.

## Archivos modificados

- `P:\00-repos\ComfyUI\corre_comfyui_background.bat` (nuevo)
- `C:\Users\Solch16\Desktop\ComfyUI RX570 (Background).lnk` (nuevo)
- `proyectos/MVP_04-comfyui-arquitectura/n_06-moodboard/WF/WF_v5_fachada_hormigon_madera/` (workflow_fachada_hormigon_madera.json, workflow_fachada_hormigon_madera_C0{1,2,3}.json, 00-README.md, 01-index.md, 02-WF-log-WFv5_fachada_hormigon_madera.md, 03-nodos-WFv5.md, 04-backlog.md, salidas/n_06-C-0{1,2,3}.png)
- `P:\00-repos\ComfyUI\output\n_06-C-01_00002_.png`, `n_06-C-02_00002_.png`, `n_06-C-03_00001_.png`
- `C:\Users\Solch16\ComfyUI\user\default\workflows\n_06-moodboard-WF_v5*.json` + `P:\00-repos\ComfyUI\user\default\workflows\` (copias)
- `proyectos/MVP_04-comfyui-arquitectura/03-log-mvp_04.md` (v1.0.0 → v1.0.2)
- `P:\00-repos\ComfyUI\wf_v5_ids.txt` (ids temporales)

## Análisis cerebro digital (Karpathy)

- Topics candidatos: `wiki/glosario/conceptos/moodboard` (fidelidad vs prompt tuscan), `wiki/glosario/software/comfyui` (R1 512 + ControlNet 0.90), `wiki/glosario/conceptos/fachada-hormigon-madera` (Hamad refs). Pendiente curaduría @vaultworm-arq con `s`.
- Entidades: Hamad house (3 refs 01/02/03), ArchitectureRealmix v1.1, ControlNet canny `control_v11p_sd15_canny.safetensors`, RX570 8GB privateuseone DirectML, ComfyUI 0.28.0, prompts Hamad hormigón visto/madera oscura/puente/voladizo/bosque pinos, denoise 0.40.
- Hechos/decisiones: ImageBatch híbrido degrada fidelidad Hamad → 1:1 rama; 768x512 3 ramas OOM en 8GB → R1 512x512 secuencial (107/102/88s) estable; Canny 0.31/0.59 + CN 0.90 supera deriva tuscan; `comfy launch --background --` detach funciona con flags custom.
- Infra efímera: prompt_ids `351ff3db` (WF_v2 376s), `ec4c64a7` (WF_v5 OOM 507s), `c3f427ce/fadffd60/2859cae3` (WF_v5.1 success); VRAM 1GB libre pre-run.
