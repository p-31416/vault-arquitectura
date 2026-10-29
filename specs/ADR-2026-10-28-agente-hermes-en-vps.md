---
tipo: adr
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: aceptada
tags: [adr, mvp_07, studio-os, hermes, agente, vps, n8n, mcp]
idioma: es
---

# ADR-2026-10-28-agente-hermes-en-vps: Hermes corre en el VPS como agente único del estudio

**Fecha**: 2026-10-28
**Estado**: aceptada
**Deciden**: SOL
**Proyecto**: [[proyectos/MVP_07-studio-os-sistema/readme-mvp_07|MVP_07 Studio OS]]

## Contexto

El vault ya tiene `opencode` con 8 servidores MCP (comfyui, n8n, fathom, leantime, autodesk-help, autocad, rhino) y un bot de Telegram en n8n que agenda en Cal.com, manda digest y sincroniza Fathom. Falta el agente que **interprete** pedidos y coordine tareas sobre archivos reales (AutoCAD, Rhino, Twinmotion, Unreal) dejando trazabilidad. `raw/docs/plan-hermes.md` §4 propone Hermes como eje, pero pide prueba de concepto antes de adoptarlo. Documentación oficial de Hermes verificada el 2026-10-28: imagen oficial `nousresearch/hermes-agent`, gateway supervisado por s6, estado íntegro en `/opt/data`, cliente MCP nativo, memoria persistente y skills; la entrada de catálogo `n8n-official` conecta con nuestro `https://n8n.pitau.tech/mcp-server/http`. Medición del VPS del 2026-10-28: 4.858 MB de RAM disponibles sobre 7.941 MB, 12 servicios Swarm vivos.

## Decisión

Instalamos **Hermes en el mismo VPS** (servicio Docker Swarm vía EasyPanel, límite `--memory=3g --cpus=2`, sin Playwright al inicio) como **agente único del estudio**, con `n8n` como motor de flujos deterministas al que Hermes llama por el MCP oficial, y el **vault como única memoria**.

## Alternativas

### OpenClaw
- Pros: 29 canales, configuración declarativa, skills; ya evaluado en el vault.
- Contras: Node, gateway local, menos cercano a lo que ya somos (n8n + Telegram + vault); el veredicto previo del vault fue que la capacidad vive en el MCP + contrato + índice, no en el shell.

### opencode + n8n sin Hermes
- Pros: ya resuelve ~90% técnico; cero RAM adicional; cero configuración duplicada.
- Contras: no aporta shell de Telegram propio ni memoria persistente por perfil; la decisión del usuario fue avanzar con Hermes desde el arranque.

### Agente dentro de n8n (LIDIA V5.0)
- Pros: ya funciona y está probado con cuentas reales.
- Contras: atado a flujos predefinidos; no escala a tareas sobre archivos con contrato, registro y aprobación.

## Consecuencias

### Positivas
- Un agente que interpreta, planifica y delega, con MCP nativo y memoria persistente, sin escribir un orquestador propio.
- El shell de Telegram, las skills y la memoria dejan de estar atados a n8n: el producto se puede mover de VPS a una PC del estudio sin reescribir el cerebro.
- La entrada `n8n-official` reutiliza el n8n que ya está andando: los flujos deterministas no se reimplementan.

### Negativas
- **RAM**: 3 GB de los 4.858 MB disponibles → el margen es real y hay que monitorear; si el swap se mueve, se recorta alcance.
- **Configuración duplicada**: los MCP viven hoy en `opencode.json` y pasaron a `config.yaml` de Hermes → hay que sostener un único archivo de verdad para los servidores MCP.
- **Dos superficies de herramientas** (opencode para desarrollo, Hermes para producción) → riesgo de divergir.

### Riesgos + mitigación
- **Dashboard/API expuestos**: en junio 2026 escáneres entraron a dashboards de Hermes sin auth y plantaron una backdoor SSH → dashboard solo en `127.0.0.1`, puerto 8642 únicamente por tailnet, auth básica siempre activa, secretos en `.env` con permisos 600 fuera de git.
- **Doble memoria**: el vault es la verdad, `memories/` de Hermes es scratch, y toda escritura pasa por el MCP del vault con aprobación → una sola trazabilidad.
- **Gateway y cron desatendidos**: el gateway de Hermes trae *tool-loop hard stops* para sesiones no interactivas → se conservan por defecto y las tareas nivel C/D siguen exigiendo aprobación humana.

## Trazabilidad

- spec: [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]] §2.2 y §2.8 · [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec-mvp_07]] §6
- wiki: [[wiki/glosario/software/opencode|opencode]] · [[wiki/glosario/software/n8n|n8n]]
- research: [[raw/research/2026-10-28-runpod-auditoria-pi|auditoría Runpod 2026-10-28]] (contexto de infraestructura cloud)
- fuente: `raw/docs/plan-hermes.md` §4 y §18
