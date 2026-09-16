---
tipo: decision
fecha_creacion: 2026-07-17
ultima_actualizacion: 2026-07-17
tags: [adr, comfyui, mcp, ia, generacion, imagenes, video]
estado: aceptada
---

# ADR-001: Integración de ComfyUI vía MCP local

## Contexto

El estudio necesita integrar generación de imágenes, video y audio por IA en el flujo de trabajo del equipo (4-5 personas: arquitectos, diseñadores, visualizadores). El vault utiliza Opencode como asistente, y queremos que el agente pueda:

- Generar renders conceptuales desde descripciones textuales
- Iterar sobre variantes de diseño (materiales, iluminación, entorno)
- Integrarse con flujos BIM y de documentación existentes
- Operar sin depender de conexión a internet para tareas críticas

ComfyUI es el motor de generación elegido por ser open source, modular, con el ecosistema más amplio de modelos y nodes. Necesitamos exponerlo como MCP server para que Opencode (y potencialmente otros agentes) pueda controlarlo.

## Opciones evaluadas

### 1. Comfy Cloud MCP (oficial, hosted)

| Aspecto | Detalle |
|---|---|
| **URL** | `https://cloud.comfy.org/mcp` |
| **Infra** | Cloud GPUs (NVIDIA RTX 6000 Pro). Sin GPU local |
| **Planes** | Free (limitado), Standard ($20/mes, 4.200 créditos), Creator ($35/mes), Pro ($100/mes), Enterprise (cotización) |
| **Costo estimado equipo** | $100/mes (5 x Standard) + créditos por GPU time + Partner Nodes |
| **Enterprise** | Sin precio público. Requiere contactar ventas. Annual commitments, volume pricing, Slack support, SSO, audit logs |
| **IP** | No entrena con datos de usuario. Inputs/outputs/workflows privados por cuenta |
| **Offline** | No |
| **Fuente** | [comfy.org/cloud/pricing](https://comfy.org/cloud/pricing), [docs.comfy.org/agent-tools/cloud](https://docs.comfy.org/agent-tools/cloud) |

**Problemas identificados:**
- Costo fijo mensual por persona + créditos consumibles. Para un equipo sin presupuesto dedicado de rendering, es desperdiciar plata — $100/mo base antes de generar nada.
- Enterprise no tiene precio transparente; seguramente requiere commitment anual.
- Dependencia de internet y de infraestructura de terceros.
- Los modelos Partner Nodes (Flux, Kling, Seedance, etc.) tienen costo adicional en créditos.

### 2. Comfy Local MCP (oficial, no disponible)

| Aspecto | Detalle |
|---|---|
| **Estado** | Private test — no disponible públicamente |
| **Requiere** | ComfyUI local + comfy-cli |
| **GPU** | Local |
| **Fuente** | [docs.comfy.org/agent-tools](https://docs.comfy.org/agent-tools) |

**Problemas identificados:**
- No disponible. Sin fecha de release público.

### 3. MCPs comunitarios

#### 3a. artokun/comfyui-mcp â­ SELECCIONADO

| Aspecto | Detalle |
|---|---|
| **Stack** | Node.js ≥22, npm package |
| **Transport** | stdio / streamable-HTTP |
| **Tools** | 108: image gen, audio gen, workflow composition/validation/viz, model search (HF/CivitAI), VRAM mgmt, custom node discovery, process control, diagnostics, generation tracker (SQLite) |
| **Skills** | 32 built-in (Flux, WAN, LTX 2.3, Qwen, Ideogram 4, etc.) |
| **Extras** | Claude Code plugin, Agent Panel sidebar (Claude/ChatGPT/Gemini/Ollama), tunnel mode, RunPod one-click, modo compact para LLMs chicos |
| **Licencia** | MIT |
| **Stars** | ~400 |
| **Instalación** | `npx -y comfyui-mcp` — sin clone. Auto-detecta ComfyUI |
| **Fuente** | [github.com/artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) — [docs](https://comfyui-mcp.artokun.io/docs) |

#### 3b. shawnrushefsky/comfyui-mcp

| Aspecto | Detalle |
|---|---|
| **Stack** | Docker / Node.js |
| **Tools** | 70+ templates, `build_node`, task/queue mgmt, agent memory persistente, SVG rendering |
| **Limitación** | Requiere Docker, templates pre-definidos, sin process control |
| **Fuente** | [github.com/shawnrushefsky/comfyui-mcp](https://github.com/shawnrushefsky/comfyui-mcp) |

#### 3c. joenorton/comfyui-mcp-server

| Aspecto | Detalle |
|---|---|
| **Stack** | Python ≥3.8, streamable-HTTP |
| **Tools** | `generate_image`, `generate_song`, `regenerate`, `view_image`, job/queue mgmt, asset browsing |
| **Limitación** | Assets efímeros, sin model mgmt, sin custom nodes, sin process control |
| **Fuente** | [github.com/joenorton/comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server) |

#### 3d. lalanikarim/comfy-mcp-server

| Aspecto | Detalle |
|---|---|
| **Stack** | Python (FastMCP + uv) |
| **Tools** | Solo 2: `generate_image` y `generate_prompt` |
| **Limitación** | Single workflow fijo, remote-only, config manual de node IDs |
| **Fuente** | [github.com/lalanikarim/comfy-mcp-server](https://github.com/lalanikarim/comfy-mcp-server) |

## Criterios de decisión

1. **Costo**: Gratis. El estudio no tiene presupuesto de rendering mensual.
2. **Control de datos**: La data nunca debe salir de la infraestructura local.
3. **Completitud funcional**: Debe exponer herramientas suficientes para que el agente opere ComfyUI autónomamente.
4. **Madurez**: Comunidad activa, documentación, stars, actualizaciones frecuentes.
5. **Instalación**: Simple, preferentemente sin Docker.
6. **Compatibilidad**: Debe funcionar con Opencode y potencialmente otros clientes MCP.

## Decisión

Se adopta **artokun/comfyui-mcp** como MCP server para ComfyUI local.

**Argumentos:**

1. **Completitud**: Es el MCP comunitario más completo (108 tools, 32 skills). No hay otro que se le acerque en capacidades.
2. **Local-first**: Corre contra ComfyUI local. Datos nunca salen de la infraestructura del estudio.
3. **Instalación cero**: `npx -y comfyui-mcp` — no requiere clonar repos, no requiere Docker. Auto-detecta la instalación de ComfyUI.
4. **Auto-detección**: Encuentra automáticamente el path y puerto de ComfyUI. Cero configuración manual.
5. **Modelos incluidos**: Trae skills pre-armadas para Flux, WAN, LTX 2.3, Qwen, SD, etc. El agente sabe qué sampler, CFG, resolución usar sin ensayo y error.
6. **Gestión de modelos**: Search en HF y CivitAI, download, listado local. No requiere salir del chat.
7. **Process control**: Puede arrancar, detener y reiniciar ComfyUI. Ideal para entornos compartidos.
8. **Licencia MIT**: Permisiva, sin restricciones comerciales.
9. **Comunidad activa**: ~400 stars, 645 commits, CI, changelog, roadmap.

## Propiedad intelectual y licencias de modelos

### Datos del estudio

Al correr ComfyUI localmente con `artokun/comfyui-mcp`:

- **Los prompts, imágenes generadas, workflows y LoRAs nunca salen de la infraestructura local**.
- Comfy Org no tiene acceso a los datos (no hay telemetría forzosa en local).
- Los archivos generados se almacenan en `activos/proyectos/` dentro del vault (referenciados desde markdown, nunca commiteados a git).

### Licencias de modelos (Hugging Face)

Cada modelo en Hugging Face tiene su propia licencia. Las más relevantes para generación de imágenes/arquitectura:

| Licencia | Uso comercial | Derivados (LoRA) | Atribución |
|---|---|---|---|
| **Apache 2.0** | Sí | Sí, sin restricciones | Requerida |
| **MIT** | Sí | Sí | Requerida |
| **CreativeML OpenRAIL-M** | Sí | Sí, con uso responsable | Requerida |
| **Stability AI Community License** | Sí (ingresos < $1M/año) | Sí, eres dueño del Derivative Work | Requerida + "Powered by Stability AI" |
| **SDXL License** | Sí | Sí | Requerida |
| **Flux (Black Forest Labs)** | Sí (licencia comercial) | Sí (check términos específicos) | Requerida |
| **Llama Community License** | Sí (< 700M MAU) | Sí, eres dueño del fine-tune | "Built with Llama" + naming |
| **CC BY-NC** | **No** | **No comercial** | Requerida |
| **Custom/propietaria** | Depende del contrato | Depende | Variable |

**Regla práctica para el estudio:**

> **Siempre verificar la licencia del modelo antes de usarlo comercialmente.** En Hugging Face está en el campo `license` de la model card. Si es Apache 2.0, MIT, OpenRAIL-M o SDXL, estamos cubiertos. Si es CC BY-NC, no usar para proyectos comerciales. Si es custom, leer el LICENSE file adjunto.

### LoRA: ¿De quién son los derechos?

Cuando entrenamos un LoRA (Low-Rank Adaptation) sobre un modelo base:

1. **Los pesos del LoRA son de nuestra autoría.** El adapter no existía antes de nuestro entrenamiento.
2. **Pero el sistema combinado (base + LoRA) hereda la licencia del modelo base.** Si el base es CC BY-NC, el LoRA + base restringido corre bajo esa misma licencia.
3. **Distribuir un LoRA públicamente activa las mismas obligaciones que distribuir el modelo fine-tuneado completo** — para Llama, Gemma, etc.
4. **Para uso interno** (no distribución): la mayoría de las licencias permiten fine-tuning y uso interno sin restricciones adicionales, siempre que se respeten las Acceptable Use Policies.
5. **Los outputs generados** (imágenes, renders) no son "distribución del modelo" sino uso del mismo. El ownership de los outputs lo define cada licencia — en Apache 2.0, MIT, OpenRAIL y SD Community License, el output te pertenece.

**Referencias:**
- [Hugging Face — Licencias en repositorios](https://huggingface.co/docs/hub/en/repositories-licenses)
- [WCR.Legal — Fine-tuned model license implications](https://wcr.legal/fine-tuned-model-license/)
- [Stability AI Community License](https://huggingface.co/stabilityai/stable-diffusion-3-medium/resolve/main/LICENSE.md)
- [Meta Llama 3.3 Community License](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/resolve/main/LICENSE)
- [The Neural Base — IP considerations for LoRA adapters](https://theneuralbase.com/lora-fundamentals/learn/advanced/ip-considerations-for-adapters/)

## Modelos instalados en el estudio (RX 570 8GB) — Licencias y uso comercial

| Modelo | Archivo | Tipo | Base | Licencia | Uso comercial | Entrenar LoRA |
|---|---|---|---|---|---|---|
| **ArchitectureRealMix v11** | `architecturerealmix_v11.safetensors` | Checkpoint | SD 1.5 | **CreativeML OpenRAIL-M** | ✅ Sí | ✅ Sí (hereda OpenRAIL-M) |
| **Juggernaut XL v9** | `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | Checkpoint | SDXL 1.0 | **CreativeML OpenRAIL++-M** | ✅ Sí | ✅ Sí (hereda OpenRAIL++-M) |
| **ControlNet Canny SD 1.5** | `control_v11p_sd15_canny.safetensors` | ControlNet | SD 1.5 | **Apache 2.0** | ✅ Sí | ✅ Sí |
| **ControlNet Depth SD 1.5 (FP16)** | `control_v11f1p_sd15_depth_fp16.safetensors` | ControlNet | SD 1.5 | **Apache 2.0** | ✅ Sí | ✅ Sí |

### Verificación de licencias (fuentes oficiales)

| Modelo | Fuente HF / CivitAI | Licencia confirmada |
|---|---|---|
| ArchitectureRealMix | [CivitAI model](https://civitai.com/models/131466/architecture-realmix) / [HF fork](https://huggingface.co/Lykon/ArchitectureRealMix) | CreativeML OpenRAIL-M |
| Juggernaut XL v9 | [CivitAI model](https://civitai.com/models/133005/juggernaut-xl) / [RunDiffusion](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9) | CreativeML OpenRAIL++-M |
| ControlNet SD 1.5 (Canny/Depth) | [lllyasviel/ControlNet-v1-1](https://huggingface.co/lllyasviel/ControlNet-v1-1) | Apache 2.0 |

> **Verificado**: Enlaces comprobados el 2026-07-24. Todos los modelos instalados son **seguros para uso comercial** en proyectos del estudio.

### Propiedad de outputs generados con ESTOS modelos

| Modelo | ¿El output (imagen/render) es tuyo? | ¿Puedes venderlo / entregarlo a cliente? |
|---|---|---|
| ArchitectureRealMix (OpenRAIL-M) | ✅ Sí | ✅ Sí |
| Juggernaut XL (OpenRAIL++-M) | ✅ Sí | ✅ Sí |
| ControlNets (Apache 2.0) | ✅ Sí | ✅ Sí |

**En todos los casos: los renders que generes para clientes son de tu propiedad y los puedes entregar/facturar sin restricciones de licencia del modelo.**

### Entrenamiento de LoRAs — ¿Sobre qué modelos podemos entrenar?

| Modelo base | ¿Podemos entrenar LoRA? | Licencia del LoRA resultante | ¿Podemos distribuir el LoRA? |
|---|---|---|---|
| **ArchitectureRealMix (SD 1.5)** | ✅ Sí | CreativeML OpenRAIL-M | ✅ Sí, con atribución + license notice |
| **Juggernaut XL (SDXL)** | ✅ Sí | CreativeML OpenRAIL++-M | ✅ Sí, con atribución + license notice |
| **SD 1.5 base (oficial)** | ✅ Sí | CreativeML OpenRAIL-M | ✅ Sí |
| **SDXL base (oficial)** | ✅ Sí | CreativeML OpenRAIL++-M | ✅ Sí |
| **Flux.1-dev** | ✅ Sí | Flux Dev License (comercial < $1M) | ✅ Sí, si cumple límites |
| **Stable Diffusion 3 Medium** | ⚠ï¸ Revisar | Stability Community License | ⚠ï¸ Solo si ingresos < $1M/año |

> **Recomendación para el estudio**: Entrenar LoRAs sobre **ArchitectureRealMix** (para arquitectura SD 1.5) o **Juggernaut XL** (para fotorrealismo SDXL). Ambos heredan licencias permisivas (OpenRAIL) que permiten uso comercial, derivados y distribución con atribución. Evitar bases con CC BY-NC o licencias restrictivas.

### Auditoría trimestral de modelos

- **Próxima revisión**: 2026-10-24
- **Qué revisar**: Que no haya cambiado la licencia en HF/CivitAI; que no se hayan añadido modelos CC BY-NC por error; validar nuevos modelos antes de instalarlos.

## Comparativa de costos (proyectada a 12 meses)

| Escenario | Costo mensual | Costo anual | GPU |
|---|---|---|---|
| **Cloud MCP — 5 personas Standard** | $100 + créditos | $1.200+ | Cloud RTX 6000 Pro |
| **Cloud MCP — Enterprise (5 seats)** | A cotizar | A cotizar | Cloud |
| **Local + artokun/comfyui-mcp** | $0 | $0 | Local (una GPU del estudio) |

**Conclusión económica:** Para un equipo de 4-5 personas sin demanda masiva ni presupuesto de rendering, la opción local ahorra $1.200+/año y evita vendor lock-in.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| artokun/comfyui-mcp es mantenido por una persona (artokun) | Código abierto (MIT). Si deja de mantenerse, migrar al Local MCP oficial cuando esté disponible, o mantener un fork |
| Node.js ≥22 required | Ya instalado en el equipo de desarrollo |
| 108 tools pueden abrumar modelos chicos | Modo `--compact` disponible. Opencode usa modelos grandes |
| GPU local puede ser insuficiente para video pesado | El estudio puede agregar GPU dedicada o usar RunPod para tareas puntuales manteniendo el mismo MCP |
| Licencias de modelos cambian | Auditoría trimestral de modelos instalados vs. licencias |

## Próximos pasos

1. Instalar artokun/comfyui-mcp en Opencode
2. Configurar ComfyUI local con modelos base (SDXL, Flux)
3. Agregar planilla de modelos aprobados para uso comercial
4. Documentar en wiki/glosario/software/comfyui.md el flujo completo
5. Evaluar migración al Comfy Local MCP oficial cuando esté disponible

## Referencias

- [artokun/comfyui-mcp — GitHub](https://github.com/artokun/comfyui-mcp)
- [artokun/comfyui-mcp — Documentación](https://comfyui-mcp.artokun.io/docs)
- [Comfy Cloud MCP — Docs oficiales](https://docs.comfy.org/agent-tools/cloud)
- [Comfy Cloud Pricing](https://comfy.org/cloud/pricing/)
- [Comfy Enterprise](https://comfy.org/cloud/enterprise/)
- [Comfy Local MCP (private test)](https://docs.comfy.org/agent-tools/local)
- [Comfy Desktop Privacy Policy](https://comfy.org/privacy/desktop/)
- [Hugging Face — Model Licenses](https://huggingface.co/docs/hub/en/repositories-licenses)
- [Comfy-Org/comfy-cli](https://github.com/Comfy-Org/comfy-cli)
