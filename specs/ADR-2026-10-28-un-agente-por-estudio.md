---
tipo: adr
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: aceptada
tags: [adr, mvp_07, studio-os, agente, permisos, producto]
idioma: es
---

# ADR-2026-10-28-un-agente-por-estudio: Un solo agente por estudio, con perfiles de operación

**Fecha**: 2026-10-28
**Estado**: aceptada
**Deciden**: SOL
**Proyecto**: [[proyectos/MVP_07-studio-os-sistema/readme-mvp_07|MVP_07 Studio OS]]

## Contexto

El relevamiento del estudio (30 respuestas del 27/08) describe un equipo de 2-4 personas con decisión parcial: los juniors tienen autonomía en tareas definidas y la titular valida las decisiones arquitectónicas. Hoy la arquitectura en n8n rutea por `chat_id` con un flujo por persona (Sol y Emilia tienen el suyo, con credenciales propias). Como producto, Studio OS se vende a estudios de ese tamaño, y la pregunta es si el agente se replica por persona o si es uno con permisos.

## Decisión

**Un agente por estudio**, con la memoria y los permisos del estudio. El operador (Sol, de PITAUTECH) entra con un **perfil de administración** separado — es una identidad del mismo agente, no otro agente del estudio. La trazabilidad de "quién pidió qué" la resuelve el registro, no la multiplicación de agentes.

## Alternativas

### Un agente por persona (como el diseño actual de n8n)
- Pros: aislamiento fino de credenciales y contexto; ya es el patrón que anda en producción con Emilia.
- Contras: multiplica la configuración, el costo y la superficie de mantenimiento por cada persona; el estudio chico no lo aprovecha y el producto se vuelve caro de sostener.

### Multi-estudio (un agente que atiende a varios estudios)
- Pros: escala para un producto con varios clientes.
- Contras: mezcla datos entre estudios y choca con el mandato de PI; además el producto todavía se está validando con un piloto.

## Consecuencias

### Positivas
- Simple de vender, instalar y sostener: una instalación, una memoria, un costo.
- La memoria del estudio se enriquece con el uso colectivo (más contexto para el agente).
- El aislamiento real se garantiza por permisos y registro, que son controles explícitos y auditables.

### Negativas
- Se pierde el aislamiento fino del diseño "un flujo por persona" que hoy funciona en n8n: dos personas comparten el mismo agente.
- La configuración de credenciales sensibles por persona se resuelve con permisos, no con instancias separadas.

### Riesgos + mitigación
- **Confusión entre personas**: el registro guarda `requested_by` y el chat de origen de cada tarea; las aprobaciones quedan atribuidas.
- **Que un agente con muchos permisos sea un blanco amplio**: los niveles de riesgo y el runner limitan qué se puede hacer; el agente no tiene acceso directo a bases ni a binarios.
- **Perfil de Sol como backdoor de aprobación**: el perfil administrativo tiene acciones que el del estudio no, y esas acciones quedan en el registro.

## Trazabilidad

- spec: [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]] §2.8 · [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec-mvp_07]] §6
- wiki: [[wiki/glosario/software/leantime|leantime]] (patrón de permisos por rol) · [[proyectos/STUDIO_OS-Emilia/03-cuestionario-plan-studio-os|03-cuestionario-plan-studio-os]] (B5)
- sesión: [[raw/sessions/2026-10-28-sesion-delinear-pitauos|sesión 2026-10-28]]
