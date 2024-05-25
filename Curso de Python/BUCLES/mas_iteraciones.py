#creando las listas

frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

cadena = "Hola Cris"

numeros = [2,5,8,10]

#evitando que se coma una manzana con la sentencia CONTINUE
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una {fruta}")
    
#evitar que el bucle siga ejecutandose el ELSE (NO SE EJECUTA tampoco debido al BREAK)
for fruta in frutas:
    if fruta == "pera":
        break
    print(f"me voy a comer una {fruta}")
else:
    print("bucle terminado")
    
#recorrer/iterar una cadena de texto
for letra in cadena:
    print(letra)
    
    
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)