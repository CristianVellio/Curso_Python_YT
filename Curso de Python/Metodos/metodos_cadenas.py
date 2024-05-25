cadena1 = "Hola,soy,Cristian"
cadena2 = "Bienvenido Maquinola"

#convierte en mayusculas
mayusc = cadena1.upper()

#convierte en minusculas
minusc = cadena1.lower()

#primera letra Capital 
primer_letra_mayusc = cadena1.capitalize()


#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("Hola")  #devuelve la posicion

#buscamos una cadena dentro de otra cadena, de no haber una coincidencia lanza una EXCEPCION
busquda_index = cadena1.index("a")

#si es numerico devuelve un valor True, sinp devuelve False
es_numerico = cadena1.isnumeric()

#si es alfabetico (solo letras) devuelve un valor True, si no False
es_alfa =  cadena1.isalpha()

#si es alfanumerico devuelve una valor True , de lo contrario False
es_alfanum = cadena1.isalnum()

#cuenta las coincidencias de una cadema em otra cadena, devuelve la cantidad dw coincidemcias
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1) #-> es una FUNCION NO UN METODO

#Verifica si una cadema empieza com otra cadena dada, de serlo devuelve True
empieza_con = cadena1.startswith("Hol")

#Verifica si una cadema termina com otra cadena dada, de serlo devuelve True
termina_con = cadena1.endswith("ian")

#remplaza un pedazo de una cadena dada, por otra cadena
#si el valor 1, se encuentra em la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("la", "li")

#separar cadenas con la cadena que le pasemos (crea lista/matriz)
cadena_separada = cadena1.split(",")

print(cadena_separada[0])