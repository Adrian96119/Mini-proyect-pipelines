
def clave_id(*expression):
	from dotenv import load_dotenv
	import os
	import requests

	load_dotenv()
		
	clave = os.getenv("clave_pepito")



	url = "https://imdb-api.com/"


	endpoint = "/en/API/SearchMovie/{apiKey}/{expression}"
	repo_info = {
		"apiKey":clave,
		"expression":expression
		}

	data = requests.get(url+endpoint.format(**repo_info)).json()
	resultados =data["results"]
	r = resultados[0]
	for i,x in r.items():
		if i == "id":
			expression = x.strip()
	return expression

print(clave_id("Raging Bull"))

#Con esta funcion obtenemos el ID de la pelicula que le metamos.
#Vamos a sacar el id de todas las peliculas. Hay que usar una clave Api de idbm.
"""
Raging Bull tt0081398
Ginger & Fred tt0091113
Wagonmaster	tt0043117
Wagon Master tt0043117
Duel tt0067023
Wise Guys tt0092226
Bellboy & the Playgirls The tt0056355
Law of Desire tt0093412
Full Metal Jacket tt0093058
Untouchables The tt0094226
Apocalipse Now tt0078788
For a Few Dollars More tt0059578
Indiana Jones & the Last Crusade t0097576
A Clockwork Orange tt0066921
Last Hurrah The tt0051845
Firefox tt0083943
They Were Expendable tt0038160
'2001: A Space Odyssey', tt0062622
'8 1/2', DESCONOCIDO

'A Fistful of Dollars', tt0058461
 'After Hours', tt0088680
 'Aliens', tt0078748
 'Amarcord', tt0071129
 'Arrowsmith', tt0021622
 'Battle of Midway The', tt0034498
 ,
 'Bird', tt12592252
 'Bonfire of the Vanities The', tt0099165
 'Bronco Billy', tt0080472
 'Cape Fear', tt0101540
 'Color of Money The', tt0090863
 'Conversation The', tt0071360
 "Donovan's Reef", tt0057007

 'E. T. The Extra-Terrestrial', tt0083866
 'Eiger Sanction The', tt0072926
 'El Guerrero Solitario', tt0091187
 'Empire of the Sun', tt0092965
 'Fellini Satyricon', tt0064940
 'Fort Apache', tt0040369

 'Gardens of Stone', tt0093073
 'Gauntlet The', tt0076070

 'Godfather The', tt0068646

 'Heartbreak Ridge', tt0091187
 'High Heels', tt0103030
 'High Plains Drifter', tt0068699
 'Honkytonk Man', tt0084088
 'Hook', tt0102057
 'Horse Soldiers The', tt0052902
 'Il Bidone', tt0047876
tt0073195
 'Jaws', tt0073195
 'Judge Priest', tt0025335
 "Killer's Kiss", tt0048254
 'Killing The', tt10665338
 'King of Comedy', tt0188766
 'La Dolce Vita', tt0053779
 'Last Hurrah The', tt0051845
 'Last Temptation of Christ The', tt0095497

 'Lolita', tt0056193
 'Long Gray Line The', tt0048312
 'Long Voyage Home The', tt0032728
 'Man Who Shot Liberty Valance The', tt0056217

 'Mister Roberts', tt0048380
 'Mogambo', tt0046085
 'My Darling Clementine', tt0038762
 'New York New York', tt0076451
 'New York Stories', tt0097965
 'Night Gallery', tt6967644
 'Nineteen Forty-One', tt0271675
 'Outsiders The', tt0086066
 'Pale Rider', tt0089767
 'Paths of Glory', tt0050825
 'Peggy Sue Got Married', tt0091738
 'People The', tt0083722
 'Pepi Luci Bom', tt0081323
 'Pink Cadillac', tt0098097
 'Play Misty for Me', tt0067588

 'Raiders of the Lost Ark', tt0082971
 'Rain People The', tt0064873
 'Rio Grande', tt0042895
 'Roma', tt6155172
 'Rookie THe',
 'Rumble Fish',
 'Searchers The',
 'She Wore a Yellow Ribbon',
 'Shining The',
 'Spartacus',
 'Sugarland Express The',
 'Sun Shines Bright The',
 'Terminator 2',
 'Terminator The',
 'They Were Expendable',
 'Three Godfathers',
 'Tie Me Up! Tie Me Down!',
 'Tonight for Sure',
 'Tucker: The Man & His Dream',

 'Wagon Master',

 'Wee Willie Winkie',
 'What Price Glory?',
 'White Hunter Black Heart',
 'Wings of Eagles The',

 'Women on the Verge of a Nervous Breakdown'
 """

