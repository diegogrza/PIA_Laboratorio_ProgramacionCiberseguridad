#Escaneo de puertos mas comunes
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

#Definimos lista con puertos que se escanarean
$portstoscan = @(20,21,22,23,24,25,51,52,53,80,110,119,135,136,137,138,139,,143,161,162,389,443,445,636,1025,1443,3389,5985,5986,8080,10000)
#Definimos un tiempo de espera
$waittime = 100

#Solicitamos IP a escanear
Write-Host 'Direccion IP a escanear: ' -NoNewline
$direccion = Read-Host

#Generamos bucle para escanear cada puerto
foreach ($p in $portstoscan)
{
    $TCPObject = new-object System.Net.Sockets.TcpClient
        try { $resultado = $TCPObject.ConnectAsync($direccion,$p).Wait($waittime)}catch{}
        if ($resultado -eq 'True')
        {
            Write-Host 'Puerto abierto = ' -NoNewline; Write-Host $p -ForegroundColor Green
        }
}

        
