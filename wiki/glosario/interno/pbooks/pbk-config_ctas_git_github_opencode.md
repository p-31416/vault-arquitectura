---
tipo: playbook
seccion: infra-playbooks
fecha_creacion: 2026-09-08
ultima_actualizacion: 2026-09-08
tags: [git, github, opencode, cuentas, credenciales, perfiles, troubleshooting, infra]
---

# Playbook: Gestión y Separación de Cuentas (Git, GitHub, OpenCode)

- [[#Resumen de Identidades y Matriz de Cuentas]]
- [[#Capa 1: Git (Local, Global y IncludeIf)]]
- [[#Capa 2: GitHub CLI (gh y Tokens PAT)]]
- [[#Capa 3: OpenCode (Perfiles Aislados y Proveedores IA)]]
- [[#Flujo de Verificación Rápida (30 seg)]]
- [[#Uso Cruzado de Proveedores IA (Conexión y Desconexión)]]
- [[#Conceptos relacionados]]
- [[#Referencias]]

---

## Resumen de Identidades y Matriz de Cuentas

Para garantizar que los commits, pull requests y el consumo de modelos de IA no se mezclen entre organizaciones, el entorno de trabajo está dividido en **dos identidades totalmente independientes**:

| Parámetro | Cuenta 1: Proyecto Pi (Este Vault) | Cuenta 2: Pitautech |
| :--- | :--- | :--- |
| **Propósito** | Arquitectura, Vault de Estudio, IA aplicada | Tech, Vault Lidia, Desarrollos Generales |
| **Email** | `proyectopi.31416@gmail.com` | `pitau.tech@gmail.com` |
| **Git User** | `proyectopi` | `pitautech` |
| **GitHub Handle** | `p-31416` | `pitautech` |
| **Ruta Repositorios** | `P:\00-repos\proyecto-pi\` | `P:\00-repos\pitau-tech\` |
| **Perfil OpenCode** | `P:\00-repos\.opencode-profiles\proyecto-pi\` | `P:\00-repos\.opencode-profiles\pitau\` |
| **Archivo Secrets (.env)** | `P:\00-repos\proyecto-pi\vault-arquitectura\.env` | `P:\00-repos\pitau-tech\vault-lidia\.env` |

---

## Capa 1: Git (Local, Global y IncludeIf)

Git determina la autoría de los commits (`user.name` y `user.email`) mediante un sistema jerárquico de precedencia.

### Dónde se guardan las configuraciones

1. **Configuración Global (`C:\Users\Solch16\.gitconfig`)**:
   - Define el usuario base del sistema (`pitautech / pitau.tech@gmail.com`).
   - Contiene la directiva condicional:
     ```ini
     [includeIf "gitdir:P:/00-repos/proyecto-pi/"]
         path = P:/00-repos/.git-config-tokens/gitconfig-proyecto-pi
     ```
2. **Configuración Condicional (`P:\00-repos\.git-config-tokens\gitconfig-proyecto-pi`)**:
   - Sobrescribe automáticamente el usuario para cualquier repositorio dentro de `P:\00-repos\proyecto-pi\`:
     ```ini
     [user]
         name = proyectopi
         email = proyectopi.31416@gmail.com
     ```
3. **Configuración Local del Repositorio (`vault-arquitectura/.git/config`)**:
   - Sobrescribe cualquier valor global si se define explícitamente en el repositorio:
     ```ini
     [user]
         name = proyectopi
         email = proyectopi.31416@gmail.com
     ```

### Comandos de Verificación Git

```powershell
# Verificar usuario y email activos en el repo actual:
git config user.name
git config user.email

# Ver origen de cada configuración:
git config --show-origin user.name
```

---

## Capa 2: GitHub CLI (gh y Tokens PAT)

GitHub CLI (`gh`) gestiona la autenticación para interactuar con GitHub (crear PRs, issues, clonar repos privados).

### Dónde se guardan las credenciales

1. **Keyring de Windows / Config Global**:
   - `C:\Users\Solch16\AppData\Roaming\GitHub CLI\hosts.yml`
2. **Token local en repositorio (`.env`)**:
   - En `vault-arquitectura/.env`: `GH_TOKEN=ghp_...` (Token PAT clásico con scopes `repo, workflow, read:org, gist, read:user`).

> [!IMPORTANT]
> `gh` prioriza la variable de entorno `GH_TOKEN` sobre la sesión global guardada en el sistema.

### Comandos de Verificación GitHub CLI

```powershell
# Verificar cuenta activa en GitHub CLI:
gh auth status

# Si necesitas reautenticar con el token de .env:
Get-Content .env | gh auth login --with-token
```

---

## Capa 3: OpenCode (Perfiles Aislados y Proveedores IA)

OpenCode almacena la configuración de sesiones, bases de datos locales, historial y credenciales en carpetas de perfiles independientes.

### Dónde se guardan las credenciales y perfiles

1. **Perfil Proyecto Pi**:
   - **Ruta Base**: `P:\00-repos\.opencode-profiles\proyecto-pi\`
   - **Credenciales activas**: `P:\00-repos\.opencode-profiles\proyecto-pi\data\opencode\auth.json`
   - **Logs de ejecución**: `P:\00-repos\.opencode-profiles\proyecto-pi\data\opencode\log\opencode.log`
   - **Configuración JSON**: `P:\00-repos\.opencode-profiles\proyecto-pi\config\opencode\opencode.jsonc`

2. **Perfil Pitautech**:
   - **Ruta Base**: `P:\00-repos\.opencode-profiles\pitau\`
   - **Credenciales activas**: `P:\00-repos\.opencode-profiles\pitau\data\opencode\auth.json`
   - **Logs de ejecución**: `P:\00-repos\.opencode-profiles\pitau\data\opencode\log\opencode.log`

3. **Variables de Entorno Locales (`.env`)**:
   - `vault-arquitectura/.env`:
     ```env
     OPENCODE_API_KEY=sk-...
     ```

### Comandos de Verificación OpenCode

```powershell
# Listar credenciales y variables detectadas en la sesión actual:
opencode auth list

# Ver contenido del archivo auth.json de Proyecto Pi:
Get-Content P:\00-repos\.opencode-profiles\proyecto-pi\data\opencode\auth.json
```

---

## Flujo de Verificación Rápida (30 seg)

Ejecutar estos comandos en la terminal de `vault-arquitectura` para validar que todo el stack esté enlazado a **Proyecto Pi**:

```powershell
# 1. Validar Git
Write-Host "--- GIT ---" -ForegroundColor Cyan
git config user.email

# 2. Validar GitHub CLI
Write-Host "--- GITHUB CLI ---" -ForegroundColor Cyan
gh auth status

# 3. Validar OpenCode
Write-Host "--- OPENCODE ---" -ForegroundColor Cyan
opencode auth list
```

**Resultado esperado**:
- Git: `proyectopi.31416@gmail.com`
- GitHub CLI: Logged in to `github.com` account `p-31416`
- OpenCode: Credentials `...proyecto-pi\data\opencode\auth.json`

---

## Uso Cruzado de Proveedores IA (Conexión y Desconexión)

Si necesitas utilizar temporalmente una cuenta con suscripción o créditos (por ejemplo, **OpenCode Go** o **Anthropic** de Pitautech) dentro del vault de arquitectura:

### 1. ¿Qué sucede al conectar una cuenta externa en este vault?
- **El consumo de tokens**: Se descuenta del saldo/plan de la cuenta proveedora (ej. Pitautech).
- **El código y repositorios**: Permanecen 100% aislados bajo Proyecto Pi. La clave sólo se guarda en `P:\00-repos\.opencode-profiles\proyecto-pi\data\opencode\auth.json`.
- **Git y GitHub**: No se modifican en absoluto.

### 2. Cómo desconectar o limpiar la cuenta externa

#### Método A: Desde CLI (Recomendado)
```powershell
opencode auth logout
```
*Seleccionar el proveedor (`opencode-go`, `opencode`, etc.) con las flechas y presionar Enter.*

#### Método B: Limpieza manual del archivo de autenticación
Editar `P:\00-repos\.opencode-profiles\proyecto-pi\data\opencode\auth.json` y remover la clave o restaurar:
```json
{
  "opencode": {
    "type": "api",
    "key": "sk-vXkO3E3txydee95ByjhoYTEFFkvciGjX0rpDGJqQNLvxHtFF5ZtvnXlPZMxMVuIm"
  }
}
```

#### Método C: Desde la interfaz interactiva
Dentro de OpenCode, escribir `/connect` y seleccionar el proveedor a remover o reconfigurar.

---

## Conceptos relacionados

- [[wiki/glosario/software/git|Git: Precedencia de Configuración e IncludeIf]]
- [[wiki/glosario/software/github-cli|GitHub CLI: Manejo de Tokens y Autenticación]]
- [[wiki/glosario/software/opencode|OpenCode: Gestión de Perfiles y Proveedores]]
- [[wiki/glosario/interno/pbooks/pbk-troubleshooting-reconexion|Playbook: Troubleshooting y Reconexión]]

---

## Referencias

- Documentación oficial OpenCode Providers & Auth: https://opencode.ai/docs/providers
- GitHub CLI Manual (`gh auth`): https://cli.github.com/manual/gh_auth
- Git Documentation (`includeIf`): https://git-scm.com/docs/git-config#_conditional_includes
