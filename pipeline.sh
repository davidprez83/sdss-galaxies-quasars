#!/bin/bash

QUERY=$(./creador_query_URL.sh)
echo $QUERY
URL="https://skyserver.sdss.org/dr18/SkyServerWS/SearchTools/SqlSearch?format=csv&cmd=${QUERY}"

# descargamos el archivo de datos
curl -o datos.csv $URL

# Con los datos descargados se hace la limpieza mediante el script "constructor_db.py"
python constructor_db.py

# Ahora graficamos y creamos resultados.png
python analisis_visual.py

