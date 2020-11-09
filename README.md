# Mini-proyect-pipelines by Adrian Madrid

## DESCRIPCIÓN

**HE COGIDO UNA BASE DE DATOS REFERENTE A LAS MEJORES PELÍCULAS DEL SIGLO XIX CON EL OBJETIVO DE LIMPIARLA Y FILTRAR LOS DATOS
QUE ME INTERESAN, PARA POSTERIORMENTE ENRIQUECER EL DATAFRAME CON INFORMACIÓN DE LA API DE IBDM Y HACIENDO WEB- SCRAPING A SU
PAGINA WEB. FINALMENTE CON TODOS LOS DATOS YA RECOGIDOS, HEMOS HECHO UNOS CUANTOS ANALISIS Y HEMOS SACADO CIERTAS CONCLUSIONES.

### PASO 1

**HEMOS LIMPIADO EL DATABASE ORIGINAL DEJANDO LAS COLUMNAS QUE MÁS NOS INTERESABAN**:
 TITULO DE LA PELICULA, DURACION, DIRECTOR, ACTOR PRINCIPAL. ACTRIZ PRINCIPAL, AÑO DE LA PELICULA, Y EL GÉNERO.
**RELLENAMOS LOS VALORES NULOS DE LA COLUMNA DURACION Y DE LA COLUMNA DE ACTRICES PARA QUE NUESTROS ANALISIS SEAN ÓPTIMOS.

EN EL REPOSITORIO, ENCONTRAREMOS UNA CARPETA DONDE SE ENCUENTRA TODO EL CÓDIGO QUE HEMOS UTILIZADO PARA SACAR LA NUEVA INFORMACIÓN
Y RELLENAR LOS VALORES NULOS.

-> columna duracion: Hemos creado una función para trabajar con la API de Ibdm que nos saca el id de cada pelicula. {funcion_id.py}
 Hemos creado otra función que nos saque la duración de cada pelicula introduciendo el id {funcion_duracion.py}
 *SE PUEDEN COMPROBAR ESTAS FUNCIONES CON EL KEY QUE TE PROPORCIONE LA API DE IBDM.*
 
 Hay otro archivo que se llama todas_las_duraciones donde se pueden ver todas las duraciones que nos faltaban.
 Cada duracion que nos faltaba se puede comprobar individualmente en los cuatro archivos: duracion_matador.py, 
 duracion_apy_ginger&fred.py y duracion_goodfellas_scraping donde en esta última se utilizo el scraping para cambiar un poco.
 
 --> Con la columna de las actrices, hicimos todo por Web Scraping. En el archivo scraping_todo_actrices.py
 se puede ver un ejemplo de como sacamos con scraping la actriz principal de tiburón, que no aparecia en la columna de Actress.
 En él, se verá una URL en el que sustituiremos el id por el de la pelicula que busquemos. Esta preparado todo de tal manera que
 usando la funcion para sacar el id de la pelicula, lo pongas en la URL y te aparezca el nombre de la Actriz.
 **NOTA --> SI NO APARECE ES PORQUE NO HAY ACTRIZ PRINCIPAL
 
 -->COLUMNA NUEVA DE RATINGS: Esta es la que mas curro dió, ya que tuvimos que sacar uno a uno la id de
 cada película(que eran muchas):p y en el archivo scraping_ratins.py hicimos lo mismo que con el de actrices.
 Iba sustituyendo los id en la url y me iba sacando automáticamente el rating de todas. Se puede comprobar
 perfectamente dentro del archivo con el ID que quieras.
 
 HUBO UN INTENTO DE FUNCIÓN DE RATING DEL ARCHIVO {funcion_rating.py} pero se me acabaron las solicitudes!
>> Tuve que buscar además correos temporales para evitar el spameo!

**POSTERIORMENTE RELLENAMOS EL DATAFRAME MEDIANTE DICCIONARIOS CON LOS DATOS QUE SACAMOS DE LOS PASOS ANTERIORES.
 
*****FINALMENTE, EXPORTAMOS YA LA TABLA TERMINADA A OTRO CUADERNO JUPITER LLAMADO ANALISIS PARA HACER NUESTRAS
DEDUCCIONES ACERCA DE LOS DATOS DEL DATASET.


-CARPETA CON TODAS LAS FUNCIONES Y CODIGO DE EXTRACCION DE DATOS A TRAVES DE API Y WEB-SCRAPING.

-UN GITIGNORE PARA NO SUBIR TODAS NUESTRAS CLAVES UTILIZADAS DE LA API DE IBDM

-CUADERNO JUPITER DE LIMPIEZA LLAMADO CLEAN

-CUADERNO JUPITER DE ANALISIS LLAMADO ANALISIS

-1 CSV LLAMADO **MovieDataset.csv** QUE ES EL DATAFRAME ORIGINAL ANTES DE LIMPIARLO.

-1 CSV LLAMADO **Movies_Ibdm.csv** QUE CONTIENE EL DATAFRAME LIMPIO.

