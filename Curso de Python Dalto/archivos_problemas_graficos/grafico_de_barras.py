import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\colla_ingresos.csv")

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#obteniendo el total de ingresos 
total_ingresos = df["ingresos"].sum()

#msotrando el toal
print(f"El totl de imgresos es de: ${total_ingresos} USD")

#mostrando el grafico
plt.show()