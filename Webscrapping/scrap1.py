import requests
#
#Obtener el html de la url
URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)
#
#Imprimir texto de la peticion get
print(page.text)