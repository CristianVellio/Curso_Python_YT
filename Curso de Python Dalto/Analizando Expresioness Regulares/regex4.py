#import re

#email = "example@example.com"

#pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#aqui el guin separa, y lo que nos dice es que
#pueden ser validos de la z a la z; de la A mayus a la Z mayus, del 0 al 9
#todo lo que no sea un espacio en linea (.); % este operador indica que "todo lo que
# encuentre antes o despues de" lo va a valida; el operado (+) a diferencia del (*)
#lo que hace es requerir que se encuentre UNA o MAS COINCIDENCIA (es INFLEXIBLE, ya que 
# no deja pasar si no hay al menos una coincidencia); luedo de + pare encontrar AL MENOS
#una coincidencia dentro del patron anterior
#a lo ultimo se pide que luego del punto haya AL MENOS 2 caracteres ALFABETICOS rango{2,} 

#result = re.match(pattern,email)
#match es una funcion que nos permite encontrar que COINCIDAN en este caso patron con email

#if result:
    #print("Direccion de correo valida")
#else:
    #print("Direccion de correo invalida")
    

