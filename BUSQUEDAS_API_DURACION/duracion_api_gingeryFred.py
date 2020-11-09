from dotenv import load_dotenv
import os
import requests





load_dotenv()
print("GINGER & FRED")
clave = os.getenv("clave_pepito")



url = "https://imdb-api.com/"


endpoint = "/en/API/Title/{apiKey}/{id}"
repo_info = {
    "apiKey":clave,
    "id":"tt0091113"
    }

data = requests.get(url+endpoint.format(**repo_info)).json()
duracion_GingeryFred = data["runtimeMins"]
print(duracion_GingeryFred)
print("-------------------------------------------")

