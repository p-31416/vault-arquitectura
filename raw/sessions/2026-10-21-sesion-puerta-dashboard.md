---
tipo: log
fecha_creacion: 2026-10-21
ultima_actualizacion: 2026-10-21
tags: [dashboard, puerta, temas, reunion, vault, indice]
---

# Sesión 2026-10-21 (madrugada) — El dashboard general pasa a ser la puerta

## Qué se pidió

Sol: el "documento que engloba todo" debería ser **el dashboard** (`proyectos/STUDIO_OS-Emilia/presentacion/dashboard-mes1-emilia.html`), que ya es la entrada al resto (los otros 4 dashboards lo enlazan). Y dos aclaraciones:
- **los `.md` no hace falta que sean links** (se va a ver en otra computadora → lo que sirve es la ruta del vault);
- **después hay que subir todos los cambios a GitHub**.

## Qué se hizo

### 1. Nuevo script `scripts/inyectar-puerta-temas-dashboard.py` (+ `_notas.md`)

Inyecta en el dashboard general la sección **"la puerta"**: los 6 temas del estudio, y en cada uno el estado en una línea + las rutas del vault (como texto `<code>`, no links) + el link a su dashboard. Debajo, la franja con los **3 pendientes de la reunión con Emilia**. Además agrega la pestaña **"Temas"** al nav y la ruta del doc de la reunión a los `toplinks`.

Detalles que_costaron un segundo intento:

- **Idempotencia**: el bloque va entre marcadores `<!-- PUERTA-TEMAS -->` / `<!-- /PUERTA-TEMAS -->` y se borra antes de reinyectar → correrlo dos veces deja el HTML igual (verificado: 36541 → 36541 → 36541 bytes).
- **La ruta del doc de la reunión en los `toplinks`**: hay que buscarla **solo dentro del bloque `<p class="toplinks">`**. Con un `if ruta not in d` sobre todo el archivo daba falso positivo (la ruta ya estaba dentro de la sección de la puerta) y nunca se agregaba.
- El archivo puede venir con CRLF → el match es por regex, no por `replace` plano.

### 2. La sección quedó así (6 tarjetas, 3 columnas)

| Tema | Estado | Dashboard |
|---|---|---|
| Fuentes · AIxGaudi | 31 PDF → 32 fichas + 31 transcripciones; gate 0 listo, faltan los gates 1-3 | `dashboard-vault.html` |
| Agentes Telegram | bot con 2 flujos (Sol y Emilia) + despachador por `chat_id`; probado end-to-end | `dashboard-estudio-os.html` |
| CAD / SET | SET_01 replanteado con 2 playbooks, SET_02 y SET_03, dashboard v2 al día | `dashboard-autocad.html` |
| Comfy | 6 workflows (F-01..F-06) + LoRA rhino-to-image + 3 modelos con luz cálida | `dashboard-comfy.html` |
| Leantime | 2 planes (33 cards, 85 subtasks) + 15 h registradas; ítem `589` corpus → ChatGPT | — |
| Estudio · comercial | 1.800/trimestral, 60 h/mes, propuestas del viernes y del mes 2 | — |

### 3. Verificación

- `scripts/check-dashboard-css.py` → **0 clases sin estilo** ✓
- Captura con Chrome headless → la sección se ve bien, el nav muestra la pestaña "Temas" y el resto del dashboard quedó intacto ✓
- Los 4 dashboards **ya** enlazaban al mes1 (no hizo falta retrofit) ✓

### 4. Índice y subida

- `proyectos/STUDIO_OS-Emilia/00-index.md` → la sección "Documentación vigente" arranca ahora con el **dashboard general** como puerta ✓
- **Todos los cambios subidos a GitHub** (`master` → `origin`), que era lo que faltaba para poder ver el trabajo desde otra computadora.

## Archivos del vault

- `scripts/inyectar-puerta-temas-dashboard.py` + `_notas.md` (nuevos)
- `proyectos/STUDIO_OS-Emilia/presentacion/dashboard-mes1-emilia.html` (con la sección de la puerta)
- `proyectos/STUDIO_OS-Emilia/00-index.md` (el dashboard como primera entrada)

## Cerebro-digital

**Topics:** dashboard como puerta única · inyección idempotente en HTML · rutas del vault como texto (no links) · patrón `build-dashboard-semanas.py` replicado.

**Entidades:** `dashboard-mes1-emilia.html` (32 KB → 36,5 KB) · `scripts/inyectar-puerta-temas-dashboard.py` · marcadores `<!-- PUERTA-TEMAS -->` · `09-agenda-reunion-2026-10-21.md` · los 4 dashboards hermanos.

**Hechos verificados:** (1) el dashboard general es el único punto de entrada real: los otros 4 ya lo enlazan; (2) las rutas del vault se muestran como texto `<code>` porque el consumo es en otra máquina (Obsidian), y los dashboards sí como link porque son HTML autocontenidos que viajan con el repo; (3) el HTML del dashboard se regenera con scripts, así que cualquier sección nueva tiene que ser inyectable → de ahí el script en vez de editar a mano; (4) `check-dashboard-css.py` da 0 clases sin estilo tras la inyección.
