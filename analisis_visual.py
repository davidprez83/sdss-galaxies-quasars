import numpy as np 
import pandas as pd 
import sqlite3 as sq3
import matplotlib.pyplot as plt

# Se realiza una consulta a la base de datos para graficar
conexion = sq3.connect('datos_mision.db')
print("se ha conectado exitosamente a la base de datos local")
consulta = pd.read_sql_query("SELECT clasificacion, redshift, error_redshift, indice_color, error_color FROM redshiftvcolor", conexion)
conexion.close()

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(14, 8))

# Separamos los datos
qso = consulta[consulta['clasificacion'] == 'QSO'].copy()
galaxy = consulta[consulta['clasificacion'] == 'GALAXY'].copy()

# Aseguramos que los errores sean positivos (tomar valor absoluto)
qso['error_redshift'] = np.abs(qso['error_redshift'])
qso['error_color'] = np.abs(qso['error_color'])
galaxy['error_redshift'] = np.abs(galaxy['error_redshift'])
galaxy['error_color'] = np.abs(galaxy['error_color']

print("Realizando la gráfica de interes...  ")
# Graficamos con barras de error
ax.errorbar(qso['redshift'], qso['indice_color'], 
            xerr=qso['error_redshift'], 
            yerr=qso['error_color'],
            fmt='o', color="#7C305D", label='QUASARES', 
            markersize=5, capsize=5, capthick=1.5, alpha=0.2, elinewidth=1.5)


ax.errorbar(galaxy['redshift'], galaxy['indice_color'], 
            xerr=galaxy['error_redshift'], 
            yerr=galaxy['error_color'],
            fmt='s', color="#99D6ED", label='GALAXIAS', 
            markersize=5, capsize=5, capthick=1.5, alpha=0.2, elinewidth=1.5)


# Configurar etiquetas y título
ax.set_xlabel('Redshift (z)', fontsize=14, fontweight='bold')
ax.set_ylabel('Índice de Color (g - r)', fontsize=14, fontweight='bold')
ax.set_title('Redshift vs Índice de Color con Barras de Error\nClasificación de Galaxias y Quasares', fontsize=16, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(fontsize=12, loc='best', framealpha=0.9)


# Mejorar el aspecto de los ejes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()

plt.show()