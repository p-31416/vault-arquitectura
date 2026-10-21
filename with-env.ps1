# with-env.ps1 — Carga .env y ejecuta el comando con las credenciales
# Uso: .\with-env.ps1 opencode
#      .\with-env.ps1 opencode debug config
# Equivalente Windows de with-env.sh (bash) — compatible PowerShell 5.1

param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Command
)

if (-not $Command -or $Command.Count -eq 0) {
    Write-Host "Uso: .\with-env.ps1 <comando> [args...]" -ForegroundColor Yellow
    Write-Host "Ej:  .\with-env.ps1 opencode" -ForegroundColor DarkGray
    exit 1
}

$envFile = Join-Path $PSScriptRoot ".env"
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        $line = $_.Trim()
        if (-not $line) { return }
        if ($line.StartsWith("#")) { return }
        $eqIdx = $line.IndexOf("=")
        if ($eqIdx -lt 1) { return }
        $key = $line.Substring(0, $eqIdx).Trim()
        $val = $line.Substring($eqIdx + 1).Trim()
        if ($val.Length -ge 2) {
            if (($val.StartsWith('"') -and $val.EndsWith('"')) -or ($val.StartsWith("'") -and $val.EndsWith("'"))) {
                $val = $val.Substring(1, $val.Length - 2)
            }
        }
        Set-Item -Path "env:$key" -Value $val
    }
    Write-Host "ok .env cargado ($envFile)" -ForegroundColor DarkGreen
} else {
    Write-Host "WARN No se encontro .env en $PSScriptRoot" -ForegroundColor Yellow
}

# Configurar perfil OpenCode (XDG) según directorio de trabajo
if ($PSScriptRoot -like "*\proyecto-pi*") {
    $env:XDG_DATA_HOME = "P:\00-repos\.opencode-profiles\proyecto-pi\data"
    $env:XDG_CONFIG_HOME = "P:\00-repos\.opencode-profiles\proyecto-pi\config"
    Write-Host "ok Perfil OpenCode: Proyecto Pi (Free / Zen)" -ForegroundColor DarkCyan
} elseif ($PSScriptRoot -like "*\pitau-tech*") {
    $env:XDG_DATA_HOME = "P:\00-repos\.opencode-profiles\pitau\data"
    $env:XDG_CONFIG_HOME = "P:\00-repos\.opencode-profiles\pitau\config"
    Write-Host "ok Perfil OpenCode: Pitautech (Go Pago + Zen)" -ForegroundColor DarkGreen
}

# Ejecutar comando
$cmd = $Command[0]
$cmdArgs = @()
if ($Command.Count -gt 1) {
    $cmdArgs = $Command[1..($Command.Count-1)]
}
& $cmd @cmdArgs
exit $LASTEXITCODE
