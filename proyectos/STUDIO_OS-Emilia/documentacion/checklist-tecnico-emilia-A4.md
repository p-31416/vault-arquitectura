---
tipo: checklist
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fecha: 2026-09-15
version: 1.3
tags: [checklist, tecnico, instalacion, inventario, disco, remoto]
---

# Checklist técnico — Visita 14:30-18:30 · STUDIO OS Emilia — v1.3

> Imprimir 1 carilla A4 · Tildar con birome · Dejar 1 copia en estudio + 1 para tu `raw/sessions/`
> Playbook completo: `playbook-instalacion-windows-emilia.md` v1.3

Fecha: ____/____/________  Máquinas: [ ] Notebook Emilia  [ ] PC01  [ ] PC02  Técnico: ___________

---

## 1) Inventario (30 min) — PowerShell Admin

```powershell
powershell -ExecutionPolicy Bypass -File E:\scripts\inventario-hardware.ps1
# o si ya hay vault: P:\00-repos\proyecto-pi\vault-arquitectura\scripts\inventario-hardware.ps1
```

Manual si falla:

```powershell
systeminfo | findstr /I "OS RAM"
wmic logicaldisk get size,freespace,caption,mediatype
fsutil volume diskfree C:
Get-PhysicalDisk | Select-Object Model,MediaType,BusType,Size,HealthStatus
Get-ChildItem C:\Users\Emilia\Downloads -Recurse -File -EA SilentlyContinue | Measure-Object -Property Length -Sum | Select @{N='GB';E={[math]::Round($_.Sum/1GB,2)}},Count
Get-Item C:\hiberfil.sys -EA SilentlyContinue | Select @{N='GB';E={[math]::Round($_.Length/1GB,2)}}
echo $env:OneDrive
```

| Máquina | CPU | RAM total/libre/slots | GPU + VRAM | Disco tipo (NVMe/SATA/HDD) | C: libre | OneDrive | hiberfil |
|---|---|---|---|---|---|---|---|
| Notebook | ___ | ___GB / ___GB / ___ slots | ___ / ___GB | ___ / ___GB ___ | ___GB ___% | ___GB | ___GB |
| PC01 | ___ | ___GB / ___GB / ___ slots | ___ / ___GB | ___ / ___GB ___ | ___GB ___% | ___GB | ___GB |
| PC02 | ___ | ___GB / ___GB / ___ slots | ___ / ___GB | ___ / ___GB ___ | ___GB ___% | ___GB | ___GB |

- [ ] `.md + .json` en `raw/sessions/` por máquina  - [ ] Foto almacenamiento antes

---

## 2) Disco (40 min) — NADA sin backup

**Foto antes:** C: libre ___GB (___%)  Descargas ___GB (___arch)  TEMP ___GB  hiberfil ___GB

```powershell
# Solo lectura
wmic logicaldisk get size,freespace,caption
Get-ChildItem C:\Users\Emilia\Downloads -Recurse -File -EA SilentlyContinue | Measure-Object -Property Length -Sum | Select @{N='GB';E={[math]::Round($_.Sum/1GB,2)}},Count
Get-Item C:\hiberfil.sys -EA SilentlyContinue | Select @{N='GB';E={[math]::Round($_.Length/1GB,2)}}
# Limpieza segura (tras backup a OneDrive/Drive/USB)
cleanmgr /sageset:1; cleanmgr /sagerun:1
Remove-Item -Recurse -Force $env:TEMP\* -EA SilentlyContinue
Remove-Item -Recurse -Force C:\Windows\Temp\* -EA SilentlyContinue
Remove-Item -Recurse -Force C:\Windows\SoftwareDistribution\Download\* -EA SilentlyContinue
# Solo si hiberfil >4GB y no hiberna y C:<20% libre
powercfg -h off
```

- [ ] Backup Descargas → OneDrive/Drive/USB (preguntar)  - [ ] `cleanmgr` + TEMP vaciado  - [ ] Storage Sense ON (semanal)  - [ ] Papelera vaciada (preguntar)

**Foto después:** C: libre ___GB (___%) → ganancia ___GB  - [ ] Reinicio ok <60s

---

## 3) Stack mínimo (60 min, con internet del estudio)

```powershell
winget install Git.Git
winget install GitHub.cli
winget install OpenJS.NodeJS.LTS
winget install Obsidian.Obsidian
winget install Google.GoogleDrive

git --version; gh --version; node -v; npm -v
git config --global user.name "Emilia Pimenta"
git config --global user.email "emilia@estudio.com"
gh auth login      # HTTPS → browser
gh auth status
where git; where gh; where node

npm install -g opencode
opencode --version; opencode auth list
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
# o: npm install -g @openai/codex
codex --version; codex auth status   # Sign in with ChatGPT
antigravity --version 2>&1 | Select -First 1
```

| Herramienta | Comando verificación | OK |
|---|---|---|
| Git | `git --version` >=2.23 | [ ] ___ |
| gh CLI | `gh auth status` logueado | [ ] ___ |
| Node | `node -v; npm -v` | [ ] ___ |
| Obsidian | abre `vault-emilia` piloto | [ ] ___ |
| Opencode | `opencode --version` | [ ] ___ |
| Codex | `codex --version` + login | [ ] ___ |
| Antigravity | `antigravity --version` | [ ] ___ / no instalado Fase2 |
| Drive | `where GoogleDriveFS` + Stream | [ ] ___ |

- [ ] Vault piloto `P:\vault-emilia` (o `D:\vault-emilia`) creado + `00-index.md` con wikilink ok
- [ ] 1 prompt lectura: `codex exec "lista los .md"` ok

---

## 4) Arquitectura (5 min, solo anotar)

AutoCAD ver ___  Lumion ___  Revit ___  Rhino8 ___  Office365/GWorkspace ___  Adobe ___

---

## 5) Remoto — Chrome Remote Desktop (10 min)

Chrome logueado con `vault.emilia.estudio@gmail.com` → https://remotedesktop.google.com/access → Configurar acceso remoto → PIN 6 dígitos

- [ ] CRD online: `Notebook-Emilia` PIN: ______  `PC01` PIN: ______
- [ ] Probado desde tu PC → ves escritorio  - [ ] Quick Assist probado (Win+S → Asistencia rápida → código 6 dígitos)

**Anotar en tu vault (no en su PC):**

```
CRD: vault.emilia.estudio@gmail.com / Notebook PIN:______ PC01 PIN:______ / Horario:______
Quick Assist: código por sesión
```
> PCs deben quedar prendidas (notebook tapa abierta "no suspender" + desktops sin suspensión).

---

## 6) Cierre — entregable tildable

- [ ] Inventario `.md+.json` por máquina en `raw/sessions/`  - [ ] C: antes ___GB → después ___GB
- [ ] git/gh/node/obsidian/opencode/codex/antigravity ok  - [ ] Drive Stream `00-PROYECTOS/` vacío  - [ ] CRD PIN en tu vault + Quick Assist ok
- [ ] Decisiones: Codex principal + Opencode fallback  / vault-emilia GitHub privado esta semana / imágenes vía Drive (no en git)
- [ ] Pendientes: Python, Pandoc/FFmpeg/OBS, Fathom + Leantime VPS (vos creas acceso)
- [ ] Próximos: S1 Vault vivo Nayara + S2 referentes + S3 estándares CAD

Firma Emilia: _________________  Firma técnico: _________________  Hora cierre: _______
