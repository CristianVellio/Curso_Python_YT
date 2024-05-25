import re

text = "reemplazzando todas las vocales por el asteriscos"

new_text = re.sub("[aeiou]","*",text)
#ponerlo entre corchetes hace que se tomen los caracteres por separado
#de lo contrario buscaria la "palabra" "aeiou"
#se sub los caracteres [a-e-i-o-u] por *s en text

print(new_text)