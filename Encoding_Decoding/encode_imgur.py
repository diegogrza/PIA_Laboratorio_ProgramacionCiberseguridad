import requests
import base64
from requests import Response
#Diego Garza Martinez 2076284
#
#Para descargar la imagen del sitio 
#
if __name__ == '__main__':
	url = 'https://imgur.com/gallery/LmzKv6k'
	Response : Response = requests.get(url, stream=True)
	with open('dog.jpg','wb') as file_down:
		for chunk in Response.iter_content():
			file_down.write(chunk)
	Response.close()
#
#Para codificar la imagen
#
with open('dog.jpg','rb') as binary_file:
	binary_file_data =  binary_file.read()
	base64_encoded_data = base64.b64encode(binary_file_data)
	base64_encoded_message = base64_encoded_data.decode('utf8')
	print(base64_encoded_message)
