#usando open para abrir el archivo con una codificacion universal (UTF-8)
archivo = open("Archivos\\texto_de_curso.txt",encoding="UTF-8")

#Leer archivo completo
archivo = archivo.read()

#leer linea por linea
#lineas archivo.readlines()

#leer una sola linea
#linea = archivo.readline()

#cerrar el archivo
archivo.close()


print(archivo)

