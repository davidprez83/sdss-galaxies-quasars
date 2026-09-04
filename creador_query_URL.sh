#!/bin/bash

# Se pide al usuario que ingrese la solicitud en lenguaje SQL
read -p "ingrese su QUERY en lenguaje SQL: " QUERY
QUERY=${QUERY:-SELECT TOP 80000 objID, class, z, zErr, zWarning, modelMag_g, modelMag_r, modelMagErr_g, modelMagErr_r, modelMag_g - modelMag_r AS color_gr FROM Specphoto WHERE class IN (\'GALAXY\', \'QSO\') AND zWarning = 0 AND z > 0 AND modelMag_g > 0 AND modelMag_r > 0 ORDER BY NEWID()}

reemplazos=(
    ",|%2C"
    "=|%3D"
    " |%20"
    ">|%3E"
    "(|%28"
    ")|%29"
    "'|%27"
)

for i in "${reemplazos[@]}"; do
    caracter="${i%%|*}"
    codigo="${i#*|}"
	QUERY="${QUERY//$caracter/$codigo}" ; done

echo $QUERY


