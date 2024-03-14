#CREANDO FUNCION QUE SUMA NUMEROS
def sumar_dos():
    #INICIANDO UN BUCLE
    while True: 
            #PIDIENDO NUMEROS
            a = input("Numero 1: ")
            b = input("Numero 2: ")
            #INTENTANDO CONVERTILOS A ENTEROS Y SUMARLOS
            try:
                resultado = int(a) + int(b)
            #SI LANZO UNA EXCEPCION, PEDIRLE QUE RE INGRESE LOS DATOS
            except ValueError as e:
                print("Se requiere ingresar un digito numerico")
                print(f"ERROR : {e}")
            #SI TODOS SALIO BIEN TERMINAMOS EL BLUCLE
            else:
                break
            #finally se ejecuta siempre
            finally:
                print("Manejo de excepcion finalizado") #para comprobar que siempre se ejecuta
    #MOSTRANDO EL RESULTADO
    return resultado

print(sumar_dos())