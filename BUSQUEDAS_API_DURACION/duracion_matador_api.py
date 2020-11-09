from dotenv import load_dotenv
import os
import requests





load_dotenv()
print("duracion matador")
clave = os.getenv("clave_pepito")



url = "https://imdb-api.com/"


endpoint = "/en/API/Title/{apiKey}/{id}"
repo_info = {
    "apiKey":clave,
    "id":"tt0091495"
    }

data = requests.get(url+endpoint.format(**repo_info)).json()
duracion_matador = data["runtimeMins"]
print(duracion_matador)
