---
tipo: plan
mvp: 07
cliente: Estudio (interno)
proyecto: Studio OS — sistema operativo para un estudio de arquitectura
fecha_creacion: 2026-10-28
ultima_actualizacion: 2026-10-28
estado: activo
tags: [mvp_07, studio-os, f0, comandos, vps, tailscale, hermes, git]
idioma: es
---

# F0 · comandos, paso a paso

> Guía ejecutable de la primera fase: [[proyectos/MVP_07-studio-os-sistema/02-ft-mvp_07|02-ft-mvp_07]] §F0. Cada paso dice **qué hacer**, **cómo se verifica** y **cómo se deshace**.
> Regla: los pasos que requieren `s` se hacen de a uno. Nada de este documento se ejecuta solo.

- [[#Paso 1 · Inventario del VPS]]
- [[#Paso 2 · Remoto canónico del vault]]
- [[#Paso 3 · Tailscale en el VPS]]
- [[#Paso 4 · Servicio Hermes]]
- [[#Paso 5 · Setup, modelo y MCP de n8n]]
- [[#Paso 6 · SOUL, skills y lectura del vault]]
- [[#Paso 7 · Cierre de F0]]

---

# Paso 1 · Inventario del VPS

**Qué hace:** deja el baseline de RAM, disco, contenedores y carga. Nada más.

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_verificar_vps.py
```

**Verificar:** el veredicto dice si entran los 3 GB de Hermes con margen.

**Deshacer:** nada que deshacer (es lectura).

**Notas:** `scripts/studio_os_verificar_vps_notas.md`

---

# Paso 2 · Remoto canónico del vault

**Qué hace:** el VPS deja de depender de GitHub para leer el vault. GitHub queda como espejo (ADR [[specs/ADR-2026-10-28-vault-canónico-en-vps|vault canónico]]).

**2.1 · Crear el repositorio bare en el VPS**

```powershell
ssh contabo "mkdir -p /srv/git && git init --bare --initial-branch=master /srv/git/vault-arquitectura.git"
```

**2.2 · Publicar el vault actual hacia el VPS** (desde la raíz del repo, en `P:`)

```powershell
git remote add vps ssh://root@89.117.73.109/srv/git/vault-arquitectura.git
git push vps master
```

**2.3 · Clon de trabajo en el VPS**

```powershell
ssh contabo "git clone /srv/git/vault-arquitectura.git /srv/vault/work"
```

**2.4 · Espejo en GitHub** (el repo privado que ya existe, `p-31416/vault-arquitectura`)

```powershell
git push origin master
```

**Verificar:**

```powershell
ssh contabo "cd /srv/vault/work && git log --oneline -3 && ls"
```

Deberías ver los mismos commits que en `P:`. **Ojo:** el vault tiene `/activos/` en `.gitignore`, así que los binarios **no** viajan: solo texto y referencias.

**Deshacer:**

```powershell
git remote remove vps
ssh contabo "rm -rf /srv/git/vault-arquitectura.git /srv/vault/work"
```

---

# Paso 3 · Tailscale en el VPS

**Qué hace:** la red privada que une VPS, banco y estudio. Sin puertos abiertos.

**3.1 · Instalar**

```powershell
ssh contabo "curl -fsSL https://tailscale.com/install.sh | sh"
```

**3.2 · Conectar (imprime una URL para autorizar)**

```powershell
ssh contabo "sudo tailscale up"
```

Abrí la URL que imprime en el navegador y autorizá el nodo.

**3.3 · Desactivar la expiración de clave** (es un servidor: no debe dejar de autenticarse solo)

En `https://login.tailscale.com/admin/machines` → ícono `…` del nodo del VPS → **Disable key expiry**.

**3.4 · Verificar**

```powershell
ssh contabo "tailscale status && tailscale ip"
```

**Deshacer:**

```powershell
ssh contabo "sudo tailscale logout"
```

---

# Paso 4 · Servicio Hermes

**Qué hace:** el agente como servicio Swarm, con volumen nombrado, límite de 3 GB y **cero puertos publicados**.

**4.1 · EasyPanel** → *Add Service* → *Compose* → pegá el bloque de `deploy/hermes.compose.yml` → Deploy.

**4.2 · Verificar**

```powershell
ssh contabo "docker service ls | grep -i hermes"
ssh contabo "docker stats --no-stream --format '{{.Name}}|{{.MemUsage}}' | grep -i hermes"
ssh contabo "docker logs --tail 40 <servicio-hermes>"
```

**4.3 · Comprobar la RAM después de instalar**

```powershell
P:\Anaconda\envs\comfyenv\python.exe scripts\studio_os_verificar_vps.py
```

**Deshacer:** EasyPanel → servicio → *Delete*. El volumen se borra con `docker volume rm <volumen>`.

**Notas:** `deploy/hermes.compose.yml`

---

# Paso 5 · Setup, modelo y MCP de n8n

**Qué hace:** el agente queda con identidad, modelo y acceso a los flujos deterministas de n8n.

**5.1 · Setup interactivo** (necesita terminal real: `ssh contabo`, nunca la consola web del VPS)

```powershell
ssh contabo "docker exec -it hermes hermes setup"
```

**5.2 · Modelo** — dos caminos:

| Opción | Cómo | Cuándo |
|---|---|---|
| **OpenRouter** (recomendado) | `hermes config set model openrouter/<modelo>` + `hermes config set OPENROUTER_API_KEY sk-or-…` | el agente razona sobre código y documentos: la calidad importa, y OpenRouter ya está declarado como subencargado en la política de privacidad |
| **Ollama local en el VPS** | `hermes config set model ollama/<modelo>` | tareas mecánicas y baratas. **Ojo:** el VPS tiene 8 GB y Ollama ahí compite por la RAM con Hermes y n8n |

**5.3 · MCP de n8n**

```powershell
ssh contabo "docker exec -it hermes hermes mcp install n8n-official"
```

Pedirá la URL del servidor: `https://n8n.pitau.tech/mcp-server/http` y luego el **OAuth**. Como el VPS es headless, el flujo es *paste-back*: copiá la URL de autorización en tu navegador, autorizá, y cuando el navegador falle al volver (es normal), copiá la URL de la barra y pegala en la terminal.

**Verificar:**

```powershell
ssh contabo "docker exec hermes hermes mcp test n8n"
ssh contabo "docker exec hermes hermes chat -q 'Listá los workflows de n8n'"
```

**Deshacer:** `hermes mcp disable n8n` (o `hermes mcp uninstall n8n-official`).

---

# Paso 6 · SOUL, skills y lectura del vault

**Qué hace:** el agente deja de ser un chat genérico y empieza a ser **el agente del estudio**.

**6.1 · Fuente de verdad en el vault** (versionada, revisable):

| Qué | Dónde va en el vault | Dónde vive en el agente |
|---|---|---|
| Identidad y reglas | `proyectos/MVP_07-studio-os-sistema/hermes/SOUL.md` | `/opt/data/SOUL.md` |
| Habilidades | `proyectos/MVP_07-studio-os-sistema/hermes/skills/<nombre>/SKILL.md` | `/opt/data/skills/<nombre>/` |

El agente redacta los borradores (ya hay un `SOUL.md` de partida en `01-spec-mvp_07.md` §6); vos los revisás y los publicás.

**6.2 · Publicar en el volumen**

```powershell
scp proyectos/MVP_07-studio-os-sistema/hermes/SOUL.md contabo:/srv/vault/work/proyectos/MVP_07-studio-os-sistema/hermes/SOUL.md
ssh contabo "docker exec hermes cp /vault/proyectos/MVP_07-studio-os-sistema/hermes/SOUL.md /opt/data/SOUL.md"
```

(El `cp` desde `/vault` es de solo lectura en el vault y escribe solo en el volumen del agente.)

**6.3 · Skill de lectura del vault**

MCP filesystem **de solo lectura** sobre `/vault`:

```yaml
mcp_servers:
  vault:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/vault"]
```

**6.4 · Verificar**

```powershell
ssh contabo "docker exec hermes hermes chat -q 'Leé /vault/AGENTS.md y decime en una línea qué reglas rigen este vault'"
```

**Deshacer:** sacar el bloque `vault:` de `config.yaml` y recargar (`/reload-mcp`).

---

# Paso 7 · Cierre de F0

**7.1 · Reiniciar el servicio y comprobar que la memoria persiste**

```powershell
ssh contabo "docker service restart <servicio-hermes>"
ssh contabo "docker exec hermes hermes chat -q '¿Qué reglas de operación tenés?'"
```

Si la respuesta incluye las reglas del `SOUL.md`, la persistencia funciona.

**7.2 · Registrar el resultado**

- `proyectos/MVP_07-studio-os-sistema/03-log-mvp_07.md` (se abre con este paso)
- `log.md` (entrada nueva arriba)
- `raw/sessions/YYYY-MM-DD-sesion-*.md` (cierre de sesión)

**7.3 · Criterio de cierre de F0**

- [ ] Hermes responde por API/CLI con el vault montado
- [ ] La memoria persiste tras reiniciar el servicio
- [ ] El MCP de n8n lista los workflows
- [ ] La RAM disponible del VPS sigue **por encima de 1 GB**
- [ ] **Telegram sigue intacto**: el bot de n8n no se tocó
