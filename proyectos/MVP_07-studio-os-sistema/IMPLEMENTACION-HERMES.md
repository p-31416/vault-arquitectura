---
tipo: proyecto
fecha_creacion: 2026-10-29
ultima_actualizacion: 2026-10-29
tags: [studio-os, hermes, implementacion, mcp, seguridad, wiki]
idioma: es
---

# Implementación en Hermes Agent

Este documento responde una sola pregunta: **de todo lo que el sistema necesita, qué ya trae Hermes y con qué configuración exacta**. No repite la visión ([[proyectos/MVP_07-studio-os-sistema/VISION|VISION]]), ni dónde vive cada pieza ([[proyectos/MVP_07-studio-os-sistema/ESTRUCTURA|ESTRUCTURA]]), ni qué tiene que cumplir ([[proyectos/MVP_07-studio-os-sistema/REQUISITOS|REQUISITOS]]). Traduce esas tres cosas a piezas de Hermes.

Verificado contra la documentación oficial el **29/10/2026**. Cada afirmación tiene su fuente al final (§15).

---

## 1. Resumen: qué resuelve Hermes sin escribir código

| Lo que el sistema necesita | Lo que Hermes ya trae | Cuánto falta |
|---|---|---|
| Leer PDF, Word, Excel, PowerPoint, ODT, EPUB | `read_file` convierte solo, sin dependencias para docx/xlsx | nada |
| Leer PDF escaneado | aviso de cobertura + `vision_analyze` o skill `ocr-and-documents` | elegir el camino |
| Acceder al Drive | MCP oficial de Google Drive + skill `google-workspace` | credencial OAuth |
| Analizar una fuente y dejarla en la wiki | skills + `AGENTS.md` + `write_file`/`patch` + git | escribir las skills |
| Recordar entre sesiones | `MEMORY.md` + `USER.md` + `session_search` (FTS5) | curar qué entra |
| Mejorar sola sus procedimientos | revisión de fondo + `skill_manage` + curador | activar aprobación |
| Tareas con fecha | cron con skills adjuntas y entrega a Telegram | definir las tareas |
| Reaccionar a un evento | webhooks con HMAC, filtros y disparo de cron | una ruta por evento |
| Pedir permiso antes de tocar algo | `approvals` (smart/manual/off), `deny`, allowlist | mapear A-D |
| Aislar la ejecución | backends local, Docker, SSH, Modal, Daytona, Vercel | elegir perfil |
| Dejar rastro de todo | `state.db`, `executions.db`, ledger del curador, logs | conectar al registro |
| Que hable con n8n, ComfyUI, Sheets | MCP (stdio o HTTP) + preset `n8n-official` | configurar servidores |

Lo que **no** resuelve: CAD, IFC, render, el cuaderno como interfaz, el portal de iteraciones y la base PostgreSQL del registro. Eso es nuestro (§11).

---

## 2. Las cinco piezas que hay que configurar

Todo el sistema se arma con cinco cosas. El resto es contenido.

1. **`config.yaml`** — el comportamiento: modelo, backend de terminal, aprobaciones, memoria, skills, curador, cron.
2. **`SOUL.md`** — quién es el agente (identidad del estudio, tono, reglas de la casa).
3. **`AGENTS.md` del vault** — el contexto que se carga solo cuando trabaja adentro del vault.
4. **Skills** — los procedimientos: analizar una fuente, mantener la wiki, preparar una entrega.
5. **Cron + webhooks** — lo que corre solo y lo que reacciona a eventos.

---

## 3. Flujo A — Análisis de fuentes que están en un Drive

### 3.1 Las tres formas de llegar al Drive

| Forma | Cómo | Cuándo conviene | Costo |
|---|---|---|---|
| **A1 · MCP oficial de Drive** | servidor remoto `https://drivemcp.googleapis.com/mcp/v1` | el estudio ya vive en Drive y quiere leer sin bajar nada | requiere OAuth y el cliente marcado como "AI-powered agent" |
| **A2 · Skill `google-workspace`** | skill incluida, con `google_token.json` en el perfil | querés Gmail, Calendar, Docs y Drive con el mismo login | OAuth una vez, token montado en el sandbox |
| **A3 · Espejo local** | `rclone` baja la carpeta a `/opt/data/fuentes/` y el agente lee archivos | control total, funciona sin red, versiona con git | sincronización programada |

**Recomendación**: **A3 para el corpus estable** (lo que ya está archivado) y **A1 para lo que llega** (buscar y leer un archivo puntual que el estudio acaba de subir). A2 solo si además queremos Gmail y Calendar en el mismo flujo.

### 3.2 Cómo se declara el MCP de Drive

```yaml
mcp_servers:
  drive:
    url: "https://drivemcp.googleapis.com/mcp/v1"
    auth: oauth                  # OAuth 2.1 con PKCE; token en ~/.hermes/mcp-tokens/drive.json
    trust: untrusted             # cualquier tool de escritura pediría aprobación
    tools:
      include: [search_files, get_file_metadata, read_file_content, list_recent_files, download_file_content]
      resources: false
      prompts: false
```

Se dejan **fuera** `create_file`, `copy_file` y todo lo que escribe: la escritura al Drive va por la skill y con aprobación, no por el MCP.

Herramientas que expone el servidor oficial: `search_files`, `read_file_content`, `get_file_metadata`, `get_file_permissions`, `list_recent_files`, `download_file_content`, `create_file`, `copy_file`.

**Trampa verificada**: desde el **11/11/2026** Google rechaza los pedidos de clientes OAuth que no estén marcados como *"Use this client for an AI-powered agent"* en Google Auth Platform. Hay que marcarlo el día que se crea la credencial, no después.

### 3.3 El flujo completo, paso a paso

```
1. Llega el archivo (Drive, mail, WhatsApp, escaneo)
2. Se materializa en /opt/data/fuentes/<proyecto>/<año>/
3. read_file lo convierte a texto (PDF, docx, xlsx, pptx, odt, epub)
4. Si el PDF es escaneado, el propio read_file avisa qué páginas no tienen texto
   y el agente decide: vision_analyze para pocas páginas, OCR para muchas
5. La skill `analizar-fuente` extrae: tipo, fecha, emisor, hechos, entidades, temas
6. Escribe la ficha en el vault y el hecho en el registro
7. Deja el original en /opt/data/fuentes/ (nunca en git)
```

La detección de PDF escaneado es automática: si más del 20 % de las páginas no devuelve texto —o son 10 páginas o más— `read_file` antepone un aviso con los rangos exactos, cada hueco etiquetado con el último texto leído antes, y sugiere dos caminos: renderizar con `pdftoppm` + `vision_analyze` (pocas páginas, sin dependencias extra) o la skill `ocr-and-documents` (marker-pdf, 90+ idiomas, tablas y ecuaciones; instala 3-5 GB). El aviso pide explícitamente no OCRear ni renderizar todo.

### 3.4 La skill `analizar-fuente` (esqueleto)

```markdown
---
name: analizar-fuente
description: Convierte un documento en una ficha de wiki con hechos y entidades.
metadata:
  hermes:
    category: vault
    requires_toolsets: [file, terminal]
---
## Cuándo se usa
Cuando llega un documento nuevo (pliego, contrato, plano, acta, mail largo).

## Procedimiento
1. Identificar tipo, fecha, emisor y proyecto. Si falta, preguntar una sola vez.
2. Leer el documento completo; si hay aviso de cobertura, resolver los huecos.
3. Extraer hechos verificables (con página o sección) y entidades (personas, obras, normas).
4. Escribir la ficha con el frontmatter del vault y enlazar con [[wikilinks]].
5. Añadir al log del proyecto una línea: qué entró y qué se concluyó.

## Errores que ya cometimos
- Citar sin página: no sirve para una auditoría.
- Resumir el documento en vez de extraer hechos: pierde valor.
```

---

## 4. Flujo B — Mantener y mejorar la wiki

Esto es lo que Hermes hace mejor y lo que hoy hacemos a mano. Son **cuatro capas** que ya existen y una que hay que escribir.

### 4.1 Capa 1 — Contexto: `AGENTS.md`

Hermes carga el `AGENTS.md` de la raíz del repo y **descubre los de los subdirectorios a medida que entra en ellos**. Es exactamente el patrón que ya usa el vault: un `AGENTS.md` en la raíz y uno por rama del glosario.

- Se carga al inicio de la sesión (system prompt).
- Los de subdirectorio se inyectan cuando el agente lee un archivo de ahí, sin inflar el prompt.
- Todos pasan por un escáner de inyección de prompts: si alguien mete "ignorá las instrucciones anteriores" en un `.md` del vault, el archivo se bloquea.

**Acción concreta**: el `AGENTS.md` del vault ya existe y es bueno. Hay que añadirle una sección `## Para el agente del estudio` con las rutas de trabajo (`/opt/data/vault`, `/opt/data/fuentes`) y la regla de que los binarios no entran.

### 4.2 Capa 2 — Procedimiento: skills

Las skills son los procedimientos del estudio escritos una vez. Se cargan solo cuando hacen falta (divulgación progresiva: índice → skill completa → archivo de referencia).

Estructura recomendada para el estudio:

```
~/.hermes/skills/vault/
├── analizar-fuente/SKILL.md
├── mantener-wiki/SKILL.md
├── preparar-entrega/SKILL.md
├── auditar-planos/SKILL.md
└── actualizar-glosario/SKILL.md
```

Tres detalles que importan:

- **`skills.create_dir`** permite que las skills creadas por el agente caigan en un repo git en vez de en el perfil: `create_dir: /opt/data/vault/skills`. Así el conocimiento del estudio se versiona con el vault.
- **Skills de proyecto**: si el vault tiene `.hermes/skills/` o `.agents/skills/`, esas skills ganan sobre las globales cuando el agente trabaja adentro del repo. Requiere `hermes skills trust` una vez (no se auto-cargan de repos clonados, por seguridad).
- **`skills.write_approval: true`**: toda escritura de skill queda en `~/.hermes/pending/skills/` hasta que alguien la apruebe con `/skills approve`. Esto es lo que convierte "el agente mejora solo" en "el agente propone mejoras".

### 4.3 Capa 3 — Memoria: `MEMORY.md` + `USER.md` + `session_search`

| Qué guarda | Dónde | Límite |
|---|---|---|
| Hechos del entorno y del estudio | `MEMORY.md` | 2.200 caracteres (~800 tokens) |
| Preferencias de las personas | `USER.md` | 1.375 caracteres (~500 tokens) |
| Todo lo conversado | SQLite con FTS5 (`state.db`) | sin límite, búsqueda en ~20 ms |

**El límite de 2.200 caracteres es una decisión de diseño, no un defecto**: obliga a que la memoria sea curada. Cuando se llena, el agente tiene que consolidar antes de añadir. Para el estudio eso está bien: lo que no entra en memoria va a la wiki.

**Lo que hay que entender**: la memoria es del *agente*, la wiki es del *estudio*. `MEMORY.md` guarda "el vault está en `/opt/data/vault` y se publica los viernes"; la wiki guarda el procedimiento y el conocimiento. Si se mezclan, la memoria se llena y la wiki se vacía.

**`session_search`** es el complemento: busca en todas las conversaciones pasadas y devuelve mensajes reales, sin resumen. Sirve para "¿qué hablamos con Emilia en marzo?".

**Práctica obligatoria**: `/new` al cerrar un tema. En Telegram la sesión es continua y puede durar semanas; sin cortes, la memoria no se recarga y la compactación se vuelve carísima.

### 4.4 Capa 4 — Mejora automática: revisión de fondo + curador

Dos mecanismos distintos, que conviene no confundir:

| | **Revisión de fondo** | **Curador** |
|---|---|---|
| Cuándo | después de cada turno | cada 7 días y con 2 h de inactividad |
| Qué hace | guarda memoria y crea/parchea skills | mueve skills sin uso a `stale` y luego a `.archive/` |
| Costo | tokens del modelo (o de un modelo auxiliar barato) | determinístico; la consolidación con LLM es opt-in |
| Riesgo | escribir una lección equivocada | archivar una skill que sí se usaba |

Configuración recomendada para el estudio:

```yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
  write_approval: true          # nada entra a la memoria sin aprobación
skills:
  write_approval: true          # nada se escribe en una skill sin aprobación
  create_dir: /opt/data/vault/skills
curator:
  enabled: true
  interval_hours: 168
  stale_after_days: 14
  archive_after_days: 30
  consolidate: false            # primero mirar; activar cuando haya 20+ skills
auxiliary:
  background_review:
    provider: auto              # después: modelo local barato
```

El curador **nunca borra**: archiva en `.archive/` y se restaura con `hermes curator restore <skill>`. Y no toca las skills escritas a mano ni las de proyecto. Lleva un ledger de cada mutación (`~/.hermes/skills/.curator_ledger.jsonl`) con actor, acción y hashes antes/después, y permite deshacer **una** edición con `hermes curator rollback <entry-id>`.

### 4.5 La capa que falta escribir: `mantener-wiki`

Hermes no trae una skill de "mantener una wiki de Obsidian". Trae `note-taking/obsidian` (para tomar notas), que es otra cosa. Hay que escribir:

```markdown
---
name: mantener-wiki
description: Revisa el vault, detecta huérfanas, enlaces roos y fichas sin frontmatter.
metadata:
  hermes:
    category: vault
---
## Cuándo se usa
En el cron semanal y cuando alguien pide "revisá la wiki".

## Procedimiento
1. Listar todos los .md y verificar frontmatter obligatorio.
2. Detectar enlaces [[...]] que no resuelven a un archivo.
3. Detectar páginas sin ningún enlace entrante (huérfanas).
4. Detectar fichas de la misma entidad con nombres distintos.
5. Escribir un informe en raw/lint/YYYY-MM-DD.md con la lista y la propuesta.
6. Aplicar solo los cambios de nivel B; los de nivel C, proponerlos.

## Verificación
El informe lista cada problema con archivo y línea.
```

### 4.6 El cron que la mantiene viva

```yaml
# creado con: hermes cron create "0 7 * * 1" "..." --skill mantener-wiki --workdir /opt/data/vault
schedule: "0 7 * * 1"
workdir: /opt/data/vault        # carga el AGENTS.md del vault
skills: [mantener-wiki]
deliver: telegram
prompt: |
  Revisá el vault completo. Escribí el informe en raw/lint/.
  No modifiques fichas: solo proponé. Si el informe tiene más de 20 problemas,
  resumí los 5 más graves en el mensaje y dejá el resto en el archivo.
```

Detalles que hacen la diferencia:

- **`workdir`** es lo que hace que el cron cargue el `AGENTS.md` del vault. Sin eso, el job corre "suelto" y no conoce las reglas.
- **Las sesiones de cron son nuevas**: no recuerdan la corrida anterior. `MEMORY.md` sí se carga, así que las preferencias durables viajan; el contexto de la corrida anterior no. El prompt tiene que ser autosuficiente.
- **Un cron no puede preguntar**: no hay nadie esperando. Los comandos peligrosos se **niegan** por defecto (`cron_mode: deny`). Está bien: el cron propone, la persona aprueba.

---

## 5. Flujo C — Seguridad, permisos y niveles A-D

Hermes trae **ocho capas**. Las que nos importan para mapear A-D:

### 5.1 Autorización: quién puede hablarle

```bash
TELEGRAM_ALLOWED_USERS=11111111,22222222
GATEWAY_ALLOWED_USERS=11111111
```

Sin allowlist configurada, **todos quedan afuera** (fail-closed). El emparejamiento por DM (`hermes pairing approve telegram ABC12DEF`) permite sumar a alguien sin editar archivos: el desconocido recibe un código de 8 caracteres, válido 1 hora, con rate limit y bloqueo tras 5 intentos.

### 5.2 Aprobación de comandos peligrosos

```yaml
approvals:
  mode: manual                 # el estudio quiere ver cada cosa destructiva
  timeout: 300
  cron_mode: deny              # un cron nunca auto-aprueba
  unattended_mode: deny
  deny:                        # piso propio, por encima de cualquier modo
    - "git push --force*"
    - "docker compose down*"
    - "*rm -rf*"
```

Tres modos:

- **`smart`** (default): un modelo auxiliar evalúa el riesgo. Lo barato pasa, lo peligroso se niega, lo dudoso pregunta.
- **`manual`**: siempre pregunta. Es lo que recomiendo para el estudio en el tramo 1-2.
- **`off`**: equivale a `--yolo`. Solo en contenedores descartables.

Además hay una **lista negra dura** que no se puede saltar ni con `--yolo`: `rm -rf /`, bombas fork, `mkfs` sobre el disco vivo, `dd` a un dispositivo, `curl | sh` en la raíz. Y un bloqueo especial que impide que el agente mate o reinicie el gateway que lo hospeda.

### 5.3 El mapeo A-D en la práctica

| Nivel | Cómo se implementa en Hermes |
|---|---|
| **A · Lectura** | toolsets `file` (read), `web`, `vision`. Sin aprobación. |
| **B · Generación aislada** | `write_file` dentro de `HERMES_WRITE_SAFE_ROOT`, en una carpeta de salida. Sin aprobación. |
| **C · Modificación** | `approvals.mode: manual` + `skills.write_approval` + `memory.write_approval`. Cada escritura pasa por un botón. |
| **D · Publicación / acción externa** | el toolset de escritura externa (mail, Drive, git push) **no está en el toolset del agente**; lo ejecuta una skill que termina en un `cron` con `deliver` a una persona, o el humano lo hace. |

**Hallazgo importante**: con backend **Docker**, Hermes **saltea** la aprobación de comandos peligrosos porque el contenedor es la frontera. Es decir: si el agente corre en Docker, los niveles C y D **no** se controlan con `approvals`; se controlan **quitando herramientas**. El gobierno tiene que estar en el toolset y en el filesystem, no solo en el prompt de aprobación.

### 5.4 Aislamiento y escritura

```yaml
terminal:
  backend: docker
  docker_image: "nousresearch/hermes-sandbox:desktop"
  container_cpu: 2
  container_memory: 3072        # 3 GB: entra en los 4.858 MB libres del VPS
  container_persistent: true
```

La imagen oficial ya define `HERMES_WRITE_SAFE_ROOT=/opt/data`: el agente **no puede** escribir fuera de ahí con `write_file`/`patch`, y hay una lista de rutas protegidas siempre (`.ssh`, `.aws`, `.kube`, `.env`, `auth.json`, `vault/`, `mcp-tokens/`).

Los contenedores corren con `--cap-drop ALL`, `no-new-privileges`, `pids-limit 256` y `/tmp` sin exec. Para el VPS, el backend **SSH** es la otra opción razonable: el agente corre en el host pero los comandos peligrosos **sí** se chequean (a diferencia de Docker).

### 5.5 Secretos

- Los secretos viven en `~/.hermes/.env`, nunca en `config.yaml`.
- Las variables sensibles **no** se pasan a los subprocesos por defecto. Una skill declara las que necesita (`required_environment_variables`) y solo esas pasan.
- Los archivos de credencial (ej. `google_token.json`) se declaran con `required_credential_files` y se montan **read-only** en el contenedor.
- Las tools de MCP reciben un entorno filtrado: solo variables de sistema y las que declare su bloque `env`.
- Hay proxy de egreso (`egress`) para limitar a dónde puede salir el agente.

---

## 6. Flujo D — Registro y trazabilidad

Hermes ya deja rastro de casi todo. La pregunta es cómo se conecta con el registro híbrido que definimos.

| Qué pasó | Dónde queda | Formato |
|---|---|---|
| Cada conversación | `~/.hermes/state.db` | SQLite + FTS5 |
| Cada corrida de cron | `~/.hermes/cron/executions.db` | SQLite, con estados `claimed/running/completed/failed/unknown` |
| Cada mutación de skill | `~/.hermes/skills/.curator_ledger.jsonl` | JSONL con hashes antes/después |
| Cada aprobación | `state.db` (comandos ejecutados) | consultable con `hermes approvals suggest` |
| Errores y gateway | `~/.hermes/logs/` | texto, secretos redactados |
| Salida de cada cron | `~/.hermes/cron/output/<job_id>/` | archivos |

**Corrección al diseño**: Hermes **no** usa PostgreSQL. Su registro es SQLite. Entonces el "registro híbrido" tiene tres opciones:

1. **Hermes SQLite + PostgreSQL nuestro** para lo de negocio (proyectos, compromisos, clientes) y el vault para lo narrativo. El agente consulta Postgres por `terminal` + `psql`.
2. **Un proveedor de memoria externo** (`Honcho`, `RetainDB`, `Mem0`, `Hindsight`, `Supermemory`) que agregue grafo y búsqueda semántica *encima* del SQLite. Corren al lado, no lo reemplazan.
3. **Postgres como única fuente** y el SQLite de Hermes como caché de sesión.

Recomiendo **(1)**: es la que menos piezas nuevas introduce y la que deja el registro de negocio en un lugar que no depende del agente.

---

## 7. Flujo E — El cuaderno digital y los croquis

Hermes no dibuja. Lo que sí hace:

- **Escaneo**: el móvil manda la foto al bot; el archivo cae en `/opt/data/cuaderno/<año>/`; `vision_analyze` lee el croquis y propone etiquetas.
- **Anclaje a la wiki**: la skill `cuaderno` escribe un `.md` con el croquis embebido y enlaces a las fichas del proyecto.
- **Búsqueda**: `session_search` encuentra "el croquis del entrepiso que mandé en junio".
- **Publicación**: el `.md` se publica con el mismo pipeline del vault (Quartz o MkDocs), sin que Hermes intervenga.

Lo que hay que construir es la **interfaz** (libro a pantalla completa, horizontal): eso es front-end nuestro, no Hermes.

---

## 8. Flujo F — Compromisos con fecha y recordatorios

Hermes tiene cron de primera clase, con más de lo que parece:

```bash
hermes cron create "2026-11-15T09:00:00" \
  "Recordá que vence la presentación del plano municipal de Emilia." \
  --deliver telegram --name "entrega-municipalidad"
```

- **Recordatorios que se pueden responder**: los jobs son "continuables"; si respondés al mensaje, el agente retoma el hilo.
- **Entrega a un tema concreto**: `telegram:chat_id:thread_id` permite que cada obra tenga su hilo.
- **`--paused`**: crear el recordatorio ya pausado, para revisarlo antes de que dispare.
- **`--workdir`**: el recordatorio corre con el contexto del proyecto.
- **Reintentos**: si el modelo no estaba disponible (red caída), reintenta a los 5, 15 y 30 minutos, sin gastar tokens.
- **Incidentes**: si un job falla siempre por lo mismo, avisa **una vez** y después cada 6 h, no en cada corrida.

**Lo que falta**: que los compromisos vivan en el registro (Postgres/Sheets) y que el cron los lea de ahí en vez de tener un job por compromiso. Patrón recomendado: **un solo job diario** que consulta los compromisos del día y manda un mensaje; no 300 jobs.

---

## 9. Flujo G — Reuniones, webhooks y eventos

```yaml
platforms:
  webhook:
    enabled: true
    extra:
      port: 8644
      secret: "..."                  # HMAC global
      routes:
        fathom:
          events: ["recording.completed"]
          secret: "..."
          cron_job: "procesar-reunion"
          prompt: "Reunión nueva: {recording.title} — {recording.url}"
```

Propiedades del webhook que sirven al estudio:

- **HMAC obligatorio**: sin firma válida, 401. Un secreto por ruta.
- **Filtros declarativos**: `equals`, `contains`, `regex`, `in_file`. Solo despierta al agente lo que importa.
- **`coalesce`**: si llegan 5 eventos del mismo archivo en 30 segundos, corre **una** vez.
- **`deliver_only`**: para avisos simples, cero tokens.
- **Toolset por ruta**: por defecto un webhook solo tiene `web_search`, `web_extract`, `vision_analyze` y `clarify`. Darle `terminal` es una edición manual del `config.yaml`, a propósito.
- **Idempotencia**: el mismo `X-GitHub-Delivery` no se procesa dos veces en una hora.

**Frase para recordar**: *autenticado no significa confiable*. La firma prueba quién manda, no que el contenido sea inocuo. El límite de seguridad es el toolset, no el canal.

---

## 10. Flujo H — Entregas y aprobaciones

El punto donde el sistema se juega la confianza. La secuencia:

```
1. El agente prepara el paquete (memoria, láminas, planos, checklist)  → nivel B
2. Escribe el borrador del mail con el formato del estudio              → nivel B
3. Pide aprobación en Telegram con el resumen y los adjuntos            → nivel C
4. Una persona revisa, corrige el tono y manda                          → nivel D (humano)
5. El sistema registra: qué se mandó, cuándo, quién aprobó, versión     → registro
```

Hermes cubre 1, 2, 3 y 5. El paso 4 es humano **por diseño** y por la regla del estudio: *se automatiza el trabajo, no la responsabilidad*.

Para el paso 5, el registro tiene que ser nuestro: `state.db` guarda el turno, pero no sabe qué versión del plano se mandó. Eso lo escribe la skill en el registro de negocio.

---

## 11. Lo que Hermes no hace (y sigue siendo nuestro)

| Pieza | Por qué no es de Hermes | Dónde vive |
|---|---|---|
| CAD / Rhino / IFC | Hermes no modela; orquesta | MCP + API del programa |
| Render y ComfyUI | idem | MCP + API |
| Cuaderno como interfaz | Hermes no tiene UI propia de lectura | front-end nuestro |
| Portal de iteraciones | no es un chat | web propia |
| Base PostgreSQL | Hermes usa SQLite | nuestro |
| Sincronización del Drive | el MCP lee; no sincroniza | rclone |
| Cumplimiento legal de planos | es criterio humano | la persona |

---

## 12. Hallazgos que cambian el diseño

1. **La memoria es chica a propósito** (2.200 + 1.375 caracteres). La wiki no compite con la memoria: la complementa.
2. **Hermes usa SQLite, no Postgres**. El registro híbrido necesita una decisión explícita (§6).
3. **Docker saltea las aprobaciones**: el gobierno A-D tiene que estar en el toolset, no solo en `approvals`.
4. **Los cron no preguntan y no recuerdan la corrida anterior**. Todo prompt de cron debe ser autosuficiente.
5. **Un solo agente por `HERMES_HOME`**: dos procesos sobre el mismo home se pisan la memoria. Coincide con "un agente por estudio", pero hay que respetarlo al montar el segundo (Ollama) — va con **perfil** propio, no con otro proceso sobre el mismo home.
6. **El curador no toca skills escritas a mano ni de proyecto**. Nuestras skills del estudio quedan fuera de su alcance salvo que las adoptemos (`hermes curator adopt`).
7. **El MCP de Drive es Developer Preview** y exige marcar el cliente OAuth como agente antes del 11/11/2026.
8. **`read_file` no hace OCR**: detecta y avisa. El OCR es una decisión aparte (visión para pocas páginas, marker-pdf para muchas).
9. **Los webhooks vienen con toolset mínimo**. Es una feature, no una limitación.
10. **La sesión de Telegram puede durar semanas**. Sin `/new`, la memoria nueva no se carga.

---

## 13. Configuración propuesta (`config.yaml` del estudio)

```yaml
# Identidad: SOUL.md se lee solo desde HERMES_HOME (~/.hermes/SOUL.md).
# No hay clave "soul": el archivo se carga si existe.

# Modelo: se elige con `hermes model` y queda guardado en config.yaml.
# Tramo 1: la suscripción que ya está paga. Después: perfil propio con Ollama.

# Terminal
terminal:
  backend: docker
  docker_image: "nousresearch/hermes-sandbox:desktop"
  container_cpu: 2
  container_memory: 3072
  container_persistent: true
  env_passthrough: [STUDIO_DB_URL]

# Aprobaciones
approvals:
  mode: manual
  timeout: 300
  cron_mode: deny
  single_query_mode: deny
  unattended_mode: deny
  deny:
    - "git push --force*"
    - "docker compose down*"
    - "*rm -rf*"

# Memoria
memory:
  memory_enabled: true
  user_profile_enabled: true
  write_approval: true

# Skills
skills:
  write_approval: true
  create_dir: /opt/data/vault/skills
  external_dirs:
    - /opt/data/vault/.agents/skills

# Curador
curator:
  enabled: true
  interval_hours: 168
  stale_after_days: 14
  archive_after_days: 30
  consolidate: false
  backup:
    enabled: true
    keep: 2

# Cron
cron:
  max_parallel_jobs: 2
  wrap_response: false         # sin el encabezado "Cronjob Response"

# MCP
mcp_servers:
  n8n:
    url: "https://n8n.pitau.tech/mcp-server/http"
    headers:
      Authorization: "Bearer ${N8N_MCP_TOKEN}"   # el secreto vive en ~/.hermes/.env
    trust: untrusted
  drive:
    url: "https://drivemcp.googleapis.com/mcp/v1"
    auth: oauth
    trust: untrusted
    tools:
      include: [search_files, get_file_metadata, read_file_content, list_recent_files]
      resources: false
      prompts: false
```

---

## 14. Decisiones que se abren con este documento

1. **Drive: MCP oficial, skill `google-workspace` o espejo con rclone** (§3.1). Recomiendo espejo para el archivo y MCP para lo nuevo.
2. **Registro: SQLite de Hermes + Postgres nuestro, o proveedor de memoria externo** (§6). Recomiendo la primera.
3. **Backend: Docker o SSH** (§5.4). Docker aísla más; SSH deja las aprobaciones activas.
4. **`approvals.mode`: `manual` desde el día uno o `smart` y ajustar** (§5.2). Recomiendo `manual` en el tramo 1.
5. **Cuándo activar la consolidación del curador** (§4.4). Recomiendo esperar a tener 20+ skills.

---

## 15. Referencias verificadas (29/10/2026)

- [Documentación de Hermes Agent](https://hermes-agent.nousresearch.com/docs/)
- [Repositorio](https://github.com/NousResearch/hermes-agent)
- [Seguridad](https://hermes-agent.nousresearch.com/docs/user-guide/security)
- [Configuración](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
- [Memoria persistente](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)
- [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Curador](https://hermes-agent.nousresearch.com/docs/user-guide/features/curator)
- [Cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
- [Webhooks](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks)
- [Extracción de documentos](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
- [Archivos de contexto](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
- [Referencias de contexto](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
- [MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [Servidor MCP de Google Drive (Google)](https://developers.google.com/workspace/drive/api/guides/configure-mcp-server)
- [Referencia de herramientas del MCP de Drive](https://developers.google.com/workspace/drive/api/reference/mcp)
- [Notas de versión de Drive API (requisito de cliente agéntico)](https://developers.google.com/workspace/drive/release-notes)
