import numpy as np
import pandas as pd 
import sqlite3 as sq3

df = pd.read_csv('datos.csv', comment='#')
print("Los datos han sido cargados exitosamente")

print("limpiando la tabla de datos... ")
# se eliminan los registros con valores nulos en las columnas 'z' y 'color_gr', y se eliminan los duplicados basados en 'objID'
df = df.dropna(subset=['z', 'color_gr']) 
df = df.drop_duplicates(subset=['objID'], keep='first')

# Filtrar solo datos sin advertencias en la medicion de redshift
df = df[df['zWarning'] == 0]
#Excluir errores negativos y mantener solo errores menores a 0.01
df = df[(df['zErr'] > 0) & (df['zErr'] < 0.01)]

#Excluimos errores negativos y mantener solo errores menores a 0.01 en las magnitudes
df = df[(df['modelMagErr_g'] > 0) & (df['modelMagErr_g'] < 0.5)]
df = df[(df['modelMagErr_r'] > 0) & (df['modelMagErr_r'] < 0.5)]

# Renombrar columnas del DataFrame pa evitar nombres complejos
df_renombrado = df.rename(columns={
    'objID': 'id_objeto',
    'class': 'clasificacion',
    'z': 'redshift',
    'zErr': 'error_redshift',
    'zWarning': 'advertencia_redshift',
    'modelMagErr_g': 'Err_g',
    'modelMagErr_r': 'Err_r',
    'modelMag_g': 'mag_g',
    'modelMag_r': 'mag_r',
    'color_gr': 'indice_color'
})
# Calculo del error de color y se agrega como una nueva columna al DataFrame
df_renombrado['error_color'] = np.sqrt(df_renombrado['Err_g']**2 + df_renombrado['Err_r']**2)

# creando tabla de de sqlite...

# se crea una conexión a la base de datos SQLite y se guarda ahi el DataFrame
conexion = sq3.connect('datos_mision.db')
df_renombrado.to_sql('redshiftvcolor', conexion, if_exists='replace', index=False)
conexion.close()