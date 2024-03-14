#creando diccionarios con dict()
diccionario = dict(nombre="Cris", apellido="Huxx")

#las listas no pueden ser claves porque son ITERABLES o MUTABLES y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Dalto", "Rancio"]):"jajajaa"}

#creando diccionario con fromkeys() vaalor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

#creando diccionario con fromkeys() cambiando el vaalor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")

print(diccionario)