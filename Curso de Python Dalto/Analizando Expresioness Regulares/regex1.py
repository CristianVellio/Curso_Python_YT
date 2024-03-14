import re

text = "The quick brown fox jumps over the lazy dog"
x= re.search("^The.*dog$",text)
#el asterisco es un operador que es uan expresion regular que lo que hace es
#intenta encontrar cero coincidencias o alguna, si no hay no termina la cadena
if x:
    print("Si")
else:
    print("No")
    
