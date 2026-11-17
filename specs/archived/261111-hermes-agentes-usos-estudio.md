---
tipo: investigacion
fecha_creacion: 2026-11-11
ultima_actualizacion: 2026-11-11
tags: [hermes, perfiles, bots, subagentes, crew-ai, usos, estudio-arquitectura, comfyui, tailscale]
idioma: es
---

# Hermes — cómo son de verdad los agentes, usos de creadores y diseño para el estudio

> Responde la duda: ¿las "oficinas de agentes" son agentes separados? ¿Puede Hermes hacer la curaduría solo? ¿Cómo conecta ComfyUI (Tailscale o pod)? ¿Y el futuro del profesor (asistente por persona + wiki compartida)? Todo verificado contra doc oficial + casos de creadores.

## 1 · El modelo oficial de Hermes (verificado en docs)

| Primitiva | Qué es | Persiste | Cuándo usarla en el estudio |
|---|---|---|---|
| **Instancia** | el proceso Hermes corriendo | permanente | 1 por VPS del estudio |
| **Profile** | hogar aislado: config, `.env`, SOUL, memoria, sesiones, skills, cron, `state.db` — `hermes profile create <nombre>` | permanente | 1 por Bot del equipo |
| **Bot (Bot Mode)** | un perfil presentado como **integrante nombrado del equipo**: avatar, chat propio persistente, rutinas, skills y modelo propios. Se `@mencionan` entre sí; chats grupales de 2-6 Bots con deliberación | permanente | los "Pipi" del estudio |
| **Subagent** | hijo efímero que el agente genera con `delegate_task` para parte de UNA tarea, conversación fresca, puede correr en paralelo | una tarea | trabajo paralelo (comparar 5 variantes, auditar 3 DWG a la vez) |
| **Messaging bot** | la cuenta de Telegram/Discord conectada por gateway (token) | permanente | el bot del estudio, 1 token por perfil |

Fuentes verificadas hoy: `hermes-agent.nousresearch.com/docs/user-guide/profiles` · `/docs/user-guide/bot-mode` · `/docs/user-guide/features/delegation`.

**Respuesta a tu duda central**: las "oficinas de agentes" que viste (y probaste en Crew AI) en Hermes **existen de verdad** pero de dos formas distintas: **Bots** (especialistas duraderos, cada uno con memoria y skills propias, que se escriben entre sí) y **subagentes** (obreros temporales de una sola tarea). No son procesos separados del mismo Hermes corriendo a la ciega: son perfiles aislados que comparten el mismo runtime. Y hay regla dura de la doc: **dos procesos nunca apuntan al mismo perfil** — si dos agentes necesitan memoria compartida, la doc recomienda un **memory provider externo** (Hindsight, Honcho), que es justo el mecanismo del futuro multi-persona (§5).

## 2 · Casos de uso de creadores (verificados hoy)

| Caso real | Quién | Mapa al estudio |
|---|---|---|
| **Negocio de servicios end-to-end por Telegram**: llegan leads → salen presupuestos → el dueño aprueba → cobro | user-stories oficial | cliente → honorarios (MVP_03/03b) → aprobación → entrega |
| **Cola de investigación con aprobación en Telegram**: Hermes investiga, puntúa y prepara; el humano aprueba los que quiere y el sistema ejecuta el resto | user-stories | fuentes y referentes: propuesta → Sol/elige → ficha |
| **28 cron jobs, 30+ skills, job "Dreaming" 3AM** que lee todas las conversaciones del día y escribe el contexto de mañana | creador independiente | cron 07:00 digest + lint + "qué decidimos ayer" |
| **Briefing diario de investigación** a Discord/Slack/Notion/Obsidian | user-stories | digest de fuentes v2 + panel |
| **Temas privados de Telegram con skills distintas por tema** | user-stories | grupos por obra con su skill (auditoría en obra-A, cómputo en obra-B) |
| **Skills autocreadas recortan ~40% el tiempo de tareas de investigación** (benchmark TokenMix) | creador | el aprendizaje del sistema se mide: skill nueva = horas ahorradas |
| **Kanban agent swarm**: worker + verifier + synthesizer como tareas persistentes | awesome-hermes-usecases | Pipi PM: tarea → ejecuta → verifica → sintetiza al vault |
| **Obsidian second brain** con dashboard y knowledge conectado | awesome-hermes-usecases | exactamente nuestro Camino 2 |
| **Team assistant con sesiones por usuario + Docker** | starter oficial | Emilia + junior + vos, 1 bot, sesiones separadas |

Repositorio de referencia: `github.com/aliaihub/awesome-hermes-usecases` (60+ casos clasificados). Documento oficial de user-stories: `hermes-agent.nousresearch.com/docs/user-stories`.

## 3 · La oficina de agentes del estudio — diseño

```text
Hermes (1 instancia, VPS estudio)
│
├─ default (PI Manager) ── gateway Telegram del estudio
│    recibe a Emilia/Sol/junior, interpreta, delega, coordina
│
├─ Bot: pipi-docs ── curaduría y memoria
│    skills: analizar-fuente · curar-cuaderno · diagnosticar-proyecto
│    conecta: MCP vault + MCP Drive + web
│    cron: ingesta diaria de fuentes + lint
│
├─ Bot: pipi-pm ── agenda y compromisos
│    skills: gestionar-clientes · preparar-compromisos · redactar-correo
│    conecta: MCP n8n (Cal.com, STT, mail) · cron digest 07:00
│
├─ Bot: pipi-cad ── planos
│    skills: auditar-documentacion-cad · computar-partidas · comparar-versiones
│    conecta: MCP dwg-worker (ezdxf) · luego N2 AutoCAD por Tailscale
│
├─ Bot: pipi-visual ── imagen y render
│    skills: rendir-con-indicacion · experto-comfyui
│    conecta: MCP ComfyUI por Tailscale (N2 con GPU) O pod (si no alcanza) O API free
│
└─ Bot: pipi-ideas ── divergencia creativa (tu rol Brainstormy)
     modelo barato propio (Bot Mode permite pin de modelo por Bot)
     skill: brainstorm/SCAMPER — "seguir la corriente" con costo mínimo
```

**Sobre tu rol Brainstormy**: en producción, la divergencia es un Bot con **modelo barato fijado** (Bot Mode permite modelo por perfil) — "que me siga la corriente" sin gastar. En tu taller N3, OpenCode + Brainstormy sigue igual: ese es tu equipo de desarrollo, con sus 4 curadores.

**Sobre la curaduría sin Sherlock**: sí, Hermes la hace solo en producción. El pipeline curadores (buscar → ficha → destino → wiki) vive como **skills de pipi-docs**: web tools + MCP Drive + MCP vault + `analizar-fuente`. Los 4 curadores de N3 siguen siendo tu instrumento de desarrollo; en el VPS, pipi-docs ejecuta el mismo procedimiento escrito. Regla HITL sin cambios: toda escritura a wiki pide `s`.

## 4 · ComfyUI — las 3 rutas de conexión (análisis pedido)

| Ruta | Cómo | Cuándo conviene | Costo |
|---|---|---|---|
| **1 · Tailscale + N2 con GPU suficiente** | PC del estudio (o N3) corre ComfyUI con su MCP; el bot la alcanza por la red privada | si la máquina del estudio tiene GPU que aguanta el workflow (SD1.5/SDXL ok en 8 GB; FLUX.2 grande necesita más) | $0 infra, usa lo existente |
| **2 · Pod on-demand (Runpod Secure)** | pod con GPU grande levanta al pedir; material derivado no sensible | FLUX.2 9B, video por lote, consistencia alta | por hora de pod (excepción ya decidida en VISION §5) |
| **3 · API imagen free (Pollinations)** | HTTP directo desde n8n/Hermes | variantes rápidas tipo "cambiá el cielo" sin ControlNet fino | $0, calidad menor |

Decisión por tipo de pedido: variante simple → ruta 3 · workflow versionado con ControlNet/LoRA → ruta 1 si hay GPU, si no ruta 2 · siempre con semilla y log (`reglas-workflows-comfy`). El MCP de ComfyUI ya validado en N3 (`comfyui_comfy_cli`) es el mismo cliente en las 3 rutas: cambia el endpoint, el contrato queda — patrón de perfiles del master.

## 5 · El futuro del profesor — asistente por persona + wiki compartida

Tu profesor piensa: cada persona con su asistente sintético, todos alimentando un sistema más grande, wiki compartida, permisos simples al inicio. Hermes ya tiene las piezas oficiales para eso:

1. **Un perfil por persona** (`hermes profile create emilia --description "..."`) — cada uno con su memoria, su SOUL, sus skills — misma regla de la doc: cada perfil es un hogar aislado.
2. **Memoria compartida via memory provider externo** (Hindsight/Honcho) — la doc recomienda exactamente esto cuando varios agentes comparten conocimiento: la wiki del vault como provider narrativo + provider vectorial opcional.
3. **Profile distributions** (`hermes profile install github.com/estudio/asistente-base`) — el paquete del asistente (SOUL + skills + config) se distribuye como repo git versionado: vos construís el asistente base una vez y cada estudio/persona lo instala y actualiza. El producto Studio OS = esa distribución.
4. **Wiki compartida sin permisos complejos al inicio**: un vault, ramas por estudio, `s` humano como única puerta de escritura — la gobernanza A-D ya cubre el caso multi-instancia.

## 6 · Crew AI vs Hermes (tu experiencia previa)

Crew AI (que probaste) es un **framework externo de orquestación**: define roles/tareas/proceso como código, y cada rol es una llamada LLM sin memoria propia, sin cron, sin gateway, sin skills persistentes. Lo que te hizo volver a Crew AI es lo que Bot Mode + kanban + delegación ya traen nativos en Hermes, más memoria que mejora, cron, gateway multiplataforma y el vault. Conclusión: **no hace falta un framework aparte** — la oficina de agentes es una feature del mismo Hermes. La analogía probada por la comunidad: "Paperclip managed employees" (empleados coordinados por tareas, checkpoints y sesiones persistentes).

## 7 · Veredicto

Hermes es la mejor solución para el estudio y para el futuro multi-persona: misma plataforma para 1 asistente (piloto Emilia) y para N (profesor), con primitivas oficiales (perfiles/Bots/distribuciones/memory providers) que ya cubren el camino completo. El equipo Pipi se materializa como **Bots** — esto resuelve la inconsistencia I1 del plan maestro.

## Pendiente de tu decisión

I1: confirmar **Pipi = Bots Hermes** (propongo PI Manager default + pipi-docs y pipi-pm primero, pipi-cad/visual cuando sus skills existan, pipi-ideas con modelo barato). Quedan I2-I7 del mapa de unificación.
