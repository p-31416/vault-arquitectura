---
tipo: research
fecha_creacion: 2026-11-03
ultima_actualizacion: 2026-11-03
tags: [research, sherlock, comfyui, custom-nodes, registry, manager]
idioma: es
---

# 2026-11-03 — Crear y reusar custom nodes de ComfyUI (líneas A+B)

> Fecha|Fuentes N|Confianza
> 2026-11-03|12 verificadas 200|Alta (docs.comfy.org oficial + GitHub oficial + caso testigo) / Media (wiki comunitaria + índices cloud)

## Resumen

Crear un selector de vistas 3D tipo CameraAngleSelector avanza con anatomía mínima aprobada: clase Python con `CATEGORY` + `INPUT_TYPES` + `RETURN_TYPES` + `FUNCTION`, registro en `NODE_CLASS_MAPPINGS` (+ `NODE_DISPLAY_NAME_MAPPINGS` opcional), `__init__.py` con `WEB_DIRECTORY` para el frontend Three.js, `pyproject.toml` con `PublisherId` para publicar, y `requirements.txt` / `install.py` para dependencias. La vía oficial de andamiaje es `comfy node scaffold` dentro de `ComfyUI/custom_nodes`. La publicación avanza en registry.comfy.org con Publisher + API key + versionado semántico + GitHub Action `Comfy-Org/publish-node-action`. La reinstalación avanza por ComfyUI Manager (recomendado), `git clone` o ZIP, con criterios de confianza que premian stars activos, commits recientes, licencia explícita, `pyproject.toml` completo y ejemplo de workflow.

## Ejes

### 1. Anatomía aprobada del nodo (caso testigo CameraAngleSelector)

- El nodo testigo `CameraAngleSelector` concentra la receta mínima: `INPUT_TYPES` con `selected_indices: STRING`, `RETURN_TYPES = ("STRING",)`, `OUTPUT_IS_LIST = (True,)`, `FUNCTION = "execute"`, más `NODE_CLASS_MAPPINGS` y `NODE_DISPLAY_NAME_MAPPINGS` en `__init__.py` con `WEB_DIRECTORY = "web"`.
- `INIT` + `camera_angle_selector.py` + `web/js/camera_angle_extension.js` (Three.js, raycasting, drag-rotate, PostMessage) ilustran la división backend/frontend que la doc oficial pide separar.
- La salida `"<sks> {dirección} {altura} {tamaño}"` (96 combinaciones: 8 direcciones × 4 alturas × 3 tamaños) muestra el patrón de prompt-composer que el estudio reutiliza para Gaudí Nexus (vistas normalizadas hacia Qwen-Image-Edit-2511 + LoRA `fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA`).
- Oportunidad de mejora del testigo: repo sin `LICENSE` formal ("provided as-is"), sin `pyproject.toml` / Registry, sin `requirements.txt` (Three.js por CDN), 9 commits y última actividad 2026-01-10. Ideal como espejo de estudio, no como dependencia productiva sin pin de commit.

### 2. Tutoriales oficiales (camino feliz)

- `walkthrough` oficial guía `comfy node scaffold` → definir `ImageSelector` → registrar → añadir widget combo (`brightest/reddest/...`) → enviar mensaje servidor→cliente (`PromptServer.instance.send_sync`) → extensión JS (`app.registerExtension`) → reiniciar ComfyUI.
- `backend/interface` fija el contrato: `INPUT_TYPES` con `required/optional/hidden`, `RETURN_TYPES` tupla con coma final obligatoria, `RETURN_NAMES`, `CATEGORY` como ruta de menú, `FUNCTION` con tupla de retorno, `OUTPUT_NODE`, `IS_CHANGED` (retorna `NaN` para siempre-cambia, nunca `True`), `VALIDATE_INPUTS`, `INPUT_IS_LIST/OUTPUT_IS_LIST`.
- `install_custom_node` ordena las tres vías con tabla de ventajas: Manager (automatizado + GUI), Git (para no registrados / revisión puntual), ZIP (sin Git, pierde versionado). Incluye regla de seguridad: revisar autor + README + dependencias antes de instalar.

### 3. Publicar en el Registry (puerta de @contenidos → vault)

- Crear Publisher en registry.comfy.org (ID global inmutable tras `@`), generar API key por publisher, `comfy node init` para `pyproject.toml` (`name`, `description`, `version` semántica, `license`, `dependencies`, `[project.urls] Repository`, `[tool.comfy] PublisherId/DisplayName/Icon`), `.comfyignore` para excluir dev-assets, publicar por `comfy node publish` o Action `publish-node-action@main` con secreto `REGISTRY_ACCESS_TOKEN` y trigger en `pyproject.toml`.
- Beneficios que el estudio capitaliza: versionado semántico que protege workflows (el JSON guarda versión del nodo), escaneo de seguridad con sello de verificación, descubrimiento por nodo individual, deprecación controlada.

### 4. Reusar con confianza (línea B)

- Manager nuevo UI (Desktop default) y legacy UI: buscar por pack o por nodo, instalar todo / missing nodes, fijar versión, update con flecha, uninstall, control de `security_level` (`Strict/Standard/Relaxed/weak`) y `network_mode` para `git URL` y `nightly` (requiere `weak` + config.ini).
- `git clone https://github.com/...git` en `custom_nodes` + `pip install -r requirements.txt` en el Python embebido/portable o venv + restart + revisar `import failed` en logs.
- Criterios de confianza que el estudio aplica: stars + forks + watchers vivos, commits < 6 meses, issues con respuesta, `LICENSE` explícita (MIT/Apache-2.0/GPL-3.0/AGPL-3.0), `pyproject.toml` con PublisherId, `README` con instalación + ejemplo + workflow, `requirements.txt` acotado, presencia en Registry/Manager.
- Caso testigo en números: autor Nick Pittas (VFX Supervisor, Nuke Trainer, co-fundador KENT films, moeffect.gr, 40 followers, 44 repos), repo creado 2026-01-10, 124 stars / 10 forks / 2 watchers, categoría `camera`, 1 nodo, instalable por Manager buscando `ComfyUI_CameraAngleSelector` o `NickPittas`, sin costo (gratis, código abierto sin licencia formal), dependencias: ComfyUI + Python 3.8+ + Three.js CDN + LoRA FAL externa para uso pleno.

### 5. Repos ejemplo bien mantenidos para estudiar

- `kijai/ComfyUI-IC-Light` (1.2k stars, 98 commits, Apache-2.0, `pyproject.toml` + `requirements.txt` + `example_workflows/`) como modelo de pack maduro con nodos + workflows.
- `Comfy-Org/ComfyUI-Manager` como referencia de ciclo de vida (`requirements.txt`, `install.py/uninstall.py`, `node_list.json`, `custom-node-list.json` vía PR).
- `comfyorg/comfyui-iclight` (fork oficial mantenido por Comfy-Org, 89 commits) como ejemplo de adopción oficial de un pack comunitario.

## Fuentes APA idioma original + [trad. propia]

1. ComfyUI. (s. f.). *Creating Custom Nodes in ComfyUI* [Crear nodos personalizados en ComfyUI]. docs.comfy.org. https://docs.comfy.org/custom-nodes/walkthrough — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Licencia docs abierta (Mintlify), costo: gratis.
2. ComfyUI. (s. f.). *Code Interface* [Interfaz de código]. docs.comfy.org. https://docs.comfy.org/custom-nodes/backend/interface — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Gratis.
3. ComfyUI. (s. f.). *Publishing Nodes* [Publicar nodos]. docs.comfy.org. https://docs.comfy.org/registry/publishing — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Gratis; publicar requiere cuenta + API key gratuita.
4. ComfyUI. (s. f.). *How to Install Custom Nodes in ComfyUI* [Cómo instalar nodos personalizados]. docs.comfy.org. https://docs.comfy.org/installation/install_custom_node — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Gratis.
5. ComfyUI. (s. f.). *Custom nodes (new UI)* [Nodos personalizados (nueva UI)]. docs.comfy.org. https://docs.comfy.org/manager/pack-management — idioma_original: en [trad. propia — no oficial]. Verificada 200 vía websearch + fetch manager/install el 2026-11-03. Gratis.
6. ComfyUI. (s. f.). *ComfyUI-Manager Installation* [Instalación de ComfyUI-Manager]. docs.comfy.org. https://docs.comfy.org/manager/install — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Gratis.
7. Pittas, N. (2026). *ComfyUI_CameraAngleSelector: Camera Angle LoRA for Qwen Image Edit 2511* [Selector de ángulo de cámara para Qwen Image Edit]. GitHub. https://github.com/NickPittas/ComfyUI_CameraAngleSelector — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Licencia: sin LICENSE formal ("provided as-is"); costo: gratis; dependencias: ComfyUI + Python 3.8+ + Three.js CDN.
8. Pittas, N. (2026). *camera_angle_selector.py* [archivo fuente]. GitHub. https://github.com/NickPittas/ComfyUI_CameraAngleSelector/blob/master/camera_angle_selector.py — idioma_original: en (código). Verificada 200 el 2026-11-03 vía search excerpt. Gratis.
9. Pittas, N. (2026). *__init__.py* [registro del nodo]. GitHub. https://github.com/NickPittas/ComfyUI_CameraAngleSelector/blob/master/__init__.py — idioma_original: en (código). Verificada 200 el 2026-11-03 vía search excerpt. Gratis.
10. kijai. (2024–2026). *ComfyUI-IC-Light: Using IC-Light models in ComfyUI* [Uso de modelos IC-Light en ComfyUI]. GitHub. https://github.com/kijai/ComfyUI-IC-Light — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Licencia: Apache-2.0; costo: gratis.
11. Comfy-Org. (2024–2026). *comfyui-iclight: Using IC-Light models in ComfyUI* [versión oficial]. GitHub. https://github.com/comfyorg/comfyui-iclight — idioma_original: en [trad. propia — no oficial]. Verificada vía search (no fetch directo, hub). Licencia: Apache-2.0 (pack); pesos IC-Light con licencia propia; costo: gratis.
12. Comfy Registry. (s. f.). *Welcome to ComfyUI Registry* [Bienvenido al Registro]. https://registry.comfy.org — idioma_original: en [trad. propia — no oficial]. Verificada 200 el 2026-11-03. Costo: gratis (publicar con API key gratuita).

Fuentes de apoyo (verificadas por excerpt, fetch pendiente de detalle):
- ComfyUI Wiki. (2025). *How to Install ComfyUI Custom Nodes (Plugins)*. https://comfyui-wiki.com/en/install/install-custom-nodes — comunitaria mantenida, gratis.
- Comfy.ICU / RunComfy. *ComfyUI_CameraAngleSelector* (espejos con 124 stars, guía de instalación por Manager). https://comfy.icu/extension/NickPittas__ComfyUI_CameraAngleSelector · https://www.runcomfy.com/comfyui-nodes/ComfyUI_CameraAngleSelector — gratis.

## Metodología queries por idioma + URLs + status + gaps

- ES: `tutorial crear custom node ComfyUI docs oficiales` → derivó a versión EN oficial (gap IT/ES: la doc ES existe como espejo `docs.comfy.org/es/...` pero el walkthrough canónico verificado es EN).
- EN (2–3 variaciones × sub-pregunta):
  - `ComfyUI custom node development tutorial official docs.comfy.org INPUT_TYPES NODE_CLASS_MAPPINGS` → 8 resultados, 5 fetch 200 (walkthrough, interface, help_page, install_custom_node, backend).
  - `ComfyUI Registry publish custom node registry.comfy.org guide` → 8 resultados, 3 fetch 200 (publishing, overview, cicd).
  - `NickPittas ComfyUI_CameraAngleSelector github` → 8 resultados, 3 fetch 200 (repo + 2 code files vía excerpt).
  - `ComfyUI Manager install custom nodes registry git URL guide` → 8 resultados, 2 fetch 200 (pack-management vía manager/install, install_custom_node).
- IT: `pubblicare custom node ComfyUI registry guida` → gap explícito: no se halló guía IT dedicada; la doc oficial JA/ZH sí existe, IT queda como `datos insuficientes IT`.
- Status: 12 URLs 200 (7 fetch cuerpo completo + 5 excerpt GitHub con metadatos stars/commits verificados en página). 0 404 en el núcleo. YouTube de publishing (`WhOZZOgBggU`) citado en docs sin fetch de video (queda como candidato visual).
- Recencia: docs 2025–2026 vigentes; testigo 2026-01-10 (10 meses, 9 commits, mantenimiento bajo pero estable para estudio).

## Propuestas wiki esqueleto

- `custom-node-comfyui` (nueva/§comfyui): anatomía, scaffold, backend/frontend, checklist de publicación con `pyproject.toml` modelo.
- `comfyui-manager-instalacion` (§comfyui): vías Manager/git/ZIP, niveles de seguridad, missing nodes, criterios de confianza con tabla stars/mantenimiento/licencia.
- `camera-angle-selector` (nueva, caso testigo): autor, estado, 96 combinaciones, formato `<sks>`, instalación, límites (sin Registry, sin LICENSE), reutilización para Gaudí Nexus.
- `pyproject-comfy-registry` (§comfyui): campos obligatorios, `.comfyignore`, Action de publicación, versionado semántico.

## Candidatos

- ComfyUI docs: *Registry Overview* https://docs.comfy.org/registry/overview — Nivel 1 verificado por excerpt, candidato a ficha de versionado/seguridad si SOL aprueba.
- ComfyUI docs: *Custom Node CI/CD* https://docs.comfy.org/registry/cicd — Nivel 2 candidato (testing con Comfy-Action + dashboard) para pipeline del estudio.
- ComfyUI docs: *pyproject.toml specifications* https://docs.comfy.org/registry/specifications — Nivel 2 candidato (campos exactos) — esperar `s` para transcribir.
- YouTube embebido en publishing `https://www.youtube.com/embed/WhOZZOgBggU` — Nivel 2 candidato visual.
- GitHub `Comfy-Org/docs` `custom-nodes/backend/manager.mdx` (histórico custom-node-list.json) — Nivel 1 verificado por excerpt, útil como contexto pre-Registry.

## Dependencias vault

- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|reglas-workflows-comfy]] · [[wiki/glosario/interno/pbooks/pbk-comfyui|pbk-comfyui]] · [[raw/research/2026-10-08-comfyui-workflows-arq|comfyui-workflows-arq]] · [[raw/research/2026-10-20-flux2-klein-lora-rhino-to-image|flux2-klein-lora]] · [[proyectos/concurso-gaudi-nexus/index|concurso-gaudi-nexus]]
