#forma no optmia de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#resultado = suma([5,3,9,10,20])

#FORMA OPTIMA DE SUMAR VALORES
def suma_total(numeros):
    return sum([*numeros])
    
resultado2 = suma_total([5,3,9,10,20,3])    

#lo mismo de arriba per utilizando el parametro * como argumento (*args)
def suma (nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum[numeros]}"
    
resultado = suma("Chris",5,3,9,10,20,3)