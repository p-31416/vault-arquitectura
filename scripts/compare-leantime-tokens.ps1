# compare-leantime-tokens.ps1 — Compara .env vs token de referencia sin imprimir valores
# NOTA ES: solo dice si coinciden o si falta el primer caracter, nunca muestra el secreto
$ErrorActionPreference = 'Stop'
$envTok = $null
foreach ($line in Get-Content '.\\.env') {
  $t = $line.Trim()
  if ($t.StartsWith('LEANTIME_TOKEN=')) { $envTok = $t.Substring(16).Trim().Trim('"').Trim("'"); break }
}
# NOTA ES: token de referencia tomado de create-user-emilia.ps1 (ya expuesto en repo, pendiente rotar)
$refLine = Get-Content '.\\create-user-emilia.ps1' -Raw
$m = [regex]::Match($refLine, "lt_[A-Za-z0-9_\\-]+")
$refTok = if ($m.Success) { $m.Value } else { '' }
Write-Output ('ENV_LEN=' + $envTok.Length)
Write-Output ('REF_LEN=' + $refTok.Length)
Write-Output ('ENV_EQ_REF=' + ($envTok -ceq $refTok))
Write-Output ('ENV_EQ_REF_SIN_PRIMERA_LETRA=' + ($envTok -ceq $refTok.Substring(1)))
Write-Output ('ENV_EQ_L_MAS_ENV=' + (('l' + $envTok) -ceq $refTok))
