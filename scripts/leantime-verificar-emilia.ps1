# leantime-verificar-emilia.ps1 — Verifica la usuaria de Emilia por JSON-RPC (read-only)
# NOTA ES: prueba variantes del metodo de listado de usuarios y muestra solo id/nombre/email/estado.
# NOTA ES: nunca imprime el token.
$ErrorActionPreference = 'Stop'
$f = 'P:\00-repos\proyecto-pi\vault-arquitectura\.env'
$tok = $null
foreach ($line in Get-Content -LiteralPath $f) {
  $t = $line.Trim()
  if ($t.StartsWith('LEANTIME_TOKEN=')) {
    $tok = $t.Substring($t.IndexOf('=') + 1).Trim().Trim('"').Trim("'")
    break
  }
}
function RpcRaw($method, $paramsObj) {
  $uri = 'https://pitautech-leantime.3nq4ow.easypanel.host/api/jsonrpc'
  $headers = @{ 'Content-Type' = 'application/json'; 'x-api-key' = $tok }
  $payload = @{ jsonrpc = '2.0'; id = 1; method = $method; params = $paramsObj } | ConvertTo-Json -Depth 6 -Compress
  $bytes = [System.Text.Encoding]::UTF8.GetBytes($payload)
  $raw = Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $bytes -TimeoutSec 25 -UseBasicParsing
  return $raw.Content
}
$target = 'arq.emiliapimentalombardi@gmail.com'
foreach ($m in @('leantime.rpc.Users.Users.getAll', 'leantime.rpc.users.getAllUsers', 'leantime.rpc.Users.Users.getUsers')) {
  try {
    $resp = RpcRaw $m @{}
    $j = $resp | ConvertFrom-Json
    if ($null -ne $j.result) {
      Write-Output ('USERS_METHOD_OK=' + $m)
      $users = if ($j.result -is [array]) { $j.result } else { @($j.result) }
      Write-Output ('USERS_COUNT=' + $users.Count)
      foreach ($u in $users) {
        Write-Output ('id=' + $u.id + ' username=' + $u.username + ' email=' + $u.mail + ' name=' + $u.firstname + ' ' + $u.lastname + ' status=' + $u.status)
      }
      $hit = $users | Where-Object { $_.mail -eq $target -or $_.username -eq $target } | Select-Object -First 1
      if ($hit) { Write-Output ('EMILIA_FOUND id=' + $hit.id + ' status=' + $hit.status) }
      else { Write-Output 'EMILIA_NOT_FOUND' }
      exit 0
    } else {
      Write-Output ('USERS_EMPTY_RESULT=' + $m + ' RAW=' + $resp.Substring(0, [Math]::Min(500, $resp.Length)))
    }
  } catch {
    Write-Output ('USERS_TRY_FAIL=' + $m + ' :: ' + $_.Exception.Message)
  }
}
