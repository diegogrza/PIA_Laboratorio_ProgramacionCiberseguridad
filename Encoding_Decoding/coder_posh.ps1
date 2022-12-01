#Limpiando pantalla
Clear-Host
#Mensaje de Bienvenida
Write-Host "Ejemplo de codificador base64 en powershell" -ForegroundColor Yellow
Write-Host "Escribe una frase a codificar : " -ForegroundColor Yellow
#Solicitando la entrada de texto
$frase = Read-Host
#Codificando en base64 y guardando resultado en cadena
$encond = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes(($frase)))
#Imprimiendo salida
Write-Host "La frase escrita en base64 es : " -ForegroundColor Green
Write-Output $encond