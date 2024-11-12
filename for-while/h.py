# h. Números Fibonacci
# Escribe un programa que imprima los primeros n números de la secuencia de Fibonacci, donde n es ingresado por el usuario.

numero = int(input('Ingresa un número: '))

a, b = 0, 1
for i in range(numero):
    if i != numero - 1:  
        print(a, end=", ") 
    else:
        print(a) 
    a, b = b, a + b  

# Pistas:

# Recuerda que los primeros dos números de Fibonacci son 0 y 1, y cada número siguiente es la suma de los dos anteriores.
# La secuencia de Fibonacci para los primeros 10 números es: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
