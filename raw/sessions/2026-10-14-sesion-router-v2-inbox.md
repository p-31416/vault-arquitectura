---
tipo: log
fecha: 2026-10-14
tags: [sesion, inbox, router-v2, voz, telegram, n8n, sheet]
---

# Sesión 2026-10-14 — Router v2 + inbox Fuentes (grupo os.emi-fuentes)

## Qué quedó funcionando

- **Router v2** (`YWpuV5p0vCDTbIHz`, 17 nodos): trigger único → `Route Identidad` (Sol→voz, resto→Fuentes→comandos legacy).
- **Voz a subflujo**: trigger propio eliminado de `Gpd6NHB4HQdU7ary` (publicado sin trigger); `Detectar Entrada` desempaqueta `update`; fix memoria `sessionKey` → trigger nuevo. Exec 3708 SUCCESS (voz responde en privado ✓).
- **Inbox**: grupo `-5417177870` cableado; `Has Link` → `Prepara Fila` (Set sin funciones) → `Append Fuentes HTTP` (API directa A:I) → Ack. Exec 3715 SUCCESS 0.8s.
- **Sheet** `18iDrvNUOApNFsEDDQ4rMMo40cw4t0hn3CApLK9iLpvI`: header A1:I1 reescrito por API tras detectar automap corrupto (`headers/query/body`).
- **Spec** `specs/261013-plan-fuentes-emilia-inbox.md` + §9 rama inbox.

## Qué sigue roto / pendiente mañana

1. Usuario reporta "sigue tirando error" sin ejecución nueva posterior a 3715 → verificar QUÉ error ve (texto del bot, celda del Sheet o ack). Pedir captura o texto exacto.
2. Tipos en Set reducidos a YT/WEB (ampliar IG/SHARE/LIBRO solo con ops sin funciones: `indexOf` + ternarios).
3. Regla de convivencia documentada: **1 trigger Telegram por token** (el Voz TEST robaba el webhook; su sticky ya lo advertía). No activar triggers paralelos con misma cred.
4. Lección n8n: ediciones crean BORRADOR (hay que publicar para activar); `update_workflow` con regex/backslash en payload falla parse (usar paths o payloads simples); expresiones n8n NO aceptan `function`/`for`/`var` (solo métodos + ternarios + `??`); no editar con el editor UI abierto (bloqueo).
5. Rutina 07:00 + digest (corte 1) pendiente. Sheet: mover a `OS-Emilia/` + compartir con Emilia (ella edita E+F).
6. Cierre: archivar workflows TMP restantes si los hubiera; pancarta `raw/entradas-emilia/` aún no creada (inbox va directo al Sheet por ahora).

## Cerebro-digital

- Topics: webhook-steal-mismo-token, draft-vs-active-n8n, expression-subset-sin-funciones, automap-sheet-corrupto, group-privacy-telegram.
- Entidades: Router YWpuV5p0vCDTbIHz, Voz Gpd6NHB4HQdU7ary, grupo os.emi-fuentes (-5417177870), Sheet Fuentes-Inbox.
- Hechos: chat_id grupo descubierto vía ejecución 3710; exec 3715 primer SUCCESS punta a punta; usuario lee terminal sin scroll (micro-pantallas + question).
