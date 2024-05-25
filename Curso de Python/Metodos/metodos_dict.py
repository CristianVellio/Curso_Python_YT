diccionario = {
    "nombre" : "cris",
    "apellido" : "huxx",
    "subs" : 1000000
}


#nos devuelve un objeto dict_item 
claves = diccionario.keys()

#obteniendo un elemento con get() (si no wncuentra nada el programa continua)
valor_de_ksadas = diccionario.get("ksadas")
print("hola papa, el programa continua")

#eliminando todo del diccionario
# diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")


#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)