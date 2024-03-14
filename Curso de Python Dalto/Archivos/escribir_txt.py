with open ("Archivos\\texto_de_curso.txt","w",encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("jjaja te la recontra teclee")
    
    #agregando 2 lineas con write lines
    archivo.writelines(["- Hola maestro que haces?\n","- Misericordia\n"])
    #agregando otras 2 lineas
    archivo.writelines(["- No se porque dijiste eso\n","- Yo tampoco"])