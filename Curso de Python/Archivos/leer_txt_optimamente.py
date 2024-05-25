#abriendo el archivo con with open
with open("Archivos\\texto_de_curso.txt",encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
#NO ES NECESARIO CERRARLO AL USAR WITH OPEN