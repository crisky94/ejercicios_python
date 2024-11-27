### c. **Tienda online:** Crea una clase base `Usuario` con un método `descuento`. Implementa subclases como `UsuarioPremium` y `UsuarioRegular` donde el usuario premium tenga un 20% de descuento.
class Usuario:
    def __init__(self, usuario):
        self.usuario = usuario
    def descuento(self, precio):
        return precio
        


class UsuarioRegular(Usuario):
    def descuento(self, precio):

        return precio

class UsuarioPremium(Usuario):
    def descuento(self, precio):

        return precio * 0.8

usuario_regular = UsuarioRegular('Pepe')
usuario_premium = UsuarioPremium('Lorena')

precio_original = 100
precio_premium = usuario_premium.descuento(precio_original)
precio_regular = usuario_regular.descuento(precio_original)

print(f' Usuario regular ({usuario_regular.usuario}): Precio final {precio_regular:.2f}')

print(f' Usuario premium ({usuario_premium.usuario}): Precio final {precio_premium:.2f}')