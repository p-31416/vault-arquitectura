# check-leantime-token-meta.ps1 — Solo metadatos del token, nunca el valor
# NOTA ES: muestra largo, prefijo de 3 chars y si parece API key lt_ o PAT
$ErrorActionPreference = 'Stop'
$envFile = '.\\.env'
$tok = $null
foreach ($line in Get-Content $envFile) {
  $t = $line.Trim()
  if ($t.StartsWith('LEANTIME_TOKEN=')) {
    $tok = $t.Substring(16).Trim().Trim('"').Trim("'")
    break
  }
}
if (-not $tok) { Write-Output 'NO_TOKEN_FOUND'; exit 1 }
$prefix = $tok.Substring(0, [Math]::Min(3, $tok.Length))
$startsLt = $tok.StartsWith('lt_')
Write-Output ('LEN=' + $tok.Length)
Write-Output ('PREFIX3=' + $prefix)
Write-Output ('STARTS_LT=' + $startsLt)
Write-Output ('HAS_SPACES=' + ($tok.Contains(' ') -or $tok.Contains("`n")))
