import requests
from bs4 import BeautifulSoup

url = 'https://globo.com/'

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

lista_noticias = soup.find_all('li',class_='menu-products__list__item')

for lista_titulos in lista_noticias:
    

