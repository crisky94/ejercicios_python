# j. Actualización de precios con descuento
# Crea un diccionario con productos y sus respectivos precios. Luego, reduce cada precio un 10% y actualiza el diccionario. Finalmente, imprime el diccionario con los precios ya actualizados.

precios = {'libro': 200, 'revista': 50, 'marcador': 10}

for producto in precios:
    precios[producto] -= precios[producto] * 0.1

print(precios)

# Salida esperada: {'libro': 180.0, 'revista': 45.0, 'marcador': 9.0}
