# Sesión 2026-09-10 — AGENTS.md slim (plan 9 pasos, modo build)

## Fase previa (plan mode): revisión con Sol

- Auditoría read-only delegada a @vaultworm-arq: inventario por bloques, drift detectado (ComfyUI duplicado, árbol stale, 18 refs numéricas rotas), veredicto MANTENER/MOVER/BORRAR por bloque, outline slim ~90L, top 3 riesgos.
- Preguntas en terminal: tamaño slim ~90, borrar dup ComfyUI, migrar refs, unificar estándares.
- Revisión paso a paso P1–P9 con decisiones registradas (contexto íntegro, template ideal, merge frontmatter sin oficina, reglas partidas, pbook nuevo, BIM borrado, sección WF aparte, canónico interno/standares, agente tasks lo hace otro agente).

## Qué se hizo

- Revisión paso a paso con Sol (9 pasos, preguntas en terminal) → ejecución completa.
- AGENTS.md 393→125 líneas: contexto, árbol, frontmatter-detalle, glosario, workflows, BIM, ComfyUI dup, WF, scripts movidos a sus canónicos.
- Estándares unificados en `interno/standares/`; `wiki/estandares/00-index` redirige.
- 7 refs `AGENTS.md:NNN` → anchors estables. Auditoría: 268 links → 0 rotos, 0 `../`.
- Incidentes: edición que había borrado el árbol de estructura-carpetas (restaurado); `output`/`balcarce` verificados; audit mejorado (ignora código).

## Pendientes

- Minuta Balcarce recreada (la reorg la había eliminado) — vigilar que persista.
- Coordinar con el otro agente (ingest→tasks) para no duplicar con `pbk-agentes-vaultarq`.
- `log.md` mojibake + links viejos siguen pendientes de decisión explícita.

## Análisis cerebro digital (Karpathy)

- **Topics:** ninguno nuevo.
- **Entidades:** —.
- **Hechos:** AGENTS slim = boot+punteros; convención links ya en AGENTS (Nombrado); scripts de auditoría/reparo en Temp opencode (reutilizables para lint trimestral).
