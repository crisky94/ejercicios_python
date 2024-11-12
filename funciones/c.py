# c. Escribe una función calcular_fibonacci que devuelva una lista con los primeros n valores de la secuencia de Fibonacci.

def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b 
fibo(5)