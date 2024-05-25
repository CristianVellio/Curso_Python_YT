#creando una lista (se pueden modoficar)
lista = ["Cris", "Cris Huxx", True, 1.78]

#creando una tupla (no se pueden modoficar)
tupla = ("Cris", "Cris Huxx", True, 1.78)

#esto es valido
lista [3] = "Maquinola"

#esto no
#tupla [3] = "Maquinola"

print(lista [3])

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)

conjunto = {"Cris", "Cris Huxx", True, 1.78, "Cris"}

# print( conjunt [3]) -> No puede acceder al elemento

#creando un diccionario (dict) (la estructura es key : value separando con ,)

diccionario = {
    "nombre" : "Cris Huxx",
    "Insta" : "Chris.ghost23",
    "esta_emocionado" : True,
    "altura" : 1.78,
    "dato_duplicado" : "Cris Huxx"
}
print(diccionario["altura"] +2)