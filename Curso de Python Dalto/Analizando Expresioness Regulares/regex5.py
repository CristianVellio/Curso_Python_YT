import re

text = "Este es un ejmeplo de una pagina web: https://www.example.com y tambien podemos visitar http://www.example.org"

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#el ? lo que hace es pedir que se encuentre una coincidencia y sino no importa
#o sea que esta diciendo que la "s" es opcional

result = re.findall(pattern,text)

print(result)