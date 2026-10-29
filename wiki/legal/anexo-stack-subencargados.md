---
tipo: legal
fecha_creacion: 2026-09-12
ultima_actualizacion: 2026-10-22
tags: [legal, stack, subencargados, studio-os, vps, contabo]
idioma: es
---

# Anexo Técnico — Stack, subencargados y niveles de privacidad

> Inventario firmado a la propuesta. Anexo del [[wiki/legal/contrato-servicios-studio-os|Contrato Marco]] y del [[wiki/legal/tratamiento-datos|DPA]].

## Inventario (quién aporta)

| Capa | Producto | Aporta | Datos que ve |
|---|---|---|---|
| VPS | Contabo VPS S 4vCPU/8GB (89.117.73.109) | PITAUTECH | n8n, MySQL, Postgres, Redis, Leantime, Chatwoot, Qdrant |
| Orquestación | n8n self-hosted (Docker Swarm / EasyPanel) | PITAUTECH | reunión → minuta → tareas |
| Kanban | Leantime 3.12 self-hosted (PHP 8.3.36, MySQL 9) | PITAUTECH | sprints, OKRs, responsables |
| Soporte | Chatwoot 4.12 self-hosted (Postgres + Redis) | PITAUTECH | mensajes de soporte |
| Memoria | Obsidian Vault | PITAUTECH instala | wiki, reuniones, decisiones |
| Modelos | OpenCode Zen/Muse Spark + ChatGPT (cliente) | Ambos | fragmentos vault como contexto |
| Gráfica | ComfyUI local | PC local | moodboards (sin transferencia) |
| Agenda | Cal.com + cuenta cliente | Ambos | mails, disponibilidad |
| Reuniones | Fathom + Google Meet | Cliente | audio, video, transcripción |
| Repo | GitHub privado | PITAUTECH | vault versionado |
| Monitoreo | UptimeRobot (externo, gratis) | PITAUTECH | estado HTTP de pitau.tech |

## Subencargados y países

Contabo (UE) · Fathom, Cal.com, Google, GitHub, OpenRouter/OpenAI (EEUU). Cambios con aviso + oposición 15 días.

## Niveles de privacidad

Estándar (nube EEUU con consentimiento) para operación general; sensible/local (ComfyUI, Ollama, sin transferencia) para fase conceptual o secreto profesional. Detalle técnico en [[wiki/estudio/decision-arquitectura-ia-privacidad|Arquitectura IA y privacidad]].
