import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("Archivos\\datos.csv")
df2 = pd.read_csv("Archivos\\datos.csv")


#obteniendo loos datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_ordenado_ascendente = df.sort_values("edad")

#ordenandolo de forma descendente
df_ordenado_descendente = df.sort_values("edad",ascending=False)

#concatenando los dos data frames
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras 3 filas con head()
primeras_filas = df.head(3)

#accediendo a las últimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del DataFrame:
df_info = df.describe()

#accediendo a un elemento especifico del df con loc la edad de la fila 2
elemento_especifico_loc = df.loc[2, "edad"]

#accediendo a la edad de la fila 2 con iloc (i hace ref a INDICE)
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 =df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 =df.iloc[2,:]

#accediendo a filas con edad mayor de 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)