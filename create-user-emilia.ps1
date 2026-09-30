[System.Net.ServicePointManager]::ServerCertificateValidationCallback = { $true }
$body = Get-Content 'P:\00-repos\pitau-tech\user-emilia.json' -Raw
$headers = @{
    Authorization = 'Bearer lt_TBqOUBHoTTgBJETAQNPYQHwbXkZXqhsR_5tUbOCMPf08Pk95Aifl9cZOmGEnL7VNi'
    'Content-Type' = 'application/json'
}
try {
    $result = Invoke-RestMethod -Uri 'https://pitau.tech/api/users' -Method Post -Headers $headers -Body $body
    Write-Output "RESULT: $($result | ConvertTo-Json -Depth 3)"
} catch {
    Write-Output "ERROR: $($_.Exception.Message)"
}
