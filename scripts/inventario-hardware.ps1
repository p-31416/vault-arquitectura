#Requires -Version 5.1
<#
.SYNOPSIS
  Inventario hardware + software para Vault Cerebro (estudio arquitectura).
  Relevamiento Semana 1 — corre en Windows (Sol y Emilia) y genera reporte para el vault.

.DESCRIPTION
  Extrae: CPU, RAM, GPU (incl. VRAM real via WMI — DirectML no la reporta),
  discos, pantallas/monitores, placa madre, BIOS, red, OS, Python, Git, Node,
  ComfyUI (ruta P:\00-repos\ComfyUI si existe), AutoCAD/Revit si instalados.
  Salida: consola + JSON + .md listo para pegar en raw/sessions o ficha proyecto.

.USAGE
  powershell -ExecutionPolicy Bypass -File scripts\inventario-hardware.ps1
  powershell -ExecutionPolicy Bypass -File scripts\inventario-hardware.ps1 -OutDir ".\raw\sesiones-assets"
#>
param(
  [string]$OutDir = "",
  [string]$ComfyPath = "P:\00-repos\ComfyUI"
)

$ErrorActionPreference = "Continue"
$ts = Get-Date -Format "yyyyMMdd-HHmm"
$host_name = $env:COMPUTERNAME
if ([string]::IsNullOrWhiteSpace($OutDir)) {
  $vaultRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
  # scripts/ -> vault root
  if ((Split-Path -Leaf $vaultRoot) -eq "scripts") { $vaultRoot = Split-Path -Parent $vaultRoot }
  $OutDir = Join-Path $vaultRoot "raw\sessions"
}
if (-not (Test-Path -LiteralPath $OutDir)) { New-Item -ItemType Directory -Path $OutDir | Out-Null }

function Get-CmdVersion([string]$cmd, [string]$args = "--version") {
  try {
    $out = & $cmd ($args -split ' ') 2>&1 | Select-Object -First 1
    return ($out | Out-String).Trim()
  } catch { return "no instalado / no en PATH" }
}

function Get-GpuVramReal {
  # DirectML reporta 1GB fantasma; WMI AdapterRAM (uint32, puede overflow en 8GB+ -> valor negativo)
  # Se corrige con firma + fallback a VideoMemoryType / pynvml no aplica (AMD).
  $gpus = Get-CimInstance Win32_VideoController | ForEach-Object {
    $raw = $_.AdapterRAM
    $vramGB = $null
    if ($raw -ne $null) {
      $u = [uint32]$raw  # reinterpretar bits
      $vramGB = [math]::Round($u / 1GB, 2)
      if ($vramGB -lt 0.5) {
        # Overflow >4GB en driver viejo: estimar por nombre conocido
        $vramGB = $null
      }
    }
    [PSCustomObject]@{
      Nombre       = $_.Name
      AdapterRAM_raw = $raw
      VRAM_GB_aprox  = $vramGB
      DriverVersion  = $_.DriverVersion
      DriverDate     = $_.DriverDate
      ResActual      = "$($_.CurrentHorizontalResolution)x$($_.CurrentVerticalResolution) @ $($_.CurrentRefreshRate)Hz"
      Status         = $_.Status
    }
  }
  return $gpus
}

Write-Host "=== Vault Cerebro — Inventario hardware ($host_name, $ts) ===" -ForegroundColor Cyan

# --- OS / placa / BIOS ---
$os   = Get-CimInstance Win32_OperatingSystem
$cs   = Get-CimInstance Win32_ComputerSystem
$base = Get-CimInstance Win32_BaseBoard
$bios = Get-CimInstance Win32_BIOS
$cpu  = Get-CimInstance Win32_Processor | Select-Object -First 1

# --- RAM detalle por slot ---
$ramSticks = Get-CimInstance Win32_PhysicalMemory | ForEach-Object {
  [PSCustomObject]@{
    Slot       = $_.DeviceLocator
    CapacidadGB= [math]::Round($_.Capacity / 1GB, 2)
    VelocidadMHz = $_.Speed
    Tipo       = $_.SMBIOSMemoryType  # 26=DDR4, 34=DDR5 (según SMBIOS)
    Fabricante = $_.Manufacturer
    PartNumber = ($_.PartNumber).Trim()
  }
}
$ramTotalGB = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)
$ramFreeGB  = [math]::Round($os.FreePhysicalMemory / 1MB, 2)

# --- GPU ---
$gpus = Get-GpuVramReal

# --- Discos ---
$discos = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" | ForEach-Object {
  [PSCustomObject]@{
    Unidad     = $_.DeviceID
    Etiqueta   = $_.VolumeName
    TotalGB    = [math]::Round($_.Size / 1GB, 2)
    LibreGB    = [math]::Round($_.FreeSpace / 1GB, 2)
    LibrePct   = if ($_.Size) { [math]::Round($_.FreeSpace / $_.Size * 100, 1) } else { $null }
    FS         = $_.FileSystem
  }
}
$nvme = Get-PhysicalDisk -ErrorAction SilentlyContinue | ForEach-Object {
  [PSCustomObject]@{ Modelo = $_.Model; Tipo = $_.MediaType; Bus = $_.BusType; TamGB = [math]::Round($_.Size / 1GB, 2); Salud = $_.HealthStatus }
}

# --- Pantallas / monitores ---
$mons = Get-CimInstance WmiMonitorID -Namespace root\wmi -ErrorAction SilentlyContinue | ForEach-Object {
  $toStr = { param($a) (-join ($a | Where-Object { $_ -ne 0 } | ForEach-Object { [char]$_ })).Trim() }
  [PSCustomObject]@{
    Fabricante = &$toStr $_.ManufacturerName
    Modelo     = &$toStr $_.ProductCodeID
    Serial     = &$toStr $_.SerialNumberID
    Anio       = $_.YearOfManufacture
  }
}
$pantallas = Get-CimInstance Win32_DesktopMonitor -ErrorAction SilentlyContinue | Select-Object Name, MonitorType, ScreenWidth, ScreenHeight

# --- Red / IP ---
$ips = Get-NetIPAddress -AddressFamily IPv4 -ErrorAction SilentlyContinue |
  Where-Object { $_.IPAddress -notlike "127.*" -and $_.PrefixOrigin -ne "WellKnown" } |
  Select-Object IPAddress, InterfaceAlias

# --- Software clave ---
$py  = Get-CmdVersion "python" "--version"
$py2 = Get-CmdVersion "py" "--version"
$git = Get-CmdVersion "git" "--version"
$node= Get-CmdVersion "node" "--version"
$code= Get-CmdVersion "code" "--version"
$gh  = Get-CmdVersion "gh" "--version"
$oc  = Get-CmdVersion "opencode" "--version"
$nvidia = Get-CmdVersion "nvidia-smi" "--query-gpu=name,memory.total --format=csv"

# --- ComfyUI local ---
$comfyInfo = [PSCustomObject]@{ Ruta = $ComfyPath; Existe = (Test-Path -LiteralPath $ComfyPath); Detalle = $null }
if ($comfyInfo.Existe) {
  $ckpt = Join-Path $ComfyPath "models\checkpoints"
  $cn   = Join-Path $ComfyPath "models\controlnet"
  $venv = Join-Path $ComfyPath ".venv"
  $comfyInfo.Detalle = [PSCustomObject]@{
    Checkpoints = if (Test-Path $ckpt) { (Get-ChildItem $ckpt -File -ErrorAction SilentlyContinue | Select-Object Name, @{n='GB';e={[math]::Round($_.Length/1GB,2)}}) } else { "sin carpeta" }
    ControlNets = if (Test-Path $cn) { (Get-ChildItem $cn -File -ErrorAction SilentlyContinue | Select-Object Name, @{n='MB';e={[math]::Round($_.Length/1MB,0)}}) } else { "sin carpeta" }
    MainPy     = (Test-Path (Join-Path $ComfyPath "main.py"))
    Bat        = (Get-ChildItem $ComfyPath -Filter "*.bat" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Name)
  }
}

# --- AutoCAD / Revit instalados (registro uninstall) ---
$apps = Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*" -ErrorAction SilentlyContinue |
  Where-Object { $_.DisplayName -match "AutoCAD|Revit|Rhino|Twinmotion|3ds Max" } |
  Select-Object DisplayName, DisplayVersion

# ============ REPORTE ============
$report = @()
$report += "# Inventario hardware — $host_name ($ts)"
$report += ""
$report += "- Usuario: $env:USERNAME | OS: $($os.Caption) $($os.OSArchitecture) build $($os.BuildNumber)"
$report += "- Placa: $($base.Manufacturer) $($base.Product) | BIOS: $($bios.Manufacturer) $($bios.SMBIOSBIOSVersion)"
$report += "- CPU: $($cpu.Name) | Núcleos: $($cpu.NumberOfCores) físicos / $($cpu.NumberOfLogicalProcessors) lógicos @ $([math]::Round($cpu.MaxClockSpeed/1000,2)) GHz"
$report += "- RAM total: $ramTotalGB GB | libre: $ramFreeGB GB"
$report += ""
$report += "## RAM por slot"
$ramSticks | ForEach-Object { $report += "- $($_.Slot): $($_.CapacidadGB) GB @ $($_.VelocidadMHz) MHz (tipo SMBIOS $($_.Tipo)) $($_.Fabricante) $($_.PartNumber)" }
$report += ""
$report += "## GPU (VRAM real via WMI — ver AGENTS.md patch model_management.py:324)"
$gpus | ForEach-Object { $report += "- $($_.Nombre) | VRAM aprox: $($_.VRAM_GB_aprox) GB (raw $($_.AdapterRAM_raw)) | driver $($_.DriverVersion) | res $($_.ResActual)" }
$report += "> Si VRAM_GB_aprox sale vacía o absurda (<0.5): driver overflow uint32 >4GB — confirmar con GPU-Z o Adrenalin y anotar manual."
$report += ""
$report += "## Discos lógicos"
$discos | ForEach-Object { $report += "- $($_.Unidad) [$($_.Etiqueta)] $($_.LibreGB)/$($_.TotalGB) GB libres ($($_.LibrePct)%) FS $($_.FS)" }
if ($nvme) { $report += ""; $report += "## Discos físicos"; $nvme | ForEach-Object { $report += "- $($_.Modelo) $($_.Tipo)/$($_.Bus) $($_.TamGB) GB salud $($_.Salud)" } }
$report += ""
$report += "## Monitores (EDID)"
if ($mons) { $mons | ForEach-Object { $report += "- $($_.Fabricante) $($_.Modelo) S/N $($_.Serial) ($($_.Anio))" } } else { $report += "- (WMI sin datos — anotar marca/pulgadas/resolución manual)" }
if ($pantallas) { $pantallas | ForEach-Object { $report += "- Pantalla: $($_.Name) $($_.ScreenWidth)x$($_.ScreenHeight)" } }
$report += ""
$report += "## Red"
$ips | ForEach-Object { $report += "- $($_.IPAddress) ($($_.InterfaceAlias))" }
$report += ""
$report += "## Software"
$report += "- python: $py | py launcher: $py2"
$report += "- git: $git | gh: $gh | node: $node | vscode: $code | opencode: $oc"
$report += "- nvidia-smi: $nvidia (esperable que falle en AMD — confirma DirectML)"
$report += ""
$report += "## ComfyUI ($ComfyPath existe=$($comfyInfo.Existe))"
if ($comfyInfo.Detalle) {
  $report += "- main.py: $($comfyInfo.Detalle.MainPy) | bats: $($comfyInfo.Detalle.Bat -join ', ')"
  $report += "- Checkpoints:"; $comfyInfo.Detalle.Checkpoints | ForEach-Object { $report += "  - $($_.Name) ($($_.GB) GB)" }
  $report += "- ControlNets:"; $comfyInfo.Detalle.ControlNets | ForEach-Object { $report += "  - $($_.Name) ($($_.MB) MB)" }
}
$report += ""
$report += "## CAD/BIM detectado"
if ($apps) { $apps | ForEach-Object { $report += "- $($_.DisplayName) $($_.DisplayVersion)" } } else { $report += "- (no detectado en registro — verificar manual)" }
$report += ""
$report += "## Aptitud ComfyUI local (regla rápida)"
$report += "- RAM >=16GB y VRAM >=6GB → SD1.5 + 2 ControlNet OK. 8GB VRAM justo para SDXL (usar --lowvram)."
$report += "- Sin GPU dedicada / solo iGPU Intel → NO local: usar RunPod (ver pbk-comfyui § RunPod)."
$report += ""
$report += "_Generado por scripts/inventario-hardware.ps1 — pegar en raw/sessions/ y en ficha proyecto._"

$text = $report -join "`r`n"
Write-Host $text

$mdPath   = Join-Path $OutDir "$ts-inventario-$($host_name.ToLower()).md"
$jsonPath = Join-Path $OutDir "$ts-inventario-$($host_name.ToLower()).json"
$text | Out-File -LiteralPath $mdPath -Encoding utf8
[PSCustomObject]@{
  host=$host_name; fecha=$ts; usuario=$env:USERNAME
  os="$($os.Caption) $($os.OSArchitecture) $($os.BuildNumber)"
  cpu="$($cpu.Name)"; nucleos_fisicos=$cpu.NumberOfCores; hilos=$cpu.NumberOfLogicalProcessors
  ram_total_gb=$ramTotalGB; ram_libre_gb=$ramFreeGB; ram_slots=$ramSticks
  gpus=$gpus; discos=$discos; discos_fisicos=$nvme; monitores=$mons; pantallas=$pantallas
  red=$ips; python=$py; git=$git; node=$node; vscode=$code; opencode=$oc
  comfy=$comfyInfo; cad_bim=$apps
} | ConvertTo-Json -Depth 6 | Out-File -LiteralPath $jsonPath -Encoding utf8

Write-Host ""
Write-Host "Guardado: $mdPath" -ForegroundColor Green
Write-Host "Guardado: $jsonPath" -ForegroundColor Green
