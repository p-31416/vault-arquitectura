---
tipo: adr
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: aceptada
tags: [adr, mvp_07, studio-os, ejecucion, perfiles, cloud, rhino-compute, twinmotion]
idioma: es
---

# ADR-2026-10-28-perfiles-de-ejecucion: Tres perfiles de ejecución y el contrato no distingue entre ellos

**Fecha**: 2026-10-28
**Estado**: aceptada
**Deciden**: SOL
**Proyecto**: [[proyectos/MVP_07-studio-os-sistema/readme-mvp_07|MVP_07 Studio OS]]

## Contexto

La PC del estudio va a estar apagada con frecuencia, así que no puede ser el servidor del sistema. Hechos verificados el 2026-10-28: **Rhino.Compute** es un servicio REST headless (Rhino y Grasshopper SDK, Windows y Linux, autohospedable o en Azure/AWS con billing por core-hour) y trae **Hops**, el componente headless oficial de Grasshopper en Rhino 8; **APS Design Automation** es la vía cloud oficial de AutoCAD, **pero no cubre AutoCAD LT** (el estudio tiene LT 2027 y el banco de pruebas la versión estudiantes); **Twinmotion no expone API pública**; ComfyUI ya vive en Runpod.

## Decisión

El sistema tiene **tres perfiles de ejecución** y el contrato **no distingue entre ellos**: lo único que cambia es el perfil (herramienta, operación, datos permitidos, costo).

| Perfil | Qué ejecuta | Dónde | Condición |
|---|---|---|---|
| **C1 · Nube oficial** | AutoCAD (scripts/LISP/.NET), Rhino + Grasshopper | APS Design Automation; Rhino.Compute + Hops | licencia AutoCAD **completa**; licencia Rhino en el servidor |
| **C2 · Nube propia GPU** | ComfyUI 9B, LoRA, video | Runpod Secure | 5 condiciones de [[specs/ADR-2026-10-28-nodo-gpu-runpod-secure|ADR Runpod]] |
| **L · Local** | AutoCAD LT GUI, Rhino 8, Twinmotion, Unreal | PC del estudio | apps abiertas; la PC es recurso elástico (Wake-on-LAN / smart plug) |

La PC del estudio deja de ser servidor y pasa a ser **lugar de interacción humana** y **runner bajo demanda**.

## Alternativas

### Solo local (PC del estudio 24/7)
- Pros: PI máxima, sin costos cloud, sin cables.
- Contras: ruido y consumo en el estudio, la PC se degrada como estación de trabajo, y cualquier apagado deja el sistema sin ejecutor.

### Solo cloud
- Pros: el sistema funciona sin máquinas del estudio, escalable.
- Contras: exige AutoCAD completo (cambio de licencias), Rhino con licencia en servidor, y el material del estudio en la nube, contra el mandato de PI.

### Mini-servidor propio siempre encendido en el estudio
- Pros: PI local, ejecuciones nocturnas, sin cloud.
- Contras: hardware + licencias + mantenimiento propio, y el estudio tiene 2-4 personas: nadie va a mantener un servidor.

## Consecuencias

### Positivas
- El sistema no depende de una sola máquina ni de que alguien esté en el estudio.
- El trabajo pesado (9B, video) sale del estudio; el trabajo sensible nunca sale.
- El contrato único permite que mañana una tarea se ejecute en el perfil cloud sin tocar el agente.

### Negativas
- El camino cloud de AutoCAD **está bloqueado por licencia** mientras el estudio use LT → la vía cloud de AutoCAD queda para el cliente que compre AutoCAD completo.
- Cada perfil tiene sus límites y su forma de fallar: hay que aprenderlos y documentarlos.
- El perfil L requiere apps abiertas y un puente vivo (el de Rhino ya se cayó una vez) → watchdog obligatorio.

### Riesgos + mitigación
- **Fallo silencioso por runner caído**: el runner declara "no disponible" y la tarea queda con estado explícito, nunca con resultado inventado.
- **Costos que se disparan**: el pod GPU se apaga solo y la cola muestra el costo por ejecución; ningún trabajo pesado se lanza sin que el perfil esté declarado.
- **Mezcla de datos entre perfiles**: el perfil declara la clase de dato que admite; una tarea que pida material sensible a un perfil que no lo admite se rechaza antes de ejecutarse.

## Trazabilidad

- spec: [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]] §2.12 · [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec-mvp_07]] §3.1
- wiki: [[wiki/glosario/software/twinmotion|twinmotion]] · [[wiki/glosario/software/comfyui|comfyui]] · [[raw/research/2026-10-15-cad-abierto-mcp-opencode|research CAD abierto 2026-10-15]]
- fuente: `raw/docs/plan-hermes.md` §5, §6 y §9
