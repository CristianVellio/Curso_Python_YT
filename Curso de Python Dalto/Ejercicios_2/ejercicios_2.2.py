#creando una funcion que nos devuelva los numeros primos
#entre 0 y el argumetno que pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse
    #por ningun numero entre dos y ese msimo nuemro
    for i in range(2,num-1):
        #si es divisible por algumo retornamos false y termina el bucle
        if num%i==0: return False
    #si termina el bucle, significa que no fue divisible, entonces es primo    
    return True


#creando una funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creando la lista
    primos = []
    for i in range(2,num+1):
        #verificando si el valor es primo
        resultado = es_primo(i)
        #en caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    #devolvemnos la lista        
    return primos

#ceramos el resultado llamando a la funcion y lo mostramos
resultado = primos_hasta(98)
print(resultado)