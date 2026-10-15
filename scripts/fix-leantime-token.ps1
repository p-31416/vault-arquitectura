# fix-leantime-token.ps1 — Repara la l inicial perdida en LEANTIME_TOKEN
# NOTA ES: solo informa largo y prefijo, nunca el valor completo
$ErrorActionPreference = 'Stop'
$f = '.\\.env'
$ls = Get-Content $f
$n = 0
$out = @()
foreach ($ln in $ls) {
  $t = $ln.Trim()
  if ($t.StartsWith('LEANTIME_TOKEN=t_')) {
    $ln = $ln -replace 'LEANTIME_TOKEN=t_', 'LEANTIME_TOKEN=lt_'
    $n = 1
  }
  $out += $ln
}
if ($n -eq 1) {
  Set-Content -Path $f -Value $out -Encoding UTF8
}
$chk = $out | Where-Object { $_.Trim().StartsWith('LEANTIME_TOKEN=') } | Select-Object -First 1
$v = $chk.Substring($chk.IndexOf('=') + 1).Trim().Trim('"').Trim("'")
Write-Output ('FIXED=' + $n)
Write-Output ('NEWLEN=' + $v.Length)
Write-Output ('PREFIX3=' + $v.Substring(0, 3))
Write-Output ('STARTS_LT=' + $v.StartsWith('lt_'))
