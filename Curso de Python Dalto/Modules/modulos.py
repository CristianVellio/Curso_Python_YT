#importando un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar 

#desde ese modulo, importamos dos funciones y las renombramos
from modulo_saludar import saludar as saludar_normal, saludar_raro as saludar_como_virgo

#creamos las variables con los saludos
saludo = saludar_normal("Chris")
saludo_raro = saludar_como_virgo("Ghost")

#mostramos los saludos
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos del namspece
#print(dir(m_saludar))

#accedemos al nombre de este modulo
#print(__name__)

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)