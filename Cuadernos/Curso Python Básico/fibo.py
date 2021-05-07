constante= 1.618033988749894
def fib(n):    # escribir la serie de Fibonacci hasta n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b

def fib2(n): # devolver la serie de Fibonacci hasta n
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado
