---
tipo: adr
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: aceptada
tags: [adr, mvp_07, studio-os, mcp, tailscale, runner, puente]
idioma: es
---

# ADR-2026-10-28-puente-mcp-p1-p3: Las herramientas de la PC se publican al VPS por proxy MCP y API de tareas

**Fecha**: 2026-10-28
**Estado**: aceptada
**Deciden**: SOL
**Proyecto**: [[proyectos/MVP_07-studio-os-sistema/readme-mvp_07|MVP_07 Studio OS]]

## Contexto

AutoCAD, Rhino y ComfyUI se manejan hoy con servidores MCP **stdio** declarados en `opencode.json` (`autocad`, `rhino`, `comfyui`), que corren en la misma máquina que el agente. Con Hermes en el VPS, esos servidores quedan al otro lado de la red: no se los ve. Además las operaciones de escritura (publicar un PDF de planos, modificar un DWG) necesitan que las reglas de riesgo se apliquen **del lado que ejecuta**, no del lado del que pide.

## Decisión

Puente en dos piezas: **P1** = proxy que convierte los MCP stdio locales en endpoints **HTTP streamable** publicados en la red privada con nombre estable de MagicDNS, para lectura e inspección; **P3** = **runner propio con API de tareas** para las operaciones de escritura, donde vive el control de niveles A-D, la aprobación, la copia de seguridad y la reversión.

## Alternativas

### P2 · Túnel SSH inverso con port-forward por puerto
- Pros: sin proxy nuevo.
- Contras: frágil con varios puertos y con reconexiones; no aporta control de riesgo del lado de la ejecución.

### Solo P1 (proxy MCP para todo)
- Pros: una sola pieza, los MCP existentes no se tocan.
- Contras: las reglas de riesgo quedan en el cliente (quien llama), y un cliente malicioso o un prompt inyectado podría escribir sin pasar por la validación del runner.

### Solo P3 (runner propio que reimplementa las operaciones)
- Pros: control total del lado que ejecuta.
- Contras: hay que reimplementar cada capacidad y duplicar lo que ya hacen los MCP; más trabajo inicial sin ganancia al inicio.

## Consecuencias

### Positivas
- Los MCP existentes siguen intactos y con su código actual: `opencode.json` no cambia de semántica.
- Las reglas de riesgo quedan donde se ejecutan: el runner valida la entrada, aplica la política y devuelve resultado estructurado.
- El runner declara **"no disponible"** cuando la PC está apagada, en lugar de fallar en silencio.

### Negativas
- Dos piezas que mantener (proxy + runner) y un contrato que los dos deben respetar.
- El runner depende de que la PC esté encendida; se resuelve con perfiles cloud y despertar por Wake-on-LAN.

### Riesgos + mitigación
- **El puente Rhino ya se cayó una vez** (27/10: puerto 9876 sin listener, necesitó un comando manual dentro de Rhino) → el runner incluye watchdog: si el puerto no responde, lo reinicia o declara el perfil caído, y la tarea queda con estado explícito.
- **Inyección de prompt en herramientas de escritura** → el runner no acepta rutas ni comandos del modelo: solo refs de archivo resueltos contra el vault y operaciones enumeradas.
- **Superficie de red**: todo el puente vive en la red privada, sin puertos públicos nuevos.

## Trazabilidad

- spec: [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]] §2.3 y §2.4 · [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec-mvp_07]] §3 y §4
- wiki: [[wiki/glosario/software/opencode|opencode]] · [[proyectos/MVP_05-rhino-mcp/pbook-rhino-mcp|pbook Rhino MCP]]
- sesión: [[raw/sessions/2026-10-28-sesion-delinear-pitauos|sesión 2026-10-28]]
