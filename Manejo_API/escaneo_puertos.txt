import socket



# creo un nuevo objecto de socket,con especificaciones de conectores ipv4, y sock_Stream es para conexiones TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#preguntas por la ip que se va a escanear
ip = input('Cual ip deseas escanear: ')
#en esta variable se guarda que puerto escanearas
puerto = int(input('Cual puerto deseas escanear: '))

def escaneo(puerto): #en esta funcion se realiza el escaneo del puerto que se especifique en la variable
    try:
        s.connect((ip, puerto))
        return True #si responde el puerto regresara true
    except:
        return False

if escaneo(puerto): #aqui si el resultado de la funcion es True, es imprimira que si esta abierto el puerto
    print('El puerto ', puerto,' esta abierto!')
else:
    print('El puerto ', puerto, ' esta cerrado!')