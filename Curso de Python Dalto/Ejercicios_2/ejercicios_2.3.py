#creando una funcion que muestre la serie Fibonacci entre 0 y el numero dado

def Fibonacci(num):
    a,b = 0,1
    Fibonacci_lista= [0]
    for i in range(num):
        if b > num: return Fibonacci_lista
        else: 
            Fibonacci_lista.append(b)
            a,b = b,a+b
    
resultado = Fibonacci(34)
print(resultado)