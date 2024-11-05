# a. Sumar números
# Escribe un programa que pida al usuario un número entero positivo n y calcule la suma de todos los números desde 1 hasta n utilizando un bucle for.

# Pistas:

# Puedes inicializar una variable suma en 0 y usarla para acumular los resultados dentro del bucle.

n = int(input('Ingresa un número: '))
suma = 0

if n > 0:
    for i in range(1, n + 1):
        suma += i
    print(f'{suma}')
else:
    print('El número no es entero positivo')