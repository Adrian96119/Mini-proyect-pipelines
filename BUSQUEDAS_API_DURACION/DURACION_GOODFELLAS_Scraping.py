import requests
from bs4 import BeautifulSoup
import re
url = "https://www.imdb.com/title/tt0099685/?ref_=fn_al_tt_1"
goodfellas = requests.get(url).text

soup = BeautifulSoup(goodfellas, "html.parser")
duracion = soup.find_all("time")


duracion_goodfellas = [i.text.strip() for i in duracion]
print(duracion_goodfellas[1])


#EN ESTA OCASIÓN, HE QUERIDO SACAR LA DURACIÓN MEDIANTE WEB SCRAPING.