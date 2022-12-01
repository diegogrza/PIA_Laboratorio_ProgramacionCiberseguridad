#Escaneo de equipos activos en la subred

#Determinando el gateway
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host '== Determinando tu Gateway ...'
Write-Host 'Tu gateway es: '$subred

#Determinando rango de subred
$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3)
Write-Host '== Determinando tu subred ...'
echo $rango

#Determinando si el $rango termina en '.'
#En ocasiones el rango de la subred no termina en punto, asi que tenemos que hacerlo

$punto = $rango.EndsWith('.')
if ( $punto -like 'False')
{
    $rango = $rango + '.' #Se agrega el punto en caso que no lo tuviera
}

#Creamos un array con 254 numeros (1 a 254) y se almacenan en $rango_ip
$rango_ip = @(1..254)

Write-Output ''
Write-Host '-- Subred actual : '
Write-Host 'Escaneando: '-NoNewline ; Write-Host $rango -NoNewline ; Write-Host '0/24' -ForegroundColor Red
Write-Output ''

#Generamos un bucle foreach para validar hosts activos en nuestra subred
foreach ($r in $rango_ip)
{
    $actual = $rango + $r #se genera la direccion ip con la subred y el array previamiente creado
    $responde = Test-Connection $actual -Quiet -Count 1 # Validamos conexion en la ip 
    if ($responde -eq 'True')
    {
        Write-Output ""
        Write-Host 'Host responde: ' -NoNewline; Write-Host $actual -ForegroundColor Green
    }
}


