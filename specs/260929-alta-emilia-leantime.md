---
tipo: metodologia
fecha_creacion: 2026-09-29
ultima_actualizacion: 2026-09-29
tags: [emilia, leantime, studio-os, accesos, plan]
idioma: es
estado: plan
---

# Alta Emilia en Leantime — spec para el 2026-09-29

> Objetivo: Emilia accede a `STUDIO_OS-Emilia` en `https://pitau.tech` con rol lectura y visualiza tareas, subtareas, Goals, Milestones y completados.

## 1. Contexto verificado el 2026-09-28

- Puente MCP local ok: `P:/00-repos/npm-global/node_modules/leantime-mcp/bin/leantime-mcp.js` presente, `LEANTIME_TOKEN` en env (68 chars, valor nunca impreso), config en `opencode.json:33-36` hacia `https://pitau.tech/mcp`.
- Payload existente fuera de git: `P:\00-repos\pitau-tech\user-emilia.json` con `arq.emiliapimentalombardi@gmail.com` / Emilia Pimental Lombardi / `member`.
- Servicio remoto en revisión: `GET https://pitau.tech/` → 404 Laravel, `POST https://pitau.tech/mcp` con JSON válido → `{"error":"Not found"}`. `https://n8n.pitau.tech/` → 200, el VPS vive. Ver plan vigente en [[specs/260924-plan-os-emilia-n8n|Plan OS-Emilia n8n]] y criterio PM en [[wiki/glosario/interno/pbooks/pbk-pm_vault|pbk-pm_vault]].
- Decisión de acceso: rol `Read-Only` a nivel compañía, asignada solo a `STUDIO_OS-Emilia` con `inherit`. Si aporta comentarios, subir a `Commenter` solo en ese proyecto.

## 2. Pre-requisitos (2 min)

1. Login Owner/Admin en `https://pitau.tech`.
2. Proyecto `STUDIO_OS-Emilia` visible con contenido (tablero + Goals + Milestones).
3. Invite al mail contractual: `arq.emiliapimentalombardi@gmail.com`.

## 3. Paso 1 — Verificar servicio (5 min)

1. Abrir `https://pitau.tech/` y confirmar que ya no devuelve 404.
2. En EasyPanel: servicio Leantime en marcha, ruta `/mcp` enrutable, plugin MCP Server activo.
3. Prueba rápida:
```powershell
& curl.exe --insecure -s -o NUL -w "%{http_code}" "https://pitau.tech/mcp" --max-time 10
```
Incluye avance cuando devuelve 200/400 con cuerpo JSON (señal de Fastify activo) en lugar del 404 Laravel.

## 4. Paso 2 — Alta (10 min, Opción A UI recomendada)

1. `https://pitau.tech` → icono compañía → `User Management → Add User`.
2. Nombre: `Emilia Pimenta` / Apellido: `Lombardi` / Email: `arq.emiliapimentalombardi@gmail.com` / Rol: `Read-Only` / Proyecto: `STUDIO_OS-Emilia` → `Invite user`.
3. Entrar a `STUDIO_OS-Emilia` → `Project Settings → Team` → tildar Emilia → rol `inherit` → `Save`.

### Opción B — MCP / API (2 min, cuando el servicio responde)

Payload de referencia `P:\00-repos\pitau-tech\user-emilia.json`:
```json
{
  "firstname": "Emilia",
  "lastname": "Pimenta",
  "email": "arq.emiliapimentalombardi@gmail.com",
  "role": "readonly",
  "projects": ["STUDIO_OS-Emilia"]
}
```

Comando exacto (usa env, evita exponer secreto):
```powershell
.\with-env.ps1 powershell -NoProfile -File ./create-user-emilia-fixed.ps1
```

Donde `create-user-emilia-fixed.ps1` replica `create-user-emilia.ps1:1-12` con esta mejora:
```powershell
$headers = @{ Authorization = "Bearer $env:LEANTIME_TOKEN"; 'Content-Type' = 'application/json' }
$body = Get-Content 'P:\00-repos\pitau-tech\user-emilia.json' -Raw
Invoke-RestMethod -Uri 'https://pitau.tech/api/users' -Method Post -Headers $headers -Body $body
```

Equivalente MCP cuando el remoto responde:
`users.create { email, role: readonly }` → `projects.addUser { STUDIO_OS-Emilia, inherit: true }`.

Oportunidad de higiene: rotar el token expuesto en `create-user-emilia.ps1:4` tras el alta.

## 5. Paso 3 — Verificación de lectura con Emilia (15 min)

1. Emilia acepta invite → login → solo ve `STUDIO_OS-Emilia`.
2. Checklist visible:
- Kanban `Backlog → Sprint actual → En curso → Revisión → Hecho ✓`.
- Abre 1 task con 2 subtareas pomodoro (regla ≤25 min).
- `Goals` con O1/O2/O3 del Mes 1 y KR linkeados.
- `Milestones` M1-M4 en Gantt.
- Filtro `Hecho` muestra completados.
3. Registrar en `log.md` (solo añade entrada nueva arriba) + nota `raw/sessions/2026-09-29-sesion-alta-emilia-leantime.md` con resultado y análisis cerebro-digital.

## 6. Criterio de cierre

Alta completa cuando Emilia abre tablero, 1 task con subtareas, Goals, Milestones y vista de completados sin permisos de edición ni visibilidad de otros clientes.
