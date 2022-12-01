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
#Formateamos la salida del objecto results de bs4
print(results.prettify())