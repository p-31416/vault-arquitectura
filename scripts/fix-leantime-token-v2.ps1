# fix-leantime-token-v2.ps1 — Repara con ruta absoluta, sin mostrar el secreto
# NOTA ES: usa ruta absoluta al .env del vault para evitar ambiguedad de relativos
$ErrorActionPreference = 'Stop'
$f = 'P:\00-repos\proyecto-pi\vault-arquitectura\.env'
$ls = Get-Content -LiteralPath $f
$n = 0
$out = @()
foreach ($ln in $ls) {
  $t = $ln.Trim()
  if ($t.StartsWith('LEANTIME_TOKEN=t_') -or $t.StartsWith('LEANTIME_TOKEN="t_') -or $t.StartsWith("LEANTIME_TOKEN='t_")) {
    $ln = $ln -replace 'LEANTIME_TOKEN="?t_', 'LEANTIME_TOKEN="lt_'
    if ($ln.Trim().StartsWith("LEANTIME_TOKEN='")) { $ln = $ln -replace "LEANTIME_TOKEN='t_", "LEANTIME_TOKEN='lt_" }
    # NOTA ES: normaliza sin comillas dobles extra
    $n = 1
  }
  $out += $ln
}
if ($n -eq 1) {
  Set-Content -LiteralPath $f -Value $out -Encoding UTF8
}
$chk = $out | Where-Object { $_.Trim().StartsWith('LEANTIME_TOKEN=') } | Select-Object -First 1
$v = $chk.Substring($chk.IndexOf('=') + 1).Trim().Trim('"').Trim("'")
Write-Output ('FIXED=' + $n)
Write-Output ('NEWLEN=' + $v.Length)
Write-Output ('PREFIX3=' + $v.Substring(0, 3))
Write-Output ('STARTS_LT=' + $v.StartsWith('lt_'))
