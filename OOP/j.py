# j. Carrito de Compras
# Crea las siguientes clases:

# Clase Producto: Representa un producto con nombre, precio y cantidad.

# Clase Carrito: Representa el carrito de compras. Tendrá métodos para:

# Agregar productos al carrito.
# Eliminar productos por nombre.
# Calcular el total del carrito.

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return (f'nombre: {self.nombre}, precio: {self.precio}, cantidad: {self.cantidad}')

class Carrito:
    def __init__(self):
        self.carrito = []

    def __str__(self):
        if not self.carrito:
            return 'El carrito está vacío'
        else:
            productos_str = '\n'.join(str(producto) for producto in self.carrito)
            return f'Productos en el carrito:\n{productos_str}'

    def agregar_producto(self, producto):
        self.carrito.append(producto)
        print(f'Producto agregado: {producto}')


    def eliminar_producto(self, nombre):
        for producto in self.carrito:
            if producto.nombre == nombre:
                self.carrito.remove(producto)
                print(f'Se elimino el producto {nombre}')
                return
        print('El producto no se encuentra en el carrito')

    def obtener_producto(self):
        print(self)
    
    def calcular_total(self):
       total = sum(producto.precio * producto.cantidad  for producto in self.carrito)
       print(f'Total del carrito: ${total:.2f}')
       return total


producto1 = Producto('Laptop HP', 750, 15)
producto2 = Producto('Samsung Galaxy S23', 999, 20)
producto3 = Producto('Audífonos Sony WH-1000XM5', 350, 30)

carrito = Carrito()

carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)

carrito.obtener_producto()

carrito.calcular_total()

carrito.eliminar_producto('Samsung Galaxy S23')

carrito.obtener_producto()
