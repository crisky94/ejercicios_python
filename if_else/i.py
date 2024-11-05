# i. Tipo de triángulo según los lados
# Escribe un programa que pida al usuario tres números enteros que representan los lados de un triángulo:

# Equilátero: todos los lados iguales
# Isósceles: dos lados iguales
# Escaleno: todos los lados diferentes
# Si los valores no cumplen con la propiedad de un triángulo válido (la suma de dos lados debe ser mayor al tercer lado), muestra un mensaje indicando que no forman un triángulo.

lado_1 = float(input('Ingresa el primer lado: '))
lado_2 = float(input('Ingresa el segundo lado: '))
lado_3 = float(input('Ingresa el tercer lado: '))
mensaje = ''

if lado_1 == lado_2 and lado_1 == lado_3:
    mensaje = 'equilátero'
elif lado_1 == lado_2 or lado_1 == lado_3:
    mensaje = 'isósceles'
else:
    mensaje = 'escaleno'

print(f'Es un triángulo {mensaje}')
