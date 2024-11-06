# b. Actualización de inventario
# Tienes un diccionario que representa el inventario de una tienda, donde las claves son los nombres de los productos y los valores son la cantidad disponible. Pide al usuario que ingrese el nombre de un producto y una cantidad, luego actualiza el inventario sumando esa cantidad al valor existente.

import pprint
inventario = {'manzanas': 10, 'naranjas': 5, 'bananas': 7}

# producto = input('Ingresa un producto: ')
# cantidad = int(input('Ingresa la cantidad del producto:'))

producto = 'manzanas'
cantidad = 13

if producto in inventario:
    inventario[producto] += cantidad
else:
    print('no existe el producto')

print(inventario)

# Salida esperada: {'manzanas': 13, 'naranjas': 5, 'bananas': 7}
