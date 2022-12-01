#Diego Garza Martinez 2076284
#
import requests
from bs4 import BeautifulSoup
#
#Obtienes html
URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)
#
#Analizamos el contenido html con bs4
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
#
#Buscar todos los elemntos de la clase jobs_elements 
job_elements = results.find_all('div', class_='card-content')
#
#Buscar elementos en 'h2' que contengan 'python' en su texto
python_jobs = results.find_all(
	'h2', string=lambda text: 'python' in text.lower()
	)
#
#Buscar cada elemento que tenga referencia python_jobs
python_jobs_elements = [
	h2_element.parent.parent.parent for h2_element in python_jobs
	]

#Mostramos la cantidad de elementos que cumplan la busqueda
print(len(python_jobs))
#
#Solamente mostramos empleos de python
for job_element in python_jobs_elements:
	title_element = job_element.find('h2', class_='title')
	company_element = job_element.find('h3', class_='company')	
	location_element = job_element.find('p', class_='location')
	#Buscamos elementos con etiqueta 'a' y href
	link_url = job_element.find_all('a')[1]['href']
	print(title_element.text.strip())
	print(company_element.text.strip())
	print(location_element.text.strip()+'\n')
	#Imprimimos link
	print(f'Apply here: {link_url}\n')
