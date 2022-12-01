#/usr/bin/python
# -*- coding: utf-8 -*-
# parte 1
# importamos librerias necesarias
# diego garza martinez 2076284
import sys 
from socket import *
#
# parte 2
# modo de ejecucion del script
# port_scan.py <host> <start_port>-<end_port>
# primer argumento se guarda en variable host
# segundo en varible portstrs
host = sys.argv[1]
portstrs = sys.argv[2].split('-')
#
# parte 3
# portstrs contiene 2 valores
# en start_port el valor de inicio
# en end_port el valor final
start_port = int(portstrs[0])
end_port = int(portstrs[1])
#
# parte 4
# para usar en el socket asignado
# lo de la variable host en target_ip
# definimos una lista de puertos opened_ports
target_ip = gethostbyname(host)
opened_ports = []
#
# parte 5
# iniciamos bucle para ver puertos abiertos
for port in range(start_port, end_port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(10)
	result = sock.connect_ex((target_ip, port))
	if result == 0:
		opened_ports.append(port)
#
# parte 6 
# se imprime la salida de ports abiertos
print("opened_ports : ")
#
for i in opened_ports:
	print(i)
