#import requests 
#URL = "https://eproc.trf2.jus.br/eproc/externo_controlador.php?acao=processo_consulta_publica&txtNumProcesso=50004043120184025112"
#r = requests.get(URL) 
#print(r.text) 

#from bs4 import BeautifulSoup
#import re
# import urllib2

#url = "file:///C:/Users/wallace/Documents/teste_python/data/arquivo_01.html"
#page = open(url)
#soup = BeautifulSoup(page.read())

#cities = soup.find_all('span', {'class' : 'city-sh'})

#for city in cities:
 #   print city

#from bs4 import BeautifulSoup
#import requests 
#soup = BeautifulSoup(page.content, 'html.parser')

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://127.0.0.1:8000/polls/")
res = BeautifulSoup(html.read(),"html5lib");
tags= res.find_all('table', class_='infraTable')
print(tags)