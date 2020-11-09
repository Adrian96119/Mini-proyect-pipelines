def duracionApi_idbm(x):
	from dotenv import load_dotenv
	import os
	import requests
	





	load_dotenv()
	
	clave = os.getenv("clave_pepito")



	url = "https://imdb-api.com/"


	endpoint = "/en/API/Title/{apiKey}/{id}"
	repo_info = {
	    "apiKey":clave,
	    "id": x
	    }

	data = requests.get(url+endpoint.format(**repo_info)).json()
	rating = data["runtimeMins"]
	return rating

print(duracionApi_idbm("tt0091495"))
#CON ESTA FUNCION, PODRIAMOS SACAR LA DURACIÓN DE LAS PELICULAS DE LA API DE IDBM MIENTRAS EXISTA O NO SEA NULO EL VALOR. PERO PARA ELLO DEBEMOS METER COMO ARGUMENTO EL ID
#DE LA PELÍCULA.



#df = pd.read_csv("../directores.csv",encoding = "ISO-8859-1")

#print(df["Title"].map(duracionApi_idbm))

