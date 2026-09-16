---
tipo: playbook
seccion: comfyui-playbooks
fecha_creacion: 2026-07-24
ultima_actualizacion: 2026-07-24
tags: [comfyui, mcp, troubleshooting, reconexion, amd, directml, oom]
---

# Playbook: Troubleshooting y Reconexión MCP ↔ ComfyUI

**Contexto**: Estudio en Argentina, AMD RX 570 8GB VRAM + DirectML, ComfyUI local en `http://127.0.0.1:8188`, MCP `artokun/comfyui-mcp` vía `npx` en Opencode/Claude.

---

## 1. Síntomas comunes

| Síntoma | Causa probable |
|---------|----------------|
| MCP no lista herramientas / "connection refused" | ComfyUI no corriendo o puerto distinto |
| "WebSocket disconnected" en medio de generación | OOM (VRAM 8GB llena), driver AMD DirectML inestable, ComfyUI crasheó |
| Generación cuelga en "executing" sin progreso | VRAM agotada, proceso worker zombie, cola bloqueada |
| MCP dice "prompt_id not found" | ComfyUI reinició y perdió historial; el MCP sigue con session vieja |
| Modelos no aparecen en dropdowns | `extra_model_paths.yaml` mal configurado o ComfyUI no reinició tras cambios |

---

## 2. Diagnóstico rápido (30 seg)

```bash
# 1. ¿ComfyUI responde?
curl -s http://127.0.0.1:8188/system_stats | head -c 200

# 2. ¿Hay GPU/VMAR libre?
# En la respuesta buscar: "gpu_free", "vram_free"

# 3. ¿La cola está atascada?
curl -s http://127.0.0.1:8188/queue | jq '.queue_running, .queue_pending'
```

**Si falla el curl** → ComfyUI caído. Ir a **Sección 3**.

**Si responde pero VRAM < 500MB** → OOM inminente. Ir a **Sección 4**.

**Si cola tiene jobs "running" eternos** → Worker zombie. Ir a **Sección 5**.

---

## 3. ComfyUI caído — Reinicio controlado

### Opción A: Via MCP (si el server MCP sigue vivo)
```bash
# En Opencode/Claude chat:
comfyui_restart_comfyui
```

### Opción B: Manual (tu `.bat` actual)
```powershell
# 1. Matar procesos previos (PowerShell)
Get-Process python* -ErrorAction SilentlyContinue | Stop-Process -Force
Get-Process comfy* -ErrorAction SilentlyContinue | Stop-Process -Force

# 2. Lanzar con tu .bat parametrizado RX 570
.\corre_comfyui.bat
# Contenido esperado del .bat:
# P:\Anaconda\envs\comfyenv\python.exe -m comfyui --directml 0 --force-fp16 --disable-cuda-malloc --listen 127.0.0.1 --port 8188
```

### Opción C: Via comfy-cli (más robusto, persiste config)
```bash
# Una vez instalado comfy-cli
comfy launch --background -- --directml 0 --force-fp16 --disable-cuda-malloc
```

**Verificación**: `curl http://127.0.0.1:8188/system_stats` → debe devolver JSON con `gpu_free`, `vram_total`, etc.

---

## 4. VRAM llena (OOM) — Liberar y prevenir

### Inmediato (vía MCP)
```bash
comfyui_clear_vram
# O desde Opencode/Claude:
# clear_vram(unload_models=true, free_memory=true)
```

### Prevención en workflows
- **Siempre** usar `ImageScale` antes de `VAEEncode` si input > 512×512 (RX 570 8GB)
- Checkpoint SD 1.5 (`architecturerealmix_v11.safetensors`) **no** SDXL (7GB+)
- Un ControlNet a la vez; dos solo si checkpoint es SD 1.5
- `K
- `--lowvram` o `--cpu-vae` en `.bat` si persiste OOM con SDXL

### Config `.bat` recomendada RX 570
```bat
@echo off
set PYTORCH_DIRECTML_DEVICE=0
P:\Anaconda\envs\comfyenv\python.exe -m comfyui ^
  --directml 0 ^
  --force-fp16 ^
  --disable-cuda-malloc ^
  --lowvram ^
  --listen 127.0.0.1 ^
  --port 8188
```

---

## 5. Cola atascada / Worker zombie

```bash
# 1. Ver cola
curl -s http://127.0.0.1:8188/queue | jq .

# 2. Cancelar job corriendo (si prompt_id conocido)
comfyui_cancel_job --prompt_id <ID> --clear_pending true

# 3. O limpiar TODO (nuclear)
comfyui_clear_queue
# + reiniciar ComfyUI (Sección 3)
```

---

## 6. MCP desconectado — Reconexión completa

**El MCP `artokun/comfyui-mcp` NO se reconecta solo.** El proceso `npx` muere o pierde el WebSocket.

### Secuencia obligatoria:

1. **Verificar ComfyUI vivo** (Sección 2)
2. **Matar proceso MCP anterior**
   - Opencode: `Ctrl+C` → volver a entrar
   - Claude Desktop: Cerrar app completa → reabrir
   - Terminal crudo: `pkill -f "comfyui-mcp"` o cerrar la pestaña
3. **Re-lanzar cliente MCP**
   - Opencode: `opencode` (lee config y levanta MCP)
   - Claude Desktop: auto al abrir
   - Manual: `npx -y @comfyorg/comfyui-mcp` (variable `COMFYUI_URL=http://127.0.0.1:8188`)
4. **Verificar tools disponibles**
   - En chat: "lista herramientas ComfyUI" → deben aparecer 100+

---

## 7. Modelos no aparecen / extra_model_paths.yaml

### Verificar config activa
```bash
comfyui_list_extra_paths
```

### Estructura correcta (standalone)
```yaml
# P:\00-repos\ComfyUI\extra_model_paths.yaml
comfyui_mcp:
  checkpoints:
    - P:\00-repos\ComfyUI\models\checkpoints
    - E:\Modelos\checkpoints
  loras:
    - P:\00-repos\ComfyUI\models\loras
  controlnet:
    - P:\00-repos\ComfyUI\models\controlnet
  vae:
    - P:\00-repos\ComfyUI\models\vae
  upscale_models:
    - P:\00-repos\ComfyUI\models\upscale_models
```

**Tras editar**: `comfyui_restart_comfyui` (obligatorio).

---

## 8. Checklist post-recuperación

- [ ] `system_stats` responde con VRAM libre > 1GB
- [ ] `list_local_models` muestra checkpoints/LoRAs/ControlNets
- [ ] `generate_image` test: "a simple cube, architectural render" → 512×512, 20 steps, SD 1.5
- [ ] Output aparece en `list_output_images` y `view_image`
- [ ] MCP lista 100+ tools sin errores

---

## 9. Escalación (si nada funciona)

| Nivel | Acción |
|-------|--------|
| 1 | Revisar logs: `comfyui_get_logs --keyword error --max_lines 200` |
| 2 | `comfyui_health_check` — reporte completo |
| 3 | Reinstalar ComfyUI limpio: `comfyui_install_comfyui --target_path P:\ComfyUI_clean --version latest` |
| 4 | Reportar issue: `comfyui_report_issue` con logs + `system_stats` + pasos para reproducir |

---

## Referencias vinculadas

- [[wiki/estudio/adr-001-comfyui-mcp|ADR-001: Decisión MCP ComfyUI]]
- [[proyectos/MVP_04-comfyui-arquitectura/pbook-comfy_setup|Playbook Setup Opciones]]
- [[proyectos/MVP_04-comfyui-arquitectura/modelos-recomendados|Modelos recomendados AMD 8GB / NVIDIA 24GB+]]
- [[proyectos/MVP_04-comfyui-arquitectura/reglas-workflows-comfy|Reglas Workflows ComfyUI (obligatorio leer)]]