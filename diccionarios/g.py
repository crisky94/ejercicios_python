# g. Filtrando productos caros
# Tienes un diccionario de productos con sus respectivos precios. Imprime solo aquellos productos cuyo precio sea mayor a un valor especificado (por ejemplo, mayor a 50).

productos = {'camisa': 30, 'zapatos': 70, 'pantalón': 55, 'gorra': 20}

for producto, precio in productos.items():
    if precio > 50:
        print(producto, precio)
# Salida esperada: {'zapatos': 70, 'pantalón': 55}