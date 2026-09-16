# Sesión 2026-09-07 — Vault Cerbero + Brain Emilia (SDD + GitHub Actions)

> Raw verbatim — cierre de sesión obligatorio según AGENTS.md

## Qué se hizo

- Investigación uso de IA en estudios internacionales (BIG, Foster, ZHA, OMA, Gensler) para propuesta comercial AR — sesión @brainstormy Double Diamond con 22 ideas, matriz Impacto×Esfuerzo, Top 3 con JTBD y wildcards
- Segunda sesión @brainstormy creativa para elevar vara: reframe Atelier Autómata — 30 días sin papel, paquetes Mate Cocido / Asado Completo / Fernet con Bica, pricing disruptivo y demo wow con peor foto de obra
- Definición de principios operativos: lenguaje en positivo (evitar "no"), creatividad con orden para liberar investigación/prueba/duda, procesos con calidad verificada + mejora semanal via MVPs
- Diseño del plan 1 mes: Vault vivo alimentado por ChatGPT + Antigravity + agente, Fathom MCP → raw → wiki/fuentes con extracción de necesidades en portugués, conectado al tiempo optimizado (14 hs netas semanales ≈ 18.5 hs elapsed, 16 pomodoros/día intenso, 100 USD por presencial quincenal)
- Pivot a arranque por AutoCAD (rótulos, standards, forma de trabajo) por impacto inmediato y bajo requerimiento de PC, con wiki por activo y caso conjunto de viviendas para academia
- Consolidación del plan en `specs/260907-vault_cerbero.md` con desglose horario por semana (210+210+390 USD), anclaje de valor 800–1200 USD y early bird bonificado como caso de éxito
- Evaluación alternativa cowork → GitHub Actions (Cerebro en la Nube): VM gratuita + OpenCode + Telegram, con transición futura a cron en VPS
- Instalación de flujo SPEC FIRST: investigación de GitHub Spec Kit (133k stars, spec-kit 1.0.0), flujo spec → plan → tasks → implement → converge via opencode
- Creación de glosario SDD como conocimiento permanente con índice interactivo y sección "Cómo se aplica al vault" al principio
- Normalización de índices: todo `index.md` → `00-index.md` (36 archivos) + actualización de 40 wikilinks
- Estructuración proyecto `260907-brain_emilia` como carpeta fecha+brain_emilia, sin duplicar planes (planes solo en /specs, link via wikilinks)

## Archivos modificados

- `specs/260907-vault_cerbero.md` — Plan Vault Cerbero (creado, luego renombrado a 260907-vault_cerbero con snake_case)
- `proyectos/260907-brain_emilia/00-index.md` — ficha proyecto Brain Emilia (creado, link a [[specs/260907-vault_cerbero]])
- `proyectos/260907-brain_emilia/documentacion/` — carpeta creada
- `proyectos/260907-brain_emilia/workflows/` — carpeta creada
- `proyectos/260907-brain_emilia/apps/` — carpeta creada
- `proyectos/260907-brain_emilia/agentes/` — carpeta creada
- `proyectos/260907-brain_emilia/reuniones/` — carpeta creada
- `proyectos/00-index.md` — índice actualizado con entrada 260907-brain_emilia
- `wiki/glosario/conceptos/sdd-spec_driven_development.md` — concepto SDD con índice interactivo + §1 Cómo se aplica al vault
- `wiki/glosario/entidades/sdd-spec_driven_development.md` — entidad SDD (registry)
- `wiki/glosario/conceptos/00-index.md` — agregado sdd-spec_driven_development
- `wiki/glosario/entidades/00-index.md` — agregado sdd-spec_driven_development
- `wiki/glosario/00-index.md` — actualizado
- `00-index.md` (raíz), `wiki/00-index.md`, `wiki/estandares/00-index.md`, `wiki/estandares/tecnico/00-index.md`, `wiki/estudio/00-index.md`, `wiki/software/00-index.md`, `proyectos/00-index.md`, etc. — 36 renombres index.md → 00-index.md
- `plan.md` (raíz) — Plan Vault Cerbero espejo (previo a mover a specs)
- `.github/workflows/opencode-vault.yml` — creado y luego retirado por SPEC FIRST (eliminado)
- `log.md` — entradas 2026-09-07 SDD y 2026-09-07 Proyecto 260907-brain_emilia
- `AGENTS.md` — actualizado indirectamente via renombres (refs a 00-index)

## Análisis cerebro digital (Karpathy)

### Topics candidatos a `wiki/glosario/software/`

- `opencode` — uso de opencode + antigravity + OPENCODE_ZEN tier gratuito, slash commands /speckit.* via opencode integration (specify init --integration opencode)
- `fathom` — MCP de Fathom para transcripción y extracción de necesidades, con conexión a raw/ y schedule cowork/GitHub Actions
- `github-actions` — workflow .github/workflows/opencode-vault.yml con cron 0 12 * * 1-5 (09:00 ART), modelo openai/gpt-4o (cuenta Emilia), envío a Telegram
- `antigravity` — IDE de agentes, comparación con Codex, uso con MCPs
- `autocad` — rótulos dinámicos, layers, DWT, bloques dinámicos para cómputo, con wiki por activo
- `comfyui` — ControlNet Canny para posproducción AutoCAD, futuro Lora y RunPod
- `spec-kit` — toolkit spec-driven (github/spec-kit) con flujo constitution → specify → clarify → plan → tasks → implement → converge

### Entidades

- **Personas:** Sol (arquitecta + consultora IA, gestora vault), Emilia (cliente, co-creadora Brain Emilia, puente desde otro rubro con conocimiento arquitectónico profundo), equipo estudios early bird (2 estudios, uno tester por reciprocidad, Lidia como sociedad inmobiliaria)
- **Clientes/Proyectos:** 260907-brain_emilia (Vault Cerbero), STUDIO_OS-Emilia (sprint USD 600), Lidia (inmobiliaria en testers/early birds), gestoría (<5 hs/mes), academia de arquitectura digital (en construcción)
- **Herramientas/Modelos:** OpenAI (cuenta Emilia, gpt-4o), OpenCode Zen (free tier), Fathom, Antigravity, Codex, GitHub Actions, Telegram Bot, Vault Cerbero, ComfyUI (architecturerealmix_v11 2.1GB SD1.5, Juggernaut-XL 7.11GB SDXL, ControlNet Canny/Depth 689MB), RunPod, n8n (descartado para Telegram directo)

### Hechos/decisiones — reutilizable vs efímero

**Reutilizable (queda en wiki/proyectos):**
- SDD como metodología permanente del vault: SPEC FIRST, specs solo en /specs con YYMMDD_snake, proyectos solo con workflows/apps/docu, link via wikilinks
- Vault Cerbero como CDE liviano con trazabilidad: ChatGPT + Antigravity → vault + wiki, Fathom → raw → wiki/fuentes (portugués), schedule cowork / GitHub Actions → Telegram
- Principio "creatividad con orden libera investigación/prueba/duda" + lenguaje en positivo + mejora semanal via MVPs con métricas (horas liberadas, victorias en log.md)
- Anclaje de valor 800–1200 USD mes con early bird 200+100 + 15 USD/h como caso de éxito para academia
- Flujo híbrido Spec Kit + template liviano via opencode, documentado en sdd-spec_driven_development con referencias verificadas

**Efímero (infra de esta sesión):**
- Workflow GitHub Actions prematuro (creado y retirado), cron tentativo 09:00 ART, modelo tentativo gpt-4o — pendiente de spec formal 260907-github_actions_cerbero_spec.md
- Estimaciones horarias de 14 hs netas/semana y equivalencia 1 día focalizado = 2 días oficina — a validar con relevamiento miércoles
- Propuestas de packaging (Atelier Autómata, Mate Cocido etc.) — chispas divergentes, no plan final
