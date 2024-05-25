
animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [52, 16, 14, 72]


#recorriendo la lista animales
for animal in animales:
    print(f'ahora la variable animale es igual a: {animal}')
    
#recorriendo (iterando) la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero *10
    print(resultado)

#iterando dos listas del mismo tamañp al mismo tiempo  NO FUNCIOINA EN CONJUNTOS/SETS {}
for numnero,animal in zip(animales,numeros):
        print(f"recorriendo lista 1: {numnero}")
        print(f"recorriendo lista 2: {animal}")
        
#forma NO OPTIMA de recorrero una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])
    
#forma CORRECTA de recorrer una lista por su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    

#usando el FOR ELSE
for numero in numeros:
     print(f"ejecutando el ultimo blucle, valor actual: {numero}")
else:
    print("El bucle termino")
    
#todo lo anterior funciona exactamente igual para tuplas () listas [] y conjuntos {}