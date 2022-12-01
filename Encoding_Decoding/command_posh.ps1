Clear-Host
#Comando powershell a codificar en base64
$comando = "Get-WmiObject win32_logicaldisk | foreach {write-host $_.deviceID $_.size $_.freespace}"
#
#Codificando comando
#
$encode = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($comando))
#
#Ejecutando comando codificado
#
Write-Host "Vamos a ejecutar el comando asi en powershell -E" $encode -ForegroundColor Cyan
Start-Sleep 1
powershell -E $encode
Start-Sleep 2
#
#$comand_secret guarda un comando codificado en powershell
# 
$comando_secret = "RwBlAHQALQBXAG0AaQBPAGIAagBlAGMAdAAgAHcAaQBuADMAMgBfAGIAYQBzAGUAcwBlAHIAdgBpAGMAZQAgAHwAZgBvAHIAZQBhAGMAaAAgAHsAVwByAGkAdABlAC0ASABvAHMAdAAgACQAXwAuAGQAaQBzAHAAbABhAHkAbgBhAG0AZQAgACQAXwAuAHMAdABhAHQAZQB9AA=="
#
#Decodificamos el mensaje
#
$decod = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($comando_secret))
#
#Mostramos el resultado
#
Write-Host "El comando codificado es : " -ForegroundColor Cyan
Write-Host $comando_secret
Write-Host "El comando decoficado es : " -ForegroundColor Cyan
Write-Host $decod