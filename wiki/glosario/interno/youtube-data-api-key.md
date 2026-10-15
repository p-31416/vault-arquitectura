---
tipo: metodologia
fecha_creacion: 2026-10-08
ultima_actualizacion: 2026-10-08
tags: [youtube, api, key, metodo, hitl]
---

# YouTube Data API v3 — cómo obtener la key

> Guía paso a paso para sacar la API key que permite traer **títulos, canal y duración**
> de los videos guardados. Sin esto, Takeout solo da el `video_id`.

## Por qué sirve

Google Takeout exporta tus listas de reproducción solo con el **ID** del video.
Con la APIkey completamos el dato que falta:

| Sin API | Con API |
|---|---|
| `7V7Aazicx-s` + fecha | `7V7Aazicx-s` + **título** + **canal** + **1:23:45** |

## Costo real

| Concepto | Valor |
|---|---|
| Cuota diaria por defecto | 10.000 unidades |
| Costo de `videos.list` | **1 unidad** (por llamada, hasta 50 videos) |
| Tus videos (~709) | ~15 llamadas = **15 unidades** |
| % de cuota diaria usada | **0,15 %** |

Gratis de sobra. Se puede re-correr 100+ veces al año sin acercarse al límite.

> **Ojo**: `search.list` cuesta **100 unidades** y viene **deshabilitado por defecto**
> en proyectos nuevos. Por eso los scripts usan `videos.list` (1 unidad), que ya
> devuelve título + canal + duración de paso. No hace falta habilitar search.

## Paso a paso

### Paso 1 — Crear el proyecto

1. Entrá a https://console.cloud.google.com/
2. Click en el **selector de proyecto** (arriba a la izquierda, dice *"Select a project"*)
3. Click en **New project**
4. Nombre: `vault-arquitectura-yt`
5. **Create**

### Paso 2 — Habilitar la API

1. Verificá que el proyecto seleccionado sea `vault-arquitectura-yt`
2. Entrá a https://console.cloud.google.com/apis/library
3. Buscá: `YouTube Data API v3`
4. Click en el resultado de googleapis.com
5. Click en **Enable**

### Paso 3 — Crear la clave

1. Entrá a https://console.cloud.google.com/apis/credentials
2. Arriba a la derecha: **Create credentials** → **API key**
3. Name: `vault-yt-titulos`
4. **Create**
5. Aparece un popup con la key: empieza con `AIzaSy`, tiene **39 caracteres**.
   **Copiá el valor completo ahora** — después Google solo muestra los primeros
   y los últimos 4 caracteres.

### Paso 4 — Restringir la key (30 segundos, importante)

En la misma pantalla, editá la clave con el ícono de lápiz:

**API restrictions**
- **Restrict key** → tildá **YouTube Data API v3** → **Apply**

**Application restrictions**
- **Restrict key** → dejalo en **None** por ahora.
  (Si lo ponés en IP, deja de funcionar desde otra compu o cuando cambia tu IP
  dinámica. Se puede endurecer después a IP de tu casa.)

**Save**

### Paso 5 — Guardarla en el vault

Agregá la línea al final de `.env` (ya está en `.gitignore`, verificado: `git ls-files` no lo trackea):

```
YOUTUBE_API_KEY=AIzaSy...tu...key...aqui
```

## Uso

```
$env:PYTHONIOENCODING="utf-8"
P:\Anaconda\envs\comfyenv\python.exe scripts\yt_titles.py
```

Después:

```
P:\Anaconda\envs\comfyenv\python.exe scripts\yt_takeout_parser.py
```

## Cache

`yt_titles.py` guarda en `raw/yt/cache-titulos.json`. Las siguientes corridas solo
piden los IDs que faltan, así que el gasto de cuota tiende a cero.

Para regenerar desde cero (borrar el cache): `Remove-Item raw\yt\cache-titulos.json`

## Diagnóstico

| Síntoma | Causa probable | Solución |
|---|---|---|
| `ERROR: YOUTUBE_API_KEY no esta en .env` | Falta la línea en `.env` | Agregala (Paso 5) |
| `ERROR de la API (403): ...Access Not Configured` | API no habilitada | Repetir Paso 2 |
| `ERROR de la API (400): ...API key not valid` | Key mal copiada | Recrear la key (Paso 3) |
| `ERROR de la API (403): ...quotaExceeded` | Cuota agotada | Esperar al reset diario (medianoche PT) o pedir extensión |
| `Sin titulo (borrados/privados): N` | Videos que ya no existen | Normal, no es error |
| Emojis `??` en la consola | Consola cp1252 | `$env:PYTHONIOENCODING="utf-8"` |

## Referencias

- Overview + quota: https://developers.google.com/youtube/v3/getting-started
- Registrar aplicación (credenciales): https://developers.google.com/youtube/registering_an_application
- Costos por método: https://developers.google.com/youtube/v3/determine_quota_cost
- Consola de cuotas: https://console.developers.google.com/iam-admin/quotas
- Extensión de cuota: https://support.google.com/youtube/contact/yt_api_form

## Conceptos relacionados

- [[raw/yt/00-index|raw/yt/00-index]] — índice del pipeline de curación
- [[wiki/glosario/interno/metodologia-curacion-youtube|metodologia-curacion-youtube]] — flujo completo
- [[raw/yt/videos-y-canales-guardados|videos-y-canales-guardados]] — el documento que se enriquece

## Origen

Sesión 2026-10-08 — definido para completar los títulos faltantes del Takeout.