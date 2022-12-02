# **Scripting_Powershell**
Este proyecto viene en conjunto con 2 scripts , que te facilitaran mucho la vida a la hora de escanear redes, ya que son scripts en powershell y lo puedes usar en practicamente muchas maquinas.
1. **escaneo_equipos_red.ps1**
Con este escaneo, dectectaremos los equipos activos en nuestra red, este es muy util para cuando estas en tu casa, y quieres ver si alguien mas esta usando tu internet.
Ejecutaras el codigo y solo hara todo, y te va imprimiendo los hosts de tu red que respondieron. (equipos encontrados)


2. **escaneo_puertos.ps1**
Despues de que ya tengas los equipos encontrados, usaras esas ip para escanear sus puertos y ver cuales estan abiertos. Si ves la variable **$portstoscan** ahi veras los puertos que escanearemos, puedes modificar agregando o quitando al gusto. La ip a escanear el mismo script te la pida al momento de ejecutar el codigo

