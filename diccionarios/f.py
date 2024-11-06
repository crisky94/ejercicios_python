# f. Suma de valores
# Crea un diccionario con varios pares clave-valor donde las claves sean nombres de productos y los valores sean sus precios. Calcula e imprime el costo total de todos los productos en el diccionario.

carrito = {'lápiz': 5, 'cuaderno': 20, 'mochila': 100}
total = 0
for item in carrito:
    total += carrito[item]
print(total)


resultado = sum(carrito.values())
print(resultado)
# Salida esperada: El costo total de todos los productos es 125.
