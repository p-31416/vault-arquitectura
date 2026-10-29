---
tipo: spec
mvp: 07
cliente: Estudio (interno)
proyecto: Studio OS — sistema operativo para un estudio de arquitectura
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: activo
tags: [mvp_07, studio-os, spec, contrato, postgres, mcp, runner, hermes, runpod]
idioma: es
---

# MVP_07 — Studio OS · contratos técnicos

> Especificación del sistema que sostiene el diseño de [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]]. Acá va lo que se implementa: el sobre de tarea, el modelo de datos, las APIs, los perfiles de ejecución y la configuración del agente.
> Decisiones que lo justifican: [[specs/ADR-2026-10-28-registro-hibrido-postgres-vault|ADR registro]] · [[specs/ADR-2026-10-28-puente-mcp-p1-p3|ADR puente]] · [[specs/ADR-2026-10-28-perfiles-de-ejecucion|ADR perfiles]] · [[specs/ADR-2026-10-28-agente-hermes-en-vps|ADR agente]] · [[specs/ADR-2026-10-28-nodo-gpu-runpod-secure|ADR Runpod]]

- [[#1 · El sobre de tarea]]
- [[#2 · Modelo de datos]]
- [[#3 · Perfiles y selección de ejecutor]]
- [[#4 · API del runner]]
- [[#5 · Perfil de pod GPU]]
- [[#6 · Configuración del agente]]
- [[#7 · Vault: remoto canónico y sincronización]]
- [[#8 · Observabilidad y métricas]]

---

# 1 · El sobre de tarea

Un único esquema para toda herramienta del estudio. Los MCP existentes se adaptan a él; no se inventa un esquema por herramienta.

```json
{
  "task_id": "5f3c9d2e-1f4a-4c2b-9a77-2c9b6e5f0a11",
  "project": "aiz",
  "tool": "audit_dwg",
  "verbo": "inspect",
  "input": {
    "file_ref": "drive://AIZ/CAD-UY-xa-RHINO_02.dwg",
    "rules_ref": "audit-aiz-v2"
  },
  "riesgo": "A",
  "approval": "not_required",
  "requested_by": "hermes",
  "chat_ref": "telegram:-1001234567890:42",
  "idem_key": "audit:aiz:cad-u-y:2026-10-28",
  "created_at": "2026-10-28T02:40:00Z"
}
```

**Reglas de validación** (las rechaza el registro antes de ejecutar):

| Regla | Motivo |
|---|---|
| `file_ref` es obligatorio y **resuelve contra el vault** | el modelo nunca elige un archivo ni manda rutas |
| `verbo` ∈ `inspect · generate · modify · publish` | el verbo define el nivel de riesgo por defecto |
| `riesgo` ∈ `A · B · C · D` y no puede bajarse por debajo del verbo | un `publish` siempre es D |
| `approval` ∈ `not_required · pending · granted` | C y D nacen en `pending` |
| `idem_key` es único | reintentos no duplican trabajo |
| `input` validado por JSON Schema **de la herramienta** | cada tool define lo que acepta |

**Respuesta estructurada**:

```json
{
  "task_id": "5f3c9d2e-1f4a-4c2b-9a77-2c9b6e5f0a11",
  "status": "completed",
  "outputs": [
    { "tipo": "informe", "ref": "vault://proyectos/MVP_05-rhino-mcp/01-AIZ/docs/audit-2026-10-28.md" }
  ],
  "warnings": ["3 sheets sin escala de viewport definida"],
  "errors": [],
  "provenance": {
    "input_version": "aiz-cad-02@3",
    "tool": "audit_dwg",
    "tool_version": "0.2.0",
    "perfil": "banco",
    "runner": "banco-runner",
    "started_at": "2026-10-28T02:40:03Z",
    "completed_at": "2026-10-28T02:41:57Z",
    "duration_ms": 114000,
    "cost": 0
  }
}
```

---

# 2 · Modelo de datos

Postgres del VPS, schema `studio_os`. Escritor único: la API `registry`.

```sql
CREATE SCHEMA IF NOT EXISTS studio_os;

CREATE TABLE studio_os.proyecto (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  slug        text NOT NULL UNIQUE,
  nombre      text NOT NULL,
  cliente     text,
  estado      text NOT NULL DEFAULT 'activo',
  creado_en   timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE studio_os.archivo (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  proyecto_id uuid NOT NULL REFERENCES studio_os.proyecto(id),
  nombre      text NOT NULL,
  clase       text NOT NULL CHECK (clase IN
                ('plano_legal','calculo','material_cliente','concurso',
                 'render_ia','modelo','documento','otro')),
  ref         text NOT NULL,
  hash_sha256 text,
  bytes       bigint,
  creado_en   timestamptz NOT NULL DEFAULT now(),
  UNIQUE (proyecto_id, ref)
);

CREATE TABLE studio_os.version (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  archivo_id  uuid NOT NULL REFERENCES studio_os.archivo(id),
  etiqueta    text NOT NULL,
  hash_sha256 text NOT NULL,
  metadata    jsonb NOT NULL DEFAULT '{}'::jsonb,
  creado_por  text NOT NULL,
  creado_en   timestamptz NOT NULL DEFAULT now(),
  UNIQUE (archivo_id, etiqueta)
);

CREATE TABLE studio_os.tarea (
  id            uuid PRIMARY KEY,
  proyecto_id   uuid NOT NULL REFERENCES studio_os.proyecto(id),
  tool          text NOT NULL,
  verbo         text NOT NULL CHECK (verbo IN ('inspect','generate','modify','publish')),
  riesgo        text NOT NULL CHECK (riesgo IN ('A','B','C','D')),
  input         jsonb NOT NULL,
  idem_key      text NOT NULL UNIQUE,
  requested_by  text NOT NULL,
  chat_ref      text,
  estado        text NOT NULL CHECK (estado IN
                  ('queued','awaiting_approval','running','completed',
                   'failed','rejected','stale')),
  creado_en     timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE studio_os.ejecucion (
  id                   uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tarea_id             uuid NOT NULL REFERENCES studio_os.tarea(id),
  perfil               text NOT NULL CHECK (perfil IN ('C1','C2','L','banco')),
  runner               text,
  herramienta          text NOT NULL,
  herramienta_version  text,
  parametros           jsonb NOT NULL DEFAULT '{}'::jsonb,
  estado               text NOT NULL,
  inicio               timestamptz,
  fin                  timestamptz,
  duracion_ms          integer,
  costo                numeric(12,6),
  error                jsonb
);

CREATE TABLE studio_os.artefacto (
  id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  ejecucion_id uuid NOT NULL REFERENCES studio_os.ejecucion(id),
  tipo         text NOT NULL,
  ref          text NOT NULL,
  hash_sha256  text,
  metadata     jsonb NOT NULL DEFAULT '{}'::jsonb,
  creado_en    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE studio_os.relacion (
  id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tipo       text NOT NULL CHECK (tipo IN
               ('derived_from','depends_on','generated_by',
                'validated_by','approved_by','supersedes')),
  desde_id   uuid NOT NULL,
  hasta_id   uuid NOT NULL,
  creado_en  timestamptz NOT NULL DEFAULT now(),
  UNIQUE (tipo, desde_id, hasta_id)
);

CREATE TABLE studio_os.aprobacion (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  tarea_id      uuid NOT NULL REFERENCES studio_os.tarea(id),
  persona       text NOT NULL,
  canal         text NOT NULL,
  decision      text NOT NULL CHECK (decision IN
                  ('aprobado','aprobado_con_cambios','rechazado')),
  comentario    text,
  contenido_hash text,
  decided_at    timestamptz NOT NULL DEFAULT now()
);
```

**Nota de diseño**: `relacion` es polimórfica (orquesta `tarea`, `artefacto`, `version`), así que sus dos id no llevan foreign key; la integridad se valida en la API `registry` antes de escribir. El resto de las tablas sí las fuerzan.

**Consultas que el sistema tiene que poder responder**:

| Pregunta | Consulta |
|---|---|
| ¿de qué salió este render? | `artefacto` → `ejecucion` → `tarea` → `version` → `archivo` |
| ¿qué quedó desactualizado si cambio el modelo? | `relacion` tipo `depends_on` desde el artefacto viejo |
| ¿qué seapproved sin esto? | `aprobacion` + `relacion` tipo `approved_by` |
| ¿cuánto costó el mes? | `ejecucion.costo` agregado por `perfil` y mes |

---

# 3 · Perfiles y selección de ejecutor

El agente pide una tarea; **el registro** elige el ejecutor según una tabla de decisión. El agente no elige perfil.

| Tool | Verbo | Perfil preferente | Alternativa | Restricción de datos |
|---|---|---|---|---|
| `inspect_dwg` | inspect | L / banco (AutoCAD) | — | acepta material sensible (no sale de la red) |
| `audit_dwg` | inspect | L / banco | — | acepta material sensible |
| `prepare_sheet` | generate | L / banco | — | escribe solo en carpeta de resultados |
| `publish_pdf` | publish | L / banco | — | **siempre D**: copia, aprobación, evidencia |
| `compare_dwg` | inspect | L / banco | — | idem |
| `extract_quantities` | inspect | L / banco | — | reglas explícitas; informa lo no clasificable |
| `inspect_3dm` | inspect | L / banco | C1 (Rhino.Compute) | — |
| `measure_geometry` | inspect | L / banco | C1 | — |
| `run_grasshopper` | generate | L / banco | C1 (Hops) | — |
| `submit_visual_job` | generate | C2 (Runpod) | L (8 GB, solo modelos chicos) | **solo material derivado no sensible** |
| `render_twinmotion` | generate | L (asistido) | — | hay una persona en el medio |
| `audit_ifc` | inspect | — | — | **fuera de alcance** hasta tener un IFC real |

**Reglas de selección**:
1. Si el perfil primario no está disponible → se informa `no disponible` con el motivo; **nunca** se degrada a otro perfil sin que el perfil elegido acepte la clase de dato.
2. Un perfil declara qué clases de dato admite. Una tarea que exija material sensible contra un perfil que no lo admite **se rechaza antes de ejecutarse**.
3. El perfil elegido queda en la ejecución (`ejecucion.perfil`).

---

# 4 · API del runner

El runner expone una API de tareas (no un chat) y valida del lado que ejecuta.

```
GET  /health                → { runner, capacidades, apps_abiertas, cola }
GET  /capabilities          → [{ tool, verbo, riesgo_max, clases_dato, apps_requeridas }]
POST /tasks                 → { task }        → 202 { task_id, estado }
GET  /tasks/{id}            → { estado, resultado?, error? }
POST /tasks/{id}/approve    → { persona, decision, comentario }  (niveles C/D)
```

**Reglas duras del runner**:

| Regla | Implementación |
|---|---|
| Nunca acepta una ruta del modelo | `file_ref` se resuelve contra el índice de archivos; si no resuelve, error `file_not_resolvable` |
| El original no se toca | toda escritura va a `resultados/<task_id>/` y el original se abre en solo lectura |
| Los niveles C y D exigen aprobación previa | sin `approved`, la tarea vuelve `awaiting_approval` |
| Nada silencioso | si la app no está abierta, la respuesta es `runner_no_disponible` + cómo habilitarlo |
| Idempotencia | `idem_key` repetida devuelve la ejecución previa, no crea una nueva |
| Evidencia | cada ejecución deja log con comandos, versiones y timestamps |

**Publicación del MCP local (P1)**: proxy `stdio → HTTP streamable` en la red privada, con nombre estable; el proxy **no** expone herramientas de escritura: esas van por la API de tareas del runner.

---

# 5 · Perfil de pod GPU

| Parámetro | Valor | Por qué |
|---|---|---|
| Proveedor | Runpod **Secure Cloud** | Community está en retirada y es peer-to-peer |
| GPU | RTX 3090 24 GB (o 4090) | 9B + LoRA entran; $0,50/h Secure |
| Imagen | template propio: ComfyUI + `tailscaled` sidecar | Runpod no soporta Docker Compose: sidecar en el mismo contenedor |
| Red | `tailscaled` con auth key; **proxy público de Runpod cerrado** | el pod no se expone a internet |
| Almacenamiento | **volume disk cifrado** (el container disk no se cifra) | el material que entra tiene que estar cifrado |
| Ciclo de vida | crear al pedir → trabajar → **detener y borrar el volume** | se cobra por segundo; sin residuos |
| Datos | solo material derivado y no sensible | política del ADR |
| Precondiciones | **DPA firmado** + **confirmación escrita de no-entrenamiento** | sin esto, el pod no se crea |

**Runbook del pod** (se escribe junto al template, en el vault):

1. Verificar precondiciones contractuales (DPA + no-entrenamiento) → si faltan, no hay pod.
2. Crear pod en Secure con el template y el volume cifrado.
3. Esperar el alta del tailnet y anotar el nombre MagicDNS del pod.
4. Encolar el job por la API de ComfyUI (misma API que el local: el workflow es el mismo).
5. Recuperar salidas, escribirlas en el vault con su metadata y **borrar el volume**.
6. Registrar la ejecución con `perfil = 'C2'` y su costo.

---

# 6 · Configuración del agente

**`SOUL.md`** (borrador; es el `AGENTS.md` del agente):

```markdown
# SOUL — Agente del estudio (Studio OS)

Sos el agente de un estudio de arquitectura. Tu trabajo es ejecutar lo repetitivo
y verificable, y devolver las decisiones al arquitecto.

## Reglas de operación (Karpathy)
1. Pensá antes de actuar: declará tus supuestos; si la tarea es ambigua, preguntá y esperá.
2. Simplicidad primero: usá la herramienta más simple que resuelva el pedido; nada especulativo.
3. Cambios quirúrgicos: nunca modifies un original; escribí en la carpeta de resultados.
4. Ejecutá contra un objetivo verificable: cada tarea tiene un criterio de cierre; no la declares
   terminada hasta que el check pase.

## Mandato de PI
- El vault es la única memoria. Tu memoria es de trabajo y no se consulta como fuente.
- Nada de planos legales, cálculos, material de cliente confidential ni material de concurso
  con PI de terceros sale de la red del estudio. Nunca pidas eso a un perfil cloud.
- No entrenes con material del estudio. No reveles claves ni contenido sensible en logs o chat.

## Niveles de riesgo
A lectura (automático) · B generación (automático en carpetas controladas) ·
C modificación (requiere aprobación) · D publicación o acción externa (requiere aprobación explícita
y deja evidencia).

## Aprobación
Pedí aprobación humana antes de toda acción C o D, en el canal donde se pidió la tarea.
Registrá quién aprobó, cuándo y sobre qué contenido.

## Herramientas
Solo usá las herramientas habilitadas para tu perfil. No inventes endpoints ni capacidades.
Si una herramienta falla, informá el fallo real: nunca devuelvas un resultado inventado.
```

**`skills/`** (desde los pbooks del vault): `auditar-documentacion-cad` · `generar-variantes-visuales` · `preparar-entrega-de-proyecto` · `documentar-visita-de-obra` · `comparar-versiones-de-documentacion` · `diagnosticar-proyecto-arquitectonico` · (pendiente) `validar-modelo-ifc`.

**MCP declarados** (`config.yaml`):

```yaml
mcp_servers:
  n8n:
    url: "https://n8n.pitau.tech/mcp-server/http"
    auth: oauth
    tools:
      include: ["list_workflows", "get_workflow", "execute_workflow", "n8n_*_read*"]
  vault:
    command: "python"
    args: ["-m", "studio_os.vault_mcp"]
    env:
      STUDIO_OS_VAULT_ROOT: "/opt/data/vault"
      STUDIO_OS_REGISTRY_URL: "http://registry:8080"
  runner:
    url: "http://estudio-runner:8080/mcp"
    headers:
      Authorization: "Bearer ${RUNNER_TOKEN}"
```

**`cron/`**: digest diario 07:00 (movimiento, desactualizados, pendientes, costo) · barrido semanal de dependencias · apagado automático del pod GPU si quedó activo.

---

# 7 · Vault: remoto canónico y sincronización

| Pieza | Dónde | Qué hace |
|---|---|---|
| Remoto canónico | VPS: repositorio git bare | fuente de verdad del vault |
| Clon de trabajo | VPS: `/opt/data/vault` | lo lee y escribe el agente (a través del MCP del vault) |
| Espejo | GitHub privado (`p-31416/vault-arquitectura`) | respaldo y canal de emergencia |
| Clon del estudio | PC del estudio | trabaja contra el remoto del VPS por SSH sobre la red privada |

**Reglas de sincronización**: `fetch` + `pull --ff-only` programados; los commits del agente pasan por el MCP del vault con aprobación; **nada de force-push ni reescrituras de historia**; `log.md` y `raw/sessions/` se verifican con su regla de append-only.

---

# 8 · Observabilidad y métricas

**Por tarea** (en el registro, consultable): duración, estado, reintentos, costo, perfil, versión de herramienta.

**Por periodo** (panel o consulta):
- tiempo manual vs automatizado por tipo de tarea
- % de ejecuciones exitosas
- % de resultados que requieren corrección
- tiempo de recuperación ante fallos
- % de resultados con trazabilidad completa (deben ser 100)
- costo por ejecución y por mes
- recursos consumidos en el VPS y en el banco

**Alertas**: tarea en `awaiting_approval` por más de X horas · runner caído · uso de swap del VPS · pod GPU activo más de Y minutos · tarea C/D ejecutada sin aprobación (debe ser 0: es una alarma).
