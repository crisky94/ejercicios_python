# b. Gestión de una biblioteca: Crea una clase base Material con atributos comunes (título, autor) y métodos como informacion. Luego, define subclases Libro, Revista y DVD.

class Material:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor =  autor

    def informacion(self):
        return f'Título: {self.titulo} - Autor: {self.autor}'
    
class Libro(Material):
    def __init__(self, titulo, autor):
        super().__init__(titulo, autor)

    def informacion(self):
        return f'-Libro: {self.titulo} - {self.autor}'

class Revista(Material):
    def __init__(self, titulo, autor):
        super().__init__(titulo, autor)

    def informacion(self):
        return f'-Libro: {self.titulo} - {self.autor}'

class DVD(Material):
    def __init__(self, titulo, autor):
        super().__init__(titulo, autor)

    def informacion(self):
        return f'-Libro: {self.titulo} - {self.autor}'

libro = Libro('El Quijote', 'Cervantes')

revista = Revista('Revista El Jueves', 'RBA Revistas')

dvd = DVD('Edward Scissorhands', 'Tim Burton')

print(libro.informacion())
print(revista.informacion())
print(dvd.informacion())