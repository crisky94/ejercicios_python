# Define una clase Producto que tenga los atributos nombre, precio y cantidad. Luego, crea dos objetos de esta clase y muestra sus atributos.

class   Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

producto1 = Producto("Camiseta", 20 ,30)
producto2 = Producto('Pantalones', 25, 50)

print(f'Producto1 ={producto1.nombre, producto1.precio, producto1.precio}')
print(f'producto2 ={producto2.nombre, producto2.precio, producto2.precio}')