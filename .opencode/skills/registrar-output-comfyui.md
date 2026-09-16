---
name: registrar-output-comfyui
description: Registra el output de una corrida de ComfyUI en el vault. Se activa cuando el usuario dice "registrá esto", "registrar output", "guardar resultado", o similar después de una generación.
---

# Skill: registrar-output-comfyui

Registra una imagen generada por ComfyUI en la documentación del workflow correspondiente. Cada registro es una entrada nueva en los archivos de log del workflow.

## Trigger

Se ejecuta **después de que ComfyUI genera una imagen** y el usuario pide registrarla. Nunca se ejecuta automáticamente — solo bajo pedido explícito.

## Inputs necesarios

| Input | Requerido | Cómo obtenerlo |
|-------|-----------|----------------|
| Archivo imagen | Sí | `comfyui_list_output_images` o ruta directa de `P:\00-repos\ComfyUI\output\` |
| Workflow asociado | Sí | Identificar cuál workflow lo generó (nombre del prefix en SaveImage) |
| Parámetros de la corrida | Sí | `comfyui_get_history` → prompt_id, o del workflow JSON |
| Evaluación del usuario | No | El usuario la provee verbalmente |

## Workflow paso a paso

### 1. Localizar el output

```powershell
Get-ChildItem "P:\00-repos\ComfyUI\output" -Filter "<prefix>*" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, Length, LastWriteTime
```

El `prefix` viene del nodo SaveImage del workflow (ej: `estadio_futbol`, `ComfyUI`).

### 2. Identificar el workflow

Mapear el prefijo del archivo al workflow correspondiente:

| Prefix SaveImage | Workflow | Ubicación |
|-----------------|----------|-----------|
| `estadio_futbol` | workflow_txt2img_estadio.json | `n_01-txt2img/log-WF-estadio/` |
| (agregar más) | | |

Si el prefix no matchea con ningún workflow conocido, preguntar al usuario.

### 3. Obtener parámetros de la corrida

```powershell
# Última ejecución
comfyui_get_history

# O por prompt_id específico
comfyui_get_history prompt_id="<prompt_id>"
```

Extraer:
- **prompt_id** (identificador único de la corrida)
- **seed** (del nodo KSampler)
- **steps, cfg, sampler, scheduler, denoise** (del nodo KSampler)
- **resolución** (del nodo EmptyLatentImage)
- **prompt positivo y negativo** (de CLIPTextEncode)
- **checkpoint** (de CheckpointLoaderSimple)
- **tiempo de ejecución** (duration_ms del history)
- **nodos cacheados** (si hubo)

Si el history no está disponible (ComfyUI se reinició), pedir al usuario o leer del workflow JSON.

### 4. Determinar nombre de variante

Formato: `n_01-{L}-{nn}` donde:
- **n_01** = nivel del MVP (n_01-txt2img, n_02-img2img, etc.)
- **L** = letra de grupo:
  - **A** = Baseline absoluto (parámetros idénticos, sin cambios)
  - **B+** = Exploración sistemática (seed, cfg, sampler, prompt...)
  - **C+** = Cambio de workflow (nodos nuevos, conexiones modificadas)
- **nn** = número secuencial dentro del grupo (01, 02, 03...)

Leer `index.md` del workflow para ver la última variante registrada y continuar la secuencia.

### 5. Copiar imagen a salidas/

```powershell
Copy-Item "P:\00-repos\ComfyUI\output\<archivo>.png" "proyectos/MVP_04-comfyui-arquitectura/<nivel>/<workflow>/salidas/n_01-{L}-{nn}.png"
```

**Nunca mover** — siempre copiar. El original queda en ComfyUI/output como backup.

### 6. Verificar si hubo cambios en el workflow

Comparar el workflow ejecutado contra el JSON guardado:

```
comfyui_get_workflow filename="<workflow>.json"
```

Preguntar al usuario si hubo cambios manuales en el canvas. Si sí:
- Actualizar el `.json` del workflow con la versión nueva
- Documentar los cambios en `prompts-log.md` como parte de la entrada
- Si hay nodos nuevos → actualizar `nodos.md` con documentación del nodo
- Marcar variante con grupo **C** en vez de A o B

### 7. Registrar en prompts-log.md

Agregar bloque al inicio de la sección `## Log` (más nuevo = más arriba):

```markdown
### `n_01-{L}-{nn}` | YYYY-MM-DD | HH:MM

**Cambio:** <descripción del cambio respecto al anterior>

| Parámetro | Valor |
|-----------|-------|
| steps | <valor> |
| cfg | <valor> |
| sampler | <valor> |
| scheduler | <valor> |
| res | <W>x<H> |
| seed | <valor> |
| checkpoint | <nombre> |
| tiempo | <X>s (<hardware>) |
| prompt_id | <prompt_id> |

**Prompt positivo:**
\```
<texto completo>
\```

**Prompt negativo:**
\```
<texto completo>
\```

![n_01-{L}-{nn}](salidas/n_01-{L}-{nn}.png)

**Evaluación:** <comentarios del usuario o "Pendiente de evaluación">

**Mejoras sugeridas → [[backlog]]:**
- <si las hay>

**Cambios en workflow:** <"sin cambios" | descripción de cambios>
```

### 8. Actualizar index.md

Agregar fila a la tabla de `## Variantes ejecutadas`:

```markdown
| `A-02` | 2026-07-18 | ~00:48 | Segunda corrida baseline | steps=30, cfg=7, euler, normal, 768×512, seed=42 | ![A-02](salidas/n_01-A-02.png) |
```

### 9. Actualizar nodos.md (si hubo cambios)

Si se detectaron nodos nuevos o modificados en el paso 6:
- Agregar sección completa del nodo nuevo en `nodos.md`
- Seguir el formato existente: tabla de propiedades, inputs/outputs, enlace a docs oficiales
- Actualizar `ultima_actualizacion` en el frontmatter

### 10. Actualizar backlog (si hay sugerencias)

Si la evaluación genera ideas de mejoras, agregar ítems a `backlog.md`:

```markdown
| 4 | <descripción de la prueba sugerida> | n_01-{L}-{nn} | <prioridad: alta/media/baja> | pendiente |
```

### 11. Actualizar README.md del workflow

Si es la primera vez que se registra O si hubo cambios significativos:
- Actualizar `ultima_actualizacion` en frontmatter
- Si se cambió el prompt o parámetros base, reflejar en la tabla de parámetros

### 12. Registrar en log.md del vault

Agregar entrada al final del archivo `log.md` del vault (inmutable):

```
- **<nivel> — <descripción>**: `<archivo>.png` registrado en `salidas/n_01-{L}-{nn}.png`. <resumen de cambios>. ~<tiempo>s render.
```

### 13. Verificación final

Confirmar que todos los archivos se actualizaron:

```powershell
# Verificar que la imagen existe en salidas/
Get-Item "proyectos/.../salidas/n_01-{L}-{nn}.png"

# Verificar que prompts-log tiene la entrada
Select-String "n_01-{L}-{nn}" "proyectos/.../prompts-log.md"

# Verificar que index tiene la fila
Select-String "n_01-{L}-{nn}" "proyectos/.../00-index.md"
```

## Checklist rápido

```
[ ] Imagen copiada a salidas/
[ ] prompts-log.md actualizado
[ ] index.md actualizado
[ ] nodos.md actualizado (si hubo cambios)
[ ] backlog.md actualizado (si hay sugerencias)
[ ] README.md actualizado (si cambió el workflow)
[ ] log.md del vault actualizado
[ ] Verificación de archivos
```

## Casos especiales

### Múltiples outputs de una corrida
Si un workflow genera múltiples imágenes (batch_size > 1), registrar cada imagen como entrada separada en prompts-log, pero como una sola variante en index.

### Corrida fallida
Si ComfyUI tira error pero genera un output parcial, igualmente registrar en prompts-log con la nota del error. No copiar a salidas/ si la imagen está corrupta.

### Workflow modificado durante la corrida
Si el usuario modificó el workflow en el canvas antes de la corrida, tratar como variante **C** y documentar TODOS los cambios (nodos agregados/eliminados, conexiones cambiadas, valores modificados).

### Output no es del workflow actual
Si el prefix del archivo no matchea con el workflow del log, preguntar al usuario qué workflow lo generó antes de registrar.
