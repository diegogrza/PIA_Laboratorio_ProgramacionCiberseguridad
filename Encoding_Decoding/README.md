# **Encoding_Decoding**
En este proyecto hay 3 scripts
1. codigo.ps1
2. cypher. py
3. encode_imgur.py

codigo.ps1
---
En este script de powershell debes de modificar las rutas de las carpetas de donde sacaras tu **secreto**, el cual codificaras, este necesita ser un archivo txt

cypher. py
---
En este script de python se utiliza el modulo cryptography, pero solamente el modulo fernet, con el que nos ayudara a generar una llave, con la cual cifraremos y descifraremos una frase

encode_imgur.py
---
En este script de python, lo que realizaremos es codificar una imagen, la cual obtendremos de internet, en la variable llamada **url** ,ahi podras poner cualquier link de una imagen, la cual descargaremos y despues la codificaremos con base64
