# g. Crea una clase Libro con atributos como título y autor, y una clase Biblioteca que gestione una lista de libros. Agrega métodos para añadir libros, eliminar libros por título y obtener todos los libros.
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"'{self.titulo} de {self.autor}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):

        self.libros.append(libro)
        print(f'Libro agregado:{libro}')

    def eliminar_libro(self, titulo):

        for libro in self.libros:
            if libro.titulo == titulo:
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

libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.obtener_libros()

biblioteca.eliminar_libro("Cien años de soledad")

biblioteca.obtener_libros()