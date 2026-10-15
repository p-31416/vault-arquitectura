# probe-leantime-mcp-v2.ps1 — Sonda read-only con extraccion correcta del token
# NOTA ES: usa IndexOf('=')+1 (no offset fijo) para no perder la l inicial de lt_
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
Write-Output ('TOKEN_LEN=' + $tok.Length)
Write-Output ('STARTS_LT=' + $tok.StartsWith('lt_'))
$headers = @{
  'Content-Type' = 'application/json'
  'Accept' = 'application/json, text/event-stream'
  'x-api-key' = $tok
}
$uri = 'https://pitautech-leantime.3nq4ow.easypanel.host/mcp'
$bodyInit = '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"probe","version":"0.0.1"}}}'
try {
  $r = Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $bodyInit -TimeoutSec 20
  Write-Output ('INIT_STATUS=' + [int]$r.StatusCode)
  $sess = $r.Headers['mcp-session-id']
  if ($sess) { Write-Output 'SESSION_OK' } else { Write-Output 'SESSION_NONE' }
  $txt = [string]$r.Content
  if ($txt.Length -gt 3000) { $txt = $txt.Substring(0, 3000) }
  Write-Output '---INIT_BODY---'
  Write-Output $txt
  $headers2 = @{
    'Content-Type' = 'application/json'
    'Accept' = 'application/json, text/event-stream'
    'x-api-key' = $tok
  }
  if ($sess) { $headers2['mcp-session-id'] = $sess }
  $bodyNotif = '{"jsonrpc":"2.0","method":"notifications/initialized"}'
  try { Invoke-WebRequest -Uri $uri -Method Post -Headers $headers2 -Body $bodyNotif -TimeoutSec 15 | Out-Null } catch {}
  $bodyTools = '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
  $r2 = Invoke-WebRequest -Uri $uri -Method Post -Headers $headers2 -Body $bodyTools -TimeoutSec 20
  Write-Output ('TOOLS_STATUS=' + [int]$r2.StatusCode)
  $txt2 = [string]$r2.Content
  if ($txt2.Length -gt 8000) { $txt2 = $txt2.Substring(0, 8000) + '...TRUNCADO' }
  Write-Output '---TOOLS_BODY---'
  Write-Output $txt2
} catch {
  Write-Output ('ERROR: ' + $_.Exception.Message)
  if ($_.ErrorDetails.Message) {
    $em = $_.ErrorDetails.Message
    if ($em.Length -gt 2000) { $em = $em.Substring(0, 2000) }
    Write-Output $em
  }
}
