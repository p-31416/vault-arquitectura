---
tipo: plan
mvp: 07
cliente: Estudio (interno)
proyecto: Studio OS — sistema operativo para un estudio de arquitectura
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: activo
tags: [mvp_07, studio-os, plan, construccion, f0, f1, f2, hermes, mcp, tailscale]
idioma: es
---

# MVP_07 — Studio OS · plan técnico de construcción

> Plan de construcción del sistema que describe [[proyectos/MVP_07-studio-os-sistema/00-filo-mvp_07|00-filo-mvp_07]]; los contratos técnicos están en [[proyectos/MVP_07-studio-os-sistema/01-spec-mvp_07|01-spec-mvp_07]].
> **Estado:** plan aprobado en diseño, sin construir. F0 arranca con el próximo `s`.

- [[#Reglas del juego]]
- [[#F0 · Fundaciones en el VPS]]
- [[#F1 · Contrato y registro]]
- [[#F2 · Puente y runner]]
- [[#F3 a F6 · Interfase, GPU, estudio y producto]]
- [[#Inventario de scripts]]
- [[#Pruebas de aceptación]]
- [[#Métricas]]
- [[#Riesgos y reversión]]
- [[#Decisiones pendientes con fecha]]
- [[#Los primeros 90 minutos]]

---

# Reglas del juego

1. **HITL**: nada se instala, nada se ejecuta y nada se escribe en `wiki/` sin `s` explícito.
2. **El agente escribe, vos corrés**: todo script nuevo llega como `scripts/<slug>.py` + `scripts/<slug>_notas.md` (línea por línea, para aprender Python leyendo). El comando exacto se propone; la terminal es tuya.
3. **Sin dependencias nuevas**: los scripts usan solo biblioteca estándar. Si algo necesita una librería, se justifica antes.
4. **Cada paso deja evidencia**: todo cambio del VPS se anota en `03-log-mvp_07.md` (se abre con F0) y en `log.md`.
5. **Reversión antes que explicación**: cada tarea define cómo se deshace.
6. **El original no se toca**: los archivos del estudio se abren en solo lectura; toda escritura va a carpeta de resultados.

---

# F0 · Fundaciones en el VPS

**Objetivo:** un Hermes andando en el VPS, con el vault montado, el n8n conectado y una herramienta de solo lectura funcionando. **Sin tocar Telegram**: el bot de n8n sigue igual.

| id | Tarea | Cómo | Quién | Verificación | Reversión | Est. |
|---|---|---|---|---|---|---|
| **F0.1** | Baseline del VPS | `free -m`, `docker stats --no-stream`, `df -h` | agente (solo lectura, con `s`) | queda en `03-log` | n/a | 10 min |
| **F0.2** | Remoto canónico del vault | `git init --bare` en el VPS + `git remote add vps …` + primer push | agente escribe los comandos; vos los corrés | el clon del VPS y el de P: comparten historia | `git remote remove vps` | 30 min |
| **F0.3** | Clon de trabajo del vault en el VPS | `git clone vps:/srv/git/vault-arquitectura.git /opt/data/vault` | vos | el clon existe y `git log` coincide | borrar el directorio | 10 min |
| **F0.4** | Tailscale en el VPS | `curl -fsSL https://tailscale.com/install.sh \| sh` + `sudo tailscale up` + **desactivar expiración de clave** (es un servidor) | vos (SSH, no la consola web: los `docker run` con `:` y `=` se corrompen al pegar) | `tailscale status` muestra el nodo; `tailscale ip` da la 100.x | `tailscale logout` + desinstalar | 20 min |
| **F0.5** | Servicio Hermes en EasyPanel | servicio con imagen `nousresearch/hermes-agent`, comando `gateway run`, volumen nombrado para `/opt/data`, límites `--memory=3g --cpus=2`, `API_SERVER_ENABLED=true`, `API_SERVER_KEY` de 32 bytes, `HERMES_DASHBOARD_HOST=127.0.0.1` | vos (UI de EasyPanel) | `docker service ls` lo muestra y el healthcheck responde | quitar el servicio | 40 min |
| **F0.6** | Setup del agente | `docker exec hermes hermes setup --portal` (o `setup` para el asistente de claves) | vos (interactivo, por SSH) | `hermes config check` sin faltantes | borrar el volumen | 30 min |
| **F0.7** | Modelo | `hermes config set model <proveedor/modelo>` + clave en `.env` | vos | el agente responde una consulta | — | 15 min |
| **F0.8** | MCP de n8n | `hermes mcp install n8n-official` + `hermes mcp login n8n-official` (OAuth por paste-back o túnel SSH, porque el VPS es headless) | vos + agente | `hermes mcp test n8n` lista los workflows | `hermes mcp disable n8n` | 45 min |
| **F0.9** | `SOUL.md` + 3 skills | el agente redacta `SOUL.md` (borrador en `01-spec` §6) y las skills desde los pbooks; vos los copiás al volumen | agente + vos | el agente se identifica con las reglas | editar el archivo | 1 h |
| **F0.10** | Herramienta de solo lectura del vault | MCP filesystem de lectura sobre `/opt/data/vault` + una skill que lo consulta | agente | el agente lee un archivo del vault y lo cita | quitar la entrada MCP | 45 min |
| **F0.11** | Cierre de F0 | reiniciar el servicio y comprobar que la memoria persiste | vos | `hermes status` + una pregunta nueva con recuerdo de la anterior | — | 30 min |

**Criterio de cierre de F0**: Hermes responde por API con el vault montado, la memoria persiste tras reiniciar el servicio, el MCP de n8n lista los workflows, y **la RAM libre del VPS sigue por encima de 1 GB**.

**Kit de F0 ya preparado** (para ejecutar sin volver a pensar):
- `scripts/studio_os_verificar_vps.py` + `_notas.md` → el baseline del VPS (paso 1).
- `proyectos/MVP_07-studio-os-sistema/deploy/00-f0-comandos.md` → los 7 pasos con comandos copiables, verificación y reversión.
- `proyectos/MVP_07-studio-os-sistema/deploy/hermes.compose.yml` → el servicio para EasyPanel (volumen nombrado, límite 3 GB, **cero puertos publicados**).
- `proyectos/MVP_07-studio-os-sistema/hermes/SOUL.md` + `hermes/skills/` → identidad y habilidades del agente, versionadas en el vault.

**Decisión de F0 que conviene tener presente**: el servicio **no publica ningún puerto**. El gateway de Telegram hace long polling (sale, no entra), la API 8642 y el dashboard 9119 quedan apagados, y cuando haga falta exponerlos van por la red privada. La razón está documentada por Hermes: en junio 2026 escáneres entraron por dashboards expuestos y plantaron una backdoor SSH.

**Riesgo de F0**: la RAM. Si al instalar Hermes la memoria disponible baja de 1 GB, la mitigación es desactivar Chatwoot (no se está usando) o mover Qdrant. No se amplía el VPS hasta ver el número.

---

# F1 · Contrato y registro

**Objetivo:** que toda tarea deje rastro verificable.

| id | Tarea | Cómo | Quién | Verificación | Reversión |
|---|---|---|---|---|---|
| **F1.1** | Schema SQL | `scripts/studio_os_migrar_sql.py` aplica el DDL de `01-spec` §2 en el schema `studio_os` | agente escribe; vos corrés | `\d studio_os.tarea` lista 8 tablas | `DROP SCHEMA studio_os CASCADE` |
| **F1.2** | API del registro | `scripts/studio_os_registry.py`: `POST /tareas`, `GET /tareas/{id}`, `POST /aprobaciones`, `POST /artefactos`, `POST /relaciones` — **escritor único** | agente escribe; vos corrés | crear una tarea y consultarla | parar el proceso |
| **F1.3** | Validador del sobre | `scripts/studio_os_contrato_validar.py`: JSON Schema del sobre + reglas (verbo→riesgo, `file_ref` obligatorio, `idem_key`) | agente escribe; vos corrés | 6 casos válidos y 6 inválidos | — |
| **F1.4** | Primer tool real | reusar `scripts/extrae-atributos-dwg.py` (ya existe) como `audit_dwg`, envolviéndolo en el sobre | agente | una auditoría de un DWG real de AIZ devuelve informe con procedencia | — |
| **F1.5** | Detección de desactualizados | consulta `depends_on` + hash: si cambia una versión, los artefactos dependientes quedan `stale` | agente | cambiar una versión y ver el Dependent stale | — |
| **F1.6** | Skill `auditar-documentacion-cad` | el agente la ejecuta vía MCP del registro | agente + vos | una tarea pedida en lenguaje natural produce una tarea registrada | — |

**Criterio de cierre de F1**: una auditoría de AIZ queda con origen, versión, herramienta, parámetros, tiempos y responsable; y un cambio de entrada marca lo dependent como desactualizado.

---

# F2 · Puente y runner

**Objetivo:** que el agente del VPS pueda trabajar sobre los archivos del estudio (primero en el banco P:).

**Camino corto primero (regla de simplicidad)**: Hermes tiene un **backend de terminal SSH** (`terminal.backend: ssh` con `TERMINAL_SSH_HOST/USER/KEY`). Con eso, desde el primer día el agente puede ejecutar comandos en la PC del estudio por la red privada **sin construir todavía el proxy MCP**. El proxy (P1) entra después, cuando las tareas sean llamadas de herramientas y no comandos.

| id | Tarea | Cómo | Quién | Verificación | Reversión |
|---|---|---|---|---|---|
| **F2.0** | Terminal SSH al banco | `terminal.backend: ssh` + `TERMINAL_SSH_*` + `StrictHostKeyChecking=accept-new` | agente (config) + vos (clave) | el agente corre `hostname` en la PC del banco | volver a `local` |
| **F2.1** | Elección del proxy MCP | decidir entre **TBXark/mcp-proxy** (un endpoint HTTP para N servidores stdio, imagen Docker, config por archivo) y **sparfenyuk/mcp-proxy** (puente simple stdio↔streamable HTTP). Reserva: `agentgateway` / `mcpgateway` si hacen falta auth y auditoría de verdad | agente propone; vos decidís | prueba con 2 servidores | — |
| **F2.2** | Publicar los MCP del banco | proxy en Docker con los tres MCP (`autocad`, `rhino`, `comfyui`) + `tailscaled` + nombre estable | vos (instalación) | el VPS lista las herramientas | bajar el servicio |
| **F2.3** | API de tareas del runner | `scripts/studio_os_runner.py`: `/health`, `/capabilities`, `POST /tasks`, `GET /tasks/{id}`, `POST /tasks/{id}/approve` — con validación, nivel de riesgo, carpeta de resultados y watchdog del puente Rhino | agente escribe; vos corrés | una tarea `publish_pdf` de nivel D queda en `awaiting_approval` | parar el proceso |
| **F2.4** | Idempotencia | la misma `idem_key` devuelve la ejecución previa | agente | correr dos veces la misma auditoría | — |
| **F2.5** | Runner no disponible | con la PC apagada, el runner responde `runner_no_disponible` con el motivo | agente | apagar el banco y consultar | — |
| **F2.6** | Perfil de pod GPU (plantilla) | template de Runpod con ComfyUI + `tailscaled` sidecar + volumen cifrado, **sin puertos públicos** | agente escribe el Dockerfile; vos creás el pod (solo cuando haya DPA firmado) | el pod entra al tailnet y se ve desde el VPS | `terminate` + borrar el volume |

**Criterio de cierre de F2**: desde Hermes (API) se dispara `audit_dwg` contra un DWG real de AIZ, el resultado vuelve con procedencia y el original queda intacto (hash antes y después).

---

# F3 a F6 · Interfase, GPU, estudio y producto

| Fase | Depende de | Riesgo principal | Decisión que espera |
|---|---|---|---|
| **F3 · Telegram** | F0-F1 | migración del webhook | ¿el token migra en F3 o espera al MVP? (ADR Telegram) |
| **F4 · Render IA** | F2 + DPA | PI y costo | ¿firmamos DPA y pedimos la confirmación escrita? (ADR Runpod) |
| **F5 · Estudio** | F2 + F0.2-F0.4 | acceso SSH del estudio al VPS | ¿la PC del estudio entra al tailnet? ¿con qué licencia de AutoCAD? |
| **F6 · Producto** | todo | mantenibilidad | ¿servicio mensual o instalación por estudio? |

---

# Inventario de scripts

Todos en `scripts/`, con su archivo `_notas.md` y solo biblioteca estándar.

| Script | Para qué | Comando que vas a correr |
|---|---|---|
| `studio_os_verificar_vps.py` | inventario del VPS (RAM, contenedores, disco, health) por SSH, en modo lectura | `P:\Anaconda\envs\comfyenv\python.exe scripts/studio_os_verificar_vps.py` |
| `studio_os_migrar_sql.py` | aplica el DDL del schema `studio_os` | `P:\Anaconda\envs\comfyenv\python.exe scripts/studio_os_migrar_sql.py` |
| `studio_os_contrato_validar.py` | valida el sobre de tarea (JSON Schema + reglas) | `P:\Anaconda\envs\comfyenv\python.exe scripts/studio_os_contrato_validar.py --archivo tarea.json` |
| `studio_os_registry.py` | API del registro (escritor único) | `P:\Anaconda\envs\comfyenv\python.exe scripts/studio_os_registry.py --puerto 8080` |
| `studio_os_runner.py` | API de tareas del runner | `P:\Anaconda\envs\comfyenv\python.exe scripts/studio_os_runner.py --puerto 8090` |
| `studio_os_vault_mcp.py` | MCP del vault (leer, buscar, índice, escribir con aprobación) | `P:\Anaconda\envs\comfyenv\python.exe scripts/studio_os_vault_mcp.py` |
| `studio_os_pod_runpod.py` | crea/detiene/borra el pod GPU con el perfil acordado | `P:\Anaconda\envs\comfyenv\python.exe scripts/studio_os_pod_runpod.py --accion crear` |

Los que ya existen y se reusan: `scripts/extrae-atributos-dwg.py` (auditoría CAD) · `scripts/indice-renders-comfy.py` (índice con metadata) · `scripts/rhino-mcp-server-rhino.py` (puente Rhino).

---

# Pruebas de aceptación

| # | Prueba | Fase |
|---|---|---|
| 1 | El agente responde por API y su memoria persiste tras reiniciar el servicio | F0 |
| 2 | El MCP de n8n lista los workflows sin intervention manual | F0 |
| 3 | El agente lee un archivo del vault y lo cita con su ruta | F0 |
| 4 | Un sobre inválido (sin `file_ref`, o `publish` con riesgo A) es rechazado | F1 |
| 5 | Una tarea registrada devuelve origen, versión, herramienta, parámetros y tiempos | F1 |
| 6 | Cambiar una versión marca los dependientes como `stale` | F1 |
| 7 | El hash de un DWG original es idéntico antes y después de una publicación | F2 |
| 8 | Una tarea de nivel D sin aprobación no se ejecuta | F2 |
| 9 | La misma `idem_key` no duplica trabajo | F2 |
| 10 | Con la PC apagada, el runner responde `runner_no_disponible` (nunca un resultado inventado) | F2 |
| 11 | El pod GPU no tiene puertos públicos y entra al tailnet | F4 |
| 12 | Una acción C/D sin aprobación deja alerta | F3 |
| 13 | Los logs no contienen claves ni secretos | F0 |

---

# Métricas

**Baseline** (se levanta en F0): tiempo manual de auditar un DWG, de publicar un PDF y de generar una tanda de renders; % de retrabajo por error de versión.

**Después de cada fase**: tiempo automatizado vs manual · % de ejecuciones exitosas · % de resultados con corrección · tiempo de recuperación ante fallos · **% de resultados con trazabilidad completa (objetivo 100)** · costo por ejecución · RAM del VPS con Hermes andando.

---

# Riesgos y reversión

| Riesgo | Fase | Reversión |
|---|---|---|
| El VPS se queda sin RAM | F0 | quitar Hermes del servicio (1 clic en EasyPanel); volver a medir |
| `state.db` corrupto por WAL sobre un bind mount | F0 | volumen nombrado (no bind); si ocurre, `hermes sessions set-journal-mode delete` |
| Config de Hermes mal y el gateway no levanta | F0 | `hermes config check`; el volumen guarda copia de `config.yaml` antes de migrar |
| El agente escribe en el vault sin control | F0-F1 | el MCP del vault exige aprobación; el `SOUL.md` lo prohíbe explícitamente |
| El bot de Telegram queda a medias en la migración | F3 | el bot de n8n queda listo y el token vuelve en 1 minuto |
| Material sensible llega al pod | F4 | política por clase de dato + validación en el runner antes de enviar |
| `n8n:latest` actualiza sin control | F0 | pinear versión en el compose del servicio (arreglo pendiente, propuesto) |

---

# Decisiones pendientes con fecha

| # | Decisión | Antes de | Impacto si no se decide |
|---|---|---|---|
| 1 | ¿Firmamos DPA + confirmación escrita de no-entrenamiento a Runpod? | F4 | el nodo GPU no se puede usar |
| 2 | ¿AutoCAD completo o seguimos con LT? | F5 | el perfil C1 (nube oficial) queda descartado |
| 3 | ¿El bot de Telegram migra en F3 o espera al MVP? | F3 | la interfase se define por defecto |
| 4 | ¿El estudio entra al tailnet con SSH al VPS? | F5 | el clon del estudio queda atado a GitHub |
| 5 | ¿Mini-servidor propio en el estudio (licencia Rhino en servidor)? | F5 | Rhino.Compute local queda descartado |
| 6 | ¿Servicio mensual o instalación por estudio? | F6 | el perfil de despliegue del producto queda indefinido |
| 7 | ¿Quién opera el repo bare y su backup? | F0.2 | el canónico queda sin dueño |

---

# Los primeros 90 minutos

Mañana, en este orden (cada paso pide `s`):

1. **F0.1** — inventario del VPS con `studio_os_verificar_vps.py` (lo escribo y vos lo corrés). Deja el baseline de RAM y disco.
2. **F0.2-F0.3** — remoto canónico del vault en el VPS: te paso los comandos git exactos.
3. **F0.4** — Tailscale en el VPS (por SSH, no por la consola web) + desactivar expiración de clave.
4. **F0.5** — servicio Hermes en EasyPanel: te paso el bloque de compose con imagen, volumen, límites y variables de entorno.
5. **F0.6-F0.8** — setup, modelo y MCP de n8n (interactivo, lo hacés vos).
6. **F0.9-F0.11** — `SOUL.md`, skills, MCP de lectura del vault y cierre de fase.

**Antes de empezar**: confirmame si el `s` de mañana cubre (a) los pasos de F0 completos, o (b) los pasos 1-3 solamente, para no installationar de más.
