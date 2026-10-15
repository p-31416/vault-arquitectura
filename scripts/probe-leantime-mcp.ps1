# probe-leantime-mcp.ps1 — Sonda read-only al MCP remoto de Leantime
# NOTA ES: lee LEANTIME_TOKEN desde .env local, nunca lo imprime, solo muestra su largo.
# NOTA ES: hace initialize JSON-RPC y luego tools/list para ver si existe users.create.
$ErrorActionPreference = 'Stop'
# NOTA ES: ruta del .env junto a este vault
$envFile = Join-Path $PSScriptRoot '..\\.env'
if (-not (Test-Path $envFile)) { $envFile = '.\\.env' }
# NOTA ES: extrae la linea LEANTIME_TOKEN=... sin mostrar el valor
$tok = $null
foreach ($line in Get-Content $envFile) {
  $t = $line.Trim()
  if ($t.StartsWith('LEANTIME_TOKEN=')) {
    $tok = $t.Substring(16).Trim().Trim('"').Trim("'")
    break
  }
}
if (-not $tok) { Write-Output 'NO_TOKEN_FOUND'; exit 1 }
Write-Output ('TOKEN_LEN=' + $tok.Length)
# NOTA ES: cabeceras que pide Leantime 3.10.3+ Streamable HTTP
$headers = @{
  'Content-Type' = 'application/json'
  'Accept' = 'application/json, text/event-stream'
  'x-api-key' = $tok
}
$uri = 'https://pitautech-leantime.3nq4ow.easypanel.host/mcp'
# NOTA ES: paso 1 initialize
$bodyInit = '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"probe","version":"0.0.1"}}}'
try {
  $r = Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $bodyInit -TimeoutSec 20
  Write-Output ('INIT_STATUS=' + [int]$r.StatusCode)
  $sess = $r.Headers['mcp-session-id']
  if ($sess) { Write-Output ('SESSION_LEN=' + $sess.Length) } else { Write-Output 'SESSION_NONE' }
  $txt = [string]$r.Content
  if ($txt.Length -gt 3000) { $txt = $txt.Substring(0,3000) }
  Write-Output '---INIT_BODY---'
  Write-Output $txt
  # NOTA ES: paso 2 notifications/initialized + tools/list si hubo sesion o aun sin sesion
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
  if ($txt2.Length -gt 8000) { $txt2 = $txt2.Substring(0,8000) + '...TRUNCADO' }
  Write-Output '---TOOLS_BODY---'
  Write-Output $txt2
} catch {
  Write-Output ('ERROR: ' + $_.Exception.Message)
  if ($_.ErrorDetails.Message) {
    $em = $_.ErrorDetails.Message
    if ($em.Length -gt 2000) { $em = $em.Substring(0,2000) }
    Write-Output $em
  }
}
