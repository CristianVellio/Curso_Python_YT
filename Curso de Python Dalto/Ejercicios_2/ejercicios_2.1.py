#falto el profe y los pibes va a armar la clase
#pedir el nombre y la edad de los compañeros que vinieron hoy a clases

#Funcion para obtener el profesor y el asistente segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un bucle for in para pedir informacion de cada compañero
    for i in  range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero:")
        edad = int (input("ingrese la edad del compañero:"))
        compañero = (nombre,edad)
        
        #agregando la informacion a la list
        compañeros.append(compañero)
        
    #ordenandolos de menor a mayor segun la edad    
    compañeros.sort(key=lambda X:X[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor.
    asistente = compañeros [0] [0]
    profesor = compañeros [-1] [0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#mostrando el resultado
print(f"el profesor es: {profesor} y su asistente es: {asistente}")