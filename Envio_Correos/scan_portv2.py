#/usr/bin/python
# -*- coding: utf-8 -*-
# parte 1
# importamos librerias
# diego garza martinez 2076284
import socket
#
# parte 2
# se define la funcion scan
# con lo cual se usa socker para probar puertos
def scan(addr, port):
	#creando un nuevo socket
	socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#
	#estableciendo el timeout para el nuevo objecto tipo socket
	socket.setdefaulttimeout(1)
	#
	#conexion exitosa devuelve 0, devuelve error en caso contrario
	result = socket_obj.connect_ex((addr,port)) #direccion y puerto en tupla
	#
	#se cierra el objecto
	socket_obj.close()
	#
	return result
# parte 3
# lista de puertos a escanear
ports=[21,22,25,80]
#
# parte 4
# bucle por todas las ip de x.x.x.x, aqui depende de cual rango sea tu red
for i in range(1,255):
	addr="10.203.212.{}".format(i)
	for port in ports:
		result=scan(addr,port)
		if result==0:
			print(addr, port, "OK")
		else:
			print(addr, port, "Failed")
