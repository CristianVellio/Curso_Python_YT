# import re 

# texto = '''Hola maestro, esta es la cadena 1. Como estas mi capitan
# Esta es la linea 2662598 de texto.
# Esta es la linea ababababbb2 de textoababbb.
# Y esta es la final (linea 3), mi capitan'''

#haciendo una busqueda simple
#resultado = re.findall("esta", texto)

#\d --> buscar digitos numericos del 0 - 9
#resultado = re.findall(r"\d",texto)

#\D --> buscar TODOS EXCEPTO digitos numericos del 0 - 9
#resultado = re.findall(r"\D",texto)

#\w --> busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w",texto)

#\W --> buscar TODOS EXCEPTO digitos alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\W",texto)

#\s --> busca espacios en blanco --> espacios, tabs, saltos de linea
#resultado = re.findall(r"\s",texto)

#\S --> busca TODO MENOS espacios en blanco --> espacios, tabs, saltos de linea
#resultado = re.findall(r"\s",texto)

#. nos muestra TODO MENOS saltos en linea
#resultado = re.findall(r".",texto)

#\n nos muestra los saltos en linea
#resultado = re.findall(r"\n",texto)

#\ cancelamos caracteres especiales, cancelando la funcion del punto y buscando puntos.
#resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r"\d\.\s",texto)

#^ busca el comienzo de una linea (buscando Hola al principio de la linea)
#flags?re.M activa la multilinea
#resultado = re.findall(r'^Esta',texto,flags=re.M)

#$ -> busca el final de una linea
#resultado = re.findall(r'capitan$',texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda
#resultado = re.findall(r"\d{3}\s",texto)

#{n,m} -> al menos n como maximo m
#resultado = re.findall(r'[ab]{2}',texto)

# | -> busca una cosa o la otra
# resultado = re.findall(r'\d{2,4}|Hola',texto)

# print(resultado)