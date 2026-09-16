---
tipo: metodologia
fecha_creacion: 2026-09-09
ultima_actualizacion: 2026-09-09
tags: [github-actions, agentes, opencode, vaultworm-arq, online, backlog]
origen: decision SOL 2026-09-09 — backlog recuperable, NO en n8n.md
estado: backlog
---

# Spec — Agentes del vault corriendo online (GitHub Actions, sin VPS)

> **Objetivo:** que `@vaultworm-arq` (y futuros agentes) se ejecuten en la nube cuando la PC no está online — sin instalar nada en un VPS. Backlog pendiente, recuperable.

## 0. Resumen en 1 línea

Workflow `.github/workflows/vaultworm-arq.yml` (schedule diario 23:00 AR + `workflow_dispatch`) corre `npx opencode run "@vaultworm-arq digest"` en un runner GitHub con `OPENCODE_API_KEY` como secret → commitea `raw/vaultworm-arq/digest-YYYY-MM-DD.md` → SOL revisa a la mañana.

## 1. Por qué GitHub Actions y no VPS ni n8n

| Opción | Costo | Cuándo corre | Veredicto |
|---|---|---|---|
| PC local (cron/schedule) | 0 | Solo PC encendida | Actual — no cubre PC apagada |
| VPS propio | ~US$5/mes + mantenimiento | Siempre | Descartado — overkill para 1 digest/día |
| n8n Cloud/túnel | Config webhook + secreto | Siempre | Descartado — el túnel local (`ngrok`) es infra efímera; n8n queda solo como integración futura documentada en `telegram.md` |
| **GitHub Actions** | **0 (minutos free tier sobran)** | **Schedule + manual** | **Elegido (backlog)** |

## 2. Arquitectura

```
[schedule cron 0 2 * * * (23:00 AR) | workflow_dispatch manual]
   ↓
[GitHub runner ubuntu-latest]
   ├─ secrets: OPENCODE_API_KEY (repo secret, nunca hardcodear)
   ├─ run: npx opencode run "@vaultworm-arq digest"
   └─ commit: raw/vaultworm-arq/digest-YYYY-MM-DD.md (sin auto-push a main — PR o push directo según decida SOL)
```

## 3. Secrets y seguridad

- `OPENCODE_API_KEY` → repo secret (Settings → Secrets → Actions). Patrón `{env:}` como en local.
- `GH_TOKEN` → `secrets.GITHUB_TOKEN` automático (commit del digest).
- `TELEGRAM_BOT_TOKEN` (futuro, envío PDF): repo secret, solo cuando se active el loop digest→PDF→Telegram.

## 4. Criterios de aceptación (para recuperar este backlog)

- [ ] Workflow corre en schedule sin intervención y genera el digest del día
- [ ] `workflow_dispatch` permite digest on-demand desde la pestaña Actions
- [ ] El commit queda trazable (1 digest/día, formato UNICO/día)
- [ ] No se expone ninguna key en logs (usar `::add-mask::` si se ecoea)
- [ ] Costo: dentro del free tier (2000 min/mes — un digest consume ~2-5 min)

## 5. Relación con el vault

- Agente: ver `.opencode/agents/vaultworm-arq.md` (misión, triggers, permisos)
- Registro de agentes: futuro `pbk-agentes-vaultarq` (decisión SOL 2026-09-09)
- Digest diario: `raw/vaultworm-arq/digest-YYYY-MM-DD.md` (cadencia 1 vez/día, decisión 2026-09-07)
- No duplicar en `wiki/glosario/software/n8n.md` — decisión explícita SOL
