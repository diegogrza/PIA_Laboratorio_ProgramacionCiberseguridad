#/usr/bin/python
# -*- coding: utf-8 -*-
# diego garza martinez 2076284
# parte 1
# importamos librerias necesarias
import sys
import threading
from socket import *
#
# parte 2
# creamos una funcion tcp_test la cual
# permite probar mediante socket los puertos
# abiertos, se les agrega lock.release()
def tcp_test(port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(10)
	result = sock.connect_ex((target_ip, port))
	if result == 0:
		print("Opened port: ", port)
#
# parte 3
# establecemos el main del scrypt
# guardamos en variables host y portstrs
if __name__ == '__main__':
	# portscan.py <host> <start_port>-<end_port>
	host = sys.argv[1]
	portstrs = sys.argv[2].split('-')
#
# parte 4
# portstrs se convierte en lista al momento
# de hacer split y de ahi obtener valores
start_port = int(portstrs[0])
end_port = int(portstrs[1])
#
# parte 5
# usando la funcion gethostname se obtiene
# la direccion ip
target_ip = gethostbyname(host)
#
# parte 6
# se inicia bucle para probar puertos
# usando la funcion tcp_test y generando
# un hilo por cada puerto probar
hilos = []
for port in range(start_port, end_port):
	hilo = threading.Thread(target=tcp_test, args=(port,))
	hilos.append(hilo)
	hilo.start()
