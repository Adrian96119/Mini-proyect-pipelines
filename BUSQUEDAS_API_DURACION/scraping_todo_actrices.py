

import requests
from bs4 import BeautifulSoup
import re
url = "https://www.imdb.com/title/tt0056355/?ref_=nv_sr_srsg_0" #voy sustituyendo en la url el id que he sacado en el archivo con la funcion
#funcion clave_id del archivo funcion_id  y me va dando el lugar donde se encuentra. Funciona en todos por igual
#esta esa actriz
actriz = requests.get(url).text

soup = BeautifulSoup(actriz, "html.parser")
actriz_peli= soup.find_all("div", class_ = "credit_summary_item")

print(actriz_peli[2]) 

print("-----------------------------------------------------------")

#el ejemplo sacado ha sido con la pelicula The Bellboy & the Playgirls , pero poniendo la Id del título que quieras te saca a la actriz correspondiente.
"""

Raging Bull tt0081398 --> Cathy Moriarty
Ginger & Fred tt0091113 --> Giulietta Masina
Wagonmaster	tt0043117 ----> Joanne Dru
Duel tt0067023 ------> >Jacqueline Scott
Wise Guys tt0092226 ------> No hay actriz principal
Bellboy & the Playgirls The tt0056355 --------------> June Wilkinson
Law of Desire tt0093412 -------------> Karin Dor
Full Metal Jacket tt0093058 ---------------> No hay actriz principal
Untouchables The tt0094226 ----------------> No hay actriz principal
Apocalipse Now tt0078788 ------------------> No hay actriz principal
For a Few Dollars More tt0059578 ----------> No hay
Indiana Jones & the Last Crusade t0097576 -------------> No se sabe
A Clockwork Orange tt0066921 ---------> No hay
Last Hurrah The tt0051845 ---------------> Dianne Foster
Firefox tt0083943 -----------------> No hay
They Were Expendable tt0038160 -------------> Donna Reed

"""