# leantime-crear-proyecto.ps1 — Lista clientes/proyectos y crea O.S_ARQ-Emi por JSON-RPC
# NOTA ES: lee LEANTIME_TOKEN desde el .env del vault, nunca imprime el valor.
# NOTA ES: endpoint unico POST /api/jsonrpc con header x-api-key (API key lt_).
# NOTA ES: primero lista (read-only), luego crea solo si el nombre no existe.
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
if (-not $tok) { Write-Output 'NO_TOKEN_FOUND'; exit 1 }
Write-Output ('TOKEN_LEN=' + $tok.Length + ' STARTS_LT=' + $tok.StartsWith('lt_'))
# NOTA ES: funcion que envia un metodo JSON-RPC y devuelve el objeto respuesta
function Rpc($method, $paramsObj) {
  $uri = 'https://pitautech-leantime.3nq4ow.easypanel.host/api/jsonrpc'
  $headers = @{
    'Content-Type' = 'application/json'
    'x-api-key' = $tok
  }
  $payload = @{
    jsonrpc = '2.0'
    id = 1
    method = $method
    params = $paramsObj
  } | ConvertTo-Json -Depth 6 -Compress
  $resp = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $payload -TimeoutSec 25
  return $resp
}
# NOTA ES: paso 1 listar clientes para obtener un clientId valido
Write-Output '---CLIENTS---'
try {
  $c = Rpc 'leantime.rpc.Clients.Clients.getAll' @{}
  $list = $c.result
  if ($null -eq $list) { $list = $c }
  $count = if ($list -is [array]) { $list.Count } else { 1 }
  Write-Output ('CLIENTS_COUNT=' + $count)
  $preview = ($list | Select-Object -First 5 | ForEach-Object {
    $cid = $_.id; $cn = $_.name; ('id=' + $cid + ' name=' + $cn)
  }) -join ' | '
  Write-Output $preview
} catch {
  Write-Output ('CLIENTS_ERROR: ' + $_.Exception.Message)
  if ($_.ErrorDetails.Message) { Write-Output $_.ErrorDetails.Message.Substring(0, [Math]::Min(1000, $_.ErrorDetails.Message.Length)) }
  exit 1
}
# NOTA ES: paso 2 listar proyectos para detectar duplicado de O.S_ARQ-Emi
Write-Output '---PROJECTS---'
$projList = @()
foreach ($m in @('leantime.rpc.Projects.Projects.getAllProjects', 'leantime.rpc.projects.getAllProjects', 'leantime.rpc.Projects.Projects.getAll')) {
  try {
    $p = Rpc $m @{}
    $res = $p.result
    if ($null -ne $res) {
      Write-Output ('PROJECTS_METHOD_OK=' + $m)
      if ($res -is [array]) { $projList = $res } else { $projList = @($res) }
      break
    }
  } catch {
    Write-Output ('PROJECTS_TRY_FAIL=' + $m)
  }
}
Write-Output ('PROJECTS_COUNT=' + $projList.Count)
$names = ($projList | Select-Object -First 20 | ForEach-Object { $_.name }) -join ' | '
if ($names) { Write-Output ('PROJECTS_NAMES=' + $names) }
$exists = $projList | Where-Object { $_.name -eq 'O.S_ARQ-Emi' } | Select-Object -First 1
if ($exists) {
  Write-Output ('ALREADY_EXISTS id=' + $exists.id + ' name=' + $exists.name)
  exit 0
}
# NOTA ES: paso 3 crear el proyecto con el primer clientId disponible
$clients = $c.result
if ($clients -isnot [array]) { $clients = @($clients) }
$clientId = [int]$clients[0].id
Write-Output ('USING_CLIENT_ID=' + $clientId + ' CLIENT_NAME=' + $clients[0].name)
$values = @{
  name = 'O.S_ARQ-Emi'
  clientId = $clientId
  details = 'Studio OS — tablero operativo de Emilia (vault-arquitectura).'
  type = 'project'
}
try {
  $r = Rpc 'leantime.rpc.Projects.Projects.addProject' @{ values = $values }
  $rid = $r.result
  Write-Output ('CREATE_RESULT=' + ($rid | ConvertTo-Json -Compress -Depth 3))
} catch {
  Write-Output ('CREATE_ERROR: ' + $_.Exception.Message)
  if ($_.ErrorDetails.Message) { Write-Output $_.ErrorDetails.Message.Substring(0, [Math]::Min(2000, $_.ErrorDetails.Message.Length)) }
  exit 1
}
