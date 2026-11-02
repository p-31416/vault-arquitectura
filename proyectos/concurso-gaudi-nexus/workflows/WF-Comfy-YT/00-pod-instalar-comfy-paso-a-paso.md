---
tipo: guia
proyecto: concurso-gaudi-nexus
fecha_creacion: 2026-11-02
ultima_actualizacion: 2026-11-02
tags: [concurso, gaudi-nexus, comfyui, youtube, wf-comfy-yt, runpod, pod, instalacion]
idioma: es
---

# 00 — Instalar ComfyUI en Runpod paso a paso (correrlo en la nube)

> Objetivo: ComfyUI corriendo en un pod y abierto en el navegador **desde cualquier PC**, sin instalar nada en local salvo el navegador. La PC queda libre; el pod hace todo el trabajo. Complementa a [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-runpod-comfyui|00 — ComfyUI en un pod]] (conceptos) y [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-flux-economico|00 — Pod Flux económico]] (costos).

## 1. Qué vas a tener al final

- Una URL tipo `https://[POD-ID]-8188.proxy.runpod.net` que abre tu ComfyUI desde cualquier PC con internet.
- Tus modelos y workflows persistiendo entre sesiones en el disco del pod.
- Costo: solo minutos de GPU usada (ej: A5000 $0,16/h) + centavos de disco.

## 2. Requisitos (5 min, una vez)

1. Cuenta en https://www.runpod.io (email, GitHub o Google).
2. Saldo para cubrir 1 h de la GPU elegida (mínimo práctico: $10).
3. Nada instalado en la PC. Opcional: clave SSH si querés terminal directa (el pod trae terminal web, alcanza).

## 3. Instalación paso a paso

### Paso 1 — Desplegar el pod (consola, desde cualquier PC)

1. Entrar a https://console.runpod.io/pods → **Deploy**.
2. GPU: **RTX A5000** community ($0,16/h, 24 GB, suficiente para klein 9B y SDXL) o **RTX 4090** community ($0,34/h) si hay prisa. Si no hay stock, probar otra región.
3. Template: **el oficial ComfyUI** (trae ComfyUI + Manager auto-arrancando; nada que instalar). Blackwell (5090/B200) solo con el template Blackwell Edition.
4. Storage: container disk 30 GB + **volume disk 100 GB** (ahí viven modelos y salidas entre stops).
5. **Deploy On-Demand**.

### Paso 2 — Esperar que esté listo

Estado `Running` no es listo: la secuencia normal es `404 → 502 → 200`. Primer boot: de ~20 s (imagen cacheada) a varios minutos (con volumen) y hasta 30 min en el peor caso. No re-desplegar: esperar y refrescar.

### Paso 3 — Abrir ComfyUI

1. En la ficha del pod → **Connect** → **Connect to HTTP Service [Port 8188]**.
2. Se abre el ComfyUI en una pestaña nueva. **Guardar esa URL como bookmark**: es tu ComfyUI desde cualquier PC.
3. No compartir la URL: quien la tiene usa tu GPU. Al terminar la sesión, stop al pod.

### Paso 4 — Modelos (una sola vez)

1. En ComfyUI → **Manager → Model Manager** → buscar e instalar (ej: klein 9B, qwen, VAE, tu LoRA subido por el file browser del puerto 8080 o el terminal web).
2. Alternativa por terminal web del pod: descargar directo a `ComfyUI/models/<carpeta>/` (no se re-descarga nunca más mientras el disco viva).
3. Refrescar el navegador (R) para que aparezcan en los dropdowns.

### Paso 5 — Custom nodes (una sola vez por nodo)

1. **Manager → Install Custom Nodes** → instalar → **reiniciar** desde el propio Manager.
2. Verificar que el nodo aparece en la librería antes de cargar el workflow que lo usa.

### Paso 6 — Workflows desde cualquier PC

1. Arrastrar el `.json` (o un PNG generado por ComfyUI) al canvas: el flujo se carga.
2. Encolar, descargar el resultado con clic derecho.
3. **Exportar cada JSON que funcione a tu PC** (Workflow → Export) antes del stop: el canvas no es backup.

### Paso 7 — Apagar bien

- **Stop** entre sesiones del mismo sprint (el disco conserva todo; ojo: el disco parado también factura, ver costos).
- **Terminate** solo al cerrar el sprint y con todo exportado (borra lo que no esté en un network volume).

## 4. Usarlo desde otra PC

Solo necesitás: la URL del pod (bookmark) + el pod corriendo. Levantás el pod desde el celu o la otra PC (console.runpod.io → Start), esperás el 200, abrís la URL. Tus modelos, nodos y workflows siguen ahí porque viven en el volume disk.

## 5. Si algo falla

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| Bad Gateway / Not Ready | boot en curso | esperar y refrescar, hasta 30 min el primero |
| Sin stock de GPU | demanda en esa región | otra GPU (A5000↔4090) u otra región |
| Modelo no aparece | falta refresh | R en el navegador; verificar carpeta `models/` |
| Nodo no aparece | falta reinicio | reiniciar desde Manager tras instalar |
| Pod parado y disco facturando | volume disk idle | terminate si la pausa es larga (con respaldo) |

## Referencias

- Tutorial oficial (verificado): https://docs.runpod.io/tutorials/pods/comfyui
- Pods: https://docs.runpod.io/pods/manage-pods · Storage: https://docs.runpod.io/storage/network-volumes
- Costos: [[proyectos/concurso-gaudi-nexus/workflows/WF-Comfy-YT/00-pod-flux-economico|00 — Pod Flux económico]] · https://www.runpod.io/pricing
