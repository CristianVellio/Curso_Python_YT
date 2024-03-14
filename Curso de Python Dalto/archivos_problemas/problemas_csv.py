#cambiar el tipo de datos de una columna

import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv")

#convertir a string los datos de una columna
df ["edad"] = df ["edad"].astype(str)

#mostrar el tipo de datp del primer elemento de la clumna edad
#print(type(df["edad"][0]))

#Reemplazando los datos "Huxx" por "Godly"
df ["apellido"].replace("Huxx","Godly",inplace=True)

#Eliminando las filas con datos vacios
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")

