---
name: corre-comfyui
description: Inicia o gestiona el servidor ComfyUI optimizado para AMD RX 570 8GB. Se activa cuando el usuario dice "corre comfyUI", "abri comfyUI", "comfyui on", o similar.
---

# Skill: corre-comfyui

Lanza y gestiona el servidor ComfyUI local optimizado para la estación de trabajo del estudio.

## Hardware

- **GPU**: AMD Radeon RX 570 8GB (gfx803, Polaris/GCN4)
- **RAM**: 32GB DDR3/DDR4
- **CPU**: Intel i5-4590 (HD Graphics 4600 integrada, no usar)
- **SO**: Windows 10/11

## Rutas

| Componente | Ruta |
|-----------|------|
| ComfyUI fuente | `P:\00-repos\ComfyUI` |
| Python (conda) | `P:\Anaconda\envs\comfyenv\python.exe` |
| Checkpoints | `P:\00-repos\ComfyUI\models\checkpoints\` |
| Script de lanzamiento | `P:\00-repos\ComfyUI\corre_comfyui.bat` |
| URL del servidor | `http://127.0.0.1:8188` |
| Guía de setup AMD | `P:\00-repos\vault-arquitectura\activos\documentos\setup-comfyui-amd-rx570.md` |

## Modelos Disponibles

| Modelo | Archivo | Notas |
|--------|---------|-------|
| ArchitectureRealMix v1.1 | `architecturerealmix_v11.safetensors` | Checkpoint principal, bueno para arquitectura |

## Cómo Ejecutar

### Opción 1 — Via opencode (recomendada)

Cuando el usuario pida iniciar ComfyUI, ejecutar en background:

```powershell
Start-Process -FilePath "P:\00-repos\ComfyUI\corre_comfyui.bat" -WorkingDirectory "P:\00-repos\ComfyUI"
```

Esperar ~5 segundos y luego verificar que esté corriendo:

```powershell
try { $r = Invoke-WebRequest -Uri "http://127.0.0.1:8188/system_stats" -UseBasicParsing -TimeoutSec 3; "ComfyUI ACTIVO — $($r.StatusCode)" } catch { "ComfyUI NO responde" }
```

### Opción 2 — Via terminal directo

```powershell
& "P:\Anaconda\envs\comfyenv\python.exe" "P:\00-repos\ComfyUI\main.py" --listen 127.0.0.1 --port 8188 --force-fp16 --preview-method auto --directml 0
```

### Opción 3 — Doble clic

Ejecutar `P:\00-repos\ComfyUI\corre_comfyui.bat`

## Parámetros Optimizados

| Flag | Valor | Por qué |
|------|-------|---------|
| `--listen` | `127.0.0.1` | Solo acceso local |
| `--port` | `8188` | Puerto por defecto |
| `--force-fp16` | — | fp16 = mitad de VRAM, la RX 570 lo soporta |
| `--preview-method` | `auto` | Preview en el frontend |
| `--cache-ram` | `2 8` | 2GB activo, hasta 8GB con 32GB disponibles |
| `--directml` | `0` | GPU index 0 (la RX 570, no la iGPU Intel) |
| `--disable-auto-launch` | — | No abre browser automáticamente |

### Flags de emergencia (si queda sin VRAM)

```powershell
# Modo bajo VRAM — text encoders van a CPU
--lowvram

# VAE en CPU (lento pero no crashea)
--cpu-vae

# FP32 completo (más VRAM, más lento)
--force-fp32

# Sin cache (mínimo uso de RAM/VRAM)
--cache-none
```

## Cómo Verificar Estado

```powershell
# Check rápido
Invoke-RestMethod -Uri "http://127.0.0.1:8188/system_stats" | ConvertTo-Json -Depth 3

# Parar ComfyUI
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Cómo Detener

```powershell
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force
```

O desde el terminal donde corre, `Ctrl+C`.

## Post-Instalación ZLUDA

Cuando se migre a ZLUDA, eliminar `--directml 0` del batch y los parámetros. ZLUDA se encarga del resto.

## Notas

- **Primera ejecución después de cambio de modelo**: puede tardar ~30s extra (compilación de kernels)
- **SDXL con 8GB**: funciona pero puede necesitar `--lowvram` o tiling en VAE
- **VRAM reportada por DirectML puede ser incorrecta** (mostraba 1GB, la real es 8GB)
- Si el usuario reporta errores de memoria, sugerir `--lowvram` primero
