---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, runpod, n8n, automatizacion]
idioma: es
---

# 00 — n8n (VPS) como mayordomo del pod: prender, correr, apagar

> Sí: la conexión n8n↔pod existe sobre todo para **prenderlo y apagarlo**. El ciclo completo es: n8n arranca el pod, espera que esté listo, encola el workflow por API, descarga el resultado, avisa por Telegram y **apaga el pod**. Sin este ciclo el ahorro del pod barato se pierde en horas olvidadas prendidas.

## 1. Arquitectura (todo por HTTP, nada que instalar)

```
n8n (VPS) ── API Runpod v2 ──▶ pod (arranca / para)
n8n (VPS) ── proxy https ──▶ ComfyUI (/prompt, /history, /view)
n8n (VPS) ── Telegram send ──▶ aviso con la imagen (saliente, sin webhook público)
```

La API key de Runpod vive en las **credenciales de n8n** (Header Auth), nunca pegada en un nodo ni en el grafo.

## 2. Endpoints (API v2 vigente; v1 se retira el 15-11-2026)

| Paso | Método + URL | Body |
|---|---|---|
| Arrancar | `POST https://api.runpod.io/v2/pods/{POD_ID}/action` | `{"action":"start"}` |
| Parar | `POST https://api.runpod.io/v2/pods/{POD_ID}/action` | `{"action":"stop"}` |
| Terminar (borra) | `DELETE https://api.runpod.io/v2/pods/{POD_ID}` | — |
| ¿Listo? | `GET https://[POD_ID]-8188.proxy.runpod.net/system_stats` | — (200 = listo) |
| Encolar | `POST https://[POD_ID]-8188.proxy.runpod.net/prompt` | `{"prompt": {<grafo API>}, "client_id": "<id>"}` |
| Ver estado | `GET https://[POD_ID]-8188.proxy.runpod.net/history/{PROMPT_ID}` | — (con outputs = terminado) |
| Descargar | `GET https://[POD_ID]-8188.proxy.runpod.net/view?filename=...&subfolder=...&type=output` | — (binario) |

Header en las de Runpod: `Authorization: Bearer TU_API_KEY`. Las de ComfyUI no llevan auth (la URL del proxy ya es privada: no compartirla).

## 3. Workflow n8n nodo por nodo

1. **Trigger**: Schedule (ej: cada vez que hay trabajo) o Manual para probar. El Telegram Trigger pide webhook público: para *recibir* órdenes por Telegram hace falta el túnel; para *avisar* con Telegram Send alcanza con salida a internet.
2. **HTTP start**: arranca el pod (tabla §2).
3. **Loop de espera**: Wait 30 s → HTTP `/system_stats` → IF status ≠ 200 → volver al Wait (tope ~15 intentos ≈ 7 min; si no llega, ir al paso 7 y avisar error).
4. **HTTP /prompt**: body con el workflow en formato API (exportado de ComfyUI) + `client_id` fijo por sesión. Guardar el `prompt_id` de la respuesta.
5. **Loop de corrida**: Wait 20 s → HTTP `/history/{PROMPT_ID}` → IF sin outputs → volver al Wait (tope según el WF; klein ≈ 5 min sobra).
6. **HTTP /view + Telegram**: descargar el PNG y mandarlo por Telegram Send (o guardarlo en el VPS).
7. **HTTP stop**: apagar el pod **siempre**, incluso si algo falló (rama de error del workflow → stop igual). Es el nodo más importante del grafo.

## 4. Prueba antes de automatizar

Cada HTTP se prueba a mano primero (curl o el propio n8n en modo test): start → 200 en system_stats → prompt de prueba → history con outputs → stop. Recién después se conectan los nodos. Un ciclo manual completo valida credenciales, pod ID y proxy de una vez.

## 5. Costo del ciclo

Con A5000 community ($0,16/h): un ciclo de 13 min ≈ $0,035 de GPU. n8n y Telegram no suman costo. El fail-safe del paso 7 es lo que separa $0,035 de $3,80 (un pod olvidado un día).

## Referencias

- Pod barato y discos: [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-flux-economico|00 — Pod Flux económico]]
- Instalar ComfyUI en el pod: [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-instalar-comfy-paso-a-paso|00 — Instalar ComfyUI en Runpod]]
- API Runpod (start/stop/terminate): https://docs.runpod.io/pods/manage-pods
- Migración v1→v2 (fechas de retiro): https://docs.runpod.io/api-reference-v2/migrate-from-v1
