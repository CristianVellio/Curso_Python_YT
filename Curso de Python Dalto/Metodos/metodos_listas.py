#creando una lista con list
lista = list([37, 65, 33, True])

#la funcion len nos devuelve el numero de elementos dentro de una lista
cantidad_de_elemtos = len(lista)

#agregando un elemento a la lista 
lista.append(85)

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"TOMA MAMA")

#agregando varios elementos a la lista
lista.extend([False, 2030])

#ekiminando un elemento de la lista (por su indice) 
lista.pop(0)    # -1 para eleminar el ultimo, -2 para eliminart el anteultipo, y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("TOMA MAMA")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort(reverse=True)

#invirtiendo los elementos de una lista
lista.reverse()

print(lista)

