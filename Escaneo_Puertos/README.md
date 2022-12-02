# **Escaneo_Puertos**
En este proyecto hay 3 scripts
1. scan_portv1.py
2. scan_portv2.py
3. scan_portv3.py

scan_portv1.py
---
En este script de python se ejecuta por medio de argumentos, con los cuales haremos un bucle para encontrar los puertos abiertos de un host. el rango de puertos a elegir lo pones en los argumentos

scan_portv2.py
---
En este script de python se escanea 4 puertos, pero en en toda la red donde se encuentra un host. La ip de la subred la tienes que modificar en el codigo en la variable llamada **addr**, y tambien puedes modificar el rango de puertos en la variable llamada **ports**

scan_portv3.py
---
En este script de python, es una combinacion de los 2 anteriores, mediante el uso de argumentos y escaneando toda la red, la cual utilizaremos una funcion llamada tcp_test