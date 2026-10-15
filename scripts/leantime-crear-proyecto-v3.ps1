# leantime-crear-proyecto-v3.ps1 — Alta con cuerpo ASCII y bytes UTF-8 explicitos
# NOTA ES: el intento anterior fallo con Parse error por el guion largo (em-dash) en details.
# NOTA ES: esta version usa solo ASCII y envia el cuerpo como bytes UTF-8.
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
$values = @{
  name = 'O.S_ARQ-Emi'
  clientId = 1
  details = 'Studio OS - tablero operativo de Emilia (vault-arquitectura).'
  type = 'project'
}
Write-Output '---CREATE---'
$cr = RpcRaw 'leantime.rpc.Projects.Projects.addProject' @{ values = $values }
Write-Output ('RAW=' + $cr)
Write-Output '---PROJECTS_AFTER---'
$after = RpcRaw 'leantime.rpc.Projects.Projects.getAllProjects' @{}
$aj = $after | ConvertFrom-Json
Write-Output ('COUNT=' + $aj.result.Count)
Write-Output (('NAMES=' + (($aj.result | ForEach-Object { $_.name }) -join ' | ')))
$new = $aj.result | Where-Object { $_.name -eq 'O.S_ARQ-Emi' } | Select-Object -First 1
if ($new) { Write-Output ('CREATED id=' + $new.id + ' name=' + $new.name) }
