#Diego Garza Martinez 2076284
#
import requests
import csv
from bs4 import BeautifulSoup
#
#URL de la pagina
url = 'http://quotes.toscrape.com/'
#
#Ejecutar Get-Request
response = requests.get(url)
#
#Analizar sintacticamente el archivo html de bs4 del texto fuente
html = BeautifulSoup(response.text, 'html.parser')
#
#Extraer todas las citas y autores del archivo html
quotes_html = html.find_all('span', class_='text')
authors_html = html.find_all('small', class_='author')
#
#Crea una lista de las citas
quotes = list()
for quote in quotes_html:
	quotes.append(quote.text)
#
#crea una lista de autores
authors = list()
for author in authors_html:
	authors.append(author.text)
#
#Hacemos la prueba y imprimimos los resultados
for t in zip(quotes, authors):
	print(t)
#Guardamos las citas y los autores en un archivo CSV en el directorio actual
with open('./citas_2076284.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file, dialect='excel')
	csv_writer.writerows(zip(quotes, authors))