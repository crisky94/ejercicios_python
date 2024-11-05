# a. Calcular el precio de un producto con descuento
# Pide al usuario el precio de un producto y aplica un descuento según este criterio:

# Si el precio es mayor a 1000, aplica un 15% de descuento.
# Si está entre 500 y 1000, aplica un 10% de descuento.
# Si es menor a 500, aplica un 5% de descuento. Muestra el precio final con el descuento aplicado.

precio = float(input('Ingresa el precio del producto: '))

if precio > 1000:
    precio *= 0.85 # precio * 0,85 15%
elif 500 <= precio <= 1000:
    precio *= 0.9 # 10%
else:
    precio *= 0.95 #5%

print(f'El precio final con descueno es {precio}')