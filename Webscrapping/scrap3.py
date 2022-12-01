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
#Imprimimos todos los elementos
for job_element in job_elements:
	print(job_element, end='\n'*2)