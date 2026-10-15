# probe-leantime-mcp-v3.ps1 — Lista prompts y resources ademas de tools
# NOTA ES: read-only, reutiliza sesion MCP para prompts/list y resources/list
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
$uri = 'https://pitautech-leantime.3nq4ow.easypanel.host/mcp'
$headers = @{
  'Content-Type' = 'application/json'
  'Accept' = 'application/json, text/event-stream'
  'x-api-key' = $tok
}
$init = '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"probe","version":"0.0.1"}}}'
$r = Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $init -TimeoutSec 20
$sess = $r.Headers['mcp-session-id']
Write-Output ('INIT=' + [int]$r.StatusCode + ' SESSION=' + ($sess -ne $null))
$h2 = @{
  'Content-Type' = 'application/json'
  'Accept' = 'application/json, text/event-stream'
  'x-api-key' = $tok
}
if ($sess) { $h2['mcp-session-id'] = $sess }
try { Invoke-WebRequest -Uri $uri -Method Post -Headers $h2 -Body '{"jsonrpc":"2.0","method":"notifications/initialized"}' -TimeoutSec 15 | Out-Null } catch {}
foreach ($m in @('tools/list', 'prompts/list', 'resources/list')) {
  $b = '{"jsonrpc":"2.0","id":2,"method":"' + $m + '","params":{}}'
  try {
    $rr = Invoke-WebRequest -Uri $uri -Method Post -Headers $h2 -Body $b -TimeoutSec 20
    $c = [string]$rr.Content
    if ($c.Length -gt 4000) { $c = $c.Substring(0, 4000) + '...TRUNCADO' }
    Write-Output ('---' + $m + ' ' + [int]$rr.StatusCode + '---')
    Write-Output $c
  } catch {
    Write-Output ('---' + $m + ' ERROR: ' + $_.Exception.Message)
  }
}
