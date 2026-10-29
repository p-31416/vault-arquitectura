---
tipo: adr
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: aceptada
tags: [adr, mvp_07, studio-os, runpod, gpu, cloud, pi, privacidad]
idioma: es
---

# ADR-2026-10-28-nodo-gpu-runpod-secure: Runpod Secure Cloud es el nodo GPU del sistema

**Fecha**: 2026-10-28
**Estado**: aceptada
**Deciden**: SOL
**Proyecto**: [[proyectos/MVP_07-studio-os-sistema/readme-mvp_07|MVP_07 Studio OS]]

## Contexto

FLUX.2 klein 9B y el LoRA del concurso no entran en la RX 570 de 8 GB del banco de pruebas: hacen falta 24 GB. La auditoría de 29 fuentes oficiales (`raw/research/2026-10-28-runpod-auditoria-pi.md`) encontró tres cosas que cambian el plan anterior del vault: **no existe cláusula de no-entrenamiento** en Privacy Policy, ToS ni DPA; **el DPA no está firmado por defecto** (PandaDoc), y los *Performance Data* (logs y telemetría) **quedan fuera del DPA**, sin plazo acotado. Además **Community Cloud deja de aceptar hosts nuevos** y el cifrado solo aplica a *volume disk*. El mandato vigente del estudio es "PI 100% protegida, nada se entrena, planos legales nunca en cloud".

## Decisión

El nodo GPU por defecto es **Runpod Secure Cloud**, bajo cinco condiciones previas verificables: **DPA firmado**, **confirmación escrita de no-entrenamiento**, **volume disk cifrado**, **cero puertos públicos** y **borrado manual del volumen** al terminar. Se usa **solo con material derivado y no sensible**.

## Alternativas

### Community Cloud ($0,22/h)
- Pros: precio mínimo; ya está en el vault como cifra de referencia.
- Contras: está en retirada (deja de aceptar hosts nuevos), es peer-to-peer entre proveedores sin SLA de Pods, y el precio barato no compensa el riesgo de confidentiality.

### Proveedores europeos (Scaleway FR / OVHcloud FR, L4 €0,75/h per-minute)
- Pros: residencia de datos en UE y GDPR; SLO 99,5% en Scaleway; sin penalización de confidencialidad.
- Contras: precio levemente superior al Secure de Runpod en 24 GB (≈$0,59/h), y no se verificó integración oficial con nuestro stack de ComfyUI + tailnet.

### 100% local
- Pros: PI máxima.
- Contras: inviable hoy: el banco de pruebas tiene 8 GB y el estudio no tiene GPU de 24 GB; el modelo 9B, el LoRA y el video quedan afuera.

## Consecuencias

### Positivas
- 24 GB bajo demanda para 9B, LoRA y video, pagados por segundo (3090 Secure ≈ $0,50/h; A100 80 GB $1,79/h): un lote de 20-40 renders cuesta $2,5-5.
- El nodo se apaga solo al terminar: no hay capacidad ociosa pagando.
- El pod se anuncia en la red privada, igual que el runner del estudio: el sistema lo llama por nombre.

### Negativas
- El precio útil se duplica respecto de la cifra que estaba anotada en el vault ($0,22 → $0,50/h).
- El DPA y la confirmación escrita son requisitos **no técnicos**: bloquean el primer pod si nadie los pide.
- Runpod **no documenta Tailscale**: la integración del pod con la red privada se construye a medida (sidecar `tailscaled` en un template propio, porque Runpod no soporta Docker Compose).

### Riesgos + mitigación
- **Material sensible en la nube**: mitigado por política por clase de dato (planos legales, material de cliente confidential y material de concurso con PI de terceros no van), y por el hecho de que solo entra material **derivado**.
- **Logs y telemetría fuera del DPA**: retenidos sin plazo acotado → el material que llega al pod se trata como expuesto a ese operador y nunca es el original.
- **Proxy público por defecto**: se cierra; el pod se alcanza solo por la red privada.
- **Sin SLA de Pods**: el flujo crítico no puede depender del pod: los renders de entrega tienen salida manual documentada.

## Trazabilidad

- spec: [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]] §2.5 · [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec-mvp_07]] §5
- wiki: [[wiki/glosario/software/comfy-cloud-vs-runpod|comfy-cloud-vs-runpod]] · [[wiki/glosario/entidades/runpod|runpod]]
- research: [[raw/research/2026-10-28-runpod-auditoria-pi|auditoría Runpod 2026-10-28]] (29 fuentes oficiales)
- sesión: [[raw/sessions/2026-10-28-sesion-delinear-pitauos|sesión 2026-10-28]]
