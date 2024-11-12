# g. Factorial
# Crea un programa que calcule el factorial de un número entero positivo ingresado por el usuario usando un bucle for.

numero = int(input("Ingresa un número entero positivo: "))

# Inicializar el acumulador en 1 (ya que el factorial de 0 es 1)
factorial = 1

# Bucle para calcular el factorial
for i in range(1, numero + 1):
    factorial *= i  # Multiplicamos el acumulador por el valor actual de i

# Mostrar el resultado
print(f"El factorial de {numero} es: {factorial}")


# Pistas:

# El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
# Puedes inicializar un acumulador en 1 y multiplicar en cada iteración.
