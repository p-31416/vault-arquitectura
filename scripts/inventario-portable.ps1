#Requires -Version 5.1
<#
.SYNOPSIS
  Inventario portable -- para llevar en pendrive. Solo hardware y consumo en reposo.
  No necesita vault, no instala nada. Guarda .md + .txt al lado del script.

.USAGE
  Doble-click en INVENTARIO-Portable-DobleClick.lnk
  o: powershell -ExecutionPolicy Bypass -File "E:\inventario-portable.ps1"
#>

$ts = Get-Date -Format "yyyy-MM-dd_HH-mm"
$hostName = $env:COMPUTERNAME
$outDir = $PSScriptRoot
if (-not $outDir -or $outDir -eq "") { $outDir = (Get-Location).Path }

Write-Host "=== Inventario portable -- $hostName ($ts) ===" -ForegroundColor Cyan

# -- OS / CPU / RAM --
$os = Get-CimInstance Win32_OperatingSystem -ErrorAction SilentlyContinue
$cpu = Get-CimInstance Win32_Processor -ErrorAction SilentlyContinue | Select-Object -First 1
$cs = Get-CimInstance Win32_ComputerSystem -ErrorAction SilentlyContinue
$ramTotalGB = if ($os) { [math]::Round($os.TotalVisibleMemorySize / 1MB, 2) } else { "?" }
$ramFreeGB = if ($os) { [math]::Round($os.FreePhysicalMemory / 1MB, 2) } else { "?" }
$ramUsedPct = if ($os -and $os.TotalVisibleMemorySize) { [math]::Round((1 - $os.FreePhysicalMemory / $os.TotalVisibleMemorySize) * 100, 1) } else { "?" }
$cpuLoad = try { (Get-CimInstance Win32_Processor -ErrorAction SilentlyContinue | Measure-Object -Property LoadPercentage -Average).Average } catch { "?" }

# RAM por slot
$ramSticks = Get-CimInstance Win32_PhysicalMemory -ErrorAction SilentlyContinue | ForEach-Object {
  [PSCustomObject]@{
    Slot = $_.DeviceLocator
    GB = [math]::Round($_.Capacity / 1GB, 2)
    MHz = $_.Speed
  }
}

# -- GPU --
$gpus = Get-CimInstance Win32_VideoController -ErrorAction SilentlyContinue | ForEach-Object {
  $raw = $_.AdapterRAM
  $vram = $null
  if ($raw -ne $null) {
    try { $u = [uint32]$raw; $vram = [math]::Round($u / 1GB, 2); if ($vram -lt 0.5) { $vram = $null } } catch { $vram = $null }
  }
  [PSCustomObject]@{
    Nombre = $_.Name
    VRAM_GB = $vram
    Driver = $_.DriverVersion
    Res = "$($_.CurrentHorizontalResolution)x$($_.CurrentVerticalResolution)"
  }
}

# -- Discos logicos --
$discos = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" -ErrorAction SilentlyContinue | ForEach-Object {
  [PSCustomObject]@{
    Unidad = $_.DeviceID
    Etiqueta = $_.VolumeName
    TotalGB = [math]::Round($_.Size / 1GB, 2)
    LibreGB = [math]::Round($_.FreeSpace / 1GB, 2)
    LibrePct = if ($_.Size) { [math]::Round($_.FreeSpace / $_.Size * 100, 1) } else { $null }
  }
}
$phys = Get-PhysicalDisk -ErrorAction SilentlyContinue | ForEach-Object {
  $bus = switch ($_.BusType) { 17 {"NVMe"} 11 {"SATA"} 8 {"SAS"} 7 {"USB"} default {"$($_.BusType)"} }
  [PSCustomObject]@{ Modelo = $_.Model; Tipo = $_.MediaType; Bus = $bus; TamGB = [math]::Round($_.Size / 1GB, 2) }
}

# -- Bateria / Chasis --
$batt = Get-CimInstance Win32_Battery -ErrorAction SilentlyContinue | Select-Object -First 1 Name, EstimatedChargeRemaining, BatteryStatus
$chassis = Get-CimInstance Win32_SystemEnclosure -ErrorAction SilentlyContinue | Select-Object -First 1 ChassisTypes
$chassisLabel = if ($chassis) { switch ($chassis.ChassisTypes[0]) { 8 {"Laptop"} 9 {"Notebook"} 10 {"Notebook"} 3 {"Desktop"} 4 {"Low Profile"} 6 {"Mini Tower"} 7 {"Tower"} default {"Tipo $($chassis.ChassisTypes[0])"} } } else { "Desconocido" }

# -- Reporte --
$report = @()
$report += "# Inventario portable -- $hostName ($ts)"
$report += ""
$report += "- Fecha: $ts | Usuario: $env:USERNAME | Equipo: $hostName ($chassisLabel)"
$report += "- Windows: $($os.Caption) $($os.OSArchitecture) Build $($os.BuildNumber) | Instalado: $($os.InstallDate)"
$report += "- CPU: $($cpu.Name) | Nucleos: $($cpu.NumberOfCores) fisicos / $($cpu.NumberOfLogicalProcessors) hilos | Carga actual: $cpuLoad %"
$report += "- RAM total: $ramTotalGB GB | libre: $ramFreeGB GB | en uso: $ramUsedPct %"
$report += ""
$report += "## RAM por slot"
if ($ramSticks) { $ramSticks | ForEach-Object { $report += "- $($_.Slot): $($_.GB) GB @ $($_.MHz) MHz" } } else { $report += "- (no detectado)" }
$report += ""
$report += "## GPU"
if ($gpus) { $gpus | ForEach-Object { $report += "- $($_.Nombre) | VRAM: $(if($_.VRAM_GB){ "$($_.VRAM_GB) GB"}else{"?"}) | Driver: $($_.Driver) | Res: $($_.Res)" } } else { $report += "- (no detectada)" }
$report += ""
$report += "## Discos logicos (libre/total)"
$discos | ForEach-Object { $report += "- $($_.Unidad) [$($_.Etiqueta)] $($_.LibreGB)/$($_.TotalGB) GB libres ($($_.LibrePct)%)" }
if ($phys) { $report += ""; $report += "## Discos fisicos (tipo real)"; $phys | ForEach-Object { $report += "- $($_.Modelo) | $($_.Tipo) / $($_.Bus) $($_.TamGB) GB" } }
$report += ""
if ($batt) { $report += "## Bateria"; $report += "- $($batt.Name): $($batt.EstimatedChargeRemaining)% (estado $($batt.BatteryStatus))"; $report += "" }
$report += "_Generado por inventario-portable.ps1 -- consumo en reposo al momento de ejecutar._"

$text = $report -join "`r`n"
Write-Host $text
Write-Host ""

# Guardar al lado del script (pendrive)
$mdPath = Join-Path $outDir "$ts-inventario-$($hostName.ToLower()).md"
$txtPath = $mdPath -replace '\.md$','.txt'
$text | Out-File -LiteralPath $mdPath -Encoding utf8
$text | Out-File -LiteralPath $txtPath -Encoding utf8
Write-Host "Guardado: $mdPath" -ForegroundColor Green
Write-Host "Guardado: $txtPath" -ForegroundColor Green

# Abrir TXT en Bloc de notas
try { Start-Process notepad.exe -ArgumentList "`"$txtPath`"" -ErrorAction SilentlyContinue | Out-Null } catch {}

Write-Host ""
Write-Host "Listo - Presiona Enter para cerrar..." -ForegroundColor Cyan
Read-Host | Out-Null
