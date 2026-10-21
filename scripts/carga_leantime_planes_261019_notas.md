# NOTA ES: `carga_leantime_planes_261019.py` línea por línea

- **Docstring:** qué carga (las cards de los 2 planes del 19/10 en Leantime), en qué proyectos, y que
  es idempotente por headline. Da el comando de uso con `--dry-run`.
- **Import de `leantime_rpc`:** el cliente JSON-RPC vive en el script hermano; se agrega su carpeta al
  `sys.path` para poder importarlo sin instalar nada.
- **`RAIZ` / `SALIDA`:** raíz del vault y archivo donde se deja el estado final de la carga
  (`raw/reuniones/leantime-carga-261019-estado.json`), que después se asienta en el vault.
- **`PROY_EMI` / `USU_EMILIA` / `USU_SOL`:** ids reales en la instancia — proyecto 4 `O.S_ARQ-Emi`,
  usuario 5 Emilia (arq.emiliapimentalombardi@gmail.com), usuario 1 Pitau Tech.
- **`COL` / `PRIORIDAD`:** mapeo de las columnas LPS del vault (Backlog, Make-ready, Sprint actual, En curso,
  Revisión, Bloqueado, Hecho) a los ids de estado de Leantime (3 New, 4 In Progress, 2 Waiting for Approval,
  1 Blocked, 0 Done) y de las prioridades (1 Critical … 4 Low).
- **`card(...)`:** armado de cada card del plan: código, headline, dueño (emilia / sol / ambos), pomodoros,
  milestone, columna inicial, criterio de cierre, subtareas con sus minutos y el origen (timestamp de la
  transcripción). Concentra los datos en un solo lugar para no repetirlos.
- **`mil(...)`:** milestone con su id de plan, nombre, proyecto, fecha de corte y descripción.
- **`MIL_A` / `PLAN_A`:** plan de agentes + agenda (proyecto 4) — 4 milestones y 20 cards.
- **`MIL_B` / `PLAN_B`:** plan del concurso Gaudí Nexus (proyecto propio) — 6 milestones y 13 cards.
- **`_existing(proyecto)`:**Arma el mapa headline → id de las cards ya cargadas, para no duplicar en una
  segunda corrida.
- **`_id(salida)`:** la API devuelve el id recién creado como **array de un elemento** (`[458]`), no como
  entero: esta función lo normaliza.
- **`_crear_milestone(...)`:** `Tickets.quickAddMilestone` con `params.{headline,projectId,priority,status,
  dateToFinish,description,tags}`. El milestone nace con `sprint = 0` y se linkea al sprint después.
- **`_crear_card(...)`:** arma la card (`type: 'task'`) con milestone, sprint, estado, `planHours`
  (pomodoros × 0,42 h), `dateToFinish`, responsable en `editorId`, colaboradores en `collaborators` y el
  criterio de cierre en `acceptanceCriteria`. Después crea cada subtarea con **`addTicket` y
  `type: 'subtask'` + `dependingTicketId`** (la vía que acepta la API; `upsertSubtask` no funciona por RPC).
- **`main()`:** (1) repara el sprint 27 que había quedado vacío → `S1 Agentes + agenda Emilia`; (2) crea el
  proyecto del concurso con Emilia y Sol; (3) crea su sprint; (4) crea los milestones de cada plan; (5) crea
  las cards y sus subtasks; y guarda el estado final en JSON.
- **Higiene:** el token nunca sale del `.env` (lo lee `leantime_rpc`), y el vault guarda nombres e ids
  públicos de las cards, nunca secretos.
