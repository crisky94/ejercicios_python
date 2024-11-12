# f. Imprimir un triángulo
# Escribe un programa que imprima un triángulo de asteriscos (*). Pide al usuario el número de filas y usa un bucle for.

numero = int(input('Ingresa el numero de filas del triangulo: '))

for i in range(1, numero + 1):
        print('*' * i)

# Pistas:

# En cada iteración, imprime el número correspondiente de asteriscos, que puede ser igual al número de la fila actual.