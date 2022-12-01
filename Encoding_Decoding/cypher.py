#importamos fernet desde cryptography
#
#Diego Garza Martinez 2076284
from cryptography.fernet import Fernet 
#
#Definicion del funcion genwrite que genera una llave
#para cifrado
def genwrite():
	key = Fernet.generate_key()
	with open('pass.key','wb') as key_file:
		key_file.write(key)
#Llamamos a la funcion genwrite para generar el archivo con pass_key.
#que contiene la llave
genwrite()
#Definicion de la funcion call_key con la cual leemos 
#el contenido del archivo pass_key
def call_key():
	return open('pass.key','rb').read()
#
#Ahora ciframos un mensaje almacenado y codificado previamente
key = call_key()
banner = 'Bienvenido al script de cypher :D '.encode()
a = Fernet(key)
coded_banner = a.encrypt(banner)
print(coded_banner)
#
#Ahora desciframos el mensaje previamente cifrado 
key = call_key()
b = Fernet(key)
decoded_banner = b.decrypt(coded_banner)
print(decoded_banner)
