\# Galaxias y Cuásares primordiales

Análisis del índice de color (g-r) en función del redshift (z)

para galaxias y cuásares utilizando datos de SDSS DR18.



\## Objetivo 

El objetivo de este proyecto es practicar como se hace una consulta de datos desde bash para la limpieza y el análisis de tablas de datos de interés, en este caso se quiere estudiar la relación entre el índice de color y el redshift reportados para galaxias y Cuasares y llegar a hacer el diagrama de índice de color - redshift que evidencia la expansión del universo.



\## Datos



Los datos utilizados provienen del Sloan Digital Sky Survey (SDSS),

Data Release 18 (DR18).



Se utiliza la tabla `SpecPhoto`, que combina información

espectroscópica y fotométrica de los objetos.



Las principales variables utilizadas son:



\- `objID`: identificador del objeto.

\- `class`: clasificación espectroscópica del objeto.

\- `z`: redshift.

\- `zErr`: incertidumbre del redshift.

\- `zWarning`: indicador de posibles problemas en la medición del redshift.

\- `modelMag\_g`: magnitud en la banda fotométrica g.

\- `modelMag\_r`: magnitud en la banda fotométrica r.



A partir de las magnitudes se calcula el índice de color:



$g-r = modelMag\_g - modelMag\_r$



\## Metodología



El análisis está dividido en tres etapas principales:



1\. Descarga de los datos mediante una consulta al servidor de SDSS.

2\. Limpieza y almacenamiento de los datos en una base de datos SQLite.

3\. Extracción, análisis y visualización de los datos mediante Python.



\### `creador\_query\_URL.sh`

Este script recibe un query en lenguaje SQL para la base de datos de skyserver con espacios, comillas y todos los símbolos especiales y lo convierte a un str listo para agregar a un endpoint.



\### `constructor\_db.py`



Este script utiliza Pandas para leer el archivo CSV descargado,

realizar la limpieza necesaria y almacenar los datos en una base

de datos SQLite llamada `datos\_mision.db`.



\### `analisis\_visual.py`



Este script se conecta a `datos\_mision.db`, realiza la consulta SQL

correspondiente, calcula las cantidades necesarias para el análisis

y genera la gráfica final.}



\### `pipeline.sh`



El script `pipeline.sh` automatiza todo el proceso.

Descarga los datos desde SDSS usando `creador\_query\_URL.sh` y ejecuta los scripts de Python

necesarios para construir la base de datos y generar el resultado final.



\## 5. Resultados



La siguiente gráfica muestra el índice de color (g-r) en función

del redshift (z) para las galaxias y los cuásares seleccionados.



!\[Redshift vs Índice de Color](resultado.png)





Se puede observar que hay un porcentaje de cuásares que tiene un redshift demasiado grande y un índice de color no muy grande, lo que sirve de evidencia para fortalecer la hipótesis de la expansión.





README.md

│

├── 1. Descripción del proyecto

├── 2. Problema científico

├── 3. Datos utilizados

├── 4. Metodología / Pipeline

├── 5. Estructura del repositorio

├── 6. Consulta SQL y filtros

├── 7. Análisis y resultado

├── 8. Interpretación física

└── 9. Cómo ejecutar el proyecto

