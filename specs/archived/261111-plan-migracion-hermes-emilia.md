---
tipo: plan
fecha_creacion: 2026-11-11
ultima_actualizacion: 2026-11-11
tags: [hermes, migracion, setup, emilia, antigravity, config, dos-bancos]
idioma: es
---

# Plan de migración a Hermes — setup, configuración y convivencia con Antigravity

> Responde: ¿cómo se configura Hermes?, ¿qué migra y en qué orden?, ¿sigo trabajando en Antigravity?
> Fuente canónica de configuración: [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#13. Configuración propuesta (config.yaml del estudio)|IMPLEMENTACION §13]] + [[proyectos/MVP_07-studio-os-sistema/IMPLEMENTACION-HERMES#2. Las cinco piezas que hay que configurar|§2 las cinco piezas]]. Alcance de la entrega: [[specs/261111-dos-caminos-emilia-35d-sistema-completo|dos caminos]].

## 0 · La respuesta corta: dos bancos de trabajo, para siempre

| | **Antigravity + OpenCode** (N3, esta PC) | **Hermes** (N1, VPS) |
|---|---|---|
| Qué es | tu **taller**: pruebas, diseño, desarrollo, vault, ComfyUI, Rhino | el **sistema entregado**: opera 24/7 para Emilia y el estudio |
| Quién lo usa | vos, ahora y siempre | Emilia, el junior futuro, vos de celular |
| Relación | construye y prueba las skills, el `config.yaml`, los flujos | **ejecuta** esas mismas piezas en producción |
| Se apaga si | nunca | nunca (ese es el punto) |

**Sí seguís trabajando en Antigravity.** Hermes llega para ser el agente de cara al cliente (decisión [[proyectos/MVP_07-studio-os-sistema/VISION#6.9 Las decisiones ya tomadas|VISION §6.9]]). Las skills que pruebes acá se copian al VPS; los flujos n8n ya son compartidos. Nada se deja de hacer acá: lo que acá probás y apruebas con `s`, viaja al VPS. La migración **solo mueve piezas maduras**, en esta secuencia:

## 1 · Qué se configura en Hermes (las 5 piezas + 3 nuevas)

### 1.1 Instalación base (S1, día 1-2)

```text
1. VPS Contabo (ya tenés n8n/Leantime ahí) → volumen EasyPanel para /opt/data
2. Imagen oficial nousresearch/hermes-agent → gateway run
   · 3 GB RAM / 2 vCPU (el VPS tiene 8 GB y 7 servicios más)
   · cero puertos publicados: Telegram long-polling sale, no entra
3. Bot Telegram NUEVO (@hermes_pitau_bot vía BotFather) — no toca emiliaospi_bot
4. Modelo: OpenCode Go (ya paga) → después perfil Ollama en el estudio
```

### 1.2 `config.yaml` (adaptado a la entrega Emilia)

```yaml
terminal:
  backend: docker
  docker_image: "nousresearch/hermes-sandbox:desktop"
  container_cpu: 2
  container_memory: 3072
  container_persistent: true

approvals:
  mode: manual            # nivel manual desde el día uno
  cron_mode: deny         # los cron no preguntan
  deny: ["git push --force*", "docker compose down*", "*rm -rf*"]

memory:
  memory_enabled: true
  user_profile_enabled: true
  write_approval: true

skills:
  write_approval: true
  create_dir: /opt/data/vault/skills
  external_dirs:
    - /opt/data/vault/.agents/skills

curator:
  enabled: true
  interval_hours: 168
  stale_after_days: 14
  backup: {enabled: true, keep: 2}

cron:
  max_parallel_jobs: 2

mcp_servers:
  n8n:
    url: "https://n8n.pitau.tech/mcp-server/http"
    headers: {Authorization: "Bearer ${N8N_MCP_TOKEN}"}   # secreto en ~/.hermes/.env
    trust: untrusted
  vault:
    trust: untrusted        # lectura auto; escritura con aprobación
  dwg-worker:
    trust: untrusted        # auditoría ezdxf server-side (S3)
```

### 1.3 `SOUL.md` (identidad para Emilia)

Un archivo corto: quién es Hermes, tono rioplatense, idioma castellano, reglas de la casa (pide email antes de agendar, cita lo que entendió, jamás inventa disponibilidad, todo cambio deja registro, materiales con nivel C-D piden aprobación).

### 1.4 Skills (S1-S3, 7 para el mes)

| Skill | Semana | Fuente |
|---|---|---|
| `gestionar-clientes` | S1 | VISION §6.3 |
| `preparar-compromisos` | S1 | idem |
| `redactar-correo-cliente` | S1 | idem |
| `minuta-reunion` | S2 | audio → STT → resumen con tipo interno/cliente → mail borrador |
| `rendir-con-indicacion` | S3 | render + texto/marca → variantes con semilla |
| `auditar-documentacion-cad` | S3 | dwg-worker ezdxf → informe |
| `computar-partidas` | S3 | bloques con atributos → tabla cómputo |

Cada skill se escribe primero en el vault (Antigravity), se prueba acá con OpenCode, y recién aprobada viaja a `/opt/data/vault/skills/`.

### 1.5 Cron + webhooks (S2)

* Cron 07:00: digest del día + recordatorios de compromisos vencidos
* Webhook n8n: al terminar STT/minuta, dispara a Hermes el armado del borrador

## 2 · Plan de migración semana a semana (35 días)

| Semana | Se migra a Hermes | Queda en Antigravity (tu taller) | Gate |
|---|---|---|---|
| **S1** | instalación base + bot nuevo + MCP n8n + 3 skills relación-cliente | redacción de SOUL.md y skills en el vault | Emilia agenda 1 reunión |
| **S2** | skill minuta + cron + webhook STT | prueba del flujo minuta en MVP_06 como comparación | 2 minutas reales ≤24h |
| **S3** | skills render + audit + cómputo; dwg-worker en VPS | pruebas Comfy local y prototipo ezdxf acá | 1 DWG real auditado |
| **S4** | portal de iteraciones + impresión PDF + pulido | demo ensayada, presentación | demo punta a punta |
| **+5d** | ensayos e imprevistos | — | presentación Emilia |

**Regla de migración**: una pieza viaja al VPS cuando (a) pasó su prueba acá, (b) su dueño humano la aprobó con `s`, (c) tiene rollback (MVP_06 vivo para agenda/minuta; Fathom vivo para reuniones Meet).

## 3 · Qué NO migra (queda acá por diseño)

* ComfyUI RX 570 — banco de pruebas de workflows (el render de Emilia va por API)
* Rhino/AutoCAD — capa operador, en la PC que lo usa
* El vault de desarrollo — Hermes recibe su espejo canónico en el VPS
* OpenCode/Antigravity — tu herramienta de desarrollo, según [[proyectos/MVP_07-studio-os-sistema/VISION#4.5 Por qué Hermes y no otras opciones|VISION §4.5]]

## 4 · Ejecución HITL

Cada paso de instalación y cada script nuevo se entrega como: comando exacto para tu terminal + archivo didáctico (`scripts/<slug>.py` + `_explicado.py` con nota línea a línea). Sin tu `s` no hay ejecución ([[AGENTS.md|regla del vault]]). Primer comando de la S1 propuesto:

```text
Paso 1.1 — bot Telegram nuevo:
  BotFather → /newbot → nombre "Hermes Pitau" → usuario @hermes_pitau_bot
  → guardar token en el gestor de secretos (nunca en el repo)

Paso 1.2 — volumen + imagen (EasyPanel, VPS):
  servicio nuevo hermes · imagen nousresearch/hermes-agent · volumen /opt/data
  · límites 3GB/2vCPU · 0 puertos · comando gateway run

¿Avanzo? s/N — con s, sigo con el checklist completo de S1 comando por comando.
```

## 5 · Qué NO decide este documento

* Elección de VPS adicional (Contabo actual alcanza; si no, se cotiza en S2)
* DPA y condiciones del render API (Pollinations vs Runpod) — decisión con la primera corrida real
* Cuándo Emilia firma su fase M4 — gate de la demo
