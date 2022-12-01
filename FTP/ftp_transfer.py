#SCRIPT para transferir archivos usando un servidor ftp
#Diego Garza Martinez 2076284
#
#importar modulo ftp
from ftplib import FTP 
#
def subiendo_archivo():
	
	try:
		#Intentamos entrar al servidor
		ftp = FTP('192.168.1.86')
		#
		#hacemos login con el usuario y su contraseña
		ftp.login('johnny', '2076284')
		#
		print('[+] Conexion exitosa establecida !! ')
		#listamos que hay en la carpeta ftp
		ftp.retrlines('LIST')
		#
		#accedemos a la carpeta upload"
		ftp.cwd('upload')
		#
		#abrimos el archivo para poder subirlo
		file = open('ADVERTENCIA.txt', 'rb')
		#subimos el archivo
		ftp.storlines('STOR ADVERTENCIA.txt',file)
		#
		#salimos de la sesion y cerramos el archivo
		ftp.quit()
		file.close()
	except Exception as e:
		print('[-] Hubo un ERROR = ' + str(e))

subiendo_archivo()