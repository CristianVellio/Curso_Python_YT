with open ("Archivos\\texto_de_curso.txt","a",encoding="UTF-8") as archivo:
    #usando un BUCLE para AGREGAR varias lineas
    archivo.write("\n")
    for i in range(5):
        #agregando lineas
        archivo.write(f"Linea {i+1} agregada\n")