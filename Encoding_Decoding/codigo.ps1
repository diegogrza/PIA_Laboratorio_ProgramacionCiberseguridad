Clear-Host
#
#Diego Garza Martinez 2076284
#
Write-Host "Bienvenido a un ejemplo de codificar / decoficar en base64 usando powershell" -ForegroundColor Green
Write-Host "Codificando un archivo de texto"
#
#Se va a leer el contenido del archivo de texto 
#
$input_file = "C:\Users\diego\UANL\5_semestre\lab_progra_ciberseguridad\Practica07\secret.txt"
$fc = Get-Content $input_file
$GB = [System.Text.Encoding]::UTF8.GetBytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo codificado es : " $etext -ForegroundColor Green
#
#Decoficando contenido de un archivo 
#
Write-Host "Decodificando el testo previo"
[System.Text.encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" C:\Users\diego\UANL\5_semestre\lab_progra_ciberseguridad\Practica07\secret.txt
$outfile12 = Get-Content C:\Users\diego\UANL\5_semestre\lab_progra_ciberseguridad\Practica07\secret.txt
Write-Host "El texto decodificado es el siguiente" -ForegroundColor Green
Write-Host "DECODIFICADO : " $outfile12