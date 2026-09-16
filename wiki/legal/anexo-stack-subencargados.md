---
tipo: legal
fecha_creacion: 2026-09-12
ultima_actualizacion: 2026-09-12
tags: [legal, stack, subencargados, studio-os]
idioma: es
---

# Anexo Técnico — Stack, subencargados y niveles de privacidad

> Inventario firmado a la propuesta. Anexo del [[wiki/legal/contrato-servicios-studio-os|Contrato Marco]] y del [[wiki/legal/tratamiento-datos|DPA]].

## Inventario (quién aporta)

| Capa | Producto | Aporta | Datos que ve |
|---|---|---|---|
| VPS | Contabo 4vCPU/8GB | PITAUTECH | n8n, Postgres, Redis, Leantime |
| Orquestación | n8n self-hosted | PITAUTECH | reunión → minuta → tareas |
| Kanban | Leantime 1 asiento | PITAUTECH | sprints, OKRs, responsables |
| Memoria | Obsidian Vault | PITAUTECH instala | wiki, reuniones, decisiones |
| Modelos | OpenCode Zen/Muse Spark + ChatGPT (cliente) | Ambos | fragmentos vault como contexto |
| Gráfica | ComfyUI local | PC local | moodboards (sin transferencia) |
| Agenda | Cal.com + cuenta cliente | Ambos | mails, disponibilidad |
| Reuniones | Fathom + Google Meet | Cliente | audio, video, transcripción |
| Repo | GitHub privado | PITAUTECH | vault versionado |

## Subencargados y países

Contabo (UE) · Fathom, Cal.com, Google, GitHub, OpenRouter/OpenAI (EEUU). Cambios con aviso + oposición 15 días.

## Niveles de privacidad

Estándar (nube EEUU con consentimiento) para operación general; sensible/local (ComfyUI, Ollama, sin transferencia) para fase conceptual o secreto profesional. Detalle técnico en [[wiki/estudio/decision-arquitectura-ia-privacidad|Arquitectura IA y privacidad]].
