import requests
import json
#Nombre = Diego Garza Martinez
#Matricula = 2076284
if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    argumentos ={'nombre':'Diego','matricula':'2076284','curso':'Programacion para Ciberseguridad'}
    response = requests.post(url, params=argumentos)

    if response.status_code == 200:
        print(response.content)