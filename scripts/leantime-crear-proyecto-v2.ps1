# leantime-crear-proyecto-v2.ps1 — Diagnostico del alta con respuesta completa
# NOTA ES: primero relista proyectos (si O.S_ARQ-Emi ya existe, no duplica).
# NOTA ES: usa el cliente Pitautech (id=1), dueño natural del Studio OS.
# NOTA ES: imprime la respuesta cruda completa para diagnosticar, nunca el token.
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
  $raw = Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $payload -TimeoutSec 25 -UseBasicParsing
  return $raw.Content
}
Write-Output '---PROJECTS_BEFORE---'
$before = RpcRaw 'leantime.rpc.Projects.Projects.getAllProjects' @{}
$bj = $before | ConvertFrom-Json
Write-Output ('COUNT=' + $bj.result.Count)
Write-Output (('NAMES=' + (($bj.result | ForEach-Object { $_.name }) -join ' | ')))
$hit = $bj.result | Where-Object { $_.name -eq 'O.S_ARQ-Emi' } | Select-Object -First 1
if ($hit) {
  Write-Output ('ALREADY_EXISTS id=' + $hit.id)
  exit 0
}
Write-Output '---CREATE---'
$values = @{
  name = 'O.S_ARQ-Emi'
  clientId = 1
  details = 'Studio OS — tablero operativo de Emilia (vault-arquitectura).'
  type = 'project'
}
$cr = RpcRaw 'leantime.rpc.Projects.Projects.addProject' @{ values = $values }
Write-Output ('RAW=' + $cr)
Write-Output '---PROJECTS_AFTER---'
$after = RpcRaw 'leantime.rpc.Projects.Projects.getAllProjects' @{}
$aj = $after | ConvertFrom-Json
Write-Output ('COUNT=' + $aj.result.Count)
Write-Output (('NAMES=' + (($aj.result | ForEach-Object { $_.name }) -join ' | ')))
