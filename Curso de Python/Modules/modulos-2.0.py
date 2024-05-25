#si el modulo estuviera en una carpeta en la misma ruta se importa asi
#import funciones_buenas.saludar as m_saludar

import sys 

sys.path.append("C:\\Users\\crist\\OneDrive\\Desktop\\Curso de Python Dalto\\funciones_buenas")

import saludar as modulo_saludo
print(modulo_saludo.saludar("Chris"))