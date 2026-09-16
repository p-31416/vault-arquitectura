---
tipo: metodologia
proyecto: STUDIO_OS-Emilia
cliente: Emilia Pimenta
fase: briefing
fecha_creacion: 2026-09-15
ultima_actualizacion: 2026-09-16
tags: [studio-os, playbook, instalacion, windows, optimizacion-disco, onboarding, inventario-portable, acceso-remoto, checklist-tecnico, portable]
estado: vigente
version: 1.4
origen: 04-plan-studio-os.md + specs/260910-plan-trimestral-unificado + scripts/inventario-portable.ps1
idioma: es
---

# Playbook tecnico -- Instalacion minima Windows -- STUDIO OS Emilia -- v1.4 (portable)

> **Visita 14:30-18:30 (3-4hs). Objetivo manana: minimo viable para que Emilia empiece a usar el vault.**
> **NO es vault-arquitectura.** Esta semana disenas vault privado nuevo `vault-emilia` (GitHub privado) compartido con ella. Manana solo dejas base instalada + inventario tomado.
> **Principio:** binarios nunca en git (`activos/` gitignored), solo referencias `activos/proyectos/...` o `C:\BIM\...` [[wiki/glosario/interno/standares/oficina/estructura-carpetas|estructura-carpetas]].
> **Sin ComfyUI manana.** Sin tunel manana. PC debe quedar prendida para remoto (notebook y desktops).

---

## 0. Que llevar y que NO llevar

**Llevar (liviano):**
- USB con `scripts/inventario-portable.ps1` + `scripts/INVENTARIO-Portable-RUN.bat` (o `.lnk`) -- version portable, genera .md + .txt al lado del script -- + este playbook impreso + birome
- Cable/adaptador notebook + zapatilla

**NO llevar installers pesados:** se descargan alla con el internet del estudio via `winget`. Solo si el wifi es malo, usar USB como fallback.

**Links que usaras alla:**
- Git https://git-scm.com/download/win -- GH CLI https://cli.github.com/
- Obsidian https://obsidian.md/download
- Node LTS https://nodejs.org/ (para opencode/codex)
- Opencode https://opencode.ai/docs/providers
- Codex https://github.com/openai/codex -- install `irm https://chatgpt.com/codex/install.ps1 | iex` -- guia Windows https://developers.openai.com/codex/windows
- Chrome Remote Desktop https://remotedesktop.google.com/access

---

## 1. Inventario hardware -- REGISTRAR TODO (30 min, hacer PRIMERO, sin tocar)

> Correr en cada maquina: su notebook + cada desktop del estudio. Un `.md + .txt` por maquina **al lado del script** (pendrive o Escritorio). Ideal para llevarte datos.

### 1.1 Script portable (PowerShell como Admin, doble-click)

**Opcion A -- Doble-click (recomendada):**
- Copia al pendrive o Escritorio: `inventario-portable.ps1` + `INVENTARIO-Portable-RUN.bat` (misma carpeta)
- Doble-click en `INVENTARIO-Portable-RUN.bat` (o click derecho -> Ejecutar como administrador para datos completos NVMe/bateria)
- Genera `2026-09-16_14-30-inventario-NOMBREPC.md` + `.txt` al lado del script y abre el `.txt` solo en Bloc de notas
- Queda pausado con `Presiona Enter para cerrar...`

**Opcion B -- Comando manual (si el doble-click abre VS Code):**
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "E:\inventario-portable.ps1"
# o si esta en el vault:
powershell -NoProfile -ExecutionPolicy Bypass -File "P:\00-repos\proyecto-pi\vault-arquitectura\scripts\inventario-portable.ps1"
```

**Que captura v1.4 portable (basico, consumo en reposo):**
- Windows version/build, CPU (nucleos/hilos + % carga actual), RAM total/libre/% en uso + por slot
- GPU + VRAM + driver + resolucion
- Discos logicos (libre/total) + fisicos tipo real NVMe/SATA/HDD + salud
- Chasis Laptop/Desktop y bateria si es notebook
- Sin programas (git/node/etc) -- solo hardware y uso en reposo

**Verificacion manual si el script falla (pegar tal cual):**
```powershell
systeminfo | findstr /I "OS RAM"
wmic logicaldisk get size,freespace,caption,mediatype
fsutil volume diskfree C:
Get-PhysicalDisk | Select-Object Model,MediaType,BusType,Size,HealthStatus
```

- [ ] Notebook Emilia: `.md + .txt` generado
- [ ] PC escritorio 1: `.md + .txt` generado
- [ ] PC escritorio 2 (si hay): `.md + .txt` generado

---

## 2. Espacio en disco -- revision segura (40 min, NADA sin backup)

> Estado reportado: OneDrive casi vacia, Descargas colapsado. Regla: nada se borra sin backup a OneDrive/Drive/USB. Solo temporales primero.

### 2.1 Verificacion (PowerShell como Admin -- pegar tal cual)

```powershell
wmic logicaldisk get size,freespace,caption
fsutil volume diskfree C:
Get-ChildItem C:\Users\Emilia\Downloads -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum | Select-Object @{N='Downloads_GB';E={[math]::Round($_.Sum/1GB,2)}},Count
Get-Item C:\hiberfil.sys -ErrorAction SilentlyContinue | Select-Object @{N='hiberfil_GB';E={[math]::Round($_.Length/1GB,2)}}
Get-ChildItem $env:TEMP -File -Recurse -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum | Select-Object @{N='TEMP_GB';E={[math]::Round($_.Sum/1GB,2)}}
```

- [ ] Anotar: `C: libre ___GB (___%)` + `Descargas ___GB` + `hiberfil ___GB` + `TEMP ___GB`

### 2.2 Limpieza segura (solo tras backup)

```powershell
cleanmgr /sageset:1
cleanmgr /sagerun:1
Remove-Item -Recurse -Force $env:TEMP\* -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force C:\Windows\Temp\* -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force C:\Windows\SoftwareDistribution\Download\* -ErrorAction SilentlyContinue
# Solo si hiberfil >4GB y NO usa hibernar y C: <20% libre
powercfg -h off
```

- [ ] Backup Descargas -> OneDrive/Drive/USB (preguntar) -- [ ] cleanmgr + TEMP vaciado -- [ ] Papelera vaciada (preguntar)

---

## 3. Stack minimo -- vault vivo (60 min, con internet del estudio)

> Orden: winget -> Git -> gh -> Node -> Obsidian -> Antigravity/Opencode/Codex. Sin VS Code manana.

### 3.1 Git + GitHub CLI (20 min) -- OBLIGATORIO

```powershell
winget install Git.Git
winget install GitHub.cli
winget install OpenJS.NodeJS.LTS

git --version; gh --version; node -v; npm -v
git config --global user.name "Emilia Pimenta"
git config --global user.email "emilia@estudio.com"
gh auth login
gh auth status
```

### 3.2 Obsidian (15 min)

```powershell
winget install Obsidian.Obsidian
```

- [ ] Abrir Obsidian -> crear vault vacio piloto `P:\vault-emilia` o `D:\vault-emilia` + `00-index.md` con wikilink ok

### 3.3 Antigravity + Opencode + Codex (15 min) -- los 3

```powershell
npm install -g opencode
opencode --version
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
codex --version
antigravity --version
codex   # Sign in with ChatGPT (usa su cuenta Plus/Pro)
```

---

## 4. Remoto -- Chrome Remote Desktop (10 min)

- Chrome logueado con cuenta del Drive nuevo -> https://remotedesktop.google.com/access -> Configurar acceso remoto -> PIN 6 digitos
- [ ] CRD online + PIN anotado en tu vault + Quick Assist probado (Win+S -> Asistencia rapida)

---

## 5. Cierre -- entregable tildable

- [ ] Inventario portable `.md + .txt` por maquina (al lado del script, en pendrive)
- [ ] C: libre antes/después + reinicio ok
- [ ] git/gh/node/obsidian/opencode/codex/antigravity ok
- [ ] CRD PIN en tu vault

**Tiempo total:** inventario 30 + disco 40 + stack 60 + remoto 10 + cierre 10 = 2.5-3hs

---

## Referencias

- [[proyectos/STUDIO_OS-Emilia/00-index|STUDIO OS Emilia -- indice]]
- [[scripts/00-index|Scripts -- inventario-portable.ps1]]
- Codex https://developers.openai.com/codex/windows -- CRD https://remotedesktop.google.com/access
