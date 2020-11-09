
def rating(x):
	from dotenv import load_dotenv
	import os
	import requests

	load_dotenv()
			
	clave = os.getenv("clavegmail")



	url = "https://imdb-api.com/"


	endpoint = "/en/API/Ratings/{apiKey}/{id}"
	repo_info = {
		"apiKey":clave,
		"id": x
	}

	data = requests.get(url+endpoint.format(**repo_info)).json()
	return data["imDb"]


#Con esta función sacamos el Rating de cada pelicula en idbm.
