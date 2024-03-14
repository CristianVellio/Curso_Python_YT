#creando una funcion de tres argumentos 
#def frase(nombre,apellido,adjetivo):
#    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#utilizando keywords arguments
#frase_reslutante = frase( adjetivo = "Dios", nombre = "Chris", apellido = "HUxx")
#print(frase_reslutante)

#creando la misma funcion con un parametro opciona y un valor por defecto
def frase(nombre,apellido,adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"
frase_reslutante = frase("Chris","Huxx","inteligente")
print(frase_reslutante)