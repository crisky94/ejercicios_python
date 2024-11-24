# b. Implementa una clase Producto que lleve la cuenta de cuántas instancias se han creado.

class Producto:
    contador: int = 0
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
        Producto.contador += 1

for _ in range(10):
    Producto(f'Producto {_}', 1000)

print(Producto.contador)