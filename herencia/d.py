#### d. **Biblioteca extendida:** Agrega control de acceso a la clase `Material` para que ciertos atributos solo puedan ser leídos mediante un método público, no directamente.
class Material:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor =  autor

    def informacion(self):
        return f'Título: {self.__titulo} - Autor: {self.__autor}'
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def __str__(self):
        return self.informacion()


class Biblioteca(Material):
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):

        self.libros.append(libro)
        print(f'Libro agregado:{libro}')

    def eliminar_libro(self, titulo):

        for libro in self.libros:
            if libro.get_titulo() == titulo:
                self.libros.remove(libro)
                print(f'Libro eliminado: {libro}.')
                return
        print(f'Libro con titulo "{titulo}" no encontrado.')

    def obtener_libros(self):

        if not self.libros:
            print('La biblioteca está vacía.')  
        else: 
            print('Libros en la biblioteca.') 
            for libro in self.libros:
                print(f'- {libro}')

biblioteca = Biblioteca()

libro1 = Material("1984", "George Orwell")
libro2 = Material("Cien años de soledad", "Gabriel García Márquez")
libro3 = Material("Don Quijote de la Mancha", "Miguel de Cervantes")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.obtener_libros()

biblioteca.eliminar_libro("Cien años de soledad")

biblioteca.obtener_libros()