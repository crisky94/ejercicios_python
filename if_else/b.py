# b. Descuento por cantidad comprada
# Escribe un programa que pida al usuario el precio de un producto y la cantidad de unidades que quiere comprar. Aplica un descuento basado en la cantidad:

# Si compra entre 1 y 5 unidades, aplica un 5% de descuento.
# Si compra entre 6 y 10 unidades, aplica un 10% de descuento.
# Si compra más de 10 unidades, aplica un 15% de descuento.
# Muestra el precio final con el descuento aplicado.

precio = float(input('Ingresa el precio del producto: '))
cantidad = float(input('Ingresa la cantidad del producto: '))

if 1 <= cantidad <= 5:
    precio = (precio * cantidad) * 0,85
elif 6 <= cantidad <= 10:
    precio = (precio * cantidad) * 0.90
else:
    precio = (precio * cantidad) * 0.85 

print(f'El precio final con descuento es {precio}')