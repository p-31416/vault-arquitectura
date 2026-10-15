---
tipo: log
fecha: 2026-10-08
sesion: handy-dictado
tags: [sesion, handy, stt, parakeet, dictado, windows, p-drive, junction]
estado: completada
proximo_paso: "Probar dictado diario en español; evaluar paste Shift+Insert si se usa en terminal"
---

# Sesión 2026-10-08 — Handy dictado local: install + modelos a P: + Parakeet V3 ES

> Más nuevo → más arriba. Estado al cierre: **completada**. Handy v0.9.8 x64 corriendo desde `P:\00-repos\Handy`, modelo Parakeet V3 español verificado con doble `Ctrl+Espacio`.

## Qué se hizo (orden cronológico)

1. **Descarga Handy v0.9.8 x64 .exe (con `s` de SOL)** — desde `handy.computer/download` → GitHub `cjpais/Handy`. Archivo `C:\Users\Solch16\AppData\Local\Temp\opencode\Handy_0.9.8_x64-setup.exe` (19.6 MB, SHA256 `4212EDB5...EECCC`). Verificado Windows 10 Pro N 64-bit, `P:` 651 GB libres vs `C:` 29,7 GB.
2. **Decisión ruta install** — `P:\` raíz deniega escritura (ACL SYSTEM); se usa `P:\00-repos\Handy`. Instalador lanzado 2 veces (PID 4888, luego 14828), modo Personalizado → `P:\00-repos\Handy`.
3. **Modelos pitau-voice ubicados** — `P:\00-repos\whisper-models` (210 MB blobs + `models--Systran--faster-whisper-base/tiny`), entrypoint `P:\00-repos\pitau-tech\pitauOS\01-PROYECTOS\pitau-voice\src\voice_input-pitau.py:10,27` (`HF_HUB_CACHE` a `P:`). README `00-README.md:45` confirma offline base int8.
4. **Modelo español Handy** — docs `handy.computer/docs/models` verificados: Parakeet V3 = `nvidia/parakeet-tdt-0.6b-v3` (~478 MB, 25 lenguas EU, auto-detect). Alternativa Whisper Small/Medium con `es` fijo. SOL eligió `parakeet TDT 0.6B v3`.
5. **Localización descarga auto (con `s`)** — `C:\Users\Solch16\AppData\Roaming\com.pais.handy\models\` vacía (solo custom .bin); real en `C:\Users\Solch16\.cache\huggingface\hub\models--handy-computer--parakeet-tdt-0.6b-v3-gguf\` (blob 705 MB). Settings `selected_model: handy-computer/parakeet-tdt-0.6b-v3-gguf/...Q8_0.gguf`, log confirma carga Vulkan RX 570.
6. **Mudanza a P: (con `si` de SOL)** — Handy cerrado, `Move-Item` de `C:\...\huggingface` → `P:\00-repos\Handy\huggingface`. Symlink interno `snapshots/...gguf` no migró (requiere admin); recreado como copia directa 705 MB. Junction `C:\Users\Solch16\.cache\huggingface` → `P:\00-repos\Handy\huggingface`. Total en P: 1,41 GB (duplicado blob+snapshot). Handy relanzado (PID 4452), carga OK `23:30:56`.
7. **Troubleshooting "no escribe aquí"** — log mostraba `Tap recording locked on until the next press` sin stop. Causa: falta segundo `Ctrl+Espacio`. Guía: foco en texto → `Ctrl+Espacio` → hablar → `Ctrl+Espacio` → pega. Nota paste: terminal usa `Shift+Insert` (Settings > Advanced). SOL confirmó: **"excelente ya funciona"**.

## Archivos modificados

| Archivo | Acción | Detalle |
|---|---|---|
| `P:\00-repos\Handy\handy.exe` + dlls | instalado (fuera del vault) | app 20 MB + `ggml-vulkan`, `onnxruntime`, `transcribe.dll` |
| `P:\00-repos\Handy\huggingface\` | creado (fuera del vault) | cache HF 1,41 GB, Parakeet V3 Q8_0 |
| `C:\Users\Solch16\.cache\huggingface` | convertido a Junction → P: | libera `C:`, Handy ve ruta original |
| `C:\Users\Solch16\AppData\Roaming\com.pais.handy\settings_store.json` | editado por Handy | `selected_model` parakeet-v3, `app_language es-ES`, binding `ctrl+space` |
| `raw/sessions/2026-10-08-sesion-handy-dictado.md` | creado | este archivo |

## Pendiente (retomar)

- Optimizar duplicado 1,41 → 0,7 GB con symlink elevado (requiere terminal admin, un comando `mklink`).
- Si se dicta en PowerShell/Windows Terminal, cambiar paste a `Shift+Insert`.
- Reutilización directa pitau-voice ↔ Handy no aplica (faster-whisper CTranslate2 vs GGUF/ONNX); conviven en `P:`.

## Análisis cerebro-digital

**Topics:** handy-install-p-drive, huggingface-cache-junction, parakeet-v3-español, tap-vs-hold-shortcut, paste-methods-windows-terminal, c-vs-p-storage-split, faster-whisper-vs-gguf-incompat.
**Entidades:** Handy v0.9.8 (P:\00-repos\Handy\handy.exe, PID 4452), Parakeet TDT 0.6B v3 Q8_0 (705 MB, Vulkan RX 570), pitau-voice (P:\00-repos\whisper-models, base/tiny int8, `language="es"`), iVCam mic, Windows 10 Pro N x64, `com.pais.handy` (Roaming + Local EBWebView).
**Hechos:** (1) `P:\` raíz sin escritura, `P:\00-repos\` sí; (2) Handy `models/` Roaming vacía por diseño, real es HF hub cache; (3) symlink HF requiere admin → fallback copia duplica a 1,41 GB; (4) modo tap exige 2 pulsaciones, log lo evidencia; (5) pastas terminal Windows exigen Shift+Insert según docs oficiales verificados.
