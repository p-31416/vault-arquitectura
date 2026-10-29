---
tipo: adr
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: aceptada
tags: [adr, mvp_07, studio-os, vault, git, vps, tailscale, sincronizacion]
idioma: es
---

# ADR-2026-10-28-vault-canónico-en-vps: El vault tiene su remoto canónico en el VPS y GitHub queda como espejo

**Fecha**: 2026-10-28
**Estado**: aceptada
**Deciden**: SOL
**Proyecto**: [[proyectos/MVP_07-studio-os-sistema/readme-mvp_07|MVP_07 Studio OS]]

## Contexto

El vault es un repo git privado (`https://github.com/p-31416/vault-arquitectura`, rama `master`) que hoy vive en la PC de desarrollo (`P:`). El agente —Hermes— va a vivir en el VPS y necesita leer y escribir el vault; el estudio necesita seguir trabajando en él. El vault tiene reglas propias: `log.md` es append-only, `raw/sessions/` es inmutable, `/activos/` (binarios) está gitignored y los `.md` solo referencian rutas de binarios. "Lo colgamos en GitHub" era el estado anterior; la pregunta es dónde queda el **canónico**.

## Decisión

El **VPS es el remoto canónico**: repositorio git bare + clon de trabajo, y el PC del estudio trabaja contra ese remoto por SSH sobre la red privada. **GitHub privado queda como espejo de respaldo y canal de emergencia** (y como vía alternativa si la PC del estudio no puede alcanzar el VPS). La sincronización es por `git fetch/pull` y `push` programados, con los hooks del vault respetados: append-only en logs, nada de binarios, escrituras del agente solo con aprobación.

## Alternativas

### GitHub como remoto canónico (estado actual)
- Pros: ya está andando, el estudio puede acceder desde cualquier red, backup fuera de casa.
- Contras: el VPS queda atado a un servicio externo y a internet para poder leer el vault; sin resolución de nombres propia; y es el punto único de falla para el agente.

### Sincronización por Drive (el vault como archivo compartido)
- Pros: multi-dispositivo sin operación, la misma carpeta que ya usan los binarios.
- Contras: sin diffs, sin atomicidad y sin historial: dos escrituras simultáneas se pisan, y el append-only de `log.md` quedaría sin garantía.

### Vault solo en la PC del estudio, leído por MCP remoto
- Pros: una sola copia, cero duplicados, cero operación de git.
- Contras: el agente deja de poder leer el vault cuando la PC está apagada, que es justo el caso que motivó los perfiles de ejecución.

## Consecuencias

### Positivas
- El agente funciona aunque todas las PCs estén apagadas: el VPS tiene su copia y su remoto.
- Una sola verdad con historia completa: git, append-only y hashes.
- El estudio sigue teniendo una vía de acceso simple (GitHub) si algo falla en la red privada.

### Negativas
- Hay que operar el repositorio bare y la sincronización: un trabajo de infraestructura nuevo.
- El acceso del estudio pasa a depender de la red privada (SSH sobre tailnet) → hay que verificar que la PC del estudio puede hablar con el VPS y, si no, documentar el camino GitHub como alternativa.

### Riesgos + mitigación
- **Divergencia entre clones**: sync con conflictos detectados de forma explícita (nada de `reset --hard` automático) y el vault nunca se "repara" a mano sin dejar rastro.
- **Pérdida de trazabilidad por force-push**: se prohíben force-push y reescrituras de historia; el append-only se verifica con el hook de `log.md`.
- **Datos sensibles en el repo**: los binarios no entran (gitignore) y el mandato de PI aplica igual: lo que no puede estar en el Drive del estudio tampoco entra al repo.

## Trazabilidad

- spec: [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]] §2.9 · [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec-mvp_07]] §7
- wiki: [[wiki/glosario/software/git|git]] · [[wiki/estudio/adrs/ADR-INFRA-001-leantime-selfhosted|ADR-INFRA-001]] (acceso remoto por Tailscale)
- sesión: [[raw/sessions/2026-10-28-sesion-delinear-pitauos|sesión 2026-10-28]]
